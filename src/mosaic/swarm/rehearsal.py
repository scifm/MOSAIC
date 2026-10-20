"""Synthetic gap landscape for swarm rehearsals (no physics, no solver).

A rehearsal runs real agent sessions against the real broker and file
protocol, with this evaluator in place of the ED. The landscape is a smooth
function of the knobs the agents actually turn, relative to the reference,
with the same traps the real search has:

- a genuine optimum (first-star density weight up, first amplitude
  deformation negative) worth about +3 % on every cluster;
- a 4×6-only bump along the first phase direction, a finite-size artifact
  that the minimum ``R_gap`` over clusters should expose;
- loss of topology (``C = 0``, PES counting fails) for large deformations.

Gaps are reported like the real solver: ``completed`` with ``C = +1`` on the
rectangular meshes, ``failed_logical: mesh_unsuitable_for_chern`` with a
valid gap on the symmetric 27-site cluster.
"""

from __future__ import annotations

import math

from mosaic.ed.contract import EDInput, EDOutput

S1 = {(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)}
BASE_GAP = 0.0342


def _features(ed: EDInput) -> tuple[float, float, float, float]:
    s1 = [c.coef.re for c in ed.form_factor.W_G if tuple(c.G_int) in S1]
    w1 = sum(s1) / len(s1) if s1 else 0.0
    a = b = 0.0
    block = ed.form_factor.deformation
    if block is not None:
        a, b = block.alpha[0][0], block.beta[0][0]
    p = [abs(x.to_python()) ** 2 for x in ed.wavefunction.a_n]
    p2 = p[2] / sum(p) if len(p) > 2 and sum(p) > 0 else 0.0
    return w1, a, b, p2


def _F(w1: float, a: float, b: float, p2: float, *, small_cluster: bool) -> float:
    g = 0.032 * math.exp(-((w1 - 0.02) ** 2) / (2 * 0.015 ** 2)) * math.exp(-((a + 0.08) ** 2) / (2 * 0.05 ** 2))
    g -= 0.4 * p2 ** 2
    if small_cluster:
        g += 0.025 * math.exp(-((b - 0.06) ** 2) / (2 * 0.02 ** 2))
    return g


def mock_pes(na: int, *, below: int, gap: float, above: int = 4) -> dict:
    """A schema-valid ``ed_output.pes`` with one momentum sector: ``below``
    levels at 1.0 and ``above`` levels at ``1.0 + gap`` (``gap < 0`` overlaps
    them: no separation; ``above = 0``: an uninformative cut). Rehearsals and
    tests; the expected counts for it are ``[below]``."""

    levels = sorted([1.0] * below + [1.0 + gap] * above)
    n = len(levels)
    return {
        "NA": na, "holes": False, "N": 7, "Ns": 21, "mixture": "equal_incoherent",
        "parents": [{"momentum": [0, 0], "state": 1, "energy": 0.0}], "parent_sectors": [0],
        "momenta": [[0, 0]], "eigenvalues": [[1.0 / n] * n], "levels": [levels],
        "display_levels": [levels], "dimensions": [n], "ranks": [n], "trace": 1.0,
        "minimum_eigenvalue": 1.0 / n, "zero_tol": 1e-14, "level_floor": 1e-15, "threshold_mode": "none",
        "threshold_diagnostic": {"threshold": None, "gap": None, "counts": None, "total_count": None},
        "counting_diagnostic": None,
    }


def _laughlin_total(n_phi: int, na: int) -> int:
    from math import comb

    return n_phi * comb(n_phi - 2 * na, na) // (n_phi - 2 * na)


class SyntheticLandscape:
    def __init__(self, reference: EDInput):
        self.ref = _features(reference)

    def __call__(self, ed: EDInput) -> EDOutput:
        extra = ed.ed_solver_params.extra
        sym = "symcluster" in extra
        small = extra.get("nk1") == 4 and extra.get("nk2") == 6
        w1, a, b, p2 = _features(ed)
        w1_ref, a_ref, b_ref, p2_ref = self.ref
        dF = _F(w1 - w1_ref, a, b, p2, small_cluster=small) - _F(0.0, a_ref, b_ref, p2_ref, small_cluster=small)
        # Mild size dependence of the absolute gap, as on the real clusters.
        gap = BASE_GAP * (1 - 0.0005 * (ed.lattice.n_k - 24)) * (1 + dF)
        lost = abs(a) > 0.3 or abs(b) > 0.3
        pes = extra.get("pes")
        return EDOutput(
            config_hash=ed.config_hash,
            status="failed_logical" if (sym or lost) else "completed",
            failure_reason="mesh_unsuitable_for_chern" if sym else ("chern_mismatch" if lost else None),
            n_k=ed.lattice.n_k, chern_solver=None if sym else (0 if lost else 1),
            gap_top_indirect_solver=gap, gs_manifold_splitting=1e-3 * gap, compute_seconds=0.0,
            pes=mock_pes(pes["NA"], below=_laughlin_total(ed.lattice.n_k, pes["NA"]), gap=-1.0 if lost else 15.0)
            if pes else None,
            solver_version="synthetic-rehearsal@v1", energy_unit=ed.energy_unit,
        )
