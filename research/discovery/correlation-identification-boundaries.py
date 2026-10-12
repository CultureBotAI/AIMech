"""Exact curator examples for correlation cascade identification; no data fitting."""
from fractions import Fraction as F
from math import factorial
import json

# Polynomials in two independent standard normal random variables.
def add(a,b):
 out=a.copy()
 for k,v in b.items():out[k]=out.get(k,F(0))+v
 return {k:v for k,v in out.items() if v}
def scale(a,c):return {k:v*c for k,v in a.items() if v*c}
def mul(a,b):
 out={}
 for i,v in a.items():
  for j,w in b.items():
   k=tuple(x+y for x,y in zip(i,j));out[k]=out.get(k,F(0))+v*w
 return out
def power(a,n):
 out={(0,0):F(1)}
 for _ in range(n):out=mul(out,a)
 return out
def normal_moment(n):return F(0) if n%2 else F(factorial(n),2**(n//2)*factorial(n//2))
def expected(a):return sum(v*normal_moment(i)*normal_moment(j) for (i,j),v in a.items())
x={(1,0):F(1)};y={(0,1):F(1)};one={(0,0):F(1)}
u0=add(one,x);u1=add(one,y);q=add(u0,scale(u1,2))
assert expected(q)==3 and expected(power(add(q,scale(one,-3)),2))==5
w_square=power(q,2);h_square=add(power(u0,2),scale(power(u1,2),2))
wc=[expected(mul(w_square,v)) for v in [x,y]];hc=[expected(mul(h_square,v)) for v in [x,y]]
assert wc==[6,12] and hc==[2,4]
# Nonzero mean input is insufficient if polynomial contributions cancel.
w_cancel=add(power(q,3),scale(q,-42))
h_cancel=add(add(power(u0,3),scale(u0,-6)),scale(add(power(u1,3),scale(u1,-6)),2))
zero_w=[expected(mul(w_cancel,v)) for v in [x,y]];zero_h=[expected(mul(h_cancel,v)) for v in [x,y]]
assert zero_w==zero_h==[0,0]
# Both nonlinearities remain nonconstant: g(0)=0, g(1)=-41 or -5.
# A zero DC-gain Wiener filter also defeats a DC shift for an even g.
q_dc0=add(u0,scale(u1,-1));dc_zero=[expected(mul(power(q_dc0,2),v)) for v in [x,y]]
assert dc_zero==[0,0]
def conv(h,u):return [sum(h[j]*u[t-j] for j in range(min(t+1,len(h)))) for t in range(len(u))]
# Separate deterministic zero-state design examples for g(v)=v+v².
h=[F(1),F(2)];u=[F(1),F(2),F(-1)];qv=conv(h,u)
wout=[v+v*v for v in qv];hout=conv(h,[v+v*v for v in u])
# The stationary first-correlation gains would be 7 and 3 respectively.
qw=conv([7*v for v in h],u);wdesign=[[v,v*v] for v in qw];wcoeff=[F(1,7),F(1,49)]
h1=conv([3*v for v in h],u);h2=conv([3*v for v in h],[v*v for v in u]);hdesign=list(map(list,zip(h1,h2)));hcoeff=[F(1,3),F(1,3)]
assert [sum(a*b for a,b in zip(row,wcoeff)) for row in wdesign]==wout==[2,20,12]
assert [sum(a*b for a,b in zip(row,hcoeff)) for row in hdesign]==hout==[2,10,12]
assert wdesign[0][0]*wdesign[1][1]-wdesign[0][1]*wdesign[1][0] != 0
assert hdesign[0][0]*hdesign[1][1]-hdesign[0][1]*hdesign[1][0] != 0
# Independent nonzero-mean noise: centering is needed for squared-input moments.
noise_mean=F(2);uncentered_noise_second=noise_mean*normal_moment(2);assert uncentered_noise_second==2
# A population through-origin fit z=u+n, E[n]=2, has slope 2 rather than 1.
# Centered first correlation is still 1; independent offset handling is distinct.
biased_slope=(expected(power(u0,2))+noise_mean*expected(u0))/expected(power(u0,2))
assert biased_slope==2 and expected(mul(add(u0,scale(one,noise_mean)),x))==1
print(json.dumps(dict(wiener_square_cross=list(map(str,wc)),hammerstein_square_cross=list(map(str,hc)),wiener_nonzero_mean_cancellation=list(map(str,zero_w)),hammerstein_nonzero_mean_cancellation=list(map(str,zero_h)),wiener_zero_dc_cross=list(map(str,dc_zero)),wiener_scaled_design=[[str(v) for v in r] for r in wdesign],hammerstein_scaled_design=[[str(v) for v in r] for r in hdesign],wiener_scaled_coefficients=list(map(str,wcoeff)),hammerstein_scaled_coefficients=list(map(str,hcoeff)),wiener_reconstructed_output=list(map(str,wout)),hammerstein_reconstructed_output=list(map(str,hout)),independent_uncentered_noise_second_moment=str(uncentered_noise_second),uncentered_noise_through_origin_slope=str(biased_slope)),indent=2))
