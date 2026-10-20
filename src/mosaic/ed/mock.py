"""Deterministic mock ED.

Maps an ``EDInput`` to a synthetic ``EDOutput`` whose value is fully
determined by the ``config_hash`` and the campaign id. Two calls with
the same input give bit-identical output.

The mock injects:
- transient failures (status=``failed_transient``)  with rate
  ``transient_failure_rate`` (default 5%);
- logical failures (status=``failed_logical``, varying reasons) with
  rate ``logical_failure_rate`` (default 5%);
- a Chern distribution skewed toward |C|=1 (~80%) with C=0 and ±2 in
  the tails;
- a smooth synthetic objective: the gap is highest when the
  ``(a_n, W_G)`` coefficients are near a campaign-specific target,
  giving the optimizer something to actually optimize against.

The mock is fast (<1 ms in normal runs); ``mock_compute_seconds`` lets
tests opt into a sleep when they want to exercise polling.
"""

from __future__ import annotations

import hashlib
import math
import time
from pathlib import Path

import numpy as np

from mosaic.ed.contract import EDInput, EDOutput
from mosaic.ed.runner import EDBackend, JobState, SubmitToken, read_output, write_input, write_output

# Synthetic-objective hyperparameters. Tunable but stable across the codebase
# because changing them silently invalidates regression tests.
_GAP_MAX = 0.05  # in whatever energy unit the campaign uses
_SIGMA_A = 1.5
_SIGMA_W = 1.5

_CHERN_BREAKPOINTS = (
    (0.40, +1),
    (0.80, -1),
    (0.93, 0),
    (0.965, +2),
    (1.00, -2),
)

_LOGICAL_REASONS = (
    "nan_gap",
    "chern_mismatch",
    "spectrum_edge",
    "gap_negative",
)
_TRANSIENT_REASONS = (
    "walltime",
    "node_failure",
    "oom_killed",
)


def _hash_bytes(s: str, salt: str = "") -> bytes:
    """Stable 32-byte digest of ``salt + s``. Accepts arbitrary strings."""

    h = hashlib.sha256()
    if salt:
        h.update(salt.encode("utf-8"))
        h.update(b"\x00")
    h.update(s.encode("utf-8"))
    return h.digest()


def _hash_uniform(s: str, lo: int, hi: int, salt: str = "") -> float:
    """Uniform in [0, 1) derived from bytes ``[lo, hi)`` of ``sha256(salt+s)``.

    Robust to non-hex strings (e.g., a campaign name).
    """

    digest = _hash_bytes(s, salt=salt)
    chunk = digest[lo:hi]
    if not chunk:
        raise ValueError(f"requested empty byte slice [{lo}:{hi}]")
    n = int.from_bytes(chunk, "big")
    return n / float(1 << (8 * len(chunk)))


def _hash_rng(s: str, salt: str = "") -> np.random.Generator:
    """``np.random.Generator`` seeded from ``sha256(salt+s)``; deterministic."""

    digest = _hash_bytes(s, salt=salt)
    seed_int = int.from_bytes(digest[:8], "big") & ((1 << 63) - 1)
    return np.random.default_rng(seed_int)


def _coefs_to_arrays(ed_input: EDInput) -> tuple[np.ndarray, np.ndarray]:
    a = np.array([c.to_python() for c in ed_input.wavefunction.a_n], dtype=complex)
    W = np.array([w.coef.to_python() for w in ed_input.form_factor.W_G], dtype=complex)
    return a, W


def _campaign_target(campaign_id: str, n_a: int, n_w: int) -> tuple[np.ndarray, np.ndarray]:
    """Pick a fixed, campaign-specific target ``(a_target, W_target)``.

    Same campaign → same target (so improvements over time make sense).
    """

    rng = _hash_rng(campaign_id, salt="mock_target")
    a = (rng.standard_normal(n_a) + 1j * rng.standard_normal(n_a)) / math.sqrt(n_a)
    W = (rng.standard_normal(n_w) + 1j * rng.standard_normal(n_w)) / math.sqrt(max(n_w, 1))
    return a, W


def _synthetic_score(ed_input: EDInput) -> float:
    """A smooth function of (a_n, W_G), max ``_GAP_MAX``."""

    a, W = _coefs_to_arrays(ed_input)
    if a.size == 0:
        return 0.0
    a_norm = a / (np.linalg.norm(a) + 1e-12)  # mock the post-normalize convention
    a_t, W_t = _campaign_target(ed_input.campaign_id, a.size, W.size)
    a_t /= np.linalg.norm(a_t) + 1e-12
    da = float(np.linalg.norm(a_norm - a_t) ** 2)
    dw = float(np.linalg.norm(W - W_t) ** 2) if W.size else 0.0
    return _GAP_MAX * math.exp(-da / (2 * _SIGMA_A**2)) * math.exp(-dw / (2 * _SIGMA_W**2))


def _synthetic_chern(ed_input: EDInput) -> int:
    u = _hash_uniform(ed_input.config_hash, 0, 8)
    for cutoff, c in _CHERN_BREAKPOINTS:
        if u < cutoff:
            return c
    return _CHERN_BREAKPOINTS[-1][1]


def _make_constant_band(n_k: int, value: float) -> list[list[float]]:
    return [[float(value)] * n_k for _ in range(n_k)]


def _completed_output(ed_input: EDInput) -> EDOutput:
    n_k = ed_input.lattice.n_k
    score = _synthetic_score(ed_input)
    chern = _synthetic_chern(ed_input)
    eps_target = _make_constant_band(n_k, 0.0)
    eps_above = _make_constant_band(n_k, +score)
    eps_below = _make_constant_band(n_k, -score)
    return EDOutput(
        config_hash=ed_input.config_hash,
        status="completed",
        n_k=n_k,
        target_band_index=1,
        epsilon_target=eps_target,
        epsilon_above=eps_above,
        epsilon_below=eps_below,
        u_k=None,
        chern_solver=chern,
        chern_quantization_error_solver=0.0,
        gap_top_indirect_solver=score,
        compute_seconds=0.0,
        solver_version="mock-ed@v1",
        solver_log_path=None,
        energy_unit=ed_input.energy_unit,
    )


def _logical_failure(ed_input: EDInput, reason: str) -> EDOutput:
    """Return a logically-failed EDOutput in the requested style.

    ``reason`` controls *what* about the output is wrong. The
    orchestrator should treat all of these as ``failed_logical`` and
    *not* retry.

    Note on energy arrays: ``failed_logical`` outputs leave the
    epsilon arrays as ``None``. The orchestrator's ``decide_terminal_state``
    inspects ``failure_reason`` (not the arrays) for these cases. The
    JSON contract (``EDOutput`` with strict floats) does not round-trip
    NaN cleanly, so a "real solver returns completed-with-NaN" path is
    tested at the unit level on ``decide_terminal_state`` directly,
    not via the mock.
    """

    if reason not in _LOGICAL_REASONS:
        raise ValueError(f"unknown logical failure reason {reason!r}")
    n_k = ed_input.lattice.n_k
    return EDOutput(
        config_hash=ed_input.config_hash,
        status="failed_logical",
        failure_reason=reason,
        n_k=n_k,
        target_band_index=1,
        epsilon_target=None,
        epsilon_above=None,
        epsilon_below=None,
        chern_solver=_synthetic_chern(ed_input) if reason != "chern_mismatch" else 99,
        gap_top_indirect_solver=None,
        compute_seconds=0.0,
        solver_version="mock-ed@v1",
        energy_unit=ed_input.energy_unit,
    )


def _transient_failure(ed_input: EDInput, reason: str) -> EDOutput:
    return EDOutput(
        config_hash=ed_input.config_hash,
        status="failed_transient",
        failure_reason=reason,
        n_k=ed_input.lattice.n_k,
        target_band_index=None,
        epsilon_target=None,
        epsilon_above=None,
        epsilon_below=None,
        chern_solver=None,
        gap_top_indirect_solver=None,
        compute_seconds=0.0,
        solver_version="mock-ed@v1",
        energy_unit=ed_input.energy_unit,
    )


def evaluate(
    ed_input: EDInput,
    *,
    logical_failure_rate: float = 0.05,
    transient_failure_rate: float = 0.05,
) -> EDOutput:
    """Pure function: ``EDInput`` + rates → ``EDOutput``. No I/O.

    Failure rolls are derived from the ``config_hash`` so the verdict is
    fully deterministic. The rate parameters control the *threshold* on
    those deterministic rolls, so two calls with the same input + rates
    give bit-identical output.
    """

    h = ed_input.config_hash
    t_roll = _hash_uniform(h, 0, 4)
    l_roll = _hash_uniform(h, 4, 8)
    if t_roll < transient_failure_rate:
        idx = int(_hash_uniform(h, 8, 12) * len(_TRANSIENT_REASONS))
        return _transient_failure(ed_input, _TRANSIENT_REASONS[idx])
    if l_roll < logical_failure_rate:
        idx = int(_hash_uniform(h, 12, 16) * len(_LOGICAL_REASONS))
        return _logical_failure(ed_input, _LOGICAL_REASONS[idx])
    return _completed_output(ed_input)


# ---------------------------------------------------------------------------
# Backend implementation (synchronous: submit does the work in-process)
# ---------------------------------------------------------------------------


class MockBackend:
    """Synchronous mock backend that implements ``EDBackend``.

    ``submit`` runs the evaluation in-process and writes
    ``ed_output.json``. ``poll`` always returns ``COMPLETED``.
    """

    name = "mock"

    def __init__(
        self,
        *,
        logical_failure_rate: float = 0.05,
        transient_failure_rate: float = 0.05,
        compute_seconds: float = 0.0,
    ):
        if not 0.0 <= logical_failure_rate <= 1.0:
            raise ValueError("logical_failure_rate must be in [0, 1]")
        if not 0.0 <= transient_failure_rate <= 1.0:
            raise ValueError("transient_failure_rate must be in [0, 1]")
        self.logical_failure_rate = logical_failure_rate
        self.transient_failure_rate = transient_failure_rate
        self.compute_seconds = float(compute_seconds)

    def prepare(self, ed_input: EDInput, run_dir: Path) -> None:
        write_input(ed_input, run_dir)

    def submit(self, run_dir: Path) -> SubmitToken:
        ed_input = EDInput.model_validate_json((run_dir / "ed_input.json").read_text())
        if self.compute_seconds > 0:
            time.sleep(self.compute_seconds)
        out = evaluate(
            ed_input,
            logical_failure_rate=self.logical_failure_rate,
            transient_failure_rate=self.transient_failure_rate,
        )
        # Stamp compute_seconds *after* evaluate to reflect the wall sleep,
        # without changing the deterministic content of the result.
        out = out.model_copy(update={"compute_seconds": self.compute_seconds})
        write_output(out, run_dir)
        return SubmitToken(backend_kind="mock", handle=ed_input.config_hash)

    def poll(self, token: SubmitToken) -> JobState:
        if token.backend_kind != "mock":
            raise ValueError(f"MockBackend cannot poll {token.backend_kind!r} token")
        return JobState.COMPLETED

    def collect(self, run_dir: Path) -> EDOutput:
        return read_output(run_dir)

    def rehydrate(self, run_dir: Path) -> SubmitToken:
        # The mock's submit is synchronous, so by definition any in-flight
        # mock job has already produced output. The token is just a
        # cosmetic handle.
        ed_input = EDInput.model_validate_json((run_dir / "ed_input.json").read_text())
        return SubmitToken(backend_kind="mock", handle=ed_input.config_hash)


# Make the backend implement the Protocol explicitly (helps mypy / IDE).
_: EDBackend = MockBackend()
