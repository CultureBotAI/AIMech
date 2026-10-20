#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 675: MiLoRA (Wang et al., NAACL 2025)."""

import math
import random


def matmul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)] for i in range(m)]


def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def frob_norm(A):
    return math.sqrt(sum(x * x for row in A for x in row))


def mat_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mat_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def random_orthogonal(n, rng):
    cols = []
    for _ in range(n):
        v = [rng.gauss(0.0, 1.0) for _ in range(n)]
        for u in cols:
            dot = sum(v[i] * u[i] for i in range(n))
            v = [v[i] - dot * u[i] for i in range(n)]
        norm = math.sqrt(sum(x * x for x in v))
        cols.append([x / norm for x in v])
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def main():
    rng = random.Random(675)
    m, n, r = 8, 8, 2
    U = random_orthogonal(m, rng)
    V = random_orthogonal(n, rng)
    # Descending singular values: top (m-r) are principal, bottom r are minor
    sigmas = [12.0, 9.0, 6.5, 4.5, 3.0, 2.0, 0.25, 0.10]

    W = [[0.0 for _ in range(n)] for _ in range(m)]
    Wp = [[0.0 for _ in range(n)] for _ in range(m)]
    for idx, s in enumerate(sigmas):
        for i in range(m):
            for j in range(n):
                val = s * U[i][idx] * V[j][idx]
                W[i][j] += val
                if idx < m - r:
                    Wp[i][j] += val

    # Eq. (5): Bm = Um sqrt(Sigma_m), Am = sqrt(Sigma_m) Vm^T
    Bm_init = [
        [U[i][m - r + k] * math.sqrt(sigmas[m - r + k]) for k in range(r)]
        for i in range(m)
    ]
    Am_init = [
        [math.sqrt(sigmas[m - r + k]) * V[j][m - r + k] for j in range(n)]
        for k in range(r)
    ]
    Wm_init = matmul(Bm_init, Am_init)

    # 1. Verify exact initial weight preservation W == Wp + Bm_init @ Am_init (Eq. 3-5)
    recon_err = frob_norm(mat_sub(W, mat_add(Wp, Wm_init)))
    assert recon_err < 1e-13, f"Initial MiLoRA reconstruction failed: {recon_err}"

    # 2. Verify strict initial orthogonality to principal singular subspace (Up, Vp)
    Up = [[U[i][k] for k in range(m - r)] for i in range(m)]
    Vp = [[V[j][k] for k in range(m - r)] for j in range(n)]
    orth_left = frob_norm(matmul(transpose(Up), Bm_init))
    orth_right = frob_norm(matmul(Am_init, Vp))
    assert orth_left < 1e-13 and orth_right < 1e-13, f"Orthogonality failed: {orth_left}, {orth_right}"

    # 3. Compare forgetting of principal knowledge between MiLoRA (adapts minor modes)
    # and PiSSA (adapts principal top-r modes):
    # Suppose a downstream task induces a rank-r update in the minor subspace while
    # pre-trained world knowledge lives in the top-r principal modes.
    # Under PiSSA initialization (top-r modes trainable, gradient step perturbs top-r singular directions),
    # principal subspace distortion ||Up_top^T dW Vp_top||_F is large; under MiLoRA (initialized in minor subspace,
    # gradient step on a task aligned with minor+orthogonal directions), principal distortion is minimal.
    Up_top = [[U[i][k] for k in range(r)] for i in range(m)]
    Vp_top = [[V[j][k] for k in range(r)] for j in range(n)]

    # Simulate 1 gradient step on loss L(W') = 0.5 * ||(W' - W_target) P_minor||_F^2 + Perturbation
    # where task signal lies predominantly in minor subspace plus small isotropic noise
    G = [[0.0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            # Strong signal in minor modes + small cross-talk in principal modes
            G[i][j] = (
                2.0 * U[i][m - 1] * V[j][m - 1]
                + 1.5 * U[i][m - 2] * V[j][m - 2]
                + 0.3 * U[i][0] * V[j][0]
                + 0.3 * U[i][1] * V[j][1]
            )

    lr = 0.2
    # First-order update in MiLoRA: dB_m = -lr * G @ Am^T, dA_m = -lr * Bm^T @ G
    dBm = matmul(G, transpose(Am_init))
    dAm = matmul(transpose(Bm_init), G)
    Bm_new = [[Bm_init[i][k] - lr * dBm[i][k] for k in range(r)] for i in range(m)]
    Am_new = [[Am_init[k][j] - lr * dAm[k][j] for j in range(n)] for k in range(r)]
    dW_milora = mat_sub(matmul(Bm_new, Am_new), Wm_init)

    # First-order update in PiSSA (initialized with top-r principal modes):
    Bp_init = [[U[i][k] * math.sqrt(sigmas[k]) for k in range(r)] for i in range(m)]
    Ap_init = [[math.sqrt(sigmas[k]) * V[j][k] for j in range(n)] for k in range(r)]
    Wp_top_init = matmul(Bp_init, Ap_init)
    dBp = matmul(G, transpose(Ap_init))
    dAp = matmul(transpose(Bp_init), G)
    Bp_new = [[Bp_init[i][k] - lr * dBp[i][k] for k in range(r)] for i in range(m)]
    Ap_new = [[Ap_init[k][j] - lr * dAp[k][j] for j in range(n)] for k in range(r)]
    dW_pissa = mat_sub(matmul(Bp_new, Ap_new), Wp_top_init)

    # Principal top-r subspace distortion ||Up_top^T dW Vp_top||_F (forgetting proxy, Table 7 & 8):
    forgetting_milora = frob_norm(matmul(matmul(transpose(Up_top), dW_milora), Vp_top))
    forgetting_pissa = frob_norm(matmul(matmul(transpose(Up_top), dW_pissa), Vp_top))
    assert forgetting_milora < 0.05 * forgetting_pissa, (
        f"MiLoRA principal distortion {forgetting_milora} should be much smaller than PiSSA {forgetting_pissa}"
    )

    print(
        f"[PASS] Round 675 MiLoRA (Wang et al., NAACL 2025): "
        f"recon_err={recon_err:.2e}, orth_err={max(orth_left, orth_right):.2e}, "
        f"forgetting_milora={forgetting_milora:.4e}<<forgetting_pissa={forgetting_pissa:.4f}"
    )


if __name__ == "__main__":
    main()
