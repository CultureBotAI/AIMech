"""Exact small-graph modularity checks, not execution of author software."""
from fractions import Fraction as F
from itertools import combinations
import json

def modularity(groups,edges):
    m=len(edges);vertices=set().union(*groups)
    degree={v:sum(v in e for e in edges) for v in vertices}
    return sum(F(sum(e<=g for e in edges),m)-F(sum(degree[v] for v in g),2*m)**2 for g in groups)
def merge(groups,i,j):return [g for k,g in enumerate(groups) if k not in (i,j)]+[groups[i]|groups[j]]

# Printed Eq8 versus the gain derived from the paper's Eq4/Eq7, on a--b--c.
e3={frozenset((0,1)),frozenset((1,2))};groups=[{0},{1},{2}];m=len(e3)
a={0:F(1,4),1:F(1,2),2:F(1,4)}
q0=modularity(groups,e3);first=merge(groups,1,2);q1=modularity(first,e3)
literal_first=F(1,2*m)-a[1]*a[2]
true_first=q1-q0
assert literal_first==F(1,8) and true_first==F(1,4)
# After merging 1 and2, Eq10b subtracts twice a2*a0 from the other stored gain.
literal_second=(F(1,2*m)-a[0]*a[1])-2*a[2]*a[0]
true_second=modularity([{0,1,2}],e3)-q1
assert literal_second==0 and true_second==F(1,8)
literal_final=q0+literal_first+literal_second
assert literal_final==F(-1,4) and modularity([{0,1,2}],e3)==0

# A separate reference procedure uses gains recomputed directly from Eq4.
# Six-vertex path: fixed lexicographic ties; only adjacent communities eligible.
e6={frozenset((i,i+1)) for i in range(5)};gs=[{i} for i in range(6)];trajectory=[modularity(gs,e6)];joins=[]
while len(gs)>1:
    candidates=[]
    for i,j in combinations(range(len(gs)),2):
        if any(frozenset((u,v)) in e6 for u in gs[i] for v in gs[j]):
            candidate=merge(gs,i,j)
            candidates.append((modularity(candidate,e6)-trajectory[-1],tuple(sorted(gs[i])),tuple(sorted(gs[j])),i,j,candidate))
    best=min(candidates,key=lambda x:(-x[0],x[1],x[2]))
    joins.append([list(best[1]),list(best[2]),str(best[0])]);gs=sorted(best[5],key=lambda g:tuple(sorted(g)))
    trajectory.append(modularity(gs,e6))
alternative=modularity([{0,1,2},{3,4,5}],e6)
assert max(trajectory)==F(13,50)<alternative==F(3,10)

# After internal merges of two disconnected edges, no stored adjacent pair remains.
disconnected={frozenset((0,1)),frozenset((2,3))};component_groups=[{0,1},{2,3}]
eligible=[(i,j) for i,j in combinations(range(len(component_groups)),2) if any(frozenset((u,v)) in disconnected for u in component_groups[i] for v in component_groups[j])]
assert len(component_groups)==2 and eligible==[]
print(json.dumps(dict(printed_initial_gain=str(literal_first),definition_initial_gain=str(true_first),printed_second_gain=str(literal_second),definition_second_gain=str(true_second),literal_accumulated_final_q=str(literal_final),definition_one_block_q='0',definition_based_six_path_joins=joins,definition_based_six_path_trajectory=[str(q) for q in trajectory],greedy_peak=str(max(trajectory)),better_two_triple_partition_q=str(alternative),disconnected_remaining_groups=2,disconnected_adjacent_candidates=0,scope='Separate checks of printed formulas, a six-node exact-definition greedy reference with fixed ties, and disconnected candidate exhaustion. No author software, benchmark data, universal failure or implementation conformance is asserted.'),indent=2))
