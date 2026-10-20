#!/bin/bash
# One swarm agent inside its arm's allocation.
# Keeps the agent's Claude Code session alive until the agent writes `done`:
# the first launch creates the session under its fixed uuid, later launches
# (after a crash, an exit, or a new allocation) resume the same session.
#   usage: swarm_agent.sh CONFIG AGENT
set -uo pipefail
CONFIG=$1 AGENT=$2
MAIN="$(cd "$(dirname "$0")/.." && pwd)"
eval "$(uv run --project "$MAIN" --no-sync python -m mosaic.swarm agent-env --config "$CONFIG" --agent "$AGENT")" || exit 1
export PATH="$MAIN/swarm/bin:$PATH"
# Use the claude.ai login, not an API key inherited from ~/.bashrc (config:
# agent_job.unset_api_key).
[ -n "$SWARM_UNSET_API_KEY" ] && unset ANTHROPIC_API_KEY
cd "$SWARM_WORKTREE" || exit 1
CHARTER="$SWARM_WORKTREE/CHARTER.md"
# The agent and everything it runs live in a bubblewrap mount namespace in which the config's
# agent_deny_read paths (other campaigns, other Claude transcript folders, the main checkout's
# results) are empty. Rebuilt at each launch, since campaigns come and go. If the sandbox cannot
# be built the agent is not launched, never launched without it.
sandbox() {
  local hide k p
  hide=$(uv run --project "$MAIN" --no-sync python -m mosaic.swarm sandbox-hide --config "$CONFIG") || return 1
  BWRAP=(bwrap --dev-bind / / --die-with-parent)
  while read -r k p; do
    case $k in d) BWRAP+=(--tmpfs "$p") ;; f) BWRAP+=(--ro-bind /dev/null "$p") ;; esac
  done <<< "$hide"
  "${BWRAP[@]}" -- true
}
while [ ! -f "$SWARM_AGENT_DIR/done" ]; do
  if ! sandbox; then
    echo "[$(date -Iseconds)] $AGENT: sandbox failed; not launching (retry in 5 min)" | tee -a "$SWARM_AGENT_DIR/launches.log"
    sleep 300; continue
  fi
  if [ -f "$SWARM_AGENT_DIR/started" ]; then
    session=(--resume "$SWARM_SESSION_UUID")
  else
    session=(--session-id "$SWARM_SESSION_UUID")
    date -Iseconds > "$SWARM_AGENT_DIR/started"
  fi
  model=(); [ -n "$SWARM_MODEL" ] && model=(--model "$SWARM_MODEL")
  echo "[$(date -Iseconds)] $AGENT: launching (${session[0]}) on $(hostname), sandbox hides $(( (${#BWRAP[@]} - 4) / 2 )) paths" | tee -a "$SWARM_AGENT_DIR/launches.log"
  t0=$(date +%s)
  "${BWRAP[@]}" -- "$SWARM_CLAUDE" "${session[@]}" --name "$AGENT" --permission-mode "$SWARM_PERMISSION_MODE" "${model[@]}" \
    --append-system-prompt "$(cat "$CHARTER")" "$SWARM_PROMPT"
  rc=$?
  echo "[$(date -Iseconds)] $AGENT: claude exited rc=$rc after $(( $(date +%s) - t0 )) s" | tee -a "$SWARM_AGENT_DIR/launches.log"
  # A resume that dies at once means there is no transcript to resume
  # (the first launch never got going): start the session fresh next time.
  if [ "${session[0]}" = "--resume" ] && [ $(( $(date +%s) - t0 )) -lt 15 ]; then
    rm -f "$SWARM_AGENT_DIR/started"
  fi
  [ -f "$SWARM_AGENT_DIR/done" ] || sleep 30
done
echo "[$(date -Iseconds)] $AGENT: done" | tee -a "$SWARM_AGENT_DIR/launches.log"
