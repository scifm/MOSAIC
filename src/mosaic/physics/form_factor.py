"""Form factor `|h(r)|² = sum_G w_G exp(i G·r)` and its `w_G` parameterization.

Conventions:

- The Fourier coefficients `w_G` parameterise the *probability density*
  `|h(r)|²`, **not** the envelope `h(r)`. The ED solver consumes
  `{w_G}` directly; the envelope is never stored.
- Hermiticity `w_{-G} = w_G*` is universal (any real density requires
  it). The previous `reality_mode` switch is dropped.
- `w_0 = 1` is fixed by the density normalisation; it is **not** a
  free DOF.
- Positivity `|h(r)|² ≥ 0` is non-linear and cannot be enforced by the
  parameterisation. We expose ``min_density_on_mesh`` so the
  orchestrator can log a soft warning.

The C_3 symmetry mode is preserved as a campaign-config knob:

- ``"C3_hard"``: parameterise within the C_3-symmetric subspace; all
  members of one C_3 orbit share a single coefficient.
- ``"none"``: independent coefficient per `±G` orbit pair.

The schema-side field name is kept as ``W_G`` (lowercase/uppercase is just
notation) — see ``src/ed/contract.py``.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import numpy as np

from mosaic.physics.lattice import (
    apply_inversion,
    c3_orbits,
    enumerate_shells,
    flat_vectors,
)

_TINY = 1e-30

SymmetryMode = Literal["C3_hard", "none"]

# Fixed by the normalisation w_0 = 1.
W0_FIXED: complex = complex(1.0, 0.0)


@dataclass(frozen=True)
class FreeDOF:
    """One independent degree of freedom in the free parameterisation.

    A DOF holds the coefficient for one *representative* ``G`` and a
    list of dependent members. Each member's coefficient is computed
    from the rep coefficient via ``transform`` (``"identity"`` or
    ``"conjugate"``).

    With the new model there is exactly one kind of non-trivial DOF —
    a complex DOF for the principal G in one ±G-paired orbit. The
    (0, 0) vector is no longer a DOF (its value is fixed by
    ``W0_FIXED``).
    """

    kind: Literal["complex"]
    rep_G: tuple[int, int]
    members: tuple[tuple[tuple[int, int], Literal["identity", "conjugate"]], ...]


class FormFactorParameterizer:
    """Map a real vector ↔ a ``{w_G}`` dict, respecting symmetry + Hermiticity.

    The forward map ``decode(x) -> w_G`` is by-construction Hermitian and
    pins ``w_{(0,0)} = 1``. The inverse ``encode(w_G) -> x`` requires
    ``w_G`` to already lie in the constrained subspace; it raises if not.

    Construction is fast (combinatorial). Cache instances per
    ``(n_shells, symmetry)`` tuple if you need many calls.
    """

    def __init__(self, n_shells: int, symmetry: SymmetryMode):
        self.n_shells = int(n_shells)
        self.symmetry = symmetry

        self.shells: list[list[tuple[int, int]]] = enumerate_shells(self.n_shells)
        self.vectors: list[tuple[int, int]] = flat_vectors(self.shells)
        self._g_to_shell: dict[tuple[int, int], int] = {
            g: s for s, shell in enumerate(self.shells) for g in shell
        }
        self._g_to_idx: dict[tuple[int, int], int] = {g: i for i, g in enumerate(self.vectors)}

        # Build C_3 orbits per shell, then concatenate (orbits never cross shells).
        self._orbits: list[tuple[tuple[int, int], ...]] = []
        for shell in self.shells:
            if symmetry == "C3_hard":
                self._orbits.extend(c3_orbits(shell))
            elif symmetry == "none":
                self._orbits.extend((g,) for g in sorted(shell))
            else:
                raise ValueError(f"unknown symmetry {symmetry!r}")

        self.dofs: tuple[FreeDOF, ...] = tuple(self._build_dofs())
        self.n_real_dof: int = sum(2 for _ in self.dofs)  # all DOFs are complex now

    # ------------------------------------------------------------------
    # Construction
    # ------------------------------------------------------------------

    def _build_dofs(self) -> list[FreeDOF]:
        g_to_orbit_idx: dict[tuple[int, int], int] = {}
        for oi, orb in enumerate(self._orbits):
            for g in orb:
                g_to_orbit_idx[g] = oi

        dofs: list[FreeDOF] = []
        consumed: set[int] = set()
        for oi, orb in sorted(enumerate(self._orbits), key=lambda x: x[1][0]):
            if oi in consumed:
                continue
            rep = orb[0]

            inv_rep = apply_inversion(rep)
            inv_oi = g_to_orbit_idx.get(inv_rep)
            if inv_oi is None:
                raise ValueError(
                    f"inversion partner of {rep} ({inv_rep}) is missing — "
                    "shell set is not closed under inversion"
                )
            inv_orb = self._orbits[inv_oi]

            if inv_oi == oi:
                # Self-paired. Only happens for the orbit of (0, 0).
                # w_0 is fixed (= 1) and contributes no DOF.
                if orb != ((0, 0),):
                    raise AssertionError(
                        f"self-paired non-trivial orbit {orb}; this should "
                        "not happen for the C_3 group on a hexagonal lattice"
                    )
                consumed.add(oi)
                continue

            # Two distinct orbits paired by inversion. Principal = lex-smaller rep.
            principal_orb, dep_orb = (orb, inv_orb) if orb[0] < inv_orb[0] else (inv_orb, orb)
            principal_oi = oi if orb[0] < inv_orb[0] else inv_oi
            dep_oi = inv_oi if orb[0] < inv_orb[0] else oi

            members = tuple(
                [(g, "identity") for g in principal_orb]
                + [(g, "conjugate") for g in dep_orb]
            )
            dofs.append(FreeDOF(kind="complex", rep_G=principal_orb[0], members=members))
            consumed.add(principal_oi)
            consumed.add(dep_oi)

        # Sanity: every non-(0,0) G must be covered exactly once.
        covered = [g for d in dofs for (g, _) in d.members]
        non_origin = [g for g in self.vectors if g != (0, 0)]
        if sorted(covered) != sorted(non_origin):
            raise AssertionError(
                "DOF layout is inconsistent: members do not cover every non-(0,0) G exactly once."
            )
        return dofs

    # ------------------------------------------------------------------
    # Decode / encode
    # ------------------------------------------------------------------

    def decode(self, x: np.ndarray) -> dict[tuple[int, int], complex]:
        """Map a real vector ``x`` of length ``n_real_dof`` to ``{w_G}``.

        Output: one entry per G in ``self.vectors``. Always:
          - ``w[(0,0)] == 1 + 0j`` (fixed by normalisation).
          - ``w_{-G} == conj(w_G)`` (Hermiticity).
        """

        x = np.asarray(x, dtype=float)
        if x.shape != (self.n_real_dof,):
            raise ValueError(f"x has shape {x.shape}; expected ({self.n_real_dof},)")
        W: dict[tuple[int, int], complex] = {}
        if (0, 0) in self._g_to_idx:
            W[(0, 0)] = W0_FIXED
        i = 0
        for dof in self.dofs:
            rep_coef = complex(float(x[i]), float(x[i + 1]))
            i += 2
            for g, transform in dof.members:
                W[g] = rep_coef if transform == "identity" else rep_coef.conjugate()
        return W

    def encode(self, W: dict[tuple[int, int], complex], tol: float = 1e-9) -> np.ndarray:
        """Inverse of ``decode``. Requires ``W`` to lie in the constrained subspace.

        Raises ``ValueError`` if ``W`` violates Hermiticity, the orbit
        symmetry, or the ``w_0 = 1`` normalisation by more than ``tol``.
        """

        if set(W.keys()) != set(self.vectors):
            raise ValueError(
                f"W has wrong key set: missing {set(self.vectors) - set(W)}, "
                f"extra {set(W) - set(self.vectors)}"
            )
        # w_0 must equal the fixed value.
        if (0, 0) in W:
            if abs(W[(0, 0)] - W0_FIXED) > tol:
                raise ValueError(
                    f"W[(0,0)] = {W[(0, 0)]} violates the fixed normalisation w_0 = 1"
                )
        x = np.empty(self.n_real_dof, dtype=float)
        i = 0
        for dof in self.dofs:
            rep_coef = complex(W[dof.rep_G])
            for g, transform in dof.members:
                expected = rep_coef if transform == "identity" else rep_coef.conjugate()
                actual = complex(W[g])
                if abs(expected - actual) > tol:
                    raise ValueError(
                        f"W[{g}]={actual} inconsistent with rep W[{dof.rep_G}]={rep_coef} "
                        f"(transform={transform!r}, sym={self.symmetry!r})"
                    )
            x[i] = rep_coef.real
            x[i + 1] = rep_coef.imag
            i += 2
        return x

    def project(self, W: dict[tuple[int, int], complex]) -> dict[tuple[int, int], complex]:
        """Project an arbitrary ``W`` onto the constrained subspace.

        For each DOF, average across (transform-corrected) members and
        re-broadcast. ``w_0`` is reset to the fixed value.
        """

        if set(W.keys()) != set(self.vectors):
            raise ValueError(f"W has wrong key set; expected {set(self.vectors)}")
        out: dict[tuple[int, int], complex] = {}
        if (0, 0) in self._g_to_idx:
            out[(0, 0)] = W0_FIXED
        for dof in self.dofs:
            samples: list[complex] = []
            for g, transform in dof.members:
                z = complex(W[g])
                samples.append(z if transform == "identity" else z.conjugate())
            avg = sum(samples) / len(samples)
            for g, transform in dof.members:
                out[g] = avg if transform == "identity" else avg.conjugate()
        return out


# -------------------------------------------------------------------------
# |h(r)|^2 evaluation (diagnostic + positivity check)
# -------------------------------------------------------------------------


def evaluate_density_on_mesh(
    W: dict[tuple[int, int], complex],
    n_mesh: int = 21,
) -> np.ndarray:
    """Evaluate ``|h(r)|² = sum_G w_G exp(i G · r)`` on a square real-space mesh.

    ``w_G`` are the Fourier coefficients of
    the density, so this returns ``|h(r)|²`` directly (not the envelope).

    For Hermitian ``w_G`` the result is real to within numerical noise;
    the imaginary part is discarded.

    Parameters
    ----------
    W : dict
        Form-factor coefficients indexed by ``G_int``. Must include
        ``(0, 0)`` for a meaningful constant baseline.
    n_mesh : int
        Real-space mesh density (``n_mesh × n_mesh`` grid over the primitive
        cell). Default ``21``.

    Returns
    -------
    rho : np.ndarray of shape (n_mesh, n_mesh), real
        The value of ``|h(r)|²`` at each mesh point.

    Notes
    -----
    The choice of physical basis ``(b_1, b_2)`` does not affect the
    minimum / maximum / mean of the density on the periodic mesh — those
    are basis-independent. It only affects which spatial point maps to
    which mesh index. We therefore evaluate with the integer convention
    ``G · r = 2π (m i + n j) / n_mesh``.
    """

    rho = np.zeros((n_mesh, n_mesh), dtype=complex)
    for (m, n), w in W.items():
        for i in range(n_mesh):
            for j in range(n_mesh):
                phase = 2.0 * np.pi * (m * i + n * j) / n_mesh
                rho[i, j] += w * np.exp(1j * phase)
    if np.max(np.abs(rho.imag)) > 1e-6:
        # The caller passed a non-Hermitian W; this is a programming error
        # (the parameteriser always produces Hermitian W). Surface it loudly.
        raise ValueError(
            "evaluate_density_on_mesh got non-Hermitian W (max imag = "
            f"{np.max(np.abs(rho.imag)):.3e})"
        )
    return rho.real


def min_density_on_mesh(
    W: dict[tuple[int, int], complex],
    n_mesh: int = 21,
) -> float:
    """Smallest value of ``|h(r)|²`` on an ``n_mesh × n_mesh`` real-space mesh.

    Positive (within tolerance) ⇒ density is non-negative on the sample.
    Negative ⇒ density goes negative somewhere; the config violates
    positivity. This is logged as a soft warning, not a
    rejection.
    """

    return float(np.min(evaluate_density_on_mesh(W, n_mesh)))


def is_hermitian(
    W: dict[tuple[int, int], complex],
    tol: float = 1e-9,
) -> bool:
    """True iff ``w_{-G} = w_G*`` for every G in ``W``."""

    for g, w in W.items():
        mg = (-g[0], -g[1])
        if mg not in W:
            return False
        if abs(w - W[mg].conjugate()) > tol:
            return False
    return True


# -------------------------------------------------------------------------
# Cholesky parameterisation:  |h(r)|² = |g(r)|².
# -------------------------------------------------------------------------


class CholeskyParameterizer:
    """Cholesky-style form-factor parameterisation.

    Write the density as a magnitude-square,

        |h(r)|²  =  |g(r)|²,        g(r)  =  Σ_{K ∈ Γ_c}  c_K  e^{i K·r},

    so the Fourier coefficients of ``|h|²`` follow by convolution,

        w_G  =  Σ_{K ∈ Γ_c}  c_K  ·  c*_{K−G}                        (★)

    Properties that fall out of (★) automatically:

    * Hermiticity ``w_{−G} = w_G*``.
    * Positivity ``|h(r)|² ≥ 0`` by construction.
    * Normalisation ``w_0 = Σ_K |c_K|² = 1`` — enforced on ``decode`` by
      rescaling ``{c_K}`` so the sum-of-squares is unity.
    * C_3 invariance of ``w`` follows when ``c`` transforms as the
      trivial 1-d C_3 irrep (``c_{R·K} = c_K``); we enforce that under
      ``symmetry="C3_hard"``.

    Gauge fix: the overall phase of ``g(r)`` leaves every ``w_G``
    unchanged, so we take ``c_0 ∈ ℝ_{≥0}``.

    Under ``C3_hard`` each C_3 orbit in the c-grid carries **one complex
    DOF** (all three members share). This is a strict superset of the
    D_6-invariant subspace the paper's Eq. S4 uses, and (for the same
    ``n_shells``) has more DOFs than the direct ``FormFactorParameterizer``
    — the extra freedom covers C_3 configurations that are not invariant
    under C_2z.

    Parameters
    ----------
    n_c_shells : int
        Number of shells in the c-grid. Must be ≥ 1.
    n_w_shells : int
        Number of shells to expose in the output ``{w_G}``. Downstream
        code (``build_ed_input`` in ``src/optim/encode.py``) reads
        ``self.shells`` and expects the same layout as
        ``FormFactorParameterizer.shells``.
    symmetry : {"C3_hard", "none"}
        C_3 symmetry on the c-side (mirrors ``FormFactorParameterizer``).
    """

    def __init__(self, n_c_shells: int, n_w_shells: int, symmetry: SymmetryMode):
        if n_c_shells < 1:
            raise ValueError(f"n_c_shells must be ≥ 1, got {n_c_shells}")
        if n_w_shells < 0:
            raise ValueError(f"n_w_shells must be ≥ 0, got {n_w_shells}")
        if symmetry not in ("C3_hard", "none"):
            raise ValueError(f"unknown symmetry {symmetry!r}")

        self.n_c_shells = int(n_c_shells)
        self.n_w_shells = int(n_w_shells)
        self.n_shells = self.n_w_shells  # alias for interface parity
        self.symmetry: SymmetryMode = symmetry

        # w-side: what we expose to downstream code (matches
        # FormFactorParameterizer.shells layout).
        self.shells: list[list[tuple[int, int]]] = enumerate_shells(self.n_w_shells)
        self.vectors: list[tuple[int, int]] = flat_vectors(self.shells)

        # c-side: what the DOFs cover.
        self._c_shells: list[list[tuple[int, int]]] = enumerate_shells(self.n_c_shells)
        self._c_vectors: list[tuple[int, int]] = flat_vectors(self._c_shells)
        self._c_set: set[tuple[int, int]] = set(self._c_vectors)

        # Truncation-safety invariant. ``|g(r)|² ≥ 0`` at every ``r``
        # by construction, but the ED consumes the *truncated* Fourier
        # series ``|h̃(r)|² = Σ_{G ∈ n_w_shells} w_G exp(i G · r)``. The
        # two agree iff every ``K − K'`` (for K, K' in the c-grid) falls
        # inside the w-grid — otherwise some ``c ⋆ c*`` contribution is
        # dropped and positivity is no longer guaranteed on the mesh.
        # Enforce the invariant at construction; raise with a clear
        # correction rather than silently breaking the
        # positivity guarantee.
        w_set = set(self.vectors)
        for K in self._c_vectors:
            for K_p in self._c_vectors:
                diff = (K[0] - K_p[0], K[1] - K_p[1])
                if diff not in w_set:
                    raise ValueError(
                        f"CholeskyParameterizer truncation invariant "
                        f"violated at K={K}, K'={K_p}: "
                        f"K − K' = {diff} is outside the w-grid "
                        f"(n_w_shells={n_w_shells}). Every pairwise "
                        "difference of c-grid vectors must land in the "
                        "w-grid, otherwise the truncated {w_G} the ED "
                        "consumes drops a c ⋆ c* contribution and the "
                        "|h(r)|² ≥ 0 guarantee no longer holds. "
                        "Increase n_w_shells or reduce n_c_shells "
                        "(the safe cap is roughly "
                        "n_c_shells ≤ n_w_shells / 3 for hexagonal "
                        "shells)."
                    )

        # C_3 orbits on the c-side. The (0, 0) orbit is degenerate
        # (single point) and receives the c_0 DOF.
        self._c_orbits: list[tuple[tuple[int, int], ...]] = []
        for shell in self._c_shells:
            if symmetry == "C3_hard":
                self._c_orbits.extend(c3_orbits(shell))
            else:
                # "none": every K is its own orbit (independent complex DOF)
                self._c_orbits.extend((k,) for k in sorted(shell))

        # DOF layout for ``x``:
        #   x[0]              — c_0 magnitude (gauge: c_0 ∈ ℝ_{≥0})
        #   x[1], x[2]        — Re, Im of the 1st non-trivial orbit
        #   x[3], x[4]        — Re, Im of the 2nd non-trivial orbit
        #   ...
        self._non_trivial_orbits: list[tuple[tuple[int, int], ...]] = [
            o for o in self._c_orbits if o != ((0, 0),)
        ]
        self.n_real_dof: int = 1 + 2 * len(self._non_trivial_orbits)

    # ------------------------------------------------------------------
    # Decode
    # ------------------------------------------------------------------

    def _pack_c(self, x: np.ndarray) -> dict[tuple[int, int], complex]:
        """Turn ``x`` into a ``{K → c_K}`` dict without normalisation."""

        if x.shape != (self.n_real_dof,):
            raise ValueError(
                f"x has shape {x.shape}; expected ({self.n_real_dof},)"
            )
        c: dict[tuple[int, int], complex] = {(0, 0): complex(abs(float(x[0])), 0.0)}
        i = 1
        for orbit in self._non_trivial_orbits:
            z = complex(float(x[i]), float(x[i + 1]))
            i += 2
            for K in orbit:
                c[K] = z
        return c

    def _normalise(
        self, c: dict[tuple[int, int], complex]
    ) -> dict[tuple[int, int], complex]:
        """Rescale so ``Σ |c_K|² = 1`` (⇒ ``w_0 = 1``)."""

        norm_sq = sum(abs(v) ** 2 for v in c.values())
        if norm_sq < _TINY:
            # BO occasionally proposes an all-zero x. Fall back to a
            # trivial c-configuration (c_0 = 1, rest zero); this decodes
            # to the trivial form factor and downstream ED sees the
            # unmodulated LLL baseline. Loud enough for a caller to
            # notice via ρ_min = 1 in diagnostics.
            fallback = {k: complex(0.0, 0.0) for k in c}
            fallback[(0, 0)] = complex(1.0, 0.0)
            return fallback
        scale = 1.0 / np.sqrt(norm_sq)
        return {k: v * scale for k, v in c.items()}

    def _convolve(
        self, c: dict[tuple[int, int], complex]
    ) -> dict[tuple[int, int], complex]:
        """Compute ``w_G = Σ_K c_K c*_{K-G}`` for every G in ``self.vectors``."""

        W: dict[tuple[int, int], complex] = {}
        for G in self.vectors:
            acc = complex(0.0, 0.0)
            for K, c_K in c.items():
                partner = (K[0] - G[0], K[1] - G[1])
                c_KG = c.get(partner)
                if c_KG is None:
                    continue
                acc += c_K * c_KG.conjugate()
            W[G] = acc
        return W

    def decode(self, x: np.ndarray) -> dict[tuple[int, int], complex]:
        """Map real vector ``x`` → ``{w_G}`` via ``|h|² = |g|²``.

        Output guarantees (they follow from (★) in the class docstring):

        * ``w[(0, 0)] == 1 + 0j`` (from normalisation).
        * ``w[(-m, -n)] == conj(w[(m, n)])`` (Hermiticity).
        * The corresponding real-space density ``|h(r)|² ≥ 0`` at every
          ``r`` (positivity by construction).
        """

        x = np.asarray(x, dtype=float)
        c = self._pack_c(x)
        c = self._normalise(c)
        return self._convolve(c)

    # ------------------------------------------------------------------
    # Encode (least-squares; diagnostic only)
    # ------------------------------------------------------------------

    def encode(
        self,
        W: dict[tuple[int, int], complex],
        tol: float = 1e-9,
        max_iter: int = 2000,
        x0: np.ndarray | None = None,
    ) -> np.ndarray:
        """Approximate inverse of ``decode`` via least-squares.

        The c → w map is many-to-one (multiple ``{c_K}`` can produce the
        same ``{w_G}``). This solver runs L-BFGS-B on the residual
        ``||decode(x) − W_target||²`` and returns whatever local minimum
        it converges to. **For round-trip diagnostics only — do not use
        this on the proposer trajectory.**

        Raises ``ValueError`` if the residual exceeds ``tol`` after
        ``max_iter`` iterations.
        """

        from scipy.optimize import minimize  # local import: keep top-level cheap

        if set(W.keys()) != set(self.vectors):
            missing = set(self.vectors) - set(W)
            extra = set(W) - set(self.vectors)
            raise ValueError(
                f"W has wrong key set: missing {missing}, extra {extra}"
            )
        w_target = np.array(
            [complex(W[g]) for g in self.vectors], dtype=complex
        )

        def residual_vec(x: np.ndarray) -> np.ndarray:
            W_x = self.decode(x)
            return np.array([complex(W_x[g]) for g in self.vectors]) - w_target

        def loss(x: np.ndarray) -> float:
            r = residual_vec(x)
            return float(np.sum(r.real ** 2 + r.imag ** 2))

        # Warm start: c_0 = 1, other orbits small random. If the user
        # supplied an x0 (e.g., a previous fit), use it.
        if x0 is None:
            rng = np.random.default_rng(seed=0)
            x_init = 0.05 * rng.standard_normal(self.n_real_dof)
            x_init[0] = 1.0
        else:
            x_init = np.asarray(x0, dtype=float).copy()
            if x_init.shape != (self.n_real_dof,):
                raise ValueError(
                    f"x0 has shape {x_init.shape}; expected ({self.n_real_dof},)"
                )

        result = minimize(
            loss,
            x_init,
            method="L-BFGS-B",
            options={"maxiter": max_iter, "gtol": 1e-16, "ftol": 1e-16},
        )
        if result.fun > tol ** 2 * len(self.vectors):
            raise ValueError(
                f"encode: L-BFGS-B residual {np.sqrt(result.fun):.3e} exceeds "
                f"tolerance {tol:.3e} after {result.nit} iterations. "
                f"W may not be representable in the Cholesky subspace at "
                f"this n_c_shells={self.n_c_shells}."
            )
        return result.x

    def project(
        self, W: dict[tuple[int, int], complex]
    ) -> dict[tuple[int, int], complex]:
        """Project an arbitrary ``W`` onto the Cholesky-representable subset.

        Runs ``encode`` (least-squares) then ``decode``. Returns the
        best-effort Cholesky representative; the residual is silently
        absorbed.
        """

        x = self.encode(W, tol=np.inf)  # accept any residual
        return self.decode(x)


class PositiveDirectParameterizer:
    """Direct ``{w_G}`` with positivity imposed by radial projection.

    There are two other ways to keep ``|h(r)|² ≥ 0`` and neither is
    satisfactory for optimisation.

    - **Direct + rejection**: decode ``x``, and if the density goes
      negative resample ``x`` and try again.
      In 20 dimensions almost every draw is infeasible, and — worse — a resample
      *discards the proposer's point*, so a GP never sees the configuration it
      asked for.
    - **Cholesky** (``CholeskyParameterizer``): write ``|h|² = |g|²`` so positivity is
      automatic. It is automatic, but **incomplete**: at ``n_c_shells=3``,
      ``n_w_shells=8`` the reachable set is a **13-dimensional** subset of the
      **20-dimensional** space of C₃-symmetric Hermitian ``w_G`` at 8 shells.
      A search in that chart optimises inside a slice, and its optimum may be
      bounded by the parameterisation rather than by physics.

    This class removes both problems. Positivity is *linear* in ``w_G`` —
    ``ρ(r) = 1 + m(r)`` with ``m`` linear in the DOF vector — so the feasible set
    is a convex cone around the trivial density, and along any direction ``d̂``
    the density first touches zero at the closed-form radius

        t_max(d̂)  =  −1 / min_r m_d̂(r).

    We therefore read ``x`` as a direction *and* a radius: the direction is
    ``x/‖x‖`` and the radius is ``tanh(‖x‖)`` as a fraction of ``t_max``. This
    is a smooth bijection from ``ℝ^n \\ {0}`` onto the cone's interior, so

    - every proposal is feasible — no rejection, nothing discarded;
    - the full 20 DOF are reachable, not a 13-D slice;
    - ``x = 0`` is the trivial band and ``‖x‖ → ∞`` approaches the boundary,
      which is where the Cholesky-chart optimum actually sits (``ρ_min ≈ +0.004``).

    ``encode`` inverts the map, so a campaign can be seeded with an existing
    winner and a GP can train on the exact ``x`` it proposed.
    """

    #: ``‖x‖`` at which the radius reaches the positivity boundary. The proposers
    #: emit standard-normal coordinates, so ``‖x‖`` concentrates near ``√n ≈ 4.5``
    #: at 20 DOF and BO may roam to ``5√n``; ``R = 6`` puts a typical draw at
    #: ~0.75 of the boundary and makes the boundary itself reachable well inside
    #: the acquisition box. Radii beyond ``R`` clamp to the boundary — deliberate,
    #: since the Cholesky-chart optimum sits exactly there, and the clamped set is still a
    #: full (n−1)-sphere of distinct directions rather than a flat objective.
    BOUNDARY_RADIUS = 6.0
    #: mesh used to locate the positivity boundary, and the much finer mesh every
    #: decode is validated on. A coarse grid *over-estimates* ``min_r ρ`` because
    #: the true minimum falls between samples, and these densities are peaked
    #: (``ρ_max`` up to ~16), so the validation mesh has to be fine. It is cheap:
    #: on the integer-``G`` lattice the density is exactly an inverse FFT.
    BOUNDARY_MESH = 384
    #: absolute floor demanded of ``min_r ρ``. A grid minimum over-estimates the
    #: continuum minimum slightly, so leaving a small positive floor rather than
    #: landing exactly on ``ρ = 0`` buys a buffer that survives any finer
    #: re-check. Mean density is ``w_0 = 1``, so this is a relative floor too.
    POSITIVITY_MARGIN = 1e-3

    def __init__(self, n_shells: int, symmetry: SymmetryMode):
        self.base = FormFactorParameterizer(n_shells, symmetry)
        self.parameterisation = "direct_positive"
        self.n_shells = self.base.n_shells
        self.shells = self.base.shells
        self.vectors = self.base.vectors
        self.symmetry = symmetry

    @property
    def n_real_dof(self) -> int:
        """Same count as the plain direct map — the radius rides on ``‖x‖``."""

        return self.base.n_real_dof

    @staticmethod
    def density_grid(W: dict[tuple[int, int], complex], n_mesh: int) -> np.ndarray:
        """``ρ(r)`` on an ``n_mesh²`` grid, by inverse FFT.

        ``ρ(r_jk) = Σ_G w_G exp(2πi(m j + n k)/N)`` is exactly ``N²·ifft2`` of the
        coefficient array, which turns an ``O(n_G · N²)`` Python loop into an
        ``O(N² log N)`` array op — the reason a 192² validation grid is
        affordable. Agrees with :func:`evaluate_density_on_mesh` to round-off.
        """

        a = np.zeros((n_mesh, n_mesh), dtype=complex)
        for (m, n), w in W.items():
            a[m % n_mesh, n % n_mesh] += w
        return np.real(np.fft.ifft2(a) * (n_mesh * n_mesh))

    def _modulation(self, dof: np.ndarray, n_mesh: int) -> np.ndarray:
        """``m(r) = ρ(r) − 1`` on an ``n_mesh²`` grid, linear in ``dof``."""

        W = self.base.decode(np.asarray(dof, dtype=float))
        W = {g: (v - 1.0 if g == (0, 0) else v) for g, v in W.items()}
        return self.density_grid(W, n_mesh)

    def t_max(self, direction: np.ndarray, n_mesh: int | None = None) -> float:
        """Radius at which ``ρ`` first touches zero along ``direction``.

        ``m`` is zero-mean, so ``min_r m < 0`` for any non-trivial direction and
        ``ρ = 1 + t·m`` vanishes at ``t = −1/min_r m``.
        """

        m_min = float(np.min(self._modulation(direction, n_mesh or self.BOUNDARY_MESH)))
        if m_min >= -1e-15:
            return float("inf")
        return -1.0 / m_min

    def decode(self, x: np.ndarray) -> dict[tuple[int, int], complex]:
        x = np.asarray(x, dtype=float)
        if x.shape != (self.n_real_dof,):
            raise ValueError(f"x has shape {x.shape}; expected ({self.n_real_dof},)")

        norm = float(np.linalg.norm(x))
        if norm < 1e-12:
            return self.base.decode(np.zeros(self.n_real_dof))    # trivial band

        unit = x / norm
        t_max = self.t_max(unit)
        if not np.isfinite(t_max):
            return self.base.decode(np.zeros(self.n_real_dof))

        # rho = 1 + t·m with min_r m = -1/t_max, so min_r rho = 1 - t/t_max.
        # Demanding min_r rho >= margin gives the admissible radius in closed
        # form -- no search, no shrink loop, and the boundary is hit exactly.
        frac = min(norm / self.BOUNDARY_RADIUS, 1.0)
        return self.base.decode(frac * (1.0 - self.POSITIVITY_MARGIN) * t_max * unit)

    def encode(self, W: dict[tuple[int, int], complex], tol: float = 1e-9) -> np.ndarray:
        """Invert :meth:`decode` — the ``x`` whose decode reproduces ``W``.

        Lets a campaign seed itself with a known winner and lets the GP train on
        the exact proposed vector rather than a lossy inversion.
        """

        dof = self.base.encode(W, tol=tol)
        t = float(np.linalg.norm(dof))
        if t < 1e-12:
            return np.zeros(self.n_real_dof)
        unit = dof / t
        t_max = self.t_max(unit)
        if not np.isfinite(t_max):
            return np.zeros(self.n_real_dof)
        frac = float(np.clip(t / ((1.0 - self.POSITIVITY_MARGIN) * t_max), 0.0, 1.0))
        return unit * (self.BOUNDARY_RADIUS * frac)
