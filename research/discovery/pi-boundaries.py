#!/usr/bin/env python3
"""Original bounded PI diagnostics; standard library, deterministic stdout only.

Sources inspected separately: Jones2001 Eq27 (inclusive event) and Eqs28–32;
Snoek2012 Eqs1–2 and6; Wang2017 Eq6/Lemma3.1 for the scoped MES comparison.
These examples are not a Gaussian-process implementation, optimizer, numerical
production-tail implementation, benchmark, or general convergence proof.
Exact Fraction arithmetic and binary64 Gaussian/entropy functions are separated.
"""
from fractions import Fraction as F
from itertools import product
import json
import math

ABS_TOL = 2e-13


def close(a, b):
    assert math.isclose(a, b, rel_tol=0, abs_tol=ABS_TOL), (a, b)


def cdf(z):
    return 0.5 * math.erfc(-z / math.sqrt(2))


def density(z):
    return math.exp(-z*z/2) / math.sqrt(2*math.pi)


def probability(mu, sigma, target, *, minimize=True, inclusive=False):
    assert all(math.isfinite(x) for x in (mu, sigma, target)) and sigma >= 0
    if sigma == 0:
        if minimize:
            return float(mu <= target if inclusive else mu < target)
        return float(mu >= target if inclusive else mu > target)
    z = (target-mu)/sigma if minimize else (mu-target)/sigma
    return cdf(z)


def ei_min(mu, sigma, incumbent):
    if sigma == 0:
        return max(incumbent-mu, 0)
    assert sigma > 0
    z = (incumbent-mu)/sigma
    return (incumbent-mu)*cdf(z) + sigma*density(z)


def mes_score(gamma):
    # Local truncated-latent Eq6 score, only evaluated at moderate finite gaps.
    return gamma*density(gamma)/(2*cdf(gamma)) - math.log(cdf(gamma))


def finite_event(rows, inclusive=False):
    # rows are (incumbent, candidate, exact probability).
    assert sum(p for _, _, p in rows) == 1
    return sum((p for b, y, p in rows if y <= b if inclusive), F(0)) if inclusive else sum((p for b, y, p in rows if y < b), F(0))


def main():
    out = {}
    grid = list(product([-1, -.5, 0, .5, 1], [.25, 1, 2], [-.5, 0, .5]))
    for mu, sigma, threshold in grid:
        close(probability(mu, sigma, threshold), probability(-mu, sigma, -threshold, minimize=False))
        close(probability(mu, sigma, threshold), probability(mu, sigma, threshold, inclusive=True))
        close(probability(mu, sigma, threshold) + probability(mu, sigma, threshold, minimize=False), 1)
    margins = [probability(.2, .5, 0-xi) for xi in [0, .1, .5]]
    assert margins[0] > margins[1] > margins[2]
    out['sign_and_margin'] = dict(grid_cases=len(grid), minimization='P(Y<T)=Phi((T-mu)/sigma) for sigma>0',
        maximization='P(Y>T)=Phi((mu-T)/sigma) for sigma>0',
        minimization_margin='T=b-xi; xi>=0 means at least xi improvement, with event convention stated',
        incumbent=0, mu=.2, sigma=.5, margins=[0,.1,.5], probabilities=margins)

    zeros=[]
    for mu, minimize, inclusive in product([-1,0,1],[True,False],[False,True]):
        got=probability(mu,0,0,minimize=minimize,inclusive=inclusive)
        expected=(mu<=0 if inclusive else mu<0) if minimize else (mu>=0 if inclusive else mu>0)
        assert got == int(expected)
        zeros.append(dict(mu=mu,minimize=minimize,inclusive=inclusive,probability=got))
    for sigma in [1,.1,.001,1e-9]:close(probability(0,sigma,0),.5)
    out['zero_variance'] = dict(exact_point_mass_cases=zeros,positive_sigma_tie_value=.5,
        strict_point_mass_tie=0,inclusive_point_mass_tie=1,
        qualification='The sigma-down-to-zero value at mu=T is .5, whereas the exact point-mass event is0 or1. Dividing by zero or assigning zero universally does not define the event.')

    candidates=[dict(name='A',mu=-.1,sigma=.1),dict(name='B',mu=.1,sigma=1)]
    scores=[]
    for c in candidates:
        scores.append(dict(**c,pi=probability(c['mu'],c['sigma'],0),ei=ei_min(c['mu'],c['sigma'],0)))
    assert scores[0]['pi']>scores[1]['pi'] and scores[0]['ei']<scores[1]['ei']
    out['pi_versus_ei'] = dict(incumbent=0,threshold=0,candidates=scores,
        interpretation='PI prefers A; EI prefers B. Probability of improvement and expected amount are distinct at the same incumbent.')
    crossover=F(-11,90)
    assert (crossover+F(1,10))/F(1,10)==(crossover-F(1,10))
    lower=[probability(c['mu'],c['sigma'],-.5) for c in candidates]
    assert lower[0]<lower[1]
    out['threshold_sensitivity'] = dict(thresholds=[0,-.5],pi_at_lower_threshold=lower,
        exact_equal_standardized_gap_target=str(crossover),
        qualification='Lower target reverses this two-candidate ranking; no universal spatial/global-search behavior follows.')

    varrows=[]
    for mu in [-1,0,1]:
        values=[probability(mu,sigma,0) for sigma in [.5,1,2]]
        if mu<0:assert values[0]>values[1]>values[2]
        elif mu>0:assert values[0]<values[1]<values[2]
        else:assert values==[.5,.5,.5]
        varrows.append(dict(mu=mu,threshold=0,sigmas=[.5,1,2],probabilities=values))
    out['variance_direction'] = dict(rows=varrows,derivative='dPI/dsigma=(mu-T)*phi((T-mu)/sigma)/sigma^2 for sigma>0',
        qualification='Increasing uncertainty need not increase PI; the direction depends on the mean relative to the fixed target.')
    for mu,sigma,threshold in grid:
        close(probability(mu,sigma,threshold),probability(3*mu-2,3*sigma,3*threshold-2))
    out['positive_affine_change'] = dict(grid_cases=len(grid),scale=3,offset=-2,
        qualification='The event probability is invariant when distribution and target transform consistently; this does not justify leaving a numeric target or margin untransformed.')

    noise=[]
    for mu in [-1,0,1]:
        latent=probability(mu,.5,0);observed=probability(mu,math.sqrt(.25+1),0)
        if mu<0:assert observed<latent
        elif mu>0:assert observed>latent
        else:close(observed,latent)
        noise.append(dict(mu=mu,threshold=0,latent_variance=.25,independent_noise_variance=1,
                          latent_event_probability=latent,noisy_observation_event_probability=observed))
    out['latent_versus_noisy_event'] = dict(rows=noise,
        qualification='Adding observation noise changes the event being scored. A fixed observed incumbent is another target choice, not integration over a random latent incumbent.')

    coupled={
        'same':[(0,0,F(1,2)),(1,1,F(1,2))],
        'independent':[(b,y,F(1,4)) for b,y in product([0,1],repeat=2)],
        'opposite':[(0,1,F(1,2)),(1,0,F(1,2))]}
    coupling={k:dict(strict=str(finite_event(v)),inclusive=str(finite_event(v,True))) for k,v in coupled.items()}
    assert [coupling[k]['strict'] for k in coupled]==['0','1/4','1/2']
    assert [coupling[k]['inclusive'] for k in coupled]==['1','3/4','1/2']
    random_inc=[(-2,1,F(1,2)),(2,1,F(1,2))]
    assert finite_event(random_inc)==F(1,2) and probability(1,0,0)==0
    out['random_incumbent'] = dict(same_uniform_binary_marginals=coupling,
        random_incumbent_example='B=-2 or2 equiprobably;Y=1. P(Y<B)=1/2, but P(Y<E[B])=0.',
        qualification='Joint dependence and the incumbent event matter; marginal prediction or replacing an uncertain incumbent by its mean is not generally sufficient.')

    weights=[F(1,3),F(2,3)];mus=[F(-2),F(1)];variance=F(1,4)
    mean=sum(w*m for w,m in zip(weights,mus));total_variance=variance+sum(w*(m-mean)**2 for w,m in zip(weights,mus))
    assert mean==0 and total_variance==F(9,4)
    components=[probability(float(m),.5,0) for m in mus]
    mixture=sum(float(w)*p for w,p in zip(weights,components));moment_matched=probability(float(mean),math.sqrt(float(total_variance)),0)
    assert abs(mixture-moment_matched)>.1
    out['fixed_event_hyperparameter_mixture'] = dict(weights=list(map(str,weights)),means=list(map(str,mus)),component_variance=str(variance),threshold=0,
        component_probabilities=components,mixture_probability=mixture,mixture_mean=str(mean),mixture_variance=str(total_variance),moment_matched_gaussian_probability=moment_matched,
        interpretation='Averaging conditional probabilities is correct for the same fixed event by total probability; a Gaussian using mixture moments is generally different. The comparison does not inherit a mutual-information noncommutation caveat.')

    ratio_rows=[]
    families=[[(F(-1,10),F(1,10)),(F(1,10),F(1))],[(F(-1),F(1)),(F(-1,2),F(1,10))],[(F(0),F(1)),(F(1),F(2)),(F(2),F(3))]]
    for ci,points in enumerate(families):
        for target in map(F,[-1,0,1]):
            ratios=[(m-target)/s for m,s in points];kappa=min(ratios);lcb=[m-kappa*s for m,s in points]
            ratio_min=[i for i,v in enumerate(ratios) if v==kappa];lcb_min=[i for i,v in enumerate(lcb) if v==min(lcb)]
            assert ratio_min==lcb_min and min(lcb)==target
            ratio_rows.append(dict(family=ci,target=str(target),kappa=str(kappa),minimizers=ratio_min))
    # At target0, B has ratio-5 versus A's-1. Every nonnegative kappa instead
    # favors A: LCB_A-LCB_B=-1/2-(9/10)kappa<0.
    assert (F(-1,2)-0)/F(1,10)==-5
    out['ratio_and_lcb'] = dict(exact_cases=ratio_rows,
        negative_coefficient_witness=dict(points=[['-1','1'],['-1/2','1/10']],target='0',matched_kappa='-5',pi_choice=1,any_nonnegative_lcb_choice=0),
        assumptions='Positive candidate standard deviations and an attained ratio minimum; finite sets here guarantee attainment. The matched kappa depends on the target and current predictive functions. Nonnegative exploration coefficients need additional restrictions.')

    gammas=[i/4 for i in range(-12,13)];single=[dict(gamma=g,pi_max=cdf(-g),mes=mes_score(g)) for g in gammas]
    assert all(a['pi_max']>b['pi_max'] and a['mes']>b['mes'] for a,b in zip(single,single[1:]))
    two=[]
    for sigma in [1,2]:
        gammas=[-1/sigma,1/sigma]
        two.append(dict(mu=0,sigma=sigma,maximum_samples=[-1,1],average_pi=sum(cdf(-g) for g in gammas)/2,average_mes=sum(mes_score(g) for g in gammas)/2))
    close(two[0]['average_pi'],.5);close(two[1]['average_pi'],.5)
    assert abs(two[0]['average_mes']-two[1]['average_mes'])>1e-5
    out['mes_scope'] = dict(single_threshold_grid=single,multiple_threshold_witness=two,
        interpretation='For one common maximum threshold and positive latent standard deviations, PI-max and MES Eq6 rank by the same standardized gap. The grid illustrates rather than proves the source monotonicity statement. With two distinct thresholds these two candidates tie in averaged PI but differ in averaged MES; this is not universal equivalence, exact noisy mutual information, or a regret claim.')
    out['scope'] = dict(categories=11,arithmetic='Fraction exact finite event, threshold and LCB algebra; binary64 erfc/exp/log/sqrt Gaussian/entropy evaluations',
        floating_absolute_tolerance=ABS_TOL,floating_relative_tolerance=0,
        excluded=['production extreme-tail accuracy','GP fitting','author-code execution','complete optimizer','benchmark','historical priority','general convergence or regret proof'])
    print(json.dumps(out,sort_keys=True,indent=2))


if __name__ == '__main__':
    main()
