"""Chosen DMN+ formula distinctions; no author implementation or training."""
import json,math
candidate=math.tanh(1.2);previous=.3;attention=.4;ordinary_update=.7
replaced=attention*candidate+(1-attention)*previous
outside=attention*(ordinary_update*candidate+(1-ordinary_update)*previous)+(1-attention)*previous
assert not math.isclose(replaced,outside)
def scan(xs):
 h=0.
 for x in xs:h=.5*math.tanh(x+.5*h)+.5*h
 return h
forward=scan([1,2]);reverse=scan([2,1]);assert not math.isclose(forward,reverse)
# Fixed equal attention scores still sum to one; recurrent aggregation is ordered.
assert math.isclose(sum([.5,.5]),1)
# Original-DMN z weights old state; the DMN+ displayed u weights candidate.
z=.8;old_weighted=z*previous+(1-z)*candidate;candidate_weighted=z*candidate+(1-z)*previous
assert not math.isclose(old_weighted,candidate_weighted)
# A scalar output from three scalar inputs requires three coefficients.
memory,context,question=.2,.3,.4;weights=[1,2,3]
rectified=max(0,sum(w*x for w,x in zip(weights,[memory,context,question])))
assert math.isclose(rectified,2)
print(json.dumps(dict(replaced_update_gate=replaced,gate_outside_full_gru=outside,ordered_scan=forward,reversed_scan=reverse,old_weighted_convention=old_weighted,candidate_weighted_convention=candidate_weighted,concatenated_input_width=3,output_width=1,rectified_update=rectified,limits='Constructed finite formula checks only; no learned gates, recurrent fusion implementation, stopping controller or benchmark.'),indent=2))
