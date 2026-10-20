# Acceptance: the glued one-period lattice with the consistent
# sewing returns an exact integer on the trivial 3x4 band, reported with the
# historical sign, and its diagnostics are populated.
using JSON3

@testset "glued-lattice Chern on the trivial 3x4 band" begin
    raw = JSON3.read(read(joinpath(@__DIR__, "data", "nk12_trivial.json"), String))
    out = MoireSolver.solve(raw; t_start = time())
    @test out[:status] == "completed"
    @test out[:chern_solver] == 1                      # −round(C_consistent)
    @test abs(out[:chern_glued_raw] + 1) < 1e-8        # consistent sewing gives −1
    @test out[:chern_glued_residual] < 1e-8
    @test out[:chern_glued_closure] < 1e-8
    @test out[:chern_max_plaquette_phase] < pi / 2
    @test out[:chern_glued_N] == 2
    @test length(out[:chern_glued_per_state]) == 3
    @test out[:chern_quantization_error_solver] < 1e-6  # plaquette diagnostic still reported
    @test out[:solver_version] == MoireSolver.SOLVER_VERSION
end

# ---------------------------------------------------------------------------
# Glued-Chern failure gates — synthetic triggers. No archive configuration trips
# these under the corrected metric, so each gate is
# exercised here on purpose: the two threshold gates through the real solve
# path with the thresholds set below the trivial band's values, the two
# structural gates at the helper level with constructed inputs.
# ---------------------------------------------------------------------------

function trivial_input_with_extra(pairs::String; fixture::String = "nk12_trivial.json")
    s = read(joinpath(@__DIR__, "data", fixture), String)
    occursin("\"extra\": {", s) || error("test fixture changed shape")
    # skip the plaquette diagnostic: it is not under test and costs 9 re-solves
    return JSON3.read(replace(s, "\"extra\": {" => "\"extra\": {$(pairs) \"wilson_plaquette_diagnostic\": false, "))
end

@testset "Glued-lattice Chern gate: plaquette phase" begin
    # trivial band: max|φ_p| = 0.524 at N = 2; a 0.1 threshold must reject it
    out = MoireSolver.solve(trivial_input_with_extra("\"chern_plaquette_phase_threshold\": 0.1,"); t_start = time())
    @test out[:status] == "failed_logical"
    @test out[:failure_reason] == "chern_plaquette_phase_too_large"
    @test out[:chern_solver] == 1                     # the integer is still reported
    @test out[:chern_max_plaquette_phase] > 0.1
    @test out[:gap_top_indirect_solver] > 0           # gap preserved on the failed output
    @test out[:chern_quantization_error_solver] === nothing   # diagnostic skipped as asked
end

@testset "Glued-lattice Chern gate: residual" begin
    # No fixture has a genuinely non-integer glued Chern number: the trivial
    # band's residual is exactly 0 and the archive reference's is round-off,
    # so a zero threshold cannot be relied on to fire.
    # A negative threshold makes the comparison `residual > threshold` true
    # for any residual and exercises the gate's failure output mechanically;
    # the measured residual is asserted to be round-off in the same breath.
    out = MoireSolver.solve(
        trivial_input_with_extra("\"chern_glued_threshold\": -1.0,"; fixture = "nk12_12cdff_ll012.json");
        t_start = time())
    @test out[:status] == "failed_logical"
    @test out[:failure_reason] == "chern_glued_not_quantized"
    @test out[:chern_glued_residual] >= 0.0
    @test out[:chern_glued_residual] < 1e-12            # round-off, not physics
    @test abs(out[:chern_glued_raw] + 1) < 1e-8
    @test out[:chern_solver] == 1
    @test out[:gap_top_indirect_solver] > 0.1           # 0.104167 under the corrected metric
end

@testset "Glued-lattice Chern gate: tilted cluster without the unit steps (solve path)" begin
    # The 12-point symmetric cluster (Gk = (6,6)) contains neither e_1 nor e_2,
    # so the glued lattice cannot be built on it. Whichever structural check
    # meets it first — the sector permutation (K + Ne·e_d not a tracked sector)
    # or the orbital relabelling (k + e_d not on the cluster) — the solve must
    # end as a logical failure carrying that reason, with the gap preserved.
    out = MoireSolver.solve(trivial_input_with_extra("\"symcluster\": 1,"); t_start = time())
    @test out[:status] == "failed_logical"
    @test out[:failure_reason] in ("chern_manifold_not_spectral_flow_orbit", "mesh_unsuitable_for_glued_chern")
    @test out[:gap_top_indirect_solver] > 0
    @test out[:chern_solver] === nothing               # no integer is claimed
    @info "tilted-cluster gate fired" reason = out[:failure_reason]
end

@testset "Glued-lattice Chern gate: tracked manifold not a spectral-flow orbit" begin
    # 3x4, Ne = 4: sector (0,0) flows to (0,0)+4·e_1 = (1,0) (mod 3), which is
    # not among the tracked sectors below → the permutation does not close.
    ss_k = [(0, 0), (0, 2), (0, 3)]
    picks = [(1, 1), (2, 1), (3, 1)]
    err = try
        MoireSolver.sector_permutation(ss_k, picks, (3, 4), 4, 1); nothing
    catch e
        e
    end
    @test err isa MoireSolver.GluedChernError
    @test err.reason == "chern_manifold_not_spectral_flow_orbit"
    # and a manifold that does close (the Laughlin orbit along direction 2:
    # (0,0) → (0,4 mod 4) = (0,0)) permutes to itself
    ss_ok = [(0, 0), (1, 0), (2, 0)]
    perm = MoireSolver.sector_permutation(ss_ok, picks, (3, 4), 4, 2)
    @test perm == [1, 2, 3]
end

@testset "Glued-lattice Chern gate: cluster without the unit steps" begin
    # a point table missing (1,0): stepping orbital 1 along direction 1 has
    # nowhere to go
    k_list = [0 0 2; 0 1 0]                      # points (0,0), (0,1), (2,0)
    index = Dict((k_list[1, i], k_list[2, i]) => i for i in 1:3)
    err = try
        MoireSolver.relabel_orbital(index, k_list, (3, 4), 1, 1); nothing
    catch e
        e
    end
    @test err isa MoireSolver.GluedChernError
    @test err.reason == "mesh_unsuitable_for_glued_chern"
    # the same table does contain (0,1): stepping along direction 2 works and
    # does not wrap
    j, wrapped = MoireSolver.relabel_orbital(index, k_list, (3, 4), 1, 2)
    @test j == 2 && wrapped == false
    # wrapping is flagged at the zone edge: (2,0) + e_1 = (0,0) with wrap
    j, wrapped = MoireSolver.relabel_orbital(index, k_list, (3, 4), 3, 1)
    @test j == 1 && wrapped == true
end
