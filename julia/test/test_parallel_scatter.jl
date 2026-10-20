# Twisted scatter lists built concurrently (fresh caches per task)
# are identical to serial builds, for the static and the k-dependent model.
using JSON3

@testset "twisted_scatter_lists == serial ED_scatterlist_twobody ($file)" for file in
        ("nk12_12cdff_ll012.json", "nk24_p024_a1M_kdep.json")
    raw = JSON3.read(read(joinpath(@__DIR__, "data", file), String))
    extra = Dict{String,Any}(string(k) => v for (k, v) in pairs(raw[:ed_solver_params][:extra]))
    glist, w = MoireSolver.decode_W_G(raw[:form_factor])
    lat = MoireSolver.lattice_from_extra(extra)
    kernel = nothing
    dfm = get(raw[:form_factor], :deformation, nothing)
    if dfm !== nothing
        kernel = MoireSolver.DeformationKernel(dfm, glist, w, lat)
        glist, w = kernel.glist, kernel.seed_w
    end
    a_n = MoireSolver.decode_a_n(raw[:wavefunction])
    tff = MoireSolver.TrialFormFactor(glist, w, lat, [(abs2(a_n[n + 1]), n) for n in 0:length(a_n) - 1];
                                      kernel = kernel)
    k_list, Gk = MoireSolver.build_kmesh(extra, Int(raw[:lattice][:n_k]))
    qmax = Int(get(extra, "qmax", 6))
    h2 = MoireSolver.TrialBandH2(tff, lat, Gk, MoireSolver.build_qgrid(qmax), qmax,
                                 Float64(extra["W0"]), Float64(extra["d_l"]), Float64(extra["D_l"]))
    para = EDPara(; k_list = k_list, Gk = Gk, H_two = h2)
    twists = [(1 // 2, 0 // 1), (0 // 1, 1 // 2), (1 // 2, 1 // 2)]
    par = MoireSolver.twisted_scatter_lists(h2, k_list, Gk, twists)
    for θ in twists
        ser = ED_scatterlist_twobody(para; kshift = θ)
        @test length(par[θ]) == length(ser)
        @test all(a.in == b.in && a.out == b.out && a.Amp == b.Amp for (a, b) in zip(par[θ], ser))
    end
end
