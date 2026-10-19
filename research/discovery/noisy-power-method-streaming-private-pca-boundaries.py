#!/usr/bin/env python3
"""Constructed boundary verification for Round 356:
The Noisy Power Method: A Meta Algorithm with Applications (Hardt & Price 2014).

Verifies:
1. Lemma 2.3 & Theorem 2.4 (Principal-Angle Tangent Contraction): Under noise G_ell satisfying
   4 ||U^T G_ell|| <= (sigma_k - sigma_{k+1}) cos theta_k(U, X) and 4 ||G_ell|| <= (sigma_k - sigma_{k+1}) eps,
   each Noisy Power Method step Y_ell = A X_{ell-1} + G_ell, Y_ell = X_ell R_ell contracts
   tan theta_k(U, X_ell) <= max(eps, max(eps, (sigma_{k+1}/sigma_k)^{1/4}) tan theta_k(U, X_{ell-1})).
2. Lemma 4.11 & Lemma 4.12 (Gram-Schmidt Orthogonal Commutativity): For any orthogonal matrix O
   commuting with A (sharing A's eigenbasis), GS(O V) == O GS(V) and PPM iterates satisfy
   f(O G_0, ..., O G_L) == O f(G_0, ..., G_L), preserving low infinity-norm coherence (Theorem 4.9).
"""

import math
import random


def gram_schmidt(cols: list[list[float]]) -> list[list[float]]:
    d = len(cols[0])
    basis: list[list[float]] = []
    for v in cols:
        w = list(v)
        for q in basis:
            r_ij = sum(q[i] * w[i] for i in range(d))
            for i in range(d):
                w[i] -= r_ij * q[i]
        r_ii = math.sqrt(sum(x * x for x in w))
        basis.append([x / r_ii for x in w])
    return basis


def mat_vec_cols(M: list[list[float]], cols: list[list[float]]) -> list[list[float]]:
    d = len(M)
    out: list[list[float]] = []
    for c in cols:
        out.append([sum(M[i][j] * c[j] for j in range(d)) for i in range(d)])
    return out


def principal_angle_tan_k1(u: list[float], X_cols: list[list[float]]) -> tuple[float, float]:
    # For k=1 and orthonormal columns X_cols in R^{d x p}, cos theta_1(u, X) = ||X^T u||_2
    cos_sq = sum(sum(u[i] * col[i] for i in range(len(u))) ** 2 for col in X_cols)
    cos_val = min(1.0, math.sqrt(max(0.0, cos_sq)))
    sin_val = math.sqrt(max(0.0, 1.0 - cos_val * cos_val))
    tan_val = sin_val / max(cos_val, 1e-15)
    return tan_val, cos_val


def main() -> None:
    rng = random.Random(356)
    d = 8
    k = 1
    p = 2
    # Symmetric diagonal A with sigma_1 = 2.0, sigma_2 = 0.5, ..., sigma_8 = 0.1
    sigmas = [2.0, 0.5, 0.4, 0.3, 0.25, 0.2, 0.15, 0.1]
    A = [[sigmas[i] if i == j else 0.0 for j in range(d)] for i in range(d)]
    u1 = [1.0 if i == 0 else 0.0 for i in range(d)]
    gap = sigmas[0] - sigmas[1]  # 1.5
    eps = 0.08
    contraction_factor = (sigmas[1] / sigmas[0]) ** 0.25  # (0.25)^{0.25} = 0.70710678

    # Initialize X_0 as QR of Gaussian d x p matrix
    G0_cols = [[rng.gauss(0.0, 1.0) for _ in range(d)] for _ in range(p)]
    X_cols = gram_schmidt(G0_cols)
    tan_0, _ = principal_angle_tan_k1(u1, X_cols)

    # 1. Verify Lemma 2.3 and Theorem 2.4 over L = 12 Noisy Power Method steps
    L = 12
    noise_history: list[list[list[float]]] = []
    tan_prev = tan_0
    for _ in range(L):
        _, cos_curr = principal_angle_tan_k1(u1, X_cols)
        # Construct noise G_ell satisfying Lemma 2.3 conditions:
        # 4 ||U^T G_ell|| <= gap * cos_curr and 4 ||G_ell|| <= gap * eps
        raw_G = [[rng.gauss(0.0, 1.0) for _ in range(d)] for _ in range(p)]
        frob_G = math.sqrt(sum(x * x for col in raw_G for x in col))
        scale = min(0.20 * gap * eps, 0.20 * gap * cos_curr) / max(frob_G, 1e-12)
        G_cols = [[scale * x for x in col] for col in raw_G]
        noise_history.append(G_cols)

        AX_cols = mat_vec_cols(A, X_cols)
        Y_cols = [[AX_cols[c][i] + G_cols[c][i] for i in range(d)] for c in range(p)]
        X_cols = gram_schmidt(Y_cols)
        tan_new, _ = principal_angle_tan_k1(u1, X_cols)
        lemma23_rhs = max(eps, max(eps, contraction_factor) * tan_prev)
        assert tan_new <= lemma23_rhs + 1e-12, f"Lemma 2.3 violated: {tan_new} > {lemma23_rhs}"
        tan_prev = tan_new

    assert tan_prev <= eps, f"Theorem 2.4 target not reached: tan_L={tan_prev} > eps={eps}"

    # 2. Verify Lemma 4.11 & Lemma 4.12 (Gram-Schmidt & PPM commute with sign-flip O in A's eigenbasis)
    signs = [1.0 if rng.random() < 0.5 else -1.0 for _ in range(d)]
    O_mat = [[signs[i] if i == j else 0.0 for j in range(d)] for i in range(d)]

    # Check GS(O G_0) == O GS(G_0)
    lhs_0 = gram_schmidt(mat_vec_cols(O_mat, G0_cols))
    rhs_0 = mat_vec_cols(O_mat, gram_schmidt(G0_cols))
    max_comm_err = max(abs(lhs_0[c][i] - rhs_0[c][i]) for c in range(p) for i in range(d))
    assert max_comm_err < 1e-12

    # Run full NPM with transformed noise O G_0, O G_1, ..., O G_L
    X_trans = gram_schmidt(mat_vec_cols(O_mat, G0_cols))
    for G_cols in noise_history:
        OG_cols = mat_vec_cols(O_mat, G_cols)
        AX_t = mat_vec_cols(A, X_trans)
        Y_t = [[AX_t[c][i] + OG_cols[c][i] for i in range(d)] for c in range(p)]
        X_trans = gram_schmidt(Y_t)

    OX_final = mat_vec_cols(O_mat, X_cols)
    lemma412_err = max(abs(X_trans[c][i] - OX_final[c][i]) for c in range(p) for i in range(d))
    assert lemma412_err < 1e-11, f"Lemma 4.12 violated: {lemma412_err}"

    print(
        f"[PASS] Round 356 Noisy Power Method (Hardt & Price 2014): "
        f"tan_0={tan_0:.4f}->tan_L={tan_prev:.5f}<=eps={eps:.3f}, "
        f"gs_comm_err={max_comm_err:.2e}, lemma412_err={lemma412_err:.2e}"
    )


if __name__ == "__main__":
    main()
