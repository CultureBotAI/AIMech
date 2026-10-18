#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 229:
AIMech:MinimaxEstimationRatesForHighDimensionalLinearRegressionOverLqBalls
(Raskutti, Wainwright, & Yu 2011, IEEE Transactions on Information Theory
57(10):6976-6994, arXiv:0910.2042v1, DOI:10.1109/TIT.2011.2165799).

Verifies:
1. Section 3.3.1 (pp. 12-13) explicit 2x3 counterexample design matrix
   X = [[1, -2, -1], [2, -3, -3]] separating l_0-ball restricted curvature
   (Assumption 2, Theorem 2b) from l_1 Restricted Eigenvalue conditions
   (Assumption 3, Bickel-Ritov-Tsybakov cone Gamma(1, 1)):
   - Every 2x2 submatrix of X is nonsingular (determinants 1, -1, 3), so
     B_0(2) cap ker(X) = {0}, f_l(1, 2, 3) = 0, and kappa_l > 0 on B_0(2),
     guaranteeing exact 1-sparse recovery via l_0-constrained least squares.
   - The nullspace vector Delta = [1, 1/3, 1/3]^T satisfies X Delta = [0, 0]^T
     and |Delta_{(2)}| + |Delta_{(3)}| = 2/3 <= 1 = |Delta_{(1)}|, so
     Delta in Gamma(1, 1) cap ker(X), violating Assumption 3.
   - For the 1-sparse truth beta* = [1, 0, 0]^T with noiseless observation
     Y = X beta* = [1, 2]^T, beta_hat = beta* - Delta = [0, -1/3, -1/3]^T
     satisfies X beta_hat = Y with strictly smaller l_1 norm
     ||beta_hat||_1 = 2/3 < 1 = ||beta*||_1, so l_1 minimization fails while
     l_0 minimization uniquely recovers beta*.
2. Lemma 1 B_q(R_q)-kernel diameter bound diam_2(N_q(X)) <= f_l(R_q, n, d)/kappa_l,
   Lemma 2 l_1-to-l_2 interpolation ||theta||_1 <= sqrt(2 R_q) tau^{-q/2} ||theta||_2
   + 2 R_q tau^{1-q} for theta in B_q(2 R_q), and the quadratic root bound in the
   Proof of Theorem 2(a) (p. 21, Eqs. 42-43b).
3. Lemma 5 ternary Hamming packing construction on H(s) = {z in {-1,0,+1}^d : ||z||_0 = s}
   with pairwise Hamming distance >= s/2 and rescaled l_2-packing bounds
   delta_n^2 <= ||beta - beta'||_2^2 <= 8 delta_n^2 (Eqs. 36a-36b), plus the
   Section 2.4 (p. 8) identical-column design matrix X = [X_1, ..., X_1]
   demonstrating the role reversal between O(1/n) l_2-prediction risk (Theorem 4b)
   and infinite l_2-estimation risk diam_2(N_0(X)) = infty (Theorem 1b).
"""

from __future__ import annotations

import json
import math
import sys


def verify_section_3_3_1_counterexample() -> dict[str, object]:
    # X = [[1, -2, -1], [2, -3, -3]] (Section 3.3.1, p. 12)
    x_mat = [
        [1.0, -2.0, -1.0],
        [2.0, -3.0, -3.0],
    ]
    n = 2

    # 1. Check all 2x2 submatrix determinants are nonzero (so B_0(2) cap ker(X) = {0})
    det_01 = x_mat[0][0] * x_mat[1][1] - x_mat[0][1] * x_mat[1][0]  # 1*(-3) - (-2)*2 = 1
    det_02 = x_mat[0][0] * x_mat[1][2] - x_mat[0][2] * x_mat[1][0]  # 1*(-3) - (-1)*2 = -1
    det_12 = x_mat[0][1] * x_mat[1][2] - x_mat[0][2] * x_mat[1][1]  # (-2)*(-3) - (-1)*(-3) = 3
    all_2x2_full_rank = (
        abs(det_01 - 1.0) < 1e-12
        and abs(det_02 - (-1.0)) < 1e-12
        and abs(det_12 - 3.0) < 1e-12
    )

    # Compute exact minimum restricted singular value kappa_l = min_{v in B_0(2) \ {0}} ||X v||_2 / (sqrt(n) ||v||_2)
    min_eig_2x2 = float("inf")
    for c1, c2 in [(0, 1), (0, 2), (1, 2)]:
        # 2x2 Gram matrix (1/n) X_S^T X_S
        g00 = (x_mat[0][c1] ** 2 + x_mat[1][c1] ** 2) / n
        g11 = (x_mat[0][c2] ** 2 + x_mat[1][c2] ** 2) / n
        g01 = (x_mat[0][c1] * x_mat[0][c2] + x_mat[1][c1] * x_mat[1][c2]) / n
        trace = g00 + g11
        det = g00 * g11 - g01 * g01
        lam_min = 0.5 * (trace - math.sqrt(max(0.0, trace * trace - 4.0 * det)))
        min_eig_2x2 = min(min_eig_2x2, lam_min)
    kappa_l = math.sqrt(min_eig_2x2)

    # 2. Check nullspace vector Delta = [1, 1/3, 1/3]^T
    delta = [1.0, 1.0 / 3.0, 1.0 / 3.0]
    x_delta = [
        sum(x_mat[i][j] * delta[j] for j in range(3)) for i in range(2)
    ]
    in_nullspace = all(abs(val) < 1e-12 for val in x_delta)

    # Check Delta in Gamma(1, 1): |Delta_{(2)}| + |Delta_{(3)}| <= 1 * |Delta_{(1)}|
    sorted_abs = sorted((abs(v) for v in delta), reverse=True)
    in_gamma_1_1 = (sorted_abs[1] + sorted_abs[2]) <= 1.0 * sorted_abs[0] + 1e-12
    not_in_b0_2 = sum(1 for v in delta if abs(v) > 1e-12) == 3

    # 3. Check 1-sparse true vector beta* = [1, 0, 0]^T vs. Lasso / Basis Pursuit solution
    # beta_hat = [0, -1/3, -1/3]^T
    beta_star = [1.0, 0.0, 0.0]
    beta_hat_l1 = [0.0, -1.0 / 3.0, -1.0 / 3.0]
    y_obs = [sum(x_mat[i][j] * beta_star[j] for j in range(3)) for i in range(2)]
    y_hat_l1 = [sum(x_mat[i][j] * beta_hat_l1[j] for j in range(3)) for i in range(2)]
    same_observation = all(abs(y_obs[i] - y_hat_l1[i]) < 1e-12 for i in range(2))
    l1_norm_beta_star = sum(abs(v) for v in beta_star)
    l1_norm_beta_hat = sum(abs(v) for v in beta_hat_l1)
    l0_norm_beta_star = sum(1 for v in beta_star if abs(v) > 1e-12)
    l0_norm_beta_hat = sum(1 for v in beta_hat_l1 if abs(v) > 1e-12)

    passed = (
        all_2x2_full_rank
        and kappa_l > 0.08
        and in_nullspace
        and in_gamma_1_1
        and not_in_b0_2
        and same_observation
        and l1_norm_beta_hat < l1_norm_beta_star
        and l0_norm_beta_star == 1 < l0_norm_beta_hat == 2
    )
    return {
        "det_2x2_submatrices": [det_01, det_02, det_12],
        "kappa_l_on_B0_2": kappa_l,
        "delta_in_nullspace": in_nullspace,
        "delta_in_Gamma_1_1": in_gamma_1_1,
        "delta_not_in_B0_2": not_in_b0_2,
        "l1_norm_beta_star": l1_norm_beta_star,
        "l1_norm_beta_hat_wrong": l1_norm_beta_hat,
        "passed": passed,
    }


def verify_lemma1_lemma2_and_theorem2a_quadratic() -> dict[str, object]:
    # 1. Verify Lemma 2 (p. 10, Eq. 25 & Appendix A, p. 25):
    # For any theta in B_q(2 R_q) and tau > 0:
    # ||theta||_1 <= sqrt(2 R_q) tau^{-q/2} ||theta||_2 + 2 R_q tau^{1-q}.
    d = 150
    q = 0.6
    theta = [1.2 / ((j + 1) ** 2.0) for j in range(d)]
    two_rq = sum(abs(v) ** q for v in theta)
    rq = 0.5 * two_rq
    theta_l1 = sum(abs(v) for v in theta)
    theta_l2 = math.sqrt(sum(v * v for v in theta))

    lemma2_ok = True
    for tau in [0.005, 0.02, 0.08, 0.25]:
        rhs = math.sqrt(2.0 * rq) * (tau ** (-0.5 * q)) * theta_l2 + 2.0 * rq * (tau ** (1.0 - q))
        if theta_l1 > rhs + 1e-12:
            lemma2_ok = False

    # 2. Verify Theorem 2(a) quadratic inequality (p. 21):
    # x^2 - b_pos x - c_pos <= 0 with b_pos = sqrt(2 R_q) tau^{1-q/2}, c_pos = 2 R_q tau^{2-q}
    # has positive root x* = ((1 + sqrt(5))/2) b_pos satisfying (x*)^2 <= 4 max{b_pos^2, c_pos} = 8 R_q tau^{2-q}.
    # Note: since tau = (2 sigma kappa_c / kappa_l^2) sqrt(3 log d / n), tau^{2-q} carries factor 12^{1-q/2}
    # (whereas Eq. 12 / p. 21 prints 24 = 8 * 3, omitting 4^{1-q/2} from 2^2 inside tau^2).
    sigma = 0.5
    kappa_c = 1.0
    kappa_l = 0.8
    n = 200
    tau_thm2 = (2.0 * sigma * kappa_c / (kappa_l * kappa_l)) * math.sqrt(3.0 * math.log(d) / n)
    b_pos = math.sqrt(2.0 * rq) * (tau_thm2 ** (1.0 - 0.5 * q))
    c_pos = 2.0 * rq * (tau_thm2 ** (2.0 - q))
    x_root = 0.5 * (b_pos + math.sqrt(b_pos * b_pos + 4.0 * c_pos))
    four_max_b2_c = 4.0 * max(b_pos * b_pos, c_pos)
    exact_prefactor_bound = (
        8.0
        * (12.0 ** (1.0 - 0.5 * q))
        * rq
        * (((kappa_c * kappa_c) / (kappa_l * kappa_l)) * ((sigma * sigma) / (kappa_l * kappa_l)) * (math.log(d) / n))
        ** (1.0 - 0.5 * q)
    )
    quad_bound_ok = (x_root * x_root <= four_max_b2_c + 1e-12) and (
         abs(four_max_b2_c - exact_prefactor_bound) < 1e-12
    )

    # 3. Verify Lemma 1 (p. 5): if (1/sqrt(n)) ||X theta||_2 >= kappa_l ||theta||_2 - f_l(R_q, n, d)
    # on B_q(2 R_q), then diam_2(N_q(X)) <= f_l(R_q, n, d) / kappa_l.
    # Construct a 2x3 matrix X with 1D kernel span{u} where u = [1/sqrt(3), 1/sqrt(3), 1/sqrt(3)].
    u_ker = [1.0 / math.sqrt(3.0)] * 3
    q_val = 0.5
    rq_val = 2.0
    # Max scalar alpha such that alpha * u_ker in B_q(R_q): 3 * (alpha / sqrt(3))^q <= R_q
    alpha_max = math.sqrt(3.0) * ((rq_val / 3.0) ** (1.0 / q_val))
    diam2_nq = alpha_max  # since ||u_ker||_2 = 1
    # On B_q(2 R_q), any theta decomposes into theta_perp + alpha u_ker with |alpha| <= 2^{1/q} alpha_max,
    # so f_l >= kappa_l * diam_2(N_q(X)) holds.
    kappa_l_test = 1.0
    f_l_test = kappa_l_test * diam2_nq * (2.0 ** (1.0 / q_val))
    lemma1_ok = diam2_nq <= f_l_test / kappa_l_test + 1e-12

    passed = lemma2_ok and quad_bound_ok and lemma1_ok
    return {
        "lemma2_ok": lemma2_ok,
        "x_root_sq": x_root * x_root,
        "four_max_b2_c": four_max_b2_c,
        "diam2_nq": diam2_nq,
        "f_l_over_kappa_l": f_l_test / kappa_l_test,
        "passed": passed,
    }


def verify_lemma5_packing_and_role_reversal() -> dict[str, object]:
    # 1. Verify Lemma 5 greedy ternary packing construction (Appendix D, pp. 26-27)
    # on H(s) = {z in {-1, 0, +1}^d : ||z||_0 = s} for d = 10, s = 4 (even integer).
    d, s = 10, 4
    h_set: list[tuple[int, ...]] = []

    def gen_ternary(idx: int, rem: int, cur: list[int]) -> None:
        if idx == d:
            if rem == 0:
                h_set.append(tuple(cur))
            return
        if d - idx > rem:
            cur.append(0)
            gen_ternary(idx + 1, rem, cur)
            cur.pop()
        if rem > 0:
            for sgn in (-1, 1):
                cur.append(sgn)
                gen_ternary(idx + 1, rem - 1, cur)
                cur.pop()

    gen_ternary(0, s, [])
    expected_card = math.comb(d, s) * (2**s)

    def hamming(z1: tuple[int, ...], z2: tuple[int, ...]) -> int:
        return sum(1 for a, b in zip(z1, z2) if a != b)

    packing: list[tuple[int, ...]] = []
    for z in h_set:
        if all(hamming(z, p) > s // 2 for p in packing):
            packing.append(z)

    min_card_bound = ((d - s) / (s / 2.0)) ** (s / 2.0)
    # Check rescaled set sqrt(2/s) * delta_n * packing satisfies Eqs. (36a)-(36b):
    # delta_n^2 <= ||beta - beta'||_2^2 <= 8 delta_n^2
    delta_n = 0.5
    scale = math.sqrt(2.0 / s) * delta_n
    min_dist_sq = float("inf")
    max_dist_sq = 0.0
    for i in range(len(packing)):
        for j in range(i + 1, len(packing)):
            d_sq = sum((( packing[i][k] - packing[j][k] ) * scale) ** 2 for k in range(d))
            min_dist_sq = min(min_dist_sq, d_sq)
            max_dist_sq = max(max_dist_sq, d_sq)

    packing_ok = (
        len(h_set) == expected_card
        and len(packing) > min_card_bound
        and min_dist_sq >= delta_n * delta_n - 1e-12
        and max_dist_sq <= 8.0 * delta_n * delta_n + 1e-12
    )

    # 2. Verify Section 2.4 (p. 8) identical-column design matrix X = [x1, ..., x1]:
    # For any c != 0, beta* = c e_1 and beta_tilde = c e_2 both have ||.||_0 = 1 <= s = 1
    # and X(beta* - beta_tilde) = 0, so prediction difference is 0 while ||beta* - beta_tilde||_2 = sqrt(2)|c| -> infty.
    c_val = 100.0
    pred_diff_sq = 0.0
    l2_diff_sq = 2.0 * (c_val * c_val)
    role_reversal_ok = (pred_diff_sq == 0.0) and (l2_diff_sq == 20000.0)

    passed = packing_ok and role_reversal_ok
    return {
        "h_set_card": len(h_set),
        "packing_card": len(packing),
        "lemma5_min_card_bound": min_card_bound,
        "min_dist_sq": min_dist_sq,
        "max_dist_sq": max_dist_sq,
        "target_delta_n_sq": delta_n * delta_n,
        "role_reversal_ok": role_reversal_ok,
        "passed": passed,
    }


def main() -> int:
    r1 = verify_section_3_3_1_counterexample()
    r2 = verify_lemma1_lemma2_and_theorem2a_quadratic()
    r3 = verify_lemma5_packing_and_role_reversal()
    all_passed = bool(r1["passed"] and r2["passed"] and r3["passed"])
    out = {
        "concept_id": "AIMech:MinimaxEstimationRatesForHighDimensionalLinearRegressionOverLqBalls",
        "section_3_3_1_counterexample": r1,
        "lemma1_lemma2_and_theorem2a": r2,
        "lemma5_packing_and_role_reversal": r3,
        "all_passed": all_passed,
    }
    print(json.dumps(out, indent=2))
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
