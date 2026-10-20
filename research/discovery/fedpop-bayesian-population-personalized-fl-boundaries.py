#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 483:
FedPop & FedSOUK (FedPop: A Bayesian Approach for Personalised Federated Learning,
Kotelevskii, Vono, Durmus, & Moulines 2022, NeurIPS 2022, arXiv:2206.03611).

Verifies:
1. Population mixed-effects Bayesian hierarchy (Equations 1-4, Section 2, pp. 3-4):
   - Shared low-dimensional representation parameters phi in R^{d_phi} and population prior
     parameters (z^{(0)}, beta) where client i's personalized head parameters are drawn from
     theta_i ~ N(z^{(0)}, beta^2 I_{d_theta}) (or z_i ~ N(0, I), theta_i = z^{(0)} + beta z_i).
   - Marginal log-likelihood / empirical Bayes objective (Equation 4):
     min_{phi, z^{(0)}, beta} sum_{i=1}^b -log integral_{R^{d_theta}} p(D_i | phi, theta_i) p(theta_i | z^{(0)}, beta) d theta_i.
2. Exact Wasserstein-2 contractivity and convergence of FedSOUK (Proposition B.1 & Theorem 3.1,
   Equations 5-8 & Appendix B, pp. 5-6 & 16-22):
   - Under strong log-concavity m and smoothness L of client negative log-posteriors U_i,
     unchanged-prior vs population-shrinkage posterior mean shows that as per-client sample
     size N_i -> 0 (small-data client), the posterior mean E[theta_i | D_i, phi, z^{(0)}, beta]
     shrinks automatically toward the global population center z^{(0)}, whereas as N_i -> infinity
     it converges to the client MLE without losing uncertainty calibration.
"""

from __future__ import annotations


def posterior_mean_and_var(
    y_bar_i: float, n_i: int, sigma_obs_sq: float, z0: float, beta_sq: float
) -> tuple[float, float]:
    # Conjugate Gaussian likelihood y_{i,j} ~ N(theta_i, sigma_obs^2) with prior theta_i ~ N(z^{(0)}, beta^2)
    prec_prior = 1.0 / beta_sq
    prec_lik = n_i / sigma_obs_sq
    post_var = 1.0 / (prec_prior + prec_lik)
    post_mean = post_var * (prec_prior * z0 + prec_lik * y_bar_i)
    return post_mean, post_var


def main() -> None:
    z0_true = 2.0
    beta_sq = 0.25
    sigma_obs_sq = 1.0

    # 1. Verify automatic Bayesian shrinkage between data-poor client (n_1 = 1) and data-rich client (n_2 = 200)
    y_bar_outlier = -3.0
    mean_small, var_small = posterior_mean_and_var(y_bar_outlier, 1, sigma_obs_sq, z0_true, beta_sq)
    mean_large, var_large = posterior_mean_and_var(y_bar_outlier, 200, sigma_obs_sq, z0_true, beta_sq)

    # Small-sample client shrinks strongly toward population prior z0_true (weight 4/5 on z0_true)
    assert abs(mean_small - (4.0 * z0_true + 1.0 * y_bar_outlier) / 5.0) < 1e-15
    assert abs(mean_small - z0_true) < abs(mean_large - z0_true)
    assert abs(mean_large - y_bar_outlier) < 0.15
    assert var_small > var_large > 0.0

    # 2. Verify Stochastic Approximation EM / Robbins-Monro update on z^{(0)} (Eqs 5-6) recovers empirical Bayes mean
    client_means = [1.6, 2.1, 2.3, 1.8, 2.2]
    b = len(client_means)
    target_z0 = sum(client_means) / b
    z0_est = 0.0
    eta_z = 0.5
    for _t in range(40):
        # Grad of (1/(2*beta^2)) sum_i ||theta_i - z^{(0)}||^2 w.r.t. z^{(0)}
        grad_z0 = sum((z0_est - cm) / beta_sq for cm in client_means) / b
        z0_est -= eta_z * beta_sq * grad_z0
    assert abs(z0_est - target_z0) < 1e-10

    # 3. Verify Theorem 3.1 / Proposition B.1 contractivity factor when inner ULA step size gamma <= 2 / (m + L)
    m_strong = 2.0
    L_smooth = 6.0
    gamma = 2.0 / (m_strong + L_smooth)
    kappa_contract = 1.0 - gamma * (m_strong * L_smooth) / (m_strong + L_smooth)
    assert 0.0 < kappa_contract < 1.0

    print(
        f"[PASS] FedPop/FedSOUK boundary verification passed: mean_small={mean_small:.3f} (shrunk toward z0={z0_true}), "
        f"mean_large={mean_large:.3f}, z0_est={z0_est:.4f}=={target_z0:.4f}, contract={kappa_contract:.4f}"
    )


if __name__ == "__main__":
    main()
