"""Constructed checks of Equation 1; no SimNet training or author code."""
import json
from math import exp,log,isclose
def mex(x,xi):
    assert len(x)>0
    if xi==0:return sum(x)/len(x)
    z=[xi*t for t in x];m=max(z)
    return (m+log(sum(exp(t-m) for t in z))-log(len(x)))/xi
x=[-2.,1.,4.];xi=1.3
value=mex(x,xi);z=[exp(xi*(t-max(x))) for t in x];gradient=[t/sum(z) for t in z]
eps=1e-5;numeric=[]
for i in range(len(x)):
    lo=x.copy();hi=x.copy();lo[i]-=eps;hi[i]+=eps
    numeric.append((mex(hi,xi)-mex(lo,xi))/(2*eps))
assert all(isclose(a,b,abs_tol=1e-8) for a,b in zip(gradient,numeric))
assert isclose(sum(gradient),1) and value!=sum(gradient)
lse=log(sum(exp(xi*t) for t in x))/xi
assert isclose(value,lse-log(len(x))/xi)
assert isclose(mex([t+7 for t in x],xi),value+7)
assert isclose(mex([3,3,3],xi),3)
groups=[[-2,1],[4,7]];flat=sum(groups,[])
nested=mex([mex(g,xi) for g in groups],xi)
assert isclose(nested,mex(flat,xi))
unequal=[[-2],[1,4,7]];unbalanced=mex([mex(g,xi) for g in unequal],xi)
assert not isclose(unbalanced,mex(flat,xi))
mixed=mex([mex(g,xi) for g in groups],0)
assert not isclose(mixed,mex(flat,xi))
finite_relu=mex([-.5,0.],1);assert finite_relu<0
assert abs(mex(x,10000)-max(x))<.001 and abs(mex(x,-10000)-min(x))<.001
assert isclose(mex(x,0),1.)
print(json.dumps(dict(value=value,normalized_input_gradient=gradient,numerical_gradient=numeric,log_sum_exp_scaled=lse,normalization_offset=log(len(x))/xi,equal_group_nested=nested,flattened=mex(flat,xi),unequal_group_nested=unbalanced,mixed_parameter_nested=mixed,finite_zero_augmented_value=finite_relu,positive_limit_approx=mex(x,10000),negative_limit_approx=mex(x,-10000),zero_limit=mex(x,0)),sort_keys=True))
