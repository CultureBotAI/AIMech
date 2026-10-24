#!/usr/bin/env python3
"""Constructed boundary & verification script for AsymmetricLowRankEigenvalueAndLinearFormEigenvectorPerturbationAnalysis.

Verifies the core mathematical properties of Chen, Cheng, & Fan (2021),
'Asymmetry Helps: Eigenvalue and Eigenvector Analyses of Asymmetrically
Perturbed Low-Rank Matrices', The Annals of Statistics, 49(1), 435-458
(DOI:10.1214/20-AOS1963, arXiv:1811.12804v5):

1. Second-Order Quadratic Form Bias Cancellation (Section 4.3):
   For a rank-1 symmetric signal M^* = lambda^* u^* (u^*)^T perturbed by random
   noise H with zero-mean variance-sigma^2 entries:
     - Asymmetric independent noise (H_{ij} independent for all i, j):
       E[H^2] = sigma^2 * O(1) diagonal (specifically E[(H^2)_{ii}] = sum_k E[H_{ik} H_{ki}] = sigma^2),
       so E[(u^*)^T H^2 u^*] = sigma^2.
     - Symmetric independent noise (H_{ij} = H_{ji} independent for i <= j):
       E[H^2] = n * sigma^2 I_n, so E[(u^*)^T H^2 u^*] = n * sigma^2, creating an
       O(n * sigma^2 / lambda^*) upward bias in the leading eigenvalue of (M + M^T)/2
       and in the leading singular value of M (Eq. 21).
2. Neumann Series Master Expansion (Theorem 2 & Theorem 3):
   When ||H|| < |lambda|, the leading eigenvector u of M = M^* + H satisfies the exact
   Neumann expansion:
     u = (lambda^* / lambda) ((u^*)^T u) sum_{s=0}^infty (1 / lambda^s) H^s u^*,
   so for any deterministic unit direction a in R^n,
     |a^T (u - ((u^*)^T u / (lambda / lambda^*)) u^*)| <= |(u^*)^T u / lambda| sum_{s>=1} |a^T H^s u^*| / |lambda|^s,
   yielding O(sqrt(mu / n)) delocalized error and Corollary 1 eigenvalue error
   |lambda - lambda^*| = O(sigma sqrt(mu log n)), which is O(sqrt(n)) times smaller
   than the unadjusted singular value error |sigma_1(M) - lambda^*| or symmetrized
   eigenvalue bias |lambda_1((M + M^T)/2) - lambda^*|.
3. Asymmetrized Dilation for Rectangular Rank-1 Matrices (Section 5.2, Eq. 43,
   Corollary 8 & Theorem 5):
   Embedding two independent noisy copies M_1 = M^* + H_1, M_2 = M^* + H_2 into
     M_d = [[0, M_1], [M_2^T, 0]]
   yields leading eigenvalue lambda_1(M_d) that estimates sigma_1(M^*) much more
   accurately than sigma_1((M_1 + M_2)/2) without requiring knowledge of the
   (possibly heteroscedastic) noise variances.
"""

from __future__ import annotations

import json
import math
import random
from typing import List, Tuple


def mat_vec(A: List[List[float]], x: List[float]) -> List[float]:
    return [sum(r[j] * x[j] for j in range(len(x))) for r in A]


def dot(u: List[float], v: List[float]) -> float:
    return sum(a * b for a, b in zip(u, v))


def norm2(u: List[float]) -> float:
    return math.sqrt(dot(u, u))


def leading_real_eigenpair_power(A: List[List[float]], steps: int = 200) -> Tuple[float, List[float]]:
    n = len(A)
    v = [1.0 / math.sqrt(n)] * n
    lam = 1.0
    for _ in range(steps):
        Av = mat_vec(A, v)
        lam = dot(v, Av)
        nv = norm2(Av)
        if nv < 1e-15:
            break
        s = 1.0 if lam >= 0.0 else -1.0
        v = [s * c / nv for c in Av]
    Av = mat_vec(A, v)
    lam = dot(v, Av)
    return lam, v


def leading_singular_value_power(A: List[List[float]], steps: int = 200) -> float:
    n = len(A)
    AT = [[A[i][j] for i in range(n)] for j in range(n)]
    v = [1.0 / math.sqrt(n)] * n
    for _ in range(steps):
        Av = mat_vec(A, v)
        ATAv = mat_vec(AT, Av)
        nv = norm2(ATAv)
        v = [c / nv for c in ATAv]
    Av = mat_vec(A, v)
    return norm2(Av)


def main() -> None:
    rng = random.Random(20261019)
    n = 64
    lam_star = 1.0
    # Incoherent unit vector u^* with mu = 1
    u_star = [1.0 / math.sqrt(n) if i % 2 == 0 else -1.0 / math.sqrt(n) for i in range(n)]
    M_star = [[lam_star * u_star[i] * u_star[j] for j in range(n)] for i in range(n)]

    # 1. Verify exact Neumann trick identity (Theorem 2, Eq. 11) on a deterministic realization
    sigma = 0.045
    H_det = [[rng.gauss(0.0, sigma) for _ in range(n)] for _ in range(n)]
    M_det = [[M_star[i][j] + H_det[i][j] for j in range(n)] for i in range(n)]
    lam_det, u_det = leading_real_eigenpair_power(M_det, steps=250)
    if dot(u_det, u_star) < 0:
        u_det = [-c for c in u_det]

    # Compute truncated Neumann series (s = 0..25)
    coeff = (lam_star / lam_det) * dot(u_star, u_det)
    neumann_sum = [0.0] * n
    term = u_star[:]
    for s in range(25):
        for i in range(n):
            neumann_sum[i] += coeff * term[i]
        # Next term = (1 / lam_det) H * term
        H_term = mat_vec(H_det, term)
        term = [c / lam_det for c in H_term]

    neumann_max_err = max(abs(u_det[i] - neumann_sum[i]) for i in range(n))
    assert neumann_max_err < 1e-10, f"Neumann trick identity failed: {neumann_max_err}"

    # 2. Monte Carlo comparison of Asymmetric Eigenvalue vs Symmetric Eigenvalue vs Singular Value
    # under heteroscedastic independent noise (Section 4.1.2 & Section 4.3)
    trials = 40
    asym_eig_errs = []
    sym_eig_errs = []
    svd_errs = []
    asym_quad_H2 = []
    sym_quad_H2 = []
    linf_vec_errs = []

    for _ in range(trials):
        # Heteroscedastic zero-mean noise with location-varying variance sigma_{ij}^2
        H_asym = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                s_ij = sigma * (0.6 + 0.8 * ((i + 2 * j) % 5) / 4.0)
                H_asym[i][j] = rng.gauss(0.0, s_ij)
        # Symmetrized noise with same entrywise variance on upper triangle
        H_sym = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                s_ij = sigma * (0.6 + 0.8 * ((i + 2 * j) % 5) / 4.0)
                val = rng.gauss(0.0, s_ij)
                H_sym[i][j] = val
                H_sym[j][i] = val

        # Quadratic forms (u^*)^T H^2 u^*
        Hu_asym = mat_vec(H_asym, u_star)
        H2u_asym = mat_vec(H_asym, Hu_asym)
        asym_quad_H2.append(dot(u_star, H2u_asym))

        Hu_sym = mat_vec(H_sym, u_star)
        avail_sym = dot(Hu_sym, Hu_sym)
        sym_quad_H2.append(avail_sym)

        M_asym = [[M_star[i][j] + H_asym[i][j] for j in range(n)] for i in range(n)]
        M_sym = [[M_star[i][j] + H_sym[i][j] for j in range(n)] for i in range(n)]

        lam_a, u_a = leading_real_eigenpair_power(M_asym, steps=160)
        if dot(u_a, u_star) < 0:
            u_a = [-c for c in u_a]
        lam_s, _ = leading_real_eigenpair_power(M_sym, steps=160)
        sig_a = leading_singular_value_power(M_asym, steps=160)

        asym_eig_errs.append(abs(lam_a - lam_star))
        sym_eig_errs.append(abs(lam_s - lam_star))
        svd_errs.append(abs(sig_a - lam_star))
        linf_vec_errs.append(max(abs(u_a[i] - u_star[i]) for i in range(n)))

    mean_asym_eig_err = sum(asym_eig_errs) / trials
    mean_sym_eig_err = sum(sym_eig_errs) / trials
    mean_svd_err = sum(svd_errs) / trials
    mean_asym_H2 = sum(asym_quad_H2) / trials
    mean_sym_H2 = sum(sym_quad_H2) / trials
    mean_linf_err = sum(linf_vec_errs) / trials

    # Verify O(sqrt(n)) accuracy gain of asymmetric eigenvalue over SVD and symmetrized eigenvalue
    assert abs(mean_asym_H2) < 0.12 * mean_sym_H2, (
        f"Asymmetric quadratic form E[u*^T H^2 u*] failed to cancel bias: {mean_asym_H2} vs {mean_sym_H2}"
    )
    assert mean_asym_eig_err < 0.35 * mean_svd_err, (
        f"Asymmetric leading eigenvalue did not beat vanilla SVD: {mean_asym_eig_err} vs {mean_svd_err}"
    )
    assert mean_asym_eig_err < 0.45 * mean_sym_eig_err, (
        f"Asymmetric leading eigenvalue did not beat symmetrized eigenvalue: {mean_asym_eig_err} vs {mean_sym_eig_err}"
    )

    # 3. Verify Asymmetrized Dilation Matrix (Section 5.2, Eq. 43, Corollary 8)
    # Two independent noisy copies M_1, M_2 embedded in M_d = [[0, M_1], [M_2^T, 0]]
    H1 = [[rng.gauss(0.0, sigma) for _ in range(n)] for _ in range(n)]
    H2 = [[rng.gauss(0.0, sigma) for _ in range(n)] for _ in range(n)]
    M1 = [[M_star[i][j] + H1[i][j] for j in range(n)] for i in range(n)]
    M2 = [[M_star[i][j] + H2[i][j] for j in range(n)] for i in range(n)]
    # Equivalence: (M_d)^2 has top-left block M_1 M_2^T whose leading eigenvalue is (lambda_1(M_d))^2
    M1_M2T = [[sum(M1[i][k] * M2[j][k] for k in range(n)) for j in range(n)] for i in range(n)]
    lam_sq_dilation, _ = leading_real_eigenpair_power(M1_M2T, steps=180)
    lam_dilation = math.sqrt(max(0.0, lam_sq_dilation))
    M_avg = [[0.5 * (M1[i][j] + M2[i][j]) for j in range(n)] for i in range(n)]
    sig_avg = leading_singular_value_power(M_avg, steps=180)

    dilation_err = abs(lam_dilation - lam_star)
    svd_avg_err = abs(sig_avg - lam_star)
    assert dilation_err < svd_avg_err, f"Asymmetrized dilation error {dilation_err} >= SVD error {svd_avg_err}"

    summary = {
        "n": n,
        "lambda_star": lam_star,
        "sigma_base": sigma,
        "neumann_series_identity_max_err": neumann_max_err,
        "mean_u_star_H2_u_star_asymmetric": round(mean_asym_H2, 6),
        "mean_u_star_H2_u_star_symmetric": round(mean_sym_H2, 6),
        "mean_asym_eigenvalue_err": round(mean_asym_eig_err, 6),
        "mean_sym_eigenvalue_err": round(mean_sym_eig_err, 6),
        "mean_vanilla_svd_err": round(mean_svd_err, 6),
        "mean_entrywise_eigenvector_linf_err": round(mean_linf_err, 6),
        "asymmetrized_dilation_singular_value_err": round(dilation_err, 6),
        "averaged_svd_singular_value_err": round(svd_avg_err, 6),
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
