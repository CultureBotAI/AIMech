#!/usr/bin/env python3
"""Constructed boundary & regime verification for POET (Fan, Liao, & Mincheva 2013).

Verifies:
1. Propositions 2.1 & 2.2 (spiked eigenvalue Weyl bounds |lambda_j - ||b_tilde_j||^2| <= ||Sigma_u||
   for j <= K, |lambda_j| <= ||Sigma_u|| for j > K, and eigenvector sin-theta alignment).
2. Theorem 2.1 algebraic equivalence between regularized PCA POET
   (Sigma_hat_K = sum_{i=1}^K lambda_hat_i xi_hat_i xi_hat_i' + R_hat_K^T)
   and constrained least-squares substitution (Sigma_tilde_K = Lambda_hat_K Lambda_hat_K' + Sigma_hat_{u,K}^T),
   plus Sherman-Morrison-Woodbury precision identity (Eq. 2.13).
3. Theorems 3.1 & 3.2 comparison of POET against unregularized sample covariance Sigma_hat_sam,
   and strict diagonal factor model SFM (tau=1) under relative entropy-loss norm
   ||Sigma_hat - Sigma||_Sigma and precision error ||Sigma_hat^{-1} - Sigma^{-1}||.
"""

import json
import math
import random


def mat_mul(A, B):
    m, k = len(A), len(A[0])
    n = len(B[0])
    C = [[0.0] * n for _ in range(m)]
    for i in range(m):
        Ai = A[i]
        Ci = C[i]
        for r in range(k):
            air = Ai[r]
            if air == 0.0:
                continue
            Br = B[r]
            for j in range(n):
                Ci[j] += air * Br[j]
    return C


def mat_trans(A):
    return [list(col) for col in zip(*A)]


def mat_add(A, B, scale_b=1.0):
    return [
        [A[i][j] + scale_b * B[i][j] for j in range(len(A[0]))]
        for i in range(len(A))
    ]


def frob_norm(A):
    return math.sqrt(sum(x * x for row in A for x in row))


def max_norm(A):
    return max(abs(x) for row in A for x in row)


def jacobi_eig_sym(A, tol=1e-12, max_sweeps=60):
    """Symmetric eigenvalue decomposition A = V diag(w) V^T sorted descending."""
    n = len(A)
    M = [row[:] for row in A]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(max_sweeps):
        off = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                off += M[i][j] * M[i][j]
        if math.sqrt(off) < tol:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                apq = M[p][q]
                if abs(apq) < tol / n:
                    continue
                app = M[p][p]
                aqq = M[q][q]
                tau = (aqq - app) / (2.0 * apq)
                t = (
                    math.copysign(1.0, tau)
                    / (abs(tau) + math.sqrt(1.0 + tau * tau))
                    if tau != 0.0
                    else 1.0
                )
                c = 1.0 / math.sqrt(1.0 + t * t)
                s = t * c
                for r in range(n):
                    if r != p and r != q:
                        mrp = M[r][p]
                        mrq = M[r][q]
                        M[r][p] = M[p][r] = c * mrp - s * mrq
                        M[r][q] = M[q][r] = s * mrp + c * mrq
                M[p][p] = c * c * app - 2.0 * s * c * apq + s * s * aqq
                M[q][q] = s * s * app + 2.0 * s * c * apq + c * c * aqq
                M[p][q] = M[q][p] = 0.0
                for r in range(n):
                    vrp = V[r][p]
                    vrq = V[r][q]
                    V[r][p] = c * vrp - s * vrq
                    V[r][q] = s * vrp + c * vrq
    vals = [M[i][i] for i in range(n)]
    order = sorted(range(n), key=lambda i: vals[i], reverse=True)
    sorted_vals = [vals[i] for i in order]
    sorted_vecs = [[V[r][order[c]] for c in range(n)] for r in range(n)]
    return sorted_vals, sorted_vecs


def sym_inv_and_invsqrt(A):
    vals, V = jacobi_eig_sym(A)
    n = len(A)
    Vt = mat_trans(V)
    inv_diag = [1.0 / max(v, 1e-12) for v in vals]
    invsqrt_diag = [1.0 / math.sqrt(max(v, 1e-12)) for v in vals]
    V_inv = [[V[i][j] * inv_diag[j] for j in range(n)] for i in range(n)]
    V_invsqrt = [[V[i][j] * invsqrt_diag[j] for j in range(n)] for i in range(n)]
    return mat_mul(V_inv, Vt), mat_mul(V_invsqrt, Vt), vals


def spectral_norm_sym(A):
    vals, _ = jacobi_eig_sym(A)
    return max(abs(v) for v in vals)


def rel_sigma_norm(Sigma_hat, Sigma_invsqrt):
    p = len(Sigma_hat)
    M = mat_mul(mat_mul(Sigma_invsqrt, Sigma_hat), Sigma_invsqrt)
    for i in range(p):
        M[i][i] -= 1.0
    return frob_norm(M) / math.sqrt(p)


def main():
    rng = random.Random(20261019)
    p = 24
    T = 120
    K = 2

    # 1. Construct canonical orthogonal factor loadings B (p x K) with distinct norms
    raw1 = [1.0 if i % 2 == 0 else -0.8 for i in range(p)]
    n1 = math.sqrt(sum(x * x for x in raw1))
    b_tilde_1 = [x * math.sqrt(1.8 * p) / n1 for x in raw1]

    raw2 = [math.sin(0.7 * (i + 1)) for i in range(p)]
    proj = sum(raw2[i] * b_tilde_1[i] for i in range(p)) / (1.8 * p)
    orth2 = [raw2[i] - proj * b_tilde_1[i] for i in range(p)]
    n2 = math.sqrt(sum(x * x for x in orth2))
    b_tilde_2 = [x * math.sqrt(0.9 * p) / n2 for x in orth2]

    B = [[b_tilde_1[i], b_tilde_2[i]] for i in range(p)]
    BBt = mat_mul(B, mat_trans(B))

    # Construct sparse block-diagonal idiosyncratic covariance Sigma_u (first 4 blocks of 2x2 have correlation 0.65)
    Sigma_u = [[0.0] * p for _ in range(p)]
    for i in range(p):
        Sigma_u[i][i] = 1.0
    for b in range(0, 8, 2):
        Sigma_u[b][b + 1] = Sigma_u[b + 1][b] = 0.65

    Sigma = mat_add(BBt, Sigma_u, 1.0)
    Sigma_inv, Sigma_invsqrt, pop_eigs = sym_inv_and_invsqrt(Sigma)
    Sigma_u_inv, _, u_eigs = sym_inv_and_invsqrt(Sigma_u)
    sigma_u_spec = max(abs(v) for v in u_eigs)

    # Verify Proposition 2.1 Weyl bounds
    b1_sq = 1.8 * p
    b2_sq = 0.9 * p
    weyl_err_1 = abs(pop_eigs[0] - b1_sq)
    weyl_err_2 = abs(pop_eigs[1] - b2_sq)
    max_tail_eig = max(abs(v) for v in pop_eigs[K:])
    assert weyl_err_1 <= sigma_u_spec + 1e-9
    assert weyl_err_2 <= sigma_u_spec + 1e-9
    assert max_tail_eig <= sigma_u_spec + 1e-9

    # Verify Proposition 2.2 eigenvector alignment
    _, pop_vecs = jacobi_eig_sym(Sigma)
    xi1 = [pop_vecs[i][0] for i in range(p)]
    u1 = [b_tilde_1[i] / math.sqrt(b1_sq) for i in range(p)]
    dot1 = sum(xi1[i] * u1[i] for i in range(p))
    if dot1 < 0:
        xi1 = [-x for x in xi1]
    vec_align_err_1 = math.sqrt(sum((xi1[i] - u1[i]) ** 2 for i in range(p)))
    assert vec_align_err_1 < 0.05

    # 2. Simulate data Y (p x T) = B F' + U
    L_u = [[0.0] * p for _ in range(p)]
    for i in range(p):
        for j in range(i + 1):
            s = sum(L_u[i][k] * L_u[j][k] for k in range(j))
            if i == j:
                L_u[i][j] = math.sqrt(Sigma_u[i][i] - s)
            else:
                L_u[i][j] = (Sigma_u[i][j] - s) / L_u[j][j]

    F = [[rng.gauss(0.0, 1.0) for _ in range(K)] for _ in range(T)]
    U = [[0.0] * T for _ in range(p)]
    for t in range(T):
        z = [rng.gauss(0.0, 1.0) for _ in range(p)]
        for i in range(p):
            U[i][t] = sum(L_u[i][k] * z[k] for k in range(i + 1))

    Y = [[0.0] * T for _ in range(p)]
    for i in range(p):
        for t in range(T):
            Y[i][t] = sum(B[i][k] * F[t][k] for k in range(K)) + U[i][t]

    # Sample covariance Sigma_hat_sam = (1/T) Y Y'
    Sigma_sam = [[0.0] * p for _ in range(p)]
    for i in range(p):
        for j in range(i, p):
            val = sum(Y[i][t] * Y[j][t] for t in range(T)) / T
            Sigma_sam[i][j] = Sigma_sam[j][i] = val

    sam_eigs, sam_vecs = jacobi_eig_sym(Sigma_sam)

    # Regularized PCA representation (Eqs. 2.4-2.7)
    LowRank_PCA = [[0.0] * p for _ in range(p)]
    for k in range(K):
        lam_k = sam_eigs[k]
        for i in range(p):
            for j in range(p):
                LowRank_PCA[i][j] += lam_k * sam_vecs[i][k] * sam_vecs[j][k]
    R_hat_K = mat_add(Sigma_sam, LowRank_PCA, -1.0)

    # Constrained Least Squares substitution representation (Eqs. 2.8-2.12)
    YtY = mat_mul(mat_trans(Y), Y)
    yty_eigs, yty_vecs = jacobi_eig_sym(YtY)
    F_hat_K = [
        [math.sqrt(T) * yty_vecs[t][k] for k in range(K)] for t in range(T)
    ]
    Lambda_hat_K = [
        [sum(Y[i][t] * F_hat_K[t][k] for t in range(T)) / T for k in range(K)]
        for i in range(p)
    ]
    LowRank_LS = mat_mul(Lambda_hat_K, mat_trans(Lambda_hat_K))
    u_hat = [
        [
            Y[i][t] - sum(Lambda_hat_K[i][k] * F_hat_K[t][k] for k in range(K))
            for t in range(T)
        ]
        for i in range(p)
    ]
    Sigma_u_hat_raw = [
        [sum(u_hat[i][t] * u_hat[j][t] for t in range(T)) / T for j in range(p)]
        for i in range(p)
    ]

    # Verify Theorem 2.1 equivalence before and after adaptive hard thresholding (Section 6.2 Step 5, p. 26)
    equiv_lowrank_diff = max_norm(mat_add(LowRank_PCA, LowRank_LS, -1.0))
    equiv_resid_diff = max_norm(mat_add(R_hat_K, Sigma_u_hat_raw, -1.0))
    assert equiv_lowrank_diff < 1e-9
    assert equiv_resid_diff < 1e-9

    omega_T = 1.0 / math.sqrt(p) + math.sqrt(math.log(p) / T)
    C_thresh = 0.45
    R_hat_T = [[0.0] * p for _ in range(p)]
    for i in range(p):
        for j in range(p):
            if i == j:
                R_hat_T[i][j] = R_hat_K[i][i]
            else:
                s_ij = Sigma_u_hat_raw[i][j]
                theta_ij = (
                    sum((u_hat[i][t] * u_hat[j][t] - s_ij) ** 2 for t in range(T))
                    / T
                )
                tau_ij = C_thresh * math.sqrt(theta_ij) * omega_T
                val = R_hat_K[i][j]
                R_hat_T[i][j] = (
                    math.copysign(abs(val) - tau_ij, val)
                    if abs(val) > tau_ij
                    else 0.0
                )

    Sigma_POET = mat_add(LowRank_PCA, R_hat_T, 1.0)
    Sigma_tilde_K = mat_add(LowRank_LS, R_hat_T, 1.0)
    assert max_norm(mat_add(Sigma_POET, Sigma_tilde_K, -1.0)) < 1e-9

    # Verify Sherman-Morrison-Woodbury precision formula (Eq. 2.13)
    R_T_inv, _, rt_eigs = sym_inv_and_invsqrt(R_hat_T)
    assert min(rt_eigs) > 0.0
    Lt_Rinv = mat_mul(mat_trans(Lambda_hat_K), R_T_inv)
    Inner = mat_mul(Lt_Rinv, Lambda_hat_K)
    for k in range(K):
        Inner[k][k] += 1.0
    Inner_inv, _, _ = sym_inv_and_invsqrt(Inner)
    Rinv_L = mat_mul(R_T_inv, Lambda_hat_K)
    Woodbury_sub = mat_mul(mat_mul(Rinv_L, Inner_inv), Lt_Rinv)
    Sigma_POET_inv_woodbury = mat_add(R_T_inv, Woodbury_sub, -1.0)
    Sigma_POET_inv_direct, _, _ = sym_inv_and_invsqrt(Sigma_POET)
    woodbury_diff = max_norm(
        mat_add(Sigma_POET_inv_woodbury, Sigma_POET_inv_direct, -1.0)
    )
    assert woodbury_diff < 1e-9

    # Compare against SFM (diagonal residual covariance) and Sample Covariance
    R_SFM = [
        [R_hat_K[i][i] if i == j else 0.0 for j in range(p)] for i in range(p)
    ]
    Sigma_SFM = mat_add(LowRank_PCA, R_SFM, 1.0)
    Sigma_SFM_inv, _, _ = sym_inv_and_invsqrt(Sigma_SFM)
    Sigma_sam_inv, _, _ = sym_inv_and_invsqrt(Sigma_sam)

    # Verify Bai-Ng IC1 recovers K_hat = 2
    ic1_scores = {}
    for k_cand in range(5):
        tot_ss = sum(Y[i][t] ** 2 for i in range(p) for t in range(T))
        explained = sum(yty_eigs[:k_cand]) if k_cand > 0 else 0.0
        rss = max((tot_ss - explained) / (p * T), 1e-12)
        pen = k_cand * ((p + T) / (p * T)) * math.log((p * T) / (p + T))
        ic1_scores[k_cand] = round(math.log(rss) + pen, 6)
    k_hat_ic1 = min(ic1_scores, key=ic1_scores.get)
    assert k_hat_ic1 == K

    poet_u_err = spectral_norm_sym(mat_add(R_hat_T, Sigma_u, -1.0))
    raw_u_err = spectral_norm_sym(mat_add(R_hat_K, Sigma_u, -1.0))
    sfm_u_err = spectral_norm_sym(mat_add(R_SFM, Sigma_u, -1.0))
    assert poet_u_err < raw_u_err
    assert poet_u_err < sfm_u_err

    poet_rel_err = rel_sigma_norm(Sigma_POET, Sigma_invsqrt)
    sfm_rel_err = rel_sigma_norm(Sigma_SFM, Sigma_invsqrt)
    sam_rel_err = rel_sigma_norm(Sigma_sam, Sigma_invsqrt)
    assert poet_rel_err < sfm_rel_err and poet_rel_err < sam_rel_err

    poet_prec_err = spectral_norm_sym(
        mat_add(Sigma_POET_inv_woodbury, Sigma_inv, -1.0)
    )
    sfm_prec_err = spectral_norm_sym(mat_add(Sigma_SFM_inv, Sigma_inv, -1.0))
    sam_prec_err = spectral_norm_sym(mat_add(Sigma_sam_inv, Sigma_inv, -1.0))
    assert poet_prec_err < sfm_prec_err and poet_prec_err < sam_prec_err, (
        f"poet={poet_prec_err}, sfm={sfm_prec_err}, sam={sam_prec_err}, "
        f"poet_u={poet_u_err}, sfm_u={sfm_u_err}, raw_u={raw_u_err}"
    )

    result = {
        "concept": "AIMech:PrincipalOrthogonalComplementThresholdingForApproximateFactorCovarianceEstimation",
        "source": "Fan, Liao, & Mincheva (2013), JRSS Series B 75(4):603-680, arXiv:1201.0175v2",
        "population_spectrum_and_weyl_bounds": {
            "p": p,
            "T": T,
            "K_true": K,
            "K_hat_IC1": k_hat_ic1,
            "sigma_u_spectral_norm": round(sigma_u_spec, 6),
            "weyl_error_1": round(weyl_err_1, 6),
            "weyl_error_2": round(weyl_err_2, 6),
            "max_tail_eigenvalue": round(max_tail_eig, 6),
            "eigenvector_1_alignment_l2": round(vec_align_err_1, 6),
        },
        "theorem_2_1_and_woodbury_equivalence": {
            "pca_vs_ls_lowrank_max_diff": round(equiv_lowrank_diff, 12),
            "pca_vs_ls_residual_max_diff": round(equiv_resid_diff, 12),
            "woodbury_precision_max_diff": round(woodbury_diff, 12),
        },
        "estimation_error_comparison": {
            "idiosyncratic_spectral_error_poet": round(poet_u_err, 6),
            "idiosyncratic_spectral_error_sfm": round(sfm_u_err, 6),
            "idiosyncratic_spectral_error_unthresholded": round(raw_u_err, 6),
            "relative_sigma_error_poet": round(poet_rel_err, 6),
            "relative_sigma_error_sfm": round(sfm_rel_err, 6),
            "relative_sigma_error_sample": round(sam_rel_err, 6),
            "precision_spectral_error_poet": round(poet_prec_err, 6),
            "precision_spectral_error_sfm": round(sfm_prec_err, 6),
            "precision_spectral_error_sample": round(sam_prec_err, 6),
        },
        "all_assertions_passed": True,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
