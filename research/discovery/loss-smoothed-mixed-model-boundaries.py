"""Finite algebra/quadrature for a fixed supplied variational state; no fitting.
Independent curator code. Does not import or execute the author Julia package.
"""
import math,json
phi=lambda z:math.exp(-z*z/2)/math.sqrt(2*math.pi)
Phi=lambda z:(1+math.erf(z/math.sqrt(2)))/2
def simpson(f,a,b,n=4000):
 h=(b-a)/n
 return h/3*(f(a)+f(b)+sum((4 if j%2 else 2)*f(a+j*h) for j in range(1,n)))
def quantile(y,xi,nu,tau):
 z=(y-xi)/nu
 return nu*(phi(z)+z*(Phi(z)-1+tau)),1-tau-Phi(z),phi(z)/nu

y0,xi0,nu0,tau=.6,-.2,.8,.7
z0=(y0-xi0)/nu0
loss=lambda z:(y0-xi0-nu0*z)*(tau-(1 if y0<xi0+nu0*z else 0))
def integ(f):return simpson(f,-10,z0)+simpson(f,z0,10)
analytic=quantile(y0,xi0,nu0,tau)
quad=(integ(lambda z:phi(z)*loss(z)),integ(lambda z:phi(z)*z*loss(z))/nu0,integ(lambda z:phi(z)*(z*z-1)*loss(z))/(nu0*nu0))
err=max(abs(a-b) for a,b in zip(analytic,quad));assert err<1e-10
# Three observations, one fixed and one random coefficient; supplied q(theta).
C=[[1.,-1.],[1.,.5],[1.,2.]];ys=[-.2,.4,1.1];mu=[.3,-.1];S=[[.8,.12],[.12,.6]]
xis=[sum(a*b for a,b in zip(row,mu)) for row in C]
variances=[sum(row[i]*S[i][j]*row[j] for i in range(2) for j in range(2)) for row in C]
psis=[quantile(y,x,math.sqrt(v),tau) for y,x,v in zip(ys,xis,variances)]
Ah,Bh,Rh=2.,1.,1.3
shape=Ah+.5;rate=Bh+.5*Rh*(mu[1]**2+S[1][1]);precision_mean=shape/rate
R=[.25,precision_mean*Rh]
P=[[sum(row[i]*row[j]*psi[2] for row,psi in zip(C,psis))+(R[i] if i==j else 0) for j in range(2)] for i in range(2)]
h=[sum(row[j]*(psi[2]*x-psi[1]) for row,psi,x in zip(C,psis,xis)) for j in range(2)]
g=[-sum(row[j]*psi[1] for row,psi in zip(C,psis))-R[j]*mu[j] for j in range(2)]
det=P[0][0]*P[1][1]-P[0][1]*P[1][0];assert P[0][0]>0 and det>0
Sn=[[P[1][1]/det,-P[0][1]/det],[-P[1][0]/det,P[0][0]/det]]
mn=[sum(Sn[i][j]*h[j] for j in range(2)) for i in range(2)]
other=[mu[i]+sum(Sn[i][j]*g[j] for j in range(2)) for i in range(2)]
assert max(abs(a-b) for a,b in zip(mn,other))<1e-14
assert max(abs(sum(P[i][j]*mn[j] for j in range(2))-h[i]) for i in range(2))<1e-14
# Source covariance sign boundary: quadratic loss has positive unit curvature.
correct=.25+1.;printed=.25-1.;assert correct>0 and printed<0
# Exp-loss is Gaussian-integrable/convex but smoothing does not converge uniformly over R.
nu_exp=.1
uniform_counterexample=[dict(xi=x,difference=math.exp(x)*math.expm1(nu_exp**2/2)) for x in [0,5,10]]
# Static transcription of SVC psi0 versus its claimed doubled first derivative.
def hinge_mean(xi,nu):
 a=1-xi;z=a/nu
 return nu*phi(z)+a*Phi(z)
xih,nuh=.2,.7;eps=1e-5
fd=(hinge_mean(xih+eps,nuh)-hinge_mean(xih-eps,nuh))/(2*eps)
true_derivative=-Phi((1-xih)/nuh);package_derivative=2*true_derivative
assert abs(fd-true_derivative)<1e-9 and abs(fd-package_derivative)>.5
print(json.dumps(dict(quantile=dict(analytic=analytic,hermite_quadrature=quad,max_error=err),mixed_model_state=dict(predictor_means=xis,predictor_variances=variances,variance_factor_shape=shape,variance_factor_rate=rate,expected_inverse_variance=precision_mean,proposal_precision=P,proposal_covariance=Sn,proposal_mean=mn,natural_and_newton_form_max_difference=max(abs(a-b) for a,b in zip(mn,other))),source_precision_sign=dict(correct=correct,printed=printed),uniform_convergence_counterexample=dict(nu=nu_exp,values=uniform_counterexample,argument='Difference exp(xi)*(exp(nu²/2)-1) has infinite supremum over real xi for each nu>0.'),package_hinge_derivative=dict(finite_difference_of_psi0=fd,correct= true_derivative,statically_transcribed_psi1=package_derivative),scope='One supplied Gaussian/IG state and finite quadratures; not an iterative fit, author-code execution, convergence test or empirical benchmark.'),indent=2))
