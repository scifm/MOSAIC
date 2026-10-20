"""
Moire many-body FCI solver — `w_G` expansion model.

Inputs are the JSON-decoded `EDInput` (v1 schema, see
`src/mosaic/ed/contract.py`). Outputs are a `Dict` ready for JSON
serialization that conforms to `EDOutput` with the many-body convention:

  - `epsilon_target`, `epsilon_above`, `epsilon_below`, `u_k` are nothing;
  - `chern_solver` is the many-body Chern (Wilson loop, integer);
  - `gap_top_indirect_solver` is `Δ_top = E_excited_first -
     max(E_GS_manifold)`.

The trial single-particle Bloch orbital at momentum `k` is built as follows
(lattice and Coulomb conventions follow the Landau-level torus example of
MomentumED.jl by Zou Bo):

  - `|h(r)|² = Σ_G w_G e^{iG·r}` is the periodic density modulation
    (the `W_G` entries of the JSON input are these `w_G` Fourier
    coefficients, *not* the envelope FT).
  - For each pair `(k, k')`, build the raw LL matrix
    `λ^raw_{mn} = Σ_g w_g η_{G-g} cis(phases) Φ_{mn}(q)`
    for LL indices `m, n = 0..nmax`.
  - Cholesky-orthonormalise the LL tower via the raw `(k, k)` overlap
    matrix → `Forth_{mn} = U(k)† λ^raw_{mn} U(k')`.
  - The trial-band form factor is the LL-mix weighted sum of diagonals
    `λ^MC_G = Σ_n t_n Forth_{nn}` with weights `t_n = |a_n|²`
    (see `TrialFormFactor`).
  - Two-body matrix elements use the gate-screened Coulomb
    `V_Coulomb(|q|; d_l, D_l)` of the MomentumED.jl Landau-level torus example.
  - `MomentumED.EDsolve` per momentum block; many-body gap from the
    sorted spectrum; many-body Chern from a Wilson loop along a small
    reciprocal-plaquette path.
"""
module MoireSolver

using LinearAlgebra
using MomentumED
using EDCore: occ_list, get_bits, MBS64, HilbertSubspace
using MomentumED.SparseArrays: SparseMatrixCSC
using MomentumED.KrylovKit: eigsolve

export SOLVER_VERSION
export solve
export transient_failure_output
export logical_failure_output
export classify_exception
export build_kmesh
export build_symmetric_kmesh
export supported_symmetric_clusters
export normalize_ed_sector_mode
export ed_sector_plan
export solve_ed_spectrum

include("particle_entanglement.jl")
using .ParticleEntanglement
export ParticleEntanglement, PESGeometry, PESParams, pes_spectrum, pes_density_matrices
export particle_entanglement_eigenvalues, particle_entanglement_spectrum
export particle_entanglement_spectrum_threaded, pes_counting_gap, pes_threshold
export pes_admissible_counts

const SOLVER_VERSION = "moire-julia-ed@v0.9.1"  # v0.9.1: opt-in PES; eigensolver settings layer (search/confirm)
const SCHEMA_VERSION = "1"

# Convention: l = 1 throughout (as in MomentumED.jl's Landau-level torus example).
const LB = 1.0
const LB2 = 1.0

# ---------------------------------------------------------------------------
# Lattice (triangular by default; matches the :triangular lattice of
# MomentumED.jl's Landau-level torus example)
# ---------------------------------------------------------------------------

"""
    ReciprocalLattice

Holds the two primitive reciprocal vectors `G1`, `G2` as ComplexF64
(real = x, imag = y), plus exact ratios used by the form factor helpers.
Constructor parameters and defaults match `ReciprocalLattice` in
the Landau-level torus example of MomentumED.jl (Zou Bo).
"""
struct ReciprocalLattice
    G1::ComplexF64
    G2::ComplexF64
    G2_ratio_G1::Float64
    cos_angle::Float64

    function ReciprocalLattice(G2_ratio_G1::Real, cos_angle::Real; G1phase_in_pi::Real = 0.0)
        sin_square = 1.0 - cos_angle^2
        @assert sin_square > 0.0 "|cosθ| must be < 1"
        sin_angle = sqrt(sin_square)
        # Choose |G1| so the triangle area gives one flux quantum per cell:
        # |G1|·|G2|·sin(θ) = 2π/l².
        G1 = sqrt(2π / LB2 / abs(G2_ratio_G1) / sin_angle) * cispi(G1phase_in_pi)
        G2 = G1 * G2_ratio_G1 * complex(cos_angle, sin_angle)
        new(G1, G2, Float64(G2_ratio_G1), Float64(cos_angle))
    end
end

triangular_lattice() = ReciprocalLattice(1.0, -0.5)
square_lattice()     = ReciprocalLattice(1.0, 0.0)

function lattice_from_extra(extra::AbstractDict)
    name = lattice_symbol_from_extra(extra)
    if name === :triangular
        return triangular_lattice()
    elseif name === :square
        return square_lattice()
    else
        error("unknown lattice type $(name); known: triangular, square")
    end
end

lattice_symbol_from_extra(extra::AbstractDict) =
    Symbol(get(extra, "lattice", "triangular"))

include("geometry.jl")
include("symmetry_reduced_ed.jl")
include("ed_settings.jl")
include("pes_diagnostics.jl")

# GPU backend, loaded on first use: CUDA adds ~4 s of load time and
# a no-GPU warning to every CPU evaluation otherwise.
const GPU_MODULE = Ref{Any}(nothing)
function gpu_solve_batch(args...; kw...)
    if GPU_MODULE[] === nothing
        GPU_MODULE[] = Base.include(@__MODULE__, joinpath(@__DIR__, "gpu_ed.jl"))
    end
    return Base.invokelatest(GPU_MODULE[].gpu_solve_batch, args...; kw...)
end

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

@inline cross2(ax::Float64, ay::Float64, bx::Float64, by::Float64) = ax * by - ay * bx

@inline function eta(g1::Int, g2::Int)
    # η_(g1,g2) = +1 if both even, else -1. Equivalently (-1)^(g1+g2+g1*g2).
    (iszero(g1 & 1) && iszero(g2 & 1)) ? 1.0 : -1.0
end

@inline function vecG(g::Tuple{Int,Int}, lattice::ReciprocalLattice)
    return reim(g[1] * lattice.G1 + g[2] * lattice.G2)
end

# --- LL form factor Φ_{mn}(q) ---

function laguerre_L(n::Int, x::Float64)
    n == 0 && return 1.0
    n == 1 && return 1.0 - x
    n == 2 && return 1.0 - 2.0x + 0.5x * x
    n == 3 && return 1.0 - 3.0x + 1.5x * x - x * x * x / 6.0
    Lnm2 = 1.0
    Lnm1 = 1.0 - x
    Ln = 0.0
    @inbounds for k in 2:n
        Ln = ((2k - 1 - x) * Lnm1 - (k - 1) * Lnm2) / k
        Lnm2, Lnm1 = Lnm1, Ln
    end
    return Ln
end

function assoc_laguerre_L(n::Int, a::Int, x::Float64)
    n < 0 && throw(ArgumentError("n must be >= 0"))
    a < 0 && throw(ArgumentError("a must be >= 0"))
    s = 0.0
    xpow = 1.0
    fac = 1.0
    @inbounds for j in 0:n
        coeff = (isodd(j) ? -1.0 : 1.0) * binomial(n + a, n - j) / fac
        s += coeff * xpow
        xpow *= x
        fac *= (j + 1)
    end
    return s
end

@inline function sqrt_fac_ratio(minn::Int, maxn::Int)
    minn > maxn && throw(ArgumentError("need minn <= maxn"))
    s = 1.0
    @inbounds for t in (minn + 1):maxn
        s /= sqrt(t)
    end
    return s
end

"""LL matrix element factor `Φ_{mn}(q)`."""
function ll_factor_mn(qx::Float64, qy::Float64, m::Int, n::Int)
    x, α, gauss = ll_factor_args(qx, qy)
    return ll_factor_mn(x, α, gauss, m, n)
end

"The `q`-dependent pieces of `Φ_{mn}(q)` shared by every `(m, n)`."
@inline function ll_factor_args(qx::Float64, qy::Float64)
    x = 0.5 * LB2 * (qx * qx + qy * qy)
    α = 1im * sqrt(0.5 * LB2) * complex(qx, qy)
    gauss = exp(-0.5 * x)
    return x, α, gauss
end

@inline function ll_factor_mn(x::Float64, α::ComplexF64, gauss::Float64, m::Int, n::Int)
    if m == n
        return gauss * laguerre_L(n, x)
    elseif m > n
        d = m - n
        return gauss * sqrt_fac_ratio(n, m) * (-conj(α))^d * assoc_laguerre_L(n, d, x)
    else
        d = n - m
        return gauss * sqrt_fac_ratio(m, n) * α^d * assoc_laguerre_L(m, d, x)
    end
end

# ---------------------------------------------------------------------------
# Raw / orthonormalised LL form factor
# ---------------------------------------------------------------------------

"""
    raw_overlap_at_k_mn(kx, ky, m, n, glist, w, lattice)

`S_{mn}(k) = <φ^raw_{m,k} | φ^raw_{n,k}>`, the raw LL overlap at a single
momentum — by definition the zero-transfer form factor
`raw_formfactor_mn(k, k, (0,0), m, n)`. Used as the Gram matrix for Cholesky
orthonormalisation, so that `formfactor(k, k, (0,0)) = 1` identically.

This used to be a separate Bragg sum carrying an explicit
`exp(-lB²|G|²/4)` on top of the Gaussian already inside `ll_factor_mn`,
i.e. `exp(-|G|²lB²/2)` per shell against the vertex's `exp(-|G|²lB²/4)`.
The orthonormaliser then enforced `U†SU = I` against the wrong metric and
`formfactor(k,k,0)` ran 0.95–1.15 across the BZ at 8-shell optima. Defining
the overlap *as* the vertex removes the possibility of the two drifting apart.
"""
function raw_overlap_at_k_mn(
    kx::Float64, ky::Float64, m::Int, n::Int,
    glist::Vector{Tuple{Int,Int}}, w::Vector{ComplexF64},
    lattice::ReciprocalLattice,
)::ComplexF64
    return raw_formfactor_mn((kx, ky), (kx, ky), (0, 0), m, n, glist, w, lattice)
end

"""
    raw_overlap_matrix(k, nmax, glist, w, lattice)

The full `(nmax+1)×(nmax+1)` raw LL overlap matrix at single momentum `k`.
Used as input to Cholesky orthonormalisation.
"""
function raw_overlap_matrix(
    k::Tuple{Float64,Float64}, nmax::Int,
    glist::Vector{Tuple{Int,Int}}, w::Vector{ComplexF64},
    lattice::ReciprocalLattice,
)
    S = Matrix{ComplexF64}(undef, nmax + 1, nmax + 1)
    @inbounds for m in 0:nmax
        S[m + 1, m + 1] = raw_overlap_at_k_mn(k[1], k[2], m, m, glist, w, lattice)
        for n in (m + 1):nmax
            v = raw_overlap_at_k_mn(k[1], k[2], m, n, glist, w, lattice)
            S[m + 1, n + 1] = v
            S[n + 1, m + 1] = conj(v)
        end
    end
    return S
end

"""
    orthonormalizer(k, nmax, glist, w, lattice; reg=0.0) -> U

`U(k) := R⁻¹` where `R = chol(S).U` and `S = raw_overlap_matrix(k, …)`.
Then `U(k)† S(k) U(k) = I`.
"""
function orthonormalizer(
    k::Tuple{Float64,Float64}, nmax::Int,
    glist::Vector{Tuple{Int,Int}}, w::Vector{ComplexF64},
    lattice::ReciprocalLattice; reg::Float64 = 0.0,
)
    S = raw_overlap_matrix(k, nmax, glist, w, lattice)
    S = 0.5 .* (S .+ S')  # numerical Hermitian cleanup
    if reg != 0.0
        @inbounds for i in 1:(nmax + 1)
            S[i, i] += reg
        end
    end
    R = cholesky(Hermitian(S)).U
    return R \ Matrix{ComplexF64}(I, size(R, 1), size(R, 2))
end

"""
    raw_formfactor_mn(kbra, kket, G, m, n, glist, w, lattice)

Raw LL form-factor matrix element
`<φ^raw_{m,kbra}| ρ_G |φ^raw_{n,kket}>`, with the implementation convention
`q_λ = k' - k - G`.
"""
function raw_formfactor_mn(
    kbra::Tuple{Float64,Float64}, kket::Tuple{Float64,Float64},
    G::Tuple{Int,Int}, m::Int, n::Int,
    glist::Vector{Tuple{Int,Int}}, w::Vector{ComplexF64},
    lattice::ReciprocalLattice,
)::ComplexF64
    kbx, kby = kbra
    kkx, kky = kket
    ksumx = kbx + kkx
    ksumy = kby + kky
    pref = cis((LB2 / 2) * cross2(kkx, kky, kbx, kby))

    s = ComplexF64(0)
    @inbounds for ig in eachindex(glist)
        wg = w[ig]
        wg == 0.0 + 0.0im && continue
        c1, c2 = glist[ig]
        d1 = G[1] - c1
        d2 = G[2] - c2
        bx, by = vecG((d1, d2), lattice)
        η = (iseven(d1) && iseven(d2)) ? 1.0 : -1.0
        qx = kkx - kbx - bx
        qy = kky - kby - by
        llmn = ll_factor_mn(qx, qy, m, n)
        phasekb = cis((LB2 / 2) * cross2(ksumx, ksumy, bx, by))
        s += η * wg * pref * phasekb * llmn
    end
    return s
end

"""
    raw_formfactor_matrix(kbra, kket, G, nmax, glist, w, lattice)

`(nmax+1)×(nmax+1)` raw LL form factor matrix between two momenta and
Umklapp `G`. Inputs identical to `raw_formfactor_mn`.
"""
function raw_formfactor_matrix(
    kbra::Tuple{Float64,Float64}, kket::Tuple{Float64,Float64},
    G::Tuple{Int,Int}, nmax::Int,
    glist::Vector{Tuple{Int,Int}}, w::Vector{ComplexF64},
    lattice::ReciprocalLattice,
)
    # Same arithmetic as `raw_formfactor_mn` for every (m, n), with the
    # per-G pieces (q, Gaussian, α, both phases) computed once instead of
    # (nmax+1)² times; the G-sum runs in the same order, so every entry is
    # bitwise identical (julia/test/test_formfactor_fast.jl). 3–4× faster.
    F = zeros(ComplexF64, nmax + 1, nmax + 1)
    kbx, kby = kbra
    kkx, kky = kket
    ksumx = kbx + kkx
    ksumy = kby + kky
    pref = cis((LB2 / 2) * cross2(kkx, kky, kbx, kby))
    @inbounds for ig in eachindex(glist)
        wg = w[ig]
        wg == 0.0 + 0.0im && continue
        c1, c2 = glist[ig]
        d1 = G[1] - c1
        d2 = G[2] - c2
        bx, by = vecG((d1, d2), lattice)
        η = (iseven(d1) && iseven(d2)) ? 1.0 : -1.0
        qx = kkx - kbx - bx
        qy = kky - kby - by
        x, α, gauss = ll_factor_args(qx, qy)
        phasekb = cis((LB2 / 2) * cross2(ksumx, ksumy, bx, by))
        c = η * wg * pref * phasekb
        for m in 0:nmax, n in 0:nmax
            F[m + 1, n + 1] += c * ll_factor_mn(x, α, gauss, m, n)
        end
    end
    return F
end

# ---------------------------------------------------------------------------
# Trial-band form factor: orthonormalised LL tower weighted by `a_n`
# ---------------------------------------------------------------------------

"""
    TrialFormFactor

Cached state for evaluating the trial-band form factor `λ^MC_G(k, k')`
at arbitrary `k`. Holds the bare `w_G` data, the lattice, the LL-mix
weights, and a `U(k)` cache so repeated calls at the same `k` skip the
Cholesky factorisation.

`level_mix` is a vector of `(weight, n_LL)` pairs with **real
non-negative weights**. The model is an incoherent (probability-weighted)
mixture of orthonormalised LL bands:

    λ_G^{MC; k k'} = (Σ_n t_n λ_G^{orth,nn; k k'}) / (Σ_n t_n)

We pass `t_n = |a_n|²` here so weights sum to 1 (since `a_n` is gauge-
fixed to unit norm upstream). Passing the complex `a_n` directly as weights
would not give a probability-weighted mixture.
"""
mutable struct TrialFormFactor
    glist::Vector{Tuple{Int,Int}}
    w::Vector{ComplexF64}
    lattice::ReciprocalLattice
    level_mix::Vector{Tuple{Float64,Int}}
    nmax::Int
    reg::Float64
    u_cache::Dict{Tuple{Float64,Float64}, Matrix{ComplexF64}}
    kernel::Any   # `nothing` (static model) or a `DeformationKernel` (k-dependent envelope)
    # `formfactor` memo keyed on (kbra, kket, G). A scatter-list build asks for
    # each (k, k', G) about 2·Nk times (once per partner pair of the two-body
    # vertex), and every request costs (nmax+1)² × |glist| LL factors; the
    # memo made the 4×6 build ~10× faster. Values are the
    # unmodified function results, so outputs are bitwise identical.
    ff_cache::Dict{NTuple{6,Float64}, ComplexF64}
end

function TrialFormFactor(
    glist::Vector{Tuple{Int,Int}}, w::Vector{ComplexF64},
    lattice::ReciprocalLattice, level_mix::Vector{Tuple{Float64,Int}};
    reg::Float64 = 0.0, kernel = nothing,
)
    nmax = isempty(level_mix) ? 0 : maximum(n for (_, n) in level_mix)
    cache = Dict{Tuple{Float64,Float64}, Matrix{ComplexF64}}()
    return TrialFormFactor(glist, w, lattice, level_mix, nmax, reg, cache, kernel,
                           Dict{NTuple{6,Float64}, ComplexF64}())
end

"""
    coeffs(tff, kbra, kket) -> Vector{ComplexF64}

The density coefficients the raw form factor between `kbra` and `kket` is
built from, aligned with `tff.glist`. Static model: the seed `w`, for every
pair. k-dependent envelope: `W_G(kbra, kket)` from the deformation
kernel, cached per ordered pair. This is the seam — the only place
the `k`-dependence enters; everything downstream is unchanged.
"""
@inline function coeffs(tff::TrialFormFactor, kbra::Tuple{Float64,Float64}, kket::Tuple{Float64,Float64})
    tff.kernel === nothing && return tff.w
    return kernel_coeffs!(tff.kernel, kbra, kket)
end

function get_U(tff::TrialFormFactor, k::Tuple{Float64,Float64})
    cached = get(tff.u_cache, k, nothing)
    cached !== nothing && return cached
    U = orthonormalizer(k, tff.nmax, tff.glist, coeffs(tff, k, k), tff.lattice; reg = tff.reg)
    tff.u_cache[k] = U
    return U
end

"""
    formfactor(tff, kbra, kket, G)

Trial-band form factor `λ^MC_G(kbra, kket)`
with the diagonal `level_mix` convention (weights `t_n = |a_n|²`,
normalisation `Σ|a_n|² = 1` handled upstream).
"""
function formfactor(
    tff::TrialFormFactor,
    kbra::Tuple{Float64,Float64}, kket::Tuple{Float64,Float64},
    G::Tuple{Int,Int},
)::ComplexF64
    isempty(tff.level_mix) && return ComplexF64(0)
    key = (kbra[1], kbra[2], kket[1], kket[2], Float64(G[1]), Float64(G[2]))
    return get!(() -> formfactor_uncached(tff, kbra, kket, G), tff.ff_cache, key)
end

function formfactor_uncached(
    tff::TrialFormFactor,
    kbra::Tuple{Float64,Float64}, kket::Tuple{Float64,Float64},
    G::Tuple{Int,Int},
)::ComplexF64
    Ubra = get_U(tff, kbra)
    Uket = get_U(tff, kket)
    Fraw = raw_formfactor_matrix(kbra, kket, G, tff.nmax, tff.glist, coeffs(tff, kbra, kket), tff.lattice)
    Forth = Ubra' * Fraw * Uket
    out = ComplexF64(0)
    @inbounds for (t, n) in tff.level_mix
        out += t * Forth[n + 1, n + 1]
    end
    return out
end

# ---------------------------------------------------------------------------
# Gate-screened Coulomb (matches `V_Coulomb` of MomentumED.jl's Landau-level
# torus example)
# ---------------------------------------------------------------------------

"""
    V_Coulomb(ql; W0=1.0, d_l=0.0, D_l=10.0, same_layer=true)

Gate-screened bilayer Coulomb interaction. When `d_l = 0` this reduces
to the monolayer form. `ql ≡ |q|·l` is the dimensionless momentum.
"""
function V_Coulomb(
    ql::Float64;
    W0::Float64 = 1.0, d_l::Float64 = 0.0, D_l::Float64 = 10.0,
    same_layer::Bool = true,
)::Float64
    DD_l = 2.0 * D_l
    if ql == 0.0
        if same_layer
            V = W0 * (DD_l + d_l) * (DD_l - d_l) / (2.0 * DD_l)
        else
            V = W0 * (DD_l - d_l)^2 / (2.0 * DD_l)
        end
        return V
    end
    expd = exp(-ql * d_l)
    expD = exp(-ql * DD_l)
    if same_layer
        return W0 * (inv(expd) - expD) * (expd - expD) / (1.0 - expD^2) / ql
    else
        return W0 * (expd - expD)^2 / (1.0 - expD^2) / ql / expd
    end
end

# ---------------------------------------------------------------------------
# H_two callable for MomentumED
# ---------------------------------------------------------------------------

"""
    TrialBandH2

Callable matching the `EDPara.H_two` 8-arg signature
`(kf1, kf2, ki2, ki1, cf1, cf2, ci2, ci1) -> ComplexF64`.

Single-component / single-band: the spin/layer indices are placeholders
and must all be 1; we never instantiate `EDPara` with more than one
component.
"""
struct TrialBandH2
    tff::TrialFormFactor
    lattice::ReciprocalLattice
    Gk::NTuple{2,Int}
    qlist::Vector{Tuple{Int,Int}}
    qmax::Int
    W0::Float64
    d_l::Float64
    D_l::Float64
end

function (h::TrialBandH2)(
    kf1::Tuple{<:Real,<:Real}, kf2::Tuple{<:Real,<:Real},
    ki2::Tuple{<:Real,<:Real}, ki1::Tuple{<:Real,<:Real},
    cf1::Int = 1, cf2::Int = 1, ci2::Int = 1, ci1::Int = 1,
)::ComplexF64
    @assert cf1 == 1 && cf2 == 1 && ci2 == 1 && ci1 == 1 "single-component trial band"

    Gx1 = real(h.lattice.G1); Gy1 = imag(h.lattice.G1)
    Gx2 = real(h.lattice.G2); Gy2 = imag(h.lattice.G2)

    # Convert fractional momenta (k1, k2) → Cartesian (kx, ky).
    function cart(k::Tuple{<:Real,<:Real})
        return (Float64(k[1]) * Gx1 + Float64(k[2]) * Gx2,
                Float64(k[1]) * Gy1 + Float64(k[2]) * Gy2)
    end
    km  = cart(ki1)
    kn  = cart(kf1)
    km2 = cart(ki2)
    kn2 = cart(kf2)

    # Net Umklapp shift from momentum conservation: nearest-integer rounding of
    # (ki1 + ki2 - kf1 - kf2) in fractional units, as in the Landau-level torus
    # example of MomentumED.jl.
    Gdif1 = round(Int, ki1[1] + ki2[1] - kf1[1] - kf2[1], RoundNearest)
    Gdif2 = round(Int, ki1[2] + ki2[2] - kf1[2] - kf2[2], RoundNearest)

    vsum = ComplexF64(0)
    @inbounds for Q in h.qlist
        # Kernel momentum: shift q by (km - kn) for the off-diagonal Umklapp
        # channels. For the diagonal m == n case the shift vanishes (km == kn).
        qxv, qyv = vecG(Q, h.lattice)
        qx_ker = qxv + (km[1] - kn[1])
        qy_ker = qyv + (km[2] - kn[2])
        qabs = sqrt(qx_ker * qx_ker + qy_ker * qy_ker)

        if Gdif1 == 0 && Gdif2 == 0
            ov = formfactor(h.tff, km, kn, Q) *
                 formfactor(h.tff, km2, kn2, (-Q[1], -Q[2]))
        else
            Q2 = (Q[1] + Gdif1, Q[2] + Gdif2)
            # Only contribute if the shifted Q lies in our cached q grid.
            (abs(Q2[1]) <= h.qmax && abs(Q2[2]) <= h.qmax &&
             abs(Q2[1] - Q2[2]) <= h.qmax) || continue
            ov = formfactor(h.tff, km, kn, Q) *
                 formfactor(h.tff, km2, kn2, (-Q2[1], -Q2[2]))
        end

        vsum += ov * V_Coulomb(
            qabs * LB; W0 = h.W0, d_l = h.d_l, D_l = h.D_l, same_layer = true,
        )
    end
    return vsum
end

"""Build the hexagonal q-grid `|i-j| ≤ qmax`, `-qmax ≤ i, j ≤ qmax`."""
function build_qgrid(qmax::Int)
    qs = Tuple{Int,Int}[]
    for i in -qmax:qmax, j in -qmax:qmax
        abs(i - j) <= qmax && push!(qs, (i, j))
    end
    return qs
end

# ---------------------------------------------------------------------------
# Single-particle BC overlap for Wilson-loop Chern
# ---------------------------------------------------------------------------

"""
    trial_orbital_overlap(tff, k_list, Gk, shift_f, shift_i, ll_weights2) -> Vector{ComplexF64}

For each `k_idx`, returns `<ψ_{k+shift_f} | ψ_{k+shift_i}>` for the
trial single-particle state in the orthonormalised-LL-tower basis with
weights `ll_weights2 = (|a_n|², n)`. Diagonal-LL approximation; off-LL
Berry-connection contributions are dropped (exact for single-LL trial
bands).

`shift_*` are in fractional units of `Gk`.
"""
function trial_orbital_overlap(
    tff::TrialFormFactor, k_list::Matrix{Int}, Gk::NTuple{2,Int},
    shift_f::Tuple{<:Real,<:Real}, shift_i::Tuple{<:Real,<:Real},
    ll_weights2::Vector{Tuple{Float64,Int}},
)
    Nk = size(k_list, 2)
    Gx1 = real(tff.lattice.G1); Gy1 = imag(tff.lattice.G1)
    Gx2 = real(tff.lattice.G2); Gy2 = imag(tff.lattice.G2)
    overlap = Vector{ComplexF64}(undef, Nk)
    for k_idx in 1:Nk
        kf_frac = (
            (k_list[1, k_idx] + shift_f[1]) / Gk[1],
            (k_list[2, k_idx] + shift_f[2]) / Gk[2],
        )
        ki_frac = (
            (k_list[1, k_idx] + shift_i[1]) / Gk[1],
            (k_list[2, k_idx] + shift_i[2]) / Gk[2],
        )
        kf_cart = (Float64(kf_frac[1]) * Gx1 + Float64(kf_frac[2]) * Gx2,
                   Float64(kf_frac[1]) * Gy1 + Float64(kf_frac[2]) * Gy2)
        ki_cart = (Float64(ki_frac[1]) * Gx1 + Float64(ki_frac[2]) * Gx2,
                   Float64(ki_frac[1]) * Gy1 + Float64(ki_frac[2]) * Gy2)

        Ubra = get_U(tff, kf_cart)
        Uket = get_U(tff, ki_cart)
        Fraw = raw_formfactor_matrix(kf_cart, ki_cart, (0, 0), tff.nmax,
                                     tff.glist, coeffs(tff, kf_cart, ki_cart), tff.lattice)
        Forth = Ubra' * Fraw * Uket
        s = ComplexF64(0)
        @inbounds for (w2, n) in ll_weights2
            s += w2 * Forth[n + 1, n + 1]
        end
        overlap[k_idx] = s
    end
    return overlap
end

# ---------------------------------------------------------------------------
# Many-body gap + Chern extraction
# ---------------------------------------------------------------------------

function compute_mb_gap(energies_per_block::Vector{Vector{Float64}}, m::Int)
    tagged = NTuple{2,Any}[]
    for (i, vals) in enumerate(energies_per_block)
        for (j, e) in enumerate(vals)
            push!(tagged, (e, (i, j)))
        end
    end
    sort!(tagged, by = x -> x[1])
    if length(tagged) < m + 1
        error("too few eigenvalues collected (have $(length(tagged)), need ≥ $(m + 1))")
    end
    e_top_gs = tagged[m][1]
    e_first_excited = tagged[m + 1][1]
    gap = e_first_excited - e_top_gs
    gs_block_idxs = sort(unique(t[2][1] for t in tagged[1:m]))
    return gap, e_top_gs, e_first_excited, gs_block_idxs
end

"""Twists of the origin-plaquette Wilson loop (closed: first == last == 0)."""
plaquette_path(N_kshift::Int) = Tuple{Rational,Rational}[
    (0 // 1, 0 // 1),
    (1 // N_kshift, 0 // 1),
    (1 // N_kshift, 1 // N_kshift),
    (0 // 1, 1 // N_kshift),
    (0 // 1, 0 // 1),
]

"""The `m` lowest many-body states as `(block_idx, state_idx)`, energy order."""
function lowest_states(energies::Vector{Vector{Float64}}, m::Int)
    tagged = NTuple{2,Any}[]
    for (i, vals) in enumerate(energies), (j, e) in enumerate(vals)
        push!(tagged, (e, (i, j)))
    end
    sort!(tagged, by = x -> x[1])
    return [t[2] for t in tagged[1:m]]
end

function per_state_wilson_chern(
    para::EDPara,
    tff::TrialFormFactor,
    subspace,
    k_list::Matrix{Int},
    Gk::NTuple{2,Int},
    gs_state_at_zero,
    gs_state_idx::Int,
    ll_weights2::Vector{Tuple{Float64,Int}};
    N_kshift::Int = 10,
    Neigen::Int = 6,
    method::Symbol = :sparse,
    scat_cache::AbstractDict = Dict{Any,Any}(),
    presolved::AbstractDict = Dict{Any,Any}(),
    block_idx::Int = 0,
    ed::Union{Nothing,EDSettings} = nothing,
    stats::Union{Nothing,EDStats} = nothing,
)
    path = plaquette_path(N_kshift)
    psi = Vector{Any}(undef, length(path))
    psi[1] = gs_state_at_zero
    psi[end] = gs_state_at_zero
    for i in 2:length(path) - 1
        hit = get(presolved, (block_idx, path[i]), nothing)
        if hit !== nothing
            psi[i] = hit[2][gs_state_idx]
            continue
        end
        # The path is the same for every tracked state; build each twist once.
        scat_list = get!(() -> ED_scatterlist_twobody(para; kshift = path[i]), scat_cache, path[i])
        if ed === nothing
            N_block = min(Neigen, length(subspace))
            _, vecs_i = EDsolve(
                subspace, scat_list;
                N = N_block, showtime = false, ishermitian = true, method_info = false,
                method = method,
            )
        else
            N_block = min(twist_levels(ed, gs_state_idx), length(subspace))
            _, vecs_i, st = cpu_solve(ed, subspace, scat_list; N = N_block)
            stats === nothing || record!(stats, st, N_block)
        end
        psi[i] = vecs_i[gs_state_idx]
    end
    WilsonLoopIntegral = Vector{ComplexF64}(undef, 4)
    for i in 1:4
        orbital_bc = trial_orbital_overlap(
            tff, k_list, Gk, path[i + 1], path[i], ll_weights2,
        )
        WilsonLoopIntegral[i] = step_inner_prod(psi[i + 1], psi[i], orbital_bc)
    end
    return angle(prod(WilsonLoopIntegral)) / (2π) * N_kshift^2
end

"""
    many_body_chern_manifold(...)

Sum of per-state Wilson-loop Chern numbers over the `m_degeneracy`
lowest-energy many-body states.

**Precondition:** the `m_degeneracy` lowest-energy states must live in
`m_degeneracy` *distinct* momentum sectors. Standard Laughlin torus
quantisation gives this for the ν=1/M GS manifold, but some mesh aspect
ratios (e.g. 3×6 at ν=1/3, where all 3 GSs cluster in `k=(0,3)`) violate
it. The caller must screen with `compute_mb_gap` and skip this routine
when the precondition fails — otherwise we integrate intra-subspace
gauge ambiguity instead of topology and produce a non-quantised
"Chern". `MoireSolver.solve` enforces this via the
`mesh_unsuitable_for_chern` short-circuit; the
`julia/diagnose_gs_sectors.jl` utility is the standalone screener.
"""
function many_body_chern_manifold(
    para::EDPara,
    tff::TrialFormFactor,
    subspaces::AbstractVector,
    k_list::Matrix{Int},
    Gk::NTuple{2,Int},
    vectors,
    energies::Vector{Vector{Float64}},
    m_degeneracy::Int,
    ll_weights2::Vector{Tuple{Float64,Int}};
    N_kshift::Int = 10,
    Neigen::Int = 6,
    method::Symbol = :sparse,
    presolved::AbstractDict = Dict{Any,Any}(),
    ed::Union{Nothing,EDSettings} = nothing,
    stats::Union{Nothing,EDStats} = nothing,
)
    chern_total = 0.0
    scat_cache = Dict{Any,Any}()
    for (block_idx, state_idx) in lowest_states(energies, m_degeneracy)
        c = per_state_wilson_chern(
            para, tff, subspaces[block_idx], k_list, Gk,
            vectors[block_idx][state_idx], state_idx, ll_weights2;
            N_kshift = N_kshift, Neigen = Neigen, method = method,
            scat_cache = scat_cache, presolved = presolved, block_idx = block_idx,
            ed = ed, stats = stats,
        )
        chern_total += c
    end
    quant_err = abs(chern_total - round(chern_total))
    return chern_total, quant_err
end

# ---------------------------------------------------------------------------
# Glued one-period FHS lattice — the production Chern estimator
# ---------------------------------------------------------------------------
#
# One twist period, N×N periodic. Across the period boundary in direction d
# the orbital labelled k sits at momentum k + e_d, i.e. it IS the orbital
# labelled T_d(k) = k + e_d (mod Gk) of the zero-twist problem, and the ground
# state of sector K flows into sector K + Ne·e_d. Gluing the Fock basis across
# the boundary needs (i) the relabelling T_d with its fermionic sign, (ii) the
# sector permutation among the m tracked states, and (iii) for the orbital
# that wraps past the zone edge, the periodic-gauge overlap
# <u_{k'}|e^{-iG·r}|u_k> — the raw form factor with Umklapp index G, the same
# bookkeeping the two-body vertex uses through `Gdif`.
#
# Sewing orientation. The two-body vertex calls `formfactor(tff, k_in, k_out, Q)`,
# so `raw(kbra, kket, Q)` acts as <kket|ρ_Q|kbra> and
# `trial_orbital_overlap(shift_f, shift_i)` returns <φ_i|φ_f>. The many-body
# link must multiply the coefficient overlap Σ conj(ψ_f)ψ_i by <φ_f|φ_i>, the
# CONJUGATE of that routine — the "consistent" sewing. Only with it does the
# glued period close (measured closure 8e-15 vs 0.7 with the
# production orientation), and only it measures C_coeff + C_orb rather than
# C_coeff − C_orb (the stored C=3 state is a clean bundle with C_coeff = +1,
# C_orb = −1, physical C = 0).
#
# Sign convention: the consistent sewing gives C = −1 for every
# LL0-based FCI where the origin-plaquette estimator gave +1. `chern_solver`
# reports −round(C_consistent) so history keeps its +1; `chern_glued_raw`
# records the unflipped value.

struct GluedChernError <: Exception
    reason::String
    msg::String
end

"Many-body link <ψ_f|ψ_i> at twists θ_f, θ_i with the consistent sewing."
function consistent_link(
    tff::TrialFormFactor, k_list::Matrix{Int}, Gk::NTuple{2,Int},
    ψ_f, θ_f, ψ_i, θ_i, ll_weights2::Vector{Tuple{Float64,Int}},
)
    orb = conj.(trial_orbital_overlap(tff, k_list, Gk, θ_f, θ_i, ll_weights2))
    return step_inner_prod(ψ_f, ψ_i, orb)
end

"""
    step_inner_prod(ψ_f, ψ_i, orb) -> ComplexF64

`MomentumED.ED_step_inner_prod` without its per-state allocations and
threaded: Σ_x conj(ψ_f[x]) ψ_i[x] Π_{occupied k} orb[k]. Each state's
orbital product is taken over set bits in ascending order — the order
`occ_list` gives — so every term is bitwise the same; per-thread partial sums
are added in a fixed order (deterministic for a given thread count). 5×6:
~50 links of 1M states each were ~25 s serial.
"""
function step_inner_prod(ψ_f, ψ_i, orb::Vector{ComplexF64})
    (ψ_f.space === ψ_i.space || ψ_f.space.list == ψ_i.space.list) ||
        error("step_inner_prod: Hilbert subspaces of the two states differ")
    L = ψ_f.space.list
    vf = ψ_f.vec; vi = ψ_i.vec
    n = length(L)
    nt = Threads.nthreads()
    chunk = cld(n, nt)
    partial = zeros(ComplexF64, nt)
    Threads.@threads :static for t in 1:nt
        acc = zero(ComplexF64)
        @inbounds for x in (t - 1) * chunk + 1:min(t * chunk, n)
            b = L[x].n
            p = one(ComplexF64)
            while b != 0
                p *= orb[trailing_zeros(b) + 1]
                b &= b - one(b)
            end
            acc += (conj(vf[x]) * vi[x]) * p
        end
        partial[t] = acc
    end
    return sum(partial)
end

"Parity sign of the permutation that sorts `v`."
function perm_sign(v::Vector{Int})
    inv = 0
    for a in 1:length(v) - 1, b in a + 1:length(v)
        v[a] > v[b] && (inv += 1)
    end
    return isodd(inv) ? -1.0 : 1.0
end

"""
Index of the mesh point `k + e_d` (mod Gk) and whether the step wrapped past
the zone edge. Uses the mesh's own point table, so any cluster that contains
the unit steps works; one that does not is reported as unsuitable.
"""
function relabel_orbital(
    index::Dict{Tuple{Int,Int},Int}, k_list::Matrix{Int}, Gk::NTuple{2,Int},
    i::Int, d::Int,
)
    k1, k2 = k_list[1, i], k_list[2, i]
    key = d == 1 ? (mod(k1 + 1, Gk[1]), k2) : (k1, mod(k2 + 1, Gk[2]))
    j = get(index, key, 0)
    j == 0 && throw(GluedChernError(
        "mesh_unsuitable_for_glued_chern",
        "mesh point $(key) is not on the cluster: the glued lattice needs the unit twist steps",
    ))
    wrapped = d == 1 ? k1 + 1 == Gk[1] : k2 + 1 == Gk[2]
    return j, wrapped
end

"""
Identification phases across the period boundary in direction `d`, indexed by
the orbital label `i` of the beyond-point labelling: orbital `T_d(i)` at twist
`θ_src` (zero-twist labelling) against orbital `i` at `θ_beyond = θ_src + e_d`.
Wrapped orbitals use the Umklapp index `e_d` so the momentum transfer is zero.
"""
function glued_orbital_overlap(
    tff::TrialFormFactor, index, k_list::Matrix{Int}, Gk::NTuple{2,Int},
    θ_src, θ_beyond, d::Int, ll_weights2::Vector{Tuple{Float64,Int}},
)
    Gx1 = real(tff.lattice.G1); Gy1 = imag(tff.lattice.G1)
    Gx2 = real(tff.lattice.G2); Gy2 = imag(tff.lattice.G2)
    cart(f1, f2) = (Float64(f1) * Gx1 + Float64(f2) * Gx2, Float64(f1) * Gy1 + Float64(f2) * Gy2)
    Gu = d == 1 ? (1, 0) : (0, 1)
    Nk = size(k_list, 2)
    o = Vector{ComplexF64}(undef, Nk)
    for i in 1:Nk
        j, wrapped = relabel_orbital(index, k_list, Gk, i, d)
        kbra = cart((k_list[1, j] + θ_src[1]) // Gk[1], (k_list[2, j] + θ_src[2]) // Gk[2])
        kket = cart((k_list[1, i] + θ_beyond[1]) // Gk[1], (k_list[2, i] + θ_beyond[2]) // Gk[2])
        Fraw = raw_formfactor_matrix(kbra, kket, wrapped ? Gu : (0, 0), tff.nmax,
                                     tff.glist, coeffs(tff, kbra, kket), tff.lattice)
        Forth = get_U(tff, kbra)' * Fraw * get_U(tff, kket)
        acc = ComplexF64(0)
        @inbounds for (t, n) in ll_weights2
            acc += t * Forth[n + 1, n + 1]
        end
        o[i] = acc
    end
    return o
end

"""
Express the zero-twist-labelled vector `ψ_src` in the basis of block `b_dst`
as seen from twist `θ_d = 1`:  `Φ[x] = (Π_{i∈x} phases[i]) · sgn(π_x) · ψ_src[T_d(x)]`.
The orientation of `phases` (not its conjugate) was fixed against a direct
solve at `θ = e_d`.
"""
function relabel_vector(
    ψ_src, subspace_dst, index, k_list::Matrix{Int}, Gk::NTuple{2,Int},
    d::Int, phases::Vector{ComplexF64},
)
    L_dst = subspace_dst.list
    L_src = ψ_src.space.list
    bits = size(k_list, 2)
    out = Vector{ComplexF64}(undef, length(L_dst))
    # Entries are independent (threaded for the 1M-dim 5×6 sectors).
    # The not-found error is raised after the loop: thrown inside @threads it
    # would arrive wrapped in TaskFailedException and be routed as transient.
    missing_state = Threads.Atomic{Bool}(false)
    Threads.@threads for x in eachindex(L_dst)
        occ = occ_list(L_dst[x])
        tocc = [relabel_orbital(index, k_list, Gk, i, d)[1] for i in occ]
        sgn = perm_sign(tocc)
        y = MBS64(bits, tocc)
        idx = searchsortedfirst(L_src, y)
        if !(idx <= length(L_src) && L_src[idx] == y)
            missing_state[] = true
            continue
        end
        out[x] = prod(phases[occ]) * sgn * ψ_src.vec[idx]
    end
    missing_state[] && throw(GluedChernError(
        "chern_manifold_not_spectral_flow_orbit",
        "relabelled Fock state not found in the target sector",
    ))
    return MBS64Vector(out, subspace_dst)
end

"Index of the tracked state whose sector is `K_s + Ne·e_d` (mod Gk)."
function sector_permutation(ss_k, picks, Gk::NTuple{2,Int}, Ne::Int, d::Int)
    perm = zeros(Int, length(picks))
    for (s, (b, _)) in enumerate(picks)
        K = ss_k[b]
        Kp = d == 1 ? (mod(Int(K[1]) + Ne, Gk[1]), Int(K[2])) : (Int(K[1]), mod(Int(K[2]) + Ne, Gk[2]))
        t = findfirst(q -> (Int(ss_k[q[1]][1]), Int(ss_k[q[1]][2])) == Kp, picks)
        t === nothing && throw(GluedChernError(
            "chern_manifold_not_spectral_flow_orbit",
            "spectral flow leaves the tracked manifold: sector $(Kp) is not a tracked ground state",
        ))
        perm[s] = t
    end
    return perm
end

"""
    glued_lattice_chern(...) -> NamedTuple

Many-body Chern number of the `m_degeneracy` tracked ground states from the
glued one-period FHS lattice with the consistent sewing. Returns
`(C, per_state, residual, max_abs_phase, closure, N)` with `C` the summed
plaquette phase / 2π in the consistent orientation (unflipped). Throws
`GluedChernError` when the mesh lacks the unit steps or the tracked manifold
is not a spectral-flow orbit.
"""
function glued_lattice_chern(
    para::EDPara, tff::TrialFormFactor, subspaces::AbstractVector, ss_k,
    k_list::Matrix{Int}, Gk::NTuple{2,Int}, Ne::Int,
    vectors, energies::Vector{Vector{Float64}}, m_degeneracy::Int,
    ll_weights2::Vector{Tuple{Float64,Int}};
    N::Int = 2, Neigen::Int = 6, method::Symbol = :sparse,
    presolved::AbstractDict = Dict{Any,Any}(),
    ed::Union{Nothing,EDSettings} = nothing,
    stats::Union{Nothing,EDStats} = nothing,
)
    N >= 2 || throw(ArgumentError("glued lattice needs N ≥ 2"))
    picks = lowest_states(energies, m_degeneracy)         # (block, state)
    m = length(picks)
    Nk = size(k_list, 2)
    index = Dict{Tuple{Int,Int},Int}((k_list[1, i], k_list[2, i]) => i for i in 1:Nk)

    p1 = sector_permutation(ss_k, picks, Gk, Ne, 1)
    p2 = sector_permutation(ss_k, picks, Gk, Ne, 2)

    # interior N×N grid; the origin reuses the zero-twist vectors
    states = [Matrix{Any}(undef, N + 1, N + 1) for _ in 1:m]
    for j in 0:N - 1, i in 0:N - 1
        if i == 0 && j == 0
            for (s, (b, st)) in enumerate(picks)
                states[s][1, 1] = vectors[b][st]
            end
            continue
        end
        if all(haskey(presolved, (b, (i // N, j // N))) for (b, _) in picks)
            for (s, (b, st)) in enumerate(picks)
                states[s][i + 1, j + 1] = presolved[(b, (i // N, j // N))][2][st]
            end
            continue
        end
        scat = ED_scatterlist_twobody(para; kshift = (i // N, j // N))
        for (s, (b, st)) in enumerate(picks)
            if ed === nothing
                N_block = min(Neigen, length(subspaces[b]))
                _, vecs = EDsolve(subspaces[b], scat;
                    N = N_block, showtime = false, ishermitian = true,
                    method = method, method_info = false)
            else
                N_block = min(twist_levels(ed, st), length(subspaces[b]))
                _, vecs, sst = cpu_solve(ed, subspaces[b], scat; N = N_block)
                stats === nothing || record!(stats, sst, N_block)
            end
            states[s][i + 1, j + 1] = vecs[st]
        end
    end
    # glued beyond column, row and corner
    for s in 1:m
        b = picks[s][1]
        for j in 0:N - 1
            o = glued_orbital_overlap(tff, index, k_list, Gk, (0 // 1, j // N), (1 // 1, j // N), 1, ll_weights2)
            states[s][N + 1, j + 1] = relabel_vector(states[p1[s]][1, j + 1], subspaces[b], index, k_list, Gk, 1, o)
        end
        for i in 0:N - 1
            o = glued_orbital_overlap(tff, index, k_list, Gk, (i // N, 0 // 1), (i // N, 1 // 1), 2, ll_weights2)
            states[s][i + 1, N + 1] = relabel_vector(states[p2[s]][i + 1, 1], subspaces[b], index, k_list, Gk, 2, o)
        end
        o2 = glued_orbital_overlap(tff, index, k_list, Gk, (0 // 1, 0 // 1), (0 // 1, 1 // 1), 2, ll_weights2)
        Φ2 = relabel_vector(states[p2[p1[s]]][1, 1], subspaces[picks[p1[s]][1]], index, k_list, Gk, 2, o2)
        o1 = glued_orbital_overlap(tff, index, k_list, Gk, (0 // 1, 1 // 1), (1 // 1, 1 // 1), 1, ll_weights2)
        states[s][N + 1, N + 1] = relabel_vector(Φ2, subspaces[b], index, k_list, Gk, 1, o1)
    end

    link(ψf, θf, ψi, θi) = consistent_link(tff, k_list, Gk, ψf, θf, ψi, θi, ll_weights2)
    per_state = zeros(Float64, m)
    max_abs_phase = 0.0
    for s in 1:m
        ψ = states[s]
        for j in 0:N - 1, i in 0:N - 1
            q1 = (i // N, j // N); q2 = ((i + 1) // N, j // N)
            q3 = ((i + 1) // N, (j + 1) // N); q4 = (i // N, (j + 1) // N)
            W = link(ψ[i + 2, j + 1], q2, ψ[i + 1, j + 1], q1) *
                link(ψ[i + 2, j + 2], q3, ψ[i + 2, j + 1], q2) *
                link(ψ[i + 1, j + 2], q4, ψ[i + 2, j + 2], q3) *
                link(ψ[i + 1, j + 1], q1, ψ[i + 1, j + 2], q4)
            φ = angle(W)
            per_state[s] += φ / (2π)
            max_abs_phase = max(max_abs_phase, abs(φ))
        end
    end
    # closure: the beyond-column links of s must equal the first-column links of p1(s)
    closure = 0.0
    for s in 1:m, j in 0:N - 2
        top = link(states[s][N + 1, j + 2], (1 // 1, (j + 1) // N), states[s][N + 1, j + 1], (1 // 1, j // N))
        bot = link(states[p1[s]][1, j + 2], (0 // 1, (j + 1) // N), states[p1[s]][1, j + 1], (0 // 1, j // N))
        closure = max(closure, abs(top - bot))
    end
    C = sum(per_state)
    return (C = C, per_state = per_state, residual = abs(C - round(C)),
            max_abs_phase = max_abs_phase, closure = closure, N = N)
end

# ---------------------------------------------------------------------------
# k-dependent envelope kernel — the seam
# ---------------------------------------------------------------------------
#
# Seed-plus-deformation chart (src/mosaic/physics/kdep_envelope.py is
# the reference implementation this must reproduce to round-off):
#
#   h_k(r)     = h_*(r) exp(γ(k, r)),
#   γ(k, r)    = Σ_{s,p} (α_sp/2 + i β_sp) O_s(r) F_p(k),
#   O_s(r)     = d_s^{-1/2} Σ_{G∈S_s} e^{iG·r},   F_p(k) = d_p^{-1/2} Σ_{R∈T_p} e^{ik·R},
#   W_G(k, k') = F_G{ ρ_*(r) exp(γ(k,r)^* + γ(k',r)) },   ρ_* = Σ_L w^(0)_L e^{iL·r}.
#
# Only ρ_* enters, so a seed on a density zero is an ordinary input, and at
# γ = 0 the kernel equals the seed coefficients exactly. The kernel obeys the
# ordered-pair Hermiticity W_G(k,k')^* = W_{-G}(k',k); the same-ordered-pair
# relation is false and must not be imposed.
#
# Fourier coefficients are taken on an n_mesh × n_mesh real-space grid with a
# separable DFT restricted to the box max(|m|,|n|) ≤ g_cutoff (no FFT
# dependency; ~1e5 multiplies per momentum pair). Exponentiation generates
# harmonics beyond the seed's, so `g_cutoff` is a convergence knob,
# defaulting to the seed's own box so that γ = 0 changes nothing.
#
# Momenta arrive in Cartesian form; F_p needs fractional BZ coordinates
# f = (f1, f2) with k = f1 G1 + f2 G2 and k·R = 2π(f1 R1 + f2 R2). The kernel
# is BZ-periodic in both momenta because R is integer, which is what lets the
# twisted (off-mesh) Chern solves use it unchanged.

struct DeformationKernel
    spatial_stars::Vector{Vector{Tuple{Int,Int}}}
    momentum_stars::Vector{Vector{Tuple{Int,Int}}}
    alpha::Matrix{Float64}
    beta::Matrix{Float64}
    n_mesh::Int
    g_cutoff::Int
    glist::Vector{Tuple{Int,Int}}          # kernel G-list: the box, seed included
    seed_w::Vector{ComplexF64}             # seed coefficients aligned with glist
    rho::Matrix{ComplexF64}                # ρ_*(r) on the mesh
    O::Vector{Matrix{Float64}}             # O_s(r)
    E::Matrix{ComplexF64}                  # DFT rows, m = -cut..cut
    Ginv::Matrix{Float64}                  # Cartesian → fractional
    cache::Dict{NTuple{4,Float64},Vector{ComplexF64}}
end

function validate_star(star::Vector{Tuple{Int,Int}}, kind::String)
    isempty(star) && throw(ArgumentError("deformation: empty $(kind) star"))
    members = Set(star)
    length(members) == length(star) || throw(ArgumentError("deformation: $(kind) star has repeated members"))
    (0, 0) in members && throw(ArgumentError("deformation: $(kind) star contains the zero mode, a redundant overall scalar"))
    for (a, b) in star
        (-a, -b) in members || throw(ArgumentError(
            "deformation: $(kind) star is not inversion-symmetric ($(a),$(b)) present, ($(-a),$(-b)) absent"))
    end
end

"""
    DeformationKernel(block, glist_seed, w_seed, lattice)

Build the kernel from the JSON `deformation` block and the seed. Throws
`ArgumentError` (a logical failure) for an invalid block.
"""
function DeformationKernel(block, glist_seed::Vector{Tuple{Int,Int}}, w_seed::Vector{ComplexF64}, lattice::ReciprocalLattice)
    stars(x) = [[(Int(g[1]), Int(g[2])) for g in star] for star in x]
    S = stars(block[:spatial_stars]); T = stars(block[:momentum_stars])
    (isempty(S) || isempty(T)) && throw(ArgumentError("deformation needs at least one spatial and one momentum star"))
    foreach(st -> validate_star(st, "spatial"), S)
    foreach(st -> validate_star(st, "momentum"), T)
    J, P = length(S), length(T)
    tomat(x, name) = begin
        M = Matrix{Float64}(undef, J, P)
        length(x) == J || throw(ArgumentError("deformation.$(name) must have $(J) rows"))
        for s in 1:J
            length(x[s]) == P || throw(ArgumentError("deformation.$(name) row $(s) must have $(P) entries"))
            for p in 1:P; M[s, p] = Float64(x[s][p]); end
        end
        M
    end
    alpha = tomat(block[:alpha], "alpha"); beta = tomat(block[:beta], "beta")
    n_mesh = Int(get(block, :n_mesh, 48))
    seed_box = maximum(max(abs(g[1]), abs(g[2])) for g in glist_seed)
    cut = Int(get(block, :g_cutoff, seed_box))
    cut >= seed_box || throw(ArgumentError("deformation.g_cutoff=$(cut) is below the seed's box $(seed_box)"))
    2cut < n_mesh || throw(ArgumentError("deformation: n_mesh=$(n_mesh) must exceed 2·g_cutoff=$(2cut) (aliasing)"))

    glist = Tuple{Int,Int}[(m, n) for n in -cut:cut for m in -cut:cut]
    seed_index = Dict(g => i for (i, g) in enumerate(glist_seed))
    seed_w = [haskey(seed_index, g) ? w_seed[seed_index[g]] : ComplexF64(0) for g in glist]

    # ρ_*(r) = Σ_L w_L e^{iL·r}, r_ij = 2π(i, j)/n_mesh in the (b1, b2) basis
    rho = zeros(ComplexF64, n_mesh, n_mesh)
    for (ig, (m, n)) in enumerate(glist_seed)
        wl = w_seed[ig]; wl == 0 && continue
        for j in 0:n_mesh - 1, i in 0:n_mesh - 1
            rho[i + 1, j + 1] += wl * cis(2π * (m * i + n * j) / n_mesh)
        end
    end
    O = Matrix{Float64}[]
    for st in S
        o = zeros(ComplexF64, n_mesh, n_mesh)
        for (m, n) in st, j in 0:n_mesh - 1, i in 0:n_mesh - 1
            o[i + 1, j + 1] += cis(2π * (m * i + n * j) / n_mesh)
        end
        o ./= sqrt(length(st))
        maximum(abs.(imag.(o))) < 1e-10 || throw(ArgumentError("deformation: spatial star function is not real"))
        push!(O, real.(o))
    end
    E = Matrix{ComplexF64}(undef, 2cut + 1, n_mesh)
    for (row, m) in enumerate(-cut:cut), i in 0:n_mesh - 1
        E[row, i + 1] = cis(-2π * m * i / n_mesh)
    end
    Gmat = [real(lattice.G1) real(lattice.G2); imag(lattice.G1) imag(lattice.G2)]
    return DeformationKernel(S, T, alpha, beta, n_mesh, cut, glist, seed_w, rho, O, E,
                             inv(Gmat), Dict{NTuple{4,Float64},Vector{ComplexF64}}())
end

is_zero(K::DeformationKernel) = all(iszero, K.alpha) && all(iszero, K.beta)

"F_p(k) for every momentum star at Cartesian `k`."
function momentum_star_values(K::DeformationKernel, k::Tuple{Float64,Float64})
    f = K.Ginv * [k[1], k[2]]
    vals = Vector{Float64}(undef, length(K.momentum_stars))
    for (p, st) in enumerate(K.momentum_stars)
        acc = ComplexF64(0)
        for (r1, r2) in st
            acc += cis(2π * (f[1] * r1 + f[2] * r2))
        end
        acc /= sqrt(length(st))
        vals[p] = real(acc)
    end
    return vals
end

"γ(k, r) on the mesh."
function gamma_on_mesh(K::DeformationKernel, k::Tuple{Float64,Float64})
    F = momentum_star_values(K, k)
    g = zeros(ComplexF64, K.n_mesh, K.n_mesh)
    for s in eachindex(K.O), p in eachindex(F)
        c = 0.5 * K.alpha[s, p] + im * K.beta[s, p]
        c == 0 && continue
        g .+= (c * F[p]) .* K.O[s]
    end
    return g
end

"""
    kernel_coeffs!(K, kbra, kket) -> Vector{ComplexF64}

`W_G(kbra, kket)` aligned with `K.glist`, cached per ordered pair.
"""
function kernel_coeffs!(K::DeformationKernel, kbra::Tuple{Float64,Float64}, kket::Tuple{Float64,Float64})
    is_zero(K) && return K.seed_w
    key = (kbra[1], kbra[2], kket[1], kket[2])
    hit = get(K.cache, key, nothing)
    hit !== nothing && return hit
    field = K.rho .* exp.(conj.(gamma_on_mesh(K, kbra)) .+ gamma_on_mesh(K, kket))
    C = (K.E * field * transpose(K.E)) ./ (K.n_mesh^2)
    cut = K.g_cutoff
    out = Vector{ComplexF64}(undef, length(K.glist))
    for (ig, (m, n)) in enumerate(K.glist)
        out[ig] = C[m + cut + 1, n + cut + 1]
    end
    K.cache[key] = out
    return out
end

# ---------------------------------------------------------------------------
# Input parsing
# ---------------------------------------------------------------------------

to_complex(c) = ComplexF64(Float64(c[:re]), Float64(c[:im]))

"Decode `W_G` list → (glist::Vector{Tuple{Int,Int}}, w::Vector{ComplexF64})."
function decode_W_G(form_factor)
    glist = Tuple{Int,Int}[]
    w = ComplexF64[]
    for entry in form_factor[:W_G]
        gi = (Int(entry[:G_int][1]), Int(entry[:G_int][2]))
        push!(glist, gi)
        push!(w, to_complex(entry[:coef]))
    end
    return glist, w
end

decode_a_n(wave) = ComplexF64[ to_complex(c) for c in wave[:a_n] ]

"""
    momentum_subspaces(k_list, Gk, Ne) -> (subspaces, sector_momenta)

The Ne-particle Fock space split by total crystal momentum mod `Gk` —
`ED_momentum_subspaces(para, (Ne,); momentum_restriction = true,
momentum_list = <k_list columns>)` state for state, same sector order, empty
sectors dropped. All `binomial(Nk, Ne)` occupation masks are visited in
increasing order (Gosper's next-combination step), so each sector's list
comes out sorted; per state the cost is Ne table look-ups, and blocks of
masks run on threads. MomentumED's recursive generator took 11.5 s at 5×6
ν = 1/3 and 86 s at ν = 1/2 on 16 threads.
Single-component bands only.
"""
function momentum_subspaces(k_list::Matrix{Int}, Gk::NTuple{2,Int}, Ne::Int)
    Nk = size(k_list, 2)
    (1 <= Nk <= 64 && 0 <= Ne <= Nk) || throw(ArgumentError("momentum_subspaces: Nk = $(Nk), Ne = $(Ne)"))
    all(>(0), Gk) || throw(ArgumentError("momentum_subspaces needs periodic momenta (Gk > 0)"))
    momenta = unique([(mod(k_list[1, i], Gk[1]), mod(k_list[2, i], Gk[2])) for i in 1:Nk])
    sector_of = zeros(Int, Gk[1], Gk[2])
    for (s, K) in enumerate(momenta)
        sector_of[K[1] + 1, K[2] + 1] = s
    end
    k1 = [mod(k_list[1, i], Gk[1]) for i in 1:Nk]
    k2 = [mod(k_list[2, i], Gk[2]) for i in 1:Nk]
    nsec = length(momenta)
    # Blocks: fixed top bit h and second bit h2 (0-based, h2 < h), the other
    # Ne − 2 bits below h2. Masks in block (h, h2) all exceed those of every
    # earlier block in (h, h2) order, so concatenating the blocks' per-sector
    # lists in that order keeps every sector sorted; blocks run on threads.
    blocks = Ne >= 2 ? [(h, h2) for h in Ne - 1:Nk - 1 for h2 in Ne - 2:h - 1] : [(-1, -1)]
    parts = Vector{Vector{Vector{MBS64{Nk}}}}(undef, length(blocks))
    Threads.@threads :dynamic for bi in eachindex(blocks)
        h, h2 = blocks[bi]
        lists = [Vector{MBS64{Nk}}() for _ in 1:nsec]
        visit(x) = begin
            a = 0; b = 0; y = x
            while y != 0
                t = trailing_zeros(y) + 1
                a += k1[t]; b += k2[t]
                y &= y - UInt64(1)
            end
            s = sector_of[mod(a, Gk[1]) + 1, mod(b, Gk[2]) + 1]
            s == 0 || push!(lists[s], MBS64{Nk}(x))
        end
        if h < 0                                   # Ne ≤ 1: plain enumeration
            if Ne == 0
                visit(UInt64(0))
            else
                for i in 0:Nk - 1
                    visit(UInt64(1) << i)
                end
            end
        else
            high = (UInt64(1) << h) | (UInt64(1) << h2)
            r = Ne - 2
            if r == 0
                visit(high)
            else
                x = (UInt64(1) << r) - UInt64(1)
                top = x << (h2 - r)
                while true
                    visit(high | x)
                    x == top && break
                    c = x & (~x + UInt64(1))        # lowest set bit
                    rr = x + c
                    x = (((rr ⊻ x) >> 2) ÷ c) | rr  # Gosper: next mask, same popcount
                end
            end
        end
        parts[bi] = lists
    end
    out = [reduce(vcat, (parts[bi][s] for bi in eachindex(blocks)); init = MBS64{Nk}[]) for s in 1:nsec]
    keep = [!isempty(l) for l in out]
    return [HilbertSubspace(l) for l in out[keep]], momenta[keep]
end

"""
Threaded `y = H x` for a Hermitian matrix stored in full CSC form: row i of H is
the conjugate of column i, so each thread owns whole output rows — no atomics.
`SparseArrays`' own product is single-threaded, which left the CPU Lanczos
flat in thread count (27 sites: 11 s at 1, 4 and 16 threads).
"""
struct ThreadedHermCSC{T,I}
    A::SparseMatrixCSC{T,I}
end
function (H::ThreadedHermCSC)(x::AbstractVector)
    A = H.A
    y = similar(x)
    Threads.@threads :static for i in 1:size(A, 2)
        acc = zero(eltype(y))
        @inbounds for k in A.colptr[i]:A.colptr[i + 1] - 1
            acc += conj(A.nzval[k]) * x[A.rowval[k]]
        end
        @inbounds y[i] = acc
    end
    return y
end

"Largest number of scatter terms (with adjoints) sharing one annihilated pair."
function maximum_group_size(scat)
    counts = Dict{UInt64,Int}()
    for s in scat
        counts[s.in.n] = get(counts, s.in.n, 0) + 1
        s.in.n == s.out.n || (counts[s.out.n] = get(counts, s.out.n, 0) + 1)
    end
    return isempty(counts) ? 0 : maximum(values(counts))
end

"""
    cpu_sector_solve(subspace, scat; N, krylovdim = 30, tol = 1e-12, maxiter = 100,
                     keep = N) -> (vals, vecs, stats)

`EDsolve(...; method = :sparse)` with its pieces exposed: same sparse build
(`SparseHmltMatrix`, threaded over columns), dense at or below `dense_max`
(EDsolve: below 100), same KrylovKit parameters with a threaded matvec — plus the Krylov parameters and a stats
NamedTuple matching `gpu_sector_solve`'s. With the defaults the values are
those of `EDsolve`.
"""
function cpu_sector_solve(subspace, scat; N::Int, krylovdim::Int = 30, tol::Real = 1e-12,
                          maxiter::Int = 100, keep::Int = N, dense_max::Int = 99)
    dim = length(subspace)
    # Int32 indices when the nonzero count provably fits (each state couples to
    # at most one target per (occupied pair, scatter term in that pair's group)):
    # 17 % less matrix memory, identical values.
    Ne = dim == 0 ? 0 : count_ones(subspace.list[1].n)
    bound = Int128(dim) * (Ne * (Ne - 1) ÷ 2) * max(1, maximum_group_size(scat))
    IT = bound < typemax(Int32) ? Int32 : Int64
    t0 = time()
    H = MomentumED.Methods.SparseHmltMatrix(subspace, scat; index_type = IT)
    t_build = time() - t0
    P = H isa Hermitian ? parent(H) : H
    nnzH = length(P.nzval)
    host_bytes = nnzH * (sizeof(eltype(P.nzval)) + sizeof(eltype(P.rowval))) + sizeof(P.colptr)
    if dim <= dense_max
        F = eigen(Hermitian(Matrix(H)))
        N = min(N, dim)
        stats = (dim = dim, nnz = nnzH, backend = :dense, build_s = t_build, solve_s = 0.0,
                 numops = 0, numiter = 0, maxres = 0.0, converged = N, host_bytes = host_bytes)
        return F.values[1:N], [MBS64Vector(F.vectors[:, i], subspace) for i in 1:min(keep, N)], stats
    end
    t1 = time()
    P isa SparseMatrixCSC && !(H isa Hermitian) || error("cpu_sector_solve expects the full Hermitian CSC")
    vals, vecs, info = eigsolve(ThreadedHermCSC(P), rand(ComplexF64, dim), N, :SR; ishermitian = true,
        krylovdim = krylovdim, tol = tol, maxiter = maxiter)
    length(vals) < N && error("Krylov method fails. Cannot find $N eigenvectors.")
    stats = (dim = dim, nnz = nnzH, backend = :sparse, build_s = t_build, solve_s = time() - t1,
             numops = info.numops, numiter = info.numiter, maxres = maximum(info.normres[1:N]),
             converged = info.converged, host_bytes = host_bytes)
    return real.(vals[1:N]), [MBS64Vector(vecs[i], subspace) for i in 1:min(keep, N)], stats
end

function solve_ed_spectrum(
    subspaces::AbstractVector,
    sector_momenta::AbstractVector,
    scatter_list,
    Gk::NTuple{2,<:Integer};
    Neigen::Int,
    method::Symbol = :sparse,
    mode = :full_ed,
    lattice::Symbol = :triangular,
    include_reflections::Bool = true,
    ed::Union{Nothing,EDSettings} = nothing,
    stats::Union{Nothing,EDStats} = nothing,
)
    ed === nothing && (ed = legacy_settings(Neigen, method))
    Neigen = ed.nlevels
    method = ed.backend
    plan = ed_sector_plan(
        sector_momenta,
        Gk;
        mode = mode,
        lattice = lattice,
        include_reflections = include_reflections,
    )
    energies = Vector{Vector{Float64}}(undef, length(subspaces))
    vectors = Vector{Any}(undef, length(subspaces))
    fill!(vectors, nothing)

    gpu_res = nothing
    if method == :gpu
        jobs = Tuple{Int,Any}[(i, :zero) for i in plan.solve_indices if length(subspaces[i]) > 0]
        gpu_res = gpu_solve_batch(jobs, subspaces, _ -> scatter_list, get_bits(first(subspaces));
                                  Neigen = Neigen, keep = ed.keep, krylov_kw(ed)...)
    end
    for i in plan.solve_indices
        N_block = min(Neigen, length(subspaces[i]))
        if N_block == 0
            energies[i] = Float64[]
            vectors[i] = Any[]
            continue
        end
        vals, vecs, st = gpu_res !== nothing ? gpu_res[(i, :zero)] :
            cpu_solve(ed, subspaces[i], scatter_list; N = N_block, keep = ed.keep)
        stats === nothing || record!(stats, st, N_block)
        energies[i] = real.(vals)
        vectors[i] = vecs
    end

    for i in eachindex(subspaces)
        representative = plan.representative_index[i]
        i == representative && continue
        length(subspaces[i]) == length(subspaces[representative]) || error(
            "symmetry-related sectors have different dimensions: " *
            "$(sector_momenta[i]) => $(length(subspaces[i])), " *
            "$(sector_momenta[representative]) => $(length(subspaces[representative]))"
        )
        energies[i] = copy(energies[representative])
    end
    return energies, vectors, plan
end

# ---------------------------------------------------------------------------
# Main solve entrypoint
# ---------------------------------------------------------------------------

"""Copy of `K` with an empty coefficient cache (the cache is not thread-safe)."""
fresh_cache(K::DeformationKernel) = DeformationKernel(
    (getfield(K, f) for f in fieldnames(DeformationKernel)[1:end - 1])...,
    Dict{NTuple{4,Float64},Vector{ComplexF64}}(),
)

"""
    twisted_scatter_lists(h2, k_list, Gk, twists) -> Dict(twist => scatter list)

Builds the scatter lists of several twists concurrently. Each task gets its own
form-factor object (and deformation kernel) with empty caches, because the
memo dictionaries are not thread-safe; values are the same function results,
so each list is identical to a serial `ED_scatterlist_twobody` build.
"""
function twisted_scatter_lists(h2::TrialBandH2, k_list::Matrix{Int}, Gk, twists::AbstractVector)
    built = Vector{Any}(undef, length(twists))
    Threads.@threads :dynamic for t in eachindex(twists)
        tff = h2.tff
        kernel = tff.kernel === nothing ? nothing : fresh_cache(tff.kernel)
        tff_t = TrialFormFactor(tff.glist, tff.w, tff.lattice, tff.level_mix; reg = tff.reg, kernel = kernel)
        h2_t = TrialBandH2(tff_t, h2.lattice, h2.Gk, h2.qlist, h2.qmax, h2.W0, h2.d_l, h2.D_l)
        built[t] = ED_scatterlist_twobody(EDPara(; k_list = k_list, Gk = Gk, H_two = h2_t); kshift = twists[t])
    end
    return Dict{Any,Any}(zip(twists, built))
end

"""
    ground_manifold_size(filling) -> Int

Torus ground-state degeneracy of the FCI at `ν = p/q`: `q`. It was
`round(1/ν)`, which agrees for `ν = 1/q` but gives 2 at `ν = 2/3`, where the
particle–hole conjugate of the Laughlin state has 3.
"""
function ground_manifold_size(filling::Real)::Int
    ν = rationalize(Int, Float64(filling); tol = 1e-9)
    return denominator(ν)
end

function solve(ed_input_raw; t_start::Float64)
    config_hash = String(ed_input_raw[:config_hash])
    energy_unit = String(get(ed_input_raw, :energy_unit, "meV"))
    n_k_field = Int(ed_input_raw[:lattice][:n_k])

    a_n = decode_a_n(ed_input_raw[:wavefunction])
    glist, w_G = decode_W_G(ed_input_raw[:form_factor])
    if isempty(a_n)
        return logical_failure_output(
            "empty_a_n", "wavefunction.a_n is empty";
            config_hash = config_hash, n_k = n_k_field, energy_unit = energy_unit,
            solver_version = SOLVER_VERSION, compute_seconds = time() - t_start,
        )
    end
    if isempty(glist)
        return logical_failure_output(
            "empty_W_G", "form_factor.W_G is empty";
            config_hash = config_hash, n_k = n_k_field, energy_unit = energy_unit,
            solver_version = SOLVER_VERSION, compute_seconds = time() - t_start,
        )
    end

    solver_params = ed_input_raw[:ed_solver_params]
    filling_raw = get(solver_params, :filling, nothing)
    filling = filling_raw === nothing ? 1 / 3 : Float64(filling_raw)
    extra_raw = get(solver_params, :extra, Dict{String,Any}())
    extra = Dict{String,Any}(string(k) => v for (k, v) in pairs(extra_raw))

    lattice_symbol = lattice_symbol_from_extra(extra)
    lattice = lattice_from_extra(extra)
    k_list, Gk = build_kmesh(extra, n_k_field)
    Nk = size(k_list, 2)

    if !(0 < filling < 1)
        return logical_failure_output(
            "filling_out_of_range", "ed_solver_params.filling must be in (0,1)";
            config_hash = config_hash, n_k = n_k_field, energy_unit = energy_unit,
            solver_version = SOLVER_VERSION, compute_seconds = time() - t_start,
        )
    end
    Ne_raw = Nk * filling
    Ne = round(Int, Ne_raw)
    if abs(Ne - Ne_raw) > 1e-9
        return logical_failure_output(
            "filling_incommensurate",
            "Nk=$(Nk) × filling=$(filling) is not an integer (got $(Ne_raw))";
            config_hash = config_hash, n_k = n_k_field, energy_unit = energy_unit,
            solver_version = SOLVER_VERSION, compute_seconds = time() - t_start,
        )
    end
    # Expected ground-manifold size: the torus degeneracy at ν = p/q unless the
    # task says otherwise (e.g. Moore–Read: 6).
    m_degeneracy = haskey(extra, "gs_degeneracy") ? Int(extra["gs_degeneracy"]) : ground_manifold_size(filling)

    # Level-mix weights `t_n = |a_n|²`
    # (real, non-negative, Σt_n = 1 since `a_n` is gauge-fixed upstream).
    level_mix = [(abs2(a_n[n + 1]), n) for n in 0:length(a_n) - 1]

    chern_target = Int(get(extra, "chern", 1))
    if abs(chern_target) != 1
        return logical_failure_output(
            "chern_target_invalid", "extra.chern must be ±1; got $(chern_target)";
            config_hash = config_hash, n_k = n_k_field, energy_unit = energy_unit,
            solver_version = SOLVER_VERSION, compute_seconds = time() - t_start,
        )
    end

    reg = Float64(get(extra, "ll_orth_reg", 0.0))
    # An optional `form_factor.deformation` block turns the seed into
    # a k-dependent kernel. Absent (or null) ⇒ the static path, byte-identical.
    deformation = get(ed_input_raw[:form_factor], :deformation, nothing)
    kernel = nothing
    if deformation !== nothing
        kernel = try
            DeformationKernel(deformation, glist, w_G, lattice)
        catch e
            e isa ArgumentError || rethrow()
            return logical_failure_output(
                "deformation_invalid", e.msg;
                config_hash = config_hash, n_k = n_k_field, energy_unit = energy_unit,
                solver_version = SOLVER_VERSION, compute_seconds = time() - t_start,
            )
        end
        # the kernel's G-list (its box) replaces the seed list; the seed sits inside it
        glist = kernel.glist
        w_G = kernel.seed_w
        @info "k-dependent kernel" n_params = 2 * length(kernel.spatial_stars) * length(kernel.momentum_stars) n_mesh = kernel.n_mesh g_cutoff = kernel.g_cutoff n_G = length(glist) static = is_zero(kernel)
    end
    tff = TrialFormFactor(glist, w_G, lattice, level_mix; reg = reg, kernel = kernel)

    qmax = Int(get(extra, "qmax", 6))
    qlist = build_qgrid(qmax)
    W0_int = Float64(get(extra, "W0", 1.0))
    d_l = Float64(get(extra, "d_l", 0.0))
    D_l = Float64(get(extra, "D_l", 10.0))

    h2 = TrialBandH2(tff, lattice, Gk, qlist, qmax, W0_int, d_l, D_l)
    para = EDPara(; k_list = k_list, Gk = Gk, H_two = h2)

    sector_mode = normalize_ed_sector_mode(
        get(extra, "ed_mode", get(extra, "sector_mode", "full_ed"))
    )
    include_reflections = Bool(get(extra, "include_reflections", true))

    phases = Dict{String,Float64}()
    function phase!(name, t0; kw...)
        phases[name] = time() - t0
        @info "phase" name seconds = phases[name] kw...
        return time()
    end
    t_phase = time()
    subspaces, ss_k = momentum_subspaces(k_list, Gk, Ne)   # == ED_momentum_subspaces (test_formfactor_fast.jl)
    max_dim = maximum(length, subspaces)
    ed = ed_settings(extra, m_degeneracy, max_dim)
    Neigen = ed.nlevels
    method = ed.backend
    stats = EDStats()
    @info "ED settings" accuracy = ed.accuracy backend = ed.backend reason = ed.backend_reason nlevels = ed.nlevels twist_margin = ed.twist_margin krylovdim = ed.krylovdim tol = ed.tol keep = ed.keep max_dim m_degeneracy
    t_phase = phase!("subspaces", t_phase; threads = Threads.nthreads(), max_dim)
    scat = ED_scatterlist_twobody(para)
    t_phase = phase!("scatter_list", t_phase; n_terms = length(scat))
    energies, vectors, sector_plan = solve_ed_spectrum(
        subspaces,
        ss_k,
        scat,
        Gk;
        Neigen = Neigen,
        method = method,
        ed = ed,
        stats = stats,
        mode = sector_mode,
        lattice = lattice_symbol,
        include_reflections = include_reflections,
    )
    t_phase = phase!("sector_spectrum", t_phase)
    @info "ED sector plan" mode = sector_plan.sector_mode total_sectors = length(subspaces) solved_sectors = length(sector_plan.solve_indices) symmetry_operations = sector_plan.operation_count

    gap_mb, e_top_gs, e_first_excited, gs_block_idxs =
        compute_mb_gap(energies, m_degeneracy)
    # Keep the sector-resolved low-energy spectrum (the
    # `neigen_per_block` lowest eigenvalues per momentum sector) and the
    # ground-manifold splitting δ_GS = E_m − E_1, so that a gap is never
    # quoted without the manifold it was measured against.
    low_energies = [copy(e) for e in energies]
    sector_momenta = [[Int(ss_k[i][1]), Int(ss_k[i][2])] for i in eachindex(energies)]
    all_energies = sort!(reduce(vcat, energies; init = Float64[]))
    gs_splitting = all_energies[m_degeneracy] - all_energies[1]

    pes_result = nothing
    pes_settings = get(extra,"pes",nothing)
    if pes_settings !== nothing && pes_settings !== false
        try
            pes_settings isa AbstractDict || throw(ArgumentError("extra.pes must be an object or null/false."))
            pes_result = pes_from_ed_spectrum(para,subspaces,ss_k,energies,vectors,scat,ed,
                Dict(string(k)=>v for (k,v) in pairs(pes_settings)),m_degeneracy; stats)
        catch e
            e isa ArgumentError || e isa DimensionMismatch || rethrow()
            return logical_failure_output("pes_invalid",sprint(showerror,e);
                config_hash, n_k=n_k_field, energy_unit, solver_version=SOLVER_VERSION,
                compute_seconds=time()-t_start, gap_top_indirect_solver=gap_mb,
                low_energies, sector_momenta, gs_manifold_splitting=gs_splitting,
                ed_backend=String(method), ed_solver_stats=solver_stats(ed,stats,phases,gap_mb))
        end
        t_phase = phase!("pes",t_phase)
    end

    # Mesh-screening gate: the Wilson-loop Chern algorithm assumes the
    # m_degeneracy GS states live in m_degeneracy distinct momentum
    # sectors (standard Laughlin torus quantisation). When they cluster
    # in fewer sectors — known case: 3×6 at ν=1/3 — the per-state loop
    # integrates intra-subspace gauge ambiguity, not topology. Short-
    # circuit before the Wilson loop fires; preserve the (still valid)
    # many-body gap on the failed_logical output for diagnostics.
    if length(gs_block_idxs) != m_degeneracy
        return logical_failure_output(
            "mesh_unsuitable_for_chern",
            "Laughlin GS manifold (m=$(m_degeneracy)) clusters in " *
            "$(length(gs_block_idxs)) distinct momentum sector(s) " *
            "(blocks=$(gs_block_idxs)); Wilson-loop Chern requires " *
            "m=$(m_degeneracy) distinct sectors. Pick a different (nk1,nk2).";
            config_hash = config_hash, n_k = n_k_field, energy_unit = energy_unit,
            solver_version = SOLVER_VERSION, compute_seconds = time() - t_start,
            gap_top_indirect_solver = gap_mb, low_energies = low_energies,
            sector_momenta = sector_momenta, gs_manifold_splitting = gs_splitting,
            ed_backend = String(method), ed_solver_stats = solver_stats(ed, stats, phases, gap_mb),
            pes = pes_result,
        )
    end

    # Expanded spectra do not manufacture eigenvectors in copied sectors.
    # The Wilson loop needs the actual zero-twist ground vector in each of
    # its sectors, so solve only those missing blocks before the Chern step.
    missing_res = nothing
    if method == :gpu
        jobs = Tuple{Int,Any}[(b, :zero) for b in gs_block_idxs if vectors[b] === nothing]
        missing_res = gpu_solve_batch(jobs, subspaces, _ -> scat, get_bits(first(subspaces));
                                      Neigen = Neigen, keep = ed.keep, krylov_kw(ed)...)
    end
    for block_idx in gs_block_idxs
        vectors[block_idx] === nothing || continue
        N_block = min(Neigen, length(subspaces[block_idx]))
        vals, vecs, mst = missing_res !== nothing ? missing_res[(block_idx, :zero)] :
            cpu_solve(ed, subspaces[block_idx], scat; N = N_block, keep = ed.keep)
        record!(stats, mst, N_block)
        actual = real.(vals)
        isapprox(actual, energies[block_idx]; atol = 1e-8, rtol = 1e-8) || error(
            "symmetry-reduced spectrum disagrees with explicit ground-sector solve " *
            "at momentum $(ss_k[block_idx])"
        )
        vectors[block_idx] = vecs
    end
    # Only the ground-manifold sectors' vectors are used from here on; at 5×6
    # the others are ~16 MB each per kept level.
    for i in eachindex(vectors)
        i in gs_block_idxs || (vectors[i] = nothing)
    end

    # --- Origin-plaquette diagnostic (the estimator before the glued lattice).
    # Kept for continuity of `chern_quantization_error_solver`, which is now a
    # curvature-uniformity residual, NOT a gate. Costs 3 twisted re-solves per
    # state; `wilson_plaquette_diagnostic: false` skips it and leaves the field
    # null.
    N_kshift = Int(get(extra, "wilson_N_kshift", 10))
    glued_N = Int(get(extra, "chern_glued_N", 2))
    # Not a gate since the glued-lattice estimator took over, and read by
    # nothing downstream; search mode skips it by default (half of the Chern
    # re-solves), confirm keeps it.
    do_plaquette = Bool(get(extra, "wilson_plaquette_diagnostic", ed.accuracy == :confirm))
    # GPU: every twisted re-solve of both Chern estimators is independent of
    # the others, so run them as one batch spread over the devices; the
    # estimators then read their vectors from `presolved` instead of solving.
    presolved = Dict{Any,Any}()
    t_phase = time()
    if method == :gpu
        picks = lowest_states(energies, m_degeneracy)
        jobs = Tuple{Int,Any}[]
        if do_plaquette
            for (b, _) in picks, θ in plaquette_path(N_kshift)[2:end - 1]
                push!(jobs, (b, θ))
            end
        end
        for j in 0:glued_N - 1, i in 0:glued_N - 1, (b, _) in picks
            (i, j) == (0, 0) || push!(jobs, (b, (i // glued_N, j // glued_N)))
        end
        unique!(jobs)
        # each sector's re-solve needs levels up to the deepest tracked state in it
        levels_for = Dict{Int,Int}()
        for (b, st) in picks
            levels_for[b] = max(get(levels_for, b, 0), twist_levels(ed, st))
        end
        twist_scats = twisted_scatter_lists(h2, k_list, Gk, unique(θ for (_, θ) in jobs))
        scat_for(θ) = twist_scats[θ]
        presolved = gpu_solve_batch(jobs, subspaces, scat_for, get_bits(first(subspaces));
                                    Neigen = Neigen, N_for = job -> levels_for[job[1]],
                                    keep = typemax(Int), krylov_kw(ed)...)
        for (job, r) in presolved
            record!(stats, r[3], min(levels_for[job[1]], length(subspaces[job[1]])))
        end
        t_phase = phase!("chern_twist_solves", t_phase; n_solves = length(jobs))
    end
    plaq_raw = nothing
    plaq_qerr = nothing
    if do_plaquette
        plaq_raw, plaq_qerr = many_body_chern_manifold(
            para, tff, subspaces, k_list, Gk,
            vectors, energies, m_degeneracy, level_mix;
            N_kshift = N_kshift, Neigen = Neigen, method = method, presolved = presolved,
            ed = ed, stats = stats,
        )
    end

    # --- Production estimator: glued one-period lattice, consistent
    # sewing. Gates: tracked manifold must be a spectral-flow orbit; every
    # plaquette phase below π/2 (principal branch with margin); residual to the
    # nearest integer below `chern_glued_threshold`. Measured residuals are
    # ~1e-14; the default 1e-6 leaves headroom for the
    # eigensolver tolerance while admitting no real non-integer.
    glued_thresh = Float64(get(extra, "chern_glued_threshold", 1e-6))
    phase_thresh = Float64(get(extra, "chern_plaquette_phase_threshold", pi / 2))
    diag = Dict{Symbol,Any}(
        :chern_quantization_error_solver => plaq_qerr,
        :chern_plaquette_raw => plaq_raw,
        :chern_glued_N => glued_N,
        :gap_top_indirect_solver => gap_mb,
        :low_energies => low_energies,
        :sector_momenta => sector_momenta,
        :gs_manifold_splitting => gs_splitting,
        :ed_backend => String(method),
    )
    t_phase = phase!("plaquette_chern", t_phase)
    pes_result === nothing || (diag[:pes] = pes_result)
    glued = try
        glued_lattice_chern(
            para, tff, subspaces, ss_k, k_list, Gk, Ne,
            vectors, energies, m_degeneracy, level_mix;
            N = glued_N, Neigen = Neigen, method = method, presolved = presolved,
            ed = ed, stats = stats,
        )
    catch e
        e isa GluedChernError || rethrow()
        return logical_failure_output(
            e.reason, e.msg;
            config_hash = config_hash, n_k = n_k_field, energy_unit = energy_unit,
            solver_version = SOLVER_VERSION, compute_seconds = time() - t_start,
            diag..., ed_solver_stats = solver_stats(ed, stats, phases, gap_mb),
        )
    end
    t_phase = phase!("glued_chern", t_phase)
    diag[:ed_solver_stats] = solver_stats(ed, stats, phases, gap_mb)
    kernel !== nothing && @info "kernel cache" momentum_pairs = length(kernel.cache)
    diag[:chern_glued_raw] = glued.C
    diag[:chern_glued_residual] = glued.residual
    diag[:chern_max_plaquette_phase] = glued.max_abs_phase
    diag[:chern_glued_closure] = glued.closure
    diag[:chern_glued_per_state] = glued.per_state
    # Glued-estimator sign convention: report −C_consistent so LL0-based history keeps +1.
    chern_int = -round(Int, glued.C)

    if glued.max_abs_phase > phase_thresh
        return logical_failure_output(
            "chern_plaquette_phase_too_large",
            "glued-lattice plaquette phase $(glued.max_abs_phase) exceeds $(phase_thresh): " *
            "curvature not resolved at N=$(glued_N); no well-defined Chern number at this size";
            config_hash = config_hash, n_k = n_k_field, energy_unit = energy_unit,
            solver_version = SOLVER_VERSION, compute_seconds = time() - t_start,
            chern_solver = chern_int, diag...,
        )
    end
    if glued.residual > glued_thresh
        return logical_failure_output(
            "chern_glued_not_quantized",
            "glued-lattice Chern not integer: raw=$(glued.C), residual=$(glued.residual)";
            config_hash = config_hash, n_k = n_k_field, energy_unit = energy_unit,
            solver_version = SOLVER_VERSION, compute_seconds = time() - t_start,
            chern_solver = chern_int, diag...,
        )
    end

    result = Dict{Symbol,Any}(
        :schema_version => SCHEMA_VERSION,
        :config_hash => config_hash,
        :status => "completed",
        :failure_reason => nothing,
        :energy_unit => energy_unit,
        :n_k => n_k_field,
        :target_band_index => nothing,
        :epsilon_target => nothing,
        :epsilon_above => nothing,
        :epsilon_below => nothing,
        :u_k => nothing,
        :chern_solver => chern_int,
        :chern_quantization_error_solver => plaq_qerr,
        :chern_plaquette_raw => plaq_raw,
        :chern_glued_raw => glued.C,
        :chern_glued_residual => glued.residual,
        :chern_glued_per_state => glued.per_state,
        :chern_max_plaquette_phase => glued.max_abs_phase,
        :chern_glued_closure => glued.closure,
        :chern_glued_N => glued_N,
        :gap_top_indirect_solver => gap_mb,
        :low_energies => low_energies,
        :sector_momenta => sector_momenta,
        :gs_manifold_splitting => gs_splitting,
        :ed_backend => String(method),
        :ed_solver_stats => diag[:ed_solver_stats],
        :compute_seconds => time() - t_start,
        :solver_version => SOLVER_VERSION,
        :solver_log_path => nothing,
    )
    pes_result === nothing || (result[:pes] = pes_result)
    return result
end

# ---------------------------------------------------------------------------
# Failure-output constructors
# ---------------------------------------------------------------------------

function failure_output(
    status::String, reason::String, msg::String;
    config_hash::String, n_k::Int, energy_unit::String,
    solver_version::String, compute_seconds::Float64,
    chern_solver = nothing,
    chern_quantization_error_solver = nothing,
    gap_top_indirect_solver = nothing,
    chern_plaquette_raw = nothing,
    chern_glued_raw = nothing,
    chern_glued_residual = nothing,
    chern_glued_per_state = nothing,
    chern_max_plaquette_phase = nothing,
    chern_glued_closure = nothing,
    chern_glued_N = nothing,
    low_energies = nothing,
    sector_momenta = nothing,
    gs_manifold_splitting = nothing,
    ed_backend = nothing,
    ed_solver_stats = nothing,
    pes = nothing,
)
    @info "ED failure" status reason msg
    result = Dict{Symbol,Any}(
        :schema_version => SCHEMA_VERSION,
        :config_hash => config_hash,
        :status => status,
        :failure_reason => reason,
        :energy_unit => energy_unit,
        :n_k => n_k,
        :target_band_index => nothing,
        :epsilon_target => nothing,
        :epsilon_above => nothing,
        :epsilon_below => nothing,
        :u_k => nothing,
        :chern_solver => chern_solver,
        :chern_quantization_error_solver => chern_quantization_error_solver,
        :chern_plaquette_raw => chern_plaquette_raw,
        :chern_glued_raw => chern_glued_raw,
        :chern_glued_residual => chern_glued_residual,
        :chern_glued_per_state => chern_glued_per_state,
        :chern_max_plaquette_phase => chern_max_plaquette_phase,
        :chern_glued_closure => chern_glued_closure,
        :chern_glued_N => chern_glued_N,
        :gap_top_indirect_solver => gap_top_indirect_solver,
        :low_energies => low_energies,
        :sector_momenta => sector_momenta,
        :gs_manifold_splitting => gs_manifold_splitting,
        :ed_backend => ed_backend,
        :ed_solver_stats => ed_solver_stats,
        :compute_seconds => compute_seconds,
        :solver_version => solver_version,
        :solver_log_path => nothing,
    )
    pes === nothing || (result[:pes] = pes)
    return result
end

logical_failure_output(reason::String, msg::String; kw...) =
    failure_output("failed_logical", reason, msg; kw...)

transient_failure_output(reason::String, msg::String; kw...) =
    failure_output("failed_transient", reason, msg; kw...)

function classify_exception(e)
    if isa(e, OutOfMemoryError)
        return :transient, "oom"
    elseif isa(e, InterruptException)
        return :transient, "interrupted"
    else
        return :transient, "exception:$(typeof(e))"
    end
end

end # module
