"""Constructed counting boundaries; no author code or empirical replication."""
from fractions import Fraction as F
from math import comb
import json

def truncated(row, cutoff):
    kept=[p if p >= cutoff else F(0) for p in row]
    total=sum(kept)
    if not total:
        raise ValueError('Cutoff removes every positive entry')
    return [p/total for p in kept]

row=[F(1,20),F(3,20),F(4,5)]
cut=truncated(row,F(1,10))
assert cut == [0,F(3,19),F(16,19)]
assert truncated(row,F(3,20)) == cut  # equality is retained
try:
    truncated(row,F(9,10))
except ValueError:
    emptied=True
else:
    raise AssertionError('Empty-row normalization must not be accepted')
rows=[row,[F(2,5),F(3,5)]]
guarded=min(F(9,10),min(max(r) for r in rows))
assert guarded==F(3,5) and all(sum(truncated(r,guarded))==1 for r in rows)

# Probabilities of individual Bernoulli arrangements are not count probabilities.
p=F(1,2); n=2
literal=[p**j*(1-p)**(n-j) for j in range(n+1)]
count_pmf=[comb(n,j)*literal[j] for j in range(n+1)]
assert sum(literal)==F(3,4) and sum(count_pmf)==1

# One parent type, two child types in one coarser group, beta=2, N=1.
# Equation4's literal pair sum repeats the same parent offspring mass twice.
parent_mass=F(1); branch=F(2); child_probability=F(1,2)
pair_sum=2*parent_mass*branch
set_sum=parent_mass*branch
assert pair_sum*child_probability==2 and set_sum*child_probability==1

# Exact homogeneous type counts: ten children, one rare type with100 leaves,
# nine terminal common children. First-level cutoff deletes the rare type.
actual=1+10+100
untruncated=1+10+10*F(1,10)*100
rare_after=truncated([F(1,10),F(9,10)],F(1,5))[0]
with_cutoff=1+10+10*rare_after*100
assert actual==untruncated==111 and with_cutoff==11

# Cache context: same root type and remaining budget1, but different absolute
# stages use different retained transition rows. TypeA has h0, typeB has h1;
# at child remaining budget0 only A is expanded. Each root has two children.
stationary_row=[F(1,5),F(4,5)]
early_row=truncated(stationary_row,F(3,10))
late_row=truncated(stationary_row,F(0))
early_prediction=1+2*early_row[0]
late_prediction=1+2*late_row[0]
assert early_prediction==1 and late_prediction==F(7,5)

print(json.dumps({
 'strict_cutoff_and_renormalization':[str(x) for x in cut],
 'equal_cutoff_retained':True,'empty_row_rejected':emptied,
 'guarded_common_cutoff':str(guarded),
 'literal_arrangement_weight_sum':str(sum(literal)),
 'binomial_count_probability_sum':str(sum(count_pmf)),
 'literal_pair_sum_child_count':str(pair_sum*child_probability),
 'distinct_parent_sum_child_count':str(set_sum*child_probability),
 'homogeneous_tree_actual_and_original_prediction':actual,
 'truncated_prediction':str(with_cutoff),
 'same_type_budget_different_stage_predictions':[str(early_prediction),str(late_prediction)],
 'scope':'Constructed mathematical checks, not author-code validation or replication.'
},indent=2))
