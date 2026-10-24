#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 648:
TONGA (Topmoumoute Online Natural Gradient Algorithm)
Primary source: Le Roux, Manzagol, & Bengio (NeurIPS 2007).
"""

import math


def mat_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def mat_vec(A, x):
    return [sum(row[j] * x[j] for j in range(len(x))) for row in A]


def transpose(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def mat_inv(A):
    n = len(A)
    M = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(A)]
    for i in range(n):
        piv = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[piv] = M[piv], M[i]
        div = M[i][i]
        M[i] = [v / div for v in M[i]]
        for r in range(n):
            if r != i:
                f = M[r][i]
                M[r] = [M[r][c] - f * M[i][c] for c in range(2 * n)]
    return [row[n:] for row in M]


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def verify_uncentered_covariance_collinearity_eq_8():
    """Verify Eq. (8): If C v = g for centered covariance C, then (C + g g^T)^{-1} g = v / (1 + g^T v),
    so using the uncentered second moment preserves the exact natural gradient direction while
    bounding the step norm by 1 / (||g|| cos(g, v))."""
    C = [
        [2.5, 0.4, -0.2, 0.1],
        [0.4, 1.8, 0.3, -0.1],
        [-0.2, 0.3, 1.5, 0.2],
        [0.1, -0.1, 0.2, 1.2],
    ]
    g = [0.7, -0.5, 0.4, 0.3]
    C_inv = mat_inv(C)
    v = mat_vec(C_inv, g)

    C_uncentered = [[C[i][j] + g[i] * g[j] for j in range(4)] for i in range(4)]
    v_bar_direct = mat_vec(mat_inv(C_uncentered), g)
    scale = 1.0 + dot(g, v)
    v_bar_formula = [vi / scale for vi in v]

    for a, b in zip(v_bar_direct, v_bar_formula):
        assert abs(a - b) < 1e-12

    # Check norm bound <= 1 / (||g|| cos(g, v)) = ||v|| / (g^T v)
    norm_v_bar = math.sqrt(dot(v_bar_direct, v_bar_direct))
    norm_v = math.sqrt(dot(v, v))
    bound = norm_v / dot(g, v)
    assert norm_v_bar < bound


def verify_woodbury_gram_natural_gradient_eqs_10_13():
    """Verify Eqs. (10)-(13): Given rank-r factor X_t = [sqrt(gamma) X_{t-1}, g_t] in R^{p x r}
    with C_t = X_t X_t^T, the regularized natural direction v_t = (X_t X_t^T + lambda I_p)^{-1} g_t
    equals X_t (G_t + lambda I_r)^{-1} e_r where G_t = X_t^T X_t is updated incrementally via Eq. (13)."""
    p = 7
    gamma = 0.95
    lam = 0.15
    grads = [
        [0.4, -0.2, 0.1, 0.5, -0.3, 0.2, 0.6],
        [-0.1, 0.5, 0.3, -0.4, 0.2, 0.1, -0.2],
        [0.3, 0.2, -0.5, 0.1, 0.4, -0.3, 0.2],
    ]
    # Build X_t in R^{p x r} column by column and update Gram matrix G_t incrementally via Eq. (13)
    X_cols = []
    G = []
    for gt in grads:
        if not X_cols:
            X_cols = [gt[:]]
            G = [[dot(gt, gt)]]
        else:
            # Cross inner products sqrt(gamma) X_{t-1}^T g_t
            cross = [math.sqrt(gamma) * dot(col, gt) for col in X_cols]
            r_prev = len(G)
            G_new = [[0.0] * (r_prev + 1) for _ in range(r_prev + 1)]
            for i in range(r_prev):
                for j in range(r_prev):
                    G_new[i][j] = gamma * G[i][j]
                G_new[i][r_prev] = cross[i]
                G_new[r_prev][i] = cross[i]
            G_new[r_prev][r_prev] = dot(gt, gt)
            G = G_new
            X_cols = [[math.sqrt(gamma) * x for x in col] for col in X_cols] + [gt[:]]

    r = len(X_cols)
    X_t = transpose(X_cols)  # p x r
    # Verify incremental Gram matrix matches X_t^T X_t
    G_exact = mat_mul(transpose(X_t), X_t)
    for i in range(r):
        for j in range(r):
            assert abs(G[i][j] - G_exact[i][j]) < 1e-12

    # Full p x p regularized natural gradient: (X_t X_t^T + lam I_p)^{-1} g_t
    C_t = mat_mul(X_t, transpose(X_t))
    C_reg = [[C_t[i][j] + (lam if i == j else 0.0) for j in range(p)] for i in range(p)]
    v_full = mat_vec(mat_inv(C_reg), grads[-1])

    # Woodbury r x r Gram formula Eq. (12): X_t (G_t + lam I_r)^{-1} y_t with y_t = [0,...,0,1]^T
    G_reg = [[G[i][j] + (lam if i == j else 0.0) for j in range(r)] for i in range(r)]
    y_t = [0.0] * (r - 1) + [1.0]
    w_r = mat_vec(mat_inv(G_reg), y_t)
    v_woodbury = mat_vec(X_t, w_r)

    for a, b in zip(v_full, v_woodbury):
        assert abs(a - b) < 1e-12


def verify_generalization_decrease_probability_section_2():
    """Verify Section 2.1/2.2 (Eqs. 5-7): Maximizing (g_tilde^T M g_tilde) / sqrt(g_tilde^T M^T C_tilde M g_tilde)
    by Cauchy-Schwarz achieves its global maximum when C_tilde^{1/2} M g_tilde is proportional to C_tilde^{-1/2} g_tilde,
    i.e., M proportional to C_tilde^{-1}."""
    C_tilde = [[2.0, 0.5, -0.3], [0.5, 1.5, 0.2], [-0.3, 0.2, 1.2]]
    g_tilde = [0.8, -0.4, 0.6]
    C_inv = mat_inv(C_tilde)
    v_nat = mat_vec(C_inv, g_tilde)

    def snr(v):
        num = dot(v, g_tilde)
        denom = math.sqrt(dot(v, mat_vec(C_tilde, v)))
        return num / denom

    snr_nat = snr(v_nat)
    # Compare with Euclidean gradient and perturbed directions
    for cand in [g_tilde, [1.0, -0.2, 0.5], [0.5, -0.8, 0.3]]:
        assert snr_nat >= snr(cand) - 1e-12


if __name__ == "__main__":
    verify_uncentered_covariance_collinearity_eq_8()
    verify_woodbury_gram_natural_gradient_eqs_10_13()
    verify_generalization_decrease_probability_section_2()
    print("[PASS] Round 648 TONGA boundary and mathematical verification succeeded.")
