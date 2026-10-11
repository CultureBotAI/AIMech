"""Curator calculations, not author-code reproduction or empirical validation.

Finite witnesses check tensor bookkeeping, conditionals and source expressions.
The stated domination arguments are analytic; finite grids do not prove tail
integrability. No model training, inference benchmark or graph recovery is run.
"""
from itertools import permutations, combinations, product
from math import prod, factorial, exp, log, sqrt, isclose
import json

def close(a,b):
    assert isclose(a,b,rel_tol=1e-10,abs_tol=1e-10),(a,b)

# Coefficient per ordered tensor entry, stored once for each unordered set.
theta={(1,(0,)):-.4,(1,(1,)):.2,(1,(2,)):-.1,
       (2,(0,)):.5,(2,(1,)):-.3,(2,(2,)):.7,
       (2,(0,1)):.25,(2,(1,2)):-.2,
       (3,(0,)):.15,(3,(0,1)):-.1,(3,(0,1,2)):.2}

def energy(x,params=theta):
    return sum(c*prod(x[i]**(1/j) for i in order)
               for (j,S),c in params.items() for order in permutations(S))

def conditional(t,x,s):
    # Fix one index at s; (ell-1)! ordered remaining slots, ell choices.
    eta={j:0. for j in (1,2,3)}
    for (j,S),c in theta.items():
        if s in S:
            rest=tuple(i for i in S if i!=s)
            eta[j]+=len(S)*sum(c*prod(x[i]**(1/j) for i in order)
                              for order in permutations(rest))
    return sum(v*t**(1/j) for j,v in eta.items())

checks=0
for x in product([0.,1.,4.,27.],repeat=3):
    for s in range(3):
        y=list(x);y[s]=8.
        close(energy(y)-energy(x),conditional(8.,x,s)-conditional(x[s],x,s))
        checks+=1
# Three-way finite difference of log kernel cancels every pairwise/unary term.
mixed=sum((-1)**(3-sum(v))*energy(v) for v in product([0,1],repeat=3))
close(mixed,factorial(3)*.2)
# If triple coefficient is zero, the same mixed difference vanishes.
pair={key:c for key,c in theta.items() if len(key[1])<=2}
close(sum((-1)**(3-sum(v))*energy(v,pair) for v in product([0,1],repeat=3)),0.)
# k=2 SQR convention: diagonal -> j=1 unary, theta -> j=2 unary.
phi=[[-.4,.25,0.],[.25,.2,-.2],[0.,-.2,-.1]];unary=[.5,-.3,.7]
k2={key:c for key,c in theta.items() if key[0]<=2}
for x in product([0.,1.,4.],repeat=3):
    close(energy(x,k2),sum(unary[i]*sqrt(x[i]) for i in range(3))+
          sum(phi[i][j]*sqrt(x[i])*sqrt(x[j]) for i in range(3) for j in range(3)))
# AM-GM growth bound for each allowed root monomial, including zero coordinates.
amgm_checks=0
for j in range(1,5):
    for ell in range(1,min(j,3)+1):
        for x in product([0.,.1,1.,4.,27.],repeat=ell):
            v=prod(t**(1/j) for t in x);s=sum(x)
            assert v<=(s/ell)**(ell/j)+1e-10
            assert (s/ell)**(ell/j)<=1+s+1e-10
            amgm_checks+=1
# Bound the finite Poisson exponent by C + sum_i d_i*x_i using absolute terms.
C=sum(factorial(len(S))*abs(c) for (j,S),c in theta.items())
d=[sum(factorial(len(S))*abs(c) for (j,S),c in theta.items() if i in S) for i in range(3)]
for x in product([0.,1.,8.,27.,100.],repeat=3):
    assert energy(x)<=C+sum(a*t for a,t in zip(d,x))+1e-9
# Analytically sum exp(C+sum d_i*x_i)/prod x_i!: exp(C+sum exp(d_i)).
log_envelope_sum=C+sum(exp(a) for a in d)
# A genuinely positive triple interaction can coexist with strict leading decay:
# L=-sum x + 1.5*(x1*x2*x3)^(1/3) <= -.5*sum x by AM-GM.
# Add sqrt(x1)+.6*(x1*x2)^(1/3), both lower degree.
def young_constant(a,r,eps):
    return (1-r)*a*(a*r/eps)**(r/(1-r))
cs=young_constant(1.,.5,.1)+young_constant(.6/2**(2/3),2/3,.1)
for x in product([0.,.1,1.,8.,27.,100.],repeat=3):
    s=sum(x);leading=-s+1.5*prod(t**(1/3) for t in x)
    assert leading<=-.5*s+1e-9
    h=leading+sqrt(x[0])+.6*(x[0]*x[1])**(1/3)
    assert h<=-.3*s+cs+1e-9
# Boundary with no degree-one terms: product exp(-sqrt(x_i)), p=3, Z=2^3.
boundary_partition=8
# Source moment formula witness: base Poisson lambda=2 has M(0)=2,
# M(1)=2+log(2); subtracting M(1) from itself gives 1, not the mean 2.
M0=2.;M1=2.+log(2.)
close(exp(M1-M0),2.);close(exp(M1-M1),1.)
# Printed Eq14 first Hessian entry, k=2,j=1: E[X^1.5]-E[X]^2
# is not Var(X). Poisson lambda=2 finite numerical approximation, tail tiny;
# the exact variance is known analytically. This is an illustration, not a tail proof.
pm=[exp(-2.)*2.**n/factorial(n) for n in range(50)]
m15=sum(n**1.5*q for n,q in enumerate(pm));wrong=m15-4.
assert abs(wrong-2.)>.1
# Inclusive singleton [0,0] has positive Poisson mass; F(0)-F(0)=0 loses it.
zero_atom=exp(-2.);assert zero_atom>0
# Continuous p=3 L1 change: Jacobian z^2; simplex volume=1/2.
correct_radius_integral=factorial(2)/2.**3*.5
bare_ray_integral=1/2*.5
close(correct_radius_integral,1/8);close(bare_ray_integral,1/4)
# Ordinary and signed Gaussian root conventions differ at x=-2.
assert sqrt((-2.)**2)==2. and -2.!=2.
print(json.dumps(dict(status='PASS',conditional_increment_checks=checks,
 triple_mixed_difference=mixed,pairwise_mixed_difference=0,
 ordered_triple_multiplicity=factorial(3),amgm_witnesses=amgm_checks,
 poisson_envelope_C=C,poisson_envelope_d=d,poisson_log_envelope_sum=log_envelope_sum,
 strict_exponential_decay=.3,lower_degree_bound_constant=cs,
 flat_leading_boundary_partition=boundary_partition,
 corrected_moment=2,printed_moment=1,exact_poisson_variance=2,
 printed_hessian_first_entry_approx=wrong,poisson_zero_atom=zero_atom,
 radial_partition_with_jacobian=correct_radius_integral,
 radial_integral_without_jacobian=bare_ray_integral,
 scope='Original finite witnesses and analytic domination arguments; no author implementation, fitting, benchmark, general boundary classification or finite-grid tail proof.'),indent=2))
