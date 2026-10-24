#!/usr/bin/env python3
"""Constructed boundary verification for Round 584: GaLore (Zhao et al., ICML 2024)."""

from __future__ import annotations

import math


def mat_mul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    m, k, n = len(a), len(a[0]), len(b[0])
    return [
        [sum(a[i][p] * b[p][j] for p in range(k)) for j in range(n)]
        for i in range(m)
    ]


def mat_transpose(a: list[list[float]]) -> list[list[float]]:
    return [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]


def frob_sq(a: list[list[float]]) -> float:
    return sum(x * x for row in a for x in row)


def spectral_norm_sq_2x2_or_3x3(a: list[list[float]]) -> float:
    # Power iteration on A^T A for exact largest singular value squared
    at_a = mat_mul(mat_transpose(a), a)
    n = len(at_a)
    v = [1.0 / math.sqrt(n)] * n
    for _ in range(80):
        wv = [sum(at_a[i][j] * v[j] for j in range(n)) for i in range(n)]
        norm = math.sqrt(sum(x * x for x in wv))
        if norm < 1e-30:
            return 0.0
        v = [x / norm for x in wv]
    wv = [sum(at_a[i][j] * v[j] for j in range(n)) for i in range(n)]
    return sum(v[i] * wv[i] for i in range(n))


def stable_rank(a: list[list[float]]) -> float:
    return frob_sq(a) / spectral_norm_sq_2x2_or_3x3(a)


def main() -> None:
    # 1. Verify Lemma 3.3 / Lemma B.3 (Equations 8-9, 28-39):
    # G_t = A - B W_t C under W_t = W_{t-1} + eta G_{t-1} -> G_t = G_{t-1} - eta B G_{t-1} C.
    # Choose diagonal PSD B = diag(1.0, 4.0) and C = diag(1.0, 2.0) on R^{2x2}.
    # Then S = C x B has eigenvalues:
    # (1*1 = 1.0) on e1 e1^T, (1*4 = 4.0) on e2 e1^T, (2*1 = 2.0) on e1 e2^T, (2*4 = 8.0) on e2 e2^T.
    # So minimal eigenvalue is lambda_1 = 1.0 (rank-1 minimal eigenspace V_1 spanned by e1 e1^T, sr(G_0^||) = 1.0)
    # and second smallest eigenvalue is lambda_2 = 2.0!
    b_diag = [1.0, 4.0]
    c_diag = [1.0, 2.0]
    lam1, lam2 = 1.0, 2.0
    eta = 0.1

    g_mat = [[1.0, 2.0], [3.0, 4.0]]
    g0_par = [[g_mat[0][0], 0.0], [0.0, 0.0]]
    g0_perp_frob_sq = g_mat[0][1] ** 2 + g_mat[1][0] ** 2 + g_mat[1][1] ** 2
    g0_par_spec_sq = g0_par[0][0] ** 2
    sr_g0_par = 1.0  # Corollary 3.5: 1D minimal eigenspace with decomposable v = e1 x e1 has sr(G_0^||) = 1

    sr_0 = stable_rank(g_mat)
    for t in range(1, 35):
        # Update G_t = G_{t-1} - eta B G_{t-1} C
        g_mat = [
            [
                g_mat[i][j] - eta * b_diag[i] * g_mat[i][j] * c_diag[j]
                for j in range(2)
            ]
            for i in range(2)
        ]
        sr_t = stable_rank(g_mat)
        rhs_bound = sr_g0_par + (((1.0 - eta * lam2) / (1.0 - eta * lam1)) ** (2 * t)) * (
            g0_perp_frob_sq / g0_par_spec_sq
        )
        assert sr_t <= rhs_bound + 1e-12, f"Lemma 3.3 bound violated at t={t}: {sr_t} > {rhs_bound}"

    sr_final = stable_rank(g_mat)
    assert abs(sr_final - 1.0) < 1e-4 and sr_final < sr_0

    # 2. Verify Theorem 3.8 & Section 4.1 (Composition of Low-Rank Subspaces vs Fixed-Rank LoRA):
    # Consider full-rank target W^* = diag(3.0, 2.0, 1.0) in R^{3x3} with linear regression loss
    # phi(W) = 0.5 * ||W - W^*||_F^2, so negative gradient is G_t = W^* - W_t.
    # Any rank-1 LoRA parameterization W = B A (B in R^{3x1}, A in R^{1x3}) has rank(W) <= 1,
    # so by Eckart-Young theorem ||B A - W^*||_F^2 >= sigma_2^2 + sigma_3^2 = 2^2 + 1^2 = 5.0!
    # In contrast, rank-1 GaLore switching subspace every T = 15 steps via top-1 singular vector p_t of G_t
    # learns the full-rank matrix W^* to < 1e-10 error while keeping rank-1 optimizer state!
    w_star = [[3.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 1.0]]
    w_galore = [[0.0, 0.0, 0.0] for _ in range(3)]
    eta_g = 0.5
    switch_t = 30
    p_proj = [[1.0], [0.0], [0.0]]  # 3 x 1 left projector

    for step in range(3 * switch_t):
        g_cur = [[w_star[i][j] - w_galore[i][j] for j in range(3)] for i in range(3)]
        if step % switch_t == 0:
            # Top-1 left singular vector of G_cur (since G_cur is diagonal, pick row with largest norm)
            row_norms = [math.sqrt(sum(g_cur[i][j] ** 2 for j in range(3))) for i in range(3)]
            best_i = max(range(3), key=lambda i: row_norms[i])
            p_proj = [[1.0 if i == best_i else 0.0] for i in range(3)]
        # Project gradient into compact space R_t = P_t^T G_t (1 x 3)
        r_t = mat_mul(mat_transpose(p_proj), g_cur)
        # Project back G_tilde = P_t R_t (3 x 3)
        g_tilde = mat_mul(p_proj, r_t)
        w_galore = [
            [w_galore[i][j] + eta_g * g_tilde[i][j] for j in range(3)]
            for i in range(3)
        ]

    err_galore_sq = frob_sq([[w_galore[i][j] - w_star[i][j] for j in range(3)] for i in range(3)])
    lora_rank1_min_err_sq = 2.0**2 + 1.0**2  # Eckart-Young lower bound for rank-1 W = B A
    assert err_galore_sq < 1e-14 and err_galore_sq < 1e-14 * lora_rank1_min_err_sq

    # 3. Verify Table 1 memory formulas for W in R^{m x n} (m <= n) with rank r:
    # GaLore: mn (weights) + mr (P_t) + 2nr (M_t, V_t) = mn + mr + 2nr
    # LoRA:   mn + mr + nr (weights W_0, B, A) + 2mr + 2nr (Adam states for B, A) = mn + 3mr + 3nr
    # Full-rank Adam: mn (weights) + 2mn (M_t, V_t) = 3mn
    m, n, r = 1024, 2048, 256
    mem_galore = m * n + m * r + 2 * n * r
    mem_lora = m * n + 3 * m * r + 3 * n * r
    mem_full = 3 * m * n
    assert mem_galore < mem_lora < mem_full

    print(
        f"[PASS] Round 584 GaLore verified: sr_0={sr_0:.4f}->sr_final={sr_final:.6f}, "
        f"err_galore_sq={err_galore_sq:.3e}<<lora_min={lora_rank1_min_err_sq:.1f}, "
        f"mem=({mem_galore}<{mem_lora}<{mem_full})"
    )


if __name__ == "__main__":
    main()
