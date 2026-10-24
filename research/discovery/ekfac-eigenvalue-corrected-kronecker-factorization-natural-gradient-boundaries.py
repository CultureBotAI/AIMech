#!/usr/bin/env python3
"""Constructed boundary verification for Round 637: EKFAC (George et al., NeurIPS 2018)."""

from __future__ import annotations
import math


def eig_2x2_sym(m: list[list[float]]) -> tuple[list[list[float]], list[float]]:
    """Exact analytical eigendecomposition of a 2x2 real symmetric matrix M = U diag(s) U^T."""
    a, b, d = m[0][0], m[0][1], m[1][1]
    if abs(b) < 1e-15:
        return [[1.0, 0.0], [0.0, 1.0]], [a, d]
    theta = 0.5 * math.atan2(2.0 * b, a - d)
    c, s = math.cos(theta), math.sin(theta)
    u = [[c, -s], [s, c]]
    lam1 = c * c * a + 2.0 * c * s * b + s * s * d
    lam2 = s * s * a - 2.0 * c * s * b + c * c * d
    return u, [lam1, lam2]


def kron_2x2(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    """Kronecker product A (x) B of two 2x2 matrices -> 4x4 matrix."""
    out = [[0.0] * 4 for _ in range(4)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    out[2 * i + k][2 * j + l] = a[i][j] * b[k][l]
    return out


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def transpose(a: list[list[float]]) -> list[list[float]]:
    n = len(a)
    return [[a[j][i] for j in range(n)] for i in range(n)]


def frob_diff(a: list[list[float]], b: list[list[float]]) -> float:
    n = len(a)
    return math.sqrt(sum((a[i][j] - b[i][j]) ** 2 for i in range(n) for j in range(n)))


def verify_ekfac_theorems_1_to_3_and_kronecker_vec() -> tuple[float, float, float, float]:
    """Verify Appendix A Lemma 1, Theorem 2, Theorem 3 (||G - G_EKFAC||_F < ||G - G_KFAC||_F), and Kronecker-vec identity."""
    # Construct 4 mini-batch samples of input activations h in R^2 and backprop gradients delta in R^2
    # where h and delta are statistically correlated across samples so E[(h h^T) (x) (delta delta^T)] != E[h h^T] (x) E[delta delta^T]
    h_samples = [
        [2.0, 0.5],
        [0.4, 1.8],
        [-1.5, 1.2],
        [1.1, -1.6],
    ]
    delta_samples = [
        [1.7, -0.3],
        [0.2, 2.1],
        [-1.4, -0.8],
        [0.9, -1.9],
    ]
    n_samples = len(h_samples)

    # Exact empirical Fisher G = E[g g^T] in R^{4x4}, where g = vec_row(h delta^T) = h (x) delta
    grads = []
    for s in range(n_samples):
        h = h_samples[s]
        d = delta_samples[s]
        g = [h[0] * d[0], h[0] * d[1], h[1] * d[0], h[1] * d[1]]
        grads.append(g)

    g_fisher = [
        [sum(grads[s][i] * grads[s][j] for s in range(n_samples)) / n_samples for j in range(4)]
        for i in range(4)
    ]

    # KFAC factors A = E[h h^T] and B = E[delta delta^T]
    a_mat = [
        [sum(h_samples[s][i] * h_samples[s][j] for s in range(n_samples)) / n_samples for j in range(2)]
        for i in range(2)
    ]
    b_mat = [
        [sum(delta_samples[s][i] * delta_samples[s][j] for s in range(n_samples)) / n_samples for j in range(2)]
        for i in range(2)
    ]
    g_kfac = kron_2x2(a_mat, b_mat)

    # Eigendecomposition of A and B -> KFE basis Q = U_A (x) U_B
    u_a, s_a = eig_2x2_sym(a_mat)
    u_b, s_b = eig_2x2_sym(b_mat)
    q_kfe = kron_2x2(u_a, u_b)
    qt_kfe = transpose(q_kfe)

    # Check Q is orthogonal: Q^T Q == I_4
    qtq = matmul(qt_kfe, q_kfe)
    ortho_err = max(abs(qtq[i][j] - (1.0 if i == j else 0.0)) for i in range(4) for j in range(4))
    assert ortho_err < 1e-14, f"KFE basis must be orthogonal: {ortho_err}"

    # EKFAC optimal diagonal scaling s*_i = E[((U_A (x) U_B)^T g)_i^2] = (Q^T G Q)_{ii}
    qt_g_q = matmul(matmul(qt_kfe, g_fisher), q_kfe)
    s_star = [
        sum(
            sum(q_kfe[k][i] * grads[s][k] for k in range(4)) ** 2
            for s in range(n_samples)
        )
        / n_samples
        for i in range(4)
    ]
    # Verify Lemma 1 identity: s*_i == (Q^T G Q)_{ii}
    lemma1_id_err = max(abs(s_star[i] - qt_g_q[i][i]) for i in range(4))
    assert lemma1_id_err < 1e-14

    d_star = [[s_star[i] if i == j else 0.0 for j in range(4)] for i in range(4)]
    g_ekfac = matmul(matmul(q_kfe, d_star), qt_kfe)

    err_ekfac = frob_diff(g_fisher, g_ekfac)
    err_kfac = frob_diff(g_fisher, g_kfac)
    # Theorem 3: ||G - G_EKFAC||_F <= ||G - G_KFAC||_F (strictly smaller when h, delta are correlated)
    assert err_ekfac < err_kfac - 1e-4, f"EKFAC error {err_ekfac} must be strictly less than KFAC {err_kfac}"

    # Verify Theorem 2 optimality: any perturbation delta_d to D* strictly increases Frobenius error
    d_pert = [[(s_star[i] + (0.25 if i % 2 == 0 else -0.2)) if i == j else 0.0 for j in range(4)] for i in range(4)]
    g_pert = matmul(matmul(q_kfe, d_pert), qt_kfe)
    err_pert = frob_diff(g_fisher, g_pert)
    assert err_ekfac < err_pert - 1e-4

    # Verify Algorithm 1 footnote 1 identity: (U_A (x) U_B)^T vec_col(C) = vec_col(U_B^T C U_A)
    # Using row-major vec_row(C) where C = h delta^T: (U_A (x) U_B)^T vec_row(C) = vec_row(U_A^T C U_B)
    c_mat = [[h_samples[0][i] * delta_samples[0][j] for j in range(2)] for i in range(2)]
    vec_proj_direct = [sum(q_kfe[k][i] * grads[0][k] for k in range(4)) for i in range(4)]
    uat_c_ub = matmul(matmul(transpose(u_a), c_mat), u_b)
    vec_proj_fast = [uat_c_ub[0][0], uat_c_ub[0][1], uat_c_ub[1][0], uat_c_ub[1][1]]
    kron_vec_err = max(abs(vec_proj_direct[i] - vec_proj_fast[i]) for i in range(4))
    assert kron_vec_err < 1e-14

    return err_ekfac, err_kfac, lemma1_id_err, kron_vec_err


if __name__ == "__main__":
    e_ekfac, e_kfac, l1_err, kv_err = verify_ekfac_theorems_1_to_3_and_kronecker_vec()
    print(
        f"[PASS] Round 637 EKFAC verified: ||G-G_EKFAC||_F={e_ekfac:.4f} < ||G-G_KFAC||_F={e_kfac:.4f}, "
        f"lemma1_err={l1_err:.2e}, kron_vec_err={kv_err:.2e}"
    )
