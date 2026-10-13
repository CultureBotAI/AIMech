"""Fixed soft-feedback calculations; no model fitting or empirical replication."""
from math import exp
import json
embeddings=[-1.,2.]
def relaxed(theta,alpha,noise=(0.,0.)):
 scores=[theta+noise[0],noise[1]];largest=max(scores)
 weights=[exp(alpha*(s-largest)) for s in scores];q=[w/sum(weights) for w in weights]
 value=sum(p*e for p,e in zip(q,embeddings))
 derivative=alpha*q[0]*(embeddings[0]-value)
 loss=(value-1.)**2/2
 return value,derivative,loss,(value-1.)*derivative
rows=[];step=1e-6
for noise in [(0.,0.),(.3,-.2)]:
 value,d,loss,g=relaxed(.2,2.,noise);fd=(relaxed(.2+step,2.,noise)[2]-relaxed(.2-step,2.,noise)[2])/(2*step)
 assert abs(g-fd)<1e-8
 rows.append(dict(fixed_noise=noise,relaxed_embedding=value,embedding_derivative=d,loss=loss,loss_gradient=g,finite_difference=fd))
# A hard greedy choice stays on its selected embedding locally, with zero choice-path derivative.
assert .2-step>0
tie=[]
for alpha in [1.,10.,100.]:
 value,d,_,_=relaxed(0.,alpha);assert abs(value-.5)<1e-12 and abs(d+.75*alpha)<1e-12
 tie.append(dict(alpha=alpha,embedding=value,embedding_derivative=d))
unique=relaxed(.2,1000.)
assert abs(unique[0]+1.)<1e-10 and abs(unique[1])<1e-10
print(json.dumps(dict(cases=rows,hard_greedy_local_choice_gradient=0,tied_maxima=tie,unique_maximum_at_alpha1000=dict(embedding=unique[0],derivative=unique[1]),scope='Finite deterministic score/embedding example, plus one fixed perturbed-score realization. No sampling-variance estimate, universal gradient guarantee, model fitting or accuracy replication.'),indent=2))
