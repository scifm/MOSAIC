# Phase-resolved timing of one MoireSolver evaluation.
#
#   julia -t N --project=julia scripts/profile_solver_phases.jl IN.json [n_sectors] [twist]
#
# Times the pieces `MoireSolver.solve` is made of, separately: the trial
# form-factor setup, the zero-twist two-body scatter list, and per momentum
# sector the sparse-matrix build and the Krylov solve (first `n_sectors`
# sectors, default all). With `twist` = 1 it also times one twisted scatter
# list, the unit every Chern re-solve pays. Prints one line per phase.

using JSON3, Printf, LinearAlgebra
using MomentumED
include(joinpath(@__DIR__, "..", "julia", "src", "MoireSolver.jl"))
using .MoireSolver
const MS = MoireSolver

function main()
    path = ARGS[1]
    n_sec_req = length(ARGS) >= 2 ? parse(Int, ARGS[2]) : typemax(Int)
    do_twist = length(ARGS) >= 3 && ARGS[3] == "1"
    raw = JSON3.read(read(path, String))
    extra = Dict{String,Any}(string(k) => v for (k, v) in pairs(raw[:ed_solver_params][:extra]))
    n_k = Int(raw[:lattice][:n_k])
    filling = raw[:ed_solver_params][:filling] === nothing ? 1 / 3 : Float64(raw[:ed_solver_params][:filling])

    t_setup = @elapsed begin
        a_n = MS.decode_a_n(raw[:wavefunction])
        glist, w_G = MS.decode_W_G(raw[:form_factor])
        lattice = MS.lattice_from_extra(extra)
        k_list, Gk = MS.build_kmesh(extra, n_k)
        Nk = size(k_list, 2)
        Ne = round(Int, Nk * filling)
        level_mix = [(abs2(a_n[n + 1]), n) for n in 0:length(a_n) - 1]
        deformation = get(raw[:form_factor], :deformation, nothing)
        kernel = nothing
        if deformation !== nothing
            kernel = MS.DeformationKernel(deformation, glist, w_G, lattice)
            glist = kernel.glist; w_G = kernel.seed_w
        end
        tff = MS.TrialFormFactor(glist, w_G, lattice, level_mix;
                                 reg = Float64(get(extra, "ll_orth_reg", 0.0)), kernel = kernel)
        qmax = Int(get(extra, "qmax", 6))
        h2 = MS.TrialBandH2(tff, lattice, Gk, MS.build_qgrid(qmax), qmax,
                            Float64(get(extra, "W0", 1.0)), Float64(get(extra, "d_l", 0.0)),
                            Float64(get(extra, "D_l", 10.0)))
        para = EDPara(; k_list = k_list, Gk = Gk, H_two = h2)
        momentum_list = [(k_list[1, i], k_list[2, i]) for i in axes(k_list, 2)]
        subspaces, ss_k = ED_momentum_subspaces(para, (Ne,); momentum_restriction = true,
                                                momentum_list = momentum_list)
    end
    @printf("threads=%d Nk=%d Ne=%d n_G=%d qmax=%d kernel=%s\n", Threads.nthreads(), Nk, Ne,
            length(glist), Int(get(extra, "qmax", 6)), kernel === nothing ? "none" : "deformed")
    @printf("setup            %8.2f s\n", t_setup)

    t_scat = @elapsed scat = ED_scatterlist_twobody(para)
    @printf("scatter list      %8.2f s  (%d terms)\n", t_scat, length(scat))
    if do_twist
        t_tw = @elapsed ED_scatterlist_twobody(para; kshift = (1 // 2, 0 // 1))
        @printf("twisted scat list %8.2f s\n", t_tw)
    end

    Neigen = Int(get(extra, "neigen_per_block", 6))
    tb = 0.0; te = 0.0
    for i in 1:min(n_sec_req, length(subspaces))
        dim = length(subspaces[i])
        t1 = @elapsed H = MomentumED.Methods.SparseHmltMatrix(subspaces[i], scat)
        t2 = @elapsed vals, _, info = MomentumED.Methods.krylov_matrix_solve(H, min(Neigen, dim))
        tb += t1; te += t2
        nnzH = H isa Hermitian ? nnz(parent(H)) : nnz(H)
        @printf("sector %2d K=%s dim=%8d nnz=%10d build %7.2f s  eig %7.2f s  (matvecs %d) E0=%.10f\n",
                i, string(ss_k[i]), dim, nnzH, t1, t2, info.numops, real(vals[1]))
    end
    @printf("TOTAL sectors: build %.2f s, eig %.2f s\n", tb, te)
end

using SparseArrays: nnz
main()
