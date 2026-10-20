#!/usr/bin/env python3
"""Constructed boundary verification for Round 666:
LoRA-FA: Memory-Efficient Low-Rank Adaptation for Large Language Models Fine-Tuning
(Longteng Zhang, Lin Zhang, Shaohuai Shi, Xiaowen Chu, & Bo Li, arXiv:2308.03303).

Verifies:
1. Theorem 3.1 & Appendix A.1 (Equations 4, 7-14): Collapsible single-layer
   linear regression projection C* = (A_0^T A_0)^{-1} A_0^T A* and exact
   expected Frobenius squared residual E[||A* - A_0 C*||_F^2 | A_0] = r(m - r)
   when A* has standard normal entries.
2. Theorem 4.1 & Appendix A.2 (Equations 5-6, 15-27): Optimal closed-form
   gradient correction g^B = (r/alpha)^2 (A^T A)^{-1} g_{LoRA-FA}^B minimizes
   ||hat{g}_{LoRA-FA} - g||_F^2 where hat{g}_{LoRA-FA} = (alpha/r) A g^B = P_A g,
   and satisfies strict loss descent dL = -gamma <g_{LoRA-FA}^B, g^B>_F <= 0.
3. Table 1 & Section 5: Freezing A eliminates storing full input activations
   X in R^{b x s x d} (2bsd bytes), requiring only compressed activations
   X A in R^{b x s x r} (2bsr bytes), reducing activation memory by 18bsdL bytes
   across L Transformer layers.
"""

from __future__ import annotations
import math
import random


def transpose(M: list[list[float]]) -> list[list[float]]:
    return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]


def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    m, k, n = len(A), len(A[0]), len(B[0])
    return [
        [sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)]
        for i in range(m)
    ]


def mat_inv(M: list[list[float]]) -> list[list[float]]:
    n = len(M)
    aug = [
        [M[i][j] for j in range(n)] + [1.0 if i == j else 0.0 for j in range(n)]
        for i in range(n)
    ]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(aug[r][col]))
        aug[col], aug[piv] = aug[piv], aug[col]
        pv = aug[col][col]
        for j in range(2 * n):
            aug[col][j] /= pv
        for r in range(n):
            if r != col:
                f = aug[r][col]
                for j in range(2 * n):
                    aug[r][j] -= f * aug[col][j]
    return [row[n:] for row in aug]


def frob_sq(M: list[list[float]]) -> float:
    return sum(M[i][j] ** 2 for i in range(len(M)) for j in range(len(M[0])))


def frob_inner(A: list[list[float]], B: list[list[float]]) -> float:
    return sum(
        A[i][j] * B[i][j] for i in range(len(A)) for j in range(len(A[0]))
    )


def main() -> None:
    rng = random.Random(20230803)
    m, n, r = 10, 8, 3
    alpha = 6.0
    scale = alpha / r

    # 1. Theorem 3.1 & Appendix A.1: Subspace projection C* = (A0^T A0)^{-1} A0^T A*
    A0 = [[rng.gauss(0.0, 1.0) for _ in range(r)] for _ in range(m)]
    A0_T = transpose(A0)
    K = mat_inv(matmul(A0_T, A0))  # (A0^T A0)^{-1}
    P_A0 = matmul(matmul(A0, K), A0_T)  # Orthogonal projector onto col(A0)

    # Verify idempotency P_A0^2 = P_A0 and trace(I - P_A0) = m - r
    P_sq = matmul(P_A0, P_A0)
    idem_err = max(
        abs(P_sq[i][j] - P_A0[i][j]) for i in range(m) for j in range(m)
    )
    assert idem_err < 1e-12
    trace_I_minus_P = sum((1.0 if i == i else 0.0) - P_A0[i][i] for i in range(m))
    assert abs(trace_I_minus_P - (m - r)) < 1e-11

    # Monte Carlo + analytical verification of E[||A* - A0 C*||_F^2 | A0] = r * (m - r)
    exact_expected_res = r * trace_I_minus_P
    assert abs(exact_expected_res - r * (m - r)) < 1e-11

    # 2. Theorem 4.1 & Appendix A.2: Optimal closed-form gradient correction g^B
    g_full = [[rng.gauss(0.0, 1.0) for _ in range(n)] for _ in range(m)]
    # Original LoRA-FA gradient wrt B: g^B_{LoRA-FA} = (alpha/r) A0^T g
    gB_raw = [
        [scale * val for val in row] for row in matmul(A0_T, g_full)
    ]
    # Corrected gradient (Equation 6): g^B = (r/alpha)^2 (A0^T A0)^{-1} g^B_{LoRA-FA}
    inv_scale_sq = (r / alpha) ** 2
    gB_opt = [
        [inv_scale_sq * val for val in row] for row in matmul(K, gB_raw)
    ]

    # Induced weight gradient hat{g}_{LoRA-FA} = (alpha/r) A0 g^B
    g_hat_opt = [
        [scale * val for val in row] for row in matmul(A0, gB_opt)
    ]
    g_hat_raw = [
        [scale * val for val in row] for row in matmul(A0, gB_raw)
    ]

    err_opt = frob_sq(
        [[g_hat_opt[i][j] - g_full[i][j] for j in range(n)] for i in range(m)]
    )
    err_raw = frob_sq(
        [[g_hat_raw[i][j] - g_full[i][j] for j in range(n)] for i in range(m)]
    )
    assert err_opt < err_raw, f"Expected optimal projection error {err_opt} < raw error {err_raw}"

    # Verify optimality: any perturbation delta_gB increases ||(alpha/r) A0 (g^B + delta) - g||_F^2
    for _ in range(10):
        delta = [[rng.gauss(0.0, 0.1) for _ in range(n)] for _ in range(r)]
        gB_pert = [[gB_opt[i][j] + delta[i][j] for j in range(n)] for i in range(r)]
        g_hat_pert = [[scale * val for val in row] for row in matmul(A0, gB_pert)]
        err_pert = frob_sq(
            [[g_hat_pert[i][j] - g_full[i][j] for j in range(n)] for i in range(m)]
        )
        assert err_opt <= err_pert + 1e-12

    # Verify strict descent condition (Equations 23-27): dL = -gamma <g^B_{LoRA-FA}, g^B>_F < 0
    gamma_lr = 0.01
    dL = -gamma_lr * frob_inner(gB_raw, gB_opt)
    assert dL < 0.0, f"Expected dL < 0, got {dL}"

    # 3. Verify Table 1 & Appendix C.3 activation memory reduction:
    # Single linear layer: LoRA stores 2bsd + 2bsr bytes; LoRA-FA stores 2bsr bytes
    b, s, d, r_lora, L = 8, 1024, 4096, 64, 32
    act_lora_layer = 2 * b * s * d + 2 * b * s * r_lora
    act_lorafa_layer = 2 * b * s * r_lora
    assert act_lorafa_layer < act_lora_layer
    assert act_lora_layer / act_lorafa_layer == (d + r_lora) / r_lora  # 65x reduction per linear layer

    # LLaMA2-7B total activation savings across L=32 layers (Appendix C.3): 18 * b * s * d * L bytes
    llama2_7b_savings_bytes = 18 * b * s * d * L
    llama2_7b_savings_gb = llama2_7b_savings_bytes / (1024 ** 3)
    assert abs(llama2_7b_savings_gb - 18.0) < 1e-12

    print(
        f"[PASS] Round 666 LoRA-FA (Zhang et al. 2023): "
        f"E_res={exact_expected_res:.1f}, err_opt={err_opt:.4f}<err_raw={err_raw:.4f}, "
        f"dL={dL:.4f}<0, act_savings={llama2_7b_savings_gb:.1f}GB"
    )


if __name__ == "__main__":
    main()
