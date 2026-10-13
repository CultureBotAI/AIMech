"""Chosen ABC-CNN algebra and table arithmetic; no author code or fitted models."""
import json
from math import exp,tanh,isclose,log

def sigmoid(x):return 1/(1+exp(-x))
def softmax(v):
    z=max(v);weights=[exp(x-z) for x in v];total=sum(weights)
    return [x/total for x in weights]
# Scalar-channel, one-position kernel example of question-dependent spatial attention.
features=[0.,2.];kernels=[sigmoid(0),sigmoid(log(3))]
maps=[softmax([k*x for x in features]) for k in kernels]
assert all(isclose(sum(m),1) for m in maps) and maps[0]!=maps[1]
assert all(isclose(a,b) for a,b in zip(softmax([1.,2.]),softmax([11.,12.])))
assert softmax([5.,5.])==[.5,.5]
# The original-image branch can remain informative if the weighted branch is set to zero.
def chosen_head(original,attention):
    weighted=[x*w for x,w in zip(original,attention)]
    return sum(original)+0*sum(weighted)
assert chosen_head(features,maps[0])==chosen_head(features,maps[1])
# Question pooling uses mean hidden states, not necessarily the last state.
hidden=[1.,-1.,2.];mean=sum(hidden)/len(hidden);assert mean!=hidden[-1]
# Previous g (scaled tanh) is not a probability-normalizing softmax in Eq6.
logits=[-1.,2.];scaled_tanh=[1.7159*tanh(2*x/3) for x in logits]
assert scaled_tanh[0]<0 and not isclose(sum(scaled_tanh),1)
# Table2 ATT minus NO-ATT, in percentage points; source prose reports different deltas.
deltas=[100*(a-b) for a,b in zip([.5803,.6814,.8966],[.5414,.6483,.8855])]
assert all(isclose(a,b) for a,b in zip(deltas,[3.89,3.31,1.11]))
print(json.dumps(dict(question_kernels=kernels,spatial_attention_maps=maps,unchanged_bypass_output=chosen_head(features,maps[0]),mean_question_state=mean,last_question_state=hidden[-1],scaled_tanh_values=scaled_tanh,softmax_values=softmax(logits),table2_attention_minus_noattention_percentage_points=deltas),sort_keys=True))
