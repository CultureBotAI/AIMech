"""Chosen algebraic examples, not author code, trained models or benchmarks."""
import json
from math import tanh,isclose

def conv(v):
    return [sum(v[j] for j in range(max(0,i-1),min(len(v),i+2))) for i in range(len(v))]

s=[1.,2.];r=[.2,.8];u=.3
before=conv([x*y for x,y in zip(r,s)])
after=[x*y for x,y in zip(r,conv(s))]
assert before!=after
candidate=tanh(before[0]);old_weighted=u*s[0]+(1-u)*candidate
candidate_weighted=(1-u)*s[0]+u*candidate
assert not isclose(old_weighted,candidate_weighted)
# Same tied kernels support different unroll lengths; counts exclude readout/embedding.
def count(n,l=2,w=4,m=24,k=3):
    return dict(cgru_parameters=3*l*(k*k*m*m+m),sequential_cgru_stages=l*n,updated_scalar_states=l*n*w*n*m)
c10=count(10);c20=count(20)
assert c10['cgru_parameters']==c20['cgru_parameters']
assert c20['sequential_cgru_stages']==2*c10['sequential_cgru_stages']
assert c20['updated_scalar_states']==4*c10['updated_scalar_states']
# Zero padding breaks exact translation equivariance at a finite boundary.
v=[1.,2.,3.]
def shift(x):return [0.]+x[:-1]
assert conv(shift(v))!=shift(conv(v))
# Averaging relaxed parameter sets is not an output ensemble through nonlinearities.
w1,w2,x=0.,2.,1.
averaged_parameters=tanh((w1+w2)*x/2)
averaged_outputs=(tanh(w1*x)+tanh(w2*x))/2
assert not isclose(averaged_parameters,averaged_outputs)
print(json.dumps(dict(reset_before=before,reset_after=after,old_weighted=old_weighted,candidate_weighted=candidate_weighted,count10=c10,count20=c20,conv_shift=conv(shift(v)),shift_conv=shift(conv(v)),averaged_parameters=averaged_parameters,averaged_outputs=averaged_outputs),sort_keys=True))
