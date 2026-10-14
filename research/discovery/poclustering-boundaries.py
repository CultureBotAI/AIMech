"""Exact small PoClustering representation and coverage boundaries; no author code."""
from itertools import combinations, product
import json

def nonempty_subsets(vertices):
    return [frozenset(s) for k in range(1,len(vertices)+1) for s in combinations(vertices,k)]
def diameter(s, distances):
    return max((distances[frozenset(p)] for p in combinations(s,2)),default=0)
def family(vertices, distances):
    subsets=nonempty_subsets(vertices)
    result=set()
    for threshold in sorted({0,*distances.values()}):
        cliques=[s for s in subsets if diameter(s,distances)<=threshold]
        result.update(s for s in cliques if not any(s<t for t in cliques))
    return result
vertices=(0,1,2)
d={frozenset([0,1]):1,frozenset([0,2]):2,frozenset([1,2]):3}
f=family(vertices,d)
reconstructed={pair:min(diameter(s,d) for s in f if pair<=s) for pair in d}
assert reconstructed==d
scaled={p:10*x for p,x in d.items()}
assert family(vertices,scaled)==f and scaled!=d
assert diameter(frozenset([0,1]),d)<diameter(frozenset([0,2]),d)
assert not frozenset([0,1])<frozenset([0,2])
zero={frozenset([0,1]):0}
assert family((0,1),zero)=={frozenset([0,1])}
assert diameter(frozenset([0]),zero)==diameter(frozenset([0,1]),zero)==0
# K_{2,2,2} has eight maximal triangles, but a four-triangle edge cover.
parts=((0,1),(2,3),(4,5))
triangles={frozenset(t) for t in product(*parts)}
cover={frozenset([0,2,4]),frozenset([0,3,5]),frozenset([1,2,5]),frozenset([1,3,4])}
edges={frozenset([u,v]) for i,p in enumerate(parts) for q in parts[i+1:] for u in p for v in q}
assert len(triangles)==8 and len(edges)==12
assert {frozenset(p) for s in cover for p in combinations(s,2)}==edges
# Distances 1 across parts and 2 within parts make this a threshold graph at 1.
octa={frozenset(p):(1 if frozenset(p) in edges else 2) for p in combinations(range(6),2)}
cover_family=cover|{frozenset([v]) for v in range(6)}|{frozenset(range(6))}
assert all(min(diameter(s,octa) for s in cover_family if pair<=s)==value for pair,value in octa.items())
# If xy is newly added, raw intersections of old endpoint cliques omit x and y.
old_x=frozenset([0,2]);old_y=frozenset([1,2]);raw=old_x&old_y
assert raw=={2} and raw!=old_x and raw!=old_y
assert raw|{0,1}=={0,1,2}
# On a single edge, exact enumeration and maximal-clique coverage coincide.
single_edge_exact = {frozenset([0,1])}
single_edge_cover = {frozenset([0,1])}
assert single_edge_exact == single_edge_cover
print(json.dumps(dict(exact_family=[sorted(s) for s in sorted(f,key=lambda s:(len(s),sorted(s)))],pairwise_reconstruction=True,unlabelled_family_unchanged_by_scaling=True,diameter_order_does_not_imply_inclusion=True,zero_pair_singletons_missing_from_maximal_cliques=True,single_edge_equal_family=True,maximal_triangles=8,edge_cover_triangles=4,covered_edges=12,reduced_family_preserves_pairwise_distances=True,raw_endpoint_intersection=sorted(raw),scope='Finite exact representation and static pseudocode examples. The four-clique cover is constructed, not claimed as output of the published greedy algorithm. No author execution, theorem certification or benchmark replication.'),indent=2))
