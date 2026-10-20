#!/usr/bin/env julia
# Moire FCI ED driver.
#
# CLI contract (relied on by `jobs/swarm_pool.sbatch`):
#
#   julia --project=<julia_dir> ed_solver.jl --config IN.json --out OUT.json
#
# - IN.json conforms to `src/mosaic/ed/contract.py` `EDInput` (v1 schema).
# - OUT.json conforms to `EDOutput` with the many-body convention:
#   `epsilon_*` and `u_k` are null; `chern_solver` and
#   `gap_top_indirect_solver` are authoritative.
#
# Physics:
# - `W_G` are Fourier coefficients of `|h(r)|² = Σ_G w_G exp(i G r)`,
#   the density modulation of the trial band; the envelope `h(r)` is
#   never stored. `w_0 = 1`, `w_{-G} = w_G*`.
# - Trial single-particle Bloch state at momentum k is built from the
#   Cholesky-orthonormalised LL tower:
#   `|ψ_k> = Σ_n a_n |φ^orth_{n,k}>` (diagonal LL-mix weights).
# - The projected two-body interaction uses
#       V(kf1,kf2,ki2,ki1) = Σ_Q λ^MC_Q(kf1,ki1) λ^MC_{-Q}(kf2,ki2) V_Coulomb(|q|)
#   with the gate-screened Coulomb kernel of the Landau-level torus
#   example of MomentumED.jl (Zou Bo).
# - `MomentumED.EDsolve` per momentum block; Δ_top = E_first_excited −
#   max(E_GS_manifold) where the GS manifold has m states, the denominator
#   q of ν = p/q (`extra.gs_degeneracy` overrides it, e.g. 6 for Moore–Read).
# - Many-body Chern from a Wilson loop on a tracked GS via twisted-BC
#   re-solves.
#
# Any error during the solve is caught and surfaced as a
# failed_transient (engine-level) or failed_logical (physics-level)
# JSON output, so the Python orchestrator can route correctly.

using ArgParse
using JSON3
using LinearAlgebra
using Printf

push!(LOAD_PATH, joinpath(@__DIR__, "src"))

# MoireSolver is self-contained (w_G of |h|² model). It uses MomentumED for
# the ED engine but builds its own form factor (Cholesky-orthonormalised LL
# tower), so the LLT example module is no longer needed.
using MomentumED

include(joinpath(@__DIR__, "src", "MoireSolver.jl"))
using .MoireSolver

# --- CLI ---------------------------------------------------------------------

function parse_cli()
    s = ArgParseSettings()
    @add_arg_table! s begin
        "--config"
            help = "Path to ed_input.json (EDInput v1)."
            required = true
        "--out"
            help = "Path to write ed_output.json (EDOutput v1)."
            required = true
    end
    return parse_args(s)
end

# --- Driver ------------------------------------------------------------------

include(joinpath(@__DIR__, "ed_driver.jl"))

function main()
    args = parse_cli()
    return run_eval(args["config"], args["out"])
end

main()
