"""Curator finite checks of literal Algorithm 2's reciprocal resistance sum.

Compare its column accumulation with directly solved pair resistances and with
shortest-path lengths using reciprocal conductance. No author implementation.
"""
from fractions import Fraction as F
from pathlib import Path
import importlib.util
import json


def companion():
    p=Path(__file__).with_name('current-flow-boundaries.py')
    spec=importlib.util.spec_from_file_location('current_flow_examples',p)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module


def columns(n, edges, module, ground=0):
    _,c=module.grounded(n,edges,ground)
    total=[F(0) for _ in range(n)]
    for v in range(n):
        for w in range(n):
            total[v]+=c[v][v]-2*c[w][v]
            total[w]+=c[v][v]
    assert all(x>0 for x in total)
    return [1/x for x in total]


def shortest(n,edges):
    dist=[[F(0) if i==j else None for j in range(n)] for i in range(n)]
    for u,v,c in edges:dist[u][v]=dist[v][u]=1/c
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] is not None and dist[k][j] is not None:
                    candidate=dist[i][k]+dist[k][j]
                    if dist[i][j] is None or candidate<dist[i][j]:dist[i][j]=candidate
    return [1/sum(row) for row in dist]


def main():
    module=companion()
    cases={'path4':(4,[(0,1,F(1)),(1,2,F(1)),(2,3,F(1))]),
           'weighted_path4':(4,[(0,1,F(1)),(1,2,F(2)),(2,3,F(3))]),
           'triangle':(3,[(0,1,F(1)),(1,2,F(1)),(2,0,F(1))]),
           'weighted_triangle':(3,[(0,1,F(1)),(1,2,F(2)),(2,0,F(3))])}
    results={}
    for name,(n,edges) in cases.items():
        output=columns(n,edges,module)
        normalized=module.direct(n,edges)[1]
        assert normalized==[(n-1)*x for x in output]
        for g in range(n):assert columns(n,edges,module,g)==output
        assert columns(n,[(u,v,7*c) for u,v,c in edges],module)==[7*x for x in output]
        path=shortest(n,edges)
        if 'path' in name:assert path==output
        else:assert path!=output
        results[name]=dict(algorithm2_inverse_resistance_sum=output,
                          definition3_normalized_closeness=normalized,
                          inverse_shortest_resistance_length_sum=path)
    assert results['triangle']['algorithm2_inverse_resistance_sum']==[F(3,4)]*3
    assert results['triangle']['inverse_shortest_resistance_length_sum']==[F(1,2)]*3
    assert results['path4']['algorithm2_inverse_resistance_sum']==[F(1,6),F(1,4),F(1,4),F(1,6)]
    return dict(cases=results,scope='Literal column accumulation, pair-resistance comparison, ground and scale checks on finite exact graphs; not an information-centrality proof, author-code execution or numerical benchmark.')


if __name__=='__main__':print(json.dumps(main(),indent=2,default=str))
