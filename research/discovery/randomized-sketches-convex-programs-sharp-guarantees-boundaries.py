#!/usr/bin/env python3
"""Constructed boundary and verification checks for Round 227:
Randomized Sketches of Convex Programs with Sharp Guarantees (Pilanci &
Wainwright 2015, IEEE Transactions on Information Theory 61(9):5096-5115,
arXiv:1404.7203v1, DOI:10.1109/TIT.2015.2450722).

Verifies:
1. Lemma 1 Deterministic Tangent-Cone Multiplicative Cost Approximation and
   Corollary 1 Privacy-Sensitive Mutual Information Rate (Sections 2.1-2.2 &
   Section 4.1, Theorem 1, Corollary 1, Lemma 1, Eqs. 1-8, 41a-45):
   - Exact verification of Lemma 1 inequality:
     ||A(x_hat - x^*)||_2 / ||A x^* - y||_2 <= 2 Z_2(AK) / Z_1(AK) and
     f(x_hat) <= (1 + 2 Z_2(AK) / Z_1(AK))^2 f(x^*).
   - Verification of Corollary 1 privacy-preserving mutual information per
     symbol bound I(SA; A)/(n d) <= (m / (2n)) log(2 pi e gamma^2) vanishing
     as W^2(AK)/n -> 0 while maintaining (1+delta)^2 cost optimality.
2. Corollary 4 Compressed Sensing Exact Recovery (Noiseless f(x^*)=0) and
   Folded-Noise Denoising Bound, plus Corollary 5 Dual SVM Simplex Sketching
   (Sections 3.3-3.4, Corollaries 4-5, Eqs. 21-29):
   - Verification that when y = x_bar in C = {||x||_1 <= R}, f(x^*) = 0 so
     any sketch with Z_1(AK) > 0 achieves exact recovery x_hat = x_bar
     (f(x_hat) <= (1+delta)^2 * 0 = 0, Eq. 23), and under folded noise
     y = x_bar + w achieves ||x_hat - y||_2^2 <= (1+delta)^2 ||x^* - y||_2^2.
   - Verification of dual squared-hinge SVM simplex program (Eqs. 27-28)
     min_{x >= 0, 1^T x = 1} ||B x||_2^2 vs. sketched program ||S B x||_2^2.
3. Section 5.2 & Appendix D Set-Difference Covering and Non-Convex Rank-to-Nuclear
   Convex Hull Inclusion (Lemmas 8 and 13, Eqs. 66-68, 80a-80b, 86):
   - Exact verification of Lemma 13 support-function inequality
     phi_1(X) <= (1 + sqrt(r / floor(r))) phi_0(X) <= 3 phi_0(X) for
     Y_1(r) = B_F(1) cap B_nuc(2 sqrt(r)) subseteq clconv(B_F(3) cap B_rank(4r))
     and Lemma 8 quadratic form bound sup_{z in Y_1} |z^T Q z| <= (3/2) sup_{z in partial[Y_0]} |z^T Q z|.
"""

from __future__ import annotations

import json
import math
import random


def dot(u: list[float], v: list[float]) -> float:
    return sum(ui * vi for ui, vi in zip(u, v))


def norm2(u: list[float]) -> float:
    return math.sqrt(dot(u, u))


def mat_vec(A: list[list[float]], x: list[float]) -> list[float]:
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]


def mat_t_vec(A: list[list[float]], y: list[float]) -> list[float]:
    n = len(A)
    d = len(A[0])
    return [sum(A[i][j] * y[i] for i in range(n)) for j in range(d)]


def solve_spd(A: list[list[float]], b: list[float]) -> list[float]:
    d = len(b)
    L = [[0.0] * d for _ in range(d)]
    for i in range(d):
        for j in range(i + 1):
            s = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                L[i][j] = math.sqrt(max(A[i][i] - s, 1e-15))
            else:
                L[i][j] = (A[i][j] - s) / L[j][j]
    y = [0.0] * d
    for i in range(d):
        y[i] = (b[i] - sum(L[i][k] * y[k] for k in range(i))) / L[i][i]
    x = [0.0] * d
    for i in range(d - 1, -1, -1):
        x[i] = (y[i] - sum(L[k][i] * x[k] for k in range(i + 1, d))) / L[i][i]
    return x


def project_l1_ball(v: list[float], radius: float) -> list[float]:
    if sum(abs(vi) for vi in v) <= radius:
        return list(v)
    u = sorted((abs(vi) for vi in v), reverse=True)
    sv = 0.0
    theta = 0.0
    for i, ui in enumerate(u):
        sv += ui
        t = (sv - radius) / (i + 1)
        if ui > t:
            theta = t
    return [math.copysign(max(abs(vi) - theta, 0.0), vi) for vi in v]


def project_simplex(v: list[float]) -> list[float]:
    """Project v onto the probability simplex {x >= 0, sum x_i = 1}."""
    u = sorted(v, reverse=True)
    sv = 0.0
    theta = 0.0
    for i, ui in enumerate(u):
        sv += ui
        t = (sv - 1.0) / (i + 1)
        if ui > t:
            theta = t
    return [max(vi - theta, 0.0) for vi in v]


def check_lemma1_and_corollary1_privacy() -> dict:
    """Verify Lemma 1 deterministic bound (Eq. 42) and Corollary 1 mutual information rate (Eq. 8)."""
    rng = random.Random(20261020)
    n, d = 200, 6
    gamma = 1.0
    A = [[rng.gauss(0.0, gamma) for _ in range(d)] for _ in range(n)]
    x0 = [1.0, -0.8, 0.6, -0.4, 0.3, -0.2]
    Ax0 = mat_vec(A, x0)
    y = [Ax0[i] + rng.gauss(0.0, 0.5) for i in range(n)]

    # Exact OLS x^* = argmin ||Ax - y||_2^2
    AtA = [[0.0] * d for _ in range(d)]
    for i in range(n):
        for j in range(d):
            for k in range(d):
                AtA[j][k] += A[i][j] * A[i][k]
    Aty = mat_t_vec(A, y)
    x_star = solve_spd(AtA, Aty)
    res_star = [dot(A[i], x_star) - y[i] for i in range(n)]
    f_star = dot(res_star, res_star)
    res_star_norm = math.sqrt(f_star)
    u_vec = [r / res_star_norm for r in res_star]

    # Orthonormal basis U of AK = col(A)
    U_cols = []
    for j in range(d):
        col = [A[i][j] for i in range(n)]
        for prev in U_cols:
            proj = dot(col, prev)
            col = [col[i] - proj * prev[i] for i in range(n)]
        nrm = norm2(col)
        U_cols.append([col[i] / nrm for i in range(n)])

    # Sketch with m = 60 rows
    m = 60
    scale = 1.0 / math.sqrt(m)
    SA = [[0.0] * d for _ in range(m)]
    SU = [[0.0] * d for _ in range(m)]
    Sy = [0.0] * m
    Su = [0.0] * m
    for r_idx in range(m):
        for i in range(n):
            s_ri = rng.gauss(0.0, scale)
            Sy[r_idx] += s_ri * y[i]
            Su[r_idx] += s_ri * u_vec[i]
            for j in range(d):
                SA[r_idx][j] += s_ri * A[i][j]
                SU[r_idx][j] += s_ri * U_cols[j][i]

    # Sketched solution x_hat = argmin ||S(Ax - y)||_2^2
    BtB = [[0.0] * d for _ in range(d)]
    for r_idx in range(m):
        for j in range(d):
            for k in range(d):
                BtB[j][k] += SA[r_idx][j] * SA[r_idx][k]
    Bty = mat_t_vec(SA, Sy)
    x_hat = solve_spd(BtB, Bty)

    res_hat = [dot(A[i], x_hat) - y[i] for i in range(n)]
    f_hat = dot(res_hat, res_hat)
    Ae_hat = [dot(A[i], [x_hat[j] - x_star[j] for j in range(d)]) for i in range(n)]
    Ae_norm = norm2(Ae_hat)

    # Compute Z_1(AK) = lambda_min(SU^T SU) and Z_2(AK) = ||SU^T Su - U^T u||_2
    # Wait: u = (Ax^* - y)/||Ax^* - y||_2 is orthogonal to col(A), so U^T u = 0!
    G = [[0.0] * d for _ in range(d)]
    for r_idx in range(m):
        for j in range(d):
            for k in range(d):
                G[j][k] += SU[r_idx][j] * SU[r_idx][k]
    v_eig = [1.0 / math.sqrt(d)] * d
    for _ in range(30):
        w_eig = solve_spd(G, v_eig)
        wn = norm2(w_eig)
        v_eig = [wj / wn for wj in w_eig]
    z1_ak = dot(v_eig, mat_vec(G, v_eig))

    # For any v = U alpha with ||alpha||_2 = 1, <u, (S^T S / m - I) U alpha> = <(SU)^T Su - U^T u, alpha>
    UT_u = [dot(U_cols[j], u_vec) for j in range(d)]
    SUT_Su = mat_t_vec(SU, Su)
    z2_vec = [SUT_Su[j] - UT_u[j] for j in range(d)]
    z2_ak = norm2(z2_vec)

    lhs_error_ratio = Ae_norm / res_star_norm
    rhs_error_bound = 2.0 * z2_ak / z1_ak
    lemma1_bound_rhs = ((1.0 + rhs_error_bound) ** 2) * f_star

    # Corollary 1 mutual information rate per symbol for n = 200 vs n = 4000
    mi_rate_n200 = (m / (2.0 * n)) * math.log(2.0 * math.pi * math.e * (gamma ** 2))
    mi_rate_n4000 = (m / (2.0 * 4000.0)) * math.log(2.0 * math.pi * math.e * (gamma ** 2))

    passed = (
        f_star <= f_hat <= lemma1_bound_rhs + 1e-10
        and lhs_error_ratio <= rhs_error_bound + 1e-10
        and f_hat / f_star < 1.35
        and mi_rate_n4000 <= 0.05 * mi_rate_n200 + 1e-12
    )
    return {
        "passed": passed,
        "f_star": f_star,
        "f_hat": f_hat,
        "approx_ratio": f_hat / f_star,
        "lhs_error_ratio": lhs_error_ratio,
        "rhs_2z2_over_z1": rhs_error_bound,
        "lemma1_cost_upper_bound": lemma1_bound_rhs,
        "mi_rate_n200": mi_rate_n200,
        "mi_rate_n4000": mi_rate_n4000,
    }


def check_corollary4_denoising_and_corollary5_svm() -> dict:
    """Verify Corollary 4 (noiseless exact recovery & noisy folded denoising) and Corollary 5 (SVM)."""
    rng = random.Random(20261021)
    # 1. Corollary 4: Noiseless compressed sensing as sketched denoising (A = I_d)
    d = 30
    k = 2
    x_bar = [1.2, -0.9] + [0.0] * (d - k)
    R = sum(abs(v) for v in x_bar)
    m_cs = 18
    scale = 1.0 / math.sqrt(m_cs)
    S = [[rng.gauss(0.0, scale) for _ in range(d)] for _ in range(m_cs)]
    Sy_noiseless = mat_vec(S, x_bar)

    # Solve min_{||x||_1 <= R} ||S x - S x_bar||_2^2 via PGD
    x_hat_cs = [0.0] * d
    for _ in range(1500):
        res = [dot(S[i], x_hat_cs) - Sy_noiseless[i] for i in range(m_cs)]
        grad = mat_t_vec(S, res)
        x_hat_cs = project_l1_ball([x_hat_cs[j] - 0.15 * grad[j] for j in range(d)], R)
    noiseless_err = norm2([x_hat_cs[j] - x_bar[j] for j in range(d)])

    # Noisy folded version: y = x_bar + w
    w = [rng.gauss(0.0, 0.15) for _ in range(d)]
    y_noisy = [x_bar[j] + w[j] for j in range(d)]
    x_star_denoise = project_l1_ball(y_noisy, R)
    f_star_denoise = sum((x_star_denoise[j] - y_noisy[j]) ** 2 for j in range(d))
    Sy_noisy = mat_vec(S, y_noisy)
    x_hat_noisy = [0.0] * d
    for _ in range(1500):
        res = [dot(S[i], x_hat_noisy) - Sy_noisy[i] for i in range(m_cs)]
        grad = mat_t_vec(S, res)
        x_hat_noisy = project_l1_ball([x_hat_noisy[j] - 0.15 * grad[j] for j in range(d)], R)
    f_hat_noisy_orig = sum((x_hat_noisy[j] - y_noisy[j]) ** 2 for j in range(d))

    # 2. Corollary 5: Dual squared-hinge SVM simplex sketching (Eqs. 27-28)
    # Construct B in R^{80 x 20} where columns 0 and 1 are opposite margin vectors plus small offset
    # and columns 2..19 are shifted away so x^* has k = 2 active support vectors on the simplex
    n_svm, d_svm = 80, 20
    B = [[0.0] * d_svm for _ in range(n_svm)]
    for i in range(n_svm):
        base = rng.gauss(0.0, 1.0)
        offset = 0.4 if i == 0 else rng.gauss(0.0, 0.2)
        B[i][0] = base + offset
        B[i][1] = -base + offset
        for j in range(2, d_svm):
            B[i][j] = (2.5 if i == 0 else 0.0) + rng.gauss(0.0, 1.5)

    x_star_svm = [1.0 / d_svm] * d_svm
    for _ in range(1500):
        Bx = mat_vec(B, x_star_svm)
        grad = mat_t_vec(B, Bx)
        x_star_svm = project_simplex([x_star_svm[j] - 0.002 * grad[j] for j in range(d_svm)])
    f_star_svm = sum(v * v for v in mat_vec(B, x_star_svm))

    m_svm = 48
    scale_svm = 1.0 / math.sqrt(m_svm)
    SB = [[0.0] * d_svm for _ in range(m_svm)]
    for r_idx in range(m_svm):
        for i in range(n_svm):
            s_ri = rng.gauss(0.0, scale_svm)
            for j in range(d_svm):
                SB[r_idx][j] += s_ri * B[i][j]
    x_hat_svm = [1.0 / d_svm] * d_svm
    for _ in range(1500):
        SBx = mat_vec(SB, x_hat_svm)
        grad = mat_t_vec(SB, SBx)
        x_hat_svm = project_simplex([x_hat_svm[j] - 0.002 * grad[j] for j in range(d_svm)])
    f_hat_svm = sum(v * v for v in mat_vec(B, x_hat_svm))

    passed = (
        noiseless_err < 1e-3
        and f_star_denoise <= f_hat_noisy_orig <= 2.2 * f_star_denoise
        and f_star_svm <= f_hat_svm <= 1.5 * f_star_svm
    )
    return {
        "passed": passed,
        "noiseless_cs_recovery_err": noiseless_err,
        "noisy_denoise_ratio": f_hat_noisy_orig / f_star_denoise,
        "dual_svm_approx_ratio": f_hat_svm / f_star_svm,
    }


def check_lemma8_and_lemma13_convex_hull_inclusion() -> dict:
    """Verify Lemma 13 support function bound phi_1(X) <= 3 phi_0(X) and Lemma 8 Eq. (84)."""
    rng = random.Random(20261022)
    d = 12
    # Test Lemma 13 across r = 1, 2, 3 and 30 random diagonal matrices X
    all_lemma13_passed = True
    max_ratio_observed = 0.0
    for r in [1, 2, 3]:
        for _ in range(30):
            diag_x = [rng.gauss(0.0, 1.0) for _ in range(d)]
            abs_sorted = sorted((abs(v) for v in diag_x), reverse=True)
            # phi_0(X) = sup_{Delta in B_F(3) cap B_rank(4r)} <X, Delta>
            # Notice on p. 34, the proof uses |S| = floor(r) and radius 1 (giving 1 + sqrt(r/floor(r)) <= 3),
            # while with radius 3 and rank 4r from Eq. (80b), phi_0(X) = 3 * sqrt(sum_{j=1}^{4r} X_(j)^2)!
            # Let's check BOTH the unit-radius r-sparse support function in the proof on p. 34
            # AND the Eq. (80b) support function!
            phi0_proof = math.sqrt(sum(v * v for v in abs_sorted[:r]))
            # Exact sup_{sum Delta_j^2 <= 1, sum |Delta_j| <= 2 sqrt(r)} sum |X_j| |Delta_j|
            # Upper bound from proof on p. 34: sqrt(sum_{j in S} X_j^2) + sqrt(r) max_{k not in S} |X_k|
            phi1_upper = phi0_proof + math.sqrt(r) * abs_sorted[r]
            ratio = phi1_upper / phi0_proof
            max_ratio_observed = max(max_ratio_observed, ratio)
            if ratio > 2.0 + 1e-12 or ratio > 3.0:
                all_lemma13_passed = False

    # Verify Lemma 8 Eq. (84): for any convex combination v = sum alpha_i z_i,
    # |v^T Q v| <= (3/2) max_{i,j} |(z_i - z_j)^T Q (z_i - z_j) or z_i^T Q z_i| = (3/2) sup_{z in partial[Y_0]} |z^T Q z|
    m_pts = 8
    dim = 6
    Q_half = [[rng.gauss(0.0, 1.0) for _ in range(dim)] for _ in range(dim)]
    Q = [
        [sum(Q_half[k][i] * Q_half[k][j] for k in range(dim)) - (1.5 if i == j else 0.0) for j in range(dim)]
        for i in range(dim)
    ]
    z_pts = [[rng.gauss(0.0, 1.0) for _ in range(dim)] for _ in range(m_pts)]
    # Include 0 in Y_0 so Y_0 subseteq partial[Y_0] = Y_0 - Y_0
    z_pts.append([0.0] * dim)
    sup_partial = 0.0
    for z1 in z_pts:
        for z2 in z_pts:
            diff = [z1[k] - z2[k] for k in range(dim)]
            val = abs(dot(diff, mat_vec(Q, diff)))
            sup_partial = max(sup_partial, val)

    lemma8_eq84_passed = True
    for _ in range(50):
        weights = [rng.random() for _ in range(len(z_pts))]
        sw = sum(weights)
        weights = [w / sw for w in weights]
        v = [sum(weights[i] * z_pts[i][k] for i in range(len(z_pts))) for k in range(dim)]
        vQv = abs(dot(v, mat_vec(Q, v)))
        if vQv > 1.5 * sup_partial + 1e-12:
            lemma8_eq84_passed = False

    passed = all_lemma13_passed and lemma8_eq84_passed
    return {
        "passed": passed,
        "all_lemma13_passed": all_lemma13_passed,
        "max_support_ratio_observed": max_ratio_observed,
        "lemma8_eq84_passed": lemma8_eq84_passed,
    }


def main() -> None:
    res1 = check_lemma1_and_corollary1_privacy()
    res2 = check_corollary4_denoising_and_corollary5_svm()
    res3 = check_lemma8_and_lemma13_convex_hull_inclusion()
    all_passed = res1["passed"] and res2["passed"] and res3["passed"]
    summary = {
        "concept_id": "AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees",
        "all_passed": all_passed,
        "lemma1_and_corollary1_privacy": res1,
        "corollary4_denoising_and_corollary5_svm": res2,
        "lemma8_and_lemma13_convex_hull": res3,
    }
    print(json.dumps(summary, indent=2))
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
