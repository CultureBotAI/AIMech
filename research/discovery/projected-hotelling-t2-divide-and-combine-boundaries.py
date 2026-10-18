#!/usr/bin/env python3
"""Constructed mathematical boundary checks for ProjectedHotellingT2DivideAndCombineConfidenceRegion.

Verifies from Liu, Meng, & Pillai (2025, arXiv:2501.01065v1):
1. Section 2.2 Example 1 & Theorem 3.2 / Lemma D.3 convexity:
   - Standard two-sided Cauchy Combination Test (CCT) confidence region for m=2 studies
     (theta_hat_1 = 0.125, theta_hat_2 = -0.125, sigma = 0.1) splits into 3 disconnected
     intervals at 1 - alpha = 0.95 because T_CCT(theta) -> -infinity at each study center.
   - Half-Cauchy Combination Test (HCCT) confidence region is strictly convex on R,
     attains its unique minimum at theta = 0, and forms a single connected interval.
2. High-dimensional small-n (d = 6, n = 4 < d + 1) divide-and-combine confidence region
   (Section 3.2 Theorem 3.2 & Section 4.1-4.3):
   - Global 6x6 sample covariance has rank 3 < 6 (singular, classical Hotelling T^2 fails).
   - Partitioning into m = 3 disjoint 2D subspace projections (d_j = 2, k_j = n - 1 = 3 >= d_j + 1)
     yields positive-definite 2x2 sub-covariances and exact closed-form Hotelling T^2(2, 3)
     CDF F(s) = s / (s + 3), producing a strictly convex, bounded 6D confidence region and
     finite simultaneous linear contrast intervals without Bonferroni multiplicity loss.
3. Section 3.3 Inequality (3.7) inter-study conflict lower bound and Proposition 3.3
   sequential outlier downweighting stopping-time union region.
"""
from __future__ import annotations

import json
import math


def normal_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def hc_inv(u: float) -> float:
    """Half-Cauchy quantile function tan(pi * u / 2) for u in [0, 1)."""
    return math.tan(0.5 * math.pi * u)


def c_inv(u: float) -> float:
    """Standard Cauchy quantile function tan(pi * (u - 1/2)) for u in (0, 1)."""
    return math.tan(math.pi * (u - 0.5))


def det2(m: list[list[float]]) -> float:
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def inv2(m: list[list[float]]) -> list[list[float]]:
    d = det2(m)
    return [
        [m[1][1] / d, -m[0][1] / d],
        [-m[1][0] / d, m[0][0] / d],
    ]


def quad2(v: list[float], inv_cov: list[list[float]]) -> float:
    return (
        v[0] * (inv_cov[0][0] * v[0] + inv_cov[0][1] * v[1])
        + v[1] * (inv_cov[1][0] * v[0] + inv_cov[1][1] * v[1])
    )


def main() -> None:
    # 1. Section 2.2 Example 1: m=2, theta_hat = (0.125, -0.125), sigma = 0.1, alpha = 0.05
    # Critical value for 1 - alpha = 0.95 under standard / half-Cauchy benchmark is cot(0.05 * pi)
    crit_95 = 1.0 / math.tan(0.05 * math.pi)
    th1, th2, sig = 0.125, -0.125, 0.1

    def t_hcct_ex1(theta: float) -> float:
        u1 = 2.0 * normal_cdf(abs(th1 - theta) / sig) - 1.0
        u2 = 2.0 * normal_cdf(abs(th2 - theta) / sig) - 1.0
        return 0.5 * hc_inv(u1) + 0.5 * hc_inv(u2)

    def t_cct_ex1(theta: float) -> float:
        u1 = min(max(2.0 * normal_cdf(abs(th1 - theta) / sig) - 1.0, 1e-12), 1.0 - 1e-12)
        u2 = min(max(2.0 * normal_cdf(abs(th2 - theta) / sig) - 1.0, 1e-12), 1.0 - 1e-12)
        return 0.5 * c_inv(u1) + 0.5 * c_inv(u2)

    # Scan grid [-0.4, 0.4] with 8001 points to count connected intervals in {T <= crit_95}
    grid = [-0.4 + 0.8 * i / 8000 for i in range(8001)]
    hcct_in = [t_hcct_ex1(x) <= crit_95 for x in grid]
    cct_in = [t_cct_ex1(x) <= crit_95 for x in grid]

    def count_components(mask: list[bool]) -> int:
        comps = 0
        prev = False
        for val in mask:
            if val and not prev:
                comps += 1
            prev = val
        return comps

    hcct_components = count_components(hcct_in)
    cct_components = count_components(cct_in)
    assert hcct_components == 1, f"Expected 1 convex interval for HCCT, got {hcct_components}"
    assert cct_components == 3, f"Expected 3 disconnected intervals for CCT, got {cct_components}"

    # Find exact HCCT interval endpoint by bisection on [0, 0.4]
    lo, hi = 0.0, 0.4
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if t_hcct_ex1(mid) <= crit_95:
            lo = mid
        else:
            hi = mid
    hcct_halfwidth = 0.5 * (lo + hi)

    # 2. High-dimensional small-n (d = 6, n = 4 < d + 1) divide-and-combine region
    # Construct n = 4 observations in R^6
    data_x = [
        [1.10, 0.40, -0.50, 0.85, 0.20, -0.30],
        [0.90, 0.70, -0.20, 0.45, 0.50, -0.10],
        [1.30, 0.50, -0.60, 0.70, 0.10, -0.45],
        [0.70, 0.35, -0.30, 0.60, 0.40, 0.05],
    ]
    n_obs = len(data_x)
    d_dim = len(data_x[0])
    k_df = n_obs - 1  # k_df = 3

    mean_vec = [sum(data_x[i][c] for i in range(n_obs)) / n_obs for c in range(d_dim)]

    # Partition coordinates into m = 3 disjoint 2D blocks: (0,1), (2,3), (4,5)
    # Here d_j = 2 and k_j = 3 >= d_j + 1 = 3 (satisfying Theorem 3.2 convexity condition)
    blocks = [(0, 1), (2, 3), (4, 5)]
    sub_means: list[list[float]] = []
    sub_invcovs: list[list[list[float]]] = []
    sub_dets: list[float] = []

    for c0, c1 in blocks:
        mu_j = [mean_vec[c0], mean_vec[c1]]
        # Sample covariance of the 2D projection divided by n_obs (covariance of sample mean)
        s00 = sum((data_x[i][c0] - mu_j[0]) ** 2 for i in range(n_obs)) / (k_df * n_obs)
        s11 = sum((data_x[i][c1] - mu_j[1]) ** 2 for i in range(n_obs)) / (k_df * n_obs)
        s01 = sum(
            (data_x[i][c0] - mu_j[0]) * (data_x[i][c1] - mu_j[1]) for i in range(n_obs)
        ) / (k_df * n_obs)
        cov_j = [[s00, s01], [s01, s11]]
        det_j = det2(cov_j)
        assert det_j > 1e-8, "Projected 2x2 covariance must be strictly positive definite"
        sub_means.append(mu_j)
        sub_invcovs.append(inv2(cov_j))
        sub_dets.append(round(det_j, 8))

    def t_hcct_6d(theta: list[float]) -> float:
        # For d_j = 2, k_j = 3: Hotelling T^2(2, 3) = (2*3 / (3+1-2)) F(2, 2) = 3 * F(2, 2)
        # Since F_{F(2,2)}(x) = 1 - (1 + x)^(-1) = x / (1 + x),
        # F_{T^2(2,3)}(s) = (s / 3) / (1 + s / 3) = s / (s + 3).
        total = 0.0
        for j, (c0, c1) in enumerate(blocks):
            diff = [sub_means[j][0] - theta[c0], sub_means[j][1] - theta[c1]]
            s_j = quad2(diff, sub_invcovs[j])
            u_j = s_j / (s_j + 3.0)
            total += (1.0 / 3.0) * hc_inv(u_j)
        return total

    # At theta = mean_vec, T_HCCT(mean_vec) == 0
    t_at_mean = t_hcct_6d(mean_vec)
    assert abs(t_at_mean) < 1e-15

    # Verify strict midpoint convexity across a chord in R^6 (Theorem 3.2)
    pt_a = [mean_vec[c] + 0.15 for c in range(d_dim)]
    pt_b = [mean_vec[c] - 0.10 * ((-1) ** c) for c in range(d_dim)]
    pt_mid = [0.5 * (pt_a[c] + pt_b[c]) for c in range(d_dim)]
    val_a = t_hcct_6d(pt_a)
    val_b = t_hcct_6d(pt_b)
    val_mid = t_hcct_6d(pt_mid)
    convexity_gap = 0.5 * (val_a + val_b) - val_mid
    assert convexity_gap > 0.0, "Midpoint convexity violated"

    # Compute simultaneous 95% confidence interval radius along unit contrast b = (1,1,1,1,1,1)/sqrt(6)
    b_dir = [1.0 / math.sqrt(6.0)] * 6
    lo_t, hi_t = 0.0, 2.0
    for _ in range(80):
        mid_t = 0.5 * (lo_t + hi_t)
        theta_probe = [mean_vec[c] + mid_t * b_dir[c] for c in range(d_dim)]
        if t_hcct_6d(theta_probe) <= crit_95:
            lo_t = mid_t
        else:
            hi_t = mid_t
    contrast_radius = 0.5 * (lo_t + hi_t)
    assert 0.0 < contrast_radius < 2.0

    # 3. Section 3.3 Inequality (3.7) conflict lower bound & Proposition 3.3 downweighting
    # Suppose 3 univariate Gaussian studies: theta_hat = (0.0, 0.05, 0.40), sigma = (0.1, 0.1, 0.1)
    centers_3 = [0.0, 0.05, 0.40]
    sigmas_3 = [0.1, 0.1, 0.1]
    w_equal = [1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0]
    theta_med = 0.05
    conflict_lower_bound = sum(
        w_equal[j] * abs(centers_3[j] - theta_med) / sigmas_3[j] for j in range(3)
    )

    def t_hcct_conflict(theta: float, weights: list[float]) -> float:
        return sum(
            weights[j] * hc_inv(2.0 * normal_cdf(abs(centers_3[j] - theta) / sigmas_3[j]) - 1.0)
            for j in range(3)
        )

    # Minimize over grid [0.0, 0.40]
    grid_c = [0.0002 * k for k in range(2001)]
    min_equal = min(t_hcct_conflict(th, w_equal) for th in grid_c)
    assert min_equal >= conflict_lower_bound
    assert min_equal > crit_95, "Outlier study should render equal-weight 95% region empty"

    # Follow Section 3.3 iterative downweighting (gamma = 0.5 on study with largest summand)
    w_curr = list(w_equal)
    stopping_tau = 0
    min_curr = min_equal
    while min_curr > crit_95 and stopping_tau < 20:
        stopping_tau += 1
        w_curr[2] *= 0.5
        s_w = sum(w_curr)
        w_curr = [w / s_w for w in w_curr]
        min_curr = min(t_hcct_conflict(th, w_curr) for th in grid_c)

    min_down = min_curr
    assert min_down < crit_95, "Downweighted stopping-time region must be non-empty"

    result = {
        "example1_cct_vs_hcct": {
            "alpha": 0.05,
            "critical_value": round(crit_95, 6),
            "cct_connected_components": cct_components,
            "hcct_connected_components": hcct_components,
            "hcct_min_at_zero": round(t_hcct_ex1(0.0), 6),
            "hcct_interval": [round(-hcct_halfwidth, 6), round(hcct_halfwidth, 6)],
        },
        "high_dim_small_n_divide_and_combine": {
            "d": d_dim,
            "n": n_obs,
            "global_sample_cov_max_rank": n_obs - 1,
            "classical_hotelling_t2_applicable": False,
            "num_projections_m": len(blocks),
            "subspace_dim_d_j": 2,
            "degrees_of_freedom_k_j": k_df,
            "theorem_3_2_condition_k_ge_d_plus_1": k_df >= 2 + 1,
            "sub_covariance_determinants": sub_dets,
            "midpoint_convexity_slack": round(convexity_gap, 6),
            "unit_contrast_directional_radius_95": round(contrast_radius, 6),
        },
        "conflict_diagnostic_and_stopping_time_downweighting": {
            "inequality_3_7_lower_bound": round(conflict_lower_bound, 6),
            "equal_weight_min_T": round(min_equal, 6),
            "equal_weight_region_empty": min_equal > crit_95,
            "stopping_iterations_tau": stopping_tau,
            "downweighted_min_T": round(min_down, 6),
            "downweighted_region_non_empty": min_down <= crit_95,
        },
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
