"""Search-boundary gate (BoundarySpec, swarm.validate.boundary_check)."""

import numpy as np

from mosaic.physics.kdep_envelope import DeformationSpec
from mosaic.swarm.config import BoundarySpec
from mosaic.swarm.validate import boundary_check

BOUND = BoundarySpec(spatial_g2_max=21, momentum_r2_max=4, alpha_max=0.6, beta_max=0.3,
                     alpha_sum_max=2.5, beta_sum_max=2.0, m2k_max_ratio=3.0)
S1 = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1))          # |G|² = 1
S7 = ((3, 1), (-3, -1))                                            # |G|² = 9 - 3 + 1 = 7
S25 = ((5, 0), (-5, 0))                                            # |G|² = 25
T1 = ((1, 0), (-1, 0))                                             # |R|² = 1
T7 = ((2, 1), (-2, -1))                                            # |R|² = 4 + 1 + 2 = 7


def spec(stars, mstars, alpha, beta):
    return DeformationSpec(spatial_stars=stars, momentum_stars=mstars, alpha=np.array(alpha, float), beta=np.array(beta, float))


def test_inside_passes():
    d = boundary_check(spec((S1, S7), (T1,), [[0.4], [0.0]], [[0.0], [0.05]]), m2k=6.9, m2_parent=3.63, bound=BOUND)
    assert d["violated"] == []
    assert d["measured"]["spatial_g2_max"] == 7 and d["measured"]["momentum_r2_max"] == 1


def test_each_bound_is_enforced():
    cases = [
        (spec((S25,), (T1,), [[0.1]], [[0.0]]), 4.0, "spatial_g2_max"),
        (spec((S1,), (T7,), [[0.1]], [[0.0]]), 4.0, "momentum_r2_max"),
        (spec((S1,), (T1,), [[0.7]], [[0.0]]), 4.0, "alpha_max"),
        (spec((S1,), (T1,), [[0.0]], [[0.31]]), 4.0, "beta_max"),
        (spec((S1, S7), (T1,), [[0.0], [0.0]], [[0.0], [0.0]]), 11.0, "m2k_max_ratio"),
    ]
    for sp, m2k, name in cases:
        v = boundary_check(sp, m2k=m2k, m2_parent=3.62875, bound=BOUND)["violated"]
        assert len(v) == 1 and v[0].startswith(name), (name, v)


def test_unused_channels_do_not_count():
    # a far star listed with zero coefficients is not part of the deformation
    d = boundary_check(spec((S1, S25), (T1, T7), [[0.2, 0.0], [0.0, 0.0]], [[0.0, 0.0], [0.0, 0.0]]),
                       m2k=4.0, m2_parent=3.63, bound=BOUND)
    assert d["violated"] == []
