"""Constructed DMN gate and recurrence boundaries; no author model or training."""
import json,math
sig=lambda x:1/(1+math.exp(-x))
gates=[sig(0),sig(0),sig(0)];assert sum(gates)==1.5
# GRU z=r=0.5, W=U=1, biases0, scalar input c and previous h.
def gru(c,h):return 0.5*h+0.5*math.tanh(c+0.5*h)
def scan(facts):
 h=0.0
 for c in facts:h=0.5*gru(c,h)+0.5*h
 return h
forward=scan([1,2]);reverse=scan([2,1]);assert not math.isclose(forward,reverse)
# Fixed equal gate logits give the QA-style normalized sum independently of order.
pooling=sum([1,2])/2;assert pooling==sum([2,1])/2
# U=[[1,1],[0,1]], h=[1,2], r=[.25,.75].
after=[.25*(1+2),.75*2];before=[.25*1+.75*2,.75*2];assert after!=before
print(json.dumps(dict(independent_sigmoid_gate_sum=sum(gates),recurrent_episode_forward=forward,recurrent_episode_reverse=reverse,fixed_logit_softmax_pool=pooling,reset_after_projection=after,reset_before_projection=before,limits='Chosen finite formulas only; no gate-label learning, stopping controller, trained DMN or empirical evaluation.'),indent=2))
