"""Shared fixtures for ED tests."""

from __future__ import annotations

import pytest

from mosaic.ed.contract import (
    Complex,
    EDInput,
    FormFactorSpec,
    LatticeSpec,
    WavefunctionSpec,
    WGCoef,
)
from mosaic.util.hashing import content_hash


def make_ed_input(
    *,
    seed: int = 0,
    n_a: int = 3,
    n_shells: int = 1,
    n_k: int = 12,
    a_values: list[complex] | None = None,
    w_values: list[complex] | None = None,
    campaign_id: str = "campaign_test_aaaaaaaaaaaa",
) -> EDInput:
    """Construct a syntactically valid ``EDInput`` for tests.

    ``W_G`` are Fourier coefficients of ``|h(r)|²`` with
    ``w_0 = 1`` and ``w_{-G} = w_G*``. The default ``w_values`` pin
    ``w_0 = 1`` and zero everything else (constant density).
    """

    if a_values is None:
        a_values = [complex(1.0, 0.0)] + [complex(0.0, 0.0)] * (n_a - 1)
    if w_values is None:
        w_values = [complex(1.0, 0.0)] + [complex(0.0, 0.0)] * 6

    a_n = [Complex.from_python(z) for z in a_values]

    shell_vectors = [(0, 0)] + [
        (1, 0),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (0, -1),
        (1, -1),
    ]
    if len(w_values) != len(shell_vectors):
        raise ValueError(
            f"w_values length {len(w_values)} ≠ shell vector count {len(shell_vectors)}"
        )
    W_G = [
        WGCoef(shell=0 if g == (0, 0) else 1, idx=i, G_int=g, coef=Complex.from_python(z))
        for i, (g, z) in enumerate(zip(shell_vectors, w_values))
    ]

    body = dict(
        schema_version="1",
        campaign_id=campaign_id,
        lattice=LatticeSpec(n_k=n_k, n_shells=n_shells).model_dump(),
        wavefunction=WavefunctionSpec(n_a=n_a, a_n=[c.model_dump() for c in a_n]).model_dump(),
        form_factor=FormFactorSpec(
            symmetry="C3_hard",
            W_G=[w.model_dump() for w in W_G],
        ).model_dump(),
        ed_solver_params={"n_basis": None, "filling": None, "extra": {}},
        energy_unit="meV",
    )
    h = content_hash(body)
    return EDInput(config_hash=h, seed=seed, **body)


def make_varied_ed_input(index: int, **kwargs) -> EDInput:
    """Like ``make_ed_input`` but produces a unique ``(a_n, W_G)`` — and
    therefore a unique ``config_hash`` — per ``index``.

    Use this in tests that sample the mock evaluator's hash-keyed
    stochastic outcomes over a population of distinct configs. The
    seed does not enter the hash, so varying it gives no hash variation;
    we have to perturb the physics. A tiny additive perturbation on ``a_values[0]``
    is enough — the mock is fully hash-keyed, so any distinct hash gives
    an independent roll.
    """

    n_a = kwargs.pop("n_a", 3)
    a_values = kwargs.pop("a_values", None)
    if a_values is None:
        a_values = [complex(1.0 + 1e-3 * index, 0.0)] + [complex(0.0, 0.0)] * (n_a - 1)
    return make_ed_input(a_values=a_values, n_a=n_a, **kwargs)


@pytest.fixture
def ed_input():
    return make_ed_input(seed=42)
