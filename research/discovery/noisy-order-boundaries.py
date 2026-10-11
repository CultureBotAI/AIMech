"""Curator examples: noisy-OR constraints, logistic interaction and NADE order objectives."""
from fractions import Fraction as F
from itertools import product
from math import exp, log, isclose
import json

# Standard noisy-OR uses failure probabilities; the always-on bias is a leak.
fail = [F(1, 2), F(1, 3)]
leak_failure = F(3, 4)
noisy = {(a, b): 1 - leak_failure * fail[0] ** a * fail[1] ** b
         for a, b in product([0, 1], repeat=2)}
assert noisy == {(0, 0): F(1, 4), (0, 1): F(3, 4),
                 (1, 0): F(5, 8), (1, 1): F(7, 8)}
assert all(0 <= p <= 1 for p in noisy.values())
# Neal's signed-weight extension: the minimum preactivation controls validity.
valid_signed = {(a, b): 1 - exp(-(2-a-b)) for a, b in product([0, 1], repeat=2)}
invalid_signed = 1 - exp(-(1-1-1))
assert min(valid_signed.values()) == 0 and invalid_signed < 0
# The standard noisy-OR logit has interaction, unlike a logistic-linear factor.
def logit(x):
    return log(float(x / (1-x)))
interaction = logit(noisy[1, 1]) - logit(noisy[1, 0]) - logit(noisy[0, 1]) + logit(noisy[0, 0])
assert not isclose(interaction, 0, abs_tol=1e-12)

# One shared conditional function across orderings; not one consistent joint.
def conditional(i, prefix):
    if i == 0:
        return F(1, 2)
    return F(3, 4) if not prefix else [F(1, 4), F(3, 4)][prefix[0]]


def joint(x, order):
    prob = F(1)
    prefix = {}
    for i in order:
        q = conditional(i, prefix)
        prob *= q if x[i] else 1-q
        prefix[i] = x[i]
    return prob

orders = [(0, 1), (1, 0)]
assert all(sum(joint(x, o) for x in product([0, 1], repeat=2)) == 1 for o in orders)
x = (0, 1)
objective = sum(-log(float(joint(x, o))) for o in orders) / 2
estimates = []
for order in orders:
    for d in [1, 2]:
        prefix = {i: x[i] for i in order[:d-1]}
        losses = []
        for i in order[d-1:]:
            q = conditional(i, prefix)
            losses.append(-log(float(q if x[i] else 1-q)))
        estimates.append(2 / (3-d) * sum(losses))
assert isclose(sum(estimates)/len(estimates), objective)
mixture = sum(joint(x, o) for o in orders)/2
mixture_nll = -log(float(mixture))
assert objective > mixture_nll
# Conditioning the mixture reweights components by evidence probability.
evidence = [sum(joint((a, 1), o) for a in [0, 1]) for o in orders]
weights = [e/sum(evidence) for e in evidence]
conditionals = [joint((1, 1), o)/e for o, e in zip(orders, evidence)]
correct = sum(w*c for w, c in zip(weights, conditionals))
uniform = sum(conditionals)/2
assert weights == [F(2, 5), F(3, 5)]
assert correct == F(3, 5) != uniform == F(5, 8)
print(json.dumps(dict(noisy_or={str(k):str(v) for k,v in noisy.items()},noisy_or_logit_interaction=interaction,valid_signed_min_probability=min(valid_signed.values()),invalid_signed_probability=invalid_signed,order_member_probabilities=[str(joint(x,o)) for o in orders],order_mean_nll=objective,prefix_estimator_mean=sum(estimates)/len(estimates),mixture_nll=mixture_nll,evidence_conditioned_component_weights=list(map(str,weights)),conditional_mixture=str(correct),uniform_component_conditional_average=str(uniform),scope='Finite curator examples; no author implementation, training or empirical benchmark.'),indent=2))
