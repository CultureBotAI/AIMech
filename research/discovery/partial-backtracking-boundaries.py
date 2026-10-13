"""Constructed finite checks; not Purdom's code or an empirical replication."""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json

def moments(outcomes):
    assert sum(p for p, value in outcomes) == 1
    mean = sum(p * value for p, value in outcomes)
    return mean, sum(p * (value - mean) ** 2 for p, value in outcomes)

# Four root candidates: two rejected leaves, and two feasible branches with
# two and three terminal children. Unit cost includes failed candidate tests.
# Root itself is not tested, matching B1/M1's zero initial accumulator.
branch_test_costs = [3, 1, 4, 1]
full_test_count = sum(branch_test_costs)
assert full_test_count == 9
feasible_nonroot_nodes = 2 + 2 + 3
assert feasible_nonroot_nodes == 7
assert feasible_nonroot_nodes + 1 == 8  # a different, root-inclusive target

basic = {}
for m in [1, 2, 4]:
    subsets = list(combinations(branch_test_costs, m))
    # The selected branches are fully explored below the first level.
    outcomes = [(F(1, len(subsets)), F(4, m) * sum(s)) for s in subsets]
    mean, variance = moments(outcomes)
    work = sum(F(sum(s), len(subsets)) for s in subsets)
    assert mean == full_test_count
    basic[m] = dict(mean=str(mean), variance=str(variance), work=str(work),
                    work_times_variance=str(work * variance))
assert basic[1]['variance'] == '27'
assert basic[2]['variance'] == '9'
assert basic[4]['variance'] == '0'
assert basic[1]['work'] == '9/4'

# M2 tests all four root candidates, then m=1 samples a feasible branch.
# Its descendants carry weight 2, while the initial tests carry weight 1.
modified = [(F(1, 2), F(4 + 2 * n)) for n in [2, 3]]
modified_mean, modified_variance = moments(modified)
assert (modified_mean, modified_variance) == (9, 1)
modified_work = F((4 + 2) + (4 + 3), 2)
assert modified_work == F(13, 2)
wrong_omit_failed_tests, _ = moments([(p, x - 2) for p, x in modified])
assert wrong_omit_failed_tests == 7
wrong_weight, _ = moments([(F(1, 6), 4 * sum(s))
                          for s in combinations(branch_test_costs, 2)])
assert wrong_weight == 18  # forgetting division by m

# Sequential r/x selection produces uniform subsets without replacement.
def sequential(a, remaining, chosen=(), probability=F(1)):
    if a == 0:
        assert remaining == 0
        return {tuple(sorted(chosen)): probability}
    result = {}
    if remaining:
        result.update(sequential(a - 1, remaining - 1, chosen + (a,),
                                 probability * F(remaining, a)))
    if remaining < a:
        result.update(sequential(a - 1, remaining, chosen,
                                 probability * F(a - remaining, a)))
    return result
subsets = sequential(4, 2)
assert len(subsets) == comb(4, 2)
assert set(subsets.values()) == {F(1, 6)}

# Random height-two binary tree: singleton with probability 1-b, otherwise
# root plus two singleton children. Full traversal has zero conditional
# sampling variance, while true tree size still varies across trees.
b = F(1, 2)
mean_tree, variance_tree = moments([(1-b, F(1)), (b, F(3))])
assert (mean_tree, variance_tree) == (2, 1)
conditional_sampling_variance = F(0)
printed_variance = 1 + 8*b*1 + 2*b*0
correct_variance = 2*b*0 + 4*b*(1-b)*1**2
assert printed_variance == 5 and correct_variance == variance_tree

# Literal placement of the bp convolution inside b(1-p)/2 on scan p.10
# drops all branching mass at p=1. Moving it outside restores normalization.
p = F(1)
literal_probability_mass = (1-b) + b*(1-p)/2 * (2+b*p)
separated_probability_mass = (1-b) + b*(1-p) + b*p
assert literal_probability_mass == F(1, 2)
assert separated_probability_mass == 1
balance_p = 2 - 2*b
assert 4*b*b == 2*b*(2-balance_p)

print(json.dumps(dict(
    basic_sampling=basic,
    modified_mean=str(modified_mean), modified_variance=str(modified_variance),
    modified_work=str(modified_work), full_candidate_tests=full_test_count,
    feasible_nodes_excluding_root=feasible_nonroot_nodes,
    feasible_nodes_including_root=feasible_nonroot_nodes + 1,
    wrong_weight_mean=str(wrong_weight), omitted_test_cost_mean=str(wrong_omit_failed_tests),
    uniform_two_of_four_probability='1/6',
    full_traversal_conditional_sampling_variance=str(conditional_sampling_variance),
    across_tree_variance=str(variance_tree), printed_variance=str(printed_variance),
    literal_work_probability_mass=str(literal_probability_mass),
    separated_probability_mass=str(separated_probability_mass),
    balanced_p=str(balance_p),
    scope='Fixed finite constructed trees and the stated height-two random family. '
          'Work counts candidate tests, not wall-clock time. No universal schedule '
          'optimality, author-code behavior or benchmark replication asserted.'
), indent=2))
