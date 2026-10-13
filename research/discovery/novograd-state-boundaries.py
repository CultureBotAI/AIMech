"""Constructed NovoGrad algebra; no TensorFlow or model execution."""
import math
import json


def norm(v):
    return math.sqrt(sum(a*a for a in v))


def near(a,b):
    return all(math.isclose(x,y,rel_tol=1e-10,abs_tol=1e-12) for x,y in zip(a,b))


def update(w,g,m,previous_v,rate=.1,beta1=.9,beta2=.25,epsilon=0,decay=0,first=False,average=False):
    v=norm(g)**2 if first else beta2*previous_v+(1-beta2)*norm(g)**2
    normalized=[x/(math.sqrt(v)+epsilon) for x in g]
    q=[a+decay*x for a,x in zip(normalized,w)]
    if average and not first:
        q=[(1-beta1)*x for x in q]
    new_m=[beta1*a+x for a,x in zip(m,q)]
    step=[rate*x for x in new_m]
    return dict(v=v,normalized=normalized,m=new_m,step=step,w=[x-y for x,y in zip(w,step)])


z=[0.,0.];w=[3.,4.]
a=update(w,[1.,0.],z,0,first=True)
b=update(a['w'],[0.,2.],a['m'],a['v'])
assert a['v']==1 and math.isclose(b['v'],3.25)
normalize_after=[x/math.sqrt(b['v']) for x in [.9,2.]]
assert not near(normalize_after,b['m'])
# Scale an entire prescribed gradient history by a common positive factor.
ascaled=update(w,[3.,0.],z,0,first=True)
bscaled=update(ascaled['w'],[0.,6.],ascaled['m'],ascaled['v'])
assert near(a['step'],ascaled['step']) and near(b['step'],bscaled['step'])
assert norm(b['normalized'])<=1/math.sqrt(1-.25)
assert norm(b['m'])>1/math.sqrt(1-.25)
# With beta2=0, epsilon changes pure unit normalization.
q=update(w,[.01,0.],z,0,beta1=0,beta2=0,epsilon=.1)
assert math.isclose(norm(q['normalized']),1/11)
try:
    update(w,z,z,0,first=True)
except ZeroDivisionError:
    first_zero='undefined without numerical offset'
else:
    raise AssertionError('Unexpected zero-denominator fallback')
zero_offset=update(w,z,z,0,first=True,epsilon=1e-7,decay=.1)
assert near(zero_offset['step'],[.03,.04])
# Decay inside momentum accumulates past shrinkage, unlike direct shrinkage.
def decay_pair():
    g=[1.,0.];d=.1
    inside1=update(w,g,z,0,first=True,decay=d)
    inside2=update(inside1['w'],g,inside1['m'],inside1['v'],decay=d)
    plain1=update(w,g,z,0,first=True)
    outside_w1=[x-s-.1*d*x for x,s in zip(w,plain1['step'])]
    plain2=update(outside_w1,g,plain1['m'],plain1['v'])
    outside2=[s+.1*d*x for s,x in zip(plain2['step'],outside_w1)]
    assert near(inside1['w'],outside_w1) and not near(inside2['step'],outside2)
    return dict(inside=inside2['step'],outside=outside2)
# Paper current-rate-outside momentum versus documented Keras velocity.
q1=[1.,0.];q2=[0.,1.];rates=[.1,.01];beta=.9
paper_m2=[beta*x+y for x,y in zip(q1,q2)]
paper2=[rates[1]*x for x in paper_m2]
keras2=[beta*rates[0]*x+rates[1]*y for x,y in zip(q1,q2)]
assert not near(paper2,keras2)
constant2=[beta*rates[0]*x+rates[0]*y for x,y in zip(q1,q2)]
assert near([rates[0]*x for x in paper_m2],constant2)
# Gradient averaging differs unless state/rate conventions are aligned.
avg2=update(a['w'],[0.,2.],a['m'],a['v'],average=True)
assert not near(avg2['step'],b['step'])
# A scalar running maximum alone does not control an increasing global rate.
vmax=[4.,4.];schedule=[.1,.2];effective=[r/math.sqrt(v) for r,v in zip(schedule,vmax)]
assert effective[1]>effective[0]
# Storage is optimizer moment elements, not total training memory.
n=1000000;layers=100;ratio=(n+layers)/(2*n)
assert ratio>.5 and math.isclose(ratio,.50005)
print(json.dumps(dict(first=a,second=b,normalize_after_momentum=normalize_after,
 positive_history_rescaling_invariant_in_ideal_case=True,
 fresh_norm=norm(b['normalized']),fresh_bound=1/math.sqrt(1-.25),momentum_norm=norm(b['m']),
 positive_epsilon_beta2_zero=q['normalized'],first_zero=first_zero,positive_epsilon_zero_gradient=zero_offset,
 decay_placement=decay_pair(),scheduled_rate_paper=paper2,scheduled_rate_keras=keras2,
 gradient_averaging_second_step=avg2['step'],increasing_rate_with_running_max=effective,
 moment_state_ratio=ratio,one_scalar_per_coordinate_ratio=1.0),indent=2))
