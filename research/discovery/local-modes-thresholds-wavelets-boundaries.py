"""Original finite checks of curation boundaries; no fitting or benchmark."""
from itertools import product
from fractions import Fraction as F
from math import exp, pi, sqrt, isclose
import json


def close(a, b):
    assert isclose(a, b, rel_tol=1e-11, abs_tol=1e-12), (a, b)


def icm_checks():
    weights = {(0, 0): 4, (0, 1): 2, (1, 0): 1, (1, 1): 3}

    def coordinate(x, i):
        candidates = [tuple(v if j == i else x[j] for j in range(2)) for v in (0, 1)]
        best = max(weights[y] for y in candidates)
        return x if weights[x] == best else next(y for y in candidates if weights[y] == best)

    def sweep(x, order):
        trace = [x]
        for i in order:
            x = coordinate(x, i)
            assert weights[x] >= weights[trace[-1]]
            trace.append(x)
        return trace

    left_first = sweep((0, 1), (0, 1))
    right_first = sweep((0, 1), (1, 0))
    assert left_first[-1] == (1, 1) and right_first[-1] == (0, 0)
    assert sweep((1, 1), (0, 1))[-1] == (1, 1)
    assert weights[(1, 1)] < max(weights.values())

    def synchronous(x):
        return tuple(coordinate(x, i)[i] for i in range(2))

    cycle = [(0, 1)]
    for _ in range(2):
        cycle.append(synchronous(cycle[-1]))
    assert cycle == [(0, 1), (1, 0), (0, 1)]
    assert weights[cycle[1]] < weights[cycle[0]]
    # A tied one-site posterior also cycles under an always-switch tie rule.
    tied_weights = {0: F(1, 2), 1: F(1, 2)}
    tied_cycle = [0]
    for _ in range(2):
        other = 1 - tied_cycle[-1]
        assert tied_weights[other] == max(tied_weights.values())
        tied_cycle.append(other)
    assert tied_cycle == [0, 1, 0]
    return dict(weights={str(k): v for k, v in weights.items()},
                left_first=left_first, right_first=right_first,
                synchronous_cycle=cycle, arbitrary_tie_cycle=tied_cycle)


def otsu_checks():
    # Four occupied gray levels in an otherwise empty integer-bin histogram.
    values = (0, 10, 11, 21)
    probabilities = (F(1, 4),) * 4
    mean = sum(p * x for x, p in zip(values, probabilities))
    total = sum(p * (x - mean) ** 2 for x, p in zip(values, probabilities))
    scores = {}
    for threshold in range(21):
        groups = [[(x, p) for x, p in zip(values, probabilities) if (x <= threshold) == flag]
                  for flag in (True, False)]
        masses = [sum(p for _, p in g) for g in groups]
        assert all(m > 0 for m in masses)
        means = [sum(x * p for x, p in g) / m for g, m in zip(groups, masses)]
        within = sum(p * (x - u) ** 2 for g, u in zip(groups, means) for x, p in g)
        between = sum(m * (u - mean) ** 2 for m, u in zip(masses, means))
        cumulative_mean = sum(x * p for x, p in groups[0])
        formula = (mean * masses[0] - cumulative_mean) ** 2 / (masses[0] * masses[1])
        assert formula == between and within + between == total
        scores[threshold] = between
    assert scores[0] == scores[11] == F(147, 4) > scores[10] == F(121, 4)
    maxima = [k for k, score in scores.items() if score == max(scores.values())]
    assert maxima == list(range(10)) + list(range(11, 21))
    # A constant histogram has no split with two nonempty classes.
    constant_histogram = {7: 4}
    valid_constant_splits = [k for k in range(8)
                            if 0 < sum(n for x, n in constant_histogram.items() if x <= k)
                            < sum(constant_histogram.values())]
    assert not valid_constant_splits
    # For three classes, exhaustively enumerate ordered cuts with nonempty groups.
    three = {}
    for a in range(21):
        for b in range(a + 1, 21):
            groups = [[x for x in values if lo < x <= hi]
                      for lo, hi in ((-1, a), (a, b), (b, 21))]
            if any(not g for g in groups):
                continue
            within = sum(sum((F(x) - sum(map(F, g)) / len(g)) ** 2 for x in g) / 4
                         for g in groups)
            three[(a, b)] = total - within
    assert max(three.values()) == F(441, 8)
    return dict(gray_values=values, total_variance=str(total),
                scores_at_0_10_11=[str(scores[k]) for k in (0, 10, 11)],
                maximizing_binary_thresholds=maxima,
                three_class_max_between_variance=str(max(three.values())))


def wavelet_tree_checks():
    # Three coefficient sites with a hidden root and two hidden children.
    root = (0.7, 0.3)
    transition = ((0.9, 0.1), (0.2, 0.8))  # [parent][child], intentionally asymmetric
    variances = (0.25, 4.0)
    observed = (0.2, 1.2, -0.4)
    states = list(product((0, 1), repeat=3))
    prior = {s: root[s[0]] * transition[s[0]][s[1]] * transition[s[0]][s[2]] for s in states}
    close(sum(prior.values()), 1.0)
    emission = [[exp(-x * x / (2 * v)) / sqrt(2 * pi * v) for v in variances]
                for x in observed]
    joint = {s: p * emission[0][s[0]] * emission[1][s[1]] * emission[2][s[2]]
             for s, p in prior.items()}
    evidence = sum(joint.values())
    posterior = {s: p / evidence for s, p in joint.items()}
    marginal = [[sum(p for s, p in posterior.items() if s[i] == m) for m in (0, 1)] for i in range(3)]
    messages = [[sum(transition[r][c] * emission[i][c] for c in (0, 1)) for r in (0, 1)]
                for i in (1, 2)]
    up = [emission[0][r] * messages[0][r] * messages[1][r] for r in (0, 1)]
    close(sum(root[r] * up[r] for r in (0, 1)), evidence)
    edges = []
    for child in (1, 2):
        sibling = 3 - child
        edge = [[root[r] * emission[0][r] * messages[sibling - 1][r]
                 * transition[r][c] * emission[child][c] / evidence for c in (0, 1)]
                for r in (0, 1)]
        for r, c in product((0, 1), repeat=2):
            enumerated = sum(p for s, p in posterior.items()
                             if s[0] == r and s[child] == c)
            close(edge[r][c], enumerated)
        for r in (0, 1):
            close(sum(edge[r]), marginal[0][r])
        for c in (0, 1):
            close(sum(edge[r][c] for r in (0, 1)), marginal[child][c])
        edges.append(edge)
    transposed_edge_mass = sum(root[r] * emission[0][r] * messages[1][r]
                               * transition[c][r] * emission[1][c] / evidence
                               for r, c in product((0, 1), repeat=2))
    assert abs(transposed_edge_mass - 1) > 0.01
    pooled_transition = [[sum(e[r][c] for e in edges) / (2 * marginal[0][r])
                          for c in (0, 1)] for r in (0, 1)]
    for row in pooled_transition:
        close(sum(row), 1)
    # Independent centered emissions imply zero cross-covariance, yet their squares depend.
    ev0 = sum(p * variances[s[0]] for s, p in prior.items())
    ev1 = sum(p * variances[s[1]] for s, p in prior.items())
    cross_square = sum(p * variances[s[0]] * variances[s[1]] for s, p in prior.items())
    square_covariance = cross_square - ev0 * ev1
    assert square_covariance > 1
    local_root = [root[r] * emission[0][r] for r in (0, 1)]
    local_high = local_root[1] / sum(local_root)
    assert abs(local_high - marginal[0][1]) > 0.01
    return dict(evidence_density=evidence, posterior_marginals=marginal,
                transposed_edge_mass=transposed_edge_mass, pooled_transition=pooled_transition,
                coefficient_cross_covariance=0, squared_coefficient_covariance=square_covariance,
                root_high_given_local_only=local_high)


if __name__ == '__main__':
    print(json.dumps(dict(icm=icm_checks(), otsu=otsu_checks(), wavelet_tree=wavelet_tree_checks()), indent=2))
