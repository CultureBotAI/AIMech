"""Finite curator calculations; no author software or benchmark execution."""
from fractions import Fraction as F
from itertools import combinations, product
import json


def simple(values, k):
    values = sorted(values)
    if len(values) <= k:
        return [[v] for v in values]
    base, extra = divmod(len(values), k)
    out, start = [], 0
    for i in range(k):
        stop = start + base + (i < extra)
        out.append(values[start:stop])
        start = stop
    return out


def equal_dist(values, k, variant):
    values = sorted(values, reverse=variant > 1)
    if len(values) <= k:
        return [[v] for v in values]
    out, j, used = [], 0, F(0)
    total = sum(values)
    for i in range(k):
        group = []
        threshold = (total - used) / (k - i) if variant == 4 else (i + 1) * total / k
        if variant == 3:
            group.append(values[j])
            used += values[j]
            j += 1
        while (sum(group) if variant == 4 else used) < threshold:
            group.append(values[j])
            used += values[j]
            j += 1
        out.append(group)
    assert j == len(values)
    return out


def moments(targets, proposals, groups):
    choices = []
    for group in groups:
        if not group:
            continue
        mass = sum(proposals[i] for i in group)
        choices.append([(proposals[i] / mass, targets[i] * mass / proposals[i]) for i in group])
    mean, second = F(0), F(0)
    for draw in product(*choices):
        probability, estimate = F(1), F(0)
        for p, contribution in draw:
            probability *= p
            estimate += contribution
        mean += probability * estimate
        second += probability * estimate**2
    return mean, second - mean**2


def sse(group):
    center = sum(group) / len(group)
    return sum((x - center)**2 for x in group)


def ward_greedy(values, k):
    groups = [(v,) for v in values]
    while len(groups) > k:
        _, i, j = min((sse(groups[i] + groups[j]) - sse(groups[i]) - sse(groups[j]), i, j)
                      for i in range(len(groups)) for j in range(i + 1, len(groups)))
        merged = tuple(sorted(groups[i] + groups[j]))
        groups = [v for idx, v in enumerate(groups) if idx not in (i, j)] + [merged]
        groups.sort()
    return groups


values = list(map(F, ['1', '1.1', '1.2', '1.3', '1.4', '1.5', '10', '100']))
partitions = {'simpleVB': simple(values, 4)}
partitions.update({f'equalDistVB{i}': equal_dist(values, 4, i) for i in range(1, 5)})
assert list(map(len, partitions['equalDistVB1'])) == [8, 0, 0, 0]
assert list(map(len, partitions['equalDistVB2'])) == [1, 0, 0, 7]
assert list(map(len, partitions['equalDistVB3'])) == [1, 1, 1, 5]
assert list(map(len, partitions['equalDistVB4'])) == [1, 1, 3, 3]
assert partitions['equalDistVB4'][2] == list(map(F, ['1.5', '1.4', '1.3']))
assert simple(values[:2], 4) == [[F('1')], [F('1.1')]]
cuts = list(combinations(range(1, 8), 3))
assert len(cuts) == 35
assert all(len(set(c)) == 3 for c in cuts)

# Equal proxy values do not imply an exact proposal or zero estimator variance.
misleading = moments([F(1), F(9)], [F(1), F(1)], [[0, 1]])
oracle = moments([F(1), F(9)], [F(2), F(18)], [[0, 1]])
split = moments([F(1), F(9)], [F(1), F(1)], [[0], [1]])
assert misleading == (10, 64) and oracle == split == (10, 0)

# Three different node-value classes can induce different sorted orders.
h, r, wg = [F(1), F(2), F(3)], [F(10), F(1), F(1)], [F(1), F(10), F(1)]
scores = {'HB': h, 'HRB': [x*y for x, y in zip(h, r)],
          'QB': [x*y*z for x, y, z in zip(h, r, wg)]}
orders = {key: sorted(range(3), key=lambda i: score[i]) for key, score in scores.items()}
assert len({tuple(order) for order in orders.values()}) == 3

# Test the global-optimum interpretation of greedy Ward, not its author implementation.
counterexample = None
for xs in combinations(range(1, 13), 5):
    xs = tuple(map(F, xs))
    greedy = ward_greedy(xs, 2)
    greedy_sse = sum(map(sse, greedy))
    optimum, cut = min((sse(xs[:i]) + sse(xs[i:]), i) for i in range(1, len(xs)))
    if greedy_sse > optimum:
        counterexample = dict(values=xs, greedy=greedy, greedy_sse=greedy_sse,
                              better_groups=[xs[:cut], xs[cut:]], better_sse=optimum)
        break
assert counterexample

print(json.dumps(dict(partitions=partitions, singleton_when_cap_exceeds_count=simple(values[:2], 4),
                     random_ordered_cut_sets=len(cuts), value_class_orders=orders,
                     equal_proxy_mean_variance=misleading, proportional_oracle_mean_variance=oracle,
                     singleton_mean_variance=split, greedy_ward_counterexample=counterexample,
                     scope='Exact finite arithmetic for partition and estimator boundaries; no general proof, author-code execution, hardware experiment or benchmark replication.'),
                 default=str, indent=2))
