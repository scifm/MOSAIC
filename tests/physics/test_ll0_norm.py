"""physics.kdep_envelope.ll0_norm reproduces the solver's raw Gram diagonal
S_00(k) (MoireSolver.raw_overlap_matrix), static and strongly deformed."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from mosaic.physics.kdep_envelope import DeformationSpec, ll0_norm

FIXTURE = Path(__file__).resolve().parents[1] / "fixtures" / "ll0_norm_reference.json"


@pytest.mark.parametrize("name", ["w3_a1p", "w3_strong"])
def test_ll0_norm_matches_solver(name):
    case = json.loads(FIXTURE.read_text())["cases"][name]
    ff = case["form_factor"]
    w0 = {tuple(c["G_int"]): complex(c["coef"]["re"], c["coef"]["im"]) for c in ff["W_G"]}
    blk = ff["deformation"]
    spec = DeformationSpec.from_block(blk)
    for k, ref in zip(case["k"], case["S00"]):
        got = ll0_norm(w0, spec, tuple(k), n_mesh=blk["n_mesh"], g_cutoff=blk.get("g_cutoff"))
        assert got == pytest.approx(ref, rel=1e-12)
