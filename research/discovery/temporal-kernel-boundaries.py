"""Constructed temporal-kernel sums, indexing and derivative checks; no training."""
from fractions import Fraction as F
import json,math
values=[F(1),F(2),F(-1)];lam=F(1,2);trace=F(0);recursive=[]
for v in values:
 trace=v+lam*trace;recursive.append(trace)
explicit=[sum(lam**k*values[t-k] for k in range(t+1)) for t in range(len(values))]
assert recursive==explicit==[F(1),F(5,2),F(1,4)]
weight_mass=sum(lam**k for k in range(3));assert weight_mass==F(7,4)>1
# Explicit convention: a trace updated at t consumes x(t-1), not x(t).
x0,x1=F(1),F(3);delayed_at_t1=x0;current_at_t1=x1
assert delayed_at_t1!=current_at_t1
# S(t+1)=tanh(2*S(t))+.5*S(t) has derivative2.5 at zero.
eps=1e-6
f=lambda s:math.tanh(2*s)+.5*s
derivative=(f(eps)-f(-eps))/(2*eps);assert math.isclose(derivative,2.5,rel_tol=1e-8)
combined=math.tanh(1+(-.5));separate=(math.tanh(1)+math.tanh(-.5))/2
assert not math.isclose(combined,separate)
print(json.dumps(dict(recursive_trace=list(map(str,recursive)),explicit_trace=list(map(str,explicit)),three_lag_weight_mass=str(weight_mass),delayed_vs_current_input=[str(delayed_at_t1),str(current_at_t1)],coupled_trace_derivative=derivative,combined_before_nonlinearity=combined,mean_of_independent_outputs=separate,interpretation='Constructed geometric sums and a coupled scalar derivative, not a trained model, exact backward audit or measured complexity result.')))
