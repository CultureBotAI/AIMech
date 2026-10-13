"""Constructed local pooling examples; no author implementation or benchmark."""
import json
import math


def probabilities(values):
    if min(values) < 0 or sum(values) <= 0:
        raise ValueError('This displayed probability rule requires nonnegative positive-total inputs.')
    return [v / sum(values) for v in values]


def local_mean(values):
    return sum(p * v for p, v in zip(probabilities(values), values))


def result():
    a = [1.0, 3.0]
    p = probabilities(a)
    mean = local_mean(a)
    nonlinear_expected = sum(q * max(v - mean, 0.0) for q, v in zip(p, a))
    nonlinear_at_mean = max(mean - mean, 0.0)
    assert sum(a) / len(a) <= mean <= max(a)
    assert mean == 2.5 and nonlinear_expected == 0.375 and nonlinear_at_mean == 0.0
    x, eps = 2.0, 1e-5
    expected_derivative = ((x * x + 2 * x - 1) / ((x + 1) ** 2))
    finite_difference = (local_mean([x + eps, 1]) - local_mean([x - eps, 1])) / (2 * eps)
    routed_derivative = probabilities([x, 1])[0]
    assert math.isclose(expected_derivative, finite_difference, abs_tol=1e-9)
    assert not math.isclose(expected_derivative, routed_derivative)
    second_selection_given_first = [probabilities([v, 1])[0] for v in a]
    exact_two_stage_mean = sum(q * local_mean([v, 1]) for q, v in zip(p, a))
    local_mean_substitution = local_mean([mean, 1])
    assert second_selection_given_first == [0.5, 0.75]
    assert not math.isclose(exact_two_stage_mean, local_mean_substitution)
    invalid = []
    for values in ([0.0, 0.0], [-1.0, 2.0]):
        try:
            probabilities(values)
        except ValueError:
            invalid.append(values)
    assert len(invalid) == 2
    assert probabilities([0.0, 2.0]) == [0.0, 1.0]
    return dict(probabilities=p, local_mean=mean, nonlinear_expected=nonlinear_expected,
                nonlinear_at_local_mean=nonlinear_at_mean,
                exact_expected_output_derivative=expected_derivative,
                finite_difference=finite_difference, expected_fixed_route_derivative=routed_derivative,
                second_selection_conditional_probabilities=second_selection_given_first,
                exact_two_stage_mean=exact_two_stage_mean,
                local_mean_substitution=local_mean_substitution, undefined_or_invalid_inputs=invalid)


if __name__ == '__main__':
    print(json.dumps(result(), indent=2, sort_keys=True))
