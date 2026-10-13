"""Exact finite checks of the printed Genie rule; no author software execution."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
import json


def gini(sizes):
    if len(sizes) == 1:
        return None  # The displayed normalisation has zero denominator here.
    return F(sum(abs(a-b) for a,b in combinations(sizes,2)), (len(sizes)-1)*sum(sizes))


def mst(n, edges):
    groups=[{i} for i in range(n)];out=[]
    for e in sorted(edges):
        _,u,v=e
        a=next(c for c in groups if u in c);b=next(c for c in groups if v in c)
        if a is b:continue
        out.append(e);groups.remove(a);groups.remove(b);groups.append(a|b)
    assert len(out)==n-1
    return out


def cluster(n, edges, threshold, use_mst):
    available=mst(n,edges) if use_mst else edges
    groups=[{i} for i in range(n)];trace=[]
    while len(groups)>1:
        sizes=list(map(len,groups));inequality=gini(sizes);minimum=min(sizes)
        forced=inequality>threshold
        def eligible(e):
            _,u,v=e
            a=next(c for c in groups if u in c);b=next(c for c in groups if v in c)
            return a is not b and (not forced or len(a)==minimum or len(b)==minimum)
        chosen=min(e for e in available if eligible(e))
        assert chosen[0]==min(e[0] for e in edges if eligible(e))
        distance,u,v=chosen
        a=next(c for c in groups if u in c);b=next(c for c in groups if v in c)
        sa,sb=len(a),len(b);k=len(groups);total=sum(sizes)
        predicted=None
        if k>2:
            numerator=total*(k-1)*inequality+sum(abs(c-sa-sb)-abs(c-sa)-abs(c-sb) for c in sizes)-sa-sb+abs(sa-sb)
            predicted=numerator/(total*(k-2))
        groups.remove(a);groups.remove(b);groups.append(a|b)
        after=gini(list(map(len,groups)))
        assert after==predicted
        trace.append(dict(edge=[u,v],distance=distance,forced=forced,gini_before=inequality,gini_after=after,partition=sorted(sorted(c) for c in groups)))
    return trace


def line(points):
    return [(abs(a-b),i,j) for (i,a),(j,b) in combinations(enumerate(map(F,points)),2)]


def main():
    pairs=list(combinations(range(4),2));thresholds=[F(1,10),F(3,10),F(1,2),F(1)]
    distinct=tied=0
    for weights in permutations(range(1,7)):
        edges=[(F(w),a,b) for w,(a,b) in zip(weights,pairs)]
        for g in thresholds:
            assert cluster(4,edges,g,False)==cluster(4,edges,g,True)
            distinct+=1
    for weights in product(range(1,4),repeat=6):
        edges=[(F(w),a,b) for w,(a,b) in zip(weights,pairs)]
        for g in thresholds:
            cluster(4,edges,g,False);cluster(4,edges,g,True)
            tied+=1
    example=cluster(5,line([0,1,3,6,10]),F(3,10),True)
    assert [x['distance'] for x in example]==[1,2,3,4]
    assert example[2]['partition']==[[0,1,2,3],[4]]
    assert example[2]['gini_before']==F(2,5) and example[2]['gini_after']==F(3,5)
    inversion=cluster(5,line([0,1,10,12,100]),F(3,20),True)
    assert [x['distance'] for x in inversion]==[1,2,88,9]
    print(json.dumps(dict(distinct_weight_cases=distinct,tied_weight_cases=tied,scope='Four-point symmetric nonnegative dissimilarities: 720 edge permutations and 729 three-valued assignments, each at four thresholds. The MST choices satisfy the full eligible-pair minimum; distinct-weight traces agree exactly. Gini incremental updates agree with direct pair-sum recomputation. This is finite verification, not a universal proof.',paper_example=dict(points=[0,1,3,6,10],threshold=F(3,10),trace=example,assessment='The printed OR eligibility rule and statically inspected Genie1.0.0 merge predicate choose distance3 at the third merge. The paper Example1 instead claims distance4 and partition {0,1,2}/{3,4}; that claim does not follow from its stated rule. No author program was executed.'),inversion=dict(points=[0,1,10,12,100],threshold=F(3,20),trace=inversion),limits='Curator reference only. No author R/C++ execution, floating-point certification, benchmark reproduction, universal tie equivalence or outlier-recovery guarantee.'),default=str,indent=2))


if __name__=='__main__':main()
