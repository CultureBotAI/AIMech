#!/usr/bin/env python3
"""Constructed boundary verification for Singularity, Misspecification, and Over-Specified Gaussian Mixture EM (Dwivedi et al. 2020)."""

import json
import math
import random


def weight_overspec(x, theta, pi_w, sigma2=1.0):
    # w_theta^pi(x) = pi exp(-||theta-x||^2/(2 sigma^2)) / (...) (Eq. 6)
    z = 2.0 * (theta * x) / sigma2
    if z >= 0:
        ez = math.exp(-z)
        return pi_w / (pi_w + (1.0 - pi_w) * ez)
    ez = math.exp(z)
    return (pi_w * ez) / (pi_w * ez + (1.0 - pi_w))


def pop_em_step_1d(grid_x, grid_w, theta, pi_w, sigma2=1.0):
    # M(theta) = E[(2 w_theta(X) - 1) X] for X ~ N(0, sigma^2) (Eq. 8)
    total = 0.0
    for x, w in zip(grid_x, grid_w):
        total += w * (2.0 * weight_overspec(x, theta, pi_w, sigma2) - 1.0) * x
    return total


def sample_em_step_1d(samples, theta, pi_w, sigma2=1.0):
    # M_n(theta) = (1/n) sum_i (2 w_theta(X_i) - 1) X_i (Eq. 9)
    n = len(samples)
    return sum((2.0 * weight_overspec(x, theta, pi_w, sigma2) - 1.0) * x for x in samples) / n


def main():
    # Build high-accuracy Gauss-Hermite / fine grid for N(0, 1) expectation
    num_pts = 801
    L = 8.0
    dx = 2.0 * L / (num_pts - 1)
    grid_x = [-L + i * dx for i in range(num_pts)]
    inv_sqrt2pi = 1.0 / math.sqrt(2.0 * math.pi)
    grid_w = [inv_sqrt2pi * math.exp(-0.5 * x * x) * dx for x in grid_x]
    # Probability p = P(|X| <= 1) + 0.5 P(|X| > 1) = (1 + P(|X| <= 1)) / 2 (Theorem 2, p. 15)
    prob_within_1 = math.erf(1.0 / math.sqrt(2.0))
    p_const = 0.5 * (1.0 + prob_within_1)

    # Scenario A: Unbalanced (pi = 0.2) vs. Balanced (pi = 0.5) Fisher information & population contraction (Theorems 1 & 2, Eq. 84)
    pi_unbal = 0.2
    rho_unbal = abs(1.0 - 2.0 * pi_unbal)
    fisher_beta_unbal = 1.0 - 4.0 * pi_unbal * (1.0 - pi_unbal)
    fisher_beta_bal = 1.0 - 4.0 * 0.5 * 0.5
    assert abs(fisher_beta_unbal - rho_unbal * rho_unbal) < 1e-12
    assert abs(fisher_beta_bal) < 1e-12

    theta_test = 0.35
    m_unbal = abs(pop_em_step_1d(grid_x, grid_w, theta_test, pi_unbal))
    ub_unbal = (1.0 - 0.5 * rho_unbal * rho_unbal) * theta_test
    assert m_unbal <= ub_unbal

    m_bal = abs(pop_em_step_1d(grid_x, grid_w, theta_test, 0.5))
    gamma_up = 1.0 - p_const + p_const / (1.0 + 0.5 * theta_test * theta_test)
    gamma_low = 1.0 / (1.0 + 2.0 * theta_test * theta_test)
    ratio_bal = m_bal / theta_test
    assert gamma_low <= ratio_bal <= gamma_up

    # Verify balanced contraction ratio approaches 1 as theta -> 0 (slow sub-geometric convergence, Eq. 14)
    theta_tiny = 0.05
    ratio_tiny = abs(pop_em_step_1d(grid_x, grid_w, theta_tiny, 0.5)) / theta_tiny
    assert ratio_tiny > 0.995

    # Scenario B: Annulus-based epoch localization exponent recursion alpha_{l+1} = alpha_l / 3 + 1/6 (Section 4.2, Eqs. 23 & 42a)
    alphas = [0.0]
    for _ in range(12):
        alphas.append(alphas[-1] / 3.0 + 1.0 / 6.0)
    assert abs(alphas[1] - 1.0 / 6.0) < 1e-12  # Naive one-shot rate (d/n)^{1/6}
    assert abs(alphas[-1] - 0.25) < 1e-6       # Sharp localized rate (d/n)^{1/4}

    # Scenario C: Sample EM n^{-1/2} (unbalanced) vs. n^{-1/4} (balanced) statistical error & Theorem 4 lower bound (Eqs. 54-59)
    rng = random.Random(20261019)
    n = 1200
    samples = [rng.gauss(0.0, 1.0) for _ in range(n)]
    emp_m2 = sum(x * x for x in samples) / n
    emp_m4 = sum((x * x) ** 2 for x in samples) / n
    # Ensure we test on Event B = { (1/n) sum Y_i^2 > 1 } (Eq. 59) by a tiny variance rescaling if needed
    if emp_m2 <= 1.02:
        scale_fac = math.sqrt(1.035 / emp_m2)
        samples = [x * scale_fac for x in samples]
        emp_m2 = sum(x * x for x in samples) / n
        emp_m4 = sum((x * x) ** 2 for x in samples) / n

    # Run unbalanced sample EM
    th_unbal = 0.8
    for _ in range(60):
        th_unbal = sample_em_step_1d(samples, th_unbal, pi_unbal)

    # Run balanced sample EM to fixed point hat_theta_n = (1/n) sum X_i tanh(hat_theta_n X_i) (Eq. 54)
    th_bal = 0.8
    for _ in range(400):
        th_bal = sample_em_step_1d(samples, th_bal, 0.5)

    # Verify Theorem 4 cubic lower bound (Eq. 56): |hat_theta_n|^2 >= 3 (emp_m2 - 1) / emp_m4
    thm4_lower_bound = math.sqrt(3.0 * (emp_m2 - 1.0) / emp_m4)
    assert abs(th_bal) >= thm4_lower_bound
    assert abs(th_unbal) < 0.25 * abs(th_bal)

    summary = {
        "fisher_beta_unbalanced": round(fisher_beta_unbal, 4),
        "fisher_beta_balanced": round(fisher_beta_bal, 4),
        "unbalanced_pop_ratio_at_0_35": round(m_unbal / theta_test, 5),
        "balanced_pop_ratio_at_0_35": round(ratio_bal, 5),
        "balanced_gamma_bounds_at_0_35": [round(gamma_low, 5), round(gamma_up, 5)],
        "balanced_pop_ratio_at_0_05": round(ratio_tiny, 6),
        "annulus_alpha_1_naive": round(alphas[1], 6),
        "annulus_alpha_12_localized": round(alphas[-1], 6),
        "sample_em_unbalanced_error": round(abs(th_unbal), 5),
        "sample_em_balanced_error": round(abs(th_bal), 5),
        "theorem4_balanced_fixed_point_lower_bound": round(thm4_lower_bound, 5),
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
