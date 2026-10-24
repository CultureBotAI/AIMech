"""Finite curator calculations; not author software or an empirical benchmark.

The vectors below are explicitly scaled to sum one, following the paper's
experimental comparison. Common positive extrapolation factors cancel in these
vectors. Neither that cancellation nor the finite examples establish statistical
unbiasedness, a confidence guarantee, or monotonic improvement in accuracy.
"""
from collections import deque
from fractions import Fraction as F
from itertools import combinations
import json
import math


def traversals(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        assert a != b and b not in adj[a]
        adj[a].append(b)
        adj[b].append(a)
    distances, dependencies = [], []
    for source in range(n):
        d = [-1] * n
        count = [0] * n
        pred = [[] for _ in range(n)]
        d[source], count[source] = 0, 1
        q, order = deque([source]), []
        while q:
            v = q.popleft()
            order.append(v)
            for w in adj[v]:
                if d[w] == -1:
                    d[w] = d[v] + 1
                    q.append(w)
                if d[w] == d[v] + 1:
                    count[w] += count[v]
                    pred[w].append(v)
        assert all(x >= 0 for x in d)
        delta = [F(0)] * n
        for w in reversed(order):
            for v in pred[w]:
                delta[v] += F(count[v], count[w]) * (1 + delta[w])
        delta[source] = F(0)  # endpoints excluded
        distances.append(d)
        dependencies.append(delta)
    return distances, dependencies


def enumerate_paths(n, edges):
    # Independent finite construction: visit all simple paths, then retain the
    # shortest and count their internal vertices. No recurrence or BFS is used.
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    dist, dependencies = [], []
    for source in range(n):
        row, delta = [0] * n, [F(0)] * n
        for target in range(n):
            if target == source:
                continue
            paths = []
            def visit(path):
                if path[-1] == target:
                    paths.append(path)
                    return
                for w in adj[path[-1]]:
                    if w not in path:
                        visit(path + [w])
            visit([source])
            best = min(len(p) for p in paths)
            chosen = [p for p in paths if len(p) == best]
            row[target] = best - 1
            for path in chosen:
                for v in path[1:-1]:
                    delta[v] += F(1, len(chosen))
        dist.append(row)
        dependencies.append(delta)
    return dist, dependencies


def normalized(values):
    total = sum(values)
    return [v / total for v in values] if total else None


def estimate(d, dep, pivots):
    n = len(d)
    assert len(set(pivots)) == len(pivots) >= 1
    sums = [sum(d[p][v] for p in pivots) for v in range(n)]
    closeness = normalized([F(1, x) for x in sums]) if all(sums) else None
    partial = [sum((dep[p][v] for p in pivots), F(0)) for v in range(n)]
    return dict(closeness=closeness, betweenness=normalized(partial), dependency_sum=partial)


def main():
    d, dep = traversals(4, [(0, 1), (1, 2), (2, 3)])
    assert (d, dep) == enumerate_paths(4, [(0, 1), (1, 2), (2, 3)])
    exact = estimate(d, dep, range(4))
    assert exact['closeness'] == [F(1, 5), F(3, 10), F(3, 10), F(1, 5)]
    assert exact['betweenness'] == [F(0), F(1, 2), F(1, 2), F(0)]
    partial = estimate(d, dep, [0, 1])
    assert partial['closeness'] == [F(15, 38), F(15, 38), F(5, 38), F(3, 38)]
    assert partial['betweenness'] == [F(0), F(1, 2), F(1, 2), F(0)]
    alternate = estimate(d, dep, [0, 2])
    assert alternate['betweenness'] == [F(0), F(3, 4), F(1, 4), F(0)]
    assert alternate['closeness'] == [F(2, 7), F(2, 7), F(2, 7), F(1, 7)]
    # Exhaust all six size-two subsets; explicitly distinguish raw extrapolation
    # from the manuscript's n/(n-1) per-pivot factor and sum-one output.
    subsets = list(combinations(range(4), 2))
    means = [sum((F(4, 2) * sum(dep[p][v] for p in ps) for ps in subsets), F(0)) / len(subsets) for v in range(4)]
    assert means == exact['dependency_sum']
    source_scaled_mean = [sum((F(4, 3) * dep[p][v] for p in range(4)), F(0)) / 4 for v in range(4)]
    assert source_scaled_mean == [x / 3 for x in exact['dependency_sum']]
    assert normalized(source_scaled_mean) == exact['betweenness']
    assert estimate(d, dep, [0])['closeness'] is None
    td, tp = traversals(3, [(0, 1), (1, 2), (0, 2)])
    assert (td, tp) == enumerate_paths(3, [(0, 1), (1, 2), (0, 2)])
    assert estimate(td, tp, [0, 1])['betweenness'] is None
    # Literal absolute-tail display on manuscript p.7 fails on this elementary
    # iid example. This is not an audit of an unseen final version or author code.
    bernoulli_tail = F(1)  # |X-E X| >= 1/2 for X equally likely 0 or 1
    printed_rhs = math.exp(-2 * (0.5 ** 2))
    assert bernoulli_tail > printed_rhs
    print(json.dumps(dict(path4_exact=exact, path4_pivots_0_1=partial, path4_pivots_0_2=alternate,
        all_six_uniform_two_pivot_subsets_raw_mean=means,
        manuscript_scaled_all_pivot_mean=source_scaled_mean,
        singleton_pivot_closeness='undefined at that pivot before a separate policy',
        complete_graph_sum_one_betweenness='undefined because every dependency is zero',
        printed_two_sided_tail_example=dict(actual_probability=str(bernoulli_tail), printed_bound=printed_rhs),
        scope='Finite exact examples plus one scalar probability counterexample; no author code, benchmark, general error theorem or statistical guarantee for normalized scores.'), default=str))


if __name__ == '__main__':
    main()
