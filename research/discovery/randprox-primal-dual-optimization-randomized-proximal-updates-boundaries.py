#!/usr/bin/env python3
"""Constructed boundary verification for Round 451:
RandProx: Primal-Dual Optimization Algorithms with Randomized Proximal Updates
(Laurent Condat & Peter Richtarik, ICLR 2023, arXiv:2207.12891).

Verifies:
1. Algorithm 1 & Theorem 1 (Sections 2-3, Equations 4-11):
   For min_x { f(x) + g(x) + h(K x) } with mu_f-strongly convex L_f-smooth f, g = 0, and
   h = iota_{x_1 = ... = x_n} (distributed consensus where prox_{tau h*} computes the dual gap to
   the global average), replacing the exact dual proximity update hat_u^{t+1} = prox_{tau h*}(u^t + tau K hat_x^t)
   with an underrelaxed randomized unbiased update
     u^{t+1} = u^t + (1 / (1 + omega)) * R^t(hat_u^{t+1} - u^t)
   and primal correction
     x^{t+1} = hat_x^t - gamma * (1 + omega) * K^* (u^{t+1} - u^t),
   where R^t(r) = r / p with probability p and 0 with probability 1 - p (omega = (1 - p) / p),
   contracts the primal-dual Lyapunov function
     Psi^t = (1 / (2 gamma)) ||x^t - x*||^2 + ((1 + omega) / (2 tau)) ||u^t - u*||^2
   linearly in expectation and converges to the exact consensus optimum x* and dual optimum u* = -nabla f(x*).
"""

from __future__ import annotations
import math
import random


def main() -> None:
    rng = random.Random(20220726)
    n_workers = 5
    d_dim = 4
    # Strongly convex local quadratics f_i(x_i) = 0.5 * mu * ||x_i - b_i||^2 + 0.5 * delta * ||x_i||^2
    # For simplicity and exact closed-form primal-dual solution:
    # f_i(x_i) = 0.5 * a_i * ||x_i - b_i||^2 with a_i in [1.0, 2.0].
    a_weights = [1.0 + 0.25 * i for i in range(n_workers)]
    b_targets = [[rng.uniform(-3.0, 3.0) for _ in range(d_dim)] for _ in range(n_workers)]

    # Exact consensus minimizer x_star = (sum_i a_i b_i) / (sum_i a_i)
    a_sum = sum(a_weights)
    x_star_vec = [sum(a_weights[i] * b_targets[i][j] for i in range(n_workers)) / a_sum for j in range(d_dim)]
    # At optimum, K = I, h(x) = iota_{x_1=...=x_n}, and u_i* = -nabla f_i(x*) = -a_i (x* - b_i)
    # satisfying sum_i u_i* = 0 (i.e. u* in dom(h*) = {u : sum_i u_i = 0}).
    u_star = [[-a_weights[i] * (x_star_vec[j] - b_targets[i][j]) for j in range(d_dim)] for i in range(n_workers)]

    l_smooth = max(a_weights)
    mu_strong = min(a_weights)
    gamma = 0.5 / l_smooth  # gamma < 1 / L_f
    p_comm = 0.25
    omega = (1.0 - p_comm) / p_comm  # exact variance parameter for Bernoulli skip operator R^t
    # By Theorem 1, step size tau satisfies gamma * tau * (1 + omega) * ||K||^2 <= 1; here K = I so ||K|| = 1
    tau = 0.8 / (gamma * (1.0 + omega))

    # For h(x) = iota_C(x) where C = {x : x_1 = ... = x_n}, prox_{tau h}(z) projects onto C (averages across workers),
    # and by Moreau identity prox_{tau h*}(v) = v - tau * prox_{h/tau}(v / tau) = v - mean_i(v_i).
    def prox_tau_h_star(v: list[list[float]]) -> list[list[float]]:
        mean_v = [sum(v[i][j] for i in range(n_workers)) / n_workers for j in range(d_dim)]
        return [[v[i][j] - mean_v[j] for j in range(d_dim)] for i in range(n_workers)]

    def lyapunov(x_state: list[list[float]], u_state: list[list[float]]) -> float:
        p_term = sum(
            (x_state[i][j] - x_star_vec[j]) ** 2 for i in range(n_workers) for j in range(d_dim)
        ) / (2.0 * gamma)
        d_term = ((1.0 + omega) / (2.0 * tau)) * sum(
            (u_state[i][j] - u_star[i][j]) ** 2 for i in range(n_workers) for j in range(d_dim)
        )
        return p_term + d_term

    x = [[0.0] * d_dim for _ in range(n_workers)]
    u = [[0.0] * d_dim for _ in range(n_workers)]
    psi_0 = lyapunov(x, u)

    n_iters = 700
    comm_events = 0
    for _ in range(n_iters):
        # Step 1: hat_x^t = x^t - gamma * nabla f(x^t) - gamma * K^* u^t
        hat_x = [
            [
                x[i][j] - gamma * a_weights[i] * (x[i][j] - b_targets[i][j]) - gamma * u[i][j]
                for j in range(d_dim)
            ]
            for i in range(n_workers)
        ]
        # Step 2: hat_u^{t+1} = prox_{tau h*}(u^t + tau * hat_x^t)
        arg_u = [[u[i][j] + tau * hat_x[i][j] for j in range(d_dim)] for i in range(n_workers)]
        hat_u = prox_tau_h_star(arg_u)
        diff_u = [[hat_u[i][j] - u[i][j] for j in range(d_dim)] for i in range(n_workers)]

        # Step 3: Bernoulli skip randomization R^t(diff_u) = diff_u / p with probability p, else 0
        # Notice (1 / (1 + omega)) * (diff_u / p) = p * (diff_u / p) = diff_u when communication occurs!
        if rng.random() < p_comm:
            comm_events += 1
            r_diff = [[diff_u[i][j] / p_comm for j in range(d_dim)] for i in range(n_workers)]
        else:
            r_diff = [[0.0] * d_dim for _ in range(n_workers)]

        u_next = [[u[i][j] + (1.0 / (1.0 + omega)) * r_diff[i][j] for j in range(d_dim)] for i in range(n_workers)]
        # Step 4: x^{t+1} = hat_x^t - gamma * (1 + omega) * (u^{t+1} - u^t)
        x = [
            [hat_x[i][j] - gamma * (1.0 + omega) * (u_next[i][j] - u[i][j]) for j in range(d_dim)]
            for i in range(n_workers)
        ]
        u = u_next

    psi_final = lyapunov(x, u)
    primal_err = math.sqrt(sum((x[i][j] - x_star_vec[j]) ** 2 for i in range(n_workers) for j in range(d_dim)))
    dual_err = math.sqrt(sum((u[i][j] - u_star[i][j]) ** 2 for i in range(n_workers) for j in range(d_dim)))

    assert psi_final < 1e-18 * psi_0, f"Expected linear Lyapunov decay, got {psi_final} vs {psi_0}"
    assert primal_err < 1e-9 and dual_err < 1e-9, f"Expected exact primal-dual convergence: {primal_err}, {dual_err}"

    print(
        f"[PASS] Round 451 RandProx (Condat & Richtarik 2023): "
        f"comm_rate={comm_events/n_iters:.3f} (p={p_comm}), "
        f"psi_ratio={psi_final/psi_0:.2e}, primal_err={primal_err:.2e}, dual_err={dual_err:.2e}"
    )


if __name__ == "__main__":
    main()
