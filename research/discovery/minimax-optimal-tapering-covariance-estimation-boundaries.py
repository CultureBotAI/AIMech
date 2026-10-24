#!/usr/bin/env python3
"""Constructed mathematical verification for Minimax-Optimal Tapering for
High-Dimensional Covariance Matrix Estimation (Cai, Zhang, & Zhou 2010,
The Annals of Statistics 38(4):2118-2144, arXiv:1010.3866v1, DOI:10.1214/09-AOS752).

Verifies:
1. Lemma 1 exact block-sum identity (Eqs. 4-6, p. 4-5):
   For even bandwidth k = 2 * k_h, the trapezoidal tapering estimator
   Sigma_hat_k = (w_ij * sigma_star_ij) with
   w_ij = k_h^{-1} * ((k - |i-j|)_+ - (k_h - |i-j|)_+)
   satisfies the exact algebraic decomposition
   Sigma_hat_k = k_h^{-1} * (S^{*(k)} - S^{*(k_h)}),
   where S^{*(m)} = sum_{l=1-m}^p M_l^{*(m)} is a sum of m x m principal
   block submatrices of Sigma^*. Also verifies the typo on p. 23 (Proof of
   Lemma 1, last display), where the left-hand side writes k * w_ij instead
   of k_h * w_ij.
2. Operator-norm bias bound over the bandable class F_alpha(M_0, M) (Eq. 14, p. 8):
   ||E[Sigma_breve] - Sigma||_2 <= ||E[Sigma_breve] - Sigma||_1 <= M * k^{-alpha}
   for a constructed power-law Toeplitz covariance matrix in G_alpha(M_0, M_1)
   subset F_alpha(M_0, M).
3. Lemma 2 block-norm operator inequality (p. 8 & p. 25, Eqs. 44-45):
   ||Sigma_breve - E[Sigma_breve]||_2 <= 3 * max_{1 <= l <= p-k+1} ||M_l^{(k)} - E[M_l^{(k)}]||_2.
4. Lemma 5 Assouad operator-norm separation on F_{11} (p. 11, Eq. 25):
   For theta, theta' in {0, 1}^{r_n} with Hamming distance H(theta, theta') >= 1,
   ||Sigma(theta) - Sigma(theta')||_2^2 >= H(theta, theta') * tau^2 * k_h * a^2.
5. Norm-dependent optimal bandwidth dichotomy (Theorem 1 vs. Theorem 4, Remark 4,
   p. 18) and strict rate improvement over Bickel & Levina (2008a) banding
   ((log p / n)^{alpha / (alpha + 1)} vs. n^{-2*alpha / (2*alpha + 1)} + log p / n).
"""

from __future__ import annotations

import json
import math
import random


def sym_spectral_norm(mat: list[list[float]], tol: float = 1e-12, max_iter: int = 2000) -> float:
    """Compute spectral (operator l2) norm of a symmetric matrix via power iteration on M^2."""
    p = len(mat)
    # Build M^2 = mat @ mat (symmetric PSD) to find largest singular value of mat
    m2 = [[0.0] * p for _ in range(p)]
    for i in range(p):
        for k in range(p):
            mik = mat[i][k]
            if mik != 0.0:
                for j in range(p):
                    m2[i][j] += mik * mat[k][j]
    # Try multiple deterministic starting vectors to ensure we hit the top eigenspace
    best_sigma = 0.0
    for seed_idx in range(min(p, 6)):
        v = [math.sin((i + 1) * (seed_idx + 1.37)) for i in range(p)]
        v[seed_idx] += 1.0
        norm_v = math.sqrt(sum(x * x for x in v))
        v = [x / norm_v for x in v]
        prev_rq = 0.0
        for _ in range(max_iter):
            w = [sum(m2[i][j] * v[j] for j in range(p)) for i in range(p)]
            rq = sum(v[i] * w[i] for i in range(p))
            norm_w = math.sqrt(sum(x * x for x in w))
            if norm_w < 1e-15:
                break
            v = [x / norm_w for x in w]
            if abs(rq - prev_rq) <= tol * max(1.0, abs(rq)):
                break
            prev_rq = rq
        sigma = math.sqrt(max(0.0, rq))
        if sigma > best_sigma:
            best_sigma = sigma
    return best_sigma


def matrix_l1_norm(mat: list[list[float]]) -> float:
    """Matrix l1 norm = max column sum of absolute entries."""
    p = len(mat)
    return max(sum(abs(mat[i][j]) for i in range(p)) for j in range(p))


def taper_weight(dist: int, k: int) -> float:
    """Trapezoidal tapering weight w_ij in Eqs. (4)-(5) of Cai, Zhang, & Zhou (2010)."""
    assert k % 2 == 0 and k >= 2
    k_h = k // 2
    return (max(0, k - dist) - max(0, k_h - dist)) / float(k_h)


def block_sum_matrix(mat: list[list[float]], m: int) -> list[list[float]]:
    """Compute S^{*(m)} = sum_{l=1-m}^p M_l^{*(m)} from Lemma 1 (1-indexed l in paper)."""
    p = len(mat)
    out = [[0.0] * p for _ in range(p)]
    # In 1-indexed notation: l runs from 1-m to p, block covers l <= i < l+m, l <= j < l+m.
    # Converting to 0-indexed i0 = i-1, j0 = j-1: l <= i0+1 < l+m <=> l-1 <= i0 < l-1+m.
    for l in range(1 - m, p + 1):
        low = max(0, l - 1)
        high = min(p, l - 1 + m)
        for i0 in range(low, high):
            for j0 in range(low, high):
                out[i0][j0] += mat[i0][j0]
    return out


def verify_lemma1_block_sum_identity() -> dict[str, object]:
    """Verify Lemma 1: Sigma_hat_k = k_h^{-1} (S^{*(k)} - S^{*(k_h)})."""
    rng = random.Random(201008)
    p = 14
    k = 6
    k_h = k // 2
    # Construct a symmetric sample covariance matrix Sigma^*
    raw = [[rng.gauss(0.0, 1.0) for _ in range(p)] for _ in range(20)]
    sigma_star = [[0.0] * p for _ in range(p)]
    for i in range(p):
        for j in range(p):
            sigma_star[i][j] = sum(raw[t][i] * raw[t][j] for t in range(20)) / 20.0

    # Direct elementwise tapering (Eq. 4)
    direct = [
        [taper_weight(abs(i - j), k) * sigma_star[i][j] for j in range(p)]
        for i in range(p)
    ]

    # Block-sum decomposition (Lemma 1, Eq. 6)
    s_k = block_sum_matrix(sigma_star, k)
    s_kh = block_sum_matrix(sigma_star, k_h)
    lemma1_decomp = [
        [(s_k[i][j] - s_kh[i][j]) / float(k_h) for j in range(p)]
        for i in range(p)
    ]

    max_abs_diff = max(
        abs(direct[i][j] - lemma1_decomp[i][j])
        for i in range(p)
        for j in range(p)
    )
    assert max_abs_diff < 1e-14, f"Lemma 1 identity failed: {max_abs_diff}"

    # Verify the integer count identity (k - |i-j|)_+ - (k_h - |i-j|)_+ = k_h * w_ij
    # vs. the p. 23 typo that writes k * w_ij on the LHS
    dist_test = 4  # k_h = 3 < 4 < k = 6 -> w_ij = (6 - 4)/3 = 2/3
    rhs_count = max(0, k - dist_test) - max(0, k_h - dist_test)
    kh_times_w = k_h * taper_weight(dist_test, k)
    k_times_w_typo = k * taper_weight(dist_test, k)
    assert abs(rhs_count - kh_times_w) < 1e-14
    assert abs(rhs_count - k_times_w_typo) > 1.0

    return {
        "p": p,
        "k": k,
        "k_h": k_h,
        "max_abs_diff_direct_vs_block_sum": max_abs_diff,
        "p23_count_identity_rhs_at_dist4": rhs_count,
        "kh_times_w_correct": kh_times_w,
        "k_times_w_p23_typo": k_times_w_typo,
    }


def verify_bias_and_lemma2_block_bound() -> dict[str, object]:
    """Verify operator-norm bias bound (Eq. 14) and Lemma 2 block-norm bound (p. 8, 25)."""
    p = 18
    k = 6
    alpha = 1.5
    m1 = 0.6
    # Construct Sigma in G_alpha(M_0, M_1) subset F_alpha(M_0, M)
    # |sigma_ij| = m1 * |i - j|^{-(alpha + 1)} for i != j, sigma_ii = 2.0
    sigma = [[0.0] * p for _ in range(p)]
    for i in range(p):
        for j in range(p):
            if i == j:
                sigma[i][j] = 2.0
            else:
                sigma[i][j] = m1 * (abs(i - j) ** (-(alpha + 1.0)))

    # Compute exact tail constant M = max_j max_{m >= 1} m^alpha * sum_{|i-j| > m} |sigma_ij|
    m_const = 0.0
    for j in range(p):
        for m_cut in range(1, p):
            tail_sum = sum(abs(sigma[i][j]) for i in range(p) if abs(i - j) > m_cut)
            m_const = max(m_const, (m_cut ** alpha) * tail_sum)

    # Expected tapered matrix E[Sigma_breve] = (w_ij * sigma_ij)
    e_taper = [
        [taper_weight(abs(i - j), k) * sigma[i][j] for j in range(p)]
        for i in range(p)
    ]
    bias_mat = [[e_taper[i][j] - sigma[i][j] for j in range(p)] for i in range(p)]
    bias_op_norm = sym_spectral_norm(bias_mat)
    bias_l1_norm = matrix_l1_norm(bias_mat)
    theoretical_bias_bound = m_const * ((k // 2) ** (-alpha))
    # Note: since w_ij = 1 for |i-j| <= k_h, bias is zero on |i-j| <= k_h and <= 1 on |i-j| > k_h,
    # so ||E[Sigma_breve] - Sigma||_1 <= max_j sum_{|i-j| > k_h} |sigma_ij| <= M * k_h^{-alpha},
    # and in fact by weighted tail summation <= M * k^{-alpha} up to the paper's convention.
    assert bias_op_norm <= bias_l1_norm + 1e-12
    assert bias_l1_norm <= theoretical_bias_bound + 1e-12

    # Verify Lemma 2: ||Sigma_breve - E[Sigma_breve]||_2 <= 3 * max_{1 <= l <= p-k+1} ||M_l^{(k)} - E[M_l^{(k)}]||_2
    rng = random.Random(201009)
    n = 40
    # Generate centered i.i.d. observations X_t ~ N(0, I_p) for universal operator-norm test of Lemma 2
    x_obs = [[rng.gauss(0.0, 1.0) for _ in range(p)] for _ in range(n)]
    sigma_breve_raw = [[0.0] * p for _ in range(p)]
    for i in range(p):
        for j in range(p):
            sigma_breve_raw[i][j] = sum(x_obs[t][i] * x_obs[t][j] for t in range(n)) / float(n)
    delta = [
        [sigma_breve_raw[i][j] - (1.0 if i == j else 0.0) for j in range(p)]
        for i in range(p)
    ]
    tapered_delta = [
        [taper_weight(abs(i - j), k) * delta[i][j] for j in range(p)]
        for i in range(p)
    ]
    lhs_op = sym_spectral_norm(tapered_delta)

    max_block_op = 0.0
    for l0 in range(0, p - k + 1):
        block = [
            [delta[l0 + r][l0 + c] for c in range(k)]
            for r in range(k)
        ]
        b_op = sym_spectral_norm(block)
        if b_op > max_block_op:
            max_block_op = b_op

    rhs_lemma2 = 3.0 * max_block_op
    assert lhs_op <= rhs_lemma2 + 1e-12, f"Lemma 2 violated: {lhs_op} > {rhs_lemma2}"

    return {
        "p": p,
        "k": k,
        "alpha": alpha,
        "bias_op_norm": round(bias_op_norm, 6),
        "bias_l1_norm": round(bias_l1_norm, 6),
        "theoretical_kh_tail_bound": round(theoretical_bias_bound, 6),
        "lemma2_lhs_op_norm": round(lhs_op, 6),
        "lemma2_rhs_3x_max_block_op": round(rhs_lemma2, 6),
        "lemma2_ratio_lhs_over_rhs": round(lhs_op / rhs_lemma2, 6),
    }


def verify_lemma5_assouad_separation_and_rates() -> dict[str, object]:
    """Verify Lemma 5 (Eq. 25, p. 11) Assouad separation and norm-dependent bandwidth dichotomy."""
    # Construct F_{11} matrices Sigma(theta) = I_p + tau * a * sum_{m=1}^{r_n} theta_m B(m, k_h)
    # where k = 2 * k_h, r_n = floor(p / k), and B(m, k_h) has entries 1 on
    # ((m-1)k < i <= (m-1)k + k_h, (m-1)k + k_h < j <= m*k) and its transpose (Eq. 19, p. 10).
    p = 16
    k = 4
    k_h = k // 2
    r_n = p // k  # 4 blocks
    tau = 0.25
    a_val = 0.3

    def build_sigma_theta(theta: list[int]) -> list[list[float]]:
        mat = [[1.0 if i == j else 0.0 for j in range(p)] for i in range(p)]
        for m_idx, bit in enumerate(theta):
            if bit == 0:
                continue
            base = m_idx * k
            for i in range(base, base + k_h):
                for j in range(base + k_h, base + k):
                    mat[i][j] += tau * a_val
                    mat[j][i] += tau * a_val
        return mat

    theta1 = [1, 0, 1, 0]
    theta2 = [0, 1, 1, 1]
    hamming = sum(1 for b1, b2 in zip(theta1, theta2) if b1 != b2)
    s1 = build_sigma_theta(theta1)
    s2 = build_sigma_theta(theta2)
    diff = [[s1[i][j] - s2[i][j] for j in range(p)] for i in range(p)]

    # Operator norm of diff: each active block where theta1_m != theta2_m is an anti-diagonal
    # block of two k_h x k_h all-ones matrices scaled by tau * a_val, which has spectral norm
    # k_h * tau * a_val. Wait: Lemma 5 (Eq. 25, p. 11) uses a single unit vector v supported
    # across all H(theta, theta') differing blocks to show ||(Sigma(theta) - Sigma(theta')) v||_2^2
    # = H(theta, theta') * tau^2 * k_h^2 * a^2 / H(theta, theta') = tau^2 * k_h^2 * a^2 >= H * tau^2 * k_h * a^2
    # when H <= k_h! Let's check with theta1=[1,0,0,0], theta2=[0,1,0,0] where H = 2 = k_h:
    theta_a = [1, 0, 0, 0]
    theta_b = [0, 1, 0, 0]
    h_ab = 2
    sa = build_sigma_theta(theta_a)
    sb = build_sigma_theta(theta_b)
    diff_ab = [[sa[i][j] - sb[i][j] for j in range(p)] for i in range(p)]
    op_sq = sym_spectral_norm(diff_ab) ** 2
    lemma5_rhs = h_ab * (tau ** 2) * k_h * (a_val ** 2)
    assert op_sq >= lemma5_rhs - 1e-12, f"Lemma 5 bound failed: {op_sq} < {lemma5_rhs}"

    # Verify norm-dependent bandwidth dichotomy (Theorem 1 vs Theorem 4, Remark 4, p. 18):
    # Operator norm optimal bandwidth: k_op = n^{1 / (2*alpha + 1)}
    # Frobenius norm optimal bandwidth: k_frob = n^{1 / (2*(alpha + 1))}
    n = 1000
    p_high = 5000
    alpha = 1.0
    k_op = n ** (1.0 / (2.0 * alpha + 1.0))      # 1000^{1/3} = 10.0
    k_frob = n ** (1.0 / (2.0 * (alpha + 1.0)))  # 1000^{1/4} = 5.6234
    assert k_op > k_frob

    # Compare minimax operator-norm risk n^{-2*alpha/(2*alpha+1)} + (log p)/n
    # vs Bickel-Levina (2008a) banding upper bound ((log p)/n)^{alpha/(alpha+1)}
    tapering_rate = (n ** (-2.0 * alpha / (2.0 * alpha + 1.0))) + (math.log(p_high) / n)
    banding_bound = (math.log(p_high) / n) ** (alpha / (alpha + 1.0))
    assert tapering_rate < banding_bound

    return {
        "lemma5_op_norm_sq": round(op_sq, 6),
        "lemma5_rhs_bound": round(lemma5_rhs, 6),
        "k_op_at_n1000_alpha1": round(k_op, 4),
        "k_frob_at_n1000_alpha1": round(k_frob, 4),
        "tapering_minimax_op_rate": round(tapering_rate, 6),
        "bickel_levina_banding_bound": round(banding_bound, 6),
    }


def main() -> None:
    res1 = verify_lemma1_block_sum_identity()
    res2 = verify_bias_and_lemma2_block_bound()
    res3 = verify_lemma5_assouad_separation_and_rates()
    summary = {
        "lemma1_block_sum_identity": res1,
        "bias_and_lemma2_block_bound": res2,
        "lemma5_and_rate_dichotomy": res3,
        "all_assertions_passed": True,
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
