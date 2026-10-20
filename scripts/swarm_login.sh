#!/bin/bash
# Login-node side of a swarm: one tmux session with the
# broker (sole Slurm submitter and store writer) and the supervisor (resubmits
# agent allocations). Both are small; the agents themselves never run here.
#   usage: scripts/swarm_login.sh configs/swarm_pilot.yaml
# Check the login cgroup first: `cat /sys/fs/cgroup/user.slice/user-$(id -u).slice/memory.{max,current}`.
set -euo pipefail
CONFIG="$(realpath "$1")"
MAIN="$(cd "$(dirname "$0")/.." && pwd)"
ID=$(uv run --project "$MAIN" --no-sync python -c "import sys; from swarm.config import load_swarm; print(load_swarm(sys.argv[1]).swarm_id)" "$CONFIG")
S="swarm-$ID"
tmux has-session -t "$S" 2>/dev/null && { echo "tmux session $S already exists"; exit 1; }
# The broker exits 3 on HALT and is then not restarted; any other exit is
# restarted after 60 s (its state is all on disk).
tmux new-session -d -s "$S" -n broker \
  "cd '$MAIN'; until uv run --no-sync python -m mosaic.swarm broker --config '$CONFIG'; [ \$? -eq 3 ]; do echo 'broker exited; restarting in 60 s'; sleep 60; done; echo 'broker halted'; exec bash"
tmux new-window -t "$S" -n supervise \
  "cd '$MAIN'; uv run --no-sync python -m mosaic.swarm supervise --config '$CONFIG' --interval 120; exec bash"
echo "started tmux session $S (windows: broker, supervise)"
