"""Finite checks for Radicchi2004 definitions and modified triangle scores.

No author software or general higher-cycle denominator is reconstructed.
"""
from fractions import Fraction as F
from itertools import combinations
import json

def neighbors(vertices,edges):
    a={v:set() for v in vertices}
    for u,v in edges:a[u].add(v);a[v].add(u)
    return a

def community(group,adj):
    inward={v:len(adj[v]&group) for v in group};outward={v:len(adj[v]-group) for v in group}
    return dict(strong=all(inward[v]>outward[v] for v in group),weak=sum(inward.values())>sum(outward.values()),inward=inward,outward=outward,internal_degree_sum=sum(inward.values()),external_degree_sum=sum(outward.values()))

def triangle_score(u,v,adj):
    denominator=min(len(adj[u])-1,len(adj[v])-1)
    assert v in adj[u] and denominator>=0
    return None if denominator==0 else F(len(adj[u]&adj[v])+1,denominator)

# Four-path: validating against the original graph differs from using the cut graph.
vertices=set(range(4));edges={(0,1),(1,2),(2,3)};a=neighbors(vertices,edges)
groups=[{0,1},{2,3}];original=[community(g,a) for g in groups]
assert all(x['weak'] and not x['strong'] for x in original)
assert [(x['internal_degree_sum'],x['external_degree_sum']) for x in original]==[(2,1),(2,1)]
cut=neighbors(vertices,edges-{(1,2)});wrong_graph=[community(g,cut) for g in groups]
assert all(x['strong'] for x in wrong_graph)
assert sum(x['weak'] for x in original)>=2 and sum(x['strong'] for x in original)<2
# A single qualifying child is insufficient for the source's split-retention test.
children=[{0},{1,2,3}];single=[community(g,a) for g in children]
assert sum(x['weak'] for x in single)==1
# Scores are modified rankings, not probabilities. Source assigns infinity to leaf edges.
path_scores={str(e):triangle_score(*e,a) for e in sorted(edges)}
assert path_scores['(1, 2)']==1 and path_scores['(0, 1)'] is None and path_scores['(2, 3)'] is None
triangle=neighbors(set(range(3)),set(combinations(range(3),2)))
clique=neighbors(set(range(4)),set(combinations(range(4),2)))
assert triangle_score(0,1,triangle)==2 and triangle_score(0,1,clique)==F(3,2)
# Triangle-free cycles give tied finite triangle scores without proving absence of communities.
cycle=neighbors(vertices,{(0,1),(1,2),(2,3),(0,3)})
assert {triangle_score(u,v,cycle) for u,v in [(0,1),(1,2),(2,3),(0,3)]}=={F(1)}
print(json.dumps(dict(original_path_children=original,children_on_deleted_graph=wrong_graph,one_qualifying_weak_child_rejected=True,modified_path_scores={k:'infinity (source convention)' if v is None else str(v) for k,v in path_scores.items()},triangle_score='2',four_clique_score='3/2',triangle_free_cycle_scores='all1',scope='Exact strong/weak degree tests on original adjacency; retention needs at least two qualifying children; explicit g3 rankings and source infinity convention. None is only an internal sentinel serialized as infinity text. No g4 denominator, author implementation, benchmark or universal structural guarantee.'),indent=2))
