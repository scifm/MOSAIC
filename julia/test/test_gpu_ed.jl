# The GPU sector solver must reproduce the CPU `:sparse` path — the
# same Hamiltonian entry by entry (in particular H, not Hᵀ: a transposed
# operator has the right spectrum but complex-conjugated eigenvectors, which
# flips every Berry phase), the same spectrum, and the same Chern number.
# Skipped on nodes without a functional GPU; on a GPU node run the suite with
#   julia -t 4 --project=julia julia/test/runtests.jl
using JSON3
using SparseArrays

const _cuda_ok = try
    @eval using CUDA
    CUDA.functional()
catch
    false
end

if !_cuda_ok
    @info "test_gpu_ed: no functional CUDA device, skipped"
else
    MoireSolver.gpu_solve_batch(Tuple{Int,Any}[], [], identity, 1; Neigen = 1)  # load the module
    G = MoireSolver.GPU_MODULE[]

    function setup_case(file)
        raw = JSON3.read(read(joinpath(@__DIR__, "data", file), String))
        extra = Dict{String,Any}(string(k) => v for (k, v) in pairs(raw[:ed_solver_params][:extra]))
        glist, w = MoireSolver.decode_W_G(raw[:form_factor])
        a_n = MoireSolver.decode_a_n(raw[:wavefunction])
        lat = MoireSolver.lattice_from_extra(extra)
        k_list, Gk = MoireSolver.build_kmesh(extra, Int(raw[:lattice][:n_k]))
        mix = [(abs2(a_n[n + 1]), n) for n in 0:length(a_n) - 1]
        tff = MoireSolver.TrialFormFactor(glist, w, lat, mix)
        qmax = Int(get(extra, "qmax", 6))
        h2 = MoireSolver.TrialBandH2(tff, lat, Gk, MoireSolver.build_qgrid(qmax), qmax,
                                     Float64(extra["W0"]), Float64(extra["d_l"]), Float64(extra["D_l"]))
        para = EDPara(; k_list = k_list, Gk = Gk, H_two = h2)
        Nk = size(k_list, 2)
        subspaces, ss_k = ED_momentum_subspaces(para, (Nk ÷ 3,); momentum_restriction = true,
            momentum_list = [(k_list[1, i], k_list[2, i]) for i in 1:Nk])
        return raw, para, subspaces
    end

    @testset "GPU ED: device CSR equals the CPU Hamiltonian entrywise (twisted)" begin
        _, para, subspaces = setup_case("nk12_12cdff_ll012.json")
        scat = ED_scatterlist_twobody(para; kshift = (1 // 3, 1 // 5))   # generic twist: complex H
        bits = MoireSolver.get_bits(first(subspaces))
        tab = G.DevScatterTable(G.PairScatterTable(scat, bits))
        for b in eachindex(subspaces)
            sub = subspaces[b]
            length(sub) == 0 && continue
            Hc = MomentumED.Methods.SparseHmltMatrix(sub, scat)
            Hcpu = Matrix(Hc isa Hermitian ? Hermitian(parent(Hc), :U) : Hc)
            Hd = G.DevSectorH(UInt64[m.n for m in sub.list], tab; max_bytes = 1e9)
            rp = Array(Hd.rowptr); ci = Array(Hd.colind); vv = Array(Hd.vals); dg = Array(Hd.diag)
            Hgpu = zeros(ComplexF64, length(sub), length(sub))
            for r in 1:length(sub)
                Hgpu[r, r] += dg[r]
                for k in rp[r]:rp[r + 1] - 1
                    Hgpu[r, ci[k]] += vv[k]
                end
            end
            @test all(ci[k] != r for r in 1:length(sub) for k in rp[r]:rp[r + 1] - 1)   # CSR is off-diagonal only
            @test maximum(abs.(Hgpu .- Hcpu)) < 1e-13
            @test maximum(abs.(imag.(Hcpu))) > 1e-6        # the check is not vacuous
            # matrix-free apply == CSR apply
            x = CuArray(rand(ComplexF64, length(sub)))
            Hmf = G.DevSectorH(UInt64[m.n for m in sub.list], tab; max_bytes = 0)
            @test Hmf.rowptr === nothing
            @test maximum(abs.(Array(G.apply(Hmf, x)) .- Array(G.apply(Hd, x)))) < 1e-12
            @test maximum(abs.(Array(G.apply(Hd, x)) .- Hcpu * Array(x))) < 1e-12
        end
    end

    @testset "GPU ED: eigenpairs match EDsolve(:sparse), vectors not conjugated" begin
        _, para, subspaces = setup_case("nk12_12cdff_ll012.json")
        scat = ED_scatterlist_twobody(para; kshift = (1 // 3, 1 // 5))
        bits = MoireSolver.get_bits(first(subspaces))
        big = [b for b in eachindex(subspaces) if length(subspaces[b]) >= 20]
        res = MoireSolver.gpu_solve_batch(Tuple{Int,Any}[(b, :tw) for b in big], subspaces,
                                          _ -> scat, bits; Neigen = 4)
        for b in big
            vc, Vc = EDsolve(subspaces[b], scat; N = 4, method = :dense, method_info = false,
                             max_dense_dim = 10^6)
            vg, Vg = res[(b, :tw)]
            @test maximum(abs.(vg .- real.(vc))) < 1e-9
            if vc[2] - vc[1] > 1e-6                          # nondegenerate ground state
                @test abs(abs(dot(Vc[1].vec, Vg[1].vec)) - 1) < 1e-8
            end
        end
    end

    @testset "GPU ED: full solve agrees with the CPU backend ($file)" for file in
            ("nk24_dcf05d3b_8shell_ll012.json", "nk24_p024_a1M_kdep.json")
        s = read(joinpath(@__DIR__, "data", file), String)
        outs = Dict{String,Any}()
        for backend in ("cpu", "gpu")
            withenv("MOIRE_ED_BACKEND" => backend) do
                outs[backend] = MoireSolver.solve(JSON3.read(s); t_start = time())
            end
        end
        c, g = outs["cpu"], outs["gpu"]
        @test c[:ed_backend] == "sparse" && g[:ed_backend] == "gpu"
        @test c[:status] == g[:status]
        @test abs(c[:gap_top_indirect_solver] - g[:gap_top_indirect_solver]) < 1e-9
        @test maximum(abs.(reduce(vcat, c[:low_energies]) .- reduce(vcat, g[:low_energies]))) < 1e-9
        @test c[:chern_solver] == g[:chern_solver]
        if c[:chern_glued_raw] !== nothing
            @test abs(c[:chern_glued_raw] - g[:chern_glued_raw]) < 1e-6
        end
        if c[:chern_plaquette_raw] !== nothing
            @test abs(c[:chern_plaquette_raw] - g[:chern_plaquette_raw]) < 1e-6
        end
    end
end
