"""ResultStore: idempotency, transitions, queries, rebuild_index."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from mosaic.ed.contract import EDOutput
from mosaic.store.state import RunState
from mosaic.store.store import ResultStore, TransitionError
from tests.ed.conftest import make_ed_input, make_varied_ed_input


@pytest.fixture
def store(tmp_path: Path) -> ResultStore:
    s = ResultStore(db_path=tmp_path / "index.db", work_dir=tmp_path / "runs")
    yield s
    s.close()


def _completed_output(ed_input, gap=0.05, chern=1):
    n_k = ed_input.lattice.n_k
    return EDOutput(
        config_hash=ed_input.config_hash,
        status="completed",
        n_k=n_k,
        target_band_index=1,
        epsilon_target=[[0.0] * n_k for _ in range(n_k)],
        epsilon_above=[[+gap] * n_k for _ in range(n_k)],
        epsilon_below=[[-gap] * n_k for _ in range(n_k)],
        chern_solver=chern,
        gap_top_indirect_solver=gap,
        compute_seconds=0.1,
        solver_version="mock-ed@v1",
    )


def test_register_writes_disk_artifacts(store: ResultStore):
    ed = make_ed_input(seed=1)
    state = store.register(ed, proposer="random", seed=1)
    assert state == RunState.PROPOSED
    rd = store.run_dir(ed.config_hash)
    assert (rd / "config_meta.json").exists()
    assert (rd / "ed_input.json").exists()
    assert (rd / "events.jsonl").exists()


def test_register_is_idempotent(store: ResultStore):
    ed = make_ed_input(seed=2)
    state1 = store.register(ed, proposer="random", seed=1)
    # Move forward once
    store.transition(ed.config_hash, RunState.SUBMITTED, payload={"job_id": "abc"})
    state2 = store.register(ed, proposer="random", seed=1)
    # Second register returns the *current* state, not PROPOSED.
    assert state1 == RunState.PROPOSED
    assert state2 == RunState.SUBMITTED
    # Still only one row.
    assert store.total() == 1


def test_transition_legal_path(store: ResultStore):
    ed = make_ed_input(seed=3)
    store.register(ed, proposer="random", seed=1)
    store.transition(ed.config_hash, RunState.SUBMITTED)
    store.transition(ed.config_hash, RunState.RUNNING)
    store.transition(ed.config_hash, RunState.COMPLETED)
    assert store.get(ed.config_hash).state == RunState.COMPLETED


def test_transition_illegal_raises(store: ResultStore):
    ed = make_ed_input(seed=4)
    store.register(ed, proposer="random", seed=1)
    with pytest.raises(TransitionError):
        store.transition(ed.config_hash, RunState.RUNNING)  # PROPOSED → RUNNING illegal


def test_transition_from_terminal_raises(store: ResultStore):
    ed = make_ed_input(seed=5)
    store.register(ed, proposer="random", seed=1)
    store.transition(ed.config_hash, RunState.SUBMITTED)
    store.transition(ed.config_hash, RunState.COMPLETED)
    with pytest.raises(TransitionError):
        store.transition(ed.config_hash, RunState.SUBMITTED)


def test_transient_retry_path(store: ResultStore):
    ed = make_ed_input(seed=6)
    store.register(ed, proposer="random", seed=1)
    store.transition(ed.config_hash, RunState.SUBMITTED)
    store.transition(ed.config_hash, RunState.FAILED_TRANSIENT)
    # Retry: back to SUBMITTED
    store.transition(ed.config_hash, RunState.SUBMITTED)
    store.transition(ed.config_hash, RunState.FAILED_TRANSIENT)
    # Give up: terminal
    store.transition(ed.config_hash, RunState.FAILED_TRANSIENT_TERMINAL)
    assert store.retry_count(ed.config_hash) == 2
    assert store.get(ed.config_hash).state == RunState.FAILED_TRANSIENT_TERMINAL


def test_ingest_result_writes_summary_and_db(store: ResultStore):
    ed = make_ed_input(seed=7)
    store.register(ed, proposer="random", seed=1)
    store.transition(ed.config_hash, RunState.SUBMITTED)
    out = _completed_output(ed, gap=0.04, chern=1)
    out_path = store.run_dir(ed.config_hash) / "ed_output.json"
    out_path.write_text(out.model_dump_json())
    store.ingest_result(out, chern_authoritative=1, gap_authoritative=0.04, ed_output_path=out_path)
    summary = json.loads((store.run_dir(ed.config_hash) / "result_summary.json").read_text())
    assert summary["chern"] == 1
    assert summary["gap_top_indirect"] == 0.04
    rec = store.get_result(ed.config_hash)
    assert rec is not None
    assert rec.chern == 1


def test_best_filters_to_pm1(store: ResultStore):
    inputs = []
    for i, (chern, gap) in enumerate([(0, 0.10), (+1, 0.05), (-1, 0.07), (+2, 0.20), (+1, 0.03)]):
        ed = make_varied_ed_input(100 + i)
        store.register(ed, proposer="random", seed=1)
        store.transition(ed.config_hash, RunState.SUBMITTED)
        out = _completed_output(ed, gap=gap, chern=chern)
        op = store.run_dir(ed.config_hash) / "ed_output.json"
        op.write_text(out.model_dump_json())
        store.ingest_result(out, chern_authoritative=chern, gap_authoritative=gap, ed_output_path=op)
        inputs.append((ed.config_hash, chern, gap))
    top = store.best(n=10)
    cherns = [r.chern for r in top]
    assert all(c in (-1, 1) for c in cherns)
    gaps = [r.gap_top_indirect for r in top]
    assert gaps == sorted(gaps, reverse=True)
    assert gaps[0] == 0.07  # the C=-1, gap=0.07 entry


def test_query_methods_filter_by_campaign_id(store: ResultStore):
    """When the same store_path holds runs from multiple campaigns
    (common in dev / shared scratch space), ``iter_runs``,
    ``list_by_state``, ``count_by_state``, ``total``, and ``best``
    must restrict to a single ``campaign_id`` when one is passed.

    The orchestrator depends on this for ``_build_history`` -- without
    it, a v2 BO would see v1's leaderboard as warm-start data, which
    is the wrong behaviour for an independent campaign."""
    # Two configs in campaign-A, one in campaign-B. All COMPLETED with
    # |C|=1 so they'd all qualify for `best` without the filter.
    eds_a = []
    for i, gap in enumerate([0.05, 0.07]):
        ed = make_varied_ed_input(500 + i, campaign_id="aaa-" * 16)
        store.register(ed, proposer="random", seed=1)
        store.transition(ed.config_hash, RunState.SUBMITTED)
        out = _completed_output(ed, gap=gap, chern=1)
        op = store.run_dir(ed.config_hash) / "ed_output.json"
        op.write_text(out.model_dump_json())
        store.ingest_result(out, chern_authoritative=1, gap_authoritative=gap, ed_output_path=op)
        store.transition(ed.config_hash, RunState.COMPLETED)
        eds_a.append(ed)
    ed_b = make_ed_input(seed=600, campaign_id="bbb-" * 16)
    store.register(ed_b, proposer="random", seed=1)
    store.transition(ed_b.config_hash, RunState.SUBMITTED)
    out_b = _completed_output(ed_b, gap=0.99, chern=1)  # would dominate without filter
    op_b = store.run_dir(ed_b.config_hash) / "ed_output.json"
    op_b.write_text(out_b.model_dump_json())
    store.ingest_result(out_b, chern_authoritative=1, gap_authoritative=0.99, ed_output_path=op_b)
    store.transition(ed_b.config_hash, RunState.COMPLETED)

    cid_a = eds_a[0].campaign_id
    cid_b = ed_b.campaign_id

    # total() / count_by_state filter.
    assert store.total() == 3
    assert store.total(campaign_id=cid_a) == 2
    assert store.total(campaign_id=cid_b) == 1
    assert sum(store.count_by_state(campaign_id=cid_a).values()) == 2

    # iter_runs filter.
    a_hashes = {r.config_hash for r in store.iter_runs(campaign_id=cid_a)}
    assert a_hashes == {ed.config_hash for ed in eds_a}

    # list_by_state filter.
    b_completed = store.list_by_state(RunState.COMPLETED, campaign_id=cid_b)
    assert len(b_completed) == 1 and b_completed[0].config_hash == ed_b.config_hash

    # best() filter -- ed_b's 0.99 gap must not leak into campaign-A's
    # leaderboard.
    best_a = store.best(n=10, campaign_id=cid_a)
    assert len(best_a) == 2
    assert max(r.gap_top_indirect for r in best_a) == 0.07
    best_b = store.best(n=10, campaign_id=cid_b)
    assert len(best_b) == 1 and best_b[0].gap_top_indirect == 0.99


def test_best_excludes_failed_logical_with_pm1_chern(store: ResultStore):
    """A run that ends in ``failed_logical`` (e.g.,
    ``chern_quantization_too_large``) can still have
    ``chern_solver = ±1`` (the rounded integer happened to be ±1
    even though qerr was over threshold). The leaderboard must
    not include these — only ``status = completed`` is a real
    optimisation hit."""
    # One real completed |C|=1 hit.
    ed_ok = make_varied_ed_input(300)
    store.register(ed_ok, proposer="random", seed=1)
    store.transition(ed_ok.config_hash, RunState.SUBMITTED)
    out_ok = _completed_output(ed_ok, gap=0.04, chern=1)
    op_ok = store.run_dir(ed_ok.config_hash) / "ed_output.json"
    op_ok.write_text(out_ok.model_dump_json())
    store.ingest_result(out_ok, chern_authoritative=1, gap_authoritative=0.04, ed_output_path=op_ok)

    # One failed_logical with chern_solver=+1 (qerr too large) — this
    # is exactly the case that leaked into the leaderboard before this
    # fix. The reported gap (0.99) is higher than the legit hit's 0.04,
    # so it would dominate the leaderboard if the filter were wrong.
    ed_bad = make_varied_ed_input(301)
    store.register(ed_bad, proposer="random", seed=1)
    store.transition(ed_bad.config_hash, RunState.SUBMITTED)
    out_bad = EDOutput(
        config_hash=ed_bad.config_hash,
        status="failed_logical",
        failure_reason="chern_quantization_too_large",
        n_k=ed_bad.lattice.n_k,
        chern_solver=1,
        chern_quantization_error_solver=0.35,
        gap_top_indirect_solver=0.99,
        compute_seconds=0.1,
        solver_version="mock-ed@v1",
    )
    op_bad = store.run_dir(ed_bad.config_hash) / "ed_output.json"
    op_bad.write_text(out_bad.model_dump_json())
    store.ingest_result(
        out_bad, chern_authoritative=1, gap_authoritative=0.99, ed_output_path=op_bad,
    )
    store.transition(ed_bad.config_hash, RunState.FAILED_LOGICAL)

    top = store.best(n=10)
    assert len(top) == 1, f"expected only the completed run; got {top}"
    assert top[0].config_hash == ed_ok.config_hash
    assert top[0].status == "completed"


def test_count_by_state_correct(store: ResultStore):
    for i, target_state in enumerate(
        [RunState.PROPOSED, RunState.SUBMITTED, RunState.SUBMITTED, RunState.COMPLETED]
    ):
        ed = make_varied_ed_input(200 + i)
        store.register(ed, proposer="random", seed=1)
        if target_state != RunState.PROPOSED:
            store.transition(ed.config_hash, RunState.SUBMITTED)
        if target_state == RunState.COMPLETED:
            store.transition(ed.config_hash, RunState.COMPLETED)
    counts = store.count_by_state()
    assert counts.get(RunState.PROPOSED, 0) == 1
    assert counts.get(RunState.SUBMITTED, 0) == 2
    assert counts.get(RunState.COMPLETED, 0) == 1


def test_rebuild_index_recovers_runs(tmp_path: Path):
    db = tmp_path / "index.db"
    work = tmp_path / "runs"
    s1 = ResultStore(db_path=db, work_dir=work)
    eds = [make_varied_ed_input(300 + i) for i in range(3)]
    for ed in eds:
        s1.register(ed, proposer="random", seed=1)
        s1.transition(ed.config_hash, RunState.SUBMITTED)
    s1.transition(eds[0].config_hash, RunState.COMPLETED)
    out = _completed_output(eds[0], gap=0.06, chern=1)
    op = s1.run_dir(eds[0].config_hash) / "ed_output.json"
    op.write_text(out.model_dump_json())
    s1.ingest_result(out, chern_authoritative=1, gap_authoritative=0.06, ed_output_path=op)
    s1.close()

    # Wipe DB; everything must be reconstructed from disk.
    db.unlink()
    s2 = ResultStore(db_path=db, work_dir=work)
    n = s2.rebuild_index()
    assert n == 3
    counts = s2.count_by_state()
    assert counts[RunState.SUBMITTED] == 2
    assert counts[RunState.COMPLETED] == 1
    rec = s2.get_result(eds[0].config_hash)
    assert rec is not None
    assert rec.chern == 1
    assert rec.gap_top_indirect == 0.06
    s2.close()


def test_event_log_durability_on_disk(store: ResultStore):
    """events.jsonl must contain every transition."""

    ed = make_ed_input(seed=400)
    store.register(ed, proposer="random", seed=1)
    store.transition(ed.config_hash, RunState.SUBMITTED, payload={"job_id": "j1"})
    store.transition(ed.config_hash, RunState.RUNNING)
    store.transition(ed.config_hash, RunState.COMPLETED)
    lines = (store.run_dir(ed.config_hash) / "events.jsonl").read_text().splitlines()
    assert len(lines) == 4  # PROPOSED + 3 transitions
    parsed = [json.loads(l) for l in lines]
    assert parsed[0]["to"] == RunState.PROPOSED.value
    assert parsed[1]["to"] == RunState.SUBMITTED.value
    assert parsed[1]["payload"]["job_id"] == "j1"
    assert parsed[-1]["to"] == RunState.COMPLETED.value


def test_get_unknown_returns_none(store: ResultStore):
    assert store.get("0" * 64) is None
    assert store.get_result("0" * 64) is None
