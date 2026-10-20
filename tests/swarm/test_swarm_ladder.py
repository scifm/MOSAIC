"""Pinned shell parents, admissibility, Laughlin gates, the stage
ladder and claims, controls, templates and batch submission (mock ED)."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from mosaic.ed.contract import EDInput, EDOutput
from mosaic.swarm import agent as A
from mosaic.swarm import gates as G
from mosaic.swarm.broker import ArmBroker, load_pes_counts, pes_expected_total
from mosaic.swarm.config import ClusterSpec, GateSpec, load_swarm
from mosaic.swarm.files import read_json
from mosaic.swarm.parents import build_parents, m2_static
from mosaic.swarm.pool import MockPool
from mosaic.swarm.rehearsal import mock_pes
from mosaic.swarm.setup import setup
from mosaic.swarm.validate import RequestRejected, normalise

from .conftest import ed_input_dict, write_config

W3 = ["0", "0", "3/5", "0", "0", "1/4", "0", "1/8"]
W2 = ["0", "-1/3", "0", "0", "1/3", "-1/6", "0", "0"]


def ladder_config(tmp_path: Path, **gates) -> Path:
    template = tmp_path / "template.json"
    template.write_text(json.dumps(ed_input_dict()))
    counts = {"s21:2": {"counts": [168], "total": 168}, "s21c:3": {"counts": [637], "total": 637},
              "r56:2": {"counts": [375], "total": 375}}           # r46 is counted from the lll reference
    (tmp_path / "pes_counts.json").write_text(json.dumps(counts))
    path = write_config(tmp_path)
    cfg = yaml.safe_load(path.read_text())
    cfg.update({
        "parents": {"w3": {"shells": W3}, "w2": {"shells": W2}, "lll": {"shells": ["0"] * 8, "role": "diagnostic"}},
        "lll_parent": "lll",
        "regime": {"template_ed_input": str(template), "a_n": [1, 0, 0], "pin_static": True},
        "clusters": {
            "s21": {"symcluster": 1, "n_k": 21, "tier": "cpu", "ed_accuracy": "search", "chern": "skip", "pes_na": 2},
            "s21c": {"symcluster": 1, "n_k": 21, "tier": "cpu", "ed_accuracy": "confirm", "chern": "skip", "pes_na": 3},
            "r46": {"nk1": 4, "nk2": 6, "tier": "cpu", "ed_accuracy": "confirm", "chern": "match_parent", "pes_na": 2,
                    "pes_reference": "lll"},
            "r56": {"nk1": 5, "nk2": 6, "tier": "gpu", "ed_accuracy": "confirm", "chern": "match_parent", "pes_na": 2},
        },
        "stages": [{"name": "screen", "clusters": ["s21"]},
                   {"name": "confirm21", "clusters": ["s21c"], "promote_min_R_gap": 1.02},
                   {"name": "r46", "clusters": ["r46"], "promote_min_R_gap": 1.0},
                   {"name": "r56", "clusters": ["r56"], "promote_min_R_gap": 1.0}],
        "claims": [{"name": "strong", "all_clusters": ["s21", "r46", "r56"], "min_R_gap": {"r46": 1.10, "r56": 1.10}},
                   {"name": "robust_positive", "all_clusters": ["s21", "r46", "r56"], "min_R_gap": {"r46": 1.05, "r56": 1.05}},
                   {"name": "suggestive", "all_clusters": ["s21", "r46", "r56"]}],
        "gates": {"pes_expected_counts": str(tmp_path / "pes_counts.json"), **gates},
        "quotas": {"evaluations_per_agent": 50, "max_in_flight_per_agent": 10},
    })
    path.write_text(yaml.safe_dump(cfg))
    return path


def evaluator(ed: EDInput) -> EDOutput:
    """gap ∝ 1 + 0.6 α + β; β > 0 degrades the PES (0 < β < 0.05: AMBIGUOUS,
    β ≥ 0.05: FAIL); symmetric clusters cannot evaluate Chern."""

    block = ed.form_factor.deformation
    a, b = (block.alpha[0][0], block.beta[0][0]) if block else (0.0, 0.0)
    gap = 0.03 * (1 + 0.6 * a + b)
    extra = ed.ed_solver_params.extra
    sym = "symcluster" in extra
    pes = extra.get("pes")
    p = None
    if pes:
        total = pes_expected_total(ed.lattice.n_k, pes["NA"])
        p = mock_pes(pes["NA"], below=total, gap=-1.0 if b >= 0.05 else (0.2 if b > 0 else 10.0))
    return EDOutput(config_hash=ed.config_hash, status="failed_logical" if sym else "completed",
                    failure_reason="chern_manifold_not_spectral_flow_orbit" if sym else None,
                    n_k=ed.lattice.n_k, chern_solver=None if sym else 1, gap_top_indirect_solver=gap,
                    gs_manifold_splitting=1e-6 * gap, pes=p, compute_seconds=0.0,
                    solver_version="mock-ed@v1", energy_unit=ed.energy_unit)


def deformed(parent: EDInput, alpha: float, beta: float = 0.0) -> dict:
    d = parent.model_dump(mode="json", exclude={"config_hash", "campaign_id", "seed", "proposer_x"})
    d["form_factor"]["deformation"] = {
        "spatial_stars": [[[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1]]],
        "momentum_stars": [[[1, 0], [-1, 0], [0, 1], [0, -1], [1, -1], [-1, 1]]],
        "alpha": [[alpha]], "beta": [[beta]], "n_mesh": 32, "g_cutoff": 4}
    return d


def test_shell_parents_and_pinning(tmp_path):
    cfg = load_swarm(ladder_config(tmp_path))
    parents = build_parents(cfg)
    assert m2_static(parents["w3"]) == pytest.approx(3.62875, abs=1e-12)
    assert m2_static(parents["w2"]) == pytest.approx(2.5, abs=1e-12)
    assert parents["w3"].form_factor.symmetry == "C3_hard" and "nk1" not in parents["w3"].ed_solver_params.extra
    w3 = parents["w3"]
    normalise(deformed(w3, 0.05), w3, cfg)                                   # deformation only: fine
    moved = deformed(w3, 0.05)
    moved["form_factor"]["W_G"][1]["coef"]["re"] += 0.01
    with pytest.raises(RequestRejected, match="pinned to the parent"):
        normalise(moved, w3, cfg)
    ll = deformed(w3, 0.05)
    ll["wavefunction"]["a_n"][1]["re"] = 0.1
    with pytest.raises(RequestRejected, match="a_n are pinned"):
        normalise(ll, w3, cfg)
    with pytest.raises(RequestRejected, match="symmetry must stay"):
        normalise({**deformed(w3, 0.05), "form_factor": {**deformed(w3, 0.05)["form_factor"], "symmetry": "none"}},
                  w3, cfg)


def test_admissibility_gate(tmp_path):
    cfg = load_swarm(ladder_config(tmp_path, admissibility_min_ratio=0.5, admissibility_grid=8))
    w3 = build_parents(cfg)["w3"]
    normalise(deformed(w3, 0.05), w3, cfg)                                   # S00 ratio ≈ 0.93
    with pytest.raises(RequestRejected, match="inadmissible envelope"):
        normalise(deformed(w3, 1.2, 0.7), w3, cfg)                          # ratio ≈ 0.07


def test_gate_verdicts():
    gates = GateSpec()
    sym = ClusterSpec(symcluster=1, n_k=21, tier="cpu", chern="skip", pes_na=2)
    rect = ClusterSpec(nk1=4, nk2=6, tier="cpu", chern="match_parent", pes_na=2)
    base = {"status": "completed", "gap_top_indirect_solver": 1e-3, "gs_manifold_splitting": 1e-8, "chern_solver": 1}
    v = lambda out, c=rect, pc=1, n=5: G.evaluate(out, c, gates, pc, [n])["verdict"]  # noqa: E731
    assert v({**base, "pes": mock_pes(2, below=5, gap=3.0)}) == G.PASS
    assert v({**base, "pes": mock_pes(2, below=5, gap=0.2)}) == G.AMBIGUOUS
    assert v({**base, "pes": mock_pes(2, below=5, gap=3.0, above=0)}) == G.AMBIGUOUS   # uninformative cut
    assert v({**base, "pes": mock_pes(2, below=5, gap=-1.0)}) == G.FAIL              # no separation
    assert v({**base, "pes": mock_pes(2, below=5, gap=3.0)}, n=6) == G.FAIL         # wrong count
    assert v(base) == G.FAIL                                                   # PES requested but missing
    assert v({**base, "pes": mock_pes(2, below=5, gap=3.0)}, pc=-1) == G.FAIL  # Chern differs from parent
    assert v({**base, "gs_manifold_splitting": 5e-4, "pes": mock_pes(2, below=5, gap=3.0)}) == G.FAIL
    sym_out = {**base, "status": "failed_logical", "failure_reason": "chern_manifold_not_spectral_flow_orbit",
               "chern_solver": None, "pes": mock_pes(2, below=5, gap=3.0)}
    assert v(sym_out, c=sym, pc=None) == G.PASS
    assert v({**sym_out, "failure_reason": "kernel_singular"}, c=sym, pc=None) == G.FAIL


def test_ladder_claims_and_tables(tmp_path):
    cfg_path = ladder_config(tmp_path)
    cfg = load_swarm(cfg_path)
    setup(cfg, cfg_path, worktrees=False, solver=False)
    parents = build_parents(cfg)
    pool = MockPool(evaluator=evaluator)
    brokers = {arm: ArmBroker(cfg, arm, pool, parents, load_pes_counts(cfg)) for arm in cfg.arms}
    a = A.Ctx(cfg, "swarm-a")

    def sub(name, alpha, beta=0.0, **kw):
        p = tmp_path / f"{name}.json"
        p.write_text(json.dumps(deformed(parents["w3"], alpha, beta)))
        return A.submit(a, p, name, parent="w3", **kw)

    reqs = {"strong": sub("strong", 0.2), "robust": sub("robust", 0.1), "phase_fail": sub("phase_fail", 0.1, 0.05),
            "ambiguous": sub("ambiguous", 0.1, 0.01), "small": sub("small", 0.01)}
    ctl = tmp_path / "ctl.json"
    c = deformed(parents["w3"], 0.0)
    for w in c["form_factor"]["W_G"]:     # static control (not pinned): 0.9 ρ + 0.1 stays ≥ 0
        if w["G_int"] != [0, 0]:
            w["coef"]["re"] *= 0.9
    ctl.write_text(json.dumps(c))
    reqs["control"] = A.submit(a, ctl, "control", parent="w3", control=True)
    for _ in range(12):
        for b in brokers.values():
            b.tick()
    res = {k: read_json(a.L.inbox("swarm-a") / v / "result.json") for k, v in reqs.items()}

    assert res["strong"]["claim"] == "strong" and res["strong"]["stage_reached"] == "r56"
    assert res["strong"]["clusters"]["r56"]["R_gap"] == pytest.approx(1.12)
    assert res["robust"]["claim"] == "robust_positive" and res["robust"]["verdict"] == G.PASS
    assert res["phase_fail"]["status"] == "failed" and res["phase_fail"]["stage_reached"] == "screen"
    assert "PES: no separation" in res["phase_fail"]["clusters"]["s21"]["reasons"][0]
    assert res["ambiguous"]["verdict"] == G.AMBIGUOUS and res["ambiguous"]["stage_reached"] == "r56"
    assert res["ambiguous"]["claim"] is None                                   # claims need PASS
    assert res["small"]["status"] == "done" and res["small"]["stage_reached"] == "screen"
    assert res["control"]["kind"] == "control" and res["control"]["claim"] is None
    assert res["control"]["stage_reached"] == "screen"                         # controls are never promoted

    # Diagnostics only: R_beyondM2 = Δ / (M2(k) Δ_LLL), with the uniform band as Δ_LLL.
    row = res["robust"]["clusters"]["s21"]
    assert row["R_beyondM2"] == pytest.approx(row["gap"] / (res["robust"]["diagnostics"]["M2_k"] * 0.03))
    assert res["robust"]["diagnostics"]["M2_parent"] == pytest.approx(3.62875)

    lb = read_json(a.L.leaderboard_json)
    ranked = [r["family"] for r in lb["leaderboards"]["w3"]]
    assert ranked == ["strong", "robust", "small", "ambiguous"]     # PASS by R_gap, then AMBIGUOUS
    assert "phase_fail" not in ranked and "control" not in ranked
    assert [r["family"] for r in lb["other_phases"]] == ["phase_fail"]
    assert [r["family"] for r in lb["controls"]] == ["control"]
    assert lb["leaderboards"]["w2"] == []
    # Parents are gated too, and the PES request carries the expected counts.
    par = read_json(a.L.root / "parents.json")
    assert par["w3"]["clusters"]["r46"]["verdict"] == G.PASS and par["w3"]["clusters"]["r46"]["chern"] == 1
    h = res["robust"]["clusters"]["r46"]["hash"]
    extra = json.loads(brokers["swarm"].store.get(h).config_json)["ed_solver_params"]["extra"]
    assert "expected_counts" not in extra["pes"]                               # counting is the broker's
    derived = read_json(a.L.root / "pes_counts_derived.json")
    assert derived["r46"]["counts"] == [228] and derived["r46"]["reference"] == "lll"


def test_template_batch_and_reference(tmp_path):
    cfg_path = ladder_config(tmp_path)
    cfg = load_swarm(cfg_path)
    setup(cfg, cfg_path, worktrees=False, solver=False)
    a = A.Ctx(cfg, "swarm-a")
    t = A.template(a, "w2")
    assert "config_hash" not in t and len(t["form_factor"]["W_G"]) == 1 + 6 * 2 + 12 * 3 + 6 * 2
    with pytest.raises(SystemExit, match="name a parent"):
        A.template(a)
    batch = tmp_path / "batch"
    batch.mkdir()
    w3 = build_parents(cfg)["w3"]
    for i, al in enumerate((0.02, 0.04)):
        (batch / f"{i}.json").write_text(json.dumps(deformed(w3, al)))
    bad = deformed(w3, 0.02)
    bad["form_factor"]["W_G"][1]["coef"]["re"] += 0.1
    (batch / "9_bad.json").write_text(json.dumps(bad))
    out = A.submit_batch(a, batch, "fam", parent="w3")
    assert [r.startswith("rejected") for _, r in out] == [False, False, True]
    rep = A.reference_report(a)
    assert "w3" in rep and "lll" not in rep.split("Pinned")[0] and "robust_positive" in rep


def test_pes_counts_checked(tmp_path):
    assert [pes_expected_total(n, na) for n, na in ((21, 2), (21, 3), (24, 2), (24, 3), (30, 2), (30, 3))] == \
        [168, 637, 228, 1088, 375, 2530]
    cfg = load_swarm(ladder_config(tmp_path))
    data = json.loads(Path(cfg.gates.pes_expected_counts).read_text())
    data["r56:2"]["counts"] = [374]
    Path(cfg.gates.pes_expected_counts).write_text(json.dumps(data))
    with pytest.raises(SystemExit, match="closed form says 375"):
        load_pes_counts(cfg)


def test_counting_gap_and_reference_counts():
    # Two sectors: expected (2, 1) below a gap of 4.
    levels = [[1.0, 1.2, 5.0, None], [1.1, 5.5]]
    assert G.counting_gap(levels, [2, 1]) == {"gap": pytest.approx(3.8), "gap_infinite": False,
                                              "matched": True, "informative": True}
    assert not G.counting_gap(levels, [1, 2])["matched"]                       # wrong momentum split
    assert G.counting_gap([[1.0, None]], [1])["gap_infinite"]                  # zero eigenvalues outside
    ref = G.reference_counts(levels, 3, 0.5)
    assert ref["counts"] == [2, 1] and ref["gap"] == pytest.approx(3.8)
    with pytest.raises(ValueError, match="not a clear Laughlin reference"):
        G.reference_counts([[1.0, 1.2, 1.3]], 2, 0.5)


def test_convergence_overrides_only_tighten():
    from mosaic.swarm.validate import tightened

    assert tightened({"n_mesh": 32, "g_cutoff": 12}, {"n_mesh": 64, "g_cutoff": 10}) == {"n_mesh": 64, "g_cutoff": 12}
    assert tightened({"g_cutoff": None}, {"g_cutoff": 10}) == {"g_cutoff": 10}
    assert tightened({"qmax": 8, "D_l": 0.1}, {"qmax": 10}) == {"qmax": 10, "D_l": 0.1}


def test_controls_on_named_clusters(tmp_path):
    cfg_path = ladder_config(tmp_path)
    cfg = load_swarm(cfg_path)
    setup(cfg, cfg_path, worktrees=False, solver=False)
    parents = build_parents(cfg)
    pool = MockPool(evaluator=evaluator)
    brokers = {arm: ArmBroker(cfg, arm, pool, parents, load_pes_counts(cfg)) for arm in cfg.arms}
    a = A.Ctx(cfg, "swarm-a")
    p = tmp_path / "ctl.json"
    c = deformed(parents["w3"], 0.0)
    for w in c["form_factor"]["W_G"]:
        if w["G_int"] != [0, 0]:
            w["coef"]["re"] *= 0.9
    p.write_text(json.dumps(c))
    with pytest.raises(SystemExit, match="control requests only"):
        A.submit(a, p, "ctl", parent="w3", clusters=["r46"])
    rid = A.submit(a, p, "ctl", parent="w3", control=True, clusters=["r46", "r56"])
    for _ in range(4):
        for b in brokers.values():
            b.tick()
    res = read_json(a.L.inbox("swarm-a") / rid / "result.json")
    acc = read_json(a.L.inbox("swarm-a") / rid / "accepted.json")
    assert set(res["clusters"]) == {"r46", "r56"} and res["stage_reached"] == "control"
    assert res["status"] == "done" and res["claim"] is None and acc["charged_evaluations"] == 2
    assert all(x["R_gap"] is not None for x in res["clusters"].values())


def test_promote_on_named_clusters(tmp_path):
    cfg_path = ladder_config(tmp_path)
    data = yaml.safe_load(cfg_path.read_text())
    # A stage gated on r46 alone at 1.05: s21's lower ratio must not block it.
    data["stages"][3] = {"name": "r56", "clusters": ["r56"], "promote_min_R_gap": 1.05, "promote_on": ["r46"]}
    cfg_path.write_text(yaml.safe_dump(data))
    cfg = load_swarm(cfg_path)
    setup(cfg, cfg_path, worktrees=False, solver=False)
    parents = build_parents(cfg)

    def grows(ed):  # gap ratio 1.03 on Nk = 21, 1.07 on rectangles
        out = evaluator(ed)
        rect = "nk1" in ed.ed_solver_params.extra
        f = (1.07 if rect else 1.03) if ed.form_factor.deformation else 1.0
        return out.model_copy(update={"gap_top_indirect_solver": 0.03 * f, "gs_manifold_splitting": 1e-9})

    brokers = {arm: ArmBroker(cfg, arm, MockPool(evaluator=grows), parents, load_pes_counts(cfg)) for arm in cfg.arms}
    a = A.Ctx(cfg, "swarm-a")
    p = tmp_path / "x.json"
    p.write_text(json.dumps(deformed(parents["w3"], 0.05)))
    rid = A.submit(a, p, "x", parent="w3")
    for _ in range(10):
        for b in brokers.values():
            b.tick()
    res = read_json(a.L.inbox("swarm-a") / rid / "result.json")
    assert res["clusters"]["s21"]["R_gap"] == pytest.approx(1.03) and res["stage_reached"] == "r56"


def test_pool_serves_strongest_first(tmp_path):
    cfg = load_swarm(ladder_config(tmp_path))

    parents = build_parents(cfg)
    b = ArmBroker(cfg, "swarm", MockPool(evaluator=evaluator), parents, load_pes_counts(cfg))
    assert b._priority_for(1.6) < b._priority_for(1.1) < b._priority_for(None) < b.PRIORITY_FIRST_STAGE
    # Two queued runs: the stronger one is renamed to sort first; parents sort before both.
    pool = b.L.pool_dir("gpu")
    runs = []
    for i, r in enumerate((1.05, 1.40)):
        h = f"{i:064x}"
        d = b.store.run_dir(h)
        (d / "ed_input.json").write_text("{}")
        b._set_priority(h, b._priority_for(r))
        (pool / f"20261002T0000{i}0.000Z_{h}").symlink_to(d)
        runs.append(h)
    hp = "f" * 64
    b.store.run_dir(hp)
    b._set_priority(hp, b.PRIORITY_PARENT)
    (pool / f"20261002T000020.000Z_{hp}").symlink_to(b.store.run_dir(hp))
    b._reprioritize()
    order = [p.name.rsplit("_", 1)[-1] for p in sorted(pool.iterdir())]
    assert order == [hp, runs[1], runs[0]]


def test_diagnostic_and_withdrawn_requests(tmp_path):
    cfg_path = ladder_config(tmp_path)
    cfg = load_swarm(cfg_path)
    setup(cfg, cfg_path, worktrees=False, solver=False)
    parents = build_parents(cfg)
    pool = MockPool(evaluator=evaluator)
    brokers = {arm: ArmBroker(cfg, arm, pool, parents, load_pes_counts(cfg)) for arm in cfg.arms}
    a = A.Ctx(cfg, "swarm-a")
    p = tmp_path / "x.json"
    p.write_text(json.dumps(deformed(parents["w3"], 0.2)))          # would climb to "strong"
    diag = A.submit(a, p, "probe", parent="w3", diagnostic=True)
    q = tmp_path / "y.json"
    q.write_text(json.dumps(deformed(parents["w3"], 0.19)))
    gone = A.submit(a, q, "gone", parent="w3")
    A.withdraw(a, [gone], "near-copy of a leader")
    for _ in range(8):
        for b in brokers.values():
            b.tick()
    rd = read_json(a.L.inbox("swarm-a") / diag / "result.json")
    rw = read_json(a.L.inbox("swarm-a") / gone / "result.json")
    assert rd["kind"] == "diagnostic" and rd["stage_reached"] == "screen" and rd["claim"] is None
    assert rw["withdrawn"] and rw["stage_reached"] == "screen"
    lb = read_json(a.L.leaderboard_json)
    assert not lb["leaderboards"]["w3"] and {r["family"] for r in lb["controls"]} == {"probe", "gone"}


def test_control_inherits_candidate_priority(tmp_path):
    cfg_path = ladder_config(tmp_path)
    cfg = load_swarm(cfg_path)
    setup(cfg, cfg_path, worktrees=False, solver=False)
    parents = build_parents(cfg)
    pool = MockPool(evaluator=evaluator)
    pool.hold = True
    b = ArmBroker(cfg, "swarm", pool, parents, load_pes_counts(cfg))
    a = A.Ctx(cfg, "swarm-a")
    p = tmp_path / "c.json"
    c = deformed(parents["w3"], 0.0)
    for w in c["form_factor"]["W_G"]:
        if w["G_int"] != [0, 0]:
            w["coef"]["re"] *= 0.9
    p.write_text(json.dumps(c))
    cand = "20990101T000000.000Z_swarm-a_req_beef"          # a candidate at R_gap_min 1.8
    (a.L.inbox("swarm-a") / cand).mkdir(parents=True)
    (a.L.inbox("swarm-a") / cand / "accepted.json").write_text(json.dumps(
        {"req_id": cand, "agent": "swarm-a", "parent": "w3", "stages": {"screen": {}}}))
    (a.L.inbox("swarm-a") / cand / "result.json").write_text(json.dumps({"R_gap_min": 1.8}))
    rid = A.submit(a, p, "ctl", parent="w3", control=True, clusters=["r56"], parents=[cand])
    b.tick()
    b.tick()
    h = read_json(a.L.inbox("swarm-a") / rid / "accepted.json")["stages"]["control"]["r56"]
    # The candidate was its parent's best, so the control inherited the top rank.
    assert b._priority(h) == 1 < b.PRIORITY_FIRST_STAGE


def test_control_on_claimed_candidate_runs_after_parents(tmp_path):
    cfg_path = ladder_config(tmp_path)
    cfg = load_swarm(cfg_path)
    setup(cfg, cfg_path, worktrees=False, solver=False)
    parents = build_parents(cfg)
    pool = MockPool(evaluator=evaluator)
    pool.hold = True
    b = ArmBroker(cfg, "swarm", pool, parents, load_pes_counts(cfg))
    a = A.Ctx(cfg, "swarm-a")
    p = tmp_path / "c.json"
    c = deformed(parents["w3"], 0.0)
    for w in c["form_factor"]["W_G"]:
        if w["G_int"] != [0, 0]:
            w["coef"]["re"] *= 0.9
    p.write_text(json.dumps(c))
    # A claimed candidate (1.2) far below its parent's best so far (3.0).
    for rid_, res in (("20990101T000000.000Z_swarm-a_req_aaaa", {"R_gap_min": 3.0}),
                      ("20990101T000000.000Z_swarm-a_req_bbbb", {"R_gap_min": 1.2, "claim": "strong"})):
        (a.L.inbox("swarm-a") / rid_).mkdir(parents=True)
        (a.L.inbox("swarm-a") / rid_ / "accepted.json").write_text(json.dumps(
            {"req_id": rid_, "agent": "swarm-a", "parent": "w3", "stages": {"screen": {}}}))
        (a.L.inbox("swarm-a") / rid_ / "result.json").write_text(json.dumps(res))
    rid = A.submit(a, p, "ctl", parent="w3", control=True, clusters=["r56"],
                   parents=["20990101T000000.000Z_swarm-a_req_bbbb"])
    b.tick()
    h = read_json(a.L.inbox("swarm-a") / rid / "accepted.json")["stages"]["control"]["r56"]
    assert b._priority_for(1.2, "w3") > 1
    assert b._priority(h) == 1


def test_failed_candidate_does_not_set_parent_best(tmp_path):
    cfg_path = ladder_config(tmp_path)
    cfg = load_swarm(cfg_path)
    setup(cfg, cfg_path, worktrees=False, solver=False)
    b = ArmBroker(cfg, "swarm", MockPool(evaluator=evaluator), build_parents(cfg), load_pes_counts(cfg))
    a = A.Ctx(cfg, "swarm-a")
    for rid_, res in (("20990101T000000.000Z_swarm-a_req_aaaa", {"R_gap_min": 2.1, "verdict": "FAIL"}),
                      ("20990101T000000.000Z_swarm-a_req_bbbb", {"R_gap_min": 1.5, "verdict": "PASS"})):
        (a.L.inbox("swarm-a") / rid_).mkdir(parents=True)
        (a.L.inbox("swarm-a") / rid_ / "accepted.json").write_text(json.dumps(
            {"req_id": rid_, "agent": "swarm-a", "parent": "w3", "stages": {"screen": {}}}))
        (a.L.inbox("swarm-a") / rid_ / "result.json").write_text(json.dumps(res))
    b._results()
    assert b._parent_best["w3"] == 1.5


def test_priority_is_relative_to_each_parent(tmp_path):
    cfg = load_swarm(ladder_config(tmp_path))
    b = ArmBroker(cfg, "swarm", MockPool(evaluator=evaluator), build_parents(cfg), load_pes_counts(cfg))
    b._parent_best = {"w3": 3.5, "w2": 1.3}
    # w2's best (1.3) and w3's best (3.5) rank together; a mediocre w3 (2.0) ranks below w2's best.
    assert b._priority_for(1.3, "w2") == b._priority_for(3.5, "w3")
    assert b._priority_for(1.3, "w2") < b._priority_for(2.0, "w3")
