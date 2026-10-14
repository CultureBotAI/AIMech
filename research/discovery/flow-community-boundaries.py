"""Finite cut checks; not author implementation or universal theorem certification."""
from itertools import combinations
import json

def subsets(vertices):
 v=sorted(vertices)
 for mask in range(1<<len(v)):yield {v[i] for i in range(len(v)) if mask>>i&1}
def boundary(edges,c):return sum((u in c)!=(v in c) for u,v in edges)
def degrees(edges,c,v):
 neighbors={y if x==v else x for x,y in edges if v in (x,y)}
 return len(neighbors&c),len(neighbors-c)
def cuts(vertices,edges,seeds,k):
 candidates=[(k*boundary(edges,seeds|x)+len(x),sorted(seeds|x)) for x in subsets(vertices-seeds)]
 best=min(x[0] for x in candidates);return best,[x[1] for x in candidates if x[0]==best]
# IEEE2002 prose: infinite seed arcs, original graph arcs k, nonseed-to-sink arcs1.
v=set(range(4));e={(0,1),(0,2),(0,3)}
best,cs=cuts(v,e,{0},1)
assert best==3 and len(cs)==8
minimal=set.intersection(*(set(c) for c in cs));assert minimal=={0}
assert degrees(e,minimal,0)==(0,3)
# With a forced center seed, exact minimum-cut optimality does not certify the seed's degree criterion.
# Nonseed included vertices satisfy the single-move inequality in every enumerated optimal cut.
for c in cs:
 for x in set(c)-{0}:
  inside,outside=degrees(e,set(c),x);assert inside>outside
# Literal rescaling of the already inserted source arc destroys seed forcing.
literal=[(len({0}-c)+boundary(e,c)+len(c-{0}),c) for c in subsets(v)]
literal_best=min(x[0] for x in literal);literal_min=[x[1] for x in literal if x[0]==literal_best]
assert literal_best==1 and literal_min==[set()]
# KDD2000 Theorem1's local degree/source-size conditions do not force recovery of a prechosen C.
a=set(range(4));b=set(range(4,8));d=set(range(8,12));vertices=a|b|d
edges=set(combinations(sorted(a),2))|set(combinations(sorted(b),2))|set(combinations(sorted(d),2))|{(3,4),(6,8),(7,9)}
c=a|b;s=0;t=11;cut=boundary(edges,c)
assert cut==2 and all(degrees(edges,c,x)[0]>degrees(edges,c,x)[1] for x in c)
assert degrees(edges,c,s)[0]==3>cut and degrees(edges,d,t)[0]==3>cut
allcuts=[(boundary(edges,x|{s}),x|{s}) for x in subsets(vertices-{s,t})]
minvalue=min(z[0] for z in allcuts);mins=[z[1] for z in allcuts if z[0]==minvalue]
assert minvalue==1 and mins==[a]
print(json.dumps(dict(ieee2002_star=dict(k=1,seed=[0],minimum_cut_value=best,minimum_cuts=cs,minimal_source_side=sorted(minimal),seed_internal_external=[0,3],scope='Forced seeds are exempt from the ordinary one-vertex improvement argument; no claim that every cut policy returns the same source side.'),literal_source_arc_rescaling=dict(minimum_cut_value=literal_best,source_side_original_vertices=[],scope='Conditional interpretation of Figure2’s all-E rescaling after source arcs are inserted; differs from the prose preexisting-edge convention, not a claim about author software.'),kdd2000_nested_cliques=dict(proposed_community=sorted(c),source=s,sink=t,proposed_boundary=cut,source_internal_degree=3,sink_internal_degree=3,minimum_cut_value=minvalue,unique_minimum_source_side=sorted(mins[0]),scope='The stated local inequalities and source/sink degree bounds alone do not force exact recovery of this prechosen community; a valid nested subcommunity has a smaller cut.'),limitations='Finite exhaustive cut calculations under explicitly stated graph conventions; no author-code execution, web crawl, benchmark replication or universal theorem certification.'),indent=2))
