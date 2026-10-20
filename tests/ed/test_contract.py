"""Schema round-trip and validation."""

from __future__ import annotations

import json

import pytest
from pydantic import ValidationError

from mosaic.ed.contract import (
    Complex,
    EDInput,
    EDOutput,
    FormFactorSpec,
    LatticeSpec,
    WavefunctionSpec,
    WGCoef,
)
from .conftest import make_ed_input


def test_input_roundtrip(ed_input: EDInput):
    s = ed_input.model_dump_json()
    restored = EDInput.model_validate_json(s)
    assert restored == ed_input


def test_output_roundtrip(ed_input: EDInput):
    out = EDOutput(
        config_hash=ed_input.config_hash,
        status="completed",
        n_k=ed_input.lattice.n_k,
        target_band_index=1,
        epsilon_target=[[0.0] * 12 for _ in range(12)],
        epsilon_above=[[0.05] * 12 for _ in range(12)],
        epsilon_below=[[-0.05] * 12 for _ in range(12)],
        chern_solver=1,
        gap_top_indirect_solver=0.05,
        compute_seconds=0.1,
        solver_version="mock-ed@v1",
    )
    s = out.model_dump_json()
    restored = EDOutput.model_validate_json(s)
    assert restored == out


def test_complex_atom_roundtrip():
    z = Complex(re=1.5, im=-2.5)
    s = z.model_dump_json()
    assert json.loads(s) == {"re": 1.5, "im": -2.5}
    assert z.to_python() == complex(1.5, -2.5)
    assert Complex.from_python(complex(1.5, -2.5)) == z


def test_input_rejects_extra_fields():
    bad = make_ed_input().model_dump()
    bad["junk_field"] = 1
    with pytest.raises(ValidationError):
        EDInput.model_validate(bad)


def test_input_rejects_bad_n_k():
    bad = make_ed_input().model_dump()
    bad["lattice"]["n_k"] = 2  # below min
    with pytest.raises(ValidationError):
        EDInput.model_validate(bad)


def test_input_rejects_invalid_symmetry():
    bad = make_ed_input().model_dump()
    bad["form_factor"]["symmetry"] = "C6_hard"  # not allowed
    with pytest.raises(ValidationError):
        EDInput.model_validate(bad)


def test_input_rejects_legacy_reality_mode_field():
    """The field is dropped — extra keys are rejected."""

    bad = make_ed_input().model_dump()
    bad["form_factor"]["reality_mode"] = "B_real"
    with pytest.raises(ValidationError):
        EDInput.model_validate(bad)


def test_lattice_spec_g_units_locked():
    with pytest.raises(ValidationError):
        LatticeSpec(n_k=12, n_shells=1, g_units="angstrom")


def test_status_values_locked():
    with pytest.raises(ValidationError):
        EDOutput(
            config_hash="a" * 16,
            status="ok",
            n_k=12,
            compute_seconds=0.0,
            solver_version="x",
        )


def test_static_form_factor_serialises_without_a_deformation_key():
    """Adding the optional block must not change any existing hash."""
    from mosaic.ed.contract import DeformationBlock, FormFactorSpec, WGCoef, Complex

    ff = FormFactorSpec(symmetry="C3_hard", W_G=[WGCoef(shell=0, idx=0, G_int=(0, 0), coef=Complex(re=1.0, im=0.0))])
    dumped = ff.model_dump(mode="json")
    assert "deformation" not in dumped
    assert '"deformation"' not in ff.model_dump_json()
    # and a present block round-trips
    star = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)]
    ff2 = FormFactorSpec(
        symmetry="C3_hard",
        W_G=ff.W_G,
        deformation=DeformationBlock(spatial_stars=[star], momentum_stars=[star], alpha=[[0.1]], beta=[[0.0]], n_mesh=24, g_cutoff=2),
    )
    dumped2 = ff2.model_dump(mode="json")
    assert dumped2["deformation"]["alpha"] == [[0.1]] and dumped2["deformation"]["g_cutoff"] == 2
    assert FormFactorSpec.model_validate(dumped2).deformation.n_mesh == 24


def test_output_accepts_spectrum_fields(ed_input: EDInput):
    """Solver >= v0.7.1: sector-resolved low energies and the
    ground-manifold splitting round-trip; older outputs without them still parse."""

    out = EDOutput(
        config_hash=ed_input.config_hash,
        status="completed",
        n_k=ed_input.lattice.n_k,
        chern_solver=1,
        gap_top_indirect_solver=0.05,
        low_energies=[[0.0, 0.1], [0.02, 0.15]],
        sector_momenta=[(0, 0), (1, 0)],
        gs_manifold_splitting=0.02,
        compute_seconds=0.1,
        solver_version="moire-julia-ed@v0.7.1",
    )
    restored = EDOutput.model_validate_json(out.model_dump_json())
    assert restored == out
    assert restored.sector_momenta == [(0, 0), (1, 0)]
    legacy = EDOutput.model_validate_json(
        '{"config_hash": "%s", "status": "completed", "n_k": 12, "compute_seconds": 1.0, "solver_version": "moire-julia-ed@v0.7.0"}'
        % ed_input.config_hash
    )
    assert legacy.low_energies is None and legacy.gs_manifold_splitting is None
