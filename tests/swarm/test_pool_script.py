"""Run the rendered pool job script for real (bash, no Slurm) against a fake
solver: lanes claim pool entries through the symlinks, write the claim's job
id and rc, never run an evaluation twice, and exit when the pool stays empty."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from mosaic.swarm.config import load_swarm
from mosaic.swarm.pool import render_pool_script

from .conftest import ed_input_dict, write_config

FAKE_SOLVER = """#!/bin/bash
# fake julia: <solver> --config IN --out OUT ; FAIL_ON=<substring> makes it crash
[ -n "${{FAIL_ON:-}}" ] && [[ "$3" == *"$FAIL_ON"* ]] && exit 7
"{python}" - "$3" "$5" <<'PY'
import json, sys
sys.path.insert(0, "{repo}")
from mosaic.ed.contract import EDInput
from tests.swarm.conftest import mock_evaluator
ed = EDInput.model_validate_json(open(sys.argv[1]).read())
open(sys.argv[2], "w").write(mock_evaluator(ed).model_dump_json())
PY
"""


def test_pool_lanes_claim_run_and_exit(tmp_path):
    cfg_path = write_config(tmp_path, **{"broker.idle_exit_seconds": 1, "broker.poll_seconds": 1})
    cfg = load_swarm(cfg_path)
    fake = tmp_path / "fake_julia"
    fake.write_text(FAKE_SOLVER.format(python=sys.executable, repo=Path(__file__).resolve().parents[2]))
    fake.chmod(0o755)
    cfg.broker.julia = str(fake)

    pool, runs = tmp_path / "pool", tmp_path / "runs"
    pool.mkdir()
    hashes = []
    for i, w1 in enumerate((0.05, 0.06, 0.07, 0.08)):
        h = f"{i:064x}"
        d = runs / h
        d.mkdir(parents=True)
        body = {**ed_input_dict(w1=w1), "config_hash": h}
        (d / "ed_input.json").write_text(json.dumps(body))
        (pool / f"2026_{i}_{h}").symlink_to(d)
        hashes.append(h)
    (runs / hashes[3] / ".claimed").mkdir()                      # held by another job: must be skipped

    script = tmp_path / "pool.sh"
    script.write_text(render_pool_script(cfg, "cpu", cfg.broker.tiers["cpu"], pool, tmp_path))
    env = {**os.environ, "SLURM_JOB_ID": "4242", "FAIL_ON": hashes[2]}
    proc = subprocess.run(["bash", str(script)], env=env, capture_output=True, text=True, timeout=60)
    assert proc.returncode == 0, proc.stderr
    logs = "\n".join((runs / h / "solver.log").read_text() for h in hashes[:3] if (runs / h / "solver.log").exists())

    for h in hashes[:2]:
        d = runs / h
        assert (d / "ed_output.json").exists(), proc.stdout + logs
        assert json.loads((d / "ed_output.json").read_text())["status"] == "completed"
        assert (d / ".claimed" / "job").read_text().strip() == "4242"
        assert (d / ".claimed" / "rc").read_text().strip() == "0"
    crashed = runs / hashes[2]
    assert not (crashed / "ed_output.json").exists() and (crashed / ".claimed" / "rc").read_text().strip() == "7"
    assert not (runs / hashes[3] / "ed_output.json").exists()     # never touched
    assert proc.stdout.count(" start ") == 3 and "idle, exiting" in proc.stdout


FAKE_BATCH = """#!/bin/bash
# fake julia: <ed_batch.jl> PASS_DIR PATTERN ; logs each pass, then runs it
echo "pass $(ls "$2" | tr '\\n' ' ')" >> "{log}"
for d in "$2"/*; do
  mkdir "$d/.claimed" 2>/dev/null || continue
  echo '{{}}' > "$d/ed_output.json"
done
"""


def test_persistent_passes_take_the_queue_head(tmp_path):
    # A pass reads its list once, so it must be short: the broker reorders the
    # pool between passes, and the next pass starts from the new head.
    cfg_path = write_config(tmp_path, **{"broker.idle_exit_seconds": 1, "broker.poll_seconds": 1})
    cfg = load_swarm(cfg_path)
    log = tmp_path / "passes.log"
    fake = tmp_path / "fake_julia"
    fake.write_text(FAKE_BATCH.format(log=log))
    fake.chmod(0o755)
    cfg.broker.julia = str(fake)
    tier = cfg.broker.tiers["cpu"].model_copy(update={"lane_mode": "persistent", "pass_size": 2, "lanes": 1})

    pool, runs = tmp_path / "pool", tmp_path / "runs"
    pool.mkdir()
    for i in range(5):
        d = runs / f"{i:064x}"
        d.mkdir(parents=True)
        (d / "ed_input.json").write_text("{}")
        (pool / f"{9 - i:07d}_{i:064x}").symlink_to(d)

    script = tmp_path / "pool.sh"
    script.write_text(render_pool_script(cfg, "cpu", tier, pool, tmp_path))
    proc = subprocess.run(["bash", str(script)], env={**os.environ, "SLURM_JOB_ID": "4242"},
                          capture_output=True, text=True, timeout=60)
    assert proc.returncode == 0, proc.stderr
    passes = [line.split()[1:] for line in log.read_text().splitlines()]
    assert [len(p) for p in passes] == [2, 2, 1]
    assert [n.split("_")[0] for p in passes for n in p] == ["0000005", "0000006", "0000007", "0000008", "0000009"]
    assert all((runs / f"{i:064x}" / "ed_output.json").exists() for i in range(5))
