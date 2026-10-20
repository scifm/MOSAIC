#!/usr/bin/env julia
# Persistent ED worker: runs every unclaimed run directory matching
# a glob in ONE Julia process, so compilation (~20 s per process on the GPU
# path) is paid once per lane instead of once per config.
#
#   julia --project=julia ed_batch.jl ROOT 'PATTERN'
#
# Per directory, the same protocol as the shell bundles: skip when
# ed_output.json exists; claim with `mkdir .claimed` (atomic on NFS, so several
# workers and shell lanes share one run list); write job_id.txt; run
# `run_eval` with this evaluation's log in its own solver.log; release the
# claim if no output appeared. Each config is still one ed_input.json →
# one ed_output.json, so orchestration and resubmission are unchanged.
# The glob is read once at start (no polling); symlinked run directories work.
# The claim directory holds `job` (the Slurm job id) for dead-claim detection.

using ArgParse
using JSON3
using Logging
using LinearAlgebra
using Printf

using MomentumED
include(joinpath(@__DIR__, "src", "MoireSolver.jl"))
using .MoireSolver
include(joinpath(@__DIR__, "ed_driver.jl"))

function glob_dirs(root::AbstractString, pattern::AbstractString)
    rx = Regex("^" * replace(pattern, "." => "\\.", "*" => ".*", "?" => ".") * "\$")
    return sort([joinpath(root, d) for d in readdir(root) if occursin(rx, d) && isdir(joinpath(root, d))])
end

function main()
    root, pattern = ARGS[1], ARGS[2]
    job = get(ENV, "SLURM_JOB_ID", "local")
    n_done = 0
    for d in glob_dirs(root, pattern)
        out = joinpath(d, "ed_output.json")
        isfile(out) && continue
        claim = joinpath(d, ".claimed")
        try
            mkdir(claim)
        catch
            continue                          # another lane has it
        end
        t0 = time()
        try
            write(joinpath(claim, "job"), job * "\n")   # for brokers that detect dead claims
            write(joinpath(d, "job_id.txt"), job * "\n")
            println("[", Libc.strftime("%FT%T", time()), "] start ", basename(d),
                    get(ENV, "CUDA_VISIBLE_DEVICES", "") == "" ? "" : " on GPU " * ENV["CUDA_VISIBLE_DEVICES"])
            flush(stdout)
            open(joinpath(d, "solver.log"), "w") do io
                with_logger(ConsoleLogger(io, Logging.Info)) do
                    run_eval(joinpath(d, "ed_input.json"), out)
                end
            end
        catch e
            # run_eval already turns solver errors into failure outputs; this is
            # for anything around it (I/O). Release the claim and move on.
            println("[", Libc.strftime("%FT%T", time()), "] worker error on ", basename(d), ": ", sprint(showerror, e))
        end
        isfile(out) || rm(claim; force = true, recursive = true)
        n_done += 1
        @printf("[%s] done %s (%.1f s)\n", Libc.strftime("%FT%T", time()), basename(d), time() - t0)
        flush(stdout)
    end
    println("worker finished: $(n_done) evaluations")
    return 0
end

main()
