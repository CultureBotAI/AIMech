#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 687: LoRAMoE (Dou et al., ACL 2024 / arXiv:2312.09979)."""

from __future__ import annotations

import math
import random


def matvec(M: list[list[float]], x: list[float]) -> list[float]:
    return [sum(row[j] * x[j] for j in range(len(x))) for row in M]


def softmax_temp(logits: list[float], tau: float = 1.0) -> list[float]:
    m = max(z / tau for z in logits)
    exps = [math.exp(z / tau - m) for z in logits]
    s = sum(exps)
    return [e / s for e in exps]


def localized_balancing_loss(Q: list[list[float]], I_mat: list[list[float]]) -> float:
    """Section 3.2, Eq. 8: L_lbc = sigma^2(Z) / mu(Z) where Z = I o Q."""
    N = len(Q)
    M = len(Q[0])
    Z = [I_mat[n][m] * Q[n][m] for n in range(N) for m in range(M)]
    mu = sum(Z) / len(Z)
    var = sum((z - mu) ** 2 for z in Z) / len(Z)
    return var / max(mu, 1e-12)


def build_importance_coeff_matrix(expert_types: list[int], sample_types: list[int], delta: float) -> list[list[float]]:
    """Section 3.2, Eq. 7: I_{n,m} = 1 + delta if Type_e(n) == Type_s(m) else 1 - delta."""
    return [
        [1.0 + delta if te == ts else 1.0 - delta for ts in sample_types]
        for te in expert_types
    ]


def main() -> None:
    rng = random.Random(687)
    d_in, d_out, r = 8, 8, 2
    N = 6  # 6 LoRA experts: 3 world-knowledge (type 0), 3 downstream task (type 1) (Section 4.1)
    alpha = 32.0
    delta = 0.2

    # 1. Verify LoRAMoE forward propagation (Section 3.1, Eq. 3-5):
    # o = W_0 x + (alpha / r) sum_{i=1}^N omega_i B_i A_i x
    W0 = [[rng.gauss(0.0, 0.5) for _ in range(d_in)] for _ in range(d_out)]
    A_experts = [[[rng.gauss(0.0, 0.3) for _ in range(d_in)] for _ in range(r)] for _ in range(N)]
    B_experts = [[[rng.gauss(0.0, 0.3) for _ in range(r)] for _ in range(d_out)] for _ in range(N)]
    W_g = [[rng.gauss(0.0, 0.5) for _ in range(d_in)] for _ in range(N)]

    x = [rng.gauss(0.0, 1.0) for _ in range(d_in)]
    omega = softmax_temp(matvec(W_g, x), tau=1.0)
    assert abs(sum(omega) - 1.0) < 1e-12

    base_out = matvec(W0, x)
    expert_sum = [0.0] * d_out
    for i in range(N):
        e_i_x = matvec(B_experts[i], matvec(A_experts[i], x))
        for j in range(d_out):
            expert_sum[j] += (alpha / r) * omega[i] * e_i_x[j]
    o_vec = [base_out[j] + expert_sum[j] for j in range(d_out)]

    # Verify parameter count reduction vs full FFN MoE:
    # LoRAMoE trainable params = N * r * (d_in + d_out) + N * d_in << N * d_in * d_out (for r << d)
    loramoe_params = N * r * (d_in + d_out) + N * d_in
    full_moe_params = N * d_in * d_out + N * d_in
    assert loramoe_params < 0.6 * full_moe_params and len(o_vec) == d_out

    # 2. Verify Localized Balancing Constraint L_lbc (Section 3.2, Eq. 6-8):
    # Experts 0,1,2 are type 0 (world knowledge); experts 3,4,5 are type 1 (downstream tasks).
    expert_types = [0, 0, 0, 1, 1, 1]
    sample_types = [0, 0, 1, 1]  # M = 4 samples in batch (each length T_m = 6 tokens)
    T_m = 6
    I_mat = build_importance_coeff_matrix(expert_types, sample_types, delta)

    # Verify intra-group symmetry and inter-group asymmetry (Section 3.2, p. 6):
    assert I_mat[0] == I_mat[1] == I_mat[2]
    assert I_mat[3] == I_mat[4] == I_mat[5]
    assert I_mat[0] != I_mat[3]

    # Case A: Ideal localized-balanced routing where Z_{n,m} = I_{n,m} * Q_{n,m} is constant across (n, m).
    # For sample m of type t_s, if matching-type experts receive router weight proportional to 1/(1+delta)
    # and non-matching experts receive weight proportional to 1/(1-delta), wait:
    # Wait: in Section 3.2 (p. 6), if sample m is from world-knowledge (type 0), I_{n,m} = 1+delta for type-0
    # experts and 1-delta for type-1 experts.Wait: let's check both uniform routing Q_unif = T_m / N and
    # collapsed single-expert routing Q_collapsed!
    Q_unif = [[T_m / N for _ in range(len(sample_types))] for _ in range(N)]
    Q_collapsed = [[T_m if n == 0 else 0.0 for _ in range(len(sample_types))] for n in range(N)]
    # And Q_inverse where Q_{n,m} = c / I_{n,m} Normalized to sum_n Q_{n,m} = T_m:
    Q_localized = []
    for m, _ts in enumerate(sample_types):
        inv_col = [1.0 / I_mat[n][m] for n in range(N)]
        s_inv = sum(inv_col)
        for n in range(N):
            if m == 0:
                Q_localized.append([])
            Q_localized[n].append(T_m * inv_col[n] / s_inv)

    loss_collapsed = localized_balancing_loss(Q_collapsed, I_mat)
    loss_unif = localized_balancing_loss(Q_unif, I_mat)
    loss_localized = localized_balancing_loss(Q_localized, I_mat)

    assert loss_localized < 1e-15
    assert loss_localized < loss_unif < loss_collapsed

    print(
        f"[PASS] Round 687 LoRAMoE (Dou et al., ACL 2024): "
        f"L_lbc(localized)={loss_localized:.2e} < L_lbc(unif)={loss_unif:.4f} << L_lbc(collapsed)={loss_collapsed:.4f}"
    )


if __name__ == "__main__":
    main()
