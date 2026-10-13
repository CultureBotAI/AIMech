"""Constructed derivative checks; no parameter fitting or author code."""
from fractions import Fraction as Q
import json
a=Q(1,2);u=[Q(1),Q(-1),Q(2)];target=[Q(0),Q(1),Q(-1)]
def loss(w,learned=True):
 h=w if learned else a;total=Q(0)
 for x,y in zip(u,target):
  h=w*h+x;total+=(h-y)**2/2+w*w/10
 return total
h=[a]
for x in u:h.append(a*h[-1]+x)
adj=[Q(0)]*4;grad=Q(0)
for t in range(3,0,-1):
 adj[t]+=h[t]-target[t-1];grad+=adj[t]*h[t-1]+a/5;adj[t-1]+=a*adj[t]
grad+=adj[0] # h0=a, hence dh0/da=1
forward=Q(0);p=Q(1)
for t in range(1,4):
 p=h[t-1]+a*p;forward+=(h[t]-target[t-1])*p+a/5
assert grad==forward
eps=Q(1,10**6);fd=(loss(a+eps)-loss(a-eps))/(2*eps)
assert abs(float(grad-fd))<1e-9
# Single terminal loss: detaching the boundary before the last transition.
full_terminal=(h[3]-target[2])*(h[2]+a*(h[1]+a*(h[0]+a)))
detached_terminal=(h[3]-target[2])*h[2]
assert full_terminal!=detached_terminal
# The same boundary state is carried numerically; only its derivative is cut.
print(json.dumps(dict(states=list(map(str,h)),shared_parameter_full_gradient=str(grad),forward_gradient=str(forward),finite_difference_error=float(abs(grad-fd)),initial_state_contribution=str(adj[0]),direct_regularizer_contribution=str(3*a/5),terminal_full_gradient=str(full_terminal),terminal_detached_boundary_gradient=str(detached_terminal),interpretation='Exact rational original example; detached boundary loses a nonzero earlier contribution even though its forward state is unchanged. No fitting or benchmark.'),indent=2))
