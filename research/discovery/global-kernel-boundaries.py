"""Finite curator checks for kernel k-means, graph shifts and seed variants.

These small examples are not the authors' software or benchmark reproduction.
The general singleton-removal bound is justified separately by an RKHS argument.
"""
import json
import math


def gram_dist(k, i, group, weights):
    total = sum(weights[j] for j in group)
    return (k[i][i] - 2 * sum(weights[j] * k[i][j] for j in group) / total
            + sum(weights[j] * weights[l] * k[j][l] for j in group for l in group) / total ** 2)


def objective(k, groups, weights):
    return sum(weights[i] * gram_dist(k, i, g, weights) for g in groups for i in g)


xs = [0.0, 2.0, 3.0, 9.0]
weights = [1.0, 2.0, 1.0, 3.0]
groups = [[0, 1, 2], [3]]
linear = [[x * y for y in xs] for x in xs]
direct = sum(weights[i] * (xs[i] - sum(weights[j] * xs[j] for j in g) /
                          sum(weights[j] for j in g)) ** 2 for g in groups for i in g)
assert math.isclose(objective(linear, groups, weights), direct)
assert math.isclose(objective(linear, groups, [7 * a for a in weights]), 7 * direct)
fast = []
for name, k in [('linear', linear), ('rbf', [[math.exp(-(x-y)**2 / 8) for y in xs] for x in xs])]:
    old_dist = [min(gram_dist(k, i, g, weights) for g in groups) for i in range(4)]
    old_e = sum(a*d for a, d in zip(weights, old_dist))
    for seed in groups[0]:
        bound_gain = sum(weights[i] * max(old_dist[i] -
                         (k[i][i] + k[seed][seed] - 2*k[i][seed]), 0) for i in range(4))
        initial = [[i for i in g if i != seed] for g in groups] + [[seed]]
        reassigned_cost = sum(weights[i] * min(gram_dist(k, i, g, weights)
                                               for g in initial) for i in range(4))
        assert reassigned_cost <= old_e - bound_gain + 1e-10
        fast.append(dict(kernel=name, seed=seed, old_objective=old_e,
                         comparison_upper_bound=old_e-bound_gain,
                         first_assignment_cost=reassigned_cost))

adj = [[1, 2, 0, 1], [2, 1, 1, 0], [0, 1, 1, 3], [1, 0, 3, 1]]
degrees = list(map(sum, adj))
partitions = [[[0, 1], [2, 3]], [[0, 2], [1, 3]], [[0], [1, 2, 3]]]
shifts = []
for mode in ['ratio_association', 'normalized_cut']:
    a = [1]*4 if mode == 'ratio_association' else degrees
    k = adj if mode == 'ratio_association' else [[adj[i][j]/degrees[i]/degrees[j]
                                                 for j in range(4)] for i in range(4)]
    shifted = [[k[i][j] + (5/a[i] if i == j else 0) for j in range(4)] for i in range(4)]
    for part in partitions:
        before = objective(k, part, a)
        after = objective(shifted, part, a)
        assert math.isclose(after-before, 5*(4-len(part)))
        if mode == 'normalized_cut':
            ncut = sum(sum(adj[i][j] for i in g for j in range(4) if j not in g) /
                       sum(degrees[i] for i in g) for g in part)
            constant = sum(adj[i][i]/degrees[i] for i in range(4))-len(part)
            assert math.isclose(before, ncut+constant)
        shifts.append(dict(mode=mode, partition=part, old_objective=before,
                           shifted_objective=after, additive_shift=after-before))

points = [0, .5, 2]
affinity = [[math.exp(-(x-y)**2) for y in points] for x in points]
q = [1/3]*3
trajectory = []
for iteration in range(6):
    z = [sum(s*v for s, v in zip(row, q)) for row in affinity]
    trajectory.append(dict(iteration=iteration, q=q, order=sorted(range(3), key=lambda j: (-q[j], j)),
                           log_score=sum(math.log(v) for v in z)/3))
    q = [q[j]*sum(affinity[i][j]/z[i] for i in range(3))/3 for j in range(3)]
    assert math.isclose(sum(q), 1)
assert trajectory[-1]['order'] == trajectory[-2]['order']
assert trajectory[-1]['log_score'] > trajectory[-2]['log_score']
assert trajectory[-1]['q'] != trajectory[-2]['q']
out = dict(weighted_gram_objective=direct, fast_bound_checks=fast, graph_shift_checks=shifts,
           cmm_ranking_last_two=trajectory[-2:],
           duplicate_zero_distortion=dict(two_identical_points_entropy=math.log(2),
                                          constant_output_mutual_information=0, distortion=0),
           interpretation='Finite checks only: weighted distances, scale invariance, singleton bounds, '
                          'fixed-count graph shift constants, and stable rankings before convergence.')
print(json.dumps(out, indent=2))
