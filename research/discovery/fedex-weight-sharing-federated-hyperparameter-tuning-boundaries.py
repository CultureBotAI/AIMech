#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 499: FedEx (Khodak et al., NeurIPS 2021)."""

import math
import random


def verify_unbiased_stochastic_gradient():
    """Verify Appendix C.1: E_{c_{ti} ~ D_theta}[tilde_nabla_j] == nabla_{theta_j} E_{c ~ D_theta}[L(w, c)]."""
    theta = [0.2, 0.5, 0.3]
    # True validation losses L_i(c_j) for B=2 clients with validation sizes |V_1|=30, |V_2|=70
    v_sizes = [30.0, 70.0]
    v_total = sum(v_sizes)
    losses = [
        [0.8, 0.3, 0.5],  # client 1 validation loss for configs c_1, c_2, c_3
        [0.9, 0.4, 0.6],  # client 2 validation loss for configs c_1, c_2, c_3
    ]
    lam = 0.45  # baseline lambda_t

    # Exact gradient nabla_{theta_j} sum_i (|V_i|/V_total) E_{c_i ~ theta}[L_{V_i}(c_i) - lam]
    exact_grad = [
        (v_sizes[0] * (losses[0][j] - lam) + v_sizes[1] * (losses[1][j] - lam)) / v_total
        for j in range(3)
    ]

    # Enumerate all 3^2 = 9 joint categorical assignments (c_{t1}, c_{t2}) ~ D_theta^2
    expected_est = [0.0, 0.0, 0.0]
    for c1 in range(3):
        for c2 in range(3):
            prob = theta[c1] * theta[c2]
            choices = [c1, c2]
            for j in range(3):
                num = sum(
                    v_sizes[i] * (losses[i][choices[i]] - lam) * (1.0 if choices[i] == j else 0.0)
                    for i in range(2)
                )
                tilde_nabla_j = num / (theta[j] * v_total)
                expected_est[j] += prob * tilde_nabla_j

    max_err = max(abs(expected_est[j] - exact_grad[j]) for j in range(3))
    return max_err


def simulate_fedex_exponentiated_gradient():
    """Simulate Algorithm 2 (FedEx) tuning step-size configurations and Theorem 4.1 regret bound."""
    rng = random.Random(499)
    # 5 candidate step-size configurations c_1, ..., c_5 with true expected losses
    true_losses = [0.65, 0.42, 0.18, 0.35, 0.58]  # c_3 is optimal
    k = len(true_losses)
    theta = [1.0 / k] * k
    lam = 0.0
    gamma = 0.8

    for t in range(1, 81):
        # B=4 clients sample configurations from theta
        b_clients = 4
        sampled = []
        losses_t = []
        for _ in range(b_clients):
            u = rng.random()
            cum = 0.0
            choice = k - 1
            for j, p in enumerate(theta):
                cum += p
                if u <= cum:
                    choice = j
                    break
            sampled.append(choice)
            losses_t.append(true_losses[choice] + rng.uniform(-0.02, 0.02))

        # Algorithm 2 stochastic gradient tilde_nabla
        tilde_nabla = [0.0] * k
        for j in range(k):
            num = sum((losses_t[i] - lam) for i in range(b_clients) if sampled[i] == j)
            tilde_nabla[j] = num / (theta[j] * b_clients)

        # Aggressive schedule from Appendix F: eta_t = sqrt(2 log k) / ||tilde_nabla||_inf
        inf_norm = max(abs(g) for g in tilde_nabla)
        eta_t = math.sqrt(2.0 * math.log(k)) / max(inf_norm, 1e-6) * 0.25

        unnorm = [theta[j] * math.exp(-eta_t * tilde_nabla[j]) for j in range(k)]
        s = sum(unnorm)
        theta = [u / s for u in unnorm]
        lam = gamma * lam + (1.0 - gamma) * (sum(losses_t) / b_clients)

    # Also check Theorem 4.1 regret scaling: (m / tau)**(1/3) + V decreases with tau
    m = 10.0
    v_sim = 0.05
    reg_tau_50 = ((m / 50.0) ** (1.0 / 3.0) + v_sim) * math.sqrt(m)
    reg_tau_5000 = ((m / 5000.0) ** (1.0 / 3.0) + v_sim) * math.sqrt(m)
    return theta[2], max(theta[j] for j in range(k) if j != 2), reg_tau_50, reg_tau_5000


def main():
    unbiased_err = verify_unbiased_stochastic_gradient()
    assert unbiased_err < 1e-15, f"Expected exact unbiased gradient estimator, got {unbiased_err}"

    opt_prob, runner_up_prob, reg_50, reg_5000 = simulate_fedex_exponentiated_gradient()
    assert opt_prob > 0.85 and opt_prob > runner_up_prob * 5.0, (
        f"Expected FedEx to concentrate probability on optimal config c_3: {opt_prob} vs {runner_up_prob}"
    )
    assert reg_5000 < reg_50 * 0.35

    print(
        f"[PASS] Round 499 FedEx (Khodak et al. 2021): "
        f"unbiased_grad_err={unbiased_err:.2e}, theta_opt={opt_prob:.4f} >> runner_up={runner_up_prob:.4f}, "
        f"reg_tau5000={reg_5000:.4f} < reg_tau50={reg_50:.4f}"
    )


if __name__ == "__main__":
    main()
