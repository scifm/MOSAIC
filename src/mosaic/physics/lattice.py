"""Moiré reciprocal lattice: shells, C_3 orbits, integer-G_int convention.

We work entirely in integer ``G_int = (m, n)`` indices on
the moiré reciprocal basis ``b_1, b_2``. Physical positions live inside
the Julia ED solver. Symmetry counting (shells, C_3 orbits) is purely
combinatorial in ``(m, n)`` space.

**Basis convention.** The integer labels mean what the
solver makes of them: ``G = m·G_1 + n·G_2`` with ``∠(G_1, G_2) = 120°``
(``MoireSolver.triangular_lattice()``), so

    Q(m, n) := |m G_1 + n G_2|² / |G_1|² = m² + n² − m·n

and the first star is ``{(±1,0), (0,±1), ±(1,1)}``. The moiré C_3 rotation
in this basis maps ``G_1 → G_2 → −G_1 − G_2``:

    R_INT = [[ 0, -1],
             [ 1, -1]],   (m, n) → (−n, m − n)

which is an isometry of the metric ``M = [[2, −1], [−1, 2]]``
(``Rᵀ M R = M``, checked in ``test_lattice.py``). Earlier versions of this module
used the 60° convention (``m² + m·n + n²``, ``R = [[−1,−1],[1,0]]``); labels
built with it and read by the solver were *not* C_3-symmetric densities.
Stored ``ed_input.json`` files keep their solver
meaning; only the Python-side shell/orbit bookkeeping changed.

This module is pure combinatorics: no optimizer, no I/O. Functions
return plain Python data structures so they're trivial to JSON-encode.
"""

from __future__ import annotations

from dataclasses import dataclass

# C_3 rotation in the integer basis (120° reciprocal basis).
R_INT = ((0, -1), (1, -1))


def Q(m: int, n: int) -> int:
    """Squared length on the moiré reciprocal lattice in units of ``|G_1|²``
    (120° basis)."""

    return m * m + n * n - m * n


def apply_R(g: tuple[int, int]) -> tuple[int, int]:
    """Apply the C_3 rotation R_INT to an integer (m, n) vector."""

    m, n = g
    (a, b), (c, d) = R_INT
    return (a * m + b * n, c * m + d * n)


def apply_inversion(g: tuple[int, int]) -> tuple[int, int]:
    return (-g[0], -g[1])


def enumerate_shells(n_shells: int) -> list[list[tuple[int, int]]]:
    """Return G_int vectors grouped by shell.

    Returns a list of length ``n_shells + 1``. Index 0 is the trivial
    shell ``[(0, 0)]``. Indices 1..n_shells are the next ``n_shells``
    distinct nonzero values of ``Q(m, n)``, each containing all
    ``(m, n)`` with that ``Q``.

    Within each shell, vectors are sorted by ``(m, n)`` lex order for
    determinism.
    """

    if n_shells < 0:
        raise ValueError(f"n_shells must be ≥ 0, got {n_shells}")

    # Enumerate a generous box. Every shell with Q ≤ Q_max is contained
    # in the box |m|, |n| ≤ Q_max. We pick Q_max big enough to cover the
    # first n_shells distinct nonzero Q values; growing if needed.
    Q_max = max(1, 4 * n_shells)
    while True:
        groups: dict[int, list[tuple[int, int]]] = {}
        for m in range(-Q_max, Q_max + 1):
            for n in range(-Q_max, Q_max + 1):
                q = Q(m, n)
                if q > Q_max * Q_max:
                    continue
                groups.setdefault(q, []).append((m, n))
        nonzero_qs = sorted(q for q in groups if q > 0)
        if len(nonzero_qs) >= n_shells:
            break
        Q_max *= 2

    chosen = [(0, sorted(groups[0]))]
    for q in nonzero_qs[:n_shells]:
        chosen.append((q, sorted(groups[q])))
    return [vecs for _q, vecs in chosen]


def flat_vectors(shells: list[list[tuple[int, int]]]) -> list[tuple[int, int]]:
    """Flatten a list of shells back to a single ordered list."""

    return [g for shell in shells for g in shell]


def c3_orbit(g: tuple[int, int]) -> tuple[tuple[int, int], ...]:
    """Return the C_3 orbit of ``g`` as a tuple of unique members.

    The orbit is at most 3 elements; only ``(0, 0)`` is fixed by C_3.
    """

    seen: list[tuple[int, int]] = [g]
    cur = g
    for _ in range(2):
        cur = apply_R(cur)
        if cur in seen:
            break
        seen.append(cur)
    return tuple(seen)


def c3_orbits(vectors: list[tuple[int, int]]) -> list[tuple[tuple[int, int], ...]]:
    """Group ``vectors`` into C_3 orbits.

    Each returned orbit is a tuple sorted by lex order. Orbits are
    returned in lex order of their representative (smallest member).
    The input must be closed under C_3; a ``ValueError`` is raised
    otherwise.
    """

    pool = set(vectors)
    if len(pool) != len(vectors):
        raise ValueError("duplicate vectors in input")
    orbits: list[tuple[tuple[int, int], ...]] = []
    while pool:
        g = min(pool)
        orb = c3_orbit(g)
        for x in orb:
            if x not in pool:
                raise ValueError(
                    f"input not closed under C_3: orbit({g}) = {orb} but {x} is missing"
                )
            pool.discard(x)
        orbits.append(tuple(sorted(orb)))
    orbits.sort(key=lambda o: o[0])
    return orbits


@dataclass(frozen=True)
class GVector:
    """One reciprocal vector with its bookkeeping metadata."""

    G_int: tuple[int, int]
    shell: int
    idx: int
