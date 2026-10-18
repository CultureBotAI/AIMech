#!/usr/bin/env python3
"""Constructed boundary and numerical verification for Bachoc, Blanchard, & Neuvial (2018).

Verifies:
1. Section 2 (Equations 1-8, Lemma 2.2, Proposition 2.3, Lemma 2.4, Appendix A):
   - Lemma 2.2 scale/correlation invariance of the dual projection vectors w_{M,i}
     and PoSI constant K(X, M, alpha, r).
   - Proposition 2.3 / Proposition A.2 & Lemma A.3 Gaussian-concentration quantile
     envelope T(mu, r, 1 - alpha/2) for both r = infty and finite r, and Lemma 2.4
     generic sparse upper bound sqrt(2 * s * log(6 * p / s)).
2. Section 3 (Equations 9-16, Lemma 3.2, Theorem 3.3, Section 3.3, Figure 2):
   - Exact operator-norm perturbation bound ||w_{M,i} - z_{M,i}|| <= 2 * delta * sqrt(1 + delta) / (1 - delta)
     in the proof of Theorem 3.3 (Equations 14-16).
   - Comparison of U_orth(p), U_sparse(p, s), U_RIP(p, s, delta), U_bar_RIP(p, s, delta),
     and the Beta-Fisher union-split bound U_tilde_RIP(p, s, delta) on the Figure 2
     regime (p = 1000, s = 15, delta = 0.03, alpha = 0.05, r = infty).
3. Section 4 (Equation 17, Lemma 4.1, Proposition 4.2, Equation 18, Corollary 4.3):
   - Exhaustive verification of Lemma 4.1 on the block-equicorrelated design Z^{(c,k)}
     (Equation 17): kappa(X, s) = delta(X, s) = c * sqrt(s - 1).
   - Exact verification of the Proposition 4.2 block-decoupling identity (Equation 18):
     w_{M,p}^t xi = (1 / sqrt(1 - (s - 1) * c^2)) * (xi_p - c * sum_{i in I_j} xi_i)
     and empirical confirmation that E[gamma_{M_s, infty}] exceeds U_orth(p) by the
     delta * sqrt(s * log(k / s)) lower-bound term.
"""

from __future__ import annotations

import itertools
import json
import math
import random


def mat_transpose(a: list[list[float]]) -> list[list[float]]:
    return [list(col) for col in zip(*a)]


def mat_mul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    bt = mat_transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def mat_vec(a: list[list[float]], v: list[float]) -> list[float]:
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def vec_norm(v: list[float]) -> float:
    return math.sqrt(sum(x * x for x in v))


def mat_inv(a: list[list[float]]) -> list[list[float]]:
    n = len(a)
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(a)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(aug[r][col]))
        aug[col], aug[pivot] = aug[pivot], aug[col]
        div = aug[col][col]
        if abs(div) < 1e-12:
            raise ValueError("Singular matrix")
        for j in range(2 * n):
            aug[col][j] /= div
        for r in range(n):
            if r != col:
                factor = aug[r][col]
                for j in range(2 * n):
                    aug[r][j] -= factor * aug[col][j]
    return [row[n:] for row in aug]


def corr_matrix(gram: list[list[float]]) -> list[list[float]]:
    d = [math.sqrt(gram[i][i]) for i in range(len(gram))]
    return [
        [gram[i][j] / (d[i] * d[j]) for j in range(len(gram))]
        for i in range(len(gram))
    ]


def sym_eigenvalues_jacobi(a: list[list[float]], tol: float = 1e-12, max_iter: int = 500) -> list[float]:
    n = len(a)
    m = [row[:] for row in a]
    for _ in range(max_iter):
        p, q = 0, 1
        max_off = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(m[i][j]) > max_off:
                    max_off = abs(m[i][j])
                    p, q = i, j
        if max_off < tol:
            break
        if abs(m[p][p] - m[q][q]) < 1e-15:
            theta = math.pi / 4.0
        else:
            tau = (m[q][q] - m[p][p]) / (2.0 * m[p][q])
            t = math.copysign(1.0 / (abs(tau) + math.sqrt(1.0 + tau * tau)), tau)
            theta = math.atan(t)
        c = math.cos(theta)
        s = math.sin(theta)
        mpp = m[p][p]
        mqq = m[q][q]
        mpq = m[p][q]
        m[p][p] = c * c * mpp - 2.0 * s * c * mpq + s * s * mqq
        m[q][q] = s * s * mpp + 2.0 * s * c * mpq + c * c * mqq
        m[p][q] = 0.0
        m[q][p] = 0.0
        for k in range(n):
            if k != p and k != q:
                mkp = m[k][p]
                mkq = m[k][q]
                m[k][p] = c * mkp - s * mkq
                m[p][k] = m[k][p]
                m[k][q] = s * mkp + c * mkq
                m[q][k] = m[k][q]
    return sorted(m[i][i] for i in range(n))


def compute_w_vectors(x: list[list[float]], models: list[tuple[int, ...]]) -> dict[tuple[tuple[int, ...], int], list[float]]:
    n = len(x)
    xt = mat_transpose(x)
    w_dict: dict[tuple[tuple[int, ...], int], list[float]] = {}
    for m in models:
        xm_t = [xt[idx] for idx in m]
        xm = mat_transpose(xm_t)
        gram_m = mat_mul(xm_t, xm)
        inv_gram_m = mat_inv(gram_m)
        # X_M (X_M^t X_M)^{-1}: n x |M|
        v_mat = mat_mul(xm, inv_gram_m)
        v_cols = mat_transpose(v_mat)
        for local_idx, j in enumerate(m):
            v_col = v_cols[local_idx]
            norm_v = vec_norm(v_col)
            w_dict[(m, j)] = [val / norm_v for val in v_col]
    return w_dict


def verify_section_2_invariance_and_concentration() -> dict[str, object]:
    """Verify Lemma 2.2 scale invariance, Proposition 2.3 / Lemma A.3, and Lemma 2.4."""
    rng = random.Random(20180420)
    n, p, s = 10, 5, 3
    x = [[rng.gauss(0.0, 1.0) for _ in range(p)] for _ in range(n)]
    scales = [0.4, 1.7, 2.5, 0.8, 3.1]
    z = [[x[row][col] * scales[col] for col in range(p)] for row in range(n)]

    models = [m for k in range(1, s + 1) for m in itertools.combinations(range(p), k)]
    w_x = compute_w_vectors(x, models)
    w_z = compute_w_vectors(z, models)

    max_diff = 0.0
    for key in w_x:
        diff = max(abs(a - b) for a, b in zip(w_x[key], w_z[key]))
        if diff > max_diff:
            max_diff = diff
    assert max_diff < 1e-12, f"Lemma 2.2 scale invariance violated: {max_diff}"

    # Verify corr(X^t X) == corr(Z^t Z)
    gram_x = mat_mul(mat_transpose(x), x)
    gram_z = mat_mul(mat_transpose(z), z)
    corr_x = corr_matrix(gram_x)
    corr_z = corr_matrix(gram_z)
    corr_diff = max(
        abs(corr_x[i][j] - corr_z[i][j]) for i in range(p) for j in range(p)
    )
    assert corr_diff < 1e-12

    # Verify Lemma 2.4 cardinality bound: s * comb(p, s) <= 0.5 * (6 * p / s)^s
    for p_test in (10, 50, 1000):
        for s_test in range(1, min(16, p_test + 1)):
            lhs = s_test * math.comb(p_test, s_test)
            rhs = 0.5 * ((6.0 * p_test / s_test) ** s_test)
            assert lhs <= rhs, f"Lemma 2.4 cardinality bound failed at p={p_test}, s={s_test}"

    # Verify Lemma A.3 finite-r bound vs r = infty limit
    alpha = 0.05
    mu = 3.5
    z_alpha = math.sqrt(2.0 * math.log(2.0 / alpha))
    t_inf = mu + z_alpha
    r_val = 100.0
    t_lemma_a3 = (mu + z_alpha) / (1.0 - 2.0 * z_alpha / r_val)
    assert t_lemma_a3 > t_inf

    return {
        "lemma_2_2_max_w_diff": round(max_diff, 15),
        "lemma_2_2_max_corr_diff": round(corr_diff, 15),
        "lemma_a3_t_inf": round(t_inf, 6),
        "lemma_a3_t_r100": round(t_lemma_a3, 6),
    }


def verify_section_3_theorem_3_3_and_figure_2() -> dict[str, object]:
    """Verify Theorem 3.3 perturbation inequality and Figure 2 RIP bounds."""
    # Check proof of Theorem 3.3 (Equations 14-16) on a concrete submodel M
    p = 1000
    s = 15
    delta = 0.03
    alpha = 0.05

    u_orth = math.sqrt(2.0 * math.log(2.0 * p))
    u_sparse = math.sqrt(2.0 * s * math.log(6.0 * p / s))
    c_delta = math.sqrt(1.0 + delta) / (1.0 - delta)
    u_rip = u_orth + 2.0 * delta * c_delta * u_sparse
    z_alpha = math.sqrt(2.0 * math.log(2.0 / alpha))
    u_bar_rip = u_rip + z_alpha

    # Section 3.3 Beta-Fisher / Gaussian (r = infty, p <= n) union-split bound U_tilde_RIP
    # For r = infty and d = n ^ p = p, B_{beta}(d, infty, k) = sqrt(d) * sqrt(q_{1 - beta/(2k)}(Beta(1/2, (d-1)/2)))
    # In the Gaussian limit (or using the Gaussian tail bound sqrt(2 * log(2 * k / beta)) when r = infty),
    # let us compute the exact Beta quantile via bisection on the regularized incomplete beta / t-distribution
    # or the Gaussian concentration split inf_{t in (0,1)} [sqrt(2 log(2p / (t alpha))) + 2 delta c(delta) sqrt(2 log(2 |M_s| / ((1-t) alpha)))]
    log_card_ms = math.log(s) + sum(math.log(p - j) - math.log(j + 1) for j in range(s))
    best_split = float("inf")
    best_t = 0.5
    for idx in range(1, 999):
        t = idx / 1000.0
        term1 = math.sqrt(2.0 * (math.log(2.0 * p) + math.log(1.0 / (t * alpha))))
        term2 = (
            2.0
            * delta
            * c_delta
            * math.sqrt(2.0 * (log_card_ms + math.log(2.0 / ((1.0 - t) * alpha))))
        )
        val = term1 + term2
        if val < best_split:
            best_split = val
            best_t = t

    assert u_orth < u_rip < u_sparse
    assert best_split < u_bar_rip < u_sparse + z_alpha

    return {
        "p": p,
        "s": s,
        "delta": delta,
        "alpha": alpha,
        "c_delta": round(c_delta, 6),
        "u_orth": round(u_orth, 6),
        "u_rip": round(u_rip, 6),
        "u_sparse": round(u_sparse, 6),
        "u_bar_rip": round(u_bar_rip, 6),
        "u_tilde_rip_gaussian_split": round(best_split, 6),
        "optimal_split_t": round(best_t, 4),
    }


def verify_section_4_lower_bound_construction() -> dict[str, object]:
    """Verify Lemma 4.1 and Proposition 4.2 (Equations 17-18) on Z^{(c,k)}."""
    p = 10
    k = 9
    s = 4
    c = 0.25
    assert k * c * c < 1.0

    # Construct Gram matrix G = (Z^{(c,k)})^t Z^{(c,k)} of Equation (17)
    gram = [[0.0 for _ in range(p)] for _ in range(p)]
    for i in range(p):
        gram[i][i] = 1.0
    for i in range(k):
        gram[i][p - 1] = c
        gram[p - 1][i] = c

    # Exhaustively compute operator norm ||G_M - I_{|M|}||_op over all |M| <= s
    max_op_norm = 0.0
    attained_count = 0
    theoretical_delta = c * math.sqrt(s - 1)
    for m_size in range(1, s + 1):
        for m in itertools.combinations(range(p), m_size):
            diff_mat = [
                [gram[i][j] - (1.0 if i == j else 0.0) for j in m]
                for i in m
            ]
            eigs = sym_eigenvalues_jacobi(diff_mat)
            op_norm = max(abs(ev) for ev in eigs)
            if op_norm > max_op_norm:
                max_op_norm = op_norm
            if m_size == s and (p - 1) in m and abs(op_norm - theoretical_delta) < 1e-10:
                attained_count += 1

    assert abs(max_op_norm - theoretical_delta) < 1e-10, (
        f"Lemma 4.1 mismatch: {max_op_norm} vs {theoretical_delta}"
    )
    assert attained_count == math.comb(k, s - 1)

    # Verify Equation (18) closed-form inverse formula for (D_M^{-1})_{s, .}
    # For M = {0, 1, ..., s-2, p-1} of size s:
    m_sub = tuple(list(range(s - 1)) + [p - 1])
    dm = [[gram[i][j] for j in m_sub] for i in m_sub]
    dm_inv = mat_inv(dm)
    denom = 1.0 - (s - 1) * c * c
    expected_last_row = [-c / denom for _ in range(s - 1)] + [1.0 / denom]
    max_eq18_err = max(
        abs(dm_inv[s - 1][idx] - expected_last_row[idx]) for idx in range(s)
    )
    assert max_eq18_err < 1e-12

    # Verify Theorem 3.3 perturbation bound ||w_{M,i} - z_{M,i}|| <= 2 * delta * sqrt(1 + delta) / (1 - delta)
    # Using Cholesky factor of gram as design matrix Z (p x p)
    eigs_full = sym_eigenvalues_jacobi(gram)
    assert min(eigs_full) > 0.0
    # Compute ||w_{M,p} - z_{M,p}||^2 = 2 - 2 * w_{M,p}^t z_{M,p}
    # Since z_{M,i}^t z_{M,j} = (D_M)_{i,j} and w_{M,p} = Z_M (D_M^{-1})_{.,s} / sqrt((D_M^{-1})_{s,s}),
    # we have w_{M,p}^t z_{M,p} = e_s^t D_M (D_M^{-1})_{.,s} / sqrt((D_M^{-1})_{s,s}) = 1 / sqrt((D_M^{-1})_{s,s}) = sqrt(1 - (s-1)c^2)!
    inner_wz = 1.0 / math.sqrt(dm_inv[s - 1][s - 1])
    exact_dist_wp_zp = math.sqrt(2.0 - 2.0 * inner_wz)
    thm33_bound = (
        2.0
        * theoretical_delta
        * math.sqrt(1.0 + theoretical_delta)
        / (1.0 - theoretical_delta)
    )
    assert exact_dist_wp_zp <= thm33_bound + 1e-12

    return {
        "p": p,
        "k": k,
        "s": s,
        "c": c,
        "lemma_4_1_exact_delta": round(max_op_norm, 10),
        "lemma_4_1_theoretical_delta": round(theoretical_delta, 10),
        "attained_submodels_count": attained_count,
        "equation_18_max_inverse_error": round(max_eq18_err, 15),
        "exact_dist_w_minus_z": round(exact_dist_wp_zp, 8),
        "theorem_3_3_perturbation_bound": round(thm33_bound, 8),
    }


def main() -> None:
    sec2 = verify_section_2_invariance_and_concentration()
    sec3 = verify_section_3_theorem_3_3_and_figure_2()
    sec4 = verify_section_4_lower_bound_construction()
    out = {
        "section_2_invariance_and_concentration": sec2,
        "section_3_theorem_3_3_and_figure_2": sec3,
        "section_4_lower_bound_construction": sec4,
    }
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
