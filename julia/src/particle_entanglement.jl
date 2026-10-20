"""Particle/hole entanglement spectrum, adapted from the authors' earlier ED code without its model dependencies."""
module ParticleEntanglement

using LinearAlgebra
using SparseArrays
using Printf
using MomentumED: EDPara, MBS64Vector

export PESGeometry, PESParams, pes_spectrum, pes_density_matrices
export particle_entanglement_eigenvalues, particle_entanglement_spectrum
export particle_entanglement_spectrum_threaded, pes_counting_gap, pes_threshold
export pes_admissible_counts

"""Finite momentum group in orbital order; PES sector numbers are zero-based."""
struct PESGeometry
    Ns::Int
    N::Int
    Nk::Int
    kk1::Vector{Int}
    kk2::Vector{Int}
    kk1A::Vector{Int}
    kk2A::Vector{Int}
    denominator1::Int
    denominator2::Int
    klookup::Matrix{Int}
end

function PESGeometry(k_list::Matrix{Int}, Gk::NTuple{2,Int}, N::Int)
    Ns = size(k_list, 2)
    1 <= Ns <= 64 || throw(ArgumentError("PES needs 1..64 orbitals."))
    size(k_list, 1) == 2 || throw(ArgumentError("PES needs two momentum coordinates."))
    all(>(0), Gk) || throw(ArgumentError("PES needs a finite periodic momentum group."))
    0 <= N <= Ns || throw(ArgumentError("PES needs 0 <= N <= Ns."))
    # Preserve the original single-particle order, including repeated momenta
    # for multiple orbitals. Tilted clusters occupy a subgroup of the grid.
    momenta = unique([(mod(k_list[1,i], Gk[1]), mod(k_list[2,i], Gk[2])) for i in 1:Ns])
    lookup = fill(-1, Gk...)
    for (i, k) in enumerate(momenta)
        lookup[k[1]+1, k[2]+1] = i-1
    end
    for a in momenta, b in momenta
        lookup[mod(a[1]-b[1],Gk[1])+1, mod(a[2]-b[2],Gk[2])+1] >= 0 ||
            throw(ArgumentError("PES momenta must form a closed finite group."))
    end
    return PESGeometry(Ns, N, length(momenta), mod.(vec(k_list[1,:]), Gk[1]),
        mod.(vec(k_list[2,:]), Gk[2]), first.(momenta), last.(momenta), Gk..., lookup)
end

PESGeometry(para::EDPara{2}, N::Int) = PESGeometry(repeat(para.k_list, 1, para.Nc), para.Gk, N)

include("pes_core.jl")

"""Embed/reorder MomentumED vectors by masks instead of assuming basis order."""
function prepare_pes_parents(para::EDPara, parents::AbstractVector{<:MBS64Vector})
    isempty(parents) && throw(ArgumentError("PES needs at least one parent state."))
    isempty(parents[1].space.list) && throw(ArgumentError("PES parent basis is empty."))
    N = count_ones(parents[1].space.list[1].n)
    p = PESGeometry(para, N)
    T = eltype(generate_masks(p.Ns, 0))
    sectors = Int[]
    vectors = Vector{ComplexF64}[]
    tables = Dict{Int,Vector{T}}()
    for (i, psi) in enumerate(parents)
        isempty(psi.space.list) && throw(ArgumentError("PES parent $(i) has an empty basis."))
        sector = ksum_mask(p, psi.space.list[1].n)
        masks = get!(tables, sector) do
            findmbstates3(p, p.Ns, N, sector)[1]
        end
        vec = zeros(ComplexF64, length(masks))
        seen = Set{T}()
        for (mbs, amplitude) in zip(psi.space.list, psi.vec)
            typeof(mbs).parameters[1] == p.Ns || throw(DimensionMismatch("PES parent orbital count differs."))
            count_ones(mbs.n) == N || throw(ArgumentError("PES parents must have fixed common particle number."))
            ksum_mask(p, mbs.n) == sector || throw(ArgumentError("PES parent must have definite momentum."))
            mask = T(mbs.n)
            mask in seen && throw(ArgumentError("PES parent basis has duplicate occupations."))
            push!(seen, mask)
            index = searchsortedfirst(masks, mask)
            index <= length(masks) && masks[index] == mask || throw(ArgumentError("Invalid PES parent mask."))
            vec[index] = amplitude
        end
        all(isfinite, vec) || throw(ArgumentError("PES parent amplitudes must be finite."))
        isapprox(sum(abs2, vec), 1; atol=1e-9, rtol=1e-9) ||
            throw(ArgumentError("PES parent $(i) is not normalized."))
        push!(sectors, sector)
        push!(vectors, vec)
    end
    return p, vectors, sectors
end

"""Trace-one particle/hole RDM blocks, averaged incoherently over parents."""
function pes_density_matrices(para::EDPara, parents::AbstractVector{<:MBS64Vector}, NA::Int;
    holes::Bool=false, threaded::Bool=true)
    p, vectors, sectors = prepare_pes_parents(para, parents)
    pes = PESParams(p, NA, holes)
    blocks = threaded ? particle_entanglement_spectrum_threaded(p, vectors, sectors, pes) :
                        particle_entanglement_spectrum(p, vectors, sectors, pes)
    return (momenta=collect(zip(p.kk1A,p.kk2A)), blocks=blocks)
end

"""Common threshold for expected counts in EVERY sector (from donor diagnostics)."""
function pes_counting_gap(levels, counts; gap_min::Real=0.5)
    length(levels) == length(counts) || throw(DimensionMismatch("PES counts and sectors disagree."))
    isfinite(gap_min) && gap_min >= 0 || throw(ArgumentError("PES gap_min must be finite and nonnegative."))
    below = Float64[]; above = Float64[]
    for (es,n) in zip(levels,counts)
        n isa Integer && 0 <= n <= length(es) ||
            throw(ArgumentError("Expected PES counts must be integers within sector dimensions."))
        issorted(es) || throw(ArgumentError("PES levels must be sorted."))
        append!(below,es[1:n]); append!(above,es[n+1:end])
    end
    if isempty(below) || isempty(above)
        return (gap=nothing, threshold=nothing, matched=false, informative=false)
    end
    low = maximum(below); high = minimum(above)
    isfinite(low) || return (gap=nothing, threshold=nothing, matched=false, informative=true)
    gap = high-low
    threshold = isfinite(high) ? (low+high)/2 : low+max(gap_min,1.0)
    matched = gap >= gap_min && [count(<(threshold),es) for es in levels] == counts
    return (gap=isfinite(gap) ? gap : nothing, threshold=threshold, matched=matched, informative=true)
end

"""
    pes_admissible_counts(para, NA; k=1, r=3)

Count cyclic (k,r) admissible occupations in the supplied orbital order,
grouped by actual subsystem momentum (ported from donor phase diagnostics).
The caller must establish that this orbital-order rule is appropriate for
their phase/cluster; this helper does not infer or assign a physical phase.
"""
function pes_admissible_counts(para::EDPara, NA::Int; k::Int=1, r::Int=3)
    p = PESGeometry(para,NA)
    p.Ns == p.Nk || throw(ArgumentError("Admissible counting needs one orbital per momentum."))
    1 <= r <= p.Ns && 0 <= k <= r || throw(ArgumentError("Need 1 <= r <= Ns and 0 <= k <= r."))
    counts = zeros(Int,p.Nk)
    for mask in generate_masks(p.Ns,NA)
        admissible = all(0:p.Ns-1) do start
            sum(Int((mask >> mod(start+j,p.Ns)) & one(mask)) for j in 0:r-1) <= k
        end
        admissible && (counts[ksum_mask(p,mask)+1] += 1)
    end
    return (momenta=collect(zip(p.kk1A,p.kk2A)),counts=counts,total_count=sum(counts))
end

"""Threshold/count diagnostics; automatic gaps use positive eigenvalues only."""
function pes_threshold(levels; mode::Symbol=:none, threshold=nothing, given_count=nothing, min_gap::Real=0.0)
    finite = sort(filter(isfinite, reduce(vcat,levels; init=Float64[])))
    isfinite(min_gap) && min_gap >= 0 || throw(ArgumentError("PES min_gap must be finite and nonnegative."))
    if mode == :none
        return (threshold=nothing, gap=nothing, counts=nothing, total_count=nothing)
    elseif mode == :manual
        threshold isa Real && isfinite(threshold) || throw(ArgumentError("Manual PES threshold must be finite."))
        gap = nothing
    elseif mode == :given_count
        given_count isa Integer && 1 <= given_count < length(finite) ||
            throw(ArgumentError("given_count must lie strictly between zero and the finite PES dimension."))
        gap = finite[given_count+1]-finite[given_count]
        threshold = (finite[given_count+1]+finite[given_count])/2
    elseif mode == :auto_gap
        gaps = diff(finite)
        if isempty(gaps) || maximum(gaps) <= min_gap
            return (threshold=nothing, gap=nothing, counts=nothing, total_count=nothing)
        end
        i = argmax(gaps)
        gap = gaps[i]; threshold = (finite[i]+finite[i+1])/2
    else
        throw(ArgumentError("PES threshold mode must be none, manual, given_count or auto_gap."))
    end
    counts = [count(x -> x < threshold,es) for es in levels]
    return (threshold=threshold, gap=gap, counts=counts, total_count=sum(counts))
end

"""
    pes_spectrum(para, parents, NA; holes=false, threaded=true, ...)

Compute a trace-one PES of an equal incoherent parent-state mixture. Levels
are sorted ascending within each zero-based sector. Eigenvalues <= zero_tol
are null modes: `levels` contains Inf and JSON `levels` contains null there.
`display_levels` applies level_floor for plots only. No null eigenvalue is
used to infer an automatic finite gap. Negative eigenvalues beyond the
positivity tolerance or a nonunit trace are errors, not silently repaired.
"""
function pes_spectrum(para::EDPara, parents::AbstractVector{<:MBS64Vector}, NA::Int;
    holes::Bool=false, threaded::Bool=true, memory_budget_bytes::Union{Nothing,Integer}=nothing,
    verbose::Bool=false, zero_tol::Real=1e-14, level_floor::Real=1e-15,
    threshold_mode::Symbol=:none, threshold=nothing, given_count=nothing,
    expected_counts=nothing, gap_min::Real=0.5, auto_min_gap::Real=0.0)
    isfinite(zero_tol) && 0 <= zero_tol < 1 || throw(ArgumentError("PES zero_tol must be in [0,1)."))
    isfinite(level_floor) && 0 < level_floor < 1 || throw(ArgumentError("PES level_floor must be in (0,1)."))
    p, vectors, sectors = prepare_pes_parents(para, parents)
    values = particle_entanglement_eigenvalues(p,vectors,sectors,PESParams(p,NA,holes);
        threaded, memory_budget_bytes, verbose)
    trace = sum(sum,values)
    minimum_value = minimum(minimum(v) for v in values if !isempty(v))
    isapprox(trace,1; atol=1e-9,rtol=1e-9) || error("PES trace is $(trace), expected one.")
    minimum_value >= -1e-10 || error("PES RDM is not positive: minimum eigenvalue $(minimum_value).")
    levels = [sort([v > zero_tol ? -log(v) : Inf for v in sector]) for sector in values]
    display_levels = [sort(-log.(max.(sector,level_floor))) for sector in values]
    counts = expected_counts === nothing ? nothing : pes_counting_gap(levels,expected_counts; gap_min)
    diagnostic = pes_threshold(levels; mode=threshold_mode,threshold,given_count,min_gap=auto_min_gap)
    return (NA=NA, holes=holes, N=p.N, Ns=p.Ns, parent_sectors=sectors,
        momenta=collect(zip(p.kk1A,p.kk2A)), eigenvalues=values, levels=levels,
        display_levels=display_levels, dimensions=length.(values),
        ranks=[count(>(zero_tol),v) for v in values], trace=trace,
        minimum_eigenvalue=minimum_value, zero_tol=Float64(zero_tol),
        level_floor=Float64(level_floor), threshold_mode=String(threshold_mode),
        threshold_diagnostic=diagnostic, counting_diagnostic=counts)
end

end
