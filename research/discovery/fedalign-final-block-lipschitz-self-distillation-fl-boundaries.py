#!/usr/bin/env python3
"""Constructed boundary verification for Round 495: FedAlign (Mendieta et al. 2022)."""

from __future__ import annotations

import math


def matmul_t_a_b(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """Compute A^T B where A is (N x D1) and B is (N x D2)."""
    n = len(a)
    d1 = len(a[0])
    d2 = len(b[0])
    out = [[0.0] * d2 for _ in range(d1)]
    for i in range(d1):
        for j in range(d2):
            out[i][j] = sum(a[r][i] * b[r][j] for r in range(n))
    return out


def power_iteration_spectral_norm(mat: list[list[float]], iters: int = 80) -> float:
    """Compute spectral norm ||X||_SN via power iteration (Yao et al. 2018 / Mendieta et al. 2022)."""
    rows = len(mat)
    cols = len(mat[0])
    v = [1.0 / math.sqrt(cols) * ((j + 1) * 0.7) for j in range(cols)]
    v_norm = math.sqrt(sum(x * x for x in v))
    v = [x / v_norm for x in v]
    sigma = 0.0
    for _ in range(iters):
        # u = X v
        u = [sum(mat[i][j] * v[j] for j in range(cols)) for i in range(rows)]
        u_norm = math.sqrt(sum(x * x for x in u))
        u = [x / u_norm for x in u]
        # v = X^T u
        v_new = [sum(mat[i][j] * u[i] for i in range(rows)) for j in range(cols)]
        sigma = math.sqrt(sum(x * x for x in v_new))
        v = [x / sigma for x in v_new]
    return sigma


def exact_2x2_or_rank2_spectral_norm(mat: list[list[float]]) -> float:
    """Exact largest singular value via eigenvalues of M M^T when rows=2."""
    assert len(mat) == 2
    cols = len(mat[0])
    a11 = sum(mat[0][j] * mat[0][j] for j in range(cols))
    a12 = sum(mat[0][j] * mat[1][j] for j in range(cols))
    a22 = sum(mat[1][j] * mat[1][j] for j in range(cols))
    tr = a11 + a22
    det = a11 * a22 - a12 * a12
    lam_max = 0.5 * (tr + math.sqrt(max(0.0, tr * tr - 4.0 * det)))
    return math.sqrt(lam_max)


def hessian_matching_metrics(diag_k: list[float], diag_j: list[float]) -> tuple[float, float]:
    """Equations 3-4 (Mendieta et al. 2022): H_N^{k,j} and H_D^{k,j}."""
    norm_k = math.sqrt(sum(x * x for x in diag_k))
    norm_j = math.sqrt(sum(x * x for x in diag_j))
    h_n = (norm_k - norm_j) ** 2
    h_d = sum(x * y for x, y in zip(diag_k, diag_j)) / (norm_k * norm_j)
    return h_n, h_d


def main() -> None:
    # 1. Transmitting matrices X_F = f_{L-1}^T f_L and X_S = f_{L-1}^T f_L^{omega_S} (Equations 6-7):
    # Batch of B=3 samples, penultimate feature dim C_{L-1}=2, final block dim C_L=4, slimming omega_S=0.5 (2 channels)
    f_prev = [
        [1.2, -0.4],
        [0.5, 1.1],
        [-0.8, 0.7],
    ]
    # Final block weights W_L (2 x 4)
    w_last = [
        [1.5, -0.6, 0.9, 1.2],
        [0.4, 1.3, -1.1, 0.8],
    ]
    # Full final-block feature map f_L = f_prev @ W_L
    f_full = [
        [sum(f_prev[b][i] * w_last[i][j] for i in range(2)) for j in range(4)]
        for b in range(3)
    ]
    # Uniformly slimmed final-block feature map f_L^{omega_S} (first 2 channels, omega_S = 0.5)
    f_slim = [row[:2] for row in f_full]

    x_f = matmul_t_a_b(f_prev, f_full)
    x_s = matmul_t_a_b(f_prev, f_slim)

    k_f = power_iteration_spectral_norm(x_f)
    k_s = power_iteration_spectral_norm(x_s)
    k_f_exact = exact_2x2_or_rank2_spectral_norm(x_f)
    k_s_exact = exact_2x2_or_rank2_spectral_norm(x_s)

    assert abs(k_f - k_f_exact) < 1e-12
    assert abs(k_s - k_s_exact) < 1e-12
    assert k_f > k_s > 0.0

    # Lipschitz self-distillation loss L_Lip(K_S, K_F) = (K_S - K_F)^2
    loss_lip_before = (k_s - k_f) ** 2
    # Shrinking the non-slimmed channels (columns 2..3 of W_L) reduces K_F toward K_S
    w_reg = [
        [w_last[i][0], w_last[i][1], 0.5 * w_last[i][2], 0.5 * w_last[i][3]]
        for i in range(2)
    ]
    f_full_reg = [
        [sum(f_prev[b][i] * w_reg[i][j] for i in range(2)) for j in range(4)]
        for b in range(3)
    ]
    k_f_reg = power_iteration_spectral_norm(matmul_t_a_b(f_prev, f_full_reg))
    loss_lip_after = (k_s - k_f_reg) ** 2
    assert loss_lip_after < loss_lip_before
    assert k_f_reg < k_f

    # 2. Second-order cross-client Hessian matching metrics (Equations 3-4):
    h_unreg_1 = [12.0, 8.5, 15.0]
    h_unreg_2 = [4.0, 9.0, 2.5]
    h_reg_1 = [4.2, 3.8, 4.5]
    h_reg_2 = [3.9, 3.6, 4.1]
    hn_unreg, hd_unreg = hessian_matching_metrics(h_unreg_1, h_unreg_2)
    hn_reg, hd_reg = hessian_matching_metrics(h_reg_1, h_reg_2)
    assert hn_reg < hn_unreg
    assert hd_reg > hd_unreg

    # 3. Computational overhead: reusing f_{L-1} on only the final block L (1 of 4 blocks) at width omega_S=0.25
    l_blocks = 4
    omega_s = 0.25
    fedalign_rel_flops = 1.0 + (omega_s ** 2) / l_blocks
    gradaug_rel_flops = 1.0 + (0.8 ** 2) + (0.9 ** 2)
    assert 1.0 < fedalign_rel_flops < 1.05 < gradaug_rel_flops

    print(
        f"[PASS] Round 495 FedAlign (Mendieta et al. 2022): K_F={k_f:.4f}->K_F_reg={k_f_reg:.4f} "
        f"(K_S={k_s:.4f}, pi_err={abs(k_f - k_f_exact):.2e}), H_N={hn_unreg:.2f}->{hn_reg:.2f}, "
        f"H_D={hd_unreg:.4f}->{hd_reg:.4f}, rel_FLOPs={fedalign_rel_flops:.4f}"
    )


if __name__ == "__main__":
    main()
