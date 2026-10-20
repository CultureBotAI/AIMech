#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 650:
IVON (Improved Variational Online Newton)
Primary source: Shen et al. (ICML 2024, PMLR v235:44665-44686, arXiv:2402.17641).
"""

import math
import random


def verify_stein_reparameterization_hessian_identity_eq_3():
    """Verify Eq. (3): Under q(theta) = N(m, diag(sigma)^2), Stein's identity ensures
    E_{theta ~ q}[grad ell(theta) * (theta - m) / sigma^2] == E_{theta ~ q}[diag(nabla^2 ell(theta))]
    for a quadratic loss ell(theta) = 0.5 * (theta - c)^T H (theta - c), and remains well-defined
    even for non-twice-differentiable piecewise-linear losses (e.g. ReLU / absolute value)."""
    # Exact analytical identity check on 1D non-smooth loss ell(theta) = |theta| where m = 0.3, sigma = 0.5:
    # Second derivative of E_{theta ~ N(m, sigma^2)}[|theta|] w.r.t. m is 2 * N(0 | m, sigma^2)
    m = 0.3
    sigma = 0.5
    analytic_smoothed_hess = 2.0 * (1.0 / (math.sqrt(2.0 * math.pi) * sigma)) * math.exp(
        -0.5 * (m / sigma) ** 2
    )
    # Gauss-Hermite / deterministic grid integration of Stein estimator g(theta)*(theta - m)/sigma^2
    # where g(theta) = sign(theta)
    n_grid = 20000
    z_min, z_max = -6.0, 6.0
    dz = (z_max - z_min) / n_grid
    stein_integral = 0.0
    for i in range(n_grid):
        z = z_min + (i + 0.5) * dz
        theta = m + sigma * z
        g = 1.0 if theta >= 0.0 else -1.0
        pdf = (1.0 / math.sqrt(2.0 * math.pi)) * math.exp(-0.5 * z * z)
        stein_integral += (g * (theta - m) / (sigma * sigma)) * pdf * dz

    assert abs(stein_integral - analytic_smoothed_hess) < 1e-3


def verify_riemannian_positivity_update_eq_4_alg_1():
    """Verify Eq. (4) & Algorithm 1 line 5:
    h_{t} = beta2 * h + (1 - beta2) * h_hat + 0.5 * (1 - beta2)^2 * (h - h_hat)^2 / (h + delta)
    guarantees h_t > 0 for all h > 0, delta >= 0, beta2 in (0, 1), even when h_hat is arbitrarily negative."""
    h = 0.25
    delta = 1e-4
    beta2 = 0.9
    rho = 1.0 - beta2

    for h_hat in [-100.0, -5.0, -0.5, -0.1, 0.0, 0.5, 10.0]:
        # Naive EMA can become negative when h_hat < -beta2/(1-beta2) * h
        h_ema = beta2 * h + rho * h_hat
        # IVON Riemannian update (Algorithm 1 line 5)
        h_ivon = beta2 * h + rho * h_hat + 0.5 * (rho ** 2) * ((h - h_hat) ** 2) / (h + delta)
        assert h_ivon > 0.0
        if h_hat == -5.0:
            assert h_ema < 0.0 and h_ivon > 0.0


def verify_ivon_gaussian_variational_convergence():
    """Verify Algorithm 1 converges to the exact variational Gaussian posterior
    m* = (H + delta I)^{-1} H theta_true, sigma*^2 = 1 / (lambda * (h* + delta))
    on a quadratic objective bar_ell(theta) = 0.5 * sum_i curvature_i * (theta_i - target_i)^2."""
    rng = random.Random(42)
    curv = [2.0, 5.0]
    target = [1.5, -1.0]
    lam = 100.0
    delta = 0.1
    beta1 = 0.9
    beta2 = 0.99
    h0 = 1.0

    m = [0.0, 0.0]
    h = [h0, h0]
    g = [0.0, 0.0]
    sigma = [1.0 / math.sqrt(lam * (hi + delta)) for hi in h]

    for t in range(1, 1501):
        alpha_t = 0.15 * (1.0 - t / 1600.0)
        # Unit-variance antithetic perturbations (+1, -1) with E[eps] = 0, E[eps^2] = 1
        eps = [1.0, 1.0]
        g_hat = [0.0, 0.0]
        h_hat = [0.0, 0.0]
        for sign in (+1.0, -1.0):
            theta = [m[i] + sign * sigma[i] * eps[i] for i in range(2)]
            grad = [curv[i] * (theta[i] - target[i]) for i in range(2)]
            for i in range(2):
                g_hat[i] += 0.5 * grad[i]
                h_hat[i] += 0.5 * grad[i] * (theta[i] - m[i]) / (sigma[i] ** 2)

        for i in range(2):
            g[i] = beta1 * g[i] + (1.0 - beta1) * g_hat[i]
            h[i] = (
                beta2 * h[i]
                + (1.0 - beta2) * h_hat[i]
                + 0.5 * ((1.0 - beta2) ** 2) * ((h[i] - h_hat[i]) ** 2) / (h[i] + delta)
            )
            g_bar = g[i] / (1.0 - (beta1 ** t))
            m[i] = m[i] - alpha_t * (g_bar + delta * m[i]) / (h[i] + delta)
            sigma[i] = 1.0 / math.sqrt(lam * (h[i] + delta))

    for i in range(2):
        m_star = (curv[i] * target[i]) / (curv[i] + delta)
        sigma_star = 1.0 / math.sqrt(lam * (curv[i] + delta))
        assert abs(h[i] - curv[i]) < 1e-2
        assert abs(m[i] - m_star) < 1e-2
        assert abs(sigma[i] - sigma_star) < 1e-3


if __name__ == "__main__":
    verify_stein_reparameterization_hessian_identity_eq_3()
    verify_riemannian_positivity_update_eq_4_alg_1()
    verify_ivon_gaussian_variational_convergence()
    print("[PASS] Round 650 IVON boundary and mathematical verification succeeded.")
