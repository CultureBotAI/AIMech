"""Chosen transition-depth and shortcut boundaries; no author implementation."""
from math import tanh,isclose
import json

def transition(x,h):
 intermediate=tanh(.6*h+.2*x)
 return tanh(1.3*intermediate)
def shallow(x,h):return tanh(.6*h+.2*x)
x=.4;h=.3;eps=1e-6
jd=(transition(x,h+eps)-transition(x,h-eps))/(2*eps)
js=(shallow(x,h+eps)-shallow(x,h-eps))/(2*eps)
assert not isclose(jd,js)
# A short path need not prevent cancellation in the complete derivative.
def shortcut(h):return tanh(h-2*tanh(.5*h))
jc=(shortcut(eps)-shortcut(-eps))/(2*eps);assert abs(jc)<1e-9
# Source Table2: DT(S) beats the selected shallow baseline but not all other models.
dt=[3.206,8.278,6.988];rnn=[3.225,8.338,6.990];stack=[3.258,8.367,6.954]
assert all(a<b for a,b in zip(dt,rnn)) and dt[2]>stack[2]
# Table3: combined DOT has lower word perplexity than DT(S).
assert 107.5<112<117.7
print(json.dumps(dict(deep_transition_jacobian=jd,shallow_transition_jacobian=js,shortcut_full_derivative=jc,music_dt_minus_shallow=[a-b for a,b in zip(dt,rnn)],muse_dt_minus_stacked=dt[2]-stack[2],word_dt_minus_dot=112-107.5),sort_keys=True))
