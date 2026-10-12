"""Exact small SVDD examples; not a historical solver or benchmark."""
from fractions import Fraction as F
import json

x = [F(-2), F(-1), F(1), F(2)]
d2 = [v*v for v in x]

def check(t, penalty, alpha, loss):
    slack = [max(v-t, F(0)) for v in d2]
    assert t >= 0 and all(a >= 0 for a in alpha)
    beta = 1-sum(alpha)
    assert beta >= 0 and beta*t == 0
    assert sum(a*v for a,v in zip(alpha,x)) == 0
    assert all(a*(v-t-s)==0 for a,v,s in zip(alpha,d2,slack))
    if loss == 1:
        assert all(a <= penalty and (penalty-a)*s==0 for a,s in zip(alpha,slack))
    else:
        assert all(a == 2*penalty*s for a,s in zip(alpha,slack))
    primal=t+penalty*sum(s**loss for s in slack)
    mass=sum(alpha)
    dual=sum(a*v for a,v in zip(alpha,d2))
    if loss == 2: dual-=sum(a*a for a in alpha)/(4*penalty)
    # The center term is zero by symmetry; the general term divides by mass.
    assert mass > 0 and primal==dual
    return dict(t=str(t), C=str(penalty), loss=loss, alpha=list(map(str,alpha)), slack=list(map(str,slack)), beta=str(beta), primal=str(primal),dual=str(dual))

results=[]
for t in [F(1),F(5,2),F(4)]:results.append(check(t,F(1,2),[F(1,2),F(0),F(0),F(1,2)],1))
results.append(check(F(0),F(1,10),[F(1,10)]*4,1))
assert 4*F(1,10)<1 # Equality-simplex dual infeasible despite feasible primal.
for t in [F(0),F(1,2),F(1)]:results.append(check(t,F(1,4),[F(1,4)]*4,1))
cstar=1/(2*sum(d2));assert cstar==F(1,20)
results.append(check(F(0),F(1,40),[F(1,5),F(1,20),F(1,20),F(1,5)],2))
results.append(check(F(0),cstar,[F(2,5),F(1,10),F(1,10),F(2,5)],2))
results.append(check(F(3,2),F(1,10),[F(1,2),F(0),F(0),F(1,2)],2))
# Identical observations: two nonessential positive coefficients do not imply LOO rejection.
k=[[F(1),F(1)],[F(1),F(1)]]
for a in [[F(1,2),F(1,2)],[F(1,4),F(3,4)]]:
    assert sum(a)==1 and max(a)<=F(3,4)
    assert sum(a[i]*k[i][i] for i in range(2))-sum(a[i]*a[j]*k[i][j] for i in range(2) for j in range(2))==0
assert F(1)>F(3,4) # A purported vertex (1,0) violates this box.
# With C=2, both full and leave-one-out descriptions have radius0 at the same feature.
assert F(1,2)<2 and F(1)<2
full_alpha=[F(1,2),F(1,2)]
full_support_fraction=F(sum(a>0 for a in full_alpha),2)
loo_rejections=[]
for omitted in range(2):
    training=[i for i in range(2) if i!=omitted]
    weights=[F(1)]
    norm=sum(weights[i]*weights[j]*k[training[i]][training[j]] for i in range(1) for j in range(1))
    query_distance=k[omitted][omitted]-2*sum(a*k[j][omitted] for a,j in zip(weights,training))+norm
    assert norm==1 and query_distance==0
    loo_rejections.append(query_distance>0)
loo_rejection_fraction=F(sum(loo_rejections),2)
assert full_support_fraction!=loo_rejection_fraction
print(json.dumps(dict(status='passed',four_point_kkt=results,L2_threshold=str(cstar),duplicate_support_fraction=str(full_support_fraction),duplicate_loo_rejection_fraction=str(loo_rejection_fraction),interpretation='Exact KKT/primal-dual examples for convex target-only problems; no claim about negative-example nonconvex extensions or historical performance.'),indent=2))
