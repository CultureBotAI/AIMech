"""Finite NeXO construction/evaluation distinctions, not author code execution."""
from fractions import Fraction as F
from math import factorial
import json

def beta(e,h):return F(factorial(e)*factorial(h),factorial(e+h+1))

# Parent p groups terminals a,b; sibling s is c. Only a--c is an edge.
# The printed removal ratio compares pooled p--s with separate a--s,b--s.
removal=beta(1,1)/(beta(1,0)*beta(0,1))
within_children=F(0);parent_sibling=F(1,2)
assert removal==F(2,3) and removal<1 and within_children<=parent_sibling
# If a,b are themselves joined, the independent density guard fails.
assert not F(1)<=parent_sibling
# Literal p10 bootstrap expression is reciprocal n*sum, not the arithmetic mean.
scores=[F(1,2),F(1,2)];literal=1/(len(scores)*sum(scores));mean=sum(scores)/len(scores)
assert literal==mean==F(1,2)
scores2=[F(1,4),F(1,4)];literal2=1/(len(scores2)*sum(scores2));mean2=sum(scores2)/len(scores2)
assert literal2==1 and mean2==F(1,4) and literal2>literal
assert sum([F(0),F(0)])==0 # Literal reciprocal is undefined here.
print(json.dumps(dict(removal_ratio=str(removal),density_guard_for_absent_child_edge=True,density_guard_for_present_child_edge=False,bootstrap_scores_first=['1/2','1/2'],literal_first=str(literal),mean_first=str(mean),bootstrap_scores_second=['1/4','1/4'],literal_second=str(literal2),mean_second=str(mean2),all_zero_scores_literal_denominator='0',scope='Static printed-formula checks only. The literal bootstrap expression is not silently replaced by a mean; the implementation and intended correction remain unverified.'),indent=2))
