#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 671: LoRA-GA (Wang et al., NeurIPS 2024)."""

import math
import random


def matmul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)] for i in range(m)]


def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def frob_sq(A):
    return sum(x * x for row in A for x in row)


def mat_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mat_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mat_scale(A, c):
    return [[c * x for x in row] for row in A]


def random_orthogonal(n, rng):
    cols = []
    for _ in range(n):
        v = [rng.gauss(0.0, 1.0) for _ in range(n)]
        for u in cols:
            dot = sum(v[i] * u[i] for i in range(n))
            v = [v[i] - dot * u[i] for i in range(n)]
        norm = math.sqrt(sum(x * x for x in v))
        cols.append([x / norm for x in v])
    # Return n x n matrix whose columns are cols
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def main():
    rng = random.Random(671)
    d_out, d_in, r = 12, 10, 2
    alpha = 16.0
    gamma = 16.0
    eta = alpha / math.sqrt(r)
    zeta = (alpha * alpha / (gamma * gamma)) * math.sqrt(d_out) / (r * r)

    # Construct exact SVD of gradient G = U S V^T
    U = random_orthogonal(d_out, rng)
    V = random_orthogonal(d_in, rng)
    sigmas = [10.0, 7.5, 5.0, 3.5, 1.2, 0.6, 0.3, 0.15, 0.08, 0.02]
    G = [[0.0 for _ in range(d_in)] for _ in range(d_out)]
    for idx, s in enumerate(sigmas):
        for i in range(d_out):
            for j in range(d_in):
                G[i][j] += s * U[i][idx] * V[j][idx]

    # Theorem 3.1: LoRA-GA uses disjoint index sets I_A = {0..r-1}, I_B = {r..2r-1}
    # A_init = (sqrt(zeta)/eta) * V[:, I_A]^T  (r x d_in)
    # B_init = (sqrt(zeta)/eta) * U[:, I_B]    (d_out x r)
    scale = math.sqrt(zeta) / eta
    A_ga = [[scale * V[j][k] for j in range(d_in)] for k in range(r)]
    B_ga = [[scale * U[i][r + k] for k in range(r)] for i in range(d_out)]

    # First-step effective gradient approximation:
    # W' = eta^2 * (G A^T A + B B^T G)
    AtA_ga = matmul(transpose(A_ga), A_ga)
    BBt_ga = matmul(B_ga, transpose(B_ga))
    approx_ga = mat_scale(mat_add(matmul(G, AtA_ga), matmul(BBt_ga, G)), eta * eta)

    # Exact rank-2r Eckart-Young optimal approximation to zeta * G:
    opt_2r = [[0.0 for _ in range(d_in)] for _ in range(d_out)]
    for idx in range(2 * r):
        s = sigmas[idx]
        for i in range(d_out):
            for j in range(d_in):
                opt_2r[i][j] += zeta * s * U[i][idx] * V[j][idx]

    ey_diff = math.sqrt(frob_sq(mat_sub(approx_ga, opt_2r)))
    assert ey_diff < 1e-12, f"Theorem 3.1 Eckart-Young rank-2r equivalence failed: {ey_diff}"

    target_zeta_G = mat_scale(G, zeta)
    err_ga = math.sqrt(frob_sq(mat_sub(approx_ga, target_zeta_G)))

    # Compare against overlapping index sets I_A = I_B = {0..r-1}
    B_overlap = [[scale * U[i][k] for k in range(r)] for i in range(d_out)]
    BBt_ov = matmul(B_overlap, transpose(B_overlap))
    approx_ov = mat_scale(mat_add(matmul(G, AtA_ga), matmul(BBt_ov, G)), eta * eta)
    err_ov = math.sqrt(frob_sq(mat_sub(approx_ov, target_zeta_G)))
    assert err_ga < err_ov, f"Disjoint rank-2r {err_ga} should beat overlapping rank-r {err_ov}"

    # Compare against vanilla LoRA (B_init = 0, A_init Kaiming uniform, rank-r update only)
    A_lora = [[scale * rng.uniform(-1.0, 1.0) for _ in range(d_in)] for _ in range(r)]
    AtA_lora = matmul(transpose(A_lora), A_lora)
    approx_lora = mat_scale(matmul(G, AtA_lora), eta * eta)
    err_lora = math.sqrt(frob_sq(mat_sub(approx_lora, target_zeta_G)))
    assert err_ga < err_lora, f"LoRA-GA {err_ga} should beat random Kaiming {err_lora}"

    # Verify weight invariance: W_init = W_0 - eta B_init A_init => W_init + eta B_init A_init == W_0
    W0 = [[rng.gauss(0.0, 1.0) for _ in range(d_in)] for _ in range(d_out)]
    BA_ga = matmul(B_ga, A_ga)
    W_init = mat_sub(W0, mat_scale(BA_ga, eta))
    W_reconstructed = mat_add(W_init, mat_scale(BA_ga, eta))
    inv_err = math.sqrt(frob_sq(mat_sub(W_reconstructed, W0)))
    assert inv_err < 1e-12, f"Weight invariance failed: {inv_err}"

    print(
        f"[PASS] Round 671 LoRA-GA (Wang et al., NeurIPS 2024): "
        f"ey_2r_diff={ey_diff:.2e}, err_ga={err_ga:.4f}<err_overlap={err_ov:.4f}<err_lora={err_lora:.4f}, "
        f"weight_inv_err={inv_err:.2e}"
    )


if __name__ == "__main__":
    main()
