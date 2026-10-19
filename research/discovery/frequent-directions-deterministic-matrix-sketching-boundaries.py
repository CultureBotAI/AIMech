#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 363:
Frequent Directions Deterministic Matrix Sketching (Ghashami, Liberty, Phillips, & Woodruff 2016).
"""

import math
import random


def mat_transpose(A):
    return [list(col) for col in zip(*A)]


def mat_mul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    return [[sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)] for i in range(m)]


def frob_sq(A):
    return sum(x * x for row in A for x in row)


def jacobi_eig_sym(S, max_iter=300, tol=1e-14):
    """Exact Jacobi eigendecomposition for symmetric d x d matrix S.
    Returns (eigenvalues_desc, eigenvectors_cols_desc).
    """
    d = len(S)
    A = [row[:] for row in S]
    V = [[1.0 if i == j else 0.0 for j in range(d)] for i in range(d)]
    for _ in range(max_iter):
        best_val = 0.0
        p, q = 0, 1
        for i in range(d):
            for j in range(i + 1, d):
                if abs(A[i][j]) > best_val:
                    best_val = abs(A[i][j])
                    p, q = i, j
        if best_val < tol:
            break
        diff = A[q][q] - A[p][p]
        if abs(A[p][q]) < tol * abs(diff):
            t = A[p][q] / diff
        else:
            phi = diff / (2.0 * A[p][q])
            t = 1.0 / (abs(phi) + math.sqrt(phi * phi + 1.0))
            if phi < 0:
                t = -t
        c = 1.0 / math.sqrt(1.0 + t * t)
        s = t * c
        tau = s / (1.0 + c)
        h = t * A[p][q]
        A[p][p] -= h
        A[q][q] += h
        A[p][q] = 0.0
        A[q][p] = 0.0
        for r in range(d):
            if r != p and r != q:
                arp, arq = A[r][p], A[r][q]
                A[r][p] = A[p][r] = arp - s * (arq + tau * arp)
                A[r][q] = A[q][r] = arq + s * (arp - tau * arq)
        for r in range(d):
            vrp, vrq = V[r][p], V[r][q]
            V[r][p] = vrp - s * (vrq + tau * vrp)
            V[r][q] = vrq + s * (vrp - tau * vrq)
    eigs = [max(0.0, A[i][i]) for i in range(d)]
    order = sorted(range(d), key=lambda i: -eigs[i])
    sorted_eigs = [eigs[i] for i in order]
    sorted_V = [[V[r][i] for i in order] for r in range(d)]
    return sorted_eigs, sorted_V


def frequent_directions(A, ell):
    """Algorithm 2.1 FrequentDirections (Page 5 of Ghashami et al. 2016).
    Maintains an ell x d sketch B where the last row is always zeroed after shrinking by delta_i = sigma_ell^2.
    Returns (B, total_Delta).
    """
    d = len(A[0])
    B = [[0.0] * d for _ in range(ell)]
    total_delta = 0.0
    for row in A:
        B[ell - 1] = row[:]
        # Compute SVD of B via eigendecomposition of B^T B
        BtB = mat_mul(mat_transpose(B), B)
        eigs, V = jacobi_eig_sym(BtB)
        # eigs[0] >= eigs[1] >= ... >= eigs[ell-1] = sigma_ell^2
        delta = eigs[ell - 1]
        total_delta += delta
        # B <- sqrt(Sigma^2 - delta I_ell) V^T
        new_B = [[0.0] * d for _ in range(ell)]
        for r in range(ell - 1):
            s_r = math.sqrt(max(0.0, eigs[r] - delta))
            for j in range(d):
                new_B[r][j] = s_r * V[j][r]
        B = new_B
    return B, total_delta


def incremental_svd_no_shrink(A, ell):
    """Incremental SVD baseline (Section 5, p. 20): drops sigma_ell without shrinking top ell-1 singular values."""
    d = len(A[0])
    B = [[0.0] * d for _ in range(ell)]
    for row in A:
        B[ell - 1] = row[:]
        BtB = mat_mul(mat_transpose(B), B)
        eigs, V = jacobi_eig_sym(BtB)
        new_B = [[0.0] * d for _ in range(ell)]
        for r in range(ell - 1):
            s_r = math.sqrt(max(0.0, eigs[r]))
            for j in range(d):
                new_B[r][j] = s_r * V[j][r]
        B = new_B
    return B


def spectral_norm_sym(M):
    eigs, _ = jacobi_eig_sym(M)
    return max(abs(x) for x in eigs)


def main():
    rng = random.Random(20261019)
    n, d, ell = 24, 6, 4
    # Construct matrix A with spiked singular spectrum + isotropic stream rows
    A = []
    for i in range(n):
        row = [
            3.0 * math.sin(0.4 * i + 0.1),
            2.0 * math.cos(0.3 * i - 0.2),
            0.7 * rng.gauss(0, 1),
            0.6 * rng.gauss(0, 1),
            0.5 * rng.gauss(0, 1),
            0.5 * rng.gauss(0, 1),
        ]
        A.append(row)

    B, Delta = frequent_directions(A, ell)
    AtA = mat_mul(mat_transpose(A), A)
    BtB = mat_mul(mat_transpose(B), B)
    eigs_A, V_A = jacobi_eig_sym(AtA)
    eigs_B, V_B = jacobi_eig_sym(BtB)

    # 1. Verify Properties 1, 2, and 3 (Page 6)
    # Diff = A^T A - B^T B must be positive semidefinite (Property 1) and have top eigenvalue <= Delta (Property 2)
    Diff = [[AtA[i][j] - BtB[i][j] for j in range(d)] for i in range(d)]
    # Check eigenvalues of Diff directly
    # Since Diff is PSD, jacobi_eig_sym gives its eigenvalues
    eigs_diff, _ = jacobi_eig_sym(Diff)
    # Verify quadratic form x^T Diff x in [0, Delta] across basis and random unit vectors
    min_quad = 1e9
    max_quad = -1e9
    for _ in range(200):
        vec = [rng.gauss(0, 1) for _ in range(d)]
        norm = math.sqrt(sum(v * v for v in vec))
        u = [v / norm for v in vec]
        q = sum(u[i] * Diff[i][j] * u[j] for i in range(d) for j in range(d))
        min_quad = min(min_quad, q)
        max_quad = max(max_quad, q)
    assert min_quad >= -1e-11, f"Property 1 violated: min_quad={min_quad}"
    assert max_quad <= Delta + 1e-11, f"Property 2 violated: max_quad={max_quad} > Delta={Delta}"

    # Property 3: Delta * ell == ||A||_F^2 - ||B||_F^2 (exact equality for Algorithm 2.1!)
    prop3_err = abs(Delta * ell - (frob_sq(A) - frob_sq(B)))
    assert prop3_err < 1e-10, f"Property 3 error: {prop3_err}"

    # 2. Verify Theorem 1.1 & Theorem 1.2 for k = 0, 1, 2 (Pages 4, 6-7)
    for k in (0, 1, 2):
        # ||A - A_k||_F^2 = sum_{i=k+1}^d sigma_i^2(A)
        rem_frob_sq = sum(eigs_A[k:])
        bound_thm11 = rem_frob_sq / float(ell - k)
        assert max_quad <= Delta <= bound_thm11 + 1e-10, f"Theorem 1.1 failed for k={k}"

        if k > 0:
            # Project A onto top-k right singular vectors of B: ||A - pi_B^k(A)||_F^2 = ||A||_F^2 - sum_{i=1}^k ||A v_i(B)||^2
            proj_norm_sq = 0.0
            for r in range(k):
                v_r = [V_B[j][r] for j in range(d)]
                Av_r_sq = sum(v_r[i] * AtA[i][j] * v_r[j] for i in range(d) for j in range(d))
                proj_norm_sq += Av_r_sq
            err_proj_sq = frob_sq(A) - proj_norm_sq
            bound_thm12 = (float(ell) / float(ell - k)) * rem_frob_sq
            assert err_proj_sq <= bound_thm12 + 1e-10, f"Theorem 1.2 failed for k={k}: {err_proj_sq} > {bound_thm12}"

    # 3. Verify Section 3.1 Mergeable Summaries (Page 8)
    A1, A2 = A[:12], A[12:]
    B1, D1 = frequent_directions(A1, ell)
    B2, D2 = frequent_directions(A2, ell)
    B_merged, D_merge = frequent_directions(B1 + B2, ell)
    Total_Delta_merged = D1 + D2 + D_merge
    prop3_merge_err = abs(Total_Delta_merged * ell - (frob_sq(A) - frob_sq(B_merged)))
    assert prop3_merge_err < 1e-10
    assert Total_Delta_merged <= sum(eigs_A[2:]) / float(ell - 2) + 1e-10

    # 4. Verify Section 5 (p. 20): Incremental SVD without shrinkage fails dramatically on adversarial stream
    # With ell=3 (2 active slots), 1 row each of e_1 (norm 2.0) and e_2 (norm 2.0), followed by 10 rows of e_3 (norm 1.8):
    # Unshrunk Incremental SVD drops e_3 (1.8 < 2.0) on EVERY step, missing the dominant direction (cov_err = 32.4),
    # whereas FrequentDirections shrinks e_1, e_2 on the first e_3 arrival and captures e_3 with cov_err <= ||A - A_1||_F^2 / 2 = 4.0!
    A_adv = [
        [2.0, 0.0, 0.0],
        [0.0, 2.0, 0.0],
    ] + [[0.0, 0.0, 1.8] for _ in range(10)]
    B_fd_adv, D_fd_adv = frequent_directions(A_adv, ell=3)
    B_inc_adv = incremental_svd_no_shrink(A_adv, ell=3)
    AtA_adv = mat_mul(mat_transpose(A_adv), A_adv)
    BtB_fd_adv = mat_mul(mat_transpose(B_fd_adv), B_fd_adv)
    BtB_inc_adv = mat_mul(mat_transpose(B_inc_adv), B_inc_adv)
    cov_err_fd = max(abs(AtA_adv[i][i] - BtB_fd_adv[i][i]) for i in range(3))
    cov_err_inc = max(abs(AtA_adv[i][i] - BtB_inc_adv[i][i]) for i in range(3))
    # ||A_adv - (A_adv)_1||_F^2 / (ell - 1) = (4.0 + 4.0) / 2 = 4.0
    assert cov_err_fd <= 4.0 + 1e-10
    assert abs(cov_err_inc - 32.4) < 1e-10
    assert cov_err_inc > 8.0 * cov_err_fd

    print(
        f"[PASS] Round 363 Frequent Directions (Ghashami et al. 2016): "
        f"prop1_min={min_quad:.2e}, Delta={Delta:.4f}<={sum(eigs_A[2:])/(ell-2):.4f}, "
        f"prop3_err={prop3_err:.2e}, merge_err={prop3_merge_err:.2e}, "
        f"adv_cov_fd={cov_err_fd:.4f}<<inc={cov_err_inc:.4f}"
    )


if __name__ == "__main__":
    main()
