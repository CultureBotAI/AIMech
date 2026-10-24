#!/usr/bin/env python3
"""Constructed boundary verification for RGD-Mult (Robust descent using smoothed multiplicative noise, Holland 2019, arXiv:1810.06207)."""

import json
import math


def std_normal_cdf(u):
    """Standard Normal cumulative distribution function Phi(u)."""
    return 0.5 * (1.0 + math.erf(u / math.sqrt(2.0)))


def catoni_giulini_psi(u):
    """Catoni-Giulini soft truncation function psi(u) (Eq. 4)."""
    rt2 = math.sqrt(2.0)
    if u > rt2:
        return 2.0 * rt2 / 3.0
    if u < -rt2:
        return -2.0 * rt2 / 3.0
    return u - (u ** 3) / 6.0


def correction_c(a, b):
    """Closed-form Gaussian noise-smoothing correction C(a, b) (Appendix A.3, p. 33)."""
    if b <= 1e-12:
        return 0.0
    rt2 = math.sqrt(2.0)
    rt2pi = math.sqrt(2.0 * math.pi)
    v_minus = (rt2 - a) / b
    v_plus = (rt2 + a) / b
    f_minus = std_normal_cdf(-v_minus)
    f_plus = std_normal_cdf(-v_plus)
    e_minus = math.exp(-0.5 * v_minus * v_minus)
    e_plus = math.exp(-0.5 * v_plus * v_plus)

    t1 = (2.0 * rt2 / 3.0) * (f_minus - f_plus)
    t2 = -(a - (a ** 3) / 6.0) * (f_minus + f_plus)
    t3 = (b / rt2pi) * (1.0 - 0.5 * a * a) * (e_plus - e_minus)
    t4 = 0.5 * a * b * b * (f_plus + f_minus + (1.0 / rt2pi) * (v_plus * e_plus + v_minus * e_minus))
    t5 = (b ** 3) / (6.0 * rt2pi) * ((2.0 + v_minus * v_minus) * e_minus - (2.0 + v_plus * v_plus) * e_plus)
    return t1 + t2 + t3 + t4 + t5


def rgdmult_estimate(grads, v_bound, delta=0.05, beta=2.0):
    """Algorithm 1 (p. 6): Smoothed multiplicative-noise robust gradient coordinate estimator."""
    n = len(grads)
    s = math.sqrt(n * v_bound / (2.0 * math.log(1.0 / delta)))
    total = 0.0
    for g in grads:
        a = g / s
        b = abs(g) / (s * math.sqrt(beta))
        main_term = g * (1.0 - (g * g) / (2.0 * s * s * beta)) - (g ** 3) / (6.0 * s * s)
        corr_term = s * correction_c(a, b)
        total += (main_term + corr_term) / n
    return total, s


def lipschitz_factor_c_nu(beta):
    """Lemma 7 (p. 9): Folded-Normal Lipschitz factor c_nu."""
    return 1.0 - 2.0 * std_normal_cdf(-math.sqrt(beta)) + math.sqrt(2.0 / (beta * math.pi)) * math.exp(-0.5 * beta)


def main():
    # 1. Verify Eq. (10) polynomial logarithmic sandwich for Catoni-Giulini psi(u)
    for u in [-1.2, -0.5, 0.0, 0.5, 1.2]:
        val = catoni_giulini_psi(u)
        lower = -math.log(1.0 - u + 0.5 * u * u)
        upper = math.log(1.0 + u + 0.5 * u * u)
        assert lower - 1e-12 <= val <= upper + 1e-12

    # 2. Verify robustness against heavy-tailed outlier gradient vs. sample mean (ERM-GD)
    # True gradient = 1.0; 19 clean samples near 1.0 and 1 extreme heavy-tailed outlier at +80.0
    grads = [1.0] * 19 + [80.0]
    true_g = 1.0
    erm_mean = sum(grads) / len(grads)
    g_hat, s_scale = rgdmult_estimate(grads, v_bound=2.0, delta=0.05, beta=2.0)

    err_erm = abs(erm_mean - true_g)
    err_rgd = abs(g_hat - true_g)
    assert err_rgd < err_erm * 0.25

    # 3. Verify Lemma 7 Lipschitz property |x_hat(x) - x_hat(x')| <= (c_nu / n) * ||x - x'||_1
    grads_perturbed = [1.0] * 19 + [85.0]
    g_hat_p, _ = rgdmult_estimate(grads_perturbed, v_bound=2.0, delta=0.05, beta=2.0)
    c_nu = lipschitz_factor_c_nu(beta=2.0)
    l1_diff = sum(abs(x - y) for x, y in zip(grads, grads_perturbed))
    lip_bound = (c_nu / len(grads)) * l1_diff
    assert abs(g_hat - g_hat_p) <= lip_bound + 1e-9

    summary = {
        "concept": "RGDMultRobustDescentUsingSmoothedMultiplicativeNoise",
        "erm_gradient_error": round(err_erm, 5),
        "rgdmult_gradient_error": round(err_rgd, 5),
        "scale_s": round(s_scale, 5),
        "lipschitz_c_nu": round(c_nu, 5),
        "eq10_sandwich_verified": True,
        "verification": "passed",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
