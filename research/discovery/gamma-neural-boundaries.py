"""Constructed gamma-memory algebra and derivatives; no fitting or author code."""
from fractions import Fraction as F
from math import comb, factorial, isclose
import json

def discrete(mu,K,inputs,init=None):
    x=[F(0)]*K if init is None else list(init);rows=[x[:]]
    for u in inputs:
        previous=[F(u)]+x
        x=[(1-mu)*x[k]+mu*previous[k] for k in range(K)]
        rows.append(x[:])
    return rows
mu=F(1,2);K=3;rows=discrete(mu,K,[1]+[0]*9)
for n,row in enumerate(rows):
    for k,val in enumerate(row,1):
        explicit=F(0) if n<k else F(comb(n-1,k-1))*mu**k*(1-mu)**(n-k)
        assert val==explicit
one=discrete(F(1),3,[1,0,0,0]);assert one[1]==[1,0,0] and one[2]==[0,1,0] and one[3]==[0,0,1]
frozen=discrete(F(0),2,[1,4,-3],init=[F(2),F(-1)]);assert all(x==[2,-1] for x in frozen)
endpoint=discrete(F(2),1,[(-1)**j for j in range(8)]);assert [r[0] for r in endpoint]==[0,2,-4,6,-8,10,-12,14,-16]
# Integral of t^j exp(-mu*t) is j!/mu^(j+1), mu>0.
k=3;rate=F(2);mass=rate**k/F(factorial(k-1))*F(factorial(k-1),1)/rate**k
mean=rate**k/F(factorial(k-1))*F(factorial(k),1)/rate**(k+1)
second=rate**k/F(factorial(k-1))*F(factorial(k+1),1)/rate**(k+2)
assert mass==1 and mean==F(3,2) and second-mean*mean==F(3,4)
# Fixed-mu sensitivity with zero states and parameter-independent inputs.
def run(m):
    x=[0.,0.];a=[0.,0.]
    for u in [1.,-.2,.6,0.]:
        old=[u]+x;oa=[0.]+a
        an=[(1-m)*a[k]+m*oa[k]+old[k]-x[k] for k in range(2)]
        x=[(1-m)*x[k]+m*old[k] for k in range(2)];a=an
    return x,a
x,a=run(.4);hi,_=run(.400001);lo,_=run(.399999);fd=[(h-l)/.000002 for h,l in zip(hi,lo)]
assert all(isclose(v,w,abs_tol=1e-9) for v,w in zip(a,fd))
print(json.dumps(dict(half_rate_impulse_first_five=[[str(v) for v in row] for row in rows[:6]],unit_rate_delay_line=[[str(v) for v in row] for row in one],zero_rate_nonzero_initial_states=[[str(v) for v in row] for row in frozen],two_rate_bounded_input_unbounded_output=[str(r[0]) for r in endpoint],continuous_order3_rate2=dict(mass=str(mass),mean=str(mean),variance=str(second-mean*mean)),fixed_rate_sensitivities=a,finite_difference_sensitivities=fd),indent=2))
