"""Finite curator calculations; no historical experiments or general convergence proof."""
from fractions import Fraction as F
from math import exp, log, isclose, pi, sqrt
import json

def scores(x,p):
    q=(F(4,5),F(1,5))
    return (p*(q[0] if x else 1-q[0]),(1-p)*(q[1] if x else 1-q[1]))
def marginal(data,p):
    ans=F(1)
    for x in data:ans*=sum(scores(x,p))
    return ans
def completed(data,labels,p):
    ans=F(1)
    for x,k in zip(data,labels):ans*=scores(x,p)[k]
    return ans

data=[1,1,0];p=F(7,9);labels=[max(range(2),key=lambda k:scores(x,p)[k]) for x in data]
assert labels==[0,0,1]
newp=F(labels.count(0),len(labels));assert newp==F(2,3)
oldL=marginal(data,p);newL=marginal(data,newp)
oldC=completed(data,labels,p);newC=completed(data,labels,newp)
assert newC>oldC and newL<oldL and oldC<oldL
post=[[v/sum(scores(x,p)) for v in scores(x,p)] for x in data]
assert post==[[F(14,15),F(1,15)],[F(14,15),F(1,15)],[F(7,15),F(8,15)]]
expected_log=sum(float(t)*log(float(j)) for x,row in zip(data,post) for t,j in zip(row,scores(x,p)))
entropy=-sum(float(t)*log(float(t)) for row in post for t in row)
assert isclose(log(float(oldL)),expected_log+entropy,abs_tol=1e-12)
completion_probability=F(1)
for row,k in zip(post,labels):completion_probability*=row[k]
assert completion_probability==oldC/oldL>0
# Unprotected zero weight is absorbing for the raw assignment/count update.
assert all(scores(x,F(1))[1]==0 for x in data)
assert labels.count(0)>0 and labels.count(1)>0
all_one_labels=[max(range(2),key=lambda k:scores(x,F(9,10))[k]) for x in data]
assert all_one_labels==[0,0,0]

# Anneal the entire weighted component density, equivalently normalized posterior.
def power_prob(j,tau):
    logs=[log(float(v))/tau for v in j];offset=max(logs)
    a=[exp(x-offset) for x in logs];return [x/sum(a) for x in a]
j=[F(9,100),F(18,100)]
assert all(isclose(x,y) for x,y in zip(power_prob(j,1),[1/3,2/3]))
assert all(isclose(x,y) for x,y in zip(power_prob(j,.5),[1/5,4/5]))
wrong=F(1,10)*F(9,10)**2/(F(1,10)*F(9,10)**2+F(9,10)*F(1,5)**2)
assert wrong==F(9,13) and wrong!=F(1,5)
assert power_prob(j,.01)[1]>1-1e-12
cold=power_prob([F(1,5),F(1,5),F(1,10)],.001)
assert isclose(cold[0],.5) and isclose(cold[1],.5) and 0<cold[2]<1e-250
assert 1.0**100==1.0 and .97**100<.05

# Equal means with unequal Gaussian variances give nested assignment regions.
def gaussian(x,sd):return exp(-x*x/(2*sd*sd))/(sd*sqrt(2*pi))
points=[-3.,-.1,.1,3.]
assign=[max(range(2),key=lambda k:gaussian(x,[3.,.5][k])) for x in points]
assert assign==[0,1,1,0]
hulls=[[min(x for x,k in zip(points,assign) if k==c),max(x for x,k in zip(points,assign) if k==c)] for c in range(2)]
assert hulls[0][0]<hulls[1][0]<hulls[1][1]<hulls[0][1]
# At fixed parameters the relaxed classification objective is affine in labels.
v0=log(.2);v1=log(.6);affine=lambda u:u*v0+(1-u)*v1
second=affine(.6)-2*affine(.5)+affine(.4)
assert abs(second)<1e-12
print(json.dumps(dict(cem=dict(known_component_bernoulli_probabilities=['4/5','1/5'],data=data,initial_weight=str(p),hard_labels=labels,updated_weight=str(newp),marginal_likelihood_before=str(oldL),marginal_likelihood_after=str(newL),completed_likelihood_before=str(oldC),completed_likelihood_after=str(newC),completed_increases_marginal_decreases=True),sem=dict(same_completion_probability=str(completion_probability),sampled_hard_likelihood_not_marginal=True,posterior_entropy_identity_verified=True,empty_map_class_possible=True,unprotected_zero_weight_absorbing=True),caem=dict(joint_scores=list(map(str,j)),tau_one=power_prob(j,1),tau_half=power_prob(j,.5),wrong_unpowered_weight=str(wrong),cold_tie_distribution=power_prob([F(1,5),F(1,5),F(1,10)],.001),a_one_does_not_cool=True),unequal_variance_gaussians=dict(points=points,assignments=assign,overlapping_convex_hulls=hulls),continuous_assignment_objective_second_difference=second,limitations='Finite examples using defined normalized laws, not random empirical runs, source code reproduction or a repaired convergence proof.'),indent=2))
