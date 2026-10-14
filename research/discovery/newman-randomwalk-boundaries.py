"""Curator exact examples for Newman's original pair-enumeration method.

No simulated walk estimates, author software or empirical benchmark.
Compare grounded-current pair enumeration with an absorbing Markov matrix.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import importlib.util
import json


def companion():
    p=Path(__file__).with_name('current-flow-boundaries.py')
    spec=importlib.util.spec_from_file_location('current_flow_examples',p)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def enumerate_pairs(n, edges, module, ground=0):
    _,tmat=module.grounded(n,edges,ground)
    totals=[F(0) for _ in range(n)]
    for s,t in combinations(range(n),2):
        p=[row[s]-row[t] for row in tmat]
        current=[F(0) for _ in range(n)]
        for u,v,c in edges:
            assert c==1
            value=abs(p[u]-p[v])/2
            current[u]+=value;current[v]+=value
        current[s]=current[t]=F(1)
        totals=[a+b for a,b in zip(totals,current)]
    return [x/F(n*(n-1),2) for x in totals]


def absorbing(n, edges, source, target, module):
    adj=[[F(0) for _ in range(n)] for _ in range(n)]
    for u,v,c in edges:
        assert c==1
        adj[u][v]=adj[v][u]=1
    degrees=[sum(row) for row in adj]
    transient=[v for v in range(n) if v!=target]
    matrix=[[F(u==v)-adj[u][v]/degrees[v] for v in transient] for u in transient]
    fundamental=module.inverse(matrix)
    visits=[F(0) for _ in range(n)]
    for i,v in enumerate(transient):visits[v]=fundamental[i][transient.index(source)]
    transitions=[[visits[u]*adj[u][v]/degrees[u] for v in range(n)] for u in range(n)]
    net=[[transitions[u][v]-transitions[v][u] for v in range(n)] for u in range(n)]
    _,cmat=module.grounded(n,edges,target)
    potentials=[row[source] for row in cmat]
    assert all(net[u][v]==adj[u][v]*(potentials[u]-potentials[v]) for u in range(n) for v in range(n))
    return dict(visits=visits,transitions=transitions,net=net,potentials=potentials)


def main():
    module=companion()
    cases={'path3':(3,[(0,1,F(1)),(1,2,F(1))]),
           'path4':(4,[(0,1,F(1)),(1,2,F(1)),(2,3,F(1))]),
           'triangle':(3,[(0,1,F(1)),(1,2,F(1)),(2,0,F(1))]),
           'complete4':(4,[(u,v,F(1)) for u,v in combinations(range(4),2)])}
    results={}
    for name,(n,edges) in cases.items():
        score=enumerate_pairs(n,edges,module)
        bf=module.sorted_rows(n,edges)
        assert score==[F(n-2,n)*x+F(2,n) for x in bf]
        for g in range(n):assert enumerate_pairs(n,edges,module,g)==score
        for s,t in combinations(range(n),2):absorbing(n,edges,s,t,module)
        results[name]=dict(newman_endpoint_included=score,brandes_fleischer_endpoint_excluded=bf)
    assert results['path3']['newman_endpoint_included']==[F(2,3),F(1),F(2,3)]
    assert results['path4']['newman_endpoint_included']==[F(1,2),F(5,6),F(5,6),F(1,2)]
    assert results['triangle']['newman_endpoint_included']==[F(7,9)]*3
    assert results['complete4']['newman_endpoint_included']==[F(5,8)]*4
    walk=absorbing(*cases['complete4'],0,3,module)
    assert walk['visits'][1]==F(3,4)
    assert walk['transitions'][1][2]==walk['transitions'][2][1]==F(1,4)
    assert walk['net'][1][2]==0
    # Two valid first-hit paths have opposite nonzero net counts on edge 1--2.
    examples=[(0,1,2,3),(0,2,1,3)]
    counts=[]
    for path in examples:
        steps=list(zip(path,path[1:]))
        counts.append(steps.count((1,2))-steps.count((2,1)))
        assert path[-1]==3 and 3 not in path[:-1]
    assert counts==[1,-1]
    return dict(cases=results,complete4_source0_target3=dict(
        expected_visits_at1=walk['visits'][1],expected_transitions_1_to_2=F(1,4),
        expected_transitions_2_to_1=F(1,4),absolute_expected_net_1_2=F(0),
        two_first_hit_paths=examples,path_probabilities=[F(1,27)]*2,
        positive_lower_bound_expected_absolute_net=F(2,27),
        note='The two paths prove E|net count| is positive while |E net count| is zero; 2/27 is a lower bound, not the complete expectation.'),
        scope='Finite exact pair and fundamental-matrix arithmetic; not author code, a random-walk simulation or an empirical validation.')


if __name__=='__main__':print(json.dumps(main(),indent=2,default=str))
