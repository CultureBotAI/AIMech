"""Finite rational recurrence and cache-boundary checks, not author software."""
from fractions import Fraction as F
from functools import lru_cache
import json
h={'A':0,'B':1};beta={'A':F(2),'B':F(1)}
p={'A':{'A':F(1,4),'B':F(3,4)},'B':{'A':F(1,2),'B':F(1,2)}}
@lru_cache(None)
def cached(t,b):
    if b<0 or h[t]>b:return F(0)
    return 1+beta[t]*sum(p[t][u]*cached(u,b-1) for u in h)
def forward(frontier,b):
    active={t:F(n) for t,n in frontier.items()};total=F(0)
    for depth in range(b+1):
        active={t:n for t,n in active.items() if h[t]<=b-depth}
        total+=sum(active.values())
        active={u:sum(n*beta[t]*p[t][u] for t,n in active.items()) for u in h}
    return total
for t in h:
    for b in range(7):assert cached(t,b)==forward({t:1},b)
assert cached('A',3)==F(27,4)
frontier={'A':1,'B':1};prefix_expanded=1;remaining=2
lookup_total=prefix_expanded+sum(n*cached(t,remaining) for t,n in frontier.items())
assert lookup_total==prefix_expanded+forward(frontier,remaining)==F(15,2)
incorrect_double_count=lookup_total+sum(frontier.values())
assert incorrect_double_count==F(19,2)

# Equality of recurrences is not equality with every concrete start tree.
assert cached('A',1)==F(3,2)
actual_same_label_start=3  # root and two allowed h=0 children
assert cached('A',1)!=actual_same_label_start

# A depth-dependent cutoff changes the law even at the same type and budget.
early_row={'A':F(0),'B':F(1)}
late_row={'A':F(1,5),'B':F(4,5)}
stage_values=[1+2*r['A'] for r in [early_row,late_row]]
assert stage_values==[1,F(7,5)]

# Illustrative costs in arbitrary units: preprocessing must be counted.
def direct_cost(q):return 10000+q
def lookup_cost(q):return 10100+F(q,100)
assert lookup_cost(1)>direct_cost(1)
assert lookup_cost(102)<direct_cost(102)
print(json.dumps({
 'fixed_model_cached_equals_forward_cases':14,
 'root_A_budget3_prediction':str(cached('A',3)),
 'prefix_plus_frontier_prediction':str(lookup_total),
 'incorrect_frontier_double_count':str(incorrect_double_count),
 'model_prediction_and_concrete_tree_count':[str(cached('A',1)),actual_same_label_start],
 'same_type_budget_different_stage_values':[str(x) for x in stage_values],
 'illustrative_one_query_costs':[str(direct_cost(1)),str(lookup_cost(1))],
 'illustrative_102_query_costs':[str(direct_cost(102)),str(lookup_cost(102))],
 'scope':'Fixed-model arithmetic equivalence and boundary constructions, not measured runtime or empirical replication.'
},indent=2))
