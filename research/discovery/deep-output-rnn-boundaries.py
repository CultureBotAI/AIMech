"""Chosen deep-output example separates recurrent state and output derivatives."""
from math import tanh,isclose
import json

def state(x,h):return tanh(.5*h+.2*x)
def shallow_output(h):return h
def deep_output(h):return tanh(3*tanh(2*h))
x=.4;previous=.3;h=state(x,previous);eps=1e-6
state_jac=(state(x,previous+eps)-state(x,previous-eps))/(2*eps)
shallow_jac=(shallow_output(state(x,previous+eps))-shallow_output(state(x,previous-eps)))/(2*eps)
deep_jac=(deep_output(state(x,previous+eps))-deep_output(state(x,previous-eps)))/(2*eps)
assert isclose(state_jac,shallow_jac) and not isclose(deep_jac,state_jac)
# Output depth can change predictions and loss gradients without adding a state.
assert not isclose(shallow_output(h),deep_output(h))
# A deterministic readout cannot undo a collision already present in the state.
first_state=state(.4,.3);second_state=state(.9,.1)
assert isclose(first_state,second_state) and isclose(deep_output(first_state),deep_output(second_state))
print(json.dumps(dict(state=h,shallow_output=shallow_output(h),deep_output=deep_output(h),state_jacobian=state_jac,shallow_output_jacobian=shallow_jac,deep_output_jacobian=deep_jac,colliding_state_1=first_state,colliding_state_2=second_state),sort_keys=True))
