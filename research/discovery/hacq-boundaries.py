"""Finite HAC-Q modularity and representation checks, not author execution."""
from fractions import Fraction as F
import json

# Three-vertex path a--b--c. Q12 equals E times the standard normalized
# modularity change when only groups 1 and 2 are merged.
vertices={'a','b','c'};edges={frozenset(('a','b')),frozenset(('b','c'))};E=len(edges)
degree={v:sum(v in e for e in edges) for v in vertices}
def score(a,b):
    observed=sum(frozenset((u,v)) in edges for u in a for v in b)
    return observed-F(sum(degree[u] for u in a)*sum(degree[v] for v in b),2*E)
def modularity(groups):
    return sum(F(sum(e<=g for e in edges),E)-F(sum(degree[v] for v in g),2*E)**2 for g in groups)
q0=modularity([{'a'},{'b'},{'c'}]);q1=modularity([{'a'},{'b','c'}]);q2=modularity([vertices])
s=score({'b'},{'c'})
assert (q0,q1,q2)==(F(-3,8),F(-1,8),F(0))
assert s==F(1,2) and q1-q0==s/E==F(1,4)
assert score({'a'},{'c'})==F(-1,4)
# Conditional on retaining the binary tree (b,c), then a, its density estimates
# differ from those of the one-block partition. This is not a claim about an
# uninspected collapse/stopping convention or the degree-filtered experiment.
flat=F(2,3);retained_bc=F(1);retained_a_bc=F(1,2)
assert retained_a_bc<flat<retained_bc
print(json.dumps(dict(modularity_singletons=str(q0),modularity_after_bc=str(q1),modularity_one_block=str(q2),bc_score=str(s),normalized_modularity_gain=str(s/E),nonadjacent_ac_score='-1/4',flat_one_block_density=str(flat),conditional_retained_bc_density=str(retained_bc),conditional_retained_a_bc_density=str(retained_a_bc),edgeless_formula_denominator='0',scope='Static modularity identity and conditional tree-versus-partition prediction example. No full run, collapse/stopping behavior, empirical comparison or global modularity guarantee is asserted.'),indent=2))
