"""Gates for the seed-plus-deformation chart.

These are the checks to pass before any optimization, restricted to the
part that lives in Python: the cross-momentum kernel itself. The gates that
contract the kernel against the LL overlap — ``S(k) > 0``, the Gram-matrix
condition, and small-cluster spectra — need the solver and are not tested here.
"""

from __future__ import annotations

import numpy as np
import pytest

from mosaic.physics.form_factor import evaluate_density_on_mesh
from mosaic.physics.kdep_envelope import (
    DeformationSpec,
    density_on_mesh,
    gamma_on_mesh,
    kernel_coefficients,
    kernel_matrix_at_r,
    star_function_k,
    star_function_r,
)

# One inversion-symmetric hexagonal star and one direct-lattice star.
STAR_G = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1))
STAR_R = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1))


def seed_w0(amp: float = 0.08) -> dict[tuple[int, int], complex]:
    """A Hermitian static seed: uniform real weight on the first shell."""
    w0: dict[tuple[int, int], complex] = {(0, 0): 1.0 + 0j}
    for g in STAR_G:
        w0[g] = amp + 0j
    return w0


def spec(alpha: float = 0.0, beta: float = 0.0) -> DeformationSpec:
    return DeformationSpec(
        spatial_stars=(STAR_G,),
        momentum_stars=(STAR_R,),
        alpha=np.array([[alpha]]),
        beta=np.array([[beta]]),
    )


# --- star functions ---------------------------------------------------------


def test_star_functions_are_real_and_zero_mean():
    o = star_function_r(STAR_G, n_mesh=24)
    assert o.dtype == np.float64
    assert abs(o.mean()) < 1e-12
    # unit mean square on its own torus
    assert np.isclose((o**2).mean(), 1.0, atol=1e-12)


def test_momentum_star_is_real():
    for k in [(0.0, 0.0), (0.3, 0.1), (0.5, 0.5)]:
        f = star_function_k(STAR_R, k)
        assert isinstance(f, float)


def test_star_must_be_inversion_symmetric():
    with pytest.raises(ValueError, match="not inversion-symmetric"):
        DeformationSpec(
            spatial_stars=(((1, 0), (0, 1)),),
            momentum_stars=(STAR_R,),
            alpha=np.zeros((1, 1)),
            beta=np.zeros((1, 1)),
        )


def test_zero_mode_is_rejected_as_redundant():
    with pytest.raises(ValueError, match="redundant overall scalar"):
        DeformationSpec(
            spatial_stars=(((0, 0),),),
            momentum_stars=(STAR_R,),
            alpha=np.zeros((1, 1)),
            beta=np.zeros((1, 1)),
        )


# --- gate: the static limit is exact ----------------------------------------


def test_density_matches_the_existing_evaluator():
    """The FFT convention agrees with physics.form_factor."""
    w0 = seed_w0()
    n = 21
    ours = density_on_mesh(w0, n)
    theirs = evaluate_density_on_mesh(w0, n)
    assert np.allclose(ours.real, theirs, atol=1e-12)
    assert np.max(np.abs(ours.imag)) < 1e-12


@pytest.mark.parametrize("deformation", [None, spec(0.0, 0.0)])
def test_gamma_zero_reproduces_the_seed_exactly(deformation):
    """At gamma = 0, W_G = w^(0)_G exactly."""
    w0 = seed_w0()
    got = kernel_coefficients(w0, deformation, (0.2, 0.1), (0.4, -0.3), n_mesh=32, g_cutoff=2)
    for g, want in w0.items():
        assert abs(got[g] - want) < 1e-12, f"G={g}"
    # and nothing else is generated
    for g, val in got.items():
        if g not in w0:
            assert abs(val) < 1e-12, f"spurious harmonic at G={g}: {val}"


def test_static_kernel_is_momentum_independent():
    w0 = seed_w0()
    a = kernel_coefficients(w0, None, (0.0, 0.0), (0.0, 0.0), n_mesh=32, g_cutoff=2)
    b = kernel_coefficients(w0, None, (0.31, -0.17), (0.05, 0.44), n_mesh=32, g_cutoff=2)
    for g in a:
        assert abs(a[g] - b[g]) < 1e-12


# --- gate 2: Hermiticity and representability -------------------------------


def test_kernel_hermiticity_relation():
    """W_G(k,k')* = W_{-G}(k',k)  --  the *ordered-pair-swapped* relation."""
    w0 = seed_w0()
    s = spec(alpha=0.3, beta=0.2)
    k, kp = (0.13, 0.29), (-0.37, 0.08)
    fwd = kernel_coefficients(w0, s, k, kp, n_mesh=48, g_cutoff=3)
    bwd = kernel_coefficients(w0, s, kp, k, n_mesh=48, g_cutoff=3)
    for g, val in fwd.items():
        mg = (-g[0], -g[1])
        assert abs(np.conjugate(val) - bwd[mg]) < 1e-10, f"G={g}"


def test_the_stronger_same_ordered_pair_relation_is_false():
    """W_G(k,k')* = W_{-G}(k,k') must not be imposed. Show it fails."""
    w0 = seed_w0()
    s = spec(alpha=0.0, beta=0.35)
    k, kp = (0.13, 0.29), (-0.37, 0.08)
    fwd = kernel_coefficients(w0, s, k, kp, n_mesh=48, g_cutoff=3)
    worst = max(
        abs(np.conjugate(v) - fwd.get((-g[0], -g[1]), 0j)) for g, v in fwd.items()
    )
    assert worst > 1e-3, "expected the same-ordered-pair relation to be violated"


def test_diagonal_kernel_is_a_real_density():
    """W_G(k,k) are the density harmonics of |h_k|^2, hence Hermitian in G."""
    w0 = seed_w0()
    s = spec(alpha=0.4, beta=0.25)
    k = (0.22, -0.11)
    diag = kernel_coefficients(w0, s, k, k, n_mesh=48, g_cutoff=4)
    for g, val in diag.items():
        mg = (-g[0], -g[1])
        assert abs(val - np.conjugate(diag[mg])) < 1e-10, f"G={g}"
    assert abs(diag[(0, 0)].imag) < 1e-12


def test_momentum_matrix_is_rank_one_and_psd():
    """At fixed r the matrix over momenta is rank-<=1 positive."""
    w0 = seed_w0()
    s = spec(alpha=0.3, beta=0.4)
    ks = [(0.0, 0.0), (0.2, 0.1), (-0.3, 0.25), (0.45, -0.4)]
    m = kernel_matrix_at_r(w0, s, ks, n_mesh=16)
    # sample a few real-space points
    for i, j in [(0, 0), (3, 7), (11, 2)]:
        block = m[i, j]
        assert np.allclose(block, block.conj().T, atol=1e-10)
        ev = np.linalg.eigvalsh(block)
        assert ev.min() > -1e-9, f"not PSD at r=({i},{j}): {ev}"
        # rank one: only the top eigenvalue survives
        assert ev[-1] > 1e-9
        assert ev[-2] / ev[-1] < 1e-9, f"not rank one at r=({i},{j}): {ev}"


def test_kernel_matches_direct_real_space_quadrature():
    """Independent check of the FFT against a literal Riemann sum."""
    w0 = seed_w0()
    s = spec(alpha=0.25, beta=0.15)
    k, kp = (0.1, -0.2), (0.35, 0.05)
    n = 32
    got = kernel_coefficients(w0, s, k, kp, n_mesh=n, g_cutoff=1)

    rho = density_on_mesh(w0, n)
    field = rho * np.exp(
        np.conjugate(gamma_on_mesh(s, k, n)) + gamma_on_mesh(s, kp, n)
    )
    idx = np.arange(n)
    for g in [(0, 0), (1, 0), (-1, 1)]:
        phase = 2.0 * np.pi * (g[0] * idx[:, None] + g[1] * idx[None, :]) / n
        want = (field * np.exp(-1j * phase)).sum() / (n * n)
        assert abs(got[g] - want) < 1e-12, f"G={g}"


# --- gate 3: momentum gauge covariance --------------------------------------


def test_bloch_gauge_covariance():
    """gamma -> gamma + i chi(k)  =>  W_G -> exp(i[chi(k') - chi(k)]) W_G.

    A momentum-only phase is pure Bloch gauge: it multiplies the whole kernel by
    a scalar and changes no observable.
    """
    w0 = seed_w0()
    s = spec(alpha=0.2, beta=0.3)
    k, kp = (0.18, -0.24), (0.41, 0.09)
    base = kernel_coefficients(w0, s, k, kp, n_mesh=48, g_cutoff=3)

    # chi(k) implemented as a spatially constant shift of gamma
    chi_k, chi_kp = 0.7, -1.3
    rho = density_on_mesh(w0, 48)
    field = rho * np.exp(
        np.conjugate(gamma_on_mesh(s, k, 48) + 1j * chi_k)
        + gamma_on_mesh(s, kp, 48)
        + 1j * chi_kp
    )
    shifted = np.fft.fft2(field) / (48 * 48)
    expected_factor = np.exp(1j * (chi_kp - chi_k))
    for g, val in base.items():
        m, n = g[0] % 48, g[1] % 48
        assert abs(shifted[m, n] - expected_factor * val) < 1e-10, f"G={g}"


# --- gate 4: phase-only deformation ------------------------------------------


def test_phase_only_leaves_the_diagonal_density_untouched():
    """Phase-only gate: unchanged diagonal density and norm, changed off-diagonal."""
    w0 = seed_w0()
    s = spec(alpha=0.0, beta=0.5)
    k, kp = (0.15, 0.35), (-0.25, 0.1)

    diag = kernel_coefficients(w0, s, k, k, n_mesh=48, g_cutoff=2)
    for g, want in w0.items():
        assert abs(diag[g] - want) < 1e-12, f"diagonal changed at G={g}"

    off = kernel_coefficients(w0, s, k, kp, n_mesh=48, g_cutoff=2)
    changed = max(abs(off[g] - w0.get(g, 0j)) for g in off)
    assert changed > 1e-3, "phase-only deformation left the off-diagonal unchanged"


def test_amplitude_only_changes_the_diagonal():
    """The complementary direction: alpha does move the density."""
    w0 = seed_w0()
    s = spec(alpha=0.5, beta=0.0)
    k = (0.15, 0.35)
    diag = kernel_coefficients(w0, s, k, k, n_mesh=48, g_cutoff=2)
    changed = max(abs(diag[g] - w0.get(g, 0j)) for g in diag)
    assert changed > 1e-3


# --- the nodal seed the old framework wrongly excluded -----------------------


def test_a_nodal_seed_is_handled_without_special_casing():
    """Real-space zeros are admissible. The chart never divides by h_*.

    ``rho_*(r) = 1 - cos(G.r)`` on a one-mode seed touches exactly zero, which
    the old pointwise-non-vanishing rule would have excluded. Here it is an
    ordinary input, and gamma = 0 still reproduces it exactly.
    """
    w0 = {(0, 0): 1.0 + 0j, (1, 0): -0.5 + 0j, (-1, 0): -0.5 + 0j}
    rho = density_on_mesh(w0, 48).real
    assert rho.min() < 1e-12, "seed should touch zero"
    assert rho.min() > -1e-12, "seed should not go negative"

    got = kernel_coefficients(w0, spec(0.3, 0.2), (0.0, 0.0), (0.0, 0.0), n_mesh=64, g_cutoff=1)
    # diagonal at equal momenta is still a real non-negative density
    assert abs(got[(0, 0)].imag) < 1e-12
    static = kernel_coefficients(w0, None, (0.1, 0.2), (0.3, 0.4), n_mesh=64, g_cutoff=1)
    for g, want in w0.items():
        assert abs(static[g] - want) < 1e-12


def test_exponentiation_generates_harmonics_beyond_the_seed():
    """A finite expansion of log h is not a finite expansion of h.

    A cost estimate that assumes otherwise is wrong; this is the measurement that
    shows why the cost must be benchmarked instead.
    """
    w0 = seed_w0()
    s = spec(alpha=0.6, beta=0.0)
    k = (0.1, 0.2)
    got = kernel_coefficients(w0, s, k, k, n_mesh=64, g_cutoff=4)
    far = [abs(v) for g, v in got.items() if max(abs(g[0]), abs(g[1])) >= 3]
    assert max(far) > 1e-8, "expected exponentiation to populate higher shells"


def test_n_mesh_convergence():
    """The kernel must be converged in the real-space grid, not the seed shells."""
    w0 = seed_w0()
    s = spec(alpha=0.4, beta=0.3)
    k, kp = (0.1, 0.2), (0.3, -0.1)
    a = kernel_coefficients(w0, s, k, kp, n_mesh=48, g_cutoff=2)
    b = kernel_coefficients(w0, s, k, kp, n_mesh=96, g_cutoff=2)
    worst = max(abs(a[g] - b[g]) for g in a)
    assert worst < 1e-9, f"not converged at n_mesh=48: {worst:.3e}"
