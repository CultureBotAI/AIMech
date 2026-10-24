"""Finite curator arithmetic for RK path sampling; no author-code or confidence certification."""
from fractions import Fraction
from itertools import permutations, product
import heapq
import json
import math


def shortest_paths_by_enumeration(graph, source, target):
    found = []
    def visit(path, weight):
        v = path[-1]
        if v == target:
            found.append((weight, tuple(path)))
            return
        for w, cost in graph[v].items():
            if w not in path:
                visit(path + [w], weight + cost)
    visit([source], 0)
    if not found:
        return []
    best = min(w for w, _ in found)
    return sorted(p for w, p in found if w == best)


def predecessor_path_law(graph, source, target, uniform_predecessors=False):
    """Dijkstra plus complete equal-distance counts, then exact weighted backtracking."""
    n = len(graph)
    dist = [math.inf] * n
    count = [0] * n
    pred = [[] for _ in graph]
    dist[source] = 0
    count[source] = 1
    heap = [(0, source)]
    while heap:
        dv, v = heapq.heappop(heap)
        if dv != dist[v]:
            continue
        for w, cost in graph[v].items():
            assert cost > 0
            d = dv + cost
            if d < dist[w]:
                dist[w] = d
                count[w] = count[v]
                pred[w] = [v]
                heapq.heappush(heap, (d, w))
            elif d == dist[w]:
                count[w] += count[v]
                pred[w].append(v)
    if not count[target]:
        return {(): Fraction(1)}
    law = {}
    def backtrack(v, suffix, probability):
        if v == source:
            law[tuple([source] + suffix)] = probability
            return
        for p in pred[v]:
            factor = Fraction(1, len(pred[v])) if uniform_predecessors else Fraction(count[p], count[v])
            backtrack(p, [v] + suffix, probability * factor)
    backtrack(target, [], Fraction(1))
    return law


def main():
    pairs = list(permutations(range(3), 2))
    cases = 0
    for weights in product((0, 1, 2), repeat=6):
        graph = [{} for _ in range(3)]
        for (s, t), w in zip(pairs, weights):
            if w:
                graph[s][t] = w
        for s, t in pairs:
            paths = shortest_paths_by_enumeration(graph, s, t)
            expected = {p: Fraction(1, len(paths)) for p in paths} if paths else {(): Fraction(1)}
            assert predecessor_path_law(graph, s, t) == expected
            cases += 1
    # Three equal-weight paths to5. Last predecessors4 and3 carry counts2 and1.
    branching = [{1: 1, 2: 1, 3: 2}, {4: 1}, {4: 1}, {5: 1}, {5: 1}, {}]
    law = predecessor_path_law(branching, 0, 5)
    wrong = predecessor_path_law(branching, 0, 5, True)
    assert set(law.values()) == {Fraction(1, 3)}
    assert sorted(wrong.values()) == [Fraction(1, 4), Fraction(1, 4), Fraction(1, 2)]
    # One directed 3-vertex chain plus an isolated vertex: 12 pairs,3 reachable.
    graph = [{1: 1}, {2: 1}, {}, {}]
    all_pairs = list(permutations(range(4), 2))
    expectation = [Fraction(0) for _ in graph]
    empty_mass = Fraction(0)
    reachable = 0
    for s, t in all_pairs:
        law0 = predecessor_path_law(graph, s, t)
        if () in law0:
            empty_mass += Fraction(1, 12)
        else:
            reachable += 1
        for path, probability in law0.items():
            for v in path[1:-1]:
                expectation[v] += probability / 12
    assert expectation == [0, Fraction(1, 12), 0, 0]
    assert empty_mass == Fraction(3, 4) and reachable == 3
    # Vertex diameter counts vertices, not weighted distance or minimum hops.
    weighted = [{1: 1, 2: 10}, {2: 1}, {}]
    paths = [p for s, t in permutations(range(3), 2) for p in shortest_paths_by_enumeration(weighted, s, t)]
    vertex_diameter = max(map(len, paths))
    weighted_diameter = max(sum(weighted[u][v] for u, v in zip(p, p[1:])) for p in paths)
    assert (vertex_diameter, weighted_diameter) == (3, 2)
    triangle = [{j: 1 for j in range(3) if i != j} for i in range(3)]
    tri_paths = [p for s, t in permutations(range(3), 2) for p in shortest_paths_by_enumeration(triangle, s, t)]
    assert max(map(len, tri_paths)) == 2 and all(not p[1:-1] for p in tri_paths)
    # Arithmetic only: using experimental c=.5 does not certify a confidence bound.
    eps, delta, dhat, c = .05, .1, 4, .5
    d = (dhat - 2).bit_length()
    eq3 = math.ceil(c / eps**2 * (d + math.log(1 / delta)))
    omitted_one = math.ceil(c / eps**2 * (d - 1 + math.log(1 / delta)))
    assert (d, eq3, omitted_one) == (2, 861, 661)
    return dict(weighted_three_node_graphs=729,ordered_pair_cases=cases,
                branching_path_probabilities={str(p): str(v) for p, v in law.items()},
                incorrect_uniform_predecessor_probabilities={str(p): str(v) for p, v in wrong.items()},
                disconnected_example=dict(ordered_pairs=12,reachable_pairs=reachable,empty_mass=str(empty_mass),central_node_expectation=str(expectation[1]),incorrect_reachable_only_expectation='1/3'),
                weighted_example=dict(vertex_diameter=vertex_diameter,weighted_distance_diameter=weighted_diameter),
                triangle=dict(edges=3,vertex_diameter=2,all_internal_scores_zero=True),
                formula_transcription_arithmetic=dict(epsilon=eps,delta=delta,diameter_upper_bound=dhat,vc_upper_bound=d,experimental_c=c,equation3_ceiling=eq3,algorithm1_omitted_one_ceiling=omitted_one,confidence_certified=False))


if __name__ == '__main__':
    print(json.dumps(main(), indent=2))
