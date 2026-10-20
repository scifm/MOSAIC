"""Request validation and cluster expansion.

An agent may change the *physics of the band*: ``wavefunction`` and
``form_factor``. With ``regime.pin_static`` only the deformation block may
differ from the named parent. Everything else (interaction, ``d_s``, ``qmax``,
filling, units) is fixed by the parent. The cluster, the accuracy mode and
the PES request are chosen by the broker.

Every check fails loudly with a reason the agent can act on; nothing is
silently corrected except filling in fixed keys the agent left out.
"""

from __future__ import annotations

import numpy as np

from mosaic.ed.contract import EDInput
from mosaic.physics.kdep_envelope import DeformationSpec, ll0_norm_batch, m2_k_batch
from mosaic.physics.lattice import apply_R
from mosaic.swarm.config import CLUSTER_KEYS, ClusterSpec, SwarmConfig
from mosaic.util.hashing import content_hash

PLACEHOLDER_HASH = "0" * 64
PLACEHOLDER_CAMPAIGN = "unassigned"
_HASH_EXCLUDE = {"config_hash", "seed", "proposer_x"}


class RequestRejected(ValueError):
    """The request is malformed or outside the search space. ``str()`` is the reason."""


def config_hash(ed_input: EDInput) -> str:
    """Identity of an evaluation: same rule as every other campaign (the body
    without ``config_hash``, ``seed`` and ``proposer_x``)."""

    return content_hash(ed_input.model_dump(mode="json", exclude=_HASH_EXCLUDE))


def parse_agent_input(raw: dict) -> EDInput:
    """Schema-validate an agent's ``ed_input.json``; identity fields may be absent."""

    data = dict(raw)
    data.setdefault("config_hash", PLACEHOLDER_HASH)
    data.setdefault("campaign_id", PLACEHOLDER_CAMPAIGN)
    data.setdefault("seed", 0)
    try:
        return EDInput.model_validate(data)
    except Exception as exc:  # pydantic's error text is the useful reason
        raise RequestRejected(f"schema: {exc}") from exc


def w_dict(ed_input: EDInput) -> dict[tuple[int, int], complex]:
    w: dict[tuple[int, int], complex] = {}
    for c in ed_input.form_factor.W_G:
        g = (int(c.G_int[0]), int(c.G_int[1]))
        if g in w:
            raise RequestRejected(f"W_G lists {g} twice")
        w[g] = c.coef.to_python()
    return w


def check_density(w: dict[tuple[int, int], complex], *, symmetry: str, positivity_tol: float,
                  grid: int = 96) -> None:
    """``w_0 = 1``, Hermiticity, honest ``C3_hard`` label, and ``|h(r)|² >= 0``.

    The C3 test uses the solver's 120° basis: a density labelled
    ``C3_hard`` must satisfy ``w(R G) = w(G)``. Densities derived from seeds
    labelled in the older 60° basis are not C3-symmetric in the 120° basis and
    must be labelled ``none``.
    """

    if abs(w.get((0, 0), 0) - 1.0) > 1e-12:
        raise RequestRejected(f"w_(0,0) must be exactly 1, got {w.get((0, 0))}")
    for g, v in w.items():
        mg = (-g[0], -g[1])
        if mg not in w or abs(v - np.conj(w[mg])) > 1e-9:
            raise RequestRejected(f"W_G not Hermitian at {g}: needs w_(-G) = conj(w_G)")
    if symmetry == "C3_hard":
        for g, v in w.items():
            rg = apply_R(g)
            if rg not in w or abs(w[rg] - v) > 1e-9:
                raise RequestRejected(
                    f"symmetry=C3_hard but w(R·{g}) != w({g}) in the solver's 120° basis "
                    "(G = m G1 + n G2); label the density 'none' or symmetrise it")
    # |h(r)|² on a grid of fractional coordinates r = x1 a1 + x2 a2, where
    # a_i · G_j = 2π δ_ij, so G·r = 2π (m x1 + n x2) in any basis convention.
    x = np.arange(grid) / grid
    rho = np.zeros((grid, grid))
    for (m, n), v in w.items():
        rho += np.real(v * np.exp(2j * np.pi * (m * x[:, None] + n * x[None, :])))
    if rho.min() < -positivity_tol:
        raise RequestRejected(f"density |h(r)|² is negative (min {rho.min():.3g}); not a probability density")


def _deformation(ed: EDInput) -> tuple[DeformationSpec | None, dict]:
    block = ed.form_factor.deformation
    if block is None:
        return None, {}
    b = block.model_dump(mode="json")
    return DeformationSpec.from_block(b), {"n_mesh": b["n_mesh"], "g_cutoff": b.get("g_cutoff")}


def tightened(settings: dict, overrides: dict) -> dict:
    """Convergence overrides only ever tighten: each numeric field becomes the
    larger of the request's value and the override (a request already run at
    a finer setting is never re-run coarser). ``None`` = the solver default."""

    out = dict(settings)
    for k, v in overrides.items():
        cur = out.get(k)
        out[k] = v if cur is None else max(cur, v)
    return out


def _is_pure_ll0(ed: EDInput) -> bool:
    a = [abs(x.to_python()) ** 2 for x in ed.wavefunction.a_n]
    return a[0] > 0 and all(v < 1e-24 for v in a[1:])


def sample_momenta(cfg: SwarmConfig) -> list[tuple[float, float]]:
    """A dense fractional grid plus every rectangular ED mesh in the config.
    The symmetric clusters' momenta lie inside the BZ and are covered by the
    dense grid, as are the twist-shifted points the Chern step uses."""

    n = cfg.gates.admissibility_grid
    pts = {(i / n, j / n) for i in range(n) for j in range(n)}
    for c in cfg.clusters.values():
        if c.nk1 is not None:
            pts |= {(i / c.nk1, j / c.nk2) for i in range(c.nk1) for j in range(c.nk2)}
    return sorted(pts)


def admissibility(ed: EDInput, cfg: SwarmConfig) -> dict:
    """``S_00(k)`` positivity and conditioning, for every
    (n_mesh, g_cutoff) the request will be evaluated with."""

    spec, kw = _deformation(ed)
    w0 = w_dict(ed)
    variants = [kw] + [tightened(kw, c.deformation_overrides) for c in cfg.clusters.values() if c.deformation_overrides]
    worst = None
    ks = sample_momenta(cfg)
    for v in variants if spec is not None else [{}]:
        # Batched: the broker accepts hundreds of requests per tick on a
        # throttled login node (per-k loops made a tick take 14 min).
        vals = ll0_norm_batch(w0, spec, ks, **v)
        row = {"min": float(vals.min()), "max": float(vals.max()),
               "ratio": float(vals.min() / vals.max()) if vals.max() > 0 else float("-inf"), "settings": v}
        if worst is None or row["ratio"] < worst["ratio"]:
            worst = row
    return worst


def boundary_check(spec: DeformationSpec, m2k: float, m2_parent: float, bound) -> dict:
    """Measure a deformation against the search boundary (``BoundarySpec``);
    returns the measurements and the list of violated bounds."""

    g2 = max(max(m * m + n * n - m * n for m, n in star) for star in spec.spatial_stars)
    r2 = max(max(m * m + n * n + m * n for m, n in star) for star in spec.momentum_stars)
    a, b = np.abs(np.asarray(spec.alpha)), np.abs(np.asarray(spec.beta))
    used = (a > 0) | (b > 0)
    g2_used = max((max(m * m + n * n - m * n for m, n in spec.spatial_stars[s]) for s in range(a.shape[0]) if used[s].any()), default=0)
    r2_used = max((max(m * m + n * n + m * n for m, n in spec.momentum_stars[q]) for q in range(a.shape[1]) if used[:, q].any()), default=0)
    m = {"spatial_g2_max": g2_used, "momentum_r2_max": r2_used, "alpha_max": float(a.max()), "beta_max": float(b.max()),
         "alpha_sum_max": float(a.sum()), "beta_sum_max": float(b.sum()), "m2k_max_ratio": m2k / m2_parent}
    violated = [f"{k} = {v:.4g} > {getattr(bound, k):g}" for k, v in m.items() if v > getattr(bound, k)]
    return {"measured": m, "declared_g2_max": g2, "declared_r2_max": r2, "violated": violated}


def m2_k(ed: EDInput, *, n_k: int = 12) -> float:
    """Diagnostic ``M2^(k) = <<rho_k(r)^2>_uc>_BZ`` with ``rho_k = |h_k|^2 /
    <|h_k|^2>_uc`` and ``|h_k|^2 = rho_* exp(2 Re gamma(k, r))``."""

    spec, kw = _deformation(ed)
    ks = [(i / n_k, j / n_k) for i in range(n_k) for j in range(n_k)]
    return m2_k_batch(w_dict(ed), spec, kw.get("n_mesh", 48), ks)


def normalise(raw: dict, parent: EDInput, cfg: SwarmConfig, report: dict | None = None) -> EDInput:
    """Validate an agent's input against its parent and return the
    cluster-agnostic base config (broker-owned keys stripped). If ``report``
    is given, the admissibility measurement is stored in it."""

    ed = parse_agent_input(raw)
    if ed.energy_unit != parent.energy_unit:
        raise RequestRejected(f"energy_unit must be {parent.energy_unit!r}")
    p, rp = ed.ed_solver_params, parent.ed_solver_params
    if (p.n_basis, p.filling) != (rp.n_basis, rp.filling):
        raise RequestRejected("n_basis / filling are fixed by the parent")
    extra = {k: v for k, v in p.extra.items() if k not in CLUSTER_KEYS}
    ref_extra = {k: v for k, v in rp.extra.items() if k not in CLUSTER_KEYS}
    for k in sorted(set(extra) | set(ref_extra)):
        if k in cfg.agent_free_extra:
            continue
        if k not in extra:
            extra[k] = ref_extra[k]
        elif k not in ref_extra or extra[k] != ref_extra[k]:
            raise RequestRejected(
                f"ed_solver_params.extra[{k!r}] = {extra[k]!r} is fixed at "
                f"{ref_extra.get(k, '<absent>')!r} by the parent (not in agent_free_extra)")
    if ed.wavefunction.n_a != len(ed.wavefunction.a_n):
        raise RequestRejected("wavefunction.n_a != len(a_n)")
    if sum(abs(a.to_python()) ** 2 for a in ed.wavefunction.a_n) <= 0:
        raise RequestRejected("a_n is all zero")
    w = w_dict(ed)
    if cfg.regime.pin_static:
        wp = w_dict(parent)
        if set(w) != set(wp) or any(abs(w[g] - wp[g]) > 1e-12 for g in w):
            raise RequestRejected("the static density W_G is pinned to the parent; change only "
                                  "form_factor.deformation (start from `swarm template`)")
        a, ap = ([x.to_python() for x in e.wavefunction.a_n] for e in (ed, parent))
        if len(a) != len(ap) or any(abs(x - y) > 1e-12 for x, y in zip(a, ap)):
            raise RequestRejected("the LL weights a_n are pinned to the parent")
        if ed.form_factor.symmetry != parent.form_factor.symmetry:
            raise RequestRejected(f"form_factor.symmetry must stay {parent.form_factor.symmetry!r} (the parent's label)")
    check_density(w, symmetry=ed.form_factor.symmetry, positivity_tol=cfg.positivity_tol)
    block = ed.form_factor.deformation
    if block is not None:
        try:
            DeformationSpec.from_block(block.model_dump(mode="json"))
        except ValueError as exc:
            raise RequestRejected(f"deformation: {exc}") from exc
    base = ed.model_copy(update={
        "ed_solver_params": p.model_copy(update={"extra": extra}),
        "config_hash": PLACEHOLDER_HASH, "campaign_id": PLACEHOLDER_CAMPAIGN, "seed": 0, "proposer_x": None,
    })
    if cfg.gates.admissibility_min_ratio is not None and block is not None:
        if not _is_pure_ll0(base):
            raise RequestRejected("the admissibility gate is implemented for pure LL0 only")
        adm = admissibility(base, cfg)
        if report is not None:
            report["admissibility"] = adm
        if not (adm["min"] > 0 and adm["ratio"] >= cfg.gates.admissibility_min_ratio):
            raise RequestRejected(
                f"inadmissible envelope: min S00 / max S00 = {adm['ratio']:.3g} (min {adm['min']:.3g}) "
                f"< {cfg.gates.admissibility_min_ratio:g} at {adm['settings']}; near-singular envelopes do not count")
    if cfg.gates.boundary is not None and block is not None:
        spec, _ = _deformation(base)
        if spec is not None and not spec.is_zero():
            wp = w_dict(parent)
            bd = boundary_check(spec, m2_k(base), float(sum(abs(v) ** 2 for v in wp.values())), cfg.gates.boundary)
            if report is not None:
                report["boundary"] = bd["measured"]
            if bd["violated"]:
                raise RequestRejected("outside the search boundary: " + "; ".join(bd["violated"]))
    return base


def expand(base: EDInput, cluster: ClusterSpec, campaign_id: str) -> EDInput:
    """The concrete evaluation of ``base`` on one cluster, with its hash."""

    extra = {k: v for k, v in base.ed_solver_params.extra.items() if k not in CLUSTER_KEYS}
    if cluster.symcluster is not None:
        extra["symcluster"] = cluster.symcluster
    else:
        extra["nk1"], extra["nk2"] = cluster.nk1, cluster.nk2
    if cluster.ed_accuracy is not None:
        extra["ed_accuracy"] = cluster.ed_accuracy
    extra = tightened(extra, cluster.extra_overrides)
    if cluster.pes_na:
        # Levels only: the broker applies the counting gate (swarm.gates), so
        # the expected counts are not part of the evaluation's identity and can
        # be fixed without re-running ED.
        extra["pes"] = {"NA": cluster.pes_na, "holes": False, "threaded": True, "threshold_mode": "none"}
    ff = base.form_factor
    if ff.deformation is not None and cluster.deformation_overrides:
        cur = {k: getattr(ff.deformation, k) for k in cluster.deformation_overrides}
        ff = ff.model_copy(update={"deformation": ff.deformation.model_copy(
            update=tightened(cur, cluster.deformation_overrides))})
    ed = base.model_copy(update={
        "campaign_id": campaign_id,
        "lattice": base.lattice.model_copy(update={"n_k": cluster.sites}),
        "ed_solver_params": base.ed_solver_params.model_copy(update={"extra": extra}),
        "form_factor": ff,
    })
    ed = EDInput.model_validate(ed.model_dump(mode="json"))  # re-validate the copy
    return ed.model_copy(update={"config_hash": config_hash(ed)})
