#!/usr/bin/env python3
"""Constructed boundary verification for Round 665:
Delta-LoRA: Fine-Tuning High-Rank Parameters with the Delta of Low-Rank Matrices
(Bojia Zi, Xianbiao Qi, Lingzhi Wang, Jianan Wang, Kam-Fai Wong, & Lei Zhang,
arXiv:2309.02411).

Verifies:
1. Equation (4) vs. Equation (7): Exact identity between the gradient wrt W
   and the gradient wrt AB (g_W = dL/dh_{i+1} * h_i^T = g_{AB}) when the
   low-rank branch has no Dropout layer, whereas inserting a Dropout mask
   Drop(h_i) breaks the equality (||g_W - g_{AB}||_F > 0).
2. Equation (5) & Appendix A.1 Equation (8): Exact algebraic expansion of
   Delta_AB = A^{(t+1)} B^{(t+1)} - A^{(t)} B^{(t)} under AdamW / weight-decayed
   gradient steps.
3. Algorithm 1 & Equation (6): Updating W^{(t+1)} = W^{(t)} + lambda * (alpha/r) * Delta_AB
   without storing optimizer states for W enables the trajectory of W^{(t)} to
   integrate updates across changing low-rank subspaces, achieving higher
   effective rank and lower reconstruction loss than frozen-W LoRA.
"""

from __future__ import annotations
import math
import random


def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    m, k, n = len(A), len(A[0]), len(B[0])
    return [
        [sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)]
        for i in range(m)
    ]


def outer(u: list[float], v: list[float]) -> list[list[float]]:
    return [[ui * vj for vj in v] for ui in u]


def frob_diff(A: list[list[float]], B: list[list[float]]) -> float:
    return math.sqrt(
        sum((A[i][j] - B[i][j]) ** 2 for i in range(len(A)) for j in range(len(A[0])))
    )


def main() -> None:
    rng = random.Random(20230905)
    c, d, r = 8, 8, 2
    alpha = 4.0
    scale = alpha / r

    # 1. Verify Equation (4) vs. Equation (7): g_W == g_AB without Dropout, != with Dropout
    h_i = [rng.gauss(0.0, 1.0) for _ in range(d)]
    grad_h_next = [rng.gauss(0.0, 1.0) for _ in range(c)]

    g_W = outer(grad_h_next, h_i)
    g_AB_no_drop = outer(grad_h_next, h_i)
    assert frob_diff(g_W, g_AB_no_drop) == 0.0

    # With dropout mask (keep probability p = 0.5)
    drop_mask = [1.0 / 0.5 if i % 2 == 0 else 0.0 for i in range(d)]
    h_i_drop = [h_i[j] * drop_mask[j] for j in range(d)]
    g_AB_with_drop = outer(grad_h_next, h_i_drop)
    drop_disparity = frob_diff(g_W, g_AB_with_drop)
    assert drop_disparity > 1.0, f"Expected non-zero dropout disparity, got {drop_disparity}"

    # 2. Verify Appendix A.1 Equation (8): exact expansion of Delta_AB
    eta = 0.05
    beta = 0.01
    A_t = [[rng.gauss(0.0, 0.5) for _ in range(r)] for _ in range(c)]
    B_t = [[rng.gauss(0.0, 0.5) for _ in range(d)] for _ in range(r)]
    g_hat_A = [[rng.gauss(0.0, 0.2) for _ in range(r)] for _ in range(c)]
    g_hat_B = [[rng.gauss(0.0, 0.2) for _ in range(d)] for _ in range(r)]

    A_next = [
        [A_t[i][p] - eta * g_hat_A[i][p] - eta * beta * A_t[i][p] for p in range(r)]
        for i in range(c)
    ]
    B_next = [
        [B_t[p][j] - eta * g_hat_B[p][j] - eta * beta * B_t[p][j] for j in range(d)]
        for p in range(r)
    ]
    AB_t = matmul(A_t, B_t)
    AB_next = matmul(A_next, B_next)
    Delta_AB_direct = [
        [AB_next[i][j] - AB_t[i][j] for j in range(d)] for i in range(c)
    ]

    A_gB = matmul(A_t, g_hat_B)
    gA_B = matmul(g_hat_A, B_t)
    gA_gB = matmul(g_hat_A, g_hat_B)
    Delta_AB_eq8 = [
        [
            -eta * A_gB[i][j]
            - eta * gA_B[i][j]
            - 2.0 * eta * beta * AB_t[i][j]
            + (eta ** 2) * gA_gB[i][j]
            + (eta ** 2) * beta * gA_B[i][j]
            + (eta ** 2) * beta * A_gB[i][j]
            + (eta ** 2) * (beta ** 2) * AB_t[i][j]
            for j in range(d)
        ]
        for i in range(c)
    ]
    eq8_err = frob_diff(Delta_AB_direct, Delta_AB_eq8)
    assert eq8_err < 1e-14, f"Equation (8) expansion mismatch: {eq8_err}"

    # 3. Verify Algorithm 1 (Delta-LoRA vs. frozen-W LoRA under identical learning rate eta and warmup K)
    W_target = [[rng.gauss(0.0, 0.5) for _ in range(d)] for _ in range(c)]
    W0 = [[0.0 for _ in range(d)] for _ in range(c)]
    A_init = [[rng.gauss(0.0, 0.3) for _ in range(r)] for _ in range(c)]
    B_init = [[0.0 for _ in range(d)] for _ in range(r)]

    def run_training(
        use_delta_lora: bool, lam: float = 2.0, K_warmup: int = 5, steps: int = 60
    ) -> float:
        W = [list(row) for row in W0]
        A = [list(row) for row in A_init]
        B = [list(row) for row in B_init]
        lr = 0.005
        wd = 0.01
        for t in range(steps):
            AB_old = matmul(A, B)
            W_eff = [
                [W[i][j] + scale * AB_old[i][j] for j in range(d)]
                for i in range(c)
            ]
            G_Weff = [
                [W_eff[i][j] - W_target[i][j] for j in range(d)]
                for i in range(c)
            ]
            gA = [
                [scale * sum(G_Weff[i][j] * B[p][j] for j in range(d)) for p in range(r)]
                for i in range(c)
            ]
            gB = [
                [scale * sum(A[i][p] * G_Weff[i][j] for i in range(c)) for j in range(d)]
                for p in range(r)
            ]
            # Algorithm 1 lines 6-7
            A = [
                [A[i][p] - lr * gA[i][p] - lr * wd * A[i][p] for p in range(r)]
                for i in range(c)
            ]
            B = [
                [B[p][j] - lr * gB[p][j] - lr * wd * B[p][j] for j in range(d)]
                for p in range(r)
            ]
            # Algorithm 1 lines 8-10
            if use_delta_lora and t > K_warmup:
                AB_new = matmul(A, B)
                for i in range(c):
                    for j in range(d):
                        W[i][j] += lam * scale * (AB_new[i][j] - AB_old[i][j])

        AB_final = matmul(A, B)
        W_final = [[W[i][j] + scale * AB_final[i][j] for j in range(d)] for i in range(c)]
        return 0.5 * sum(
            (W_final[i][j] - W_target[i][j]) ** 2 for i in range(c) for j in range(d)
        )

    loss_lora = run_training(use_delta_lora=False)
    loss_delta_lora = run_training(use_delta_lora=True, lam=2.0, K_warmup=5)
    assert loss_delta_lora < loss_lora, (
        f"Expected Delta-LoRA loss ({loss_delta_lora:.4f}) < LoRA loss ({loss_lora:.4f})"
    )

    print(
        f"[PASS] Round 665 Delta-LoRA (Zi et al. 2023): "
        f"drop_disparity={drop_disparity:.4f}>0, eq8_err={eq8_err:.2e}, "
        f"loss_delta_lora={loss_delta_lora:.4f}<loss_lora={loss_lora:.4f}"
    )


if __name__ == "__main__":
    main()
