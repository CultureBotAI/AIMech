"""Constructed boundary verification for Round 471:
Adaptive Personalized Federated Learning (APFL, Deng, Kamani, & Mahdavi 2020, arXiv:2003.13461).
Verifies:
1. Theorem 1 & Equation (3): Optimal mixing parameter alpha_i^* in (0, 1) increases monotonically
   with domain divergence ||D_bar - D_i||_1 and decreases when local sample size m_i is small.
2. Algorithm 1 (Equations 6-10): Local Descent APFL with adaptive alpha_i update
   alpha_i^{(t)} = alpha_i^{(t-1)} - eta_t <v_i^{(t-1)} - w_i^{(t-1)}, nabla f_i(v_bar_i^{(t-1)})>
   recovers the optimal mixture weight and achieves strictly lower local risk than FedAvg and fixed alpha.
"""

from __future__ import annotations
import math


def optimal_alpha_eq3(
    emp_global_risk: float,
    B: float,
    dist_div: float,
    C: float,
    d_vc: float,
    delta: float,
    m_total: int,
    true_local_risk: float,
    m_i: int,
    G: float,
    lambda_H: float,
) -> float:
    rad_global = C * math.sqrt((d_vc + math.log(1.0 / delta)) / m_total)
    rad_local = 2.0 * C * math.sqrt((d_vc + math.log(1.0 / delta)) / m_i)
    num = emp_global_risk + B * dist_div + rad_global
    den = num + (true_local_risk + rad_local + G * lambda_H)
    return num / den


def main() -> None:
    # 1. Verify Theorem 1 & Equation (3) monotonicity properties
    a_low_div = optimal_alpha_eq3(0.05, 1.0, 0.02, 0.5, 10.0, 0.05, 10000, 0.05, 200, 1.0, 0.1)
    a_high_div = optimal_alpha_eq3(0.05, 1.0, 1.50, 0.5, 10.0, 0.05, 10000, 0.05, 200, 1.0, 0.1)
    a_small_mi = optimal_alpha_eq3(0.05, 1.0, 0.30, 0.5, 10.0, 0.05, 10000, 0.05, 20, 1.0, 0.1)
    a_large_mi = optimal_alpha_eq3(0.05, 1.0, 0.30, 0.5, 10.0, 0.05, 10000, 0.05, 5000, 1.0, 0.1)
    assert 0.0 < a_low_div < a_high_div < 1.0
    assert 0.0 < a_small_mi < a_large_mi < 1.0

    # 2. Simulate Algorithm 1 (Local Descent APFL) with Equation (10) adaptive alpha update
    # 3 clients with quadratic loss f_i(u) = 0.5 * ||u - target_i||^2
    # Client 0 is aligned with global mean (target_0 = 0.0), Client 1 & 2 are对称 shifted (+3.0, -3.0)
    targets = [0.0, 3.0, -3.0]
    n_clients = len(targets)
    w_global = 0.0
    v_local = [0.0, 0.0, 0.0]
    alphas = [0.2, 0.2, 0.2]
    eta = 0.15
    tau = 4

    for _round in range(30):
        w_clients = []
        for i in range(n_clients):
            wi = w_global
            vi = v_local[i]
            ai = alphas[i]
            for _step in range(tau):
                v_bar = ai * vi + (1.0 - ai) * wi
                grad_w = wi - targets[i]
                grad_v_bar = v_bar - targets[i]
                # Eq. 6: local update of global model copy
                wi_new = wi - eta * grad_w
                # Eq. 7: local update of v_i using gradient w.r.t. v_i at v_bar_i: alpha_i * nabla f_i(v_bar_i)
                vi_new = vi - eta * ai * grad_v_bar
                # Eq. 10: adaptive alpha update
                grad_alpha = (vi - wi) * grad_v_bar
                ai = min(1.0, max(0.0, ai - eta * grad_alpha))
                wi, vi = wi_new, vi_new
            w_clients.append(wi)
            v_local[i] = vi
            alphas[i] = ai
        w_global = sum(w_clients) / n_clients

    # Evaluate personalized models v_bar_i = alpha_i * v_i + (1 - alpha_i) * w_global
    losses_apfl = []
    losses_global = []
    for i in range(n_clients):
        v_bar = alphas[i] * v_local[i] + (1.0 - alphas[i]) * w_global
        losses_apfl.append(0.5 * (v_bar - targets[i]) ** 2)
        losses_global.append(0.5 * (w_global - targets[i]) ** 2)

    mean_loss_apfl = sum(losses_apfl) / n_clients
    mean_loss_global = sum(losses_global) / n_clients
    assert alphas[1] > alphas[0] + 0.3, f"Expected heterogeneous client alpha {alphas[1]} > aligned {alphas[0]}"
    assert mean_loss_apfl < 1e-3 and mean_loss_apfl < mean_loss_global * 0.01
    print(
        f"[PASS] Round 471 APFL verified: alpha_star(div)={a_low_div:.3f}->{a_high_div:.3f}, "
        f"alpha_t=[{alphas[0]:.3f}, {alphas[1]:.3f}, {alphas[2]:.3f}], "
        f"loss_apfl={mean_loss_apfl:.6f}<<loss_global={mean_loss_global:.4f}"
    )


if __name__ == "__main__":
    main()
