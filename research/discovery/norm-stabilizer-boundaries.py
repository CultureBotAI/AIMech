"""Constructed norm-stabilizer boundaries; no recurrent training or source execution."""
import math
import json


def norm(v):return math.sqrt(sum(x*x for x in v))

def penalty(path,beta=1.):
    t=len(path)-1;assert t>0 and beta>=0
    return beta*sum((norm(b)-norm(a))**2 for a,b in zip(path,path[1:]))/t


turning=[[1.,0.],[0.,1.],[-1.,0.]];constant=[[100.,0.]]*3
assert penalty(turning)==0 and penalty(constant)==0
coherence=sum(sum((x-y)**2 for x,y in zip(a,b)) for a,b in zip(turning,turning[1:]))/2
assert coherence==2.
path=[[0.,0.],[3.,4.],[6.,8.]];p=penalty(path);scaled=penalty([[.1*x for x in v] for v in path])
assert p==25. and math.isclose(scaled,.01*p)
zero_initial=penalty([[0.,0.],[100.,0.],[100.,0.]])
assert zero_initial==5000. and penalty(constant)==0
# A small mean squared increment can still permit cumulative norm drift.
drift=[[i*.01,0.] for i in range(1001)]
assert math.isclose(penalty(drift),.0001) and norm(drift[-1])==10.
# One norm-preserved trajectory does not imply orthogonality of the transition.
j=[[1.,0.],[0.,10.]];fixed=[1.,0.]
assert [sum(j[i][k]*fixed[k] for k in range(2)) for i in range(2)]==fixed
assert j[1][1]**2==100.
# Interior direct derivative where the selected state norm is positive.
prev=1.;cur=[3.,4.];nxt=7.;r=norm(cur);beta=2.;t=2
coef=2*beta/t*(2*r-prev-nxt)
analytic=[coef*x/r for x in cur]
def local_cost(v):return beta/t*((norm(v)-prev)**2+(nxt-norm(v))**2)
h=1e-6;numeric=[]
for i in range(2):
    a=cur.copy();a[i]+=h;b=cur.copy();b[i]-=h;numeric.append((local_cost(a)-local_cost(b))/(2*h))
assert all(math.isclose(a,b,rel_tol=1e-7,abs_tol=1e-7) for a,b in zip(analytic,numeric))
print(json.dumps(dict(turning_state_penalty=penalty(turning),turning_state_coherence=coherence,
 constant_large_norm_penalty=penalty(constant),zero_initial_boundary_penalty=zero_initial,
 original_penalty=p,scaled_penalty=scaled,drift_penalty=penalty(drift),final_drift_norm=norm(drift[-1]),
 unconstrained_orthogonal_gain=10.,interior_direct_gradient=analytic,numerical_direct_gradient=numeric),indent=2))
