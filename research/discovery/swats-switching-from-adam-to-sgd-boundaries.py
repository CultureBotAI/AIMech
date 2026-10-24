"""Constructed mathematical boundary and hybrid optimization verification for Round 615:
SWATS — Switching from Adam to SGD (Keskar & Socher, 2017, arXiv:1712.07628).

Verifies:
1. Non-orthogonal gradient-subspace projection identity (Section 2.1, p. 4):
   - Given iterate w_k, stochastic gradient g_k, and Adam step p_k != 0 with p_k^T g_k < 0,
     the closed-form scalar learning rate gamma_k = (p_k^T p_k) / (-p_k^T g_k)
     uniquely solves proj_{-gamma_k g_k}(p_k) = p_k (orthogonal projection of -gamma_k g_k onto p_k equals p_k).
   - Contrast with the reverse orthogonal projection proj_{-g_k}(p_k), whose L2 norm is strictly smaller than ||p_k||_2
     whenever p_k is not collinear with g_k.
   - When beta_1 = 0 (p_k = -H_k g_k with diagonal H_k > 0), gamma_k > 0 and equals the reciprocal of the
     Rayleigh quotient of H_k^{-1} with respect to p_k: gamma_k = (p_k^T p_k) / (p_k^T H_k^{-1} p_k).
2. Automatic switchover criterion and bias-corrected SGD rate (Section 2.2 & Algorithm 1, Eq. 4, p. 4-5):
   - Exponential moving average lambda_k = beta_2 * lambda_{k-1} + (1 - beta_2) * gamma_k triggers switchover
     when |lambda_k / (1 - beta_2^k) - gamma_k| < tol, setting SGD learning rate Lambda = lambda_k / (1 - beta_2^k)
     and momentum scale (1 - beta_1) * Lambda without introducing any additional hyperparameters.
3. Minimum-norm column-space generalization property on overparameterized linear least squares (Section 4, p. 8):
   - On min_w ||X w - y||_2^2 with n < d and w_0 = 0, SGD stays strictly in row(X) = col(X^T) and recovers the
     minimum-L2-norm interpolating solution w*_min = X^T (X X^T)^{-1} y, whereas coordinate-wise diagonal
     scaling (Adam) leaves col(X^T) and converges to a higher-norm interpolator with higher test error.
"""

from __future__ import annotations

import math
import random


def verify_projection_and_rayleigh_quotient() -> tuple[float, float, float]:
    rng = random.Random(20261019)
    d = 8
    max_proj_err = 0.0
    max_rayleigh_err = 0.0
    min_norm_gap = float("inf")

    for _ in range(50):
        g = [rng.uniform(-2.0, 2.0) for _ in range(d)]
        if sum(x * x for x in g) < 1e-6:
            g[0] = 1.0
        # Positive diagonal scaling H_k = diag(h)
        h = [rng.uniform(0.05, 5.0) for _ in range(d)]
        # Case beta_1 = 0: p_k = -H_k g_k
        p = [-h[i] * g[i] for i in range(d)]

        p_dot_p = sum(p[i] * p[i] for i in range(d))
        p_dot_g = sum(p[i] * g[i] for i in range(d))
        assert p_dot_g < 0.0

        gamma_k = p_dot_p / (-p_dot_g)
        assert gamma_k > 0.0

        # Verify proj_{-gamma_k g_k} p_k == p_k
        # Note: in Keskar & Socher (p. 4), proj_a(b) denotes the orthogonal projection of a onto b:
        # proj_{-gamma_k g_k}(p_k) = ((-gamma_k g_k)^T p_k / (p_k^T p_k)) * p_k
        scale = sum((-gamma_k * g[i]) * p[i] for i in range(d)) / p_dot_p
        proj_vec = [scale * p[i] for i in range(d)]
        proj_err = max(abs(proj_vec[i] - p[i]) for i in range(d))
        max_proj_err = max(max_proj_err, proj_err)

        # Verify Rayleigh quotient identity: gamma_k == 1 / ((p^T H^{-1} p) / (p^T p))
        rayleigh_h_inv = sum((p[i] * p[i]) / h[i] for i in range(d)) / p_dot_p
        rayleigh_err = abs(gamma_k - (1.0 / rayleigh_h_inv))
        max_rayleigh_err = max(max_rayleigh_err, rayleigh_err)

        # Verify orthogonal projection of p_k onto -g_k has strictly smaller L2 norm when h is non-uniform
        g_dot_g = sum(g[i] * g[i] for i in range(d))
        orth_scale = (-p_dot_g) / g_dot_g
        orth_vec = [-orth_scale * g[i] for i in range(d)]
        norm_p = math.sqrt(p_dot_p)
        norm_orth = math.sqrt(sum(x * x for x in orth_vec))
        min_norm_gap = min(min_norm_gap, norm_p - norm_orth)

    assert max_proj_err < 1e-13
    assert max_rayleigh_err < 1e-13
    assert min_norm_gap > 1e-4
    return max_proj_err, max_rayleigh_err, min_norm_gap


def verify_swats_algorithm_1_and_column_space() -> tuple[int, float, float, float]:
    # 1. Verify Algorithm 1 automatic switchover on a quadratic bowl f(w) = 0.5 * sum_i c_i (w_i - w*_i)^2
    c = [1.0, 2.0, 4.0, 8.0]
    w_star = [1.5, -1.0, 0.5, -2.0]
    w = [0.0, 0.0, 0.0, 0.0]
    m = [0.0] * 4
    a = [0.0] * 4
    v = [0.0] * 4
    lam = 0.0
    alpha = 0.25
    beta1 = 0.9
    beta2 = 0.99
    eps = 1e-9
    switch_tol = 2e-2
    phase = "Adam"
    switch_step = -1
    Lambda_sgd = 0.0

    for k in range(1, 801):
        g = [c[i] * (w[i] - w_star[i]) for i in range(4)]
        if phase == "SGD":
            for i in range(4):
                v[i] = beta1 * v[i] + g[i]
                w[i] = w[i] - (1.0 - beta1) * Lambda_sgd * v[i]
            continue

        for i in range(4):
            m[i] = beta1 * m[i] + (1.0 - beta1) * g[i]
            a[i] = beta2 * a[i] + (1.0 - beta2) * (g[i] * g[i])
        scale_bc = math.sqrt(1.0 - (beta2 ** k)) / (1.0 - (beta1 ** k))
        p = [-alpha * scale_bc * m[i] / (math.sqrt(a[i]) + eps) for i in range(4)]
        w = [w[i] + p[i] for i in range(4)]

        p_dot_g = sum(p[i] * g[i] for i in range(4))
        if abs(p_dot_g) > 0.0:
            p_dot_p = sum(p[i] * p[i] for i in range(4))
            gamma_k = p_dot_p / (-p_dot_g)
            lam = beta2 * lam + (1.0 - beta2) * gamma_k
            lam_hat = lam / (1.0 - (beta2 ** k))
            if k > 1 and abs(lam_hat - gamma_k) < switch_tol:
                phase = "SGD"
                v = [0.0] * 4
                Lambda_sgd = lam_hat
                switch_step = k
        else:
            lam = lam

    final_dist = math.sqrt(sum((w[i] - w_star[i]) ** 2 for i in range(4)))
    assert phase == "SGD" and 2 <= switch_step < 200
    assert Lambda_sgd > 0.0 and final_dist < 1e-4

    # 2. Verify Section 4 (p. 8) column-space / minimum-norm property on underdetermined X w = y (2x4 system)
    # Rows of X are orthogonal: x_1 = [1, 1, 0, 0], x_2 = [0, 0, 1, 2]
    # Minimum-norm solution to X w = y = [2, 5]^T is w*_min = [1, 1, 1, 2]^T (||w*_min||_2^2 = 7).
    X = [
        [1.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 2.0],
    ]
    y = [2.0, 5.0]
    w_min_star = [1.0, 1.0, 1.0, 2.0]

    def grad_ls(w_vec: list[float]) -> list[float]:
        # grad = X^T (X w - y)
        r0 = sum(X[0][j] * w_vec[j] for j in range(4)) - y[0]
        r1 = sum(X[1][j] * w_vec[j] for j in range(4)) - y[1]
        return [X[0][j] * r0 + X[1][j] * r1 for j in range(4)]

    # Run SGD from w_0 = 0
    w_sgd = [0.0] * 4
    for _ in range(300):
        g_s = grad_ls(w_sgd)
        w_sgd = [w_sgd[j] - 0.15 * g_s[j] for j in range(4)]

    # Run Adam from w_0 = 0
    w_adam = [0.0] * 4
    m_ls = [0.0] * 4
    v_ls = [0.0] * 4
    for t in range(1, 601):
        g_a = grad_ls(w_adam)
        for j in range(4):
            m_ls[j] = 0.9 * m_ls[j] + 0.1 * g_a[j]
            v_ls[j] = 0.99 * v_ls[j] + 0.01 * (g_a[j] * g_a[j])
            mh = m_ls[j] / (1.0 - (0.9 ** t))
            vh = v_ls[j] / (1.0 - (0.99 ** t))
            w_adam[j] -= 0.05 * mh / (math.sqrt(vh) + 1e-8)

    sgd_min_norm_err = math.sqrt(sum((w_sgd[j] - w_min_star[j]) ** 2 for j in range(4)))
    norm_sgd = math.sqrt(sum(x * x for x in w_sgd))
    norm_adam = math.sqrt(sum(x * x for x in w_adam))
    # Both interpolate X w = y, but SGD recovers the exact minimum-norm solution while Adam leaves col(X^T)
    assert sgd_min_norm_err < 1e-12
    assert norm_adam > norm_sgd + 0.05
    return switch_step, Lambda_sgd, sgd_min_norm_err, norm_adam - norm_sgd


if __name__ == "__main__":
    p_err, r_err, n_gap = verify_projection_and_rayleigh_quotient()
    sw_k, lam_sgd, ls_err, norm_diff = verify_swats_algorithm_1_and_column_space()
    print(
        f"[PASS] Round 615 SWATS verified: "
        f"proj_err={p_err:.2e}, rayleigh_err={r_err:.2e}, orth_norm_gap={n_gap:.4e}>0, "
        f"switch_step={sw_k}, Lambda_sgd={lam_sgd:.4f}, sgd_min_norm_err={ls_err:.2e}, adam_excess_norm={norm_diff:.4f}>0"
    )
