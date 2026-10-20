#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 633: Accordion (Agarwal et al., MLSys 2021)."""

from __future__ import annotations

import math


def accordion_select_level(
    norm_prev: float,
    norm_curr: float,
    lr_curr: float,
    lr_next: float,
    eta: float,
    level_low: str,
    level_high: str,
) -> str:
    """Algorithm 1: Accordion critical regime detector and compression/batch-size selector."""
    rel_change = abs(norm_prev - norm_curr) / norm_prev if norm_prev > 0.0 else 1.0
    if rel_change >= eta or lr_next < lr_curr:
        return level_low
    return level_high


def verify_algorithm1_schedule_and_savings() -> tuple[int, int, float]:
    """Verify Algorithm 1 critical regime detection on a 300-epoch CIFAR-100 ResNet-18 schedule
    (check every 10 epochs, LR decay at epochs 150 and 250, eta = 0.5).
    """
    eta = 0.5
    # Simulate 30 check windows (10 epochs each, total 300 epochs)
    # Rapid gradient norm decay occurs in early epochs (windows 0, 1) and right after LR drops at epoch 150 (window 15) and 250 (window 25)
    norms = [
        5.0, 2.0, 0.9, 0.85, 0.82, 0.80, 0.79, 0.78, 0.77, 0.76,
        0.75, 0.75, 0.74, 0.74, 0.73, 0.30, 0.28, 0.27, 0.27, 0.26,
        0.26, 0.26, 0.25, 0.25, 0.25, 0.10, 0.09, 0.09, 0.09, 0.09,
    ]
    lrs = [0.4] * 15 + [0.04] * 10 + [0.004] * 5

    low_count = 0
    high_count = 0
    norm_prev = 12.0  # initial steep drop in first window
    for w in range(len(norms)):
        lr_curr = lrs[w]
        lr_next = lrs[w + 1] if w + 1 < len(lrs) else lrs[w]
        choice = accordion_select_level(norm_prev, norms[w], lr_curr, lr_next, eta, "LOW_COMP", "HIGH_COMP")
        if choice == "LOW_COMP":
            low_count += 1
        else:
            high_count += 1
        norm_prev = norms[w]

    # Critical regimes occur at the beginning and around LR decays (epochs 150, 250), leaving most epochs in HIGH_COMP
    assert 4 <= low_count <= 7, f"Expected 4..7 critical regime windows, got {low_count}"
    assert high_count == 30 - low_count

    # Batch size switching communication reduction (Section 3 & Table 5/6):
    # Using B_low = 512 in critical windows and B_high = 4096 (8x fewer steps per epoch) outside critical windows:
    low_frac = low_count / 30.0
    comm_ratio = 1.0 / (low_frac + (1.0 - low_frac) / (4096.0 / 512.0))
    assert 3.0 < comm_ratio < 6.0, f"Expected batch-size communication reduction in (3x, 6x), got {comm_ratio}"
    return low_count, high_count, comm_ratio


def verify_appendix_b_lemma1_sparse_mean_plus_dense_noise() -> tuple[int, float, float]:
    """Verify Appendix B Lemma 1:
    For LASSO 1/2 ||X w - y||_2^2 + lambda ||w||_1 with x_+ ~ N(mu, sigma^2 I), x_- ~ N(-mu, sigma^2 I),
    E[grad_w l(w; x, y)] = w + lambda * sign(w) + mu * (mu^T w) has support size <= k1 + k2,
    and Chebyshev bound ((sigma^4 + 2 ||mu||_max^2 sigma^2) ||w||_2^2 + sigma^2) / gamma^2 == eps / (n d).
    """
    d = 10
    # mu is k2 = 2 sparse (indices 0, 1); w is k1 = 3 sparse (indices 1, 2, 3)
    mu = [1.5, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    w = [0.0, 0.8, -1.2, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    lam = 0.1

    k2 = sum(1 for x in mu if abs(x) > 0.0)
    k1 = sum(1 for x in w if abs(x) > 0.0)
    mu_dot_w = sum(mu[j] * w[j] for j in range(d))

    expected_grad = []
    for j in range(d):
        sgn = (1.0 if w[j] > 0.0 else (-1.0 if w[j] < 0.0 else 0.0))
        val = w[j] + lam * sgn + mu[j] * mu_dot_w
        expected_grad.append(val)

    support_size = sum(1 for x in expected_grad if abs(x) > 0.0)
    assert support_size <= k1 + k2, f"Lemma 1 sparsity violated: {support_size} > {k1 + k2}"

    nonzero_vals = [abs(x) for x in expected_grad if abs(x) > 0.0]
    gamma = min(nonzero_vals)
    eps = 0.05
    n_samples = 16
    target_rhs = eps / (n_samples * d)

    w_norm_sq = sum(x * x for x in w)
    mu_max_sq = max(x * x for x in mu)

    # Solve for small sigma > 0 such that ((sigma^4 + 2 * mu_max^2 * sigma^2) * w_norm_sq + sigma^2) / gamma^2 <= target_rhs
    sigma = math.sqrt((target_rhs * (gamma ** 2)) / (2.0 * (2.0 * mu_max_sq * w_norm_sq + 1.0)))
    chebyshev_lhs = (((sigma ** 4) + 2.0 * mu_max_sq * (sigma ** 2)) * w_norm_sq + (sigma ** 2)) / (gamma ** 2)
    assert 0.0 < chebyshev_lhs <= target_rhs
    return support_size, gamma, chebyshev_lhs


if __name__ == "__main__":
    low_c, high_c, comm_r = verify_algorithm1_schedule_and_savings()
    supp, gamma, cheb = verify_appendix_b_lemma1_sparse_mean_plus_dense_noise()
    print(
        f"[PASS] Round 633 Accordion verified: critical_windows={low_c}/30, "
        f"high_comp_windows={high_c}/30, bs_comm_red={comm_r:.2f}x, "
        f"lemma1_supp={supp}<=5, gamma={gamma:.4f}, cheb={cheb:.2e}"
    )
