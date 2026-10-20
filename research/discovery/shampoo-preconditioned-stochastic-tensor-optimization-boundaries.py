#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 588:
Shampoo (Preconditioned Stochastic Tensor Optimization) — Gupta, Koren, Singer (ICML 2018; arXiv:1802.09568).
"""

import math
import random
from typing import List, Tuple

Matrix = List[List[float]]


def zeros(m: int, n: int) -> Matrix:
    return [[0.0] * n for _ in range(m)]


def eye(n: int, scale: float = 1.0) -> Matrix:
    out = zeros(n, n)
    for i in range(n):
        out[i][i] = scale
    return out


def transpose(a: Matrix) -> Matrix:
    return [list(col) for col in zip(*a)]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    m, k, n = len(a), len(a[0]), len(b[0])
    out = zeros(m, n)
    for i in range(m):
        for p in range(k):
            aip = a[i][p]
            for j in range(n):
                out[i][j] += aip * b[p][j]
    return out


def matadd(a: Matrix, b: Matrix, scale_b: float = 1.0) -> Matrix:
    return [[a[i][j] + scale_b * b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def trace(a: Matrix) -> float:
    return sum(a[i][i] for i in range(len(a)))


def frob_norm(a: Matrix) -> float:
    return math.sqrt(sum(x * x for row in a for x in row))


def vec_row(a: Matrix) -> List[float]:
    """Row-major vectorization \\overline{vec}(A) used in Section 2.3."""
    return [x for row in a for x in row]


def kron(a: Matrix, b: Matrix) -> Matrix:
    m, n = len(a), len(a[0])
    p, q = len(b), len(b[0])
    out = zeros(m * p, n * q)
    for i in range(m):
        for j in range(n):
            aij = a[i][j]
            for r in range(p):
                for s in range(q):
                    out[i * p + r][j * q + s] = aij * b[r][s]
    return out


def jacobi_eigh(a: Matrix, tol: float = 1e-13, max_sweeps: int = 100) -> Tuple[List[float], Matrix]:
    """Symmetric eigenvalue decomposition A = V diag(w) V^T via Jacobi rotations."""
    n = len(a)
    d = [row[:] for row in a]
    v = eye(n)
    for _ in range(max_sweeps):
        max_off = 0.0
        p, q = 0, 1
        for i in range(n):
            for j in range(i + 1, n):
                if abs(d[i][j]) > max_off:
                    max_off = abs(d[i][j])
                    p, q = i, j
        if max_off < tol:
            break
        tau = (d[q][q] - d[p][p]) / (2.0 * d[p][q])
        t = (1.0 if tau >= 0 else -1.0) / (abs(tau) + math.sqrt(1.0 + tau * tau))
        c = 1.0 / math.sqrt(1.0 + t * t)
        s = t * c
        d_pp, d_qq, d_pq = d[p][p], d[q][q], d[p][q]
        d[p][p] = c * c * d_pp - 2.0 * s * c * d_pq + s * s * d_qq
        d[q][q] = s * s * d_pp + 2.0 * s * c * d_pq + c * c * d_qq
        d[p][q] = d[q][p] = 0.0
        for k in range(n):
            if k != p and k != q:
                dkp, dkq = d[k][p], d[k][q]
                d[k][p] = d[p][k] = c * dkp - s * dkq
                d[k][q] = d[q][k] = s * dkp + c * dkq
        for k in range(n):
            vkp, vkq = v[k][p], v[k][q]
            v[k][p] = c * vkp - s * vkq
            v[k][q] = s * vkp + c * vkq
    w = [d[i][i] for i in range(n)]
    return w, v


def psd_power(a: Matrix, alpha: float) -> Matrix:
    w, v = jacobi_eigh(a)
    n = len(a)
    scaled_vt = [[(max(w[i], 1e-15) ** alpha) * v[j][i] for j in range(n)] for i in range(n)]
    return matmul(v, scaled_vt)


def main() -> None:
    rng = random.Random(588)
    m, n = 3, 2
    mn = m * n
    eps = 0.1
    L = eye(m, eps)
    R = eye(n, eps)
    full_cov = eye(mn, eps)
    r = min(m, n)

    # 1. Verify Lemma 4, Lemma 8, Lemma 9, and Theorem 7 regret bound on online convex matrix task
    W_star = [[0.6, -0.4], [-0.3, 0.5], [0.2, -0.7]]
    W = zeros(m, n)
    eta = 0.25
    cum_regret = 0.0
    max_dist = frob_norm(matadd(W, W_star, -1.0))
    max_lemma4_err = 0.0

    T = 25
    for _ in range(T):
        # Generate random linear-quadratic convex loss f_t(W) = 0.5 * ||A_t (W - W*)||_F^2
        u = [rng.gauss(0.0, 1.0) for _ in range(m)]
        v = [rng.gauss(0.0, 1.0) for _ in range(n)]
        diff = matadd(W, W_star, -1.0)
        max_dist = max(max_dist, frob_norm(diff))
        dot_val = sum(u[i] * diff[i][j] * v[j] for i in range(m) for j in range(n))
        f_w = 0.5 * dot_val * dot_val
        f_star = 0.0
        cum_regret += f_w - f_star
        G = [[dot_val * u[i] * v[j] for j in range(n)] for i in range(m)]

        L = matadd(L, matmul(G, transpose(G)), 1.0)
        R = matadd(R, matmul(transpose(G), G), 1.0)
        g = vec_row(G)
        ggT = [[g[i] * g[j] for j in range(mn)] for i in range(mn)]
        full_cov = matadd(full_cov, ggT, 1.0 / r)

        L_m14 = psd_power(L, -0.25)
        R_m14 = psd_power(R, -0.25)
        step_mat = matmul(matmul(L_m14, G), R_m14)
        # Verify Lemma 4: vec(L^{-1/4} G R^{-1/4}) == (L^{-1/4} \otimes R^{-1/4}) vec(G)
        kron_m14 = kron(L_m14, R_m14)
        vec_lhs = vec_row(step_mat)
        vec_rhs = [sum(kron_m14[i][j] * g[j] for j in range(mn)) for i in range(mn)]
        lemma4_err = max(abs(vec_lhs[i] - vec_rhs[i]) for i in range(mn))
        max_lemma4_err = max(max_lemma4_err, lemma4_err)

        W = matadd(W, step_mat, -eta)

    assert max_lemma4_err < 1e-13, f"Lemma 4 identity error too high: {max_lemma4_err}"

    # Verify Lemma 8 PSD inequality: eps I_{mn} + (1/r) sum g_t g_t^T <= L_T^{1/2} \otimes R_T^{1/2}
    rhs_lemma8 = kron(psd_power(L, 0.5), psd_power(R, 0.5))
    slack_mat = matadd(rhs_lemma8, full_cov, -1.0)
    eigs_slack, _ = jacobi_eigh(slack_mat)
    min_eig_slack = min(eigs_slack)
    assert min_eig_slack >= -1e-10, f"Lemma 8 violated: min_eig={min_eig_slack}"

    # Verify Theorem 7 regret bound expression
    L_14 = psd_power(L, 0.25)
    R_14 = psd_power(R, 0.25)
    thm7_bound = math.sqrt(2.0 * r) * max_dist * trace(L_14) * trace(R_14)
    assert cum_regret <= thm7_bound, f"Theorem 7 regret bound violated: {cum_regret} > {thm7_bound}"

    # Verify memory complexity reduction m^2 + n^2 << m^2 n^2 for 1024x1024 layer
    m_big, n_big = 1024, 1024
    shampoo_space = m_big * m_big + n_big * n_big
    full_adagrad_space = (m_big * n_big) ** 2
    assert shampoo_space * 500_000 < full_adagrad_space

    print(
        f"[PASS] Round 588 Shampoo verified: lemma4_err={max_lemma4_err:.2e}, "
        f"lemma8_min_eig={min_eig_slack:.4e}>=0, regret={cum_regret:.4f}<={thm7_bound:.4f}"
    )


if __name__ == "__main__":
    main()
