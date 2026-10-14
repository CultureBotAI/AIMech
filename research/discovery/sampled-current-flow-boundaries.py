"""Finite curator arithmetic for sampled-pair current-flow betweenness.

Enumerate independent pair draws, rather than executing author software.
The companion exact-current calculator supplies rational grounded solves.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import permutations, product
from math import ceil, exp, log
from pathlib import Path
import importlib.util
import json


def companion():
    local = Path(__file__).with_name('current-flow-boundaries.py')
    spec = importlib.util.spec_from_file_location('current_flow_examples', local)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def samples(n, edges, module):
    lap, cmat = module.grounded(n, edges)
    pairs = list(permutations(range(n), 2))
    rows = []
    for s, t in pairs:
        p = [row[s]-row[t] for row in cmat]
        b = [F(v==s)-F(v==t) for v in range(n)]
        assert [sum(lap[u][v]*p[v] for v in range(n)) for u in range(n)] == b
        tau = [F(0) for _ in range(n)]
        for u, v, conductance in edges:
            current = conductance*abs(p[u]-p[v])
            if u not in (s,t): tau[u] += current/2
            if v not in (s,t): tau[v] += current/2
        assert tau[s] == tau[t] == 0 and all(0 <= x <= 1 for x in tau)
        rows.append([F(n,n-2)*x for x in tau])
    return pairs, rows


def main():
    module = companion()
    cases = {
        'path3': (3, [(0,1,F(1)),(1,2,F(1))]),
        'path4': (4, [(0,1,F(1)),(1,2,F(1)),(2,3,F(1))]),
        'weighted_triangle': (3, [(0,1,F(1)),(1,2,F(2)),(2,0,F(3))]),
    }
    results = {}
    for name, (n, edges) in cases.items():
        pairs, rows = samples(n, edges, module)
        exact = module.sorted_rows(n, edges)
        mean = [sum(row[v] for row in rows)/len(rows) for v in range(n)]
        assert mean == exact
        sequences = list(product(range(len(rows)), repeat=2))
        averages = [[(rows[i][v]+rows[j][v])/2 for v in range(n)] for i,j in sequences]
        assert [sum(row[v] for row in averages)/len(averages) for v in range(n)] == exact
        assert samples(n, [(u,v,7*c) for u,v,c in edges], module)[1] == rows
        results[name] = dict(pair_count=len(pairs), exact=exact,
                             single_draw_expectation=mean, two_draw_sequence_count=len(sequences))
        if name == 'path3':
            distribution = Counter(row[1] for row in averages)
            probabilities = {str(k): F(v,len(averages)) for k,v in sorted(distribution.items())}
            assert probabilities == {'0':F(4,9), '3/2':F(4,9), '3':F(1,9)}
            clipped = sum(min(F(1),row[1]) for row in averages)/len(averages)
            assert clipped == F(5,9) != exact[1]
            repeated_pair = rows[pairs.index((0,2))]
            assert repeated_pair == [F(0),F(3),F(0)]
            results[name].update(two_draw_middle_distribution=probabilities,
                                 probability_middle_estimate_above_one=F(5,9),
                                 hypothetical_clipped_expectation=clipped,
                                 repeated_pair_for_k_equal_pair_count=repeated_pair,
                                 note='Clipping is a hypothetical altered estimator, not adopted.')
    n = 3; epsilon = F(1,2); delta = F(1,20); scale = F(n,n-2)
    k = ceil(float(scale**2/(2*epsilon**2))*log(2*n/float(delta)))
    bound = 2*n*exp(-2*k*float((epsilon/scale)**2))
    assert k == 87 and bound <= float(delta)
    return dict(cases=results, sufficient_sample_count=dict(n=n,epsilon=epsilon,
                failure_probability=delta,k=k,union_bound=bound),
                scope='Finite exact-current iid pair enumeration and explicit sufficient-bound algebra; no clipping, author software, numerical-solver guarantee or empirical benchmark.')


if __name__ == '__main__':
    print(json.dumps(main(), indent=2, default=str))
