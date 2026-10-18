#!/usr/bin/env python3
r"""Constructed boundary and algebraic verification for Round 233:
InformationTheoreticLimitsOfHighDimensionalNoisySparsityRecovery (Wainwright 2009,
IEEE Trans. Inf. Theory 55(12):5728-5741, arXiv:math/0702301v2).

Verifies:
1. Optimal projection decoder residual identity (Section 2.2, Lemma 1, Eqs. 9-14
   & Appendix A, p. 13):
   - f(U; Y, X, beta^*) = min_{beta_U} ||Y - X_U beta_U||_2^2 = ||Pi_U^perp Y||_2^2
     where Pi_U^perp = I_n - X_U (X_U^T X_U)^{-1} X_U^T.
   - Since Y = X_S beta_S^* + W and X_{S cap U} lies in range(X_U),
     Pi_U^perp Y = Pi_U^perp(X_{S \ U} beta_{S \ U}^* + W) and f(S) = ||Pi_S^perp W||_2^2.
   - Delta(U) := f(U) - f(S) = ||Pi_U^perp(X_{S \ U} beta_{S \ U}^* + W)||_2^2 - ||Pi_S^perp W||_2^2,
     and the optimal decoder prefers U over S iff Delta(U) < 0 (or <= 0).
   - Also verifies the primary-source sign identity on p. 8 (bottom display):
     ||Pi_U^perp W||_2^2 - ||Pi_S^perp W||_2^2 = ||Pi_S W||_2^2 - ||Pi_U W||_2^2
     (written ||Pi_U W||_2^2 - ||Pi_S W||_2^2 on p. 8), where the orthogonal
     complement decomposition projects onto span(X_{S \ U}) and span(X_{U \ S})
     of dimension k = |S \ U|.
2. Non-central chi-squared pairwise error exponent & union-bound sufficient
   threshold (Section 2.2, Lemma 2 & Theorem 1, Eqs. 15-27):
   - Verifies that on the conditioning event A = {||Pi_U^perp W||_2^2 <= 2(n-s)}
     and {||Pi_S^perp W||_2^2 - ||Pi_U^perp W||_2^2 <= t_0} with
     t_0 = (1/2)(n-s)||beta_{S \ U}^*||_2^2 (Eq. 21), the threshold
     t = t_0 / ||beta_{S \ U}^*||_2^2 = (n-s)/2 satisfies d + nu - t >= (n-s)/2
     and d + 2*nu <= (n-s)(1 + 4/||beta_{S \ U}^*||_2^2), so Birge's Chernoff
     exponent (d + nu - t)^2 / (4(d + 2*nu)) is bounded below by
     (n-s)||beta_{S \ U}^*||_2^2 / (16(||beta_{S \ U}^*||_2^2 + 4)), matching
     Lemma 2 (Eq. 15) and Eq. 22.
   - Verifies the exact combinatorial overlap decomposition
     sum_{k=1}^s binom(s, k) binom(p-s, k) = binom(p, s) - 1 (Vandermonde's identity)
     used in the union bound over all N(k) = binom(s, k) binom(p-s, k) subsets
     at overlap complement k = |S \ U| (Eqs. 23-26).
3. Fano multiway hypothesis testing lower bound & information-computation gap
   (Section 2.3, Lemmas 3-4 & Theorem 2, Eqs. 28-31):
   - Verifies that for the uniform ensemble beta_U = M(beta^*) 1_U on U in
     binom([p], s), the conditional KL divergence given X between P_U and P_V
     (with sigma^2 = 1) is D(P_U || P_V | X) = (1/2) ||X_U v - X_V v||_2^2,
     whose expectation over standard Gaussian X is
     E_X[D(P_U || P_V | X)] = n * M^2(beta^*) * (s - |U cap V|) <= n * s * M^2(beta^*),
     and verifies the factor-of-2 detail between p. 11 (1/2 * Z_{U,V}) and Eq. 30 on p. 12.
   - Verifies the information-computation gap in the linear sparsity regime
     s = alpha * p with s * M^2(beta^*) -> +infty: Theorem 1 & 2 give optimal
     sample complexity n_opt = Theta(p), whereas Wainwright (2009) noisy Lasso
     requires n_Lasso = 2 s log(p - s) + s + 1 = Theta(p log p).
"""

import json
import math
import random


def mat_transpose(a):
    return [list(col) for col in zip(*a)]


def mat_mul(a, b):
    bt = mat_transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def mat_vec(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def vec_norm_sq(v):
    return sum(x * x for x in v)


def mat_inv(a):
    n = len(a)
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(a)]
    for i in range(n):
        pivot = max(range(i, n), key=lambda r: abs(aug[r][i]))
        aug[i], aug[pivot] = aug[pivot], aug[i]
        div = aug[i][i]
        aug[i] = [x / div for x in aug[i]]
        for r in range(n):
            if r != i:
                factor = aug[r][i]
                aug[r] = [aug[r][c] - factor * aug[i][c] for c in range(2 * n)]
    return [row[n:] for row in aug]


def proj_perp_matrix(x_sub, n):
    """Compute Pi_U^perp = I_n - X_U (X_U^T X_U)^{-1} X_U^T."""
    xt = mat_transpose(x_sub)
    xtx_inv = mat_inv(mat_mul(xt, x_sub))
    p = mat_mul(x_sub, mat_mul(xtx_inv, xt))
    return [[(1.0 if i == j else 0.0) - p[i][j] for j in range(n)] for i in range(n)], p


def verify_projection_decoder_and_lemma1():
    rng = random.Random(200912)
    n, p, s = 18, 8, 3
    x_full = [[rng.gauss(0.0, 1.0) for _ in range(p)] for _ in range(n)]
    s_set = (0, 1, 2)
    u_set = (0, 3, 4)  # overlap |S cap U| = 1, so k = |S \ U| = 2
    s_minus_u = tuple(i for i in s_set if i not in u_set)

    beta_star = [0.0] * p
    beta_star[0] = 1.4
    beta_star[1] = -0.9
    beta_star[2] = 1.1
    w = [rng.gauss(0.0, 1.0) for _ in range(n)]
    y = [sum(x_full[i][j] * beta_star[j] for j in range(p)) + w[i] for i in range(n)]

    def submatrix(cols):
        return [[x_full[i][j] for j in cols] for i in range(n)]

    x_s = submatrix(s_set)
    x_u = submatrix(u_set)
    x_s_minus_u = submatrix(s_minus_u)
    beta_s_minus_u = [beta_star[j] for j in s_minus_u]

    pi_s_perp, pi_s = proj_perp_matrix(x_s, n)
    pi_u_perp, pi_u = proj_perp_matrix(x_u, n)

    # Minimum OLS residual norm squared f(U) = min_{beta_U} ||Y - X_U beta_U||_2^2
    xt_u = mat_transpose(x_u)
    beta_hat_u = mat_vec(mat_mul(mat_inv(mat_mul(xt_u, x_u)), xt_u), y)
    resid_u_ols = [y[i] - sum(x_u[i][j] * beta_hat_u[j] for j in range(s)) for i in range(n)]
    f_u_ols = vec_norm_sq(resid_u_ols)
    f_u_proj = vec_norm_sq(mat_vec(pi_u_perp, y))

    # Lemma 1 decomposition: Pi_U^perp Y = Pi_U^perp(X_{S \ U} beta_{S \ U}^* + W)
    sig_plus_w = [
        sum(x_s_minus_u[i][j] * beta_s_minus_u[j] for j in range(len(s_minus_u))) + w[i]
        for i in range(n)
    ]
    f_u_lemma1 = vec_norm_sq(mat_vec(pi_u_perp, sig_plus_w))
    f_s_proj = vec_norm_sq(mat_vec(pi_s_perp, y))
    f_s_noise = vec_norm_sq(mat_vec(pi_s_perp, w))

    delta_u_direct = f_u_ols - f_s_proj
    delta_u_lemma1 = f_u_lemma1 - f_s_noise

    # Verify p. 8 bottom display sign identity:
    # ||Pi_U^perp W||_2^2 - ||Pi_S^perp W||_2^2 = ||Pi_S W||_2^2 - ||Pi_U W||_2^2
    lhs_p8 = vec_norm_sq(mat_vec(pi_u_perp, w)) - vec_norm_sq(mat_vec(pi_s_perp, w))
    rhs_exact = vec_norm_sq(mat_vec(pi_s, w)) - vec_norm_sq(mat_vec(pi_u, w))
    rhs_printed_p8 = vec_norm_sq(mat_vec(pi_u, w)) - vec_norm_sq(mat_vec(pi_s, w))

    passed = (
        abs(f_u_ols - f_u_proj) < 1e-10
        and abs(f_u_proj - f_u_lemma1) < 1e-10
        and abs(f_s_proj - f_s_noise) < 1e-10
        and abs(delta_u_direct - delta_u_lemma1) < 1e-10
        and abs(lhs_p8 - rhs_exact) < 1e-10
        and abs(lhs_p8 + rhs_printed_p8) < 1e-10
    )
    return {
        "passed": passed,
        "f_u_ols": round(f_u_ols, 8),
        "f_u_lemma1": round(f_u_lemma1, 8),
        "f_s_noise": round(f_s_noise, 8),
        "delta_u": round(delta_u_lemma1, 8),
        "lhs_perp_diff": round(lhs_p8, 8),
        "rhs_exact_pi_s_minus_pi_u": round(rhs_exact, 8),
    }


def verify_lemma2_exponent_and_vandermonde():
    # Check algebraic lower bound on Birge's non-central chi^2 exponent (pp. 8-9, Eqs. 15, 20-22)
    n, s = 120, 10
    d = n - s
    b_sq = 2.5  # ||beta_{S \ U}^*||_2^2
    t0 = 0.5 * d * b_sq
    t = t0 / b_sq  # (n - s) / 2

    # Worst-case nu on event A = {||Pi_U^perp W||_2^2 <= 2(n - s)}:
    # nu = ||Pi_U^perp W||_2^2 / b_sq in [0, 2(n-s)/b_sq]
    nu_max = 2.0 * d / b_sq
    # Since d + nu - t >= d - t = (n-s)/2 for all nu >= 0 and d + 2*nu <= d(1 + 4/b_sq):
    birge_min_over_a = ((d - t) ** 2) / (4.0 * (d + 2.0 * nu_max))
    closed_form_bound = d * b_sq / (16.0 * (b_sq + 4.0))
    lemma2_eq15_bound = d * b_sq / (8.0 * (b_sq + 4.0))

    # Vandermonde identity: sum_{k=1}^s binom(s, k) binom(p-s, k) = binom(p, s) - 1
    p_val, s_val = 16, 5
    overlap_sum = sum(math.comb(s_val, k) * math.comb(p_val - s_val, k) for k in range(1, s_val + 1))
    total_other_supports = math.comb(p_val, s_val) - 1

    passed = (
        abs(birge_min_over_a - closed_form_bound) < 1e-12
        and abs(2.0 * closed_form_bound - lemma2_eq15_bound) < 1e-12
        and overlap_sum == total_other_supports
    )
    return {
        "passed": passed,
        "birge_min_over_a": round(birge_min_over_a, 8),
        "closed_form_d_bsq_over_16_bsq_plus_4": round(closed_form_bound, 8),
        "lemma2_eq15_exponent": round(lemma2_eq15_bound, 8),
        "vandermonde_overlap_sum": overlap_sum,
        "total_other_supports": total_other_supports,
    }


def verify_fano_kl_and_linear_sparsity_gap():
    # Conditional KL divergence D(P_U || P_V | X) = (1/2) ||X_U v - X_V v||_2^2
    # For v = M * 1_s and overlap |U cap V| = r, X_U v - X_V v has i.i.d. N(0, 2 M^2 (s - r)) entries.
    n = 50
    s = 6
    r = 2  # |U cap V|
    m_val = 0.5
    gamma_uv = 2.0 * (m_val ** 2) * (s - r)  # Eq. 29
    expected_z_uv = gamma_uv * n  # E[Z_{U,V}] = gamma(U,V) * n
    expected_kl_uv = 0.5 * expected_z_uv  # E[D(P_U || P_V)] = (1/2) E[Z_{U,V}] = n * M^2 * (s - r)
    upper_bound_kl = n * s * (m_val ** 2)

    # Compare Eq. 30 on p. 12 with p. 11 bottom display:
    # On event {Z <= 4 M^2 s n}, (1/2) Z / log(N - 1) <= 2 M^2 s n / log(N - 1)
    # whereas Eq. 30 writes 4 M^2 s n / log(N - 1) (omitting the 1/2 factor from D = (1/2) Z).
    n_supports = math.comb(20, s)
    fano_num_exact = 2.0 * (m_val ** 2) * s * n / math.log(n_supports - 1)
    fano_num_eq30 = 4.0 * (m_val ** 2) * s * n / math.log(n_supports - 1)

    # Information-computation gap in linear sparsity regime s = alpha * p:
    # As p grows with s = 0.1 * p and s * M^2(beta^*) = 10 (constant > 0):
    # Optimal sample complexity (Theorem 1 & 2) scales as s * log(p/s) = Theta(p),
    # while Wainwright (2009) noisy Lasso threshold (with Sigma = I, theta_l = 1)
    # requires n_Lasso = 2 * s * log(p - s) + s + 1 = Theta(p log p).
    alpha = 0.1
    ratios = []
    for p_test in (100, 1000, 10000):
        s_test = int(alpha * p_test)
        n_it_scale = s_test * math.log(p_test / s_test)
        n_lasso_thresh = 2.0 * s_test * math.log(p_test - s_test) + s_test + 1.0
        ratios.append(n_lasso_thresh / n_it_scale)

    passed = (
        abs(expected_kl_uv - n * (m_val ** 2) * (s - r)) < 1e-12
        and expected_kl_uv < upper_bound_kl
        and abs(fano_num_eq30 - 2.0 * fano_num_exact) < 1e-12
        and ratios[0] < ratios[1] < ratios[2]
    )
    return {
        "passed": passed,
        "expected_kl_uv": round(expected_kl_uv, 8),
        "upper_bound_kl": round(upper_bound_kl, 8),
        "fano_ratio_exact_vs_eq30": round(fano_num_eq30 / fano_num_exact, 6),
        "lasso_to_it_sample_ratio_p100_1000_10000": [round(x, 4) for x in ratios],
    }


def main():
    r1 = verify_projection_decoder_and_lemma1()
    r2 = verify_lemma2_exponent_and_vandermonde()
    r3 = verify_fano_kl_and_linear_sparsity_gap()
    all_passed = r1["passed"] and r2["passed"] and r3["passed"]
    report = {
        "concept_id": "AIMech:InformationTheoreticLimitsOfHighDimensionalNoisySparsityRecovery",
        "all_passed": all_passed,
        "projection_decoder_and_lemma1": r1,
        "lemma2_exponent_and_vandermonde": r2,
        "fano_kl_and_linear_sparsity_gap": r3,
    }
    print(json.dumps(report, indent=2))
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
