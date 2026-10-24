#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 351:
Linear Coupling of Gradient and Mirror Descent for First-Order Optimization
(Allen-Zhu & Orecchia, 2014/2017, ITCS 2017, LIPIcs 67:3:1-3:22, arXiv:1407.1537).
"""

import math


def main():
    # 1. Verify Algorithm 1 (AGM via Linear Coupling) on an L-smooth convex quadratic in Euclidean l2 norm
    # f(x) = 1/2 * sum_{i=1}^d lambda_i (x_i - x^*_i)^2
    d = 6
    lambdas = [0.02, 0.05, 0.1, 0.4, 1.0, 2.0]
    L = max(lambdas)
    x_star = [1.5, -2.0, 0.8, -1.2, 0.5, -0.7]

    def f(x):
        return 0.5 * sum(lam * (xi - xsi) ** 2 for lam, xi, xsi in zip(lambdas, x, x_star))

    def grad_f(x):
        return [lam * (xi - xsi) for lam, xi, xsi in zip(lambdas, x, x_star)]

    def bregman_l2(z, u):
        return 0.5 * sum((ui - zi) ** 2 for zi, ui in zip(z, u))

    x0 = [0.0] * d
    y = list(x0)
    z = list(x0)
    Theta = bregman_l2(z, x_star)
    T = 40

    max_coupling_lemma_violation = -float("inf")
    for k in range(T):
        alpha_k1 = (k + 2.0) / (2.0 * L)
        tau_k = 1.0 / (alpha_k1 * L)  # = 2 / (k + 2)
        assert abs(tau_k - 2.0 / (k + 2.0)) < 1e-15

        # Line 5: x_{k+1} = tau_k z_k + (1 - tau_k) y_k
        x_k1 = [tau_k * zk + (1.0 - tau_k) * yk for zk, yk in zip(z, y)]
        g = grad_f(x_k1)

        # Line 6: Gradient step y_{k+1} = Grad(x_{k+1}) = x_{k+1} - (1/L) grad f(x_{k+1})
        y_k1 = [xk - (1.0 / L) * gk for xk, gk in zip(x_k1, g)]
        # Verify Eq (2.1) primal progress: f(y_{k+1}) <= f(x_{k+1}) - 1/(2L) ||grad f(x_{k+1})||_2^2
        grad_norm_sq = sum(gk * gk for gk in g)
        assert f(y_k1) <= f(x_k1) - grad_norm_sq / (2.0 * L) + 1e-12

        # Line 7: Mirror step z_{k+1} = Mirr_{z_k}(alpha_{k+1} grad f(x_{k+1})) = z_k - alpha_{k+1} grad f(x_{k+1})
        z_k1 = [zk - alpha_k1 * gk for zk, gk in zip(z, g)]

        # Verify Lemma 4.3 (Coupling Lemma) at u = x^*:
        # (alpha_{k+1}^2 L) f(y_{k+1}) - (alpha_{k+1}^2 L - alpha_{k+1}) f(y_k) + (V_{z_{k+1}}(x^*) - V_{z_k}(x^*)) <= alpha_{k+1} f(x^*)
        lhs = (
            (alpha_k1 ** 2 * L) * f(y_k1)
            - (alpha_k1 ** 2 * L - alpha_k1) * f(y)
            + (bregman_l2(z_k1, x_star) - bregman_l2(z, x_star))
        )
        rhs = alpha_k1 * f(x_star)
        max_coupling_lemma_violation = max(max_coupling_lemma_violation, lhs - rhs)

        y, z = y_k1, z_k1

    assert max_coupling_lemma_violation <= 1e-12, f"Lemma 4.3 violated: {max_coupling_lemma_violation}"

    # Verify Theorem 4.1 bound: f(y_T) - f(x^*) <= 4 * Theta * L / (T + 1)^2
    thm41_bound = 4.0 * Theta * L / ((T + 1.0) ** 2)
    agm_err = f(y) - f(x_star)
    assert agm_err <= thm41_bound + 1e-12, f"Theorem 4.1 violated: {agm_err} > {thm41_bound}"

    # Compare against standard unaccelerated Gradient Descent after T steps
    x_gd = list(x0)
    for _ in range(T):
        g = grad_f(x_gd)
        x_gd = [xi - (1.0 / L) * gi for xi, gi in zip(x_gd, g)]
    gd_err = f(x_gd) - f(x_star)
    assert agm_err < gd_err * 0.25, f"Expected AGM ({agm_err}) << GD ({gd_err})"

    # 2. Verify Appendix A.1 / A.2: Non-Euclidean l1-norm simplex mirror step with entropy DGF w(x) = sum_i x_i log x_i
    # On simplex Delta_n, V_x(u) = sum_i u_i log(u_i / x_i) >= 1/2 ||x - u||_1^2 (Pinsker's inequality)
    p = [0.1, 0.2, 0.3, 0.4]
    q = [0.25, 0.25, 0.25, 0.25]
    kl_pq = sum(pi * math.log(pi / qi) for pi, qi in zip(p, q))
    l1_sq_half = 0.5 * (sum(abs(pi - qi) for pi, qi in zip(p, q)) ** 2)
    assert kl_pq >= l1_sq_half - 1e-12

    print(
        f"[PASS] Round 351 Linear Coupling AGM (Allen-Zhu & Orecchia 2014/2017): "
        f"max_lemma43_viol={max_coupling_lemma_violation:.2e}, "
        f"agm_err={agm_err:.6f} <= thm41_bound={thm41_bound:.6f} (vs gd_err={gd_err:.6f}), "
        f"kl_pinsker_gap={kl_pq - l1_sq_half:.4e}"
    )


if __name__ == "__main__":
    main()
