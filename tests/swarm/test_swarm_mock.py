"""End-to-end swarm test against the mock ED (< 60 s).

Scripted fake agents drive the real broker, file protocol and digest; only
Slurm and the solver are replaced (``MockPool`` with a deterministic
evaluator)."""

from __future__ import annotations

import json
import multiprocessing as mp
import shutil
import subprocess
from pathlib import Path

import pytest

from mosaic.store.state import RunState
from mosaic.swarm import agent as A
from mosaic.swarm.broker import ArmBroker, BrokerHalt, run
from mosaic.swarm.parents import build_parents
from mosaic.swarm.config import load_swarm
from mosaic.swarm.files import read_json, read_markdown_with_front_matter, visible_entries
from mosaic.swarm.layout import ArmLayout
from mosaic.swarm.pool import MockPool, render_pool_script
from mosaic.swarm.setup import permission_settings, render_agents_job, render_charter, setup
from mosaic.swarm.validate import RequestRejected, normalise

from .conftest import ed_input_dict, mock_evaluator, write_config


def _submit(ctx: A.Ctx, tmp_path: Path, name: str, family: str = "fam", **kw) -> str:
    p = tmp_path / f"{ctx.agent}-{name}.json"
    p.write_text(json.dumps(ed_input_dict(**kw)))
    return A.submit(ctx, p, family)


def _brokers(cfg, pool):
    parents = build_parents(cfg)
    return {arm: ArmBroker(cfg, arm, pool, parents, {}) for arm in cfg.arms}


def _tick(brokers, n=1):
    for _ in range(n):
        for b in brokers.values():
            b.tick()


def _result(ctx: A.Ctx, rid: str) -> dict:
    return read_json(ctx.L.inbox(ctx.agent) / rid / "result.json")


def test_end_to_end_two_arms(cfg, cfg_path, tmp_path):
    setup(cfg, cfg_path, worktrees=False, solver=False)
    pool = MockPool(evaluator=mock_evaluator)
    brokers = _brokers(cfg, pool)
    a, b, c = A.Ctx(cfg, "swarm-a"), A.Ctx(cfg, "swarm-b"), A.Ctx(cfg, "ctrl-a")

    win = _submit(a, tmp_path, "win", family="shell1-up", w1=0.07)        # R = +4 % everywhere
    loss = _submit(a, tmp_path, "loss", family="shell1-down", w1=0.04)    # R = −2 %
    dup = _submit(b, tmp_path, "dup", family="shell1-up", w1=0.07)        # same physics as `win`
    bad_path = tmp_path / "bad.json"
    bad = ed_input_dict(w1=0.07)
    bad["ed_solver_params"]["extra"]["qmax"] = 10                          # fixed by the reference
    bad_path.write_text(json.dumps(bad))
    with pytest.raises(RequestRejected, match="qmax"):
        A.submit(a, bad_path, "x")
    ctl = _submit(c, tmp_path, "ctl", family="shell1-up", w1=0.07)

    _tick(brokers, 4)

    r = _result(a, win)
    assert r["status"] == "done" and r["stage_reached"] == "confirm" and r["claim"] == "win"
    assert r["R_gap_min"] == pytest.approx(1.04) and r["clusters"]["s27"]["R_gap"] == pytest.approx(1.04)
    assert r["clusters"]["s27"]["chern"] is None and r["clusters"]["s27"]["verdict"] == "PASS"
    r = _result(a, loss)
    assert r["status"] == "done" and r["stage_reached"] == "screen" and r["R_gap_min"] == pytest.approx(0.98)
    assert "s27" not in r["clusters"] and r["claim"] is None

    # Deduplication: b's request is the same evaluations, served free.
    acc_a = read_json(a.L.inbox("swarm-a") / win / "accepted.json")
    acc_b = read_json(b.L.inbox("swarm-b") / dup / "accepted.json")
    assert acc_a["stages"] == acc_b["stages"]
    assert acc_a["charged_evaluations"] == 2 and acc_b["charged_evaluations"] == 0
    assert _result(b, dup)["R_gap_min"] == pytest.approx(1.04)

    # Shared arm: any agent's request is readable; private arm: only one's own.
    assert A.show(b, win)["agent"] == "swarm-a" and A.show(b, win)["result"]["claim"] == "win"
    with pytest.raises(SystemExit):
        A.show(c, win)
    rep = A.reference_report(a)
    assert "p1" in rep and "4×6" in rep and "Stage ladder" in rep and "win" in rep

    # The control arm is a separate campaign with its own store and reference.
    acc_c = read_json(c.L.inbox("ctrl-a") / ctl / "accepted.json")
    assert set(acc_c["stages"]["screen"].values()).isdisjoint(acc_a["stages"]["screen"].values())
    assert _result(c, ctl)["claim"] == "win"

    # Leaderboard: store-derived, best first; private arm sees only its own rows.
    lb = read_json(a.L.leaderboard_json)
    assert [row["req_id"] for row in lb["leaderboards"]["p1"]][:1] in ([win], [dup])
    assert lb["budget"]["swarm-a"]["charged"] == 4 and lb["budget"]["swarm-b"]["charged"] == 0
    own = read_json(c.L.agent_dir("ctrl-a") / "leaderboard.json")
    assert {row["agent"] for row in own["leaderboards"]["p1"]} == {"ctrl-a"}

    # One reference evaluation per cluster per arm; no evaluation ran twice.
    for arm, br in brokers.items():
        counts = br.store.count_by_state(br.campaign)
        assert counts == {RunState.COMPLETED: counts.get(RunState.COMPLETED, 0),
                          RunState.FAILED_LOGICAL: counts.get(RunState.FAILED_LOGICAL, 0)}
    n_runs = sum(len(list(ArmLayout(cfg, arm).runs_dir.iterdir())) for arm in cfg.arms)
    # swarm: ref 3 + win 2 + loss 2 + s27 confirm 1 ; control: ref 3 + ctl 2 + confirm 1
    assert n_runs == 8 + 6


def test_board_mail_roster_and_digest(cfg, cfg_path, tmp_path):
    setup(cfg, cfg_path, worktrees=False, solver=False)
    a, b, c = A.Ctx(cfg, "swarm-a"), A.Ctx(cfg, "swarm-b"), A.Ctx(cfg, "ctrl-a")
    A.heartbeat(a, current_family="shell1-up", note="mapping shell 1")
    pid = A.post(a, "hypothesis", "shell1-up", "first shell up helps", "Expect R > 0 on both clusters.")
    A.mail(a, "swarm-b", "your family", "Looks like a relabelling of mine.", refs=[pid])
    A.post(c, "note", "x", "control note", "private")

    d = A.digest(b)
    assert pid in d and "first shell up helps" in d
    assert "Looks like a relabelling of mine." in d and "swarm-a: active, family=shell1-up" in d
    assert "control note" not in d
    d2 = A.digest(b)
    assert pid not in d2 and "Unread mail (0)" in d2          # marked read

    dc = A.digest(c)
    assert "control note" in dc and pid not in dc and "Roster" not in dc
    with pytest.raises(SystemExit):
        A.mail(c, "ctrl-b", "s", "private arms have no mail")
    with pytest.raises(SystemExit):
        A.read_item(c, pid)                                     # swarm post invisible to control

    hid = A.human_post(cfg, "swarm", "answer", "The real solver reads every column.", to="swarm-b", refs=[pid])
    d3 = A.digest(b)
    assert hid in d3 and "from human: answer" in d3
    A.human_post(cfg, "control", "private answer", "only ctrl-a sees this", to="ctrl-a")
    assert "private answer" in A.digest(c) and "private answer" not in A.digest(a)

    A.done(a, "spent")
    assert any(s["name"] == "swarm-a" and s["state"] == "done" for s in A.roster(b))


def test_quota_and_in_flight_order(tmp_path):
    cfg_path = write_config(tmp_path, **{"quotas.evaluations_per_agent": 4, "quotas.max_in_flight_per_agent": 1})
    cfg = load_swarm(cfg_path)
    setup(cfg, cfg_path, worktrees=False, solver=False)
    pool = MockPool(evaluator=mock_evaluator)
    pool.hold = True                                              # evaluations never finish
    brokers = _brokers(cfg, pool)
    a = A.Ctx(cfg, "swarm-a")
    r1, r2, r3 = (_submit(a, tmp_path, f"r{i}", w1=0.05 + 0.01 * i) for i in (1, 2, 3))
    _tick(brokers)
    assert _result(a, r1)["status"] == "pending"
    assert _result(a, r2) is None and _result(a, r3) is None    # waiting behind the in-flight cap
    pool.hold = False
    pool.alive.clear()                                            # the held job "ends": requeue + run
    _tick(brokers, 8)                                             # r1, then r2, each screened and promoted
    assert _result(a, r1)["status"] == "done"
    assert _result(a, r2)["status"] == "done"
    assert _result(a, r3)["status"] == "rejected" and "quota" in _result(a, r3)["reason"]


def test_restart_requeues_dead_claims_without_duplicates(cfg, cfg_path, tmp_path):
    setup(cfg, cfg_path, worktrees=False, solver=False)
    pool = MockPool(evaluator=mock_evaluator)
    pool.hold = True
    brokers = _brokers(cfg, pool)
    a = A.Ctx(cfg, "swarm-a")
    rid = _submit(a, tmp_path, "x", w1=0.07)
    _tick(brokers)
    br = brokers["swarm"]
    held = br.store.list_by_state(RunState.RUNNING, RunState.SUBMITTED, campaign_id=br.campaign)
    assert held and all((br.store.run_dir(r.config_hash) / ".claimed" / "job").exists() for r in held)
    for b in brokers.values():
        b.close()

    # "kill -9": the held job dies, a fresh broker process starts.
    pool2 = MockPool(evaluator=mock_evaluator)
    brokers2 = _brokers(cfg, pool2)
    _tick(brokers2, 4)
    br2 = brokers2["swarm"]
    assert _result(a, rid)["status"] == "done" and _result(a, rid)["stage_reached"] == "confirm"
    for r in held:
        # s27 ends FAILED_LOGICAL by design (mesh_unsuitable_for_chern, gap valid).
        assert br2.store.get(r.config_hash).state in (RunState.COMPLETED, RunState.FAILED_LOGICAL)
        assert br2.store.get_result(r.config_hash).gap_top_indirect is not None
        assert br2.store.retry_count(r.config_hash) == 1
    assert len(list(br2.L.runs_dir.iterdir())) == 3 + 2 + 1


def test_transient_failures_exhaust_retries(cfg, cfg_path, tmp_path):
    setup(cfg, cfg_path, worktrees=False, solver=False)

    def always_transient(ed):
        return mock_evaluator(ed).model_copy(update={"status": "failed_transient", "failure_reason": "oom",
                                                     "gap_top_indirect_solver": None})

    ref_ok = MockPool(evaluator=mock_evaluator)
    brokers = _brokers(cfg, ref_ok)
    _tick(brokers, 2)                                            # reference done
    a = A.Ctx(cfg, "swarm-a")
    rid = _submit(a, tmp_path, "x", w1=0.07)
    ref_ok.evaluator = always_transient
    _tick(brokers, 6)
    r = _result(a, rid)
    assert r["status"] == "failed"
    assert all(c["verdict"] == "FAIL" and c["reasons"] == ["transient failures exhausted"]
               for c in r["clusters"].values())


def test_crash_between_register_and_accept_charges_once(cfg, cfg_path, tmp_path):
    setup(cfg, cfg_path, worktrees=False, solver=False)
    pool = MockPool(evaluator=mock_evaluator)
    brokers = _brokers(cfg, pool)
    a = A.Ctx(cfg, "swarm-a")
    rid = _submit(a, tmp_path, "x", w1=0.07)
    br = brokers["swarm"]
    orig = br._register

    def register_then_crash(ed, cluster, proposer, git_sha=None):
        orig(ed, cluster, proposer, git_sha)
        raise KeyboardInterrupt  # dies before accepted.json is written

    br._register = register_then_crash
    with pytest.raises(KeyboardInterrupt):
        br._accept_requests()
    br._register = orig
    _tick(brokers, 3)
    acc = read_json(a.L.inbox("swarm-a") / rid / "accepted.json")
    assert acc["charged_evaluations"] == 2
    assert read_json(a.L.leaderboard_json)["budget"]["swarm-a"]["charged"] == 2


def test_partial_output_is_transient(cfg, cfg_path, tmp_path):
    setup(cfg, cfg_path, worktrees=False, solver=False)
    pool = MockPool(evaluator=mock_evaluator)
    pool.hold = True
    brokers = _brokers(cfg, pool)
    _tick(brokers)
    br = brokers["swarm"]
    rec = br.store.list_by_state(RunState.RUNNING, RunState.SUBMITTED, campaign_id=br.campaign)[0]
    (br.store.run_dir(rec.config_hash) / "ed_output.json").write_text('{"config_hash": "trunc')
    br._reconcile()
    assert br.store.get(rec.config_hash).state == RunState.FAILED_TRANSIENT
    assert list(br.store.run_dir(rec.config_hash).glob("ed_output.transient-*.json"))


def test_parent_drift_halts(tmp_path):
    cfg_path = write_config(tmp_path, **{"parents.p1.expected_gap": {"4x6": 0.05}})
    cfg = load_swarm(cfg_path)
    setup(cfg, cfg_path, worktrees=False, solver=False)
    pool = MockPool(evaluator=mock_evaluator)
    assert run(cfg_path, once=True, backend=pool) == 0           # reference queued and run
    assert run(cfg_path, once=True, backend=pool) == 3           # ingested: 0.03 != 0.05
    assert "parent p1 gap on 4x6" in (cfg.root_path / "HALT").read_text()
    assert run(cfg_path, once=True, backend=pool) == 3           # stays halted
    assert "BROKER HALTED" in A.digest(A.Ctx(cfg, "swarm-a"))


def test_solver_version_mismatch_halts(cfg, cfg_path):
    setup(cfg, cfg_path, worktrees=False, solver=False)
    pool = MockPool(evaluator=lambda ed: mock_evaluator(ed).model_copy(update={"solver_version": "other@v9"}))
    brokers = _brokers(cfg, pool)
    with pytest.raises(BrokerHalt, match="solver"):
        _tick(brokers, 2)


def test_validation_rules(cfg):
    ref = build_parents(cfg)["p1"]
    ok = ed_input_dict(w1=0.07)
    base = normalise(ok, ref, cfg)
    assert "nk1" not in base.ed_solver_params.extra                  # cluster keys belong to the broker
    cases = {
        "Hermitian": lambda d: d["form_factor"]["W_G"][1]["coef"].update(im=0.1),
        "exactly 1": lambda d: d["form_factor"]["W_G"][0]["coef"].update(re=1.1),
        "negative": lambda d: [c["coef"].update(re=-0.4) for c in d["form_factor"]["W_G"][1:]],
        "fixed at": lambda d: d["ed_solver_params"]["extra"].update(D_l=0.3),
        "<absent>": lambda d: d["ed_solver_params"]["extra"].update(ed_mode="symmetry_reduced_ed"),
        "deformation": lambda d: d["form_factor"].update(deformation={
            "spatial_stars": [[[1, 0]]], "momentum_stars": [[[1, 0], [-1, 0]]], "alpha": [[0.1]], "beta": [[0.0]]}),
    }
    for reason, mutate in cases.items():
        d = ed_input_dict(w1=0.07)
        mutate(d)
        with pytest.raises(RequestRejected, match=reason):
            normalise(d, ref, cfg)
    # C3_hard must be true in the solver's 120° basis.
    sym = ed_input_dict(w1=0.07, symmetry="C3_hard")
    normalise(sym, ref, cfg)                                          # shell-1 constant: symmetric
    sym["form_factor"]["W_G"][1]["coef"]["re"] = 0.06
    sym["form_factor"]["W_G"][2]["coef"]["re"] = 0.06
    with pytest.raises(RequestRejected, match="C3_hard"):
        normalise(sym, ref, cfg)


def _atomic_writer(args):
    cfg_path, agent, n = args
    ctx = A.Ctx(load_swarm(cfg_path), agent)
    return [A.post(ctx, "note", "f", f"t{i}", "x" * 2000) for i in range(n)]


def test_concurrent_posts_are_atomic(cfg, cfg_path):
    setup(cfg, cfg_path, worktrees=False, solver=False)
    with mp.get_context("spawn").Pool(4) as p:
        ids = sum(p.map(_atomic_writer, [(str(cfg_path), a, 25) for a in ("swarm-a", "swarm-b") * 2]), [])
    assert len(ids) == len(set(ids)) == 100
    posts = visible_entries(ArmLayout(cfg, "swarm").board_dir("swarm-a"), ".md")
    assert len(posts) == 100
    for p in posts:
        meta, body = read_markdown_with_front_matter(p)
        assert body.strip() == "x" * 2000


def test_rendered_scripts_and_guardrails(cfg, cfg_path, tmp_path):
    for name, tier in cfg.broker.tiers.items():
        script = tmp_path / f"pool_{name}.sh"
        script.write_text(render_pool_script(cfg, name, tier, tmp_path / "pool", tmp_path))
        subprocess.run(["bash", "-n", str(script)], check=True)
        if tier.gpus:
            assert "--gres=gpu:1" in script.read_text() and "MOIRE_ED_BACKEND=gpu" in script.read_text()
    for arm in cfg.arms:
        script = tmp_path / f"agents_{arm}.sh"
        script.write_text(render_agents_job(cfg, arm, cfg_path))
        subprocess.run(["bash", "-n", str(script)], check=True)
    for s in ("scripts/swarm_agent.sh", "scripts/swarm_login.sh", "swarm/bin/swarm"):
        subprocess.run(["bash", "-n", str(Path(cfg.repo_main) / s)], check=True)

    ctrl = permission_settings(cfg, "ctrl-a")["permissions"]["deny"]
    assert f"Read(/{cfg.arm_root('swarm')}/**)" in ctrl
    assert any("ctrl-b" in d and d.startswith("Read(") for d in ctrl)
    assert "Bash(sbatch *)" in ctrl and "Edit(/src/**)" in ctrl
    swarm = permission_settings(cfg, "swarm-a")["permissions"]["deny"]
    assert f"Read(/{cfg.arm_root('control')}/**)" in swarm

    # Self-directed (no predefined direction), with a shared mission brief.
    brief = tmp_path / "brief.md"
    brief.write_text("Find the largest gap.")
    free = cfg.model_copy(update={"directions": {}, "mission": str(brief)})
    s_free, p_free = render_charter(free, "swarm-a"), render_charter(free, "ctrl-a")
    assert "Choosing your own scope" in s_free and "Your starting direction" not in s_free
    assert "Prefer directions nobody covers" in s_free and "Prefer directions nobody covers" not in p_free
    assert "The campaign brief" in s_free and "Find the largest gap." in p_free
    assert "sleep $((i * 0))" in render_agents_job(cfg, "swarm", cfg_path)

    shared, private = render_charter(cfg, "swarm-a"), render_charter(cfg, "ctrl-a")
    assert "swarm mail" in shared and "SendMessage" in shared
    assert "swarm mail" not in private and "independently" in private and "share a board" not in private


def test_setup_creates_worktrees_and_snapshot_idempotently(tmp_path):
    repo = tmp_path / "repo"
    (repo / "swarm").mkdir(parents=True)
    shutil.copytree(Path(__file__).resolve().parents[1] / "fixtures" / "directions", repo / "tests" / "fixtures" / "directions")
    (repo / "julia").mkdir()
    (repo / "julia" / "ed_solver.jl").write_text("# solver\n")
    (repo / ".gitignore").write_text("julia/Manifest.toml\n")
    (repo / "julia" / "Manifest.toml").write_text(f'[[deps.Pkg]]\npath = "{repo}/julia/Pkg.jl/Pkg"\n')
    git = lambda *a: subprocess.run(["git", *a], cwd=repo, check=True, capture_output=True, text=True).stdout.strip()  # noqa: E731
    git("init", "-q")
    git("-c", "user.name=t", "-c", "user.email=t@t", "add", ".")
    git("-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "init")
    sha = git("rev-parse", "--short", "HEAD")
    cfg_path = write_config(tmp_path, repo_main=str(repo), **{"broker.solver_ref": sha})
    cfg = load_swarm(cfg_path)

    first = setup(cfg, cfg_path)
    again = setup(cfg, cfg_path)                                    # idempotent
    assert first["arms"]["swarm"]["agents"]["swarm-a"]["session_uuid"] == \
        again["arms"]["swarm"]["agents"]["swarm-a"]["session_uuid"]
    assert (cfg.solver_dir / "julia" / "ed_solver.jl").exists()
    man = (cfg.solver_dir / "julia" / "Manifest.toml").read_text()
    assert f'path = "{cfg.solver_dir}/julia/Pkg.jl/Pkg"' in man and str(repo) + "/" not in man
    assert git("rev-parse", "--short", "HEAD") == sha
    for agent in ("swarm-a", "ctrl-b"):
        wt = cfg.worktree(agent)
        assert (wt / "CHARTER.md").exists() and (wt / "NOTEBOOK.md").exists() and (wt / "work").is_dir()
        settings = json.loads((wt / ".claude" / "settings.local.json").read_text())
        assert "Bash(sbatch *)" in settings["permissions"]["deny"]
    assert f"swarm/test-swarm/swarm-a" in git("branch", "--list", "swarm/*")
    env = __import__("mosaic.swarm.setup", fromlist=["agent_env"]).agent_env(cfg, "swarm-a", cfg_path)
    assert "SWARM_SESSION_UUID" in env and "/loop" in env
    # The wrapper evals these lines; backticks in the prompt must survive verbatim.
    out = subprocess.run(["bash", "-c", env + 'printf %s "$SWARM_PROMPT"'], capture_output=True, text=True).stdout
    assert out == __import__("mosaic.swarm.setup", fromlist=["LOOP_PROMPT"]).LOOP_PROMPT and "`swarm digest`" in out
    assert (cfg.arm_root("swarm") / "agents_job.sbatch").exists()


def test_acceptance_is_capped_and_round_robin(tmp_path):
    cfg_path = write_config(tmp_path, **{"broker.max_accepts_per_tick": 2})
    cfg = load_swarm(cfg_path)
    setup(cfg, cfg_path, worktrees=False, solver=False)
    pool = MockPool(evaluator=mock_evaluator)
    pool.hold = True
    brokers = _brokers(cfg, pool)
    a, b = A.Ctx(cfg, "swarm-a"), A.Ctx(cfg, "swarm-b")
    ra = [_submit(a, tmp_path, f"a{i}", w1=0.05 + 0.001 * i) for i in range(3)]
    rb = [_submit(b, tmp_path, f"b{i}", w1=0.06 + 0.001 * i) for i in range(3)]
    brokers["swarm"]._accept_requests()
    accepted = lambda ctx, rs: [(ctx.L.inbox(ctx.agent) / r / "accepted.json").exists() for r in rs]  # noqa: E731
    assert accepted(a, ra) == [True, False, False] and accepted(b, rb) == [True, False, False]
