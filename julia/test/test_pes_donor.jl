# Regression tests carried over from the authors' earlier ED code, from which
# the PES implementation is adapted.
# Included after MoireSolver by julia/test/runtests.jl.
using Test
using LinearAlgebra
using Random
using .MoireSolver.ParticleEntanglement
const PE = MoireSolver.ParticleEntanglement

function pes_test_params(Nk, N; symcluster=0, N1=3, N2=2)
    k_list, Gk = symcluster == 1 ? build_symmetric_kmesh(Nk) :
        build_kmesh(Dict("nk1"=>N1,"nk2"=>N2),Nk)
    return PESGeometry(k_list,Gk,N)
end

pes_parent_masks(p,s) = PE.findmbstates3(p,p.Ns,p.N,s)[1]

function streamed_density_blocks(p, vecs, sectors, pes; threaded)
    nparticles = pes.holes ? p.Ns - p.N : p.N
    agroups = [PE.findmbstates3(p, p.Ns, pes.NA, s)[1] for s in 0:p.Nk-1]
    bgroups = [PE.findmbstates3(p, p.Ns, nparticles - pes.NA, s)[1] for s in 0:p.Nk-1]
    sector_masks = PE.build_sector_mask_table(p, p.N, sectors)
    weight = inv(length(sectors) * binomial(nparticles, pes.NA))
    return [Matrix(PE._pes_density_block(
        p, vecs, sectors, pes, agroups, bgroups, sector_masks, ka, weight, threaded,
    )) for ka in 0:p.Nk-1]
end

@testset "PES streaming preserves density matrices and spectra" begin
    rng = MersenneTwister(987)
    rectangular = pes_test_params(6, 4)
    tilted = pes_test_params(7, 3; symcluster = 1)
    # Two orbitals at each momentum also exercise Ns != Nk.
    orbital_fields = (
        Ns = 12, N = 3,
        kk1 = repeat(rectangular.kk1A; inner = 2),
        kk2 = repeat(rectangular.kk2A; inner = 2),
    )
    two_orbitals = typeof(rectangular)((
        get(orbital_fields, name, getfield(rectangular, name))
        for name in fieldnames(typeof(rectangular))
    )...)
    for p in (rectangular, tilted, two_orbitals)
        populated = [s for s in 0:p.Nk-1 if !isempty(pes_parent_masks(p,s))]
        # A pure state and a manifold with two states in one sector, plus
        # another sector, catch changes in mixture weights or parent ordering.
        for sectors in ([first(populated)], [first(populated), first(populated), last(populated)])
            vecs = Vector{ComplexF64}[]
            for s in unique(sectors)
                dim = length(pes_parent_masks(p,s))
                mult = count(==(s), sectors)
                Q = Matrix(qr(randn(rng, ComplexF64, dim, mult)).Q)
                append!(vecs, [Q[:, i] for i in 1:mult])
            end
            for holes in (false, true)
                nparticles = holes ? p.Ns - p.N : p.N
                # Keep the multi-orbital case small while covering asymmetric
                # cuts and the full-particle cut in the single-orbital cases.
                cuts = p.Ns == p.Nk ? (0:nparticles) : (0:2)
                for NA in cuts
                    pes = PESParams(p, NA, holes)
                    reference = particle_entanglement_spectrum(p, vecs, sectors, pes)
                    original_threaded = particle_entanglement_spectrum_threaded(p, vecs, sectors, pes)
                    @test all(isapprox(a, b; atol = 1e-12, rtol = 1e-12) for (a, b) in zip(original_threaded, reference))
                    reference_values = [isempty(rho) ? Float64[] : eigen(Hermitian(rho)).values for rho in original_threaded]
                    @test sum(real(tr(rho)) for rho in reference) ≈ 1 atol = 1e-12
                    for threaded in (false, true)
                        blocks = streamed_density_blocks(p, vecs, sectors, pes; threaded)
                        @test all(isapprox(a, b; atol = 1e-12, rtol = 1e-12) for (a, b) in zip(blocks, reference))
                        values = particle_entanglement_eigenvalues(p, vecs, sectors, pes; threaded)
                        @test length.(values) == length.(reference_values)
                        @test all(isapprox(a, b; atol = 1e-12, rtol = 1e-12) for (a, b) in zip(values, reference_values))
                        @test sum(sum, values) ≈ 1 atol = 1e-12
                        @test minimum(minimum(v) for v in values if !isempty(v)) >= -1e-12
                        # Use the reference code's exact logarithm and level floor,
                        # including the null levels of rank-deficient blocks.
                        for (a, b) in zip(values, reference_values)
                            @test sort(-log.(max.(a, 1e-15))) ≈ sort(-log.(max.(b, 1e-15))) atol = 1e-9 rtol = 1e-10
                        end
                    end
                end
            end
        end
    end
end

@testset "PES boundary partitions and validation" begin
    p = pes_test_params(6, 4)
    masks = PE.findmbstates3(p, p.Ns, p.N, 0)[1]
    state = zeros(ComplexF64, length(masks))
    state[1] = 1
    for holes in (false, true)
        nparticles = holes ? p.Ns - p.N : p.N
        for NA in 0:nparticles
            values = particle_entanglement_eigenvalues(p, [state], [0], PESParams(p, NA, holes))
            positive = filter(>(1e-12), reduce(vcat, values))
            @test length(positive) == binomial(nparticles, NA)
            @test positive ≈ fill(inv(binomial(nparticles, NA)), length(positive))
        end
        @test_throws ArgumentError PESParams(p, -1, holes)
        @test_throws ArgumentError PESParams(p, nparticles + 1, holes)
    end
    pes = PESParams(p, 2, false)
    @test_throws ArgumentError particle_entanglement_eigenvalues(p, [], [], pes)
    @test_throws DimensionMismatch particle_entanglement_eigenvalues(p, [state], [], pes)
    @test_throws ArgumentError particle_entanglement_eigenvalues(p, [state], [p.Nk], pes)
    @test_throws DimensionMismatch particle_entanglement_eigenvalues(p, [state[1:1]], [0], pes)
    @test_throws ArgumentError particle_entanglement_eigenvalues(p, [state], [0], pes; memory_budget_bytes = -1)
end

@testset "PES automatic concurrency limits" begin
    workers = PE._pes_sector_worker_count
    @test workers(100, 1000, 7, 4, 1, true) == 4
    @test workers(100, 250, 7, 4, 1, true) == 2
    @test workers(100, 100, 7, 4, 1, true) == 1
    @test workers(100, 0, 7, 4, 1, true) == 1
    @test workers(100, 1000, 2, 4, 1, true) == 2
    @test workers(100, 1000, 7, 4, 2, true) == 2
    @test workers(100, 1000, 7, 4, 8, true) == 1
    @test workers(100, 1000, 7, 1, 1, true) == 1
    @test workers(100, 1000, 7, 4, 1, false) == 1

    # The original kernel-crashing partition must retain the low-memory path
    # even at the maximum automatic budget of a 16 GiB machine.
    p = pes_test_params(21, 14; symcluster = 1)
    pes = PESParams(p, 7, false)
    groups = [eltype(pes.annimasks)[] for _ in 1:p.Nk]
    for mask in pes.annimasks
        push!(groups[PE.ksum_mask(p, mask) + 1], mask)
    end
    sectors = [0, 7, 14]
    masks = PE.build_sector_mask_table(p, p.N, sectors)
    workspace = PE._pes_sector_workspace_bytes(p, sectors, pes, groups, groups, masks)
    @test workers(workspace, 4 * 2^30, p.Nk, 4, 1, true) == 1
end

@testset "PES sector parallelism preserves spectra and BLAS settings" begin
    p = pes_test_params(7, 3; symcluster = 1)
    rng = MersenneTwister(135)
    sectors = [0, 0, 6] # Repeated parent sector; seven sectors leave a partial batch.
    vecs = [normalize!(randn(rng, ComplexF64, length(pes_parent_masks(p,s)))) for s in sectors]
    original_blas_threads = BLAS.get_num_threads()
    try
        for blas_threads in (1, 2)
            BLAS.set_num_threads(blas_threads)
            for holes in (false, true), NA in 0:(holes ? p.Ns - p.N : p.N)
                pes = PESParams(p, NA, holes)
                serial = particle_entanglement_eigenvalues(p, vecs, sectors, pes; threaded = false)
                for budget in (0, 2^30)
                    parallel = particle_entanglement_eigenvalues(
                        p, vecs, sectors, pes; memory_budget_bytes = budget,
                    )
                    @test length.(parallel) == length.(serial)
                    @test all(isapprox(a, b; atol = 1e-12, rtol = 1e-12) for (a, b) in zip(parallel, serial))
                    @test all(isapprox(sort(-log.(max.(a, 1e-15))), sort(-log.(max.(b, 1e-15))); atol = 1e-9)
                              for (a, b) in zip(parallel, serial))
                    @test BLAS.get_num_threads() == blas_threads
                end
            end
        end
    finally
        BLAS.set_num_threads(original_blas_threads)
    end
end
