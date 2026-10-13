"""Finite diagnostic arithmetic, not source software, fitting or calibration."""
import json
import math


def simpson(f, lo, hi, n=20000):
    assert n % 2 == 0
    h = (hi-lo)/n
    return h/3*(f(lo)+f(hi)+sum((4 if i % 2 else 2)*f(lo+i*h) for i in range(1,n)))


def mv(a, x):
    return [sum(t*v for t,v in zip(row,x)) for row in a]


def tr(a):
    return list(map(list,zip(*a)))


def mm(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def add(a,b):
    return [[x+y for x,y in zip(ra,rb)] for ra,rb in zip(a,b)]


def inv(a):
    d=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    assert d > 0 and a[0][0] > 0
    return [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]


def quadratic(x,a):
    return sum(t*v for t,v in zip(x,mv(a,x)))


def experiment():
    # Supplied proper global factors; a deliberately constructed local stationary
    # Poisson block. This is not a globally optimized variational posterior.
    nu, scale, beta_mean, beta_var = 6.,3.,-.5,.2
    a_mean, a_var, y = 0.,.25,3.
    exposure=2*math.exp(-a_var/2)
    precision=nu/scale
    g=exposure*math.exp(a_mean+a_var/2)
    likelihood_precision=g
    prior_mean=beta_mean
    prior_var=1/precision
    likelihood_mean=a_mean+(y-g)/likelihood_precision
    likelihood_var=1/likelihood_precision
    combined_var=1/(precision+likelihood_precision)
    combined_mean=combined_var*(precision*prior_mean+likelihood_precision*likelihood_mean)
    assert abs(combined_var-a_var)<1e-14 and abs(combined_mean-a_mean)<1e-14

    def local_objective(m,v):
        return -.5*precision*((m-beta_mean)**2+v+beta_var)+y*m-exposure*math.exp(m+v/2)+.5*math.log(v)

    h=1e-5
    dm=(local_objective(a_mean+h,a_var)-local_objective(a_mean-h,a_var))/(2*h)
    dv=(local_objective(a_mean,a_var+h)-local_objective(a_mean,a_var-h))/(2*h)
    assert abs(dm)<1e-8 and abs(dv)<1e-8
    delta=prior_mean-likelihood_mean
    difference_var=prior_var+likelihood_var
    lower=.5*math.erfc(delta/math.sqrt(2*difference_var))
    upper=1-lower
    two_sided=2*min(lower,upper)
    assert delta == -1 and difference_var == 1 and lower > .5

    # Exact flat-prior likelihood posterior for this one-count Poisson example:
    # exposure*exp(a) has Gamma(shape=y, rate=1). Integrate its a-density.
    def exact_likelihood(a):
        return math.exp(y*(a+math.log(exposure))-exposure*math.exp(a)-math.lgamma(y))

    mass=simpson(exact_likelihood,-12,8)
    exact_mean=simpson(lambda a:a*exact_likelihood(a),-12,8)/mass
    exact_variance=simpson(lambda a:(a-exact_mean)**2*exact_likelihood(a),-12,8)/mass
    analytic_mean=1.5-.5772156649015328606-math.log(exposure)
    analytic_var=math.pi**2/6-1.25
    assert abs(mass-1)<1e-12
    assert abs(exact_mean-analytic_mean)<1e-11 and abs(exact_variance-analytic_var)<1e-10
    assert abs(exact_mean-likelihood_mean)>.1 and abs(exact_variance-likelihood_var)>.1
    predictive_prior_var=scale/(nu-2)+beta_var  # scalar IW, independent q(beta)
    assert predictive_prior_var > prior_var

    # A proper two-dimensional Gaussian-difference diagnostic is invariant
    # under a common invertible linear coordinate change.
    s=[[1.2,.3],[.3,.8]];d=[.8,-.6];t=[[1.,.5],[-.2,1.3]]
    q=quadratic(d,inv(s));qt=quadratic(mv(t,d),inv(mm(mm(t,s),tr(t))))
    assert abs(q-qt)<1e-13
    chi2_upper=math.exp(-q/2)  # exactly r=2, not a general chi-square routine
    singular_likelihood=[[2.,0.],[0.,0.]]
    proper_combined=add(singular_likelihood,[[1.,0.],[0.,1.]])
    assert singular_likelihood[0][0]*singular_likelihood[1][1]==0
    assert proper_combined[0][0]*proper_combined[1][1]==3

    # Known variances, balanced Gaussian units and flat beta reference prior.
    # Full-data and leave-one-unit-out predictive conflicts are not identical.
    k=4;between=1.;observation=.5;values=[3.,0.,0.,0.]
    loo_mean=sum(values[1:])/(k-1);full_mean=sum(values)/k
    loo_beta_var=(between+observation)/(k-1)
    full_beta_var=(between+observation)/k
    loo_stat=(values[0]-loo_mean)**2/(between+loo_beta_var+observation)
    full_stat=(values[0]-full_mean)**2/(between+full_beta_var+observation)
    assert abs(full_stat/loo_stat-(k-1)/(k+1))<1e-14
    return dict(
        limits='Finite supplied-state arithmetic only. The Poisson local block is stationary under supplied globals, which are not optimized. No global fit, source software or calibration simulation was run.',
        local_poisson=dict(mean=a_mean,variance=a_var,exposure=exposure,y=y,finite_gradient_mean=dm,finite_gradient_variance=dv,prior_message_mean=prior_mean,prior_message_variance=prior_var,likelihood_message_mean=likelihood_mean,likelihood_message_variance=likelihood_var,recombined_mean=combined_mean,recombined_variance=combined_var,difference_mean=delta,difference_variance=difference_var,lower_tail=lower,upper_tail=upper,two_sided=two_sided),
        approximation_boundaries=dict(exact_flat_prior_likelihood_mass=mass,exact_flat_prior_likelihood_mean=exact_mean,exact_flat_prior_likelihood_variance=exact_variance,full_q_predictive_prior_variance=predictive_prior_var,message_prior_variance=prior_var),
        multivariate=dict(mahalanobis=q,transformed_mahalanobis=qt,chi2_two_degrees_upper=chi2_upper,singular_likelihood_determinant=0,combined_precision_determinant=3),
        balanced_gaussian=dict(loo_statistic=loo_stat,full_data_statistic=full_stat,ratio=full_stat/loo_stat,expected_ratio=(k-1)/(k+1)))


if __name__=='__main__':
    print(json.dumps(experiment(),indent=2,sort_keys=True))
