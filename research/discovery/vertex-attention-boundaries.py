"""Small explicit attention calculations; not trained VAIN or author code."""
import math
import json


def kernel(addresses,sign=-1):
    return [[math.exp(sign*sum((x-y)**2 for x,y in zip(a,b))) for b in addresses] for a in addresses]


def aggregate(addresses,messages,mode='post-softmax-mask'):
    k = kernel(addresses)
    weights = []
    for i,row in enumerate(k):
        denominator = sum(row) if mode=='post-softmax-mask' else (sum(v for j,v in enumerate(row) if i!=j) if mode=='pre-softmax-exclusion' else 1)
        weights.append([0 if i==j else v/denominator for j,v in enumerate(row)])
    pooled = [sum(w*m for w,m in zip(row,messages)) for row in weights]
    return weights,pooled


addresses = [(0.0,),(1.0,),(3.0,)]
messages = [2.0,5.0,11.0]
post,pooled = aggregate(addresses,messages)
pre,renormalized = aggregate(addresses,messages,'pre-softmax-exclusion')
physical,additive = aggregate(addresses,messages,'unnormalized')
assert all(0<sum(row)<1 for row in post)
assert all(math.isclose(sum(row),1) for row in pre)
assert all(not math.isclose(a,b) for a,b in zip(pooled,renormalized))
assert post[0][1]>post[0][2] and kernel(addresses,1)[0][1]<kernel(addresses,1)[0][2]
assert all(math.isclose(physical[i][j],physical[j][i]) for i in range(3) for j in range(3))
assert not math.isclose(post[0][1],post[1][0])
perm = [2,0,1]
_,permuted = aggregate([addresses[i] for i in perm],[messages[i] for i in perm])
assert all(math.isclose(x,pooled[i]) for x,i in zip(permuted,perm))
same,_ = aggregate([(0.0,)]*3,messages)
assert all(math.isclose(sum(row),2/3) for row in same)
single,single_pool = aggregate([(0.0,)],[9.0])
assert single==[[0]] and single_pool==[0]
print(json.dumps(dict(scope='Three fixed agents, equal-address and singleton cases; no learned encoders, training or timing.',post_softmax_mask=dict(weights=post,row_sums=list(map(sum,post)),pooled=pooled),pre_softmax_exclusion=dict(weights=pre,pooled=renormalized),unnormalized_physical=dict(weights=physical,pooled=additive),permutation_equivariance=True,sign_reversal_changes_distance_preference=True,identical_address_row_sum=2/3,singleton_pool=single_pool,operation_counts=[dict(agents=n,shared_encoder_calls=2*n,full_pairwise_scores=n*n,offdiagonal_messages=n*(n-1)) for n in [2,4,8]]),indent=2))
