"""Laughlin phase gates and claims.

A gate verdict is computed per evaluation from its ``ed_output.json``:

- numerical: a completed solve (or, where the cluster skips Chern, a
  ``failed_logical`` whose reason only says the Chern step could not run),
  ``Δ > 0``, and ground-manifold splitting / Δ below ``split_max``;
- Chern: skipped, ``|C| = 1``, or equal to the parent's on the same cluster;
- PES: the solver returns the entanglement levels; ``counting_gap`` (the
  solver's ``pes_counting_gap`` rule, re-implemented here so the expected
  counts are not part of an evaluation's identity) checks that the expected
  momentum-resolved counts separate at one common threshold. The
  entanglement gap there grades PASS (≥ ``pes_gap_pass``) vs AMBIGUOUS; no
  separation at the expected count is FAIL.

The evaluation verdict is FAIL if any gate fails, else AMBIGUOUS if any is
ambiguous, else PASS.
"""

from __future__ import annotations

from typing import Optional

from mosaic.swarm.config import ClaimSpec, ClusterSpec, GateSpec

PASS, AMBIGUOUS, FAIL = "PASS", "AMBIGUOUS", "FAIL"
_RANK = {PASS: 0, AMBIGUOUS: 1, FAIL: 2}


def _sorted_levels(levels: list[list]) -> list[list[float]]:
    # JSON null = a zero RDM eigenvalue = infinite entanglement energy.
    return [sorted(float("inf") if x is None else x for x in sector) for sector in levels]


def counting_gap(levels: list[list], counts: list[int]) -> dict:
    """``MoireSolver.pes_counting_gap`` with ``gap_min = 0``: the gap between the
    highest level inside the expected counts and the lowest level outside,
    over all sectors, and whether one threshold reproduces every count."""

    lv = _sorted_levels(levels)
    if len(lv) != len(counts):
        raise ValueError(f"PES has {len(lv)} sectors, expected counts {len(counts)}")
    below = [x for s, n in zip(lv, counts) for x in s[:n]]
    above = [x for s, n in zip(lv, counts) for x in s[n:]]
    if any(n > len(s) for s, n in zip(lv, counts)):
        return {"gap": None, "matched": False, "informative": True}
    if not below or not above:
        return {"gap": None, "matched": False, "informative": False}
    low, high = max(below), min(above)
    if low == float("inf"):
        return {"gap": None, "matched": False, "informative": True}
    gap = high - low
    thr = (low + high) / 2 if high != float("inf") else low + 1.0
    matched = gap >= 0 and [sum(1 for x in s if x < thr) for s in lv] == list(counts)
    # Everything outside the counts is an exact zero eigenvalue: infinite separation.
    infinite = high == float("inf")
    return {"gap": None if infinite else gap, "gap_infinite": infinite, "matched": matched, "informative": True}


def reference_counts(levels: list[list], total: int, gap_min: float) -> dict:
    """Momentum-resolved counts from a reference state's PES: the ``total``
    lowest levels, which must sit below an entanglement gap ≥ ``gap_min``."""

    lv = _sorted_levels(levels)
    flat = sorted(x for s in lv for x in s)
    if len(flat) <= total or flat[total - 1] == float("inf"):
        raise ValueError(f"reference PES has too few finite levels for {total}")
    gap = flat[total] - flat[total - 1]
    if not gap >= gap_min:
        raise ValueError(f"reference PES gap at count {total} is {gap:.3g} < {gap_min}: not a clear Laughlin reference")
    thr = (flat[total - 1] + flat[total]) / 2
    return {"counts": [sum(1 for x in s if x < thr) for s in lv], "total": total, "gap": gap}


def worst(*verdicts: str) -> str:
    return max(verdicts, key=_RANK.__getitem__) if verdicts else PASS


def evaluate(out: dict, cluster: ClusterSpec, gates: GateSpec, parent_chern: Optional[int] = None,
             expected_counts: Optional[list[int]] = None) -> dict:
    """Gate verdict for one evaluation. ``out`` is the parsed ed_output.json;
    ``expected_counts`` the cluster's momentum-resolved Laughlin counts."""

    reasons, verdicts = [], []
    gap = out.get("gap_top_indirect_solver")
    split = out.get("gs_manifold_splitting")
    status, reason = out.get("status"), out.get("failure_reason")

    completed = status == "completed" or (
        cluster.chern == "skip" and status == "failed_logical" and reason in gates.chern_skip_reasons)
    if not completed:
        verdicts.append(FAIL)
        reasons.append(f"solve {status}" + (f" ({reason})" if reason else ""))
    if gap is None or gap <= 0:
        verdicts.append(FAIL)
        reasons.append(f"gap {gap}")
    elif split is not None and split / gap >= gates.split_max:
        verdicts.append(FAIL)
        reasons.append(f"ground manifold not clean: splitting/Δ = {split / gap:.3g}")

    chern = out.get("chern_solver")
    if cluster.chern == "abs1" and chern not in (-1, 1):
        verdicts.append(FAIL)
        reasons.append(f"Chern {chern}")
    elif cluster.chern == "match_parent":
        if parent_chern is None:
            verdicts.append(FAIL)
            reasons.append("parent Chern unknown on this cluster")
        elif chern != parent_chern:
            verdicts.append(FAIL)
            reasons.append(f"Chern {chern} != parent's {parent_chern}")

    pes = None
    if cluster.pes_na:
        p = out.get("pes")
        if not p or not p.get("levels") or expected_counts is None:
            verdicts.append(FAIL)
            reasons.append("PES missing" if expected_counts is not None else "expected PES counts missing")
            cd = None
        else:
            cd = counting_gap(p["levels"], expected_counts)
            egap = cd["gap"]
            pes = {"NA": p.get("NA"), "matched": cd.get("matched"), "informative": cd.get("informative"),
                   "entanglement_gap": egap}
            if not cd.get("informative"):
                verdicts.append(AMBIGUOUS)
                reasons.append("PES counting not informative")
            elif not cd.get("matched"):
                verdicts.append(FAIL)
                reasons.append("PES: no separation at the expected Laughlin count")
            elif not cd.get("gap_infinite") and (egap is None or egap < gates.pes_gap_pass):
                verdicts.append(AMBIGUOUS)
                reasons.append(f"PES entanglement gap {egap} < {gates.pes_gap_pass}")
    return {"verdict": worst(*verdicts), "reasons": reasons, "gap": gap, "splitting": split,
            "chern": chern, "pes": pes}


def claim(rows: dict[str, dict], claims: list[ClaimSpec]) -> Optional[str]:
    """The strongest claim a request has earned. ``rows`` maps cluster name to
    its evaluated row (with ``verdict`` and ``R_gap``)."""

    for c in claims:
        need = set(c.all_clusters) | set(c.min_R_gap)
        if not all(n in rows and rows[n].get("R_gap") is not None for n in need):
            continue
        if any(rows[n]["verdict"] != PASS or rows[n]["R_gap"] <= 1 for n in c.all_clusters):
            continue
        if all(rows[n]["R_gap"] >= v for n, v in c.min_R_gap.items()):
            return c.name
    return None
