"""Original finite arithmetic for synthesis and activation-mask conventions.

This does not execute SMOTE, TensorFlow or an author implementation.
"""
import json
import math
from fractions import Fraction


def calculate():
    start, neighbor = (0, 0), (2, 4)
    scalar = Fraction(1, 4)
    line = [a + scalar * (b - a) for a, b in zip(start, neighbor)]
    coordinate = [Fraction(1, 4) * 2, Fraction(3, 4) * 4]
    cross = coordinate[0] * 4 - coordinate[1] * 2
    assert line == [Fraction(1, 2), 1] and cross != 0
    # 3x3 map, 2x2 fully contained blocks: four independent possible seeds.
    gamma = Fraction(1, 10) * Fraction(9, 16)
    coverage_counts = [1, 2, 1, 2, 4, 2, 1, 2, 1]
    expected_drop = sum(1 - (1 - gamma) ** n for n in coverage_counts) / 9
    assert expected_drop < Fraction(1, 10)
    # Different per-map and whole-tensor normalization despite identical masks.
    retained = [1, 3]
    per_map_scales = [4 / count for count in retained]
    whole_tensor_scale = 8 / sum(retained)
    assert per_map_scales == [4.0, 4 / 3] and whole_tensor_scale == 2
    attention, ratio = [0.0, 1.0, 2.0], 0.5
    threshold = ratio * max(attention)
    definite_drop = [a > threshold for a in attention]
    equality = [a == threshold for a in attention]
    assert definite_drop == [False, False, True] and equality[1]
    weights = [1 / (1 + math.exp(-a)) for a in attention]
    assert all(0 < w < 1 for w in weights)
    return {
        "smote": {
            "scalar_interpolation": [float(x) for x in line],
            "independent_coordinate_example": [float(x) for x in coordinate],
            "coordinate_example_cross_product": float(cross),
            "interpretation": "Independent coordinate gaps need not lie on the endpoint segment.",
        },
        "dropblock": {
            "seed_probability": float(gamma),
            "target_drop_fraction": 0.1,
            "expected_union_drop_fraction": float(expected_drop),
            "per_map_rescale": per_map_scales,
            "whole_tensor_rescale": whole_tensor_scale,
            "all_zero_denominator": 0,
            "interpretation": "Overlap changes the exact drop fraction; normalization scope matters and zero retention needs a guard.",
        },
        "adl": {
            "threshold": threshold,
            "strictly_above_threshold": definite_drop,
            "equality_positions": equality,
            "sigmoid_weights": weights,
            "interpretation": "Threshold equality needs a convention; sigmoid gates are bounded and branch probability is not pixel drop fraction.",
        },
    }


if __name__ == "__main__":
    print(json.dumps(calculate(), indent=2))
