"""Exact self-inclusive OPTICS-OF/LOF boundary comparisons, not ELKI execution."""
from fractions import Fraction as F
import json


def score(data, m, include_self=True, exact_count=False):
    n=len(data)
    assert 1 <= m <= n if include_self else 1 <= m <= n-1
    rows=[sorted((abs(x-y),j) for j,y in enumerate(data)
                 if include_self or i != j) for i,x in enumerate(data)]
    radius=[r[m-1][0] for r in rows]
    neighbors=[([j for d,j in row[:m]] if exact_count else
                [j for d,j in row if d <= radius[i]]) for i,row in enumerate(rows)]
    reaches=[{j:max(radius[j],abs(data[i]-data[j])) for j in ns}
             for i,ns in enumerate(neighbors)]
    sums=[sum(r.values(),F(0)) for r in reaches]
    if any(s == 0 for s in sums):
        raise ArithmeticError('Zero mean reachability; no epsilon is assumed.')
    densities=[F(len(neighbors[i]),1)/s for i,s in enumerate(sums)]
    values=[sum((densities[j]/densities[i] for j in ns),F(0))/len(ns)
            for i,ns in enumerate(neighbors)]
    return dict(radius=radius,neighbors=neighbors,reaches=reaches,
                densities=densities,scores=values)


def main():
    data=list(map(F,[0,1,3]))
    inc2=score(data,2);exc1=score(data,1,False)
    inc3=score(data,3);exc2=score(data,2,False)
    assert inc2['scores']==[1,1,F(3,2)]
    assert exc1['scores']==[1,1,2]
    assert inc3['scores']==[1,1,1]
    assert exc2['scores']==[F(11,12),F(6,5),F(11,12)]
    assert inc2['radius']==exc1['radius']
    assert all(i in ns for i,ns in enumerate(inc2['neighbors']))
    assert inc2['reaches'][0][0]==1
    assert score([13+7*x for x in data],2)['scores']==inc2['scores']
    tied=score(list(map(F,[0,2,4,5])),2)
    trunc=score(list(map(F,[0,2,4,5])),2,exact_count=True)
    assert len(tied['neighbors'][1])==3
    assert tied['scores'][1]==F(4,3) and trunc['scores'][1]==1
    failures=[]
    for xs,k in [(data,1),([F(0),F(0),F(3)],2)]:
        try:score(xs,k)
        except ArithmeticError:failures.append(True)
    assert failures==[True,True]
    print(json.dumps(dict(
        data_0_1_3_self_inclusive_m2=list(map(str,inc2['scores'])),
        corresponding_self_excluded_k1=list(map(str,exc1['scores'])),
        data_0_1_3_self_inclusive_m3=list(map(str,inc3['scores'])),
        corresponding_self_excluded_k2=list(map(str,exc2['scores'])),
        identical_core_radii_do_not_make_algorithms_equivalent=True,
        self_reachability_is_core_distance_not_zero=True,
        all_reference_neighborhoods_give_score_one=True,
        boundary_ties_score='4/3',truncated_score='1',
        self_only_and_duplicate_zero_means_undefined=True,
        uniform_positive_scaling_preserves_defined_core_scores=True,
        scope='Exact arithmetic from inspected self-inclusive scoring formulas and pinned source, compared to self-excluded LOF. No Java execution, index-backend validation or benchmark reproduction.'
    ),indent=2))


if __name__=='__main__':main()
