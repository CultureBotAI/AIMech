"""Finite exact constructions for breadth-limited repeated search, not author code."""
from fractions import Fraction as F
from math import comb
from itertools import combinations,product
import json

def choose(n,k):return comb(n,k) if 0<=k<=n else 0

def failure(b,s,c,d):
    q=F(0)
    law=[F(choose(s,i)*choose(b-s,c-i),choose(b,c)) for i in range(c+1)]
    assert sum(law)==1
    for _ in range(d):q=sum(p*q**i for i,p in enumerate(law))
    return q
assert failure(4,2,2,1)==F(1,6)
assert failure(4,2,2,2)==F(61,216)
for d in range(1,8):assert failure(4,2,3,d)==0
for b in range(2,9):
    for s in range(1,b+1):
        c=b-s+1
        assert all(set(good)&set(range(c)) for good in combinations(range(b),s))

# Every node has b ordered children. Breadth c retains c per parent, not c globally.
def leaves(b,d,c,prefix=()):
    return [prefix] if d==0 else [leaf for j in range(min(b,c)) for leaf in leaves(b,d-1,c,prefix+(j,))]
assert len(leaves(4,2,2))==4
assert leaves(2,3,2)==leaves(2,3,3)

# Explicit finite tree, goal only at the last child of root. First pass revisits nodes.
def dfs(tree,c,goal_name):
    visited=[]
    def visit(t):
        visited.append(t if isinstance(t,str) else 'internal')
        if isinstance(t,str):return t if t==goal_name else None
        for child in t[:c]:
            found=visit(child)
            if found is not None:return found
        return None
    return visit(tree),visited
tr=['fail0','fail1','goal'];first,v1=dfs(tr,2,'goal');second,v2=dfs(tr,3,'goal');direct,vd=dfs(tr,3,'goal')
assert first is None and second==direct=='goal' and len(v1)+len(v2)==7>len(vd)==4

# With fixed ordering failure of a wider pass implies failure of a narrower pass.
# Rearranging the order destroys that implication: width2 finds g, width3 can omit g.
labels=['g','a','b','c'];old=set(labels[:2]);new=set(['a','b','c','g'][:3])
assert 'g' in old and 'g' not in new

# Goals are accepted by traversal order; the search rule has no path-cost comparison.
goal_cost={'expensive':10,'cheap':1}
assert goal_cost[next(x for x in ['expensive','cheap'] if x in goal_cost)]==10>min(goal_cost.values())
print(json.dumps(dict(model_failure_depth1=str(failure(4,2,2,1)),model_failure_depth2=str(failure(4,2,2,2)),model_success_depth2=str(1-failure(4,2,2,2)),pigeonhole_cutoff='b-s+1',per_parent_width2_depth2_leaf_count=4,binary_width2_already_full=True,repeated_vs_direct_node_visits=[7,4],changed_order_breaks_nested_failure=True,first_goal_cost_vs_minimum=[10,1],scope='Finite arithmetic and search constructions. Does not certify approximate expected-time analysis, infinite-tree completeness, author implementation or benchmark speedup.'),indent=2))
