"""Fixed finite probability checks, not model fitting or empirical replication."""
from fractions import Fraction as Q
from math import log
import json
joint={(0,0):Q(9,20),(0,1):Q(1,20),(1,0):Q(1,20),(1,1):Q(9,20)}
first={x:sum(v for (i,y),v in joint.items() if i==x) for x in [0,1]}
second={y:sum(v for (x,j),v in joint.items() if j==y) for y in [0,1]}
truth={x:joint[x,1]/first[x] for x in [0,1]}
rows=[]
for epsilon in [Q(1),Q(1,2),Q(0)]:
 mixed={(x,y):epsilon*joint[x,y]+(1-epsilon)*first[x]*second[y] for x in [0,1] for y in [0,1]}
 best={x:mixed[x,1]/sum(mixed[x,y] for y in [0,1]) for x in [0,1]}
 def cost(probs):return -sum(float(mixed[x,y])*log(float(probs[x] if y else 1-probs[x])) for x in [0,1] for y in [0,1])
 if epsilon==1:assert best==truth
 else:assert cost(best)<cost(truth)
 # Partial gradients for independently parameterized second-token probabilities.
 # The first-token sampler is held fixed at the correct marginal.
 gradient={x:first[x]*(truth[x]-best[x])/(truth[x]*(1-truth[x])) for x in [0,1]}
 if epsilon==0:assert best[0]==best[1]==second[1]
 rows.append(dict(reference_probability=str(epsilon),true_conditional={str(x):str(q) for x,q in truth.items()},mixed_target_conditional={str(x):str(q) for x,q in best.items()},conditional_cross_entropy_at_truth=cost(truth),conditional_cross_entropy_at_mixed_optimum=cost(best),partial_gradient_at_truth={str(x):str(q) for x,q in gradient.items()}))
print(json.dumps(dict(first_marginal={str(x):str(q) for x,q in first.items()},cases=rows,scope='Idealized two-token sampled-prefix expected loss; fixed correct first-token marginal, independent conditional parameters and positive support. Original partial-gradient convention is not asserted to equal a full derivative through a parameter-dependent sampler. No fitting, empirical guarantee or claim about every schedule.'),indent=2))
