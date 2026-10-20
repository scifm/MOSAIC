# Eigensolver settings: one place that turns the physical task and the wanted
# accuracy into backend / nlevels / Krylov parameters. Included into
# MoireSolver.
#
# Inputs, all optional:
#   extra.ed_accuracy      "confirm" (default) | "search"            — hashed
#   extra.gs_degeneracy    expected ground-manifold size (default: the
#                          denominator of ν; Moore–Read needs 6)    — hashed
#   extra.neigen_per_block explicit levels per sector (wins)         — hashed
#   extra.ed_method        explicit backend (legacy override)        — hashed
#   ENV MOIRE_ED_BACKEND   cpu | gpu | auto (default auto)           — not hashed
#
# "confirm" reproduces the pre-0.9 numerics exactly (6 levels per sector,
# KrylovKit defaults krylovdim 30 / tol 1e-12, every vector kept). "search"
# uses the smallest settings the benchmarks showed to give the same physics.

"""Solver parameters for one evaluation."""
struct EDSettings
    accuracy::Symbol        # :confirm | :search
    backend::Symbol         # :sparse (CPU) | :gpu
    nlevels::Int            # eigenvalues per sector at zero twist
    twist_margin::Int       # twisted re-solves ask for state_index + margin levels; -1 ⇒ nlevels
    krylovdim::Int
    tol::Float64            # KrylovKit residual tolerance (absolute, energy units)
    maxiter::Int
    keep::Int               # eigenvectors kept per zero-twist sector (≤ nlevels)
    dense_max::Int          # CPU: sectors up to this size are diagonalised densely
    backend_reason::String
end

# Benchmark-derived constants.
# tol 1e-6: worst eigenvalue error 2.6e-11 over 12–30 sites (error ∝ residual²),
#   20–30 % fewer matvecs than 1e-12; the rigorous bound |δE| ≤ residual is
#   still below the 1e-4 × spectrum-range target.
# krylovdim: matvec count is flat in krylovdim from 16 to 128 at every size;
#   larger subspaces only add orthogonalisation (GPU 1M states: 0.71 s at 16,
#   1.64 s at 128), so the smallest works best.
const SEARCH_TOL = 1e-6
const SEARCH_KRYLOVDIM_GPU = 16
const SEARCH_KRYLOVDIM_GPU_LARGE = 32   # ≥ 2M states: 183 vs 211 matvecs at 5.2M (ν = 1/2, 5×6)
const LARGE_DIM = 2_000_000
const SEARCH_KRYLOVDIM_CPU = 24
const GPU_MIN_DIM = 20_000          # below this the CPU path wins end-to-end (JIT + load)
# Dense below 1500 states in search mode: exact, and immune to single-vector
# Lanczos missing a copy of an exactly degenerate level (Moore–Read: 6 levels
# at Γ in an ~800-state sector at Nk = 16, N = 8); ≤ 0.3 s per sector.
const SEARCH_DENSE_MAX = 1500
const LEGACY_DENSE_MAX = 99         # EDsolve's min_sparse_dim = 100

"Is a GPU allocated to this process? (Slurm sets CUDA_VISIBLE_DEVICES with --gres.)"
gpu_visible() = !isempty(strip(get(ENV, "CUDA_VISIBLE_DEVICES", ""))) &&
                get(ENV, "CUDA_VISIBLE_DEVICES", "") != "NoDevFiles"

function choose_backend(extra::AbstractDict, max_dim::Int)
    if haskey(extra, "ed_method")
        b = Symbol(extra["ed_method"])
        return b, "extra.ed_method = $(b)"
    end
    env = lowercase(get(ENV, "MOIRE_ED_BACKEND", "auto"))
    env in ("cpu", "gpu", "auto") || throw(ArgumentError("MOIRE_ED_BACKEND must be cpu, gpu or auto, got $(env)"))
    env == "cpu" && return :sparse, "MOIRE_ED_BACKEND=cpu"
    env == "gpu" && return :gpu, "MOIRE_ED_BACKEND=gpu"
    gpu_visible() || return :sparse, "auto: no GPU allocated"
    max_dim < GPU_MIN_DIM && return :sparse, "auto: largest sector $(max_dim) < $(GPU_MIN_DIM)"
    return :gpu, "auto: largest sector $(max_dim) ≥ $(GPU_MIN_DIM), GPU allocated"
end

"""
    ed_settings(extra, m_degeneracy, max_dim) -> EDSettings

`m_degeneracy` is the ground-manifold size the gap is measured above. In
search mode each sector solves `m + 1` levels: the gap needs the `m + 1`
lowest levels overall, and one sector can hold all of them, so this is the
smallest per-sector count that is never wrong. Twisted Chern re-solves need
only the tracked state's index in its sector, plus one level of margin.
"""
function ed_settings(extra::AbstractDict, m_degeneracy::Int, max_dim::Int)::EDSettings
    acc = Symbol(lowercase(string(get(extra, "ed_accuracy", "confirm"))))
    acc in (:confirm, :search) || throw(ArgumentError("extra.ed_accuracy must be confirm or search, got $(acc)"))
    backend, why = choose_backend(extra, max_dim)
    if acc == :confirm
        nlev = Int(get(extra, "neigen_per_block", 6))
        # Only ground-manifold vectors are used (Chern); keeping fewer changes no value.
        return EDSettings(acc, backend, nlev, -1, 30, 1e-12, 100, min(m_degeneracy, nlev), LEGACY_DENSE_MAX, why)
    end
    nlev = Int(get(extra, "neigen_per_block", m_degeneracy + 1))
    kd = backend == :gpu ? (max_dim >= LARGE_DIM ? SEARCH_KRYLOVDIM_GPU_LARGE : SEARCH_KRYLOVDIM_GPU) :
                           SEARCH_KRYLOVDIM_CPU
    return EDSettings(acc, backend, nlev, 1, max(kd, nlev + 4), SEARCH_TOL, 200, min(m_degeneracy, nlev),
                      SEARCH_DENSE_MAX, why)
end

"Default settings for callers that predate EDSettings (diagnostic scripts)."
legacy_settings(Neigen::Int, method::Symbol) =
    EDSettings(:confirm, method, Neigen, -1, 30, 1e-12, 100, Neigen, LEGACY_DENSE_MAX, "legacy call")

"Levels to request in a twisted re-solve that tracks state `st`."
twist_levels(ed::EDSettings, st::Int) = ed.twist_margin < 0 ? ed.nlevels : st + ed.twist_margin

"Krylov keyword arguments shared by both backends."
krylov_kw(ed::EDSettings) = (krylovdim = ed.krylovdim, tol = ed.tol, maxiter = ed.maxiter)

"""
One CPU sector solve under `ed`. With confirm settings this is `EDsolve`'s
sparse path value for value (same build, same KrylovKit defaults).
"""
cpu_solve(ed::EDSettings, subspace, scat; N::Int, keep::Int = N) =
    cpu_sector_solve(subspace, scat; N = min(N, length(subspace)), keep = keep, dense_max = ed.dense_max,
                     krylov_kw(ed)...)

"Accumulates per-solve statistics for the output's `ed_solver_stats`."
mutable struct EDStats
    n_solves::Int
    matvecs::Int
    max_residual::Float64
    unconverged::Int
    build_s::Float64
    solve_s::Float64
    peak_matrix_bytes::Int
    matrix_free_solves::Int     # GPU solves that fell back to matrix-free (memory)
end
EDStats() = EDStats(0, 0, 0.0, 0, 0.0, 0.0, 0, 0)

function record!(S::EDStats, st, N::Int)
    S.n_solves += 1
    S.matvecs += st.numops
    S.max_residual = max(S.max_residual, st.maxres)
    S.unconverged += max(0, N - st.converged)
    S.build_s += st.build_s
    S.solve_s += st.solve_s
    S.peak_matrix_bytes = max(S.peak_matrix_bytes, hasproperty(st, :device_bytes) ? st.device_bytes : st.host_bytes)
    st.backend == :gpu_mf && (S.matrix_free_solves += 1)
    return S
end

"""
The output's `ed_solver_stats`: the settings that ran, totals over every
sector solve (zero twist and Chern twists), phase timings, and
`gap_error_bound = 2 · max Ritz residual` — for a Hermitian matrix each
returned eigenvalue is within its residual norm of an exact one.
"""
solver_stats(ed::EDSettings, S::EDStats, phases::AbstractDict, gap) = Dict{Symbol,Any}(
    :accuracy => String(ed.accuracy), :backend => String(ed.backend), :backend_reason => ed.backend_reason,
    :nlevels => ed.nlevels, :twist_margin => ed.twist_margin, :krylovdim => ed.krylovdim,
    :tol => ed.tol, :maxiter => ed.maxiter, :kept_vectors => ed.keep, :dense_max => ed.dense_max,
    :n_solves => S.n_solves, :matvecs => S.matvecs, :max_residual => S.max_residual,
    :unconverged => S.unconverged, :build_seconds => S.build_s, :solve_seconds => S.solve_s,
    :peak_matrix_bytes => S.peak_matrix_bytes, :matrix_free_solves => S.matrix_free_solves, :gap_error_bound => 2 * S.max_residual,
    :gap_resolved => gap === nothing ? nothing : gap > 2 * S.max_residual,
    :phases => Dict{String,Float64}(phases), :threads => Threads.nthreads(),
    :maxrss_bytes => Int(Sys.maxrss()),
)
