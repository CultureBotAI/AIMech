#!/usr/bin/env python3
"""Deterministic boundary verification for Round 831:
Prior-Expansion Marginal Likelihood Score Prior-Data Conflict Check
(Nott, Seah, Al-Labadi, Evans, Ng, & Englert, 2020, Bayesian Analysis 15(1):239-265, arXiv:1902.10393v2).

Verifies:
1. Score identity (Section 1, Equation 1.1 & Section 2.1):
   For an expanded prior p(theta | gamma) reducing to p_0(theta) at gamma = gamma_0,
   the marginal likelihood score S_gamma(y) = d/dgamma log p(y | gamma)|_{gamma_0}
   equals the posterior expectation E[d/dgamma log p(theta | gamma)|_{gamma_0} | y].
2. Location-scale Gaussian prior expansion (Section 2.2, Equation 2.4):
   For y | theta ~ N(theta, sigma^2/n) and location expansion theta | gamma ~ N(mu_0 + gamma, tau_0^2),
   S_gamma(y) = (y_bar - mu_0) / (sigma^2/n + tau_0^2), whose standardized quadratic statistic
   Q(y) = S_gamma(y)^2 / Var_{Y ~ p(y|gamma_0)}(S_gamma(Y)) = (y_bar - mu_0)^2 / (sigma^2/n + tau_0^2)
   matches the Box (1980) / Evans & Moshonov (2006) prior-data conflict statistic.
3. Monotonicity of conflict p-value p_S(y_obs) = P(Q(Y) >= Q(y_obs)) as |y_bar - mu_0| grows.
"""

import math


def normal_Location_expansion_score(y_bar: float, mu0: float, sigma2_n: float, tau0_2: float):
    # Direct derivative of log marginal likelihood log N(y_bar; mu0 + gamma, sigma2_n + tau0_2) at gamma=0
    marginal_var = sigma2_n + tau0_2
    score_marginal = (y_bar - mu0) / marginal_var

    # Posterior expectation of prior score d/dgamma log N(theta; mu0 + gamma, tau0_2)|_{gamma=0} = (theta - mu0)/tau0_2
    # Posterior mean of theta given y_bar at gamma=0:
    post_var = 1.0 / (1.0 / sigma2_n + 1.0 / tau0_2)
    post_mean = post_var * (y_bar / sigma2_n + mu0 / tau0_2)
    score_posterior_expectation = (post_mean - mu0) / tau0_2

    # Prior predictive variance of S_gamma(Y) under Y_bar ~ N(mu0, sigma2_n + tau0_2):
    var_score = 1.0 / marginal_var
    quad_stat = (score_marginal ** 2) / var_score
    p_val = math.erfc(math.sqrt(quad_stat / 2.0))
    return score_marginal, score_posterior_expectation, quad_stat, p_val


def main() -> None:
    s_marg_0, s_post_0, q_0, p_0 = normal_Location_expansion_score(1.0, 1.0, 0.25, 0.75)
    assert abs(s_marg_0 - s_post_0) < 1e-12
    assert abs(q_0) < 1e-12 and abs(p_0 - 1.0) < 1e-12

    s_marg_1, s_post_1, q_1, p_1 = normal_Location_expansion_score(2.5, 1.0, 0.25, 0.75)
    assert abs(s_marg_1 - s_post_1) < 1e-12

    s_marg_2, s_post_2, q_2, p_2 = normal_Location_expansion_score(4.2, 1.0, 0.25, 0.75)
    assert abs(s_marg_2 - s_post_2) < 1e-12
    assert q_2 > q_1 > q_0
    assert p_2 < p_1 < p_0 and p_2 < 0.005

    print(
        f"[PASS] Round 831 Prior-Expansion Score Check verified: "
        f"|S_marg - E_post|=0.0, Q={q_1:.3f}->{q_2:.3f}, p_S={p_1:.4f}->{p_2:.5f}"
    )


if __name__ == "__main__":
    main()
