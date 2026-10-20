"""Form factor: parameterizer DOF counts, decode/encode
round-trip, Hermiticity, fixed ``w_0 = 1``, density positivity check."""

from __future__ import annotations

import numpy as np
import pytest

from mosaic.physics.form_factor import (
    FormFactorParameterizer,
    W0_FIXED,
    evaluate_density_on_mesh,
    is_hermitian,
    min_density_on_mesh,
)
from mosaic.physics.lattice import enumerate_shells, flat_vectors


# ----- DOF counts (density model; C3_hard / none symmetry modes) -----


def test_dof_count_C3_shell1():
    p = FormFactorParameterizer(n_shells=1, symmetry="C3_hard")
    # w_0 is fixed (0 DOFs) + 1 complex orbit-pair = 2 real DOFs
    assert p.n_real_dof == 2


def test_dof_count_none_shell1():
    p = FormFactorParameterizer(n_shells=1, symmetry="none")
    # 6 nearest-shell vectors → 3 inversion pairs → 3 complex DOFs = 6 real
    assert p.n_real_dof == 6


def test_dof_count_C3_shell2():
    """Shell-1 + shell-2, both with 6 vectors / 2 C_3 orbits each
    paired by inversion: 1 complex DOF per shell × 2 shells = 4 real."""

    p = FormFactorParameterizer(n_shells=2, symmetry="C3_hard")
    assert p.n_real_dof == 4


def test_dof_count_shell0():
    """No DOFs when only the trivial shell is present (w_0 is fixed)."""

    p = FormFactorParameterizer(n_shells=0, symmetry="C3_hard")
    assert p.n_real_dof == 0


# ----- decode / encode round-trip -----


@pytest.mark.parametrize("symmetry", ["C3_hard", "none"])
@pytest.mark.parametrize("n_shells", [0, 1, 2])
def test_decode_encode_round_trip(symmetry, n_shells):
    rng = np.random.default_rng(seed=hash((symmetry, n_shells)) & 0xFFFF)
    p = FormFactorParameterizer(n_shells=n_shells, symmetry=symmetry)
    if p.n_real_dof == 0:
        # Still test the trivial shell: decode → only w_0 entry.
        W = p.decode(np.zeros(0))
        assert set(W.keys()) == {(0, 0)} if n_shells == 0 else set(W.keys()) == set(flat_vectors(enumerate_shells(n_shells)))
        return
    x = rng.standard_normal(p.n_real_dof)
    W = p.decode(x)
    x_back = p.encode(W)
    np.testing.assert_allclose(x_back, x, atol=1e-12)


@pytest.mark.parametrize("symmetry", ["C3_hard", "none"])
def test_decode_covers_every_G(symmetry):
    p = FormFactorParameterizer(n_shells=2, symmetry=symmetry)
    x = np.zeros(p.n_real_dof)
    W = p.decode(x)
    expected_keys = set(flat_vectors(enumerate_shells(2)))
    assert set(W.keys()) == expected_keys


# ----- Hermiticity + w_0 = 1 enforcement -----


def test_decode_pins_w0_to_one():
    rng = np.random.default_rng(0)
    p = FormFactorParameterizer(n_shells=2, symmetry="C3_hard")
    for _ in range(8):
        x = rng.standard_normal(p.n_real_dof)
        W = p.decode(x)
        assert W[(0, 0)] == W0_FIXED


def test_decode_satisfies_Hermiticity():
    rng = np.random.default_rng(1)
    p = FormFactorParameterizer(n_shells=2, symmetry="none")
    for _ in range(5):
        x = rng.standard_normal(p.n_real_dof)
        W = p.decode(x)
        assert is_hermitian(W, tol=1e-12)


def test_C3_hard_decode_assigns_same_coef_within_orbit():
    rng = np.random.default_rng(3)
    p = FormFactorParameterizer(n_shells=2, symmetry="C3_hard")
    x = rng.standard_normal(p.n_real_dof)
    W = p.decode(x)
    from mosaic.physics.lattice import c3_orbit

    for g, w in W.items():
        for h in c3_orbit(g):
            assert W[h] == w


# ----- encode rejects out-of-subspace inputs -----


def test_encode_rejects_violation():
    p = FormFactorParameterizer(n_shells=1, symmetry="none")
    # Build a W that violates Hermiticity.
    W = {g: 1.0 + 0.0j for g in p.vectors}
    W[(0, 0)] = W0_FIXED
    W[(1, 0)] = 1.0 + 1.0j  # but W[(-1, 0)] is still 1.0 ⇒ violation
    with pytest.raises(ValueError):
        p.encode(W)


def test_encode_rejects_wrong_w0():
    p = FormFactorParameterizer(n_shells=1, symmetry="C3_hard")
    W = {g: 0.0 + 0j for g in p.vectors}
    W[(0, 0)] = 0.5 + 0j  # violates w_0 = 1
    with pytest.raises(ValueError):
        p.encode(W)


def test_encode_rejects_wrong_keys():
    p = FormFactorParameterizer(n_shells=1, symmetry="C3_hard")
    W = {(0, 0): W0_FIXED}  # missing the rest
    with pytest.raises(ValueError):
        p.encode(W)


# ----- project: idempotent, lands in the subspace -----


def test_project_is_idempotent():
    rng = np.random.default_rng(4)
    p = FormFactorParameterizer(n_shells=2, symmetry="C3_hard")
    W_random = {g: complex(rng.standard_normal(), rng.standard_normal()) for g in p.vectors}
    W_proj = p.project(W_random)
    W_proj2 = p.project(W_proj)
    for g in p.vectors:
        assert W_proj[g] == pytest.approx(W_proj2[g], abs=1e-12)


def test_project_resets_w0_to_one():
    rng = np.random.default_rng(7)
    p = FormFactorParameterizer(n_shells=1, symmetry="C3_hard")
    W_random = {g: complex(rng.standard_normal(), rng.standard_normal()) for g in p.vectors}
    W_proj = p.project(W_random)
    assert W_proj[(0, 0)] == W0_FIXED


def test_project_lands_in_constrained_subspace():
    rng = np.random.default_rng(5)
    p = FormFactorParameterizer(n_shells=2, symmetry="C3_hard")
    W_random = {g: complex(rng.standard_normal(), rng.standard_normal()) for g in p.vectors}
    W_proj = p.project(W_random)
    # encode should now succeed (lies in subspace).
    x = p.encode(W_proj)
    W_back = p.decode(x)
    for g in p.vectors:
        assert W_back[g] == pytest.approx(W_proj[g], abs=1e-12)


# ----- |h(r)|² evaluation + positivity diagnostic -----


def test_density_for_constant_w0_is_one():
    # Just w_0 = 1, everything else zero → |h|² ≡ 1.
    p = FormFactorParameterizer(n_shells=1, symmetry="C3_hard")
    W = p.decode(np.zeros(p.n_real_dof))
    rho = evaluate_density_on_mesh(W, n_mesh=11)
    np.testing.assert_allclose(rho, 1.0, atol=1e-12)


def test_min_density_positive_for_small_perturbation():
    p = FormFactorParameterizer(n_shells=1, symmetry="C3_hard")
    rng = np.random.default_rng(10)
    x = 0.05 * rng.standard_normal(p.n_real_dof)  # small perturbation
    W = p.decode(x)
    rho_min = min_density_on_mesh(W, n_mesh=21)
    assert rho_min > 0.5  # constant 1 ± O(0.05)


def test_min_density_can_go_negative_for_large_perturbation():
    """Big enough modulation drives |h|² negative on some mesh point.
    The parameterizer doesn't enforce positivity; the diagnostic flags it."""

    p = FormFactorParameterizer(n_shells=1, symmetry="C3_hard")
    # Force a single large complex coef in the only DOF.
    x = np.array([5.0, 0.0])
    W = p.decode(x)
    rho_min = min_density_on_mesh(W, n_mesh=21)
    assert rho_min < 0.0  # very negative — sum of 6 terms with |w| = 5
