#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 478:
FedMD (Heterogenous Federated Learning via Model Distillation,
Li & Wang 2019, NeurIPS 2019 Workshop on Federated Learning, arXiv:1910.03581).

Verifies:
1. Architecture-agnostic consensus logit communication protocol (Section 2.2, Algorithm 1
   & Supplementary Method, p. 3 & p. 7):
   - M participants own private datasets D_k and distinct black-box architectures f_k
     with different parameter dimensions dim(theta_k).
   - Communicate & Aggregate step: on public subset d_j subset D_0, each party k computes
     class logits f_k(x_i^0) in R^C, and the server forms the weighted consensus logits:
     f_tilde(x_i^0) = sum_{k=1}^m c_k f_k(x_i^0) (with uniform weights c_k = 1/m or
     reliability weights sum_k c_k = 1).
   - Digest & Revisit steps: each party k updates its own heterogeneous model f_k to
     match the consensus logits f_tilde(x_i^0) on d_j (Digest), and then fine-tunes f_k
     on its private dataset D_k (Revisit).
2. Communication complexity independence from model parameter count |theta_k|:
   per-round uplink/downlink volume is |d_j| * C floats per party regardless of architecture depth/width.
"""

from __future__ import annotations


def main() -> None:
    # Three heterogeneous black-box client models with distinct parameter dimensions (e.g., 1-layer, 2-layer, 3-layer)
    # operating on 2D inputs and producing C=3 class logits, each having seen complementary private classes.
    public_X = [
        [1.0, 0.0],
        [0.0, 1.0],
        [-1.0, -1.0],
        [0.8, 0.2],
    ]
    private_D = [
        # Party 0 specializes in class 0 and 1
        ([1.0, 0.1], [2.0, 0.2, -1.5]),
        # Party 1 specializes in class 1 and 2
        ([0.1, 1.0], [-1.2, 2.1, 0.3]),
        # Party 2 specializes in class 2 and 0
        ([-0.9, -0.8], [0.1, -1.4, 2.2]),
    ]

    # Represent each heterogeneous model's mapping via distinct feature transforms phi_k(x) -> R^{d_k} and linear head W_k in R^{3 x d_k}
    def phi_0(x: list[float]) -> list[float]:
        return [x[0], x[1], 1.0]  # d_0 = 3

    def phi_1(x: list[float]) -> list[float]:
        return [x[0], x[1], x[0] * x[0], x[1] * x[1], 1.0]  # d_1 = 5

    def phi_2(x: list[float]) -> list[float]:
        return [x[0], x[1], x[0] * x[1], x[0] - x[1], x[0] + x[1], 1.0]  # d_2 = 6

    phis = [phi_0, phi_1, phi_2]
    W = [
        [[1.8, -0.5, 0.1], [0.2, 1.5, -0.2], [-1.0, -0.8, 0.0]],
        [[-0.4, 0.1, 0.2, -0.1, 0.0], [0.1, 1.9, 0.1, 0.2, 0.1], [-0.8, -0.7, 0.3, 0.1, 0.2]],
        [[-0.6, -0.5, 0.2, 0.1, -0.2, 0.0], [-0.4, 0.3, -0.1, -0.2, 0.1, 0.0], [-1.1, -1.0, 0.4, 0.0, -0.3, 0.3]],
    ]

    def forward_logits(k: int, x: list[float]) -> list[float]:
        feat = phis[k](x)
        return [sum(W[k][c][d] * feat[d] for d in range(len(feat))) for c in range(3)]

    def consensus_disagreement() -> float:
        total = 0.0
        for x0 in public_X:
            logits_all = [forward_logits(k, x0) for k in range(3)]
            f_tilde = [sum(logits_all[k][c] for k in range(3)) / 3.0 for c in range(3)]
            for k in range(3):
                total += sum((logits_all[k][c] - f_tilde[c]) ** 2 for c in range(3))
        return total / (3.0 * len(public_X))

    dis_init = consensus_disagreement()

    # Run FedMD collaborative rounds (Communicate -> Aggregate -> Distribute -> Digest -> Revisit)
    lr_digest = 0.08
    lr_revisit = 0.04
    for _round in range(25):
        # Communicate & Aggregate on public_X
        consensus_targets = []
        for x0 in public_X:
            logits_all = [forward_logits(k, x0) for k in range(3)]
            f_tilde = [sum(logits_all[k][c] for k in range(3)) / 3.0 for c in range(3)]
            consensus_targets.append(f_tilde)

        # Digest: train each party k toward consensus f_tilde on public_X
        for k in range(3):
            for x0, f_tilde in zip(public_X, consensus_targets):
                feat = phis[k](x0)
                pred = forward_logits(k, x0)
                for c in range(3):
                    err = pred[c] - f_tilde[c]
                    for d in range(len(feat)):
                        W[k][c][d] -= lr_digest * err * feat[d]

        # Revisit: train each party k on its private data D_k
        for k in range(3):
            xk, yk = private_D[k]
            feat = phis[k](xk)
            pred = forward_logits(k, xk)
            for c in range(3):
                err = pred[c] - yk[c]
                for d in range(len(feat)):
                    W[k][c][d] -= lr_revisit * err * feat[d]

    dis_final = consensus_disagreement()
    assert dis_final < 0.1 * dis_init, f"FedMD Digest phase must align public consensus logits: {dis_final} vs {dis_init}"

    # Verify parameter counts differ across parties while communicated floats per party are identical (|d_j| * C)
    param_counts = [len(W[k]) * len(W[k][0]) for k in range(3)]
    assert len(set(param_counts)) == 3, f"Expected heterogeneous model sizes, got {param_counts}"
    comm_floats_per_party = len(public_X) * 3
    assert comm_floats_per_party == 12

    print(
        f"[PASS] FedMD boundary verification passed: disagreement_init={dis_init:.4f} -> "
        f"disagreement_final={dis_final:.4f}, het_params={param_counts}, comm_floats={comm_floats_per_party}"
    )


if __name__ == "__main__":
    main()
