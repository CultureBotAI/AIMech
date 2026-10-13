"""Finite rational checks of Chen's GS weights; not author software or a benchmark."""
from fractions import Fraction as F
from itertools import permutations
import json


def moments(outcomes):
    assert sum(p for p, _ in outcomes) == 1
    mean = sum(p * x for p, x in outcomes)
    return mean, sum(p * (x - mean) ** 2 for p, x in outcomes)


def collision(old_weight, old_value, new_weight, new_value, p):
    assert 0 < p < 1
    return [(1 - p, old_weight * old_value / (1 - p)),
            (p, new_weight * new_value / p)]


def merge_arrivals(values, proposal):
    # Each incoming leaf has weight one. The retained leaf may already have
    # an inverse-probability weight from an earlier collision in this stratum.
    states = [(F(1), F(1), values[0])]
    for value in values[1:]:
        next_states = []
        for probability, weight, representative in states:
            p = proposal(weight)
            next_states += [(probability * (1-p), weight / (1-p), representative),
                            (probability * p, 1 / p, value)]
        states = next_states
    return [(probability, weight * representative) for probability, weight, representative in states]


uniform = moments(collision(F(1), F(1), F(3), F(5), F(1, 2)))
hs = moments(collision(F(1), F(1), F(3), F(5), F(3, 4)))
oracle = moments(collision(F(1), F(1), F(3), F(5), F(15, 16)))
incorrect = moments([(F(1, 2), F(4)), (F(1, 2), F(20))])
signed = moments(collision(F(1), F(-1), F(3), F(5), F(15, 16)))
assert uniform == (16, 196) and hs == (16, 48) and oracle == (16, 0)
assert incorrect == (12, 64) and signed == (14, 60)

# Root has two incomparable parent strata A and B, with zero node costs.
# A has leaves of costs 2 and 5; B has a leaf of cost 11. All leaves share a
# lower stratum. Both A-before-B and B-before-A are valid stratum orders.
ab = moments(merge_arrivals([F(2), F(5), F(11)], lambda w: F(1, 2)))
ba = moments(merge_arrivals([F(11), F(2), F(5)], lambda w: F(1, 2)))
assert ab == (18, 34) and ba == (18, 226)
hs_permutations = [moments(merge_arrivals(list(order), lambda w: 1/(w+1)))
                   for order in permutations([F(2), F(5), F(11)])]
assert all(x == (18, 126) for x in hs_permutations)

# Verify the conditional identity over positive weights, signed functionals,
# and several supported proposals, without assuming weight-proportional p.
cases = 0
for old_w in [F(1), F(2), F(7)]:
    for new_w in [F(1), F(3), F(8)]:
        for old_v in [F(-2), F(0), F(5)]:
            for new_v in [F(-3), F(0), F(11)]:
                for p in [F(1, 100), F(1, 4), F(1, 2), F(9, 10)]:
                    assert moments(collision(old_w, old_v, new_w, new_v, p))[0] == old_w*old_v + new_w*new_v
                    cases += 1
assert cases == 324
print(json.dumps(dict(uniform_corrected_mean_variance=list(map(str, uniform)),
    hs_mean_variance=list(map(str, hs)), oracle_mean_variance=list(map(str, oracle)),
    uncorrected_uniform_mean_variance=list(map(str, incorrect)),
    signed_absolute_mass_proposal_mean_variance=list(map(str, signed)),
    valid_order_AB_mean_variance=list(map(str, ab)), valid_order_BA_mean_variance=list(map(str, ba)),
    hs_all_six_arrival_orders_mean_variance=list(map(str, hs_permutations[0])),
    conditional_expectation_cases=cases,
    unsupported_zero_probability_example=dict(retained_old_contribution=1, omitted_new_contribution=15, target=16),
    scope='Finite exact arithmetic for weighted collisions and two valid stratum orders. No author code, benchmark, general variance-bound proof or infinite-tree claim.')))
