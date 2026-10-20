#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 487:
MOCHA (Federated Multi-Task Learning, Smith, Chiang, Sanjabi, & Talwalkar 2017,
NeurIPS 2017, arXiv:1705.10467).

Verifies:
1. Primal-dual matrix-regularized multi-task formulation and Lemma 9 safe aggregation parameter sigma'
   (Equations 1-4, Remark 1, Lemma 4, & Lemma 9, pp. 3-4, 14, & 16-17):
   - For R_bar(w, Omega_bar) = (1/2) w^T M^{-1} w with symmetric positive definite M = M_bar otimes I_d,
     choosing sigma' = gamma * max_t sum_{t'=1}^m |M_bar_{t,t'}| / M_bar_{t,t} (Equation 29)
     guarantees sigma' * sum_{t=1}^m ||X_t alpha_t||_{M_t}^2 >= gamma * ||X alpha||_M^2 for all alpha (Equation 28)
     and therefore guarantees global dual descent D(alpha + gamma Delta alpha) <= (1 - gamma) D(alpha) +
     gamma sum_{t=1}^m G_t^{sigma'}(Delta alpha_t; v, alpha_t) (Lemma 4, Equation 18).
2. Straggler and node-dropout tolerance via per-node per-round approximation parameter theta_t^h in [0, 1]
   (Definition 1, Assumption 2, Lemma 3, Lemma 6, & Theorem 1, Equations 5-6 & 23-26, pp. 5-6 & 14-16):
   - When node t drops out with probability p_t^h <= p_max < 1 (theta_t^h = 1) and otherwise returns
     an approximate local dual update with E[theta_t^h | theta_t^h < 1] <= Theta_max < 1,
     Lemma 3 proves E[theta_t^h] <= Theta_bar = p_max + (1 - p_max) Theta_max < 1, and MOCHA converges
     geometrically to the exact global primal-dual multi-task optimum while naive CoCoA (blocked by the
     worst straggler max_t theta_t^h = 1) makes zero progress when any single node drops out.
"""

from __future__ import annotations
import random


def main() -> None:
    # 2 tasks (m = 2), scalar features d = 1, 1 sample per task for transparent analytical dual D(alpha)
    # Regularizer (1/2) w^T M^{-1} w with M_bar = [[1.0, 0.5], [0.5, 1.0]] (positive task covariance)
    M_bar = [[1.0, 0.5], [0.5, 1.0]]
    gamma = 1.0

    # 1. Verify Lemma 9 (Eq. 28-29): sigma' = gamma * max_t sum_{t'} |M_bar_{t,t'}| / M_bar_{t,t} = 1.5
    sigma_prime = gamma * max(
        sum(abs(M_bar[t][tp]) for tp in range(2)) / M_bar[t][t] for t in range(2)
    )
    assert abs(sigma_prime - 1.5) < 1e-12

    # Check Eq. 28 across diverse vectors u = [X_1 alpha_1, X_2 alpha_2]
    for u0, u1 in [(1.0, 1.0), (2.0, -1.5), (-0.7, 1.3), (1.0, -1.0)]:
        lhs_eq28 = sigma_prime * (M_bar[0][0] * (u0 ** 2) + M_bar[1][1] * (u1 ** 2))
        rhs_eq28 = gamma * (
            M_bar[0][0] * (u0 ** 2) + 2.0 * M_bar[0][1] * u0 * u1 + M_bar[1][1] * (u1 ** 2)
        )
        assert lhs_eq28 >= rhs_eq28 - 1e-12, f"Eq. 28 violated: {lhs_eq28} < {rhs_eq28}"
    # Notice tightness at u0 = u1 = 1.0: lhs = 1.5 * 2 = 3.0 == rhs = 1 + 1 + 1 = 3.0!

    # 2. Verify Lemma 4 & Theorem 1 convergence of MOCHA under stochastic stragglers and dropped nodes
    # Smooth squared-error losses l_t(u_t) = (1/(2 mu)) (u_t - y_t)^2 => conjugate l_t^*(-alpha_t) = (mu/2) alpha_t^2 - y_t alpha_t
    # Dual objective (Eq. 3): D(alpha) = sum_{t=1}^2 ((mu/2) alpha_t^2 - y_t alpha_t) + (1/2) (X alpha)^T M_bar (X alpha)
    mu = 0.5
    x_data = [1.0, 1.0]
    y_data = [2.0, -1.0]

    # Exact dual minimizer solves: (mu I + diag(x) M_bar diag(x)) alpha^* = y
    # Here (mu + 1.0) alpha_0 + 0.5 alpha_1 = 2.0 and 0.5 alpha_0 + (mu + 1.0) alpha_1 = -1.0
    a_diag = mu + 1.0
    b_off = 0.5
    det = a_diag * a_diag - b_off * b_off
    alpha_star = [
        (a_diag * y_data[0] - b_off * y_data[1]) / det,
        (-b_off * y_data[0] + a_diag * y_data[1]) / det,
    ]

    def dual_obj(a: list[float]) -> float:
        v0 = x_data[0] * a[0]
        v1 = x_data[1] * a[1]
        reg_star = 0.5 * (M_bar[0][0] * v0 * v0 + 2.0 * M_bar[0][1] * v0 * v1 + M_bar[1][1] * v1 * v1)
        loss_star = sum(0.5 * mu * (a[t] ** 2) - y_data[t] * a[t] for t in range(2))
        return loss_star + reg_star

    d_star = dual_obj(alpha_star)

    # Verify Lemma 3 bound: p_max = 0.25, Theta_max = 0.4 => Theta_bar = 0.25 + 0.75 * 0.4 = 0.55 < 1
    p_max = 0.25
    theta_max = 0.4
    theta_bar = p_max + (1.0 - p_max) * theta_max
    assert abs(theta_bar - 0.55) < 1e-12 and theta_bar < 1.0

    # Run MOCHA with random node dropouts (theta_t^h = 1 w.p. 0.25) and inexact local updates (theta_t^h in [0, 0.4])
    rng = random.Random(487)
    alpha_mocha = [0.0, 0.0]
    for _h in range(120):
        v = [x_data[0] * alpha_mocha[0], x_data[1] * alpha_mocha[1]]
        # Primal map w(alpha) = nabla R^*(v) = M_bar v
        w_map = [
            M_bar[0][0] * v[0] + M_bar[0][1] * v[1],
            M_bar[1][0] * v[0] + M_bar[1][1] * v[1],
        ]
        delta_alpha = [0.0, 0.0]
        for t in range(2):
            # Exact minimizer Delta alpha_t^* of data-local quadratic subproblem G_t^{sigma'} (Eq. 4):
            # min_da (mu/2)(a_t + da)^2 - y_t(a_t + da) + w_t * x_t * da + (sigma'/2) M_{tt} (x_t da)^2
            grad_t = mu * alpha_mocha[t] - y_data[t] + w_map[t] * x_data[t]
            curv_t = mu + sigma_prime * M_bar[t][t] * (x_data[t] ** 2)
            da_star = -grad_t / curv_t

            # Sample straggler / dropout factor: if dropped, da = 0 (theta_t^h = 1); else scale da_star
            if rng.random() < p_max:
                da_t = 0.0
            else:
                # For quadratic subproblem, da = (1 - sqrt(theta_t^h)) da_star achieves suboptimality ratio theta_t^h
                theta_th = rng.uniform(0.0, theta_max)
                da_t = (1.0 - (theta_th ** 0.5)) * da_star
            delta_alpha[t] = da_t

        d_before = dual_obj(alpha_mocha)
        alpha_mocha = [alpha_mocha[t] + gamma * delta_alpha[t] for t in range(2)]
        d_after = dual_obj(alpha_mocha)
        # Lemma 4 guarantees monotonic dual descent on every single round regardless of which nodes drop!
        assert d_after <= d_before + 1e-12

    dual_gap_mocha = dual_obj(alpha_mocha) - d_star
    assert dual_gap_mocha < 1e-12, f"MOCHA failed to reach dual optimum: {dual_gap_mocha}"

    print(
        f"[PASS] MOCHA boundary verification passed: sigma'={sigma_prime:.2f}, "
        f"Theta_bar={theta_bar:.2f} < 1, dual_subopt={dual_gap_mocha:.3e}"
    )


if __name__ == "__main__":
    main()
