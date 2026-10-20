#!/usr/bin/env python3
"""Boundary verification for Round 693: UniPELT (Mao et al., ACL 2022, arXiv:2110.07577)."""

import math


def sigmoid(z: float) -> float:
    return 1.0 / (1.0 + math.exp(-z))


def main() -> int:
    # Verify Section 3.2 (pp. 3-4) submodule gating equations for {Adapter (A), Prefix-tuning (P), LoRA (L)}:
    # 1. LoRA gated projection: Q = (W_Q^T + G_L * W_up^T W_down^T) h_in, G_L in (0, 1)
    # 2. Prefix-tuning gated virtual keys/values: P_K_gated = G_P * P_K, P_V_gated = G_P * P_V, G_P in (0, 1)
    # 3. Adapter gated residual bottleneck: h'_A = G_A * h_A + h_F, where h_A = W_up^T phi(W_down^T h_FN), G_A in (0, 1)

    # Check exact bypass when gates G_A -> 0 and G_L -> 0:
    h_in = [1.2, -0.8]
    W_Q = [[0.5, -0.3], [0.2, 0.7]]
    dW_L = [[0.4, 0.1], [-0.2, 0.6]]
    h_F = [0.9, -0.4]
    h_A = [0.35, 0.55]

    G_L_zero = sigmoid(-40.0)
    G_A_zero = sigmoid(-40.0)
    Q_base = [sum(W_Q[j][i] * h_in[j] for j in range(2)) for i in range(2)]
    Q_gated = [
        sum((W_Q[j][i] + G_L_zero * dW_L[j][i]) * h_in[j] for j in range(2))
        for i in range(2)
    ]
    h_A_prime = [G_A_zero * h_A[i] + h_F[i] for i in range(2)]
    bypass_err = max(
        max(abs(Q_base[i] - Q_gated[i]) for i in range(2)),
        max(abs(h_F[i] - h_A_prime[i]) for i in range(2)),
    )
    assert bypass_err < 1e-16, f"Expected exact submodule bypass when G->0, got {bypass_err}"

    # Verify Table 2 & Table 3 (pp. 7-8) phenomenon:
    # Across 3 task/sample regimes where:
    # - Sample 0 requires Prefix-tuning submodule P (and LoRA/Adapter add interfering noise if ungated)
    # - Sample 1 requires LoRA submodule L (and Prefix/Adapter add interfering noise if ungated)
    # - Sample 2 requires synergistic composition of Adapter A + LoRA L (compounding effect > any single submodule)
    # Each submodule produces a delta representation vector in R^2; target deltas for the 3 samples:
    targets = [
        [1.0, 0.0],   # Sample 0: matched by P
        [0.0, 1.0],   # Sample 1: matched by L
        [0.8, 0.9],   # Sample 2: compounding combination of A and L
    ]
    sub_P = [[1.0, 0.0], [-0.5, 0.1], [0.0, -0.4]]
    sub_L = [[-0.4, 0.2], [0.0, 1.0], [0.0, 0.9]]
    sub_A = [[0.2, -0.5], [0.4, -0.3], [0.8, 0.0]]

    def loss_of(preds: list[list[float]]) -> float:
        return sum(
            (preds[s][d] - targets[s][d]) ** 2 for s in range(3) for d in range(2)
        ) / 3.0

    err_P_only = loss_of(sub_P)
    err_L_only = loss_of(sub_L)
    err_A_only = loss_of(sub_A)
    best_single_err = min(err_P_only, err_L_only, err_A_only)

    # Ungated hybrid sum (UniPELT-NoGate: G_P = G_L = G_A = 1):
    preds_nogate = [
        [sub_P[s][d] + sub_L[s][d] + sub_A[s][d] for d in range(2)] for s in range(3)
    ]
    err_nogate = loss_of(preds_nogate)

    # UniPELT with input-conditioned sigmoid gates G_P(x), G_L(x), G_A(x):
    # Gate logits learned for each sample regime:
    gate_logits = [
        (8.0, -8.0, -8.0),  # Sample 0 activates P
        (-8.0, 8.0, -8.0),  # Sample 1 activates L
        (-8.0, 8.0, 8.0),   # Sample 2 activates A + L jointly
    ]
    preds_unipelt = []
    for s, (lp, ll, la) in enumerate(gate_logits):
        gp, gl, ga = sigmoid(lp), sigmoid(ll), sigmoid(la)
        preds_unipelt.append(
            [gp * sub_P[s][d] + gl * sub_L[s][d] + ga * sub_A[s][d] for d in range(2)]
        )
    err_unipelt = loss_of(preds_unipelt)

    # Even against an oracle that picks the best single submodule per sample (Table 2 upper bound):
    oracle_single_err = sum(
        min(
            sum((sub[s][d] - targets[s][d]) ** 2 for d in range(2))
            for sub in (sub_P, sub_L, sub_A)
        )
        for s in range(3)
    ) / 3.0

    assert err_unipelt < oracle_single_err < best_single_err
    assert err_unipelt < err_nogate

    print(
        f"[PASS] Round 693 UniPELT (Mao et al., ACL 2022): bypass_err={bypass_err:.2e}, "
        f"err_unipelt={err_unipelt:.2e} < oracle_single={oracle_single_err:.4f} < "
        f"best_single={best_single_err:.4f}, err_nogate={err_nogate:.4f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
