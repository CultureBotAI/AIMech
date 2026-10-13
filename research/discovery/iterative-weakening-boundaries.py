"""Finite policy-cost constructions, separate from the paper's formal claims."""
from fractions import Fraction as F
from math import isqrt
import json

geometric=[];linear=[]
for m in [2,4,8,16]:
    geometric.append(str(F(sum(2**i for i in range(1,m+1)),2**m)))
    linear.append(str(F(sum(range(1,m+1)),m)))
assert all(F(x)<2 for x in geometric)
assert linear==['3/2','5/2','9/2','17/2']
# An exponential upper bound alone does not impose exponential growth.
constant_cost_ratios=[m for m in [2,4,8,16]]
assert all(1<=2**i for i in range(1,17))

# Equal-cost multiplicity remains even when per-state cost grows exponentially.
m=8
sum_cost=sum(2**(i+j) for i in range(1,m) for j in range(1,m) if i+j<=m)
assert sum_cost==sum((k-1)*2**k for k in range(2,m+1))
# A sufficient bias (1,m) costs 2^(m+1); a diagonal policy first reaches (m,m).
diagonal_last_ratio=F(2**(2*m),2**(m+1));assert diagonal_last_ratio==128
# In the dual-sum case its diagonal cost is at most twice the asymmetric state's cost.
assert F(2*2**m,2+2**m)<2

pairs=[(i,6//i) for i in range(1,7) if 6%i==0]
assert len(pairs)==4 and len(pairs)**2>6
assert len(pairs)<=2*isqrt(6)

# A separately labeled integer-budget construction for the paper's joint b,d idea.
def width(k,d):
    lo,hi=1,2**k+1
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid**d<=2**k:lo=mid
        else:hi=mid
    return lo
cases=0
for b in range(2,13):
    for d in range(1,7):
        N=b**d;K=(N-1).bit_length();B=width(K,d)
        assert B>=b and N<=B**d<=2**K<2*N
        cases+=1
for K in range(1,13):
    total=sum(width(k,d)**d for k in range(1,K+1) for d in range(1,k+1))
    assert total<=sum(k*2**k for k in range(1,K+1))<2*K*2**K
# Literal integer k=d log2(b) misses b=3, d=1 because 3 is not a power of two.
assert 3 & (3-1) != 0
print(json.dumps(dict(geometric_total_to_final_ratios=geometric,linear_total_to_final_ratios=linear,constant_cost_upper_bound_only_ratios=constant_cost_ratios,two_dimension_exponent8_total_cost=sum_cost,asymmetric_product_cost_diagonal_last_ratio=str(diagonal_last_ratio),ordered_factor_pairs6=pairs,integer_budget_dominance_cases=cases,joint_budget_scope='Curator construction uses floor(2^(k/d)) with b>=2 and componentwise sufficiency; width1 paths need separate treatment. Not a transcription or certification of the printed procedure.',scope='Finite cost-model checks. No search benchmarks, author code or proof of all optimal-policy claims.'),indent=2))
