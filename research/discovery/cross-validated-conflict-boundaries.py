"""Finite analytic conflict-diagnostic boundaries; no fitted model or MCMC."""
import json
import math
from statistics import NormalDist

normal = NormalDist()


def experiment():
    # Known between-unit and observation variances, three omitted-unit training
    # observations, and a proper Gaussian population-mean prior.
    n, between, observation, prior_var = 3, 1.0, 0.5, 0.25
    population_mean, observed, other_mean = 2.0, 3.0, 0.0
    total = between + observation
    posterior_var = 1 / (1/prior_var + n/total)
    weight = n*posterior_var/total
    posterior_mean = weight*other_mean
    prior_rep_var = between + posterior_var
    likelihood_rep_var = observation
    difference_mean = posterior_mean-observed
    difference_var = prior_rep_var+likelihood_rep_var
    conflict_lower = normal.cdf(-difference_mean/math.sqrt(difference_var))
    predictive_lower = NormalDist(posterior_mean, math.sqrt(difference_var)).cdf(observed)
    assert abs(conflict_lower-predictive_lower) < 1e-15

    # As data repeat at a fixed population mean, posterior predictive normality
    # does not ensure uniform p-values with this informative prior.
    fixed_residual_mean = (1-weight)*population_mean
    fixed_residual_var = total*(1+weight**2/n)
    prior_integrated_var = fixed_residual_var+(1-weight)**2*prior_var
    assert abs(prior_integrated_var-difference_var) < 1e-14
    threshold = normal.inv_cdf(0.95)*math.sqrt(difference_var)
    fixed_upper_rejection = 1-NormalDist(fixed_residual_mean,math.sqrt(fixed_residual_var)).cdf(threshold)
    assert fixed_upper_rejection > 0.2
    preposterior_upper_rejection = 1-NormalDist(0, math.sqrt(prior_integrated_var)).cdf(threshold)
    assert abs(preposterior_upper_rejection-0.05) < 1e-14

    # The flat population-mean limit has weight 1 and yields a pivotal residual.
    flat_reference_var = total+total/n
    flat_actual_var = total*(1+1/n)
    assert abs(flat_reference_var-flat_actual_var) < 1e-14

    # Cut nuisance example: p(gamma | other data) gives equal weights at1,2;
    # local likelihood y=2 ~ N(gamma*phi,1), with flat reference dphi.
    # Each proper conditional local posterior is N(2/gamma,1/gamma^2).
    # Integrating the UNNORMALIZED likelihood first reweights gamma by1/gamma.
    gammas=[1.,2.]
    cut_weights=[.5,.5]
    conditional_means=[2/g for g in gammas]
    conditional_vars=[1/g**2 for g in gammas]
    local_normalizers=[1/g for g in gammas]
    joint_weights=[w*z for w,z in zip(cut_weights,local_normalizers)]
    joint_weights=[w/sum(joint_weights) for w in joint_weights]
    cut_mean=sum(w*m for w,m in zip(cut_weights,conditional_means))
    joint_mean=sum(w*m for w,m in zip(joint_weights,conditional_means))
    assert cut_mean == 1.5 and abs(joint_mean-5/3) < 1e-14

    # A shared draw of correlated hyperparameters (beta,gamma)=(0,1) or(2,2)
    # gives correlated replications despite conditionally independent noises.
    prior_means=[0.,2.]
    prior_var=1+sum(.5*(m-1)**2 for m in prior_means)
    likelihood_var=sum(.5*(v+(m-cut_mean)**2) for m,v in zip(conditional_means,conditional_vars))
    covariance=sum(.5*a*b for a,b in zip(prior_means,conditional_means))-1*cut_mean
    true_difference_var=prior_var+likelihood_var-2*covariance
    mixture_lower=sum(.5*normal.cdf((m-a)/math.sqrt(1+v)) for a,m,v in zip(prior_means,conditional_means,conditional_vars))
    assert covariance == -.5 and true_difference_var == 3.875
    assert abs(true_difference_var-(prior_var+likelihood_var)) == 1

    return dict(
        limits='Analytic finite normal and two-state-nuisance examples only. No empirical calibration experiment, MCMC, author implementation or global model fit.',
        gaussian_equivalence=dict(posterior_mean=posterior_mean,posterior_variance=posterior_var,prior_rep_variance=prior_rep_var,likelihood_rep_variance=likelihood_rep_var,difference_mean=difference_mean,difference_variance=difference_var,conflict_lower=conflict_lower,predictive_lower=predictive_lower),
        calibration=dict(shrinkage_weight=weight,fixed_population_mean=population_mean,fixed_residual_mean=fixed_residual_mean,fixed_residual_variance=fixed_residual_var,preposterior_residual_variance=prior_integrated_var,nominal_upper_size=.05,fixed_parameter_upper_size=fixed_upper_rejection,preposterior_upper_size=preposterior_upper_rejection,flat_reference_variance=flat_reference_var,flat_actual_variance=flat_actual_var),
        nuisance_normalization=dict(cut_weights=cut_weights,conditional_means=conditional_means,conditional_variances=conditional_vars,local_normalizers=local_normalizers,normalize_after_mixing_weights=joint_weights,cut_mean=cut_mean,normalize_after_mixing_mean=joint_mean),
        nuisance_dependence=dict(prior_rep_variance=prior_var,likelihood_rep_variance=likelihood_var,covariance=covariance,difference_variance=true_difference_var,incorrect_independent_sum=prior_var+likelihood_var,exact_mixture_lower_tail=mixture_lower),
    )


if __name__ == '__main__':
    print(json.dumps(experiment(),indent=2,sort_keys=True))
