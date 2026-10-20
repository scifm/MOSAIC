# Sector-level ED engine benchmark.
#
#   julia -t T --project=julia scripts/bench_ed_engine.jl OUT.jsonl IN.json \
#         [filling=1/3] [sectors=1] [backends=cpu,gpu] [nlevels=4,6] \
#         [krylovdim=30] [tol=1e-12] [label=...]
#
# For each requested momentum sector of IN.json (same Hamiltonian the solver
# builds) it runs every backend × nlevels × krylovdim × tol combination and
# appends one JSON row per run: build/solve time, matvecs, restarts, largest
# Ritz residual, matrix/Krylov memory, peak device memory (polled), and the
# eigenvalue error against a strict reference (dense below 4000 states, else
# a tol = 1e-13, krylovdim = 64 Lanczos on the best available backend).
# Backends: cpu (sparse), gpu (device CSR, F64), gpu32 (CSR values in
# ComplexF32), gpumf (matrix-free). Each backend is warmed up first so JIT
# is excluded; JIT is measured separately by the eval-level runs.

using JSON3, Printf, LinearAlgebra
using MomentumED
include(joinpath(@__DIR__, "..", "julia", "src", "MoireSolver.jl"))
using .MoireSolver
const MS = MoireSolver

kv = Dict(split(a, "=")[1] => split(a, "=")[2] for a in ARGS[3:end])
parse_list(T, s) = [parse(T, x) for x in split(s, ",")]
parse_ratio(s) = occursin("/", s) ? (p = split(s, "/"); parse(Int, p[1]) / parse(Int, p[2])) : parse(Float64, s)
outpath, inpath = ARGS[1], ARGS[2]
filling = parse_ratio(get(kv, "filling", "1/3"))
sectors = parse_list(Int, get(kv, "sectors", "1"))
backends = split(get(kv, "backends", "cpu,gpu"), ",")
nlevels_l = parse_list(Int, get(kv, "nlevels", "4,6"))
kdim_l = parse_list(Int, get(kv, "krylovdim", "30"))
tol_l = parse_list(Float64, get(kv, "tol", "1e-12"))
label = get(kv, "label", basename(dirname(inpath)))

raw = JSON3.read(read(inpath, String))
extra = Dict{String,Any}(string(k) => v for (k, v) in pairs(raw[:ed_solver_params][:extra]))
glist, w = MS.decode_W_G(raw[:form_factor]); lat = MS.lattice_from_extra(extra)
dfm = get(raw[:form_factor], :deformation, nothing)
kernel = dfm === nothing ? nothing : MS.DeformationKernel(dfm, glist, w, lat)
kernel === nothing || (glist = kernel.glist; w = kernel.seed_w)
a_n = MS.decode_a_n(raw[:wavefunction])
tff = MS.TrialFormFactor(glist, w, lat, [(abs2(a_n[n + 1]), n) for n in 0:length(a_n) - 1]; kernel = kernel)
k_list, Gk = MS.build_kmesh(extra, Int(raw[:lattice][:n_k])); Nk = size(k_list, 2)
qmax = Int(get(extra, "qmax", 6))
h2 = MS.TrialBandH2(tff, lat, Gk, MS.build_qgrid(qmax), qmax, Float64(extra["W0"]),
                    Float64(get(extra, "d_l", 0.0)), Float64(get(extra, "D_l", 10.0)))
para = EDPara(; k_list = k_list, Gk = Gk, H_two = h2)
Ne = round(Int, Nk * filling)
t_sub = @elapsed subs, ss_k = ED_momentum_subspaces(para, (Ne,); momentum_restriction = true,
    momentum_list = [(k_list[1, i], k_list[2, i]) for i in 1:Nk])
t_scat = @elapsed scat = ED_scatterlist_twobody(para)
@printf("%s: Nk=%d Ne=%d dims %d..%d  subspaces %.1f s  scatter %.1f s (%d terms)  threads %d\n",
        label, Nk, Ne, minimum(length.(subs)), maximum(length.(subs)), t_sub, t_scat, length(scat), Threads.nthreads())

const HAS_GPU = any(startswith(b, "gpu") for b in backends)
G = nothing
if HAS_GPU
    MS.gpu_solve_batch(Tuple{Int,Any}[], subs, identity, Nk; Neigen = 1)   # load the module
    G = MS.GPU_MODULE[]
    MomentumED.CUDA_KRYLOV_SHRINK_RELEASE[] = false; MomentumED.CUDA_MEMORY_MONITOR[] = false
    MomentumED.CUDA_KRYLOV_SHRINK_MINOR_GC[] = get(ENV, "MOIRE_GPU_MINOR_GC", "1") == "1"
    G.KrylovKit.set_num_threads(1)
    tab = G.DevScatterTable(G.PairScatterTable(scat, Nk))
end

function run_one(backend, sub, N, kd, tol; keep = 1)
    if backend == "cpu"
        return MS.cpu_sector_solve(sub, scat; N, krylovdim = kd, tol, keep)
    end
    CUDA = G.CUDA
    GC.gc(); CUDA.reclaim()
    base = CUDA.total_memory() - CUDA.free_memory()
    peak = Threads.Atomic{Int}(0); done = Threads.Atomic{Bool}(false)
    dev = CUDA.device()
    poller = Threads.@spawn begin
        CUDA.device!(dev)
        while !done[]
            Threads.atomic_max!(peak, Int(CUDA.total_memory() - CUDA.free_memory()))
            sleep(0.02)
        end
    end
    vt = backend == "gpu32" ? ComplexF32 : ComplexF64
    res = G.gpu_sector_solve(sub, tab; N, max_bytes = 0.6 * CUDA.free_memory(), krylovdim = kd, tol,
                             value_type = vt, keep, force_matrix_free = backend == "gpumf")
    done[] = true; wait(poller)
    return res[1], res[2], merge(res[3], (device_peak_bytes = peak[] - base,))
end

# warm-up (JIT) on the smallest sector ≥ 100 states
wsub = subs[argmin([length(s) >= 100 ? length(s) : typemax(Int) for s in subs])]
for b in backends
    run_one(b, wsub, 2, 30, 1e-8)
end

open(outpath, "a") do io
    for si in sectors
        sub = subs[si]; dim = length(sub)
        Nref = maximum(nlevels_l) + 2
        t_ref = @elapsed begin
            if dim <= 4000
                Hs = MomentumED.Methods.SparseHmltMatrix(sub, scat)
                Eref = eigvals(Hermitian(Matrix(Hs)))[1:min(Nref, dim)]
                refkind = "dense"
            else
                rb = HAS_GPU ? "gpu" : "cpu"
                v, _, st = run_one(rb, sub, Nref, 64, 1e-13)
                Eref = v; refkind = "$(rb)_tol1e-13_kd64"
            end
        end
        @printf("sector %d K=%s dim %d reference %s (%.1f s)\n", si, string(ss_k[si]), dim, refkind, t_ref)
        for b in backends, N in nlevels_l, kd in kdim_l, tol in tol_l
            kd <= N && continue
            local vals, st
            try
                vals, _, st = run_one(b, sub, N, kd, tol)
            catch e
                @printf("  %-6s N=%d kd=%3d tol=%.0e FAILED %s\n", b, N, kd, tol, sprint(showerror, e)[1:min(end, 120)])
                continue
            end
            err = maximum(abs.(vals[1:N] .- Eref[1:N]))
            krylov_bytes = (kd + 1) * dim * 16
            row = Dict(pairs(st)..., :label => label, :Nk => Nk, :Ne => Ne, :sector => si,
                       :K => collect(ss_k[si]), :nlevels => N, :krylovdim => kd, :tol => tol,
                       :request => b, :eig_err => err, :krylov_bytes => krylov_bytes,
                       :total_s => st.build_s + st.solve_s, :ref => refkind,
                       :E => vals[1:N], :Eref => Eref[1:N], :threads => Threads.nthreads(),
                       :maxrss => Int(Sys.maxrss()))
            println(io, JSON3.write(row)); flush(io)
            @printf("  %-6s N=%d kd=%3d tol=%.0e  build %7.3f  solve %8.3f  ops %5d  iters %3d  res %.1e  err %.1e\n",
                    b, N, kd, tol, st.build_s, st.solve_s, st.numops, st.numiter, st.maxres, err)
        end
    end
end
