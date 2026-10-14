"""Finite HAC-ES external-vertex neighborhood checks, not author execution."""
from fractions import Fraction as F
import json

edges={frozenset(x) for x in [('a1','b'),('a1','c'),('a2','c'),('b','c'),('d','e'),('d','f')]}
def adjacent(a,b,graph=edges):return frozenset((a,b)) in graph
def score(a,b,graph=edges):
    assert a and b and not a&b
    vertices=set().union(*graph)
    external=vertices-a-b
    na={u for u in external if any(adjacent(x,u,graph) for x in a)}
    nb={u for u in external if any(adjacent(x,u,graph) for x in b)}
    density=F(sum(adjacent(x,y,graph) for x in a for y in b),len(a)*len(b))
    overlap=F(len(na&nb),len(na|nb)) if na|nb else None
    return density,overlap
ab=score({'a1','a2'},{'b'});de=score({'d'},{'e'})
assert ab==(F(1,2),F(1)) and de==(F(1),F(0))
assert ab[0]<de[0] and sum(ab)>sum(de)
# External vertex c counts once despite touching both members of the first group.
assert sum(adjacent(x,'c') for x in {'a1','a2'})==2
# A graph containing only a single edge gives no external neighboring vertices.
single=score({'a'},{'b'},{frozenset(('a','b'))})
assert single==(F(1),None)
print(json.dumps(dict(pair_ab_edge_density=str(ab[0]),pair_ab_shared_vertex_jaccard=str(ab[1]),pair_ab_combined_score=str(sum(ab)),pair_de_edge_density=str(de[0]),pair_de_shared_vertex_jaccard=str(de[1]),pair_de_combined_score=str(sum(de)),external_vertex_c_contribution='1 despite two incident edges from group A',single_edge_density=str(single[0]),single_edge_shared_score=single[1],scope='Candidate-pair score reversal and undefined empty-union boundary only. The pairs are not claimed to be selected in a full run; no author convention for 0/0 is invented.'),indent=2))
