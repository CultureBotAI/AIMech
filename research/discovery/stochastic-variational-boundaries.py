"""Curator calculations, not author code or a model benchmark."""
from fractions import Fraction as F
from math import exp, log
import json

# Standard logistic noise at a=0: integrate the positive-part survival function.
# Simpson quadrature is approximate; the omitted tail is bounded by exp(-30).
n = 10000
step = 30 / n
survival = lambda x: exp(-x) / (1 + exp(-x))
area = step / 3 * (survival(0) + survival(30) + sum(
    (4 if i % 2 else 2) * survival(i * step) for i in range(1, n)))
assert abs(area - log(2)) < 1e-9

# STS at p=1/4: b~Bernoulli(1/2), h=b/2, p'=p(1-p).
p, amplitude = F(1, 4), F(1, 2)
dp = p * (1 - p)
outcomes = [(F(1, 2), F(0)), (F(1, 2), amplitude)]
mean = sum(prob * value for prob, value in outcomes)
second = sum(prob * value**2 for prob, value in outcomes)
fixed_gate_gradient = amplitude * dp / (2 * amplitude)
assert mean == p and second == F(1, 8) != mean**2
assert fixed_gate_gradient == F(3, 32) != dp == F(3, 16)

# BBVI example: q=N(mu,1), p=N(1,1), at mu=0.
# h(z)=z, log(p/q)=z-1/2, f(z)=z^2-z/2; true gradient E[f]=1.
# For two distinct samples, sample Cov(f,h)/Var(h)=z1+z2-1/2.
# This calculation investigates hypothetical sample reuse, not author behavior.
def add(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, F(0)) + value
    return {k: v for k, v in out.items() if v}
def multiply(a, b):
    out = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            key = (i+k, j+l)
            out[key] = out.get(key, F(0)) + x*y
    return {k: v for k, v in out.items() if v}
mean_f = {(2,0):F(1,2), (0,2):F(1,2), (1,0):F(-1,4), (0,1):F(-1,4)}
coefficient = {(1,0):F(1), (0,1):F(1), (0,0):F(-1,2)}
mean_h = {(1,0):F(1,2), (0,1):F(1,2)}
corrected = add(mean_f, {k:-v for k,v in multiply(coefficient, mean_h).items()})
assert corrected == {(1,1):F(-1)}
moments = {0:F(1), 1:F(0), 2:F(1)}
expectation = lambda poly: sum(v*moments[i]*moments[j] for (i,j),v in poly.items())
assert expectation(mean_f) == 1 and expectation(corrected) == 0
# The population-optimal fixed coefficient is -1/2, giving f-a*h=z^2.
fixed = add(mean_f, {k:F(1,2)*v for k,v in mean_h.items()})
assert expectation(fixed) == 1
print(json.dumps(dict(
    noisy_rectifier=dict(activation_probability="1/2", numerical_mean=area,
        exact_mean="log(2)", noiseless_output=0, omitted_tail_upper_bound=exp(-30)),
    stochastic_times_smooth=dict(mean=str(mean), second_moment=str(second),
        square_of_mean=str(mean**2), expected_fixed_gate_derivative=str(fixed_gate_gradient),
        derivative_of_mean=str(dp)),
    bbvi=dict(true_elbo_gradient="1", fixed_optimal_coefficient="-1/2",
        fixed_coefficient_mean="1", hypothetical_two_sample_reuse_mean="0",
        corrected_polynomial="-z1*z2", source_behavior_claim=False),
    status="PASS"), indent=2))
