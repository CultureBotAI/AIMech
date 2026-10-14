"""PageRank contraction argument and finite exact-arithmetic illustrations.

Curator argument, separate from the finite examples below: let P be a finite
nonnegative row-stochastic matrix, v a probability row vector, and 0 <= alpha < 1.
For any row vectors x and y, the triangle inequality gives

    sum_j |sum_i (x_i - y_i) P_ij|
    <= sum_i |x_i - y_i| sum_j P_ij = ||x - y||_1.

Consequently F(x) = alpha x P + (1-alpha) v contracts L1 distance by at most
alpha and maps the closed probability simplex into itself. This simplex is a
complete metric space, so the contraction mapping theorem gives a unique fixed
point and convergence of exact-arithmetic iteration from every probability
vector. Neither irreducibility of P nor strictly positive entries of v is needed.
The conclusion requires the stated probability domain and alpha below one.

The finite rational substitutions below illustrate boundary cases; they do not
prove the general contraction statement or guarantee finite-precision accuracy
or convergence within a specified max_iter. No external graph or library is run.
"""
from fractions import Fraction as F
import json


def step(x, matrix, alpha, restart):
    n = len(x)
    return [alpha * sum(x[i] * matrix[i][j] for i in range(n))
            + (1 - alpha) * restart[j] for j in range(n)]


def fixed(x, matrix, alpha, restart):
    assert sum(x) == 1 and all(t >= 0 for t in x)
    assert all(sum(row) == 1 and all(t >= 0 for t in row) for row in matrix)
    assert step(x, matrix, alpha, restart) == x
    return list(map(str, x))


half = F(1, 2)
uniform2 = [half, half]
cycle = [[F(0), F(1)], [F(1), F(0)]]
dangling_uniform = [[F(0), F(1)], uniform2]
sink = [[F(0), F(1)], [F(0), F(1)]]
identity = [[F(1), F(0)], [F(0), F(1)]]
four = [[F(int(j == dest)) for j in range(4)] for dest in [1, 0, 1, 2]]
rank4 = [F(5, 16), F(3, 8), F(3, 16), F(1, 8)]
assert rank4[0] != rank4[2]  # Both nodes have indegree one.
leaky = [[F(0), F(1)], [F(0), F(0)]]
lost = [F(1, 4), F(3, 8)]
assert step(lost, leaky, half, uniform2) == lost and sum(lost) == F(5, 8)
assert step([F(1), F(0)], cycle, F(1), uniform2) == [F(0), F(1)]
assert step([F(0), F(1)], cycle, F(1), uniform2) == [F(1), F(0)]
out = {
    "alpha": str(half),
    "equal_indegree_distinct_rank": {
        "edges": [[0, 1], [1, 0], [2, 1], [3, 2]],
        "indegrees": [1, 2, 1, 0],
        "stationary": fixed(rank4, four, half, [F(1, 4)] * 4),
    },
    "dangling_policy": {
        "graph": "0 -> 1; node 1 has no outgoing link",
        "restart": ["1/2", "1/2"],
        "uniform_redistribution": fixed([F(2, 5), F(3, 5)], dangling_uniform, half, uniform2),
        "redistribution_to_zero": fixed(uniform2, cycle, half, uniform2),
        "omitted_redistribution_fixed_mass": str(sum(lost)),
    },
    "personalization": {
        "graph": "0 -> 1; 1 -> 1",
        "uniform": fixed([F(1, 4), F(3, 4)], sink, half, uniform2),
        "restart_at_zero": fixed(uniform2, sink, half, [F(1), F(0)]),
        "restart_at_one": fixed([F(0), F(1)], sink, half, [F(0), F(1)]),
    },
    "reducible_transition": fixed([F(1), F(0)], identity, half, [F(1), F(0)]),
    "alpha_one_cycle_can_oscillate": True,
    "printed_uniform_baseline": "For stochastic P, r=(1-d)*1+d*r*P implies sum(r)=N when d != 1; p=r/N uses baseline (1-d)/N.",
    "scope": "Finite rational substitutions and normalization checks, not an implementation or historical benchmark reproduction.",
}
print(json.dumps(out, indent=2))
