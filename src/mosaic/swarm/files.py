"""File primitives for the swarm.

All coordination is files on NFS, written by many processes on many nodes.
Two rules make that safe without locks:

- every file is written to a temp name in the same directory and renamed
  into place (rename is atomic on one filesystem), so a reader never sees a
  partial file;
- files that several writers could create are named so that two writers
  never pick the same name (timestamp + agent + random suffix).

Readers never order by mtime (NFS attribute caching makes cross-node mtimes
unreliable); they order by the UTC stamp in the name, and track what they
have already seen as a set of ids, so a file that becomes visible late is
still delivered.
"""

from __future__ import annotations

import json
import os
import secrets
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def utc_stamp(t: datetime | None = None) -> str:
    """Sortable, filename-safe UTC stamp, e.g. ``20260930T153012.123Z``."""

    t = t or utc_now()
    return t.strftime("%Y%m%dT%H%M%S.") + f"{t.microsecond // 1000:03d}Z"


def utc_iso(t: datetime | None = None) -> str:
    return (t or utc_now()).isoformat(timespec="seconds")


def parse_iso(s: str) -> datetime:
    return datetime.fromisoformat(s)


def atomic_write_text(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.parent / f".tmp-{path.name}-{os.getpid()}-{secrets.token_hex(3)}"
    tmp.write_text(text)
    os.replace(tmp, path)
    return path


def atomic_write_json(path: Path, obj: Any) -> Path:
    return atomic_write_text(path, json.dumps(obj, indent=1, sort_keys=True) + "\n")


def read_json(path: Path, default: Any = None) -> Any:
    try:
        return json.loads(path.read_text())
    except FileNotFoundError:
        return default


def new_id(agent: str, kind: str) -> str:
    return f"{utc_stamp()}_{agent}_{kind}_{secrets.token_hex(2)}"


def write_markdown_with_front_matter(path: Path, meta: dict, body: str) -> Path:
    head = yaml.safe_dump(meta, sort_keys=True, allow_unicode=True).strip()
    return atomic_write_text(path, f"---\n{head}\n---\n{body.rstrip()}\n")


def read_markdown_with_front_matter(path: Path) -> tuple[dict, str]:
    text = path.read_text()
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing front matter")
    end = text.index("\n---\n", 4)
    return yaml.safe_load(text[4:end]) or {}, text[end + 5:]


def visible_entries(directory: Path, suffix: str = "") -> list[Path]:
    """Entries of ``directory`` that are complete (no temp files), sorted by name."""

    if not directory.is_dir():
        return []
    return sorted(p for p in directory.iterdir()
                  if not p.name.startswith(".") and p.name.endswith(suffix))
