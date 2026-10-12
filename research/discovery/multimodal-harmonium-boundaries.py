#!/usr/bin/env python3
"""Curator probability checks; no historical implementation or benchmark run."""
import itertools
import json
import math


def logsumexp(values):
    peak=max(values)
    return peak+math.log(sum(math.exp(x-peak) for x in values))


def softplus(x):
    return max(x,0)+math.log1p(math.exp(-abs(x)))


def sigmoid(x):
    return 1/(1+math.exp(-x))


def rap():
    m=[2,1];a=[math.log(.6),math.log(.8)];beta=[.3,-.2]
    w=[[.2,-.3],[-.1,.25]]
    hs=list(itertools.product(*[range(n+1) for n in m]))
    def rates(h,aa,ww):
        return [math.exp(aa[i]+sum(ww[i][j]*h[j] for j in range(2))) for i in range(2)]
    def hidden_logmass(h,aa,bb,ww):
        return sum(math.log(math.comb(m[j],h[j]))-bb[j]*h[j] for j in range(2))+sum(rates(h,aa,ww))
    def logz(aa,bb,ww):
        return logsumexp([hidden_logmass(h,aa,bb,ww) for h in hs])
    def visible_logmass(x,aa,bb,ww):
        return sum(aa[i]*x[i]-math.lgamma(x[i]+1) for i in range(2))+sum(m[j]*softplus(sum(ww[i][j]*x[i] for i in range(2))-bb[j]) for j in range(2))
    z=logz(a,beta,w);conditional_error=0.;marginal_error=0.;checked=0
    for x in itertools.product(range(4),repeat=2):
        logs=[]
        for h in hs:
            logs.append(sum(a[i]*x[i]-math.lgamma(x[i]+1) for i in range(2))
                        +sum(math.log(math.comb(m[j],h[j]))-beta[j]*h[j] for j in range(2))
                        +sum(w[i][j]*x[i]*h[j] for i in range(2) for j in range(2)))
        v=logsumexp(logs);marginal_error=max(marginal_error,abs(v-visible_logmass(x,a,beta,w)))
        probs=[sigmoid(sum(w[i][j]*x[i] for i in range(2))-beta[j]) for j in range(2)]
        for h,lp in zip(hs,logs):
            expected=math.prod(math.comb(m[j],h[j])*probs[j]**h[j]*(1-probs[j])**(m[j]-h[j]) for j in range(2))
            conditional_error=max(conditional_error,abs(expected-math.exp(lp-v)));checked+=1
    # Integrating infinitely supported Poisson variables leaves a finite hidden sum.
    ph=[math.exp(hidden_logmass(h,a,beta,w)-z) for h in hs]
    assert abs(sum(ph)-1)<1e-12
    x=[2,1];j=0;i=1
    expected_xh=sum(p*rates(h,a,w)[i]*h[j] for p,h in zip(ph,hs))
    grad=x[i]*m[j]*sigmoid(sum(w[k][j]*x[k] for k in range(2))-beta[j])-expected_xh
    eps=1e-5;plus=[r[:] for r in w];minus=[r[:] for r in w];plus[i][j]+=eps;minus[i][j]-=eps
    finite=((visible_logmass(x,a,beta,plus)-logz(a,beta,plus))-(visible_logmass(x,a,beta,minus)-logz(a,beta,minus)))/(2*eps)
    # Complement h_0 -> M_0-h_0, adjusting the visible baseline.
    aa=[a[i]+m[0]*w[i][0] for i in range(2)];bb=[-beta[0],beta[1]];ww=[[-row[0],row[1]] for row in w]
    z2=logz(aa,bb,ww)
    complement_error=max(abs((visible_logmass(x,a,beta,w)-z)-(visible_logmass(x,aa,bb,ww)-z2)) for x in itertools.product(range(4),repeat=2))
    assert conditional_error<1e-12 and marginal_error<1e-12 and complement_error<1e-12 and abs(grad-finite)<1e-8
    return dict(hidden_states=len(hs),checked_hidden_probabilities=checked,conditional_error=conditional_error,marginal_error=marginal_error,exact_log_normalizer=z,gradient=grad,finite_difference=finite,complement_error=complement_error,normalization='Finite hidden sum after exact Poisson summation, without truncating visible support.')


def family_of_harmonium():
    # One binary word, one Gaussian image feature and one unit-Gaussian latent.
    def partition(alpha,beta,w,u):
        precision=1-u*u
        assert precision>0
        return math.sqrt(2*math.pi/precision)*sum(math.exp(alpha*x+.5*w*w*x*x+(beta+u*w*x)**2/(2*precision)) for x in [0,1])
    params=[(0.,0.,.2,.2),(0.,0.,1.,.6)]
    raw=[math.exp(.5*w*w) for alpha,beta,w,u in params] # observation x=1,z=0
    zs=[partition(*p) for p in params]
    proper=[v/z for v,z in zip(raw,zs)]
    assert raw[1]>raw[0] and proper[0]>proper[1]
    # An additive energy constant must cancel against that class's normalizer.
    c=4.
    assert abs(math.exp(c)*raw[0]/(math.exp(c)*zs[0])-proper[0])<1e-14
    return dict(class_unnormalized_scores=raw,class_normalizers=zs,class_densities=proper,raw_winner=1,proper_winner=0,gaussian_precision_condition='For identity variances, I-U U^T must be positive definite; equivalently every singular value of U is below one.')


def hierarchical_harmonium():
    # Given observed x,z with zero base projection: tau=0, v_1=v_2=1.
    states=list(itertools.product([0,1],repeat=2))
    weights=[math.exp(.5*sum(y)**2) for y in states]
    p=[v/sum(weights) for v in weights]
    marginals=[sum(q*y[j] for q,y in zip(p,states)) for j in range(2)]
    assert p[-1]>.5 and sum(marginals)>1
    # Restricting support to exactly one label changes the law.
    onehot=[q/sum(v for v,y in zip(p,states) if sum(y)==1) if sum(y)==1 else 0. for q,y in zip(p,states)]
    assert onehot==[0.,.5,.5,0.]
    h=1.;bernoulli_means=[sigmoid(h)]*2;onehot_given_h=[.5,.5]
    posterior_mean_h=sum(q*sum(y) for q,y in zip(p,states))
    plugin=sigmoid(posterior_mean_h)
    assert abs(plugin-marginals[0])>.01
    return dict(binary_label_states=states,joint_label_probabilities=p,label_marginals=marginals,onehot_restricted_probabilities=onehot,bernoulli_means_given_h_one=bernoulli_means,onehot_means_given_h_one=onehot_given_h,logistic_at_posterior_mean=plugin,exact_label_marginal=marginals[0],interpretation='One-hot training observations do not constrain the binary-cube joint; conditional Bernoulli logits differ from categorical softmax. Integrating a missing label layer yields Gaussian mixtures, not a single plug-in Gaussian.')


def dual_wing_boundary():
    # Even with image coupling absent, the stated Poisson/Gaussian construction
    # integrates h to q(n) proportional to exp(w^2*n^2/2)/n!.
    # For every w != 0, log q(n)=w^2*n^2/2-n*log(n)+O(n) -> +infinity.
    w=.2;ns=[100,1000,10000]
    terms=[.5*w*w*n*n-math.lgamma(n+1) for n in ns]
    assert terms[-1]>terms[-2]>0
    negative_w_terms=[.5*(-w)**2*n*n-math.lgamma(n+1) for n in ns]
    assert terms==negative_w_terms
    # General nonzero count row gives a positive quadratic coefficient ||w_i||^2/2
    # while image z is held in any bounded region. A changed bounded count support
    # would require truncated conditionals; binary observations alone are insufficient.
    return dict(counts=ns,log_integrated_terms=terms,negative_coupling_same_divergence=True,conclusion='The unbounded count/unit-Gaussian-hidden specialization is not jointly normalizable for a nonzero count coupling. A proper-support revision or clarification is needed before an asserted native probability-model record.',additional_display_note='Poisson base measure is 1/Gamma(n+1), not the printed 1/Gamma(n); correcting that factorial does not repair quadratic tail growth.')


if __name__=='__main__':
    print(json.dumps(dict(rap=rap(),family_of_harmonium=family_of_harmonium(),hierarchical_harmonium=hierarchical_harmonium(),dual_wing_boundary=dual_wing_boundary(),status='PASS'),indent=2))
