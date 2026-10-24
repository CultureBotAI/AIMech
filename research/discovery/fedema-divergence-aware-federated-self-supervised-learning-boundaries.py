#!/usr/bin/env python3
"""Constructed boundary verification for Round 490: FedEMA (Zhuang et al. 2022, ICLR 2022).

Verifies:
1. Divergence-Aware Dynamic EMA Update (Section 4, Equations 1-3, Algorithm 1):
   W_k^r = mu * W_k^{r-1} + (1 - mu) * W_g^r,
   W_k^{p,r} = mu * W_k^{p,r-1} + (1 - mu) * W_g^{p,r},
   where mu = min(lambda_k * ||W_g^r - W_k^{r-1}||_2, 1).
2. Exact Reduction to FedBYOL at lambda_k = 0 (Section 4):
   When lambda_k = 0, mu = 0 and W_k^r = W_g^r, W_k^{p,r} = W_g^{p,r} (full global replacement).
3. Practical Personalized Autoscaler Calibration (Section 4, Algorithm 1 line 10):
   lambda_k = tau / ||W_g^{r+1} - W_k^r||_2 calibrated at client k's earliest sampled round
   guarantees that the initial divergence-aware decay rate equals tau in (0, 1) when evaluated
   at the calibration divergence, and decreases monotonically as ||W_g^r - W_k^{r-1}||_2 shrinks.
4. Non-IID Local Representation Retention Advantage (Sections 3.5 & 4):
   On heterogeneous client feature subspaces, divergence-aware EMA retains client-specific
   online/target alignment and achieves lower representation reconstruction error than
   naive global overwriting (FedBYOL, mu = 0) or isolated standalone training (mu = 1).
"""

import math


def l2_dist(u, v):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))


def fedema_update(w_local_prev, w_global, lam_k):
    """Equations (1)-(3) divergence-aware EMA update."""
    div = l2_dist(w_global, w_local_prev)
    mu = min(lam_k * div, 1.0)
    w_updated = [mu * wl + (1.0 - mu) * wg for wl, wg in zip(w_local_prev, w_global)]
    return w_updated, mu, div


def verify_fedema_boundaries():
    # 1. Verify exact reduction to FedBYOL at lambda = 0 (Section 4)
    w_prev = [1.2, -0.8, 0.5]
    w_glob = [0.2, 0.4, -0.3]
    w_byol, mu_zero, _ = fedema_update(w_prev, w_glob, lam_k=0.0)
    assert mu_zero == 0.0
    assert all(abs(a - b) < 1e-12 for a, b in zip(w_byol, w_glob)), "lambda=0 must reduce to FedBYOL"

    # 2. Verify Autoscaler calibration (Section 4, Algorithm 1 line 10):
    # At earliest round r=0, client k finishes local training with W_k^0 and server aggregates W_g^1
    tau = 0.7
    init_div = l2_dist(w_glob, w_prev)
    lam_k = tau / init_div
    _, mu_cal, _ = fedema_update(w_prev, w_glob, lam_k)
    assert abs(mu_cal - tau) < 1e-12, f"Autoscaler failed to calibrate mu={mu_cal} to tau={tau}"

    # Verify that as divergence shrinks during training (Figure 6), mu decreases monotonically
    w_glob_later = [0.8 * a + 0.2 * b for a, b in zip(w_prev, w_glob)]  # 20% of initial divergence
    _, mu_later, div_later = fedema_update(w_prev, w_glob_later, lam_k)
    assert div_later < init_div and mu_later < mu_cal, (
        f"Expected smaller mu as divergence shrinks: {mu_later} vs {mu_cal}"
    )

    # 3. Verify Siamese target-online alignment under non-IID heterogeneity (Sections 3.5 & 4):
    # Suppose K = 2 clients have true representation prototypes theta^*_k = theta_shared + delta_k
    # where theta_shared = [1.0, 1.0] is shared semantic structure and delta_k = [+-0.6, -+0.6]
    # is client-specific non-IID view structure, and each client has noisy local estimate hat_theta_k.
    theta_true = [[1.6, 0.4], [0.4, 1.6]]
    # Local noisy online encoders after local SSL epoch (high variance [+-0.35, +-0.35] on shared direction):
    w_local = [[1.95, 0.75], [0.05, 1.25]]
    # Server global aggregate W_g = 0.5 * (w_local[0] + w_local[1]) cancels zero-mean shared noise
    # [1.0, 1.0] accurately on the shared component, but erases client-specific skew delta_k:
    w_g = [0.5 * (w_local[0][d] + w_local[1][d]) for d in range(2)]

    # Compare MSE to true client representation prototypes under:
    # (a) FedBYOL (mu = 0: full overwrite with W_g)
    # (b) Standalone (mu = 1: no global collaboration)
    # (c) FedEMA (autoscaled tau = 0.7 -> mu = 0.7)
    def mse_clients(models):
        return sum(l2_dist(models[k], theta_true[k]) ** 2 for k in range(2)) / 2.0

    models_byol = [fedema_update(w_local[k], w_g, lam_k=0.0)[0] for k in range(2)]
    models_standalone = [fedema_update(w_local[k], w_g, lam_k=100.0)[0] for k in range(2)]
    models_fedema = []
    for k in range(2):
        lk = 0.7 / l2_dist(w_g, w_local[k])
        models_fedema.append(fedema_update(w_local[k], w_g, lam_k=lk)[0])

    err_byol = mse_clients(models_byol)
    err_standalone = mse_clients(models_standalone)
    err_fedema = mse_clients(models_fedema)

    assert err_fedema < err_byol and err_fedema < err_standalone, (
        f"FedEMA MSE {err_fedema} should beat FedBYOL {err_byol} and Standalone {err_standalone}"
    )

    print(
        f"[PASS] Round 490 FedEMA (Zhuang et al. 2022): mu_cal={mu_cal:.2f} -> mu_later={mu_later:.2f}, "
        f"err_fedema={err_fedema:.4f} < err_standalone={err_standalone:.4f} < err_byol={err_byol:.4f}"
    )


if __name__ == "__main__":
    verify_fedema_boundaries()
