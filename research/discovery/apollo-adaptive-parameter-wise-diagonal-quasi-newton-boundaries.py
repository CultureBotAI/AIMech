#!/usr/bin/env python3
"""Boundary & mathematical verification for Round 607: Apollo (Xuezhe Ma, arXiv:2009.13586)."""

from __future__ import annotations

import math


def verify_weak_secant_variational_diagonal_update() -> tuple[float, float, float]:
    """Verify Section 3.1-3.2 Eqs. (6)-(8) (p. 5):
    1. B_{t+1} = B_t + ((s_t^T y_t - s_t^T B_t s_t) / ||s_t||_4^4) Diag(s_t^2) uniquely minimizes ||B - B_t||_F
       among diagonal matrices satisfying the weak secant condition s_t^T B s_t = s_t^T y_t.
    2. Stepsize bias correction (Eq. 8) makes B_{t+1} - B_t independent of eta_t."""
    s_t = [0.4, -0.7, 1.1, -0.3, 0.8]
    y_t = [0.9, -1.2, 2.5, -0.1, 1.4]
    B_t = [1.5, 0.8, 2.1, 0.5, 1.2]

    s_dot_y = sum(si * yi for si, yi in zip(s_t, y_t))
    s_B_s = sum((si * si) * bi for si, bi in zip(s_t, B_t))
    s_norm4_4 = sum(si ** 4 for si in s_t)

    coeff = (s_dot_y - s_B_s) / s_norm4_4
    B_next = [bi + coeff * (si * si) for bi, si in zip(B_t, s_t)]

    # Check weak secant condition s_t^T B_{t+1} s_t == s_t^T y_t
    lhs_secant = sum((si * si) * bi for si, bi in zip(s_t, B_next))
    secant_err = abs(lhs_secant - s_dot_y)
    assert secant_err < 1e-15, f"Weak secant condition failed: {secant_err}"

    # Check minimum Frobenius norm property: any perturbation delta_B with sum_i s_i^2 delta_B_i = 0 increases ||B - B_t||_F^2
    # Choose delta_B orthogonal to s_t^2
    s_sq = [si * si for si in s_t]
    raw_pert = [1.0, -2.0, 0.5, 1.5, -0.8]
    proj = sum(pi * sqi for pi, sqi in zip(raw_pert, s_sq)) / s_norm4_4
    orth_pert = [pi - proj * sqi for pi, sqi in zip(raw_pert, s_sq)]
    assert abs(sum(oi * sqi for oi, sqi in zip(orth_pert, s_sq))) < 1e-15

    frob_opt = sum((b1 - b0) ** 2 for b1, b0 in zip(B_next, B_t))
    frob_alt = sum((b1 + 0.1 * oi - b0) ** 2 for b1, oi, b0 in zip(B_next, orth_pert, B_t))
    frob_gain = frob_alt - frob_opt
    assert frob_gain > 0.0, f"Expected minimum Frobenius norm, got frob_gain={frob_gain}"

    # Verify Eq. (8) stepsize bias correction identity: replacing s_t = -eta_t d_t and y'_t = eta_t y_t
    eta_t = 0.037
    d_t = [-si / eta_t for si in s_t]
    y_prime = [eta_t * yi for yi in y_t]
    # Left expression in Eq. (8) using s_t and y'_t
    s_dot_yp = sum(si * ypi for si, ypi in zip(s_t, y_prime))
    lam_left = [((s_dot_yp - s_B_s) / s_norm4_4) * (si * si) for si in s_t]
    # Right expression in Eq. (8) using d_t and y_t (independent of eta_t)
    d_dot_y = sum(di * yi for di, yi in zip(d_t, y_t))
    d_B_d = sum((di * di) * bi for di, bi in zip(d_t, B_t))
    d_norm4_4 = sum(di ** 4 for di in d_t)
    lam_right = [-((d_dot_y + d_B_d) / d_norm4_4) * (di * di) for di in d_t]

    eq8_err = max(abs(a - b) for a, b in zip(lam_left, lam_right))
    assert eq8_err < 1e-15, f"Eq. 8 stepsize bias correction identity failed: {eq8_err}"
    return secant_err, frob_gain, eq8_err


def run_apollo_trajectory(
    eta: float,
    sigma: float,
    scale_c: float = 1.0,
    scale_invariant: bool = False,
    eps: float = 0.0,
) -> tuple[list[float], list[float], list[float], list[float]]:
    """Run Apollo (Algorithm 1, p. 6) or Scale-Invariant Apollo (Appendix G, Eq. 31, p. 31) on a 2-layer decoupled objective."""
    beta = 0.9
    theta = [1.2, -0.8, 0.5, -1.1]
    m = [0.0] * 4
    d = [0.0] * 4
    B = [0.0] * 4
    D = [0.0] * 4
    g_prev = [0.0] * 4

    # Decoupled parameters: group 1 = indices [0, 1], group 2 = indices [2, 3]
    groups = [[0, 1], [2, 3]]

    for t in range(1, 25):
        # Nonconvex objective f(theta) = sum_i (0.5 * a_i * theta_i^2 + 0.3 * cos(2 * theta_i))
        a_coeffs = [2.0, 0.5, 1.5, 3.0]
        g = [
            scale_c * (a_coeffs[i] * theta[i] - 0.6 * math.sin(2.0 * theta[i]) + 0.1 * math.cos(t + i))
            for i in range(4)
        ]
        m_next = [
            (beta * (1.0 - (beta ** (t - 1))) / (1.0 - (beta ** t))) * m[i]
            + ((1.0 - beta) / (1.0 - (beta ** t))) * g[i]
            for i in range(4)
        ]

        for grp in groups:
            d_norm4 = sum(d[i] ** 4 for i in grp) ** 0.25
            denom = (d_norm4 + eps) ** 4
            if denom > 0.0:
                num = sum(d[i] * (m_next[i] - m[i]) + (d[i] * d[i]) * B[i] for i in grp)
                alpha_step = num / denom
            else:
                alpha_step = 0.0
            if scale_invariant:
                g_diff_inf = max(abs(g[i] - g_prev[i]) for i in grp) if t > 1 else max(abs(g[i]) for i in grp)
                thresh = sigma * g_diff_inf
            else:
                thresh = sigma
            for i in grp:
                B[i] = B[i] - alpha_step * (d[i] * d[i])
                D[i] = max(abs(B[i]), thresh)
                d[i] = m_next[i] / D[i]
                theta[i] = theta[i] - eta * d[i]

        m = m_next
        g_prev = g

    return theta, m, B, d


def verify_theorem1_coupled_stepsize_and_scale_invariance() -> tuple[float, float, float]:
    """Verify Theorem 1 (Section 3.4, Eq. 12, p. 7 & Appendix A, Eq. 16, p. 19) and Appendix G Scale-Invariant Apollo (Eq. 31, p. 31)."""
    # 1. Theorem 1: For (eta, sigma) and (eta', sigma') = (alpha * eta, alpha * sigma) with eps=0 (exact Eq. 8),
    # B'_t = alpha * B_t, d'_t = d_t / alpha, and theta'_t = theta_t for all t!
    alpha_ratio = 100.0
    th1, m1, B1, d1 = run_apollo_trajectory(eta=0.01, sigma=0.01, scale_c=1.0, scale_invariant=False, eps=0.0)
    th2, m2, B2, d2 = run_apollo_trajectory(
        eta=0.01 * alpha_ratio,
        sigma=0.01 * alpha_ratio,
        scale_c=1.0,
        scale_invariant=False,
        eps=0.0,
    )

    th_coupled_err = max(abs(a - b) for a, b in zip(th1, th2))
    B_coupled_err = max(abs(B2[i] - alpha_ratio * B1[i]) for i in range(4))
    assert th_coupled_err < 1e-12, f"Theorem 1 trajectory invariance failed: {th_coupled_err}"
    assert B_coupled_err < 1e-11, f"Theorem 1 B'_t = alpha B_t failed: {B_coupled_err}"

    # 2. Scale-Invariant Apollo (Appendix G, Eq. 31, p. 31):
    # Rescaling objective f(theta) -> c * f(theta) leaves trajectory theta_t invariant when D_t = max(|B_t|, sigma * ||g_{t+1} - g_t||_infty)
    th_s1, _, _, _ = run_apollo_trajectory(eta=0.02, sigma=1.0, scale_c=1.0, scale_invariant=True, eps=0.0)
    th_s2, _, _, _ = run_apollo_trajectory(eta=0.02, sigma=1.0, scale_c=37.5, scale_invariant=True, eps=0.0)
    scale_inv_err = max(abs(a - b) for a, b in zip(th_s1, th_s2))
    assert scale_inv_err < 1e-12, f"Appendix G Scale-Invariant Apollo failed: {scale_inv_err}"
    return th_coupled_err, B_coupled_err, scale_inv_err


def main() -> None:
    secant_err, frob_gain, eq8_err = verify_weak_secant_variational_diagonal_update()
    th_err, B_err, scale_err = verify_theorem1_coupled_stepsize_and_scale_invariance()
    print(
        f"[PASS] Round 607 Apollo verified: secant_err={secant_err:.2e}, frob_gain={frob_gain:.4e}>0, "
        f"eq8_err={eq8_err:.2e}, thm1_th_err={th_err:.2e}, thm1_B_err={B_err:.2e}, scale_inv_err={scale_err:.2e}"
    )


if __name__ == "__main__":
    main()
