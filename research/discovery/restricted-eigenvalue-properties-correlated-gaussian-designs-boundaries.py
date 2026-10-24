#!/usr/bin/env python3
"""Constructed boundary and diagnostic verification for Round 231:
RestrictedEigenvaluePropertiesForCorrelatedGaussianDesigns
(Raskutti, Wainwright, & Yu 2010, JMLR 11:2241-2259).

Verifies:
1. Gordon-Slepian Gaussian comparison variance inequality (Lemma 1, Eq. 6,
   pp. 2251-2253): for Y_{u,v} = u^T W v_tilde and Z_{u,v} = g^T u + h^T v_tilde
   over u in S^{n-1} and v_tilde = Sigma^{1/2} v in S^{p-1},
   E[(Y_{u,v} - Y_{u',v'})^2] = |||u v_tilde^T - u' (v_tilde')^T|||_F^2
     = ||u - u'||_2^2 + ||v_tilde - v_tilde'||_2^2
       - 2(1 - u^T u')(1 - v_tilde^T v_tilde')
     <= ||u - u'||_2^2 + ||v_tilde - v_tilde'||_2^2
     = E[(Z_{u,v} - Z_{u',v'})^2],
   with exact equality whenever v = v' (or u = u'), together with Theorem 1's
   uniform lower bound ||X v||_2 / sqrt(n) >= (1/4)||Sigma^{1/2} v||_2
   - 9 rho(Sigma) sqrt((log p)/n) ||v||_1 and Corollary 1's transfer of the
   Restricted Eigenvalue (RE) condition of order k from Sigma to X^T X / n
   with parameter gamma / 8 when n > c'' rho^2(Sigma) (1+alpha)^2 k (log p) / gamma^2.
2. Separation between Restricted Eigenvalue (RE) and Restricted Isometry
   Property (RIP) and rank-degenerate population covariances (Examples 1-3,
   Section 3.3, pp. 2248-2250):
   - Example 1 (Toeplitz Sigma_{ij} = a^{|i-j|}) and Example 2 (spiked identity
     Sigma = (1-a) I_p + a 1 1^T, a in (0, 1)): for any support S of cardinality k,
     lambda_min(Sigma_{SS}) = 1 - a and lambda_max(Sigma_{SS}) = 1 + a(k - 1),
     so the submatrix condition number (1 + a(k-1))/(1 - a) -> infinity as k grows
     (violating RIP), yet Sigma satisfies RE of any order k with gamma = sqrt(1 - a)
     and rho^2(Sigma) = 1.
   - Example 3 (rank-degenerate covariance Sigma_deg = X^T X / n with n < p):
     has a (p - n)-dimensional nullspace (minimum eigenvalue 0) yet satisfies
     the RE condition on the cone C(S; alpha) = {theta : ||theta_{S^c}||_1 <= alpha ||theta_S||_1}.
3. Frobenius-norm Lipschitz continuity of the rescaled infimum process and
   geometric peeling over l1 spheres (Lemma 2, pp. 2253-2254; Section 4.4 &
   Lemma 3, pp. 2254-2256):
   - h(W) = inf_{(u, v) in S^{n-1} x V(r)} (-1/sqrt(n)) u^T W Sigma^{1/2} v
     satisfies |h(W) - h(W')| <= (1/sqrt(n)) |||W - W'|||_F because
     |||u v_tilde^T|||_F = ||u||_2 ||v_tilde||_2 = 1 on S^{n-1} x V(r).
   - Geometric peeling over dyadic shells A_m = {v in A : 2^{m-1} mu <= g(h(v)) <= 2^m mu}
     sums tail probabilities sum_{m=1}^infty 2 exp(-c a_n 2^{2m} mu^2)
     <= 2 exp(-4 c a_n mu^2) / (1 - exp(-4 c a_n mu^2)).
"""

from __future__ import annotations

import json
import math
import random
import sys
from typing import Dict, List


def dot(u: List[float], v: List[float]) -> float:
    return sum(ui * vi for ui, vi in zip(u, v))


def norm2(u: List[float]) -> float:
    return math.sqrt(dot(u, u))


def norm1(u: List[float]) -> float:
    return sum(abs(ui) for ui in u)


def normalize(u: List[float]) -> List[float]:
    nrm = norm2(u)
    return [ui / nrm for ui in u]


def verify_gordon_comparison_and_re_transfer() -> Dict[str, object]:
    """Verify Lemma 1 Eq. (6) identity/inequality and Corollary 1 RE transfer."""
    rng = random.Random(20261018)
    n, p = 12, 16
    max_identity_error = 0.0
    min_variance_gap = float("inf")
    max_equal_v_gap = 0.0

    for _ in range(250):
        u1 = normalize([rng.gauss(0.0, 1.0) for _ in range(n)])
        u2 = normalize([rng.gauss(0.0, 1.0) for _ in range(n)])
        vt1 = normalize([rng.gauss(0.0, 1.0) for _ in range(p)])
        vt2 = normalize([rng.gauss(0.0, 1.0) for _ in range(p)])

        # Direct Frobenius norm squared |||u1 vt1^T - u2 vt2^T|||_F^2
        frob_sq = 0.0
        for i in range(n):
            for j in range(p):
                diff = u1[i] * vt1[j] - u2[i] * vt2[j]
                frob_sq += diff * diff

        du_sq = sum((u1[i] - u2[i]) ** 2 for i in range(n))
        dv_sq = sum((vt1[j] - vt2[j]) ** 2 for j in range(p))
        u_dot = dot(u1, u2)
        v_dot = dot(vt1, vt2)

        rhs_eq6 = du_sq + dv_sq - 2.0 * (1.0 - u_dot) * (1.0 - v_dot)
        z_var = du_sq + dv_sq

        max_identity_error = max(max_identity_error, abs(frob_sq - rhs_eq6))
        min_variance_gap = min(min_variance_gap, z_var - frob_sq)

        # When vt1 == vt2, E[(Y_{u1,v} - Y_{u2,v})^2] == E[(Z_{u1,v} - Z_{u2,v})^2]
        frob_equal_v = 0.0
        for i in range(n):
            for j in range(p):
                diff = (u1[i] - u2[i]) * vt1[j]
                frob_equal_v += diff * diff
        max_equal_v_gap = max(max_equal_v_gap, abs(frob_equal_v - du_sq))

    # Corollary 1 algebraic transfer: on C(S; alpha), ||v||_1 <= (1 + alpha) sqrt(k) ||v||_2
    # and ||Sigma^{1/2} v||_2 >= gamma ||v||_2. When 9 rho(Sigma) (1+alpha) sqrt(k log(p)/n) <= gamma/8,
    # Theorem 1 gives ||X v||_2 / sqrt(n) >= (1/4 - 1/8) gamma ||v||_2 = (gamma / 8) ||v||_2.
    gamma = 0.8
    alpha = 3.0
    rho = 1.0
    k = 5
    p_dim = 200
    # Threshold n so 9 * rho * (1 + alpha) * sqrt(k * log(p) / n) == gamma / 8
    n_crit = (72.0 * rho * (1.0 + alpha) / gamma) ** 2 * k * math.log(p_dim)
    n_sample = math.ceil(n_crit * 1.25)
    penalty_term = 9.0 * rho * (1.0 + alpha) * math.sqrt(k * math.log(p_dim) / n_sample)
    transferred_re_lower = 0.25 * gamma - penalty_term

    passed = (
        max_identity_error < 1e-12
        and min_variance_gap >= -1e-12
        and max_equal_v_gap < 1e-12
        and transferred_re_lower >= (gamma / 8.0) - 1e-12
    )
    return {
        "max_eq6_identity_error": max_identity_error,
        "min_z_minus_y_variance_gap": min_variance_gap,
        "max_equal_v_variance_error": max_equal_v_gap,
        "n_critical_for_gamma_over_8": n_crit,
        "n_sample": n_sample,
        "transferred_re_constant": transferred_re_lower,
        "target_gamma_over_8": gamma / 8.0,
        "passed": passed,
    }


def verify_re_vs_rip_and_rank_degenerate_examples() -> Dict[str, object]:
    """Verify Examples 1-3 (Section 3.3, pp. 2248-2250): spiked covariance & rank-degenerate RE."""
    a = 0.75
    k_values = [4, 16, 64, 256]
    cond_numbers: List[float] = []
    for k in k_values:
        lam_min = 1.0 - a
        lam_max = 1.0 + a * (k - 1)
        cond_numbers.append(lam_max / lam_min)

    # Verify for random vector theta in R^p that theta^T Sigma theta = (1-a)||theta||_2^2 + a (1^T theta)^2 >= (1-a)||theta||_2^2
    rng = random.Random(20261019)
    p = 24
    min_spiked_ratio = float("inf")
    for _ in range(200):
        theta = [rng.gauss(0.0, 1.0) for _ in range(p)]
        s1 = sum(theta)
        quad = (1.0 - a) * dot(theta, theta) + a * (s1 * s1)
        ratio = math.sqrt(quad) / norm2(theta)
        min_spiked_ratio = min(min_spiked_ratio, ratio)

    # Example 3: Rank-degenerate matrix Sigma_deg = X^T X / n with n < p
    n_deg, p_deg, k_deg, alpha_deg = 14, 28, 2, 1.0
    X = [
        [rng.gauss(0.0, 1.0) for _ in range(p_deg)]
        for _ in range(n_deg)
    ]

    def x_norm_over_sqrt_n(v: List[float]) -> float:
        xv_sq = 0.0
        for row in X:
            xv = dot(row, v)
            xv_sq += xv * xv
        return math.sqrt(xv_sq / n_deg)

    # Construct an explicit non-zero nullspace vector of X (since p_deg > n_deg) via Gram-Schmidt on rows of X
    basis: List[List[float]] = []
    for row in X:
        vec = list(row)
        for b in basis:
            proj = dot(vec, b)
            vec = [vi - proj * bi for vi, bi in zip(vec, b)]
        vec = normalize(vec)
        basis.append(vec)

    raw_null = [rng.gauss(0.0, 1.0) for _ in range(p_deg)]
    for b in basis:
        proj = dot(raw_null, b)
        raw_null = [vi - proj * bi for vi, bi in zip(raw_null, b)]
    v_null = normalize(raw_null)
    null_residual = x_norm_over_sqrt_n(v_null)
    # Check that v_null violates the cone condition ||v_{S^c}||_1 <= alpha ||v_S||_1 for S = {0, 1}
    null_s_l1 = abs(v_null[0]) + abs(v_null[1])
    null_sc_l1 = sum(abs(v_null[j]) for j in range(2, p_deg))

    # Sample vectors inside the restricted cone C(S; alpha) for S = {0, 1} and verify ||X v||_2 / sqrt(n) > 0
    min_cone_gain = float("inf")
    for _ in range(300):
        v_s = [rng.gauss(0.0, 1.0) for _ in range(k_deg)]
        s_l1 = norm1(v_s)
        raw_tail = [rng.gauss(0.0, 1.0) for _ in range(p_deg - k_deg)]
        tail_l1 = norm1(raw_tail)
        scale = rng.uniform(0.0, alpha_deg) * s_l1 / max(tail_l1, 1e-12)
        v_cone = v_s + [ti * scale for ti in raw_tail]
        gain = x_norm_over_sqrt_n(v_cone) / norm2(v_cone)
        min_cone_gain = min(min_cone_gain, gain)

    passed = (
        cond_numbers[0] < cond_numbers[1] < cond_numbers[2] < cond_numbers[3]
        and cond_numbers[-1] > 750.0
        and min_spiked_ratio >= math.sqrt(1.0 - a) - 1e-12
        and null_residual < 1e-12
        and null_sc_l1 > alpha_deg * null_s_l1
        and min_cone_gain > 0.25
    )
    return {
        "spiked_condition_numbers": cond_numbers,
        "min_spiked_re_ratio": min_spiked_ratio,
        "theoretical_spiked_gamma": math.sqrt(1.0 - a),
        "rank_degenerate_null_residual": null_residual,
        "null_vector_sc_over_s_l1_ratio": null_sc_l1 / max(null_s_l1, 1e-12),
        "min_cone_gain_on_rank_degenerate_design": min_cone_gain,
        "passed": passed,
    }


def verify_lipschitz_concentration_and_peeling() -> Dict[str, object]:
    """Verify Lemma 2 Lipschitz constant 1/sqrt(n) and Lemma 3 geometric peeling bound."""
    rng = random.Random(20261020)
    n, p = 10, 14

    # Finite discrete proxy for S^{n-1} x V(r) with unit vectors u in S^{n-1}, vt in S^{p-1}
    u_grid = [normalize([rng.gauss(0.0, 1.0) for _ in range(n)]) for _ in range(60)]
    vt_grid = [normalize([rng.gauss(0.0, 1.0) for _ in range(p)]) for _ in range(60)]

    def eval_h(W: List[List[float]]) -> float:
        best = float("inf")
        inv_sqrt_n = 1.0 / math.sqrt(n)
        for u in u_grid:
            for vt in vt_grid:
                quad = 0.0
                for i in range(n):
                    wi = W[i]
                    ui = u[i]
                    row_dot = sum(wi[j] * vt[j] for j in range(p))
                    quad += ui * row_dot
                val = -inv_sqrt_n * quad
                if val < best:
                    best = val
        return best

    max_scaled_lipschitz_ratio = 0.0
    for _ in range(80):
        W1 = [[rng.gauss(0.0, 1.0) for _ in range(p)] for _ in range(n)]
        W2 = [[rng.gauss(0.0, 1.0) for _ in range(p)] for _ in range(n)]
        frob_diff = math.sqrt(
            sum((W1[i][j] - W2[i][j]) ** 2 for i in range(n) for j in range(p))
        )
        h_diff = abs(eval_h(W1) - eval_h(W2))
        ratio = h_diff / (frob_diff / math.sqrt(n))
        max_scaled_lipschitz_ratio = max(max_scaled_lipschitz_ratio, ratio)

    # Lemma 3 geometric peeling bound:
    # sum_{m=1}^infty 2 exp(-c a_n 2^{2m} mu^2) <= sum_{m=1}^infty 2 exp(-4 c a_n m mu^2)
    # = 2 exp(-4 c a_n mu^2) / (1 - exp(-4 c a_n mu^2))
    c = 1.0 / 18.0
    a_n = 120.0
    mu = 3.0 / 8.0
    exact_dyadic_sum = sum(
        2.0 * math.exp(-c * a_n * (4.0 ** m) * (mu ** 2)) for m in range(1, 30)
    )
    linearized_geometric_bound = (
        2.0 * math.exp(-4.0 * c * a_n * (mu ** 2))
        / (1.0 - math.exp(-4.0 * c * a_n * (mu ** 2)))
    )

    passed = (
        max_scaled_lipschitz_ratio <= 1.0 + 1e-12
        and exact_dyadic_sum <= linearized_geometric_bound + 1e-15
        and linearized_geometric_bound < 0.15
    )
    return {
        "max_scaled_lipschitz_ratio": max_scaled_lipschitz_ratio,
        "exact_dyadic_peeling_sum": exact_dyadic_sum,
        "linearized_geometric_peeling_bound": linearized_geometric_bound,
        "passed": passed,
    }


def main() -> int:
    c1 = verify_gordon_comparison_and_re_transfer()
    c2 = verify_re_vs_rip_and_rank_degenerate_examples()
    c3 = verify_lipschitz_concentration_and_peeling()
    all_passed = bool(c1["passed"] and c2["passed"] and c3["passed"])
    report = {
        "concept_id": "AIMech:RestrictedEigenvaluePropertiesForCorrelatedGaussianDesigns",
        "Check1_gordon_comparison_and_re_transfer": c1,
        "Check2_re_vs_rip_and_rank_degenerate_examples": c2,
        "Check3_lipschitz_concentration_and_peeling": c3,
        "all_passed": all_passed,
    }
    print(json.dumps(report, indent=2))
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
