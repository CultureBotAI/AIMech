"""Original finite curator checks; no author implementation or benchmark audit."""
from itertools import product
from math import exp, log, pi, sqrt
import json

def sigmoid(x): return 1 / (1 + exp(-x))
def close(a, b): assert abs(a-b) < 2e-8, (a, b)
def binary(a, c, w):
    u = {(v,h): exp(a*v+c*h+w*v*h) for v,h in product((0,1), repeat=2)}
    z = sum(u.values())
    return {k:x/z for k,x in u.items()}

# Stochastic TRBM history: local normalized RBMs do not remove smoothing.
a,b,w,B,C,A = .2,-.3,.8,.9,.4,-.2
p0 = binary(a,b,w)
joint = {}
for v1,h1,v2,h2 in product((0,1), repeat=4):
    joint[v1,h1,v2,h2] = p0[v1,h1]*binary(a+A*v1,b+B*h1+C*v1,w)[v2,h2]
close(sum(joint.values()),1)
filtered = sigmoid(b+w)
den = sum(q for (v1,h1,v2,h2),q in joint.items() if v1==1 and v2==1)
smoothed = sum(q for (v1,h1,v2,h2),q in joint.items() if v1==h1==v2==1)/den
assert abs(filtered-smoothed)>1e-3
exact_next = sum((filtered if h else 1-filtered)*sum(q for (v,j),q in binary(a+A,b+B*h+C,w).items() if v==1) for h in (0,1))
plug_next = sum(q for (v,j),q in binary(a+A,b+B*filtered+C,w).items() if v==1)
assert abs(exact_next-plug_next)>1e-4

# RTRBM: state is deterministic by definition, unlike sampled TRBM history.
def recurrent(theta, sequence, derivatives=False):
    av,bh,ww,uu = theta
    r = 0.; saved=[]; objective=0.
    for v in sequence:
        c=bh+uu*r; q=binary(av,c,ww); p=sum(x for (vv,h),x in q.items() if vv==v)
        rt=sigmoid(c+ww*v); objective+=log(p)
        gh=rt-sum(h*x for (vv,h),x in q.items())
        gw=v*rt-sum(vv*h*x for (vv,h),x in q.items())
        ga=v-sum(vv*x for (vv,h),x in q.items())
        saved.append((v,r,rt,gh,gw,ga));r=rt
    if not derivatives:return objective
    lam=0.; grad=[0.]*4; direct_u=0.; indirect_u=0.
    for v,rprev,rt,gh,gw,ga in reversed(saved):
        back=lam*rt*(1-rt);total=gh+back
        grad[0]+=ga;grad[1]+=total;grad[2]+=gw+back*v;grad[3]+=total*rprev
        direct_u+=gh*rprev;indirect_u+=back*rprev;lam=uu*total
    return objective,grad,direct_u,indirect_u
theta=[.2,-.3,.8,.9];seq=[1,0,1]
objective,gradient,direct,indirect=recurrent(theta,seq,True)
epsilon=1e-5
for i,g in enumerate(gradient):
    plus=theta.copy();minus=theta.copy();plus[i]+=epsilon;minus[i]-=epsilon
    close(g,(recurrent(plus,seq)-recurrent(minus,seq))/(2*epsilon))
close(sum(exp(recurrent(theta,s)) for s in product((0,1),repeat=3)),1)
two=recurrent(theta,[1,0],True)
close(two[3],0);assert abs(two[2])>.01
# In a length-two sequence, the terminal recurrent state has no future loss.
# A recurrence-only recurrent-weight derivative is zero, but the exact
# conditional output RBM depends directly on that weight through its bias.
close(two[1][3],two[2])

# Gaussian-visible autoregressive CRBM; history is observed and fixed.
x,v=.7,-.2
def gaussian(theta):
    c,bh,ww,aa,dd=theta;dv=c+aa*x;eh=bh+dd*x
    prior=sigmoid(eh+dv*ww+ww*ww/2)
    posterior=sigmoid(eh+ww*v)
    z=sqrt(2*pi)*(1+exp(eh+dv*ww+ww*ww/2))
    logp=-.5*(v-dv)**2+log(1+exp(eh+ww*v))-log(z)
    mean=dv+ww*prior;variance=1+ww*ww*prior*(1-prior)
    return logp,prior,posterior,mean,variance,dv
gtheta=[.1,-.4,.8,.5,-.3];ll,prior,post,mean,var,dv=gaussian(gtheta)
ggradient=[v-mean,post-prior,v*post-(dv+gtheta[2])*prior,x*(v-mean),x*(post-prior)]
for i,g in enumerate(ggradient):
    plus=gtheta.copy();minus=gtheta.copy();plus[i]+=epsilon;minus[i]-=epsilon
    close(g,(gaussian(plus)[0]-gaussian(minus)[0])/(2*epsilon))
normal=lambda value,mu:exp(-.5*(value-mu)**2)/sqrt(2*pi)
close(exp(ll),(1-prior)*normal(v,dv)+prior*normal(v,dv+gtheta[2]))
close(post,prior*normal(v,dv+gtheta[2])/exp(ll))
for future in (-2.,2.):
    # With v fully observed, its future factor cancels from P(h|all v).
    future_factor=normal(future,gtheta[3]*v)
    close(prior*normal(v,dv+gtheta[2])*future_factor/(exp(ll)*future_factor),post)
# If a visible frame is missing, even the zero-coupling linear-Gaussian
# subcase requires future information for smoothing.
missing_filtered=0.;missing_smoothed=(0.+.5*2)/(1+.5**2)
assert missing_smoothed != missing_filtered
assert var>1 # Replacing Gaussian draws by means removes conditional variance.
print(json.dumps(dict(
    trbm=dict(normalized_joint=sum(joint.values()),filtered_h1=filtered,smoothed_h1=smoothed,exact_next=exact_next,plug_mean_next=plug_next),
    rtrbm=dict(log_probability=objective,gradient=gradient,direct_recurrent_term=direct,indirect_recurrent_term=indirect,length_two_exact_recurrent_gradient=two[1][3],length_two_recurrence_only_gradient=two[3],finite_differences_pass=True),
    crbm=dict(log_density=ll,hidden_prior=prior,hidden_posterior=post,visible_mean=mean,visible_variance=var,gradient=ggradient,missing_frame_filtered_mean=missing_filtered,missing_frame_smoothed_mean=missing_smoothed,finite_differences_pass=True)),indent=2))
