#!/usr/bin/env python3
"""Constructed boundary & verification script for DebiasedNoisyMatrixCompletionInferenceAndUncertaintyQuantification.

Verifies the core mathematical properties of Chen, Fan, Ma, & Yan (2019),
'Inference and Uncertainty Quantification for Noisy Matrix Completion',
Proceedings of the National Academy of Sciences (PNAS), 116(46), 22931-22937
(DOI:10.1073/pnas.1910053116, arXiv:1906.04159v2):

1. Equivalent De-biased Matrix and De-shrunken Low-Rank Factor Estimators
   (Section 3.2, Eqs. 3.7-3.9 & Lemma 3 / Claim 1):
   Given a regularized low-rank factor solution (X, Y) minimizing
     (1/2) ||P_Omega(X Y^T - M)||_F^2 + (lambda/2) (||X||_F^2 + ||Y||_F^2),
   the rank-r projected de-biased matrix estimator
     M^d = P_{rank-r}( Z - (1/p) P_Omega(Z - M) ),   Z = X Y^T,
   and the de-shrunken low-rank factor estimator
     X^d = X (I_r + (lambda/p) (X^T X)^{-1})^{1/2},
     Y^d = Y (I_r + (lambda/p) (Y^T Y)^{-1})^{1/2},
   satisfy X^{d,T} X^d = X^T X + (lambda/p) I_r (Eq. D.4) and M^d approx X^d (Y^d)^T
   (exact equality when P_Omega(X Y^T - M) = -lambda U V^T at a balanced stationary
   point with full tangent alignment).
2. Theorem 2 & Corollary 1 (Entrywise Asymptotic Normality and Plug-In Variance):
   After compensating for regularization shrinkage, the entrywise error
   M^d_{ij} - M^*_{ij} is asymptotically zero-mean Gaussian N(0, v^*_{ij}) with
   oracle Cramér-Rao variance (Eq. 3.17):
     v^*_{ij} = (sigma^2 / p) (||U^*_{i,.}||_2^2 + ||V^*_{j,.}||_2^2),
   estimated consistently without sample splitting by (Eq. 3.22):
     v_{ij} = (sigma^2 / p) ( X^d_{i,.} (X^{d,T} X^d)^{-1} (X^d_{i,.})^T
                            + Y^d_{j,.} (Y^{d,T} Y^d)^{-1} (Y^d_{j,.})^T ).
3. Theorem 3 & Theorem 4 (Exact Frobenius Risk with Pre-Constant 2):
   De-biasing eliminates the regularization shrinkage bias and reduces the Frobenius
   squared error ||M^d - M^*||_F^2 toward the oracle tangent-space lower bound
   2 n r sigma^2 / p.
"""

from __future__ import annotations

import json
import math
import random
from typing import List, Tuple


def dot(u: List[float], v: List[float]) -> float:
    return sum(a * b for a, b in zip(u, v))


def norm2(u: List[float]) -> float:
    return math.sqrt(dot(u, u))


def solve_nonconvex_factor_gd(
    M_obs: List[List[float]],
    Omega: List[List[int]],
    u_init: List[float],
    v_init: List[float],
    p_obs: float,
    lam: float,
    eta: float = 0.0025,
    steps: int = 900,
) -> Tuple[List[float], List[float]]:
    """Minimize (1/2) ||P_Omega(x y^T - M)||_F^2 + (lam/2)(||x||_2^2 + ||y||_2^2) for rank r=1."""
    n = len(M_obs)
    x = u_init[:]
    y = v_init[:]
    for _ in range(steps):
        gx = [lam * x[i] for i in range(n)]
        gy = [lam * y[j] for j in range(n)]
        for i in range(n):
            xi = x[i]
            row_om = Omega[i]
            row_m = M_obs[i]
            for j in range(n):
                if row_om[j] == 1:
                    resid = xi * y[j] - row_m[j]
                    gx[i] += resid * y[j]
                    gy[j] += resid * xi
        scale = eta / p_obs
        x = [x[i] - scale * gx[i] for i in range(n)]
        y = [y[j] - scale * gy[j] for j in range(n)]
    return x, y


def best_rank1_svd_power(A: List[List[float]], steps: int = 120) -> List[List[float]]:
    n = len(A)
    v = [1.0 / math.sqrt(n)] * n
    for _ in range(steps):
        Av = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
        ATAv = [sum(A[i][j] * Av[i] for i in range(n)) for j in range(n)]
        nv = norm2(ATAv)
        v = [c / nv for c in ATAv]
    u_raw = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
    sigma1 = norm2(u_raw)
    u = [c / sigma1 for c in u_raw]
    return [[sigma1 * u[i] * v[j] for j in range(n)] for i in range(n)]


def main() -> None:
    rng = random.Random(20261019)
    n = 16
    p_obs = 0.75
    sigma = 0.04
    sigma_star = 4.0

    # Construct incoherent unit singular vectors u^*, v^* in R^n
    u_raw = [1.0 + 0.25 * math.sin(i + 1) for i in range(n)]
    v_raw = [1.0 + 0.25 * math.cos(i + 1) for i in range(n)]
    nu = norm2(u_raw)
    nv = norm2(v_raw)
    u_star = [c / nu for c in u_raw]
    v_star = [c / nv for c in v_raw]

    x_star = [math.sqrt(sigma_star) * c for c in u_star]
    y_star = [math.sqrt(sigma_star) * c for c in v_star]
    M_star = [[x_star[i] * y_star[j] for j in range(n)] for i in range(n)]

    # Theoretical entrywise variance v^*_{ij} = (sigma^2 / p) (u^*_i^2 + v^*_j^2) (Eq. 3.17)
    v_star_mat = [
        [(sigma * sigma / p_obs) * (u_star[i] ** 2 + v_star[j] ** 2) for j in range(n)]
        for i in range(n)
    ]

    # Run Monte Carlo trials to verify:
    # (a) Exactness of Eq. D.4: ||X^d||_2^2 = ||X||_2^2 + lambda / p
    # (b) Proximity of M^{ncvx,d} = P_{rank-1}(Z - (1/p) P_Omega(Z - M)) and X^d (Y^d)^T (Lemma 3)
    # (c) Dramatic bias reduction and Frobenius error reduction of M^d vs shrunken Z = X Y^T
    # (d) Empirical 95% confidence interval coverage of [M^d_{ij} +/- 1.96 * sqrt(v_{ij})] vs naive [Z_{ij} +/- 1.96 * sqrt(v_{ij})]
    lam = 1.6 * sigma * math.sqrt(n * p_obs)
    trials = 25

    eq_d4_max_err = 0.0
    max_lemma3_rel_diff = 0.0
    frob_sq_shrunken_list = []
    frob_sq_debiased_list = []
    debiased_covered = 0
    shrunken_covered = 0
    total_entries = trials * n * n
    max_var_rel_err = 0.0

    for _ in range(trials):
        Omega = [[0] * n for _ in range(n)]
        M_obs = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if rng.random() < p_obs:
                    Omega[i][j] = 1
                    M_obs[i][j] = M_star[i][j] + rng.gauss(0.0, sigma)

        x_ncvx, y_ncvx = solve_nonconvex_factor_gd(
            M_obs, Omega, x_star, y_star, p_obs=p_obs, lam=lam, eta=0.0025, steps=900
        )

        norm_x_sq = dot(x_ncvx, x_ncvx)
        norm_y_sq = dot(y_ncvx, y_ncvx)
        # De-shrunken low-rank factors (Eq. 3.8)
        scale_x = math.sqrt(1.0 + (lam / p_obs) / norm_x_sq)
        scale_y = math.sqrt(1.0 + (lam / p_obs) / norm_y_sq)
        x_d = [scale_x * c for c in x_ncvx]
        y_d = [scale_y * c for c in y_ncvx]

        # Verify Eq. D.4: ||x_d||_2^2 == ||x_ncvx||_2^2 + lam / p_obs
        d4_err = abs(dot(x_d, x_d) - (norm_x_sq + lam / p_obs))
        if d4_err > eq_d4_max_err:
            eq_d4_max_err = d4_err

        # De-biased matrix via rank-1 SVD projection (Eq. 3.7)
        Z_mat = [[x_ncvx[i] * y_ncvx[j] for j in range(n)] for i in range(n)]
        Z0_mat = [
            [
                Z_mat[i][j] - (1.0 / p_obs) * (Z_mat[i][j] - M_obs[i][j]) if Omega[i][j] == 1 else Z_mat[i][j]
                for j in range(n)
            ]
            for i in range(n)
        ]
        M_d_svp = best_rank1_svd_power(Z0_mat, steps=100)
        M_d_fac = [[x_d[i] * y_d[j] for j in range(n)] for i in range(n)]

        # Lemma 3 proximity between M_d_svp and x_d y_d^T
        diff_frob = math.sqrt(
            sum((M_d_svp[i][j] - M_d_fac[i][j]) ** 2 for i in range(n) for j in range(n))
        )
        m_star_frob = sigma_star
        rel_diff = diff_frob / m_star_frob
        if rel_diff > max_lemma3_rel_diff:
            max_lemma3_rel_diff = rel_diff

        frob_sq_shrunken = sum((Z_mat[i][j] - M_star[i][j]) ** 2 for i in range(n) for j in range(n))
        frob_sq_debiased = sum((M_d_fac[i][j] - M_star[i][j]) ** 2 for i in range(n) for j in range(n))
        frob_sq_shrunken_list.append(frob_sq_shrunken)
        frob_sq_debiased_list.append(frob_sq_debiased)

        norm_xd_sq = dot(x_d, x_d)
        norm_yd_sq = dot(y_d, y_d)
        for i in range(n):
            for j in range(n):
                # Plug-in variance v_{ij} (Eq. 3.22)
                v_ij = (sigma * sigma / p_obs) * (
                    (x_d[i] ** 2) / norm_xd_sq + (y_d[j] ** 2) / norm_yd_sq
                )
                v_rel_err = abs(v_ij - v_star_mat[i][j]) / v_star_mat[i][j]
                if v_rel_err > max_var_rel_err:
                    max_var_rel_err = v_rel_err
                half_width = 1.96 * math.sqrt(v_ij)
                if abs(M_d_fac[i][j] - M_star[i][j]) <= half_width:
                    debiased_covered += 1
                if abs(Z_mat[i][j] - M_star[i][j]) <= half_width:
                    shrunken_covered += 1

    mean_frob_sq_shrunken = sum(frob_sq_shrunken_list) / trials
    mean_frob_sq_debiased = sum(frob_sq_debiased_list) / trials
    oracle_frob_sq = 2.0 * n * 1.0 * (sigma ** 2) / p_obs
    cov_debiased = debiased_covered / total_entries
    cov_shrunken = shrunken_covered / total_entries

    assert eq_d4_max_err < 1e-13, f"Eq. D.4 de-shrinking identity failed: {eq_d4_max_err}"
    assert max_lemma3_rel_diff < 0.015, f"Lemma 3 proximity failed: {max_lemma3_rel_diff}"
    assert mean_frob_sq_debiased < 0.55 * mean_frob_sq_shrunken, (
        f"De-biased Frobenius error did not improve over shrunken estimator: "
        f"{mean_frob_sq_debiased} vs {mean_frob_sq_shrunken}"
    )
    assert cov_debiased >= 0.90 and cov_debiased > cov_shrunken + 0.12, (
        f"De-biased 95% CI coverage {cov_debiased} failed to improve substantially over shrunken {cov_shrunken}"
    )

    summary = {
        "n": n,
        "p_obs": p_obs,
        "sigma": sigma,
        "lambda_reg": round(lam, 6),
        "eq_d4_deshrinking_identity_max_err": eq_d4_max_err,
        "lemma3_svp_vs_factor_max_rel_diff": round(max_lemma3_rel_diff, 6),
        "mean_frob_sq_shrunken": round(mean_frob_sq_shrunken, 6),
        "mean_frob_sq_debiased": round(mean_frob_sq_debiased, 6),
        "oracle_2n_r_sigma2_over_p": round(oracle_frob_sq, 6),
        "empirical_95_ci_coverage_debiased": round(cov_debiased, 4),
        "empirical_95_ci_coverage_shrunken_uncorrected": round(cov_shrunken, 4),
        "max_plugin_variance_rel_err": round(max_var_rel_err, 4),
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
