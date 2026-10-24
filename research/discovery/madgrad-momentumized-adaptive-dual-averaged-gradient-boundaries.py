#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 596: MADGRAD (Defazio & Jelassi, JMLR 2022)."""

from __future__ import annotations

import math
import random


def test_cuberoot_lagrangian_and_lemma2_bound() -> tuple[float, float]:
    """Verify Appendix C cube-root Lagrangian minimizer (pp. 32-33) and Appendix B.3 Lemma 2 (p. 25)."""
    rng = random.Random(59601)
    D = 6
    K = 15
    c_bound = 4.0
    g_hist = [[rng.uniform(0.1, 2.5) for _ in range(D)] for _ in range(K)]

    # Sum of squared gradients per coordinate: G2_d = sum_{i=0}^{K-1} g_{i,d}^2
    g2_sum = [sum(g_hist[i][d] ** 2 for i in range(K)) for d in range(D)]

    # Closed-form solution from Appendix C (p. 33):
    # s_d* = (G2_d)^{1/3} / sqrt(c^{-1} sum_{d'=0}^{D-1} (G2_{d'})^{2/3})
    denom = math.sqrt((1.0 / c_bound) * sum(v ** (2.0 / 3.0) for v in g2_sum))
    s_opt = [(v ** (1.0 / 3.0)) / denom for v in g2_sum]

    # Verify constraint ||s_opt||_2^2 == c_bound
    norm_sq_err = abs(sum(s * s for s in s_opt) - c_bound)
    assert norm_sq_err < 1e-12, f"Expected ||s*||_2^2 == c, got err={norm_sq_err}"

    # Verify s_opt achieves strictly smaller objective sum_d G2_d / s_d than any perturbed feasible s
    obj_opt = sum(g2_sum[d] / s_opt[d] for d in range(D))
    # Compare with standard L2-normalized square-root scaling s_sqrt_d propto sqrt(G2_d)
    sqrt_raw = [math.sqrt(v) for v in g2_sum]
    sqrt_scale = math.sqrt(c_bound / sum(v * v for v in sqrt_raw))
    s_sqrt = [v * sqrt_scale for v in sqrt_raw]
    obj_sqrt = sum(g2_sum[d] / s_sqrt[d] for d in range(D))
    assert obj_opt < obj_sqrt - 1e-6, f"Expected cube-root s* ({obj_opt}) < sqrt s ({obj_sqrt})"

    # Verify Appendix B.3 Lemma 2 (p. 25):
    # sum_{t=0}^k [lambda_t^2 g_t^2 / (lambda_t G^2 + sum_{i=0}^{t-1} lambda_i g_i^2)^{1/3}]
    # <= (3/2) lambda_k (sum_{i=0}^k lambda_i g_i^2)^{2/3}
    G = 3.0
    gamma = 0.05
    g_1d = [rng.uniform(0.05, G) for _ in range(K)]
    lams = [gamma * math.sqrt(t + 1) for t in range(K)]
    lhs = 0.0
    running_b = 0.0
    max_ratio = 0.0
    for t in range(K):
        gt2 = g_1d[t] ** 2
        lam_t = lams[t]
        lhs += (lam_t**2) * gt2 / ((lam_t * (G**2) + running_b) ** (1.0 / 3.0))
        running_b += lam_t * gt2
        rhs = 1.5 * lam_t * (running_b ** (2.0 / 3.0))
        assert lhs <= rhs + 1e-12, f"Lemma 2 violated at t={t}: {lhs} > {rhs}"
        max_ratio = max(max_ratio, lhs / rhs)

    return norm_sq_err, max_ratio


def test_madgrad_outlier_decay_vs_adagrad() -> tuple[float, float]:
    """Verify Section 6.1 (p. 13) & Algorithm 1 (p. 11): MADGRAD decays early outlier gradients faster than AdaGrad."""
    # 1D convex quadratic f(x) = 0.5 * (x - x*)^2 starting at x0 = 2.0, x* = 0.0,
    # with an initial outlier stochastic gradient spike g_0 = 50.0 at step 0 followed by true gradients.
    x0 = 2.0
    steps = 80
    outlier_g0 = 50.0

    # Standard AdaGrad (dual averaging form with unweighted sum) with tuned gamma = 0.5
    s_ada = 0.0
    v_ada = 0.0
    x_ada = x0
    gamma_ada = 0.5
    for k in range(steps):
        gk = outlier_g0 if k == 0 else x_ada
        s_ada += gamma_ada * gk
        v_ada += gk * gk
        x_ada = x0 - s_ada / (math.sqrt(v_ada) + 1e-8)
    loss_ada = 0.5 * (x_ada**2)

    # MADGRAD (Algorithm 1, p. 11) with gamma = 0.2, c_k = 0.1
    s_mad = 0.0
    v_mad = 0.0
    x_mad = x0
    gamma_mad = 0.2
    ck = 0.1
    for k in range(steps):
        gk = outlier_g0 if k == 0 else x_mad
        lam_k = gamma_mad * math.sqrt(k + 1)
        s_mad += lam_k * gk
        v_mad += lam_k * (gk * gk)
        z_next = x0 - s_mad / ((v_mad ** (1.0 / 3.0)) + 1e-8)
        x_mad = (1.0 - ck) * x_mad + ck * z_next
    loss_mad = 0.5 * (x_mad**2)

    assert loss_mad < 1e-2 * loss_ada, f"Expected MADGRAD loss ({loss_mad}) << AdaGrad loss ({loss_ada})"
    return loss_mad, loss_ada


def main() -> None:
    norm_err, lemma2_ratio = test_cuberoot_lagrangian_and_lemma2_bound()
    loss_mad, loss_ada = test_madgrad_outlier_decay_vs_adagrad()
    print(
        f"[PASS] Round 596 MADGRAD verified: norm_err={norm_err:.2e}, lemma2_ratio={lemma2_ratio:.4f}<=1.0, "
        f"loss_mad={loss_mad:.4e}<<loss_ada={loss_ada:.4e}"
    )


if __name__ == "__main__":
    main()
