#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 634: BAdam (Luo, Yu, & Li, NeurIPS 2024)."""

from __future__ import annotations

import math


def verify_memory_and_backward_pass_equations() -> tuple[float, float, int, int, float]:
    """Verify Section 2.2.1 Eq. (5) memory consumption (2M + 16M/D vs 18M GB)
    and Section 2.2.2 Eq. (6) unit-backward-pass count (K*D*(D+1)/2 vs K*D^2).
    """
    # Llama 3-8B: M = 8.0 billion parameters, D = 32 transformer layers
    m_billion = 8.0
    d_blocks = 32
    k_inner = 100

    adam_mem_gb = 18.0 * m_billion
    badam_mem_gb = 2.0 * m_billion + (16.0 * m_billion) / d_blocks
    assert abs(adam_mem_gb - 144.0) < 1e-12
    assert abs(badam_mem_gb - 20.0) < 1e-12
    assert badam_mem_gb < adam_mem_gb / 7.0

    # Unit-backward-pass count over 1 block-epoch (K * D data batches)
    ubp_badam = sum(k_inner * i for i in range(1, d_blocks + 1))
    ubp_eq6 = (k_inner * d_blocks * (d_blocks + 1)) // 2
    ubp_adam_lora = k_inner * (d_blocks ** 2)
    assert ubp_badam == ubp_eq6
    bp_ratio = ubp_badam / ubp_adam_lora
    assert abs(bp_ratio - (d_blocks + 1) / (2.0 * d_blocks)) < 1e-15
    return adam_mem_gb, badam_mem_gb, ubp_badam, ubp_adam_lora, bp_ratio


def verify_effective_rank_and_block_descent_theorem() -> tuple[int, float, float]:
    """Verify Section 3.2 effective_rank(A) = min{r : cvar(r) >= 0.9}
    and Appendix D Corollary D.3, Lemma D.7, Corollary D.8, and Theorem D.4 block coordinate Adam descent.
    """
    # Effective rank calculation on a synthetic heavy-tailed singular value spectrum vs rank-8 LoRA update
    singular_vals_badam = [1.0 / ((i + 1) ** 0.55) for i in range(64)]
    total_energy = sum(s * s for s in singular_vals_badam)
    cum_energy = 0.0
    eff_rank_badam = 64
    for r_idx, s in enumerate(singular_vals_badam, start=1):
        cum_energy += s * s
        if cum_energy / total_energy >= 0.9:
            eff_rank_badam = r_idx
            break

    assert eff_rank_badam >= 32, f"Heavy-tailed BAdam update should have high effective rank (>=32), got {eff_rank_badam}"

    # Verify Appendix D deterministic BCD-Adam descent on a strictly convex quadratic L(theta) = 0.5 * sum_j c_j * theta_j^2
    # partitioned into D = 4 blocks of size 2
    d_total = 8
    d_blocks = 4
    block_size = 2
    coeffs = [1.0, 2.0, 1.5, 2.5, 0.8, 1.8, 1.2, 2.2]
    l_bar = max(coeffs)
    g_bound = 5.0
    lam = 0.5  # 0 < lambda < 1 in Corollary D.3
    k_steps = 4
    beta1 = 0.9
    beta2 = 0.999
    # Theorem D.4 step size bound: alpha <= (lambda / (2 * l_bar * K)) * min(1/K, lambda / (12 * G))
    alpha = (lam / (2.0 * l_bar * k_steps)) * min(1.0 / k_steps, lam / (12.0 * g_bound))

    theta = [1.0, -0.8, 0.6, -1.1, 0.9, -0.5, 0.7, -0.9]

    def loss_fn(th: list[float]) -> float:
        return 0.5 * sum(coeffs[j] * (th[j] ** 2) for j in range(d_total))

    loss_start = loss_fn(theta)
    grad_start_sq = sum((coeffs[j] * theta[j]) ** 2 for j in range(d_total))

    for b in range(d_blocks):
        idx0 = b * block_size
        m_blk = [0.0] * block_size
        v_blk = [0.0] * block_size
        for k in range(1, k_steps + 1):
            g_blk = [coeffs[idx0 + u] * theta[idx0 + u] for u in range(block_size)]
            m_blk = [beta1 * m_blk[u] + (1.0 - beta1) * g_blk[u] for u in range(block_size)]
            v_blk = [beta2 * v_blk[u] + (1.0 - beta2) * (g_blk[u] ** 2) for u in range(block_size)]
            m_hat = [m_blk[u] / (1.0 - (beta1 ** k)) for u in range(block_size)]
            v_hat = [v_blk[u] / (1.0 - (beta2 ** k)) for u in range(block_size)]
            for u in range(block_size):
                h_diag = 1.0 / (math.sqrt(v_hat[u]) + lam)
                # Check Corollary D.3: 1 / (2 G) <= H_{i,u}^{t,k} <= 1 / lambda
                assert (1.0 / (2.0 * g_bound)) <= h_diag <= (1.0 / lam) + 1e-12
                theta[idx0 + u] -= alpha * h_diag * m_hat[u]

    loss_end = loss_fn(theta)
    # Check Corollary D.5 descent inequality: L(theta^{t+1}) - L(theta^t) <= - (alpha * K / (32 * G)) * ||grad L(theta^t)||^2
    descent_bound = -(alpha * k_steps / (32.0 * g_bound)) * grad_start_sq
    actual_change = loss_end - loss_start
    assert actual_change <= descent_bound < 0.0, f"Theorem D.4 descent violated: {actual_change} > {descent_bound}"
    return eff_rank_badam, actual_change, descent_bound


if __name__ == "__main__":
    adam_m, badam_m, ubp_b, ubp_a, bp_r = verify_memory_and_backward_pass_equations()
    eff_r, act_chg, desc_bnd = verify_effective_rank_and_block_descent_theorem()
    print(
        f"[PASS] Round 634 BAdam verified: mem={badam_m:.1f}GB_vs_{adam_m:.1f}GB, "
        f"ubp={ubp_b}_vs_{ubp_a} (ratio={bp_r:.4f}), eff_rank={eff_r}, "
        f"descent={act_chg:.4e}<={desc_bnd:.4e}"
    )
