#!/usr/bin/env python3
"""Boundary verification for Round 455: FedALA (Zhang et al., AAAI 2023, arXiv:2212.01197).

Verifies:
1. Layer-split element-wise Adaptive Local Aggregation initialization (Eq. 4):
   Theta_hat_i^t = Theta_i^{t-1} + (Theta^{t-1} - Theta_i^{t-1}) odot [1^{|Theta_i|-p}; sigma(W_i^p)]
   where lower |Theta_i|-p layers are overwritten by Theta^{t-1} (weights=1) and higher p layers
   are element-wise interpolated with clipped weights sigma(w) = max(0, min(1, w)) in [0, 1].
2. Weight gradient identity (Eq. 5, Eq. 6, and Appendix A Eq. 7):
   nabla_{W_i^p} L_i^t = nabla_{Theta_hat_i^p} L_i^t odot (Theta^{t-1} - Theta_i^{t-1})^p,
   so one gradient step on W_i^p induces an element-wise squared-difference scaled parameter step
   Delta Theta_hat_i^{t,p} = -eta * ((Theta^{t-1} - Theta_i^{t-1})^p)^{odot 2} odot nabla_{Theta_hat_i^p} L_i^t
   (when W_i^p stays in the interior (0, 1)), strictly reducing client i's local objective L_i^t
   relative to FedAvg overwriting (W_i^p = 1).
"""

def clip01(x):
    return max(0.0, min(1.0, x))

def main():
    # 4 parameters: first 2 in lower layers (|Theta|-p = 2), last 2 in higher layers (p = 2)
    theta_global = [1.0, -1.0, 2.0, -2.0]
    theta_local = [0.2, -0.3, 0.5, -0.4]
    # True client target optimum has generic lower layers matching global [1.0, -1.0]
    # but personalized higher layers [0.6, -0.2] (where global -2.0 is harmful!)
    theta_client_star = [1.0, -1.0, 0.6, -0.2]

    def local_loss(th):
        return 0.5 * sum((th[k] - theta_client_star[k]) ** 2 for k in range(4))

    def local_grad(th):
        return [th[k] - theta_client_star[k] for k in range(4)]

    # FedAvg overwrites all layers (W_i^p = [1.0, 1.0])
    W_p = [1.0, 1.0]
    theta_hat_init = [
        theta_local[0] + (theta_global[0] - theta_local[0]) * 1.0,
        theta_local[1] + (theta_global[1] - theta_local[1]) * 1.0,
        theta_local[2] + (theta_global[2] - theta_local[2]) * clip01(W_p[0]),
        theta_local[3] + (theta_global[3] - theta_local[3]) * clip01(W_p[1]),
    ]
    loss_fedavg_init = local_loss(theta_hat_init)

    # One unclipped interior step (starting from W_p = [0.5, 0.5]) to verify exact Eq. 6 identity
    W_p_int = [0.5, 0.5]
    th_before = [
        theta_global[0],
        theta_global[1],
        theta_local[2] + (theta_global[2] - theta_local[2]) * W_p_int[0],
        theta_local[3] + (theta_global[3] - theta_local[3]) * W_p_int[1],
    ]
    g_th = local_grad(th_before)
    eta = 0.1
    # Appendix A Eq. 7 gradient wrt W_i^p
    grad_W_p = [
        g_th[2] * (theta_global[2] - theta_local[2]),
        g_th[3] * (theta_global[3] - theta_local[3]),
    ]
    W_p_after = [W_p_int[j] - eta * grad_W_p[j] for j in range(2)]
    th_after = [
        theta_global[0],
        theta_global[1],
        theta_local[2] + (theta_global[2] - theta_local[2]) * W_p_after[0],
        theta_local[3] + (theta_global[3] - theta_local[3]) * W_p_after[1],
    ]
    # Verify Eq. 6: th_after[2+j] - th_before[2+j] == -eta * (theta_global[2+j] - theta_local[2+j])^2 * g_th[2+j]
    for j in range(2):
        lhs = th_after[2 + j] - th_before[2 + j]
        rhs = -eta * ((theta_global[2 + j] - theta_local[2 + j]) ** 2) * g_th[2 + j]
        assert abs(lhs - rhs) < 1e-15, f"Eq. 6 mismatch on dim {j}: {lhs} vs {rhs}"

    # Run clipped ALA weight optimization from W_p = [1.0, 1.0]
    W_curr = [1.0, 1.0]
    for _ in range(15):
        th_curr = [
            theta_global[0],
            theta_global[1],
            theta_local[2] + (theta_global[2] - theta_local[2]) * clip01(W_curr[0]),
            theta_local[3] + (theta_global[3] - theta_local[3]) * clip01(W_curr[1]),
        ]
        g_curr = local_grad(th_curr)
        for j in range(2):
            W_curr[j] = clip01(W_curr[j] - 0.25 * g_curr[2 + j] * (theta_global[2 + j] - theta_local[2 + j]))

    th_ala = [
        theta_global[0],
        theta_global[1],
        theta_local[2] + (theta_global[2] - theta_local[2]) * W_curr[0],
        theta_local[3] + (theta_global[3] - theta_local[3]) * W_curr[1],
    ]
    loss_ala_init = local_loss(th_ala)
    assert loss_ala_init < 0.05 * loss_fedavg_init, f"Expected ALA loss {loss_ala_init} << FedAvg init loss {loss_fedavg_init}"
    print(f"[PASS] Round 455 FedALA verified: loss_fedavg_init={loss_fedavg_init:.4f} -> loss_ala_init={loss_ala_init:.6f}, W_p={W_curr}")

if __name__ == "__main__":
    main()
