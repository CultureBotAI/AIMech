"""Curator rational examples for current-flow centrality; no author software.

Compute each ordered-pair current directly and compare its throughput average
with Algorithm 1's sorted current rows. Exact fractions avoid solver tolerance.
These are finite mechanism/notation checks, not general complexity proofs.
"""
from fractions import Fraction as F
from itertools import permutations
import json


def inverse(matrix):
    n = len(matrix)
    aug = [[F(x) for x in row]+[F(i==j) for j in range(n)]
           for i, row in enumerate(matrix)]
    for i in range(n):
        p = next(j for j in range(i, n) if aug[j][i])
        aug[i], aug[p] = aug[p], aug[i]
        divisor = aug[i][i]
        aug[i] = [x/divisor for x in aug[i]]
        for j in range(n):
            if j != i:
                factor = aug[j][i]
                aug[j] = [a-factor*b for a, b in zip(aug[j], aug[i])]
    result = [row[n:] for row in aug]
    assert all(sum(matrix[i][k]*result[k][j] for k in range(n)) == F(i==j)
               for i in range(n) for j in range(n))
    return result


def grounded(n, edges, ground=0):
    lap = [[F(0) for _ in range(n)] for _ in range(n)]
    for u, v, c in edges:
        assert c > 0 and u != v
        lap[u][u] += c; lap[v][v] += c
        lap[u][v] -= c; lap[v][u] -= c
    vertices = [v for v in range(n) if v != ground]
    reduced = [[lap[u][v] for v in vertices] for u in vertices]
    inv = inverse(reduced)
    result = [[F(0) for _ in range(n)] for _ in range(n)]
    for i, u in enumerate(vertices):
        for j, v in enumerate(vertices):
            result[u][v] = inv[i][j]
    return lap, result


def direct(n, edges, ground=0):
    lap, cmat = grounded(n, edges, ground)
    totals = [F(0) for _ in range(n)]
    resistances = [[F(0) for _ in range(n)] for _ in range(n)]
    for s, t in permutations(range(n), 2):
        potential = [row[s]-row[t] for row in cmat]
        supply = [F(v==s)-F(v==t) for v in range(n)]
        assert [sum(lap[u][v]*potential[v] for v in range(n))
                for u in range(n)] == supply
        absolute = [F(0) for _ in range(n)]
        net = [F(0) for _ in range(n)]
        for u, v, c in edges:
            current = c*(potential[u]-potential[v])
            absolute[u] += abs(current); absolute[v] += abs(current)
            net[u] += current; net[v] -= current
        assert net == supply
        throughput = [(absolute[v]-abs(supply[v]))/2 for v in range(n)]
        assert throughput[s] == throughput[t] == 0
        assert all(0 <= x <= 1 for x in throughput)
        totals = [a+b for a, b in zip(totals, throughput)]
        resistances[s][t] = potential[s]-potential[t]
    between = [x/((n-1)*(n-2)) for x in totals]
    closeness = [F(n-1)/sum(row) for row in resistances]
    return between, closeness, cmat


def sorted_rows(n, edges, ground=0, reverse_ties=False):
    _, cmat = grounded(n, edges, ground)
    totals = [F(0) for _ in range(n)]
    for u, v, conductance in edges:
        row = [conductance*(cmat[u][j]-cmat[v][j]) for j in range(n)]
        order = sorted(range(n), key=lambda j: (-row[j], -j if reverse_ties else j))
        ranks = {j: r+1 for r, j in enumerate(order)}
        for j, value in enumerate(row):
            i = j+1
            totals[u] += (i-ranks[j])*value
            totals[v] += (n+1-i-ranks[j])*value
    return [(value-j)*2/((n-1)*(n-2)) for j, value in enumerate(totals)]


def main():
    cases = {'path4': (4, [(0,1,F(1)),(1,2,F(1)),(2,3,F(1))]),
             'triangle': (3, [(0,1,F(1)),(1,2,F(1)),(2,0,F(1))]),
             'weighted_triangle': (3, [(0,1,F(1)),(1,2,F(2)),(2,0,F(3))]),
             'square_diagonal': (4, [(0,1,F(1)),(1,2,F(2)),(2,3,F(3)),(3,0,F(4)),(0,2,F(2))])}
    results = {}
    for name, (n, edges) in cases.items():
        exact, closeness, cmat = direct(n, edges)
        assert exact == sorted_rows(n, edges)
        for root in range(n):
            assert direct(n, edges, root)[:2] == (exact, closeness)
            assert sorted_rows(n, edges, root) == exact
            assert sorted_rows(n, edges, root, True) == exact
        assert sorted_rows(n, [(v,u,c) for u,v,c in edges]) == exact
        assert direct(n, [(u,v,7*c) for u,v,c in edges])[:2] == (exact,[7*x for x in closeness])
        for p in permutations(range(n)):
            remapped = [(p[u],p[v],c) for u,v,c in edges]
            changed = sorted_rows(n, remapped)
            assert [changed[p[u]] for u in range(n)] == exact
        # Algorithm2 computes inverse SUM resistance rather than n-1 times it.
        raw_closeness = [1/sum(cmat[u][u]+cmat[v][v]-2*cmat[u][v]
                              for v in range(n)) for u in range(n)]
        assert closeness == [(n-1)*x for x in raw_closeness]
        results[name] = dict(betweenness=exact, normalized_closeness=closeness,
                             algorithm2_inverse_sum=raw_closeness)
    assert results['path4']['betweenness'] == [F(0),F(2,3),F(2,3),F(0)]
    assert results['triangle']['betweenness'] == [F(1,3)]*3
    assert results['weighted_triangle']['betweenness'] == [F(3,11),F(2,11),F(6,11)]
    _, _, cmat = direct(*cases['weighted_triangle'])
    potential = [row[0]-row[1] for row in cmat]
    currents = [c*(potential[u]-potential[v]) for u,v,c in cases['weighted_triangle'][1]]
    voltage_sum = sum(i/c for i, (_,_,c) in zip(currents,cases['weighted_triangle'][1]))
    assert sum(currents) == -F(7,11) and voltage_sum == 0
    return dict(cases=results, weighted_cycle=dict(currents=currents,
                sum_current=sum(currents), sum_current_divided_by_conductance=voltage_sum),
                invariance='Ground vertex, orientation, tie order, vertex relabeling and common conductance scaling checked on four finite graphs.',
                scope='Curator exact arithmetic; no author implementation, stochastic approximation, numerical solver benchmark or general proof by finite enumeration.')


if __name__ == '__main__':
    print(json.dumps(main(), indent=2, default=str))
