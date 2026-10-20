"""ED JSON v1 contract.

This module is the **single source of truth** for the ED-side JSON
schema. Both the mock ED and the real Julia wrapper conform to it.
Any breaking change bumps ``schema_version`` and must be documented.

The pydantic models here:
- validate JSON on read (so a bad solver output fails loudly),
- serialize JSON on write (so disk artifacts stay schema-conformant),
- accept and emit ``Complex`` numbers as ``{"re": ..., "im": ...}``
  pairs (Julia's ``ComplexF64`` does not have a canonical JSON form,
  and ``[re, im]`` would conflict with vector types).
"""

from __future__ import annotations

from typing import Annotated, Literal, Optional

from pydantic import model_serializer, model_validator, BaseModel, ConfigDict, Field

# ---------------------------------------------------------------------------
# Atomic types
# ---------------------------------------------------------------------------


class Complex(BaseModel):
    """JSON representation of a complex scalar."""

    model_config = ConfigDict(extra="forbid")
    re: float
    im: float

    def to_python(self) -> complex:
        return complex(self.re, self.im)

    @classmethod
    def from_python(cls, z: complex) -> "Complex":
        return cls(re=float(z.real), im=float(z.imag))


class WGCoef(BaseModel):
    """One form-factor coefficient at reciprocal vector ``G_int``.

    ``G_int`` is the integer index ``(m, n)`` on the moiré reciprocal
    basis ``b_1, b_2``, in the solver's 120° convention
    (``G = m G_1 + n G_2``, ``|G|² ∝ m² + n² − mn``). ``shell`` and
    ``idx`` are Python-side bookkeeping only; in configurations stored under
    the older 60° convention they refer to 60° shells and are legacy metadata.

    **Semantics.** ``coef`` is the Fourier
    coefficient ``w_G`` of the *probability density*
    ``|h(r)|² = sum_G w_G exp(i G · r)``, not of an envelope. The
    constraints ``w_{(0,0)} = 1 + 0i`` and ``w_{-G} = w_G*`` are
    enforced upstream by the parameterizer.
    """

    model_config = ConfigDict(extra="forbid")
    shell: int
    idx: int
    G_int: tuple[int, int]
    coef: Complex


# ---------------------------------------------------------------------------
# Input
# ---------------------------------------------------------------------------


class LatticeSpec(BaseModel):
    model_config = ConfigDict(extra="forbid")
    n_k: int = Field(..., ge=4, description="Number of k-points of the cluster (24 for 4×6, 27 for the 27-site cluster).")
    n_shells: int = Field(..., ge=0, description="Form-factor shell count.")
    g_units: Literal["b_M"] = "b_M"


class WavefunctionSpec(BaseModel):
    model_config = ConfigDict(extra="forbid")
    n_a: int = Field(..., ge=1)
    a_n: list[Complex]
    norm_convention: Literal["renormalize_post", "explicit_unit"] = "renormalize_post"


class DeformationBlock(BaseModel):
    """The k-dependent envelope deformation.

    ``gamma(k, r) = sum_{s,p} (alpha[s][p]/2 + i beta[s][p]) O_s(r) F_p(k)``
    with ``O_s`` / ``F_p`` the real, zero-mean, unit-mean-square star
    functions of the listed reciprocal (``spatial_stars``) and direct-lattice
    (``momentum_stars``) stars. The solver builds
    ``W_G(k,k') = F_G{rho_* exp(gamma(k)^* + gamma(k'))}`` from the seed
    ``W_G`` on an ``n_mesh``² grid, keeping harmonics with
    ``max(|m|,|n|) <= g_cutoff`` (default: the seed's own box). All-zero
    ``alpha``/``beta`` is the static model exactly. Reference implementation:
    ``physics.kdep_envelope``.
    """

    model_config = ConfigDict(extra="forbid")
    spatial_stars: list[list[tuple[int, int]]]
    momentum_stars: list[list[tuple[int, int]]]
    alpha: list[list[float]]
    beta: list[list[float]]
    n_mesh: int = Field(48, ge=2)
    g_cutoff: Optional[int] = Field(None, ge=0)


class FormFactorSpec(BaseModel):
    """Form-factor block of the ED input.

    There is no ``reality_mode`` switch — the
    Hermiticity constraint ``w_{-G} = w_G*`` is universal. ``W_G`` here
    are Fourier coefficients of ``|h(r)|²`` (see ``WGCoef``).

    ``deformation`` is optional; ``None`` is the static model and
    is excluded from the config hash so that every pre-existing hash is
    unchanged.
    """

    model_config = ConfigDict(extra="forbid")
    symmetry: Literal["C3_hard", "none"]
    W_G: list[WGCoef]
    deformation: Optional[DeformationBlock] = None

    @model_serializer(mode="wrap")
    def _omit_absent_deformation(self, handler):
        # A static model serialises exactly as it did before the deformation block existed, so the
        # canonical JSON — and therefore every existing config hash and every
        # stored ed_input.json — is unchanged. The Julia decoder treats an
        # absent key and a null identically.
        data = handler(self)
        if data.get("deformation") is None:
            data.pop("deformation", None)
        return data


class EDSolverParams(BaseModel):
    """Solver-specific knobs passed through opaquely.

    The Python side does not validate ``extra``; the Julia solver does.
    """

    model_config = ConfigDict(extra="forbid")
    n_basis: Optional[int] = None
    filling: Optional[float] = None
    extra: dict = Field(default_factory=dict)


class EDInput(BaseModel):
    """Input to one ED evaluation. Hashed for identity."""

    model_config = ConfigDict(extra="forbid")
    schema_version: Literal["1"] = "1"
    config_hash: str = Field(..., min_length=8)
    campaign_id: str = Field(..., min_length=8)
    seed: int
    lattice: LatticeSpec
    wavefunction: WavefunctionSpec
    form_factor: FormFactorSpec
    ed_solver_params: EDSolverParams = Field(default_factory=EDSolverParams)
    energy_unit: str = "meV"
    # Metadata only (like ``seed``): the proposer's raw parameter vector
    # x that decoded to this config. Persisted so the BO surrogate can
    # train on the exact x it proposed instead of inverting W->x via
    # ``encode`` (which is lossy/undefined for the many-to-one Cholesky
    # parameterisation). Excluded from ``config_hash``; None
    # for older runs and for configs not produced by a proposer.
    proposer_x: Optional[list[float]] = None


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------


class PESParent(BaseModel):
    model_config = ConfigDict(extra="forbid", allow_inf_nan=False)
    momentum: tuple[int, int]
    state: int = Field(ge=1)
    energy: float


class PESThresholdDiagnostic(BaseModel):
    model_config = ConfigDict(extra="forbid", allow_inf_nan=False)
    threshold: Optional[float]
    gap: Optional[float]
    counts: Optional[list[int]]
    total_count: Optional[int]


class PESCountingDiagnostic(BaseModel):
    model_config = ConfigDict(extra="forbid", allow_inf_nan=False)
    gap: Optional[float]
    threshold: Optional[float]
    matched: bool
    informative: bool


class PESOutput(BaseModel):
    """Trace-one particle/hole PES; null levels represent zero eigenvalues."""

    model_config = ConfigDict(extra="forbid", allow_inf_nan=False)
    NA: int = Field(ge=0)
    holes: bool
    N: int = Field(ge=0)
    Ns: int = Field(ge=1, le=64)
    mixture: Literal["equal_incoherent"]
    parents: list[PESParent]
    parent_sectors: list[int]
    momenta: list[tuple[int, int]]
    eigenvalues: list[list[float]]
    levels: list[list[Optional[float]]]
    display_levels: list[list[float]]
    dimensions: list[int]
    ranks: list[int]
    trace: float
    minimum_eigenvalue: float
    zero_tol: float = Field(ge=0, lt=1)
    level_floor: float = Field(gt=0, lt=1)
    threshold_mode: Literal["none", "manual", "given_count", "auto_gap"]
    threshold_diagnostic: PESThresholdDiagnostic
    counting_diagnostic: Optional[PESCountingDiagnostic]

    @model_validator(mode="after")
    def validate_sector_shapes(self) -> "PESOutput":
        n = len(self.momenta)
        arrays = (self.eigenvalues, self.levels, self.display_levels, self.dimensions, self.ranks)
        if n == 0 or any(len(array) != n for array in arrays):
            raise ValueError("PES arrays must have one entry per momentum sector")
        if not self.parents or len(self.parents) != len(self.parent_sectors):
            raise ValueError("PES requires one sector per nonempty parent list")
        if self.N > self.Ns or self.NA > (self.Ns - self.N if self.holes else self.N):
            raise ValueError("PES particle partition is out of range")
        for i, dimension in enumerate(self.dimensions):
            if dimension < 0 or not 0 <= self.ranks[i] <= dimension:
                raise ValueError("Invalid PES dimensions/ranks")
            if any(len(array[i]) != dimension for array in arrays[:3]):
                raise ValueError("PES eigenvalues and levels must match sector dimensions")
        if any(s < 0 or s >= n for s in self.parent_sectors):
            raise ValueError("PES parent sector is out of range")
        return self


class EDOutput(BaseModel):
    """Output of one ED evaluation.

    Shapes (when ``status == "completed"``):
        ``epsilon_target``, ``epsilon_above``, ``epsilon_below`` :
            ``[n_k, n_k]`` arrays of floats. ``None`` if no neighbor
            band exists (rejected as ``failed_logical: spectrum_edge``).
        ``u_k`` :
            ``[n_k, n_k, N_r, N_r]`` complex amplitudes of the periodic
            Bloch function on a real-space mesh.
            Optional. The mock omits this; the real solver should
            populate it. Stored as nested lists of ``Complex`` (large;
            offload to a sibling .npz if memory becomes an issue).
        ``chern_solver`` :
            Solver-side Chern number. Cross-check against Python's FHS
            recomputation when ``u_k`` is present.
    """

    model_config = ConfigDict(extra="forbid")
    schema_version: Literal["1"] = "1"
    config_hash: str = Field(..., min_length=8)
    status: Literal["completed", "failed_logical", "failed_transient"]
    failure_reason: Optional[str] = None
    energy_unit: str = "meV"
    n_k: int
    target_band_index: Optional[int] = None
    epsilon_target: Optional[list[list[float]]] = None
    epsilon_above: Optional[list[list[float]]] = None
    epsilon_below: Optional[list[list[float]]] = None
    u_k: Optional[list[list[list[list[Complex]]]]] = None
    chern_solver: Optional[int] = None
    chern_quantization_error_solver: Optional[float] = None
    # Solver >= v0.6.0: the glued one-period lattice with the
    # consistent sewing is the estimator behind ``chern_solver``; the
    # plaquette value above is kept as a curvature-uniformity diagnostic.
    chern_plaquette_raw: Optional[float] = None
    chern_glued_raw: Optional[float] = None
    chern_glued_residual: Optional[float] = None
    chern_glued_per_state: Optional[list[float]] = None
    chern_max_plaquette_phase: Optional[float] = None
    chern_glued_closure: Optional[float] = None
    chern_glued_N: Optional[int] = None
    gap_top_indirect_solver: Optional[float] = None
    # Solver >= v0.7.1: the ``neigen_per_block`` lowest
    # eigenvalues per momentum sector, in ``sector_momenta`` order, and the
    # ground-manifold splitting ``E_m - E_1`` (m = round(1/nu)).
    low_energies: Optional[list[list[float]]] = None
    sector_momenta: Optional[list[tuple[int, int]]] = None
    gs_manifold_splitting: Optional[float] = None
    # Solver >= v0.8.0: eigensolver backend that ran ("sparse" =
    # CPU, "gpu"). Chosen by the job environment, so it is not in the hash.
    ed_backend: Optional[str] = None
    # Solver >= v0.9.0: settings that ran (accuracy mode, nlevels,
    # Krylov parameters), totals (solves, matvecs, max Ritz residual,
    # gap_error_bound), phase timings and memory.
    ed_solver_stats: Optional[dict] = None
    # v0.9.1: opt-in equal-mixture particle/hole entanglement diagnostic.
    pes: Optional[PESOutput] = None
    compute_seconds: float
    solver_version: str
    solver_log_path: Optional[str] = None
