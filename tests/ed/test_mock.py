"""Mock ED determinism, fault injection, and backend behavior."""

from __future__ import annotations

import json
import math
from collections import Counter
from pathlib import Path

import pytest

from mosaic.ed.contract import EDInput
from mosaic.ed.mock import MockBackend, evaluate
from mosaic.ed.runner import JobState, read_output

from .conftest import make_ed_input, make_varied_ed_input


def test_mock_is_deterministic_on_hash():
    a = make_ed_input(seed=1)
    b = make_ed_input(seed=1)
    assert a.config_hash == b.config_hash
    out_a = evaluate(a)
    out_b = evaluate(b)
    assert out_a == out_b


def test_mock_different_inputs_differ():
    a = make_ed_input(a_values=[complex(1.0, 0), complex(0, 0), complex(0, 0)])
    b = make_ed_input(a_values=[complex(0.0, 0), complex(1, 0), complex(0, 0)])
    assert a.config_hash != b.config_hash
    out_a = evaluate(a, logical_failure_rate=0.0, transient_failure_rate=0.0)
    out_b = evaluate(b, logical_failure_rate=0.0, transient_failure_rate=0.0)
    assert out_a.status == "completed"
    assert out_b.status == "completed"
    assert out_a.gap_top_indirect_solver != out_b.gap_top_indirect_solver


def test_mock_failure_rates_approximate_target():
    """Empirical rates over 400 distinct configs match within slack."""

    n = 400
    p_log = 0.10
    p_tr = 0.10
    counts = Counter()
    for i in range(n):
        ed = make_varied_ed_input(i)
        out = evaluate(ed, logical_failure_rate=p_log, transient_failure_rate=p_tr)
        counts[out.status] += 1
    # Hash-derived rolls are uniform, so expected counts are p*n with binomial spread.
    # Allow 3σ on the binomial.
    def slack(p: float) -> float:
        return 3 * math.sqrt(n * p * (1 - p))

    assert abs(counts["failed_logical"] - p_log * n) < slack(p_log)
    assert abs(counts["failed_transient"] - p_tr * n) < slack(p_tr)
    assert counts["completed"] + counts["failed_logical"] + counts["failed_transient"] == n


def test_mock_chern_distribution_skews_to_pm1():
    n = 400
    counts = Counter()
    for i in range(n):
        ed = make_varied_ed_input(i)
        out = evaluate(ed, logical_failure_rate=0.0, transient_failure_rate=0.0)
        counts[out.chern_solver] += 1
    # Per _CHERN_BREAKPOINTS: ~80% of completed runs are |C|=1.
    pm1 = counts[+1] + counts[-1]
    assert pm1 / n > 0.7


def test_mock_synthetic_score_is_smooth():
    """Score is highest at the mock's campaign-specific target.

    We don't know the target a-priori, but the score should be > 0 for
    *some* random {a_n} and the global maximum should be ≤ _GAP_MAX.
    """

    from mosaic.ed.mock import _GAP_MAX  # noqa: PLC2701  - intentional whitebox

    scores = []
    for i in range(50):
        ed = make_varied_ed_input(i)
        out = evaluate(ed, logical_failure_rate=0.0, transient_failure_rate=0.0)
        scores.append(out.gap_top_indirect_solver)
    assert max(scores) > 0.0
    assert all(0 <= s <= _GAP_MAX + 1e-12 for s in scores)


def test_mock_completed_output_has_gap_consistent_with_bands(ed_input: EDInput):
    out = evaluate(ed_input, logical_failure_rate=0.0, transient_failure_rate=0.0)
    if out.status != "completed":
        pytest.skip("non-completed output for this hash")
    # Indirect gap = min(min(eps_above - eps_target), min(eps_target - eps_below))
    above = min(min(row) for row in out.epsilon_above)
    below = min(eps_t - min(row) for row, eps_t in zip(out.epsilon_below, [0.0] * out.n_k))
    # eps_target is constant 0; so above is +score, below is +score.
    assert math.isclose(above, out.gap_top_indirect_solver, abs_tol=1e-12)


def test_mock_backend_round_trip_via_disk(tmp_path: Path, ed_input: EDInput):
    backend = MockBackend(logical_failure_rate=0.0, transient_failure_rate=0.0)
    run_dir = tmp_path / "run"
    backend.prepare(ed_input, run_dir)
    assert (run_dir / "ed_input.json").exists()
    token = backend.submit(run_dir)
    assert token.backend_kind == "mock"
    assert backend.poll(token) == JobState.COMPLETED
    out = backend.collect(run_dir)
    assert out.config_hash == ed_input.config_hash
    assert out.status == "completed"


def test_mock_backend_no_tmp_files_left(tmp_path: Path, ed_input: EDInput):
    backend = MockBackend(logical_failure_rate=0.0, transient_failure_rate=0.0)
    run_dir = tmp_path / "run"
    backend.prepare(ed_input, run_dir)
    backend.submit(run_dir)
    leftovers = [p.name for p in run_dir.iterdir() if p.name.endswith(".tmp")]
    assert leftovers == []


def test_mock_disk_output_validates_against_schema(tmp_path: Path, ed_input: EDInput):
    backend = MockBackend(logical_failure_rate=0.0, transient_failure_rate=0.0)
    run_dir = tmp_path / "run"
    backend.prepare(ed_input, run_dir)
    backend.submit(run_dir)
    raw = json.loads((run_dir / "ed_output.json").read_text())
    assert raw["schema_version"] == "1"
    assert raw["status"] in ("completed", "failed_logical", "failed_transient")
    out = read_output(run_dir)
    assert out.config_hash == ed_input.config_hash


def test_mock_logical_failure_reasons_cover_all_types():
    """Sampling enough configs at high p_logical hits every reason."""

    seen = set()
    for i in range(2000):
        ed = make_varied_ed_input(i)
        out = evaluate(ed, logical_failure_rate=1.0, transient_failure_rate=0.0)
        assert out.status == "failed_logical"
        seen.add(out.failure_reason)
    assert seen == {"nan_gap", "chern_mismatch", "spectrum_edge", "gap_negative"}


def test_mock_transient_failure_reasons_cover_all_types():
    seen = set()
    for i in range(2000):
        ed = make_varied_ed_input(i)
        out = evaluate(ed, logical_failure_rate=0.0, transient_failure_rate=1.0)
        assert out.status == "failed_transient"
        seen.add(out.failure_reason)
    assert seen == {"walltime", "node_failure", "oom_killed"}


def test_mock_invalid_rates_rejected():
    with pytest.raises(ValueError):
        MockBackend(logical_failure_rate=-0.1)
    with pytest.raises(ValueError):
        MockBackend(transient_failure_rate=1.1)


def test_mock_evaluate_stable_under_repeated_calls():
    """Calling evaluate() many times with same input gives same output."""

    ed = make_ed_input(seed=12345)
    refs = [evaluate(ed) for _ in range(5)]
    assert all(r == refs[0] for r in refs)
