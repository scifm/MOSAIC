"""Lattice combinatorics: shells, C_3 orbits, R_INT correctness."""

from __future__ import annotations

from mosaic.physics.lattice import (
    R_INT,
    Q,
    apply_R,
    c3_orbit,
    c3_orbits,
    enumerate_shells,
    flat_vectors,
)


def test_R_INT_cubes_to_identity():
    g = (3, -2)
    assert apply_R(apply_R(apply_R(g))) == g


def test_R_INT_eigenvalues_are_cube_roots_of_unity():
    """Trace −1, det +1 ⇒ eigenvalues exp(±2πi/3)."""

    (a, b), (c, d) = R_INT
    assert a + d == -1
    assert a * d - b * c == 1


def test_shell_zero_only_origin():
    shells = enumerate_shells(0)
    assert shells == [[(0, 0)]]


def test_shell_one_has_six_vectors_at_Q1():
    shells = enumerate_shells(1)
    assert len(shells) == 2
    assert shells[0] == [(0, 0)]
    s1 = shells[1]
    assert len(s1) == 6
    assert all(Q(*g) == 1 for g in s1)
    # 120° basis: the first star is ±G_1, ±G_2, ±(G_1 + G_2)
    assert set(s1) == {(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1)}


def test_shell_two_has_six_vectors_at_Q3():
    shells = enumerate_shells(2)
    assert len(shells) == 3
    s2 = shells[2]
    assert len(s2) == 6
    assert all(Q(*g) == 3 for g in s2)


def test_shell_four_includes_Q7_with_twelve_vectors():
    """Q=7 has 12 solutions: the first shell with size > 6."""

    shells = enumerate_shells(4)
    qs = [Q(*shell[0]) for shell in shells[1:]]
    sizes = [len(shell) for shell in shells[1:]]
    assert qs == [1, 3, 4, 7]
    assert sizes == [6, 6, 6, 12]


def test_c3_orbit_of_origin_is_singleton():
    assert c3_orbit((0, 0)) == ((0, 0),)


def test_c3_orbit_of_shell_one_member_has_three_elements():
    orb = c3_orbit((1, 0))
    assert len(orb) == 3
    assert (1, 0) in orb
    # Closure
    for g in orb:
        assert apply_R(g) in orb


def test_c3_orbits_partition_shell_one_into_two_orbits():
    shells = enumerate_shells(1)
    orbits = c3_orbits(shells[1])
    assert len(orbits) == 2
    sizes = sorted(len(o) for o in orbits)
    assert sizes == [3, 3]
    # The two orbits are inversion partners of each other.
    a, b = orbits
    a_set = set(a)
    b_set = set(b)
    assert {(-m, -n) for (m, n) in a_set} == b_set


def test_c3_orbits_raise_on_non_closed_input():
    import pytest
    from mosaic.physics.lattice import c3_orbits

    with pytest.raises(ValueError):
        c3_orbits([(1, 0), (0, 1)])  # not closed under R


def test_flat_vectors_preserves_order():
    shells = enumerate_shells(2)
    flat = flat_vectors(shells)
    assert flat[0] == (0, 0)
    assert len(flat) == 1 + 6 + 6


# --- 120° basis acceptance ---------------------------------------------------

SOLVER_METRIC = ((2, -1), (-1, 2))   # Gram matrix of (G_1, G_2) at 120°, |G_1|² = 2


def test_R_INT_is_an_isometry_of_the_solver_metric():
    """R^T M R = M for the 120° metric: the C_3 used for orbits is a lattice symmetry
    of the solver's geometry (the old 60°-basis R = [[-1,-1],[1,0]] is not)."""

    import numpy as np

    R = np.array(R_INT); M = np.array(SOLVER_METRIC)
    assert (R.T @ M @ R == M).all()
    old = np.array(((-1, -1), (1, 0)))
    assert not (old.T @ M @ old == M).all()


def test_Q_matches_the_solver_cartesian_vectors():
    import math

    g1 = (1.0, 0.0); g2 = (-0.5, math.sqrt(3) / 2)      # ReciprocalLattice(1.0, -0.5)
    for m in range(-3, 4):
        for n in range(-3, 4):
            v = (m * g1[0] + n * g2[0], m * g1[1] + n * g2[1])
            assert abs(v[0] ** 2 + v[1] ** 2 - Q(m, n)) < 1e-12


def test_eight_shells_match_the_solver_length_classes():
    """|G|² classes 1,3,4,7,9,12,13,16 with multiplicities 6,6,6,12,6,6,12,6 —
    the same numbers as in the old 60° basis, but now on the members the solver puts there."""

    shells = enumerate_shells(8)
    assert [Q(*sh[0]) for sh in shells[1:]] == [1, 3, 4, 7, 9, 12, 13, 16]
    assert [len(sh) for sh in shells[1:]] == [6, 6, 6, 12, 6, 6, 12, 6]
    for sh in shells[1:]:
        for g in sh:
            assert apply_R(g) in sh and (-g[0], -g[1]) in sh
