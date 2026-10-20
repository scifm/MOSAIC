"""Swarm config: one YAML describes both arms, the broker and the
agent allocation. Paths are resolved against ``repo_main`` so the same file
works from the main checkout, from an agent worktree and from a compute node.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Literal, Optional

import yaml
from pydantic import BaseModel, ConfigDict, Field, model_validator

REPO_ROOT = Path(__file__).resolve().parents[3]

# Keys of ``ed_solver_params.extra`` the broker owns: the cluster, the solver
# accuracy mode ("search" for screening, "confirm" for finalists) and
# the PES request. An agent's values are overwritten by the
# expansion.
CLUSTER_KEYS = ("nk1", "nk2", "symcluster", "ed_accuracy", "pes")


class ClusterSpec(BaseModel):
    """One finite cluster every request is evaluated on.

    Either a rectangular mesh (``nk1`` × ``nk2``) or the solver's symmetric
    cluster (``symcluster`` with ``n_k`` sites).
    """

    model_config = ConfigDict(extra="forbid")
    nk1: Optional[int] = None
    nk2: Optional[int] = None
    symcluster: Optional[int] = None
    n_k: Optional[int] = None
    tier: str
    # Solver accuracy mode written into ``extra["ed_accuracy"]``; None leaves
    # the key out (solvers before v0.9.0 do not know it).
    ed_accuracy: Optional[Literal["search", "confirm"]] = None
    # Topology gate: "skip" where the glued Chern estimator
    # cannot run (symmetric clusters), "abs1" for |C| = 1, "match_parent" for
    # the same C as the request's parent on this cluster.
    chern: Literal["skip", "abs1", "match_parent"] = "abs1"
    # PES cut N_A for the Laughlin gate; None runs no PES on this cluster.
    pes_na: Optional[int] = Field(None, ge=1)
    # Where the momentum-resolved Laughlin counts come from. None: the (1,3)
    # admissible rule (gates.pes_expected_counts). A parent name: that parent's
    # measured PES on this cluster at the closed-form total (used where the
    # rule's orbital order does not fit the cluster, e.g. 4×6).
    pes_reference: Optional[str] = None
    # Convergence rungs: solver extras (e.g. qmax) and deformation-block fields
    # (n_mesh, g_cutoff) the broker overrides on this cluster only.
    extra_overrides: dict = Field(default_factory=dict)
    deformation_overrides: dict = Field(default_factory=dict)

    @model_validator(mode="after")
    def _shape(self) -> "ClusterSpec":
        rect = self.nk1 is not None and self.nk2 is not None
        sym = self.symcluster is not None and self.n_k is not None
        if rect == sym:
            raise ValueError("cluster needs exactly one of (nk1, nk2) or (symcluster, n_k)")
        return self

    @property
    def sites(self) -> int:
        return self.n_k if self.symcluster is not None else self.nk1 * self.nk2


class TierSpec(BaseModel):
    """A Slurm pool for one class of evaluation (CPU 4×6, GPU 5×6, ...)."""

    model_config = ConfigDict(extra="forbid")
    partition: str
    reservation: Optional[str] = None
    qos: Optional[str] = None
    lanes: int = Field(..., ge=1)
    threads: int = Field(..., ge=1)
    gpus: int = Field(0, ge=0)
    mem: str
    walltime: str
    max_jobs: int = Field(1, ge=1)
    # A lane does not start an evaluation it cannot finish before walltime.
    est_run_seconds: int = Field(..., ge=1)
    # per_eval: one ed_solver.jl process per evaluation (pays ~20 s of JIT each).
    # persistent: julia/ed_batch.jl compiles once per pass (solver >= v0.9.0).
    lane_mode: Literal["per_eval", "persistent"] = "per_eval"
    # persistent: entries per pass. A pass works from the queue order it read
    # at its start, so a long pass ignores re-prioritization.
    pass_size: int = Field(8, ge=1)


class ArmSpec(BaseModel):
    model_config = ConfigDict(extra="forbid")
    # shared: board/roster/mail/leaderboard visible to the whole arm.
    # private: each agent sees only its own posts and results (the control).
    mode: Literal["shared", "private"]
    agents: list[str] = Field(..., min_length=1)


class ParentSpec(BaseModel):
    """A static parent band. Either a full ``ed_input`` file,
    or static density shell weights on the solver-basis shells (120° basis),
    completed from ``regime.template_ed_input`` and ``regime.a_n``."""

    model_config = ConfigDict(extra="forbid")
    ed_input: Optional[str] = None
    # One weight per shell 1..n (strings such as "3/5" are exact fractions).
    shells: Optional[list[str]] = None
    # Gaps measured before the swarm, per cluster name. The broker halts if its
    # own parent evaluations disagree: the solver or the parent changed.
    expected_gap: dict[str, float] = Field(default_factory=dict)
    # One tolerance, or one per cluster: search-accuracy gaps vary between runs
    # by up to ~1e-5 relative (Krylov tol 1e-6), confirm
    # accuracy reproduces to ~1e-14.
    expected_rtol: float | dict[str, float] = 1e-6

    def rtol(self, cluster: str) -> float:
        if isinstance(self.expected_rtol, dict):
            return self.expected_rtol.get(cluster, 1e-6)
        return self.expected_rtol
    # "diagnostic" parents (e.g. the uniform LLL band) are evaluated on every
    # cluster for reported ratios but cannot be named by requests.
    role: Literal["parent", "diagnostic"] = "parent"

    @model_validator(mode="after")
    def _one_source(self) -> "ParentSpec":
        if (self.ed_input is None) == (self.shells is None):
            raise ValueError("a parent needs exactly one of ed_input or shells")
        return self


class RegimeSpec(BaseModel):
    """What every request shares with its parent."""

    model_config = ConfigDict(extra="forbid")
    # Interaction / normalization extras and units come from this input.
    template_ed_input: Optional[str] = None
    a_n: Optional[list[float]] = None
    # True: only the deformation block may differ from the named parent.
    pin_static: bool = False


class StageSpec(BaseModel):
    """One rung of the promotion ladder."""

    model_config = ConfigDict(extra="forbid")
    name: str
    clusters: list[str] = Field(..., min_length=1)
    # Entry rule (ignored for the first stage): every gate so far in
    # ``promote_verdicts`` and the minimum R_gap so far at least this.
    promote_min_R_gap: float = 1.0
    # Clusters the threshold is taken over (default: every cluster reached so
    # far), so a cluster such as Nk = 21 can set the sign without setting the threshold.
    promote_on: Optional[list[str]] = None
    promote_verdicts: list[Literal["PASS", "AMBIGUOUS"]] = Field(default_factory=lambda: ["PASS", "AMBIGUOUS"])


class ClaimSpec(BaseModel):
    """An outcome label, strongest first. A request earns it
    when every cluster in ``all_clusters`` is reached with gate PASS and
    R_gap > 1, and every cluster in ``min_R_gap`` reaches its threshold."""

    model_config = ConfigDict(extra="forbid")
    name: str
    all_clusters: list[str]
    min_R_gap: dict[str, float] = Field(default_factory=dict)


class BoundarySpec(BaseModel):
    """Search boundary: a request outside it is refused.

    Shells are measured as |G|²/|G1|² = m² + n² − mn for spatial stars (120°
    reciprocal basis) and |R|²/|a|² = m² + n² + mn for momentum stars (60°
    lattice basis); a star counts by its largest member. Coefficient bounds act
    on the α, β entries of the deformation block; the M2 cap bounds the
    BZ-averaged envelope sharpness M2^(k) relative to the parent's static M2,
    so a gain cannot come from sharpening the density without limit."""

    model_config = ConfigDict(extra="forbid")
    spatial_g2_max: int = Field(..., ge=1)
    momentum_r2_max: int = Field(..., ge=1)
    alpha_max: float = Field(..., gt=0)
    beta_max: float = Field(..., gt=0)
    alpha_sum_max: float = Field(..., gt=0)
    beta_sum_max: float = Field(..., gt=0)
    m2k_max_ratio: float = Field(..., gt=1)


class GateSpec(BaseModel):
    model_config = ConfigDict(extra="forbid")
    split_max: float = 0.1            # ground-manifold splitting / Δ
    pes_gap_pass: float = 0.5         # entanglement gap for PASS (else AMBIGUOUS)
    # Laughlin (1,3) counts per sector, "<cluster>:<N_A>" -> {momenta, counts,
    # total}; produced by scripts/pes_expected_counts.jl (`swarm pes-cases`).
    pes_expected_counts: Optional[str] = None
    # Admissibility (pure LL0): min S00 / max S00 over the ED meshes and a
    # dense fractional grid.
    admissibility_min_ratio: Optional[float] = None
    admissibility_grid: int = 24
    boundary: Optional[BoundarySpec] = None     # search boundary; None = only the chart and admissibility
    # failed_logical reasons that still carry a valid gap where chern = "skip".
    chern_skip_reasons: list[str] = Field(default_factory=lambda: [
        "mesh_unsuitable_for_chern", "chern_manifold_not_spectral_flow_orbit"])


class QuotaSpec(BaseModel):
    model_config = ConfigDict(extra="forbid")
    # Charged per newly registered first-stage evaluation (promotions are free).
    evaluations_per_agent: int = Field(..., ge=1)
    max_in_flight_per_agent: int = Field(..., ge=1)


class BrokerSpec(BaseModel):
    model_config = ConfigDict(extra="forbid")
    backend: Literal["slurm", "mock"] = "slurm"
    tick_seconds: int = 30
    max_retries: int = 1
    idle_exit_seconds: int = 600
    poll_seconds: int = 20  # how often an idle lane rescans its pool
    # Requests accepted per arm per tick (round-robin across agents), so a
    # backlog never holds a tick in acceptance.
    max_accepts_per_tick: int = 60
    julia: str = "julia"
    # Git ref the solver snapshot is checked out at (``swarm setup``); pool
    # jobs never run the main checkout's julia/, which other sessions edit.
    solver_ref: str
    solver_version_prefix: str
    tiers: dict[str, TierSpec]
    # Mock backend only. "synthetic" is the rehearsal landscape
    # (swarm.rehearsal); "ed_mock" is ed.mock.evaluate with the rates below.
    mock_evaluator: Literal["ed_mock", "synthetic"] = "ed_mock"
    mock_logical_failure_rate: float = 0.0
    mock_transient_failure_rate: float = 0.0


class AgentJobSpec(BaseModel):
    """The Slurm allocation the agent sessions run in."""

    model_config = ConfigDict(extra="forbid")
    partition: str = "cpu"
    reservation: Optional[str] = None
    qos: Optional[str] = None
    cpus_per_agent: int = 2
    # Seconds between agent launches within an arm, so later agents start by
    # reading the plans earlier ones have posted instead of all choosing at once.
    stagger_seconds: int = 0
    mem_per_agent_gb: int = 4
    walltime: str = "48:00:00"
    claude: str = "claude"
    model: Optional[str] = None
    permission_mode: Literal["auto", "acceptEdits", "manual"] = "auto"
    # An inherited ANTHROPIC_API_KEY takes precedence over the Claude subscription
    # login; unset it in agent jobs when agents should use the login.
    # True: unset it, so agents use the login.
    unset_api_key: bool = True
    # If an agent allocation is still pending after this many minutes, move it
    # onto this reservation/QOS (the general partition is often full while the
    # group's short reservation sits idle, or the reverse).
    fallback_reservation: Optional[str] = None
    fallback_qos: Optional[str] = None
    fallback_after_minutes: int = 15

class SwarmConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    swarm_id: str = Field(..., min_length=4, pattern=r"^[a-z0-9][a-z0-9-]+$")
    root: str
    repo_main: str = str(REPO_ROOT)
    worktree_root: str
    arms: dict[str, ArmSpec]
    # Optional per-agent starting directions. Left out (the default), agents
    # choose and coordinate their own scope (see the charter).
    directions: dict[str, str] = Field(default_factory=dict)
    # Optional shared campaign prompt every agent reads (e.g. a
    # search brief), inserted into each charter.
    mission: Optional[str] = None
    parents: dict[str, ParentSpec]
    regime: RegimeSpec = Field(default_factory=RegimeSpec)
    clusters: dict[str, ClusterSpec]
    # Promotion is by threshold, not top-k, so the rule never depends on other
    # agents' results (the control arm must not learn about its peers).
    stages: list[StageSpec] = Field(..., min_length=1)
    claims: list[ClaimSpec] = Field(default_factory=list)
    gates: GateSpec = Field(default_factory=GateSpec)
    # A diagnostic parent (uniform envelope) whose gap is Δ_LLL for the reported
    # R_staticM2 / R_beyondM2 ratios (diagnostics only).
    lll_parent: Optional[str] = None
    # Keys of ``extra`` an agent may change; every other non-broker key must
    # equal the parent's value (d_sc, qmax, W0, ... stay fixed).
    agent_free_extra: list[str] = Field(default_factory=list)
    positivity_tol: float = 1e-6
    quotas: QuotaSpec
    deadline_utc: Optional[str] = None
    broker: BrokerSpec
    agent_job: AgentJobSpec = Field(default_factory=AgentJobSpec)
    # Set for a dress rehearsal: shown at the top of every charter so agents
    # know the evaluator is synthetic and the numbers mean nothing physically.
    rehearsal_note: Optional[str] = None
    # Commit the agent worktrees branch from (``swarm/<swarm_id>/<agent>``).
    agent_base_ref: str = "HEAD"
    # Repository the agent worktrees are created in (default: ``repo_main``).
    # Campaigns that must not see earlier results use a single-commit clone of a
    # sanitized tree: a worktree of the main repository shares its object store,
    # so ``git show <branch>:<path>`` would reach every committed result.
    worktree_repo: Optional[str] = None
    # Extra guardrails for independent campaigns: paths the agents' file tools
    # may not read (absolute, or relative to ``repo_main``), and Bash command
    # prefixes they may not run. Guardrails, not a sandbox (see the runbook).
    agent_deny_read: list[str] = Field(default_factory=list)
    agent_deny_bash: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def _consistent(self) -> "SwarmConfig":
        names = [a for arm in self.arms.values() for a in arm.agents]
        if len(names) != len(set(names)):
            raise ValueError("agent names must be unique across arms")
        for a in names:
            if not a.replace("-", "").isalnum() or a.startswith("_"):
                raise ValueError(f"bad agent name {a!r}")
        for a in self.directions:
            if a not in names:
                raise ValueError(f"direction given for unknown agent {a!r}")
        for st in self.stages:
            for c in st.clusters:
                if c not in self.clusters:
                    raise ValueError(f"stage {st.name!r}: unknown cluster {c!r}")
        if len({c for st in self.stages for c in st.clusters}) != sum(len(st.clusters) for st in self.stages):
            raise ValueError("a cluster may appear in only one stage")
        for cl in self.claims:
            for c in list(cl.all_clusters) + list(cl.min_R_gap):
                if c not in self.clusters:
                    raise ValueError(f"claim {cl.name!r}: unknown cluster {c!r}")
        for name, c in self.clusters.items():
            if c.tier not in self.broker.tiers:
                raise ValueError(f"cluster {name!r} uses unknown tier {c.tier!r}")
        if not [p for p in self.parents.values() if p.role == "parent"]:
            raise ValueError("need at least one parent with role 'parent'")
        if self.lll_parent is not None and self.parents.get(self.lll_parent, None) is None:
            raise ValueError(f"lll_parent {self.lll_parent!r} is not a parent")
        if any(p.shells is not None for p in self.parents.values()) and not self.regime.template_ed_input:
            raise ValueError("shell-weight parents need regime.template_ed_input")
        if any(c.pes_na and not c.pes_reference for c in self.clusters.values()) and not self.gates.pes_expected_counts:
            raise ValueError("rule-counted PES clusters need gates.pes_expected_counts")
        for name, c in self.clusters.items():
            if c.pes_reference is not None and c.pes_reference not in self.parents:
                raise ValueError(f"cluster {name!r}: pes_reference {c.pes_reference!r} is not a parent")
        if self.broker.mock_evaluator == "synthetic" and self.rehearsal_note is None:
            raise ValueError("a synthetic evaluator needs a rehearsal_note, so agents are told")
        return self

    # ------------------------------------------------------------------
    # Paths
    # ------------------------------------------------------------------

    def path(self, p: str) -> Path:
        q = Path(p)
        return Path(os.path.normpath(q if q.is_absolute() else Path(self.repo_main) / q))

    @property
    def root_path(self) -> Path:
        return self.path(self.root)

    def arm_root(self, arm: str) -> Path:
        return self.root_path / arm

    @property
    def all_clusters(self) -> list[str]:
        return [c for st in self.stages for c in st.clusters]

    @property
    def request_parents(self) -> list[str]:
        return [n for n, p in self.parents.items() if p.role == "parent"]

    def campaign_id(self, arm: str) -> str:
        return f"{self.swarm_id}-{arm}"

    def arm_of(self, agent: str) -> str:
        for name, arm in self.arms.items():
            if agent in arm.agents:
                return name
        raise KeyError(f"agent {agent!r} is in no arm")

    @property
    def worktree_root_path(self) -> Path:
        return self.path(self.worktree_root)

    def worktree(self, agent: str) -> Path:
        return self.worktree_root_path / agent

    @property
    def solver_dir(self) -> Path:
        # A detached git worktree at ``broker.solver_ref``: pool jobs never run
        # the main checkout's julia/, which other sessions edit in place.
        return self.worktree_root_path / f"solver-{self.broker.solver_ref}"


def load_swarm(path: str | Path) -> SwarmConfig:
    data = yaml.safe_load(Path(path).read_text())
    return SwarmConfig.model_validate(data)
