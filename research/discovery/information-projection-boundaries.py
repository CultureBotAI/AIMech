"""Finite curator checks for information-projection boundaries; not author software."""
import json, math

def kl(p,q):
    assert len(p)==len(q) and min(p)>=0 and min(q)>=0
    return sum(x*math.log(x/y) for x,y in zip(p,q) if x)

def close(a,b,tol=1e-12):
    assert abs(a-b)<tol,(a,b)

# The 1984 stopping bound integrates against P*: mass must be retained.
p1=(.48,.12,.08,.32);q0=(.4,.1,.1,.4);q1=(.448,.112,.088,.352)
for x in [p1,q0,q1]:close(sum(x),1)
gap=kl(p1,q1);ratio_bound=math.log(max(b/a for a,b in zip(q0,q1)))
assert 0<gap<ratio_bound
scaled_gap=kl([100*x for x in p1],[100*x for x in q1])
close(scaled_gap,100*gap)
assert scaled_gap>ratio_bound and scaled_gap<=100*ratio_bound
# Feasible optimum: component weights (2/3,1/3) produce target (.6,.4).
close((2/3)*.8+(1/3)*.2,.6)

# Convergence of Q does not force successive ratios to one at zero coordinates.
def q(n):
    t=(2 if n%2==0 else 1)/n
    return (.5,t,.5-t)
ratio_examples=[]
for n in [100,1000,10000]:
    old,new=q(n-1),q(n)
    close(kl((1,0,0),old),math.log(2));close(kl((1,0,0),new),math.log(2))
    r=max(y/x for x,y in zip(old,new));assert r>1.9
    ratio_examples.append([n,r])

# Closed convex finite-measure sets need not bound Q off support(P).
for n in [1,10,100]:close(kl((1,0),(1,n)),0)

# Weight-only EM: components remain fixed, zero starts can lock the wrong face.
mu=((.8,.2),(.2,.8));target=(.6,.4)
def em(w):
    density=[sum(w[i]*mu[i][y] for i in range(2)) for y in range(2)]
    new=[w[i]*sum(target[y]*mu[i][y]/density[y] for y in range(2)) for i in range(2)]
    close(sum(new),1)
    return new
w=[.5,.5];old=kl(target,(.5,.5))
for _ in range(1000):
    w=em(w);density=[sum(w[i]*mu[i][y] for i in range(2)) for y in range(2)]
    current=kl(target,density);assert current<=old+1e-14;old=current
close(w[0],2/3);close(old,0)
assert em([1,0])==[1,0]
# Identical components preserve every initial weight, disproving unique coefficients.
for c in [.2,.8]:
    same=(.6,.4)
    close(c*sum(target[y]*same[y]/same[y] for y in range(2)),c)

# Binary rate-distortion BA at fixed beta, not a solve at prescribed distortion.
beta=math.log(3);source=(.5,.5)
def rd_step(marg):
    channel=[]
    for x in range(2):
        row=[marg[y]*math.exp(-beta*(x!=y)) for y in range(2)]
        channel.append([v/sum(row) for v in row])
    nxt=[sum(source[x]*channel[x][y] for x in range(2)) for y in range(2)]
    distortion=sum(source[x]*channel[x][y]*(x!=y) for x in range(2) for y in range(2))
    info=sum(source[x]*channel[x][y]*math.log(channel[x][y]/nxt[y]) for x in range(2) for y in range(2) if channel[x][y])
    return nxt,channel,distortion,info,info+beta*distortion
marg=[.9,.1];prev=math.inf
for _ in range(1000):
    marg,channel,distortion,info,obj=rd_step(marg)
    assert obj<=prev+1e-14;prev=obj
close(marg[0],.5);close(distortion,.25);close(obj,math.log(1.5))
locked=rd_step([1,0]);assert locked[0]==[1,0] and locked[-1]>obj

# Capacity's positive log(reverse/input) is maximized; its KL recasting is negative.
entropy=lambda p:-sum(x*math.log(x) for x in p if x)
assert entropy((.5,.5))>entropy((1,0))
close(kl((.5,.5),(1,1)),-math.log(2))

# Moving singleton sets satisfy squared-distance C1/C2. Error summability is sufficient,
# not necessary: a_n=1/n or2/n converges, with occasional objective increases.
a=lambda n:(2 if n%2==0 else 1)/n
assert a(4)**2>a(3)**2
assert a(10000)**2<1e-7
# Constant D=0 permits oscillating exact minimizers even with fixed compact sets.
assert len(set(n%2 for n in range(10)))==2

# Niesen's weighted product-space squared norm minimizes squared distances;
# it does not minimize the unsquared distances printed in Eq22.
points=(0,4,4);mean=sum(points)/3;median=4
abs_cost=lambda z:sum(abs(z-x) for x in points)/3
square_cost=lambda z:sum((z-x)**2 for x in points)/3
assert abs_cost(mean)>abs_cost(median)
assert square_cost(mean)<square_cost(median)

print(json.dumps(dict(status='pass',finite_measure_stopping_bound=dict(probability_gap=gap,printed_bound=ratio_bound,mass100_gap=scaled_gap,corrected_bound=100*ratio_bound),vanishing_coordinate_ratios=ratio_examples,weight_em=dict(weights=w,divergence=old),binary_rate_distortion=dict(marginal=marg,channel=channel,distortion=distortion,mutual_information=info,objective=obj,zero_support_objective=locked[-1]),squared_vs_unsquared=dict(mean=mean,median=median,absolute_cost_at_mean=abs_cost(mean),absolute_cost_at_median=abs_cost(median))),indent=2))
