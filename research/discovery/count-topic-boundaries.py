"""Finite curator witnesses for fixed-length counts and canonical admixtures.

These are direct mathematical checks, not source-code reproduction, fitted models
or empirical validation. Infinite-support conclusions use explicit tail arguments.
"""
from itertools import product
from collections import Counter
from math import exp, log, factorial, prod, isclose
import json

def close(a,b):assert isclose(a,b,rel_tol=1e-10,abs_tol=1e-10),(a,b)
def compositions(L,p):return [x for x in product(range(L+1),repeat=p) if sum(x)==L]
def energy(x,theta,Phi):return sum(a*b for a,b in zip(theta,x))+sum(x[i]*Phi[i][j]*x[j] for i in range(len(x)) for j in range(len(x)))
def count_weights(L,theta,Phi):return {x:exp(energy(x,theta,Phi))/prod(factorial(t) for t in x) for x in compositions(L,len(theta))}
# Exact finite support, multinomial reduction and normalized distribution.
theta=[log(2),log(3),log(5)];zero=[[0.]*3 for _ in range(3)]
for L in range(7):
 q=count_weights(L,theta,zero);Z=sum(q.values());close(Z,10.**L/factorial(L))
 for x,w in q.items():close(w/Z,factorial(L)*prod((v/10)**n/factorial(n) for v,n in zip([2,3,5],x)))
# Fixed-total gauge: common theta shift and rank-one Phi shift add constants.
Phi=[[0.,.2,-.1],[.2,0.,.3],[-.1,.3,0.]];L=4
q=count_weights(L,theta,Phi);shifted=count_weights(L,[t+.7 for t in theta],[[v-.2 for v in row] for row in Phi])
for x in q:close(shifted[x]/q[x],exp(.7*L-.2*L*L))
# Sequence multiplicity cancels factorial base measure.
seq_totals=Counter();L=3
for seq in product(range(3),repeat=L):
 x=tuple(seq.count(i) for i in range(3));seq_totals[x]+=exp(energy(x,theta,Phi))/factorial(L)
q=count_weights(L,theta,Phi)
for x in q:close(seq_totals[x],q[x])
# Token Gibbs requires the diagonal correction for an arbitrary symmetric matrix.
P=[[.4,.2,-.1],[.2,-.3,.3],[-.1,.3,.1]];rest=[1,1,0];increment=[]
for s in range(3):
 x=rest.copy();x[s]+=1
 actual=energy(x,theta,P)-energy(rest,theta,P)
 predicted=theta[s]+2*sum(P[s][j]*rest[j] for j in range(3))+P[s][s]
 close(actual,predicted);increment.append(actual)
# Under fixed-total counts, knowing p-1 coordinates determines the last.
assert [x for x in compositions(3,3) if x[1:]==(1,1)]==[(1,1,1)]
# A positive two-variable potential does not imply positive count covariance.
q=count_weights(2,[0.,0.],[[0.,.7],[.7,0.]])
Z=sum(q.values());mean=sum(x[0]*w/Z for x,w in q.items());var=sum((x[0]-mean)**2*w/Z for x,w in q.items());cov=sum((x[0]-mean)*(x[1]-(2-mean))*w/Z for x,w in q.items());close(cov,-var);assert cov<0
# Eigenvalue display needs sign care for arbitrary diagonals: Phi=-I, p=2,L=2.
qneg=count_weights(2,[0.,0.],[[-1.,0.],[0.,-1.]])
actual=log(sum(qneg.values()));printed=-4+2*log(2)-log(2)
assert actual>printed
safe=2*log(2)-log(2);assert actual<=safe
# Independent Poisson / Poisson-total * multinomial identity.
rates=[2.,3.,5.]
for x in product(range(4),repeat=3):
 L=sum(x);left=prod(exp(-r)*r**n/factorial(n) for r,n in zip(rates,x));right=exp(-10)*10**L/factorial(L)*factorial(L)*prod((r/10)**n/factorial(n) for r,n in zip(rates,x));close(left,right)
# Canonical mixture of normalized rates differs from LDA arithmetic mixing.
p1=[.2,.8];p2=[.9,.1];arithmetic=[(a+b)/2 for a,b in zip(p1,p2)];geometric=[(a*b)**.5 for a,b in zip(p1,p2)];canonical=[a/sum(geometric) for a in geometric]
close(arithmetic[0],.55);close(canonical[0],.6);assert arithmetic!=canonical
# For fixed topic totals m1=m2=1, convolution differs from averaged-parameter law.
conv=[p1[1]*p2[1],p1[0]*p2[1]+p1[1]*p2[0],p1[0]*p2[0]];close(sum(conv),1.)
# Prior update interaction hyperparameter is beta beta^T+x x^T, not
# (beta+x)(beta+x)^T. Cross terms make the claimed closure fail.
beta=[1,2];x=[3,4]
correct=[[beta[i]*beta[j]+x[i]*x[j] for j in range(2)] for i in range(2)]
claimed=[[(beta[i]+x[i])*(beta[j]+x[j]) for j in range(2)] for i in range(2)]
assert correct[0][1]==14 and claimed[0][1]==24
# Proposed topic transfer preserves total: m_l+a, m_q-a (not m_q+a).
ml,mq,a=2,4,1;assert (ml+a)+(mq-a)==ml+mq;assert (ml+a)+(mq+a)!=ml+mq
print(json.dumps(dict(status='PASS',multinomial_reduction_lengths=list(range(7)),sequence_count_states=len(seq_totals),token_increment_with_diagonal=increment,fixed_total_positive_potential_covariance=cov,negative_eigenvalue_actual_log_partition=actual,unqualified_printed_bound=printed,safe_positive_part_bound=safe,arithmetic_topic_probability=arithmetic,canonical_topic_probability=canonical,conditional_topic_convolution=conv,prior_interaction_correct=correct,prior_interaction_claimed=claimed,scope='Original finite witnesses; no implementation inspection, fit, empirical benchmark, AIS accuracy proof or automatic extension of unconstrained graph semantics.'),indent=2))
