#!/bin/bash
# Agent allocation for one swarm arm, rendered by
# `swarm setup`. Runs every agent of arm `{arm}` as an interactive Claude Code
# session in a detached tmux server on this node, one window per agent, so the
# sessions survive any terminal disconnecting and stay off the login node.
#   attach: srun --jobid=$SLURM_JOB_ID --overlap --pty tmux -L {socket} attach -t {arm}
# The job ends when every agent has written `done`, or at walltime; the
# login-node supervisor (`swarm supervise`) then resubmits it if agents remain,
# and each agent resumes its own session (scripts/swarm_agent.sh).
#SBATCH --job-name=swarm-agents-{arm}
#SBATCH --partition={partition}
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task={cpus}
#SBATCH --mem={mem}
#SBATCH --time={walltime}{extra_sbatch}
#SBATCH --output={arm_root}/agents_%j.log
#SBATCH --error={arm_root}/agents_%j.log
set -uo pipefail
CONFIG="{config}"
SOCK={socket}
echo "[$(date -Iseconds)] agents job $SLURM_JOB_ID on $(hostname): {agents}"
tmux -L $SOCK kill-server 2>/dev/null
first=1
i=0
for a in {agents}; do
  # Staggered starts ({stagger} s apart): later agents read earlier plans first.
  cmd="sleep $((i * {stagger})); bash {repo_main}/scripts/swarm_agent.sh '$CONFIG' $a"
  i=$((i + 1))
  if [ $first -eq 1 ]; then
    tmux -L $SOCK new-session -d -s {arm} -n "$a" -x 220 -y 60 "$cmd"
    first=0
  else
    tmux -L $SOCK new-window -t "{arm}:" -n "$a" "$cmd"   # "arm:" = next free index
  fi
done
while tmux -L $SOCK has-session -t {arm} 2>/dev/null; do
  left=0
  for a in {agents}; do [ -f "{arm_root}/agents/$a/done" ] || left=$((left + 1)); done
  [ $left -eq 0 ] && break
  sleep 60
done
echo "[$(date -Iseconds)] agents job $SLURM_JOB_ID: $left agents not done; stopping tmux"
tmux -L $SOCK kill-server 2>/dev/null
