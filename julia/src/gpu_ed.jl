# GPU momentum-sector eigensolver.
#
# Included into MoireSolver. Replaces `EDsolve(...; method = :sparse)` for one
# (sector, scatter list) pair with a CUDA path that returns the same thing:
# the lowest `N` eigenvalues and host `MBS64Vector` eigenvectors.
#
# Why not MomentumED's `:cuda_map`:
#   - it only accepts an `MBOperator`, while the solver builds `Vector{Scatter}`;
#   - its kernel visits every scatter term for every basis state
#     (O(dim × n_scat) bit tests per matvec) instead of only the terms whose
#     annihilated pair the state occupies;
#   - it accumulates `amp * x[j]` for `amp = <j|s|i>`, i.e. it applies Hᵀ, not
#     H. Eigenvalues agree, but the eigenvectors come out complex-conjugated,
#     which flips every Berry phase — unusable for the Chern step.
#
# Here the Hamiltonian is materialised once per (sector, twist) as a CSR matrix
# on the device, built by the same pair-grouped enumeration, and Lanczos
# (KrylovKit, identical defaults to the CPU path) runs on device vectors.
#
# Row convention. The scatter list holds the upper-triangle terms; the table
# adds the adjoint of every off-diagonal term, so Σ_s s = H. Thread `i`
# applies every term to basis state i, which yields `a = <j|s|i> = H[j,i]`
# contributions; since H is Hermitian, row i of H is `H[i,j] = conj(H[j,i])`.
# Duplicate (i, j) entries from different terms are kept and summed by SpMV.

module GPUSectorED

using CUDA
using LinearAlgebra
using MomentumED
using MomentumED.KrylovKit: eigsolve, KrylovKit

export gpu_solve_batch

"""
Two-body scatter terms grouped by annihilated pair, host side.

Term `t` of group `p = a·bits + b` (bit positions `a < b`, 0-based) annihilates
bits `a, b`; `out[t]` is its creation mask and `amp[t]` its amplitude. Group
`p` is `offsets[p+1] : offsets[p+2]-1` (1-based indices into `out`/`amp`).
"""
struct PairScatterTable
    bits::Int
    offsets::Vector{Int32}
    out::Vector{UInt64}
    amp::Vector{ComplexF64}
end

function PairScatterTable(scat_upper::AbstractVector{<:Scatter}, bits::Int)
    bits <= 64 || throw(ArgumentError("GPU ED supports at most 64 orbitals, got $(bits)"))
    ins = UInt64[]; outs = UInt64[]; amps = ComplexF64[]
    for s in scat_upper
        count_ones(s.in.n) == 2 && count_ones(s.out.n) == 2 || throw(ArgumentError(
            "GPU ED handles two-body terms only; got a $(count_ones(s.in.n))→$(count_ones(s.out.n)) term"))
        push!(ins, s.in.n); push!(outs, s.out.n); push!(amps, s.Amp)
        if s.in.n != s.out.n
            push!(ins, s.out.n); push!(outs, s.in.n); push!(amps, conj(s.Amp))
        end
    end
    key(m) = trailing_zeros(m) * bits + (63 - leading_zeros(m))
    keys = [key(m) for m in ins]
    perm = sortperm(keys)
    npair = bits * bits
    offsets = zeros(Int32, npair + 1)
    for k in keys
        offsets[k + 2] += 1
    end
    offsets[1] = 1
    for p in 2:npair + 1
        offsets[p] += offsets[p - 1]
    end
    return PairScatterTable(bits, offsets, outs[perm], amps[perm])
end

"Device copy of a `PairScatterTable` (on the task's current device)."
struct DevScatterTable
    bits::Int
    offsets::CuVector{Int32}
    out::CuVector{UInt64}
    amp::CuVector{ComplexF64}
end
DevScatterTable(t::PairScatterTable) = DevScatterTable(t.bits, CuArray(t.offsets), CuArray(t.out), CuArray(t.amp))

# Number of occupied orbitals strictly between the paired bits of `mask`, the
# fermionic sign counter of EDCore.scat_occ_number (bit-for-bit the same loop).
@inline function _dev_occ_between(n::UInt64, mask::UInt64)
    m = zero(UInt64)
    im = mask
    while im > UInt64(0)
        tz1 = trailing_zeros(im)
        im &= im - UInt64(1)
        tz2 = trailing_zeros(im)
        im &= im - UInt64(1)
        m += UInt64(1) << tz2
        m -= UInt64(1) << (tz1 + 1)
    end
    return count_ones(n & m)
end

@inline function _dev_bsearch(basis, target::UInt64, n::Int32)
    lo = Int32(1); hi = n
    while lo <= hi
        mid = (lo + hi) >>> 1
        v = @inbounds basis[mid]
        if v < target
            lo = mid + Int32(1)
        elseif v > target
            hi = mid - Int32(1)
        else
            return mid
        end
    end
    return Int32(0)
end

# Visit every (j, a = H[j,i]) produced by the terms acting on basis state i.
# mode 0: count the off-diagonal entries of row i and write the summed diagonal
#         to diag[i] (every occupied pair contributes one diagonal term — 45 per
#         row at ν = 1/3 on 30 sites, 190 at 2/3 — so storing them as CSR
#         entries cost 13 % / 38 % of the matrix);
# mode 1: fill the off-diagonal CSR row;
# mode 2: matrix-free y[i] = Σ conj(a) x[j], diagonal included.
function _row_kernel!(mode::Int32, counts, diag, rowptr, colind, vals, y, x,
                      basis, offsets, outm, amp, bits::Int32, err)
    i = (blockIdx().x - Int32(1)) * blockDim().x + threadIdx().x
    n = Int32(length(basis))
    i > n && return nothing
    st = @inbounds basis[i]
    cnt = Int32(0)
    pos = mode == Int32(1) ? Int64(@inbounds rowptr[i]) : Int64(0)
    acc = zero(ComplexF64)
    dacc = zero(ComplexF64)
    ra = st
    while ra != UInt64(0)
        a = trailing_zeros(ra)
        ra &= ra - UInt64(1)
        rb = ra
        while rb != UInt64(0)
            b = trailing_zeros(rb)
            rb &= rb - UInt64(1)
            p = Int32(a) * bits + Int32(b)
            inm = (UInt64(1) << a) | (UInt64(1) << b)
            mid = st & ~inm
            for t in (@inbounds offsets[p + 1]):(@inbounds offsets[p + 2]) - Int32(1)
                om = @inbounds outm[t]
                if om == inm
                    dacc += conj(@inbounds amp[t])
                    continue
                end
                (mid & om) != UInt64(0) && continue
                j = _dev_bsearch(basis, mid | om, n)
                if j == Int32(0)
                    @inbounds err[1] = Int32(1)
                    continue
                end
                s = _dev_occ_between(mid, inm) + _dev_occ_between(mid, om)
                av = iseven(s) ? (@inbounds amp[t]) : -(@inbounds amp[t])
                if mode == Int32(0)
                    cnt += Int32(1)
                elseif mode == Int32(1)
                    @inbounds colind[pos] = j
                    @inbounds vals[pos] = conj(av)
                    pos += Int64(1)
                else
                    acc += conj(av) * (@inbounds x[j])
                end
            end
        end
    end
    if mode == Int32(0)
        @inbounds counts[i] = cnt
        @inbounds diag[i] = dacc
    elseif mode == Int32(2)
        @inbounds y[i] = acc + dacc * (@inbounds x[i])
    end
    return nothing
end

# One warp per row: lanes stride the row's off-diagonal entries (stored as
# ComplexF64 or ComplexF32; accumulation is always Float64), shuffle-reduce,
# then add the diagonal.
function _spmv_warp_kernel!(y, rowptr, colind, vals, diag, x)
    tid = (blockIdx().x - Int32(1)) * blockDim().x + threadIdx().x - Int32(1)
    row = tid ÷ Int32(32) + Int32(1)
    lane = tid % Int32(32)
    row > Int32(length(y)) && return nothing
    acc = zero(ComplexF64)
    k = (@inbounds rowptr[row]) + lane
    stop = @inbounds rowptr[row + 1]
    while k < stop
        acc += ComplexF64(@inbounds vals[k]) * (@inbounds x[colind[k]])
        k += Int64(32)
    end
    re = real(acc); im = imag(acc)
    off = Int32(16)
    while off > Int32(0)
        re += CUDA.shfl_down_sync(0xffffffff, re, off)
        im += CUDA.shfl_down_sync(0xffffffff, im, off)
        off >>= Int32(1)
    end
    lane == Int32(0) && (@inbounds y[row] = complex(re, im) + (@inbounds diag[row]) * (@inbounds x[row]))
    return nothing
end

"Sector Hamiltonian on the device: diagonal + off-diagonal CSR, or matrix-free."
struct DevSectorH
    n::Int
    basis::CuVector{UInt64}
    table::DevScatterTable
    diag::CuVector{ComplexF64}
    rowptr::Union{Nothing, CuVector{Int64}}   # Int64: sectors pass 2^31 nonzeros at ν = 1/2
    colind::Union{Nothing, CuVector{Int32}}
    vals::Union{Nothing, CuVector}
    dummyI::CuVector{Int32}
    dummyC::CuVector{ComplexF64}
    err::CuVector{Int32}
end

matrix_free(H::DevSectorH) = H.rowptr === nothing
"Device bytes held by `H` (basis, diagonal, CSR)."
device_bytes(H::DevSectorH) = sizeof(H.basis) + sizeof(H.diag) +
    (matrix_free(H) ? 0 : sizeof(H.rowptr) + sizeof(H.colind) + sizeof(H.vals))

const _THREADS = 256

function _launch_rows!(mode, basis, tab, counts, diag, rowptr, colind, vals, y, x, err)
    n = length(basis)
    @cuda threads = _THREADS blocks = cld(n, _THREADS) _row_kernel!(
        Int32(mode), counts, diag, rowptr, colind, vals, y, x,
        basis, tab.offsets, tab.out, tab.amp, Int32(tab.bits), err)
end

"Bytes of the off-diagonal CSR for `nnz` entries of type `T` over `n` rows."
csr_bytes(nnz::Integer, n::Integer, ::Type{T}) where {T} = nnz * (sizeof(T) + sizeof(Int32)) + (n + 1) * sizeof(Int64)

"""
    DevSectorH(basis_host, tab; max_bytes, value_type = ComplexF64, force_matrix_free = false)

Build the sector Hamiltonian on the current device. The off-diagonal part is
materialised as CSR when it fits in `max_bytes` (and `force_matrix_free` is
off), else the operator stays matrix-free. Throws if any produced state is
missing from the basis (a non-momentum-conserving term).
"""
function DevSectorH(basis_host::Vector{UInt64}, tab::DevScatterTable; max_bytes::Real,
                    value_type::Type = ComplexF64, force_matrix_free::Bool = false,
                    retry_fraction::Real = 0.0)
    n = length(basis_host)
    n < typemax(Int32) || throw(ArgumentError("sector too large for Int32 indexing: $(n)"))
    basis = CuArray(basis_host)
    err = CUDA.zeros(Int32, 1)
    dummyI = CUDA.zeros(Int32, 1); dummyC = CUDA.zeros(ComplexF64, 1)
    counts = CUDA.zeros(Int32, n)
    diag = CUDA.zeros(ComplexF64, n)
    _launch_rows!(0, basis, tab, counts, diag, dummyI, dummyI, dummyC, dummyC, dummyC, err)
    Array(err)[1] == 0 || error("GPU ED: a scatter term leaves the momentum sector")
    nnz_total = sum(Int64, counts)
    need = csr_bytes(nnz_total, n, value_type)
    if !force_matrix_free && need > max_bytes && retry_fraction > 0
        # Dead device arrays promoted past the minor GC still count as used;
        # one full GC before giving up on CSR (only when it would not fit).
        GC.gc(true)
        max_bytes = retry_fraction * available_device_memory()
    end
    if force_matrix_free || need > max_bytes
        CUDA.unsafe_free!(counts)
        return DevSectorH(n, basis, tab, diag, nothing, nothing, nothing, dummyI, dummyC, err)
    end
    rowptr = CuArray(vcat(Int64[1], Int64(1) .+ cumsum(Int64.(Array(counts)))))
    CUDA.unsafe_free!(counts)
    colind = CuVector{Int32}(undef, nnz_total)
    vals64 = CuVector{ComplexF64}(undef, nnz_total)
    _launch_rows!(1, basis, tab, dummyI, dummyC, rowptr, colind, vals64, dummyC, dummyC, err)
    vals = value_type === ComplexF64 ? vals64 : (v = value_type.(vals64); CUDA.unsafe_free!(vals64); v)
    return DevSectorH(n, basis, tab, diag, rowptr, colind, vals, dummyI, dummyC, err)
end

function apply!(y::CuVector{ComplexF64}, H::DevSectorH, x::CuVector{ComplexF64})
    if matrix_free(H)
        _launch_rows!(2, H.basis, H.table, H.dummyI, H.dummyC, H.dummyI, H.dummyI, H.dummyC, y, x, H.err)
    else
        @cuda threads = _THREADS blocks = cld(H.n * 32, _THREADS) _spmv_warp_kernel!(
            y, H.rowptr, H.colind, H.vals, H.diag, x)
    end
    return y
end
apply(H::DevSectorH, x::CuVector{ComplexF64}) = apply!(similar(x), H, x)

function release!(H::DevSectorH)
    CUDA.unsafe_free!(H.basis); CUDA.unsafe_free!(H.diag)
    matrix_free(H) || (CUDA.unsafe_free!(H.rowptr); CUDA.unsafe_free!(H.colind); CUDA.unsafe_free!(H.vals))
    return nothing
end

"""
    gpu_sector_solve(subspace, tab; N, max_bytes, krylovdim = 30, tol = 1e-12,
                     maxiter = 100, value_type = ComplexF64, keep = N,
                     force_matrix_free = false) -> (vals, vecs, stats)

Lowest `N` eigenvalues of one sector on the current device and the first
`keep` eigenvectors as host `MBS64Vector`s (`EDsolve`'s return shape plus a
stats NamedTuple). The Krylov defaults are KrylovKit's, i.e. the CPU path's.
Sectors below EDsolve's `min_sparse_dim` (100), where it switches to dense,
are diagonalised densely on the host from the device-built matrix.
`stats.maxres` is the largest Ritz residual ‖Hv − λv‖ of the `N` pairs.
"""
function gpu_sector_solve(subspace, tab::DevScatterTable; N::Int, max_bytes::Real,
                          krylovdim::Int = 30, tol::Real = 1e-12, maxiter::Int = 100,
                          value_type::Type = ComplexF64, keep::Int = N,
                          force_matrix_free::Bool = false, retry_fraction::Real = 0.0)
    dim = length(subspace)
    basis_host = UInt64[m.n for m in subspace.list]
    t0 = time()
    H = DevSectorH(basis_host, tab; max_bytes, value_type, force_matrix_free, retry_fraction)
    CUDA.synchronize()
    t_build = time() - t0
    nnz = matrix_free(H) ? -1 : length(H.vals)
    kind = matrix_free(H) ? :gpu_mf : :gpu_csr
    try
        if dim < 100
            matrix_free(H) && error("GPU ED: dense fallback needs the CSR form")
            rp = Array(H.rowptr); ci = Array(H.colind); vv = Array(H.vals); dg = Array(H.diag)
            M = zeros(ComplexF64, dim, dim)
            for r in 1:dim
                M[r, r] += dg[r]
                for k in rp[r]:rp[r + 1] - 1
                    M[r, ci[k]] += vv[k]
                end
            end
            F = eigen(Hermitian(M))
            N = min(N, dim)
            stats = (dim = dim, nnz = nnz, backend = :dense, build_s = t_build, solve_s = 0.0,
                     numops = 0, numiter = 0, maxres = 0.0, converged = N, device_bytes = device_bytes(H))
            return F.values[1:N], [MBS64Vector(F.vectors[:, i], subspace) for i in 1:min(keep, N)], stats
        end
        # Memory rule: the Krylov basis (krylovdim + 1 vectors) must fit next to
        # the matrix; shrink the subspace (never below N + 2) rather than fail.
        fit = floor(Int, 0.4 * available_device_memory() / (16 * dim)) - 1
        krylovdim = max(min(krylovdim, fit), N + 2)
        t1 = time()
        x0 = CuArray(rand(ComplexF64, dim))
        vals, vecs, info = eigsolve(x -> apply(H, x), x0, N, :SR;
                                    ishermitian = true, krylovdim = krylovdim, tol = tol, maxiter = maxiter)
        length(vals) < N && error("Krylov method fails. Cannot find $N eigenvectors.")
        t_solve = time() - t1
        stats = (dim = dim, nnz = nnz, backend = kind, build_s = t_build, solve_s = t_solve,
                 numops = info.numops, numiter = info.numiter, maxres = maximum(info.normres[1:N]),
                 converged = info.converged, device_bytes = device_bytes(H))
        return real.(vals[1:N]), [MBS64Vector(Array(vecs[i]), subspace) for i in 1:min(keep, N)], stats
    finally
        release!(H)
    end
end

"""
Device memory a new allocation can use: driver-free bytes plus what CUDA.jl's
pool holds but no live array uses. `CUDA.free_memory()` alone excludes the
pool cache, so after a 41 GB sector the next sector's CSR "did not fit" and
fell back to matrix-free (5×6 ν = ½: 24 s instead of 4.7 s per sector).
A minor GC first returns dead Krylov vectors to the pool.
"""
function available_device_memory()
    GC.gc(false)
    return CUDA.free_memory() + max(0, CUDA.cached_memory() - CUDA.used_memory())
end

"""
    GPUSolveBatch

Runs a list of independent sector solves `(block_idx, twist_key)` across all
visible GPUs, one worker task per device pulling from a shared queue.
`scat_for(key)` returns the upper-triangle scatter list for a twist key; each
worker uploads a key's table once. Results come back keyed by the job tuple.
Host threads ≥ number of devices keep the workers truly concurrent.
"""
function gpu_solve_batch(
    jobs::Vector, subspaces::AbstractVector, scat_for::Function, bits::Int;
    Neigen::Int, mem_fraction::Float64 = 0.6, keep::Int = Neigen,
    N_for::Union{Nothing,Function} = nothing, solver_kw...,
)
    CUDA.functional() || error("GPU ED requested but CUDA is not functional on this node")
    devs = collect(CUDA.devices())
    isempty(devs) && error("GPU ED requested but no CUDA device is visible")
    # The vendored CUDA extension's Lanczos-restart hook runs a full GC (stops
    # every worker) and prints the pool status; neither is wanted here. A minor
    # GC per restart instead keeps dead Krylov vectors from piling up on the
    # device (MOIRE_GPU_MINOR_GC=0 turns it off).
    MomentumED.CUDA_KRYLOV_SHRINK_RELEASE[] = false
    MomentumED.CUDA_KRYLOV_SHRINK_MINOR_GC[] = get(ENV, "MOIRE_GPU_MINOR_GC", "1") == "1"
    MomentumED.CUDA_MEMORY_MONITOR[] = false
    # KrylovKit's own host threading would spawn tasks that touch device
    # arrays outside the worker's device context.
    nthreads_krylov = KrylovKit.get_num_threads()
    KrylovKit.set_num_threads(1)
    # Host scatter tables are built serially: scat_for may touch caches that
    # are not thread-safe (form-factor memo, deformation kernel).
    host_tabs = Dict{Any,PairScatterTable}()
    for (_, key) in jobs
        haskey(host_tabs, key) || (host_tabs[key] = PairScatterTable(scat_for(key), bits))
    end
    # Largest sectors first so the tail of the queue is short.
    order = sort(collect(eachindex(jobs)); by = j -> -length(subspaces[jobs[j][1]]))
    queue = Channel{Int}(length(order))
    foreach(j -> put!(queue, j), order)
    close(queue)
    results = Dict{Any,Any}()
    lk = ReentrantLock()
    function worker(dev)
            CUDA.device!(dev)
            dev_tabs = Dict{Any,DevScatterTable}()
            for j in queue
                b, key = jobs[j]
                tab = get!(() -> DevScatterTable(host_tabs[key]), dev_tabs, key)
                max_bytes = mem_fraction * available_device_memory()
                N = min(N_for === nothing ? Neigen : N_for(jobs[j]), length(subspaces[b]))
                res = gpu_sector_solve(subspaces[b], tab; N = N, max_bytes = max_bytes,
                                       keep = min(keep, N), retry_fraction = mem_fraction, solver_kw...)
                lock(lk) do
                    results[jobs[j]] = res
                end
            end
            for t in values(dev_tabs)
                CUDA.unsafe_free!(t.offsets); CUDA.unsafe_free!(t.out); CUDA.unsafe_free!(t.amp)
            end
    end
    # One device: run in this task. A Lanczos step is a handful of small
    # kernels plus host syncs, and syncing from a spawned task cost 2–3× per
    # solve (27 sites: 0.16 s inline vs 0.33–0.62 s spawned).
    if length(devs) == 1
        worker(only(devs))
    else
        @sync for dev in devs
            Threads.@spawn worker(dev)
        end
    end
    KrylovKit.set_num_threads(nthreads_krylov)
    return results
end

end # module
