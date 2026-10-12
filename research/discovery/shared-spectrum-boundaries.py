"""Finite curator calculations for shared Gaussian inverse-lengthscale features.
No model fitting, training, source-code execution or empirical benchmark.
"""
import json,math

def simpson(f,a,b,n=8000):
    assert n%2==0
    h=(b-a)/n
    return h/3*(f(a)+f(b)+sum((4 if j%2 else 2)*f(a+j*h) for j in range(1,n)))

mu,var=.4,.7
ts=[.6,1.3]
def ec(t):return math.exp(-.5*var*t*t)*math.cos(mu*t)
def es(t):return math.exp(-.5*var*t*t)*math.sin(mu*t)
def features(x):return [math.cos(t*x) for t in ts]+[math.sin(t*x) for t in ts]
mean=[ec(t) for t in ts]+[es(t) for t in ts]
second=[[0.0]*4 for _ in range(4)]
for i,a in enumerate(ts):
 for j,c in enumerate(ts):
  second[i][j]=.5*(ec(a-c)+ec(a+c))
  second[i+2][j+2]=.5*(ec(a-c)-ec(a+c))
  second[i][j+2]=.5*(es(c+a)+es(c-a))
  second[j+2][i]=second[i][j+2]
normal=lambda x:math.exp(-.5*(x-mu)**2/var)/math.sqrt(2*math.pi*var)
lo,hi=mu-10*math.sqrt(var),mu+10*math.sqrt(var)
mean_num=[simpson(lambda x,k=k:normal(x)*features(x)[k],lo,hi) for k in range(4)]
second_num=[[simpson(lambda x,i=i,j=j:normal(x)*features(x)[i]*features(x)[j],lo,hi) for j in range(4)] for i in range(4)]
err=max([abs(a-c) for a,c in zip(mean,mean_num)]+[abs(second[i][j]-second_num[i][j]) for i in range(4) for j in range(4)])
assert err<1e-11
cross_cov=second[0][1]-mean[0]*mean[1]
assert abs(cross_cov)>.01
assert abs(sum(second[i][i] for i in range(4))-2)<1e-14
# H after inverse-scale substitution: integrand written without x^-2 at zero.
def H(p,C,A):
 assert p>=0 and C>0 and A>0
 return simpson(lambda x:x**(p+2)*math.exp(-C*x*x)/(1+A*A*x*x),0,12/math.sqrt(C))
def direct_scale(k,C,A,power):
 def f(t):
  if t in (0,1):return 0.0
  s=t/(1-t)
  return math.exp(-C/(s*s)+(power-k)*math.log(s)-math.log(A*A+s*s)-2*math.log(1-t))
 return simpson(f,0,1)
scale_results=[]
for label,k,C,A in [('coefficient-scale',4,1.2,.8),('noise-scale',4,2.1,1.1)]:
 norm=H(k-2,C,A)
 direct=direct_scale(k,C,A,0)
 inv2=H(k,C,A)/norm
 moment2=H(k-4,C,A)/norm
 e0=abs(norm-direct)
 e1=abs(inv2-direct_scale(k,C,A,-2)/direct)
 e2=abs(moment2-direct_scale(k,C,A,2)/direct)
 assert max(e0,e1,e2)<1e-9
 scale_results.append(dict(label=label,k=k,C=C,A=A,normalizer=norm,expected_inverse_square=inv2,expected_square=moment2,max_dual_integration_error=max(e0,e1,e2)))
# General tail: q_gamma(gamma) proportional gamma^-n/(A²+gamma²)*exp(-C/gamma²).
# Thus E[gamma^r] tail exponent = r-n-2; converges iff r<n+1.
assert 2>=1+1 and 2<2+1
# Scalar, one-pair source Algorithm1 curvature/mean contributions, frozen old q(lambda).
t=.9;y=.8;u=1.4;a,b=.3,-.2
A,D,B=a*a+.4,b*b+.5,a*b+.07
m0,v0=.1,1.2
c1,s1=ec(t),es(t);c2,s2=ec(2*t),es(2*t)
F1=y*(a*c1+b*s1)*t*t
F2=-.25*((A-D)*c2+2*B*s2)*(2*t)**2
F3=-2*y*(b*c1-a*s1)*t
F4=.5*(2*B*c2+(D-A)*s2)*(2*t)
precision=1/v0+u*(F1+F2)
g_mu=(m0-mu)/v0-.5*u*(F3+F4)
def expected_joint(m,v):
 c=lambda z:math.exp(-.5*v*z*z)*math.cos(m*z)
 sn=lambda z:math.exp(-.5*v*z*z)*math.sin(m*z)
 trace=.5*(A+D)+.5*(A-D)*c(2*t)+B*sn(2*t)
 return -.5*((m-m0)**2+v)/v0+u*(y*(a*c(t)+b*sn(t))-.5*trace)
eps=1e-5
g_mu_num=(expected_joint(mu+eps,var)-expected_joint(mu-eps,var))/(2*eps)
g_v_num=(expected_joint(mu,var+eps)-expected_joint(mu,var-eps))/(2*eps)
assert abs(g_mu-g_mu_num)<1e-9 and abs(precision+2*g_v_num)<1e-9
assert precision>0
proposed_var=1/precision;proposed_mu=mu+proposed_var*g_mu
source_derivative_check=dict(precision=precision,mean_gradient=g_mu,proposed_mean=proposed_mu,proposed_variance=proposed_var,max_finite_difference_error=max(abs(g_mu-g_mu_num),abs(precision+2*g_v_num)),scope='Scalar one-pair source F1–F4 checked against independent derivatives at old mu/variance. This is not a multidimensional proof or fitted algorithm run.')
# One coefficient coordinate at fixed supplied scale/lambda moments; not a fit loop.
F=[[ec(z),es(z)] for z in ts]
K=[[sum(.5*(1+ec(2*z)) for z in ts),sum(.5*es(2*z) for z in ts)],
   [sum(.5*es(2*z) for z in ts),sum(.5*(1-ec(2*z)) for z in ts)]]
u0,v0c=1.4,.7;responses=[.2,-.4]
P=[[u0*K[i][j]+(v0c if i==j else 0) for j in range(2)] for i in range(2)]
det=P[0][0]*P[1][1]-P[0][1]*P[1][0];assert det>0 and P[0][0]>0
Sa=[[P[1][1]/det,-P[0][1]/det],[-P[1][0]/det,P[0][0]/det]]
h=[u0*sum(F[i][j]*responses[i] for i in range(2)) for j in range(2)]
ma=[sum(Sa[i][j]*h[j] for j in range(2)) for i in range(2)]
residual=max(abs(h[i]-sum(P[i][j]*ma[j] for j in range(2))) for i in range(2));assert residual<1e-14
coefficient_check=dict(mean=ma,covariance=Sa,precision_determinant=det,expected_log_joint_mean_gradient_residual=residual,scope='One analytic Gaussian coordinate for supplied fixed neighboring moments; no iterative posterior fit.')
# Predictive law of total variance: independently integrate conditional moments.
weights=[.3,-.2,.1,.4]
factor=[[.4,0,0,0],[.1,.5,0,0],[.05,-.03,.3,0],[0,.1,.1,.4]]
cov=[[sum(factor[i][k]*factor[j][k] for k in range(4)) for j in range(4)] for i in range(4)]
noise2=scale_results[1]['expected_square']
pred_mean=sum(weights[i]*mean[i] for i in range(4))
pred_second=noise2+sum((cov[i][j]+weights[i]*weights[j])*second[i][j] for i in range(4) for j in range(4))
pred_var=pred_second-pred_mean**2
def conditional_second(x):
 z=features(x)
 return noise2+sum((cov[i][j]+weights[i]*weights[j])*z[i]*z[j] for i in range(4) for j in range(4))
pred_second_num=simpson(lambda x:normal(x)*conditional_second(x),lo,hi)
assert pred_var>0 and abs(pred_second-pred_second_num)<1e-10
predictive_check=dict(mean=pred_mean,variance=pred_var,second_moment_integration_error=abs(pred_second-pred_second_num),scope='Two-pair fixed coefficient moments with a positive-definite supplied covariance; integrates the conditional second moment over shared lambda.')
print(json.dumps(dict(feature_mean=mean,feature_second_moment=second,shared_cosine_cross_covariance=cross_cov,max_feature_quadrature_error=err,paired_feature_squared_norm=2,scale_checks=scale_results,source_derivative_check=source_derivative_check,coefficient_check=coefficient_check,predictive_check=predictive_check,noise_second_moment_boundary='For C>0 and A>0: finite iff n>1; n=1 has logarithmically divergent second moment.',scope='Supplied fixed variational parameters, analytic Gaussian moments and two numerical integration coordinate systems; no fitting or author implementation.'),indent=2))
