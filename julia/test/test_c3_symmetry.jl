# Acceptance: a C3_hard density built on the Python side's orbits
# (120° convention) is C3-symmetric AS THE SOLVER EVALUATES IT, and on a
# C6-symmetric cluster the symmetry-reduced ED of a modulated band with REAL
# orbit coefficients equals the full ED — the symmetry-reduction benchmark, which had only
# been run on the uniform band. With complex (chiral) coefficients the density
# loses inversion and the lattice-point-group reduction is invalid; that case is
# pinned as a documented limitation.
using LinearAlgebra

@testset "C3_hard density is C3-symmetric in the solver" begin
    lat = MoireSolver.triangular_lattice()
    # one complex orbit coefficient on the first star {(1,0),(0,1),(-1,-1)} + inversion partners
    z = 0.12 + 0.05im
    glist = Tuple{Int,Int}[(0, 0), (1, 0), (0, 1), (-1, -1), (-1, 0), (0, -1), (1, 1)]
    w = ComplexF64[1, z, z, z, conj(z), conj(z), conj(z)]
    rot(k, θ) = (cos(θ) * k[1] - sin(θ) * k[2], sin(θ) * k[1] + cos(θ) * k[2])
    S00(k) = MoireSolver.raw_formfactor_mn(k, k, (0, 0), 0, 0, glist, w, lat)
    worst = 0.0
    for _ in 1:20
        k = (rand() - 0.5, rand() - 0.5)
        worst = max(worst, abs(S00(k) - S00(rot(k, 2π / 3))))
    end
    @test worst < 1e-12
    # the pre-fix orbit {(1,0),(-1,1),(0,-1)} is NOT a symmetry orbit here
    glist_old = Tuple{Int,Int}[(0, 0), (1, 0), (-1, 1), (0, -1), (-1, 0), (1, -1), (0, 1)]
    S00old(k) = MoireSolver.raw_formfactor_mn(k, k, (0, 0), 0, 0, glist_old, w, lat)
    k = (0.31, -0.17)
    @test abs(S00old(k) - S00old(rot(k, 2π / 3))) > 1e-4
end

@testset "symmetry-reduced ED = full ED on a modulated C3_hard band" begin
    lat = MoireSolver.triangular_lattice()
    glist = Tuple{Int,Int}[(0, 0), (1, 0), (0, 1), (-1, -1), (-1, 0), (0, -1), (1, 1)]
    k_list, Gk = MoireSolver.build_symmetric_kmesh(12)
    qlist = MoireSolver.build_qgrid(6)
    ml = [(k_list[1, i], k_list[2, i]) for i in axes(k_list, 2)]
    function spectra(z)
        w = ComplexF64[1, z, z, z, conj(z), conj(z), conj(z)]
        tff = MoireSolver.TrialFormFactor(glist, w, lat, [(1.0, 0)]; reg = 0.0)
        h2 = MoireSolver.TrialBandH2(tff, lat, Gk, qlist, 6, 2.6935473741771965, 0.0, 0.1)
        para = EDPara(; k_list = k_list, Gk = Gk, H_two = h2)
        scat = ED_scatterlist_twobody(para)
        subs, ks = ED_momentum_subspaces(para, (4,); momentum_restriction = true, momentum_list = ml)
        e_full, _, _ = MoireSolver.solve_ed_spectrum(subs, ks, scat, Gk; Neigen = 4, method = :sparse, mode = :full_ed, lattice = :triangular)
        e_red, _, plan = MoireSolver.solve_ed_spectrum(subs, ks, scat, Gk; Neigen = 4, method = :sparse, mode = :symmetry_reduced_ed, lattice = :triangular)
        worst = maximum(maximum(abs.(e_full[i] .- e_red[i])) for i in eachindex(subs) if !isempty(e_full[i]))
        return worst, length(plan.solve_indices), length(subs)
    end
    # real orbit coefficient: the density has the full C6 (and mirror) symmetry, the
    # symmetry-reduction benchmark holds on a MODULATED band (it had only been run on the uniform one)
    worst, nsolved, ntot = spectra(0.12 + 0.0im)
    @test nsolved < ntot
    @test worst < 1e-8
    # complex orbit coefficient: rho(r) is real but not even, so inversion (and hence
    # the solver's C6 sector reduction) is NOT a symmetry — the reduced spectrum is wrong.
    # Documented limitation: symmetry_reduced_ed needs real C3_hard coefficients on the
    # solver's labels; the pre-fix labels never qualify.
    worst_chiral, _, _ = spectra(0.12 + 0.05im)
    @test worst_chiral > 1e-6
end
