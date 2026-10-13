"""Constructed transition algebra for IRNN; no training or framework execution."""
import json, math

def transition(h, w, u):
    return [max(0., sum(a*b for a,b in zip(row,h))+v) for row,v in zip(w,u)]

def near(a,b):
    assert len(a)==len(b) and all(math.isclose(x,y,rel_tol=1e-10,abs_tol=1e-10) for x,y in zip(a,b)), (a,b)

i=[[1.,0.],[0.,1.]]
h=[2.,3.]
near(transition(h,i,[0.,0.]),h)
inactive=transition(h,i,[-3.,0.]);near(inactive,[0.,3.])
eps=1e-6
finite_difference=(transition([2.+eps,3.],i,[-3.,0.])[0]-transition([2.-eps,3.],i,[-3.,0.])[0])/(2*eps)
assert finite_difference==0.
c=.5;v=h
for _ in range(4):v=transition(v,[[c,0.],[0.,c]],[0.,0.])
near(v,[.125,.1875])
acc=[0.,0.]
for _ in range(100):acc=transition(acc,i,[1.,2.])
near(acc,[100.,200.])
# A constructed dense update from I creates cross-coordinate dependence.
w=[[1.,.1],[0.,1.]]
a=transition([2.,3.],w,[0.,0.]);z=transition([2.,4.],w,[0.,0.]);near(a,[2.3,3.]);near(z,[2.4,4.])
print(json.dumps(dict(identity_copy=h,input_deactivated_state=inactive,inactive_input_derivative=finite_difference,scaled_four_step_state=v,scaled_active_derivative=c**4,positive_input_after_100_steps=acc,dense_update_cross_dependence=[a,z],scope='Constructed elementary transition/derivative checks; no fitted network or benchmark.'),indent=2))
