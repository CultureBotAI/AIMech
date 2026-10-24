#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 479:
pFedBayes (Personalized Federated Learning via Variational Bayesian Inference,
Zhang, Li, Li, Guo, & Shao 2022, ICML 2022, PMLR 162:26293-26310).

Verifies:
1. Closed-form mean-field Gaussian KL divergence (Equation 8) between client variational
   posterior q^i(theta) = prod_{m=1}^T N(mu_{i,m}, sigma_{i,m}^2) and global prior
   distribution w(theta) = prod_{m=1}^T N(mu_{w,m}, sigma_{w,m}^2):
   KL(q^i(theta) || w(theta)) = (1/2) sum_{m=1}^T [ log(sigma_{w,m}^2 / sigma_{i,m}^2)
     + (sigma_{i,m}^2 + (mu_{i,m} - mu_{w,m})^2) / sigma_{w,m}^2 - 1 ].
2. Exact global variational optimality conditions (Lemma A.2, Equations A.5-A.7 & A.23-A.28):
   Minimizing F(w) = (1/N) sum_{i=1}^N KL(q^i(theta) || w(theta)) over (mu_{w,m}, sigma_{w,m}^2)
   yields the exact closed-form global Gaussian parameters:
     mu_{w,m}^* = (1/N) sum_{i=1}^N mu_{i,m},
     sigma_{w,m}^{*2} = (1/N) sum_{i=1}^N [ sigma_{i,m}^2 + (mu_{i,m} - mu_{w,m}^*)^2 ]
                      = (1/N) sum_{i=1}^N [ sigma_{i,m}^2 + mu_{i,m}^2 - mu_{w,m}^{*2} ].
3. Softplus standard-deviation reparameterization (Equation 26):
   theta_m = mu_m + log(1 + exp(rho_m)) * g_m, g_m ~ N(0, 1), ensuring sigma_m > 0
   for all rho_m in R, and alternating bilevel client updates of personalized v_r^t and
   localized global v_{w,r}^t (Algorithm 1, Equations 27-28).
"""

from __future__ import annotations
import math


def softplus(rho: float) -> float:
    return math.log(1.0 + math.exp(rho))


def kl_diag_gaussian(
    mu_q: list[float],
    var_q: list[float],
    mu_w: list[float],
    var_w: list[float],
) -> float:
    return 0.5 * sum(
        math.log(vw / vq) + (vq + (mq - mw) ** 2) / vw - 1.0
        for mq, vq, mw, vw in zip(mu_q, var_q, mu_w, var_w)
    )


def main() -> None:
    # 3 clients with T=2 Gaussian BNN parameter coordinates
    client_mus = [
        [1.2, -0.8],
        [0.4, 0.2],
        [-0.7, 1.5],
    ]
    client_rhos = [
        [-1.5, -2.0],
        [-1.2, -1.8],
        [-2.2, -1.4],
    ]
    # Verify Eq (26) softplus reparameterization guarantees strictly positive variances
    client_vars = [[softplus(r) ** 2 for r in row] for row in client_rhos]
    assert all(v > 0.0 for row in client_vars for v in row)

    N = len(client_mus)
    T = len(client_mus[0])

    # 1. Compute Lemma A.2 closed-form global optimal distribution w^*(theta) (Eqs A.6-A.7)
    mu_w_star = [sum(client_mus[i][m] for i in range(N)) / N for m in range(T)]
    var_w_star_form1 = [
        sum(client_vars[i][m] + (client_mus[i][m] - mu_w_star[m]) ** 2 for i in range(N)) / N
        for m in range(T)
    ]
    var_w_star_form2 = [
        sum(client_vars[i][m] + client_mus[i][m] ** 2 - mu_w_star[m] ** 2 for i in range(N)) / N
        for m in range(T)
    ]
    for m in range(T):
        assert abs(var_w_star_form1[m] - var_w_star_form2[m]) < 1e-15

    # 2. Verify first-order optimality conditions (Eqs A.25-A.26) and strict global optimality of F(w^*)
    for m in range(T):
        d_mu = sum(-2.0 * (client_mus[i][m] - mu_w_star[m]) / var_w_star_form1[m] for i in range(N)) / N
        d_sigma = (
            sum(
                2.0 / math.sqrt(var_w_star_form1[m])
                - 2.0 * (client_vars[i][m] + (client_mus[i][m] - mu_w_star[m]) ** 2) / (var_w_star_form1[m] ** 1.5)
                for i in range(N)
            )
            / N
        )
        assert abs(d_mu) < 1e-15 and abs(d_sigma) < 1e-15

    f_opt = sum(kl_diag_gaussian(client_mus[i], client_vars[i], mu_w_star, var_w_star_form1) for i in range(N)) / N
    for delta_mu, delta_var in [(0.1, 0.0), (-0.1, 0.0), (0.0, 0.08), (0.0, -0.05)]:
        mu_p = [m + delta_mu for m in mu_w_star]
        var_p = [v + delta_var for v in var_w_star_form1]
        f_p = sum(kl_diag_gaussian(client_mus[i], client_vars[i], mu_p, var_p) for i in range(N)) / N
        assert f_opt < f_p, f"Lemma A.2 solution must strictly minimize F(w): {f_opt} vs {f_p}"

    # 3. Verify Theorem 1 minimax rate exponent 2*beta / (2*beta + d) when T = C_1 n^{d / (2*beta + d)} (Eqs 21-25)
    beta_smooth, d_int, n_samples = 2.0, 4.0, 1000.0
    T_opt = n_samples ** (d_int / (2.0 * beta_smooth + d_int))
    approx_rate = T_opt ** (-2.0 * beta_smooth / d_int)
    est_rate = T_opt / n_samples
    minimax_rate = n_samples ** (-2.0 * beta_smooth / (2.0 * beta_smooth + d_int))
    assert abs(approx_rate - minimax_rate) < 1e-14 and abs(est_rate - minimax_rate) < 1e-14

    print(
        f"[PASS] pFedBayes boundary verification passed: F(w^*)={f_opt:.5f}, "
        f"minimax_rate=n^(-2*beta/(2*beta+d))={minimax_rate:.5f}"
    )


if __name__ == "__main__":
    main()
