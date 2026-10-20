#!/usr/bin/env python3
"""Boundary verification for Round 644: K-BFGS and K-BFGS(L) (Goldfarb, Ren, & Bahamou, NeurIPS 2020 / arXiv:2006.08877)."""

from __future__ import annotations

import math
import random


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    m, k, n = len(a), len(a[0]), len(b[0])
    out = [[0.0] * n for _ in range(m)]
    for i in range(m):
        for p in range(k):
            aip = a[i][p]
            for j in range(n):
                out[i][j] += aip * b[p][j]
    return out


def matvec(a: list[list[float]], x: list[float]) -> list[float]:
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def dot(x: list[float], y: list[float]) -> float:
    return sum(xi * yi for xi, yi in zip(x, y))


def outer(x: list[float], y: list[float]) -> list[list[float]]:
    return [[xi * yj for yj in y] for xi in x]


def invert_spd(a: list[list[float]]) -> list[list[float]]:
    n = len(a)
    aug = [a[i][:] + [1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(aug[r][col]))
        aug[col], aug[piv] = aug[piv], aug[col]
        div = aug[col][col]
        for j in range(2 * n):
            aug[col][j] /= div
        for r in range(n):
            if r != col:
                fac = aug[r][col]
                for j in range(2 * n):
                    aug[r][j] -= fac * aug[col][j]
    return [row[n:] for row in aug]


def broyden_update(h: list[list[float]], s: list[float], y: list[float], phi: float) -> list[list[float]]:
    """Equation (11): Broyden family inverse update for phi in [0, 1] (phi=1 is BFGS, phi=0 is DFP)."""
    n = len(h)
    sy = dot(s, y)
    hy = matvec(h, y)
    yhy = dot(y, hy)
    rho = 1.0 / sy
    sigma = 1.0 / yhy
    h_vec = [rho * s[i] - sigma * hy[i] for i in range(n)]
    hy_hy = outer(hy, hy)
    s_s = outer(s, s)
    hh_t = outer(h_vec, h_vec)
    out = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            out[i][j] = h[i][j] - sigma * hy_hy[i][j] + rho * s_s[i][j] + phi * yhy * hh_t[i][j]
    return out


def double_damping(
    s: list[float], y: list[float], h: list[list[float]], mu1: float, mu2: float
) -> tuple[list[float], list[float]]:
    """Algorithm 3 (page 5): Double Damping (DD) of (s, y) pair."""
    n = len(s)
    sy = dot(s, y)
    hy = matvec(h, y)
    yhy = dot(y, hy)
    if sy < mu1 * yhy:
        theta1 = (1.0 - mu1) * yhy / (yhy - sy)
    else:
        theta1 = 1.0
    s_tilde = [theta1 * s[i] + (1.0 - theta1) * hy[i] for i in range(n)]
    st_y = dot(s_tilde, y)
    st_st = dot(s_tilde, s_tilde)
    if st_y < mu2 * st_st:
        theta2 = (1.0 - mu2) * st_st / (st_st - st_y)
    else:
        theta2 = 1.0
    y_tilde = [theta2 * y[i] + (1.0 - theta2) * s_tilde[i] for i in range(n)]
    return s_tilde, y_tilde


def main() -> None:
    rng = random.Random(644)

    # 1. Verify Theorem 1 (Section 4, Equation 11, page 5):
    # Hessian-action BFGS for A^+ = A + c * a * a^T with s = H * a, y = A^+ * s equals exact (A^+)^{-1}
    # for every phi in [0, 1] in the Broyden family.
    d = 5
    a_mat = [
        [2.5, 0.4, -0.2, 0.1, 0.3],
        [0.4, 1.8, 0.3, -0.1, 0.2],
        [-0.2, 0.3, 2.1, 0.5, -0.2],
        [0.1, -0.1, 0.5, 1.6, 0.3],
        [0.3, 0.2, -0.2, 0.3, 1.9],
    ]
    h_mat = invert_spd(a_mat)
    a_vec = [rng.gauss(0.0, 1.0) for _ in range(d)]
    c_val = 0.75
    aa_t = outer(a_vec, a_vec)
    a_plus = [[a_mat[i][j] + c_val * aa_t[i][j] for j in range(d)] for i in range(d)]
    a_plus_inv_exact = invert_spd(a_plus)

    s_ha = matvec(h_mat, a_vec)
    y_ha = matvec(a_plus, s_ha)

    for phi in [0.0, 0.5, 1.0]:
        h_plus = broyden_update(h_mat, s_ha, y_ha, phi)
        max_diff = max(abs(h_plus[i][j] - a_plus_inv_exact[i][j]) for i in range(d) for j in range(d))
        assert max_diff < 1e-12, f"Theorem 1 failed for phi={phi}: max_diff={max_diff:.2e}"

    # 2. Verify Algorithm 3 Double Damping (Section 3, Equations 6-10, pages 4-5):
    # Test on a non-convex indefinite secant pair with s^T y < 0
    mu1, mu2 = 0.2, 0.3
    s_raw = [1.2, -0.8, 0.5, -1.1, 0.7]
    y_raw = [-0.9, 0.6, -0.4, 0.9, -0.5]  # s_raw^T y_raw < 0!
    assert dot(s_raw, y_raw) < 0.0

    s_tilde, y_tilde = double_damping(s_raw, y_raw, h_mat, mu1, mu2)
    hy_raw = matvec(h_mat, y_raw)
    # Step 1 guarantees s_tilde^T y >= mu1 * y^T H y
    assert dot(s_tilde, y_raw) >= mu1 * dot(y_raw, hy_raw) - 1e-12
    # Step 2 guarantees s_tilde^T y_tilde >= mu2 * ||s_tilde||^2 > 0
    st_yt = dot(s_tilde, y_tilde)
    st_st = dot(s_tilde, s_tilde)
    assert st_yt >= mu2 * st_st - 1e-12 and st_yt > 0.0

    # Verify that BFGS update H^+ with (s_tilde, y_tilde) remains strictly positive definite
    h_bfgs_dd = broyden_update(h_mat, s_tilde, y_tilde, phi=1.0)
    for _ in range(40):
        v = [rng.gauss(0.0, 1.0) for _ in range(d)]
        quad = dot(v, matvec(h_bfgs_dd, v))
        assert quad > 0.0, "BFGS update after Double Damping must remain positive definite"

    # 3. Verify Kronecker-Factored Quasi-Newton Step Identity (Section 2 Eq. 4, page 3):
    # vec(H_g * G * H_a) == (H_a (x) H_g) vec(G)
    di, do = 4, 3
    h_a = [[1.5 if i == j else 0.2 for j in range(di)] for i in range(di)]
    h_g = [[1.8 if i == j else -0.15 for j in range(do)] for i in range(do)]
    grad_w = [[rng.gauss(0.0, 1.0) for _ in range(di)] for _ in range(do)]
    step_mat = matmul(matmul(h_g, grad_w), h_a)
    # Compare against explicit Kronecker product (H_a (x) H_g) on column-major vec(grad_w)
    vec_g = [grad_w[r][c] for c in range(di) for r in range(do)]
    vec_step = [step_mat[r][c] for c in range(di) for r in range(do)]
    kron_step = [0.0] * (di * do)
    for c1 in range(di):
        for r1 in range(do):
            idx1 = c1 * do + r1
            for c2 in range(di):
                for r2 in range(do):
                    idx2 = c2 * do + r2
                    kron_step[idx1] += h_a[c1][c2] * h_g[r1][r2] * vec_g[idx2]
    kron_err = max(abs(vec_step[k] - kron_step[k]) for k in range(di * do))
    assert kron_err < 1e-12

    print(
        f"[PASS] Round 644 K-BFGS verified: thm1_diff={max_diff:.2e}, s_raw^T y_raw={dot(s_raw, y_raw):.3f}->st^T yt={st_yt:.4f}>=mu2*||st||^2={mu2*st_st:.4f}, kron_err={kron_err:.2e}"
    )


if __name__ == "__main__":
    main()
