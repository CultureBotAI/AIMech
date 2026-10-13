"""Finite lower-bound checks using linear queue selection, not author software."""
from fractions import Fraction as F
from itertools import combinations, product
import json


def update(method, ac, bc, ab, a, b, c):
    if method == 'single': return min(ac, bc)
    if method == 'complete': return max(ac, bc)
    if method == 'average': return (a * ac + b * bc) / (a + b)
    if method == 'weighted': return (ac + bc) / 2
    if method == 'ward': return ((a + c) * ac + (b + c) * bc - c * ab) / (a + b + c)
    if method == 'centroid': return (a * ac + b * bc) / (a + b) - F(a * b, (a + b) ** 2) * ab
    if method == 'median': return (ac + bc) / 2 - ab / 4
    if method == 'sum3': return ac + bc + ab
    raise ValueError(method)


def lazy(n, initial, method):
    groups = {i:(i,) for i in range(n)}
    ds = {k:F(v) for k,v in initial.items()}
    bound, near, trace, rescans = {}, {}, [], 0
    def d(i,j): return ds[tuple(sorted((i,j)))]
    def row(i):
        j=min((j for j in groups if j>i),key=lambda j:(d(i,j),j))
        return d(i,j),j
    for i in range(n-1): bound[i],near[i]=row(i)
    while len(groups)>1:
        for i in bound:
            assert near[i] in groups and near[i]>i
            assert bound[i] <= row(i)[0]
            if bound[i] == d(i,near[i]): assert bound[i] == row(i)[0]
        while True:
            a=min(bound,key=lambda i:(bound[i],i))
            if bound[a] == d(a,near[a]): break
            assert bound[a] < d(a,near[a])
            bound[a],near[a]=row(a);rescans+=1
        b=near[a];height=bound[a]
        assert height==min(d(i,j) for i,j in combinations(groups,2))
        trace.append(dict(left=groups[a],right=groups[b],height=height))
        sa,sb=len(groups[a]),len(groups[b])
        for c in list(groups):
            if c not in (a,b): ds[tuple(sorted((b,c)))]=update(method,d(a,c),d(b,c),height,sa,sb,len(groups[c]))
        groups[b]=tuple(sorted(groups[a]+groups[b]));del groups[a];del bound[a];del near[a]
        if len(groups)==1:break
        for i in groups:
            if i<b:
                if d(i,b)<bound[i]: bound[i],near[i]=d(i,b),b
                elif near[i]==a: near[i]=b
        if b<n-1: bound[b],near[b]=row(b)
    return trace,rescans


def main():
    cases=0;stale_cases=0;max_rescans=0
    for vals in product((1,2,3),repeat=6):
        ds=dict(zip(combinations(range(4),2),vals))
        for method in ('single','complete','average','weighted','sum3'):
            trace,r=lazy(4,ds,method);cases+=1;stale_cases+=r>0;max_rescans=max(max_rescans,r)
    euclidean_cases=0
    for points in product(range(3),repeat=4):
        ds={(i,j):(points[i]-points[j])**2 for i,j in combinations(range(4),2)}
        for method in ('ward','centroid','median'):
            trace,r=lazy(4,ds,method);euclidean_cases+=1
    # Centroid/median inversion: A=(-1,0), B=(1,0), C=(0,9/5).
    ds={(0,1):F(4),(0,2):F(106,25),(1,2):F(106,25)}
    inversions={m:lazy(3,ds,m)[0] for m in ('centroid','median')}
    for rows in inversions.values():assert [r['height'] for r in rows]==[4,F(81,25)]
    counter=dict(zip(combinations(range(5),2),[3,4,6,15,5,7,12,1,13,14]))
    counter_trace,r=lazy(5,counter,'sum3');assert [x['height'] for x in counter_trace]==[1,3,27,85]
    assert lazy(1,{},'complete')==([],0)
    assert [x['height'] for x in lazy(2,{(0,1):1},'complete')[0]]==[1]
    print(json.dumps(dict(matrix_cases=cases,euclidean_cases=euclidean_cases,
        cases_with_stale_rescan=stale_cases,maximum_rescans_in_four_object_cases=max_rescans,
        inversion_examples=inversions,sum3_primitive_trace=counter_trace,
        one_and_two_object_boundaries='passed',
        limits='Curator reference with linear selection from row bounds, not the author heap implementation. Checks the lower-bound/equality invariant and global merge admissibility; does not establish implementation runtime, memory, floating-point behavior or universal correctness.'
    ),default=str,indent=2))


if __name__=='__main__':main()
