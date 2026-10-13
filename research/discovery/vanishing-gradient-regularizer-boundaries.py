"""Constructed directional-gradient regularizer boundaries; no Theano or training."""
import math
import json


def penalties(gain):return ((gain-1)**2,(gain*gain-1)**2)


small=penalties(.5);large=penalties(2.);unit=penalties(1.)
assert small==(.25,.5625) and large==(1.,9.) and unit==(0.,0.)
# Unit gain in one direction does not constrain an orthogonal direction.
j=[[1.,0.],[0.,10.]];v=[1.,0.]
vj=[sum(v[k]*j[k][i] for k in range(2)) for i in range(2)]
assert vj==v and penalties(1.)==(0.,0.) and j[1][1]==10.
# For the squared-gain penalty, freeze a tanh-state derivative at w0.
w0=.5;h=math.tanh(w0);activation_derivative=1-h*h
j0=w0*activation_derivative
frozen_derivative=4*j0*(j0*j0-1)*activation_derivative
full_derivative=4*j0*(j0*j0-1)*(activation_derivative-2*w0*h*activation_derivative)
assert not math.isclose(frozen_derivative,full_derivative)
# A finite soft penalty does not impose exact norm preservation.
lam=1.;optimum=(.5+lam)/(1+lam)
assert optimum==.75 and optimum!=1. and (optimum-.5)**2>0
# Masked averaging is undefined if every error-norm term is excluded.
mask=[False,False];valid_count=sum(mask);assert valid_count==0
try:
    0./valid_count
    raise AssertionError('The unguarded all-masked quotient must be undefined')
except ZeroDivisionError:
    pass
print(json.dumps(dict(half_gain_penalties=small,double_gain_penalties=large,
 unit_gain_penalties=unit,unconstrained_orthogonal_gain=j[1][1],
 immediate_squared_gain_derivative=frozen_derivative,
 full_state_dependent_derivative=full_derivative,
 finite_soft_penalty_optimum=optimum,all_masked_count=valid_count),indent=2))
