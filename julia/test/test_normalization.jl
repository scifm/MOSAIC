# Acceptance: the orthonormaliser's Gram matrix is the q = 0 vertex,
# so the orthonormalised trial band has unit norm at every k.
#
# Inputs are real archived configurations (copied under test/data/) plus a
# synthetic LL-mixed 8-shell case, covering the regime where the pre-fix
# solver ran 0.95–1.15.

using JSON3
using LinearAlgebra

const MS = MoireSolver

function tff_from_input(path::String)
    raw = JSON3.read(read(path, String))
    a_n = MS.decode_a_n(raw[:wavefunction])
    glist, w = MS.decode_W_G(raw[:form_factor])
    extra = Dict{String,Any}(string(k) => v for (k, v) in pairs(raw[:ed_solver_params][:extra]))
    lat = MS.lattice_from_extra(extra)
    lm = [(abs2(a_n[n + 1]), n) for n in 0:length(a_n) - 1]
    return MS.TrialFormFactor(glist, w, lat, lm), lat, glist, w
end

function cart(lat, f1, f2)
    return (f1 * real(lat.G1) + f2 * real(lat.G2), f1 * imag(lat.G1) + f2 * imag(lat.G2))
end

@testset "unit norm of the orthonormalised band" begin
    datadir = joinpath(@__DIR__, "data")
    # ED-input fixtures only (nk*.json); other JSON files in data/ are kernel fixtures
    inputs = filter(f -> startswith(basename(f), "nk") && endswith(f, ".json"), readdir(datadir; join = true))
    @test length(inputs) >= 3
    for path in inputs
        tff, lat, glist, w = tff_from_input(path)
        worst = 0.0
        worst_gram = 0.0
        for i in 0:7, j in 0:7
            k = cart(lat, i / 8 + 0.013, j / 8 + 0.021)   # off-mesh points too
            worst = max(worst, abs(MS.formfactor(tff, k, k, (0, 0)) - 1))
            # the Gram matrix IS the q = 0 vertex, entry by entry
            S = MS.raw_overlap_matrix(k, tff.nmax, glist, w, lat)
            F = MS.raw_formfactor_matrix(k, k, (0, 0), tff.nmax, glist, w, lat)
            worst_gram = max(worst_gram, maximum(abs.(S .- F)))
            # and the orthonormalised tower is orthonormal in that metric
            U = MS.get_U(tff, k)
            @test maximum(abs.(U' * F * U - I)) < 1e-10
        end
        @test worst < 1e-12
        @test worst_gram < 1e-14
    end
end
