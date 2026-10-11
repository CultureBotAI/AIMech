"""Original finite arithmetic checks; no training or author-code execution."""
import json
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def model(t):
    w, b, c = t
    q = [math.exp(b*v)*(1+math.exp(c+w*v)) for v in (0, 1)]
    return [x/sum(q) for x in q]

def kernel(t):
    w, b, c = t
    rows = []
    for v in (0, 1):
        h = sigmoid(c+w*v)
        q = (1-h)*sigmoid(b)+h*sigmoid(b+w)
        rows.append([1-q, q])
    return rows

def step(q, t):
    k = kernel(t)
    return [sum(q[v]*k[v][z] for v in (0, 1)) for z in (0, 1)]

def stats(q, t):
    w, _, c = t
    return [q[1]*sigmoid(c+w), q[1], sum(q[v]*sigmoid(c+w*v) for v in (0, 1))]

def sub(a, b):
    return [x-y for x, y in zip(a, b)]

def cd(t, k=1):
    q = [1., 0.]
    for _ in range(k):
        q = step(q, t)
    return sub(stats([1., 0.], t), stats(q, t))

def kl(p, q):
    return sum(a*math.log(a/b) for a,b in zip(p,q) if a)

def objective(t):
    p = model(t)
    return kl([1.,0.],p)-kl(step([1.,0.],t),p)

def derivative(fn, t, i, eps=1e-5):
    a, b = t[:], t[:]
    a[i] += eps
    b[i] -= eps
    return (fn(a)-fn(b))/(2*eps)

t = [1.,0.,0.]
u = cd(t)
ml = sub(stats([1.,0.],t),stats(model(t),t))
formal = [-derivative(objective,t,i) for i in range(3)]
curl = derivative(lambda x:cd(x)[1],t,0)-derivative(lambda x:cd(x)[0],t,1)
e = math.e
printed = e*(e-1)*(e+3)/(8*(e+1)**3)
assert abs(curl)>1e-3
assert abs(curl-printed)<1e-9
assert max(abs(x-y) for x,y in zip(u,ml))>1e-3
assert max(abs(x-y) for x,y in zip(u,formal))>1e-3
assert objective(t)>=0
assert max(abs(x-y) for x,y in zip(step(model(t),t),model(t)))<1e-14
assert max(abs(x-y) for x,y in zip(cd(t,100),ml))<1e-13

# Carry a distribution through two different transition kernels; no optimizer.
t2 = [1.4,-.3,.2]
first = step([1.,0.],t)
persistent_next = step(first,t2)
restart_next = step([1.,0.],t2)
assert abs(persistent_next[1]-restart_next[1])>1e-3
fixed_r = [.8,.2]
frozen_diff = sub(stats([1.,0.],t),stats(fixed_r,t))
frozen_objective = lambda x:kl([1.,0.],model(x))-kl(fixed_r,model(x))
frozen_fd = [-derivative(frozen_objective,t,i) for i in range(3)]
assert max(abs(x-y) for x,y in zip(frozen_diff,frozen_fd))<1e-9

fast = [.6,-.2,.3]
effective = [x+y for x,y in zip(t,fast)]
g = sub(stats([1.,0.],t),stats([0.,1.],effective))
regular_new = [x+.01*d for x,d in zip(t,g)]
fast_new = [.95*x+.1*d for x,d in zip(fast,g)]
base_probability = model(t)[1]
overlay_probability = model(effective)[1]
assert abs(base_probability-overlay_probability)>1e-3
q = sigmoid(effective[2]+effective[0])
exact_visible_next = (1-q)*sigmoid(effective[1])+q*sigmoid(effective[1]+effective[0])
mean_hidden_plug_in = sigmoid(effective[1]+effective[0]*q)
assert abs(exact_visible_next-mean_hidden_plug_in)>1e-3

print(json.dumps(dict(
    setting='One binary visible and one binary hidden; theta=(w,b_visible,b_hidden); data visible=0; exact state enumeration.',
    cd1_update=u, likelihood_gradient=ml, negative_formal_cd_gradient=formal,
    cd_objective=objective(t), cross_partial_difference=curl,
    source_equation10_value=printed, source_equation10_difference=curl-printed,
    stationary_visible_probability=model(t)[1],
    cd100_likelihood_error=max(abs(x-y) for x,y in zip(cd(t,100),ml)),
    persistent_next=persistent_next, restarted_next=restart_next,
    frozen_distribution_gradient_error=max(abs(x-y) for x,y in zip(frozen_diff,frozen_fd)),
    fast_overlay=dict(regular=t,fast=fast,effective=effective,update=g,
        regular_new=regular_new,fast_new=fast_new,
        base_visible_probability=base_probability,overlay_visible_probability=overlay_probability,
        exact_gibbs_visible_probability=exact_visible_next,mean_hidden_plug_in=mean_hidden_plug_in),
    limitation='Finite mathematical witnesses only; no general convergence, mixing-speed, implementation or empirical-performance certification.'
),indent=2))
