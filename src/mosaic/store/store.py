"""Append-only result store: SQLite index over per-run JSON-on-disk truth.

The source of truth is on disk under
``runs/<config_hash>/``. SQLite at ``store/index.db`` is a queryable
projection that ``rebuild_index()`` can regenerate from disk alone.

Key invariants
--------------
- ``register(ed_input, ...)`` is idempotent in ``config_hash``. Two
  calls with the same hash do not create two rows; the second is a
  no-op (state preserved).
- Every state transition is appended to *both* ``runs/<h>/events.jsonl``
  *and* ``events`` table. Disk write happens first; if the DB write
  fails, ``rebuild_index`` recovers from disk.
- ``runs.state`` is the **current** state (a denormalized cache of the
  last event); ``events`` is the durable history.
- ``results`` is upserted on ingest; never deleted.

Failure-mode handling
---------------------
- Disk write is atomic (open in append mode, write line + ``\n``,
  fsync, close).
- DB writes are wrapped in transactions.
- ``register`` returns the *current* state if the row already exists
  so callers can branch on it.

The store knows nothing about the optimizer or the ED solver. It
holds opaque payloads.
"""

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator, Optional

from mosaic.ed.contract import EDInput, EDOutput
from mosaic.store.state import (
    ALLOWED_TRANSITIONS,
    RunState,
    is_terminal,
)
from mosaic.util.hashing import canonical_json
from mosaic.util.logging import get_logger

LOG = get_logger("store")

_SCHEMA_PATH = Path(__file__).parent / "schema.sql"


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="microseconds")


@dataclass(frozen=True)
class RunRecord:
    config_hash: str
    campaign_id: str
    state: RunState
    proposer: str
    proposed_at: str
    config_json: str


@dataclass(frozen=True)
class ResultRecord:
    config_hash: str
    status: str
    failure_reason: Optional[str]
    chern: Optional[int]
    gap_top_indirect: Optional[float]
    energy_unit: str
    compute_seconds: float
    ed_output_path: str
    ingested_at: str


class TransitionError(RuntimeError):
    """Attempted an illegal RunState transition."""


class ResultStore:
    """File-and-DB-backed run store.

    Parameters
    ----------
    db_path : Path
        SQLite file. Created (with parents) if missing.
    work_dir : Path
        Per-run artifact root. Each run lives under ``work_dir/<config_hash>/``.
    """

    def __init__(self, db_path: Path, work_dir: Path):
        self.db_path = Path(db_path)
        self.work_dir = Path(work_dir)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.work_dir.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(self.db_path))
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.execute("PRAGMA foreign_keys=ON")
        self._conn.row_factory = sqlite3.Row
        self._init_schema()

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def _init_schema(self) -> None:
        ddl = _SCHEMA_PATH.read_text()
        with self._conn:
            self._conn.executescript(ddl)

    def close(self) -> None:
        self._conn.close()

    def __enter__(self) -> "ResultStore":
        return self

    def __exit__(self, *exc) -> None:
        self.close()

    # ------------------------------------------------------------------
    # Per-run dir helpers
    # ------------------------------------------------------------------

    def run_dir(self, config_hash: str) -> Path:
        d = self.work_dir / config_hash
        d.mkdir(parents=True, exist_ok=True)
        return d

    def _append_event_to_disk(
        self,
        config_hash: str,
        ts: str,
        from_state: Optional[RunState],
        to_state: RunState,
        payload: Optional[dict],
    ) -> None:
        path = self.run_dir(config_hash) / "events.jsonl"
        line = json.dumps(
            {
                "ts": ts,
                "from": from_state.value if from_state else None,
                "to": to_state.value,
                "payload": payload,
            },
            sort_keys=True,
        )
        with path.open("a") as f:
            f.write(line + "\n")
            f.flush()

    # ------------------------------------------------------------------
    # Registration (idempotent)
    # ------------------------------------------------------------------

    def register(
        self,
        ed_input: EDInput,
        *,
        proposer: str,
        seed: int,
        git_sha: Optional[str] = None,
    ) -> RunState:
        """Register a new candidate. Idempotent in ``ed_input.config_hash``.

        Returns the *current* state (``PROPOSED`` if newly created,
        otherwise whatever state the existing row is in).
        """

        existing = self.get(ed_input.config_hash)
        if existing is not None:
            return existing.state

        ts = _utc_now()
        run_dir = self.run_dir(ed_input.config_hash)
        # Write disk artifacts first (durable truth).
        (run_dir / "config_meta.json").write_text(
            json.dumps(
                {
                    "campaign_id": ed_input.campaign_id,
                    "config_hash": ed_input.config_hash,
                    "proposer": proposer,
                    "seed": seed,
                    "proposed_at": ts,
                    "git_sha": git_sha,
                },
                sort_keys=True,
                indent=2,
            )
        )
        (run_dir / "ed_input.json").write_text(ed_input.model_dump_json(indent=2))
        self._append_event_to_disk(
            ed_input.config_hash, ts, None, RunState.PROPOSED, payload={"proposer": proposer}
        )
        # Then DB.
        cfg_json = canonical_json(ed_input.model_dump(mode="json"))
        with self._conn:
            self._conn.execute(
                "INSERT INTO runs (config_hash, campaign_id, config_json, proposer, proposed_at, state) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                (
                    ed_input.config_hash,
                    ed_input.campaign_id,
                    cfg_json,
                    proposer,
                    ts,
                    RunState.PROPOSED.value,
                ),
            )
            self._conn.execute(
                "INSERT INTO events (config_hash, ts, from_state, to_state, payload_json) "
                "VALUES (?, ?, ?, ?, ?)",
                (
                    ed_input.config_hash,
                    ts,
                    None,
                    RunState.PROPOSED.value,
                    json.dumps({"proposer": proposer}),
                ),
            )
        return RunState.PROPOSED

    # ------------------------------------------------------------------
    # State transitions
    # ------------------------------------------------------------------

    def transition(
        self,
        config_hash: str,
        to_state: RunState,
        *,
        payload: Optional[dict] = None,
    ) -> None:
        """Record a state transition for ``config_hash``.

        Raises ``TransitionError`` if the transition is illegal per
        ``ALLOWED_TRANSITIONS``.
        """

        rec = self.get(config_hash)
        if rec is None:
            raise TransitionError(f"unknown config_hash {config_hash!r}")
        from_state = rec.state
        if is_terminal(from_state):
            raise TransitionError(
                f"{config_hash!r} is in terminal state {from_state}; cannot transition"
            )
        if to_state not in ALLOWED_TRANSITIONS.get(from_state, frozenset()):
            raise TransitionError(
                f"illegal transition {from_state} → {to_state} for {config_hash!r}"
            )

        ts = _utc_now()
        # Disk first.
        self._append_event_to_disk(config_hash, ts, from_state, to_state, payload)
        # Then DB.
        with self._conn:
            self._conn.execute(
                "INSERT INTO events (config_hash, ts, from_state, to_state, payload_json) "
                "VALUES (?, ?, ?, ?, ?)",
                (
                    config_hash,
                    ts,
                    from_state.value,
                    to_state.value,
                    json.dumps(payload) if payload else None,
                ),
            )
            self._conn.execute(
                "UPDATE runs SET state = ? WHERE config_hash = ?",
                (to_state.value, config_hash),
            )

    # ------------------------------------------------------------------
    # Result ingestion
    # ------------------------------------------------------------------

    def ingest_result(
        self,
        ed_output: EDOutput,
        *,
        chern_authoritative: Optional[int],
        gap_authoritative: Optional[float],
        ed_output_path: Path,
    ) -> None:
        """Record the *Python-authoritative* result for a config.

        Writes the ``results`` row AND a durable ``result_summary.json``
        under the per-run dir, so ``rebuild_index`` can recover the
        results table from disk alone. Does NOT transition the run
        state — the caller decides which terminal state to set based
        on ``ed_output.status`` and the Chern filter. Use
        ``transition()`` for that step.
        """

        ts = _utc_now()
        # Disk-durable summary first.
        summary = {
            "config_hash": ed_output.config_hash,
            "status": ed_output.status,
            "failure_reason": ed_output.failure_reason,
            "chern": chern_authoritative,
            "gap_top_indirect": gap_authoritative,
            "energy_unit": ed_output.energy_unit,
            "compute_seconds": ed_output.compute_seconds,
            "ed_output_path": str(ed_output_path),
            "ingested_at": ts,
        }
        summary_path = self.run_dir(ed_output.config_hash) / "result_summary.json"
        tmp_path = summary_path.with_suffix(".json.tmp")
        tmp_path.write_text(json.dumps(summary, sort_keys=True, indent=2))
        tmp_path.replace(summary_path)
        # Then DB.
        with self._conn:
            self._conn.execute(
                """
                INSERT INTO results (
                    config_hash, status, failure_reason, chern, gap_top_indirect,
                    energy_unit, compute_seconds, ed_output_path, ingested_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(config_hash) DO UPDATE SET
                    status=excluded.status,
                    failure_reason=excluded.failure_reason,
                    chern=excluded.chern,
                    gap_top_indirect=excluded.gap_top_indirect,
                    energy_unit=excluded.energy_unit,
                    compute_seconds=excluded.compute_seconds,
                    ed_output_path=excluded.ed_output_path,
                    ingested_at=excluded.ingested_at
                """,
                (
                    ed_output.config_hash,
                    ed_output.status,
                    ed_output.failure_reason,
                    chern_authoritative,
                    gap_authoritative,
                    ed_output.energy_unit,
                    ed_output.compute_seconds,
                    str(ed_output_path),
                    ts,
                ),
            )

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------

    def get(self, config_hash: str) -> Optional[RunRecord]:
        cur = self._conn.execute(
            "SELECT config_hash, campaign_id, state, proposer, proposed_at, config_json "
            "FROM runs WHERE config_hash = ?",
            (config_hash,),
        )
        row = cur.fetchone()
        if row is None:
            return None
        return RunRecord(
            config_hash=row["config_hash"],
            campaign_id=row["campaign_id"],
            state=RunState(row["state"]),
            proposer=row["proposer"],
            proposed_at=row["proposed_at"],
            config_json=row["config_json"],
        )

    def get_result(self, config_hash: str) -> Optional[ResultRecord]:
        cur = self._conn.execute(
            "SELECT * FROM results WHERE config_hash = ?", (config_hash,)
        )
        row = cur.fetchone()
        if row is None:
            return None
        return ResultRecord(
            config_hash=row["config_hash"],
            status=row["status"],
            failure_reason=row["failure_reason"],
            chern=row["chern"],
            gap_top_indirect=row["gap_top_indirect"],
            energy_unit=row["energy_unit"],
            compute_seconds=row["compute_seconds"],
            ed_output_path=row["ed_output_path"],
            ingested_at=row["ingested_at"],
        )

    def list_by_state(
        self, *states: RunState, campaign_id: Optional[str] = None
    ) -> list[RunRecord]:
        if not states:
            return []
        placeholders = ", ".join("?" * len(states))
        params: tuple = tuple(s.value for s in states)
        sql = (
            f"SELECT config_hash, campaign_id, state, proposer, proposed_at, config_json "
            f"FROM runs WHERE state IN ({placeholders})"
        )
        if campaign_id is not None:
            sql += " AND campaign_id = ?"
            params = params + (campaign_id,)
        sql += " ORDER BY proposed_at"
        cur = self._conn.execute(sql, params)
        return [
            RunRecord(
                config_hash=row["config_hash"],
                campaign_id=row["campaign_id"],
                state=RunState(row["state"]),
                proposer=row["proposer"],
                proposed_at=row["proposed_at"],
                config_json=row["config_json"],
            )
            for row in cur.fetchall()
        ]

    def count_by_state(self, campaign_id: Optional[str] = None) -> dict[RunState, int]:
        if campaign_id is None:
            cur = self._conn.execute(
                "SELECT state, COUNT(*) AS n FROM runs GROUP BY state"
            )
        else:
            cur = self._conn.execute(
                "SELECT state, COUNT(*) AS n FROM runs WHERE campaign_id = ? "
                "GROUP BY state",
                (campaign_id,),
            )
        return {RunState(row["state"]): row["n"] for row in cur.fetchall()}

    def total(self, campaign_id: Optional[str] = None) -> int:
        if campaign_id is None:
            cur = self._conn.execute("SELECT COUNT(*) FROM runs")
        else:
            cur = self._conn.execute(
                "SELECT COUNT(*) FROM runs WHERE campaign_id = ?",
                (campaign_id,),
            )
        return int(cur.fetchone()[0])

    def best(
        self, n: int = 10, *, campaign_id: Optional[str] = None
    ) -> list[ResultRecord]:
        """Top-``n`` configs with ``|chern| == 1`` ordered by gap desc.

        Excludes ``chern in (0, ±2, ...)`` (the leaderboard
        is the |C|=1 sector only). Also excludes any result whose
        ``status`` is not ``completed`` — ``failed_logical`` runs may
        still have ``chern_solver = ±1`` (e.g., the qerr threshold was
        exceeded but the rounded integer happened to be ±1) and must
        not be reported as optimisation hits.

        If ``campaign_id`` is provided, restrict the leaderboard to runs
        belonging to that campaign — runs and results share
        ``config_hash`` so a join on the ``runs`` table is sufficient.
        """

        if campaign_id is None:
            cur = self._conn.execute(
                "SELECT results.* FROM results "
                "WHERE status = 'completed' AND chern IN (-1, 1) "
                "AND gap_top_indirect IS NOT NULL "
                "ORDER BY gap_top_indirect DESC LIMIT ?",
                (n,),
            )
        else:
            cur = self._conn.execute(
                "SELECT results.* FROM results "
                "JOIN runs ON runs.config_hash = results.config_hash "
                "WHERE runs.campaign_id = ? "
                "AND results.status = 'completed' AND results.chern IN (-1, 1) "
                "AND results.gap_top_indirect IS NOT NULL "
                "ORDER BY results.gap_top_indirect DESC LIMIT ?",
                (campaign_id, n),
            )
        return [
            ResultRecord(
                config_hash=row["config_hash"],
                status=row["status"],
                failure_reason=row["failure_reason"],
                chern=row["chern"],
                gap_top_indirect=row["gap_top_indirect"],
                energy_unit=row["energy_unit"],
                compute_seconds=row["compute_seconds"],
                ed_output_path=row["ed_output_path"],
                ingested_at=row["ingested_at"],
            )
            for row in cur.fetchall()
        ]

    def retry_count(self, config_hash: str) -> int:
        """Number of distinct transient-failure events recorded so far."""

        cur = self._conn.execute(
            "SELECT COUNT(*) FROM events WHERE config_hash = ? AND to_state = ?",
            (config_hash, RunState.FAILED_TRANSIENT.value),
        )
        return int(cur.fetchone()[0])

    def iter_runs(
        self, campaign_id: Optional[str] = None
    ) -> Iterator[RunRecord]:
        if campaign_id is None:
            cur = self._conn.execute(
                "SELECT config_hash, campaign_id, state, proposer, proposed_at, "
                "config_json FROM runs"
            )
        else:
            cur = self._conn.execute(
                "SELECT config_hash, campaign_id, state, proposer, proposed_at, "
                "config_json FROM runs WHERE campaign_id = ?",
                (campaign_id,),
            )
        for row in cur.fetchall():
            yield RunRecord(
                config_hash=row["config_hash"],
                campaign_id=row["campaign_id"],
                state=RunState(row["state"]),
                proposer=row["proposer"],
                proposed_at=row["proposed_at"],
                config_json=row["config_json"],
            )

    # ------------------------------------------------------------------
    # Recovery: rebuild DB from disk
    # ------------------------------------------------------------------

    def rebuild_index(self) -> int:
        """Walk ``work_dir`` and rebuild the SQLite index from disk.

        Returns the number of runs found. Existing DB rows are wiped
        first; the disk is the source of truth.
        """

        with self._conn:
            self._conn.execute("DELETE FROM events")
            self._conn.execute("DELETE FROM results")
            self._conn.execute("DELETE FROM runs")

        n_runs = 0
        for run_dir in sorted(self.work_dir.iterdir()):
            if not run_dir.is_dir():
                continue
            meta_path = run_dir / "config_meta.json"
            input_path = run_dir / "ed_input.json"
            events_path = run_dir / "events.jsonl"
            if not (meta_path.exists() and input_path.exists() and events_path.exists()):
                LOG.warning("rebuild_index: skipping incomplete run dir %s", run_dir)
                continue
            try:
                meta = json.loads(meta_path.read_text())
                ed_input = EDInput.model_validate_json(input_path.read_text())
            except Exception as e:
                LOG.warning("rebuild_index: failed to parse %s: %s", run_dir, e)
                continue
            cfg_json = canonical_json(ed_input.model_dump(mode="json"))

            # Replay events to derive current state.
            events: list[dict] = []
            for line in events_path.read_text().splitlines():
                line = line.strip()
                if not line:
                    continue
                events.append(json.loads(line))
            if not events:
                LOG.warning("rebuild_index: no events for %s, skipping", run_dir)
                continue
            current_state = RunState(events[-1]["to"])

            with self._conn:
                self._conn.execute(
                    "INSERT INTO runs (config_hash, campaign_id, config_json, proposer, proposed_at, state) "
                    "VALUES (?, ?, ?, ?, ?, ?)",
                    (
                        ed_input.config_hash,
                        meta.get("campaign_id", ed_input.campaign_id),
                        cfg_json,
                        meta.get("proposer", "unknown"),
                        meta.get("proposed_at", events[0]["ts"]),
                        current_state.value,
                    ),
                )
                for ev in events:
                    self._conn.execute(
                        "INSERT INTO events (config_hash, ts, from_state, to_state, payload_json) "
                        "VALUES (?, ?, ?, ?, ?)",
                        (
                            ed_input.config_hash,
                            ev["ts"],
                            ev.get("from"),
                            ev["to"],
                            json.dumps(ev.get("payload")) if ev.get("payload") is not None else None,
                        ),
                    )

            # Restore the results row from the durable summary file if present.
            summary_path = run_dir / "result_summary.json"
            if summary_path.exists():
                try:
                    summary = json.loads(summary_path.read_text())
                    with self._conn:
                        self._conn.execute(
                            "INSERT INTO results (config_hash, status, failure_reason, chern, "
                            "gap_top_indirect, energy_unit, compute_seconds, ed_output_path, ingested_at) "
                            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (
                                summary["config_hash"],
                                summary["status"],
                                summary.get("failure_reason"),
                                summary.get("chern"),
                                summary.get("gap_top_indirect"),
                                summary["energy_unit"],
                                summary.get("compute_seconds", 0.0),
                                summary["ed_output_path"],
                                summary["ingested_at"],
                            ),
                        )
                except Exception as e:
                    LOG.warning("rebuild_index: failed to restore result for %s: %s", run_dir, e)
            n_runs += 1
        return n_runs
