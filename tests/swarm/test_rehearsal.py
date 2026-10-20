"""The rehearsal landscape has the traps it claims: R = 0 at the reference, a
real optimum on every cluster, a 4×6-only artifact, topology loss far out."""

from __future__ import annotations

from mosaic.ed.contract import EDInput
from mosaic.swarm.rehearsal import SyntheticLandscape

from .conftest import ed_input_dict


def _ed(w1=0.05, alpha=None, beta=0.0, mesh=(4, 6)):
    d = ed_input_dict(w1=w1)
    d["ed_solver_params"]["extra"].update(nk1=mesh[0], nk2=mesh[1])
    d["lattice"]["n_k"] = mesh[0] * mesh[1]
    if alpha is not None:
        d["form_factor"]["deformation"] = {"spatial_stars": [[[1, 0], [-1, 0]]], "momentum_stars": [[[1, 0], [-1, 0]]],
                                           "alpha": [[alpha]], "beta": [[beta]]}
    return EDInput.model_validate({**d, "config_hash": "f" * 64})


def test_landscape_traps():
    land = SyntheticLandscape(_ed())
    ratio = lambda e, mesh: land(e).gap_top_indirect_solver / land(_ed(mesh=mesh)).gap_top_indirect_solver - 1  # noqa: E731
    for mesh in ((4, 6), (5, 6)):
        assert abs(ratio(_ed(mesh=mesh), mesh)) < 1e-12
        assert ratio(_ed(w1=0.07, alpha=-0.08, mesh=mesh), mesh) > 0.02
    assert ratio(_ed(alpha=0.0, beta=0.06, mesh=(4, 6)), (4, 6)) > 0.02      # artifact on 4×6 ...
    assert ratio(_ed(alpha=0.0, beta=0.06, mesh=(5, 6)), (5, 6)) < 0.005     # ... absent on 5×6
    out = land(_ed(alpha=0.4))
    assert out.chern_solver == 0 and out.status == "failed_logical"
