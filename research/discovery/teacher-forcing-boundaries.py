"""Constructed teacher-input and hidden-recurrence derivative distinctions."""
from fractions import Fraction as Q
from math import log
import json
# Same recurrent hidden state, but externally supplied previous output tokens.
a=Q(1,2);start=Q(1);tokens=[Q(2),Q(-1)]
h0=Q(0);h1=a*h0+start;h2=a*h1+tokens[0];h3=a*h2+tokens[1]
d1=h0;d2=h1+a*d1;d3=h2+a*d2
assert (h1,h2,h3)==(Q(1),Q(5,2),Q(1,4)) and d3==3
assert h2!=d3 # falsely detaching h2 would give only h2=2.5
# Feedback replacement changes the rollout even with the same coefficients.
free2=a*h1+h1;free3=a*free2+free2
assert free3!=h3
# A tiny normalized binary autoregression; observed-prefix likelihood is exact.
p_first={0:Q(3,5),1:Q(2,5)}
p_second={0:{0:Q(4,5),1:Q(1,5)},1:{0:Q(1,4),1:Q(3,4)}}
joint={(x,y):p_first[x]*p_second[x][y] for x in [0,1] for y in [0,1]}
assert sum(joint.values())==1 and joint[(1,0)]==Q(1,10)
nll=-log(float(p_first[1]))-log(float(p_second[1][0]))
assert abs(nll+log(float(joint[(1,0)])))<1e-12
print(json.dumps(dict(teacher_states=list(map(str,[h1,h2,h3])),teacher_final_derivative=str(d3),incorrect_hidden_detachment_derivative=str(h2),free_running_final_state=str(free3),observed_sequence_probability=str(joint[(1,0)]),joint_total=str(sum(joint.values())),observed_prefix_negative_log_likelihood=nll,interpretation='Externally supplied token paths are fixed; recurrent hidden paths still contribute. Exact observed-prefix likelihood does not imply matching autonomous trajectories. No fitting, sampling experiment or benchmark.'),indent=2))
