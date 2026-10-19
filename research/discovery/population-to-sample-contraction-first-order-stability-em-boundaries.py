#!/usr/bin/env python3
"""Constructed boundary verification for Population-to-Sample Contraction and First-Order Stability EM (Balakrishnan, Wainwright, & Yu 2017)."""

import json
import math
import random


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def norm2(u):
    return math.sqrt(dot(u, u))


def sub(u, v):
    return [x - y for x, y in zip(u, v)]


def add(u, v):
    return [x + y for x, y in zip(u, v)]


def scale(c, u):
    return [c * x for x in u]


def weight_gmm(y, theta, sigma2):
    # w_theta(y) = 1 / (1 + exp(-2 <theta, y> / sigma^2)) (Eq. 12)
    z = 2.0 * dot(theta, y) / sigma2
    if z >= 0:
        return 1.0 / (1.0 + math.exp(-z))
    ez = math.exp(z)
    return ez / (1.0 + ez)


def em_step_gmm(samples, theta, sigma2):
    # M_n(theta) = (1/n) sum_i (2 w_theta(y_i) - 1) y_i (Eq. 13a/14)
    n = len(samples)
    d = len(theta)
    out = [0.0] * d
    for y in samples:
        c = 2.0 * weight_gmm(y, theta, sigma2) - 1.0
        for j in range(d):
            out[j] += c * y[j] / n
    return out


def grad_em_step_gmm(samples, theta, sigma2, alpha):
    # G_n(theta) = theta + alpha * (M_n(theta) - theta) (Eq. 14)
    mn = em_step_gmm(samples, theta, sigma2)
    return [theta[j] + alpha * (mn[j] - theta[j]) for j in range(len(theta))]


def main():
    rng = random.Random(20261019)
    d = 4
    sigma = 1.0
    sigma2 = sigma * sigma
    # True parameter theta^* with SNR = ||theta^*||_2 / sigma = 2.5 (Section 4.1, Eq. 57)
    theta_star = [2.0, 1.5, 0.0, 0.0]
    snr = norm2(theta_star) / sigma

    # Scenario A: Population-level FOS(gamma) and geometric contraction (Theorems 1 & 3, Corollary 1)
    n_pop = 4000
    pop_samples = []
    for _ in range(n_pop):
        z_sign = 1.0 if rng.random() < 0.5 else -1.0
        y = [z_sign * theta_star[j] + rng.gauss(0.0, sigma) for j in range(d)]
        pop_samples.append(y)

    # Approximate population fixed point theta^*_pop = M_pop(theta^*)
    theta_pop_fp = theta_star[:]
    for _ in range(25):
        theta_pop_fp = em_step_gmm(pop_samples, theta_pop_fp, sigma2)

    # Initialize inside basin B_2(||theta^*||_2 / 4; theta^*) (Corollary 1, Eq. 58)
    r_basin = norm2(theta_star) / 4.0
    theta0 = add(theta_star, [0.35, -0.35, 0.25, -0.20])
    init_dist = norm2(sub(theta0, theta_star))
    assert init_dist <= r_basin

    # Check FOS ratio ||M(theta^0) - M(theta^*)||_2 / ||theta^0 - theta^*||_2 <= gamma < lambda = 1
    m_theta0 = em_step_gmm(pop_samples, theta0, sigma2)
    fos_gamma_emp = norm2(sub(m_theta0, theta_pop_fp)) / norm2(sub(theta0, theta_pop_fp))
    assert fos_gamma_emp < 0.35

    # Scenario B: Sample-based EM & Gradient EM geometric decay to statistical plateau (Theorem 2, Corollary 2)
    n_sample = 600
    samples = pop_samples[:n_sample]

    # Compute exact sample EM fixed point hat_theta_EM
    theta_em_fp = theta_star[:]
    for _ in range(60):
        theta_em_fp = em_step_gmm(samples, theta_em_fp, sigma2)

    theta_em = theta0[:]
    theta_gem = theta0[:]
    for _ in range(25):
        theta_em = em_step_gmm(samples, theta_em, sigma2)
    for _ in range(60):
        theta_gem = grad_em_step_gmm(samples, theta_gem, sigma2, alpha=0.5)

    opt_err_em = norm2(sub(theta_em, theta_em_fp))
    opt_err_gem = norm2(sub(theta_gem, theta_em_fp))
    stat_err_em = norm2(sub(theta_em, theta_star))
    stat_err_init = norm2(sub(theta0, theta_star))

    assert opt_err_em < 1e-11
    assert opt_err_gem < 1e-9
    assert stat_err_em < 0.35 * stat_err_init

    # Scenario C: Missing-covariate linear regression upper-SNR basin condition (Corollary 6, Eqs. 66-68)
    rho_miss = 0.15
    # Moderate SNR: xi_1 = 0.5, xi_2 = 0.2 => xi = (xi_1 + xi_2)^2 = 0.49
    xi_mod = (0.5 + 0.2) ** 2
    rho_max_mod = 1.0 / (1.0 + 2.0 * xi_mod * (1.0 + xi_mod))
    kappa_mod = (xi_mod + rho_miss * (1.0 + 2.0 * xi_mod * (1.0 + xi_mod))) / (1.0 + xi_mod)

    # Excessive SNR: xi_1 = 1.8, xi_2 = 0.2 => xi = 4.0, violating Eq. (67)
    xi_high = (1.8 + 0.2) ** 2
    rho_max_high = 1.0 / (1.0 + 2.0 * xi_high * (1.0 + xi_high))
    kappa_high = (xi_high + rho_miss * (1.0 + 2.0 * xi_high * (1.0 + xi_high))) / (1.0 + xi_high)

    assert rho_miss < rho_max_mod and kappa_mod < 1.0
    assert rho_miss > rho_max_high and kappa_high > 1.0

    summary = {
        "snr": round(snr, 4),
        "basin_radius": round(r_basin, 4),
        "init_dist": round(init_dist, 4),
        "empirical_fos_contraction_gamma": round(fos_gamma_emp, 5),
        "sample_em_opt_error": opt_err_em,
        "sample_grad_em_opt_error": opt_err_gem,
        "sample_em_stat_error": round(stat_err_em, 5),
        "missing_covariate_kappa_moderate_snr": round(kappa_mod, 5),
        "missing_covariate_kappa_excessive_snr": round(kappa_high, 5),
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
