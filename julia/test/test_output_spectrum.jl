# The solver saves the sector-resolved low-energy spectrum and
# the ground-manifold splitting alongside the gap, and they are consistent with it.
using JSON3

@testset "output spectrum: low_energies / sector_momenta / gs_manifold_splitting" begin
    s = read(joinpath(@__DIR__, "data", "nk12_trivial.json"), String)
    s = replace(s, "\"extra\": {" => "\"extra\": {\"wilson_plaquette_diagnostic\": false, ")
    out = MoireSolver.solve(JSON3.read(s); t_start = time())
    @test out[:status] == "completed"
    E = out[:low_energies]
    K = out[:sector_momenta]
    @test length(E) == length(K) == 12
    @test all(length(k) == 2 for k in K)
    @test length(unique(K)) == 12                      # one entry per momentum sector
    flat = sort(reduce(vcat, E))
    @test abs((flat[4] - flat[3]) - out[:gap_top_indirect_solver]) < 1e-12   # ν = 1/3: Δ = E_4 − E_3
    @test abs((flat[3] - flat[1]) - out[:gs_manifold_splitting]) < 1e-12     # δ_GS = E_3 − E_1
    @test out[:gs_manifold_splitting] >= 0
    @test out[:solver_version] == "moire-julia-ed@v0.9.1"
end
