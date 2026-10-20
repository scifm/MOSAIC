"""Canonical JSON serialization and content hashing.

The config hash is the *identity* of every ED evaluation. Hash inputs
must therefore be (a) reproducible across processes, (b) insensitive to
dict ordering, and (c) insensitive to JSON whitespace formatting. Any
change to the canonicalization rules is a breaking schema change.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any


def canonical_json(obj: Any) -> str:
    """Serialize ``obj`` to JSON in the canonical form used for hashing.

    Rules: sorted keys, no insignificant whitespace, ASCII-safe escapes
    off (so unicode round-trips), separators fixed. Floats are formatted
    by the standard JSON encoder; if you want a different float repr,
    quantize before calling this function.
    """

    return json.dumps(
        obj,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    )


def content_hash(obj: Any) -> str:
    """Return the sha256 hex digest of ``canonical_json(obj)``."""

    payload = canonical_json(obj).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def short_hash(h: str, n: int = 12) -> str:
    """Truncate a hash for human-readable logging. Never use as identity."""

    if len(h) < n:
        raise ValueError(f"hash {h!r} shorter than requested {n}")
    return h[:n]
