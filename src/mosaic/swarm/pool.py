"""Pool jobs: how queued evaluations reach the cluster.

The broker never submits one job per evaluation. It writes a pool entry per
queued run and keeps at most ``max_jobs`` long-lived allocations per tier
alive; their lanes pull from the pool (``jobs/swarm_pool.sbatch``). That keeps
the swarm's footprint in the scheduler to a handful of jobs whatever the
number of agents, which matters under a per-user job limit.

Two backends share one interface: ``SlurmPool`` (sbatch/sacct) and
``MockPool`` (runs the mock ED in-process; tests and dry runs).
"""

from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path
from typing import Protocol

from mosaic.ed.contract import EDInput
from mosaic.ed.mock import evaluate as mock_evaluate
from mosaic.ed.runner import write_output
from mosaic.swarm.config import REPO_ROOT, SwarmConfig, TierSpec
from mosaic.swarm.files import atomic_write_text

TEMPLATE = REPO_ROOT / "jobs" / "swarm_pool.sbatch"

# Slurm states in which a job still holds (or will hold) its claims.
ALIVE_STATES = {"PENDING", "CONFIGURING", "REQUEUED", "RUNNING", "COMPLETING", "SUSPENDED"}


class PoolBackend(Protocol):
    def submit(self, tier: str, script: Path) -> str: ...
    def states(self, job_ids: list[str]) -> dict[str, str]: ...


def wall_seconds(walltime: str) -> int:
    """``[D-]HH:MM:SS`` → seconds."""

    m = re.fullmatch(r"(?:(\d+)-)?(\d+):(\d\d):(\d\d)", walltime)
    if not m:
        raise ValueError(f"bad walltime {walltime!r}")
    d, h, mi, s = (int(x) if x else 0 for x in m.groups())
    return ((d * 24 + h) * 60 + mi) * 60 + s


def render_pool_script(cfg: SwarmConfig, tier_name: str, tier: TierSpec, pool_dir: Path, log_dir: Path) -> str:
    if tier.gpus:
        if tier.gpus % tier.lanes:
            raise ValueError(f"tier {tier_name}: gpus must be a multiple of lanes")
        per = tier.gpus // tier.lanes
        backend_env = "\nexport MOIRE_ED_BACKEND=gpu"
        dispatch = (
            'IFS=, read -ra GPUS <<< "${CUDA_VISIBLE_DEVICES:?no GPUs allocated}"\n'
            f"for ((l = 0; l < {tier.lanes}; l++)); do\n"
            f'  (export CUDA_VISIBLE_DEVICES=$(IFS=,; echo "${{GPUS[*]:$((l * {per})):{per}}}"); lane $l) &\n'
            "done\nwait"
        )
        gres = f"\n#SBATCH --gres=gpu:{tier.gpus}"
    else:
        backend_env = ""
        dispatch = f"for ((l = 0; l < {tier.lanes}; l++)); do lane $l & done\nwait"
        gres = ""
    extra = gres
    if tier.reservation:
        extra += f"\n#SBATCH --reservation={tier.reservation}"
    if tier.qos:
        extra += f"\n#SBATCH --qos={tier.qos}"
    return TEMPLATE.read_text().format(
        tier=tier_name, partition=tier.partition, cpus=tier.lanes * tier.threads, mem=tier.mem,
        walltime=tier.walltime, extra_sbatch=extra, log_dir=log_dir, threads=tier.threads,
        backend_env=backend_env, pool_dir=pool_dir, est_run_seconds=tier.est_run_seconds,
        idle_exit_seconds=cfg.broker.idle_exit_seconds, poll_seconds=cfg.broker.poll_seconds, wall_seconds=wall_seconds(tier.walltime),
        julia_project=cfg.solver_dir / "julia", julia=cfg.broker.julia,
        solver=cfg.solver_dir / "julia" / "ed_solver.jl", batch=cfg.solver_dir / "julia" / "ed_batch.jl",
        lane_mode=tier.lane_mode, lanes=tier.lanes, dispatch=dispatch, pass_size=tier.pass_size,
    )


class SlurmPool:
    def submit(self, tier: str, script: Path) -> str:
        proc = subprocess.run(["sbatch", "--parsable", str(script)], check=True, capture_output=True, text=True)
        return proc.stdout.strip().split(";")[0]

    def states(self, job_ids: list[str]) -> dict[str, str]:
        if not job_ids:
            return {}
        proc = subprocess.run(
            ["sacct", "-j", ",".join(job_ids), "-X", "-n", "-P", "--format=JobID,State"],
            capture_output=True, text=True,
        )
        if proc.returncode != 0:
            # Never guess job death from a failed query: that would requeue
            # (and double-run) everything in flight.
            raise RuntimeError(f"sacct failed: {proc.stderr.strip()}")
        out = {}
        for line in proc.stdout.splitlines():
            if "|" in line:
                jid, state = line.split("|", 1)
                out[jid.strip()] = re.split(r"[+ ]", state.strip())[0]
        # A job sacct has not recorded yet was just submitted.
        return {j: out.get(j, "PENDING") for j in job_ids}


class MockPool:
    """In-process stand-in for Slurm. ``submit`` runs every lane to completion
    immediately (unless ``hold`` is set, which leaves claims in place as if a
    job were still running — used to test broker restarts and dead jobs)."""

    def __init__(self, *, logical_failure_rate: float = 0.0, transient_failure_rate: float = 0.0,
                 evaluator=None):
        # evaluator(EDInput) -> EDOutput; default is ed.mock.evaluate.
        self.evaluator = evaluator
        self.logical_failure_rate = logical_failure_rate
        self.transient_failure_rate = transient_failure_rate
        self.hold = False
        self.alive: set[str] = set()
        self.submitted: list[tuple[str, str]] = []
        self._n = 0
        self.pool_dirs: dict[str, Path] = {}

    def submit(self, tier: str, script: Path) -> str:
        self._n += 1
        # Unique across broker restarts, so a new process never mistakes an
        # old claim for one of its own live jobs.
        job = f"mock-{os.getpid()}-{self._n}"
        self.submitted.append((tier, job))
        pool = self.pool_dirs[tier]
        for d in sorted(p for p in pool.iterdir() if not p.name.startswith(".")):
            if (d / "ed_output.json").exists():
                continue
            try:
                (d / ".claimed").mkdir()
            except FileExistsError:
                continue
            atomic_write_text(d / ".claimed" / "job", job + "\n")
            if self.hold:
                self.alive.add(job)
                continue
            ed_input = EDInput.model_validate_json((d / "ed_input.json").read_text())
            if self.evaluator is not None:
                out = self.evaluator(ed_input)
            else:
                out = mock_evaluate(ed_input, logical_failure_rate=self.logical_failure_rate,
                                    transient_failure_rate=self.transient_failure_rate)
            write_output(out, d)
            atomic_write_text(d / ".claimed" / "rc", "0\n")
        return job

    def states(self, job_ids: list[str]) -> dict[str, str]:
        return {j: ("RUNNING" if j in self.alive else "COMPLETED") for j in job_ids}
