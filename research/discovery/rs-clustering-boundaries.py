"""Local geometric/threshold checks only; not an RS algorithm or empirical benchmark."""
from fractions import Fraction as F
from math import ceil, log
from collections import deque
import json

def squared_distance(a,b):return sum((x-y)**2 for x,y in zip(a,b))
def midpoint(a,b):return tuple((x+y)/2 for x,y in zip(a,b))
def main():
    points=[(F(x),) for x in (0,1,3,7,15,31,63)]
    near=[min((j for j in range(len(points)) if j!=i),key=lambda j:squared_distance(points[i],points[j])) for i in range(len(points))]
    assert near==[1,0,1,2,3,4,5]
    edges={i:set() for i in range(len(points))}
    for i,j in enumerate(near):
        edges[i].add(j);edges[j].add(i)
    def distances(start):
        found={start:0};todo=deque([start])
        while todo:
            u=todo.popleft()
            for v in edges[u]:
                if v not in found:found[v]=found[u]+1;todo.append(v)
        return found
    to_p,to_q=distances(0),distances(1)
    depths=[F(to_p[i]+to_q[i]+1,2) for i in range(len(points))]
    assert depths==[1,1,2,3,4,5,6]
    # Exact alpha2 power boundary uses n+1=8, avoiding floating rounding.
    threshold2=3;assert 2**threshold2==len(points)+1
    retained=[i for i,h in enumerate(depths) if h<=threshold2];pruned=[i for i,h in enumerate(depths) if h>threshold2]
    assert retained==[0,1,2,3] and pruned==[4,5,6]
    assert ceil(log(len(points)+1,1.5))==6
    root=midpoint(points[0],points[1]);centroid=(sum(points[i][0] for i in retained)/len(retained),)
    assert root==(F(1,2),) and centroid==(F(11,4),)
    a,b,c,d=map(lambda t:tuple(map(F,t)),[(0,0),(2,0),(0,4),(6,4)])
    single_formula=(squared_distance(a,c)+squared_distance(b,c))/2-squared_distance(a,b)/4
    pair_formula=(squared_distance(a,c)+squared_distance(a,d)+squared_distance(b,c)+squared_distance(b,d)-squared_distance(a,b)-squared_distance(c,d))/4
    assert single_formula==squared_distance(midpoint(a,b),c)==17
    assert pair_formula==squared_distance(midpoint(a,b),midpoint(c,d))==20
    # Standalone midpoint extension fails for a valid four-cycle metric.
    # This is NOT an attainable-support-pair RS execution counterexample.
    cycle_radical=(F(1)+1+1+1-F(4)-4)/4
    assert cycle_radical==-1
    print(json.dumps(dict(chain_neighbors=near,depths=depths,alpha2=dict(threshold=3,retained=retained,pruned_singletons=pruned),alpha1_5_threshold=6,support_midpoint=root,retained_member_centroid=centroid,euclidean_squared_midpoint_formulas=dict(point=single_formula,pair=pair_formula),standalone_non_euclidean_metric_formula=dict(squared_result=cycle_radical,qualification='Four-cycle metric with opposite support-pair distances2 and cross distances1; these pairs are not reciprocal in this four-point input. This disproves an unrestricted geometric identity, not an actual RS execution.'),limits='Boundary arithmetic only; no author code, full RS implementation, source benchmark or general complexity proof.'),default=str,indent=2))
if __name__=='__main__':main()
