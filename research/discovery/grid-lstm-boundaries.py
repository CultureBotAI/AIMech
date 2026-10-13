"""Chosen Grid LSTM formula checks, not author code or model training."""
import json
from math import tanh,isclose
# Hold incoming hidden features and gate/candidate outputs fixed to isolate direct memory paths.
m=[2.,-1.];f=.5;addition=.1
grid=[f*x+addition for x in m];summed=f*sum(m)+addition
assert grid==[1.1,-.4] and not any(isclose(summed,v) for v in grid)
# Follow the source's printed output equation for this constructed one-unit cell.
def cell(hidden,memory):
    new_memory=.5*memory+.5*tanh(sum(hidden))
    return tanh(.5*new_memory),new_memory
h=[.2,-.3];mem=[.4,-.7]
sim=[cell(h,v) for v in mem]
priority_first=cell([h[0],sim[1][0]],mem[0])
assert not isclose(priority_first[0],sim[0][0])
# Output gate location matters; the two displayed conventions are not algebraically equal.
o=.25;value=1.6
printed=tanh(o*value);outside=o*tanh(value)
assert not isclose(printed,outside)
# Fixed input dimension; exclude input/output projections and biases as in the displayed W matrices.
def one_axis_weights(depth,d=10,tied=True):return 4*d*d*(1 if tied else depth)
assert one_axis_weights(10)==one_axis_weights(20)
assert one_axis_weights(20,tied=False)==2*one_axis_weights(10,tied=False)
# Hypothetical IID test sampling, not a statistical estimate of a trained paper model.
miss_probability=(1-.01)**100
assert miss_probability>.36
print(json.dumps(dict(separate_memory_outputs=grid,summed_memory_output=summed,simultaneous_hidden=[x[0] for x in sim],priority_first_hidden=priority_first[0],printed_output_gate=printed,alternative_output_gate=outside,tied_weights10=one_axis_weights(10),tied_weights20=one_axis_weights(20),untied_weights20=one_axis_weights(20,tied=False),hypothetical_one_percent_error_missed_by_100_tests=miss_probability),sort_keys=True))
