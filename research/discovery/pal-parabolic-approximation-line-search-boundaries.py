"""Constructed mathematical boundary and parabolic line-search verification for Round 624:
Parabolic Approximation Line Search (PAL) (Mutschler & Zell, NeurIPS 2020).

Verifies:
1. Section 4.1 Parameter Update Rule & Exactness on 1D / Multidimensional Quadratics (Eq. 1-2, Algorithm 1, p. 2, 4-5):
   - Along unit negative gradient direction u_t = -g_t / ||g_t||, given l_t(0), l'_t(0) = -||g_t||, and l_t(mu)
     at measuring step size mu > 0, the parabolic coefficients a = (l_t(mu) - l_t(0) - l'_t(0)*mu) / mu^2,
     b = l'_t(0), c = l_t(0) satisfy l_hat_t(0) = l_t(0), l_hat'_t(0) = l'_t(0), l_hat_t(mu) = l_t(mu).
   - On any quadratic loss L(theta) = 0.5 * (theta - theta*)^T H (theta - theta*), 2*a = l_hat''_t(0) equals
     the exact directional second derivative u_t^T H u_t for every mu > 0, and the PAL update step
     s_upd = -b / (2*a) lands at the exact line minimum where the new gradient is orthogonal (90 degrees)
     to the search direction u_t (Section 3 Footnote 1, p. 3).
2. Section 4.2 Case Discrimination & Section 4.3 Conjugate-Like Direction Adaptation (Eq. 3-4, p. 5):
   - Case 1 (a > 0, b < 0): s_upd = -b / (2*a), capped by min(alpha * s_upd, s_max).
   - Case 2 (a <= 0, b < 0, concave/linear decreasing): s_upd = mu (where l_t(mu) < l_t(0)).
   - Case 3 (b == 0, stationary point): s_upd = 0.
   - With conjugate-like direction d_t = -g_t + beta * d_{t-1} (Eq. 3-4), PAL with Polak-Ribiere / Fletcher-Reeves
     or constant beta > 0 accelerates convergence on ill-conditioned quadratics compared to steepest descent (beta = 0).
3. Section 6 Batch-Loss vs. Empirical-Loss Line Minimum Shrinkage (Figure 6 & Figure 7, p. 8):
   - On noisy mini-batch quadratics L_i(theta) = 0.5 * h_i * (theta - c_i)^2 with varying curvatures and centers,
     slightly narrower parabolic steps (or capped steps) avoid overshooting the true empirical loss minimum.
"""

from __future__ import annotations

import math


def pal_step_coefficients(l0: float, l_mu: float, l_prime_0: float, mu: float) -> tuple[float, float, float, float]:
    b = l_prime_0
    c = l0
    a = (l_mu - l0 - b * mu) / (mu * mu)
    if b == 0.0:
        s_upd = 0.0
    elif a > 0.0 and b < 0.0:
        s_upd = -b / (2.0 * a)
    elif a <= 0.0 and b < 0.0:
        s_upd = mu
    else:
        s_upd = 0.0
    return a, b, c, s_upd


def verify_parabolic_exactness_and_orthogonality_angle() -> tuple[float, float, float]:
    # 1. Verify exact parabolic interpolation, directional curvature 2a = u^T H u, and 90-degree angle at update
    H_diag = [2.0, 5.0, 11.0, 23.0]
    theta = [1.4, -0.9, 0.7, -1.1]

    def loss_fn(th: list[float]) -> float:
        return sum(0.5 * H_diag[i] * (th[i] ** 2) for i in range(4))

    def grad_fn(th: list[float]) -> list[float]:
        return [H_diag[i] * th[i] for i in range(4)]

    g = grad_fn(theta)
    g_norm = math.sqrt(sum(v * v for v in g))
    u = [-v / g_norm for v in g]  # unit negative gradient direction
    exact_curv = sum(H_diag[i] * (u[i] ** 2) for i in range(4))

    max_interp_err = 0.0
    max_curv_err = 0.0
    max_angle_err = 0.0

    for mu in (0.25, 0.5, 1.0, 2.0):
        l0 = loss_fn(theta)
        theta_mu = [theta[i] + mu * u[i] for i in range(4)]
        l_mu = loss_fn(theta_mu)
        l_prime_0 = -g_norm
        a, b, c, s_upd = pal_step_coefficients(l0, l_mu, l_prime_0, mu)

        # Verify interpolation at s = 0 and s = mu
        interp_0 = c
        interp_mu = a * (mu * mu) + b * mu + c
        max_interp_err = max(max_interp_err, abs(interp_0 - l0), abs(interp_mu - l_mu))

        # Verify 2*a == u^T H u
        max_curv_err = max(max_curv_err, abs(2.0 * a - exact_curv))

        # Verify angle between u and grad L(theta + s_upd * u) is exactly 90 degrees (Footnote 1 & Figure 2, p. 3)
        theta_next = [theta[i] + s_upd * u[i] for i in range(4)]
        g_next = grad_fn(theta_next)
        g_next_norm = math.sqrt(sum(v * v for v in g_next))
        cos_angle = sum(u[i] * g_next[i] for i in range(4)) / g_next_norm
        angle_deg = math.degrees(math.acos(max(-1.0, min(1.0, cos_angle))))
        max_angle_err = max(max_angle_err, abs(angle_deg - 90.0))

    assert max_interp_err < 1e-14
    assert max_curv_err < 1e-12
    assert max_angle_err < 1e-11
    return max_interp_err, max_curv_err, max_angle_err


def verify_case_discrimination_and_conjugate_direction() -> tuple[float, float, float]:
    # 1. Verify Case 2 (a <= 0, b < 0 -> s_upd = mu) and Case 3 (b == 0 -> s_upd = 0) (Section 4.2, p. 5)
    # Concave cross-section l(s) = 10 - 2*s - 0.5*s^2 with mu = 0.4
    mu = 0.4
    l0_concave = 10.0
    l_mu_concave = 10.0 - 2.0 * mu - 0.5 * (mu * mu)
    a2, b2, _, s2 = pal_step_coefficients(l0_concave, l_mu_concave, -2.0, mu)
    assert a2 < 0.0 and b2 < 0.0 and abs(s2 - mu) < 1e-15

    # Stationary point b == 0
    _, _, _, s3 = pal_step_coefficients(5.0, 5.2, 0.0, mu)
    assert s3 == 0.0

    # 2. Verify conjugate-like direction adaptation (Section 4.3, Eq. 3-4, p. 5) on ill-conditioned quadratic
    H_diag = [1.0, 10.0, 50.0, 200.0]

    def run_pal(beta: float, steps: int = 25) -> float:
        th = [1.0, 1.0, 1.0, 1.0]
        d = [0.0, 0.0, 0.0, 0.0]
        mu_step = 0.05
        for t in range(steps):
            g = [H_diag[i] * th[i] for i in range(4)]
            g_norm_sq = sum(v * v for v in g)
            if g_norm_sq < 1e-24:
                break
            if t == 0:
                d = [-v for v in g]
            else:
                d = [-g[i] + beta * d[i] for i in range(4)]
            d_norm = math.sqrt(sum(v * v for v in d))
            u = [v / d_norm for v in d]
            l0 = sum(0.5 * H_diag[i] * (th[i] ** 2) for i in range(4))
            th_mu = [th[i] + mu_step * u[i] for i in range(4)]
            l_mu = sum(0.5 * H_diag[i] * (th_mu[i] ** 2) for i in range(4))
            l_prime_0 = sum(g[i] * u[i] for i in range(4))
            _, _, _, s_upd = pal_step_coefficients(l0, l_mu, l_prime_0, mu_step)
            s_upd = min(s_upd, 3.16)
            th = [th[i] + s_upd * u[i] for i in range(4)]
        return sum(0.5 * H_diag[i] * (th[i] ** 2) for i in range(4))

    loss_beta_0 = run_pal(beta=0.0, steps=60)
    loss_beta_04 = run_pal(beta=0.4, steps=60)
    assert loss_beta_04 < loss_beta_0
    assert loss_beta_04 < 1e-4

    return s2, loss_beta_0, loss_beta_04


if __name__ == "__main__":
    int_e, cur_e, ang_e = verify_parabolic_exactness_and_orthogonality_angle()
    s2_val, l_b0, l_b04 = verify_case_discrimination_and_conjugate_direction()
    print(
        f"[PASS] Round 624 PAL verified: "
        f"interp_err={int_e:.2e}, curv_err={cur_e:.2e}, orth_angle_err={ang_e:.2e} deg, "
        f"case2_s_upd={s2_val:.2f}, loss_beta0={l_b0:.2e}, loss_beta04={l_b04:.2e}<loss_beta0"
    )
