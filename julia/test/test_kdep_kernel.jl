# Acceptance: the solver's k-dependent kernel reproduces the Python
# reference (src/mosaic/physics/kdep_envelope.py) to round-off, obeys the ordered-pair
# Hermiticity, collapses to the seed at γ = 0, and runs end to end.
using JSON3
using LinearAlgebra

const FIX = JSON3.read(read(joinpath(@__DIR__, "data", "kdep_kernel_fixture.json"), String))

function fixture_seed()
    glist = Tuple{Int,Int}[]; w = ComplexF64[]
    for e in FIX[:seed_W_G]
        push!(glist, (Int(e[:G_int][1]), Int(e[:G_int][2]))); push!(w, ComplexF64(e[:re], e[:im]))
    end
    return glist, w
end

# the fixture's momenta are fractional BZ coordinates; the solver takes Cartesian
cartk(lat, f) = (Float64(f[1]) * real(lat.G1) + Float64(f[2]) * real(lat.G2),
                 Float64(f[1]) * imag(lat.G1) + Float64(f[2]) * imag(lat.G2))

@testset "k-dependent kernel: matches the Python builder to round-off" begin
    lat = MoireSolver.lattice_from_extra(Dict{String,Any}())
    glist, w = fixture_seed()
    K = MoireSolver.DeformationKernel(FIX[:deformation], glist, w, lat)
    @test K.g_cutoff == 3 && K.n_mesh == 24 && length(K.glist) == 49
    index = Dict(g => i for (i, g) in enumerate(K.glist))
    worst = 0.0
    for pr in FIX[:pairs]
        W = MoireSolver.kernel_coeffs!(K, cartk(lat, pr[:k_bra]), cartk(lat, pr[:k_ket]))
        for e in pr[:W]
            g = (Int(e[:G_int][1]), Int(e[:G_int][2]))
            worst = max(worst, abs(W[index[g]] - ComplexF64(e[:re], e[:im])))
        end
    end
    @test worst < 1e-12
    # the cache serves repeated pairs
    n_before = length(K.cache)
    MoireSolver.kernel_coeffs!(K, cartk(lat, FIX[:pairs][1][:k_bra]), cartk(lat, FIX[:pairs][1][:k_ket]))
    @test length(K.cache) == n_before
end

@testset "k-dependent kernel: ordered-pair Hermiticity, and γ = 0 is the seed" begin
    lat = MoireSolver.lattice_from_extra(Dict{String,Any}())
    glist, w = fixture_seed()
    K = MoireSolver.DeformationKernel(FIX[:deformation], glist, w, lat)
    index = Dict(g => i for (i, g) in enumerate(K.glist))
    ka = cartk(lat, (0.13, 0.41)); kb = cartk(lat, (0.72, -0.05))
    Wab = MoireSolver.kernel_coeffs!(K, ka, kb); Wba = MoireSolver.kernel_coeffs!(K, kb, ka)
    herm = maximum(abs(conj(Wab[index[(m, n)]]) - Wba[index[(-m, -n)]]) for (m, n) in K.glist)
    @test herm < 1e-12
    # the stronger same-ordered-pair relation is false
    same = maximum(abs(conj(Wab[index[(m, n)]]) - Wab[index[(-m, -n)]]) for (m, n) in K.glist)
    @test same > 1e-3
    # diagonal kernel is a real density: W_{-G}(k,k) = W_G(k,k)^*
    Waa = MoireSolver.kernel_coeffs!(K, ka, ka)
    @test maximum(abs(conj(Waa[index[(m, n)]]) - Waa[index[(-m, -n)]]) for (m, n) in K.glist) < 1e-12
    # γ = 0: the seed, exactly, at any pair
    zero_block = Dict(:spatial_stars => FIX[:deformation][:spatial_stars], :momentum_stars => FIX[:deformation][:momentum_stars],
                      :alpha => [[0.0]], :beta => [[0.0]], :n_mesh => 24, :g_cutoff => 3)
    K0 = MoireSolver.DeformationKernel(zero_block, glist, w, lat)
    W0 = MoireSolver.kernel_coeffs!(K0, ka, kb)
    seed = Dict(g => w[i] for (i, g) in enumerate(glist))
    @test maximum(abs(W0[index[g]] - get(seed, g, 0.0)) for g in K0.glist) == 0.0   # exact: the seed vector itself
    # the Python builder at γ = 0 with the fixture's cutoff agrees to round-off as well
    for e in FIX[:static_pair][:W]
        g = (Int(e[:G_int][1]), Int(e[:G_int][2]))
        @test abs(W0[index[g]] - ComplexF64(e[:re], e[:im])) < 1e-12
    end
end

function trivial_with_block(block_json::String)
    s = read(joinpath(@__DIR__, "data", "nk12_trivial.json"), String)
    s = replace(s, "\"symmetry\": \"C3_hard\"," => "\"symmetry\": \"C3_hard\", \"deformation\": $(block_json),")
    s = replace(s, "\"extra\": {" => "\"extra\": {\"wilson_plaquette_diagnostic\": false, ")
    return JSON3.read(s)
end
const STAR6 = "[[1,0],[-1,0],[0,1],[0,-1],[1,-1],[-1,1]]"

@testset "k-dependent solve path: zero block reproduces the static run; a deformation runs and keeps C" begin
    ref = MoireSolver.solve(trivial_with_block("null"); t_start = time())
    @test ref[:status] == "completed"
    zero = MoireSolver.solve(trivial_with_block("{\"spatial_stars\": [$(STAR6)], \"momentum_stars\": [$(STAR6)], \"alpha\": [[0.0]], \"beta\": [[0.0]], \"n_mesh\": 24, \"g_cutoff\": 1}"); t_start = time())
    @test zero[:status] == "completed"
    @test abs(zero[:gap_top_indirect_solver] - ref[:gap_top_indirect_solver]) < 1e-10
    @test zero[:chern_solver] == ref[:chern_solver] == 1
    # amplitude-only deformation: the diagonal density changes, the band stays a C = +1 FCI
    amp = MoireSolver.solve(trivial_with_block("{\"spatial_stars\": [$(STAR6)], \"momentum_stars\": [$(STAR6)], \"alpha\": [[0.3]], \"beta\": [[0.0]], \"n_mesh\": 24, \"g_cutoff\": 2}"); t_start = time())
    @test amp[:status] == "completed"
    @test amp[:chern_solver] == 1
    @test amp[:chern_glued_residual] < 1e-8
    @test abs(amp[:gap_top_indirect_solver] - ref[:gap_top_indirect_solver]) > 1e-9   # it did something
    @info "amplitude deformation" gap_static = ref[:gap_top_indirect_solver] gap_deformed = amp[:gap_top_indirect_solver]
    # phase-only deformation, small step: diagonal density unchanged, vertices move, C kept
    ph = MoireSolver.solve(trivial_with_block("{\"spatial_stars\": [$(STAR6)], \"momentum_stars\": [$(STAR6)], \"alpha\": [[0.0]], \"beta\": [[0.05]], \"n_mesh\": 24, \"g_cutoff\": 2}"); t_start = time())
    @test ph[:status] == "completed"
    @test ph[:chern_solver] == 1
    @test ph[:chern_glued_residual] < 1e-8
    @info "phase deformation (β = 0.05)" gap_deformed = ph[:gap_top_indirect_solver]
    # a large phase step (β = 0.3) closes the pure-LL0 gap at d_sc = 0.1 (the
    # baseline is a near-exact zero mode with gap 1.6e-4): the solver must report
    # the collapse as a logical failure, not a wrong integer
    big = MoireSolver.solve(trivial_with_block("{\"spatial_stars\": [$(STAR6)], \"momentum_stars\": [$(STAR6)], \"alpha\": [[0.0]], \"beta\": [[0.3]], \"n_mesh\": 24, \"g_cutoff\": 2}"); t_start = time())
    @test big[:status] == "failed_logical"
    @test big[:failure_reason] in ("mesh_unsuitable_for_chern", "chern_manifold_not_spectral_flow_orbit", "chern_plaquette_phase_too_large")
    @test big[:gap_top_indirect_solver] < 1e-8
    @test big[:chern_solver] === nothing
    @info "phase deformation (β = 0.3) closes the gap" reason = big[:failure_reason] gap = big[:gap_top_indirect_solver]
end

@testset "k-dependent solve path: operator Hermiticity of the deformed form factor" begin
    # λ_Q(k,k')^* = λ_{-Q}(k',k) must hold for the projected two-body operator to be Hermitian
    raw = trivial_with_block("{\"spatial_stars\": [$(STAR6)], \"momentum_stars\": [$(STAR6)], \"alpha\": [[0.2]], \"beta\": [[0.15]], \"n_mesh\": 24, \"g_cutoff\": 2}")
    glist, w = MoireSolver.decode_W_G(raw[:form_factor])
    lat = MoireSolver.lattice_from_extra(Dict{String,Any}())
    K = MoireSolver.DeformationKernel(raw[:form_factor][:deformation], glist, w, lat)
    tff = MoireSolver.TrialFormFactor(K.glist, K.seed_w, lat, [(1.0, 0)]; kernel = K)
    worst = 0.0
    for (fa, fb) in (((0.1, 0.2), (0.35, -0.15)), ((0.0, 0.0), (0.5, 0.5)), ((0.7, 0.9), (0.05, 0.4)))
        ka = cartk(lat, fa); kb = cartk(lat, fb)
        for Q in ((0, 0), (1, 0), (-1, 1), (2, -1))
            lhs = conj(MoireSolver.formfactor(tff, ka, kb, Q))
            rhs = MoireSolver.formfactor(tff, kb, ka, (-Q[1], -Q[2]))
            worst = max(worst, abs(lhs - rhs))
        end
    end
    @test worst < 1e-10
    # and the orthonormalised band has unit norm under the deformed metric (the q = 0 vertex Gram matrix carries over)
    ka = cartk(lat, (0.1, 0.2))
    @test abs(MoireSolver.formfactor(tff, ka, ka, (0, 0)) - 1) < 1e-12
end

@testset "k-dependent solve path: invalid block is a logical failure" begin
    bad = MoireSolver.solve(trivial_with_block("{\"spatial_stars\": [[[1,0],[0,1]]], \"momentum_stars\": [$(STAR6)], \"alpha\": [[0.1]], \"beta\": [[0.0]], \"n_mesh\": 24}"); t_start = time())
    @test bad[:status] == "failed_logical"
    @test bad[:failure_reason] == "deformation_invalid"
    zeromode = MoireSolver.solve(trivial_with_block("{\"spatial_stars\": [[[0,0]]], \"momentum_stars\": [$(STAR6)], \"alpha\": [[0.1]], \"beta\": [[0.0]], \"n_mesh\": 24}"); t_start = time())
    @test zeromode[:failure_reason] == "deformation_invalid"
end
