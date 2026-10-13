"""Constructed LARC clipping boundaries; no PyTorch or training execution."""
import json
import math


def norm(v):return math.sqrt(sum(x*x for x in v))

def near(a,b):return all(math.isclose(x,y,rel_tol=1e-10,abs_tol=1e-12) for x,y in zip(a,b))

def wrapper_gradient(w,g,gamma=.1,eta=.02,decay=0,epsilon=0,clip=True):
    wn=norm(w);gn=norm(g)
    if wn==0 or gn==0:
        return dict(gradient=list(g),fallback=True,local_rate=None,factor=1.)
    a=eta*wn/(gn+decay*wn+epsilon)
    factor=min(a/gamma,1.) if clip else a
    return dict(gradient=[factor*(x+decay*y) for x,y in zip(g,w)],fallback=False,local_rate=a,factor=factor)


def fresh(w,g,**kwargs):
    q=wrapper_gradient(w,g,**kwargs);gamma=kwargs.get('gamma',.1)
    q['step']=[gamma*x for x in q['gradient']];q['norm']=norm(q['step']);return q


w=[3.,4.]
small=fresh(w,[.03,.04]);large=fresh(w,[3.,4.]);scaling=fresh(w,[3.,4.],clip=False)
assert math.isclose(small['norm'],.005) and math.isclose(large['norm'],.1)
assert math.isclose(scaling['norm'],.01) and not near(large['step'],scaling['step'])
scaling_high=fresh(w,[3.,4.],gamma=10,clip=False)
assert scaling_high['norm']>.02*norm(w)
opposed=fresh(w,[-3.,-4.],decay=.2)
assert math.isclose(opposed['norm'],1/15) and opposed['norm']<=.02*norm(w)
# Changing the raw gradient scale changes the unclipped branch's fresh step.
small_twice=fresh(w,[.06,.08])
assert math.isclose(small_twice['norm'],2*small['norm'])
# Momentum keeps old contributions, so clipping a fresh gradient is not a full-step cap.
w1=[5.,0.];q1=fresh(w1,[1.,0.],gamma=.5);w2=[x-y for x,y in zip(w1,q1['step'])]
q2=wrapper_gradient(w2,[1.,0.],gamma=.5)
m2=[.9*x+y for x,y in zip(q1['gradient'],q2['gradient'])]
step2=[.5*x for x in m2]
assert norm(step2)>.02*norm(w2)
# Ideal first-step Adam cancels a positive block gradient multiplier.
q=wrapper_gradient(w,[3.,4.])
adam_step=[.1*x/abs(x) for x in q['gradient']]
assert near(adam_step,[.1,.1]) and norm(adam_step)>.02*norm(w)
zero_weight=fresh([0.,0.],[1.,0.]);zero_gradient=fresh(w,[0.,0.],decay=.2)
assert zero_weight['norm']>.02*0 and zero_gradient['norm']==0
# The wrapper skips decay with zero gradient, while direct decay would move weights.
assert not near(zero_gradient['step'],[.1*.2*x for x in w])
print(json.dumps(dict(small_gradient=small,large_gradient=large,scaling_mode=scaling,
 scaling_high_rate=scaling_high,opposed_decay=opposed,
 unclipped_branch_rescaling=small_twice,momentum_second_step=step2,
 momentum_current_weight_cap=.02*norm(w2),ideal_adam_first_step=adam_step,
 zero_weight_fallback=zero_weight,zero_gradient_skips_wrapper_decay=zero_gradient),indent=2))
