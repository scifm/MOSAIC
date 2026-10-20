# v0.8.1: the tracked ground manifold at ν = p/q has q states (torus degeneracy),
# so ν = 2/3 measures its gap above the third level, not inside the manifold.
using JSON3

@testset "ground_manifold_size = denominator of ν" begin
    @test MoireSolver.ground_manifold_size(1 / 3) == 3
    @test MoireSolver.ground_manifold_size(2 / 3) == 3
    @test MoireSolver.ground_manifold_size(1 / 2) == 2
    @test MoireSolver.ground_manifold_size(2 / 5) == 5
    @test MoireSolver.ground_manifold_size(0.25) == 4
end

@testset "ν = 2/3 solve: gap above the third state (nk12 trivial)" begin
    s = read(joinpath(@__DIR__, "data", "nk12_trivial.json"), String)
    raw = JSON3.read(s)
    d = JSON3.read(JSON3.write(raw), Dict{String,Any})
    d["ed_solver_params"]["filling"] = 2 / 3
    out = MoireSolver.solve(JSON3.read(JSON3.write(d)); t_start = time())
    @test out[:failure_reason] != "mesh_unsuitable_for_chern"
    flat = sort(reduce(vcat, out[:low_energies]))
    @test abs((flat[4] - flat[3]) - out[:gap_top_indirect_solver]) < 1e-12
    @test abs((flat[3] - flat[1]) - out[:gs_manifold_splitting]) < 1e-12
    @info "nu=2/3 nk12 trivial" status = out[:status] reason = out[:failure_reason] chern = out[:chern_solver] glued = get(out, :chern_glued_raw, nothing) gap = out[:gap_top_indirect_solver]
end
