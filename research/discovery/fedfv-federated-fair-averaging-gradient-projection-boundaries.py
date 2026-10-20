#!/usr/bin/env python3
"""Constructed boundary verification for Round 494: FedFV (Wang et al. 2021)."""

from __future__ import annotations

import math


def dot(u: list[float], v: list[float]) -> float:
    return sum(a * b for a, b in zip(u, v))


def norm(u: list[float]) -> float:
    return math.sqrt(dot(u, u))


def mitigate_internal_conflict(
    gradients: list[list[float]], losses: list[float], alpha: float = 0.0
) -> list[float]:
    """Algorithm 2 (Wang et al. 2021): Loss-ordered internal conflict projection."""
    m = len(gradients)
    order = sorted(range(m), key=lambda idx: losses[idx])
    top_alpha_count = int(math.floor((1.0 - alpha) * m))
    s_alpha = set(order[:top_alpha_count])

    g_pc = [list(g) for g in gradients]
    for k in range(m):
        if k not in s_alpha:
            continue
        for ij in order:
            if k == ij:
                continue
            g_target = gradients[ij]
            ip = dot(g_pc[k], g_target)
            if ip < 0.0:
                denom = dot(g_target, g_target)
                scale = ip / denom
                g_pc[k] = [g_pc[k][d] - scale * g_target[d] for d in range(len(g_target))]

    d_dim = len(gradients[0])
    return [sum(g_pc[k][d] for k in range(m)) / m for d in range(d_dim)]


def theorem2_bound_factor(m: int, k: int, eps1: float, eps2: float) -> float:
    """Equation 8 / Theorem 2 (Wang et al. 2021): f(m, k, eps1, eps2)."""
    r = math.sqrt(1.0 - eps1 * eps1)
    return (eps2 * eps2 * r * (1.0 - (r ** (m - k)))) / (1.0 - r)


def main() -> None:
    # 1. Internal conflict mitigation (Algorithm 2 & Theorems 1-2):
    # Suppose 3 clients have losses l_1 < l_2 < l_3 and gradients with large magnitude disparity
    # where majority/low-loss client 1 conflicts with high-loss clients 2 and 3.
    g1 = [4.0, 0.0]
    g2 = [-1.0, 1.0]
    g3 = [-0.8, -0.6]
    losses = [0.2, 0.9, 1.8]
    grads = [g1, g2, g3]

    g_avg = [sum(g[d] for g in grads) / 3.0 for d in range(2)]
    g_fv = mitigate_internal_conflict(grads, losses, alpha=0.0)

    # Naive average conflicts strongly with worst-loss client g3 (dot < 0),
    # whereas FedFV mitigates conflict in loss-ascending projection order.
    conflict_avg_g3 = dot(g_avg, g3)
    conflict_fv_g3 = dot(g_fv, g3)
    assert conflict_avg_g3 < -0.5, f"Expected naive average to conflict with g3, got {conflict_avg_g3}"
    assert conflict_fv_g3 > conflict_avg_g3, "Expected FedFV to reduce conflict with worst-loss client g3"

    # Theorem 2 upper bound factor f(m, k, eps1, eps2) strictly decreases with projection index k
    f_vals = [theorem2_bound_factor(4, k, 0.3, 0.6) for k in (1, 2, 3, 4)]
    assert f_vals[0] > f_vals[1] > f_vals[2] > f_vals[3] == 0.0

    # 2. External conflict mitigation and norm rescaling (Algorithm 3 & Algorithm 1 line 10):
    # Unselected client h has recent gradient g_h in GH conflicting with g_fv
    g_hist = [-g_fv[0] - 0.5 * g_fv[1], -g_fv[1] + 0.5 * g_fv[0]]
    assert dot(g_fv, g_hist) < 0.0
    ip_ext = dot(g_fv, g_hist)
    denom_ext = dot(g_hist, g_hist)
    g_ext = [g_fv[d] - (ip_ext / denom_ext) * g_hist[d] for d in range(2)]
    assert abs(dot(g_ext, g_hist)) < 1e-12
    orig_avg_norm = norm(g_avg)
    g_rescaled = [g_ext[d] / norm(g_ext) * orig_avg_norm for d in range(2)]
    assert abs(norm(g_rescaled) - orig_avg_norm) < 1e-12

    # 3. Theorem 3 two-user identity (Equations 10-19):
    # When u1 . u2 < 0, g_bar' = u1 + u2 - (u1.u2/||u1||^2)u1 - (u1.u2/||u2||^2)u2
    # satisfies (u1+u2)^T g_bar' = (1 - cos^2 phi_12)||u1+u2||^2 == ||g_bar'||^2.
    u1 = [3.0, 1.0]
    u2 = [-2.0, 0.5]
    ip12 = dot(u1, u2)
    assert ip12 < 0.0
    cos12 = ip12 / (norm(u1) * norm(u2))
    u_sum = [u1[0] + u2[0], u1[1] + u2[1]]
    g_bar_prime = [
        u_sum[d] - (ip12 / dot(u1, u1)) * u1[d] - (ip12 / dot(u2, u2)) * u2[d]
        for d in range(2)
    ]
    lhs_ip = dot(u_sum, g_bar_prime)
    rhs_id = (1.0 - cos12 * cos12) * (dot(u1, u1) + dot(u2, u2))
    u_diff = [u1[0] - u2[0], u1[1] - u2[1]]
    norm_sq_gbp = dot(g_bar_prime, g_bar_prime)
    rhs_norm_sq = (1.0 - cos12 * cos12) * dot(u_diff, u_diff)
    assert abs(lhs_ip - rhs_id) < 1e-12
    assert abs(norm_sq_gbp - rhs_norm_sq) < 1e-12

    # When u1 = -beta * u2 (cos12 = -1, Pareto stationary), g_bar_prime == 0
    u2_opp = [-1.5, -0.5]
    ip_opp = dot(u1, u2_opp)
    g_opp = [
        (u1[d] + u2_opp[d])
        - (ip_opp / dot(u1, u1)) * u1[d]
        - (ip_opp / dot(u2_opp, u2_opp)) * u2_opp[d]
        for d in range(2)
    ]
    assert norm(g_opp) < 1e-12

    print(
        f"[PASS] Round 494 FedFV (Wang et al. 2021): conflict_avg_g3={conflict_avg_g3:.4f} -> "
        f"conflict_fv_g3={conflict_fv_g3:.4f}, Thm2_f={f_vals[0]:.4f}>{f_vals[2]:.4f}>{f_vals[3]:.1f}, "
        f"Thm3_id_err={abs(lhs_ip - rhs_id):.2e}, pareto_norm={norm(g_opp):.2e}"
    )


if __name__ == "__main__":
    main()
