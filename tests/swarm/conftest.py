"""Fixtures for the swarm tests: a tiny reference band, a deterministic mock
evaluator, and a two-arm config rooted in tmp_path (no worktrees, no Slurm)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from mosaic.ed.contract import EDInput, EDOutput
from mosaic.swarm.config import REPO_ROOT, SwarmConfig, load_swarm
from mosaic.swarm.rehearsal import mock_pes

# One shell in the solver basis, inversion-closed, real and small enough that
# |h(r)|² = 1 + 2 Σ w cos(G·r) stays positive.
SHELL1 = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)]


def ed_input_dict(w1: float = 0.05, *, symmetry: str = "none", extra: dict | None = None) -> dict:
    w = [{"shell": 0, "idx": 0, "G_int": [0, 0], "coef": {"re": 1.0, "im": 0.0}}]
    w += [{"shell": 1, "idx": i, "G_int": list(g), "coef": {"re": w1, "im": 0.0}} for i, g in enumerate(SHELL1)]
    return {
        "schema_version": "1", "config_hash": "0" * 64, "campaign_id": "reference-campaign", "seed": 0,
        "lattice": {"n_k": 24, "n_shells": 1, "g_units": "b_M"},
        "wavefunction": {"n_a": 2, "a_n": [{"re": 0.7071067811865476, "im": 0.0}] * 2},
        "form_factor": {"symmetry": symmetry, "W_G": w},
        "ed_solver_params": {"extra": {"D_l": 0.1, "qmax": 8, "nk1": 4, "nk2": 6, **(extra or {})}},
        "energy_unit": "meV",
    }


def mock_gap(ed: EDInput) -> float:
    """Deterministic: grows with the first-shell weight, plus a small
    cluster-size term so R differs between clusters."""
    w1 = next(c.coef.re for c in ed.form_factor.W_G if tuple(c.G_int) == (1, 0))
    return 0.03 * (1 + 2 * (w1 - 0.05)) * (1 + 1e-3 * (ed.lattice.n_k - 24))


def mock_evaluator(ed: EDInput) -> EDOutput:
    extra = ed.ed_solver_params.extra
    sym = "symcluster" in extra
    pes = extra.get("pes")
    return EDOutput(
        config_hash=ed.config_hash, status="failed_logical" if sym else "completed",
        failure_reason="mesh_unsuitable_for_chern" if sym else None, n_k=ed.lattice.n_k,
        chern_solver=None if sym else 1, gap_top_indirect_solver=mock_gap(ed),
        gs_manifold_splitting=1e-4 * mock_gap(ed),
        pes=mock_pes(pes["NA"], below=1, gap=10.0) if pes else None,
        compute_seconds=0.0, solver_version="mock-ed@v1", energy_unit=ed.energy_unit,
    )


def write_config(tmp_path: Path, **overrides) -> Path:
    ref = tmp_path / "reference_ed_input.json"
    ref.write_text(json.dumps(ed_input_dict()))
    cfg = {
        "swarm_id": "test-swarm", "root": str(tmp_path / "root"), "repo_main": str(REPO_ROOT),
        "worktree_root": str(tmp_path / "wt"),
        "arms": {"swarm": {"mode": "shared", "agents": ["swarm-a", "swarm-b"]},
                 "control": {"mode": "private", "agents": ["ctrl-a", "ctrl-b"]}},
        "directions": {a: "tests/fixtures/directions/a-finite-size.md" for a in ("swarm-a", "swarm-b", "ctrl-a", "ctrl-b")},
        "parents": {"p1": {"ed_input": str(ref)}},
        "clusters": {"4x6": {"nk1": 4, "nk2": 6, "tier": "cpu"}, "5x6": {"nk1": 5, "nk2": 6, "tier": "gpu"},
                     "s27": {"symcluster": 1, "n_k": 27, "tier": "gpu", "chern": "skip"}},
        "stages": [{"name": "screen", "clusters": ["4x6", "5x6"]},
                   {"name": "confirm", "clusters": ["s27"], "promote_min_R_gap": 1.01}],
        "claims": [{"name": "win", "all_clusters": ["4x6", "5x6", "s27"],
                    "min_R_gap": {"4x6": 1.02, "5x6": 1.02, "s27": 1.02}}],
        "quotas": {"evaluations_per_agent": 10, "max_in_flight_per_agent": 3},
        "broker": {"backend": "mock", "tick_seconds": 1, "max_retries": 1, "solver_ref": "test",
                   "solver_version_prefix": "mock-ed",
                   "tiers": {"cpu": {"partition": "p", "lanes": 2, "threads": 1, "mem": "1G", "walltime": "01:00:00",
                                     "max_jobs": 2, "est_run_seconds": 10},
                             "gpu": {"partition": "g", "lanes": 1, "threads": 1, "gpus": 1, "mem": "1G",
                                     "walltime": "01:00:00", "max_jobs": 1, "est_run_seconds": 10}}},
    }
    for k, v in overrides.items():
        cur = cfg
        *head, last = k.split(".")
        for h in head:
            cur = cur[h]
        cur[last] = v
    path = tmp_path / "swarm.yaml"
    path.write_text(yaml.safe_dump(cfg))
    return path


@pytest.fixture
def cfg_path(tmp_path: Path) -> Path:
    return write_config(tmp_path)


@pytest.fixture
def cfg(cfg_path: Path) -> SwarmConfig:
    return load_swarm(cfg_path)
