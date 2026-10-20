# Particle entanglement spectrum, adapted from the authors' earlier ED code.
@inline function ksum_mask(p::PESGeometry, mask)

    k1 = 0
    k2 = 0

    m = mask
    while m != 0
        i = trailing_zeros(m)
        k1 += p.kk1[i + 1]
        k2 += p.kk2[i + 1]
        m &= m - 1
    end

    k1 %= p.denominator1
    k2 %= p.denominator2

    return p.klookup[k1 + 1, k2 + 1]
end

function _full_mask(::Type{UInt32}, Ns::Int)
    Ns == 32 && return typemax(UInt32)
    return (UInt32(1) << Ns) - UInt32(1)
end

function _full_mask(::Type{UInt64}, Ns::Int)
    Ns == 64 && return typemax(UInt64)
    return (UInt64(1) << Ns) - UInt64(1)
end

function generate_masks(Ns::Int, N::Int)
    0 <= N <= Ns || throw(ArgumentError("Need 0 <= N <= Ns, got N=$N, Ns=$Ns"))

    T = Ns <= 32 ? UInt32 : UInt64
    nm = binomial(Ns, N)
    masks = Vector{T}(undef, nm)

    if N == 0
        masks[1] = zero(T)
        return masks
    elseif N == Ns
        masks[1] = _full_mask(T, Ns)
        return masks
    end

    x = (one(T) << N) - one(T)

    for idx in eachindex(masks)
        masks[idx] = x
        idx == nm && break

        c = x & -x
        r = x + c
        x = (((r ⊻ x) >> 2) ÷ c) | r
    end

    return masks
end

@inline function signmask(state::T, submask::T) where {T<:Unsigned}
    count = 0
    while submask != 0
        i = trailing_zeros(submask)
        count += count_ones(state & ((one(T)<<i)-one(T)))
        submask &= submask - one(T)
    end
    return isodd(count) ? -1 : 1
end

struct PESParams{T}
    NA::Int
    annimasks::Vector{T}
    cremasks::Vector{Vector{T}}
    holes::Bool
end

@inline function bit_positions(mask::T) where {T<:Unsigned}
    pos = Int[]
    m = mask
    while m != 0
        i = trailing_zeros(m)
        push!(pos, i)
        m &= m - 1
    end
    return pos
end

function foreach_submask_of_size(f, mask::T, k::Int) where {T<:Unsigned}
    pos = bit_positions(mask)
    n = length(pos)
    0 <= k <= n || return nothing
    if k == 0
        f(zero(T))
        return nothing
    elseif k == n
        f(mask)
        return nothing
    end
    # Count iterations rather than shifting a signed Int by n (n can be 64).
    x = (UInt64(1) << k) - UInt64(1)
    total = binomial(n, k)
    for index in 1:total
        sub = zero(T)
        y = x
        while y != 0
            p = trailing_zeros(y)
            sub |= one(T) << pos[p + 1]
            y &= y - 1
        end
        f(sub)
        index == total && break
        c = x & -x
        r = x + c
        x = ((xor(r, x) >> 2) ÷ c) | r
    end
    return nothing
end

function submasks_of_size(mask::T, k::Int) where {T<:Unsigned}
    result = T[]
    foreach_submask_of_size(mask, k) do sub
        push!(result, sub)
    end
    return result
end

function build_creation_lookup_fast(p::PESGeometry, NA)
    Ns = p.Ns
    Nk = p.Nk

    T = Ns <= 32 ? UInt32 : UInt64
    annimasks = generate_masks(Ns, NA)
    groups = [T[] for _ in 1:Nk]

    for m in annimasks
        push!(groups[ksum_mask(p, m) + 1], m)
    end

    for g in groups
        sort!(g)
    end

    cremasks = Vector{Vector{T}}(undef, length(annimasks))
    for (i, annimask) in enumerate(annimasks)
        cremasks[i] = groups[ksum_mask(p, annimask) + 1]
    end

    return annimasks, cremasks
end

function PESParams(p::PESGeometry, NA::Int, holes::Bool)
    nparticles = holes ? p.Ns - p.N : p.N
    0 <= NA <= nparticles || throw(ArgumentError(
        "PES requires 0 <= NA <= $(nparticles) for holes=$(holes); got NA=$(NA).",
    ))
    annimasks, cremasks = build_creation_lookup_fast(p, NA)
    return PESParams(NA, annimasks, cremasks, holes)
end

# C[a, b] is the signed parent-state amplitude for the disjoint occupations
# a and b. Keep it sparse: most pairs overlap and therefore have zero weight.
function _pes_schmidt_block(p, amasks, bmasks, masks, vec, holes)
    mask_full = _full_mask(eltype(masks), p.Ns)
    colptr = Int[1]
    rowval = Int[]
    nzval = ComplexF64[]
    for b in bmasks
        for (i, a) in enumerate(amasks)
            iszero(a & b) || continue
            state = a | b
            parent = holes ? (~state) & mask_full : state
            idx = searchsortedfirst(masks, parent)
            idx <= length(masks) && masks[idx] == parent || error(
                "PES partition does not belong to the parent momentum sector.",
            )
            value = vec[idx] * signmask(state, a)
            iszero(value) && continue
            push!(rowval, i)
            push!(nzval, value)
        end
        push!(colptr, length(rowval) + 1)
    end
    return SparseMatrixCSC(length(amasks), length(bmasks), colptr, rowval, nzval)
end

function _pes_accumulate_column!(rho, C, Crows, j, weight)
    # Each worker owns one output column. No thread-local density matrices
    # are needed, and only the lower triangle is read by the eigensolver.
    @inbounds for entry in nzrange(Crows, j)
        b = Crows.rowval[entry]
        coefficient = weight * conj(Crows.nzval[entry])
        for other in nzrange(C, b)
            i = C.rowval[other]
            i < j && continue
            rho[i, j] += C.nzval[other] * coefficient
        end
    end
    return nothing
end

function _pes_accumulate_parent!(rho, p, amasks, bmasks, masks, vec, holes, weight, threaded)
    C = _pes_schmidt_block(p, amasks, bmasks, masks, vec, holes)
    Crows = copy(transpose(C))
    if threaded && Threads.nthreads() > 1
        Threads.@threads for j in axes(rho, 2)
            _pes_accumulate_column!(rho, C, Crows, j, weight)
        end
    else
        for j in axes(rho, 2)
            _pes_accumulate_column!(rho, C, Crows, j, weight)
        end
    end
    return nothing
end

function _pes_density_block(p, eigvecs, sectors, pes, agroups, bgroups, sector_masks, ka, weight, threaded)
    amasks = agroups[ka + 1]
    rho = zeros(ComplexF64, length(amasks), length(amasks))
    isempty(amasks) && return Hermitian(rho, :L)
    for idx in eachindex(eigvecs)
        masks = sector_masks[Int(sectors[idx]) + 1]
        parent = first(masks)
        full = _full_mask(eltype(masks), p.Ns)
        total_sector = pes.holes ? ksum_mask(p, (~parent) & full) : Int(sectors[idx])
        kb1 = mod(p.kk1A[total_sector + 1] - p.kk1A[ka + 1], p.denominator1)
        kb2 = mod(p.kk2A[total_sector + 1] - p.kk2A[ka + 1], p.denominator2)
        kb = p.klookup[kb1 + 1, kb2 + 1]
        _pes_accumulate_parent!(
            rho, p, amasks, bgroups[kb + 1], masks, eigvecs[idx], pes.holes, weight, threaded,
        )
    end
    return Hermitian(rho, :L)
end

function _pes_block_eigenvalues(args...)
    # Overwrite this sector's matrix and compute no unused eigenvectors.
    return eigvals!(_pes_density_block(args...))
end

function _pes_sector_workspace_bytes(p, sectors, pes, agroups, bgroups, sector_masks)
    # Include the dense block, LAPACK workspace, both sparse orientations,
    # vector-growth slack, and garbage from all parents until the batch GC.
    # Bound sparse nnz by both the rectangular shape and all parent partitions.
    na = maximum(length, agroups)
    nb = maximum(length, bgroups)
    nparticles = pes.holes ? p.Ns - p.N : p.N
    partitions = Float64(binomial(nparticles, pes.NA))
    sparse_bytes = sum(sectors) do sector
        nnz_bound = min(Float64(na) * nb, length(sector_masks[Int(sector) + 1]) * partitions)
        6 * (sizeof(ComplexF64) + sizeof(Int)) * nnz_bound + 2 * sizeof(Int) * (na + nb + 2)
    end
    return 2 * sizeof(ComplexF64) * Float64(na)^2 + sparse_bytes + 2.0^20
end

function _pes_sector_worker_count(workspace_bytes, budget_bytes, nsectors, nthreads, blas_threads, threaded)
    threaded || return 1
    # Sector eigensolvers may themselves use BLAS threads. Avoid multiplying
    # two full thread pools; the caller's BLAS setting is never changed.
    cpu_limit = max(1, nthreads ÷ max(1, blas_threads))
    limit = min(nsectors, cpu_limit)
    return max(1, floor(Int, min(limit, budget_bytes / workspace_bytes)))
end

"""
    particle_entanglement_eigenvalues(p, eigvecs, sectors, pes;
        threaded=true, memory_budget_bytes=nothing, verbose=false)

Return the reduced-density-matrix eigenvalues in each momentum sector for an
equal mixture of the supplied parent states. Sector labels are zero-based,
and the returned vector is indexed by `sector + 1`, as in
`particle_entanglement_spectrum`.

Automatically build and diagonalize independent sectors in parallel when
Julia threads and memory permit, retaining only their eigenvalues. The default
sector-parallel workspace budget is half the currently free memory, capped at
one quarter of total RAM. `memory_budget_bytes` overrides that budget; zero
forces one sector at a time. This budget limits concurrency, not the memory
required by a single sector or the existing model and parent states.

The workspace estimate includes dense and sparse matrices, allocation slack,
and eigensolver workspace. Completed batches are reclaimed before starting
the next batch. If only one sector fits, workers instead write disjoint columns
of that sector's matrix, without per-thread matrix copies. `threaded=false`
disables both forms of Julia parallelism. Existing BLAS thread settings are
respected when limiting sector workers and are not modified.

Start Julia with `--threads=auto` to enable automatic sector parallelism.
`verbose=true` prints the selected worker count and memory budget. This is the
preferred entry point when only the PES levels are needed.
"""
function particle_entanglement_eigenvalues(
    p::PESGeometry, eigvecs, sectors, pes::PESParams;
    threaded::Bool = true, memory_budget_bytes::Union{Nothing,Integer} = nothing,
    verbose::Bool = false,
)
    isnothing(memory_budget_bytes) || memory_budget_bytes >= 0 || throw(ArgumentError(
        "PES memory_budget_bytes must be nonnegative or nothing.",
    ))
    length(eigvecs) == length(sectors) || throw(DimensionMismatch(
        "PES needs one momentum sector per parent vector.",
    ))
    isempty(sectors) && throw(ArgumentError("PES needs at least one parent state."))
    all(s -> 0 <= s < p.Nk, sectors) || throw(ArgumentError("PES parent sector is out of range."))
    nparticles = pes.holes ? p.Ns - p.N : p.N
    0 <= pes.NA <= nparticles || throw(ArgumentError("PES particle partition is out of range."))
    sector_masks = build_sector_mask_table(p, p.N, sectors)
    for idx in eachindex(eigvecs)
        masks = sector_masks[Int(sectors[idx]) + 1]
        !isempty(masks) && length(eigvecs[idx]) == length(masks) || throw(DimensionMismatch(
            "PES parent vector $(idx) must match its nonempty momentum-sector basis.",
        ))
    end

    T = eltype(pes.annimasks)
    agroups = [T[] for _ in 1:p.Nk]
    bgroups = [T[] for _ in 1:p.Nk]
    for mask in pes.annimasks
        push!(agroups[ksum_mask(p, mask) + 1], mask)
    end
    for mask in generate_masks(p.Ns, nparticles - pes.NA)
        push!(bgroups[ksum_mask(p, mask) + 1], mask)
    end
    weight = inv(Float64(length(sectors)) * binomial(nparticles, pes.NA))
    workspace_bytes = _pes_sector_workspace_bytes(p, sectors, pes, agroups, bgroups, sector_masks)
    budget_bytes = isnothing(memory_budget_bytes) ?
        min(Sys.free_memory() ÷ 2, Sys.total_memory() ÷ 4) : memory_budget_bytes
    workers = _pes_sector_worker_count(
        workspace_bytes, budget_bytes, p.Nk, Threads.nthreads(), BLAS.get_num_threads(), threaded,
    )
    if verbose
        @printf("PES: %d parallel sector worker(s), %d Julia thread(s), %d BLAS thread(s); estimated workspace %.3f GiB/worker, budget %.3f GiB.\n",
            workers, Threads.nthreads(), BLAS.get_num_threads(), workspace_bytes / 2.0^30, budget_bytes / 2.0^30)
        Threads.nthreads() == 1 && threaded && println("PES: start Julia with --threads=auto to enable Julia parallelism.")
        flush(stdout)
    end
    values = Vector{Vector{Float64}}(undef, p.Nk)
    for first_sector in 0:workers:(p.Nk - 1)
        batch = first_sector:min(first_sector + workers - 1, p.Nk - 1)
        if verbose
            for ka in batch
                println("PES sector $(ka): $(length(agroups[ka + 1])) levels")
            end
            flush(stdout)
        end
        if workers == 1
            values[first_sector + 1] = _pes_block_eigenvalues(
                p, eigvecs, sectors, pes, agroups, bgroups, sector_masks, first_sector, weight, threaded,
            )
        else
            Threads.@threads for ka in batch
                values[ka + 1] = _pes_block_eigenvalues(
                    p, eigvecs, sectors, pes, agroups, bgroups, sector_masks, ka, weight, false,
                )
            end
        end
        # All workers have finished before reclaiming this batch, including
        # sparse workspaces that can be large even when the dense block is small.
        workspace_bytes * length(batch) >= 32 * 2^20 && GC.gc()
    end
    return values
end

function findmbstates3(p::PESGeometry, Ns, N, sector)
    mbstate = generate_masks(Ns, N)

    masks = eltype(mbstate)[]
    labels = Int[]

    for (i, mask) in enumerate(mbstate)
        if ksum_mask(p, mask) == sector
            push!(masks, mask)
            push!(labels, i)
        end
    end

    return masks, labels
end

@inline function accumulate_rdm_mask!(
    mats,
    alist,
    masks,
    i::Int,
    p::PESGeometry,
    pes::PESParams,
    psel1,
    mask_full,
)
    NA = pes.NA
    mask = masks[i]
    ai = alist[i]
    cai = conj(ai)

    if pes.holes
        mask = (~mask) & mask_full
    end

    foreach_submask_of_size(mask, NA) do annimask
        reduced = xor(mask, annimask)
        kna = ksum_mask(p, annimask)
        sgn1 = signmask(mask, annimask)

        annipos = searchsortedfirst(pes.annimasks, annimask)
        cremlist = pes.cremasks[annipos]
        l1 = searchsortedfirst(cremlist, annimask)

        @inbounds for l2 in eachindex(cremlist)
            crem = cremlist[l2]

            if (reduced & crem) != 0
                continue
            end

            newmask = reduced | crem
            sgn2 = signmask(newmask, crem)
            if pes.holes
                newmask = (~newmask) & mask_full
            end
            mbn = searchsortedfirst(masks, newmask)

            mats[kna + 1][l2, l1] += alist[mbn] * cai * sgn1 * sgn2 / psel1
        end
    end

    return nothing
end

function accumulate_rdm!(
    mats,
    alist,
    masks,
    p::PESGeometry,
    pes::PESParams
)
    T = eltype(masks)
    NA = pes.NA
    N = p.N
    psel1 = pes.holes ? binomial(p.Ns - N, NA) : binomial(N, NA)
    mask_full = (one(T) << p.Ns) - one(T)

    for i in eachindex(masks)
        accumulate_rdm_mask!(mats, alist, masks, i, p, pes, psel1, mask_full)
    end

    return nothing
end

function build_sector_mask_table(p::PESGeometry, N::Int, sectors)
    T = p.Ns <= 32 ? UInt32 : UInt64
    sector_masks = [T[] for _ in 1:p.Nk]
    sector_ready = falses(p.Nk)

    for sector in sectors
        sector_idx = Int(sector) + 1
        if !sector_ready[sector_idx]
            sector_masks[sector_idx], _ = findmbstates3(p, p.Ns, N, Int(sector))
            sector_ready[sector_idx] = true
        end
    end

    return sector_masks
end

function particle_entanglement_spectrum(
    p::PESGeometry,
    eigvecs,
    sectors,
    pes::PESParams
)
    Nk = p.Nk
    Ns = p.Ns
    N = p.N
    NA = pes.NA

    mblabelA = Vector{Vector{Int}}(undef, Nk)
    for ss in 0:(Nk - 1)
        _, mblabelA[ss + 1] = findmbstates3(p, Ns, NA, ss)
    end
    mats = [
        zeros(ComplexF64,
              length(mblabelA[i]),
              length(mblabelA[i]))
        for i in 1:Nk
    ]
    sector_masks = build_sector_mask_table(p, N, sectors)

    for idx in eachindex(eigvecs)
        vec = eigvecs[idx]
        sector = Int(sectors[idx])
        masks = sector_masks[sector + 1]
        accumulate_rdm!(mats, vec, masks, p, pes)
    end

    return mats ./ length(sectors)
end

function particle_entanglement_spectrum_threaded(
    p::PESGeometry,
    eigvecs,
    sectors,
    pes::PESParams
)
    Nk = p.Nk
    Ns = p.Ns
    N = p.N
    NA = pes.NA

    mblabelA = Vector{Vector{Int}}(undef, Nk)
    for ss in 0:(Nk - 1)
        _, mblabelA[ss + 1] = findmbstates3(p, Ns, NA, ss)
    end
    mats = [
        zeros(ComplexF64,
              length(mblabelA[i]),
              length(mblabelA[i]))
        for i in 1:Nk
    ]
    sector_masks = build_sector_mask_table(p, N, sectors)

    nT = Threads.maxthreadid()
    mats_thread = [
        [zeros(ComplexF64, size(m, 1), size(m, 2)) for m in mats]
        for _ in 1:nT
    ]

    T = eltype(pes.annimasks)
    psel1 = pes.holes ? binomial(p.Ns - N, NA) : binomial(N, NA)
    mask_full = (one(T) << p.Ns) - one(T)

    for idx in eachindex(eigvecs)
        vec = eigvecs[idx]
        sector = Int(sectors[idx])
        masks = sector_masks[sector + 1]

        if nT == 1 || length(masks) < nT
            accumulate_rdm!(mats_thread[1], vec, masks, p, pes)
            continue
        end

        nchunks = min(nT, length(masks))
        Threads.@threads for chunk in 1:nchunks
            mats_local = mats_thread[chunk]
            for i in chunk:nchunks:length(masks)
                accumulate_rdm_mask!(mats_local, vec, masks, i, p, pes, psel1, mask_full)
            end
        end
    end

    for t in 1:nT, k in 1:Nk
        mats[k] .+= mats_thread[t][k]
    end

    return mats ./ length(sectors)
end
