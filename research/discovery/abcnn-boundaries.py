"""Chosen ABCNN formula examples; no author implementation or training."""
import json
from math import isclose,tanh

def interactions(x,y):return [[1/(1+abs(a-b)) for b in y] for a in x]
def weights(x,y):return [sum(row) for row in interactions(x,y)]
def read(x,y,w=2):
    a=weights(x,y)
    return [sum(a[k]*x[k] for k in range(j,j+w)) for j in range(len(x)-w+1)]
x=[1.,2.,4.];y=[0.,3.]
a=weights(x,y);pool=read(x,y);duplicated=read(x,y+y)
assert all(isclose(v,2*u) for u,v in zip(pool,duplicated))
normalized=sum(a[k]*x[k] for k in range(2))/sum(a[:2])
assert not isclose(pool[0],normalized)
assert not isclose(sum(a),1)
# Sentence lengths and convolution widths imply alignment and pooling dimensions.
s0,s1,w=5,7,3
conv_shape=(s0+w-1,s1+w-1)
assert conv_shape==(7,9)
pool_shape=(conv_shape[0]-w+1,conv_shape[1]-w+1)
assert pool_shape==(s0,s1)
# Positive distance affinity differs from a bilinear-tanh interaction.
euc=interactions([0.,1.],[0.,2.]);bilinear=[[tanh(a*b) for b in [0.,2.]] for a in [0.,1.]]
assert euc!=bilinear
print(json.dumps(dict(row_sums=a,weighted_window_sum=pool,duplicated_counterpart=duplicated,normalized_first_window=normalized,conv_alignment_shape=conv_shape,pooled_lengths=pool_shape,distance_affinity=euc,bilinear_tanh=bilinear),sort_keys=True))
