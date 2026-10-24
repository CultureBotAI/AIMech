"""Small exact graph examples for Brandes vertex-betweenness boundaries.

Curator code only: compare shortest-path dependency accumulation against
independent enumeration of simple paths on explicitly constructed positive-length
graphs. This is not execution of author software or a historical benchmark.
"""
from fractions import Fraction as F
from heapq import heappop, heappush
from itertools import combinations
import json


def graph(n, edges):
    adjacency = [[] for _ in range(n)]
    for u, v, length in edges:
        assert u != v and length > 0
        adjacency[u].append((v, F(length)))
        adjacency[v].append((u, F(length)))
    return adjacency


def enumerate_centrality(adjacency):
    n = len(adjacency)
    centrality = [F(0)] * n
    stress = [0] * n
    for source, target in combinations(range(n), 2):
        paths = []

        def visit(path, length):
            if path[-1] == target:
                paths.append((length, path))
                return
            for nxt, edge_length in adjacency[path[-1]]:
                if nxt not in path:
                    visit(path + [nxt], length + edge_length)

        visit([source], F(0))
        assert paths  # The constructed graphs are connected.
        distance = min(length for length, _ in paths)
        shortest = [path for length, path in paths if length == distance]
        for path in shortest:
            for vertex in path[1:-1]:
                centrality[vertex] += F(1, len(shortest))
                stress[vertex] += 1
    return centrality, stress


def accumulate(adjacency):
    n = len(adjacency)
    total = [F(0)] * n
    for source in range(n):
        distance = [None] * n
        distance[source] = F(0)
        counts = [0] * n
        counts[source] = 1
        predecessors = [[] for _ in range(n)]
        queue = [(F(0), source)]
        order = []
        while queue:
            length, vertex = heappop(queue)
            if distance[vertex] != length:
                continue
            order.append(vertex)
            for nxt, weight in adjacency[vertex]:
                candidate = length + weight
                if distance[nxt] is None or candidate < distance[nxt]:
                    distance[nxt] = candidate
                    counts[nxt] = 0
                    predecessors[nxt] = []
                    heappush(queue, (candidate, nxt))
                if candidate == distance[nxt]:
                    counts[nxt] += counts[vertex]
                    predecessors[nxt].append(vertex)
        dependency = [F(0)] * n
        for vertex in reversed(order):
            for prior in predecessors[vertex]:
                dependency[prior] += F(counts[prior], counts[vertex]) * (1 + dependency[vertex])
            if vertex != source:
                total[vertex] += dependency[vertex]
    return total, [value / 2 for value in total]


examples = {
    'three_vertex_path': graph(3, [(0, 1, 1), (1, 2, 1)]),
    'four_cycle': graph(4, [(0, 1, 1), (1, 3, 1), (3, 2, 1), (2, 0, 1)]),
    'weighted_tied_triangle': graph(3, [(0, 1, 1), (1, 2, 1), (0, 2, 2)]),
    'weighted_detour_triangle': graph(3, [(0, 1, 1), (1, 2, 1), (0, 2, 3)]),
    'unweighted_triangle': graph(3, [(0, 1, 1), (1, 2, 1), (0, 2, 1)]),
}
out = {}
for label, adjacency in examples.items():
    expected, stress = enumerate_centrality(adjacency)
    ordered, actual = accumulate(adjacency)
    assert actual == expected
    out[label] = dict(ordered_source_sum=list(map(str, ordered)),
                      unordered_betweenness=list(map(str, actual)),
                      unordered_stress=stress)
assert out['four_cycle']['unordered_betweenness'] == ['1/2'] * 4
assert out['four_cycle']['unordered_stress'] == [1] * 4
assert out['three_vertex_path']['unordered_betweenness'] == ['0', '1', '0']
assert out['weighted_tied_triangle']['unordered_betweenness'] == ['0', '1/2', '0']
assert out['weighted_detour_triangle']['unordered_betweenness'] == ['0', '1', '0']
assert out['unweighted_triangle']['unordered_betweenness'] == ['0'] * 3
out['single_diamond_successor_share'] = str(F(1, 2) * (1 + 0))
out['incorrect_reciprocal_share'] = str(F(2, 1) * (1 + 0))
out['scope'] = 'Exact finite examples on connected simple undirected positive-length graphs; no general complexity proof, author-code execution or empirical validation.'
print(json.dumps(out, indent=2))
