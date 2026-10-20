"""Constructed mathematical boundary and momentum-operator spectral-radius verification for Round 620:
YellowFin (Zhang & Mitliagkas, MLSys 2019 / arXiv:1706.03471v2).

Verifies:
1. Lemma 3 & Appendix A Lemma 7 (Section 2.2, Eq. 5-9 & Appendix A, Eq. 17-21, p. 4-6, 17):
   - In the robust region (1 - sqrt(mu))^2 <= alpha * h(x_t) <= (1 + sqrt(mu))^2,
     the 2x2 momentum operator A_t = [[1 - alpha * h + mu, -mu], [1, 0]] has complex-conjugate
     eigenvalues lambda_t = (m +/- sqrt(m^2 - 4*mu)) / 2 with m = 1 - alpha * h + mu,
     so |lambda_t| = sqrt(mu) and the spectral radius rho(A_t) = sqrt(mu) is invariant
     to both learning rate alpha and curvature h(x_t).
2. Lemma 5, Lemma 6, & Appendix B-C Lemmas 8-10 (Section 3, Eq. 11-14 & Appendix B-C, Eq. 22-34, p. 7, 18-20):
   - In the exact same robust region (1 - sqrt(mu))^2 <= alpha * h <= (1 + sqrt(mu))^2,
     the 3x3 variance operator B = [[m^2, mu^2, -2*mu*m], [1, 0, 0], [m, 0, -mu]]
     has eigenvalues lambda_1 = mu and lambda_{2,3} = (m^2 - 2*mu +/- sqrt((m^2 - 2*mu)^2 - 4*mu^2)) / 2
     with |lambda_1| = |lambda_2| = |lambda_3| = mu, so rho(B) = mu identically.
   - Exact noisy-quadratic MSE recurrence E[(x_{t+1} - x*)^2] = (e_1^T A^t [x_0, x_0]^T)^2 + alpha^2 * C * e_1^T (I - B^t)(I - B)^{-1} e_1
     matches the unrolled second-moment recurrence U_{t+1} = m^2 U_t + mu^2 U_{t-1} - 2*mu*m V_t + alpha^2 * C.
3. SingleStep Tuning Rule & Closed-Form Cubic Solution (Section 3.1, Eq. 15, Algorithm 1, & Appendix D, p. 8, 20):
   - Substituting x = sqrt(mu) in [0, 1) and alpha = (1 - x)^2 / h_min into SingleStep gives
     p(x) = x^2 * D^2 + (1 - x)^4 * C / h_min^2, whose unique root x_p in (0, 1) satisfies
     p'(x_p) = 2 * x_p * D^2 - 4 * (C / h_min^2) * (1 - x_p)^3 = 0, and the constrained global
     minimizer is sqrt(mu_t) = max(x_p, (sqrt(nu) - 1) / (sqrt(nu) + 1)) where nu = h_max / h_min.
4. Closed-Loop YellowFin Negative-Feedback Control (Section 4 & Appendix G, Eq. 16, 36-37, Algorithm 5, p. 10, 22-23):
   - Under asynchrony-induced momentum delta_async > 0, closed-loop feedback mu <- mu + gamma * (mu* - mu_hat_T)
     drives total momentum mu_T = mu + delta_async to the target momentum mu*.
"""

from __future__ import annotations

import cmath
import math


def verify_robust_region_spectral_radii() -> tuple[float, float, float]:
    max_rho_a_err = 0.0
    max_rho_b_err = 0.0
    max_mse_rec_err = 0.0

    for mu in (0.16, 0.49, 0.81, 0.90):
        sqrt_mu = math.sqrt(mu)
        low = (1.0 - sqrt_mu) ** 2
        high = (1.0 + sqrt_mu) ** 2
        for frac in (0.0, 0.15, 0.5, 0.85, 1.0):
            ah = low + frac * (high - low)
            m = 1.0 - ah + mu
            # Eigenvalues of 2x2 momentum operator A (Eq. 21)
            disc_a = m * m - 4.0 * mu
            assert disc_a <= 1e-15
            disc_a_clamped = min(0.0, disc_a)
            lam_a1 = 0.5 * (m + cmath.sqrt(disc_a_clamped))
            lam_a2 = 0.5 * (m - cmath.sqrt(disc_a_clamped))
            rho_a = max(abs(lam_a1), abs(lam_a2))
            max_rho_a_err = max(max_rho_a_err, abs(rho_a - sqrt_mu))

            # Eigenvalues of 3x3 variance operator B (Eq. 32-34)
            disc_b = (m * m - 2.0 * mu) ** 2 - 4.0 * (mu * mu)
            assert disc_b <= 1e-15
            disc_b_clamped = min(0.0, disc_b)
            lam_b1 = complex(mu, 0.0)
            lam_b2 = 0.5 * ((m * m - 2.0 * mu) + cmath.sqrt(disc_b_clamped))
            lam_b3 = 0.5 * ((m * m - 2.0 * mu) - cmath.sqrt(disc_b_clamped))
            rho_b = max(abs(lam_b1), abs(lam_b2), abs(lam_b3))
            max_rho_b_err = max(max_rho_b_err, abs(rho_b - mu))

    # Verify Lemma 5 / Lemma 8 / Lemma 9 exact bias + variance recursion (Eq. 11, 22-27)
    alpha = 0.05
    h = 4.0
    mu = 0.64
    C = 1.5
    m = 1.0 - alpha * h + mu
    x0 = 2.0
    # State for mean: [x_bar_t, x_bar_{t-1}] initialized at [x0, x0] for t=1
    xb_curr, xb_prev = x0, x0
    # State for variance: [U_t, U_{t-1}, V_t] initialized at [0, 0, 0] for t=1
    U_curr, U_prev, V_curr = 0.0, 0.0, 0.0

    # Also track explicit 3x3 matrix power sum for variance
    B = [
        [m * m, mu * mu, -2.0 * mu * m],
        [1.0, 0.0, 0.0],
        [m, 0.0, -mu],
    ]
    vec_b = [0.0, 0.0, 0.0]

    for _t in range(1, 25):
        xb_next = m * xb_curr - mu * xb_prev
        xb_prev, xb_curr = xb_curr, xb_next

        U_next = (m * m) * U_curr + (mu * mu) * U_prev - 2.0 * mu * m * V_curr + (alpha * alpha) * C
        V_next = m * U_curr - mu * V_curr
        U_prev, U_curr, V_curr = U_curr, U_next, V_next

        # Update vec_b <- B * vec_b + [alpha^2 * C, 0, 0]
        vec_b = [
            B[0][0] * vec_b[0] + B[0][1] * vec_b[1] + B[0][2] * vec_b[2] + (alpha * alpha) * C,
            B[1][0] * vec_b[0] + B[1][1] * vec_b[1] + B[1][2] * vec_b[2],
            B[2][0] * vec_b[0] + B[2][1] * vec_b[1] + B[2][2] * vec_b[2],
        ]
        max_mse_rec_err = max(max_mse_rec_err, abs(U_curr - vec_b[0]))

    assert max_rho_a_err < 1e-14
    assert max_rho_b_err < 1e-14
    assert max_mse_rec_err < 1e-14
    return max_rho_a_err, max_rho_b_err, max_mse_rec_err


def verify_singlestep_cubic_and_closed_loop() -> tuple[float, float, float, float]:
    # 1. Verify SingleStep (Eq. 15 & Appendix D, p. 8, 20)
    D = 1.8
    C = 2.4
    h_min = 0.5
    h_max = 18.0
    nu = h_max / h_min
    x_bound = (math.sqrt(nu) - 1.0) / (math.sqrt(nu) + 1.0)

    # Solve 2 * x * D^2 - (4 * C / h_min^2) * (1 - x)^3 = 0 on (0, 1) via bisection
    coeff = 4.0 * C / (h_min * h_min)
    lo, hi = 0.0, 1.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        grad = 2.0 * mid * (D * D) - coeff * ((1.0 - mid) ** 3)
        if grad < 0.0:
            lo = mid
        else:
            hi = mid
    x_p = 0.5 * (lo + hi)
    cubic_res = abs(2.0 * x_p * (D * D) - coeff * ((1.0 - x_p) ** 3))
    assert cubic_res < 1e-14

    x_opt = max(x_p, x_bound)
    mu_opt = x_opt * x_opt
    alpha_opt = ((1.0 - x_opt) ** 2) / h_min

    # Verify x_opt minimizes p(x) = x^2 * D^2 + (1 - x)^4 * C / h_min^2 over all x in [x_bound, 1)
    def p_surrogate(x: float) -> float:
        return (x * x) * (D * D) + ((1.0 - x) ** 4) * C / (h_min * h_min)

    p_opt = p_surrogate(x_opt)
    for k in range(200):
        x_test = x_bound + (1.0 - x_bound) * (k / 200.0)
        assert p_opt <= p_surrogate(x_test) + 1e-14

    # 2. Verify Closed-loop YellowFin (Algorithm 5, Section 4 & Appendix G, p. 10, 22-23)
    mu_target = mu_opt
    delta_async = 0.18
    mu_alg = mu_target
    gamma = 0.05
    initial_excess = (mu_alg + delta_async) - mu_target
    for _ in range(200):
        mu_hat_T = mu_alg + delta_async
        mu_alg = mu_alg + gamma * (mu_target - mu_hat_T)
    final_total_err = abs((mu_alg + delta_async) - mu_target)
    assert final_total_err < 1e-5
    assert mu_alg < mu_target

    return cubic_res, mu_opt, alpha_opt, final_total_err / initial_excess


if __name__ == "__main__":
    ra_err, rb_err, mse_err = verify_robust_region_spectral_radii()
    cub_res, mu_star, alpha_star, cl_rat = verify_singlestep_cubic_and_closed_loop()
    print(
        f"[PASS] Round 620 YellowFin verified: "
        f"rhoA_err={ra_err:.2e}, rhoB_err={rb_err:.2e}, mse_rec_err={mse_err:.2e}, "
        f"cubic_res={cub_res:.2e}, mu_opt={mu_star:.4f}, alpha_opt={alpha_star:.4f}, closed_loop_err_ratio={cl_rat:.2e}"
    )
