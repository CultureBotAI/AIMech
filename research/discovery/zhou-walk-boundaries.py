"""Finite exact curator checks of Zhou's two random-walk constructions."""
from fractions import Fraction as F
from itertools import combinations, product
import json


def inverse(a):
    n = len(a)
    z = [list(row) + [F(i == j) for j in range(n)] for i, row in enumerate(a)]
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


def connected(a):
    seen = {0}
    pending = [0]
    while pending:
        i = pending.pop()
        for j, weight in enumerate(a[i]):
            if weight and j not in seen:
                seen.add(j)
                pending.append(j)
    return len(seen) == len(a)


def distance(a):
    n = len(a)
    strengths = list(map(sum, a))
    assert connected(a) and all(strengths)
    p = [[F(v, strengths[i]) for v in row] for i, row in enumerate(a)]
    d = [[F(0)] * n for _ in range(n)]
    for target in range(n):
        # Source equation zeroes the TARGET COLUMN, not the target row.
        killed = [[F(i == j) - (p[i][j] if j != target else 0) for j in range(n)] for i in range(n)]
        inv = inverse(killed)
        for i in range(n):
            d[i][target] = sum(inv[i])
        # Independent absorbing-target solve excludes the target coordinate.
        others = [i for i in range(n) if i != target]
        reduced = inverse([[F(i == j) - p[i][j] for j in others] for i in others])
        for row, i in enumerate(others):
            assert d[i][target] == sum(reduced[row])
        assert d[target][target] == 1 + sum(p[target][i] * d[i][target] for i in others)
        assert d[target][target] == F(sum(strengths), strengths[target])
    return d


def components(arrows):
    n = len(arrows)
    adjacency = [set(row) for row in arrows]
    for i, row in enumerate(arrows):
        for j in row:
            adjacency[j].add(i)
    unseen = set(range(n))
    out = []
    while unseen:
        part = {min(unseen)}
        todo = list(part)
        while todo:
            for j in adjacency[todo.pop()]:
                if j not in part:
                    part.add(j)
                    todo.append(j)
        unseen -= part
        out.append(sorted(part))
    return out


def attractors(a, d, local):
    out = []
    for i, row in enumerate(d):
        candidates = [j for j in range(len(a)) if not local or a[i][j] > 0]
        best = min(row[j] for j in candidates)
        out.append([j for j in candidates if row[j] == best])
    return out


def dissimilarity_squared(d, i, j):
    n = len(d)
    assert n > 2 and i != j
    # PDF equation1 has (N-2) OUTSIDE the radical.
    return sum((d[i][k] - d[j][k]) ** 2 for k in range(n) if k not in [i, j]) / (n - 2) ** 2


def adjacency(n, edges):
    a = [[0] * n for _ in range(n)]
    for i, j, w in edges:
        a[i][j] = a[j][i] = w
    return a


def main():
    count = 0
    crossing = None
    edge_pairs = list(combinations(range(4), 2))
    for weights in product([0, 1, 2], repeat=len(edge_pairs)):
        a = adjacency(4, [(i, j, w) for (i, j), w in zip(edge_pairs, weights)])
        if not connected(a):
            continue
        d = distance(a)
        local = components(attractors(a, d, True))
        glob = components(attractors(a, d, False))
        if crossing is None and any(not any(set(part) <= set(g) for g in glob) for part in local):
            crossing = dict(adjacency=a,local=local,global_partition=glob)
        count += 1
    chain = adjacency(3, [(0, 1, 1), (1, 2, 1)])
    cd = distance(chain)
    assert cd == [[4, 1, 4], [3, 2, 3], [4, 1, 4]]
    ga = attractors(chain, cd, False)
    assert ga == [[1], [1], [1]] and components(ga) == [[0, 1, 2]]
    zero = [list(row) for row in cd]
    for i in range(3):
        zero[i][i] = F(0)
    assert components(attractors(chain, zero, False)) == [[0], [1], [2]]
    cycle = adjacency(4, [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 0, 1)])
    d = distance(cycle)
    la = attractors(cycle, d, True)
    assert la == [[1, 3], [0, 2], [1, 3], [0, 2]]
    assert components(la) == [[0, 1, 2, 3]]
    assert components([[1], [0], [3], [2]]) == [[0, 1], [2, 3]]
    assert dissimilarity_squared(d, 0, 1) == F(1, 2)
    root_mean_square_squared = sum((d[0][k] - d[1][k]) ** 2 for k in [2, 3]) / 2
    assert root_mean_square_squared == 1
    complete = adjacency(4, [(i, j, 1) for i, j in edge_pairs])
    kd = distance(complete)
    assert dissimilarity_squared(kd, 0, 1) == 0
    scaled = [[5 * w for w in row] for row in cycle]
    assert distance(scaled) == d
    # A reachable friend partition can oscillate under simultaneous adjustment.
    trap = adjacency(4, [(i, j, 1 if (i, j) in [(0, 1), (2, 3)] else 2) for i, j in edge_pairs])
    td = distance(trap)
    assert dissimilarity_squared(td, 0, 1) == dissimilarity_squared(td, 2, 3) == 0
    cross_squared = dissimilarity_squared(td, 0, 2)
    assert cross_squared > 0
    labels = [0, 0, 1, 1]
    steps = [list(labels)]
    for _ in range(2):
        updated = []
        for i in range(4):
            own = sum(trap[i][j] for j in range(4) if labels[j] == labels[i] and j != i)
            other = sum(trap[i][j] for j in range(4) if labels[j] != labels[i])
            assert own == 1 and other == 4
            updated.append(1 - labels[i])
        labels = updated
        steps.append(list(labels))
    assert steps == [[0, 0, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1]]
    hierarchy_cycle = dict(adjacency=trap,within_pair_index_squared='0',cross_pair_index_squared=str(cross_squared),threshold='Any nonnegative threshold below the cross-pair index produces friend sets {0,1} and {2,3}.',synchronous_label_steps=steps,own_weight='1',other_community_weight='4',interpretation='Every vertex remains strictly unstable. Labels swap simultaneously; the unlabeled partition is unchanged and step4 does not reach its stated stopping condition.')
    assert count == 624
    return dict(enumeration=dict(connected_four_vertex_weighted_graphs=count,target_equations_checked=4*count,arc_weights=[0,1,2]),chain=dict(distance=[[str(x) for x in row] for row in cd],global_attractors=ga,source_global_partition=components(ga),incorrect_zero_diagonal_partition=components(attractors(chain,zero,False))),cycle=dict(distance=[[str(x) for x in row] for row in d],local_attractors=la,all_tie_partition=components(la),arbitrary_tie_partition=components([[1],[0],[3],[2]]),source_index_squared='1/2',root_mean_square_squared=str(root_mean_square_squared)),complete_four=dict(distinct_adjacent_index_squared='0'),local_global_nesting_counterexample=crossing,hierarchy_simultaneous_cycle=hierarchy_cycle,scope='Exact finite curator arithmetic. First-passage solves work for periodic connected walks and do not require convergence of ordinary state probabilities. No author-code execution, complete source hierarchy implementation, biological validation or benchmark replication.')


if __name__ == '__main__':
    print(json.dumps(main(), indent=2))
