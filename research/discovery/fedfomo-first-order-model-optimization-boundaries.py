#!/usr/bin/env python3
"""Constructed boundary verification for FedFomo (Zhang et al., ICLR 2021, arXiv:2012.08565)."""

import math

def quad_loss(theta, target):
    return 0.5 * sum((a - b) ** 2 for a, b in zip(theta, target))

def l2_dist(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

def fomo_weights(theta_prev_i, candidate_models, target_i):
    # Eq. (3) & (12)-(13): w_n = (L_i(theta_i^{l(t-1)}) - L_i(theta_n^{l(t)})) / ||theta_n^{l(t)} - theta_i^{l(t-1)}||
    base_loss = quad_loss(theta_prev_i, target_i)
    raw_w = []
    for theta_n in candidate_models:
        dist = l2_dist(theta_n, theta_prev_i)
        if dist < 1e-12:
            raw_w.append(0.0)
        else:
            raw_w.append((base_loss - quad_loss(theta_n, target_i)) / dist)
    pos_w = [max(w, 0.0) for w in raw_w]
    denom = sum(pos_w)
    if denom < 1e-12:
        norm_w = [0.0 for _ in raw_w]
    else:
        norm_w = [w / denom for w in pos_w]
    return raw_w, norm_w

def main():
    # 1. Verify Appendix A.1 Eq. (9)-(11): phi_n(w) = w * theta_n + (1 - w) * theta_prev_i
    # For linear loss L_i(theta) = g^T theta + c, L_i(phi_n(1)) - L_i(phi_n(0)) == d/dw L_i(phi_n(0)) exactly
    theta_prev = [0.2, -0.4, 0.5]
    theta_cand = [0.8, 0.1, -0.2]
    g = [-1.2, 0.7, 0.4]
    def lin_loss(th):
        return sum(gi * ti for gi, ti in zip(g, th))
    def phi_n(w):
        return [w * tn + (1.0 - w) * tp for tn, tp in zip(theta_cand, theta_prev)]
    eps = 1e-7
    deriv_at_0 = (lin_loss(phi_n(eps)) - lin_loss(phi_n(0.0))) / eps
    secant_diff = lin_loss(phi_n(1.0)) - lin_loss(phi_n(0.0))
    assert abs(deriv_at_0 - secant_diff) < 1e-9

    # 2. Verify Eq. (3) & (13) on in-distribution and out-of-local-distribution personalization
    # 4 clients: Clients 0 and 1 share target A = [2.0, 2.0]; Clients 2 and 3 share target B = [-2.0, -2.0]
    target_0 = [2.0, 2.0]
    theta_prev_0 = [0.5, 0.4]  # previous round model of client 0
    uploaded_models = [
        [1.5, 1.4],   # Client 0 current model (closer to target A)
        [1.8, 1.9],   # Client 1 current model (even closer to target A)
        [-1.6, -1.5], # Client 2 current model (target B, harmful for client 0)
        [-1.9, -1.8], # Client 3 current model (target B, harmful for client 0)
    ]
    raw_w, w_star = fomo_weights(theta_prev_0, uploaded_models, target_0)
    # Harmful models (2, 3) have negative raw weights and are clipped to 0 in w_star
    assert raw_w[0] > 0.0 and raw_w[1] > 0.0
    assert raw_w[2] < 0.0 and raw_w[3] < 0.0
    assert w_star[2] == 0.0 and w_star[3] == 0.0
    assert abs(sum(w_star) - 1.0) < 1e-12

    theta_fomo = [
        theta_prev_0[d] + sum(w_star[n] * (uploaded_models[n][d] - theta_prev_0[d]) for n in range(4))
        for d in range(2)
    ]
    theta_fedavg = [sum(uploaded_models[n][d] for n in range(4)) / 4.0 for d in range(2)]
    loss_prev = quad_loss(theta_prev_0, target_0)
    loss_fomo = quad_loss(theta_fomo, target_0)
    loss_fedavg = quad_loss(theta_fedavg, target_0)
    assert loss_fomo < loss_prev < loss_fedavg

    # 3. Verify early-stopping fallback when all candidate models perform worse than theta_prev_i
    worse_models = [[-1.0, -1.0], [-2.0, -2.0]]
    _, w_fallback = fomo_weights([1.9, 1.9], worse_models, target_0)
    assert sum(w_fallback) == 0.0

    print(
        f"[PASS] Round 464 FedFomo verified: w_star={[round(w, 3) for w in w_star]}, "
        f"L_fomo={loss_fomo:.4f} < L_prev={loss_prev:.4f} < L_fedavg={loss_fedavg:.4f}"
    )

if __name__ == "__main__":
    main()
