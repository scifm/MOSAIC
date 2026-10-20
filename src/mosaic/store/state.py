"""RunState enum and transition rules.

The state of a single ED evaluation as it moves through the pipeline.
Stored as a string in the DB and on disk so it survives schema drift.
"""

from __future__ import annotations

from enum import Enum


class RunState(str, Enum):
    PROPOSED = "PROPOSED"
    SUBMITTED = "SUBMITTED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED_LOGICAL = "FAILED_LOGICAL"
    FAILED_TRANSIENT = "FAILED_TRANSIENT"
    FAILED_TRANSIENT_TERMINAL = "FAILED_TRANSIENT_TERMINAL"


TERMINAL_STATES = frozenset(
    {RunState.COMPLETED, RunState.FAILED_LOGICAL, RunState.FAILED_TRANSIENT_TERMINAL}
)
"""Terminal: no further transitions allowed by the orchestrator."""


# Allowed transitions. Source of truth for ``ResultStore.transition``.
ALLOWED_TRANSITIONS: dict[RunState | None, frozenset[RunState]] = {
    None: frozenset({RunState.PROPOSED}),  # initial
    RunState.PROPOSED: frozenset({RunState.SUBMITTED, RunState.FAILED_LOGICAL}),
    RunState.SUBMITTED: frozenset(
        {RunState.RUNNING, RunState.COMPLETED, RunState.FAILED_LOGICAL, RunState.FAILED_TRANSIENT}
    ),
    RunState.RUNNING: frozenset(
        {RunState.COMPLETED, RunState.FAILED_LOGICAL, RunState.FAILED_TRANSIENT}
    ),
    # FAILED_TRANSIENT can be re-submitted (retry) or escalated to terminal.
    RunState.FAILED_TRANSIENT: frozenset(
        {RunState.SUBMITTED, RunState.FAILED_TRANSIENT_TERMINAL}
    ),
}


def is_terminal(state: RunState) -> bool:
    return state in TERMINAL_STATES
