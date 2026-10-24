"""Constructed Euclidean gradient-clipping examples; no source code or training execution."""
import json
import math


def norm(v):return math.sqrt(sum(x*x for x in v))

def clip(v,tau):
    assert tau>0 and all(math.isfinite(x) for x in v)
    n=norm(v)
    return list(v) if n<=tau else [tau*x/n for x in v]


def near(a,b):return all(math.isclose(x,y,abs_tol=1e-12) for x,y in zip(a,b))


g=[3.,4.];q=clip(g,2.)
assert near(q,[1.2,1.6]) and math.isclose(norm(q),2.)
assert math.isclose(q[0]*g[1],q[1]*g[0])
assert near(clip([0.,0.],2.),[0.,0.]) and near(clip([1.,0.],2.),[1.,0.])
assert near(clip([2.,0.],2.),[2.,0.])
coordinate=[max(-2.,min(2.,x)) for x in g]
per_tensor=[clip([x],2.)[0] for x in g]
assert coordinate==per_tensor==[2.,2.] and norm(coordinate)>2. and not near(coordinate,q)
# Projection optimality boundary: q is radial, and sampled feasible points have
# nonpositive dot product with the residual g-q relative to q.
for v in [[0.,0.],[2.,0.],[0.,2.],[-2.,0.],[0.,-2.],q]:
    assert sum((x-y)*(z-y) for x,y,z in zip(g,q,v))<=1e-12
sgd=[.1*x for x in q];assert math.isclose(norm(sgd),.2)
# Equal-probability scalar gradients can reverse expectation after clipping.
samples=[9.,-1.,-1.];mean=sum(samples)/3
clip_mean=clip([mean],1.)[0];mean_clip=sum(clip([x],1.)[0] for x in samples)/3
assert mean>0 and clip_mean==1. and mean_clip<0
# Stateful updates do not inherit the fresh-gradient cap.
fresh=clip([2.,0.],1.);momentum=[.9*x+y for x,y in zip(fresh,fresh)]
momentum_step=[.1*x for x in momentum];assert norm(momentum_step)>.1
small=clip([.003,.004],.01);adam_step=[.1*x/abs(x) for x in small]
assert norm(adam_step)>.1*.01
# Historical emergency replacement is not ordinary clipping.
rescue=[.02*x for x in [100.,0.]];assert norm(rescue)>1.
print(json.dumps(dict(joint_clip=q,coordinate_clip=coordinate,per_tensor_clip=per_tensor,
 sgd_step_norm=norm(sgd),raw_mean=mean,clip_of_mean=clip_mean,mean_of_clipped=mean_clip,
 momentum_step_norm=norm(momentum_step),fresh_sgd_cap=.1,
 ideal_adam_step=adam_step,ideal_adam_comparison_cap=.001,
 historical_rescue_gradient_norm=norm(rescue)),indent=2))
