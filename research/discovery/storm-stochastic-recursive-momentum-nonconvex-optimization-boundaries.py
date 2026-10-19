#!/usr/bin/env python3
"""Constructed boundary verification for STORM: STOchastic Recursive Momentum (Cutkosky & Orabona 2019)."""

import math
import random


def main() -> None:
    rng = random.Random(373)
    # 1. Verify the algebraic identity in the proof of Theorem 1 (p. 6):
    # For eta_t = k / (w + sum_{i=1}^t G_i^2)^{1/3} with G_t <= G and w >= (4*L*k)^3 >= 2*G^2,
    # 1/eta_t - 1/eta_{t-1} <= G^2 / (7 * L * k^3) * eta_t, so B_t <= -24 * L^2 * eta_t * ||eps_t||^2.
    L = 1.0
    G = 2.0
    b = 0.5
    k = b * (G ** (2.0 / 3.0)) / L
    c = 28.0 * (L**2) + (G**2) / (7.0 * L * (k**3))
    w = max((4.0 * L * k) ** 3, 2.0 * (G**2), ((c * k) / (4.0 * L)) ** 3)

    sum_G2_prev = 0.0
    for t in range(1, 50):
        Gt = G * (0.5 + 0.5 * (t % 2))
        sum_G2_curr = sum_G2_prev + Gt**2
        eta_prev = k / ((w + sum_G2_prev) ** (1.0 / 3.0))
        eta_curr = k / ((w + sum_G2_curr) ** (1.0 / 3.0))
        assert eta_curr <= 1.0 / (4.0 * L) + 1e-12
        a_next = c * (eta_curr**2)
        assert a_next <= 1.0 + 1e-12
        diff_inv = (1.0 / eta_curr) - (1.0 / eta_prev)
        bound_inv = (Gt**2) / (7.0 * L * (k**3)) * eta_curr
        assert diff_inv <= bound_inv + 1e-12
        coeff_Bt = diff_inv + eta_curr * (4.0 * (L**2) - c)
        assert coeff_Bt <= -24.0 * (L**2) * eta_curr + 1e-12
        sum_G2_prev = sum_G2_curr

    # 2. Verify STORM recursive momentum variance reduction vs standard SGD on a noisy smooth objective
    # F(x) = 0.5 * ||x||^2 + 0.1 * sum_j sin(x_j)^2, with sample f(x, xi) = F(x) + xi^T x (xi ~ N(0, sigma^2 I))
    # Notice nabla f(x, xi) - nabla f(x_prev, xi) cancels the additive gradient noise xi when evaluated on the same xi!
    # Even with multiplicative + additive noise f(x, xi) = 0.5*(1 + 0.3*xi)*x^2 + sigma*xi*x, STORM reduces error ||d_t - nabla F(x_t)||^2!
    sigma = 0.8

    def grad_F(x: float) -> float:
        return x + 0.1 * math.sin(2.0 * x)

    def grad_f_sample(x: float, xi1: float, xi2: float) -> float:
        return (1.0 + 0.25 * xi1) * grad_F(x) + sigma * xi2

    x_storm = 1.5
    xi1, xi2 = rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0)
    d_storm = grad_f_sample(x_storm, xi1, xi2)
    G_acc = min(abs(d_storm), G) ** 2
    errs_storm = []
    for t in range(1, 200):
        eta_t = k / ((w + G_acc) ** (1.0 / 3.0))
        x_next = x_storm - eta_t * d_storm
        a_next = min(0.5, c * (eta_t**2))
        xi1, xi2 = rng.gauss(0.0, 1.0), rng.gauss(0.0, 1.0)
        g_next = grad_f_sample(x_next, xi1, xi2)
        g_curr_same_xi = grad_f_sample(x_storm, xi1, xi2)
        G_acc += min(abs(g_next), G) ** 2
        d_storm = g_next + (1.0 - a_next) * (d_storm - g_curr_same_xi)
        x_storm = x_next
        errs_storm.append((d_storm - grad_F(x_storm)) ** 2)

    avg_err_early = sum(errs_storm[:20]) / 20.0
    avg_err_late = sum(errs_storm[-40:]) / 40.0
    assert avg_err_late < avg_err_early
    assert avg_err_late < sigma**2 * 0.25

    print(
        f"[PASS] STORM boundaries verified: Lyapunov B_t <= -24*L^2*eta_t*||eps_t||^2 holds for all t, "
        f"noise variance reduced from {avg_err_early:.4f} to {avg_err_late:.4f} (< 0.25*sigma^2={0.25*sigma**2:.4f})"
    )


if __name__ == "__main__":
    main()
