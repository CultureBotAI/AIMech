#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 562: GradSkip & GradSkip+ (Maranjyan, Safaryan, & Richtarik, 2022)."""

import math
import random


def vec_sub(u, v):
    return [a - b for a, b in zip(u, v)]


def sq_norm(u):
    return sum(a * a for a in u)


def main():
    rng = random.Random(20221028)
    # 1. Verify Theorem 3.6 optimal probabilities and expected local gradient evaluations (Equation 7)
    # and Lemma 3.1 fake local steps property
    mu = 1.0
    L_clients = [1.5, 4.0, 10.0, 100.0]  # kappa_i = L_i / mu = [1.5, 4.0, 10.0, 100.0]
    n = len(L_clients)
    kappas = [L_i / mu for L_i in L_clients]
    kappa_max = max(kappas)  # 100.0 -> sqrt(kappa_max) = 10.0
    L_max = max(L_clients)

    p = 1.0 / math.sqrt(kappa_max)  # p = 0.1
    q_clients = [(1.0 - 1.0 / k_i) / (1.0 - 1.0 / kappa_max) for k_i in kappas]

    # Verify step size bound in Theorem 3.5 / 3.6: min_i (1/L_i) * p^2 / (1 - q_i * (1 - p^2)) == 1 / L_max
    step_bounds = [
        (1.0 / L_clients[i]) * (p ** 2) / (1.0 - q_clients[i] * (1.0 - p ** 2))
        for i in range(n)
    ]
    gamma = min(step_bounds)
    assert abs(gamma - 1.0 / L_max) < 1e-12

    # Verify contraction rate 1 - min{gamma * mu, 1 - q_max * (1 - p^2)} == 1 - 1 / kappa_max
    q_max = max(q_clients)
    assert abs(q_max - 1.0) < 1e-12
    rho = min(gamma * mu, 1.0 - q_max * (1.0 - p ** 2))
    assert abs(rho - 1.0 / kappa_max) < 1e-12

    # Verify Equation (7): E[local steps of client i] = 1 / (1 - q_i * (1 - p)) <= min(kappa_i, sqrt(kappa_max))
    expected_grad_evals = []
    for i in range(n):
        e_steps = 1.0 / (1.0 - q_clients[i] * (1.0 - p))
        closed_form = kappas[i] * (1.0 + math.sqrt(kappa_max)) / (kappas[i] + math.sqrt(kappa_max))
        assert abs(e_steps - closed_form) < 1e-12
        assert e_steps <= min(kappas[i], math.sqrt(kappa_max)) + 1e-12
        expected_grad_evals.append(e_steps)

    # Total expected gradient evaluations per communication round in GradSkip vs Scaffnew (n * sqrt(kappa_max))
    gradskip_total_expected = sum(expected_grad_evals)
    scaffnew_total_expected = n * math.sqrt(kappa_max)
    assert gradskip_total_expected < 0.55 * scaffnew_total_expected

    # 2. Simulate Algorithm 1 (GradSkip) and verify Lemma 3.1 (fake local steps) and linear Lyapunov contraction
    d = 4
    b_clients = [[(i - 1.5) * 3.0 * ((-1) ** c) for c in range(d)] for i in range(n)]
    # f_i(x) = 0.5 * L_i * ||x - b_i||^2 -> grad f(x*) = 0 => x* = (sum_i L_i b_i) / (sum_i L_i)
    L_sum = sum(L_clients)
    x_star = [sum(L_clients[i] * b_clients[i][c] for i in range(n)) / L_sum for c in range(d)]

    def grad_i(i, x):
        return [L_clients[i] * (x[c] - b_clients[i][c]) for c in range(d)]

    h_star = [grad_i(i, x_star) for i in range(n)]

    x_local = [[2.0] * d for _ in range(n)]
    h_local = [[0.0] * d for _ in range(n)]

    def lyapunov(xs, hs):
        term_x = sum(sq_norm(vec_sub(xs[i], x_star)) for i in range(n))
        term_h = ((gamma / p) ** 2) * sum(sq_norm(vec_sub(hs[i], h_star[i])) for i in range(n))
        return term_x + term_h

    psi_0 = lyapunov(x_local, h_local)
    active_local = [True] * n
    real_grad_calls = 0
    fake_step_count = 0

    for _ in range(1200):
        theta_t = 1 if rng.random() < p else 0
        x_hat = [[0.0] * d for _ in range(n)]
        h_hat = [[0.0] * d for _ in range(n)]

        for i in range(n):
            eta_it = 1 if rng.random() < q_clients[i] else 0
            if not active_local[i]:
                # Lemma 3.1: once eta_i = 0 during a non-communicating epoch, x_hat = x and h_hat = h = grad f_i(x)
                # without any new gradient evaluation
                fake_step_count += 1
                h_hat[i] = h_local[i][:]
                x_hat[i] = x_local[i][:]
            else:
                real_grad_calls += 1
                g_i = grad_i(i, x_local[i])
                if eta_it == 1:
                    h_hat[i] = h_local[i][:]
                else:
                    h_hat[i] = g_i[:]
                    active_local[i] = False
                x_hat[i] = [x_local[i][c] - gamma * (g_i[c] - h_hat[i][c]) for c in range(d)]

        if theta_t == 1:
            x_avg = [
                sum(x_hat[j][c] - (gamma / p) * h_hat[j][c] for j in range(n)) / n
                for c in range(d)
            ]
            x_next = [x_avg[:] for _ in range(n)]
            active_local = [True] * n
        else:
            x_next = [x_hat[i][:] for i in range(n)]

        h_next = [
            [h_hat[i][c] + (p / gamma) * (x_next[i][c] - x_hat[i][c]) for c in range(d)]
            for i in range(n)
        ]
        x_local, h_local = x_next, h_next

    psi_final = lyapunov(x_local, h_local)
    assert psi_final < 1e-4 * psi_0
    assert fake_step_count > 0

    print(
        f"[PASS] Round 562 GradSkip verified: psi {psi_0:.3f} -> {psi_final:.3e}, "
        f"E[steps]={gradskip_total_expected:.2f} vs Scaffnew={scaffnew_total_expected:.2f}, "
        f"real_grads={real_grad_calls}, fake_steps={fake_step_count}"
    )


if __name__ == "__main__":
    main()
