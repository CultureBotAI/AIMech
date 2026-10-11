"""Curator calculations for model and estimator boundaries; no author code."""
from fractions import Fraction as F
from itertools import product
from math import exp, log, isclose
import json


def sigmoid(x):
    return 1 / (1 + exp(-x))


# A two-node sigmoid belief network: forward and posterior conditionals differ.
joint = {(h, x): F(1, 2) * ([F(1, 4), F(3, 4)][h] if x else
                            1 - [F(1, 4), F(3, 4)][h])
         for h, x in product([0, 1], repeat=2)}
assert sum(joint.values()) == 1
posterior = joint[1, 1] / sum(joint[h, 1] for h in [0, 1])
assert posterior == F(3, 4) != F(1, 2)
for h in [0, 1]:
    assert isclose(sigmoid(-log(3) + 2 * log(3) * h),
                   sigmoid(log(3) * (2 * h - 1)))

# Original binary NADE, one deterministic hidden unit and two visible bits.
# W[:,1]=log(3), W[:,2]=0, c=0; V[1]=0, V[2]=4log(3).
nade = {}
bad_zero = {}
bad_plus = {}
for x1, x2 in product([0, 1], repeat=2):
    a = 0.0
    correct, zero_init, plus_factor = 1.0, 0.0, 1.0
    for i, x in enumerate([x1, x2]):
        h = sigmoid(a)
        prob = sigmoid((0 if i == 0 else -3 * log(3)) +
                       (0 if i == 0 else 4 * log(3)) * h)
        factor = prob ** x * (1 - prob) ** (1 - x)
        correct *= factor
        zero_init *= factor
        plus_factor *= prob ** x + (1 - prob) ** (1 - x)
        a += [log(3), 0][i] * x
    nade[x1, x2], bad_zero[x1, x2], bad_plus[x1, x2] = correct, zero_init, plus_factor
assert isclose(sum(nade.values()), 1)
assert all(isclose(nade[k], v) for k, v in
           {(0, 0): 3/8, (0, 1): 1/8, (1, 0): 1/4, (1, 1): 1/4}.items())
assert sum(bad_zero.values()) == 0
assert isclose(sum(bad_plus.values()), 9)
assert not isclose(log(3) * 1, 0 * 0)  # correct W[:,1]x1 vs printed i+1 term

# A small DARN generative component with two autoregressive stochastic h units.
def bern(prob, value):
    return prob if value else 1 - prob


def pj(h1, h2, x):
    return F(1, 2) * bern([F(1, 4), F(3, 4)][h1], h2) * bern([F(1, 4), F(3, 4)][h2], x)


assert sum(pj(*s) for s in product([0, 1], repeat=3)) == 1
px = sum(pj(h1, h2, 1) for h1, h2 in product([0, 1], repeat=2))
assert px == F(1, 2)
q = F(1, 4)  # a valid factorized recognition proposal, not the posterior
free_energy = sum(float(q) * log(float(q / pj(h1, h2, 1)))
                  for h1, h2 in product([0, 1], repeat=2))
kl = sum(float(q) * log(float(q / (pj(h1, h2, 1) / px)))
         for h1, h2 in product([0, 1], repeat=2))
assert kl > 0 and isclose(free_energy, -log(float(px)) + kl)

# DARN Appendix A Eq24, isolated Bernoulli unit, f independent of logit a.
p = F(1, 4)
dp = p * (1 - p)
def expected_surrogate(power):
    return sum(bern(p, h) * dp * power * h ** (power - 1) / (2 * bern(p, h)) for h in [0, 1])
assert expected_surrogate(2) == dp
assert expected_surrogate(3) == F(9, 32) != dp  # true derivative of E[h^3] is dp
print(json.dumps(dict(
    sigmoid_belief=dict(prior_h1='1/2', posterior_h1_given_x1=str(posterior), binary_encoding_transform='verified'),
    nade=dict(joint={str(k): v for k, v in nade.items()}, total_mass=sum(nade.values()), zero_initialized_total=sum(bad_zero.values()), plus_factor_total=sum(bad_plus.values()), prefix_recurrence_index='i, not i+1'),
    darn=dict(marginal_x1=str(px), recognition_to_posterior_kl_nats=kl, free_energy_nats=free_energy, negative_log_marginal=-log(float(px)), quadratic_expected_gradient=str(expected_surrogate(2)), cubic_expected_gradient=str(expected_surrogate(3)), cubic_true_gradient=str(dp)),
    scope='Finite curator examples and algebra; not author implementation, training, benchmark or general convergence proof.'
), indent=2))
