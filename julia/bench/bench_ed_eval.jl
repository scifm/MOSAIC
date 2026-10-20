# Eval-level benchmark/validation of the solver settings.
#
#   julia -t T --project=julia scripts/bench_ed_eval.jl OUT.jsonl LABEL IN.json \
#         backends=cpu,gpu accuracy=confirm,search [filling=2/3] [reps=2]
#
# Runs MoireSolver.solve end to end for every backend × accuracy, `reps`
# times in this one process (rep 1 includes compilation, later reps do not),
# and appends one JSON row per run: compute seconds, gap, Chern (glued raw,
# residual, plaquette), low energies, and the solver's ed_solver_stats.

using JSON3, Printf, LinearAlgebra
using MomentumED
include(joinpath(@__DIR__, "..", "julia", "src", "MoireSolver.jl"))
using .MoireSolver

outpath, label, inpath = ARGS[1], ARGS[2], ARGS[3]
kv = Dict(split(a, "=")[1] => split(a, "=")[2] for a in ARGS[4:end])
backends = split(get(kv, "backends", "cpu,gpu"), ",")
accs = split(get(kv, "accuracy", "confirm,search"), ",")
reps = parse(Int, get(kv, "reps", "2"))
parse_ratio(s) = occursin("/", s) ? (p = split(s, "/"); parse(Int, p[1]) / parse(Int, p[2])) : parse(Float64, s)

base = JSON3.read(read(inpath, String), Dict{String,Any})
haskey(kv, "filling") && (base["ed_solver_params"]["filling"] = parse_ratio(kv["filling"]))
for (k, v) in kv
    startswith(k, "x.") && (base["ed_solver_params"]["extra"][k[3:end]] = tryparse(Int, v) === nothing ? v : parse(Int, v))
end

open(outpath, "a") do io
    for b in backends, acc in accs, r in 1:reps
        d = deepcopy(base)
        d["ed_solver_params"]["extra"]["ed_accuracy"] = acc
        t0 = time()
        out = withenv("MOIRE_ED_BACKEND" => b) do
            MoireSolver.solve(JSON3.read(JSON3.write(d)); t_start = time())
        end
        wall = time() - t0
        row = Dict{Symbol,Any}(:label => label, :backend_req => b, :accuracy => acc, :rep => r,
                               :wall => wall, :threads => Threads.nthreads())
        for k in (:status, :failure_reason, :gap_top_indirect_solver, :chern_solver, :chern_glued_raw,
                  :chern_glued_residual, :chern_plaquette_raw, :chern_max_plaquette_phase,
                  :gs_manifold_splitting, :low_energies, :sector_momenta, :ed_backend,
                  :ed_solver_stats, :compute_seconds)
            row[k] = get(out, k, nothing)
        end
        println(io, JSON3.write(row)); flush(io)
        st = out[:ed_solver_stats]
        @printf("%-8s %-4s %-7s rep %d  %7.1f s  %-10s gap %.10f  C %s  glued %s  matvecs %s  maxres %s\n",
                label, b, acc, r, wall, out[:status], something(out[:gap_top_indirect_solver], NaN),
                string(out[:chern_solver]), string(get(out, :chern_glued_raw, nothing)),
                st === nothing ? "-" : string(st[:matvecs]), st === nothing ? "-" : @sprintf("%.1e", st[:max_residual]))
    end
end
