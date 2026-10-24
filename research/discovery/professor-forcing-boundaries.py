"""Finite discriminator and sampling-gradient identities, without fitting."""
from math import exp,log
import json
p=[.75,.25];q=[.25,.75];d=[a/(a+b) for a,b in zip(p,q)];m=[(a+b)/2 for a,b in zip(p,q)]
cd=-sum(a*log(c)+b*log(1-c) for a,b,c in zip(p,q,d))
js=.5*sum(a*log(a/z)+b*log(b/z) for a,b,z in zip(p,q,m))
assert abs(cd-(log(4)-2*js))<1e-12
cf=-sum(b*log(c) for b,c in zip(q,d));ct=-sum(a*log(1-c) for a,c in zip(p,d))
sigmoid=lambda x:1/(1+exp(-x))
def expected(theta):
 prob=sigmoid(theta);loss=[-log(sigmoid(theta+y)) for y in [0,1]]
 direct=(1-prob)*(sigmoid(theta)-1)+prob*(sigmoid(theta+1)-1)
 score=prob*(1-prob)*(loss[1]-loss[0])
 return (1-prob)*loss[0]+prob*loss[1],direct,score
value,direct,score=expected(.3);step=1e-6;fd=(expected(.3+step)[0]-expected(.3-step)[0])/(2*step)
assert abs(fd-direct-score)<1e-9 and abs(score)>1e-3
# A constant observed feature has identical distributions despite unequal token laws.
assert p!=q and sum(p)==sum(q)==1
print(json.dumps(dict(frozen_behavior_distributions=dict(teacher=p,free=q),optimal_balanced_discriminator=d,discriminator_loss=cd,jensen_shannon=js,free_confusion_loss=cf,optional_teacher_confusion_loss=ct,constant_feature_pushforwards=dict(teacher=[1.],free=[1.]),sampling_gradient_example=dict(expected_loss=value,fixed_realization_path_derivative=direct,sampling_distribution_term=score,full_finite_difference=fd),scope='Finite frozen-distribution discriminator algebra and a constructed parameter-dependent Bernoulli expectation. This demonstrates mathematical distinctions, not an assertion about uninspected author code or a proof of Professor Forcing convergence. No fitting or empirical replication.'),indent=2))
