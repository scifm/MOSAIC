"""Helpers for solving only one many-body momentum sector per symmetry orbit."""

function normalize_ed_sector_mode(mode)::Symbol
    value = Symbol(lowercase(String(mode)))
    if value in (:full_ed, :full, :all, :all_sectors)
        return :full_ed
    elseif value in (:symmetry_reduced_ed, :symmetry_reduced, :unique_sectors)
        return :symmetry_reduced_ed
    end
    throw(ArgumentError(
        "unsupported ED mode $(mode); use full_ed or symmetry_reduced_ed"
    ))
end

function _lattice_metric(lattice::Symbol)
    lattice === :triangular && return [2 -1; -1 2]
    lattice === :square && return [1 0; 0 1]
    throw(ArgumentError("unsupported lattice $(lattice) for sector symmetry"))
end

"Return reciprocal-basis point-group matrices, with the identity first."
function lattice_point_group(lattice::Symbol; include_reflections::Bool = true)
    metric = _lattice_metric(lattice)
    identity = [1 0; 0 1]
    operations = Matrix{Int}[]
    for r11 in -1:1, r12 in -1:1, r21 in -1:1, r22 in -1:1
        R = [r11 r12; r21 r22]
        detR = r11 * r22 - r12 * r21
        abs(detR) == 1 || continue
        include_reflections || detR == 1 || continue
        transpose(R) * metric * R == metric || continue
        push!(operations, R)
    end
    sort!(operations; by = R -> R == identity ? (0, 0, 0, 0, 0) :
        (1, R[1, 1], R[1, 2], R[2, 1], R[2, 2]))
    return operations
end

function _sector_permutation(
    sector_momenta::AbstractVector,
    Gk::NTuple{2,<:Integer},
    R::AbstractMatrix{<:Integer},
)
    index_of = Dict((Int(k[1]), Int(k[2])) => i for (i, k) in enumerate(sector_momenta))
    permutation = Vector{Int}(undef, length(sector_momenta))
    for (i, k) in enumerate(sector_momenta)
        q1 = Int(k[1]) // Int(Gk[1])
        q2 = Int(k[2]) // Int(Gk[2])
        image1 = R[1, 1] * q1 + R[1, 2] * q2
        image2 = R[2, 1] * q1 + R[2, 2] * q2
        grid1 = image1 * Gk[1]
        grid2 = image2 * Gk[2]
        denominator(grid1) == 1 && denominator(grid2) == 1 || return nothing
        key = (mod(Int(numerator(grid1)), Gk[1]), mod(Int(numerator(grid2)), Gk[2]))
        target = get(index_of, key, 0)
        target == 0 && return nothing
        permutation[i] = target
    end
    return permutation
end

function _sector_orbits(n::Int, permutations::AbstractVector)
    unseen = Set(1:n)
    orbits = Vector{Vector{Int}}()
    while !isempty(unseen)
        seed = minimum(unseen)
        orbit = Set([seed])
        frontier = [seed]
        while !isempty(frontier)
            point = pop!(frontier)
            for permutation in permutations
                image = permutation[point]
                if !(image in orbit)
                    push!(orbit, image)
                    push!(frontier, image)
                end
            end
        end
        values = sort(collect(orbit))
        push!(orbits, values)
        foreach(point -> delete!(unseen, point), values)
    end
    return orbits
end

"""
    ed_sector_plan(sector_momenta, Gk; mode, lattice, include_reflections)

Return indices of sectors to diagonalize and a representative index for every
result sector. The full result always retains every original momentum sector.
"""
function ed_sector_plan(
    sector_momenta::AbstractVector,
    Gk::NTuple{2,<:Integer};
    mode = :full_ed,
    lattice::Symbol = :triangular,
    include_reflections::Bool = true,
)
    sector_mode = normalize_ed_sector_mode(mode)
    nsectors = length(sector_momenta)
    if sector_mode === :full_ed
        indices = collect(1:nsectors)
        return (
            sector_mode = sector_mode,
            solve_indices = indices,
            representative_index = indices,
            orbits = [[i] for i in indices],
            operation_count = 1,
        )
    end

    permutations = Vector{Vector{Int}}()
    operations = lattice_point_group(lattice; include_reflections = include_reflections)
    for R in operations
        permutation = _sector_permutation(sector_momenta, Gk, R)
        permutation === nothing || push!(permutations, permutation)
    end
    isempty(permutations) && push!(permutations, collect(1:nsectors))

    orbits = _sector_orbits(nsectors, permutations)
    representatives = Vector{Int}(undef, nsectors)
    for orbit in orbits
        representative = first(orbit)
        representatives[orbit] .= representative
    end
    return (
        sector_mode = sector_mode,
        solve_indices = first.(orbits),
        representative_index = representatives,
        orbits = orbits,
        operation_count = length(permutations),
    )
end
