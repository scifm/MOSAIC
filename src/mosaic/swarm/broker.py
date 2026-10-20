"""The ED broker: the only process that submits to
Slurm and the only writer of each arm's store.

One ``tick`` per arm, every step idempotent and keyed on content hashes, so
the broker can be killed at any point and restarted without losing or
re-running work:

1. parents     — register every parent on every cluster; gate them and check
   their gaps against values measured before the swarm (halt on failure);
2. accept      — validate new requests against their parent (pinning,
   admissibility), expand onto the first stage's clusters, register, charge
   quota in evaluations (``accepted.json``);
3. reconcile   — ingest finished outputs; requeue claims whose job died;
4. enqueue     — put PROPOSED / retryable evaluations into the tier pools;
5. jobs        — keep a pool job alive per tier while it has unclaimed work;
6. results     — per-request gate verdicts, R_gap per cluster, promotion up
   the stage ladder, claims (``result.json``, ``promotions.json``);
7. leaderboard — per parent, from the store only, plus the other-phases and
   controls tables.

Agents never touch the store; they read ``result.json``, ``parents.json`` and
the leaderboards.
"""

from __future__ import annotations

import json
import os
import shutil
import socket
import time
from pathlib import Path
from typing import Optional

from mosaic.ed.contract import EDInput, EDOutput
from mosaic.store.state import RunState
from mosaic.store.store import ResultStore
from mosaic.swarm import gates as G
from mosaic.swarm.config import SwarmConfig, load_swarm
from mosaic.swarm.files import (
    atomic_write_json,
    atomic_write_text,
    parse_iso,
    read_json,
    utc_iso,
    utc_now,
    utc_stamp,
    visible_entries,
)
from mosaic.swarm.layout import ArmLayout
from mosaic.swarm.parents import build_parents, m2_static
from mosaic.swarm.pool import ALIVE_STATES, MockPool, PoolBackend, SlurmPool, render_pool_script
from mosaic.swarm.validate import RequestRejected, expand, m2_k, normalise
from mosaic.util.logging import get_logger

LOG = get_logger("swarm.broker")

PENDING, DONE, FAILED, REJECTED = "pending", "done", "failed", "rejected"
TERMINAL = {RunState.COMPLETED, RunState.FAILED_LOGICAL, RunState.FAILED_TRANSIENT_TERMINAL}
# A claim directory without a job file is a lane between ``mkdir`` and
# ``echo``; only after this long is it treated as abandoned.
ORPHAN_CLAIM_SECONDS = 600


class BrokerHalt(RuntimeError):
    """A condition no retry can fix (parent drift or gate failure, solver
    version change). The broker stops and writes ``HALT``; a human decides."""


def pes_expected_total(n_phi: int, na: int) -> int:
    """Torus quasihole count of the ν = 1/3 Laughlin state for a particle cut."""

    from math import comb

    return n_phi * comb(n_phi - 2 * na, na) // (n_phi - 2 * na)


def load_pes_counts(cfg: SwarmConfig) -> dict:
    """``"<cluster>:<N_A>" -> {momenta, counts, total}``, checked against the
    closed-form totals. ν = 1/3 so N_phi = number of sites."""

    if not cfg.gates.pes_expected_counts:
        return {}
    data = json.loads(cfg.path(cfg.gates.pes_expected_counts).read_text())
    for name, c in cfg.clusters.items():
        if not c.pes_na or c.pes_reference:
            continue
        key = f"{name}:{c.pes_na}"
        if key not in data:
            raise SystemExit(f"{cfg.gates.pes_expected_counts} has no entry {key!r} (run `swarm pes-cases`)")
        want = pes_expected_total(c.sites, c.pes_na)
        if sum(data[key]["counts"]) != want or data[key].get("total", want) != want:
            raise SystemExit(f"{key}: expected PES counts total {sum(data[key]['counts'])}, closed form says {want}")
    return data


class ArmBroker:
    def __init__(self, cfg: SwarmConfig, arm: str, backend: PoolBackend,
                 parents: dict[str, EDInput], pes_counts: dict):
        self.cfg, self.arm, self.backend = cfg, arm, backend
        self.L = ArmLayout(cfg, arm)
        self.L.ensure()
        self.store = ResultStore(self.L.store_db, self.L.runs_dir)
        self.campaign = cfg.campaign_id(arm)
        self.parents = parents
        # cluster -> momentum-resolved Laughlin counts: from the (1,3) rule file,
        # or derived at runtime from the reference parent's PES (pes_reference).
        self.cluster_counts = {n: pes_counts[f"{n}:{c.pes_na}"]["counts"]
                               for n, c in cfg.clusters.items() if c.pes_na and not c.pes_reference}
        self.derived_counts: dict[str, dict] = {}
        self.parent_rows: dict[str, dict[str, dict]] = {}
        if isinstance(backend, MockPool):
            for t in cfg.broker.tiers:
                backend.pool_dirs.setdefault(f"{arm}/{t}", self.L.pool_dir(t))

    def close(self) -> None:
        self.store.close()

    # ------------------------------------------------------------------
    # helpers
    # ------------------------------------------------------------------

    def _expand(self, base: EDInput, cluster: str) -> EDInput:
        return expand(base, self.cfg.clusters[cluster], self.campaign)

    def _counts(self, cluster: str) -> Optional[list[int]]:
        """Expected counts, or None while a reference-counted cluster's
        reference is not yet evaluated."""

        c = self.cfg.clusters[cluster]
        if not c.pes_na:
            return []
        return self.cluster_counts.get(cluster)

    def _register(self, ed: EDInput, cluster: str, proposer: str, git_sha: Optional[str] = None) -> bool:
        """Register; True if this proposer is the one that created the run."""

        rec = self.store.get(ed.config_hash)
        if rec is None:
            self.store.register(ed, proposer=proposer, seed=0, git_sha=git_sha)
            atomic_write_json(self.store.run_dir(ed.config_hash) / "swarm_cluster.json", {"cluster": cluster})
            return True
        if not (self.store.run_dir(ed.config_hash) / "swarm_cluster.json").exists():
            atomic_write_json(self.store.run_dir(ed.config_hash) / "swarm_cluster.json", {"cluster": cluster})
        return rec.proposer == proposer

    # Pool order: lanes take entries in name
    # order, so the name starts with a priority. Parents first; promoted runs
    # by their request's current R_gap_min, highest first; first-stage runs
    # after promotions, first-come first-served.
    PRIORITY_PARENT, PRIORITY_FIRST_STAGE, PRIORITY_WITHDRAWN = 0, 900000, 990000

    def _priority_for(self, r_gap_min: Optional[float], parent: Optional[str] = None) -> int:
        """Smaller runs first. With a parent, rank relative to that parent's best
        so far, (R - 1)/(R_best - 1), so one parent's large ratios never starve
        another parent's candidates."""

        if r_gap_min is None:
            return self.PRIORITY_FIRST_STAGE - 1
        best = getattr(self, "_parent_best", {}).get(parent) if parent else None
        if best is not None and best > 1:
            score = min(1.0, max(0.0, (r_gap_min - 1) / (best - 1)))
            return 1 + int(round((1 - score) * 100000))
        return max(1, min(899999, int(round((10.0 - r_gap_min) * 10000))))

    def _set_priority(self, h: str, priority: int) -> None:
        path = self.store.run_dir(h) / "swarm_cluster.json"
        meta = read_json(path) or {}
        if meta.get("priority") != priority:
            atomic_write_json(path, {**meta, "priority": priority})

    def _priority(self, h: str) -> int:
        return int((read_json(self.store.run_dir(h) / "swarm_cluster.json") or {}).get(
            "priority", self.PRIORITY_FIRST_STAGE))

    def _reprioritize(self) -> None:
        """Rename unclaimed pool entries whose priority changed. Claims live in
        the run directory, so a rename never loses or duplicates work; a lane
        that listed the old name just skips it."""

        for t in self.cfg.broker.tiers:
            for p in visible_entries(self.L.pool_dir(t)):
                parts = p.name.split("_")
                h = parts[-1]
                if (p / ".claimed").exists() or (p / "ed_output.json").exists():
                    continue
                prio = f"{self._priority(h):07d}"
                if len(parts) == 3 and parts[0] == prio:
                    continue
                stamp = parts[-2]
                try:
                    os.replace(p, p.parent / f"{prio}_{stamp}_{h}")
                except FileNotFoundError:
                    pass

    def _cluster_of(self, h: str) -> str:
        c = (read_json(self.store.run_dir(h) / "swarm_cluster.json") or {}).get("cluster")
        if c not in self.cfg.clusters:
            raise BrokerHalt(f"run {h[:12]} has cluster {c!r}, not in the config (config changed mid-campaign?)")
        return c

    def _pool_links(self) -> dict[str, Path]:
        links = {}
        for t in self.cfg.broker.tiers:
            for p in visible_entries(self.L.pool_dir(t)):
                links[p.name.rsplit("_", 1)[-1]] = p
        return links

    def _output(self, h: str) -> Optional[dict]:
        res = self.store.get_result(h)
        if res is None:
            return None
        try:
            return json.loads(Path(res.ed_output_path).read_text())
        except FileNotFoundError:
            return None

    def _row(self, h: str, cluster: str, parent: Optional[str]) -> Optional[dict]:
        """Gate verdict and R_gap of one evaluation; None while not terminal."""

        rec = self.store.get(h)
        if rec.state not in TERMINAL:
            return None
        if rec.state == RunState.FAILED_TRANSIENT_TERMINAL:
            return {"hash": h, "verdict": G.FAIL, "reasons": ["transient failures exhausted"], "gap": None,
                    "R_gap": None}
        pchern = None
        if parent is not None:
            prow = self.parent_rows.get(parent, {}).get(cluster)
            if prow is None:
                return None  # wait for the parent on this cluster
            pchern = prow["chern"]
        counts = self._counts(cluster)
        if counts is None:
            return None  # wait for the reference PES on this cluster
        row = G.evaluate(self._output(h) or {}, self.cfg.clusters[cluster], self.cfg.gates, pchern, counts or None)
        row["hash"] = h
        row["R_gap"] = None
        if parent is not None and row["gap"] is not None:
            row["R_gap"] = row["gap"] / self.parent_rows[parent][cluster]["gap"]
        lll = self.cfg.lll_parent
        if lll and row["gap"] is not None and self.parent_rows.get(lll, {}).get(cluster):
            row["delta_lll"] = self.parent_rows[lll][cluster]["gap"]
        return row

    # ------------------------------------------------------------------
    # 1. parents
    # ------------------------------------------------------------------

    def parent_hashes(self) -> dict[str, dict[str, str]]:
        out = {}
        for name, base in self.parents.items():
            out[name] = {}
            for cluster in self.cfg.all_clusters:
                ed = self._expand(base, cluster)
                self._register(ed, cluster, f"_parent/{name}")
                self._set_priority(ed.config_hash, self.PRIORITY_PARENT)
                out[name][cluster] = ed.config_hash
        return out

    def _derive_reference_counts(self, hashes: dict[str, dict[str, str]]) -> None:
        for cluster, c in self.cfg.clusters.items():
            if not (c.pes_na and c.pes_reference) or cluster in self.cluster_counts:
                continue
            h = hashes[c.pes_reference][cluster]
            if self.store.get(h).state not in TERMINAL:
                continue
            out = self._output(h) or {}
            total = pes_expected_total(c.sites, c.pes_na)
            try:
                ref = G.reference_counts((out.get("pes") or {}).get("levels") or [], total, self.cfg.gates.pes_gap_pass)
            except ValueError as exc:
                raise BrokerHalt(f"PES reference {c.pes_reference} on {cluster}: {exc}") from exc
            self.cluster_counts[cluster] = ref["counts"]
            self.derived_counts[cluster] = {**ref, "reference": c.pes_reference, "hash": h,
                                            "momenta": (out.get("pes") or {}).get("momenta")}
            LOG.info("PES counts for %s from %s: total %d, entanglement gap %.2f",
                     cluster, c.pes_reference, total, ref["gap"])
        if self.derived_counts:
            atomic_write_json(self.L.root / "pes_counts_derived.json", self.derived_counts)

    def _parents(self) -> None:
        table = {}
        all_hashes = self.parent_hashes()
        self._derive_reference_counts(all_hashes)
        for name, hashes in all_hashes.items():
            spec = self.cfg.parents[name]
            table[name] = {"role": spec.role, "M2": m2_static(self.parents[name]), "clusters": {}}
            self.parent_rows.setdefault(name, {})
            for cluster, h in hashes.items():
                rec = self.store.get(h)
                entry = {"hash": h, "state": rec.state.value}
                if rec.state in TERMINAL:
                    # A parent's own Chern gate is |C| = 1; requests are matched to it.
                    c = self.cfg.clusters[cluster]
                    c = c.model_copy(update={"chern": "abs1"}) if c.chern == "match_parent" else c
                    if rec.state == RunState.FAILED_TRANSIENT_TERMINAL:
                        raise BrokerHalt(f"parent {name} on {cluster}: transient failures exhausted")
                    counts = self._counts(cluster)
                    if counts is None:
                        table[name]["clusters"][cluster] = {**entry, "state": "waiting for the PES reference"}
                        continue
                    row = G.evaluate(self._output(h) or {}, c, self.cfg.gates, None, counts or None)
                    if row["verdict"] == G.FAIL and spec.role == "parent":
                        raise BrokerHalt(f"parent {name} fails the Laughlin gate on {cluster}: {row['reasons']}")
                    exp = spec.expected_gap.get(cluster)
                    if exp is not None and abs(row["gap"] / exp - 1) > spec.rtol(cluster):
                        raise BrokerHalt(f"parent {name} gap on {cluster} is {row['gap']:.9g}, expected {exp:.9g} "
                                         f"(rtol {spec.rtol(cluster)}); solver or parent changed")
                    entry.update(gap=row["gap"], chern=row["chern"], verdict=row["verdict"],
                                 reasons=row["reasons"], pes=row["pes"], splitting=row["splitting"])
                    self.parent_rows[name][cluster] = row
                table[name]["clusters"][cluster] = entry
        atomic_write_json(self.L.root / "parents.json", table)

    # ------------------------------------------------------------------
    # 2. accept
    # ------------------------------------------------------------------

    def _accepted(self, agent: str) -> list[tuple[Path, dict]]:
        out = []
        for d in visible_entries(self.L.inbox(agent)):
            acc = read_json(d / "accepted.json")
            if acc is not None:
                out.append((d, acc))
        return out

    def _reject(self, d: Path, reason: str) -> None:
        LOG.info("reject %s: %s", d.name, reason)
        atomic_write_json(d / "result.json", {"status": REJECTED, "reason": reason, "updated_at": utc_iso()})

    def _accept_requests(self) -> None:
        """Accept new requests round-robin across agents, at most
        ``broker.max_accepts_per_tick`` per tick, so a large backlog never
        starves queueing and scoring (one 18-agent burst once held a
        tick in acceptance for >10 min), and no agent's batch starves the rest."""

        q = self.cfg.quotas
        past_deadline = self.cfg.deadline_utc is not None and utc_now() >= parse_iso(self.cfg.deadline_utc)
        first = self.cfg.stages[0]
        state, queues = {}, {}
        for agent in self.L.agents:
            accepted = self._accepted(agent)
            state[agent] = {
                "charged": sum(a.get("charged_evaluations", 0) for _, a in accepted),
                "in_flight": sum(1 for d, _ in accepted
                                 if not (read_json(d / "result.json") or {}).get("first_stage_done")),
            }
            queues[agent] = [d for d in visible_entries(self.L.inbox(agent))
                             if not (d / "accepted.json").exists() and not (d / "result.json").exists()]
        budget = self.cfg.broker.max_accepts_per_tick
        while budget > 0 and any(queues.values()):
            for agent in self.L.agents:
                if budget <= 0 or not queues[agent]:
                    continue
                d = queues[agent][0]
                outcome = self._accept_one(agent, d, state[agent], first, q, past_deadline)
                if outcome == "wait":
                    queues[agent] = []  # keep order: later requests wait behind this one
                    continue
                queues[agent].pop(0)
                if outcome == "accepted":
                    budget -= 1

    def _accept_one(self, agent: str, d: Path, st: dict, first, q, past_deadline: bool) -> str:
        req = read_json(d / "request.json")
        raw = read_json(d / "ed_input.json")
        if req is None or raw is None:
            self._reject(d, "request directory lacks request.json or ed_input.json")
            return "rejected"
        if req.get("agent") != agent:
            self._reject(d, f"request.json says agent {req.get('agent')!r}, inbox belongs to {agent!r}")
            return "rejected"
        if past_deadline:
            self._reject(d, "deadline passed; no new requests")
            return "rejected"
        parent = req.get("parent") or (self.cfg.request_parents[0] if len(self.cfg.request_parents) == 1 else None)
        if parent not in self.cfg.request_parents:
            self._reject(d, f"name a parent: one of {self.cfg.request_parents}")
            return "rejected"
        if st["in_flight"] >= q.max_in_flight_per_agent:
            return "wait"
        kind = req.get("kind", "search")
        report: dict = {}
        try:
            cfg = self.cfg if kind != "control" else self.cfg.model_copy(
                update={"regime": self.cfg.regime.model_copy(update={"pin_static": False})})
            base = normalise(raw, self.parents[parent], cfg, report)
        except RequestRejected as exc:
            self._reject(d, str(exc))
            return "rejected"
        # A control may name the clusters it runs on (mechanism checks belong on
        # the cluster where a claim would be made); it is
        # never promoted, and every evaluation it adds is charged.
        stage_name, clusters = first.name, list(first.clusters)
        if kind == "control" and req.get("clusters"):
            unknown = [c for c in req["clusters"] if c not in self.cfg.all_clusters]
            if unknown:
                self._reject(d, f"unknown clusters {unknown}; one of {self.cfg.all_clusters}")
                return "rejected"
            stage_name, clusters = "control", list(dict.fromkeys(req["clusters"]))
        if st["charged"] + len(clusters) > q.evaluations_per_agent:
            self._reject(d, f"quota exhausted ({st['charged']}/{q.evaluations_per_agent} evaluations charged)")
            return "rejected"
        proposer = f"{agent}/{d.name}"
        hashes, new = {}, 0
        for cluster in clusters:
            ed = self._expand(base, cluster)
            new += int(self._register(ed, cluster, proposer, req.get("git_sha")))
            hashes[cluster] = ed.config_hash
        atomic_write_text(d / "base_ed_input.json", base.model_dump_json(indent=1))
        diag = {"M2_k": m2_k(base), "M2_parent": m2_static(self.parents[parent]), **report}
        atomic_write_json(d / "accepted.json", {
            "req_id": d.name, "agent": agent, "family": req.get("family"), "parent": parent, "kind": kind,
            "stages": {stage_name: hashes}, "charged_evaluations": new, "diagnostics": diag,
            "accepted_at": utc_iso()})
        atomic_write_json(d / "result.json", {"status": PENDING, "first_stage_done": False, "updated_at": utc_iso()})
        st["charged"] += new
        st["in_flight"] += 1
        self._heartbeat()
        LOG.info("accept %s/%s parent=%s kind=%s family=%s charged=%d",
                 agent, d.name, parent, kind, req.get("family"), new)
        return "accepted"

    # ------------------------------------------------------------------
    # 3. reconcile + ingest
    # ------------------------------------------------------------------

    def _ingest(self, h: str, path: Path, links: dict[str, Path]) -> None:
        try:
            out = EDOutput.model_validate_json(path.read_text())
        except Exception as exc:  # partial write from a killed job
            self._transient(h, f"unreadable ed_output.json: {exc}")
            return
        if out.config_hash != h:
            raise BrokerHalt(f"{path} carries hash {out.config_hash}, expected {h}")
        if not out.solver_version.startswith(self.cfg.broker.solver_version_prefix):
            raise BrokerHalt(f"{h[:12]} ran solver {out.solver_version!r}, campaign is pinned to "
                             f"{self.cfg.broker.solver_version_prefix!r}")
        if out.status == "failed_transient":
            self._transient(h, out.failure_reason or "failed_transient")
            return
        self.store.ingest_result(out, chern_authoritative=out.chern_solver,
                                 gap_authoritative=out.gap_top_indirect_solver, ed_output_path=path)
        to = RunState.COMPLETED if out.status == "completed" else RunState.FAILED_LOGICAL
        self.store.transition(h, to, payload={"failure_reason": out.failure_reason})
        if h in links:
            links[h].unlink(missing_ok=True)

    def _transient(self, h: str, reason: str) -> None:
        d = self.store.run_dir(h)
        out = d / "ed_output.json"
        if out.exists():
            out.replace(d / f"ed_output.transient-{utc_stamp()}.json")
        shutil.rmtree(d / ".claimed", ignore_errors=True)
        self.store.transition(h, RunState.FAILED_TRANSIENT, payload={"reason": reason})
        LOG.warning("transient %s: %s", h[:12], reason)

    def _reconcile(self) -> None:
        links = self._pool_links()
        recs = self.store.list_by_state(RunState.SUBMITTED, RunState.RUNNING, campaign_id=self.campaign)
        claims = {}
        for rec in recs:
            d = self.store.run_dir(rec.config_hash)
            if (d / "ed_output.json").exists():
                self._ingest(rec.config_hash, d / "ed_output.json", links)
            elif (d / ".claimed").is_dir():
                claims[rec.config_hash] = (rec, d / ".claimed")
        jobs = {(c / "job").read_text().strip() for _, c in claims.values() if (c / "job").exists()}
        states = self.backend.states(sorted(jobs))
        for h, (rec, claim) in claims.items():
            if (claim.parent / "ed_output.json").exists():  # landed since the scan
                self._ingest(h, claim.parent / "ed_output.json", links)
                continue
            job = (claim / "job").read_text().strip() if (claim / "job").exists() else None
            if (claim / "rc").exists():
                self._transient(h, f"lane finished (rc {(claim / 'rc').read_text().strip()}) without output")
            elif job is not None and states.get(job) not in ALIVE_STATES:
                self._transient(h, f"job {job} is {states.get(job)} and left no output")
            elif job is None and time.time() - claim.stat().st_mtime > ORPHAN_CLAIM_SECONDS:
                self._transient(h, "claim without a job id for > 10 min")
            elif rec.state == RunState.SUBMITTED:
                self.store.transition(h, RunState.RUNNING, payload={"job": job})

    # ------------------------------------------------------------------
    # 4. enqueue
    # ------------------------------------------------------------------

    def _enqueue(self) -> None:
        links = self._pool_links()
        for rec in self.store.list_by_state(RunState.FAILED_TRANSIENT, campaign_id=self.campaign):
            if self.store.retry_count(rec.config_hash) > self.cfg.broker.max_retries:
                self.store.transition(rec.config_hash, RunState.FAILED_TRANSIENT_TERMINAL)
                if rec.config_hash in links:
                    links[rec.config_hash].unlink(missing_ok=True)
        for rec in self.store.list_by_state(RunState.PROPOSED, RunState.FAILED_TRANSIENT, campaign_id=self.campaign):
            h = rec.config_hash
            if h not in links:
                tier = self.cfg.clusters[self._cluster_of(h)].tier
                link = self.L.pool_dir(tier) / f"{self._priority(h):07d}_{utc_stamp()}_{h}"
                tmp = link.parent / f".tmp-{link.name}"
                tmp.symlink_to(self.store.run_dir(h))
                os.replace(tmp, link)
            self.store.transition(h, RunState.SUBMITTED, payload={"pool": True})

    # ------------------------------------------------------------------
    # 5. jobs
    # ------------------------------------------------------------------

    def _jobs(self) -> None:
        for tier_name, tier in self.cfg.broker.tiers.items():
            pool = self.L.pool_dir(tier_name)
            unclaimed = sum(1 for p in visible_entries(pool)
                            if not (p / "ed_output.json").exists() and not (p / ".claimed").exists())
            reg = self.L.jobs_dir(tier_name)
            live = {p.stem: read_json(p) for p in visible_entries(reg, ".json") if not read_json(p).get("ended")}
            states = self.backend.states(sorted(live))
            for job, st in states.items():
                if st not in ALIVE_STATES:
                    atomic_write_json(reg / f"{job}.json", {**live[job], "ended": st, "ended_at": utc_iso()})
            alive = [j for j, st in states.items() if st in ALIVE_STATES]
            queued = [j for j in alive if states[j] == "PENDING"]
            if unclaimed and len(alive) < tier.max_jobs and not queued:
                script = reg / f"pool_{utc_stamp()}.sbatch"
                atomic_write_text(script, render_pool_script(self.cfg, tier_name, tier, pool, reg))
                job = self.backend.submit(f"{self.arm}/{tier_name}", script)
                atomic_write_json(reg / f"{job}.json", {"job": job, "script": str(script), "submitted_at": utc_iso(),
                                                        "unclaimed_at_submit": unclaimed})
                LOG.info("pool job %s on %s (%d unclaimed)", job, tier_name, unclaimed)

    # ------------------------------------------------------------------
    # 6. results: gates, R_gap, promotion, claims
    # ------------------------------------------------------------------

    def _results(self) -> None:
        # A deduplicated run belongs to every request that uses it: it keeps the
        # best priority any active request gives it; runs only withdrawn
        # requests want go to the back.
        prios: dict[str, int] = {}
        # Request id -> (R_gap_min, parent, claim), so a control that builds on a
        # candidate can inherit the candidate's queue priority.
        self._r_index = {}
        self._parent_best = {}
        for agent in self.L.agents:
            for d, acc in self._accepted(agent):
                res = read_json(d / "result.json") or {}
                r = res.get("R_gap_min")
                self._r_index[d.name] = (r, acc.get("parent"), res.get("claim"))
                # A failed candidate's ratio is not attainable: counting it would
                # push the parent's real best down the queue.
                if (r is not None and acc.get("kind", "search") == "search"
                        and res.get("verdict") != "FAIL"
                        and not (d / "withdrawn.json").exists()):
                    self._parent_best[acc["parent"]] = max(self._parent_best.get(acc["parent"], 1.0), r)
        for agent in self.L.agents:
            for d, acc in self._accepted(agent):
                old = read_json(d / "result.json") or {}
                new = self._evaluate_request(d, acc, prios)
                old_cmp = {k: v for k, v in old.items() if k != "updated_at"}
                if old_cmp != new:
                    atomic_write_json(d / "result.json", {**new, "updated_at": utc_iso()})
        for h, p in prios.items():
            if self.store.get(h).state not in TERMINAL:
                self._set_priority(h, p)

    def _evaluate_request(self, d: Path, acc: dict, prios: Optional[dict] = None) -> dict:
        parent, kind = acc["parent"], acc.get("kind", "search")
        withdrawn = (d / "withdrawn.json").exists()
        prios = {} if prios is None else prios
        promotions = read_json(d / "promotions.json") or {}
        stage_hashes = {**acc["stages"], **promotions}
        rows: dict[str, dict] = {}
        reached, pending = None, False
        if "control" in acc["stages"]:
            # Controls on named clusters: one flat stage, no promotion. A control
            # that builds on candidates runs at the best candidate's priority; on
            # a claimed candidate, right after the parents: its parent's best keeps
            # rising, so a relative rank would leave it behind every search run.
            refs = [self._r_index.get(r) for r in (read_json(d / "request.json") or {}).get("builds_on", [])]
            refs = [x for x in refs if x is not None and x[0] is not None]
            if refs and not withdrawn:
                best_ref = min(1 if claim else self._priority_for(rv, par) for rv, par, claim in refs)
                for h in acc["stages"]["control"].values():
                    prios[h] = min(prios.get(h, self.PRIORITY_WITHDRAWN), best_ref)
            for cluster, h in acc["stages"]["control"].items():
                row = self._row(h, cluster, parent)
                if row is None:
                    pending = True
                    row = {"hash": h, "verdict": None, "R_gap": None, "state": self.store.get(h).state.value}
                rows[cluster] = row
            reached = "control"
        for i, st in enumerate(self.cfg.stages if "control" not in acc["stages"] else []):
            hashes = stage_hashes.get(st.name)
            if hashes is None:
                if pending or kind != "search" or i == 0 or withdrawn:
                    break
                on = [rows.get(c) for c in st.promote_on] if st.promote_on else list(rows.values())
                passing = [r for r in on if r is not None and r.get("R_gap") is not None]
                if (passing and len(passing) == len(on)
                        and all(r["verdict"] in st.promote_verdicts for r in rows.values())
                        and min(r["R_gap"] for r in passing) >= st.promote_min_R_gap):
                    hashes = self._promote(d, acc, st.name, st.clusters, promotions)
                else:
                    break
            if i > 0:
                known = [r["R_gap"] for r in rows.values() if r.get("R_gap") is not None]
                prio = (self.PRIORITY_WITHDRAWN if withdrawn
                        else self._priority_for(min(known) if known else None, parent))
                for h in hashes.values():
                    prios[h] = min(prios.get(h, self.PRIORITY_WITHDRAWN), prio)
            for cluster, h in hashes.items():
                row = self._row(h, cluster, parent)
                if row is None:
                    pending = True
                    rows[cluster] = {"hash": h, "verdict": None, "R_gap": None, "state": self.store.get(h).state.value}
                else:
                    rows[cluster] = row
            if pending:
                reached = st.name
                break
            reached = st.name
            if any(r["verdict"] == G.FAIL for r in rows.values()):
                break
        first_clusters = acc["stages"]["control"] if "control" in acc["stages"] else self.cfg.stages[0].clusters
        first_done = all(rows.get(c, {}).get("verdict") is not None for c in first_clusters)
        verdicts = [r["verdict"] for r in rows.values() if r.get("verdict")]
        verdict = G.worst(*verdicts) if verdicts else None
        status = PENDING if pending else (FAILED if verdict == G.FAIL else DONE)
        r_gaps = [r["R_gap"] for r in rows.values() if r.get("R_gap") is not None]
        diag = acc.get("diagnostics", {})
        for r in rows.values():
            if r.get("delta_lll") and r.get("gap") and diag.get("M2_k"):
                r["R_beyondM2"] = r["gap"] / (diag["M2_k"] * r["delta_lll"])
                r["R_staticM2"] = r["gap"] / (diag["M2_parent"] * r["delta_lll"])
        return {"status": status, "first_stage_done": first_done, "parent": parent, "kind": kind,
                "withdrawn": withdrawn, "stage_reached": reached, "verdict": verdict, "clusters": rows,
                "R_gap_min": min(r_gaps) if r_gaps else None,
                "claim": G.claim(rows, self.cfg.claims) if kind == "search" else None,
                "diagnostics": diag}

    def _promote(self, d: Path, acc: dict, stage: str, clusters: list[str], promotions: dict) -> dict:
        # The validated, cluster-agnostic input saved at acceptance: no stage's
        # overrides leak into another stage.
        base = EDInput.model_validate_json((d / "base_ed_input.json").read_text())
        hashes = {}
        for cluster in clusters:
            ed = self._expand(base, cluster)
            self._register(ed, cluster, f"_promote/{acc['agent']}/{acc['req_id']}")
            hashes[cluster] = ed.config_hash
        promotions = {**promotions, stage: hashes}
        atomic_write_json(d / "promotions.json", promotions)
        LOG.info("promote %s/%s -> %s", acc["agent"], acc["req_id"], stage)
        return hashes

    # ------------------------------------------------------------------
    # 7. leaderboards (store-derived)
    # ------------------------------------------------------------------

    def _collect(self) -> list[dict]:
        out = []
        for agent in self.L.agents:
            for d, acc in self._accepted(agent):
                res = read_json(d / "result.json") or {}
                if res.get("status") in (None, REJECTED):
                    continue
                out.append({"req_id": d.name, "agent": agent, "family": acc.get("family"), **res})
        return out

    def leaderboard_data(self, rows: list[dict], agents: list[str]) -> dict:
        board, other, controls = {p: [] for p in self.cfg.request_parents}, [], []
        for r in rows:
            if r["agent"] not in agents:
                continue
            if r.get("kind") != "search" or r.get("withdrawn"):
                controls.append(r)
            elif r.get("verdict") == G.FAIL:
                if any((c.get("R_gap") or 0) > 1 for c in r["clusters"].values()):
                    other.append(r)
            elif r.get("R_gap_min") is not None:
                board[r["parent"]].append(r)
        for lst in board.values():
            # PASS first; AMBIGUOUS (sent for inspection) after, flagged.
            lst.sort(key=lambda r: (r.get("verdict") != G.PASS, -r["R_gap_min"]))
        acc = {a: self._accepted(a) for a in agents}
        budget = {a: {"charged": sum(x.get("charged_evaluations", 0) for _, x in acc[a]),
                      "quota": self.cfg.quotas.evaluations_per_agent} for a in agents}
        return {"arm": self.arm, "updated_at": utc_iso(), "stages": [s.name for s in self.cfg.stages],
                "parents": {p: {c: (r or {}).get("gap") for c, r in self.parent_rows.get(p, {}).items()}
                            for p in self.cfg.parents},
                "leaderboards": board, "other_phases": other, "controls": controls, "budget": budget}

    def _leaderboard(self) -> None:
        rows = self._collect()
        data = self.leaderboard_data(rows, self.L.agents)
        data["evaluations"] = {s.value: n for s, n in self.store.count_by_state(self.campaign).items()}
        atomic_write_json(self.L.leaderboard_json, data)
        atomic_write_text(self.L.leaderboard_md, render_leaderboard(data, self.cfg))
        if self.L.private:
            for agent in self.L.agents:
                own = self.leaderboard_data(rows, [agent])
                atomic_write_json(self.L.agent_dir(agent) / "leaderboard.json", own)
                atomic_write_text(self.L.agent_dir(agent) / "leaderboard.md", render_leaderboard(own, self.cfg))

    # ------------------------------------------------------------------

    def _heartbeat(self) -> None:
        # Also written mid-tick: a long acceptance pass must not look like a
        # dead broker to the agents (digest flags > 10 ticks of silence).
        atomic_write_json(self.L.root / "broker.json", {
            "pid": os.getpid(), "host": socket.gethostname(), "last_tick": utc_iso()})

    def tick(self) -> None:
        self._heartbeat()
        self._parents()
        self._accept_requests()
        self._reconcile()
        self._enqueue()
        self._jobs()
        self._parents()  # pick up parent results ingested this tick
        self._results()
        self._reprioritize()
        self._leaderboard()
        self._heartbeat()


def _fmt(x: Optional[float], f: str = "{:.4f}") -> str:
    return "" if x is None else f.format(x)


def render_leaderboard(data: dict, cfg: SwarmConfig) -> str:
    clusters = cfg.all_clusters
    lines = [f"# Leaderboards — arm `{data['arm']}` (updated {data['updated_at']})", "",
             "R_gap = Δ / Δ_static(parent) on the same cluster. Ranked by the minimum R_gap over the clusters a "
             "request has reached. Verdict per cluster: P = PASS, A = AMBIGUOUS, F = FAIL, … = running. "
             "Built from the store only.", "",
             "Stages: " + " → ".join(f"{s.name} [{', '.join(s.clusters)}]" for s in cfg.stages), ""]
    for p, gaps in data["parents"].items():
        lines.append(f"Parent `{p}` Δ: " + ", ".join(f"{c} {g:.6e}" for c, g in gaps.items() if g))
    head = ["#", "req", "agent", "family"] + [f"{c}" for c in clusters] + ["R_gap min", "stage", "claim", "M2(k)"]

    def table(rows):
        out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
        for i, r in enumerate(rows, 1):
            cells = [str(i), r["req_id"], r["agent"], str(r.get("family"))]
            for c in clusters:
                x = r["clusters"].get(c)
                if not x:
                    cells.append("")
                elif x.get("verdict") is None:
                    cells.append("…")
                else:
                    cells.append(f"{_fmt(x.get('R_gap'))} {x['verdict'][0]}")
            cells += [_fmt(r.get("R_gap_min")), str(r.get("stage_reached")), r.get("claim") or "",
                      _fmt((r.get("diagnostics") or {}).get("M2_k"), "{:.3f}")]
            out.append("| " + " | ".join(cells) + " |")
        return out

    for p, rows in data["leaderboards"].items():
        lines += ["", f"## Parent `{p}` — Laughlin-qualified (PASS first, then AMBIGUOUS for inspection)", ""] + (
            table(rows) if rows else ["(empty)"])
    lines += ["", "## Other phases — a gate FAILed, R_gap > 1 somewhere", ""] + (
        table(data["other_phases"]) if data["other_phases"] else ["(empty)"])
    if data["controls"]:
        lines += ["", "## Controls, diagnostics and withdrawn requests (not ranked)", ""] + table(data["controls"])
    lines += ["", "Budget (evaluations charged / quota): " + ", ".join(
        f"{a} {b['charged']}/{b['quota']}" for a, b in data["budget"].items())]
    if data.get("evaluations"):
        lines.append("Evaluations by state: " + ", ".join(f"{k} {v}" for k, v in sorted(data["evaluations"].items())))
    return "\n".join(lines) + "\n"


def make_backend(cfg: SwarmConfig, parents: dict[str, EDInput]) -> PoolBackend:
    if cfg.broker.backend == "mock":
        if cfg.broker.mock_evaluator == "synthetic":
            from mosaic.swarm.rehearsal import SyntheticLandscape

            primary = parents[cfg.request_parents[0]]
            return MockPool(evaluator=SyntheticLandscape(primary))
        return MockPool(logical_failure_rate=cfg.broker.mock_logical_failure_rate,
                        transient_failure_rate=cfg.broker.mock_transient_failure_rate)
    return SlurmPool()


def run(config_path: str | Path, *, once: bool = False, backend: Optional[PoolBackend] = None) -> int:
    cfg = load_swarm(config_path)
    halt = cfg.root_path / "HALT"
    if halt.exists():
        LOG.error("HALT present (%s); remove it after fixing the cause", halt.read_text().strip())
        return 3
    parents = build_parents(cfg)
    pes_counts = load_pes_counts(cfg)
    backend = backend or make_backend(cfg, parents)
    brokers = [ArmBroker(cfg, arm, backend, parents, pes_counts) for arm in cfg.arms]
    try:
        while True:
            for b in brokers:
                b.tick()
            if once:
                return 0
            time.sleep(cfg.broker.tick_seconds)
    except BrokerHalt as exc:
        LOG.error("HALT: %s", exc)
        atomic_write_text(halt, f"{utc_iso()} {exc}\n")
        return 3
    finally:
        for b in brokers:
            b.close()
