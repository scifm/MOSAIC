from __future__ import annotations

import copy

import pytest
from pydantic import ValidationError

from mosaic.ed.contract import EDOutput


def pes_output() -> dict:
    return {
        "config_hash": "pes_contract_fixture", "status": "completed", "n_k": 4,
        "compute_seconds": 0.01, "solver_version": "moire-julia-ed@v0.9.1",
        "pes": {
            "NA": 1, "holes": False, "N": 1, "Ns": 4,
            "mixture": "equal_incoherent",
            "parents": [{"momentum": [0, 0], "state": 1, "energy": 0.0}],
            "parent_sectors": [0], "momenta": [[0, 0], [1, 0], [2, 0], [3, 0]],
            "eigenvalues": [[1.0], [0.0], [0.0], [0.0]],
            "levels": [[0.0], [None], [None], [None]],
            "display_levels": [[0.0], [34.538776], [34.538776], [34.538776]],
            "dimensions": [1, 1, 1, 1], "ranks": [1, 0, 0, 0],
            "trace": 1.0, "minimum_eigenvalue": 0.0, "zero_tol": 1e-14,
            "level_floor": 1e-15, "threshold_mode": "none",
            "threshold_diagnostic": {
                "threshold": None, "gap": None, "counts": None, "total_count": None,
            },
            "counting_diagnostic": None,
        },
    }


def test_pes_roundtrip_preserves_null_modes():
    output = EDOutput.model_validate(pes_output())
    restored = EDOutput.model_validate_json(output.model_dump_json())
    assert restored == output
    assert restored.pes.levels[1] == [None]
    assert restored.pes.trace == 1.0


@pytest.mark.parametrize("field,value", [
    ("dimensions", [1]), ("ranks", [2, 0, 0, 0]),
    ("levels", [[0.0, 1.0], [None], [None], [None]]),
    ("parent_sectors", [4]), ("NA", 2), ("trace", float("nan")),
])
def test_pes_rejects_invalid_shapes_and_nonfinite_values(field, value):
    data = copy.deepcopy(pes_output())
    data["pes"][field] = value
    with pytest.raises(ValidationError):
        EDOutput.model_validate(data)


def test_old_ed_output_does_not_require_pes():
    data = pes_output()
    del data["pes"]
    assert EDOutput.model_validate(data).pes is None
