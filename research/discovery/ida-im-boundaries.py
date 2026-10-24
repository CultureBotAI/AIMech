"""Constructed algebraic search-boundary examples, not author code or benchmarks."""
from collections import defaultdict
import json

def convolution(left, right):
    out = defaultdict(float)
    for value_a, mass_a in left.items():
        for value_b, mass_b in right.items():
            out[value_a + value_b] += mass_a * mass_b
    return dict(out)

# An exact uniform two-child tree: one edge of cost1 and one of cost2.
depth1 = convolution({0: 1}, {1: 1, 2: 1})
depth2 = convolution(depth1, {1: 1, 2: 1})
assert depth2 == {2: 1, 3: 2, 4: 1} and sum(depth2.values()) == 4
assert convolution({0: 1}, {1: .5, 2: .5}) == {1: .5, 2: .5}
# Offspring per parent sets mass growth; its reciprocal does not.
parents, offspring = 20, 60
assert offspring / parents == 3 and parents / offspring == 1 / 3

# Pooling increments loses a dependency on parent f absent from grouping features.
# Same selected type/distance, parents f0 and f10; respective child increments1,11.
actual = {1: 1, 21: 1}
pooled = convolution({0: 1, 10: 1}, {1: .5, 11: .5})
assert pooled == {1: .5, 11: 1, 21: .5} and pooled != actual
assert sum(pooled.values()) == sum(actual.values())

# A complete unit-cost binary tree admits cumulative counts1,3,7,..., not6.
contours = [2 ** (depth + 1) - 1 for depth in range(5)]
target = 2 * contours[1]
assert target == 6 and target not in contours

# Two goal leaves under an over-large threshold: traversal order can find7 before4.
threshold, ordered_goal_costs = 10, [7, 4]
first_goal = next(cost for cost in ordered_goal_costs if cost <= threshold)
incumbent = threshold
updates = []
for cost in ordered_goal_costs:
    if cost < incumbent:
        incumbent = cost
        updates.append(cost)
assert first_goal == 7 and incumbent == 4 and updates == [7, 4]

# A poor model cannot reduce a completed iteration's bound in the stated fallback.
previous, prediction, minimum_pruned = 3, 2.5, 4
next_bound = max(prediction, minimum_pruned)
assert next_bound > previous

print(json.dumps(dict(
    exact_uniform_convolution=depth2,
    branching_factor=offspring / parents,
    reciprocal_ratio=parents / offspring,
    nonuniform_actual=actual,
    pooled_increment_prediction=pooled,
    binary_tree_contour_counts=contours,
    unattainable_doubled_count=target,
    first_goal_under_large_threshold=first_goal,
    branch_and_bound_incumbents=updates,
    fallback_next_bound=next_bound,
    scope='Finite constructed arithmetic examples only; no author implementation, trained model, benchmark or unconditional completeness proof.'
), sort_keys=True))
