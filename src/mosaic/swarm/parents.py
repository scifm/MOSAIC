"""Static parents.

A parent is a cluster-agnostic ``EDInput`` (broker-owned keys stripped). It is
either read from a file or built from static-density shell weights on the
solver-basis shells (120° basis) plus the regime template's interaction extras.
Shell-uniform weights are C3-symmetric by construction, which
``check_density`` verifies, together with Hermiticity, ``w_0 = 1`` and
``|h(r)|² >= 0``.
"""

from __future__ import annotations

import json
from fractions import Fraction

from mosaic.ed.contract import EDInput
from mosaic.physics.lattice import enumerate_shells
from mosaic.swarm.config import CLUSTER_KEYS, SwarmConfig
from mosaic.swarm.validate import PLACEHOLDER_CAMPAIGN, PLACEHOLDER_HASH, check_density, w_dict


def strip_owned(ed: EDInput) -> EDInput:
    p = ed.ed_solver_params
    extra = {k: v for k, v in p.extra.items() if k not in CLUSTER_KEYS}
    return ed.model_copy(update={"ed_solver_params": p.model_copy(update={"extra": extra}),
                                 "config_hash": PLACEHOLDER_HASH, "campaign_id": PLACEHOLDER_CAMPAIGN,
                                 "seed": 0, "proposer_x": None})


def shell_density(weights: list[str]) -> list[dict]:
    shells = enumerate_shells(len(weights))  # shells[0] is G = 0
    w = [{"shell": 0, "idx": 0, "G_int": [0, 0], "coef": {"re": 1.0, "im": 0.0}}]
    for s, raw in enumerate(weights, start=1):
        value = float(Fraction(raw))
        for i, g in enumerate(shells[s]):
            w.append({"shell": s, "idx": i, "G_int": list(g), "coef": {"re": value, "im": 0.0}})
    return w


def build_parents(cfg: SwarmConfig) -> dict[str, EDInput]:
    out = {}
    template = None
    if cfg.regime.template_ed_input:
        template = json.loads(cfg.path(cfg.regime.template_ed_input).read_text())
    for name, spec in cfg.parents.items():
        if spec.ed_input is not None:
            ed = EDInput.model_validate_json(cfg.path(spec.ed_input).read_text())
        else:
            body = json.loads(json.dumps(template))
            body["form_factor"] = {"symmetry": "C3_hard", "W_G": shell_density(spec.shells)}
            body["lattice"] = {**body["lattice"], "n_shells": len(spec.shells)}
            if cfg.regime.a_n is not None:
                body["wavefunction"] = {"n_a": len(cfg.regime.a_n),
                                        "a_n": [{"re": float(a), "im": 0.0} for a in cfg.regime.a_n],
                                        "norm_convention": body["wavefunction"].get("norm_convention", "renormalize_post")}
            body.update(config_hash=PLACEHOLDER_HASH, campaign_id=PLACEHOLDER_CAMPAIGN, seed=0)
            body.pop("proposer_x", None)
            ed = EDInput.model_validate(body)
            check_density(w_dict(ed), symmetry="C3_hard", positivity_tol=cfg.positivity_tol)
        out[name] = strip_owned(ed)
    return out


def m2_static(ed: EDInput) -> float:
    """``M2* = <rho_*^2>_uc = sum_G |w_G|^2`` for a normalized density (w_0 = 1)."""

    return float(sum(abs(v) ** 2 for v in w_dict(ed).values()))
