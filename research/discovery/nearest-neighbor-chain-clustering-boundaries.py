"""Finite rational NN-chain examples, not an author implementation or benchmark."""
from fractions import Fraction as F
from itertools import combinations, product
import json


def updated(method, ac, bc, ab, a, b, c):
    if method == 'single': return min(ac, bc)
    if method == 'complete': return max(ac, bc)
    if method == 'average': return (a * ac + b * bc) / (a + b)
    if method == 'weighted': return (ac + bc) / 2
    if method == 'ward': return ((a + c) * ac + (b + c) * bc - c * ab) / (a + b + c)
    if method == 'sum3': return ac + bc + ab
    raise ValueError(method)


class State:
    def __init__(self, n, distances, method):
        self.groups = {(i,): 1 for i in range(n)}
        self.distances = {tuple(sorted(((i,), (j,)))): F(v) for (i, j), v in distances.items()}
        self.method = method
    def d(self, a, b): return self.distances[tuple(sorted((a, b)))]
    def merge(self, a, b):
        value = self.d(a, b)
        union = tuple(sorted(a + b))
        for c in list(self.groups):
            if c not in (a, b):
                self.distances[tuple(sorted((union, c)))] = updated(self.method, self.d(a, c), self.d(b, c), value, len(a), len(b), len(c))
        del self.groups[a]
        del self.groups[b]
        self.groups[union] = 1
        return dict(left=a, right=b, height=value)


def chain(n, distances, method, first=0):
    state = State(n, distances, method)
    path = [(first,)] if n else []
    rows = []
    scans = 0
    while len(state.groups) > 1:
        if not path: path = [min(state.groups)]
        a = path[-1]
        previous = path[-2] if len(path) > 1 else None
        options = [b for b in state.groups if b != a]
        b = min(options, key=lambda x: (state.d(a, x), x != previous, x))
        scans += len(options)
        if b == previous:
            rows.append(state.merge(a, b))
            path = path[:-2]
        else:
            path.append(b)
        assert len(path) <= n
    return rows, sorted(rows, key=lambda row: row['height']), scans


def validate_stepwise(n, distances, method, rows):
    state = State(n, distances, method)
    for row in rows:
        a, b = row['left'], row['right']
        if a not in state.groups or b not in state.groups: return False
        minimum = min(state.d(i, j) for i, j in combinations(state.groups, 2))
        if row['height'] != state.d(a, b) or row['height'] != minimum: return False
        state.merge(a, b)
    return len(state.groups) == 1 and len(rows) == n - 1


def primitive(n, distances, method):
    state = State(n, distances, method)
    rows = []
    while len(state.groups) > 1:
        a, b = min(combinations(sorted(state.groups), 2), key=lambda p: (state.d(*p), p))
        rows.append(state.merge(a, b))
    return rows


def main():
    count = 0
    for values in product((1, 2, 3), repeat=6):
        distances = dict(zip(combinations(range(4), 2), values))
        for method in ('single', 'complete', 'average', 'weighted'):
            for first in range(4):
                raw, ordered, scans = chain(4, distances, method, first)
                assert validate_stepwise(4, distances, method, ordered)
                count += 1
    ward_count = 0
    for points in product(range(3), repeat=4):
        distances = {(i, j): (points[i] - points[j]) ** 2 for i, j in combinations(range(4), 2)}
        for first in range(4):
            raw, ordered, scans = chain(4, distances, 'ward', first)
            assert validate_stepwise(4, distances, 'ward', ordered)
            ward_count += 1
    footnote = dict(zip(combinations(range(5), 2), [3,4,6,15,5,7,12,1,13,14]))
    good_raw, good_sorted, _ = chain(5, footnote, 'complete')
    assert good_raw[0]['height'] == 3 and good_sorted[0]['height'] == 1
    assert validate_stepwise(5, footnote, 'complete', good_sorted)
    bad_raw, bad_sorted, _ = chain(5, footnote, 'sum3')
    correct = primitive(5, footnote, 'sum3')
    assert [r['height'] for r in correct] == [1,3,27,85]
    assert [r['height'] for r in bad_sorted] == [1,3,28,87]
    assert not validate_stepwise(5, footnote, 'sum3', bad_sorted)
    ab_first = State(5, footnote, 'sum3')
    ab_first.merge((0,), (1,)); ab_first.merge((2,), (3,))
    cd_first = State(5, footnote, 'sum3')
    cd_first.merge((2,), (3,)); cd_first.merge((0,), (1,))
    disjoint_orders = [ab_first.d((0,1),(2,3)), cd_first.d((0,1),(2,3))]
    assert disjoint_orders == [29,27]
    # All-ones ties permit a directed length-three cycle under arbitrary choices.
    arbitrary_cycle = [0,1,2,0]
    ties = dict.fromkeys(combinations(range(3), 2), 1)
    tie_raw, tie_sorted, _ = chain(3, ties, 'complete')
    assert len(tie_raw) == 2 and validate_stepwise(3, ties, 'complete', tie_sorted)
    assert not validate_stepwise(3, ties, 'complete', list(reversed(tie_sorted)))
    for a,b in zip(arbitrary_cycle,arbitrary_cycle[1:]): assert a != b and ties[tuple(sorted((a,b)))] == 1
    # Figure4 really prints <=3, matching the pinned implementation.
    # Exercise only this indexing boundary, not the whole literal listing.
    restart_boundaries = []
    for length in range(9):
        printed_chain = list(range(length))
        if len(printed_chain) <= 3:
            action = 'restart'
            printed_chain = [0]  # any active cluster, with at least two active
        else:
            action = 'reuse'
            a, b = printed_chain[-4], printed_chain[-3]
            del printed_chain[-3:]
            assert a == length - 4 and b == length - 3
            assert printed_chain[-1] == a
        restart_boundaries.append(dict(length=length, action=action))
    assert restart_boundaries[3]['action'] == 'restart'
    # Equal minima do not imply reciprocity in de Rham's displayed equality.
    ds = {(0,1):1,(0,2):5,(0,3):5,(1,2):5,(1,3):5,(2,3):1}
    s = State(4, ds, 'complete')
    minima = {a:min(s.d(a,b) for b in s.groups if b!=a) for a in s.groups}
    assert minima[(0,)] == minima[(2,)] == 1 and s.d((0,),(2,)) == 5
    print(json.dumps(dict(matrix_cases=count,ward_euclidean_cases=ward_count,
        reordered_complete=dict(raw=good_raw,stable_sorted=good_sorted),
        reducibility_without_commutation=dict(primitive=correct,chain_sorted=bad_sorted,disjoint_pair_order_distances=disjoint_orders),
        arbitrary_tie_cycle=arbitrary_cycle,predecessor_tie_trace=tie_sorted,reversing_equal_height_dependencies_is_invalid=True,
        actual_figure4_restart_boundaries=restart_boundaries,
        equal_minima_not_reciprocal=dict(minima=1,pair_distance=5),
        limits='Finite rational checks of a curator-written conceptual algorithm; no author program run, no universal proof, no timing or floating-point replication.'
    ),default=str,indent=2))


if __name__ == '__main__': main()
