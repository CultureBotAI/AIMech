"""Exact curator examples, not an implementation or empirical evaluation of an estimator."""
from fractions import Fraction as F
from math import factorial, comb
import json

def filt(h, u):
    return [sum(F(h[j])*u[t-j] for j in range(min(t+1,len(h)))) for t in range(len(u))]

def wh(r, f, s, u):
    return filt(s, [f(v) for v in filt(r,u)])

def hw(f, g, h, u):
    return [h(v) for v in filt(g,[f(v) for v in u])]

def moment(n):
    return F(0) if n%2 else F(factorial(n),2**(n//2)*factorial(n//2))

def mixed(poly, mean, weights, powers):
    """E[p(mean+aX+bY) X**p Y**q] for independent standard Gaussians."""
    total=F(0)
    for degree,c in enumerate(poly):
        for i in range(degree+1):
            for j in range(degree-i+1):
                k=degree-i-j
                total+=c*comb(degree,i)*comb(degree-i,j)*mean**k*weights[0]**i*weights[1]**j*moment(i+powers[0])*moment(j+powers[1])
    return total

u=list(map(F,[1,2,-1]));r=list(map(F,[1,2]));s=list(map(F,[1,3]));square=lambda x:x*x
w=wh(r,square,s,u);assert w==[1,19,57]
a,b=F(2),F(3)
ws=wh([a*v for v in r],lambda x:b*square(x/a),[v/b for v in s],u);assert ws==w
h=lambda x:x+x**3
n=hw(square,r,h,u);assert n==[2,222,738]
ns=hw(lambda x:a*square(x),[b/a*v for v in r],lambda x:h(x/b),u);assert ns==n
printed=hw(lambda x:a*square(x),[v/(a*b) for v in r],lambda x:b*h(x),u)
assert printed==[F(10,9),30,90] and printed!=n
identity=lambda x:x
assert wh([1],square,r,u)==filt(r,[square(v) for v in u])
assert wh(r,square,[1],u)==[square(v) for v in filt(r,u)]
assert hw(identity,r,h,u)==[h(v) for v in filt(r,u)]
assert hw(square,r,identity,u)==filt(r,[square(v) for v in u])
# A non-even polynomial can have zero Gaussian best-linear gain.
first=[mixed([0,-15,0,1],F(0),r,p) for p in [(1,0),(0,1)]];assert first==[0,0]
# ACSE131: zero centered second correlation does not imply linearity.
poly=[0,27,-9,1];mean=F(3)
first2=[mixed(poly,mean,r,p) for p in [(1,0),(0,1)]]
second=[mixed(poly,mean,r,p)-mixed(poly,mean,r,(0,0)) for p in [(2,0),(0,2)]]
assert first2==[15,30] and second==[0,0]
# A Wiener square with equal taps passes the proposed proportionality test.
first3=[mixed([0,0,1],F(2),[F(1),F(1)],p) for p in [(1,0),(0,1)]]
second3=[mixed([0,0,1],F(2),[F(1),F(1)],p)-mixed([0,0,1],F(2),[F(1),F(1)],(0,0)) for p in [(2,0),(0,2)]]
assert first3==[4,4] and second3==[2,2]
# Any Hammerstein sum over scalar input lags has zero mixed finite difference.
interaction=square(1+1)-square(1+0)-square(0+1)+square(0+0);assert interaction==2
# ACSE131 Eq19's cubic coefficient: E[(q^3-Eq^3)X^2]=6 mean(q) a^2.
cubic_second=mixed([0,0,0,1],F(3),r,(2,0))-mixed([0,0,0,1],F(3),r,(0,0));assert cubic_second==18
# Gaussian noise before h(z)=z+z^3 creates z-dependent mean shift.
offsets=[mixed([0,1,0,1],F(z),[F(1),F(0)],(0,0))-h(F(z)) for z in [1,2]];assert offsets==[3,6]
result=dict(wiener_hammerstein_output=w,wiener_hammerstein_rescaled=ws,hammerstein_wiener_output=n,hammerstein_wiener_rescaled=ns,printed_hw_scaling_output=printed,non_even_zero_first_correlation=first,nonlinear_zero_second_correlation=dict(first=first2,second=second),non_hammerstein_proportional_correlations=dict(first=first3,second=second3,mixed_difference=interaction),cubic_second_centered_correlation=cubic_second,pre_output_gaussian_noise_mean_shifts=offsets)
print(json.dumps(result,default=str,indent=2))
