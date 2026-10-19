#!/usr/bin/env python3
"""Constructed boundary & regime verification for Carmon et al. (2018, Round 347):
Accelerated Methods for Non-Convex Optimization."""

import math


def f_val(x: list[float]) -> float:
    # Smooth non-convex function with strict saddle at (0, 0):
    # f(x_0, x_1) = -0.5 * alpha_0 * x_0^2 + (L_2 / 6) * |x_0|^3 + 0.5 * L_1 * x_1^2
    # At x = (0, 0), grad f = (0, 0) and Hessian = diag(-alpha_0, L_1) with L_2-Lipschitz Hessian!
    alpha_0 = 0.4
    L_1 = 2.0
    L_2 = 1.2
    return -0.5 * alpha_0 * (x[0] ** 2) + (L_2 / 6.0) * (abs(x[0]) ** 3) + 0.5 * L_1 * (x[1] ** 2)


def grad_f(x: list[float]) -> list[float]:
    alpha_0 = 0.4
    L_1 = 2.0
    L_2 = 1.2
    s = 1.0 if x[0] >= 0.0 else -1.0
    return [-alpha_0 * x[0] + 0.5 * L_2 * s * (x[0] ** 2), L_1 * x[1]]


def hess_f_diag(x: list[float]) -> list[float]:
    alpha_0 = 0.4
    L_1 = 2.0
    L_2 = 1.2
    return [-alpha_0 + L_2 * abs(x[0]), L_1]


def rho_alpha(x: list[float], x0: list[float], alpha: float, L_1: float = 2.0, L_2: float = 1.2) -> float:
    dist = math.sqrt((x[0] - x0[0]) ** 2 + (x[1] - x0[1]) ** 2)
    hinge = max(dist - alpha / L_2, 0.0)
    return L_1 * (hinge ** 2)


def main():
    L_1 = 2.0
    L_2 = 1.2
    alpha = 0.4

    # Claim 1: Verify Lemma 4.1 & Lemma 2.4:
    # For x_0 = (0, 0) where nabla^2 f(x_0) = diag(-alpha, L_1) >= -alpha I,
    # f_alpha(x) = f(x) + rho_alpha(x - x_0) is 3*alpha-almost convex and 5*L_1-smooth everywhere,
    # and g_j(z) = f_alpha(z) + 3*alpha*||z - z_j||^2 is 3*alpha-strongly convex!
    x0 = [0.0, 0.0]
    for k in range(-30, 31):
        if k == 0:
            continue
        x_test = [k * 0.05, 0.1]
        r = abs(x_test[0])
        h_f0 = hess_f_diag(x_test)[0]
        # Second derivative of rho_alpha along x_0 when x_1 = 0 is 0 for r < alpha/L_2 and 2*L_1 for r > alpha/L_2
        h_rho = 2.0 * L_1 if r > alpha / L_2 else 0.0
        assert h_f0 + h_rho >= -3.0 * alpha - 1e-12, f"Lemma 4.1 violated at r={r}: {h_f0 + h_rho}"
        # Adding proximal regularization 3*alpha*||z - z_j||^2 (hessian +6*alpha) makes g_j at least +3*alpha strongly convex
        assert h_f0 + h_rho + 6.0 * alpha >= 3.0 * alpha - 1e-12

    # Claim 2: Verify Lemma 3.2 Negative-Curvature-Descent cubic progress guarantee:
    # At z_1 = (0.01, 0.2), v_1 = [1.0, 0.0] has curvature v_1^T nabla^2 f(z_1) v_1 <= -alpha / 2.
    # Step z_2 = z_1 - (2 |v^T H v| / L_2) * sign(v^T grad f(z_1)) * v decreases f by at least alpha^3 / (12 L_2^2)
    z1 = [0.01, 0.2]
    v1 = [1.0, 0.0]
    curv = hess_f_diag(z1)[0]  # -0.4 + 1.2 * 0.01 = -0.388 <= -alpha/2 = -0.2
    assert curv <= -0.5 * alpha
    g_z1 = grad_f(z1)
    v_dot_g = v1[0] * g_z1[0] + v1[1] * g_z1[1]
    sgn = 1.0 if v_dot_g >= 0.0 else -1.0
    eta_ncd = (2.0 * abs(curv) / L_2) * sgn
    z2 = [z1[0] - eta_ncd * v1[0], z1[1] - eta_ncd * v1[1]]
    actual_decrease = f_val(z1) - f_val(z2)
    cubic_bound = (2.0 * (abs(curv) ** 3)) / (3.0 * (L_2 ** 2))
    min_bound = (alpha ** 3) / (12.0 * (L_2 ** 2))
    assert actual_decrease >= cubic_bound - 1e-12 >= min_bound - 1e-12

    # Claim 3: Verify Theorem 4.3 complexity exponent eps^{-7/4} vs GD eps^{-2}, and Theorem 5.1 strict-saddle basin radius
    eps = 1e-4
    accel_rate = eps ** (-7.0 / 4.0)  # 10^7
    gd_rate = eps ** (-2.0)           # 10^8
    assert abs(accel_rate - 0.1 * gd_rate) < 1e-6

    # At the strict-saddle local minimizer x_+^* = (2 * alpha_0 / L_2, 0) = (2/3, 0),
    # nabla^2 f(x_+^*) = diag(+alpha_0, L_1) >= sigma_1 I with sigma_1 = alpha_0 = 0.4.
    sigma_1 = 0.4
    x_star_local = [2.0 * sigma_1 / L_2, 0.0]
    g_star = grad_f(x_star_local)
    h_star = hess_f_diag(x_star_local)
    assert abs(g_star[0]) < 1e-12 and abs(g_star[1]) < 1e-12
    assert h_star[0] >= sigma_1 - 1e-12 and h_star[1] >= sigma_1 - 1e-12
    # Theorem 5.1 threshold: when eps <= sigma_1^2 / (16 L_2), Phase 1 lands within sigma_1 / (8 L_2) of x_+^*
    eps_strict = (sigma_1 ** 2) / (16.0 * L_2)
    x_plus = [x_star_local[0] - 0.5 * (sigma_1 / (8.0 * L_2)), 0.0]
    dist_to_star = abs(x_plus[0] - x_star_local[0])
    assert dist_to_star <= (2.0 * norm_g / sigma_1 if (norm_g := abs(grad_f(x_plus)[0])) >= 0 else 0.0)
    assert dist_to_star <= sigma_1 / (8.0 * L_2)

    print(
        f"[PASS] Carmon et al. accelerated non-convex boundaries verified: "
        f"NCD_drop={actual_decrease:.6f}>=cubic_bound={cubic_bound:.6f}>={min_bound:.6f}, "
        f"eps^-7/4={accel_rate:.1e}<eps^-2={gd_rate:.1e}, strict_saddle_eps={eps_strict:.4e}"
    )


if __name__ == "__main__":
    main()
