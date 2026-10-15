#!/usr/bin/env python3
"""Original small MES interpretation checks; not MES or author code.

Rational covariance and finite probability examples are exact. Normal/Gumbel
functions and entropy use Python floating math with explicit absolute tolerance.
The grid is a bounded numerical check, not a proof of global monotonicity or of
the published regret theorem. Provenance/timestamps live in an external receipt.
"""
from fractions import Fraction as F
from math import erf, erfc, exp, log, pi, sqrt, isclose
import json


def phi(x):
    return exp(-x*x/2)/sqrt(2*pi)


def Phi(x):
    return erfc(-x/sqrt(2))/2


def score(gamma):
    c=Phi(gamma)
    return gamma*phi(gamma)/(2*c)-log(c)


def determinant3(k):
    return (k[0][0]*(k[1][1]*k[2][2]-k[1][2]*k[2][1])
            -k[0][1]*(k[1][0]*k[2][2]-k[1][2]*k[2][0])
            +k[0][2]*(k[1][0]*k[2][1]-k[1][1]*k[2][0]))


def main():
    gammas=[i/20 for i in range(-100,101)]
    scores=[score(x) for x in gammas]
    assert all(a>b for a,b in zip(scores,scores[1:]))
    assert all(x>0 for x in scores)
    assert isclose(score(0),log(2),rel_tol=0,abs_tol=2e-14)
    # The Gaussian covariance below is positive definite, with positive entries.
    k=[[F(1),F(1,5),F(7,10)],
       [F(1,5),F(1),F(7,10)],
       [F(7,10),F(7,10),F(1)]]
    minors=[k[0][0],k[0][0]*k[1][1]-k[0][1]**2,determinant3(k)]
    assert minors==[F(1),F(24,25),F(22,125)]
    post=[[k[i][j]-k[i][2]*k[2][j]/k[2][2] for j in range(2)] for i in range(2)]
    assert post==[[F(51,100),-F(29,100)],[-F(29,100),F(51,100)]]
    # Prior independence of additive components is lost after observing a sum.
    additive_cov=-F(1,3)
    additive_var=F(2,3)
    assert F(0)-F(1)*F(1)/F(3)==additive_cov
    assert F(1)-F(1)*F(1)/F(3)==additive_var
    # Exact conditional law for two iid standard normals and their maximum M:
    # F1|M=m is 1/2 delta_m + 1/2 Normal(0,1) truncated below m.
    trunc_mean=-sqrt(2/pi)
    maximum_conditioned_mean=trunc_mean/2
    assert maximum_conditioned_mean!=trunc_mean
    # One-point domain: latent M=F~N(0,1), independent observation noise N(0,1).
    # Actual I(M;Y)=1/2 log(2); Y|M=0 has variance1 and P(Y>M)=1/2.
    noisy_mi=log(2)/2
    assert noisy_mi!=score(0)
    # Percentile-matched Gumbel for the maximum of one standard normal.
    # Quantile bisection is our own deterministic finite algorithm.
    def quantile(r):
        lo,hi=-10.0,10.0
        for _ in range(80):
            mid=(lo+hi)/2
            if Phi(mid)<r:lo=mid
            else:hi=mid
        return (lo+hi)/2
    r1,r2=.25,.75
    q1,q2=quantile(r1),quantile(r2)
    l1,l2=log(-log(r1)),log(-log(r2))
    b=(q2-q1)/(l1-l2);a=q1+b*l1
    G=lambda x:exp(-exp(-(x-a)/b))
    assert b>0
    assert isclose(G(q1),r1,rel_tol=0,abs_tol=2e-14)
    assert isclose(G(q2),r2,rel_tol=0,abs_tol=2e-14)
    assert G(0)>Phi(0) and G(2)<Phi(2)
    # Two finite distributions of functions, all support weights exactly1/2.
    laws=[[(2,0),(3,1)],[(1,0),(0,1)]]
    target_examples=[]
    for functions in laws:
        maximum=[max(x) for x in functions]
        location=[x.index(max(x)) for x in functions]
        observation=[x[0] for x in functions]
        assert len(set(observation))==2
        target_examples.append({'functions':functions,'weights':[F(1,2),F(1,2)],
            'max_value_information_nats':log(2) if len(set(maximum))==2 else 0,
            'max_location_information_nats':log(2) if len(set(location))==2 else 0})
    # The stated normalized random-feature map approximates k(0)=1.
    # A nonunit stationary kernel requires its spectral mass/amplitude factor.
    spectral_mass=F(4)
    normalized_feature_expected_diagonal=F(1)
    assert spectral_mass!=normalized_feature_expected_diagonal
    result={
        'role':'Supporting same-author curator boundary calculations, not independent scientific approval.',
        'score_grid':{'gamma_interval':[-5,5],'points':len(gammas),'strict_adjacent_decreases':len(gammas)-1,'minimum_score':min(scores),'maximum_score':max(scores),'score_zero':score(0),'scope':'Finite grid only, no universal monotonicity proof.'},
        'positive_prior_negative_posterior':{'prior':k,'leading_principal_minors':minors,'observe':'Third latent value exactly, a Gaussian conditional covariance calculation.','posterior_first_two':post,'scope':'Nonnegative prior covariance does not imply the nonnegative posterior covariance required by the source Slepian comparison.'},
        'local_truncation_not_max_conditioning':{'construction':'F1,F2 iid N(0,1), M=max(F1,F2), condition M=0 by the usual conditional density in M.','conditional_atom_at_zero':F(1,2),'conditional_truncated_component_weight':F(1,2),'mean_if_only_F1_below_zero':trunc_mean,'mean_given_global_maximum_zero':maximum_conditioned_mean,'scope':'Analytic exchangeability/order-statistic identity; floating numbers evaluate its closed-form means, not a simulated GP.'},
        'noise_boundary':{'construction':'One-point compact domain, latent F~N(0,1), M=F, Y=F+epsilon with epsilon~N(0,1) independent.','true_predictive_variance':2,'latent_variance_used_by_eq6':1,'conditional_Y_variance_at_M_zero':1,'conditional_probability_Y_above_M':F(1,2),'true_mutual_information_nats':noisy_mi,'eq6_term_at_sampled_maximum_zero':score(0),'scope':'The pointwise comparison diagnoses the local/noise approximation; it is not a numerical estimate of the full expected MES score.'},
        'gumbel_approximation_not_exact_or_order_preserving':{'target':'One standard normal, also the maximum over a singleton.','percentiles':[r1,r2],'quantiles':[q1,q2],'a':a,'b':b,'cdf_at_zero':{'normal':Phi(0),'gumbel':G(0)},'cdf_at_minus_two':{'normal':Phi(-2),'gumbel':G(-2)},'cdf_at_plus_two':{'normal':Phi(2),'gumbel':G(2)},'scope':'The fitted CDF crosses the exact independent maximum CDF; percentile matching does not automatically preserve stochastic domination.'},
        'value_location_information_distinction':target_examples,
        'additive_prior_independence_boundary':{'construction':'F1,F2,epsilon independent N(0,1), observe Y=F1+F2+epsilon.','posterior_variance_each':additive_var,'posterior_cross_covariance':additive_cov,'scope':'Contextual additive-extension caveat, not an add-MES implementation.'},
        'spectral_normalization_boundary':{'kernel':'k(h)=4 exp(-h^2/2)','spectral_mass':spectral_mass,'expected_feature_diagonal_without_amplitude':normalized_feature_expected_diagonal,'required_feature_amplitude':2},
        'numerics':'Float normal/Gumbel functions and natural logarithms; isclose uses rel_tol=0 and abs_tol=2e-14. Rational matrix and probability computations are exact.',
        'limits':['No author code, random-feature sampling, Gaussian-process fit, acquisition optimization or benchmark executed.','No verification of the general MES regret theorem, additive convergence or universal practical runtime.','The positive-variance score is undefined at zero posterior standard deviation without an additional policy.']}
    def serial(v):
        if isinstance(v,F):return str(v)
        if isinstance(v,dict):return {k:serial(x) for k,x in v.items()}
        if isinstance(v,(list,tuple)):return [serial(x) for x in v]
        return v
    print(json.dumps(serial(result),indent=2,sort_keys=True))


if __name__=='__main__':
    main()
