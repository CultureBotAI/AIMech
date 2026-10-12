"""Analytic curator checks; no fitted GP, author code or benchmark execution."""
from fractions import Fraction as F
import json
import math


def posterior(x, derivative, value_noise=0.0, derivative_noise=0.0):
    """Unit RBF, independent noise variances, observed f(0)=1 and f'(0)=d."""
    k = math.exp(-x*x/2)
    mean = k/(1+value_noise) + x*k*derivative/(1+derivative_noise)
    variance = 1-k*k/(1+value_noise)-x*x*k*k/(1+derivative_noise)
    return dict(mean=mean, variance=variance)


def calculate():
    zero = posterior(1.0, 0.0)
    one = posterior(1.0, 1.0)
    noisy = posterior(1.0, 0.0, derivative_noise=1.0)
    assert math.isclose(zero['mean'], math.exp(-0.5))
    assert math.isclose(one['mean'], 2*zero['mean'])
    assert math.isclose(zero['variance'], 1-2/math.e)
    assert zero['variance'] > 0 and noisy['variance'] > zero['variance']
    # Conditional variance at an exactly observed point is zero. A derivative
    # and value at zero leave positive variance at any fixed nonzero h.
    finite = [{'h':h, 'derivative_conditioned_variance':posterior(h,0)['variance'],
               'two_exact_values_variance_at_h':0.0} for h in [1.0,0.5,0.1]]
    assert all(q['derivative_conditioned_variance'] > 0 for q in finite)
    # OLS coefficients for x=0,1,2 with independent unit observation variance.
    # X^T X=[[3,3],[3,5]]; its inverse gives intercept/slope covariance.
    covariance = [[F(5,6),F(-1,2)],[F(-1,2),F(1,2)]]
    full = sum(sum(row) for row in covariance)
    diagonal = covariance[0][0]+covariance[1][1]
    assert full == F(1,3) and diagonal == F(4,3)
    # f~N(0,1), y=f+e, Var(e)=1: a copied y is not independent new evidence.
    single_variance = F(1,2)
    false_independent_variance = F(1,3)
    assert false_independent_variance < single_variance
    return {
        'scope':'Curator analytic Gaussian-conditioning and exact rational illustrations; not a reproduction of Figures 2–5 or source software.',
        'unit_rbf_at_x1':{'f0_1_derivative0':zero,'f0_1_derivative1':one,
                         'derivative0_noise_variance1':noisy},
        'finite_separation':finite,
        'ols_at_x_0_1_2_unit_noise':{
            'intercept_slope_covariance':[[str(v) for v in row] for row in covariance],
            'prediction_variance_at_x1_full_covariance':str(full),
            'prediction_variance_at_x1_diagonal_only':str(diagonal)},
        'duplicate_observation':{
            'correct_posterior_variance':str(single_variance),
            'false_independent_posterior_variance':str(false_independent_variance)},
        'limits':[
            'Conditioning formulas use fixed unit squared-exponential hyperparameters and known Gaussian noise variances.',
            'The two-value comparison is at a fixed nonzero separation, not the derivative limit as separation tends to zero.',
            'The OLS example is an unregularized illustrative covariance calculation, not validation of arbitrary ridge-prior scaling.',
            'The copied-observation example demonstrates dependence; it does not estimate the error in the paper\u2019s datasets.'
        ]}


if __name__ == '__main__':
    print(json.dumps(calculate(), indent=2))
