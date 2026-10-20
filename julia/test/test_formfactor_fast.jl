# The hoisted raw_formfactor_matrix is entry-for-entry the
# per-element raw_formfactor_mn — bitwise, not approximately.
@testset "raw_formfactor_matrix == raw_formfactor_mn bitwise" begin
    lat = MoireSolver.ReciprocalLattice(1.0, -0.5)
    glist = [(m, n) for m in -3:3 for n in -3:3]
    w = [cis(0.3m - 0.7n) * exp(-0.1(m^2 + n^2)) for (m, n) in glist]
    nmax = 3
    for (kb, kk, G) in (((0.11, -0.4), (0.3, 0.25), (0, 0)), ((1.2, 0.7), (-0.6, 0.05), (2, -1)),
                        ((0.0, 0.0), (0.0, 0.0), (1, 1)))
        F = MoireSolver.raw_formfactor_matrix(kb, kk, G, nmax, glist, w, lat)
        @test all(F[m + 1, n + 1] === MoireSolver.raw_formfactor_mn(kb, kk, G, m, n, glist, w, lat)
                  for m in 0:nmax, n in 0:nmax)
    end
end

# step_inner_prod (threaded, allocation-free) == MomentumED.ED_step_inner_prod
@testset "step_inner_prod == ED_step_inner_prod" begin
    k_list, Gk = MoireSolver.build_kmesh(Dict{String,Any}("nk1" => 3, "nk2" => 4), 12)
    para = EDPara(; k_list = k_list, Gk = Gk, H_two = (args...) -> 0.0im)
    subs, _ = ED_momentum_subspaces(para, (4,); momentum_restriction = true,
        momentum_list = [(k_list[1, i], k_list[2, i]) for i in 1:12])
    sub = subs[1]
    ψf = MBS64Vector(randn(ComplexF64, length(sub)), sub)
    ψi = MBS64Vector(randn(ComplexF64, length(sub)), sub)
    orb = cis.(2π .* rand(12)) .* (0.9 .+ 0.1 .* rand(12))
    a = MoireSolver.step_inner_prod(ψf, ψi, orb)
    b = ED_step_inner_prod(ψf, ψi, orb)
    @test abs(a - b) <= 1e-13 * max(1.0, abs(b))
end

# momentum_subspaces (Gosper enumeration) == MomentumED.ED_momentum_subspaces
@testset "momentum_subspaces == ED_momentum_subspaces ($(nk1)x$(nk2), Ne=$Ne)" for (nk1, nk2, Ne) in
        ((3, 4, 4), (3, 6, 6), (4, 4, 8), (4, 6, 8), (3, 4, 0), (3, 4, 1), (3, 4, 2), (3, 4, 12))
    k_list, Gk = MoireSolver.build_kmesh(Dict{String,Any}("nk1" => nk1, "nk2" => nk2), nk1 * nk2)
    para = EDPara(; k_list = k_list, Gk = Gk, H_two = (args...) -> 0.0im)
    ref, ref_k = ED_momentum_subspaces(para, (Ne,); momentum_restriction = true,
        momentum_list = [(k_list[1, i], k_list[2, i]) for i in axes(k_list, 2)])
    new, new_k = MoireSolver.momentum_subspaces(k_list, Gk, Ne)
    @test new_k == ref_k
    @test length(new) == length(ref)
    @test all(a.list == b.list for (a, b) in zip(new, ref))
end
@testset "momentum_subspaces on the 27-site symmetric cluster" begin
    k_list, Gk = MoireSolver.build_kmesh(Dict{String,Any}("symcluster" => 1), 27)
    para = EDPara(; k_list = k_list, Gk = Gk, H_two = (args...) -> 0.0im)
    ref, ref_k = ED_momentum_subspaces(para, (4,); momentum_restriction = true,
        momentum_list = [(k_list[1, i], k_list[2, i]) for i in axes(k_list, 2)])
    new, new_k = MoireSolver.momentum_subspaces(k_list, Gk, 4)
    @test new_k == ref_k && all(a.list == b.list for (a, b) in zip(new, ref))
end
