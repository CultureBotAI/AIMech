"""Constructed mathematical boundary and step-size verification for Round 626:
Stochastic Polyak Step-size (SPS) (Loizou, Vaswani, Laradji, & Lacoste-Julien, AISTATS 2021, arXiv:2002.10542v3).

Verifies:
1. Section 2 Eq. (2)-(3) & Section 3.1 Eq. (5) & Appendix B Eq. (17) (p. 3-4, 14):
   - For mu_i-strongly convex, L_i-smooth functions f_i, the Stochastic Polyak Step-size
     gamma_k = (f_i(x^k) - f_i^*) / (c * ||grad f_i(x^k)||^2) is sandwiched in
     [1 / (2 * c * L_max), 1 / (2 * c * mu_i)].
   - Bounded variant SPS_max: gamma_k = min((f_i(x^k) - f_i^*) / (c * ||grad f_i(x^k)||^2), gamma_b)
     satisfies the fundamental self-bounding inequality gamma_k^2 * ||grad f_i(x^k)||^2 <= (gamma_k / c) * (f_i(x^k) - f_i^*)
     with exact equality when gamma_b = infinity.
2. Section 3.2 Theorem 3.1, Corollary 3.2, Corollary 3.3, & Section 3.4 / Appendix B.3 Theorem B.3 (p. 4-5, 14-19):
   - Theorem 3.1 recurrence E[||x^k - x*||^2] <= (1 - mu * alpha)^k ||x^0 - x*||^2 + 2 * gamma_b * sigma^2 / (mu * alpha)
     where alpha = min(1 / (2 * c * L_max), gamma_b) and sigma^2 = E_i[f_i(x*) - f_i^*].
   - Under interpolation (sigma^2 = 0, Corollary 3.2), SPS with c = 1/2 converges linearly to x* at rate (1 - mu / L_max)^k.
   - For consistent linear systems A x = b under sketch-and-project reformulation f_S(x) = 0.5 * ||A x - b||_H^2
     (Lemma B.2, Eq. 30), f_S(x) - f_S^* = 0.5 * ||grad f_S(x)||^2 identically, so SPS with c = 1/2 reduces
     exactly to the optimal Randomized Kaczmarz constant step-size gamma_k = 1.
3. Appendix D Closed-Form Component Infima f_i^* via Lambert W_0 and r-Lambert W_1 Functions (Theorem D.3, Eq. 67-77, p. 29-31):
   - For l2-regularized binary logistic loss f_i(x) = log(1 + exp(-<x, z_i>)) + (lambda / 2) * ||x||^2,
     the radial minimizer alpha* = ||x*|| satisfies alpha* + alpha* * exp(alpha* * ||z_i||) = ||z_i|| / lambda,
     solved by alpha* = (1 / ||z_i||) * W_1(||z_i||^2 / lambda) where W_1(a) solves w * exp(w) + w = a.
   - For l2-regularized binary exponential loss f_i(x) = exp(-<x, z_i>) + (lambda / 2) * ||x||^2,
     the radial minimizer satisfies alpha* * exp(alpha* * ||z_i||) = ||z_i|| / lambda, solved by
     alpha* = (1 / ||z_i||) * W_0(||z_i||^2 / lambda).
"""

from __future__ import annotations

import math


def verify_sps_bounds_and_strongly_convex_convergence() -> tuple[float, float, float, float]:
    # 1. Verify Eq. (5) sandwich bounds and Eq. (17) self-bounding identity on strongly convex quadratics
    # f_i(x) = 0.5 * a_i * (x - b_i)^2 with mu_i = L_i = a_i
    A = [2.0, 4.0, 8.0, 12.0]
    B_centers = [0.0, 0.0, 0.0, 0.0]  # interpolation setting first (x* = 0, f_i^* = 0, sigma^2 = 0)
    L_max = max(A)
    mu = sum(A) / len(A)  # f(x) = (1/n) sum f_i(x) is mu-strongly convex
    c = 0.5

    max_eq17_unbounded_err = 0.0
    for i, a_i in enumerate(A):
        for x_val in (-2.5, -0.7, 0.4, 1.9):
            f_val = 0.5 * a_i * ((x_val - B_centers[i]) ** 2)
            grad_val = a_i * (x_val - B_centers[i])
            gamma_k = f_val / (c * (grad_val * grad_val))
            lb = 1.0 / (2.0 * c * L_max)
            ub = 1.0 / (2.0 * c * a_i)
            assert lb - 1e-15 <= gamma_k <= ub + 1e-15
            lhs_17 = (gamma_k * gamma_k) * (grad_val * grad_val)
            rhs_17 = (gamma_k / c) * f_val
            max_eq17_unbounded_err = max(max_eq17_unbounded_err, abs(lhs_17 - rhs_17))
    assert max_eq17_unbounded_err < 1e-15

    # 2. Verify Corollary 3.2 exact linear convergence under interpolation (sigma^2 = 0)
    x0 = 3.0
    K = 30
    # Expected squared distance after 1 step conditional on x: E_i[(1 - gamma_i * a_i)^2] * x^2
    # Note that for 1D quadratic f_i(x) = 0.5 * a_i * x^2, gamma_k = (0.5 * a_i * x^2) / (0.5 * a_i^2 * x^2) = 1 / a_i!
    # For 2D quadratic f_i(x1, x2) = 0.5 * (a_{i,1} x1^2 + a_{i,2} x2^2), check Theorem 3.1 / Corollary 3.2 bound:
    pairs = [(2.0, 6.0), (4.0, 8.0), (3.0, 10.0), (7.0, 12.0)]
    L_max_2d = 12.0
    mu_2d = min(sum(p[0] for p in pairs) / 4.0, sum(p[1] for p in pairs) / 4.0)  # 4.0
    x_vec = [2.0, -1.5]
    init_dist_sq = x_vec[0] ** 2 + x_vec[1] ** 2
    max_cor32_ratio = 0.0

    for k in range(1, K + 1):
        i = (k - 1) % 4
        a1, a2 = pairs[i]
        fi_val = 0.5 * (a1 * (x_vec[0] ** 2) + a2 * (x_vec[1] ** 2))
        gi_1, gi_2 = a1 * x_vec[0], a2 * x_vec[1]
        gi_norm_sq = gi_1 * gi_1 + gi_2 * gi_2
        gamma_k = fi_val / (0.5 * gi_norm_sq)
        x_vec = [x_vec[0] - gamma_k * gi_1, x_vec[1] - gamma_k * gi_2]
        dist_sq = x_vec[0] ** 2 + x_vec[1] ** 2
        cor32_rhs = ((1.0 - mu_2d / L_max_2d) ** k) * init_dist_sq
        assert dist_sq <= cor32_rhs + 1e-14
        max_cor32_ratio = max(max_cor32_ratio, dist_sq / cor32_rhs)

    # 3. Verify Theorem 3.1 non-interpolated bound (sigma^2 > 0)
    # f_1(x) = 0.5 * 4 * (x - 1)^2, f_2(x) = 0.5 * 4 * (x + 1)^2 -> x* = 0, f_i(x*) = 2.0, f_i^* = 0, sigma^2 = 2.0
    sigma_sq = 2.0
    mu_noninterp = 4.0
    L_max_noninterp = 4.0
    gamma_b = 0.1
    alpha = min(1.0 / (2.0 * 0.5 * L_max_noninterp), gamma_b)  # min(0.25, 0.1) = 0.1
    # Exact expected second moment E[x_k^2] under uniform sampling of i in {1, 2}:
    # At x, for i=1: g1 = 4(x-1), f1 = 2(x-1)^2, gamma_1 = min(0.25, 0.1) = 0.1, x_next = x - 0.4(x-1) = 0.6 x + 0.4
    # For i=2: x_next = 0.6 x - 0.4. Thus E[x_{k+1}^2 | x_k] = 0.36 x_k^2 + 0.16.
    expected_sq = 4.0  # x0 = 2.0 -> x0^2 = 4.0
    max_thm31_ratio = 0.0
    for k in range(1, 30):
        expected_sq = 0.36 * expected_sq + 0.16
        thm31_rhs = ((1.0 - mu_noninterp * alpha) ** k) * 4.0 + (2.0 * gamma_b * sigma_sq) / (mu_noninterp * alpha)
        assert expected_sq <= thm31_rhs + 1e-14
        max_thm31_ratio = max(max_thm31_ratio, expected_sq / thm31_rhs)

    # 4. Verify Section 3.4 & Appendix B.3 (Lemma B.2 & Theorem B.3):
    # For consistent linear system A x = b with rank-1 coordinate sketch H_i = e_i e_i^T / ||A_{i:}||^2,
    # f_i(x) = 0.5 * (A_{i:} x - b_i)^2 / ||A_{i:}||^2 and grad f_i(x) = ((A_{i:} x - b_i) / ||A_{i:}||^2) A_{i:}^T,
    # so ||grad f_i(x)||^2 = (A_{i:} x - b_i)^2 / ||A_{i:}||^2 = 2 * f_i(x) and SPS (c = 1/2) gives gamma_k == 1!
    A_mat = [[3.0, 4.0], [1.0, -2.0], [2.0, 1.0]]
    x_true = [1.5, -0.5]
    b_vec = [A_mat[i][0] * x_true[0] + A_mat[i][1] * x_true[1] for i in range(3)]
    x_probe = [-1.0, 2.2]
    max_rk_step_err = 0.0
    for i in range(3):
        row_norm_sq = A_mat[i][0] ** 2 + A_mat[i][1] ** 2
        res = A_mat[i][0] * x_probe[0] + A_mat[i][1] * x_probe[1] - b_vec[i]
        f_s = 0.5 * (res * res) / row_norm_sq
        g_s = [(res / row_norm_sq) * A_mat[i][0], (res / row_norm_sq) * A_mat[i][1]]
        g_s_norm_sq = g_s[0] ** 2 + g_s[1] ** 2
        gamma_sps = (f_s - 0.0) / (0.5 * g_s_norm_sq)
        max_rk_step_err = max(max_rk_step_err, abs(gamma_sps - 1.0))
    assert max_rk_step_err < 1e-15

    return max_eq17_unbounded_err, max_cor32_ratio, max_thm31_ratio, max_rk_step_err


def lambert_w_r(a: float, r: float) -> float:
    """Solve w * exp(w) + r * w = a for w >= 0 via Newton's method (Definition D.1-D.2, Eq. 67-68, p. 29)."""
    assert a >= 0.0 and r >= 0.0
    w = math.log(1.0 + a)
    for _ in range(40):
        ew = math.exp(w)
        res = w * ew + r * w - a
        deriv = (w + 1.0) * ew + r
        w = w - res / deriv
    assert abs(w * math.exp(w) + r * w - a) < 1e-14
    return w


def verify_lambert_w_closed_form_surrogate_infima() -> tuple[float, float]:
    # Verify Appendix D.1 (Eq. 70-73, p. 30): l2-regularized binary log-loss
    # f_i(x) = log(1 + exp(-<x, z_i>)) + (lambda / 2) * ||x||^2
    # Radial minimum along x = alpha * z_i / ||z_i|| minimizes g(alpha) = log(1 + exp(-alpha * c)) + (lambda / 2) * alpha^2
    # where c = ||z_i||, solved in closed form by alpha* = (1 / c) * W_1(c^2 / lambda).
    c_norm = 2.4
    lam = 0.35
    w1_val = lambert_w_r((c_norm * c_norm) / lam, r=1.0)
    alpha_star_log = w1_val / c_norm

    # Check first-order stationarity g'(alpha*) == 0 (Eq. 72-73)
    grad_g_log = (-c_norm * math.exp(-alpha_star_log * c_norm)) / (1.0 + math.exp(-alpha_star_log * c_norm)) + lam * alpha_star_log
    assert abs(grad_g_log) < 1e-15

    # Check strict optimality against neighboring values
    f_star_log = math.log(1.0 + math.exp(-alpha_star_log * c_norm)) + 0.5 * lam * (alpha_star_log ** 2)
    for delta in (-1e-4, -1e-6, 1e-6, 1e-4):
        a_test = alpha_star_log + delta
        f_test = math.log(1.0 + math.exp(-a_test * c_norm)) + 0.5 * lam * (a_test ** 2)
        assert f_star_log < f_test

    # Verify Appendix D.2 (Eq. 74-77, p. 30-31): l2-regularized binary exponential loss
    # f_i(x) = exp(-<x, z_i>) + (lambda / 2) * ||x||^2 -> alpha* = (1 / c) * W_0(c^2 / lambda)
    w0_val = lambert_w_r((c_norm * c_norm) / lam, r=0.0)
    alpha_star_exp = w0_val / c_norm
    grad_g_exp = -c_norm * math.exp(-alpha_star_exp * c_norm) + lam * alpha_star_exp
    assert abs(grad_g_exp) < 1e-15

    f_star_exp = math.exp(-alpha_star_exp * c_norm) + 0.5 * lam * (alpha_star_exp ** 2)
    for delta in (-1e-4, -1e-6, 1e-6, 1e-4):
        a_test = alpha_star_exp + delta
        f_test = math.exp(-a_test * c_norm) + 0.5 * lam * (a_test ** 2)
        assert f_star_exp < f_test

    return abs(grad_g_log), abs(grad_g_exp)


if __name__ == "__main__":
    eq17_e, cor32_r, thm31_r, rk_e = verify_sps_bounds_and_strongly_convex_convergence()
    log_g_err, exp_g_err = verify_lambert_w_closed_form_surrogate_infima()
    print(
        f"[PASS] Round 626 SPS verified: "
        f"eq17_err={eq17_e:.2e}, cor32_rat={cor32_r:.4f}<=1, thm31_rat={thm31_r:.4f}<=1, "
        f"rk_step_err={rk_e:.2e}, w1_logloss_grad_err={log_g_err:.2e}, w0_exploss_grad_err={exp_g_err:.2e}"
    )
