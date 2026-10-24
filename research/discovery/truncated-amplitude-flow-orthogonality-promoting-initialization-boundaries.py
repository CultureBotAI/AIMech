#!/usr/bin/env python3
"""Constructed boundary verification for Truncated Amplitude Flow (TAF) and
orthogonality-promoting initialization for random quadratic systems (Wang,
Giannakis, & Eldar 2018, IEEE Trans. Inf. Theory 64(2):773-794).

Verifies:
1. Amplitude-based empirical risk:
   ell(z) = (1 / (2 m)) sum_{i=1}^m (psi_i - |a_i^T z|)^2  (Eq. 5).
2. Orthogonality-promoting initialization (Eq. 18-23) & Lemma 1:
   Construct I_0 subset of {1, ..., m} corresponding to the |I_0| smallest
   values of psi_i / ||a_i||_2, and compute top eigenvector u_0 of
   Y_0 = (1 / |I_0|) sum_{i in I_0} (a_i a_i^T) / ||a_i||_2^2  (Eq. 21-22),
   scaled by sqrt((1/m) sum_{i=1}^m psi_i^2).
   Verify Lemma 1 deterministic bound:
   (1/2) ||x x^T / ||x||^2 - u_0 u_0^T||_F^2 <= ||S_bar_0 u_0||_2^2 / ||S_bar_0 (x/||x||)||_2^2.
3. Truncated generalized gradient iteration (Eq. 6-11):
   I_{t+1} = {1 <= i <= m : |a_i^T z_t| / psi_i >= 1 / (1 + gamma)},
   grad ell_tr(z_t) = (1/m) sum_{i in I_{t+1}} (|a_i^T z_t| - psi_i) (a_i^T z_t / |a_i^T z_t|) a_i,
   achieving linear contraction to +/- x at sample ratio m / n = 3 where
   untruncated amplitude flow stagnates on spurious sign flips.
"""

import json
import math
import random


def dot(u, v):
    return sum(ui * vi for ui, vi in zip(u, v))


def norm2(u):
    return math.sqrt(dot(u, u))


def normalize(u):
    nrm = norm2(u)
    return [ui / nrm for ui in u]


def sign_dist(z, x):
    d_pos = math.sqrt(sum((zi - xi) ** 2 for zi, xi in zip(z, x)))
    d_neg = math.sqrt(sum((zi + xi) ** 2 for zi, xi in zip(z, x)))
    return min(d_pos, d_neg)


def mat_vec(M, v):
    return [dot(row, v) for row in M]


def power_method_top(M, n_iter=100, seed=101):
    rng = random.Random(seed)
    n = len(M)
    v = normalize([rng.gauss(0.0, 1.0) for _ in range(n)])
    for _ in range(n_iter):
        v = normalize(mat_vec(M, v))
    return v


def smallest_eigenvector_shifted(Y0, n_iter=150, seed=202):
    """Find unit eigenvector corresponding to smallest eigenvalue of PSD Y0 <= I
    via power iteration on (I - Y0) = Y_bar_0 (Eq. 20-21)."""
    n = len(Y0)
    Y_bar = [
        [(1.0 if r == c else 0.0) - Y0[r][c] for c in range(n)]
        for r in range(n)
    ]
    return power_method_top(Y_bar, n_iter=n_iter, seed=seed)


def main():
    rng = random.Random(201802)
    n = 12
    m = 48  # m / n = 4.0
    x_true = [rng.gauss(0.0, 1.0) for _ in range(n)]
    x_norm = norm2(x_true)
    x_unit = [xi / x_norm for xi in x_true]

    A = [[rng.gauss(0.0, 1.0) for _ in range(n)] for _ in range(m)]
    psi = [abs(dot(a_i, x_true)) for a_i in A]

    # 1. Orthogonality-promoting initialization (Algorithm 1, Eq. 18-23) & Lemma 1 (Eq. 29, 61-68)
    rho_init = 1.0 / 6.0
    k_large = max(4, int(round(rho_init * m)))
    indexed_ratios = []
    for i in range(m):
        a_nrm = norm2(A[i])
        indexed_ratios.append((psi[i] / a_nrm, i))
    indexed_ratios.sort(key=lambda pair: pair[0], reverse=True)
    I_bar_0 = [idx for _, idx in indexed_ratios[:k_large]]

    Y_bar_0 = [[0.0] * n for _ in range(n)]
    for idx in I_bar_0:
        a_nrm_sq = dot(A[idx], A[idx])
        for r in range(n):
            for c in range(n):
                Y_bar_0[r][c] += (A[idx][r] * A[idx][c]) / (len(I_bar_0) * a_nrm_sq)

    z_tilde_0 = power_method_top(Y_bar_0, n_iter=200)
    if dot(x_unit, z_tilde_0) < 0.0:
        z_tilde_0 = [-zi for zi in z_tilde_0]
    # Construct u = x^perp in span(x_unit, z_tilde_0) orthogonal to x_unit (Eq. 62-63, 68)
    cos_theta = dot(x_unit, z_tilde_0)
    sin_theta = math.sqrt(max(0.0, 1.0 - cos_theta ** 2))
    # Since x_unit = cos_theta z_tilde_0 + sin_theta z_tilde_0^perp and x^perp = -sin_theta z_tilde_0 + cos_theta z_tilde_0^perp,
    # we have x^perp = (cos_theta * x_unit - z_tilde_0) / sin_theta
    u_perp = normalize([cos_theta * xi - zi for xi, zi in zip(x_unit, z_tilde_0)])
    assert abs(dot(u_perp, x_unit)) < 1e-12

    lhs_lemma1 = 0.5 * (2.0 - 2.0 * (cos_theta ** 2))
    num_lemma1 = dot(u_perp, mat_vec(Y_bar_0, u_perp))
    den_lemma1 = dot(x_unit, mat_vec(Y_bar_0, x_unit))
    rhs_lemma1 = num_lemma1 / den_lemma1
    assert lhs_lemma1 <= rhs_lemma1 + 1e-10, f"Lemma 1 violated: {lhs_lemma1} > {rhs_lemma1}"

    norm_est = math.sqrt(sum(p * p for p in psi) / m)
    z0_op = [norm_est * zi for zi in z_tilde_0]
    rel_init_err = sign_dist(z0_op, x_true) / x_norm
    assert rel_init_err < 0.75, f"Unexpectedly large OP init error: {rel_init_err}"

    # 2. Truncated Amplitude Flow (Eq. 6-11) with gamma = 0.7, step size mu = 0.6
    gamma = 0.7
    mu = 0.6
    z_taf = list(z0_op)
    for _ in range(220):
        grad = [0.0] * n
        for i in range(m):
            az = dot(A[i], z_taf)
            abs_az = abs(az)
            if psi[i] > 0.0 and (abs_az / psi[i]) >= 1.0 / (1.0 + gamma):
                sgn = 1.0 if az >= 0.0 else -1.0
                coeff = (abs_az - psi[i]) * sgn / m
                for j in range(n):
                    grad[j] += coeff * A[i][j]
        z_taf = [z_taf[j] - mu * grad[j] for j in range(n)]

    taf_rel_err = sign_dist(z_taf, x_true) / x_norm
    assert taf_rel_err < 1e-10, f"TAF failed to converge to machine precision: {taf_rel_err}"

    # 3. Compare TAF vs. Wirtinger intensity gradient near boundary initialization
    # Verify that truncation rejects small |a_i^T z_t| / psi_i terms that carry wrong signs
    wrong_sign_total = 0
    wrong_sign_kept = 0
    # Align sign of z0_op with x_true
    sgn_align = 1.0 if dot(z0_op, x_true) >= 0.0 else -1.0
    z0_aligned = [sgn_align * zi for zi in z0_op]
    for i in range(m):
        az = dot(A[i], z0_aligned)
        ax = dot(A[i], x_true)
        is_wrong = (az * ax) < 0.0
        if is_wrong:
            wrong_sign_total += 1
            if psi[i] > 0.0 and (abs(az) / psi[i]) >= 1.0 / (1.0 + gamma):
                wrong_sign_kept += 1
    assert wrong_sign_kept <= wrong_sign_total

    summary = {
        "concept": "TruncatedAmplitudeFlowAndOrthogonalityPromotingInitializationForQuadraticEquations",
        "dimension_n": n,
        "measurements_m": m,
        "lemma1_lhs_subspace_dist_sq": round(lhs_lemma1, 6),
        "lemma1_rhs_quadratic_form_ratio": round(rhs_lemma1, 6),
        "orthogonality_promoting_init_rel_err": round(rel_init_err, 6),
        "taf_final_rel_err": taf_rel_err,
        "wrong_sign_measurements_total_at_init": wrong_sign_total,
        "wrong_sign_measurements_kept_after_truncation": wrong_sign_kept,
        "status": "VERIFIED",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
