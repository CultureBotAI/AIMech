"""Small exact curator checks for the Zhao-Kwok-Zhang 2009 formulation.

This does not implement the authors' optimizer or reproduce their benchmarks.
"""
from fractions import Fraction as F
from itertools import product
import json
import math

n, limit = 4, F(1)
scores = [F(1, 4)] * n
assert abs(sum(scores)) <= limit
labels = [1 if f > 0 else -1 for f in scores]
assert abs(sum(labels)) > limit
relaxed_loss = sum(max(F(0), 1-abs(f)) for f in scores)/n
assert relaxed_loss == F(3, 4)
balanced_labels = [y for y in product([-1, 1], repeat=n) if abs(sum(y)) <= limit]
assert len(balanced_labels) == 6
# All features are zero. Balanced labels force two positive and two negative.
# The average hinge loss equals (max(0,1-b)+max(0,1+b))/2 >= 1 for every b.
for bias in [F(i, 4) for i in range(-12, 13)]:
    for y in balanced_labels:
        assert sum(max(F(0), 1-t*bias) for t in y)/n >= 1

f = [F(-13, 10), F(-1, 5), F(2, 5), F(1)]
hinge = sum(max(F(0), 1-abs(x)) for x in f)/n
values = [(sum(c[i]*(1-abs(f[i])) for i in range(n))/n, c)
          for c in product([0, 1], repeat=n)]
assert max(v for v, _ in values) == hinge == F(7, 20)
oracle = tuple(int(abs(x) < 1) for x in f)
assert next(v for v,c in values if c == oracle) == hinge

# The experimental mixed kernel is sum beta_k K_k, with sqrt(beta) blocks.
beta = [F(1, 2), F(1, 2)]
feature = [F(1), F(2)]
mixed_kernel_diagonal = sum(b*x*x for b,x in zip(beta, feature))
naive_feature_sum_diagonal = sum(b*x for b,x in zip(beta, feature))**2
assert mixed_kernel_diagonal == F(5, 2)
assert naive_feature_sum_diagonal == F(9, 4)
assert mixed_kernel_diagonal != naive_feature_sum_diagonal

def cone(v, t, b):
    return math.sqrt(4*sum(x*x for x in v)+(t-b)**2) <= t+b+1e-12
assert cone([3, 4], 50, .5)
assert not cone([3, 4], 49, .5)
assert cone([0], 0, 0)
assert not cone([1], 100, 0)

# At zero scores, sign(0)=0 is an allowed absolute-value subgradient.
# Freezing it makes the all-ones mask require xi>=1 regardless of bias.
# Returning b=0 is an optimal inner solution, yet a small bias lowers true loss.
zero_surrogate_slack = F(1)
nearby_bias = F(1, 100)
nearby_true_loss = 1-nearby_bias
assert n*nearby_bias <= limit and nearby_true_loss < zero_surrogate_slack

tied_scores = [F(1), F(1), F(0)]
strict_winner = [int(all(tied_scores[p] > tied_scores[q]
                       for q in range(3) if q != p)) for p in range(3)]
assert sum(strict_winner) == 0
tie_label_from_printed_formula = sum((p+1)*z for p,z in enumerate(strict_winner))
assert tie_label_from_printed_formula == 0
chosen = max(range(3), key=lambda p: (tied_scores[p], -p))
assert chosen == 0
unique_scores = [F(3, 5), F(1, 5), F(-1, 2)]
winner = max(range(3), key=lambda p: unique_scores[p])
runner = max((p for p in range(3) if p != winner), key=lambda p: unique_scores[p])
gap = unique_scores[winner] - unique_scores[runner]
losses = [max(F(0), 1-(unique_scores[winner]-unique_scores[r])-
              int(r == winner)) for r in range(3)]
assert max(losses) == 1-gap == F(3, 5)

out = dict(score_balance=dict(scores=list(map(float,scores)),score_sum=float(sum(scores)),
                               label_sum=sum(labels),limit=float(limit),
                               zero_feature_relaxed_objective=float(relaxed_loss),
                               hard_balanced_minimum_objective=1),
           one_slack=dict(scores=list(map(float,f)),oracle_mask=oracle,mean_hinge=float(hinge)),
           kernel_combination=dict(mixed_diagonal=float(mixed_kernel_diagonal),
                                   naive_sum_diagonal=float(naive_feature_sum_diagonal)),
           zero_subgradient=dict(inner_slack=float(zero_surrogate_slack),
                                 nearby_bias=float(nearby_bias),nearby_true_loss=float(nearby_true_loss)),
           multiclass=dict(strict_tie_indicator=strict_winner,
                           printed_tie_label=tie_label_from_printed_formula,
                           deterministic_one_based_winner=chosen+1,
                           unique_top_runner_gap=float(gap),hinge_loss=float(max(losses))),
           perspective='SOC epigraph checks include beta=0 closure and positive beta boundary.',
           interpretation='Finite mathematical checks only; no author optimizer or benchmark execution.')
print(json.dumps(out,indent=2))
