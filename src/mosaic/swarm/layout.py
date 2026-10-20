"""Directory layout of one arm.

    <root>/<arm>/
        board/                    shared arm: every post; private arm: board/<agent>/
        mail/<agent>/             directed mail (shared arm only)
        agents/<agent>/           status.json (roster), cursor.json, session.json, done
        inbox/<agent>/<req_id>/   request.json + ed_input.json (agent);
                                  accepted.json, result.json (broker)
        store/                    index.db + runs/<hash>/   (broker is the only writer)
        pool/<tier>/              one ``<stamp>_<hash>.run`` per queued evaluation
        jobs/<tier>/              one ``<job_id>.json`` per pool job submitted
        leaderboard.json, leaderboard.md
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from mosaic.swarm.config import SwarmConfig


@dataclass(frozen=True)
class ArmLayout:
    cfg: SwarmConfig
    arm: str

    @property
    def root(self) -> Path:
        return self.cfg.arm_root(self.arm)

    @property
    def private(self) -> bool:
        return self.cfg.arms[self.arm].mode == "private"

    @property
    def agents(self) -> list[str]:
        return list(self.cfg.arms[self.arm].agents)

    def board_dir(self, agent: str) -> Path:
        return self.root / "board" / agent if self.private else self.root / "board"

    def board_dirs_visible_to(self, agent: str) -> list[Path]:
        return [self.board_dir(agent)]

    def mail_dir(self, agent: str) -> Path:
        return self.root / "mail" / agent

    def agent_dir(self, agent: str) -> Path:
        return self.root / "agents" / agent

    def inbox(self, agent: str) -> Path:
        return self.root / "inbox" / agent

    @property
    def store_db(self) -> Path:
        return self.root / "store" / "index.db"

    @property
    def runs_dir(self) -> Path:
        return self.root / "store" / "runs"

    def pool_dir(self, tier: str) -> Path:
        return self.root / "pool" / tier

    def jobs_dir(self, tier: str) -> Path:
        return self.root / "jobs" / tier

    @property
    def leaderboard_json(self) -> Path:
        return self.root / "leaderboard.json"

    @property
    def leaderboard_md(self) -> Path:
        return self.root / "leaderboard.md"

    def ensure(self) -> None:
        for a in self.agents:
            for d in (self.board_dir(a), self.agent_dir(a), self.inbox(a)):
                d.mkdir(parents=True, exist_ok=True)
            if not self.private:
                self.mail_dir(a).mkdir(parents=True, exist_ok=True)
        for t in self.cfg.broker.tiers:
            self.pool_dir(t).mkdir(parents=True, exist_ok=True)
            self.jobs_dir(t).mkdir(parents=True, exist_ok=True)
        self.runs_dir.mkdir(parents=True, exist_ok=True)
