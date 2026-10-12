"""Finite curator checks; no historical fit or general convergence proof."""
from fractions import Fraction as F
import json
import math

# Valid complete model p(y,z|theta)=N(y;theta,1) N(z;theta,1).
# For observed y=0 the latent conditional is N(theta,1), while theta_M=s/2.
ll = lambda theta: -theta * theta / 2
old, s_old, latent_value = 1., 2., 3.
exact_em = old / 2
mcem = latent_value / 2
sa_stat = s_old + .25 * (latent_value - s_old)
saem = sa_stat / 2
assert ll(exact_em) > ll(old) > ll(saem) > ll(mcem)
assert s_old + 0 * (latent_value - s_old) == s_old
assert s_old + 1 * (latent_value - s_old) == latent_value
# Independent finite batches give nonzero noise even at a fitted point; no ascent certificate.
# These values are possible sample summaries, not claimed random experiment outcomes.

# Averaging sufficient statistics before a nonlinear maximizer differs from parameter averaging.
variance_after_stat_average = (1. + 9.) / 2
log_variance_after_stat_average = math.log(variance_after_stat_average)
average_log_variance = (math.log(1.) + math.log(9.)) / 2
assert not math.isclose(log_variance_after_stat_average, average_log_variance)

# Bernoulli latent example: prior P(z=1)=2/5; likelihoods P(y=1|z)=1/5,4/5.
# Target at this parameter is (3/11,8/11). A prior independence MH proposal
# cancels the prior from acceptance. Rejections remain in the chain.
pi = [F(3, 11), F(8, 11)]
K = [[F(3, 5), F(2, 5)], [F(3, 20), F(17, 20)]]
def step(p, kernel):
    return [sum(p[i] * kernel[i][j] for i in range(2)) for j in range(2)]
assert all(sum(row) == 1 for row in K)
assert step(pi, K) == pi
one_step = step([F(1), F(0)], K)
assert one_step != pi
conditional_noise = one_step[1] - pi[1]
assert conditional_noise == -F(18, 55)
# A second transition uses the retained state distribution, not a reset to state zero.
two_steps = step(one_step, K)
assert two_steps != one_step
# Target invariance plus irreducibility need not give convergence: periodic flip.
flip = [[F(0), F(1)], [F(1), F(0)]]
uniform = [F(1, 2), F(1, 2)]
assert step(uniform, flip) == uniform
assert step(step([F(1), F(0)], flip), flip) == [F(1), F(0)]

# Information/Hessian distinction in the1999 Eq11 and2004 Eq8-10.
# At theta*=0: complete Hessian=-2, score=z, E z=0, Var z=1.
G, score_mean = -2 + 1, 0
H = G - score_mean ** 2
assert H == -1 and -H == 1  # observed Hessian and observed information respectively.

# Compact latent support does not bound beta sufficient statistics near its endpoints.
logs = [math.log(10. ** -n) for n in [2, 6, 12, 24]]
assert all(a > b for a, b in zip(logs, logs[1:]))
# A nonconstant smooth mean difference delta cannot be bounded by a common
# constant times delta^(1/alpha), alpha<1, as delta tends to zero.
holder_ratios = [d / d ** 2 for d in [1e-2, 1e-4, 1e-6]]
assert holder_ratios == [100., 10000., 1000000.]
# A weaker Holder estimate delta^alpha does not directly supply a Lipschitz bound.
weaker_ratios = [math.sqrt(d) / d for d in [1e-2, 1e-4, 1e-6]]
assert all(math.isclose(x,y,rel_tol=1e-12) for x,y in zip(weaker_ratios,[10.,100.,1000.]))
# Newton ascent for concave L(theta)=-theta^2/2: minus H^-1 grad is the direction.
start, grad, hess = 1., -1., -1.
assert start - grad / hess == 0
assert ll(start + grad / hess) < ll(start)
print(json.dumps(dict(
    gaussian=dict(old=old, exact_em=exact_em, mcem=mcem, saem=saem,
                  likelihoods=[ll(x) for x in [old,exact_em,mcem,saem]]),
    nonlinear_averaging=dict(maximize_averaged_statistic=log_variance_after_stat_average,
                             average_parameter=average_log_variance),
    markov=dict(target=pi, transition=K, first=one_step, second=two_steps,
                conditional_noise=conditional_noise, periodic_flip=flip),
    information=dict(complete_hessian=-2,G=G,H=H,observed_information=-H),
    proof_boundaries=dict(endpoint_logs=logs,superlinear_holder_ratio=holder_ratios,
                         weaker_holder_to_lipschitz_ratio=weaker_ratios),
    scope='Finite algebraic checks only; no general convergence-proof repair, '
          'original software, empirical fit, or calibration experiment.'),default=str,indent=2))
