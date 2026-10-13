"""Curator algebra checks; no execution of the paper's implementation."""
import json
import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def log_sigmoid(x):
    return -math.log1p(math.exp(-x))


def derivative(f, x):
    h = 1e-5
    return (f(x + h) - f(x - h)) / (2 * h)


def main():
    # Two equally weighted experts, only the first logit depends on theta.
    theta = 1.0
    p_member = sigmoid(3 * theta)
    p_ensemble = sigmoid((3 * theta - 3) / 2)
    scores = [3 * (1 - p_member), -3 * p_member]
    expectation = p_ensemble * scores[0] + (1 - p_ensemble) * scores[1]
    minus_normalizer = (scores[0] - expectation) / 2
    printed_plus = (scores[0] + expectation) / 2
    numerical = derivative(lambda t: log_sigmoid((3 * t - 3) / 2), theta)
    assert math.isclose(minus_normalizer, numerical, rel_tol=1e-8)
    assert minus_normalizer > 0 and printed_plus < 0
    # Tied logits theta and -theta give a constant ensemble, but the average
    # individual log likelihood is not constant.
    ensemble_gradient = derivative(lambda t: log_sigmoid((t - t) / 2), 1)
    individual_gradient = derivative(lambda t: (log_sigmoid(t) + log_sigmoid(-t)) / 2, 1)
    assert ensemble_gradient == 0 and individual_gradient < -0.23
    tied_partial_sum = (1 - 0.5) / 2 + -(1 - 0.5) / 2
    assert tied_partial_sum == 0
    # Dropout across a rectifier boundary changes the ensemble proxy. Averaging
    # selected-mask score terms with that proxy need not yield the exact gradient.
    t = 1.2
    actual_logits = [max(0, m * t - 0.5) for m in [0, 1]]
    true_prediction = sigmoid(sum(actual_logits) / 2)
    scaled_prediction = sigmoid(max(0, 0.5 * t - 0.5))
    exact_gradient = 0.5 * (1 - true_prediction)
    proxy_gradient = 0.5 * (1 - scaled_prediction)
    numerical_tied = derivative(lambda z: log_sigmoid((max(0, -0.5) + max(0, z - 0.5)) / 2), t)
    assert math.isclose(exact_gradient, numerical_tied, rel_tol=1e-8)
    assert abs(proxy_gradient - exact_gradient) > 0.03
    return dict(normalizer_subtraction_gradient=minus_normalizer,
                finite_difference_gradient=numerical, printed_plus_gradient=printed_plus,
                tied_ensemble_gradient=ensemble_gradient,
                average_individual_log_likelihood_gradient=individual_gradient,
                sum_of_tied_partial_contributions=tied_partial_sum,
                exact_mask_ensemble_prediction=true_prediction,
                weight_scaled_prediction=scaled_prediction,
                exact_tied_gradient=exact_gradient,
                selected_mask_proxy_mean_gradient=proxy_gradient)


if __name__ == '__main__':
    print(json.dumps(main(), sort_keys=True))
