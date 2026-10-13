"""Finite curator calculations; not the authors' implementation or a benchmark."""
from collections import Counter
from fractions import Fraction as F
from itertools import permutations, product
import json


def balanced(sequence, cap):
    assert 1 <= cap <= len(sequence)
    base, extras = divmod(len(sequence), cap)
    start = 0
    groups = []
    for i in range(cap):
        end = start + base + (i < extras)
        groups.append(tuple(sequence[start:end]))
        start = end
    assert start == len(sequence)
    return tuple(groups)


def canonical(groups):
    return tuple(sorted(tuple(sorted(g)) for g in groups))


def moments(groups, contributions, masses):
    outcomes = []
    for choices in product(*groups):
        probability, estimate = F(1), F(0)
        for group, node in zip(groups, choices):
            p = masses[node] / sum(masses[j] for j in group)
            probability *= p
            estimate += contributions[node] / p
        outcomes.append((probability, estimate))
    assert sum(p for p, _ in outcomes) == 1
    mean = sum(p * x for p, x in outcomes)
    variance = sum(p * (x - mean) ** 2 for p, x in outcomes)
    return mean, variance


def main():
    nodes = tuple(range(4))
    counts = Counter(canonical(balanced(order, 2)) for order in permutations(nodes))
    assert len(counts) == 3 and set(counts.values()) == {8}
    sorted_cut_groups = [canonical((nodes[:cut], nodes[cut:])) for cut in range(1, 4)]
    assert len(set(counts) & set(sorted_cut_groups)) == 1
    values = [F(x) for x in [1, 1, 9, 9]]
    uniform = [F(1)] * 4
    rows = []
    for groups, count in sorted(counts.items()):
        mean, variance = moments(groups, values, uniform)
        assert mean == 20
        rows.append(dict(groups=groups, permutations=count, mean=str(mean), variance=str(variance)))
    mean_variance = sum(F(count, 24) * moments(g, values, uniform)[1] for g, count in counts.items())
    assert mean_variance == F(256, 3)
    masses = [F(x) for x in [1, 2, 3, 4]]
    inclusion = [sum(F(count, 24) * masses[i] / sum(masses[j] for j in next(g for g in groups if i in g)) for groups, count in counts.items()) for i in nodes]
    assert sum(inclusion) == 2 and len(set(inclusion)) == 4
    conditional_mean, conditional_variance = moments(((0, 1),), [F(1), F(9)], [F(1), F(3)])
    assert (conditional_mean, conditional_variance) == (10, 12)
    invalid_probability_correction = F(1, 2) * (F(1) / F(1, 4) + F(9) / F(3, 4))
    assert invalid_probability_correction == 8
    size_cases = []
    for n in range(1, 21):
        for cap in range(1, n + 1):
            groups = balanced(tuple(range(n)), cap)
            sizes = list(map(len, groups))
            assert max(sizes) - min(sizes) <= 1
            assert sum(sizes) == n and len(groups) == cap and min(sizes) >= 1
            size_cases.append((n, cap))
    print(json.dumps(dict(
        balanced_cardinality_cases=len(size_cases), permutation_count=24,
        random_balanced_partitions=rows,
        sorted_random_cut_partitions=sorted_cut_groups,
        shared_partitions=1,
        uniform_representative_random_partition_variance=str(mean_variance),
        fixed_value_group_variance=str(moments(((0, 1), (2, 3)), values, uniform)[1]),
        weighted_representative_inclusion_probabilities=list(map(str, inclusion)),
        weighted_representative_inclusion_sum=str(sum(inclusion)),
        conditional_correction=dict(mean=str(conditional_mean), variance=str(conditional_variance)),
        uniform_choice_with_wrong_weighted_correction_mean=str(invalid_probability_correction),
        limits='Finite positive-mass examples and exhaustive small permutations only; no author software or empirical evaluation.'
    ), indent=2))


if __name__ == '__main__':
    main()
