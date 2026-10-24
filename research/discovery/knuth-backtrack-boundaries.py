"""Constructed finite-tree checks for a prospective Knuth estimator record.
Not an author implementation, benchmark, or general proof certification.
"""
from fractions import Fraction as F
import json

# Explicit, immutable tree for exhaustive outcome enumeration.
tree = {'r': ['a', 'b'], 'a': [], 'b': ['c', 'd'], 'c': [], 'd': []}

def outcomes(node, cost, probabilities=None, use_degree_weights=False):
    kids = tree[node]
    if not kids:
        return [(F(1), F(cost[node]))]
    probs = probabilities.get(node) if probabilities and node in probabilities else [F(1, len(kids))] * len(kids)
    assert sum(probs) == 1 and all(p > 0 for p in probs)
    result = []
    for child, probability in zip(kids, probs):
        multiplier = len(kids) if use_degree_weights else 1 / probability
        for downstream_probability, downstream_estimate in outcomes(child, cost, probabilities, use_degree_weights):
            result.append((probability * downstream_probability, cost[node] + multiplier * downstream_estimate))
    return result

def moments(distribution):
    assert sum(p for p, _ in distribution) == 1
    mean = sum(p * x for p, x in distribution)
    variance = sum(p * (x - mean) ** 2 for p, x in distribution)
    return mean, variance

count_cost = dict.fromkeys(tree, F(1))
uniform = moments(outcomes('r', count_cost))
assert uniform == (5, 4)
importance = {'r': [F(1,4), F(3,4)]}
weighted = moments(outcomes('r', count_cost, importance))
wrong = moments(outcomes('r', count_cost, importance, True))
assert weighted == (5, 0) and wrong[0] == 6
leaf_cost = {n: F(not children) for n, children in tree.items()}
assert moments(outcomes('r', leaf_cost))[0] == 3
variable_cost = dict(r=F(2), a=F(1), b=F(3), c=F(4), d=F(5))
assert moments(outcomes('r', variable_cost))[0] == sum(variable_cost.values()) == 15
# Cost-preserving contraction of b includes its own cost and both children.
contracted_right_cost = variable_cost['b'] + variable_cost['c'] + variable_cost['d']
assert variable_cost['r'] + variable_cost['a'] + contracted_right_cost == 15
assert variable_cost['r'] + variable_cost['a'] + variable_cost['c'] + variable_cost['d'] == 12
# 999 shallow leaves and one child with 1000 terminal children.
rare = [(F(999,1000), F(1001)), (F(1,1000), F(1001001))]
rare_mean, rare_variance = moments(rare)
assert rare_mean == 2001 and rare_variance == 999000000
assert F(999,1000) ** 5 > F(99,100)
print(json.dumps(dict(uniform_mean=str(uniform[0]), uniform_variance=str(uniform[1]),
    positive_probability_mean=str(weighted[0]), oracle_probability_variance=str(weighted[1]),
    biased_selection_with_wrong_degree_weights=str(wrong[0]), leaf_count=3, weighted_cost_total=15,
    contraction_with_omitted_node_cost=12, rare_tree_size=str(rare_mean), rare_variance=str(rare_variance),
    five_probe_miss_probability=float(F(999,1000)**5),
    scope='Fixed finite trees, actual positive selection probabilities and additive costs. Oracle probabilities use known subtree totals; they are not a practical unknown-tree solution.'), indent=2))
