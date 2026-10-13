"""Constructed soft-read and encoding boundaries; no trained model or author code."""
from fractions import Fraction as F
import itertools,json,math

def read(keys,values,u):
 s=[u*k for k in keys];e=[math.exp(x-max(s)) for x in s];p=[x/sum(e) for x in e]
 return p,sum(a*v for a,v in zip(p,values))
k=[math.log(2),0];v=[1,3];p,o=read(k,v,1)
assert math.isclose(o,5/3)
for perm in itertools.permutations(range(2)):
 assert math.isclose(read([k[i] for i in perm],[v[i] for i in perm],1)[1],o)
pdup,odup=read([k[0],k[0],k[1]],[1,1,3],1)
pzero,ozero=read(k+[0],v+[0],1)
assert math.isclose(odup,7/5) and math.isclose(ozero,5/4)
assert not math.isclose(odup,o) and not math.isclose(ozero,o)
def encode(words):
 J=len(words);d=len(words[0]);return [sum((1-F(j,J)-F(c,d)*(1-2*F(j,J)))*word[c-1] for j,word in enumerate(words,1)) for c in range(1,d+1)]
a=[[1,0],[0,1]];forward=encode(a);backward=encode(a[::-1]);assert forward!=backward
assert [sum(w[c] for w in a) for c in range(2)]==[sum(w[c] for w in a[::-1]) for c in range(2)]
print(json.dumps(dict(soft_weights=p,read=o,additive_next_query=1+o,paired_permutation_invariant=True,duplicated_slot_read=odup,zero_value_unmasked_slot_read=ozero,bow_reverse_equal=True,position_encoded_forward=list(map(str,forward)),position_encoded_reverse=list(map(str,backward)),limits='Chosen one-hop values only; temporal embeddings, training, full architecture and empirical results are not implemented.'),indent=2))
