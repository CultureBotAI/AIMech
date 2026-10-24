#!/usr/bin/env python3
"""Constructed boundary verification for Round 355:
Randomized Block Krylov Methods for Stronger and Faster Approximate SVD (Musco & Musco 2015).

Verifies:
1. Lemma 5 (Chebyshev Minimizing Polynomial): p(x) = (1+gamma)*alpha * T_q(x/alpha) / T_q(1+gamma)
   satisfies p((1+gamma)*alpha) == (1+gamma)*alpha, p(x) >= x for x >= (1+gamma)*alpha,
   |p(x)| <= alpha / 2^{q*sqrt(gamma) - 1} for x in [0, alpha], and odd-power structure for odd q.
2. Algorithm 2 (Block Krylov Iteration) vs Algorithm 1 (Simultaneous Iteration) on a constructed
   matrix with a small singular value gap (sigma_1=1.08, sigma_2=1.04, sigma_3=1.00, heavy tail):
   Block Krylov achieves smaller spectral norm error ||A - Z Z^T A||_2, Frobenius norm error
   ||A - Z Z^T A||_F, and per-vector PCA variance error max_{i<=k} |u_i^T A A^T u_i - z_i^T A A^T z_i|
   at the same iteration count q.
"""

import math
import random


def chebyshev_T(q: int, x: float) -> float:
    if q == 0:
        return 1.0
    if q == 1:
        return x
    t0, t1 = 1.0, x
    for _ in range(2, q + 1):
        t0, t1 = t1, 2.0 * x * t1 - t0
    return t1


def chebyshev_min_poly(q: int, alpha: float, gamma: float, x: float) -> float:
    return (1.0 + gamma) * alpha * chebyshev_T(q, x / alpha) / chebyshev_T(q, 1.0 + gamma)


def gram_schmidt(cols: list[list[float]]) -> list[list[float]]:
    basis: list[list[float]] = []
    for v in cols:
        w = list(v)
        for u in basis:
            proj = sum(w[i] * u[i] for i in range(len(w)))
            for i in range(len(w)):
                w[i] -= proj * u[i]
        norm = math.sqrt(sum(x * x for x in w))
        if norm > 1e-12:
            basis.append([x / norm for x in w])
    return basis


def jacobi_sym_eig(M: list[list[float]]) -> tuple[list[float], list[list[float]]]:
    m = len(M)
    A = [row[:] for row in M]
    V = [[1.0 if i == j else 0.0 for j in range(m)] for i in range(m)]
    for _ in range(80):
        max_val = 0.0
        p, q = 0, 1
        for i in range(m):
            for j in range(i + 1, m):
                if abs(A[i][j]) > max_val:
                    max_val = abs(A[i][j])
                    p, q = i, j
        if max_val < 1e-14:
            break
        diff = A[q][q] - A[p][p]
        if abs(diff) < 1e-15:
            theta = math.pi / 4.0
        else:
            theta = 0.5 * math.atan2(2.0 * A[p][q], diff)
        c, s = math.cos(theta), math.sin(theta)
        for i in range(m):
            if i != p and i != q:
                aip, aiq = A[i][p], A[i][q]
                A[i][p] = A[p][i] = c * aip - s * aiq
                A[i][q] = A[q][i] = s * aip + c * aiq
        app, aqq, apq = A[p][p], A[q][q], A[p][q]
        A[p][p] = c * c * app - 2.0 * s * c * apq + s * s * aqq
        A[q][q] = s * s * app + 2.0 * s * c * apq + c * c * aqq
        A[p][q] = A[q][p] = 0.0
        for i in range(m):
            vip, viq = V[i][p], V[i][q]
            V[i][p] = c * vip - s * viq
            V[i][q] = s * vip + c * viq
    eigs = [A[i][i] for i in range(m)]
    vecs = [[V[row][col] for row in range(m)] for col in range(m)]
    order = sorted(range(m), key=lambda idx: eigs[idx], reverse=True)
    return [eigs[i] for i in order], [vecs[i] for i in order]


def main() -> None:
    # 1. Verify Lemma 5 (Chebyshev Minimizing Polynomial)
    alpha = 1.0
    gamma = 0.09
    q = 7  # odd degree
    val_at_threshold = chebyshev_min_poly(q, alpha, gamma, (1.0 + gamma) * alpha)
    assert abs(val_at_threshold - (1.0 + gamma) * alpha) < 1e-12
    for x in [1.09, 1.15, 1.3, 1.6, 2.0]:
        assert chebyshev_min_poly(q, alpha, gamma, x) >= x - 1e-12
    upper_bound = alpha / (2.0 ** (q * math.sqrt(gamma) - 1.0))
    max_in_tail = max(abs(chebyshev_min_poly(q, alpha, gamma, i * 0.05 * alpha)) for i in range(21))
    assert max_in_tail <= upper_bound + 1e-12
    # Odd symmetry p(-x) == -p(x) for odd q
    assert abs(chebyshev_min_poly(q, alpha, gamma, -0.7) + chebyshev_min_poly(q, alpha, gamma, 0.7)) < 1e-12

    # 2. Verify Block Krylov Iteration (Algorithm 2) vs Simultaneous Iteration (Algorithm 1)
    # Construct diagonal A in R^{12 x 12} with small gap and heavy tail:
    # sigma_1 = 1.10, sigma_2 = 1.05, sigma_3 = 1.00, sigma_4..12 in [0.85..0.98]
    sigmas = [1.10, 1.05, 1.00, 0.98, 0.96, 0.94, 0.92, 0.90, 0.88, 0.86, 0.84, 0.82]
    n = len(sigmas)
    k = 2
    q_iter = 4
    rng = random.Random(355)

    # Generate Pi in R^{n x k}
    Pi_cols = [[rng.gauss(0.0, 1.0) for _ in range(n)] for _ in range(k)]

    def apply_A(v: list[float]) -> list[float]:
        return [sigmas[i] * v[i] for i in range(n)]

    def apply_AAT(v: list[float]) -> list[float]:
        return [(sigmas[i] ** 2) * v[i] for i in range(n)]

    # Simultaneous Iteration: K_sim = (A A^T)^q A Pi
    sim_cols = [apply_A(col) for col in Pi_cols]
    for _ in range(q_iter):
        sim_cols = [apply_AAT(col) for col in sim_cols]
    Q_sim = gram_schmidt(sim_cols)

    # Block Krylov Iteration: K_bk = [A Pi, (A A^T) A Pi, ..., (A A^T)^q A Pi]
    bk_cols: list[list[float]] = []
    curr_cols = [apply_A(col) for col in Pi_cols]
    bk_cols.extend(curr_cols)
    for _ in range(q_iter):
        curr_cols = [apply_AAT(col) for col in curr_cols]
        bk_cols.extend(curr_cols)
    Q_bk = gram_schmidt(bk_cols)

    def extract_top_k(Q: list[list[float]]) -> list[list[float]]:
        m = len(Q)
        AQ = [apply_A(col) for col in Q]
        M = [[sum(AQ[i][r] * AQ[j][r] for r in range(n)) for j in range(m)] for i in range(m)]
        _, u_vecs = jacobi_sym_eig(M)
        Z: list[list[float]] = []
        for idx in range(k):
            u = u_vecs[idx]
            z = [sum(Q[j][r] * u[j] for j in range(m)) for r in range(n)]
            Z.append(z)
        return Z

    Z_sim = extract_top_k(Q_sim)
    Z_bk = extract_top_k(Q_bk)

    def eval_errors(Z: list[list[float]]) -> tuple[float, float, float]:
        # Residual R = (I - Z Z^T) A
        # Frobenius norm squared = sum_j ||(I - Z Z^T) A e_j||_2^2
        frob_sq = 0.0
        R_cols: list[list[float]] = []
        for j in range(n):
            col = [sigmas[j] if i == j else 0.0 for i in range(n)]
            for z in Z:
                proj = sum(z[i] * col[i] for i in range(n))
                for i in range(n):
                    col[i] -= proj * z[i]
            frob_sq += sum(x * x for x in col)
            R_cols.append(col)
        # Spectral norm via top eigenvalue of R^T R
        RTR = [[sum(R_cols[i][r] * R_cols[j][r] for r in range(n)) for j in range(n)] for i in range(n)]
        eigs_rtr, _ = jacobi_sym_eig(RTR)
        spec_err = math.sqrt(max(0.0, eigs_rtr[0]))
        # Per-vector PCA error: max_{i<k} |sigma_{i+1}^2 - z_i^T A A^T z_i|
        pv_err = 0.0
        for i in range(k):
            z = Z[i]
            rayleigh = sum((sigmas[r] ** 2) * (z[r] ** 2) for r in range(n))
            pv_err = max(pv_err, abs((sigmas[i] ** 2) - rayleigh))
        return spec_err, math.sqrt(frob_sq), pv_err

    spec_sim, frob_sim, pv_sim = eval_errors(Z_sim)
    spec_bk, frob_bk, pv_bk = eval_errors(Z_bk)
    opt_spec = sigmas[k]
    opt_frob = math.sqrt(sum(s * s for s in sigmas[k:]))

    assert spec_bk < spec_sim, f"Expected spec_bk ({spec_bk}) < spec_sim ({spec_sim})"
    assert frob_bk < frob_sim, f"Expected frob_bk ({frob_bk}) < frob_sim ({frob_sim})"
    assert pv_bk < pv_sim, f"Expected pv_bk ({pv_bk}) < pv_sim ({pv_sim})"
    assert spec_bk <= 1.02 * opt_spec

    print(
        f"[PASS] Round 355 Block Krylov SVD (Musco & Musco 2015): "
        f"cheb_tail={max_in_tail:.4e}<=bound={upper_bound:.4e}, "
        f"spec_bk={spec_bk:.5f}<spec_sim={spec_sim:.5f} (opt={opt_spec:.5f}), "
        f"pv_bk={pv_bk:.5f}<pv_sim={pv_sim:.5f}"
    )


if __name__ == "__main__":
    main()
