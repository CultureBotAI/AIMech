"""Exact illustrative gates; not a BAM implementation or model evaluation."""
from fractions import Fraction as F
import itertools
import json

features = [[-6,0,2,4,8,10],[3,-2,1,9,0,-5]]
channel_means = [sum(map(F,row))/len(row) for row in features]
spatial_maxima = [max(row[p] for row in features) for p in range(6)]
assert channel_means==[F(3),F(1)] and spatial_maxima==[3,0,2,9,8,10]
# Values strictly inside (0,1) can be sigmoid outputs of finite real logits.
# No claim is made that fitted ACAM/MSAM weights produce these chosen gates.
channel = [F(1,4),F(3,4)]
spatial = [F(2,3),F(1,2),F(1,5),F(4,5),F(3,5),F(1,3)]
gate = [[c*s for s in spatial] for c in channel]
out = [[x*g for x,g in zip(row,gr)] for row,gr in zip(features,gate)]
assert all(abs(y)<=abs(x) for row,yr in zip(features,out) for x,y in zip(row,yr))
assert all(0<g<1 for row in gate for g in row)
assert all(gate[0][i]*gate[1][j]-gate[0][j]*gate[1][i]==0 for i,j in itertools.combinations(range(6),2))
nonseparable = [[F(1,2),F(1,4)],[F(1,4),F(1,2)]]
determinant = nonseparable[0][0]*nonseparable[1][1]-nonseparable[0][1]*nonseparable[1][0]
assert determinant==F(3,16)
# Product of separately sigmoid-normalized logits differs from sigmoid of their sum.
assert F(1,2)*F(1,2)==F(1,4) and F(1,4)!=F(1,2)
print(json.dumps(dict(scope='Chosen exact gates demonstrate pooling axes, separability and attenuation; no learned branch execution or empirical validation.',channel_means=list(map(str,channel_means)),spatial_maxima=spatial_maxima,gate=[[str(x) for x in row] for row in gate],output=[[str(x) for x in row] for row in out],all_two_by_two_gate_minors_zero=True,nonrepresentable_gate_determinant=str(determinant),zero_logits=dict(product_of_sigmoids='1/4',sigmoid_of_sum='1/2')),indent=2))
