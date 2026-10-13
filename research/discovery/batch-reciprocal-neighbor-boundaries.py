"""Finite curator batch-RNN checks; tie matching is explicit, not attributed to the paper."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
import json


def update(method, ac, bc, ab, a, b, c):
    if method == 'single': return min(ac, bc)
    if method == 'complete': return max(ac, bc)
    if method == 'average': return (a * ac + b * bc) / (a + b)
    if method == 'weighted': return (ac + bc) / 2
    if method == 'ward': return ((a + c) * ac + (b + c) * bc - c * ab) / (a + b + c)
    raise ValueError(method)


class State:
    def __init__(self, n, ds, method):
        self.groups = {(i,) for i in range(n)}
        self.ds = {((i,), (j,)): F(v) for (i, j), v in ds.items()}
        self.method = method
    def d(self, a, b): return self.ds[tuple(sorted((a, b)))]
    def merge(self, a, b):
        value = self.d(a, b); u = tuple(sorted(a + b))
        for c in self.groups - {a, b}:
            self.ds[tuple(sorted((u, c)))] = update(self.method, self.d(a,c), self.d(b,c), value, len(a), len(b), len(c))
        self.groups.difference_update({a, b}); self.groups.add(u)
        return dict(left=a, right=b, height=value)


def batch(n, ds, method):
    state = State(n, ds, method); rows = []; rounds = []
    while len(state.groups) > 1:
        minima = {a:min(state.d(a,b) for b in state.groups if b != a) for a in state.groups}
        all_pairs = [(a,b) for a,b in combinations(sorted(state.groups),2) if state.d(a,b) == minima[a] == minima[b]]
        # An explicit curator extension selects disjoint pairs under ties.
        used = set(); selected = []
        for a,b in all_pairs:
            if not used.intersection({a,b}): selected.append((a,b)); used.update({a,b})
        assert selected
        rounds.append(dict(active=len(state.groups), reciprocal_pairs=len(all_pairs), disjoint_merges=len(selected)))
        for a,b in selected: rows.append(state.merge(a,b))
    return rows, sorted(rows,key=lambda r:r['height']), rounds


def valid(n, ds, method, rows):
    s=State(n,ds,method)
    for r in rows:
        a,b=r['left'],r['right']
        if a not in s.groups or b not in s.groups:return False
        if r['height'] != s.d(a,b) or r['height'] != min(s.d(i,j) for i,j in combinations(s.groups,2)):return False
        s.merge(a,b)
    return len(rows)==n-1 and len(s.groups)==1


def main():
    counts={}
    for label,matrices in [('distinct_initial',permutations(range(1,7))),('ties_allowed',product((1,2,3),repeat=6))]:
        count=0
        for vals in matrices:
            ds=dict(zip(combinations(range(4),2),vals))
            for method in ('single','complete','average','weighted'):
                raw,ordered,rounds=batch(4,ds,method);assert valid(4,ds,method,ordered);count+=1
        counts[label]=count
    ties=dict.fromkeys(combinations(range(3),2),1)
    raw,ordered,rounds=batch(3,ties,'complete');assert rounds[0]['reciprocal_pairs']==3 and rounds[0]['disjoint_merges']==1
    ds={(0,1):1,(0,2):5,(0,3):5,(1,2):5,(1,3):5,(2,3):1};s=State(4,ds,'complete')
    assert min(s.d((0,),a) for a in s.groups if a!=(0,))==min(s.d((2,),a) for a in s.groups if a!=(2,))==1
    assert s.d((0,),(2,))==5
    slow={(i,j):2**j for i,j in combinations(range(8),2)}
    raw,ordered,slow_rounds=batch(8,slow,'complete');assert len(slow_rounds)==7 and all(x['disjoint_merges']==1 for x in slow_rounds)
    points=[(0,40),(15,45),(0,0),(20,10),(40,40),(45,20)]
    ward={(i,j):sum(F(points[i][k]-points[j][k])**2 for k in range(2))/2 for i,j in combinations(range(6),2)}
    raw,ordered,ward_rounds=batch(6,ward,'ward');assert valid(6,ward,'ward',ordered)
    assert [r['height'] for r in ordered]==[F(125),F(425,2),F(250),F(5525,4),F(19225,12)]
    assert ward_rounds[0]['disjoint_merges']==3
    print(json.dumps(dict(matrix_cases=counts,overlapping_ties=rounds,equal_minima_counterexample=dict(nearest_minimum=1,cross_pair_distance=5),one_pair_per_pass=slow_rounds,source_six_point_ward=dict(raw=raw,sorted=ordered,rounds=ward_rounds),limits='Finite rational checks of a curator implementation. Lexicographic disjoint matching is an explicit tie extension, not specified by deRham. No author code, timing or universal correctness proof.'),default=str,indent=2))


if __name__=='__main__':main()
