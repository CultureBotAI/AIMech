#!/usr/bin/env python3
"""Constructed boundary and mechanism verification for Round 223:
AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
(Ostrovskii & Rudi 2019, COLT PMLR 99:2531-2550, arXiv:1902.03086v2).

Verifies:
1. Degrees-of-freedom dyadic halving stability (Lemma 14: df_{lambda/2}(S) <= 2 df_lambda(S)
   and |df_{lambda/2}(S) - df_lambda(S)| <= df_lambda(S)) and Lemma 6 spectral-similarity
   and trace-surrogate bounds (Eqs. 35-37): whenever ||S_lambda^{-1/2}(S_hat - S)S_lambda^{-1/2}|| <= 1/2,
   (2/3) I <= S_lambda^{1/2} S_hat_lambda^{-1} S_lambda^{1/2} <= 2 I and
   |Tr(S S_hat_lambda^{-1}) - df_lambda(S)| <= 3 df_lambda(S).
2. Iterative Cholesky-decorrelated calibrated covariance estimation (Algorithm 1,
   Theorem 7, Corollary 8) vs. non-affine-equivariant norm-clipped Wei-Minsker
   estimation (Eq. 7) on an ill-conditioned heavy-tailed Student-t design
   (nu = 5 degrees of freedom, kurtosis kappa <= 9^(1/4)): verifies that
   Algorithm 1 drastically reduces the calibrated spectral error
   ||S_lambda^{-1/2}(S_hat - S)S_lambda^{-1/2}|| and satisfies Corollary 12
   relative eigenvalue bounds across all orders of magnitude of S.
3. Lepskii-adaptive truncation selection (Algorithm 2, Equation 28, Theorem 10)
   and heavy-tailed pseudo-decorrelated ridge regression decomposition
   (Equation 33, Theorem 13, Appendix D Equations 44-48).
"""

from __future__ import annotations

import json
import math
import random
import sys


def verify_lemmas_14_and_6() -> dict[str, object]:
    """Verify Lemma 14 (df_{lambda/2}(S) <= 2 df_lambda(S)) and Lemma 6 Eqs. (35)-(37)."""
    # Construct an anisotropic spectrum S = diag(s_1, ..., s_d) with power-law decay s_j = j^(-2)
    d = 12
    eigs = [1.0 / ((j + 1) ** 2) for j in range(d)]

    max_df_ratio = 0.0
    max_trace_surrogate_ratio = 0.0
    min_sim_eig = 10.0
    max_sim_eig = 0.0

    for lam in (0.005, 0.02, 0.1, 0.5):
        df_lam = sum(s / (s + lam) for s in eigs)
        df_half = sum(s / (s + 0.5 * lam) for s in eigs)
        ratio = df_half / df_lam
        if ratio > max_df_ratio:
            max_df_ratio = ratio

        # Perturb S_hat so that delta_j = (S_hat_j - s_j) / (s_j + lam) in [-0.49, 0.49]
        # satisfying Eq. (15): ||S_lambda^{-1/2}(S_hat - S)S_lambda^{-1/2}|| <= 1/2.
        deltas = [(-0.48 if j % 2 == 0 else 0.48) for j in range(d)]
        s_hat_lam = [(s + lam) * (1.0 + dj) for s, dj in zip(eigs, deltas)]

        # Similarity matrix M = S_lambda^{1/2} S_hat_lambda^{-1} S_lambda^{1/2} has eigenvalues 1 / (1 + delta_j)
        sim_eigs = [1.0 / (1.0 + dj) for dj in deltas]
        min_sim_eig = min(min_sim_eig, min(sim_eigs))
        max_sim_eig = max(max_sim_eig, max(sim_eigs))

        # Surrogate trace Tr(S S_hat_lambda^{-1}) vs df_lambda(S)
        tr_surrogate = sum(s / sh_l for s, sh_l in zip(eigs, s_hat_lam))
        surr_diff_ratio = abs(tr_surrogate - df_lam) / df_lam
        if surr_diff_ratio > max_trace_surrogate_ratio:
            max_trace_surrogate_ratio = surr_diff_ratio

    passed = (
        1.0 <= max_df_ratio <= 2.0 + 1e-12
        and min_sim_eig >= (2.0 / 3.0) - 1e-12
        and max_sim_eig <= 2.0 + 1e-12
        and max_trace_surrogate_ratio <= 3.0 + 1e-12
    )
    return {
        "passed": passed,
        "max_df_halving_ratio": round(max_df_ratio, 6),
        "similarity_eigenvalue_range": [round(min_sim_eig, 6), round(max_sim_eig, 6)],
        "theoretical_similarity_bounds": [round(2.0 / 3.0, 6), 2.0],
        "max_trace_surrogate_diff_ratio": round(max_trace_surrogate_ratio, 6),
    }


def rho_theta(x: float, theta: float) -> float:
    """Truncation weight rho_theta(x) = min(x^2, theta) / x^2 (Eqs. 6-7)."""
    x2 = x * x
    if x2 <= theta or x2 == 0.0:
        return 1.0
    return theta / x2


def sample_student_t5(rng: random.Random) -> float:
    """Sample standard Student-t with nu = 5 degrees of freedom and unit variance."""
    # If Z ~ N(0,1) and V ~ chi^2_5 = sum_{k=1}^5 G_k^2, then Z / sqrt(V/5) has variance 5/(5-2) = 5/3.
    # Scaling by sqrt(3/5) gives unit variance E[T^2] = 1 and kurtosis E[T^4] = 9 (so kappa = 9^(1/4)).
    z = rng.gauss(0.0, 1.0)
    v = sum(rng.gauss(0.0, 1.0) ** 2 for _ in range(5))
    return z * math.sqrt(3.0 / max(v, 1e-12))


def verify_algorithm1_and_lepskii() -> dict[str, object]:
    """Verify Algorithm 1 iterative calibrated covariance estimation and Algorithm 2 Lepskii grid selection."""
    rng = random.Random(20261018)
    # Diagonal covariance S = diag(100.0, 10.0, 1.0, 0.1) in d = 4
    s_diag = [100.0, 10.0, 1.0, 0.1]
    d = len(s_diag)
    lam = 0.05
    L = 128.0
    T = int(math.ceil(math.log2(L / lam)))  # log2(2560) -> 12
    q = T + 1
    n = 5200
    m = n // (2 * q)

    # Generate n heavy-tailed samples X_i in R^d with independent Student-t(5) coordinates scaled by sqrt(s_j)
    samples = [
        [math.sqrt(s_diag[j]) * sample_student_t5(rng) for j in range(d)]
        for _ in range(n)
    ]

    def run_alg1_diagonal_cholesky(theta_val: float) -> list[float]:
        """Run Algorithm 1 on the sample; returns diagonal covariance estimate."""
        # Note: even for general matrices, when initialized and evaluated on basis-aligned axes,
        # we can also verify full d x d Cholesky; let's run exact full d x d Cholesky!
        return [0.0] * d

    def cholesky_d(mat: list[list[float]]) -> list[list[float]]:
        """Lower-triangular Cholesky factor R such that R R^T = mat."""
        low = [[0.0] * d for _ in range(d)]
        for i in range(d):
            for j in range(i + 1):
                s = sum(low[i][k] * low[j][k] for k in range(j))
                if i == j:
                    low[i][j] = math.sqrt(max(mat[i][i] - s, 1e-12))
                else:
                    low[i][j] = (mat[i][j] - s) / low[j][j]
        return low

    def solve_lower(low: list[list[float]], vec: list[float]) -> list[float]:
        """Solve R y = vec for y."""
        y = [0.0] * d
        for i in range(d):
            s = sum(low[i][k] * y[k] for k in range(i))
            y[i] = (vec[i] - s) / low[i][i]
        return y

    def calibrated_error(s_hat: list[list[float]]) -> float:
        """Compute Frobenius upper bound and exact diagonal/Rayleigh calibrated error ||S_lam^{-1/2}(S_hat - S)S_lam^{-1/2}||_F."""
        err2 = 0.0
        for i in range(d):
            for j in range(d):
                target = s_diag[i] if i == j else 0.0
                diff = (s_hat[i][j] - target) / math.sqrt((s_diag[i] + lam) * (s_diag[j] + lam))
                err2 += diff * diff
        return math.sqrt(err2)

    def run_alg1_full(theta_val: float) -> list[list[float]]:
        # Line 2-3: batch 0
        s_curr = [[0.0] * d for _ in range(d)]
        for idx in range(m):
            x = samples[idx]
            norm_x = math.sqrt(sum(v * v for v in x))
            alpha = L * rho_theta(norm_x / math.sqrt(L), theta_val)
            for a in range(d):
                for b in range(d):
                    s_curr[a][b] += (alpha / m) * x[a] * x[b]
        lam_t = L
        for t in range(T):
            s_lam = [
                [s_curr[a][b] + (lam_t if a == b else 0.0) for b in range(d)]
                for a in range(d)
            ]
            r_mat = cholesky_d(s_lam)
            s_next = [[0.0] * d for _ in range(d)]
            start = m * (t + 1)
            for idx in range(start, start + m):
                x = samples[idx]
                y = solve_lower(r_mat, x)
                norm_y = math.sqrt(sum(v * v for v in y))
                alpha = rho_theta(norm_y, theta_val)
                for a in range(d):
                    for b in range(d):
                        s_next[a][b] += (alpha / m) * x[a] * x[b]
            s_curr = s_next
            lam_t = 0.5 * lam_t

        # Final batch (lines 11-16)
        r_rem = n - m * (T + 1)
        theta_T = 2.0 * theta_val * math.sqrt(T + 1)
        s_lam_T = [
            [s_curr[a][b] + (lam_t if a == b else 0.0) for b in range(d)]
            for a in range(d)
        ]
        r_mat_T = cholesky_d(s_lam_T)
        s_final = [[0.0] * d for _ in range(d)]
        start_rem = m * (T + 1)
        for idx in range(start_rem, n):
            x = samples[idx]
            y = solve_lower(r_mat_T, x)
            norm_y = math.sqrt(sum(v * v for v in y))
            alpha = rho_theta(norm_y, theta_T)
            for a in range(d):
                for b in range(d):
                    s_final[a][b] += (alpha / r_rem) * x[a] * x[b]
        return s_final

    # Compare with non-affine-equivariant Wei-Minsker estimator at the same truncation scale
    # scaled for the largest eigenvalue (theta_wm = 15.0 * s_diag[0] = 1500.0 vs tight theta_wm = 15.0)
    theta_alg1 = 16.0
    s_hat_alg1 = run_alg1_full(theta_alg1)
    cal_err_alg1 = calibrated_error(s_hat_alg1)

    # Wei-Minsker with Euclidean norm clipping at theta_wm = 16.0 (clips the large-variance coordinate heavily!)
    s_wm_small = [[0.0] * d for _ in range(d)]
    for x in samples:
        nx = math.sqrt(sum(v * v for v in x))
        w = rho_theta(nx, theta_alg1)
        for a in range(d):
            for b in range(d):
                s_wm_small[a][b] += (w / n) * x[a] * x[b]
    cal_err_wm_small = calibrated_error(s_wm_small)

    # Relative eigenvalue error on diagonal entries of s_hat_alg1 (Corollary 12)
    max_rel_diag_err = max(
        abs(s_hat_alg1[j][j] - s_diag[j]) / s_diag[j] for j in range(d)
    )

    # Verify Algorithm 2 Lepskii grid selection over theta_j in {4.0, 8.0, 16.0, 32.0}
    grid = [4.0, 8.0, 16.0, 32.0]
    est_grid = [run_alg1_full(th) for th in grid]
    eps_grid = [0.015 * th for th in grid]
    selected_idx = len(grid) - 1
    for j_idx in range(len(grid)):
        ok = True
        for jp_idx in range(j_idx, len(grid)):
            # Compute ||S_{jp,lam}^{-1/2} (S_{jp} - S_j) S_{jp,lam}^{-1/2}||_F
            s_jp_lam = [
                [est_grid[jp_idx][a][b] + (lam if a == b else 0.0) for b in range(d)]
                for a in range(d)
            ]
            # Use diagonal scale of s_jp_lam for fast check
            diff2 = 0.0
            for a in range(d):
                for b in range(d):
                    d_ab = est_grid[jp_idx][a][b] - est_grid[j_idx][a][b]
                    diff2 += (d_ab * d_ab) / (s_jp_lam[a][a] * s_jp_lam[b][b])
            if math.sqrt(diff2) > 2.0 * (eps_grid[jp_idx] + eps_grid[j_idx]):
                ok = False
                break
        if ok:
            selected_idx = j_idx
            break

    cal_err_lepskii = calibrated_error(est_grid[selected_idx])

    passed = (
        cal_err_alg1 < 0.20
        and cal_err_alg1 < 0.35 * cal_err_wm_small
        and max_rel_diag_err < 0.15
        and cal_err_lepskii < 0.25
    )
    return {
        "passed": passed,
        "calibrated_error_alg1": round(cal_err_alg1, 6),
        "calibrated_error_wei_minsker_uncalibrated": round(cal_err_wm_small, 6),
        "max_relative_diagonal_error_alg1": round(max_rel_diag_err, 6),
        "lepskii_selected_theta": grid[selected_idx],
        "calibrated_error_lepskii": round(cal_err_lepskii, 6),
    }


def verify_theorem13_ridge_decomposition() -> dict[str, object]:
    """Verify Appendix D Equations (44)-(48) three-term excess risk decomposition for heavy-tailed ridge regression."""
    # Exact algebraic check of Eqs. (44)-(48) for S = diag(s_1, ..., s_d), w^*, w_lam = S_lam^{-1} S w^*,
    # w_hat_lam = S_hat_lam^{-1} S w^*, and E_3 = ||S^{1/2}(w_lam - w^*)|| <= lam ||S_lam^{-1/2} w^*||.
    s_diag = [100.0, 10.0, 1.0, 0.1]
    w_star = [0.2, -0.5, 1.0, 2.0]
    lam = 0.2
    # Suppose ||S_lam^{-1/2}(S_hat - S)S_lam^{-1/2}|| = eps <= 0.25
    eps = 0.2
    s_hat_diag = [s + eps * (s + lam) for s in s_diag]

    w_lam = [(s / (s + lam)) * w for s, w in zip(s_diag, w_star)]
    w_hat_lam = [(s / (sh + lam)) * w for s, sh, w in zip(s_diag, s_hat_diag, w_star)]

    # E_3 = ||S^{1/2}(w_lam - w^*)||_2 vs RHS_3 = lam ||S_lam^{-1/2} w^*||_2 (Eq. 47)
    e3 = math.sqrt(sum(s * ((wl - w) ** 2) for s, wl, w in zip(s_diag, w_lam, w_star)))
    rhs3 = lam * math.sqrt(sum((w * w) / (s + lam) for s, w in zip(s_diag, w_star)))

    # E_2 = ||S^{1/2}(w_hat_lam - w_lam)||_2 vs Eq. (48) upper bound:
    # ||S_lam^{1/2} S_hat_lam^{-1/2}||^2 * eps * ||S_lam^{-1/2} S^{1/2}|| * ||S^{1/2} w^*||
    e2 = math.sqrt(sum(s * ((whl - wl) ** 2) for s, whl, wl in zip(s_diag, w_hat_lam, w_lam)))
    norm_sim_sq = max((s + lam) / (sh + lam) for s, sh in zip(s_diag, s_hat_diag))
    norm_s_slam = math.sqrt(max(s / (s + lam) for s in s_diag))
    norm_s_wstar = math.sqrt(sum(s * (w * w) for s, w in zip(s_diag, w_star)))
    rhs2 = norm_sim_sq * eps * norm_s_slam * norm_s_wstar

    passed = (
        e3 <= rhs3 + 1e-12
        and e2 <= rhs2 + 1e-12
    )
    return {
        "passed": passed,
        "E3_fixed_design_bias": round(e3, 6),
        "Eq47_bias_upper_bound": round(rhs3, 6),
        "E2_covariance_estimation_term": round(e2, 6),
        "Eq48_upper_bound": round(rhs2, 6),
    }


def main() -> int:
    c1 = verify_lemmas_14_and_6()
    c2 = verify_algorithm1_and_lepskii()
    c3 = verify_theorem13_ridge_decomposition()
    all_passed = bool(c1["passed"] and c2["passed"] and c3["passed"])
    summary = {
        "concept_id": "AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression",
        "all_passed": all_passed,
        "check_1_lemmas_14_and_6": c1,
        "check_2_algorithm1_and_lepskii": c2,
        "check_3_theorem13_ridge_decomposition": c3,
    }
    print(json.dumps(summary, indent=2))
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
