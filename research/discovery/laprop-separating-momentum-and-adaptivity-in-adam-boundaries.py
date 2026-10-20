#!/usr/bin/env python3
"""Boundary & mathematical verification for Round 605: LaProp (Ziyin, Wang, and Ueda, arXiv:2002.04839)."""

from __future__ import annotations

import math
import random


def verify_generalized_adaptive_momentum_framework() -> tuple[float, float, float]:
    """Verify Eqs. (5)-(7) (p. 3): Adam couples momentum via K_t = H_t^{-1} H_{t-1}, whereas LaProp sets K_t = I."""
    mu = 0.9
    nu = 0.9
    lam = 0.05
    # Consider un-bias-corrected form of Eqs. (5)-(7) on a 1D sequence with an impulse gradient at t=2
    grads = [1.0, 1.0, 50.0, 1.0]
    n_prev = 0.0
    m_adam = 0.0
    m_laprop = 0.0
    th_adam = [0.0]
    th_laprop = [0.0]
    H_hist = []

    max_eq6_err = 0.0
    max_eq7_err = 0.0
    for t_idx, g in enumerate(grads, start=1):
        n_cur = nu * n_prev + (1.0 - nu) * (g * g)
        H_cur = math.sqrt(n_cur)
        H_hist.append(H_cur)

        # Adam (un-bias-corrected form matching Eq. 5-6 where (1-mu) is absorbed into lam)
        m_adam = mu * m_adam + g
        th_adam_next = th_adam[-1] - lam * (m_adam / H_cur)
        if t_idx >= 2:
            H_prev = H_hist[-2]
            K_t = H_prev / H_cur
            rhs_eq6 = th_adam[-1] - lam * (g / H_cur) + mu * K_t * (th_adam[-1] - th_adam[-2])
            max_eq6_err = max(max_eq6_err, abs(th_adam_next - rhs_eq6))
        th_adam.append(th_adam_next)

        # LaProp (Eq. 7): K_t = 1
        m_laprop = mu * m_laprop + (g / H_cur)
        th_laprop_next = th_laprop[-1] - lam * m_laprop
        if t_idx >= 2:
            rhs_eq7 = th_laprop[-1] - lam * (g / H_cur) + mu * (th_laprop[-1] - th_laprop[-2])
            max_eq7_err = max(max_eq7_err, abs(th_laprop_next - rhs_eq7))
        th_laprop.append(th_laprop_next)
        n_prev = n_cur

    # At impulse step t=3 (g=50), H_3/H_2 spikes, so Adam's K_3 = H_2/H_3 << 1 damps prior momentum by ~37x
    K_impulse = H_hist[1] / H_hist[2]
    assert max_eq6_err < 1e-15, f"Eq. 6 identity error too large: {max_eq6_err}"
    assert max_eq7_err < 1e-15, f"Eq. 7 identity error too large: {max_eq7_err}"
    assert K_impulse < 0.05, f"Expected Adam momentum attenuation K_t << 1 on impulse gradient, got {K_impulse}"
    return max_eq6_err, max_eq7_err, K_impulse


def verify_propositions_1_and_2_and_ssg_interpolation() -> tuple[float, float, float]:
    """Verify Propositions 1 & 2 (p. 6, 14) and Section 3 interpolation to Signed Stochastic Gradient (p. 4-5)."""
    # 1. Proposition 1: For ANY mu, nu in [0, 1) and arbitrary gradients, |m_t / c_m(t)| <= 1 / sqrt(1 - nu)
    # 2. Proposition 2: When mu > sqrt(nu) (violating Adam's condition mu < sqrt(nu)), Adam update exceeds 1/sqrt(1-nu)
    mu = 0.95
    nu = 0.25  # sqrt(nu) = 0.5 < mu = 0.95
    eps = 1e-15
    prop1_bound = 1.0 / math.sqrt(1.0 - nu)

    # Sequence of gradients starting large and decaying geometrically so Adam's denominator shrinks faster than numerator
    m_la = 0.0
    n_la = 0.0
    m_ad = 0.0
    n_ad = 0.0
    max_la_ratio = 0.0
    max_ad_ratio = 0.0

    for t in range(1, 40):
        g = 1.0 if t == 1 else (0.51 ** (t - 1))
        cn = 1.0 - (nu ** t)
        cm = 1.0 - (mu ** t)
        n_la = nu * n_la + (1.0 - nu) * (g * g)
        m_la = mu * m_la + (1.0 - mu) * (g / (math.sqrt(n_la / cn) + eps))
        upd_la = abs(m_la / cm)
        max_la_ratio = max(max_la_ratio, upd_la / prop1_bound)

        n_ad = nu * n_ad + (1.0 - nu) * (g * g)
        m_ad = mu * m_ad + (1.0 - mu) * g
        upd_ad = abs((m_ad / cm) / (math.sqrt(n_ad / cn) + eps))
        max_ad_ratio = max(max_ad_ratio, upd_ad / prop1_bound)

    assert max_la_ratio <= 1.0 + 1e-12, f"Proposition 1 violated: max_la_ratio={max_la_ratio}"
    assert max_ad_ratio > 20.0, f"Expected Adam to blow up when mu > sqrt(nu), got ratio {max_ad_ratio}"

    # 3. Section 3: At nu = 0, LaProp exactly equals Signed Stochastic Gradient with Momentum (SSG-M)
    rng = random.Random(605)
    m_nu0 = 0.0
    m_ssg = 0.0
    ssg_err = 0.0
    for t in range(1, 25):
        g = rng.uniform(-5.0, 5.0)
        if abs(g) < 0.1:
            g = 0.5
        # LaProp with nu = 0, eps = 0: n_t = g_t^2, c_n = 1
        n_t = g * g
        m_nu0 = mu * m_nu0 + (1.0 - mu) * (g / math.sqrt(n_t))
        m_ssg = mu * m_ssg + (1.0 - mu) * (1.0 if g > 0 else -1.0)
        ssg_err = max(ssg_err, abs(m_nu0 - m_ssg))

    assert ssg_err < 1e-15, f"SSG-M interpolation error at nu=0: {ssg_err}"
    return max_la_ratio, max_ad_ratio, ssg_err


def verify_noisy_rosenbrock_and_extensions() -> tuple[float, float, float]:
    """Verify Section 5.1 Noisy Rosenbrock stability at small nu (p. 7) and Appendix B.3-B.5 extensions (p. 18-19)."""
    # Noisy Rosenbrock: l(x,y) = (1 - (x + e1))^2 + 100 * ((y + e2) - (x + e1)^2)^2
    rng_la = random.Random(2020)
    rng_ad = random.Random(2020)
    sigma = 0.10
    lr = 0.01
    mu = 0.9
    nu = 0.1  # small nu regime where Adam fails due to mu > sqrt(nu) and noise
    eps = 1e-8

    def run_rosenbrock(mode: str, rng: random.Random) -> float:
        x, y = 0.0, 0.0
        mx, my = 0.0, 0.0
        nx, ny = 0.0, 0.0
        best_clean = float("inf")
        for t in range(1, 3001):
            e1 = rng.uniform(-sigma, sigma)
            e2 = rng.uniform(-sigma, sigma)
            u = x + e1
            v = y + e2
            gx = -2.0 * (1.0 - u) - 400.0 * u * (v - u * u)
            gy = 200.0 * (v - u * u)
            cn = 1.0 - (nu ** t)
            cm = 1.0 - (mu ** t)
            nx = nu * nx + (1.0 - nu) * (gx * gx)
            ny = nu * ny + (1.0 - nu) * (gy * gy)
            if mode == "laprop":
                mx = mu * mx + (1.0 - mu) * (gx / (math.sqrt(nx / cn) + eps))
                my = mu * my + (1.0 - my) * 0.0 + (1.0 - mu) * (gy / (math.sqrt(ny / cn) + eps))
                x -= lr * (mx / cm)
                y -= lr * (my / cm)
            else:
                mx = mu * mx + (1.0 - mu) * gx
                my = mu * my + (1.0 - mu) * gy
                x -= lr * (mx / cm) / (math.sqrt(nx / cn) + eps)
                y -= lr * (my / cm) / (math.sqrt(ny / cn) + eps)
            clean = (1.0 - x) ** 2 + 100.0 * ((y - x * x) ** 2)
            if clean < best_clean:
                best_clean = clean
        return best_clean

    loss_la = run_rosenbrock("laprop", rng_la)
    loss_ad = run_rosenbrock("adam", rng_ad)
    assert loss_la < 0.1, f"Expected LaProp to converge (<0.1) on noisy Rosenbrock, got {loss_la}"
    assert loss_la < loss_ad, f"Expected LaProp ({loss_la}) < Adam ({loss_ad})"

    # Verify Centered LaProp (Algorithm 4, p. 19) non-negative variance n_t - n_bar_t^2 >= 0 by Cauchy-Schwarz
    n_t = 0.0
    n_bar = 0.0
    min_var = 0.0
    for t, g in enumerate([1.2, -0.7, 2.3, 0.4, -1.5, 0.8], start=1):
        n_t = 0.9 * n_t + 0.1 * (g * g)
        n_bar = 0.9 * n_bar + 0.1 * g
        cn = 1.0 - (0.9 ** t)
        # Bias-corrected second moment E[g^2] - (E[g])^2 = n_t/cn - (n_bar/cn)^2 >= 0;
        # and even unnormalized n_t - n_bar^2 >= 0 since sum w_i = 1 - 0.9^t <= 1
        var_est = (n_t - n_bar * n_bar) / cn
        min_var = min(min_var, var_est)
    assert min_var >= -1e-15, f"Centered LaProp variance became negative: {min_var}"
    return loss_la, loss_ad, min_var


def main() -> None:
    eq6_err, eq7_err, k_imp = verify_generalized_adaptive_momentum_framework()
    la_ratio, ad_ratio, ssg_err = verify_propositions_1_and_2_and_ssg_interpolation()
    loss_la, loss_ad, min_var = verify_noisy_rosenbrock_and_extensions()
    print(
        f"[PASS] Round 605 LaProp verified: eq6_err={eq6_err:.2e}, eq7_err={eq7_err:.2e}, "
        f"K_impulse={k_imp:.4f}, prop1_ratio={la_ratio:.4f}<=1, prop2_viol={ad_ratio:.1f}, "
        f"ssg_err={ssg_err:.2e}, rosenbrock=(LaProp:{loss_la:.4f}<Adam:{loss_ad:.4f}), min_var={min_var:.2e}"
    )


if __name__ == "__main__":
    main()
