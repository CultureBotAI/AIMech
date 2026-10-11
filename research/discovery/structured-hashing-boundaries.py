"""Original finite curator examples; no author implementation or benchmark."""
from itertools import product
from math import exp,log,cos,pi
import json

def close(a,b):assert abs(a-b)<2e-8,(a,b)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sig(x):return 1/(1+exp(-x))
def free(p,v):
    d=len(v);return -dot(p[:d],v)-log(1+exp(p[d]+dot(p[d+1:],v)))
def dfree(p,v):
    d=len(v);h=sig(p[d]+dot(p[d+1:],v))
    return [-x for x in v]+[-h]+[-h*x for x in v]
def prob(p,support):
    assert support and len(support)==len(set(support))
    m={v:exp(-free(p,v)) for v in support};z=sum(m.values())
    return {v:x/z for v,x in m.items()}
def fdcheck(fun,p,g):
    largest=0.
    for i in range(len(p)):
        plus=p[:];minus=p[:];plus[i]+=1e-5;minus[i]-=1e-5
        fd=(fun(plus)-fun(minus))/2e-5;close(fd,g[i]);largest=max(largest,abs(fd-g[i]))
    return largest

support=[(1,1,0),(1,0,1),(0,1,1)];p=[.2,-.1,.3,-.4,.5,.7,-.2];data=support[0]
q=prob(p,support);close(sum(q.values()),1)
gd=dfree(p,data);g=[gd[i]-sum(q[v]*dfree(p,v)[i] for v in support) for i in range(len(p))]
err=fdcheck(lambda t:-log(prob(t,support)[data]),p,g)
uniform=prob([0.]*7,support);marginal=tuple(int(sum(w*v[i] for v,w in uniform.items())>.5) for i in range(3))
assert marginal==(1,1,1) and marginal not in support
risk=lambda prediction:sum(w*sum(a!=b for a,b in zip(prediction,v)) for v,w in uniform.items())
close(risk(marginal),1);close(risk(support[0]),4/3)
# Hash buckets store associated output values; repeated values must be deduplicated.
buckets={'00':[support[0]],'01':[support[0],support[1]],'10':[support[2]]}
retrieved=set(v for key in ['00','01','10'] for v in buckets[key]);assert retrieved==set(support)
deduplicated_mass=1/3;duplicate_weighted_mass=2/4;assert deduplicated_mass!=duplicate_weighted_mass

# A finite search pool can miss the global conditional mode despite using valid states.
p2=[.4,.9,.2,.6,-.1];states=list(product((0,1),repeat=2));pool=[(0,0),(1,0),(0,0)]
pred=min(pool,key=lambda v:free(p2,v));global_mode=min(states,key=lambda v:free(p2,v))
assert pred==(1,0) and global_mode==(1,1)
data2=(0,0);frozen_gradient=[a-b for a,b in zip(dfree(p2,data2),dfree(p2,pred))]
err2=fdcheck(lambda t:free(t,data2)-free(t,pred),p2,frozen_gradient)
q2=prob(p2,states);likelihood_gradient=[dfree(p2,data2)[i]-sum(q2[v]*dfree(p2,v)[i] for v in states) for i in range(len(p2))]
assert max(abs(a-b) for a,b in zip(frozen_gradient,likelihood_gradient))>.1
missed_loss=free(p2,global_mode)-free(p2,pred);assert missed_loss<0
zero_update=[a-b for a,b in zip(dfree(p2,pred),dfree(p2,pred))];assert all(x==0 for x in zero_update)

# Spectral hashing: rectangle modes are ranked by squared frequency / side length.
widths=[3.,1.];modes=sorted(((m/length)**2,j,m) for j,length in enumerate(widths) for m in range(1,5))[:4]
assert [(j,m) for _,j,m in modes]==[(0,1),(0,2),(0,3),(1,1)]
def bit(x,a,b,m):return 1 if cos(m*pi*(x-a)/(b-a))>=0 else -1
points=[.1,.4,.8];assert [bit(x,0,1,1) for x in points]==[bit(x+2,2,3,1) for x in points]
# Equation (4) needs a shifted coordinate if its stated interval is [a,b].
assert [bit(x+.5,.5,1.5,1) for x in points] != [1 if cos(pi*(x+.5))>=0 else -1 for x in points]
# An n-row +/-1 matrix has diagonal Y^T Y = n, not one, before rescaling.
y=[(1,1),(1,-1),(-1,1),(-1,-1)]
gram=[[sum(row[i]*row[j] for row in y) for j in range(2)] for i in range(2)]
assert gram==[[4,0],[0,4]]
# Pairwise-uncorrelated balanced product bits need not be jointly independent.
triples=[(a,b,a*b) for a,b in product((-1,1),repeat=2)]
assert all(sum(v[i] for v in triples)==0 for i in range(3))
assert all(sum(v[i]*v[j] for v in triples)==0 for i in range(3) for j in range(i))
assert all(v[2]==v[0]*v[1] for v in triples)
# Even single-axis thresholded continuous orthogonal modes can be correlated.
grid=[(i+.5)/6000 for i in range(6000)]
corr=sum(bit(x,0,1,1)*bit(x,0,1,3) for x in grid)/len(grid);close(corr,-1/3)
print(json.dumps(dict(hashcrbm=dict(normalized_mass=sum(q.values()),maximum_gradient_error=err,marginal_mode=marginal,marginal_mode_hamming_risk=risk(marginal),support_mode_hamming_risk=risk(support[0]),deduplicated_equal_energy_probability=deduplicated_mass,duplicate_weighted_probability=duplicate_weighted_mass),cd_percloss=dict(searched_prediction=pred,global_mode=global_mode,maximum_frozen_gradient_error=err2,negative_approximate_loss=missed_loss,zero_update_despite_missed_mode=zero_update,frozen_prediction_gradient=frozen_gradient,likelihood_gradient=likelihood_gradient),spectral_hashing=dict(selected_modes=modes,binary_code_gram=gram,single_axis_thresholded_mode_correlation=corr,product_bit_joint_support_size=len(triples))),indent=2))
