#!/usr/bin/env python3
"""Constructed boundary verification for Round 496: TERM (Li, Beirami, Sanjabi, & Smith 2021)."""

from __future__ import annotations

import math


def term_objective(losses: list[float], t: float) -> float:
    """Equation 2 (Li et al. 2021): t-tilted loss R_tilde(t; theta)."""
    n = len(losses)
    if abs(t) < 1e-12:
        return sum(losses) / n
    m = max(t * x for x in losses)
    lse = m + math.log(sum(math.exp(t * x - m) for x in losses) / n)
    return lse / t


def term_weights(losses: list[float], t: float) -> list[float]:
    """Equation 3 / Lemma 1 (Li et al. 2021): Tilted gradient weights w_i(t; theta)."""
    n = len(losses)
    if abs(t) < 1e-12:
        return [1.0 / n] * n
    m = max(t * x for x in losses)
    exps = [math.exp(t * x - m) for x in losses]
    s = sum(exps)
    return [e / s for e in exps]


def solve_1d_point_estimation(points: list[float], t: float, lo: float = 0.8, hi: float = 2.6) -> float:
    """Solve grad_theta R_tilde(t; theta) = 0 on [lo, hi] via bisection."""
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        losses = [0.5 * ((mid - x) ** 2) for x in points]
        w = term_weights(losses, t)
        grad = sum(wi * (mid - xi) for wi, xi in zip(w, points))
        if grad < 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def hierarchical_term(groups: list[list[float]], t: float, tau: float) -> tuple[float, list[list[float]]]:
    """Equation 4 & Lemma 6 (Li et al. 2021): Multi-objective hierarchical TERM J_tilde(t, tau; theta)."""
    n_total = sum(len(g) for g in groups)
    r_g = [term_objective(g, tau) for g in groups]
    m = max(t * rg for rg in r_g)
    j_val = (m + math.log(sum(len(g) * math.exp(t * rg - m) for g, rg in zip(groups, r_g)) / n_total)) / t

    # Weights w_{g,x}(t, tau) from Lemma 6 (Equations 47, 50, 52)
    g_exps = [len(g) * math.exp(t * rg - m) for g, rg in zip(groups, r_g)]
    g_sum = sum(g_exps)
    w_g = [ge / g_sum for ge in g_exps]
    w_gx = []
    for wg, g in zip(w_g, groups):
        w_x = term_weights(g, tau)
        w_gx.append([wg * wx for wx in w_x])
    return j_val, w_gx


def main() -> None:
    # 1. Lemma 2 (limits as t -> -inf, 0, +inf) & Theorem 7 (monotonicity in t):
    sample_losses = [0.2, 0.7, 1.5, 3.2]
    r_neg = term_objective(sample_losses, -50.0)
    r_zero = term_objective(sample_losses, 0.0)
    r_pos = term_objective(sample_losses, 50.0)
    assert abs(r_neg - min(sample_losses)) < 0.05
    assert abs(r_zero - sum(sample_losses) / len(sample_losses)) < 1e-12
    assert abs(r_pos - max(sample_losses)) < 0.05

    ts = [-5.0, -1.0, 0.0, 1.0, 5.0]
    r_vals = [term_objective(sample_losses, t) for t in ts]
    for i in range(len(r_vals) - 1):
        assert r_vals[i] < r_vals[i + 1], f"Expected R_tilde strictly increasing in t: {r_vals}"

    # 2. Outlier suppression (t < 0) vs. ERM (t = 0) and Theorems 2, 4, 5 for t > 0:
    # 4 clean inliers around 1.0 and 1 extreme outlier at 10.0
    pts_outlier = [0.8, 0.95, 1.05, 1.2, 10.0]
    theta_neg = solve_1d_point_estimation(pts_outlier, -1.0, lo=0.8, hi=1.5)
    theta_erm = sum(pts_outlier) / len(pts_outlier)
    w_neg = term_weights([0.5 * ((theta_neg - x) ** 2) for x in pts_outlier], -1.0)
    # Outlier weight is exponentially suppressed for t = -1.0, keeping theta_neg close to clean mean 1.0
    assert w_neg[-1] < 1e-6
    assert abs(theta_neg - 1.0) < 0.01 < abs(theta_erm - 1.0)

    # Theorems 2, 4, 5 across increasing t on GLM quadratic losses:
    # As t increases: max-loss decreases, average-loss increases (for t >= 0),
    # empirical loss variance decreases, and cosine similarity with 1_N increases.
    pts = [0.6, 0.9, 1.2, 2.5]
    t_grid = [-0.2, 0.0, 0.5, 1.5, 4.0]
    avg_losses = []
    max_losses = []
    variances = []
    cos_sims = []
    for t in t_grid:
        th = solve_1d_point_estimation(pts, t, lo=0.6, hi=2.5)
        f_vec = [0.5 * ((th - x) ** 2) for x in pts]
        mean_f = sum(f_vec) / len(f_vec)
        var_f = sum((fi - mean_f) ** 2 for fi in f_vec) / len(f_vec)
        cos_f = sum(f_vec) / (math.sqrt(len(f_vec)) * math.sqrt(sum(fi * fi for fi in f_vec)))
        avg_losses.append(mean_f)
        max_losses.append(max(f_vec))
        variances.append(var_f)
        cos_sims.append(cos_f)

    for i in range(len(t_grid) - 1):
        assert max_losses[i] > max_losses[i + 1]
        assert variances[i] > variances[i + 1]
        assert cos_sims[i] < cos_sims[i + 1]
        if t_grid[i] >= 0.0:
            assert avg_losses[i] < avg_losses[i + 1]

    # 3. Hierarchical multi-objective TERM (Lemma 6 & Lemma 7):
    groups = [[0.2, 0.5, 0.9], [1.1, 2.4]]
    flat = groups[0] + groups[1]
    j_same, _ = hierarchical_term(groups, 1.5, 1.5)
    r_same = term_objective(flat, 1.5)
    assert abs(j_same - r_same) < 1e-12, "Lemma 7: J_tilde(t, t) must equal R_tilde(t)"

    # Verify Lemma 6 analytical weights w_{g,x}(t, tau) against finite difference dJ/df_{g,x}
    j_base, w_gx = hierarchical_term(groups, 2.0, -1.0)
    eps = 1e-7
    groups_pert = [[groups[0][0] + eps, groups[0][1], groups[0][2]], list(groups[1])]
    j_pert, _ = hierarchical_term(groups_pert, 2.0, -1.0)
    fd_grad = (j_pert - j_base) / eps
    assert abs(fd_grad - w_gx[0][0]) < 1e-7

    print(
        f"[PASS] Round 496 TERM (Li et al. 2021): theta(-1)={theta_neg:.4f} vs ERM={theta_erm:.4f} "
        f"(w_outlier={w_neg[-1]:.2e}), var(t=-0.2)={variances[0]:.2f}->var(t=2.0)={variances[-1]:.2f}, "
        f"cos(1_N)={cos_sims[0]:.4f}->{cos_sims[-1]:.4f}, Lemma7_err={abs(j_same - r_same):.2e}"
    )


if __name__ == "__main__":
    main()
