"""Finite modularity examples for the symmetric convention in Newman2003 note19.

Curator reference calculations, not author software or benchmark replication.
"""
from fractions import Fraction as F
from itertools import combinations
import json

def edge_fractions(groups,weights):
    total=sum(weights.values())
    e=[[F(0) for _ in groups] for _ in groups]
    owners={v:i for i,g in enumerate(groups) for v in g}
    for edge,w in weights.items():
        u,v=tuple(edge);i,j=owners[u],owners[v]
        if i==j:e[i][i]+=F(w,total)
        else:e[i][j]+=F(w,2*total);e[j][i]+=F(w,2*total)
    return e

def score(groups,weights):
    e=edge_fractions(groups,weights)
    return sum(e[i][i]-sum(e[i])**2 for i in range(len(groups)))

def joined(groups,i,j):return sorted([g for k,g in enumerate(groups) if k not in (i,j)]+[groups[i]|groups[j]],key=lambda g:tuple(sorted(g)))

w={frozenset((i,i+1)):1 for i in range(5)};gs=[{i} for i in range(6)]
e=edge_fractions(gs,w);gain=2*(e[0][1]-sum(e[0])*sum(e[1]))
assert gain==score(joined(gs,0,1),w)-score(gs,w)==F(4,25)
assert sum(map(sum,e))==1 and e==list(map(list,zip(*e)))
trajectory=[score(gs,w)];merges=[]
while len(gs)>1:
    e=edge_fractions(gs,w);a=list(map(sum,e));options=[]
    for i,j in combinations(range(len(gs)),2):
        if e[i][j]>0:options.append((2*(e[i][j]-a[i]*a[j]),tuple(sorted(gs[i])),tuple(sorted(gs[j])),i,j))
    best=min(options,key=lambda x:(-x[0],x[1],x[2]));new=joined(gs,best[3],best[4]);q=score(new,w)
    assert q-trajectory[-1]==best[0]
    merges.append([list(best[1]),list(best[2]),str(best[0])]);trajectory.append(q);gs=new
alternative=score([{0,1,2},{3,4,5}],w)
assert max(trajectory)==F(13,50)<alternative==F(3,10)

# Re-running on an induced subgraph redefines edge normalization and degrees.
subw={edge:weight for edge,weight in w.items() if edge<={0,1,2}};subgs=[{0},{1},{2}]
subgain=score(joined(subgs,0,1),subw)-score(subgs,subw)
assert subgain==F(1,4)!=gain
# Normalized fractions preserve the objective under positive common scaling.
partition=[{0,1,2},{3,4,5}];scaled={edge:7*weight for edge,weight in w.items()}
assert edge_fractions(partition,w)==edge_fractions(partition,scaled)
assert score(partition,w)==score(partition,scaled)
# Disconnected components cannot be joined when only positive e_ij are eligible.
wd={frozenset((0,1)):1,frozenset((2,3)):1};ed=edge_fractions([{0,1},{2,3}],wd)
assert ed[0][1]==0
print(json.dumps(dict(symmetric_fraction_total=str(sum(map(sum,e))),initial_six_path_gain=str(gain),greedy_joins=merges,greedy_trajectory=[str(q) for q in trajectory],greedy_peak=str(max(trajectory)),better_feasible_partition=str(alternative),induced_three_path_gain=str(subgain),common_positive_weight_scaling_preserves_q=True,disconnected_cross_fraction=str(ed[0][1]),scope='Symmetric edge-fraction convention, exact local gains, fixed-tie greedy counterexample, induced-subgraph rescaling and positive common weight scaling. Not author-code conformance, benchmark replication or global optimum certification.'),indent=2))
