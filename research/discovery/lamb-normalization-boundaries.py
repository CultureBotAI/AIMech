"""Constructed LAMB formula boundaries; no TensorFlow or training execution."""
import json
import math


def norm(v):
    return math.sqrt(sum(x*x for x in v))


def close(a,b):
    return all(math.isclose(x,y,rel_tol=1e-10,abs_tol=1e-12) for x,y in zip(a,b))


def moments(g,m,v,t,b1=.9,b2=.999,epsilon=0,correction=True):
    m1=[b1*x+(1-b1)*y for x,y in zip(m,g)]
    v1=[b2*x+(1-b2)*y*y for x,y in zip(v,g)]
    mh=[x/(1-b1**t) for x in m1] if correction else m1
    vh=[x/(1-b2**t) for x in v1] if correction else v1
    ratio=[a/(math.sqrt(z)+epsilon) for a,z in zip(mh,vh)]
    return m1,v1,ratio


def step(w,r,rate=.02,decay=0,phi=None,zero_fallback=False):
    u=[a+decay*x for a,x in zip(r,w)]
    wn=norm(w);un=norm(u)
    scale=wn if phi is None else phi(wn)
    if zero_fallback and (wn==0 or un==0):
        multiplier=1
    elif un==0:
        raise ZeroDivisionError('Paper block normalization has zero denominator.')
    else:
        multiplier=scale/un
    increment=[rate*multiplier*a for a in u]
    return dict(direction=u,multiplier=multiplier,increment=increment,norm=norm(increment))


w=[3.,4.];g=[1.,100.];z=[0.,0.]
m,v,r=moments(g,z,z,1)
assert close(r,[1.,1.])
basic=step(w,r)
raw_gradient=step(w,g)
assert math.isclose(basic['norm'],.1) and not close(basic['increment'],raw_gradient['increment'])
_,_,uncorrected=moments(g,z,z,1,correction=False)
assert close(basic['increment'],step(w,uncorrected)['increment'])
with_decay=[step(w,r,decay=.1),step(w,uncorrected,decay=.1)]
assert not close(with_decay[0]['increment'],with_decay[1]['increment'])
# Decay is outside the moments but inside block normalization.
separate_shrink=[a+.02*.1*x for a,x in zip(basic['increment'],w)]
assert not close(with_decay[0]['increment'],separate_shrink)
_,_,re=moments(g,z,z,1,epsilon=.1)
_,_,rue=moments(g,z,z,1,epsilon=.1,correction=False)
epsilon_steps=[step(w,re),step(w,rue)]
assert not close(epsilon_steps[0]['increment'],epsilon_steps[1]['increment'])
# Corrected moments are views of raw state, never fed back as EMA state.
g2=[4.,1.];m2,v2,r2=moments(g2,m,v,2)
wrong_m=[x/(1-.9) for x in m];wrong_v=[x/(1-.999) for x in v]
_,_,wrong_r2=moments(g2,wrong_m,wrong_v,2)
assert not close(step(w,r2)['increment'],step(w,wrong_r2)['increment'])
try:
    step([-1.,-1.],[1.,1.],decay=1)
except ZeroDivisionError:
    cancellation='undefined paper denominator'
else:
    raise AssertionError('Unspecified zero fallback introduced')
fallback=step([-1.,-1.],[1.,1.],decay=1,zero_fallback=True)
assert fallback['norm']==0
zero_weights=step(z,[1.,1.])
zero_fallback=step(z,[1.,1.],zero_fallback=True)
assert zero_weights['norm']==0 and zero_fallback['norm']>0
clipped=step([30.,40.],r,phi=lambda x:min(max(x,1),10))
assert math.isclose(clipped['norm'],.2)
_,_,sign_approx=moments([.01,1.],z,z,1,b1=0,b2=0,epsilon=.1)
assert not close(sign_approx,[1.,1.])
# A chosen partition changes the normalized direction and update allocation.
whole=step(w,[1.,2.])['increment']
split=[step([x],[a])['increment'][0] for x,a in zip(w,[1.,2.])]
assert not close(whole,split)
print(json.dumps(dict(first_step=basic,raw_gradient_normalization=raw_gradient,
    bias_correction_cancels_without_decay_or_epsilon=True,with_decay=with_decay,
    independent_shrinkage=separate_shrink,with_epsilon=epsilon_steps,
    second_raw_moment=m2,second_raw_second_moment=v2,
    second_correct_increment=step(w,r2)['increment'],second_overwritten_state_increment=step(w,wrong_r2)['increment'],
    cancellation=cancellation,implementation_zero_direction=fallback,
    zero_weight_paper_identity_phi=zero_weights,zero_weight_implementation_fallback=zero_fallback,
    clipped_phi=clipped,positive_epsilon_sign_approximation=sign_approx,
    partition_whole=whole,partition_split=split),indent=2))
