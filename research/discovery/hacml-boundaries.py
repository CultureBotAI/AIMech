"""Exact finite source-formula checks; no HAC-ML implementation execution."""
from fractions import Fraction as F
from math import factorial
import json

def ml(e,h):
    if e+h==0:return F(1)
    return F(e**e*h**h,(e+h)**(e+h))

def bayes(e,h):
    return F(factorial(e)*factorial(h),factorial(e+h+1))

# Two singleton groups disagree about their edge to one external singleton.
ratio=ml(1,1)/(ml(1,0)*ml(0,1))
bayes_ratio=bayes(1,1)/(bayes(1,0)*bayes(0,1))
assert ratio==F(1,4) and ratio!=F(1,2) and bayes_ratio==F(2,3)
# Agreement about the external edge has different integrated/profiled scores.
same_ml=ml(2,0)/(ml(1,0)**2)
same_bayes=bayes(2,0)/(bayes(1,0)**2)
assert same_ml==1 and same_bayes==F(4,3)
# Eq8: two singleton groups have no within-group pairs; collapse ratio is one.
assert all(bayes(e,1-e)/(bayes(0,0)**2*bayes(e,1-e))==1 for e in (0,1))
# Independent types multiply scores, whereas their log scores add.
assert ratio*ratio==F(1,16)
# Balanced test precision differs from deployment precision with sparse positives.
tpr=fpr=F(1,2)
balanced=tpr/(tpr+fpr)
pi=F(1,100)
sparse=pi*tpr/(pi*tpr+(1-pi)*fpr)
assert balanced==F(1,2) and sparse==F(1,100)
print(json.dumps(dict(single_mismatch_profile_ratio=str(ratio),printed_single_mismatch_expression='1/2',single_mismatch_integrated_ratio=str(bayes_ratio),matching_external_edges_profile_ratio=str(same_ml),matching_external_edges_integrated_ratio=str(same_bayes),singleton_collapse_ratio='1',two_independent_mismatch_types_ratio='1/16',balanced_test_precision=str(balanced),precision_at_one_percent_prevalence=str(sparse),scope='Exact source-formula and base-rate examples. No author code, full merge sequence, benchmark or universal optimality claim.'),indent=2))
