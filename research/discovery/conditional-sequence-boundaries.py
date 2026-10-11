"""Original finite curator calculations, independent of author implementations."""
from itertools import product
from math import exp, log
from copy import deepcopy
import json

def sigmoid(x): return 1/(1+exp(-x))
def close(a,b): assert abs(a-b)<2e-8,(a,b)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
vectors=list(product((0,1),repeat=2))

def rbm(a,c,w,v):
    masses={x:exp(dot(a,x))*(1+exp(c+dot(w,x))) for x in vectors}
    z=sum(masses.values());q={x:m/z for x,m in masses.items()}
    hd=sigmoid(c+dot(w,v))
    ga=[sum(q[x]*x[i] for x in vectors)-v[i] for i in range(2)]
    gc=sum(q[x]*sigmoid(c+dot(w,x)) for x in vectors)-hd
    gw=[sum(q[x]*x[i]*sigmoid(c+dot(w,x)) for x in vectors)-v[i]*hd for i in range(2)]
    return -log(q[tuple(v)]),ga,gc,gw,[0.,0.],q

def nade(a,c,w,out,v):
    loss=0.;ga=[];gc=0.;gw=[0.,0.];go=[];pre=c
    for i in range(2):
        h=sigmoid(pre);p=sigmoid(a[i]+out[i]*h);delta=p-v[i]
        loss-=log(p if v[i] else 1-p);ga.append(delta);go.append(delta*h)
        d=delta*out[i]*h*(1-h);gc+=d
        for j in range(i):gw[j]+=d*v[j]
        pre+=w[i]*v[i]
    return loss,ga,gc,gw,go,None

# Recurrent width two, output hidden width one: distinct parameter dimensions.
theta=dict(w=[.8,-.5],out=[.6,-.7],bv=[.2,-.1],bh=[-.3],
           uv=[[.4,-.2],[-.1,.3]],uh=[.5,.1],
           f=[[.7,-.3],[.2,.6]],b=[[.1,.8],[-.4,.2]],c=[-.1,.2],r0=[.25,.6])
def zero(x):return [zero(y) for y in x] if isinstance(x,list) else 0.
def evaluate(p,seq,kind,with_grad=False):
    r=p['r0'][:];saved=[];total=0.
    for v in seq:
        a=[p['bv'][i]+dot(p['uv'][i],r) for i in range(2)]
        c=p['bh'][0]+dot(p['uh'],r)
        loc=rbm(a,c,p['w'],v) if kind=='rbm' else nade(a,c,p['w'],p['out'],v)
        rt=[sigmoid(p['c'][i]+dot(p['f'][i],v)+dot(p['b'][i],r)) for i in range(2)]
        total+=loc[0];saved.append((v,r,rt,loc));r=rt
    if not with_grad:return total
    g={k:zero(v) for k,v in p.items()};lam=[0.,0.]
    for v,prev,r,loc in reversed(saved):
        _,ga,gc,gw,go,_=loc;delta=[lam[i]*r[i]*(1-r[i]) for i in range(2)]
        g['bh'][0]+=gc
        for i in range(2):
            g['w'][i]+=gw[i];g['out'][i]+=go[i];g['bv'][i]+=ga[i]
            g['uh'][i]+=gc*prev[i];g['c'][i]+=delta[i]
            for j in range(2):
                g['uv'][i][j]+=ga[i]*prev[j]
                g['f'][i][j]+=delta[i]*v[j];g['b'][i][j]+=delta[i]*prev[j]
        lam=[sum(p['uv'][i][j]*ga[i]+p['b'][i][j]*delta[i] for i in range(2))+p['uh'][j]*gc for j in range(2)]
    g['r0']=lam
    return total,g

def coordinates(p):
    for k,v in p.items():
        for i,x in enumerate(v):
            if isinstance(x,list):
                for j in range(len(x)):yield k,i,j
            else:yield k,i
def get(p,key):
    for k in key:p=p[k]
    return p
def perturb(p,key,amount):
    q=deepcopy(p);ref=q
    for k in key[:-1]:ref=ref[k]
    ref[key[-1]]+=amount;return q

seq=[(1,0),(0,1),(1,1)];epsilon=1e-5;results={}
for kind in ['rbm','nade']:
    loss,g=evaluate(theta,seq,kind,True);largest=0.
    for key in coordinates(theta):
        fd=(evaluate(perturb(theta,key,epsilon),seq,kind)-evaluate(perturb(theta,key,-epsilon),seq,kind))/(2*epsilon)
        close(fd,get(g,key));largest=max(largest,abs(fd-get(g,key)))
    total=sum(exp(-evaluate(theta,s,kind)) for s in product(vectors,repeat=3));close(total,1)
    results[kind]=dict(nll=loss,normalized_sequence_mass=total,maximum_gradient_error=largest,recurrent_matrix_gradient=g['b'],initial_state_gradient=g['r0'],output_hidden_input_gradient=g['w'])
close(results['nade']['output_hidden_input_gradient'][1],0)
assert abs(results['rbm']['output_hidden_input_gradient'][1])>.01
assert results['rbm']['nll']!=results['nade']['nll']

# Static conditional RBM: distinct conditioning inputs change distributions,
# while the input marginal is unspecified. Output bits need not be independent.
def conditional(u):
    a=[.2+.4*u,-.1-.3*u];c=-.3+.5*u
    return rbm(a,c,[.8,-.5],(1,0))[-1]
q0,q1=conditional(0),conditional(1)
close(sum(q0.values()),1);close(sum(q1.values()),1)
assert q0!=q1
p1=sum(p for v,p in q1.items() if v[0]);p2=sum(p for v,p in q1.items() if v[1])
cov=q1[1,1]-p1*p2;assert abs(cov)>.001
posterior=sigmoid(-.3+.5+.8)
negative_bias_posterior=sigmoid(-(-.3+.5)+.8)
negative_all_posterior=sigmoid(-(-.3+.5)-.8)
assert posterior!=negative_bias_posterior and posterior!=negative_all_posterior
results['conditional_rbm']=dict(probabilities_u0={str(k):v for k,v in q0.items()},probabilities_u1={str(k):v for k,v in q1.items()},conditional_output_covariance=cov,positive_sign_hidden_posterior=posterior,negative_bias_hidden_posterior=negative_bias_posterior,negative_all_hidden_posterior=negative_all_posterior)
print(json.dumps(results,indent=2))
