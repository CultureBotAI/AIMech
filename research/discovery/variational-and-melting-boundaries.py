"""Finite curator checks of GAM/variational-EM boundaries; no empirical fit."""
from math import log,exp,isclose,tanh
from itertools import product
import json

def coin_likelihood(theta):return theta**2+(1-theta)**2
def posterior(theta):return theta**2/coin_likelihood(theta)
def divergence(q,theta):return q*log(q/theta**2)+(1-q)*log((1-q)/(1-theta)**2)
oldtheta=.3;oldq=.4;newq=min(.6,max(.4,posterior(oldtheta)));newtheta=newq
assert newq==.4 and newtheta==.4
assert divergence(newq,newtheta)<divergence(oldq,oldtheta)
assert coin_likelihood(newtheta)<coin_likelihood(oldtheta)
assert isclose(coin_likelihood(oldtheta),.58) and isclose(coin_likelihood(newtheta),.52)
assert min(.6,max(.4,posterior(newtheta)))==newq
assert 4*newtheta-2!=0
assert posterior(.5)==.5 and coin_likelihood(.5)<coin_likelihood(.4)

# A correlated fixed latent law outside the mean-field family has a positive gap
# independent of the learned observed-data parameter. This refutes a universal
# claim that any inexact independence-based variational EM cannot be stationary
# for observed likelihood. It does not refute the paper's conditional GAM theorem.
states=list(product([0,1],repeat=2));r={(0,0):.3,(0,1):.2,(1,0):.2,(1,1):.3}
def meanfield(mu,nu):return {(a,b):(mu if a else 1-mu)*(nu if b else 1-nu) for a,b in states}
def kl(q,p):return sum(v*log(v/p[z]) for z,v in q.items() if v)
q=meanfield(.5,.5);gap=kl(q,r);assert gap>0 and isclose(gap,.5*log(25/24))
J=log(r[1,1]*r[0,0]/(r[1,0]*r[0,1]));assert 4-abs(J)>0
# KL Hessian in (mu,nu) has diagonal 1/[mu(1-mu)] >=4 and cross term -J.
# Therefore it is strictly convex, and symmetry gives the unique minimum (.5,.5).
assert sum(q.values())==1 and isclose(sum(r.values()),1)
assert not isclose(r[1,1],sum(v for (a,b),v in r.items() if a)*sum(v for (a,b),v in r.items() if b))
data=[1,1,0]
def observed_loglike(theta):return sum(log(theta if y else 1-theta) for y in data)
def joint(theta,y,z):return (theta if y else 1-theta)*r[z]
def elbo(theta):return sum(sum(q[z]*log(joint(theta,y,z)/q[z]) for z in states) for y in data)
for theta in [.2,.4,2/3,.8]:
 assert isclose(sum(joint(theta,y,z) for y in [0,1] for z in states),1)
 assert isclose(observed_loglike(theta)-elbo(theta),len(data)*gap)
theta_star=2/3;assert isclose(2/theta_star-1/(1-theta_star),0,abs_tol=1e-12)

# At fixed q, d KL(q||p_J)/dJ is E_p[z1z2]-E_q[z1z2].
h=log(2/3)
def boltzmann(j):
 raw={(a,b):exp(h*(a+b)+j*a*b) for a,b in states};normalizer=sum(raw.values())
 return {z:v/normalizer for z,v in raw.items()}
p=boltzmann(J);assert all(isclose(p[z],r[z]) for z in states)
eps=1e-6;derivative=(kl(q,boltzmann(J+eps))-kl(q,boltzmann(J-eps)))/(2*eps)
assert isclose(derivative,p[1,1]-q[1,1],abs_tol=1e-9) and derivative>0

# Marginal independence of one pair does not imply its direct coupling is zero.
# Indirect effects through a third hidden variable can cancel that direct effect.
a=1.;j12=-log((1+exp(2*a))*2/(1+exp(a))**2)
raw3={(x,y,z):exp(j12*x*y+a*x*z+a*y*z) for x,y,z in product([0,1],repeat=3)}
z3=sum(raw3.values());p3={s:v/z3 for s,v in raw3.items()}
ex=sum(x*v for (x,y,z),v in p3.items());ey=sum(y*v for (x,y,z),v in p3.items());exy=sum(x*y*v for (x,y,z),v in p3.items())
assert abs(j12)>.01 and isclose(exy,ex*ey,abs_tol=1e-14)
# For points -1,+1 the melting map is tanh(2*beta*y). At beta=1,
# y=0 is an unstable fixed point, F''(0)=2-4*beta=-2. At beta=.5
# the map is tanh(y)=y-y^3/3+..., with no contraction factor below1.
def melting(y,beta):
 w=[exp(-beta*(x-y)**2) for x in [-1,1]]
 return sum(x*v for x,v in zip([-1,1],w))/sum(w)
assert melting(0,1)==0 and 2-4*1<0
for y in [.1,.01,.001]:assert isclose(melting(y,.5),tanh(y),abs_tol=1e-15)
ratios=[tanh(y)/y for y in [.1,.01,.001]]
assert ratios[0]<ratios[1]<ratios[2]<1 and ratios[-1]>.999999
print(json.dumps(dict(constrained_coin=dict(old_likelihood=coin_likelihood(oldtheta),new_likelihood=coin_likelihood(newtheta),divergence_decreased=True,restricted_fixed_point=newtheta,observed_derivative=4*newtheta-2,ordinary_em_can_stick_at_minimum=True),inexact_variational_stationarity=dict(latent_probabilities=list(r.values()),unique_meanfield_probabilities=list(q.values()),gap_per_observation=gap,parameter_independent_gap=True,likelihood_stationary_theta=theta_star,hessian_lower_bound=4-abs(J)),kl_gradient=dict(finite_difference=derivative,correct_expectation_difference=p[1,1]-q[1,1],printed_sign_opposite=True),pair_coupling=dict(direct_coupling=j12,marginal_covariance=exy-ex*ey),melting=dict(unstable_fixed_center=0,free_energy_second_derivative=-2,critical_point_map='tanh(y)',critical_ratios=ratios),limitations='Normalized finite constructions and explicit algebra; not historical software, a repaired general theorem or a broad empirical study.'),indent=2))
