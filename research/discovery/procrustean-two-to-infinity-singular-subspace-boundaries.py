#!/usr/bin/env python3
"""Constructed boundary & regime verification for Round 282:
Procrustean Matrix Decomposition and Two-to-Infinity Norm Singular Subspace
Perturbation Bounds (Cape, Tang, & Priebe 2019, The Annals of Statistics
47(5):2405-2439, DOI:10.1214/18-AOS1752, arXiv:1705.10735v3).

Verifies:
1. Two-to-infinity subordinate matrix norm geometry (Section 6.1 Propositions
   6.1-6.6): exact non-submultiplicativity counterexample ||A B||_{2->inf} = 2 >
   sqrt(2) = ||A||_{2->inf} ||B||_{2->inf} and asymmetrically constrained
   sub-multiplicativity ||A B||_{2->inf} <= ||A||_{2->inf} ||B||_2 and
   ||C A||_{2->inf} <= ||C||_inf ||A||_{2->inf}.
2. Exact 4-term Procrustean matrix decomposition (Theorem 3.1) to machine
   precision (~1e-15) and Lemma 6.7 quadratic canonical-angle sandwich
   (1/2)||sin Theta(U_hat, U)||_2^2 <= ||U^T U_hat - W_U||_2 <= ||sin Theta(U_hat, U)||_2^2.
3. Theorem 4.2 uniform 2->inf perturbation bound ||U_hat - U W_U||_{2->inf} <=
   14 (||E||_inf / |lambda_r|) ||U||_{2->inf} under repeated top eigenvalues
   (lambda_1 = lambda_2) where individual eigenvectors rotate by O(1) due to
   zero internal eigengap.
"""

from __future__ import annotations

import json
import math
import random


def jacobi_eig_symmetric(a_in: list[list[float]], tol: float = 1e-13, max_sweeps: int = 120) -> tuple[list[float], list[list[float]]]:
    """Full symmetric eigendecomposition via classical Jacobi rotations."""
    n = len(a_in)
    a = [row[:] for row in a_in]
    v = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    for _ in range(max_sweeps):
        max_off = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(a[i][j]) > max_off:
                    max_off = abs(a[i][j])
        if max_off < tol:
            break
        for p in range(n):
            for q in range(p + 1, n):
                apq = a[p][q]
                if abs(apq) < tol:
                    continue
                app = a[p][p]
                aqq = a[q][q]
                tau = (aqq - app) / (2.0 * apq)
                t = math.copysign(1.0 / (abs(tau) + math.sqrt(1.0 + tau * tau)), tau) if tau != 0.0 else 1.0
                c = 1.0 / math.sqrt(1.0 + t * t)
                s = t * c
                a[p][p] = app - t * apq
                a[q][q] = aqq + t * apq
                a[p][q] = 0.0
                a[q][p] = 0.0
                for k in range(n):
                    if k != p and k != q:
                        akp = a[k][p]
                        akq = a[k][q]
                        a[k][p] = c * akp - s * akq
                        a[p][k] = a[k][p]
                        a[k][q] = s * akp + c * akq
                        a[q][k] = a[k][q]
                for k in range(n):
                    vkp = v[k][p]
                    vkq = v[k][q]
                    v[k][p] = c * vkp - s * vkq
                    v[k][q] = s * vkp + c * vkq

    evals = [a[i][i] for i in range(n)]
    order = sorted(range(n), key=lambda idx: evals[idx], reverse=True)
    evals_sorted = [evals[idx] for idx in order]
    v_sorted = [[v[i][idx] for idx in order] for i in range(n)]
    return evals_sorted, v_sorted


def mat_mul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    m = len(a)
    k_len = len(b)
    n = len(b[0])
    return [[sum(a[i][k] * b[k][j] for k in range(k_len)) for j in range(n)] for i in range(m)]


def mat_add(a: list[list[float]], b: list[list[float]], scale_b: float = 1.0) -> list[list[float]]:
    return [[a[i][j] + scale_b * b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def transpose(a: list[list[float]]) -> list[list[float]]:
    return [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]


def norm_2_to_inf(a: list[list[float]]) -> float:
    return max(math.sqrt(sum(val * val for val in row)) for row in a)


def norm_inf_op(a: list[list[float]]) -> float:
    return max(sum(abs(val) for val in row) for row in a)


def norm_op_2(a: list[list[float]]) -> float:
    ata = mat_mul(transpose(a), a)
    evals, _ = jacobi_eig_symmetric(ata)
    return math.sqrt(max(0.0, evals[0]))


def procrustes_orthogonal(m_mat: list[list[float]]) -> tuple[list[list[float]], list[float]]:
    """Given M = U^T U_hat in R^{r x r}, computes the orthogonal Procrustes factor
    W_U = W_1 W_2^T = M (M^T M)^{-1/2} and singular values sigma_k(M) = cos(theta_k).
    """
    r = len(m_mat)
    mtm = mat_mul(transpose(m_mat), m_mat)
    evals, evecs = jacobi_eig_symmetric(mtm)
    svals = [math.sqrt(max(0.0, ev)) for ev in evals]
    inv_sqrt = [[0.0 for _ in range(r)] for _ in range(r)]
    for k in range(r):
        s_inv = 1.0 / max(svals[k], 1e-15)
        for i in range(r):
            for j in range(r):
                inv_sqrt[i][j] += s_inv * evecs[i][k] * evecs[j][k]
    w_u = mat_mul(m_mat, inv_sqrt)
    return w_u, svals


def verify_norm_geometry() -> dict[str, float | bool]:
    """Experiment 1: Section 6.1 Propositions 6.1-6.5 (counterexample to
    2->inf submultiplicativity and asymmetric submultiplicativity bounds).
    """
    a_ce = [[1.0, 1.0], [1.0, 1.0]]
    b_ce = [[1.0, 0.0], [1.0, 0.0]]
    ab_ce = mat_mul(a_ce, b_ce)
    norm_a_2inf = norm_2_to_inf(a_ce)
    norm_b_2inf = norm_2_to_inf(b_ce)
    norm_ab_2inf = norm_2_to_inf(ab_ce)
    # ||AB||_{2->inf} = 2 > sqrt(2) = ||A||_{2->inf} ||B||_{2->inf}
    assert abs(norm_ab_2inf - 2.0) < 1e-12
    assert abs(norm_a_2inf * norm_b_2inf - math.sqrt(2.0)) < 1e-12
    assert norm_ab_2inf > norm_a_2inf * norm_b_2inf

    rng = random.Random(201905)
    a_rand = [[rng.gauss(0.0, 1.0) for _ in range(5)] for _ in range(8)]
    b_rand = [[rng.gauss(0.0, 1.0) for _ in range(4)] for _ in range(5)]
    c_rand = [[rng.gauss(0.0, 1.0) for _ in range(8)] for _ in range(6)]

    lhs_ab = norm_2_to_inf(mat_mul(a_rand, b_rand))
    rhs_ab = norm_2_to_inf(a_rand) * norm_op_2(b_rand)
    lhs_ca = norm_2_to_inf(mat_mul(c_rand, a_rand))
    rhs_ca = norm_inf_op(c_rand) * norm_2_to_inf(a_rand)

    assert lhs_ab <= rhs_ab + 1e-12
    assert lhs_ca <= rhs_ca + 1e-12

    return {
        "counterexample_AB_2_to_inf": round(norm_ab_2inf, 6),
        "counterexample_A_2inf_times_B_2inf": round(norm_a_2inf * norm_b_2inf, 6),
        "non_submultiplicative_confirmed": norm_ab_2inf > norm_a_2inf * norm_b_2inf,
        "prop65_AB_lhs": round(lhs_ab, 6),
        "prop65_AB_rhs": round(rhs_ab, 6),
        "prop65_CA_lhs": round(lhs_ca, 6),
        "prop65_CA_rhs": round(rhs_ca, 6),
    }


def verify_procrustean_decomposition_and_thm42() -> dict[str, float | int | bool]:
    """Experiment 2 & 3: Theorem 3.1 exact 4-term Procrustean decomposition,
    Lemma 6.7 canonical-angle sandwich, and Theorem 4.2 uniform 2->inf bound
    under degenerate top eigenvalues (lambda_1 = lambda_2 = 12.0).
    """
    rng = random.Random(201909)
    p = 24
    r = 2

    # Construct incoherent orthonormal U in R^{p x 2}
    u1 = [1.0 / math.sqrt(p) for _ in range(p)]
    u2 = [1.0 / math.sqrt(p) if i < p // 2 else -1.0 / math.sqrt(p) for i in range(p)]
    u_mat = [[u1[i], u2[i]] for i in range(p)]

    # Include a small non-zero residual component X = U Sigma V^T + U_perp Sigma_perp V_perp^T
    # with repeated top singular/eigenvalues lambda_1 = lambda_2 = 12.0 and third eigenvalue 1.5
    u3 = [1.0 / math.sqrt(p) if i % 2 == 0 else -1.0 / math.sqrt(p) for i in range(p)]
    lam1 = 12.0
    lam2 = 12.0  # Exact multiplicity! Individual eigengap is 0.
    lam3 = 1.5

    x_mat = [
        [
            lam1 * u1[i] * u1[j] + lam2 * u2[i] * u2[j] + lam3 * u3[i] * u3[j]
            for j in range(p)
        ]
        for i in range(p)
    ]

    e_mat = [[0.0 for _ in range(p)] for _ in range(p)]
    sigma_e = 0.04
    for i in range(p):
        e_mat[i][i] = rng.gauss(0.0, sigma_e)
        for j in range(i + 1, p):
            val = rng.gauss(0.0, sigma_e)
            e_mat[i][j] = val
            e_mat[j][i] = val

    x_hat = mat_add(x_mat, e_mat, 1.0)
    evals_hat, evecs_hat = jacobi_eig_symmetric(x_hat)
    u_hat = [[evecs_hat[i][k] for k in range(r)] for i in range(p)]
    sigma_hat_inv = [[1.0 / evals_hat[0], 0.0], [0.0, 1.0 / evals_hat[1]]]

    # For PSD X and X_hat with positive top eigenvalues, V = U and V_hat = U_hat
    v_mat = u_mat
    v_hat = u_hat

    ut_uhat = mat_mul(transpose(u_mat), u_hat)
    w_u, cos_thetas = procrustes_orthogonal(ut_uhat)
    w_v = w_u

    # Projector I - U U^T
    uut = mat_mul(u_mat, transpose(u_mat))
    proj_perp = [[(1.0 if i == j else 0.0) - uut[i][j] for j in range(p)] for i in range(p)]

    # Exact 4-term Procrustean decomposition of Theorem 3.1:
    # LHS = U_hat - U W_U
    lhs = mat_add(u_hat, mat_mul(u_mat, w_u), -1.0)

    # Term 1: (I - U U^T) E V W_V Sigma_hat^{-1}
    t1 = mat_mul(mat_mul(mat_mul(proj_perp, e_mat), mat_mul(v_mat, w_v)), sigma_hat_inv)
    # Term 2: (I - U U^T) E (V_hat - V W_V) Sigma_hat^{-1}
    vhat_minus_vw = mat_add(v_hat, mat_mul(v_mat, w_v), -1.0)
    t2 = mat_mul(mat_mul(mat_mul(proj_perp, e_mat), vhat_minus_vw), sigma_hat_inv)
    # Term 3: (I - U U^T) X (V_hat - V V^T V_hat) Sigma_hat^{-1}
    vvt_vhat = mat_mul(mat_mul(v_mat, transpose(v_mat)), v_hat)
    vhat_proj_perp = mat_add(v_hat, vvt_vhat, -1.0)
    t3 = mat_mul(mat_mul(mat_mul(proj_perp, x_mat), vhat_proj_perp), sigma_hat_inv)
    # Term 4: U (U^T U_hat - W_U)
    t4 = mat_mul(u_mat, mat_add(ut_uhat, w_u, -1.0))

    rhs = mat_add(mat_add(t1, t2, 1.0), mat_add(t3, t4, 1.0), 1.0)
    decomp_diff = mat_add(lhs, rhs, -1.0)
    max_abs_decomp_err = max(abs(val) for row in decomp_diff for val in row)
    assert max_abs_decomp_err < 1e-13, f"Theorem 3.1 decomposition error: {max_abs_decomp_err}"

    # Verify Lemma 6.7: 0.5 ||sin Theta(U_hat, U)||_2^2 <= ||U^T U_hat - W_U||_2 <= ||sin Theta(U_hat, U)||_2^2
    sin_sq_max = max(max(0.0, 1.0 - c * c) for c in cos_thetas)
    ut_uhat_minus_w_op2 = norm_op_2(mat_add(ut_uhat, w_u, -1.0))
    assert 0.5 * sin_sq_max - 1e-14 <= ut_uhat_minus_w_op2 <= sin_sq_max + 1e-14

    # Verify Theorem 4.2 bound on rank-2 pure signal + noise (setting lam3 = 0)
    x_rank2 = [
        [lam1 * u1[i] * u1[j] + lam2 * u2[i] * u2[j] for j in range(p)]
        for i in range(p)
    ]
    x_rank2_hat = mat_add(x_rank2, e_mat, 1.0)
    _, evecs_r2 = jacobi_eig_symmetric(x_rank2_hat)
    u_r2_hat = [[evecs_r2[i][k] for k in range(r)] for i in range(p)]
    w_r2, _ = procrustes_orthogonal(mat_mul(transpose(u_mat), u_r2_hat))

    procrustes_2inf_err = norm_2_to_inf(mat_add(u_r2_hat, mat_mul(u_mat, w_r2), -1.0))
    # Unaligned column 1 error (minimized over +-1 sign only)
    col1_plus = max(abs(u_r2_hat[i][0] - u1[i]) for i in range(p))
    col1_minus = max(abs(u_r2_hat[i][0] + u1[i]) for i in range(p))
    unaligned_col1_inf_err = min(col1_plus, col1_minus)

    thm42_bound = 14.0 * (norm_inf_op(e_mat) / lam2) * norm_2_to_inf(u_mat)
    assert procrustes_2inf_err <= thm42_bound
    assert procrustes_2inf_err < 0.25 * unaligned_col1_inf_err

    return {
        "p": p,
        "r": r,
        "degenerate_top_eigenvalues": [lam1, lam2],
        "theorem31_max_abs_err": max_abs_decomp_err,
        "lemma67_half_sin_sq": round(0.5 * sin_sq_max, 8),
        "lemma67_ut_uhat_minus_w_op2": round(ut_uhat_minus_w_op2, 8),
        "lemma67_sin_sq": round(sin_sq_max, 8),
        "unaligned_col1_inf_err": round(unaligned_col1_inf_err, 6),
        "procrustes_aligned_2_to_inf_err": round(procrustes_2inf_err, 6),
        "theorem42_upper_bound": round(thm42_bound, 6),
    }


def main() -> None:
    res1 = verify_norm_geometry()
    res2 = verify_procrustean_decomposition_and_thm42()
    payload = {
        "concept": "AIMech:ProcrusteanMatrixDecompositionAndTwoToInfinityNormSingularSubspacePerturbationBounds",
        "source": "Cape, Tang, & Priebe (2019), Annals of Statistics 47(5):2405-2439, arXiv:1705.10735v3",
        "results": {
            "norm_geometry": res1,
            "procrustean_decomposition_and_thm42": res2,
        },
        "all_assertions_passed": True,
    }
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
