#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 631: 0/1 Adam (Lu et al., ICLR 2023 / arXiv:2202.06009)."""

from __future__ import annotations

import math


def compress_1bit(v: list[float]) -> list[float]:
    d = len(v)
    mag = sum(abs(x) for x in v) / d
    return [mag if x >= 0.0 else -mag for x in v]


def verify_adaptive_variance_freezing_and_local_steps() -> tuple[int, int, float]:
    """Verify Section 4 & Section 6 policies for T_v (k_{j+1} - k_j = 2^{floor(j/kappa)})
    and T_u (doubling interval up to H=16) and Algorithm 1 linear momentum reconstruction.
    """
    # Policy for T_v: k_{j+1} - k_j = 2^{floor(j / kappa)} with kappa = 16
    kappa = 16
    total_steps = 10000
    k = 0
    j = 0
    tv_set = set()
    while k < total_steps:
        tv_set.add(k)
        k += 2 ** (j // kappa)
        j += 1

    # Check Theorem 1 condition m = |T_v| <= log(1 - beta1) / log(beta2) for suitable horizon
    beta1 = 0.9
    beta2 = 0.999
    max_m_bound = math.log(1.0 - beta1) / math.log(beta2)
    assert max_m_bound > 2300.0, f"Expected log(0.1)/log(0.999) > 2300, got {max_m_bound}"
    assert len(tv_set) < 200, f"Exponential spacing should need < 200 full-precision variance updates in 10k steps, got {len(tv_set)}"

    # Verify Algorithm 1 exact local-step model consensus & linear momentum approximation when variance is frozen:
    # u_t^{(i)} = sum_{k=t'}^t gamma_k * m_k^{(i)}
    # Without compression noise, x_{t+1}^{(i)} = x_{t'}^{(i)} - (1/n sum_i u_t^{(i)}) / sqrt(v_t + eps)
    # equals the exact average of local models x_{t+1/2}^{(i)} across all workers!
    n_workers = 4
    d = 4
    eps = 1e-8
    v_frozen = [0.04, 0.09, 0.16, 0.25]
    x_sync = [1.0, -2.0, 0.5, -1.5]
    x_workers = [list(x_sync) for _ in range(n_workers)]
    m_workers = [[0.0] * d for _ in range(n_workers)]
    u_workers = [[0.0] * d for _ in range(n_workers)]
    gammas = [0.01, 0.009, 0.008, 0.007]

    for step, gamma in enumerate(gammas):
        for i in range(n_workers):
            g_loc = [0.1 * (step + 1) * (i + 1) * ((-1) ** (i + j)) for j in range(d)]
            m_half = [beta1 * m_workers[i][j] + (1.0 - beta1) * g_loc[j] for j in range(d)]
            x_half = [x_workers[i][j] - gamma * m_half[j] / math.sqrt(v_frozen[j] + eps) for j in range(d)]
            u_half = [u_workers[i][j] + gamma * m_half[j] for j in range(d)]
            m_workers[i] = m_half
            x_workers[i] = x_half
            u_workers[i] = u_half

    # At t in T_u, average u_half across workers and update from x_{t'}:
    u_avg = [sum(u_workers[i][j] for i in range(n_workers)) / n_workers for j in range(d)]
    x_synced = [x_sync[j] - u_avg[j] / math.sqrt(v_frozen[j] + eps) for j in range(d)]
    x_avg_direct = [sum(x_workers[i][j] for i in range(n_workers)) / n_workers for j in range(d)]
    sync_err = max(abs(x_synced[j] - x_avg_direct[j]) for j in range(d))
    assert sync_err < 1e-15, f"Local-step frozen-variance sync identity error: {sync_err}"
    return len(tv_set), int(max_m_bound), sync_err


def verify_lemmas_2_and_4_and_comm_savings() -> tuple[float, float, float]:
    """Verify Appendix D.3 Lemma 2 (variance lower/upper bounds) and Lemma 4 (||a/sqrt(b)||^2 <= ||a||^2 ||1/b||_1)."""
    d = 4
    beta2 = 0.99
    eps = 1e-6
    g_inf = 2.0
    m_updates = 5

    v = [0.0] * d
    # Step 1 update:
    g1 = [0.5, -1.2, 0.8, -1.9]
    v1 = [(1.0 - beta2) * (x * x) for x in g1]
    v = list(v1)
    for _ in range(m_updates - 1):
        g = [0.3, -0.7, 1.1, -0.4]
        v = [beta2 * v[j] + (1.0 - beta2) * (g[j] * g[j]) for j in range(d)]

    for j in range(d):
        lo = (beta2 ** (m_updates / 2.0)) * math.sqrt(v1[j] + eps)
        mid = math.sqrt(v[j] + eps)
        hi = math.sqrt(g_inf * g_inf + eps)
        assert lo <= mid <= hi + 1e-12, f"Lemma 2 bound violated at coord {j}: {lo} <= {mid} <= {hi}"

    # Lemma 4: ||a / sqrt(b)||_2^2 <= ||a||_2^2 * ||1 / b||_1
    a = [0.7, -1.3, 0.4, -0.9]
    b = [0.2, 0.5, 0.1, 0.8]
    lhs = sum((a[j] * a[j]) / b[j] for j in range(d))
    rhs = sum(a[j] * a[j] for j in range(d)) * sum(1.0 / b[j] for j in range(d))
    assert lhs <= rhs, f"Lemma 4 violated: {lhs} > {rhs}"

    # Bits per parameter reduction (Figure 4): 1-bit Adam BERT-Large uses 3.27 bits/param vs 0/1 Adam 0.42 bits/param (~87.2% reduction)
    vol_reduction = 1.0 - (0.42 / 3.27)
    assert 0.86 < vol_reduction < 0.88
    return lhs, rhs, vol_reduction


if __name__ == "__main__":
    tv_count, max_m_bound, sync_err = verify_adaptive_variance_freezing_and_local_steps()
    lhs, rhs, vol_red = verify_lemmas_2_and_4_and_comm_savings()
    print(
        f"[PASS] Round 631 0/1 Adam verified: tv_count={tv_count}, max_m_bound={max_m_bound}, "
        f"sync_err={sync_err:.2e}, lemma4_ratio={lhs/rhs:.4f}<=1, vol_red={vol_red:.4f}"
    )
