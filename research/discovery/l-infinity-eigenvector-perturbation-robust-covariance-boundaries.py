#!/usr/bin/env python3
"""Constructed boundary and mechanism verification for Round 279:
L-Infinity Eigenvector Perturbation Bound and Robust Factor Covariance Estimation
(Fan, Wang, & Zhong 2018, JMLR 18(207):1-42; arXiv:1603.03516v2).
"""

import json
import math
import random


def vec_dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def vec_norm2(u):
    return math.sqrt(vec_dot(u, u))


def vec_norm_inf(u):
    return max(abs(x) for x in u)


def mat_vec(A, x):
    return [vec_dot(row, x) for row in A]


def mat_mul(A, B):
    m = len(A)
    k = len(B)
    n = len(B[0])
    BT = [[B[r][c] for r in range(k)] for c in range(n)]
    return [[vec_dot(A[i], BT[j]) for j in range(n)] for i in range(m)]


def mat_norm_inf(E):
    """Matrix l_infinity operator norm: max_i sum_j |E_{ij}|."""
    return max(sum(abs(x) for x in row) for row in E)


def top_k_symmetric_eigen(A, k, max_iter=400, tol=1e-13):
    """Orthogonal iteration (simultaneous power iteration with Modified Gram-Schmidt) for top k eigenpairs."""
    d = len(A)
    # Deterministic initialization
    Q = [[0.0] * k for _ in range(d)]
    for j in range(k):
        for i in range(d):
            Q[i][j] = math.cos((i + 0.5) * (j + 1) * math.pi / d) + (0.1 if i == j else 0.0)
    # Orthonormalize columns of Q
    def orthonormalize(M):
        cols = [[M[i][j] for i in range(d)] for j in range(k)]
        for j in range(k):
            for r in range(j):
                proj = vec_dot(cols[j], cols[r])
                cols[j] = [cols[j][i] - proj * cols[r][i] for i in range(d)]
            nrm = vec_norm2(cols[j])
            cols[j] = [cols[j][i] / nrm for i in range(d)]
        return [[cols[j][i] for j in range(k)] for i in range(d)]

    Q = orthonormalize(Q)
    for _ in range(max_iter):
        Z = mat_mul(A, Q)
        Q_new = orthonormalize(Z)
        for j in range(k):
            if sum(Q[i][j] * Q_new[i][j] for i in range(d)) < 0:
                for i in range(d):
                    Q_new[i][j] = -Q_new[i][j]
        diff = max(abs(Q[i][j] - Q_new[i][j]) for i in range(d) for j in range(k))
        Q = Q_new
        if diff < tol:
            break

    cols = [[Q[i][j] for i in range(d)] for j in range(k)]
    evals = [vec_dot(cols[j], mat_vec(A, cols[j])) for j in range(k)]
    return evals, cols


def verify_l_infinity_vs_davis_kahan_delocalization():
    """Verify Theorem 1 / Theorem 2.1: l_infinity perturbation bound improves on Davis-Kahan l_2 by 1/sqrt(d) for incoherent V."""
    d = 36
    r = 2
    # Construct exact delocalized orthonormal columns via DCT-II basis
    v1 = [math.sqrt(2.0 / d) * math.cos((i + 0.5) * math.pi / d) for i in range(d)]
    v2 = [math.sqrt(2.0 / d) * math.cos(2.0 * (i + 0.5) * math.pi / d) for i in range(d)]
    lam1 = 18.0
    lam2 = 12.0
    gamma0 = lam2  # gap to zero bulk is 12.0, gap between lam1 and lam2 is 6.0

    # Coherence mu(V) = (d / r) max_i sum_{k=1}^r V_{ik}^2
    mu_V = (d / r) * max(v1[i] ** 2 + v2[i] ** 2 for i in range(d))
    assert mu_V <= 2.0 + 1e-12

    A = [
        [lam1 * v1[i] * v1[j] + lam2 * v2[i] * v2[j] for j in range(d)]
        for i in range(d)
    ]

    rng = random.Random(20261019)
    E = [[0.0] * d for _ in range(d)]
    for i in range(d):
        for j in range(i + 1, d):
            val = 0.035 * (1.0 if rng.random() < 0.5 else -1.0)
            E[i][j] = val
            E[j][i] = val

    E_inf = mat_norm_inf(E)
    A_tilde = [[A[i][j] + E[i][j] for j in range(d)] for i in range(d)]
    evals_tilde, cols_tilde = top_k_symmetric_eigen(A_tilde, r)

    # Align signs with v1, v2
    u1_tilde = cols_tilde[0]
    if vec_dot(u1_tilde, v1) < 0:
        u1_tilde = [-x for x in u1_tilde]
    u2_tilde = cols_tilde[1]
    if vec_dot(u2_tilde, v2) < 0:
        u2_tilde = [-x for x in u2_tilde]

    diff1 = [u1_tilde[i] - v1[i] for i in range(d)]
    diff2 = [u2_tilde[i] - v2[i] for i in range(d)]
    err1_inf = vec_norm_inf(diff1)
    err1_l2 = vec_norm2(diff1)
    err2_inf = vec_norm_inf(diff2)
    err2_l2 = vec_norm2(diff2)

    # Delocalization ratio: sqrt(d) * ||u_tilde - v||_inf / ||u_tilde - v||_2 is O(1)
    deloc_ratio_1 = math.sqrt(d) * err1_inf / err1_l2
    deloc_ratio_2 = math.sqrt(d) * err2_inf / err2_l2
    assert err1_inf < err1_l2 / (0.33 * math.sqrt(d))
    assert deloc_ratio_1 < 3.0
    assert deloc_ratio_2 < 3.0

    # Contrast with coherent (localized) rank-1 matrix A_loc = lam1 * e_1 e_1^T (mu = d)
    # Perturb entry (0, 1) and (1, 0) by eps_loc = 0.8
    A_loc = [[0.0] * d for _ in range(d)]
    A_loc[0][0] = lam1
    A_loc_tilde = [row[:] for row in A_loc]
    A_loc_tilde[0][1] = 0.8
    A_loc_tilde[1][0] = 0.8
    _, cols_loc = top_k_symmetric_eigen(A_loc_tilde, 1)
    u_loc = cols_loc[0]
    if u_loc[0] < 0:
        u_loc = [-x for x in u_loc]
    diff_loc = [u_loc[0] - 1.0] + u_loc[1:]
    err_loc_inf = vec_norm_inf(diff_loc)
    err_loc_l2 = vec_norm2(diff_loc)
    # For localized perturbation, l_inf error is almost equal to l_2 error (no 1/sqrt(d) gain!)
    assert err_loc_inf > 0.95 * err_loc_l2

    return {
        "d": d,
        "r": r,
        "coherence_mu_V": round(mu_V, 6),
        "matrix_E_norm_inf": round(E_inf, 6),
        "v1_err_inf": round(err1_inf, 6),
        "v1_err_l2": round(err1_l2, 6),
        "v1_sqrt_d_inf_over_l2": round(deloc_ratio_1, 6),
        "v2_err_inf": round(err2_inf, 6),
        "v2_err_l2": round(err2_l2, 6),
        "localized_err_inf_over_l2": round(err_loc_inf / err_loc_l2, 6),
    }


def verify_neumann_series_and_schur_complement_expansion():
    """Verify Section 5.1 Lemma 5.1 & 5.2 exact Schur-complement / Neumann expansion for x^* = u_tilde / (u^T u_tilde) - u."""
    d = 20
    u = [1.0 / math.sqrt(d) if i % 2 == 0 else -1.0 / math.sqrt(d) for i in range(d)]
    lam = 15.0
    A = [[lam * u[i] * u[j] for j in range(d)] for i in range(d)]

    rng = random.Random(20261020)
    E = [[0.0] * d for _ in range(d)]
    for i in range(d):
        for j in range(i + 1, d):
            val = 0.04 * rng.uniform(-1.0, 1.0)
            E[i][j] = val
            E[j][i] = val

    A_tilde = [[A[i][j] + E[i][j] for j in range(d)] for i in range(d)]
    evals, cols = top_k_symmetric_eigen(A_tilde, 1, max_iter=600, tol=1e-15)
    lam_tilde = evals[0]
    u_tilde_unit = cols[0]
    if vec_dot(u_tilde_unit, u) < 0:
        u_tilde_unit = [-x for x in u_tilde_unit]

    # Normalize u_tilde so u^T u_tilde = 1 => u_tilde = u + x^* with x^* orthogonal to u (Section 5.1 p. 25)
    scale = vec_dot(u, u_tilde_unit)
    u_tilde = [x / scale for x in u_tilde_unit]
    x_star = [u_tilde[i] - u[i] for i in range(d)]
    assert abs(vec_dot(u, x_star)) < 1e-13

    # Projection Q = I - u u^T
    def proj_Q(v):
        dot_uv = vec_dot(u, v)
        return [v[i] - dot_uv * u[i] for i in range(d)]

    # Check exact secular identity: lam_tilde = lam + u^T E u + u^T E x^*
    Eu = mat_vec(E, u)
    Ex_star = mat_vec(E, x_star)
    secular_rhs = lam + vec_dot(u, Eu) + vec_dot(u, Ex_star)
    secular_err = abs(lam_tilde - secular_rhs)
    assert secular_err < 1e-12

    # Neumann expansion: x_neumann = sum_{k=0}^{12} lam_tilde^{-(k+1)} (Q E Q)^k Q E u
    term = [x / lam_tilde for x in proj_Q(Eu)]
    x_neumann = term[:]
    for _ in range(1, 14):
        term = [x / lam_tilde for x in proj_Q(mat_vec(E, term))]
        x_neumann = [x_neumann[i] + term[i] for i in range(d)]

    neumann_err_inf = vec_norm_inf([x_star[i] - x_neumann[i] for i in range(d)])
    assert neumann_err_inf < 1e-12

    return {
        "d": d,
        "lam": lam,
        "lam_tilde": round(lam_tilde, 8),
        "secular_equation_abs_err": secular_err,
        "x_star_norm_inf": round(vec_norm_inf(x_star), 8),
        "neumann_expansion_err_inf": neumann_err_inf,
    }


def catoni_m_estimator_mean(samples, alpha):
    """Solve sum_{i=1}^n psi(alpha * (X_i - mu)) = 0 where psi(x) = sgn(x) * log(1 + |x| + x^2 / 2)."""
    def psi(x):
        ax = abs(x)
        val = math.log(1.0 + ax + 0.5 * ax * ax)
        return val if x >= 0 else -val

    lo = min(samples)
    hi = max(samples)
    if lo == hi:
        return lo
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        s = sum(psi(alpha * (x - mid)) for x in samples)
        if s > 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def verify_robust_factor_covariance_catoni_and_kendall():
    """Verify Section 3 (Catoni robust factor covariance) and Section 4 (spatial Kendall's tau eigenvectors) under heavy tails."""
    rng = random.Random(20261021)
    n = 140
    d = 18
    r = 2

    # True delocalized factor loading directions V (d x 2)
    v1 = [math.sqrt(2.0 / d) * math.cos((j + 0.5) * math.pi / d) for j in range(d)]
    v2 = [math.sqrt(2.0 / d) * math.cos(2.0 * (j + 0.5) * math.pi / d) for j in range(d)]
    lam1 = 14.0
    lam2 = 8.0
    sigma_eps_sq = 0.5

    # True covariance Sigma = lam1 v1 v1^T + lam2 v2 v2^T + sigma_eps_sq I_d
    Sigma_true = [
        [
            lam1 * v1[j] * v1[k] + lam2 * v2[j] * v2[k] + (sigma_eps_sq if j == k else 0.0)
            for k in range(d)
        ]
        for j in range(d)
    ]

    # Helper to draw unit-variance heavy-tailed idiosyncratic noise
    def draw_heavy_tail():
        if rng.random() < 0.98:
            return rng.gauss(0.0, math.sqrt(0.20 / 0.98))
        return rng.gauss(0.0, math.sqrt(0.80 / 0.02))

    Y = []
    for _ in range(n):
        f1 = math.sqrt(lam1) * rng.gauss(0.0, 1.0)
        f2 = math.sqrt(lam2) * rng.gauss(0.0, 1.0)
        row = [
            f1 * v1[j] + f2 * v2[j] + math.sqrt(sigma_eps_sq) * draw_heavy_tail()
            for j in range(d)
        ]
        Y.append(row)

    # Sample covariance matrix
    Sigma_samp = [
        [sum(Y[i][j] * Y[i][k] for i in range(n)) / n for k in range(d)]
        for j in range(d)
    ]

    # Catoni M-estimator entrywise (Section 3.1 Eq. 3.3)
    alpha_catoni = 0.035
    Sigma_catoni = [[0.0] * d for _ in range(d)]
    for j in range(d):
        for k in range(j, d):
            prods = [Y[i][j] * Y[i][k] for i in range(n)]
            est = catoni_m_estimator_mean(prods, alpha_catoni)
            Sigma_catoni[j][k] = est
            Sigma_catoni[k][j] = est

    max_err_samp = max(
        abs(Sigma_samp[j][k] - Sigma_true[j][k]) for j in range(d) for k in range(d)
    )
    max_err_catoni = max(
        abs(Sigma_catoni[j][k] - Sigma_true[j][k]) for j in range(d) for k in range(d)
    )
    assert max_err_catoni < max_err_samp

    # Spatial Kendall's tau matrix Sigma_tilde^K (Section 4.1 Eq. 4.2)
    Sigma_kendall = [[0.0] * d for _ in range(d)]
    pair_count = 0
    for i in range(n):
        for ip in range(i + 1, n):
            diff = [Y[i][j] - Y[ip][j] for j in range(d)]
            sq_norm = vec_dot(diff, diff)
            if sq_norm > 1e-14:
                inv_sq = 1.0 / sq_norm
                for j in range(d):
                    dj = diff[j] * inv_sq
                    for k in range(j, d):
                        Sigma_kendall[j][k] += dj * diff[k]
                pair_count += 1
    for j in range(d):
        for k in range(j, d):
            val = Sigma_kendall[j][k] / pair_count
            Sigma_kendall[j][k] = val
            Sigma_kendall[k][j] = val

    trace_kendall = sum(Sigma_kendall[j][j] for j in range(d))
    assert abs(trace_kendall - 1.0) < 1e-12

    # Compare leading eigenvector l_infinity errors of Sample, Catoni, and Spatial Kendall's tau
    _, cols_samp = top_k_symmetric_eigen(Sigma_samp, r)
    _, cols_catoni = top_k_symmetric_eigen(Sigma_catoni, r)
    _, cols_kendall = top_k_symmetric_eigen(Sigma_kendall, r)

    def aligned_inf_err(u_est, u_true):
        if vec_dot(u_est, u_true) < 0:
            u_est = [-x for x in u_est]
        return vec_norm_inf([u_est[j] - u_true[j] for j in range(d)])

    v1_err_samp = aligned_inf_err(cols_samp[0], v1)
    v1_err_catoni = aligned_inf_err(cols_catoni[0], v1)
    v1_err_kendall = aligned_inf_err(cols_kendall[0], v1)

    assert v1_err_catoni < v1_err_samp
    assert v1_err_kendall < v1_err_samp

    return {
        "n": n,
        "d": d,
        "max_entrywise_err_sample": round(max_err_samp, 6),
        "max_entrywise_err_catoni": round(max_err_catoni, 6),
        "trace_spatial_kendall": round(trace_kendall, 8),
        "v1_inf_err_sample": round(v1_err_samp, 6),
        "v1_inf_err_catoni": round(v1_err_catoni, 6),
        "v1_inf_err_kendall": round(v1_err_kendall, 6),
    }


def main():
    res1 = verify_l_infinity_vs_davis_kahan_delocalization()
    res2 = verify_neumann_series_and_schur_complement_expansion()
    res3 = verify_robust_factor_covariance_catoni_and_kendall()
    report = {
        "concept": "LInfinityEigenvectorPerturbationBoundAndRobustFactorCovarianceEstimation",
        "primary_source": "Fan, Wang, & Zhong (2018), JMLR 18(207):1-42 (arXiv:1603.03516v2)",
        "checks": {
            "l_infinity_vs_davis_kahan_delocalization": res1,
            "neumann_series_and_schur_complement": res2,
            "robust_factor_covariance_catoni_and_kendall": res3,
        },
        "all_passed": True,
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
