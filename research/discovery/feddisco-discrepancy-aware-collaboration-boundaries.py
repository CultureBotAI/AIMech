#!/usr/bin/env python3
"""Constructed boundary verification for FedDisco (Ye et al., ICML 2023, PMLR 202:39879-39902, arXiv:2305.19229)."""

import math

def l2_discrepancy(D_k, T_dist):
    return math.sqrt(sum((dk - tc) ** 2 for dk, tc in zip(D_k, T_dist)))

def disco_weights(n_rel, d_vals, a, b):
    # Eq. (3): p_k = ReLU(n_k - a * d_k + b) / sum_m ReLU(n_m - a * d_m + b)
    raw = [max(0.0, nk - a * dk + b) for nk, dk in zip(n_rel, d_vals)]
    total = sum(raw)
    return [r / total for r in raw]

def theorem45_bound(p_weights, n_rel, d_vals):
    # Theorem 4.5 (Eq. 49) in finite-T regime (Appendix C.4): A = 2*tau*(tau-1)*eta^2*L^2 < 1/3
    K = len(p_weights)
    tau = 5
    eta = 0.035
    L = 2.0
    sigma = 0.2
    B = 4.0
    T_rounds = 20
    F_gap = 1.0
    A = 2.0 * tau * (tau - 1.0) * (eta ** 2) * (L ** 2)  # A = 40 * 0.001225 * 4 = 0.196 < 1/3
    W_D = 2.0 * K * sum((n_rel[k] - p_weights[k]) ** 2 for k in range(K))
    T0 = 1.0 - 3.0 * A - W_D * (1.0 - A)
    assert T0 > 0.0, f"Expected T0 > 0, got {T0}"
    T1 = 2.0 * (1.0 - A) * F_gap / (tau * eta * T_rounds)
    T2 = (1.0 - A) * W_D * B * sum(d_vals) / K
    T3 = 2.0 * (1.0 - A) * L * eta * (sigma ** 2) * sum(p ** 2 for p in p_weights)
    T4 = 2.0 * (tau - 1.0) * (sigma ** 2) * (L ** 2) * (eta ** 2)
    T5 = 2.0 * A * B * sum(p_weights[k] * d_vals[k] for k in range(K))
    return (T1 + T2 + T3 + T4 + T5) / T0

def main():
    # NIID-2 setup from Section 7.1: 5 biased clients (each holding 1 out of 5 classes) and 1 unbiased client (uniform across all 5 classes)
    C = 5
    K = 6
    T_unif = [1.0 / C for _ in range(C)]
    D_clients = [
        [1.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 1.0],
        [0.2, 0.2, 0.2, 0.2, 0.2],  # Client 5: unbiased category distribution
    ]
    n_rel = [1.0 / K for _ in range(K)]  # Equal dataset sizes
    d_vals = [l2_discrepancy(D_k, T_unif) for D_k in D_clients]
    assert abs(d_vals[5]) < 1e-15
    assert all(d_vals[k] > 0.8 for k in range(5))

    p_fedavg = list(n_rel)
    # Test both large-distinguishing Disco weights (Section 5.1) and KKT-optimal Theorem 4.5 weights (Appendix C.5 Eq. 54)
    p_disco_dist = disco_weights(n_rel, d_vals, a=0.15, b=0.05)
    assert abs(sum(p_disco_dist) - 1.0) < 1e-14
    assert p_disco_dist[5] > 1.5 * p_disco_dist[0], f"Expected unbiased client weight > 1.5x biased client weight: {p_disco_dist}"

    # Verify Theorem 4.5 optimization upper bound is strictly tighter under discrepancy-aware weights (Eq. 2-3 / Eq. 54) than naive dataset-size weights
    d_bar = sum(d_vals) / K
    a_kkt = 0.008
    p_disco_thm = disco_weights(n_rel, d_vals, a=a_kkt, b=a_kkt * d_bar)
    assert p_disco_thm[5] > p_disco_thm[0]
    bound_fedavg = theorem45_bound(p_fedavg, n_rel, d_vals)
    bound_disco = theorem45_bound(p_disco_thm, n_rel, d_vals)
    assert bound_disco < bound_fedavg, f"Expected bound_disco={bound_disco} < bound_fedavg={bound_fedavg}"

    print(
        f"[PASS] Round 469 FedDisco verified: p_biased={p_disco_dist[0]:.4f} < p_unbiased={p_disco_dist[5]:.4f}, "
        f"Thm4.5_bound={bound_fedavg:.6f}->{bound_disco:.6f}"
    )

if __name__ == "__main__":
    main()
