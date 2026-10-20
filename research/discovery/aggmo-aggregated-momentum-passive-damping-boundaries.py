#!/usr/bin/env python3
"""Boundary & mathematical verification for Round 606: Aggregated Momentum (AggMo, Lucas et al., ICLR 2019)."""

from __future__ import annotations

import math


def verify_nesterov_reparameterization_equivalence() -> tuple[float, float]:
    """Verify Section 4 Eqs. (4)-(7) (p. 4): Generalized AggMo with beta=[0, beta] and gamma=[2*gamma, 2*beta*gamma]
    is algebraically identical to Nesterov's half-step reparameterization phi_t = theta_t + gamma*beta*v_t."""
    beta = 0.95
    gamma = 0.04
    # 2D quadratic objective f(x) = 0.5 * (1.2 x_0^2 + 0.08 x_1^2) + 0.3 x_0 - 0.5 x_1
    def grad_f(th: list[float]) -> list[float]:
        return [1.2 * th[0] + 0.3, 0.08 * th[1] - 0.5]

    th_agg = [2.5, -1.8]
    v1_agg = [0.0, 0.0]  # beta^(1) = 0
    v2_agg = [0.0, 0.0]  # beta^(2) = beta
    gamma1 = 2.0 * gamma
    gamma2 = 2.0 * beta * gamma

    th_nag = list(th_agg)
    v_nag = [0.0, 0.0]
    phi_nag = list(th_nag)  # phi_0 = theta_0 + gamma*beta*v_0 = theta_0

    max_phi_diff = 0.0
    max_eq5_diff = 0.0

    for _ in range(50):
        # 1. Generalized AggMo (Eq. 4 & Eq. 5)
        g_agg = grad_f(th_agg)
        v2_prev = list(v2_agg)
        v1_agg = [-g_agg[0], -g_agg[1]]  # beta^(1) = 0
        v2_agg = [beta * v2_agg[0] - g_agg[0], beta * v2_agg[1] - g_agg[1]]
        th_agg_next = [
            th_agg[j] + 0.5 * (gamma1 * v1_agg[j] + gamma2 * v2_agg[j])
            for j in range(2)
        ]
        # Verify Eq. (5) closed form: theta_t = theta_{t-1} + gamma*beta^2*v_{t-1} - (1+beta)*gamma*grad_f(theta_{t-1})
        th_eq5 = [
            th_agg[j] + gamma * (beta * beta) * v2_prev[j] - (1.0 + beta) * gamma * g_agg[j]
            for j in range(2)
        ]
        for j in range(2):
            max_eq5_diff = max(max_eq5_diff, abs(th_agg_next[j] - th_eq5[j]))
        th_agg = th_agg_next

        # 2. Nesterov momentum (Eq. 6) and half-step reparameterization phi_t = theta_t + gamma*beta*v_t (Eq. 7)
        lookahead = [th_nag[j] + gamma * beta * v_nag[j] for j in range(2)]
        g_nag = grad_f(lookahead)
        v_nag = [beta * v_nag[j] - g_nag[j] for j in range(2)]
        th_nag = [th_nag[j] + gamma * v_nag[j] for j in range(2)]
        phi_nag = [th_nag[j] + gamma * beta * v_nag[j] for j in range(2)]

        for j in range(2):
            max_phi_diff = max(max_phi_diff, abs(th_agg[j] - phi_nag[j]))

    assert max_eq5_diff < 1e-15, f"Eq. 5 identity error: {max_eq5_diff}"
    assert max_phi_diff < 1e-14, f"Nesterov reparameterization phi_t != theta_t^AggMo: {max_phi_diff}"
    return max_eq5_diff, max_phi_diff


def verify_companion_matrix_and_finite_difference_equation() -> tuple[float, float, float]:
    """Verify Appendix B & C.1 (p. 12-13, 17-18): block companion matrix B_j and (K+1)-th order difference equation."""
    # 1. Verify block companion matrix B_j (Appendix C.1, p. 17) for K=3, betas=[0.0, 0.9, 0.99]
    betas = [0.0, 0.9, 0.99]
    K = len(betas)
    gamma = 0.25
    lam_j = 0.4  # quadratic eigenvalue f(x) = 0.5 * lam_j * (x - x*)^2
    x_star = 1.5
    x = -2.0
    v = [0.0] * K

    # Build (K+1) x (K+1) matrix B_j for state s_t = [v_t^(1), ..., v_t^(K), x_t - x*]^T
    B = [[0.0] * (K + 1) for _ in range(K + 1)]
    for i in range(K):
        B[i][i] = betas[i]
        B[i][K] = -lam_j
        B[K][i] = gamma * betas[i] / K
    B[K][K] = 1.0 - gamma * lam_j

    state = [*v, x - x_star]
    max_mat_err = 0.0
    for _ in range(30):
        # Direct AggMo step (Eq. 3)
        grad = lam_j * (x - x_star)
        v = [betas[i] * v[i] - grad for i in range(K)]
        x = x + (gamma / K) * sum(v)
        direct_state = [*v, x - x_star]

        # Linear dynamical system step B_j * state
        mat_state = [sum(B[r][c] * state[c] for c in range(K + 1)) for r in range(K + 1)]
        for r in range(K + 1):
            max_mat_err = max(max_mat_err, abs(direct_state[r] - mat_state[r]))
        state = direct_state

    assert max_mat_err < 1e-15, f"Block companion matrix B_j mismatch: {max_mat_err}"

    # 2. Verify K=2 third-order finite difference equation (Appendix C.1, Eqs. 9-12, p. 18):
    # Since delta_{t+1} - delta_t = (gamma/2)(v_{t+1}^(1) + v_{t+1}^(2)) and (1 - beta_i L) v_{t+1}^(i) = -g_t,
    # multiplying by (1 - beta_1 L)(1 - beta_2 L) gives:
    # delta_{t+1} - (1 + beta_1 + beta_2) delta_t + (beta_1 + beta_2 + beta_1*beta_2) delta_{t-1} - beta_1*beta_2*delta_{t-2}
    # = -(gamma/2) * (2 g_t - (beta_1 + beta_2) g_{t-1}).
    b1, b2 = 0.5, 0.9
    th_hist = [2.0]
    g_hist = []
    u1, u2 = 0.0, 0.0
    for _ in range(20):
        th_cur = th_hist[-1]
        # Non-quadratic smooth gradient nabla f(theta) = theta + 0.2 * sin(theta)
        g_cur = th_cur + 0.2 * math.sin(th_cur)
        g_hist.append(g_cur)
        u1 = b1 * u1 - g_cur
        u2 = b2 * u2 - g_cur
        th_next = th_cur + (gamma / 2.0) * (u1 + u2)
        th_hist.append(th_next)

    max_fde_err = 0.0
    for t in range(2, len(g_hist)):
        lhs = (
            th_hist[t + 1]
            - (1.0 + b1 + b2) * th_hist[t]
            + (b1 + b2 + b1 * b2) * th_hist[t - 1]
            - (b1 * b2) * th_hist[t - 2]
        )
        rhs = -(gamma / 2.0) * (2.0 * g_hist[t] - (b1 + b2) * g_hist[t - 1])
        max_fde_err = max(max_fde_err, abs(lhs - rhs))

    assert max_fde_err < 1e-14, f"(K+1)-th order finite difference error: {max_fde_err}"

    # 3. Compare passive damping on multi-scale quadratic (eigenvalues [0.01, 0.001, 0.0001, 1e-5], Section 3, Fig. 1, p. 3)
    def run_multiscale(betas_list: list[float], steps: int = 500) -> float:
        lams = [0.01, 0.001, 0.0001, 1e-5]
        lr = 0.33
        xs = [10.0] * len(lams)
        vs = [[0.0] * len(lams) for _ in betas_list]
        for _ in range(steps):
            gs = [lams[j] * xs[j] for j in range(len(lams))]
            for i, b in enumerate(betas_list):
                for j in range(len(lams)):
                    vs[i][j] = b * vs[i][j] - gs[j]
            for j in range(len(lams)):
                xs[j] += (lr / len(betas_list)) * sum(vs[i][j] for i in range(len(betas_list)))
        return math.sqrt(sum(xj * xj for xj in xs))

    err_cm_low = run_multiscale([0.9])
    err_cm_high = run_multiscale([0.999])
    err_aggmo = run_multiscale([0.0, 0.9, 0.99, 0.999])
    assert err_aggmo < err_cm_low and err_aggmo < err_cm_high, (
        f"Expected AggMo ({err_aggmo}) < CM_0.9 ({err_cm_low}) and CM_0.999 ({err_cm_high})"
    )
    return max_mat_err, max_fde_err, err_aggmo


def verify_lemma1_regret_and_beta_averaged_momentum() -> tuple[float, float]:
    """Verify Appendix C Lemma 1 (p. 14) and Appendix F Beta-Averaged Momentum raw moments (Eqs. 16-17, p. 21)."""
    # 1. Lemma 1 (p. 14): sum_{t=1}^T sum_{i=1}^K (v_{t,j}^(i))^2 / sqrt(t)
    # <= ||g_{1:T,j}||_4^2 * sqrt(1 + log T) * sum_{i=1}^K 1 / (1 - beta^(i))^2
    betas = [0.0, 0.9, 0.99]
    lam = 0.98
    T = 40
    vs = [0.0 for _ in betas]
    lhs_sum = 0.0
    g_fourth_sum = 0.0
    for t in range(1, T + 1):
        gt = math.cos(0.3 * t) + 0.5
        g_fourth_sum += gt ** 4
        for i, b in enumerate(betas):
            b_t = b * (lam ** t)
            vs[i] = b_t * vs[i] - gt
            lhs_sum += (vs[i] * vs[i]) / math.sqrt(t)

    g_l4_sq = math.sqrt(g_fourth_sum)
    rhs_bound = g_l4_sq * math.sqrt(1.0 + math.log(T)) * sum(1.0 / ((1.0 - b) ** 2) for b in betas)
    ratio = lhs_sum / rhs_bound
    assert ratio <= 1.0, f"Lemma 1 violated: ratio={ratio}"

    # 2. Beta-Averaged Momentum (Appendix F, Eqs. 16-17, p. 21):
    # E_{b ~ Beta(alpha, beta)}[b^k] = prod_{r=0}^{k-1} (alpha + r) / (alpha + beta + r)
    alpha_p, beta_p = 4.0, 2.0
    max_moment_err = 0.0
    # Compare closed-form product against exact Beta-function integral int_0^1 b^{k + alpha - 1} (1 - b)^{beta - 1} db / B(alpha, beta)
    # Using Simpson's rule with N=2000 subintervals
    n_grid = 2000
    def beta_integral(a: float, b: float) -> float:
        h = 1.0 / n_grid
        total = 0.0
        for idx in range(n_grid + 1):
            u = idx * h
            val = (u ** (a - 1.0)) * ((1.0 - u) ** (b - 1.0)) if 0.0 < u < 1.0 else 0.0
            w = 1.0 if (idx == 0 or idx == n_grid) else (4.0 if idx % 2 == 1 else 2.0)
            total += w * val
        return total * h / 3.0

    denom = beta_integral(alpha_p, beta_p)
    for k in range(1, 6):
        closed = 1.0
        for r in range(k):
            closed *= (alpha_p + r) / (alpha_p + beta_p + r)
        num = beta_integral(alpha_p + k, beta_p)
        max_moment_err = max(max_moment_err, abs(closed - (num / denom)))

    assert max_moment_err < 1e-11, f"Beta-Averaged Momentum raw moment error: {max_moment_err}"
    return ratio, max_moment_err


def main() -> None:
    eq5_err, phi_err = verify_nesterov_reparameterization_equivalence()
    mat_err, fde_err, err_agg = verify_companion_matrix_and_finite_difference_equation()
    lemma1_ratio, beta_err = verify_lemma1_regret_and_beta_averaged_momentum()
    print(
        f"[PASS] Round 606 AggMo verified: eq5_err={eq5_err:.2e}, nag_phi_err={phi_err:.2e}, "
        f"companion_err={mat_err:.2e}, fde_err={fde_err:.2e}, quad_err={err_agg:.4e}, "
        f"lemma1_ratio={lemma1_ratio:.4f}<=1, beta_moment_err={beta_err:.2e}"
    )


if __name__ == "__main__":
    main()
