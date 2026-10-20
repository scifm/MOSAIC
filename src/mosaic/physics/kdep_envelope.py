"""Momentum-dependent envelopes: the seed-plus-deformation chart.

The trial envelope is an existing *static* seed times an exponential
deformation,

    h_k(r) = h_*(r) exp(gamma(k, r)),

and the object the ED consumes is the cross-momentum kernel

    h_k^*(r) h_k'(r) = sum_G W_G(k, k') exp(i G . r).

Because ``h_*^* h_* = rho_*`` is exactly the density the static search already
optimises, the kernel is

    W_G(k, k') = F_G{ rho_*(r) exp(gamma(k, r)^* + gamma(k', r)) },

which needs only ``rho_*``. Nothing here takes ``sqrt(rho_*)`` or ``log(rho_*)``,
chooses a static phase, or requires a Cholesky representation — that is the whole
point of the chart, and it is why a seed sitting on (or at) a density zero is
usable as-is.

At ``gamma = 0`` the kernel collapses to the static coefficients exactly, so the
existing model is the origin of the new search space.

Conventions match `physics.form_factor.evaluate_density_on_mesh`: ``G`` is an
integer pair ``(m, n)`` and ``G . r = 2*pi*(m*i + n*j)/n_mesh`` on the real-space
mesh. Momenta are fractional BZ coordinates ``k = (k1, k2)`` with
``k . R = 2*pi*(k1*R1 + k2*R2)`` for an integer direct-lattice vector ``R``.

The Chern number is preserved when the *state norm*
``S(k) > 0``, not when ``h_k(r)`` is pointwise non-vanishing. ``S(k)`` contracts
this kernel against the LL overlap and therefore lives on the solver side.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

__all__ = [
    "DeformationSpec",
    "star_function_r",
    "star_function_k",
    "gamma_on_mesh",
    "density_on_mesh",
    "kernel_coefficients",
    "kernel_matrix_at_r",
]


@dataclass(frozen=True)
class DeformationSpec:
    """A ``2*J*P``-real-parameter deformation ``gamma(k, r)``.

    ``gamma(k, r) = sum_{s,p} (alpha[s,p]/2 + i beta[s,p]) O_s(r) F_p(k)``

    with ``O_s`` and ``F_p`` the real, zero-mean, unit-mean-square star
    functions (``star_function_r``, ``star_function_k``). ``alpha`` drives amplitude,
    ``beta`` drives phase; test these separately before jointly.

    Attributes
    ----------
    spatial_stars : tuple of tuple of (int, int)
        Each entry is one inversion-symmetric reciprocal star ``S_s``, listed as
        integer ``G`` pairs. Must not contain ``(0, 0)`` — the zero mode is a
        redundant overall scalar.
    momentum_stars : tuple of tuple of (int, int)
        Each entry is one inversion-symmetric direct-lattice star ``T_p``,
        listed as integer ``R`` pairs. Must not contain ``(0, 0)``.
    alpha, beta : np.ndarray of shape (J, P), real
        Deformation coefficients. All-zero recovers the static model exactly.
    """

    spatial_stars: tuple[tuple[tuple[int, int], ...], ...]
    momentum_stars: tuple[tuple[tuple[int, int], ...], ...]
    alpha: np.ndarray
    beta: np.ndarray

    def __post_init__(self) -> None:
        j, p = len(self.spatial_stars), len(self.momentum_stars)
        if j == 0 or p == 0:
            raise ValueError("DeformationSpec needs at least one spatial and one momentum star")
        for name, arr in (("alpha", self.alpha), ("beta", self.beta)):
            a = np.asarray(arr)
            if a.shape != (j, p):
                raise ValueError(f"{name} has shape {a.shape}, expected {(j, p)}")
            if not np.isrealobj(a):
                raise ValueError(f"{name} must be real; got dtype {a.dtype}")
        for star in self.spatial_stars:
            _validate_star(star, "spatial")
        for star in self.momentum_stars:
            _validate_star(star, "momentum")

    @property
    def n_params(self) -> int:
        """Number of real search parameters (``2*J*P``)."""
        return 2 * len(self.spatial_stars) * len(self.momentum_stars)

    def is_zero(self) -> bool:
        """True iff this is the static model."""
        return not (np.any(self.alpha) or np.any(self.beta))

    def to_block(self, *, n_mesh: int = 48, g_cutoff: int | None = None) -> dict:
        """The ``form_factor.deformation`` block of the ED input.

        Plain JSON-serialisable dict matching ``ed.contract.DeformationBlock``;
        the Julia solver rebuilds exactly this kernel from it.
        """

        block = {
            "spatial_stars": [[list(g) for g in star] for star in self.spatial_stars],
            "momentum_stars": [[list(r) for r in star] for star in self.momentum_stars],
            "alpha": np.asarray(self.alpha, dtype=float).tolist(),
            "beta": np.asarray(self.beta, dtype=float).tolist(),
            "n_mesh": int(n_mesh),
        }
        if g_cutoff is not None:
            block["g_cutoff"] = int(g_cutoff)
        return block

    @classmethod
    def from_block(cls, block: dict) -> "DeformationSpec":
        """Inverse of :meth:`to_block` (``n_mesh``/``g_cutoff`` are not part of the spec)."""

        return cls(
            spatial_stars=tuple(tuple((int(a), int(b)) for a, b in star) for star in block["spatial_stars"]),
            momentum_stars=tuple(tuple((int(a), int(b)) for a, b in star) for star in block["momentum_stars"]),
            alpha=np.asarray(block["alpha"], dtype=float),
            beta=np.asarray(block["beta"], dtype=float),
        )


def _validate_star(star: tuple[tuple[int, int], ...], kind: str) -> None:
    """Reject stars that would make the star function complex or redundant.

    Fails loudly rather than silently symmetrising: a star that is not closed
    under inversion gives a complex ``O_s`` / ``F_p``, which silently changes
    the meaning of ``alpha`` and ``beta``.
    """

    if len(star) == 0:
        raise ValueError(f"empty {kind} star")
    members = set(star)
    if len(members) != len(star):
        raise ValueError(f"{kind} star has repeated members: {star}")
    if (0, 0) in members:
        raise ValueError(
            f"{kind} star contains the zero mode; it is a redundant overall "
            "scalar and must be excluded from the deformation block"
        )
    for a, b in star:
        if (-a, -b) not in members:
            raise ValueError(
                f"{kind} star is not inversion-symmetric: {(a, b)} present but "
                f"{(-a, -b)} absent, so the star function would be complex"
            )


def star_function_r(
    star: tuple[tuple[int, int], ...],
    n_mesh: int,
) -> np.ndarray:
    """``O_s(r) = d_s^{-1/2} sum_{G in S_s} exp(i G . r)`` on the real mesh.

    Returns
    -------
    np.ndarray of shape (n_mesh, n_mesh), real
    """

    i = np.arange(n_mesh)
    out = np.zeros((n_mesh, n_mesh), dtype=complex)
    for m, n in star:
        phase = 2.0 * np.pi * (m * i[:, None] + n * i[None, :]) / n_mesh
        out += np.exp(1j * phase)
    out /= np.sqrt(len(star))
    _assert_real(out, "spatial star function O_s")
    return out.real


def star_function_k(
    star: tuple[tuple[int, int], ...],
    k: tuple[float, float],
) -> float:
    """``F_p(k) = d_p^{-1/2} sum_{R in T_p} exp(i k . R)`` at one momentum.

    ``k`` is in fractional BZ coordinates, so ``k . R = 2*pi*(k1*R1 + k2*R2)``.
    """

    total = 0.0 + 0.0j
    for r1, r2 in star:
        total += np.exp(2j * np.pi * (k[0] * r1 + k[1] * r2))
    total /= np.sqrt(len(star))
    _assert_real(np.asarray(total), "momentum star function F_p")
    return float(total.real)


def _assert_real(arr: np.ndarray, what: str) -> None:
    worst = float(np.max(np.abs(arr.imag)))
    if worst > 1e-10:
        raise ValueError(f"{what} is not real (max |imag| = {worst:.3e})")


def gamma_on_mesh(
    spec: DeformationSpec,
    k: tuple[float, float],
    n_mesh: int,
) -> np.ndarray:
    """``gamma(k, r)`` on the real-space mesh, as a complex array.

    Returns
    -------
    np.ndarray of shape (n_mesh, n_mesh), complex
    """

    o_r = [star_function_r(s, n_mesh) for s in spec.spatial_stars]
    f_k = [star_function_k(t, k) for t in spec.momentum_stars]
    out = np.zeros((n_mesh, n_mesh), dtype=complex)
    for s, o in enumerate(o_r):
        for p, f in enumerate(f_k):
            coef = 0.5 * spec.alpha[s, p] + 1j * spec.beta[s, p]
            out += coef * o * f
    return out


def density_on_mesh(
    w0: dict[tuple[int, int], complex],
    n_mesh: int,
) -> np.ndarray:
    """``rho_*(r) = sum_L w0[L] exp(i L . r)`` via an inverse FFT.

    Equivalent to ``physics.form_factor.evaluate_density_on_mesh`` but keeps the
    complex result, because this is an intermediate of the kernel construction
    rather than a density to be validated. Hermiticity of ``w0`` is the caller's
    responsibility and is checked by the kernel builder.
    """

    grid = np.zeros((n_mesh, n_mesh), dtype=complex)
    for (m, n), w in w0.items():
        grid[m % n_mesh, n % n_mesh] += w
    return np.fft.ifft2(grid) * (n_mesh * n_mesh)


def kernel_coefficients(
    w0: dict[tuple[int, int], complex],
    spec: DeformationSpec | None,
    k_bra: tuple[float, float],
    k_ket: tuple[float, float],
    *,
    n_mesh: int = 48,
    g_cutoff: int | None = None,
) -> dict[tuple[int, int], complex]:
    """``W_G(k, k')`` for one momentum pair.

    Computes ``rho_*(r) * exp(gamma(k,r)^* + gamma(k',r))`` on an
    ``n_mesh x n_mesh`` grid and returns its Fourier coefficients.

    Parameters
    ----------
    w0 : dict
        Static seed density coefficients ``w^(0)_L``, indexed by integer ``L``.
        Must be Hermitian (``w_{-L} = w_L^*``) and contain ``(0, 0)``.
    spec : DeformationSpec or None
        The deformation. ``None`` (or an all-zero spec) is the static model, and
        then the returned coefficients equal ``w0`` exactly, up to the mesh
        aliasing of harmonics outside the grid.
    k_bra, k_ket : (float, float)
        Fractional BZ coordinates of ``k`` and ``k'``.
    n_mesh : int
        Real-space grid. Exponentiation generates harmonics beyond those of
        ``gamma``, so this must be converged independently — it is not
        set by the seed's shell count.
    g_cutoff : int or None
        If given, drop coefficients with ``max(|m|, |n|) > g_cutoff``.

    Returns
    -------
    dict mapping integer ``G`` to complex ``W_G(k, k')``.

    Notes
    -----
    The returned table satisfies ``W_G(k,k')^* = W_{-G}(k',k)`` by construction.
    The *stronger* relation with the same ordered pair on the right is generally
    false and must not be imposed.
    """

    if (0, 0) not in w0:
        raise ValueError("w0 must contain the (0, 0) coefficient")
    _check_hermitian(w0)
    if n_mesh < 2:
        raise ValueError(f"n_mesh must be >= 2, got {n_mesh}")

    field = density_on_mesh(w0, n_mesh)
    if spec is not None and not spec.is_zero():
        g_bra = gamma_on_mesh(spec, k_bra, n_mesh)
        g_ket = gamma_on_mesh(spec, k_ket, n_mesh)
        field = field * np.exp(np.conjugate(g_bra) + g_ket)

    coeffs = np.fft.fft2(field) / (n_mesh * n_mesh)

    out: dict[tuple[int, int], complex] = {}
    half = n_mesh // 2
    for m in range(n_mesh):
        for n in range(n_mesh):
            # map FFT bin to the signed integer G in (-half, half]
            gm = m - n_mesh if m > half else m
            gn = n - n_mesh if n > half else n
            if g_cutoff is not None and max(abs(gm), abs(gn)) > g_cutoff:
                continue
            val = complex(coeffs[m, n])
            if val != 0:
                out[(gm, gn)] = val
    return out


def _check_hermitian(w0: dict[tuple[int, int], complex], tol: float = 1e-9) -> None:
    for g, w in w0.items():
        mg = (-g[0], -g[1])
        if mg not in w0:
            raise ValueError(f"w0 is not Hermitian: {g} present but {mg} absent")
        if abs(w - np.conjugate(w0[mg])) > tol:
            raise ValueError(
                f"w0 is not Hermitian at {g}: {w!r} vs conj({w0[mg]!r})"
            )


def kernel_matrix_at_r(
    w0: dict[tuple[int, int], complex],
    spec: DeformationSpec | None,
    k_list: list[tuple[float, float]],
    *,
    n_mesh: int = 48,
) -> np.ndarray:
    """The momentum matrix ``M_ij(r) = h_{k_i}^*(r) h_{k_j}(r)`` on the mesh.

    Used by the representability gate: at every ``r`` this matrix must be
    rank-at-most-one and positive semidefinite. Building it from the
    envelope makes that automatic, so a *failure* here indicates a bug in the
    chart rather than a rejected configuration — which is exactly what makes it
    a useful test.

    Returns
    -------
    np.ndarray of shape (n_mesh, n_mesh, len(k_list), len(k_list)), complex
    """

    rho = density_on_mesh(w0, n_mesh)
    n_k = len(k_list)
    gammas = [
        np.zeros((n_mesh, n_mesh), dtype=complex)
        if spec is None or spec.is_zero()
        else gamma_on_mesh(spec, k, n_mesh)
        for k in k_list
    ]
    out = np.empty((n_mesh, n_mesh, n_k, n_k), dtype=complex)
    for i in range(n_k):
        for j in range(n_k):
            out[:, :, i, j] = rho * np.exp(np.conjugate(gammas[i]) + gammas[j])
    return out


# Solver geometry (MoireSolver.triangular_lattice): G1 along x, G2 at
# 120°, |G1| |G2| sin 120° = 2π (one flux quantum per cell, l_B = 1).
_G_LEN = float(np.sqrt(2 * np.pi / np.sin(2 * np.pi / 3)))
_G1 = np.array([_G_LEN, 0.0])
_G2 = _G_LEN * np.array([-0.5, np.sqrt(3) / 2])


def ll0_norm(
    w0: dict[tuple[int, int], complex],
    spec: DeformationSpec | None,
    k_frac: tuple[float, float],
    *,
    n_mesh: int = 48,
    g_cutoff: int | None = None,
) -> float:
    """The LL0 diagonal of the raw Gram matrix, ``S_00(k)``.

    ``S_00(k) = sum_G eta_G W_G(k,k) exp(-i k x G - |G|^2/4)`` — the solver's
    ``raw_overlap_at_k_mn(k, 0, 0)`` (zero-transfer raw form factor), with the
    k-dependent coefficients ``W_G(k,k)`` of the deformation kernel. For a pure
    LL0 band this is the norm whose positivity and conditioning define an
    admissible envelope. ``k_frac`` is in fractional
    reciprocal coordinates, ``k = f1 G1 + f2 G2``.

    ``g_cutoff`` defaults to the seed's own box (``max |m|, |n|`` over ``w0``),
    as the solver's ``DeformationKernel`` does.
    """

    if g_cutoff is None:
        g_cutoff = max(max(abs(m), abs(n)) for m, n in w0)
    if spec is None or spec.is_zero():
        w = w0
    else:
        w = kernel_coefficients(w0, spec, k_frac, k_frac, n_mesh=n_mesh, g_cutoff=g_cutoff)
    k = k_frac[0] * _G1 + k_frac[1] * _G2
    s = 0j
    for (m, n), wg in w.items():
        g = m * _G1 + n * _G2
        eta = 1.0 if (m % 2 == 0 and n % 2 == 0) else -1.0
        s += eta * wg * np.exp(-1j * (k[0] * g[1] - k[1] * g[0]) - 0.25 * (g @ g))
    if abs(s.imag) > 1e-9 * max(1.0, abs(s.real)):
        raise ValueError(f"S_00(k) is not real at k = {k_frac}: {s}")
    return float(s.real)


def _gamma_batch(spec: DeformationSpec, k_list: np.ndarray, n_mesh: int) -> np.ndarray:
    """``gamma(k, r)`` for many momenta at once: shape (len(k_list), n_mesh, n_mesh)."""

    o_r = np.stack([star_function_r(s, n_mesh) for s in spec.spatial_stars])          # (J, n, n)
    f_k = np.stack([
        np.real(np.exp(2j * np.pi * (k_list @ np.asarray(t, dtype=float).T)).sum(axis=1)) / np.sqrt(len(t))
        for t in spec.momentum_stars], axis=1)                                         # (K, P)
    coef = 0.5 * np.asarray(spec.alpha, dtype=float) + 1j * np.asarray(spec.beta, dtype=float)  # (J, P)
    return np.einsum("kp,jp,jxy->kxy", f_k, coef, o_r)


def ll0_norm_batch(
    w0: dict[tuple[int, int], complex],
    spec: DeformationSpec | None,
    k_list: list[tuple[float, float]],
    *,
    n_mesh: int = 48,
    g_cutoff: int | None = None,
) -> np.ndarray:
    """``ll0_norm`` for many momenta in one batched FFT (same conventions, same
    harmonic selection; agrees with ``ll0_norm`` to rounding). Shape (len(k_list),)."""

    if g_cutoff is None:
        g_cutoff = max(max(abs(m), abs(n)) for m, n in w0)
    ks = np.asarray(k_list, dtype=float)
    if spec is None or spec.is_zero():
        harm = list(w0.items())
        gm = np.array([g for g, _ in harm], dtype=float)
        coeffs = np.tile(np.array([v for _, v in harm]), (len(ks), 1))
    else:
        rho = density_on_mesh(w0, n_mesh)
        field = rho[None] * np.exp(2 * np.real(_gamma_batch(spec, ks, n_mesh)))
        c = np.fft.fft2(field, axes=(1, 2)) / (n_mesh * n_mesh)
        half = n_mesh // 2
        signed = np.array([m - n_mesh if m > half else m for m in range(n_mesh)])
        sel = [(m, n) for m in range(n_mesh) for n in range(n_mesh)
               if max(abs(signed[m]), abs(signed[n])) <= g_cutoff]
        idx = np.array(sel)
        gm = np.stack([signed[idx[:, 0]], signed[idx[:, 1]]], axis=1).astype(float)
        coeffs = c[:, idx[:, 0], idx[:, 1]]                                              # (K, H)
    g = gm[:, 0, None] * _G1[None] + gm[:, 1, None] * _G2[None]                         # (H, 2)
    eta = np.where((gm[:, 0] % 2 == 0) & (gm[:, 1] % 2 == 0), 1.0, -1.0)
    kc = ks[:, 0, None] * _G1[None] + ks[:, 1, None] * _G2[None]                        # (K, 2)
    cross = kc[:, 0, None] * g[None, :, 1] - kc[:, 1, None] * g[None, :, 0]             # (K, H)
    s = (coeffs * eta[None] * np.exp(-1j * cross - 0.25 * (g * g).sum(axis=1)[None])).sum(axis=1)
    if np.max(np.abs(s.imag)) > 1e-9 * max(1.0, float(np.max(np.abs(s.real)))):
        raise ValueError("S_00(k) is not real")
    return s.real


def m2_k_batch(w0: dict[tuple[int, int], complex], spec: DeformationSpec | None, n_mesh: int,
               k_list: list[tuple[float, float]]) -> float:
    """``<<rho_k(r)^2>_uc>_BZ`` with ``rho_k = |h_k|^2 / <|h_k|^2>_uc``, batched."""

    rho = np.real(density_on_mesh(w0, n_mesh))
    if spec is None or spec.is_zero():
        r = rho / rho.mean()
        return float((r ** 2).mean())
    hk = rho[None] * np.exp(2 * np.real(_gamma_batch(spec, np.asarray(k_list, dtype=float), n_mesh)))
    r = hk / hk.mean(axis=(1, 2), keepdims=True)
    return float((r ** 2).mean())
