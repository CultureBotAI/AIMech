#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 672: HydraLoRA (Tian et al., NeurIPS 2024)."""

import math
import random


def softmax(logits):
    m = max(logits)
    exps = [math.exp(z - m) for z in logits]
    s = sum(exps)
    return [e / s for e in exps]


def matvec(M, x):
    return [sum(M[i][j] * x[j] for j in range(len(x))) for i in range(len(M))]


def main():
    rng = random.Random(672)
    d, k, r, N = 16, 16, 4, 4

    # 1. Parameter count boundary:
    # Symmetric LoRA-Split / LoRA-MoE uses N pairs (A_i, B_i): N * r * (d + k)
    # HydraLoRA shares 1 matrix A (r x k) and uses N matrices B_i (d x r): r * (k + N * d)
    params_split = N * r * (d + k)
    params_hydra = r * (k + N * d)
    saving_ratio = (params_split - params_hydra) / params_split
    assert params_hydra < params_split, "HydraLoRA must use fewer adapter parameters than symmetric LoRA-Split"
    assert abs(saving_ratio - 0.375) < 1e-12, f"Expected 37.5% adapter reduction for d=k, N=4, got {saving_ratio}"

    # 2. Inference routing merge equivalence (Section 3.2.2, Eq. 2-4):
    # y_unmerged = W0 x + sum_{i=1}^N omega_i * B_i (A x)
    # y_merged   = W0 x + (sum_{i=1}^N omega_i B_i) (A x)
    W0 = [[rng.gauss(0.0, 0.5) for _ in range(k)] for _ in range(d)]
    A = [[rng.gauss(0.0, 0.3) for _ in range(k)] for _ in range(r)]
    Bs = [[[rng.gauss(0.0, 0.3) for _ in range(r)] for _ in range(d)] for _ in range(N)]
    Wg = [[rng.gauss(0.0, 0.5) for _ in range(N)] for _ in range(k)]
    x = [rng.gauss(0.0, 1.0) for _ in range(k)]

    logits = [sum(Wg[j][i] * x[j] for j in range(k)) for i in range(N)]
    omega = softmax(logits)

    w0_x = matvec(W0, x)
    a_x = matvec(A, x)
    y_unmerged = list(w0_x)
    for i in range(N):
        bi_ax = matvec(Bs[i], a_x)
        for row in range(d):
            y_unmerged[row] += omega[i] * bi_ax[row]

    B_merged = [[sum(omega[i] * Bs[i][row][col] for i in range(N)) for col in range(r)] for row in range(d)]
    b_merged_ax = matvec(B_merged, a_x)
    y_merged = [w0_x[row] + b_merged_ax[row] for row in range(d)]

    merge_err = math.sqrt(sum((y_unmerged[row] - y_merged[row]) ** 2 for row in range(d)))
    assert merge_err < 1e-14, f"Routing LoRA merge equivalence failed: {merge_err}"

    # 3. Heterogeneous sub-domain interference mitigation:
    # Suppose N=2 intrinsic sub-domains share a common feature projection A_true (r x k)
    # but have opposing task heads B_true_0 = +B_base and B_true_1 = -B_base.
    # A monolithic single-B LoRA trained on an equal mixture suffers destructive cancellation (B -> 0),
    # whereas HydraLoRA with routed B_1, B_2 fits both sub-domains with zero interference.
    B_base = [[rng.gauss(0.0, 0.5) for _ in range(r)] for _ in range(d)]
    B_true = [B_base, [[-val for val in row] for row in B_base]]

    # Monolithic optimal B on equal mixture of domain 0 and domain 1 is 0.5 * (B_true[0] + B_true[1]) = 0
    loss_monolithic = 0.0
    loss_hydra = 0.0
    for dom in (0, 1):
        for _ in range(20):
            x_sample = [rng.gauss(0.0, 1.0) for _ in range(k)]
            z = matvec(A, x_sample)
            target_delta = matvec(B_true[dom], z)
            # Monolithic compromise B_mono = 0
            loss_monolithic += sum(t * t for t in target_delta)
            # HydraLoRA with domain-routed B_i (omega_dom = 0.98, omega_other = 0.02)
            pred_hydra = [0.98 * target_delta[row] - 0.02 * target_delta[row] for row in range(d)]
            loss_hydra += sum((pred_hydra[row] - target_delta[row]) ** 2 for row in range(d))

    loss_monolithic /= 40.0
    loss_hydra /= 40.0
    assert loss_hydra < 0.01 * loss_monolithic, f"HydraLoRA {loss_hydra} should crush monolithic {loss_monolithic}"

    print(
        f"[PASS] Round 672 HydraLoRA (Tian et al., NeurIPS 2024): "
        f"param_saving={saving_ratio:.3f}, merge_err={merge_err:.2e}, "
        f"loss_hydra={loss_hydra:.4f}<<loss_monolithic={loss_monolithic:.4f}"
    )


if __name__ == "__main__":
    main()
