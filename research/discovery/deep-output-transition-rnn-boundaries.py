"""Chosen nonlinear maps and source-table arithmetic; no fitted model or author code."""
from math import tanh,isclose
import json
# One recurrent state; intermediate values have no independent past-state input.
def step(x,h):
 transition=tanh(.7*h+.4*x)
 state=tanh(1.2*transition)
 output=tanh(.9*tanh(.8*state))
 return transition,state,output
intermediate,state,output=step(.3,.5)
assert not isclose(state,output)
# A learned plus operator is neither literal addition nor necessarily commutative.
def plus(x,h):return tanh(2*x+h)
assert not isclose(plus(.2,.6),plus(.6,.2))
# A shortcut term does not impose a positive lower bound on the total derivative.
def shortcut(h):return tanh(h-2*tanh(.5*h))
eps=1e-6;derivative=(shortcut(eps)-shortcut(-eps))/(2*eps)
assert abs(derivative)<1e-9
# Table2 negative log-probability: base DOT does not dominate shallow RNN.
rnn=[3.225,8.338,6.990];dot=[3.215,8.437,6.973]
assert dot[0]<rnn[0] and dot[1]>rnn[1] and dot[2]<rnn[2]
# Table3 character result is below own baselines but above cited LSTM.
assert 1.386<1.414 and 1.386>1.24
print(json.dumps(dict(intermediate=intermediate,state=state,output=output,plus_forward=plus(.2,.6),plus_swapped=plus(.6,.2),shortcut_derivative_at_zero=derivative,music_dot_minus_shallow=[a-b for a,b in zip(dot,rnn)],character_dot_minus_cited_lstm=1.386-1.24,word_perplexity_rnn_minus_dot=117.7-107.5),sort_keys=True))
