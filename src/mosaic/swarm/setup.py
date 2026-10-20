"""Launch preparation and supervision.

``setup`` is idempotent and launches nothing: it creates the arm directories,
the pinned solver snapshot, one git worktree per agent with its permission
guardrails, rendered charter and notebook, a stable session uuid per agent,
and the Slurm script for each arm's agent allocation.

``supervise`` is the login-node loop that resubmits an arm's agent
allocation when it ends (walltime, node failure) while agents remain who
have not written ``done``.
"""

from __future__ import annotations

import hashlib
import shlex
import shutil
import subprocess
import time
import uuid
from pathlib import Path

from mosaic.swarm.config import REPO_ROOT, SwarmConfig, load_swarm
from mosaic.swarm.files import atomic_write_json, atomic_write_text, parse_iso, read_json, utc_iso
from mosaic.swarm.layout import ArmLayout
from mosaic.util.logging import get_logger

LOG = get_logger("swarm.setup")

AGENTS_TEMPLATE = REPO_ROOT / "jobs" / "swarm_agents.sbatch"
CHARTER_TEMPLATE = REPO_ROOT / "swarm" / "charter.md"

LOOP_PROMPT = ("/loop Continue your swarm work as your charter describes: run `swarm digest`, decide, act, "
               "append to NOTEBOOK.md, run `swarm heartbeat`, then pace your next wakeup. "
               "When your quota is spent or nothing is left to try, run `swarm done` and stop the loop.")

SHARED_RULES = """9. **Coordinate only through the board, the roster and mail.** Do not use
   `SendMessage`: it only reaches sessions on the same node and leaves no
   record. Substantive messages go to `swarm mail` or a post.
10. Read the open hypotheses before starting a family. If another agent has an
    open hypothesis on it, mail them or post why you are entering it.
11. About one post in five should be a critique of another agent's claim:
    conditioning, gates, finite size, the ADR-0035 basis, or whether it is a
    relabelling of a direction already measured. Mail the author as well.
12. Watch for herding. If most agents are converging on one family, ask
    whether an unexplored direction is the better use of your budget.
"""

PRIVATE_RULES = """9. You work independently. Your board is your own record; there is no
   roster or mail. Do not look for other agents' files or sessions.
"""


def render_charter(cfg: SwarmConfig, agent: str) -> str:
    L = ArmLayout(cfg, cfg.arm_of(agent))
    n = len(L.agents)
    banner = f"> **REHEARSAL.** {cfg.rehearsal_note}\n\n" if cfg.rehearsal_note else ""
    mission = ""
    if cfg.mission:
        mission = ("\n## The campaign brief\n\n" + cfg.path(cfg.mission).read_text().strip() + "\n")
    return banner + CHARTER_TEMPLATE.read_text().format(mission=mission,
        agent=agent, arm=L.arm, mode="private" if L.private else "shared",
        team_line=("an autonomous research agent working independently" if L.private
                   else f"one of {n} autonomous research agents who share a board,"),
        quota=cfg.quotas.evaluations_per_agent, in_flight=cfg.quotas.max_in_flight_per_agent,
        mail_tool="" if L.private else "\n    swarm mail --to AGENT --subject S < body.md   directed message to one agent",
        shared_rules=PRIVATE_RULES if L.private else SHARED_RULES,
        direction_section=_direction_section(cfg, agent, L.private),
    )


SELF_DIRECTED_SHARED = """## Choosing your own scope

Nobody assigns you a role or a region; the swarm organizes itself through the
board. On your first wakeup, before submitting anything:

1. Read the whole board (`swarm digest`, repeated until no backlog remains)
   and the leaderboard.
2. Decide what you will work on and post it as a `hypothesis`: the family or
   parameterization, its bounds, the method, the request budget you intend to
   spend, and why this is the best use of your budget given what is already
   claimed.
3. Prefer directions nobody covers. If you join one someone else has claimed,
   say what you add (a different method, a wider range, a check of their
   result) and mail them.

Roles are yours to choose and change: explorer, optimizer, verifier, ablation,
whatever the swarm needs most at that moment. Revisit your choice whenever the
board changes what is most useful, and post when you switch.
"""

SELF_DIRECTED_PRIVATE = """## Choosing your own scope

Nobody assigns you a role or a region. Decide what to work on, post it as a
`hypothesis` (family, bounds, method, intended budget, rationale) before your
first submission, and revise it as your results come in.
"""


def _direction_section(cfg: SwarmConfig, agent: str, private: bool) -> str:
    if agent in cfg.directions:
        return ("## Your starting direction\n\n" + cfg.path(cfg.directions[agent]).read_text().strip()
                + "\n\nThis is a starting point, not a territory. Move when the evidence says so,\n"
                  "and say why on the board.\n")
    return SELF_DIRECTED_PRIVATE if private else SELF_DIRECTED_SHARED


def permission_settings(cfg: SwarmConfig, agent: str) -> dict:
    """Guardrails, not a sandbox: Bash can still read anything. The real
    enforcement is the broker (validation, pinned solver, sole store writer)."""

    arm = cfg.arm_of(agent)
    L = ArmLayout(cfg, arm)

    def under(tool: str, p: Path) -> str:  # absolute paths take a leading "//"
        return f"{tool}(/{p}/**)"

    frozen = ["src", "julia", "configs", "docs", "jobs", "scripts", "swarm"]
    deny = [f"Edit(/{d}/**)" for d in frozen]
    # Every swarm file is written through the `swarm` command, never edited.
    deny.append(under("Edit", cfg.root_path))
    for other in cfg.arms:
        if other != arm:
            deny.append(under("Read", cfg.arm_root(other)))
    if L.private:
        for a in L.agents:
            if a != agent:
                deny += [under("Read", d) for d in (L.agent_dir(a), L.board_dir(a), L.inbox(a))]
    deny += [f"Read(/{cfg.path(d)})" if cfg.path(d).is_file() else under("Read", cfg.path(d)) for d in cfg.agent_deny_read]
    deny += [f"Bash({c} *)" for c in ("sbatch", "srun", "salloc", "scancel", "git push", "git commit",
                                        *cfg.agent_deny_bash)]
    allow = ["Bash(swarm *)", "Bash(uv run *)", "Edit(/work/**)", "Edit(/NOTEBOOK.md)"]
    return {"permissions": {"allow": allow, "deny": deny}}


def pin_manifest(main: Path, snapshot: Path) -> dict:
    """Freeze the solver's Julia environment in the snapshot. julia/deps/ (the
    patched MomentumED.jl from scripts/setup_solver.sh) is gitignored, so a git
    snapshot has none: copy it, so the snapshot never loads the live, editable
    packages. Then copy the main checkout's Manifest (the one the solver's tests
    ran with) and point any absolute path dependencies at the snapshot's copy."""

    deps = main / "julia" / "deps"
    if deps.exists() and not (snapshot / "julia" / "deps").exists():
        shutil.copytree(deps, snapshot / "julia" / "deps", ignore=shutil.ignore_patterns(".git"))
    src, dst = main / "julia" / "Manifest.toml", snapshot / "julia" / "Manifest.toml"
    if not src.exists():
        raise SystemExit(f"{src} not found; run scripts/setup_solver.sh first")
    text = src.read_text()
    rewritten = text.replace(f'path = "{main / "julia"}/', f'path = "{snapshot / "julia"}/')
    if f'"{main}/' in rewritten:
        raise SystemExit(f"{src} still references {main} after rewriting path deps; inspect it")
    if not dst.exists() or dst.read_text() != rewritten:
        atomic_write_text(dst, rewritten)
    return {"manifest_source_sha256": hashlib.sha256(text.encode()).hexdigest(),
            "manifest_sha256": hashlib.sha256(rewritten.encode()).hexdigest()}


def _git(*args: str, cwd: Path) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


def setup(cfg: SwarmConfig, config_path: Path, *, worktrees: bool = True, solver: bool = True) -> dict:
    main = Path(cfg.repo_main)
    report: dict = {"root": str(cfg.root_path), "arms": {}}
    cfg.root_path.mkdir(parents=True, exist_ok=True)
    from mosaic.swarm.parents import build_parents

    parents = build_parents(cfg)  # fails loudly on a bad parent (M2 checks are in the tests)
    if solver:
        if not cfg.solver_dir.exists():
            if cfg.worktree_repo:
                # Independent campaigns: a plain export, not a worktree, so nothing
                # under the campaign's worktree root links back to the main repository.
                cfg.solver_dir.mkdir(parents=True)
                subprocess.run(f"git archive {shlex.quote(cfg.broker.solver_ref)} | tar -x -C {shlex.quote(str(cfg.solver_dir))}",
                               shell=True, check=True, cwd=main)
            else:
                _git("worktree", "add", "--detach", str(cfg.solver_dir), cfg.broker.solver_ref, cwd=main)
        sha = _git("rev-parse", f"{cfg.broker.solver_ref}^{{commit}}", cwd=main)
        report["solver"] = {"dir": str(cfg.solver_dir), "sha": sha, **pin_manifest(main, cfg.solver_dir)}
        atomic_write_json(cfg.root_path / "solver.json", report["solver"])

    wt_repo = cfg.path(cfg.worktree_repo) if cfg.worktree_repo else main
    base_sha = _git("rev-parse", cfg.agent_base_ref, cwd=wt_repo) if worktrees else None
    for arm in cfg.arms:
        L = ArmLayout(cfg, arm)
        L.ensure()
        for name, ed in parents.items():
            atomic_write_text(L.root / "parents" / f"{name}.json", ed.model_dump_json(indent=1))
        arm_report = {}
        for agent in L.agents:
            ad = L.agent_dir(agent)
            sess = read_json(ad / "session.json")
            if sess is None:
                sess = {"uuid": str(uuid.uuid4()), "created": utc_iso()}
                atomic_write_json(ad / "session.json", sess)
            wt = cfg.worktree(agent)
            if worktrees:
                if not wt.exists():
                    _git("worktree", "add", "-b", f"swarm/{cfg.swarm_id}/{agent}", str(wt), base_sha, cwd=wt_repo)
                (wt / "work").mkdir(exist_ok=True)
                atomic_write_json(wt / ".claude" / "settings.local.json", permission_settings(cfg, agent))
                atomic_write_text(wt / "CHARTER.md", render_charter(cfg, agent))
                if not (wt / "NOTEBOOK.md").exists():
                    atomic_write_text(wt / "NOTEBOOK.md", f"# {agent} notebook\n\nStarted {utc_iso()}.\n")
            arm_report[agent] = {"worktree": str(wt), "session_uuid": sess["uuid"]}
        script = L.root / "agents_job.sbatch"
        atomic_write_text(script, render_agents_job(cfg, arm, config_path))
        report["arms"][arm] = {"agents": arm_report, "agents_job": str(script)}
    atomic_write_json(cfg.root_path / "setup.json", {**report, "at": utc_iso(), "base_sha": base_sha})
    return report


def render_agents_job(cfg: SwarmConfig, arm: str, config_path: Path) -> str:
    L = ArmLayout(cfg, arm)
    j = cfg.agent_job
    n = len(L.agents)
    return AGENTS_TEMPLATE.read_text().format(
        arm=arm, swarm_id=cfg.swarm_id, partition=j.partition, cpus=n * j.cpus_per_agent,
        mem=f"{n * j.mem_per_agent_gb}G", walltime=j.walltime, arm_root=L.root,
        agents=" ".join(L.agents), repo_main=cfg.repo_main, socket=f"swarm-{cfg.swarm_id}-{arm}",
        stagger=j.stagger_seconds,
        config=Path(config_path).resolve(),
        extra_sbatch=("\n#SBATCH --reservation=" + j.reservation if j.reservation else "")
        + ("\n#SBATCH --qos=" + j.qos if j.qos else ""),
    )


def agent_env(cfg: SwarmConfig, agent: str, config_path: Path) -> str:
    """Shell ``export`` lines for ``scripts/swarm_agent.sh``."""

    L = ArmLayout(cfg, cfg.arm_of(agent))
    sess = read_json(L.agent_dir(agent) / "session.json")
    if sess is None:
        raise SystemExit(f"{agent}: no session.json; run `swarm setup` first")
    j = cfg.agent_job
    env = {
        "SWARM_CONFIG": str(Path(config_path).resolve()), "SWARM_AGENT": agent,
        "MOIRE_MAIN": cfg.repo_main, "SWARM_AGENT_DIR": str(L.agent_dir(agent)),
        "SWARM_WORKTREE": str(cfg.worktree(agent)), "SWARM_SESSION_UUID": sess["uuid"],
        "SWARM_CLAUDE": j.claude, "SWARM_MODEL": j.model or "", "SWARM_PERMISSION_MODE": j.permission_mode,
        "SWARM_PROMPT": LOOP_PROMPT, "SWARM_UNSET_API_KEY": "1" if j.unset_api_key else "",
    }
    # Single-quoted: the wrapper evals this, and the prompt contains backticks.
    return "\n".join(f"export {k}={shlex.quote(v)}" for k, v in env.items()) + "\n"


# ----------------------------------------------------------------------
# supervise (login node)
# ----------------------------------------------------------------------


def _job_state(job: str) -> str:
    out = subprocess.run(["sacct", "-j", job, "-X", "-n", "-P", "--format=State"],
                         capture_output=True, text=True)
    if out.returncode != 0:
        raise RuntimeError(out.stderr.strip())
    line = out.stdout.strip().splitlines()
    return line[0].split()[0] if line else "PENDING"


def supervise_once(cfg: SwarmConfig, *, submit: bool = True) -> dict:
    """Resubmit an arm's agent allocation if it ended while agents remain."""

    status = {}
    for arm in cfg.arms:
        L = ArmLayout(cfg, arm)
        remaining = [a for a in L.agents if not (L.agent_dir(a) / "done").exists()]
        reg = L.root / "agents_jobs.json"
        jobs = read_json(reg, []) or []
        last = jobs[-1]["job"] if jobs else None
        state = _job_state(last) if last else None
        alive = state in {"PENDING", "RUNNING", "CONFIGURING", "COMPLETING", "REQUEUED", "SUSPENDED"}
        status[arm] = {"remaining": remaining, "job": last, "state": state}
        j = cfg.agent_job
        if (state == "PENDING" and submit and j.fallback_reservation and not jobs[-1].get("fallback")
                and time.time() - parse_iso(jobs[-1]["submitted_at"]).timestamp() > 60 * j.fallback_after_minutes):
            upd = ["scontrol", "update", f"JobId={last}", f"Reservation={j.fallback_reservation}"]
            upd += [f"QOS={j.fallback_qos}"] if j.fallback_qos else []
            res = subprocess.run(upd, capture_output=True, text=True)
            jobs[-1]["fallback"] = {"at": utc_iso(), "rc": res.returncode, "err": res.stderr.strip()}
            atomic_write_json(reg, jobs)
            LOG.info("arm %s: agents job %s pending; moved to reservation %s (rc %s)", arm, last, j.fallback_reservation, res.returncode)
        if remaining and not alive and submit and not (cfg.root_path / "HALT").exists():
            # Size the allocation to the agents still running (the script skips done agents).
            n = len(remaining)
            proc = subprocess.run(["sbatch", "--parsable", f"--cpus-per-task={n * j.cpus_per_agent}",
                                   f"--mem={n * j.mem_per_agent_gb}G", str(L.root / "agents_job.sbatch")],
                                  check=True, capture_output=True, text=True)
            job = proc.stdout.strip().split(";")[0]
            jobs.append({"job": job, "submitted_at": utc_iso(), "previous": last, "previous_state": state})
            atomic_write_json(reg, jobs)
            LOG.info("arm %s: agents job %s (previous %s %s; %d agents remaining)", arm, job, last, state, len(remaining))
            status[arm]["job"] = job
    return status


def supervise(config_path: str | Path, *, interval: int = 600) -> None:
    cfg = load_swarm(config_path)
    while True:
        st = supervise_once(cfg)
        if all(not s["remaining"] for s in st.values()):
            LOG.info("every agent in every arm is done")
            return
        time.sleep(interval)
