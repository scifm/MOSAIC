# Momentum-resolved (1,3) Laughlin PES counts per cluster and N_A, in the
# solver's own subsystem-momentum order. The broker passes
# these as `extra.pes.expected_counts`; it refuses them unless the totals match
# N_phi/(N_phi-2N_A) * binomial(N_phi-2N_A, N_A).
#
#   julia --project=<snapshot>/julia scripts/pes_expected_counts.jl <snapshot> <cases.json> <out.json>
#
# cases.json: [{"name": "s21_NA2", "n_k": 21, "extra": {"symcluster": 1}, "NA": 2}, ...]
using JSON3

snapshot, cases_path, out_path = ARGS
include(joinpath(snapshot, "julia", "src", "MoireSolver.jl"))
using .MoireSolver
using MomentumED: EDPara

out = Dict{String,Any}()
for case in JSON3.read(read(cases_path, String))
    extra = Dict{String,Any}(string(k) => v for (k, v) in pairs(case[:extra]))
    k_list, Gk = MoireSolver.build_kmesh(extra, Int(case[:n_k]))
    para = EDPara(; k_list = k_list, Gk = Gk)
    r = MoireSolver.pes_admissible_counts(para, Int(case[:NA]); k = 1, r = 3)
    out[string(case[:name])] = Dict("momenta" => [collect(m) for m in r.momenta], "counts" => r.counts,
                                    "total" => r.total_count, "Nk" => size(k_list, 2), "Gk" => collect(Gk))
    println(case[:name], ": total ", r.total_count)
end
open(out_path, "w") do io
    JSON3.pretty(io, out)
end
