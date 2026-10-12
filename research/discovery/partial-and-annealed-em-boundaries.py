"""Finite curator checks for partial and annealed EM; not historical experiments."""
from fractions import Fraction as F
from math import log, exp, pi, sqrt, isclose
import json

def bernoulli_joint(x,weights,components):
    return [p*(c if x else 1-c) for p,c in zip(weights,components)]
def L(data,w,c):
    return sum(log(float(sum(bernoulli_joint(x,w,c)))) for x in data)
def objective(data,qs,w,c):
    return sum(float(q)*log(float(j)/float(q)) for x,row in zip(data,qs) for q,j in zip(row,bernoulli_joint(x,w,c)) if q)
def weights_of(qs):return [sum(row[k] for row in qs)/len(qs) for k in range(len(qs[0]))]
def posterior(joint):return [v/sum(joint) for v in joint]

# For observed X=0 from Normal(theta,1) and an independent Bernoulli(1/2) latent,
# Q below omits only a theta-independent constant. GEM ascent alone need not give stationarity.
q=lambda theta:-theta*theta/2
assert q(F(1,2))>q(F(1)) and q(F(1,2))<q(F(0))
theta=F(1);step_sum=F(0)
for k in range(30):
    step=F(1,2**(k+2));nxt=(1-step)*theta
    assert q(nxt)>q(theta);theta=nxt;step_sum+=step
assert theta>=1-step_sum>F(1,2)
# The infinite step sum is 1/2, so the elementary product bound keeps theta away from zero.

data=[1,1,0];comp=[F(4,5),F(1,5)];oldw=[F(7,9),F(2,9)]
cache=[[F(19,20),F(1,20)],[F(19,20),F(1,20)],[F(13,30),F(17,30)]]
assert weights_of(cache)==oldw
newcache=[row[:] for row in cache];newcache[0]=posterior(bernoulli_joint(1,oldw,comp))
neww=weights_of(newcache);assert neww[0]==F(139,180)
assert objective(data,newcache,neww,comp)>objective(data,cache,oldw,comp)
assert L(data,neww,comp)<L(data,oldw,comp)
oldtotal=sum(row[0] for row in cache);newtotal=oldtotal-cache[0][0]+newcache[0][0]
assert newtotal==sum(row[0] for row in newcache)
assert F(9,10)*oldtotal+newcache[0][0]!=newtotal

# Sparse EM keeps nonzero frozen outside mass while optimizing relative mass within S.
c3=[F(9,10),F(3,5),F(1,10)];w3=[F(1,2),F(1,3),F(1,6)]
qs=[w3[:] for _ in data];Q=F(5,6);joint=bernoulli_joint(1,w3,c3)
qs2=[]
for x in data:
    j=bernoulli_joint(x,w3,c3)
    qs2.append([Q*j[0]/sum(j[:2]),Q*j[1]/sum(j[:2]),F(1,6)])
assert sum(qs2[0])==1 and qs2[0][2]==qs[0][2]>0
w32=weights_of(qs2)
assert objective(data,qs2,w32,c3)>objective(data,qs,w3,c3)
assert L(data,w32,c3)<L(data,w3,c3)
truncated=[joint[0]/sum(joint[:2]),joint[1]/sum(joint[:2]),F(0)]
assert truncated!=qs2[0]

# A finite-state deterministic annealed E/M step need not improve beta=1 likelihood.
beta=.5
qbeta=[]
for x in data:
    j=bernoulli_joint(x,oldw,comp);v=[float(t)**beta for t in j];qbeta.append([t/sum(v) for t in v])
annealed_w=weights_of(qbeta)
def profile(beta,w):return sum(log(sum(float(j)**beta for j in bernoulli_joint(x,w,comp)))/beta for x in data)
assert profile(beta,annealed_w)>profile(beta,oldw)
assert L(data,annealed_w,comp)<L(data,oldw,comp)
assert isclose(profile(1,oldw),L(data,oldw,comp))
# For observed X=0 with X~Normal(0,.1^2) and independent latent Y~Uniform(0,1),
# the complete density equals the Gaussian peak on its support, so E=-log(peak)<0.
peak=1/(.1*sqrt(2*pi));assert peak>1 and -log(peak)<0
# Cauchy density raised to beta=1/4 has a nonintegrable |y|^-1/2 tail.
assert 2*.25<=1
# Literal '< beta_max' after increment omits fitting the endpoint.
visited=[];current=F(1,4)
while True:
    visited.append(current);current+=F(1,4)
    if not current<F(1):break
assert F(1) not in visited
result=dict(gem=dict(partial_update='1 -> 1/2, exact maximizer 0',thirty_step_parameter=float(theta),all_exact_objectives_increase=True,infinite_sequence_lower_bound='1/2'),incremental=dict(old_weights=list(map(str,oldw)),new_weights=list(map(str,neww)),cached_bound_increase=True,marginal_change=L(data,neww,comp)-L(data,oldw,comp),exact_cached_sum=str(newtotal),decay_is_different=True),sparse=dict(plausible_set=[0,1],fixed_total_mass=str(Q),updated_first_distribution=list(map(str,qs2[0])),outside_mass_preserved=True,bound_increase=True,marginal_change=L(data,w32,c3)-L(data,w3,c3),truncation_different=True),annealing=dict(beta=beta,profiled_tempered_change=profile(beta,annealed_w)-profile(beta,oldw),marginal_change=L(data,annealed_w,comp)-L(data,oldw,comp),beta_one_identity=True,negative_energy_example=-log(peak),continuous_cauchy_power_nonintegrable=True,literal_schedule_stages=list(map(str,visited)),endpoint_missing=True),limitations='Finite algebra and explicit counterexamples; no primary code, empirical fitting study or general convergence proof reproduced.')
print(json.dumps(result,indent=2))
