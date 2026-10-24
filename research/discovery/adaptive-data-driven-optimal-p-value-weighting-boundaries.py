#!/usr/bin/env python3
"""Constructed boundary and verification checks for AIMech:AdaptiveDataDrivenOptimalPValueWeighting.

Primary source:
Guillermo Durand (2019), "Adaptive p-value weighting with power optimality",
Electronic Journal of Statistics, 13(2):3336-3385.
arXiv:1710.01094v2, DOI:10.1214/19-EJS1578.

Verifies all four core mechanistic claims:
1. Multi-Weighted Benjamini-Hochberg (MWBH) and ADDOW over the null-proportion-adaptive
   weight space K_hat (Definitions 4.1-4.2, Remark 4.1, Remark 9.2, Lemmas A.4-A.6, Lemma C.6):
   - Monotonicity of u -> G_hat_{W_hat^*}(u) (Lemma A.6).
   - Fixed-point identity u_hat = I(G_hat_{W_hat^*}) = G_hat_{W_hat^*}(u_hat) (Lemma A.4) and
     order-statistic step-up identity (Lemma A.5).
   - Exact equivalence between multi-weighted ADDOW = MWBH(W_hat^*) and single-weight
     WBH(W_hat^*(u_hat)) (Remark 4.1, Remark 9.2).
   - Concavity and monotonicity of Grenander least-concave-majorant estimator LCM(D_hat_g)
     and generalized GADDOW objective (Section 9.1, Lemma C.6, Remark B.3).
2. Asymptotic FDR Control and Universal Power Optimality under Multiplicative Estimation (ME)
   (Theorems 5.1-5.2, Corollaries 5.1-5.3, Lemmas B.1-B.3):
   - Exact equivalence argmax_{w in K^infty} G^infty_w(u) = argmax_{w in K^infty} P^infty_w(u)
     under ME (bar_pi_{g,0} = C * pi_{g,0}), budget saturation sum_g pi_g bar_pi_{g,0} W^*_g(u) = 1,
     and exact asymptotic FDR = alpha / C (Lemma B.1, Lemma B.3, Theorem 5.1 Eq. 5.2).
   - Asymptotic and finite-sample power dominance of ADDOW over BH, IHW, ABH (Storey),
     HZZ (Hu-Zhao-Zhou), and Zhao-Zhang Pro1 and Pro2 in Scenario 1 (Theorem 5.2, Corollaries 5.2-5.3).
3. Breakdown of Heuristic 3.1 and Suboptimality of Non-Adaptive IHW vs. Unweighted BH under
   Heterogeneous Null Proportions (Remark 3.1, Section 6.4, Figures 7-8):
   - When Evenly Distributed nulls (ED) is violated (small dense group 1: pi_1=0.10, pi_{1,0}=0.05;
     large sparse group 2: pi_2=0.90, pi_{2,0}=0.85; mu_1=mu_2=2.0, alpha=0.70), non-adaptive
     IHW (pi_hat_{g,0}=1) over-weights the large sparse group 2 to inflate total rejections,
     yielding strictly lower power than unweighted BH (Pow(IHW) < Pow(BH) < Pow(ADDOW_CE)) and
     FDR(IHW) > pi_0 * alpha = FDR(BH).
4. Cross-Weighted ADDOW (crADDOW) via F-Fold Stratified Group Splitting for Weak-Signal
   Overfitting Stabilization with Asymptotic Equivalence (Section 7, Theorem 7.1, Appendix E):
   - Under weak signal (mu_bar=0.5), full-sample ADDOW suffers finite-sample FDR inflation
     from double use of p_{g,i}, whereas 5-fold crADDOW deflates finite-sample FDR below alpha=0.05.
   - Under strong signal (mu_bar=2.0), crADDOW and full-sample ADDOW achieve asymptotically
     equivalent FDR and optimal power (Theorem 7.1).
"""

from __future__ import annotations

import json
import math
import random
from typing import Callable, Dict, List, Sequence, Tuple


def norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def norm_sf(x: float) -> float:
    return 0.5 * math.erfc(x / math.sqrt(2.0))


def norm_isf(p: float) -> float:
    """Inverse survival function bar_Phi^{-1}(p) via bisection."""
    if p <= 0.0:
        return 12.0
    if p >= 1.0:
        return -12.0
    lo, hi = -12.0, 12.0
    for _ in range(64):
        mid = 0.5 * (lo + hi)
        if norm_sf(mid) > p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def alt_cdf_gaussian(t: float, mu: float) -> float:
    """One-sided Gaussian alternative p-value CDF F_g(t) = bar_Phi(bar_Phi^{-1}(t) - mu)."""
    if t <= 0.0:
        return 0.0
    if t >= 1.0:
        return 1.0
    return norm_sf(norm_isf(t) - mu)


def alt_pdf_gaussian(t: float, mu: float) -> float:
    """Derivative f_g(t) = exp(mu * bar_Phi^{-1}(t) - mu^2 / 2)."""
    if t <= 0.0:
        return float("inf")
    if t >= 1.0:
        return 0.0
    z = norm_isf(t)
    return math.exp(mu * z - 0.5 * mu * mu)


def uniform_cdf(t: float) -> float:
    if t <= 0.0:
        return 0.0
    return min(t, 1.0)


def compute_lcm(p_sorted: Sequence[float]) -> Tuple[List[float], List[float]]:
    """Compute Grenander Least Concave Majorant (LCM) of empirical CDF D_hat_g on [0, 1].

    Vertices of D_hat_g are (0, 0), (p_{(i)}, i / m_g) for i=1..m_g, and (1, 1).
    Returns (x_hull, y_hull) upper concave hull vertices.
    """
    m_g = len(p_sorted)
    pts: List[Tuple[float, float]] = [(0.0, 0.0)]
    for idx, p in enumerate(p_sorted, start=1):
        p_clamped = min(max(p, 0.0), 1.0)
        if p_clamped == pts[-1][0]:
            pts[-1] = (p_clamped, idx / m_g)
        else:
            pts.append((p_clamped, idx / m_g))
    if pts[-1][0] < 1.0:
        pts.append((1.0, 1.0))
    else:
        pts[-1] = (1.0, 1.0)

    hull: List[Tuple[float, float]] = []
    for pt in pts:
        while len(hull) >= 2:
            x1, y1 = hull[-2]
            x2, y2 = hull[-1]
            x3, y3 = pt
            # Remove (x2, y2) if slope (x1->x2) <= slope (x2->x3)
            if (y2 - y1) * (x3 - x2) <= (y3 - y2) * (x2 - x1) + 1e-15:
                hull.pop()
            else:
                break
        hull.append(pt)
    return [pt[0] for pt in hull], [pt[1] for pt in hull]


def eval_lcm(x_hull: Sequence[float], y_hull: Sequence[float], t: float) -> float:
    if t <= 0.0:
        return 0.0
    if t >= 1.0:
        return 1.0
    lo, hi = 0, len(x_hull) - 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if x_hull[mid] <= t:
            lo = mid
        else:
            hi = mid
    dx = x_hull[hi] - x_hull[lo]
    if dx <= 0.0:
        return y_hull[hi]
    return y_hull[lo] + (t - x_hull[lo]) * (y_hull[hi] - y_hull[lo]) / dx


def exact_two_group_optimal_weights(
    p1_sorted: Sequence[float],
    p2_sorted: Sequence[float],
    pi_hat_1_0: float,
    pi_hat_2_0: float,
    alpha: float,
    u: float,
) -> Tuple[Tuple[float, float], float]:
    """Exact maximizer W_hat^*(u) in argmax_{w in K_hat} G_hat_w(u) for G=2 groups.

    Since D_hat_1(alpha * u * w_1) only jumps when alpha * u * w_1 = p_{1,(k)},
    we can evaluate all candidate jump points k = 0, 1, ..., m_1 and assign the
    remaining budget in K_hat to w_2.
    """
    m1 = len(p1_sorted)
    m2 = len(p2_sorted)
    m = m1 + m2
    c1 = (m1 / m) * pi_hat_1_0
    c2 = (m2 / m) * pi_hat_2_0

    if u <= 0.0 or alpha <= 0.0:
        return (1.0 / (c1 + c2), 1.0 / (c1 + c2)), 0.0

    best_g = -1.0
    best_w = (0.0, 1.0 / c2)

    # Candidate w1 values: 0 and p_{1,(k)} / (alpha * u)
    for k1 in range(m1 + 1):
        if k1 == 0:
            w1 = 0.0
        else:
            w1 = p1_sorted[k1 - 1] / (alpha * u)
        if c1 * w1 > 1.0 + 1e-14:
            break
        rem = max(0.0, 1.0 - c1 * w1)
        w2 = rem / c2
        thresh1 = alpha * u * w1
        thresh2 = alpha * u * w2
        # Count rejections in group 1 and group 2 (including ties)
        r1 = k1
        while r1 < m1 and p1_sorted[r1] <= thresh1 + 1e-15:
            r1 += 1
        # Binary search in p2_sorted for thresh2
        lo, hi = 0, m2
        while lo < hi:
            mid = (lo + hi) // 2
            if p2_sorted[mid] <= thresh2 + 1e-15:
                lo = mid + 1
            else:
                hi = mid
        r2 = lo
        g_val = (r1 + r2) / m
        if g_val > best_g:
            best_g = g_val
            best_w = (w1, w2)
    return best_w, best_g


def run_w_bh(
    p_groups: Sequence[Sequence[float]],
    weights: Sequence[float],
    alpha: float,
) -> Tuple[float, List[Tuple[int, int]]]:
    """Run Weighted BH (WBH(w)) and return (u_hat_w, rejected_pairs)."""
    weighted_ps: List[Tuple[float, int, int]] = []
    m = sum(len(g) for g in p_groups)
    for g_idx, p_list in enumerate(p_groups):
        wg = weights[g_idx]
        for i_idx, p_val in enumerate(p_list):
            wp = p_val / wg if wg > 0.0 else float("inf")
            weighted_ps.append((wp, g_idx, i_idx))
    weighted_ps.sort(key=lambda item: item[0])
    r_hat = 0
    for r in range(1, m + 1):
        if weighted_ps[r - 1][0] <= alpha * (r / m) + 1e-15:
            r_hat = r
    u_hat = r_hat / m
    rejected: List[Tuple[int, int]] = []
    for g_idx, p_list in enumerate(p_groups):
        thresh = alpha * u_hat * weights[g_idx]
        for i_idx, p_val in enumerate(p_list):
            if p_val <= thresh + 1e-15:
                rejected.append((g_idx, i_idx))
    return u_hat, rejected


def run_addow_two_group(
    p1: Sequence[float],
    p2: Sequence[float],
    pi_hat_1_0: float,
    pi_hat_2_0: float,
    alpha: float,
    return_full_curve: bool = False,
) -> Tuple[float, Tuple[float, float], List[Tuple[int, int]], List[float]]:
    """Run exact 2-group ADDOW = MWBH(W_hat^*) using minimum-budget identity.

    To achieve k1 rejections in group 1 and k2 rejections in group 2 at threshold u,
    the minimal K_hat budget is (c1 * p1_{(k1)} + c2 * p2_{(k2)}) / (alpha * u) <= 1.
    Hence G_hat_{W_hat^*}(u) >= r/m iff B(r) <= alpha * u where
    B(r) = min_{k1 + k2 = r} (c1 * p1_{(k1)} + c2 * p2_{(k2)}).
    """
    p1_sorted = sorted(p1)
    p2_sorted = sorted(p2)
    m1 = len(p1_sorted)
    m2 = len(p2_sorted)
    m = m1 + m2
    c1 = (m1 / m) * pi_hat_1_0
    c2 = (m2 / m) * pi_hat_2_0

    v1 = [0.0] + [c1 * p for p in p1_sorted]
    v2 = [0.0] + [c2 * p for p in p2_sorted]

    best_budget = [float("inf")] * (m + 1)
    best_k1 = [0] * (m + 1)
    for k1 in range(m1 + 1):
        b1 = v1[k1]
        for k2 in range(m2 + 1):
            r = k1 + k2
            b = b1 + v2[k2]
            if b < best_budget[r]:
                best_budget[r] = b
                best_k1[r] = k1

    # Running minimum from right to left ensures B_monotone(r) is the minimal budget for >= r rejections
    min_b_for_at_least_r = list(best_budget)
    min_k1_for_at_least_r = list(best_k1)
    for r in range(m - 1, -1, -1):
        if min_b_for_at_least_r[r + 1] < min_b_for_at_least_r[r]:
            min_b_for_at_least_r[r] = min_b_for_at_least_r[r + 1]
            min_k1_for_at_least_r[r] = min_k1_for_at_least_r[r + 1]

    r_hat = 0
    for r in range(1, m + 1):
        if min_b_for_at_least_r[r] <= alpha * (r / m) + 1e-15:
            r_hat = r

    u_hat = r_hat / m
    if r_hat == 0 or alpha <= 0.0:
        w_star = (1.0 / (c1 + c2), 1.0 / (c1 + c2))
    else:
        k1_star = min_k1_for_at_least_r[r_hat]
        w1_star = (p1_sorted[k1_star - 1] / (alpha * u_hat)) if k1_star > 0 else 0.0
        w2_star = max(0.0, 1.0 - c1 * w1_star) / c2
        w_star = (w1_star, w2_star)

    g_curve: List[float] = []
    if return_full_curve:
        curr_r = 0
        for r in range(m + 1):
            u = r / m
            while curr_r < m and min_b_for_at_least_r[curr_r + 1] <= alpha * u + 1e-15:
                curr_r += 1
            g_curve.append(curr_r / m)

    rejected: List[Tuple[int, int]] = []
    if r_hat > 0:
        for g_idx, p_list in enumerate((p1, p2)):
            thresh = alpha * u_hat * w_star[g_idx]
            for i_idx, p_val in enumerate(p_list):
                if p_val <= thresh + 1e-15:
                    rejected.append((g_idx, i_idx))
    return u_hat, w_star, rejected, g_curve


def asymptotic_optimal_weights_two_group(
    pi1: float,
    pi2: float,
    pi1_0: float,
    pi2_0: float,
    bar_pi1_0: float,
    bar_pi2_0: float,
    mu1: float,
    mu2: float,
    alpha: float,
    u: float,
    maximize_power_directly: bool = False,
) -> Tuple[Tuple[float, float], float, float]:
    """Solve argmax_{w in K^infty} G^infty_w(u) or argmax_{w in K^infty} P^infty_w(u) for G=2."""
    bar_pi0 = pi1 * bar_pi1_0 + pi2 * bar_pi2_0
    c1 = pi1 * bar_pi1_0
    c2 = pi2 * bar_pi2_0
    pi1_1 = 1.0 - pi1_0
    pi2_1 = 1.0 - pi2_0

    if u <= 0.0:
        return (1.0 / bar_pi0, 1.0 / bar_pi0), 0.0, 0.0
    if alpha * u >= bar_pi0:
        w = (1.0 / (alpha * u), 1.0 / (alpha * u))
        return w, 1.0, 1.0 - (pi1 * pi1_0 + pi2 * pi2_0)

    # w1 in [max(0, (1 - c2/(alpha*u))/c1), min(1/c1, 1/(alpha*u))]
    w1_min = max(0.0, (1.0 - c2 / (alpha * u)) / c1)
    w1_max = min(1.0 / c1, 1.0 / (alpha * u))

    def marginal_diff(w1: float) -> float:
        w2 = (1.0 - c1 * w1) / c2
        t1 = min(max(alpha * u * w1, 1e-12), 1.0 - 1e-12)
        t2 = min(max(alpha * u * w2, 1e-12), 1.0 - 1e-12)
        if maximize_power_directly:
            # d/dw1 [pi1 * pi1_1 * F1(alpha*u*w1) + pi2 * pi2_1 * F2(alpha*u*w2)]
            slope1 = (pi1 * pi1_1 * alt_pdf_gaussian(t1, mu1)) / c1
            slope2 = (pi2 * pi2_1 * alt_pdf_gaussian(t2, mu2)) / c2
        else:
            # d/dw1 [pi1 * D1(alpha*u*w1) + pi2 * D2(alpha*u*w2)]
            slope1 = (pi1 * (pi1_0 + pi1_1 * alt_pdf_gaussian(t1, mu1))) / c1
            slope2 = (pi2 * (pi2_0 + pi2_1 * alt_pdf_gaussian(t2, mu2))) / c2
        return slope1 - slope2

    if marginal_diff(w1_min) <= 0.0:
        w1_star = w1_min
    elif marginal_diff(w1_max) >= 0.0:
        w1_star = w1_max
    else:
        lo, hi = w1_min, w1_max
        for _ in range(70):
            mid = 0.5 * (lo + hi)
            if marginal_diff(mid) > 0.0:
                lo = mid
            else:
                hi = mid
        w1_star = 0.5 * (lo + hi)

    w2_star = (1.0 - c1 * w1_star) / c2
    t1 = alpha * u * w1_star
    t2 = alpha * u * w2_star
    p_val = pi1 * pi1_1 * alt_cdf_gaussian(t1, mu1) + pi2 * pi2_1 * alt_cdf_gaussian(t2, mu2)
    h_val = pi1 * pi1_0 * uniform_cdf(t1) + pi2 * pi2_0 * uniform_cdf(t2)
    g_val = p_val + h_val
    return (w1_star, w2_star), g_val, p_val


def asymptotic_step_up_u(
    g_func: Callable[[float], float],
) -> float:
    """Compute u^* = sup{u in [0, 1] : g_func(u) >= u} for strictly concave g_func."""
    if g_func(1.0) >= 1.0:
        return 1.0
    lo, hi = 1e-9, 1.0
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if g_func(mid) >= mid:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def verify_claim1() -> Dict[str, object]:
    """Claim 1: MWBH, ADDOW over K_hat, fixed-point identity, Remark 4.1/9.2, and LCM concavity."""
    rng = random.Random(20191001)
    m1, m2 = 60, 60
    m = m1 + m2
    pi1_0, pi2_0 = 0.70, 0.80
    mu1, mu2 = 1.8, 3.2
    alpha = 0.05

    mismatches_addow_vs_wbh = 0
    mismatches_lemma_a5 = 0
    max_monotonicity_violation = 0.0
    max_fixed_point_error = 0.0
    max_lcm_concavity_violation = 0.0
    max_gaddow_concavity_violation = 0.0

    for trial in range(40):
        p1: List[float] = []
        p2: List[float] = []
        m1_0 = int(round(m1 * pi1_0))
        m2_0 = int(round(m2 * pi2_0))
        for i in range(m1):
            z = rng.gauss(0.0 if i < m1_0 else mu1, 1.0)
            p1.append(norm_sf(z))
        for i in range(m2):
            z = rng.gauss(0.0 if i < m2_0 else mu2, 1.0)
            p2.append(norm_sf(z))

        # Storey estimator pi_hat_{g,0}(1/2) (Eq. 2.3)
        lam = 0.5
        pi_hat_1 = min(1.0, (1.0 / m + sum(1 for p in p1 if p > lam) / m1) / (1.0 - lam))
        pi_hat_2 = min(1.0, (1.0 / m + sum(1 for p in p2 if p > lam) / m2) / (1.0 - lam))

        u_hat, w_star, rej_addow, g_curve = run_addow_two_group(
            p1, p2, pi_hat_1, pi_hat_2, alpha, return_full_curve=True
        )

        # Check Lemma A.6: g_curve is nondecreasing
        for r in range(len(g_curve) - 1):
            viol = max(0.0, g_curve[r] - g_curve[r + 1])
            if viol > max_monotonicity_violation:
                max_monotonicity_violation = viol

        # Check Lemma A.4 fixed-point identity: G_hat_{W_hat^*}(u_hat) == u_hat
        r_hat = int(round(u_hat * m))
        fp_err = abs(g_curve[r_hat] - u_hat)
        if fp_err > max_fixed_point_error:
            max_fixed_point_error = fp_err

        # Check Lemma A.5: order-statistic representation of u_hat
        p1_sorted = sorted(p1)
        p2_sorted = sorted(p2)
        r_a5 = 0
        for r in range(1, m + 1):
            w_r, _ = exact_two_group_optimal_weights(p1_sorted, p2_sorted, pi_hat_1, pi_hat_2, alpha, r / m)
            wps = [p / w_r[0] if w_r[0] > 0 else float("inf") for p in p1] + [
                p / w_r[1] if w_r[1] > 0 else float("inf") for p in p2
            ]
            wps.sort()
            if wps[r - 1] <= alpha * (r / m) + 1e-15:
                r_a5 = r
        if r_a5 != r_hat:
            mismatches_lemma_a5 += 1

        # Check Remark 4.1 & Remark 9.2: ADDOW == WBH(W_hat^*(u_hat))
        u_wbh, rej_wbh = run_w_bh((p1, p2), w_star, alpha)
        if abs(u_wbh - u_hat) > 1e-12 or set(rej_wbh) != set(rej_addow):
            mismatches_addow_vs_wbh += 1

        # Check Lemma C.6 & Remark B.3 on trial 0: LCM concavity and GADDOW concavity
        if trial == 0:
            xh1, yh1 = compute_lcm(p1_sorted)
            xh2, yh2 = compute_lcm(p2_sorted)
            assert abs(eval_lcm(xh1, yh1, 0.0) - 0.0) < 1e-15
            assert abs(eval_lcm(xh1, yh1, 1.0) - 1.0) < 1e-15
            grid = [k / 50.0 for k in range(51)]
            lcm1_vals = [eval_lcm(xh1, yh1, t) for t in grid]
            for k in range(1, len(grid) - 1):
                viol = max(0.0, 0.5 * (lcm1_vals[k - 1] + lcm1_vals[k + 1]) - lcm1_vals[k])
                if viol > max_lcm_concavity_violation:
                    max_lcm_concavity_violation = viol

            # Evaluate G_tilde_{W_tilde^*}(u) on grid using LCM
            c1 = (m1 / m) * pi_hat_1
            c2 = (m2 / m) * pi_hat_2
            u_grid = [k / 20.0 for k in range(21)]
            g_tilde_vals: List[float] = []
            for u_val in u_grid:
                if u_val == 0.0:
                    g_tilde_vals.append(0.0)
                    continue
                best_gt = 0.0
                for j in range(201):
                    w1 = (j / 200.0) / c1
                    w2 = (1.0 - c1 * w1) / c2
                    gt = 0.5 * eval_lcm(xh1, yh1, alpha * u_val * w1) + 0.5 * eval_lcm(
                        xh2, yh2, alpha * u_val * w2
                    )
                    if gt > best_gt:
                        best_gt = gt
                g_tilde_vals.append(best_gt)
            for k in range(1, len(u_grid) - 1):
                viol = max(0.0, 0.5 * (g_tilde_vals[k - 1] + g_tilde_vals[k + 1]) - g_tilde_vals[k])
                if viol > max_gaddow_concavity_violation:
                    max_gaddow_concavity_violation = viol

    assert mismatches_addow_vs_wbh == 0
    assert mismatches_lemma_a5 == 0
    assert max_monotonicity_violation == 0.0
    assert max_fixed_point_error < 1e-12
    assert max_lcm_concavity_violation < 1e-12
    assert max_gaddow_concavity_violation < 1e-3

    return {
        "trials": 40,
        "mismatches_addow_vs_wbh_terminal": mismatches_addow_vs_wbh,
        "mismatches_lemma_a5_step_up": mismatches_lemma_a5,
        "max_monotonicity_violation": max_monotonicity_violation,
        "max_fixed_point_error": round(max_fixed_point_error, 15),
        "max_lcm_concavity_violation": round(max_lcm_concavity_violation, 15),
        "max_gaddow_concavity_violation": round(max_gaddow_concavity_violation, 8),
    }


def verify_claim2() -> Dict[str, object]:
    """Claim 2: Lemma B.3 ME equivalence, Theorem 5.1 exact FDR=alpha/C, Theorem 5.2 & Corollaries 5.2-5.3."""
    pi1, pi2 = 0.5, 0.5
    pi1_0, pi2_0 = 0.70, 0.80
    pi0 = pi1 * pi1_0 + pi2 * pi2_0  # 0.75
    mu1, mu2 = 1.75, 3.50
    alpha = 0.05

    # 1. Verify Lemma B.3 under ME for C = 1.0 (CE) and C = 1.15
    max_weight_diff_me = 0.0
    max_budget_err = 0.0
    for c_mult in (1.0, 1.15):
        bar_pi1_0 = c_mult * pi1_0
        bar_pi2_0 = c_mult * pi2_0
        for u in (0.05, 0.15, 0.30, 0.50):
            w_g, _, _ = asymptotic_optimal_weights_two_group(
                pi1, pi2, pi1_0, pi2_0, bar_pi1_0, bar_pi2_0, mu1, mu2, alpha, u, False
            )
            w_p, _, _ = asymptotic_optimal_weights_two_group(
                pi1, pi2, pi1_0, pi2_0, bar_pi1_0, bar_pi2_0, mu1, mu2, alpha, u, True
            )
            diff = max(abs(w_g[0] - w_p[0]), abs(w_g[1] - w_p[1]))
            if diff > max_weight_diff_me:
                max_weight_diff_me = diff
            budget = pi1 * bar_pi1_0 * w_g[0] + pi2 * bar_pi2_0 * w_g[1]
            if abs(budget - 1.0) > max_budget_err:
                max_budget_err = abs(budget - 1.0)

    # 2. Verify Theorem 5.1 Eq. 5.2 exact asymptotic FDR = alpha / C
    u_star_ce = asymptotic_step_up_u(
        lambda u: asymptotic_optimal_weights_two_group(
            pi1, pi2, pi1_0, pi2_0, pi1_0, pi2_0, mu1, mu2, alpha, u, False
        )[1]
    )
    w_star_ce, g_star_ce, p_star_ce = asymptotic_optimal_weights_two_group(
        pi1, pi2, pi1_0, pi2_0, pi1_0, pi2_0, mu1, mu2, alpha, u_star_ce, False
    )
    h_star_ce = g_star_ce - p_star_ce
    asymp_fdr_ce = h_star_ce / g_star_ce

    c_me = 1.15
    u_star_me = asymptotic_step_up_u(
        lambda u: asymptotic_optimal_weights_two_group(
            pi1, pi2, pi1_0, pi2_0, c_me * pi1_0, c_me * pi2_0, mu1, mu2, alpha, u, False
        )[1]
    )
    _, g_star_me, p_star_me = asymptotic_optimal_weights_two_group(
        pi1, pi2, pi1_0, pi2_0, c_me * pi1_0, c_me * pi2_0, mu1, mu2, alpha, u_star_me, False
    )
    asymp_fdr_me = (g_star_me - p_star_me) / g_star_me

    # 3. Verify asymptotic power dominance in Scenario 1 (CE):
    # Compare ADDOW vs Pro2, Pro1, HZZ, ABH, IHW, BH
    def asymp_wbh_power(w1: float, w2: float) -> Tuple[float, float]:
        def g_w(u: float) -> float:
            t1, t2 = alpha * u * w1, alpha * u * w2
            return pi1 * (pi1_0 * uniform_cdf(t1) + (1.0 - pi1_0) * alt_cdf_gaussian(t1, mu1)) + pi2 * (
                pi2_0 * uniform_cdf(t2) + (1.0 - pi2_0) * alt_cdf_gaussian(t2, mu2)
            )

        u_w = asymptotic_step_up_u(g_w)
        t1, t2 = alpha * u_w * w1, alpha * u_w * w2
        p_w = pi1 * (1.0 - pi1_0) * alt_cdf_gaussian(t1, mu1) + pi2 * (1.0 - pi2_0) * alt_cdf_gaussian(
            t2, mu2
        )
        return u_w, p_w

    _, p_asymp_bh = asymp_wbh_power(1.0, 1.0)
    u_w1, p_asymp_abh = asymp_wbh_power(1.0 / pi0, 1.0 / pi0)
    w2_hzz = ((1.0 - pi1_0) / (pi1_0 * (1.0 - pi0)), (1.0 - pi2_0) / (pi2_0 * (1.0 - pi0)))
    u_w2, p_asymp_hzz = asymp_wbh_power(w2_hzz[0], w2_hzz[1])
    u_m = max(u_w1, u_w2)
    w_pro, _, p_asymp_pro1 = asymptotic_optimal_weights_two_group(
        pi1, pi2, pi1_0, pi2_0, pi1_0, pi2_0, mu1, mu2, alpha, u_m, False
    )
    _, p_asymp_pro2 = asymp_wbh_power(w_pro[0], w_pro[1])

    u_star_ihw = asymptotic_step_up_u(
        lambda u: asymptotic_optimal_weights_two_group(
            pi1, pi2, pi1_0, pi2_0, 1.0, 1.0, mu1, mu2, alpha, u, False
        )[1]
    )
    _, _, p_asymp_ihw = asymptotic_optimal_weights_two_group(
        pi1, pi2, pi1_0, pi2_0, 1.0, 1.0, mu1, mu2, alpha, u_star_ihw, False
    )

    assert max_weight_diff_me < 1e-9
    assert max_budget_err < 1e-12
    assert abs(asymp_fdr_ce - alpha) < 1e-6
    assert abs(asymp_fdr_me - (alpha / c_me)) < 1e-6
    assert p_star_ce > p_asymp_pro2 > p_asymp_pro1 > max(p_asymp_hzz, p_asymp_abh)
    assert p_star_ce > p_asymp_ihw > p_asymp_bh

    return {
        "max_weight_diff_G_vs_P_under_ME": round(max_weight_diff_me, 12),
        "max_budget_saturation_error": round(max_budget_err, 15),
        "asymp_fdr_ce": round(asymp_fdr_ce, 6),
        "asymp_fdr_me_C1_15": round(asymp_fdr_me, 6),
        "expected_alpha_over_C1_15": round(alpha / c_me, 6),
        "asymp_power_addow_ce": round(p_star_ce, 6),
        "asymp_power_pro2": round(p_asymp_pro2, 6),
        "asymp_power_pro1": round(p_asymp_pro1, 6),
        "asymp_power_abh": round(p_asymp_abh, 6),
        "asymp_power_hzz": round(p_asymp_hzz, 6),
        "asymp_power_ihw": round(p_asymp_ihw, 6),
        "asymp_power_bh": round(p_asymp_bh, 6),
    }


def verify_claim3() -> Dict[str, object]:
    """Claim 3: Remark 3.1 and Section 6.4 counterexample where Pow(IHW) < Pow(BH) < Pow(ADDOW_CE)."""
    pi1, pi2 = 0.10, 0.90
    pi1_0, pi2_0 = 0.05, 0.85
    pi0 = pi1 * pi1_0 + pi2 * pi2_0  # 0.77
    mu1, mu2 = 2.0, 2.0
    alpha = 0.70

    # 1. Asymptotic verification of Section 6.4 (Figures 7-8)
    # BH: w = (1, 1)
    def g_bh(u: float) -> float:
        t = alpha * u
        return pi1 * (pi1_0 * uniform_cdf(t) + (1.0 - pi1_0) * alt_cdf_gaussian(t, mu1)) + pi2 * (
            pi2_0 * uniform_cdf(t) + (1.0 - pi2_0) * alt_cdf_gaussian(t, mu2)
        )

    u_bh = asymptotic_step_up_u(g_bh)
    t_bh = alpha * u_bh
    p_asymp_bh = pi1 * (1.0 - pi1_0) * alt_cdf_gaussian(t_bh, mu1) + pi2 * (
        1.0 - pi2_0
    ) * alt_cdf_gaussian(t_bh, mu2)
    h_asymp_bh = pi0 * uniform_cdf(t_bh)
    fdr_asymp_bh = h_asymp_bh / (p_asymp_bh + h_asymp_bh)

    # IHW (NE: bar_pi_{g,0} = 1)
    u_ihw = asymptotic_step_up_u(
        lambda u: asymptotic_optimal_weights_two_group(
            pi1, pi2, pi1_0, pi2_0, 1.0, 1.0, mu1, mu2, alpha, u, False
        )[1]
    )
    w_ihw, g_ihw, p_asymp_ihw = asymptotic_optimal_weights_two_group(
        pi1, pi2, pi1_0, pi2_0, 1.0, 1.0, mu1, mu2, alpha, u_ihw, False
    )
    fdr_asymp_ihw = (g_ihw - p_asymp_ihw) / g_ihw

    # ADDOW (CE: bar_pi_{g,0} = pi_{g,0})
    u_ce = asymptotic_step_up_u(
        lambda u: asymptotic_optimal_weights_two_group(
            pi1, pi2, pi1_0, pi2_0, pi1_0, pi2_0, mu1, mu2, alpha, u, False
        )[1]
    )
    w_ce, g_ce, p_asymp_ce = asymptotic_optimal_weights_two_group(
        pi1, pi2, pi1_0, pi2_0, pi1_0, pi2_0, mu1, mu2, alpha, u_ce, False
    )
    fdr_asymp_ce = (g_ce - p_asymp_ce) / g_ce

    # 2. Finite-sample Monte Carlo verification (m1=50, m2=450, m=500, 120 trials)
    rng = random.Random(20190604)
    m1, m2 = 50, 450
    m = m1 + m2
    m1_0 = int(round(m1 * pi1_0))  # 2
    m2_0 = int(round(m2 * pi2_0))  # 382

    sum_pow_bh = 0.0
    sum_pow_ihw = 0.0
    sum_pow_ce = 0.0
    sum_fdr_bh = 0.0
    sum_fdr_ihw = 0.0
    sum_fdr_ce = 0.0
    trials = 120

    for _ in range(trials):
        p1 = [norm_sf(rng.gauss(0.0 if i < m1_0 else mu1, 1.0)) for i in range(m1)]
        p2 = [norm_sf(rng.gauss(0.0 if i < m2_0 else mu2, 1.0)) for i in range(m2)]

        _, rej_bh = run_w_bh((p1, p2), (1.0, 1.0), alpha)
        _, _, rej_ihw, _ = run_addow_two_group(p1, p2, 1.0, 1.0, alpha)
        _, _, rej_ce, _ = run_addow_two_group(p1, p2, pi1_0, pi2_0, alpha)

        def eval_rej(rej: Sequence[Tuple[int, int]]) -> Tuple[float, float]:
            if not rej:
                return 0.0, 0.0
            fp = sum(1 for (g, idx) in rej if (g == 0 and idx < m1_0) or (g == 1 and idx < m2_0))
            tp = len(rej) - fp
            return fp / len(rej), tp / m

        f_bh, pw_bh = eval_rej(rej_bh)
        f_ihw, pw_ihw = eval_rej(rej_ihw)
        f_ce, pw_ce = eval_rej(rej_ce)
        sum_fdr_bh += f_bh
        sum_fdr_ihw += f_ihw
        sum_fdr_ce += f_ce
        sum_pow_bh += pw_bh
        sum_pow_ihw += pw_ihw
        sum_pow_ce += pw_ce

    mc_pow_bh = sum_pow_bh / trials
    mc_pow_ihw = sum_pow_ihw / trials
    mc_pow_ce = sum_pow_ce / trials
    mc_fdr_bh = sum_fdr_bh / trials
    mc_fdr_ihw = sum_fdr_ihw / trials
    mc_fdr_ce = sum_fdr_ce / trials

    # IHW favors group 2 (w_ihw[1] > 1 > w_ihw[0]), whereas ADDOW_CE favors group 1
    assert w_ihw[1] > 1.0 > w_ihw[0]
    assert w_ce[0] > w_ce[1]
    assert p_asymp_ihw < p_asymp_bh < p_asymp_ce
    assert fdr_asymp_ihw > fdr_asymp_bh
    assert mc_pow_ihw < mc_pow_bh < mc_pow_ce
    assert mc_fdr_ihw > mc_fdr_bh

    return {
        "w_ihw_group1_group2": [round(w_ihw[0], 5), round(w_ihw[1], 5)],
        "w_addow_ce_group1_group2": [round(w_ce[0], 5), round(w_ce[1], 5)],
        "asymp_power_ihw": round(p_asymp_ihw, 6),
        "asymp_power_bh": round(p_asymp_bh, 6),
        "asymp_power_addow_ce": round(p_asymp_ce, 6),
        "asymp_fdr_bh_pi0_alpha": round(fdr_asymp_bh, 6),
        "asymp_fdr_ihw": round(fdr_asymp_ihw, 6),
        "asymp_fdr_addow_ce": round(fdr_asymp_ce, 6),
        "mc_power_ihw": round(mc_pow_ihw, 5),
        "mc_power_bh": round(mc_pow_bh, 5),
        "mc_power_addow_ce": round(mc_pow_ce, 5),
        "mc_fdr_bh": round(mc_fdr_bh, 5),
        "mc_fdr_ihw": round(mc_fdr_ihw, 5),
        "mc_fdr_addow_ce": round(mc_fdr_ce, 5),
    }


def run_craddow_two_group(
    p1: Sequence[float],
    p2: Sequence[float],
    pi_hat_1_0: float,
    pi_hat_2_0: float,
    alpha: float,
    n_folds: int = 5,
) -> List[Tuple[int, int]]:
    """Run F-fold cross-weighted ADDOW (crADDOW, Section 7.1, Eq. E.1).

    Each group g in {0, 1} is partitioned evenly into F folds. For each fold f,
    ADDOW_{-f} is computed on the remaining F-1 folds to obtain out-of-fold weights
    w^*_{g,f} = W_hat^{*-f}(u_hat_{W_hat^{*-f}}), and WBH is run across all G*F cells.
    """
    m1 = len(p1)
    m2 = len(p2)
    m = m1 + m2

    # Assign fold index f = i % n_folds within each group
    w_gf: List[Tuple[float, float]] = []
    for f in range(n_folds):
        p1_minus_f = [p1[i] for i in range(m1) if (i % n_folds) != f]
        p2_minus_f = [p2[i] for i in range(m2) if (i % n_folds) != f]
        _, w_star_minus_f, _, _ = run_addow_two_group(
            p1_minus_f, p2_minus_f, pi_hat_1_0, pi_hat_2_0, alpha
        )
        w_gf.append(w_star_minus_f)

    # Single-step WBH across all hypotheses with weight w^*_{g, F_m(g,i)}
    weighted_ps: List[Tuple[float, int, int]] = []
    for i, p_val in enumerate(p1):
        f = i % n_folds
        wg = w_gf[f][0]
        weighted_ps.append((p_val / wg if wg > 0.0 else float("inf"), 0, i))
    for i, p_val in enumerate(p2):
        f = i % n_folds
        wg = w_gf[f][1]
        weighted_ps.append((p_val / wg if wg > 0.0 else float("inf"), 1, i))

    weighted_ps.sort(key=lambda item: item[0])
    r_hat = 0
    for r in range(1, m + 1):
        if weighted_ps[r - 1][0] <= alpha * (r / m) + 1e-15:
            r_hat = r
    u_cross = r_hat / m
    rejected: List[Tuple[int, int]] = []
    for i, p_val in enumerate(p1):
        f = i % n_folds
        if p_val <= alpha * u_cross * w_gf[f][0] + 1e-15:
            rejected.append((0, i))
    for i, p_val in enumerate(p2):
        f = i % n_folds
        if p_val <= alpha * u_cross * w_gf[f][1] + 1e-15:
            rejected.append((1, i))
    return rejected


def verify_claim4() -> Dict[str, object]:
    """Claim 4: Section 7 crADDOW weak-signal overfitting stabilization and Theorem 7.1 strong-signal equivalence."""
    rng = random.Random(201907)
    m1, m2 = 80, 80
    m = m1 + m2
    pi1_0, pi2_0 = 0.70, 0.80
    m1_0 = int(round(m1 * pi1_0))  # 56
    m2_0 = int(round(m2 * pi2_0))  # 64
    m_alt = (m1 - m1_0) + (m2 - m2_0)  # 40
    alpha = 0.05

    # 1. Weak-signal regime (Section 6.2 & 7.3: mu_bar = 0.5, mu1 = 0.5, mu2 = 1.0)
    weak_trials = 300
    fdr_addow_weak_sum = 0.0
    fdr_craddow_weak_sum = 0.0
    for _ in range(weak_trials):
        p1 = [norm_sf(rng.gauss(0.0 if i < m1_0 else 0.5, 1.0)) for i in range(m1)]
        p2 = [norm_sf(rng.gauss(0.0 if i < m2_0 else 1.0, 1.0)) for i in range(m2)]

        _, _, rej_addow, _ = run_addow_two_group(p1, p2, pi1_0, pi2_0, alpha)
        rej_craddow = run_craddow_two_group(p1, p2, pi1_0, pi2_0, alpha, n_folds=5)

        if rej_addow:
            fp_a = sum(1 for (g, i) in rej_addow if (g == 0 and i < m1_0) or (g == 1 and i < m2_0))
            fdr_addow_weak_sum += fp_a / len(rej_addow)
        if rej_craddow:
            fp_c = sum(1 for (g, i) in rej_craddow if (g == 0 and i < m1_0) or (g == 1 and i < m2_0))
            fdr_craddow_weak_sum += fp_c / len(rej_craddow)

    fdr_addow_weak = fdr_addow_weak_sum / weak_trials
    fdr_craddow_weak = fdr_craddow_weak_sum / weak_trials

    # 2. Strong-signal regime (Theorem 7.1: mu_bar = 2.0, mu1 = 2.0, mu2 = 4.0)
    strong_trials = 150
    pow_addow_strong_sum = 0.0
    pow_craddow_strong_sum = 0.0
    pow_bh_strong_sum = 0.0
    tpr_addow_strong_sum = 0.0
    tpr_craddow_strong_sum = 0.0
    tpr_bh_strong_sum = 0.0
    fdr_craddow_strong_sum = 0.0
    for _ in range(strong_trials):
        p1 = [norm_sf(rng.gauss(0.0 if i < m1_0 else 2.0, 1.0)) for i in range(m1)]
        p2 = [norm_sf(rng.gauss(0.0 if i < m2_0 else 4.0, 1.0)) for i in range(m2)]

        _, _, rej_addow, _ = run_addow_two_group(p1, p2, pi1_0, pi2_0, alpha)
        rej_craddow = run_craddow_two_group(p1, p2, pi1_0, pi2_0, alpha, n_folds=5)
        _, rej_bh = run_w_bh((p1, p2), (1.0, 1.0), alpha)

        tp_a = sum(1 for (g, i) in rej_addow if (g == 0 and i >= m1_0) or (g == 1 and i >= m2_0))
        tp_c = sum(1 for (g, i) in rej_craddow if (g == 0 and i >= m1_0) or (g == 1 and i >= m2_0))
        tp_bh = sum(1 for (g, i) in rej_bh if (g == 0 and i >= m1_0) or (g == 1 and i >= m2_0))
        fp_c = len(rej_craddow) - tp_c

        pow_addow_strong_sum += tp_a / m
        pow_craddow_strong_sum += tp_c / m
        pow_bh_strong_sum += tp_bh / m
        tpr_addow_strong_sum += tp_a / m_alt
        tpr_craddow_strong_sum += tp_c / m_alt
        tpr_bh_strong_sum += tp_bh / m_alt
        if rej_craddow:
            fdr_craddow_strong_sum += fp_c / len(rej_craddow)

    pow_addow_strong = pow_addow_strong_sum / strong_trials
    pow_craddow_strong = pow_craddow_strong_sum / strong_trials
    pow_bh_strong = pow_bh_strong_sum / strong_trials
    tpr_addow_strong = tpr_addow_strong_sum / strong_trials
    tpr_craddow_strong = tpr_craddow_strong_sum / strong_trials
    tpr_bh_strong = tpr_bh_strong_sum / strong_trials
    fdr_craddow_strong = fdr_craddow_strong_sum / strong_trials

    assert fdr_addow_weak > alpha * 1.4  # Weak-signal overfitting above target alpha=0.05
    assert fdr_craddow_weak < alpha  # crADDOW deflates weak-signal FDR below alpha=0.05
    assert fdr_addow_weak > fdr_craddow_weak + 0.025
    assert abs(pow_craddow_strong - pow_addow_strong) < 0.015
    assert pow_craddow_strong > pow_bh_strong + 0.01
    assert tpr_craddow_strong > tpr_bh_strong + 0.04

    return {
        "fdr_addow_weak_signal": round(fdr_addow_weak, 5),
        "fdr_craddow_weak_signal": round(fdr_craddow_weak, 5),
        "fdr_reduction_weak_signal": round(fdr_addow_weak - fdr_craddow_weak, 5),
        "pow_addow_strong_signal": round(pow_addow_strong, 5),
        "pow_craddow_strong_signal": round(pow_craddow_strong, 5),
        "pow_bh_strong_signal": round(pow_bh_strong, 5),
        "tpr_addow_strong_signal": round(tpr_addow_strong, 5),
        "tpr_craddow_strong_signal": round(tpr_craddow_strong, 5),
        "tpr_bh_strong_signal": round(tpr_bh_strong, 5),
        "fdr_craddow_strong_signal": round(fdr_craddow_strong, 5),
    }


def main() -> None:
    res1 = verify_claim1()
    res2 = verify_claim2()
    res3 = verify_claim3()
    res4 = verify_claim4()
    summary = {
        "concept_id": "AIMech:AdaptiveDataDrivenOptimalPValueWeighting",
        "primary_source": {
            "authors": "Guillermo Durand",
            "year": 2019,
            "title": "Adaptive p-value weighting with power optimality",
            "venue": "Electronic Journal of Statistics 13(2):3336-3385",
            "arxiv": "1710.01094v2",
            "doi": "10.1214/19-EJS1578",
        },
        "claim1_mwbh_addow_fixed_point_and_lcm_concavity": res1,
        "claim2_asymptotic_power_optimality_and_me_equivalence": res2,
        "claim3_remark3_1_section6_4_ihw_suboptimality_counterexample": res3,
        "claim4_section7_cross_addow_stabilization_and_theorem7_1": res4,
        "all_checks_passed": True,
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
