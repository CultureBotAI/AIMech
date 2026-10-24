"""Constructed checks of the learned centered power mean, not author code."""
import json
from math import exp,log1p,isclose,sqrt
def lp(a,p,c=None):
    c=[0.]*len(a) if c is None else c
    assert len(a)>0 and len(a)==len(c) and p>=1
    v=[abs(x-y) for x,y in zip(a,c)];m=max(v)
    return 0. if m==0 else m*(sum((x/m)**p for x in v)/len(v))**(1/p)
a=[-3.,1.];mean=sum(a)/2
assert lp(a,1)==2 and mean==-1
assert isclose(lp(a,2),sqrt(5))
assert lp(a,8)<3 and abs(lp(a,10000)-3)<.001
assert max(a)==1 and max(map(abs,a))==3
p=1+log1p(exp(0));assert p>1
# Learned centers invalidate original-input norm axioms in general.
center=[1.];at0=lp([0.],2,center);at1=lp([1.],2,center)
assert at0==1 and at1==0 and lp([2.],2,center)!=2*at1
# The scalar centered norm remains continuous but has distinct one-sided slopes.
eps=1e-6;left=(lp([1.],2,center)-lp([1.-eps],2,center))/eps
right=(lp([1.+eps],2,center)-lp([1.],2,center))/eps
assert isclose(left,-1,abs_tol=1e-8) and isclose(right,1,abs_tol=1e-8)
# A rank-deficient projection can ignore an input direction entirely.
projection=lambda x:lp([x[0]],2)
assert projection([2.,0.])==projection([2.,100.])
print(json.dumps(dict(mean_absolute=lp(a,1),signed_mean=mean,rms=lp(a,2),signed_maximum=max(a),absolute_maximum=max(map(abs,a)),finite_p8=lp(a,8),large_p=lp(a,10000),rho0_order=p,centered_value_at_origin=at0,centered_value_at_center=at1,one_sided_slopes=[left,right],rank_deficient_equal_values=[projection([2.,0.]),projection([2.,100.])]),sort_keys=True))
