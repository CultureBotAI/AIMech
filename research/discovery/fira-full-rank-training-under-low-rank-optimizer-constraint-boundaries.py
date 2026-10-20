#!/usr/bin/env python3
"""Constructed boundary verification for Round 636: Fira (Chen et al., NeurIPS 2025)."""

from __future__ import annotations
import math


def verify_theorem1_scaling_approximation_bound() -> tuple[float, float, float]:
    """Verify Appendix E.1 Theorem 1 error upper bound kappa(r) <= Delta_{phi^2} * (1 - ||G_r||^2 / ||G||^2)."""
    # Full-rank gradient components g_1, ..., g_n (n = 8) sorted by magnitude
    g = [4.0, -3.5, 3.0, -2.5, 1.2, -0.8, 0.5, -0.3]
    # Adaptive optimizer element-wise scaling factors c_i = psi_i(g_i) / g_i bounded in [c_min, c_max]
    scales = [1.8, 1.6, 1.75, 1.5, 1.2, 1.9, 1.3, 1.4]
    psi = [scales[i] * g[i] for i in range(len(g))]

    c_min = min(abs(psi[i] / g[i]) for i in range(len(g)))
    c_max = max(abs(psi[i] / g[i]) for i in range(len(g)))
    delta_phi2 = c_max * c_max - c_min * c_min

    s_n = sum(x * x for x in g)
    cap_s_n = sum(y * y for y in psi)
    phi2_full = cap_s_n / s_n

    prev_bound = float("inf")
    max_slack_violation = 0.0
    kappa_r4 = 0.0
    bound_r4 = 0.0
    for r in range(1, len(g) + 1):
        s_r = sum(g[i] * g[i] for i in range(r))
        cap_s_r = sum(psi[i] * psi[i] for i in range(r))
        phi2_low = cap_s_r / s_r
        kappa_r = abs(phi2_full - phi2_low)
        bound_r = delta_phi2 * (1.0 - s_r / s_n)
        assert kappa_r <= bound_r + 1e-14, f"Theorem 1 violated at r={r}: {kappa_r} > {bound_r}"
        assert bound_r <= prev_bound + 1e-14, "Upper bound must decrease monotonically with rank r"
        prev_bound = bound_r
        if r == 4:
            kappa_r4 = kappa_r
            bound_r4 = bound_r

    # At full rank r = n, both kappa(n) and bound(n) are exactly 0
    assert abs(prev_bound) < 1e-15
    return kappa_r4, bound_r4, max_slack_violation


def verify_theorem2_dirichlet_variance_and_norm_limiter() -> tuple[float, float, float]:
    """Verify Appendix E.2 Theorem 2 Dirichlet variance factor 3/(n+2) and Section 4.2 Norm-Growth Limiter."""
    # Theorem 2 Eq. (36)-(39): For X_i / sigma^2 ~ chi^2_1, weights w = (w_1, ..., w_n) ~ Dirichlet(1/2, ..., 1/2).
    # E[w_i^2] = (1/2 * 3/2) / ((n/2) * (n/2 + 1)) = 3 / (n * (n + 2)), so sum_{i=1}^n E[w_i^2] = 3 / (n + 2) <= 1.
    for n in [1, 2, 4, 16, 64, 256]:
        alpha_i = 0.5
        alpha_sum = 0.5 * n
        e_wi_sq = (alpha_i * (alpha_i + 1.0)) / (alpha_sum * (alpha_sum + 1.0))
        sum_e_wi_sq = n * e_wi_sq
        closed_form = 3.0 / (n + 2.0)
        assert abs(sum_e_wi_sq - closed_form) < 1e-15
        assert sum_e_wi_sq <= 1.0 + 1e-15

    var_ratio_n64 = 3.0 / (64.0 + 2.0)

    # Verify Norm-Growth Limiter (Eq. 12) and full-rank reconstruction (Eq. 10)
    gamma = 1.01
    s_prev_norm = 2.0
    # Simulate an abrupt subspace-switch spike in the scaled orthogonal complement gradient S_t
    s_t = [6.0, -8.0]  # norm = 10.0 > gamma * 2.0 = 2.02
    raw_norm = math.sqrt(sum(v * v for v in s_t))
    assert raw_norm / s_prev_norm > gamma

    # Apply Eq. (12): if ||S_t|| / ||S_{t-1}|| > gamma, S_t <- (S_t / ||S_t||) * gamma * ||S_{t-1}||
    s_t_limited = [v * (gamma * s_prev_norm / raw_norm) for v in s_t]
    limited_norm = math.sqrt(sum(v * v for v in s_t_limited))
    assert abs(limited_norm - gamma * s_prev_norm) < 1e-14

    # Verify cosine similarity of direction is preserved (1.0)
    dot = sum(s_t[i] * s_t_limited[i] for i in range(2))
    cos_sim = dot / (raw_norm * limited_norm)
    assert abs(cos_sim - 1.0) < 1e-14

    # Verify Table 2 optimizer state count for m x n matrix (m <= n) of rank r: mr + 2nr + 1 vs Full-rank 2mn
    m, n, r = 64, 128, 8
    fira_states = m * r + 2 * n * r + 1
    full_states = 2 * m * n
    mem_saving = 1.0 - (fira_states / full_states)
    assert fira_states == 2561 and full_states == 16384 and mem_saving > 0.84
    return var_ratio_n64, limited_norm, mem_saving


if __name__ == "__main__":
    k4, b4, _ = verify_theorem1_scaling_approximation_bound()
    vr64, lnorm, msav = verify_theorem2_dirichlet_variance_and_norm_limiter()
    print(
        f"[PASS] Round 636 Fira verified: thm1_kappa4={k4:.4f}<=bound4={b4:.4f}, "
        f"thm2_var_ratio_n64={vr64:.4f}, limited_norm={lnorm:.4f}, state_saving={msav:.2%}"
    )
