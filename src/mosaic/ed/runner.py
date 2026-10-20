"""Backend-agnostic interface for invoking the ED solver.

A backend is a small state machine over a single per-run directory:

    prepare(input, run_dir)   →  writes ed_input.json
    submit(run_dir)            →  returns SubmitToken (job id, etc.)
    poll(token)                →  PENDING | RUNNING | COMPLETED | FAILED_TRANSIENT
    collect(run_dir)           →  parses ed_output.json and returns EDOutput

The mock backend (``src/ed/mock.py``) implements this synchronously:
``submit`` does the work and writes ``ed_output.json`` immediately, and
``poll`` always reports ``COMPLETED``. The real Julia backend will use
sbatch + sacct.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Protocol

from mosaic.ed.contract import EDInput, EDOutput


class JobState(str, Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED_TRANSIENT = "FAILED_TRANSIENT"


@dataclass(frozen=True)
class SubmitToken:
    """Opaque-ish handle to an in-flight ED job.

    For the mock backend, ``backend_kind == "mock"`` and ``handle`` is a
    sentinel string. For the real Slurm backend, ``handle`` will be the
    Slurm job id.
    """

    backend_kind: str
    handle: str


class EDBackend(Protocol):
    name: str

    def prepare(self, ed_input: EDInput, run_dir: Path) -> None: ...
    def submit(self, run_dir: Path) -> SubmitToken: ...
    def poll(self, token: SubmitToken) -> JobState: ...
    def collect(self, run_dir: Path) -> EDOutput: ...

    def rehydrate(self, run_dir: Path) -> SubmitToken:
        """Reconstruct a ``SubmitToken`` for an in-flight job after restart.

        Implementations should read whatever per-run on-disk metadata
        (``slurm.json`` for Slurm, the ``ed_input.json`` for the mock,
        etc.) is needed to restore the token. Used by the orchestrator's
        reconcile pass.
        """
        ...


def write_input(ed_input: EDInput, run_dir: Path) -> Path:
    """Write ``ed_input.json`` to a run directory and return its path.

    Helper used by every backend's ``prepare``. Atomic via write-then-rename.
    """

    run_dir.mkdir(parents=True, exist_ok=True)
    path = run_dir / "ed_input.json"
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(ed_input.model_dump_json(indent=2))
    tmp.replace(path)
    return path


def read_output(run_dir: Path) -> EDOutput:
    """Read and validate ``ed_output.json`` from a run directory."""

    path = run_dir / "ed_output.json"
    return EDOutput.model_validate_json(path.read_text())


def write_output(ed_output: EDOutput, run_dir: Path) -> Path:
    """Write ``ed_output.json`` atomically. Used by the mock and by tests."""

    run_dir.mkdir(parents=True, exist_ok=True)
    path = run_dir / "ed_output.json"
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(ed_output.model_dump_json(indent=2))
    tmp.replace(path)
    return path
