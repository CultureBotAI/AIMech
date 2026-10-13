"""Constructed forward stack operators; no author code or training execution."""
import json, math

def step(old, value, push, pop, stay=0.):
    assert all(a>=0 for a in [push,pop,stay]) and math.isclose(push+pop+stay,1.)
    return [push*(value if i==0 else old[i-1])+pop*(old[i+1] if i+1<len(old) else -1.)+stay*old[i] for i in range(len(old))]
def close(a,b):assert len(a)==len(b) and all(math.isclose(x,y,abs_tol=1e-12) for x,y in zip(a,b)),(a,b)
old=[.2,.7,-1.]
pushed=step(old,.9,1.,0.);close(pushed,[.9,.2,.7])
close(step(pushed,0.,0.,1.),old);close(step(old,.9,0.,0.,1.),old)
mix=step(old,.9,.5,.5);close(mix,[.8,-.4,-.15])
# Overflow loses the old bottom entry; a later pop does not undo that loss.
full=[.2,.7,.4];overflow=step(full,.9,1.,0.);lost=step(overflow,0.,0.,1.);close(lost,[.2,.7,-1.]);assert lost!=full
sigmoid=lambda x:1/(1+math.exp(-x))
mixed_hidden=sigmoid(4*mix[0]);expected_hidden=.5*sigmoid(4*.9)+.5*sigmoid(4*.7)
assert not math.isclose(mixed_hidden,expected_hidden,rel_tol=1e-6)
# Equal top logits remain tied under temperature sharpening; no unique one-hot limit.
equal_logits=[.5,.5]
weights=[math.exp(0.0),math.exp(-1000.0)]
underflow_weights=[x/sum(weights) for x in weights]
assert underflow_weights==[1.0,0.0]
print(json.dumps(dict(finite_logits=[0.0,-1000.0],binary64_softmax=underflow_weights,push=pushed,mixed_update=mix,overflow_then_pop=lost,nonlinear_controller_of_mean=mixed_hidden,mean_of_discrete_controllers=expected_hidden,tied_softmax_under_any_positive_scale=equal_logits,scope='Elementary finite-capacity operator and nonlinear-mixture calculations; no training, full gradient audit or author source execution.'),indent=2))
