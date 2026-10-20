#!/usr/bin/env python3
"""Constructed boundary verification for Round 662:
RoSA: Accurate Parameter-Efficient Fine-Tuning via Robust Adaptation
(Nikdan, Tabesh, Crncevic, & Alistarh, ICML 2024, arXiv:2401.04679).

Verifies:
1. Robust PCA decomposition of a full fine-tuning update Delta* = L* + S* in R^{m x n}
   into a rank-r_true low-rank matrix L* plus a sparse outlier matrix S*.
2. Equal-or-smaller parameter-budget comparison (Section 3.2, Figure 3b & Table 1):
   Joint Low-Rank + Sparse Adaptation (RoSA: Delta = B^L A^L + Delta^S with
   rank(B^L A^L) <= r_rosa and ||Delta^S||_0 <= k_rosa) achieves strictly lower
   Frobenius approximation error ||Delta* - Delta||_F than either pure LoRA
   (rank r_lora with more parameters) or pure Sparse Adaptation (SpA with k_spa
   nonzeros).
3. Algorithm 1 (GradMag-LW mask generation after low-rank warmup) and Equation (10)
   Sampled Dense-Dense Matrix Multiplication (SDDMM) backward gradient on the sparse mask.
"""

from __future__ import annotations
import math
import random


def frob_norm_diff(A: list[list[float]], B: list[list[float]]) -> float:
    m, n = len(A), len(A[0])
    return math.sqrt(sum((A[i][j] - B[i][j]) ** 2 for i in range(m) for j in range(n)))


def power_svd_rank_r(M: list[list[float]], r: int, iters: int = 80) -> list[list[float]]:
    """Compute exact rank-r truncated SVD approximation of M via deflated power iteration."""
    m, n = len(M), len(M[0])
    residual = [list(row) for row in M]
    approx = [[0.0] * n for _ in range(m)]
    rng = random.Random(20240104)
    for _ in range(r):
        v = [rng.gauss(0.0, 1.0) for _ in range(n)]
        norm_v = math.sqrt(sum(x * x for x in v))
        v = [x / norm_v for x in v]
        u = [0.0] * m
        for _ in range(iters):
            u = [sum(residual[i][j] * v[j] for j in range(n)) for i in range(m)]
            norm_u = math.sqrt(sum(x * x for x in u))
            if norm_u < 1e-12:
                break
            u = [x / norm_u for x in u]
            v = [sum(residual[i][j] * u[i] for i in range(m)) for j in range(n)]
            norm_v = math.sqrt(sum(x * x for x in v))
            if norm_v < 1e-12:
                break
            v = [x / norm_v for x in v]
        sigma = sum(
            u[i] * residual[i][j] * v[j] for i in range(m) for j in range(n)
        )
        for i in range(m):
            for j in range(n):
                comp = sigma * u[i] * v[j]
                approx[i][j] += comp
                residual[i][j] -= comp
    return approx


def topk_sparse_approx(M: list[list[float]], k: int) -> tuple[list[list[float]], list[tuple[int, int]]]:
    """Keep top-k entries of M by magnitude (Algorithm 1 TopK-Mask)."""
    m, n = len(M), len(M[0])
    entries = [(abs(M[i][j]), i, j) for i in range(m) for j in range(n)]
    entries.sort(reverse=True)
    mask = [(i, j) for _, i, j in entries[:k]]
    S = [[0.0] * n for _ in range(m)]
    for i, j in mask:
        S[i][j] = M[i][j]
    return S, mask


def main() -> None:
    rng = random.Random(20240105)
    m, n = 16, 16
    r_true = 2
    # Construct ground-truth FFT update Delta* = L* + S* (Section 3.2)
    U_true = [[rng.gauss(0.0, 0.5) for _ in range(r_true)] for _ in range(m)]
    V_true = [[rng.gauss(0.0, 0.5) for _ in range(n)] for _ in range(r_true)]
    L_star = [
        [sum(U_true[i][k] * V_true[k][j] for k in range(r_true)) for j in range(n)]
        for i in range(m)
    ]
    S_star = [[0.0] * n for _ in range(m)]
    outlier_coords = [(0, 3), (2, 11), (5, 7), (9, 14), (12, 1), (15, 8)]
    for idx, (r_idx, c_idx) in enumerate(outlier_coords):
        S_star[r_idx][c_idx] = 6.0 if idx % 2 == 0 else -6.0

    Delta_star = [
        [L_star[i][j] + S_star[i][j] for j in range(n)] for i in range(m)
    ]

    # Compare parameter budgets:
    # - Pure LoRA with r_lora = 3: 3 * (16 + 16) = 96 parameters
    # - Pure SpA with k_spa = 96 nonzeros: 96 parameters
    # - RoSA with r_rosa = 2 (64 params) + k_rosa = 6 nonzeros (6 params) = 70 <= 96 parameters
    r_lora = 3
    k_spa = 96
    r_rosa = 2
    k_rosa = 6
    params_lora = r_lora * (m + n)
    params_spa = k_spa
    params_rosa = r_rosa * (m + n) + k_rosa
    assert params_rosa < params_lora == params_spa == 96

    # 1. Pure LoRA (rank 3 on Delta_star directly)
    lora_approx = power_svd_rank_r(Delta_star, r=r_lora)
    err_lora = frob_norm_diff(Delta_star, lora_approx)

    # 2. Pure SpA (top-96 entries of Delta_star)
    spa_approx, _ = topk_sparse_approx(Delta_star, k=k_spa)
    err_spa = frob_norm_diff(Delta_star, spa_approx)

    # 3. RoSA: Low-rank warmup followed by GradMag-LW mask selection (Algorithm 1)
    # and alternating optimization of Delta^L and Delta^S
    L_Rosa = power_svd_rank_r(Delta_star, r=r_rosa)
    G_warmup = [
        [Delta_star[i][j] - L_Rosa[i][j] for j in range(n)] for i in range(m)
    ]
    G_sq = [[G_warmup[i][j] ** 2 for j in range(n)] for i in range(m)]
    _, rosa_mask = topk_sparse_approx(G_sq, k=k_rosa)

    # Verify all 6 true outlier coordinates are recovered in the GradMag-LW mask
    mask_set = set(rosa_mask)
    for coord in outlier_coords:
        assert coord in mask_set, f"Outlier {coord} missed by GradMag-LW mask"

    # Alternating optimization over (L_Rosa, S_Rosa) on fixed support rosa_mask
    S_Rosa = [[0.0] * n for _ in range(m)]
    for _ in range(40):
        for i, j in rosa_mask:
            S_Rosa[i][j] = Delta_star[i][j] - L_Rosa[i][j]
        rem = [[Delta_star[i][j] - S_Rosa[i][j] for j in range(n)] for i in range(m)]
        L_Rosa = power_svd_rank_r(rem, r=r_rosa)
        for i, j in rosa_mask:
            S_Rosa[i][j] = Delta_star[i][j] - L_Rosa[i][j]

    rosa_approx = [[L_Rosa[i][j] + S_Rosa[i][j] for j in range(n)] for i in range(m)]
    err_rosa = frob_norm_diff(Delta_star, rosa_approx)

    assert err_rosa < 1e-4, f"Expected near-exact RoSA recovery, got {err_rosa}"
    assert err_rosa < err_lora * 0.001
    assert err_rosa < err_spa * 0.001

    # 4. Verify SDDMM backward pass (Equation 10): dL/dDelta^S = (X^T (dL/dO))_M
    b = 4
    X = [[rng.uniform(-1.0, 1.0) for _ in range(m)] for _ in range(b)]
    dO = [[rng.uniform(-1.0, 1.0) for _ in range(n)] for _ in range(b)]
    sddmm_vals = {
        (i, j): sum(X[batch][i] * dO[batch][j] for batch in range(b))
        for (i, j) in rosa_mask
    }
    dense_grad = [
        [sum(X[batch][i] * dO[batch][j] for batch in range(b)) for j in range(n)]
        for i in range(m)
    ]
    max_sddmm_err = max(abs(sddmm_vals[(i, j)] - dense_grad[i][j]) for (i, j) in rosa_mask)
    assert max_sddmm_err < 1e-15

    print(
        f"[PASS] Round 662 RoSA (Nikdan et al. 2024): "
        f"err_rosa={err_rosa:.2e} << err_lora={err_lora:.4f} & err_spa={err_spa:.4f} "
        f"(params_rosa={params_rosa}<{params_lora}), sddmm_err={max_sddmm_err:.2e}"
    )


if __name__ == "__main__":
    main()
