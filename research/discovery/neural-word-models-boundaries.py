"""Original finite curator checks, not author software or trained models."""
import math
import json

def close(a,b,tol=1e-7):
    assert abs(a-b)<tol,(a,b)
def sig(x):return 1/(1+math.exp(-x))
def diff(f,x,e=1e-5):return (f(x+e)-f(x-e))/(2*e)

# Conditional FRBM: one output word, one hidden bit, fixed context.
def frbm(hidden_bias=math.log(2),output_weight=math.log(3),word_bias=math.log(2)):
    state={(word,h):math.exp(word*word_bias+h*(hidden_bias+word*output_weight)) for word in [0,1] for h in [0,1]}
    z=sum(state.values())
    return {k:v/z for k,v in state.items()}
p=frbm();word_a=p[1,0]+p[1,1]
close(word_a,14/17)
close(p[1,1]/word_a,6/7)
model_h=sum(h*q for (w,h),q in p.items())
gradient_hidden=6/7-model_h
gradient_output=6/7-p[1,1]
def log_a(**kwargs):
    q=frbm(**kwargs);return math.log(q[1,0]+q[1,1])
close(gradient_hidden,diff(lambda v:log_a(hidden_bias=v),math.log(2)))
close(gradient_output,diff(lambda v:log_a(output_weight=v),math.log(3)))
wrong_bias=(7/2)/(7/2+3)
close(wrong_bias,7/13)
assert abs(word_a-wrong_bias)>0.2
one_step=(6/7)*(6/7)+(1/7)*(2/3)
close(one_step,122/147)
assert abs(one_step-word_a)>0.001
mean_hidden_reconstruction=sig(math.log(2)+(6/7)*math.log(3))
assert abs(mean_hidden_reconstruction-one_step)>0.001

# Temporal extension: exact uncertain-previous-state mixture vs substitution.
q0=frbm(hidden_bias=0,output_weight=math.log(3),word_bias=0)
q1=frbm(hidden_bias=math.log(4),output_weight=math.log(3),word_bias=0)
mix={k:(q0[k]+q1[k])/2 for k in q0}
exact_a=mix[1,0]+mix[1,1]
exact_h=mix[1,1]/exact_a
plug=frbm(hidden_bias=math.log(2),output_weight=math.log(3),word_bias=0)
plug_a=plug[1,0]+plug[1,1];plug_h=plug[1,1]/plug_a
close(exact_a,25/36);close(exact_h,21/25)
close(plug_a,7/10);close(plug_h,6/7)
assert abs(exact_h-plug_h)>0.01
smoothed_previous=(q1[1,0]+q1[1,1])/2/exact_a
close(smoothed_previous,13/25)
assert abs(smoothed_previous-0.5)>0.01

# Bengio NPLM: shared input lookup, independent output parameters, optional W.
embedding=[0.3,-0.2];context=[0,0];target=1
H=[0.7,-0.4];U=[0.8,-0.6];W=[[0.2,-0.1],[-0.3,0.5]];b=[0.05,-0.1];d=0.1
def nplm(c, direct=True, ctx=context):
    x=[c[i] for i in ctx];hidden=math.tanh(d+sum(v*w for v,w in zip(x,H)))
    logits=[bias+u*hidden+(sum(v*w for v,w in zip(x,row)) if direct else 0) for bias,u,row in zip(b,U,W)]
    ex=[math.exp(v) for v in logits];return [v/sum(ex) for v in ex],hidden
prob,hidden=nplm(embedding)
delta=[prob[j]-(j==target) for j in range(2)]
gx=[sum(delta[j]*(W[j][i]+U[j]*(1-hidden**2)*H[i]) for j in range(2)) for i in range(2)]
def loss(value,k):
    c=embedding.copy();c[k]=value;return -math.log(nplm(c)[0][target])
close(sum(gx),diff(lambda v:loss(v,0),embedding[0]))
close(0,diff(lambda v:loss(v,1),embedding[1]))
assert abs(prob[1]-nplm(embedding,False)[0][1])>0.001
assert abs(nplm(embedding,ctx=[0,1])[0][1]-nplm(embedding,ctx=[1,0])[0][1])>0.01
close(sum(prob),1)
print(json.dumps(dict(frbm=dict(word_a_probability=word_a,wrong_printed_bias_probability=wrong_bias,hidden_bias_gradient=gradient_hidden,output_weight_gradient=gradient_output,one_gibbs_step_a_probability=one_step,mean_hidden_reconstruction_a=mean_hidden_reconstruction),temporal=dict(exact_word_a_probability=exact_a,plug_in_word_a_probability=plug_a,exact_current_hidden_posterior=exact_h,plug_in_hidden_posterior=plug_h,previous_hidden_posterior_after_current_word=smoothed_previous),nplm=dict(probabilities=prob,shared_input_embedding_gradient=sum(gx),unused_input_embedding_likelihood_gradient=0,independent_output_bias_gradient=delta[1],optional_direct_and_order_checks=True),scope='Finite conditional models and derivative checks only; no author-code or empirical certification.'),indent=2))
