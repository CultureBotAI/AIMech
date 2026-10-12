"""Exact LOF definition checks; not historical code or statistical evaluation."""
from fractions import Fraction as F
from itertools import combinations
import json


def lof(data, k, exact_k=False):
    n = len(data)
    assert 1 <= k <= n-1
    d = [[abs(x-y) for y in data] for x in data]
    ordered = [sorted((d[i][j], j) for j in range(n) if i != j)
               for i in range(n)]
    radius = [row[k-1][0] for row in ordered]
    neighbors = [([j for _, j in row[:k]] if exact_k else
                  [j for dist, j in row if dist <= radius[i]])
                 for i, row in enumerate(ordered)]
    reaches = [{j: max(radius[j], d[i][j]) for j in ns}
               for i, ns in enumerate(neighbors)]
    sums = [sum(row.values(), F(0)) for row in reaches]
    if any(v == 0 for v in sums):
        raise ArithmeticError('Zero mean reachability; no regularizer assumed.')
    densities = [F(len(ns), 1)/sums[i] for i, ns in enumerate(neighbors)]
    scores = [sum((densities[j]/densities[i] for j in ns), F(0))/len(ns)
              for i, ns in enumerate(neighbors)]
    return dict(radius=radius, neighbors=neighbors, reaches=reaches,
                densities=densities, scores=scores)


def main():
    x = [F(0), F(1), F(3)]
    a = lof(x, 1)
    b = lof(x, 2)
    assert a['scores'] == [F(1), F(1), F(2)]
    assert b['scores'] == [F(11, 12), F(6, 5), F(11, 12)]
    assert all(i not in ns for i, ns in enumerate(b['neighbors']))
    assert b['reaches'][0][1] == 2 > abs(x[0]-x[1])
    assert b['reaches'][0][1] != b['reaches'][1][0]
    assert lof([7*t+13 for t in x], 2)['scores'] == b['scores']
    assert lof([F(0), F(1000000)], 1)['scores'] == [1, 1]

    tied = lof([F(0), F(2), F(4), F(5)], 1)
    truncated = lof([F(0), F(2), F(4), F(5)], 1, exact_k=True)
    assert tied['neighbors'][1] == [0, 2]
    assert tied['scores'][1] == F(3, 2)
    assert truncated['scores'][1] == 1
    # Exact-k truncation has silently changed the original all-ties definition.
    try:
        lof([F(0), F(0), F(1)], 1)
    except ArithmeticError:
        duplicate_undefined = True
    else:
        duplicate_undefined = False
    assert duplicate_undefined

    def fixed_epsilon_scores(run, epsilon):
        density = [1/(1/v + epsilon) for v in run['densities']]
        return [sum((density[j]/density[i] for j in ns), F(0))/len(ns)
                for i, ns in enumerate(run['neighbors'])]
    epsilon = F(1, 10**10)
    assert fixed_epsilon_scores(b, epsilon) != fixed_epsilon_scores(
        lof([7*t for t in x], 2), epsilon)

    found = None
    for data in combinations(range(8), 5):
        runs = [lof(list(map(F, data)), k)['scores'] for k in range(1, 5)]
        for i in range(5):
            profile = [r[i] for r in runs]
            changes = [v-u for u, v in zip(profile, profile[1:])]
            if any(c > 0 for c in changes) and any(c < 0 for c in changes):
                found = dict(data=list(data), index=i,
                             scores_by_k_1_to_4=list(map(str, profile)))
                break
        if found:
            break
    assert found
    print(json.dumps(dict(
        self_excluded_and_asymmetric_neighbor_radius=True,
        k2_reachability_need_not_equal_raw_distance=True,
        scores_at_k1=list(map(str, a['scores'])),
        scores_at_k2=list(map(str, b['scores'])),
        scores_can_be_below_one_and_rankings_change=True,
        positive_uniform_scale_and_translation_invariant=True,
        isolated_pair_both_score_one=True,
        tie_inclusive_score='3/2', exact_k_truncation_score='1',
        zero_reachability_without_regularization_is_undefined=duplicate_undefined,
        fixed_additive_epsilon_breaks_exact_scale_invariance=True,
        nonmonotonic_k_example=found,
        scope='Exact finite rational calculations from Definitions3-7; no original implementation, learned model or benchmark executed.'
    ), indent=2))


if __name__ == '__main__':
    main()
