using Random
using LinearAlgebra
using JSON3

# Independent dense partial trace: build coefficient tensors by orbital
# subsets and count A/B inversions directly, without the port's sign helper.
function independent_pes_blocks(para,parents,NA; holes=false)
    ns = para.Nk*para.Nc
    n = count_ones(parents[1].space.list[1].n)
    total = holes ? ns-n : n
    amasks = [UInt64(m) for m in 0:2^ns-1 if count_ones(m)==NA]
    bmasks = [UInt64(m) for m in 0:2^ns-1 if count_ones(m)==total-NA]
    rho = zeros(ComplexF64,length(amasks),length(amasks))
    full = UInt64(2^ns-1)
    for psi in parents
        coefficients = Dict(m.n=>v for (m,v) in zip(psi.space.list,psi.vec))
        C = zeros(ComplexF64,length(amasks),length(bmasks))
        for (i,a) in enumerate(amasks),(j,b) in enumerate(bmasks)
            iszero(a&b) || continue
            inversions = sum(((a >> x)&1)*((b >> y)&1) for x in 0:ns-1 for y in 0:x-1; init=0)
            parent = holes ? full ⊻ (a|b) : a|b
            C[i,j] = (-1)^inversions*get(coefficients,parent,0.0+0im)
        end
        rho .+= C*C'/(length(parents)*binomial(total,NA))
    end
    geometry = PESGeometry(para,n)
    direct_momentum(m) = Tuple(mod(sum(para.k_list[d,mod(i,para.Nk)+1] for i in 0:ns-1 if !iszero((m>>i)&1); init=0),para.Gk[d]) for d in 1:2)
    groups = [[i for (i,a) in enumerate(amasks) if direct_momentum(a)==k] for k in zip(geometry.kk1A,geometry.kk2A)]
    return [rho[g,g] for g in groups]
end

@testset "PES explicit parents restore discarded and copied vectors" begin
    kl,Gk=build_kmesh(Dict("nk1"=>3,"nk2"=>2),6)
    para=EDPara(k_list=kl,Gk=Gk)
    subs,ks=ED_momentum_subspaces(para,(3,))
    scat=ED_scatterlist_twobody(para)
    ed=MoireSolver.ed_settings(Dict("ed_accuracy"=>"search","ed_method"=>"sparse"),1,maximum(length,subs))
    energies,vectors,_=solve_ed_spectrum(subs,ks,scat,Gk; Neigen=ed.nlevels,ed)
    blocks=findall(s -> length(s)>=2,subs)[1:2]
    vectors[blocks[1]]=vectors[blocks[1]][1:1]
    vectors[blocks[2]]=nothing
    settings=Dict("NA"=>1,"parents"=>[
        Dict("momentum"=>collect(ks[blocks[1]]),"state"=>2),
        Dict("momentum"=>collect(ks[blocks[2]]),"state"=>1)])
    stats=MoireSolver.EDStats()
    result=MoireSolver.pes_from_ed_spectrum(para,subs,ks,energies,vectors,scat,ed,settings,1; stats)
    @test result[:trace] ≈ 1 atol=1e-12
    @test [p[:state] for p in result[:parents]]==[2,1]
    @test stats.n_solves==2
    bad=copy(settings);bad["nparents"]=2
    @test_throws ArgumentError MoireSolver.pes_from_ed_spectrum(para,subs,ks,energies,vectors,scat,ed,bad,1)
    bad=Dict("NA"=>1,"parents"=>[settings["parents"][1],settings["parents"][1]])
    @test_throws ArgumentError MoireSolver.pes_from_ed_spectrum(para,subs,ks,energies,vectors,scat,ed,bad,1)
    for key in ("NA","nparents","given_count","memory_budget_bytes")
        bad=Dict("NA"=>1,key=>1.5)
        @test_throws ArgumentError MoireSolver.pes_from_ed_spectrum(para,subs,ks,energies,vectors,scat,ed,bad,1)
    end
    for key in ("zero_tol","level_floor","gap_min","auto_min_gap")
        bad=Dict("NA"=>1,key=>nothing)
        @test_throws ArgumentError MoireSolver.pes_from_ed_spectrum(para,subs,ks,energies,vectors,scat,ed,bad,1)
    end
end

@testset "PES independent partial trace and state adapter" begin
    rng = MersenneTwister(9911)
    kl,Gk = build_kmesh(Dict("nk1"=>3,"nk2"=>2),6)
    para = EDPara(k_list=kl,Gk=Gk)
    spaces,ks = ED_momentum_subspaces(para,(3,))
    # Repeat a sector and include a second sector, preserving complex phases.
    parents = MBS64Vector[ MBS64Vector(normalize!(randn(rng,ComplexF64,length(spaces[b]))),spaces[b]) for b in (1,1,4)]
    for holes in (false,true), NA in 0:3
        actual = pes_density_matrices(para,parents,NA; holes,threaded=false).blocks
        expected = independent_pes_blocks(para,parents,NA; holes)
        @test all(isapprox(a,b; atol=1e-12,rtol=1e-12) for (a,b) in zip(actual,expected))
        result = pes_spectrum(para,parents,NA; holes)
        @test result.trace ≈ 1 atol=1e-12
        @test sum(result.dimensions) == binomial(6,NA)
    end
    # A single Slater determinant in a truncated basis is embedded correctly.
    determinant = MBS64Vector(ComplexF64[1],HilbertSubspace([MBS64(6,(1,2,4))]))
    for holes in (false,true),NA in 0:3
        result = pes_spectrum(para,[determinant],NA; holes)
        vals = filter(>(1e-12),reduce(vcat,result.eigenvalues))
        @test length(vals)==binomial(3,NA)
        @test vals ≈ fill(1/binomial(3,NA),length(vals))
        @test result.display_levels == [sort(-log.(max.(v,1e-15))) for v in result.eigenvalues]
    end
    # Explicitly permute an existing basis after construction.
    parent = parents[1]
    permutation = reverse(eachindex(parent.vec))
    reordered_space = HilbertSubspace(copy(parent.space.list))
    reordered_space.list[:] = parent.space.list[permutation]
    reordered = MBS64Vector(parent.vec[permutation],reordered_space)
    @test pes_spectrum(para,[parent],2).eigenvalues ≈ pes_spectrum(para,[reordered],2).eigenvalues
    @test_throws ArgumentError pes_spectrum(para,[MBS64Vector(2parent.vec,parent.space)],2)
    @test_throws ArgumentError pes_spectrum(para,parents,2; zero_tol=-1.0)
    @test_throws ArgumentError pes_spectrum(para,parents,2; level_floor=0.0)
    @test_throws ArgumentError PESGeometry([0 1;0 0],(3,1),1)
    # End-bit and zero/full subset handling, without enumerating large bases.
    @test PE.generate_masks(64,64)==[typemax(UInt64)]
    @test PE.submasks_of_size(UInt64(0),0)==[UInt64(0)]
    @test PE.submasks_of_size(typemax(UInt64),64)==[typemax(UInt64)]
    @test length(PE.submasks_of_size(typemax(UInt64),1))==64
    # Donor's Ns<32 choice disagreed with its mask generator at exactly 32.
    p32=PESGeometry([collect(0:31)';zeros(Int,1,32)],(32,1),1)
    @test PESParams(p32,1,false) isa PESParams{UInt32}
    values32=particle_entanglement_eigenvalues(p32,[ComplexF64[1]],[0],PESParams(p32,1,false))
    @test sum(sum,values32) ≈ 1 atol=1e-12
    p64=PESGeometry([collect(0:63)';zeros(Int,1,64)],(64,1),64)
    sector=PE.ksum_mask(p64,typemax(UInt64))
    for cut in (0,1,64)
        values=particle_entanglement_eigenvalues(p64,[ComplexF64[1]],[sector],PESParams(p64,cut,false))
        @test sum(sum,values) ≈ 1 atol=1e-12
    end
end

@testset "PES null modes, thresholds and expected counting" begin
    levels = [[1.0,3.0,Inf],[1.5,4.0,Inf]]
    @test pes_threshold(levels; mode=:auto_gap).total_count==2
    @test pes_threshold(levels; mode=:manual,threshold=3.5).counts==[2,1]
    @test pes_threshold(levels; mode=:given_count,given_count=2).gap==1.5
    @test pes_counting_gap(levels,[1,1]).matched
    @test !pes_counting_gap(levels,[1,2]).matched
    @test !pes_counting_gap([[Inf],[Inf]],[1,0]).matched
    @test_throws ArgumentError pes_threshold(levels; mode=:manual,threshold=Inf)
    @test_throws ArgumentError pes_threshold(levels; mode=:given_count,given_count=4)
    @test_throws DimensionMismatch pes_counting_gap(levels,[1])
    kl,Gk = build_kmesh(Dict("nk1"=>3,"nk2"=>4),12)
    para = EDPara(k_list=kl,Gk=Gk)
    @test pes_admissible_counts(para,2).total_count==42
    for nk in supported_symmetric_clusters()
        kl,Gk = build_symmetric_kmesh(nk)
        p = PESGeometry(kl,Gk,1)
        @test p.Nk==nk
        @test all(p.klookup[k[1]+1,k[2]+1]==i-1 for (i,k) in enumerate(zip(p.kk1A,p.kk2A)))
    end
end

@testset "PES solver integration: same-sector parents and optional output" begin
    raw = JSON3.read(read(joinpath(@__DIR__,"data","nk12_trivial.json"),String),Dict{String,Any})
    extra = raw["ed_solver_params"]["extra"]
    extra["ed_accuracy"] = "search"
    extra["wilson_plaquette_diagnostic"] = false
    extra["pes"] = Dict("NA"=>2,"threshold_mode"=>"given_count","given_count"=>42)
    output = MoireSolver.solve(JSON3.read(JSON3.write(raw)); t_start=time())
    @test output[:pes][:trace] ≈ 1 atol=1e-12
    @test length(output[:pes][:parents])==3
    @test sum(output[:pes][:dimensions])==66
    @test !occursin("Infinity",JSON3.write(output))
    @test output[:pes][:threshold_diagnostic].total_count==42
    # A mesh rejected for the existing Chern method still returns its PES.
    extra["nk1"]=3; extra["nk2"]=6
    raw["lattice"]["n_k"]=18
    extra["pes"] = Dict("NA"=>2)
    output = MoireSolver.solve(JSON3.read(JSON3.write(raw)); t_start=time())
    @test output[:failure_reason]=="mesh_unsuitable_for_chern"
    @test output[:pes][:trace] ≈ 1 atol=1e-12
    @test length(unique(output[:pes][:parent_sectors]))<3
    extra["pes"] = Dict("NA"=>100)
    output = MoireSolver.solve(JSON3.read(JSON3.write(raw)); t_start=time())
    @test output[:failure_reason]=="pes_invalid"
    delete!(extra,"pes")
    output = MoireSolver.solve(JSON3.read(JSON3.write(raw)); t_start=time())
    @test !haskey(output,:pes)
end
