"""Finite curator examples, not author-code execution or theorem certification."""
from fractions import Fraction as F
import json

points={0:0,1:1,2:10}
H={frozenset([i]) for i in points}
def score(a,b):
    return sum((F(11-abs(points[i]-points[j])) for i in a for j in b),F())/(len(a)*len(b))
choices={a:max(H-{a},key=lambda b:score(a,b)) for a in H}
next_h={a|b for a,b in choices.items()}
D=H|next_h
assert len(next_h)==2 and frozenset(points) not in D
# Average linkage from A union B to C, where A and B overlap.
A={0,1};B={1,2};values={0:F(0),1:F(9),2:F(0)}
exact=sum(values[i] for i in A|B)/len(A|B)
weighted_tree_update=(sum(values[i] for i in A)+sum(values[i] for i in B))/(len(A)+len(B))
assert exact==3 and weighted_tree_update==F(9,2)
# Perfect two-leaf tree: ordered pairs / unordered pair normalizer.
printed_dp=F(2,1);conventional_dp=F(1,1)
assert printed_dp!=conventional_dp
print(json.dumps(dict(one_round_clusters=sorted([sorted(x) for x in next_h]),full_root_present=frozenset(points) in D,overlap_exact_average=str(exact),tree_update_average=str(weighted_tree_update),literal_printed_purity=str(printed_dp),unordered_pair_purity=str(conventional_dp),scope='Finite arithmetic examples only; no model fitting, theorem refutation or author implementation execution.'),indent=2))
