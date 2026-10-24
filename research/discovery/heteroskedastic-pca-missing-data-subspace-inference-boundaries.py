#!/usr/bin/env python3
"""
Constructed boundary and mechanism verification for Round 293:
Inference for Heteroskedastic PCA with Missing Data
(Yan, Chen, & Fan 2024, The Annals of Statistics 52(2):729-756, arXiv:2107.12365v2).

Verifies:
1. Under heteroskedastic noise and missing observations, the raw rescaled sample Gram matrix
   has systematically biased diagonal entries sum_t (Z_{i,t})^2 / p^2 that distort the leading
   eigenspace when row noise variances sigma_i^2 vary sharply across features.
2. Zeroing the diagonal of the inverse-probability-weighted empirical Gram matrix (Deflated
   Heteroskedastic PCA / HeteroPCA-style diagonal deflation) eliminates the diagonal noise spike
   and yields an asymptotically normal linear form and valid Wald confidence region for the principal
   subspace U* H with plug-in variance covariance estimator S_hat.
"""

import json
import math
import random


def power_method_rank1(mat: list[list[float]], n_iter: int = 80) -> tuple[float, list[float]]:
    d = len(mat)
    v = [1.0 / math.sqrt(d)] * d
    for _ in range(n_iter):
        w = [sum(mat[i][j] * v[j] for j in range(d)) for i in range(d)]
        norm = math.sqrt(sum(x * x for x in w))
        v = [x / norm for x in w]
    lam = sum(v[i] * sum(mat[i][j] * v[j] for j in range(d)) for i in range(d))
    if v[0] < 0:
        v = [-x for x in v]
    return lam, v


def subspace_sin_theta(u: list[float], u_star: list[float]) -> float:
    dot = max(-1.0, min(1.0, abs(sum(a * b for a, b in zip(u, u_star)))))
    return math.sqrt(max(0.0, 1.0 - dot * dot))


def run_simulation(seed: int = 20261019) -> dict:
    rng = random.Random(seed)
    d = 16
    n = 450
    p_obs = 0.65
    lam_star = 8.0

    # Ground-truth unit eigenvector u_star in R^d (incoherent)
    raw_u = [1.0 if i % 2 == 0 else -0.8 for i in range(d)]
    norm_u = math.sqrt(sum(x * x for x in raw_u))
    u_star = [x / norm_u for x in raw_u]

    # Strongly heteroskedastic noise variances across coordinates i = 0..d-1
    sigma_sq = [2.2 if i < 3 else 0.15 for i in range(d)]

    n_trials = 120
    vanilla_sin_thetas = []
    deflated_sin_thetas = []
    wald_covered_0 = 0
    linear_form_z_scores = []

    c_vec = [1.0 / math.sqrt(d)] * d

    for _ in range(n_trials):
        # Generate n columns X_{:, t} = sqrt(lam_star) * f_t * u_star + E_{:, t}
        # and missingness indicator delta_{i, t} ~ Bernoulli(p_obs)
        Z = [[0.0] * n for _ in range(d)]
        for t in range(n):
            f_t = rng.gauss(0.0, 1.0)
            for i in range(d):
                if rng.random() < p_obs:
                    e_it = rng.gauss(0.0, math.sqrt(sigma_sq[i]))
                    x_it = math.sqrt(lam_star) * f_t * u_star[i] + e_it
                    Z[i][t] = x_it / p_obs

        # Empirical Gram matrix G = (1/n) Z Z^T
        G_vanilla = [[0.0] * d for _ in range(d)]
        for i in range(d):
            zi = Z[i]
            for j in range(i, d):
                zj = Z[j]
                val = sum(zi[t] * zj[t] for t in range(n)) / n
                G_vanilla[i][j] = val
                G_vanilla[j][i] = val

        # Diagonal-deleted / deflated estimator M = P_off_diag(G_vanilla)
        G_deflated = [row[:] for row in G_vanilla]
        for i in range(d):
            G_deflated[i][i] = 0.0

        _, u_vanilla = power_method_rank1(G_vanilla)
        lam_hat, u_hat = power_method_rank1(G_deflated)

        vanilla_sin_thetas.append(subspace_sin_theta(u_vanilla, u_star))
        deflated_sin_thetas.append(subspace_sin_theta(u_hat, u_star))

        # Align sign H = sign(u_hat^T u_star)
        if sum(a * b for a, b in zip(u_hat, u_star)) < 0:
            u_hat = [-x for x in u_hat]

        # Influence function of leading eigenvector of diagonal-deleted Gram matrix M:
        # u_hat - u_star ≈ (1 / lam_star) * (I - u_star u_star^T) (M - M_star) u_star
        # Sample t contributes vector psi_t in R^d with i-th entry:
        # g_{i,t} = Z_{i,t} * (sum_{j != i} Z_{j,t} u_hat[j]) - lam_hat * (1 - u_hat[i]^2) * u_hat[i]
        # projected orthogonal to u_hat: psi_t = g_t - (u_hat^T g_t) u_hat
        psi_0_vals = []
        psi_lin_vals = []
        for t in range(n):
            dot_z_u = sum(Z[j][t] * u_hat[j] for j in range(d))
            g_t = [
                Z[i][t] * (dot_z_u - Z[i][t] * u_hat[i]) - lam_hat * (1.0 - u_hat[i] ** 2) * u_hat[i]
                for i in range(d)
            ]
            proj = sum(u_hat[i] * g_t[i] for i in range(d))
            psi_t = [(g_t[i] - proj * u_hat[i]) / lam_hat for i in range(d)]
            psi_0_vals.append(psi_t[0])
            psi_lin_vals.append(sum(c_vec[i] * psi_t[i] for i in range(d)))

        mean_psi_0 = sum(psi_0_vals) / n
        var_0 = sum((v - mean_psi_0) ** 2 for v in psi_0_vals) / (n * (n - 1))
        se_0 = math.sqrt(max(var_0, 1e-12))

        if abs(u_hat[0] - u_star[0]) <= 1.96 * se_0:
            wald_covered_0 += 1

        mean_psi_lin = sum(psi_lin_vals) / n
        var_lin = sum((v - mean_psi_lin) ** 2 for v in psi_lin_vals) / (n * (n - 1))
        z_lin = sum(c_vec[i] * (u_hat[i] - u_star[i]) for i in range(d)) / math.sqrt(max(var_lin, 1e-12))
        linear_form_z_scores.append(z_lin)

    mean_vanilla_sin = sum(vanilla_sin_thetas) / n_trials
    mean_deflated_sin = sum(deflated_sin_thetas) / n_trials
    coverage_95 = wald_covered_0 / n_trials
    lin_cov_95 = sum(1 for z in linear_form_z_scores if abs(z) <= 1.96) / n_trials

    assert mean_deflated_sin < mean_vanilla_sin, (
        f"Expected diagonal-deflated estimator ({mean_deflated_sin:.4f}) to outperform "
        f"vanilla diagonal-included estimator ({mean_vanilla_sin:.4f}) under heteroskedastic noise"
    )
    assert 0.88 <= coverage_95 <= 1.0, f"Expected ~95% coverage, got {coverage_95:.3f}"

    return {
        "dimension_d": d,
        "sample_size_n": n,
        "observation_prob_p": p_obs,
        "mean_vanilla_sin_theta": round(mean_vanilla_sin, 5),
        "mean_deflated_sin_theta": round(mean_deflated_sin, 5),
        "bias_reduction_ratio": round(mean_vanilla_sin / mean_deflated_sin, 3),
        "coordinate_0_wald_95_coverage": round(coverage_95, 4),
        "linear_form_95_coverage": round(lin_cov_95, 4),
    }


if __name__ == "__main__":
    result = run_simulation()
    print(json.dumps(result, indent=2))
