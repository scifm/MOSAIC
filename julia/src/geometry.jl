"""
Finite momentum-cluster builders.

The symmetric-cluster table is adapted from the authors' earlier ED code.
The integer coordinates represent fractional momenta
`(kk1 / denominator1, kk2 / denominator2)` in the reciprocal basis.
"""

const SYMMETRIC_CLUSTER_DATA = Dict{Int,NamedTuple}(
    7 => (denominator = (7, 7),
          kk1 = [0, 3, 6, 2, 5, 1, 4],
          kk2 = [0, 1, 2, 3, 4, 5, 6]),
    9 => (denominator = (3, 3),
          kk1 = [0, 1, 2, 0, 1, 2, 0, 1, 2],
          kk2 = [0, 0, 0, 1, 1, 1, 2, 2, 2]),
    12 => (denominator = (6, 6),
           kk1 = [0, 3, 2, 5, 1, 4, 0, 3, 2, 5, 1, 4],
           kk2 = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]),
    13 => (denominator = (13, 13),
           kk1 = [0, 4, 8, 12, 3, 7, 11, 2, 6, 10, 1, 5, 9],
           kk2 = collect(0:12)),
    14 => (denominator = (7, 14),
           kk1 = [0, 3, 6, 2, 5, 1, 4, 0, 3, 6, 2, 5, 1, 4],
           kk2 = collect(0:13)),
    15 => (denominator = (3, 15),
           kk1 = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2],
           kk2 = collect(0:14)),
    18 => (denominator = (9, 18),
           kk1 = [0, 4, 8, 3, 7, 2, 6, 1, 5, 0, 4, 8, 3, 7, 2, 6, 1, 5],
           kk2 = collect(0:17)),
    20 => (denominator = (4, 20),
           kk1 = [0, 3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1],
           kk2 = collect(0:19)),
    21 => (denominator = (21, 21),
           kk1 = [0, 5, 10, 15, 20, 4, 9, 14, 19, 3, 8, 13, 18, 2, 7, 12, 17, 1, 6, 11, 16],
           kk2 = collect(0:20)),
    22 => (denominator = (11, 22),
           kk1 = [0, 7, 3, 10, 6, 2, 9, 5, 1, 8, 4, 0, 7, 3, 10, 6, 2, 9, 5, 1, 8, 4],
           kk2 = collect(0:21)),
    24 => (denominator = (6, 24),
           kk1 = [0, 5, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1],
           kk2 = collect(0:23)),
    26 => (denominator = (26, 13),
           kk1 = [0, 13, 7, 20, 1, 14, 8, 21, 2, 15, 9, 22, 3, 16, 10, 23, 4, 17, 11, 24, 5, 18, 12, 25, 6, 19],
           kk2 = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]),
    27 => (denominator = (9, 9),
           kk1 = [0, 3, 6, 2, 5, 8, 1, 4, 7, 0, 3, 6, 2, 5, 8, 1, 4, 7, 0, 3, 6, 2, 5, 8, 1, 4, 7],
           kk2 = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8]),
    28 => (denominator = (14, 14),
           kk1 = [0, 7, 5, 12, 3, 10, 1, 8, 6, 13, 4, 11, 2, 9, 0, 7, 5, 12, 3, 10, 1, 8, 6, 13, 4, 11, 2, 9],
           kk2 = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13]),
    36 => (denominator = (6, 6),
           kk1 = repeat(collect(0:5), 6),
           kk2 = repeat(collect(0:5), inner = 6)),
    39 => (denominator = (39, 39),
           kk1 = [0, 23, 7, 30, 14, 37, 21, 5, 28, 12, 35, 19, 3, 26, 10, 33, 17, 1, 24, 8, 31, 15, 38, 22, 6, 29, 13, 36, 20, 4, 27, 11, 34, 18, 2, 25, 9, 32, 16],
           kk2 = collect(0:38)),
)

supported_symmetric_clusters() = sort(collect(keys(SYMMETRIC_CLUSTER_DATA)))

function _symcluster_enabled(raw)::Bool
    raw isa Bool && return raw
    raw isa Integer && raw in (0, 1) && return raw == 1
    value = lowercase(String(raw))
    value in ("0", "false", "regular", "rectangular") && return false
    value in ("1", "true", "symmetric", "symmetry") && return true
    throw(ArgumentError("extra.symcluster must be 0/1 or false/true; got $(raw)"))
end

function build_symmetric_kmesh(n_k::Int)
    data = get(SYMMETRIC_CLUSTER_DATA, n_k, nothing)
    data === nothing && throw(ArgumentError(
        "unsupported symmetric cluster Nk=$(n_k); supported Nk values are " *
        join(supported_symmetric_clusters(), ", ")
    ))
    k_list = Matrix{Int}(undef, 2, n_k)
    k_list[1, :] .= data.kk1
    k_list[2, :] .= data.kk2
    return k_list, data.denominator
end

function build_regular_kmesh(extra::AbstractDict, n_k::Int)
    nk1_raw = get(extra, "nk1", nothing)
    nk2_raw = get(extra, "nk2", nothing)
    if nk1_raw !== nothing && nk2_raw !== nothing
        nk1, nk2 = Int(nk1_raw), Int(nk2_raw)
    else
        n_k <= 1 && error("lattice.n_k must be >= 2; got $(n_k)")
        nk1, nk2 = 1, n_k
        for f in 1:isqrt(n_k)
            if n_k % f == 0
                nk1 = f
                nk2 = n_k ÷ f
            end
        end
    end
    nk1 * nk2 == n_k || throw(ArgumentError(
        "extra.nk1 * extra.nk2 must equal lattice.n_k; got $(nk1) * $(nk2) != $(n_k)"
    ))

    k_list = Matrix{Int}(undef, 2, n_k)
    col = 1
    for k2 in 0:nk2 - 1, k1 in 0:nk1 - 1
        k_list[1, col] = k1
        k_list[2, col] = k2
        col += 1
    end
    return k_list, (nk1, nk2)
end

"""
    build_kmesh(extra, n_k)

Build the configured finite momentum cluster. `extra.symcluster = 1` selects
the symmetric-cluster table and takes precedence over `nk1`/`nk2`; the default
`symcluster = 0` preserves the previous rectangular behavior.
"""
function build_kmesh(extra::AbstractDict, n_k::Int)
    if _symcluster_enabled(get(extra, "symcluster", 0))
        return build_symmetric_kmesh(n_k)
    end
    return build_regular_kmesh(extra, n_k)
end
