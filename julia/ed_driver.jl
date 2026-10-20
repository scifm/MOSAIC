# One-evaluation driver shared by `ed_solver.jl` (one config per process) and
# `ed_batch.jl` (many configs per process, JIT paid once).
# Expects `MoireSolver` and `JSON3` in scope.

"""
Run one evaluation: read `config_path`, write `out_path` (EDOutput JSON).
Solver errors become failure outputs; returns 0.
"""
function run_eval(config_path::AbstractString, out_path::AbstractString)
    t_start = time()
    ed_input_raw = nothing
    config_hash = "unknown"
    n_k = 0
    energy_unit = "meV"
    solver_version = MoireSolver.SOLVER_VERSION

    try
        ed_input_raw = JSON3.read(read(config_path, String))
    catch e
        # Cannot even read input → treat as transient (orchestrator retries
        # or surfaces).
        out = MoireSolver.transient_failure_output(
            "io_error",
            "failed to parse $(config_path): $(typeof(e))";
            config_hash=config_hash,
            n_k=n_k,
            energy_unit=energy_unit,
            solver_version=solver_version,
            compute_seconds=time() - t_start,
        )
        write_output_json(out, out_path)
        return 0
    end

    config_hash = String(get(ed_input_raw, :config_hash, "unknown"))
    n_k = Int(get(ed_input_raw[:lattice], :n_k, 0))
    energy_unit = String(get(ed_input_raw, :energy_unit, "meV"))

    try
        result = MoireSolver.solve(ed_input_raw; t_start=t_start)
        write_output_json(result, out_path)
    catch e
        bt = sprint(showerror, e, catch_backtrace())
        @warn "solver raised" bt
        # Distinguish: out-of-memory or other engine-level transient vs
        # logical bug. Default to transient so the orchestrator can retry.
        kind, reason = MoireSolver.classify_exception(e)
        if kind == :logical
            out = MoireSolver.logical_failure_output(
                reason, sprint(showerror, e);
                config_hash=config_hash,
                n_k=n_k,
                energy_unit=energy_unit,
                solver_version=solver_version,
                compute_seconds=time() - t_start,
            )
        else
            out = MoireSolver.transient_failure_output(
                reason, sprint(showerror, e);
                config_hash=config_hash,
                n_k=n_k,
                energy_unit=energy_unit,
                solver_version=solver_version,
                compute_seconds=time() - t_start,
            )
        end
        write_output_json(out, out_path)
    end

    return 0
end

function write_output_json(out::Dict, path::AbstractString)
    tmp = path * ".tmp"
    open(tmp, "w") do f
        JSON3.pretty(f, out)
    end
    mv(tmp, path; force=true)
end

