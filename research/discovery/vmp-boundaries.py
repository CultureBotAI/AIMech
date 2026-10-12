"""Curator checks for the exact conjugate VMP core; no model fit or source benchmark."""
from fractions import Fraction as F
import json, math

# Independent q(mu)q(tau), fixed observations and priors.
y=[F(1),F(2),F(4)];n=len(y)
prior_mean=F(0);prior_precision=F(1);shape=F(2);rate=F(3)
old_mean=F(1);old_variance=F(2);expected_tau=F(5,2)
# Direct expectation of Gaussian log joint: natural coefficients of mu,mu^2.
direct=(prior_precision*prior_mean+expected_tau*sum(y),-(prior_precision+n*expected_tau)/2)
prior=(prior_precision*prior_mean,-prior_precision/2)
children=[(expected_tau*z,-expected_tau/2) for z in y]
routed=tuple(prior[j]+sum(c[j] for c in children) for j in [0,1])
assert direct==routed
new_variance=-1/(2*direct[1]);new_mean=new_variance*direct[0]
assert (new_mean,new_variance)==(F(35,17),F(2,17))
# Current q(mu) moments needed for tau update. Include variance, not mean square only.
shape_next=shape+F(n,2)
rate_next=rate+sum((z-new_mean)**2+new_variance for z in y)/2
wrong_rate=rate+sum((z-new_mean)**2 for z in y)/2
assert rate_next-wrong_rate==n*new_variance/2
# For fixed q(tau), Gaussian coordinate ELBO improvement = KL(q_old||q_optimal).
kl=0.5*(math.log(float(new_variance/old_variance))+float((old_variance+(old_mean-new_mean)**2)/new_variance)-1)
assert kl>0
# Saddle despite exact fixed coordinate updates: target exp(2*x*y) on {-1,+1}^2.
# Its mean-field ELBO = 2*m_x*m_y + H(m_x)+H(m_y) - logZ; H''(0)=-1.
hessian=((F(-1),F(2)),(F(2),F(-1)))
assert (hessian[0][0]+hessian[0][1],hessian[0][0]-hessian[0][1])==(F(1),F(-3))
assert math.tanh(2*0)==0
# Along equal means the local curvature is positive; opposite means negative.
def entropy(m):return -sum(p*math.log(p) for p in [(1+m)/2,(1-m)/2])
epsilon=1e-3
change_equal=2*epsilon**2+2*(entropy(epsilon)-entropy(0))
change_opposite=-2*epsilon**2+2*(entropy(epsilon)-entropy(0))
assert change_equal>0>change_opposite
out=dict(gaussian_natural_parameters=[str(x) for x in routed],gaussian_coordinate_mean=str(new_mean),gaussian_coordinate_variance=str(new_variance),gamma_shape=str(shape_next),gamma_rate=str(rate_next),omitted_variance_rate_error=str(rate_next-wrong_rate),gaussian_coordinate_elbo_improvement=kl,saddle_hessian=[[str(x) for x in row] for row in hessian],saddle_eigenvalues=[1,-3],saddle_equal_mean_elbo_change=change_equal,saddle_opposite_mean_elbo_change=change_opposite,interpretation='Exact Fraction message/expectation identities and analytic Hessian, with floating-point KL and finite perturbation illustrations. No fitted source model or empirical reproduction.')
print(json.dumps(out,indent=2))
