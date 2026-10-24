"""Exact finite curator checks of random-walk centrality, not source-experiment replication."""
from fractions import Fraction as F
import json


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def inverse(a):
    n = len(a)
    z = [list(row) + eye for row, eye in zip(a, identity(n))]
    for col in range(n):
        pivot = next(i for i in range(col, n) if z[i][col])
        z[col], z[pivot] = z[pivot], z[col]
        scale = z[col][col]
        z[col] = [v / scale for v in z[col]]
        for i in range(n):
            if i != col:
                scale = z[i][col]
                z[i] = [v - scale * w for v, w in zip(z[i], z[col])]
    return [row[n:] for row in z]


def transition(n, edges):
    adj = [set() for _ in range(n)]
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)
    degrees = list(map(len, adj))
    assert all(degrees)
    p = [[F(int(j in adj[i]), degrees[i]) for j in range(n)] for i in range(n)]
    pi = [F(d, sum(degrees)) for d in degrees]
    assert all(pi[i] * p[i][j] == pi[j] * p[j][i] for i in range(n) for j in range(n))
    return p, pi, degrees


def inspect(n, edges):
    p, pi, degrees = transition(n, edges)
    eye = identity(n)
    projection = [list(pi) for _ in range(n)]
    z = inverse([[eye[i][j] - p[i][j] + pi[j] for j in range(n)] for i in range(n)])
    r = [[z[i][j] - pi[j] for j in range(n)] for i in range(n)]
    assert multiply([[eye[i][j] - p[i][j] for j in range(n)] for i in range(n)], r) == [[eye[i][j] - pi[j] for j in range(n)] for i in range(n)]
    assert multiply(r, projection) == [[0] * n for _ in range(n)]
    tau = [r[i][i] for i in range(n)]
    assert all(t > 0 for t in tau)
    centrality = [pi[i] / tau[i] for i in range(n)]
    h = [[F(0)] * n for _ in range(n)]
    # Solve the independent absorbing-target equations h_i=1+sum P_ik h_k.
    for target in range(n):
        transient = [i for i in range(n) if i != target]
        inv = inverse([[F(i == j) - p[i][j] for j in transient] for i in transient])
        for row, i in enumerate(transient):
            h[i][target] = sum(inv[row])
            assert h[i][target] == (r[target][target] - r[i][target]) / pi[target]
        # Positive return convention includes one initial transition.
        h[target][target] = 1 + sum(p[target][j] * h[j][target] for j in transient)
        assert h[target][target] == 1 / pi[target]
    for i in range(n):
        for j in range(n):
            if i != j:
                assert h[i][j] - h[j][i] == 1 / centrality[j] - 1 / centrality[i]
    return dict(degrees=degrees,stationary=list(map(str, pi)),tau=list(map(str, tau)),centrality=list(map(str, centrality)),mean_hitting_or_positive_return=[[str(x) for x in row] for row in h])


def main():
    triangle = inspect(3, [(0, 1), (1, 2), (2, 0)])
    assert triangle['centrality'] == ['3/4'] * 3
    asymmetric = inspect(5, [(0, 1), (1, 2), (2, 0), (0, 3), (3, 4)])
    assert asymmetric['degrees'][1] == asymmetric['degrees'][3] and asymmetric['centrality'][1] != asymmetric['centrality'][3]
    # The ordinary deviation series fails on the bipartite4-cycle.
    p, pi, _ = transition(4, [(0, 1), (1, 2), (2, 3), (3, 0)])
    power = identity(4)
    total = F(0)
    sums = []
    terms = []
    for _ in range(8):
        term = power[0][0] - pi[0]
        terms.append(str(term))
        total += term
        sums.append(str(total))
        power = multiply(power, p)
    assert sums == ['3/4','1/2','3/4','1/2','3/4','1/2','3/4','1/2']
    return dict(triangle=triangle,triangle_with_two_edge_tail=asymmetric,bipartite_four_cycle=dict(deviation_terms=terms,partial_sums=sums,ordinary_series_converges=False),scope='Exact rational finite checks. Inverse representation is curator mathematics equivalent to the convergent deviation series on the two connected non-bipartite examples. No source code, simulation replication, directed extension or universal early-arrival probability claim.')


if __name__ == '__main__':
    print(json.dumps(main(), indent=2))
