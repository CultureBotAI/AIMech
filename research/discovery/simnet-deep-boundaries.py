"""Chosen SimNet operator identities and boundary cases; no author implementation."""
from math import exp,log,isclose
import json

def mex(values,xi):
 if xi==0:return sum(values)/len(values)
 scaled=[xi*v for v in values];shift=max(scaled)
 return (shift+log(sum(exp(v-shift) for v in scaled)/len(values)))/xi
values=[-1.,2.,3.]
assert min(values)<mex(values,1)<max(values)
assert isclose(mex(values,0),4/3)
assert abs(mex(values,1000)-max(values))<.002
assert abs(mex(values,-1000)-min(values))<.002
# Equal group sizes and common parameter give the stated nested collapse.
groups=[[0.,1.],[2.,4.]]
collapsed=mex([mex(g,1) for g in groups],1);flat=mex(sum(groups,[]),1)
assert isclose(collapsed,flat)
# Unequal groups change normalization; different parameters also break this identity.
unequal=[[0.],[1.,2.,4.]]
assert not isclose(mex([mex(g,1) for g in unequal],1),flat)
assert not isclose(mex([mex(g,1) for g in groups],0),flat)
# Finite MEX with the extra zero is not exact ReLU.
finite_relu=mex([-.5,0.],1);assert finite_relu<0
# Positive-xi, unit-weight l2 identity: MEX of similarities+offsets equals log kernel sum.
x=.4;templates=[-.2,.9];offsets=[.1,-.3];xi=.7
lhs=mex([-(x-z)**2+b for z,b in zip(templates,offsets)],xi)
rhs=log(sum(exp(xi*b)*exp(-xi*(x-z)**2) for z,b in zip(templates,offsets))/2)/xi
assert isclose(lhs,rhs)
# Averaging real class scores can disagree with hard majority voting.
scores=[(1.,0.),(1.,0.),(0.,10.)]
assert sum(a>b for a,b in scores)==2 and sum(a for a,b in scores)<sum(b for a,b in scores)
result=dict(mex_positive=mex(values,1),mex_zero_limit=mex(values,0),mex_max_approx=mex(values,1000),mex_min_approx=mex(values,-1000),equal_group_collapse=collapsed,unequal_group_nested=mex([mex(g,1) for g in unequal],1),different_parameter_nested=mex([mex(g,1) for g in groups],0),finite_relu_surrogate=finite_relu,kernel_identity_lhs=lhs,kernel_identity_rhs=rhs,hard_majority_class=0,mean_score_class=1)

from math import sqrt
xs=[-sqrt(1.5),0.,sqrt(1.5)];ys=[(x*x-1)/sqrt(.5) for x in xs]
assert isclose(sum(xs)/3,0,abs_tol=1e-12) and isclose(sum(ys)/3,0,abs_tol=1e-12)
assert isclose(sum(x*x for x in xs)/3,1) and isclose(sum(y*y for y in ys)/3,1)
assert isclose(sum(x*y for x,y in zip(xs,ys))/3,0,abs_tol=1e-12)
dependence=sum(x*x*y for x,y in zip(xs,ys))/3
assert abs(dependence)>0.1
result.update(whitened_variances=[1.,1.],whitened_covariance=0.,dependent_cross_moment=dependence)
print(json.dumps(result,sort_keys=True))
