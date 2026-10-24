"""Finite curator path-law checks, not author code or a performance benchmark."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, permutations
from math import ceil, log, sqrt
import json


def all_shortest(n, edges, source, target, directed):
    adjacency = [[] for _ in range(n)]
    for u, v in edges:
        adjacency[u].append(v)
        if not directed:
            adjacency[v].append(u)
    found = []
    def visit(path):
        if path[-1] == target:
            found.append(path)
            return
        for v in adjacency[path[-1]]:
            if v not in path:
                visit(path + (v,))
    visit((source,))
    size = min(map(len, found), default=0)
    return [p for p in found if len(p) == size]


def balanced_cut(n, edges, source, target, directed):
    forward = [[] for _ in range(n)]
    reverse = [[] for _ in range(n)]
    for u, v in edges:
        forward[u].append(v)
        reverse[v].append(u)
        if not directed:
            forward[v].append(u)
            reverse[u].append(v)
    frontiers = [{source}, {target}]
    distance = [{source: 0}, {target: 0}]
    counts = [{source: 1}, {target: 1}]
    scans = 0
    while frontiers[0] and frontiers[1]:
        volumes = [sum(len(adjacency[v]) for v in frontier)
                   for adjacency, frontier in zip((forward, reverse), frontiers)]
        side = 0 if volumes[0] <= volumes[1] else 1
        adjacency = (forward, reverse)[side]
        other = 1 - side
        next_frontier = set()
        meeting = []
        for v in sorted(frontiers[side]):
            for w in adjacency[v]:
                scans += 1
                if w in distance[other]:
                    edge = (v, w) if side == 0 else (w, v)
                    meeting.append((edge, counts[side][v] * counts[other][w]))
                elif w not in distance[side]:
                    distance[side][w] = distance[side][v] + 1
                    counts[side][w] = counts[side][v]
                    next_frontier.add(w)
                elif distance[side][w] == distance[side][v] + 1:
                    counts[side][w] += counts[side][v]
        if meeting:
            return meeting, distance[0], distance[1], counts, scans
        frontiers[side] = next_frontier
    return [], distance[0], distance[1], counts, scans


def check_pair(n, edges, source, target, directed):
    paths = all_shortest(n, edges, source, target, directed)
    meeting, ds, dt, counts, scans = balanced_cut(n, edges, source, target, directed)
    assert bool(paths) == bool(meeting)
    if not paths:
        return dict(paths=[], meeting=[], scans=scans)
    weights = dict(meeting)
    assert len(weights) == len(meeting)
    assert sum(weights.values()) == len(paths)
    law = defaultdict(F)
    for path in paths:
        crossed = [(u, v) for u, v in zip(path, path[1:]) if (u, v) in weights]
        assert len(crossed) == 1
        u, v = crossed[0]
        assert ds[u] + 1 + dt[v] == len(path) - 1
        # Uniform meeting-edge weighting, then uniform counted prefix/suffix.
        law[path] += F(weights[(u, v)], sum(weights.values())) / counts[0][u] / counts[1][v]
    assert all(probability == F(1, len(paths)) for probability in law.values())
    assert sum(law.values()) == 1
    return dict(paths=paths, meeting=meeting, probabilities=[str(law[p]) for p in paths], scans=scans)


def confidence(mean, failure, horizon, count):
    assert 0 <= mean <= 1 and 0 < failure < 1 and 1 <= count <= horizon
    ell = log(1 / failure)
    a = 1 / 3 - horizon / count
    c = 1 / 3 + horizon / count
    f = ell / count * (a + sqrt(a * a + 2 * mean * horizon / ell))
    g = ell / count * (c + sqrt(c * c + 2 * mean * horizon / ell))
    return f, g


def main():
    coverage = []
    for directed in (False, True):
        possible = list(permutations(range(4), 2) if directed else combinations(range(4), 2))
        pair_count = 0
        for mask in range(1 << len(possible)):
            edges = [e for i, e in enumerate(possible) if mask & (1 << i)]
            for s, t in permutations(range(4), 2):
                check_pair(4, edges, s, t, directed)
                pair_count += 1
        coverage.append(dict(directed=directed,graphs=1 << len(possible),ordered_pair_cases=pair_count))
    # Three shortest paths, with meeting-edge multiplicities two and one.
    edges = [(0,1),(0,2),(1,3),(2,3),(3,5),(5,6),
             (0,4),(4,7),(7,8),(8,6)] + [(i,6) for i in range(9,14)]
    branching = check_pair(14, edges, 0, 6, True)
    assert sorted(weight for _, weight in branching['meeting']) == [1,2]
    assert branching['probabilities'] == ['1/3'] * 3
    cut_weights = dict(branching['meeting'])
    wrong_law = []
    for path in branching['paths']:
        crossed = next(edge for edge in zip(path,path[1:]) if edge in cut_weights)
        wrong_law.append(F(1,len(cut_weights)*cut_weights[crossed]))
    assert wrong_law == [F(1,4),F(1,4),F(1,2)]
    branching['uniform_meeting_edge_would_give_path_probabilities'] = [str(x) for x in wrong_law]
    diamond = [(0,1),(0,2),(1,3),(2,3)]
    fractions = []
    indicator_mean = F(0)
    for s, t in permutations(range(4), 2):
        paths = all_shortest(4, diamond, s, t, False)
        q = F(sum(0 in path[1:-1] for path in paths),len(paths))
        fractions.append(q)
        indicator_mean += q / 12
    mean = sum(fractions)/12
    pair_variance = sum(q*q for q in fractions)/12 - mean*mean
    path_variance = indicator_mean*(1-indicator_mean)
    assert (mean,pair_variance,path_variance)==(F(1,12),F(5,144),F(11,144))
    path = check_pair(129, [(i,i+1) for i in range(128)], 0, 128, False)
    assert path['scans'] >= 128
    delta, tolerance, n = .1, .05, 3
    # Curator Hoeffding-plus-union cap; not the source's optimized RK cap.
    horizon = ceil(log(4*n/delta)/(2*tolerance*tolerance))
    node_budget = delta/(4*n)
    zero_stop = next(t for t in range(1,horizon+1)
                     if max(confidence(0,node_budget,horizon,t)) <= tolerance)
    lower,upper=confidence(0,node_budget,horizon,zero_stop)
    assert lower == 0 and upper <= tolerance and zero_stop < horizon
    return dict(exhaustive_path_law=coverage,unequal_meeting_edge_weights=branching,
                diamond_vertex0=dict(mean=str(mean),pair_fraction_variance=str(pair_variance),
                                     one_path_indicator_variance=str(path_variance)),
                long_path=dict(nodes=129,distance=128,incident_edges_scanned=path['scans'],
                               note='Selected path endpoints require linear work; no universal square-root bound.'),
                zero_score_triangle=dict(delta=delta,tolerance=tolerance,curator_hoeffding_cap=horizon,
                                         uniform_node_tail_budget=node_budget,first_stopping_count=zero_stop,
                                         lower_radius=lower,upper_radius=upper,
                                         note='The literal inclusive event truth<=estimate-f is true with probability1 at zero; closed-interval coverage uses strict outside errors.'),
                scope='Finite exact path laws and variance arithmetic, plus floating evaluation of source radii under an explicitly curator-derived cap. No author software, benchmark, general proof certification or replication.')


if __name__ == '__main__':
    print(json.dumps(main(),indent=2))
