"""Finite curation witnesses, not author-code execution or empirical replication."""
from math import exp, lgamma, isclose
import json

def close(a,b,tol=1e-6):
    assert isclose(a,b,rel_tol=tol,abs_tol=tol),(a,b)

def score(weights,human,m):
    assert 0 <= m <= len(human) == len(weights)
    # Stable index ordering is an explicit curator tie convention.
    order=sorted(range(len(weights)),key=lambda j:(-weights[j],j))
    return sum(human[j] for j in order[:m])

def mean_weights(topics):
    return [sum(v)/len(topics) for v in zip(*topics)]

human=[10.,1.,0.]
topics=[[4.,0.,-1.],[0.,6.,-1.]]
evoc1=sum(score(t,human,1) for t in topics)/2
evoc2=score(mean_weights(topics),human,1)
scaled=[[2*v for v in topics[0]],topics[1]]
evoc1_scaled=sum(score(t,human,1) for t in scaled)/2
evoc2_scaled=score(mean_weights(scaled),human,1)
close(evoc1,evoc1_scaled);assert evoc2 != evoc2_scaled
for t in topics:
    for m in range(4):close(score(t,human,m),score([3*exp(v) for v in t],human,m))
assert score([1,1],[10,1],1) != score([1,1],[1,10],1)

# One scalar topic-coordinate direction in the average Poisson regression loss.
design=[.25,.7,1.2];counts=[1.,0.,3.];n=len(counts);theta=.3
loss=lambda v:sum(exp(q*v)-y*q*v for q,y in zip(design,counts))/n
grad=sum(q*(exp(q*theta)-y) for q,y in zip(design,counts))/n
hessian=sum(q*q*exp(q*theta) for q in design)/n
h=1e-4
grad_fd=(loss(theta+h)-loss(theta-h))/(2*h)
hess_fd=(loss(theta+h)-2*loss(theta)+loss(theta-h))/(h*h)
close(grad,grad_fd);close(hessian,hess_fd)
assert not isclose(n*hessian,hess_fd,rel_tol=.01)

# With two topics, second log-rate fixed at zero, w is an interior simplex coordinate.
# At theta=0, w=.5 and observed y=2, exp(w*theta)-2*w*theta is convex in each
# coordinate but its joint Hessian has determinant -1.
biconvex_hessian=[[.25,-1.],[-1.,0.]]
joint_det=biconvex_hessian[0][0]*biconvex_hessian[1][1]-biconvex_hessian[0][1]**2
assert joint_det<0

# Positive conditional rates alone do not imply compatibility of nodewise laws.
# The same joint four-cell cross ratio would have to equal both exp(b12) and exp(b21).
conditional_cross_ratios=[exp(.3),exp(-.2)]
assert conditional_cross_ratios[0]!=conditional_cross_ratios[1]
# A positive raw-count quadratic eventually dominates factorial penalties.
raw_diagonal_logs=[.1*t*t-2*lgamma(t+1) for t in [100,200,400]]
assert raw_diagonal_logs[0]<raw_diagonal_logs[1]<raw_diagonal_logs[2]

# Symmetry of averaged coefficients does not guarantee a selected edge stays nonzero.
assert (.2+(-.2))/2==0
# Literal large-n gradient block loop in the inspected release covers 1:p,
# whereas its augmented design has p+1 rows. No MATLAB execution is implied.
p=4;n_large=6000;block_size=round(p/(n_large/5000))+1
visited=[]
for start in range(1,p+1,block_size):visited+=list(range(start,min(start+block_size-1,p)+1))
assert p+1 not in visited
# Pair-transfer simplex direction stays feasible over the exact bound interval.
w=[.2,.3,.5];mu=.17;updated=[w[0]+mu,w[1]-mu,w[2]]
assert all(v>=0 for v in updated);close(sum(updated),1.)
print(json.dumps(dict(status='passed',evocation=dict(evoc1=evoc1,evoc2=evoc2,evoc1_after_topic_rescaling=evoc1_scaled,evoc2_after_topic_rescaling=evoc2_scaled),poisson_derivatives=dict(gradient=grad,finite_gradient=grad_fd,hessian=hessian,finite_hessian=hess_fd,unnormalized_hessian=n*hessian),joint_hessian_determinant=joint_det,incompatible_conditional_cross_ratios=conditional_cross_ratios,positive_raw_interaction_diagonal_log_terms=raw_diagonal_logs,large_n_gradient_rows=dict(visited=visited,expected=list(range(1,p+2))),simplex_pair_update=updated),indent=2))
