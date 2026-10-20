#!/bin/bash
# Swarm pool job, rendered by mosaic.swarm.pool.render_pool_script.
# One allocation, {lanes} lanes. Each lane repeatedly takes the oldest entry in
# {pool_dir}, claims its run directory with an atomic mkdir (the same protocol
# as the 024 bundles and julia/ed_batch.jl), runs the pinned solver snapshot,
# and goes back to the pool. A lane stops when the pool has been empty for {idle_exit_seconds} s, or
# when the next evaluation could not finish before walltime. The broker reads
# .claimed/job (who holds it) and .claimed/rc (lane finished) to detect claims
# whose job died, and requeues them.
#SBATCH --job-name=swarm-{tier}
#SBATCH --partition={partition}
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task={cpus}
#SBATCH --mem={mem}
#SBATCH --time={walltime}{extra_sbatch}
#SBATCH --output={log_dir}/pool_%j.log
#SBATCH --error={log_dir}/pool_%j.log
set -uo pipefail
export JULIA_PROJECT="{julia_project}"
export OPENBLAS_NUM_THREADS={threads} OMP_NUM_THREADS={threads} MKL_NUM_THREADS={threads}
export JULIA_NUM_THREADS={threads}{backend_env}

POOL="{pool_dir}"
EST={est_run_seconds}
IDLE={idle_exit_seconds}
DEADLINE=$(( $(date +%s) + {wall_seconds} - 120 ))

# Pool entries are symlinks <stamp>_<hash> -> store/runs/<hash>.
unclaimed() {{
  local f
  for f in $(ls "$POOL" 2>/dev/null | sort); do
    [ -f "$POOL/$f/ed_input.json" ] && [ ! -f "$POOL/$f/ed_output.json" ] && [ ! -d "$POOL/$f/.claimed" ] && echo "$f"
  done
}}

# One solver process per evaluation (any solver version).
run_next_per_eval() {{
  local f d rc
  for f in $(unclaimed); do
    d="$POOL/$f"
    mkdir "$d/.claimed" 2>/dev/null || continue
    echo "$SLURM_JOB_ID" > "$d/.claimed/job"
    echo "[$(date -Iseconds)] lane $1 start $f${{CUDA_VISIBLE_DEVICES:+ GPU $CUDA_VISIBLE_DEVICES}}"
    "{julia}" "{solver}" --config "$d/ed_input.json" --out "$d/ed_output.json" > "$d/solver.log" 2>&1
    rc=$?
    echo "$rc" > "$d/.claimed/rc"
    echo "[$(date -Iseconds)] lane $1 done $f rc=$rc"
    return 0
  done
  return 1
}}

# One persistent worker per pass (solver >= v0.9.0, julia/ed_batch.jl): it walks
# a pass directory once, claiming with the same mkdir protocol, and compiles
# once. The pass holds only the first {pass_size} unclaimed entries in priority
# order: ed_batch.jl reads its list at start, so a pass over the whole pool
# would run hours on a stale order and skip entries renamed meanwhile.
run_next_persistent() {{
  local pass="${{TMPDIR:-/tmp}}/swarm_pass_${{SLURM_JOB_ID}}_$1" f
  rm -rf "$pass"; mkdir -p "$pass"
  for f in $(unclaimed | head -{pass_size}); do
    ln -s "$(readlink -f "$POOL/$f")" "$pass/$f"
  done
  [ -n "$(ls "$pass")" ] || {{ rm -rf "$pass"; return 1; }}
  echo "[$(date -Iseconds)] lane $1 persistent pass ($(ls "$pass" | wc -l))${{CUDA_VISIBLE_DEVICES:+ GPU $CUDA_VISIBLE_DEVICES}}"
  "{julia}" "{batch}" "$pass" '*'
  local rc=$?
  rm -rf "$pass"
  echo "[$(date -Iseconds)] lane $1 persistent pass done rc=$rc"
  return 0
}}

lane() {{
  local idle_since
  idle_since=$(date +%s)
  while :; do
    [ $(( $(date +%s) + EST )) -gt $DEADLINE ] && {{ echo "[$(date -Iseconds)] lane $1: walltime margin reached"; return; }}
    if run_next_{lane_mode} "$1"; then
      idle_since=$(date +%s)
    else
      [ $(( $(date +%s) - idle_since )) -gt $IDLE ] && {{ echo "[$(date -Iseconds)] lane $1: idle, exiting"; return; }}
      sleep {poll_seconds}
    fi
  done
}}

echo "[$(date -Iseconds)] pool job $SLURM_JOB_ID ({tier}) on $(hostname), {lanes} lanes"
{dispatch}
echo "[$(date -Iseconds)] pool job $SLURM_JOB_ID finished"
