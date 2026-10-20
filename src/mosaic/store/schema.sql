-- Schema for store/index.db.
-- The disk (runs/<hash>/) is the source of truth; this DB is a
-- queryable index, rebuildable by ResultStore.rebuild_index().

CREATE TABLE IF NOT EXISTS runs (
  config_hash      TEXT PRIMARY KEY,
  campaign_id      TEXT NOT NULL,
  config_json      TEXT NOT NULL,
  proposer         TEXT NOT NULL,
  proposed_at      TEXT NOT NULL,
  state            TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS events (
  id               INTEGER PRIMARY KEY AUTOINCREMENT,
  config_hash      TEXT NOT NULL,
  ts               TEXT NOT NULL,
  from_state       TEXT,
  to_state         TEXT NOT NULL,
  payload_json     TEXT,
  FOREIGN KEY (config_hash) REFERENCES runs(config_hash)
);

CREATE TABLE IF NOT EXISTS results (
  config_hash               TEXT PRIMARY KEY,
  status                    TEXT NOT NULL,
  failure_reason            TEXT,
  chern                     INTEGER,
  gap_top_indirect          REAL,
  energy_unit               TEXT NOT NULL,
  compute_seconds           REAL,
  ed_output_path            TEXT NOT NULL,
  ingested_at               TEXT NOT NULL,
  FOREIGN KEY (config_hash) REFERENCES runs(config_hash)
);

CREATE INDEX IF NOT EXISTS idx_runs_state    ON runs(state);
CREATE INDEX IF NOT EXISTS idx_runs_campaign ON runs(campaign_id);
CREATE INDEX IF NOT EXISTS idx_results_chern ON results(chern);
CREATE INDEX IF NOT EXISTS idx_results_gap   ON results(gap_top_indirect);
CREATE INDEX IF NOT EXISTS idx_events_hash   ON events(config_hash);
