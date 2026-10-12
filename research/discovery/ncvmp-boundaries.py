"""Exact Gaussian NCVMP algebra at supplied parameters; no model fitting."""
from fractions import Fraction as F
import json


def update(mean, variance, mean_gradient, variance_gradient):
    # Fisher covariance of the minimal sufficient statistics (x, x**2).
    a, b, c = variance, 2 * mean * variance, 2 * variance**2 + 4 * mean**2 * variance
    determinant = a * c - b * b
    assert determinant == 2 * variance**3 > 0
    # Chain rule from moment parameters to natural parameters.
    g1 = variance * mean_gradient
    g2 = 2 * mean * variance * mean_gradient + 2 * variance**2 * variance_gradient
    theta = ((c * g1 - b * g2) / determinant, (-b * g1 + a * g2) / determinant)
    assert theta == (mean_gradient - 2 * mean * variance_gradient, variance_gradient)
    return theta


def main():
    mean, variance = F(2, 3), F(4, 5)
    # Conjugate log target: linear*x - precision*x**2/2.
    precision, linear = F(7, 3), F(-5, 4)
    conjugate = update(mean, variance, linear - precision * mean, -precision / 2)
    assert conjugate == (linear, -precision / 2)
    # Proper quartic log target -x**4/4 - x**2/2: finite Gaussian expectations.
    gm = -mean**3 - 3 * mean * variance - mean
    gv = -F(3, 2) * (mean**2 + variance) - F(1, 2)
    theta = update(mean, variance, gm, gv)
    new_variance = -1 / (2 * theta[1])
    new_mean = new_variance * theta[0]
    assert new_variance == 1 / (3 * mean**2 + 3 * variance + 1)
    assert new_mean == mean + new_variance * gm
    old_theta = (mean / variance, -1 / (2 * variance))
    fisher_natural_elbo = (theta[0] - old_theta[0], theta[1] - old_theta[1])
    # A normalizable bimodal target exp(2*x**2 - x**4/4) gives an invalid
    # unit proposal at q=N(0,1): precision_new = 3*variance - 4 = -1.
    invalid = update(F(0), F(1), F(0), F(1, 2))
    assert invalid == (F(0), F(1, 2))
    step = F(1, 4)
    damped = ((1 - step) * F(0) + step * invalid[0], (1 - step) * F(-1, 2) + step * invalid[1])
    assert damped == (F(0), F(-1, 4))
    print(json.dumps({
        "conjugate_natural_parameters": list(map(str, conjugate)),
        "quartic_supplied_mean_variance": [str(mean), str(variance)],
        "quartic_updated_mean_variance": [str(new_mean), str(new_variance)],
        "natural_elbo_direction": list(map(str, fisher_natural_elbo)),
        "proper_bimodal_target_unit_proposal_is_improper": True,
        "bimodal_proposal_natural_parameters": list(map(str, invalid)),
        "quarter_step_natural_parameters": list(map(str, damped)),
        "scope": "Exact Fraction arithmetic at supplied Gaussian parameters, not a fit, convergence proof, empirical performance or author-code execution. Damped propriety does not assert ELBO ascent."
    }, indent=2))


if __name__ == "__main__":
    main()
