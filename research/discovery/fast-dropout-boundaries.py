"""Finite moment and approximation boundaries; no model fitting or author code."""
from itertools import product
from math import exp,isclose
import json
w=[2.,-1.];mu=[1.,-2.];sd=[2.,1.];p=[.7,.4];rows=[]
for signs in product([-1,1],repeat=2):
 x=[m+s*t for m,s,t in zip(mu,sd,signs)]
 for z in product([0,1],repeat=2):
  prob=.25
  for pi,zi in zip(p,z):prob*=pi if zi else 1-pi
  rows.append((sum(a*b*c for a,b,c in zip(w,x,z)),prob))
mean=sum(y*q for y,q in rows);var=sum((y-mean)**2*q for y,q in rows)
expected_mean=sum(a*b*c for a,b,c in zip(w,mu,p));expected_var=sum(a*a*(r*(1-r)*m*m+r*s*s) for a,m,s,r in zip(w,mu,sd,p))
assert isclose(mean,expected_mean) and isclose(var,expected_var)
squared=sum((y-3)**2*q for y,q in rows);assert isclose(squared,(mean-3)**2+var)
sig=lambda x:1/(1+exp(-x));esig=sum(sig(y)*q for y,q in rows);assert not isclose(esig,sig(mean),abs_tol=.01)
# A single retained unit has matched Gaussian moments but different fourth moment.
mask4=.5;gauss4=.5**4+6*.5**2*.25+3*.25**2;assert mask4!=gauss4
# Fully correlated inputs, mask retention1, w=(1,1): diagonal-only variance misses covariance.
correlated_var=4.;diagonal_var=2.;assert correlated_var!=diagonal_var
# Local variance path for J(V)=V^2 with incoming moments held fixed.
coef=.7*(1-.7)*1**2+.7*2**2;a=2.;v=lambda a:coef*a*a;j=lambda a:v(a)**2
h=1e-5;fd=(j(a+h)-j(a-h))/(2*h);analytic=2*a*coef*(2*v(a));assert isclose(fd,analytic,rel_tol=1e-8)
print(json.dumps(dict(mean=mean,variance=var,expected_squared_loss=squared,expected_sigmoid=esig,sigmoid_of_mean=sig(mean),bernoulli_fourth=mask4,matched_gaussian_fourth=gauss4,correlated_variance=correlated_var,diagonal_only_variance=diagonal_var,local_variance_gradient=analytic),sort_keys=True))
