@testset "symmetry-reduced ED sector plan" begin
    k_list, Gk = build_symmetric_kmesh(12)
    sectors = [(k_list[1, i], k_list[2, i]) for i in axes(k_list, 2)]

    full = ed_sector_plan(sectors, Gk; mode = :full_ed)
    reduced = ed_sector_plan(
        sectors,
        Gk;
        mode = :symmetry_reduced_ed,
        lattice = :triangular,
        include_reflections = true,
    )
    @test full.solve_indices == collect(1:12)
    @test length(reduced.solve_indices) == 4
    @test sort(reduce(vcat, reduced.orbits)) == collect(1:12)
    @test all(i -> reduced.representative_index[i] in reduced.solve_indices, 1:12)

    rotations_only = ed_sector_plan(
        sectors,
        Gk;
        mode = :symmetry_reduced_ed,
        lattice = :triangular,
        include_reflections = false,
    )
    @test length(rotations_only.solve_indices) >= length(reduced.solve_indices)
    @test sort(reduce(vcat, rotations_only.orbits)) == collect(1:12)

    @test normalize_ed_sector_mode("symmetry_reduced_ed") === :symmetry_reduced_ed
    @test normalize_ed_sector_mode(:full) === :full_ed
    @test_throws ArgumentError normalize_ed_sector_mode("bad_mode")
end
