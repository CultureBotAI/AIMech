"""Finite curator checks for ECM, ECME and PX-EM; no fitting benchmark."""
import json
import math


def close(a, b):
    assert math.isclose(a, b, rel_tol=1e-12, abs_tol=1e-12), (a, b)


# Observed y=(0,0) has independent unit-variance normals with means (a,b).
# The independent missing z is N(a+10*b,1). At old=(1,1), E[z]=11.
# Its conditional variance adds a parameter-independent constant to Q.
def ll(a, b):
    return -(a*a+b*b)/2


def q(a, b):
    return ll(a, b)-(a+10*b-11)**2/2


old = (1.0, 1.0)
first = (0.5, 1.0)
ecm = (0.5, 105/101)
em = (11/102, 110/102)
ecme = (0.5, 0.0)
invalid_first = (1.0, 0.0)
invalid_final = (5.5, 0.0)
assert q(old[0], old[1]) < q(*first) < q(*ecm) <= q(*em)
assert ll(*ecm) > ll(*old)
assert ll(*ecm) < ll(*first)  # A CM substep need not increase observed LL.
assert ll(*ecme) > ll(*first) > ll(*old)
assert ll(*invalid_first) > ll(*old)
assert q(*invalid_final) > q(*invalid_first)
assert ll(*invalid_final) < ll(*old)  # Stale Q after an L step is unsafe.
close(em[0]+(em[0]+10*em[1]-11), 0)
close(em[1]+10*(em[0]+10*em[1]-11), 0)
schedule = {name: dict(theta=t, observed_log_likelihood=ll(*t), old_q=q(*t))
            for name, t in [('old', old), ('first_cm', first), ('ecm', ecm),
                            ('em', em), ('ecme', ecme),
                            ('invalid_l_then_q', invalid_final)]}
# Complete-data coordinate maximization that forever fixes b misses stationarity.
restricted = (0.0, 1.0)
assert ll(*restricted) > ll(*old) and -restricted[1] != 0

# Liu-Rubin-Wu scalar-normal example: y|z ~ N(z,1), z~N(theta,sigma2).
y, theta, sigma2 = 2.0, 0.0, 0.25
m = (theta+sigma2*y)/(1+sigma2)
alpha = y-m
reduced = m+alpha
close(reduced, y)
close((y-m)/(y-theta), 1/(1+sigma2))
# Expanded y|z ~ N(z+alpha,1) preserves N(theta_star+alpha,1+sigma2).
scalar = dict(old=theta, ordinary_em=m, expanded_theta=m, expanded_alpha=alpha,
              reduced_theta=reduced, next_auxiliary_reset=0,
              ordinary_error_factor=1/(1+sigma2), px_error_factor=0)


def t_ll(data, mu, scatter, nu):
    constant = (math.lgamma((nu+1)/2)-math.lgamma(nu/2)
                - math.log(nu*math.pi*scatter)/2)
    return sum(constant-(nu+1)/2*math.log1p((x-mu)**2/(nu*scatter))
               for x in data)


data, nu = [-2.0, -0.5, 1.0, 4.0], 4.0
weights = [(nu+1)/(nu+x*x) for x in data]
sumw = sum(weights)
new_mu = sum(w*x for w, x in zip(weights, data))/sumw
weighted_residual = sum(w*(x-new_mu)**2 for w, x in zip(weights, data))
em_scatter = weighted_residual/len(data)
alpha_new = sumw/len(data)
px_scatter = em_scatter/alpha_new
close(px_scatter, weighted_residual/sumw)
old_ll = t_ll(data, 0, 1, nu)
em_ll = t_ll(data, new_mu, em_scatter, nu)
px_ll = t_ll(data, new_mu, px_scatter, nu)
assert em_ll > old_ll and px_ll > old_ll
t_example = dict(data=data, nu=nu, weights=weights, mu=new_mu,
                 ordinary_scatter=em_scatter, expanded_alpha=alpha_new,
                 reduced_scatter=px_scatter, old_ll=old_ll,
                 ordinary_ll=em_ll, px_ll=px_ll)

# Audit inconsistent displayed expressions against elementary model moments.
truncated_mean = math.sqrt(2/math.pi)
true_second = 1.0  # Standard normal conditioned positive; square is symmetric.
printed_second = truncated_mean**2+1  # PX-EM p.766 at a=0.
assert printed_second != true_second
k, intensity, a0, background, count = 2, 3, 0.5, 4, 7
rate = k*intensity+background
ez = count*k*intensity/rate
eu = count*k*a0/rate
er = count*(background-k*a0)/rate
wrong_eu = count*a0*intensity/rate
close(ez+eu+er, count)
assert wrong_eu != eu
conditional_mean = 0.5*2  # Cov(Y_m,Y_o)=.5, Var(Y_o)=1, Y_o=2.
assert conditional_mean == 1 and conditional_mean != -1
scatter_new_mean = sum((x-1)**2 for x in [0, 2])/2
scatter_old_mean = sum(x*x for x in [0, 2])/2
close(scatter_new_mean, 1)
assert scatter_old_mean != scatter_new_mean
formula_checks = dict(probit_true_second=true_second,
                      probit_printed_second=printed_second,
                      poisson_true_eu=eu, poisson_printed_eu=wrong_eu,
                      conditional_normal_mean=conditional_mean,
                      new_mean_scatter=scatter_new_mean,
                      old_mean_scatter=scatter_old_mean)

print(json.dumps(dict(schedule=schedule, restricted_gradient_b=-restricted[1],
                      scalar_pxem=scalar, fixed_nu_t=t_example,
                      source_formula_audits=formula_checks,
                      scope='Finite analytic curator examples, not author code, '
                            'empirical reproduction or a general convergence proof.'),
                 indent=2))
