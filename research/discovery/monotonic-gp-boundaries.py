"""Curator calculations for finite derivative constraints; no fitted GP experiment."""
from fractions import Fraction as F
from math import erfc, exp, pi, sqrt
import json

def phi(x):
    return erfc(-x / sqrt(2)) / 2

def f(x):
    return 2*x**3 - 3*x**2 + x

def df(x):
    return 6*x*x - 6*x + 1

# Endpoint derivatives are positive, but the smooth function decreases inside.
sites = [F(0), F(1, 2), F(1)]
slopes = [df(x) for x in sites]
assert slopes == [1, F(-1, 2), 1]
assert f(F(1, 4)) == F(3, 32) and f(F(3, 4)) == F(-3, 32)

# A finite probit steepness weights negative slopes instead of excluding them.
negative_slope_likelihood = phi(-1)
assert 0.15865 < negative_slope_likelihood < 0.15866

# With a standard normal derivative prior, a single hard positive-sign factor
# gives a half-normal law. Its Gaussian moment approximation still has a tail
# on negative derivatives. This is a limiting one-site calculation, not an
# executed EP implementation and not a quantitative claim about the paper's fits.
mu = sqrt(2/pi)
variance = 1-2/pi
negative_mass = phi(-mu/sqrt(variance))
assert 0.092 < negative_mass < 0.093

# Unit squared-exponential kernel mixed derivatives at separated coordinates.
def derivative_covariance(delta):
    return (1-delta*delta)*exp(-delta*delta/2)

assert derivative_covariance(0) == 1
assert derivative_covariance(1) == 0
assert derivative_covariance(2) < 0

print(json.dumps(dict(
    finite_site_derivatives=[str(v) for v in slopes],
    interior_values=[str(f(F(1,4))),str(f(F(3,4)))],
    probit_likelihood_at_slope_minus_one_nu_one=negative_slope_likelihood,
    limiting_half_normal_mean=mu,
    limiting_half_normal_variance=variance,
    matched_gaussian_negative_derivative_probability=negative_mass,
    unit_squared_exponential_derivative_covariances=[derivative_covariance(x) for x in [0,1,2]],
),indent=2))
