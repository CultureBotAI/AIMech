"""Constructed fractional stack and surrogate-loss checks; no author code."""
from fractions import Fraction as F
import json

# Top first. Nonempty examples avoid unreported empty-stack/underflow rules.
stack=[('a',F(4,10)),('b',F(5,10)),('c',F(8,10))]
pushed=[('c',F(6,10))]+stack
remaining=F(9,10);popped=[]
for symbol,amount in pushed:
 removed=min(remaining,amount);remaining-=removed
 if amount>removed:popped.append((symbol,amount-removed))
assert remaining==0 and popped==[('a',F(1,10)),('b',F(5,10)),('c',F(8,10))]

def read_top(items):
 depth=F(1);out={}
 for symbol,amount in items:
  used=min(depth,amount);out[symbol]=out.get(symbol,F(0))+used;depth-=used
  if depth==0:break
 return out

read=read_top(popped);assert read==dict(a=F(1,10),b=F(5,10),c=F(4,10))
# The read vector loses ordering within the unit-depth interval.
x=[('a',F(1,2)),('b',F(1,2))];y=list(reversed(x));assert read_top(x)==read_top(y)
sout,length=F(3,5),F(7,10);illegal_loss=max(sout-length,F(0))
assert illegal_loss==0 and sout>0 and length<1
print(json.dumps(dict(after_push=[(s,str(a)) for s,a in pushed],after_pop=[(s,str(a)) for s,a in popped],read={s:str(a) for s,a in read.items()},same_read_different_order=read_top(x)==read_top(y),zero_illegal_loss_example=dict(output=str(sout),length=str(length),loss=str(illegal_loss)),interpretation='Specified nonempty fractional stack and read aggregation; no unspecified endpoint, underflow, training or gradient implementation is certified.')))
