"""Exact finite Ward-criterion calculations; no clustering package execution."""
from fractions import Fraction as F
from itertools import combinations
import json


def mean(group):
    return sum(group) / len(group)


def ess(group):
    center = mean(group)
    return sum((x - center) ** 2 for x in group)


def increment(a, b):
    return F(len(a) * len(b), len(a) + len(b)) * (mean(a) - mean(b)) ** 2


def ward(values):
    groups = [(F(x),) for x in values]
    rows = [dict(groups=groups.copy(), ess=sum(map(ess, groups)), increment=F(0))]
    while len(groups) > 1:
        i, j = min(combinations(range(len(groups)), 2), key=lambda pair: (increment(groups[pair[0]], groups[pair[1]]), groups[pair[0]], groups[pair[1]]))
        cost = increment(groups[i], groups[j])
        merged = tuple(sorted(groups[i] + groups[j]))
        groups = sorted([g for k, g in enumerate(groups) if k not in (i, j)] + [merged])
        current = sum(map(ess, groups))
        assert current - rows[-1]['ess'] == cost
        rows.append(dict(groups=groups.copy(), ess=current, increment=cost))
    return rows


def recurrence_hierarchy(values, power):
    """Linear Ward recurrence with deliberately varied initial distance power."""
    groups = {i: (i,) for i in range(len(values))}
    sizes = {i: 1 for i in groups}
    ds = {(i, j): F(abs(values[i] - values[j]) ** power) for i, j in combinations(groups, 2)}
    trace = []
    fresh = len(values)
    def distance(i, j):
        return ds[tuple(sorted((i, j)))]
    while len(groups) > 1:
        a, b = min(combinations(sorted(groups), 2), key=lambda pair: (distance(*pair), groups[pair[0]], groups[pair[1]]))
        merged = tuple(sorted(groups[a] + groups[b]))
        trace.append(dict(merged_indices=merged, height=distance(a, b)))
        for c in list(groups):
            if c in (a, b):
                continue
            ds[c, fresh] = ((sizes[a] + sizes[c]) * distance(a, c)
                            + (sizes[b] + sizes[c]) * distance(b, c)
                            - sizes[c] * distance(a, b)) / (sizes[a] + sizes[b] + sizes[c])
        groups[fresh] = merged
        sizes[fresh] = sizes[a] + sizes[b]
        del groups[a]
        del groups[b]
        fresh += 1
    return trace


def main():
    example = ward([1, 7, 2, 9, 12])
    assert [r['ess'] for r in example] == [0, F(1, 2), F(5, 2), F(79, 6), F(434, 5)]
    counter = ward([1, 2, 3, 4, 6])
    two = next(r for r in counter if len(r['groups']) == 2)
    alternative = [(F(1), F(2), F(3)), (F(4), F(6))]
    assert two['ess'] == 5 and sum(map(ess, alternative)) == 4
    rows = []
    sets = [(F(0),), (F(1), F(3)), (F(2), F(4), F(8))]
    for a, b, c in [(sets[0], sets[1], sets[2]), (sets[1], sets[2], sets[0]), (sets[2], sets[0], sets[1])]:
        assert increment(a, b) == ess(a + b) - ess(a) - ess(b)
        total = len(a) + len(b) + len(c)
        recurrence = (F(len(a) + len(c), total) * 2 * increment(a, c)
                      + F(len(b) + len(c), total) * 2 * increment(b, c)
                      - F(len(c), total) * 2 * increment(a, b))
        direct = 2 * increment(a + b, c)
        assert recurrence == direct
        rows.append(dict(recurrence=recurrence, direct_twice_ess_increment=direct))
    a, b, c = (F(0),) * 100, (F(1),) * 100, (F(3),)
    costs = {'AB': increment(a, b), 'AC': increment(a, c), 'BC': increment(b, c)}
    assert min(costs, key=costs.get) == 'BC'
    ten = [F(x) for x in [2, 6, 5, 6, 2, 2, 2, 0, 0, 0]]
    assert ess(ten) == F(101, 2)
    inputs = [0, 1, 2, 5, 10]
    ordinary, squared = recurrence_hierarchy(inputs, 1), recurrence_hierarchy(inputs, 2)
    assert ordinary[2]["merged_indices"] == (3, 4)
    assert squared[2]["merged_indices"] == (0, 1, 2, 3)
    exact = ward(inputs)
    assert [r["height"] for r in squared] == [2 * r["increment"] for r in exact[1:]]
    print(json.dumps(dict(
        input_scale_example=dict(values=inputs, ordinary_input=ordinary, squared_input=squared),
        ward1963_ten_value_ess=ess(ten), ward1963_five_value_trace=example,
        greedy_counterexample=two, better_two_groups=alternative, better_ess=sum(map(ess, alternative)),
        recurrence_checks=rows, unequal_cardinality_costs=costs,
        nearest_centroids='AB', smallest_ess_increase='BC',
        limits='One-dimensional finite rational constructions, fixed lexicographic tie convention, no author-code execution or general performance claim.'
    ), default=lambda x: str(x), indent=2))


if __name__ == '__main__':
    main()
