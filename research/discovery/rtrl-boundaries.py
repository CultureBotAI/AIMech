"""Constructed fixed-parameter differentiation checks; no fitting or author code."""
import json
from math import tanh, exp, isclose
from fractions import Fraction as F
W=[[.4,-.2,.3,.1],[-.1,.5,-.4,.2]]
X=[[.3,1.],[-.2,1.],[.6,1.]]
D=[[.1,None],[None,.2],[.3,-.1]]
def forward(weights,with_sens=False):
    y=[.2,-.1];p=[[[0.]*4 for _ in range(2)] for _ in range(2)]
    grad=[[0.]*4 for _ in range(2)];loss=0.;cache=[]
    for x,d in zip(X,D):
        z=y+x;yn=[tanh(sum(a*b for a,b in zip(row,z))) for row in weights]
        pn=[[[ (1-yn[k]**2)*(sum(weights[k][l]*p[l][i][j] for l in range(2))+(z[j] if i==k else 0.)) for j in range(4)] for i in range(2)] for k in range(2)]
        err=[0. if d[k] is None else yn[k]-d[k] for k in range(2)]
        loss+=.5*sum(v*v for v in err)
        for i in range(2):
            for j in range(4):grad[i][j]+=sum(err[k]*pn[k][i][j] for k in range(2))
        cache.append((z,yn,err));y,p=yn,pn
    return loss,grad,cache
loss,g,cache=forward(W);adj=[0.,0.];back=[[0.]*4 for _ in range(2)]
for z,y,e in reversed(cache):
    a=[(e[k]+adj[k])*(1-y[k]**2) for k in range(2)]
    for i in range(2):
        for j in range(4):back[i][j]+=a[i]*z[j]
    adj=[sum(W[k][j]*a[k] for k in range(2)) for j in range(2)]
maxdiff=0.
for i in range(2):
    for j in range(4):
        plus=[r[:] for r in W];minus=[r[:] for r in W];plus[i][j]+=1e-6;minus[i][j]-=1e-6
        fd=(forward(plus)[0]-forward(minus)[0])/(2e-6)
        maxdiff=max(maxdiff,abs(g[i][j]-fd));assert isclose(g[i][j],back[i][j],abs_tol=1e-14)
assert maxdiff<1e-8
w0,w1=F(1,2),F(3,5);y0=F(1);y1=w0*y0;p1=y0;p2=w1*p1+y1
assert p2==F(11,10) and 2*w1==F(6,5) and y1==F(1,2)
sig=lambda x:1/(1+exp(-x));w=.7;old=.2;first=sig(w*old);pfirst=first*(1-first)*old
forced=sig(w*.9);pforced=forced*(1-forced)*.9
free=sig(w*first);pfree=free*(1-free)*(first+w*pfirst)
assert pfirst>0 and abs(pforced-pfree)>.01
n,m=2,2;r=n*(n+m);assert n*r==16 and n*n*r==32
print(json.dumps(dict(fixed_trajectory_loss=loss,forward_gradient=g,reverse_gradient=back,max_finite_difference_error=maxdiff,changing_weights=dict(weights=[str(w0),str(w1)],propagated_sensitivity=str(p2),fixed_current_weight_trajectory_derivative=str(2*w1),current_weight_partial_holding_past_fixed=str(y1)),teacher_forcing=dict(first_output_derivative_before_reset=pfirst,next_forced_derivative=pforced,next_free_derivative=pfree),dense_sensitivity_values=n*r,naive_recurrent_multiplications_per_step=n*n*r),indent=2))
