"""Finite curator examples for maxout boundaries; not author-code replication."""
import json
import math


def maxout(x, pieces):
    return max(w * x + b for w, b in pieces)


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def main():
    grid = [-2, -1, 0, 0.5, 1, 2]
    relu = [(0, 0), (1, 0)]
    absolute = [(1, 0), (-1, 0)]
    assert all(maxout(x, relu) == max(0, x) for x in grid)
    assert all(maxout(x, absolute) == abs(x) for x in grid)
    negative = maxout(0, [(0, -1), (0, -2)])
    assert negative == -1
    # A winner need not provide a nonzero input derivative.
    zero_input_derivative = maxout(1.001, [(0, 2), (0, 1)]) - maxout(1, [(0, 2), (0, 1)])
    assert zero_input_derivative == 0
    eps = 1e-6
    left = (maxout(0, absolute) - maxout(-eps, absolute)) / eps
    right = (maxout(eps, absolute) - maxout(0, absolute)) / eps
    assert (left, right) == (-1, 1)
    # A linear output of two convex maxout units need not be convex.
    def difference(x):
        return maxout(x, absolute) - 2 * maxout(x, [(0, 0), (1, -1)])
    values = [difference(x) for x in [0, 1, 2]]
    assert values == [0, 1, 0]
    # Input dropout m~Bernoulli(0.5) can cross an affine-region boundary.
    logits = [maxout(m, [(0, 0), (2, -1)]) for m in [0, 1]]
    probabilities = [sigmoid(z) for z in logits]
    g1 = math.sqrt(probabilities[0] * probabilities[1])
    g0 = math.sqrt((1 - probabilities[0]) * (1 - probabilities[1]))
    normalized_geometric = g1 / (g0 + g1)
    arithmetic = sum(probabilities) / 2
    scaled = sigmoid(maxout(0.5, [(0, 0), (2, -1)]))
    assert math.isclose(normalized_geometric, sigmoid(sum(logits) / 2))
    assert abs(normalized_geometric - arithmetic) > 0.006
    assert abs(normalized_geometric - scaled) > 0.12
    # In a fixed affine regime, expectation commutes with that affine map.
    fixed_logits = [maxout(m, [(2, 1), (0, -3)]) for m in [0, 1]]
    fixed_scaled = maxout(0.5, [(2, 1), (0, -3)])
    assert sum(fixed_logits) / 2 == fixed_scaled == 2
    return dict(relu_and_absolute_special_cases=True, negative_output=negative,
                constant_winner_input_derivative=zero_input_derivative,
                tie_one_sided_derivatives=[left, right],
                nonconvex_two_unit_output=values, dropout_mask_logits=logits,
                normalized_geometric_prediction=normalized_geometric,
                arithmetic_prediction=arithmetic, weight_scaled_prediction=scaled,
                fixed_affine_regime_mean_logit=fixed_scaled)


if __name__ == '__main__':
    print(json.dumps(main(), sort_keys=True))
