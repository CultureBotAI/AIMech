"""Chosen depth-gate algebra; no author implementation or fitted model."""
import json
from math import exp,tanh,isclose

def sigmoid(x):return 1/(1+exp(-x))
# Fixed ordinary coupled gates and separately selected depth gate.
f=.7;i=1-f;d=.8;lower=2.;past=2.;candidate=.5
ordinary=f*past+i*candidate
cell=d*lower+ordinary
assert isclose(f+i,1) and cell>max(lower,past,candidate)
hidden=.2*tanh(lower)
assert not isclose(d*lower,d*hidden)
# Isolate the depth path with a cell-dependent sigmoid: F(c)=c*sigmoid(2c).
def path(c):return c*sigmoid(2*c)
def derivative(c):
 g=sigmoid(2*c);return g+2*c*g*(1-g)
for c in [-1.,1.]:
 numerical=(path(c+1e-6)-path(c-1e-6))/2e-6
 assert isclose(derivative(c),numerical,rel_tol=1e-7)
assert derivative(1)>1 and derivative(-1)<0
# Table2 is a separate reranking protocol; preserve its explicit arithmetic.
test_gain=43.08-40.63;dev_gain=30.05-26.61
assert isclose(test_gain,2.45) and isclose(dev_gain,3.44)
bleu=[34.48,33.81,32.19];assert all(a>b for a,b in zip(bleu,bleu[1:]))
print(json.dumps(dict(ordinary_cell=ordinary,with_depth_carry=cell,total_fixed_gate_weight=d+f+i,lower_cell_carry=d*lower,lower_hidden_carry=d*hidden,depth_path_derivative_positive=derivative(1),depth_path_derivative_negative=derivative(-1),table2_test_gain=test_gain,table2_dev_gain=dev_gain,table1_depth3_5_10_bleu=bleu),sort_keys=True))
