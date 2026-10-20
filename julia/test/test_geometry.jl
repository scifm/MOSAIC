@testset "finite cluster geometry" begin
    expected = [7, 9, 12, 13, 14, 15, 18, 20, 21, 22, 24, 26, 27, 28, 36, 39]
    @test supported_symmetric_clusters() == expected

    for Nk in expected
        k_list, Gk = build_symmetric_kmesh(Nk)
        @test size(k_list) == (2, Nk)
        points = Set((k_list[1, i], k_list[2, i]) for i in axes(k_list, 2))
        @test length(points) == Nk
        @test (0, 0) in points

        # A valid finite cluster is an additive subgroup of the denominator grid.
        for left in points, right in points
            @test (mod(left[1] + right[1], Gk[1]),
                   mod(left[2] + right[2], Gk[2])) in points
        end
    end

    regular, periods = build_kmesh(Dict("nk1" => 3, "nk2" => 4), 12)
    @test periods == (3, 4)
    @test regular[:, 1] == [0, 0]
    @test regular[:, end] == [2, 3]

    symmetric, periods = build_kmesh(
        Dict("symcluster" => 1, "nk1" => 3, "nk2" => 4),
        12,
    )
    @test periods == (6, 6)
    @test symmetric != regular
    @test_throws ArgumentError build_symmetric_kmesh(8)
end
