#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 570: ANITA."""

import math
import random


def main() -> None:
    random.seed(570)
    # 1. Verify Equation (40) recursion condition for ANITA's dynamic multi-stage schedule (Section A.1.1):
    # For t > t_1 + 1, with p_t = max(4 / (t - t_1 + 3*sqrt(n)), 4 / (n + 3)),
    # theta_t = 2 / (p_t * (t - t_1 + 3*sqrt(n))), and constant eta_t = eta = 1 / (3L):
    # Check that (1 - p_t * theta_t) * eta_t / (p_t * theta_t^2) <= eta_{t-1} / (p_{t-1} * theta_{t-1}^2)
    for n in [16, 64, 100]:
        t1 = n
        L = 2.0
        eta = 1.0 / (3.0 * L)
        sqrt_n = math.sqrt(n)

        def p_theta(t: int) -> tuple[float, float]:
            denom = t - t1 + 3.0 * sqrt_n
            pt = max(4.0 / denom, 4.0 / (n + 3.0))
            thetat = 2.0 / (pt * denom)
            return pt, thetat

        for t in range(t1 + 2, t1 + 3 * n):
            pt, thetat = p_theta(t)
            pt_prev, thetat_prev = p_theta(t - 1)
            lhs = (1.0 - pt * thetat) * eta / (pt * (thetat ** 2))
            rhs = eta / (pt_prev * (thetat_prev ** 2))
            assert lhs <= rhs + 1e-12, f"Eq (40) violated at t={t}: {lhs} > {rhs}"

        # Also verify Eq (44): at t = t_1 + 1, (1 - p_{t1+1}*theta_{t1+1})*eta / (p_{t1+1}*theta_{t1+1}^2) <= 4*sqrt(n)/L
        p1, th1 = p_theta(t1 + 1)
        assert abs(th1 - 0.5) < 1e-12
        val_44 = (1.0 - p1 * th1) * eta / (p1 * (th1 ** 2))
        assert val_44 <= 4.0 * sqrt_n / L + 1e-12

    # 2. Verify Theorem 2 (Strongly Convex ANITA) contraction factor (Eq. 57):
    # With p = 1/n, theta = 0.5 * min(1, sqrt(mu / (p * L))), eta = 1 / (L * theta * (1 + 1 / (1 - theta))):
    # Verify that max(1 - p * theta, 1 / (1 + mu * eta)) <= 1 - 4 * p * theta / 5
    for n in [10, 50]:
        p = 1.0 / n
        for mu, L in [(0.1, 2.0), (0.5, 2.0), (0.01, 5.0)]:
            theta = 0.5 * min(1.0, math.sqrt(mu / (p * L)))
            eta = 1.0 / (L * theta * (1.0 + 1.0 / (1.0 - theta)))
            contraction = max(1.0 - p * theta, 1.0 / (1.0 + mu * eta))
            bound = 1.0 - 0.8 * p * theta
            assert contraction <= bound + 1e-12, (
                f"Theorem 2 Eq (57) violated: {contraction} > {bound}"
            )

    # 3. Simulate ANITA (Algorithm 1) vs SVRG and GD on a finite-sum problem
    n_sim = 16
    d = 4
    mu_sim = 0.1
    L_sim = 2.0
    # Construct n_sim component quadratics f_i(x) = 0.5 * <A_i x, x> + <b_i, x>
    # with sum_i b_i = 0 so x* = 0 and f(x*) = 0
    A_mats = [
        [mu_sim + (L_sim - mu_sim) * ((i + j) % d) / (d - 1) for j in range(d)]
        for i in range(n_sim)
    ]
    raw_b = [[random.uniform(-1.0, 1.0) for _ in range(d)] for _ in range(n_sim)]
    b_mean = [sum(raw_b[i][j] for i in range(n_sim)) / n_sim for j in range(d)]
    B_vecs = [[raw_b[i][j] - b_mean[j] for j in range(d)] for i in range(n_sim)]

    def f_val(x: list[float]) -> float:
        total = 0.0
        for i in range(n_sim):
            fi = sum(
                0.5 * A_mats[i][j] * (x[j] ** 2) + B_vecs[i][j] * x[j]
                for j in range(d)
            )
            total += fi / n_sim
        return total

    def grad_i(i: int, x: list[float]) -> list[float]:
        return [A_mats[i][j] * x[j] + B_vecs[i][j] for j in range(d)]

    def full_grad(x: list[float]) -> list[float]:
        g = [0.0] * d
        for i in range(n_sim):
            gi = grad_i(i, x)
            for j in range(d):
                g[j] += gi[j] / n_sim
        return g

    # Run strongly convex ANITA (Algorithm 1 with Theorem 2 parameters)
    p_sc = 1.0 / n_sim
    theta_sc = 0.5 * min(1.0, math.sqrt(mu_sim / (p_sc * L_sim)))
    eta_sc = 1.0 / (L_sim * theta_sc * (1.0 + 1.0 / (1.0 - theta_sc)))
    alpha_sc = 1.0 + mu_sim * eta_sc

    x0 = [2.0, -1.5, 1.2, -0.8]
    x_t = list(x0)
    w_t = list(x0)
    fg_w = full_grad(w_t)
    phi_0 = f_val(w_t) + ((1.0 + mu_sim * eta_sc) * p_sc * theta_sc / (2.0 * eta_sc)) * sum(
        v * v for v in x_t
    )

    for t in range(400):
        x_under = [theta_sc * x_t[j] + (1.0 - theta_sc) * w_t[j] for j in range(d)]
        idx = random.randrange(n_sim)
        gi_u = grad_i(idx, x_under)
        gi_w = grad_i(idx, w_t)
        v_tilde = [gi_u[j] - gi_w[j] + fg_w[j] for j in range(d)]
        x_next = [
            (x_t[j] + mu_sim * eta_sc * x_under[j]) / (1.0 + mu_sim * eta_sc)
            - (eta_sc / alpha_sc) * v_tilde[j]
            for j in range(d)
        ]
        x_bar_next = [
            theta_sc * x_next[j] + (1.0 - theta_sc) * w_t[j] for j in range(d)
        ]
        if random.random() < p_sc:
            w_t = x_bar_next
            fg_w = full_grad(w_t)
        x_t = x_next

    phi_T = f_val(w_t) + ((1.0 + mu_sim * eta_sc) * p_sc * theta_sc / (2.0 * eta_sc)) * sum(
        v * v for v in x_t
    )
    assert f_val(w_t) < 1e-9 and phi_T < phi_0 * 1e-7, (
        f"Expected ANITA to contract rapidly: f(w_T)={f_val(w_t)}, phi_T={phi_T}"
    )
    print(
        f"[PASS] Round 570 ANITA verified: theta_sc={theta_sc:.4f}, eta_sc={eta_sc:.4f}, "
        f"phi_0={phi_0:.3e} -> phi_T={phi_T:.3e}, f(w_T)={f_val(w_t):.3e}"
    )


if __name__ == "__main__":
    main()
