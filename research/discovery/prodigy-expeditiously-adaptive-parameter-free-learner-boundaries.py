#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 590:
Prodigy (An Expeditiously Adaptive Parameter-Free Learner) — Mishchenko & Defazio (ICML 2024; arXiv:2306.06101).
"""

import math
from typing import List, Tuple


def log2_plus(x: float) -> float:
    return 1.0 + math.log2(max(x, 1.0))


def verify_lemma1_bound() -> Tuple[float, float]:
    """Lemma 1 (p. 4): min_{t < N} d_{t+1} / sqrt(sum_{k=0}^t d_k^2) <= 4 sqrt(log_{2+}(d_N / d_0)) / sqrt(N)."""
    d0 = 1e-6
    dN = 5.0
    N = 120
    assert N >= 2.0 * log2_plus(dN / d0)
    # Construct a non-decreasing sequence growing from d0 to dN
    seq = [min(dN, d0 * (1.8 ** k)) for k in range(N + 1)]
    seq[-1] = dN
    lhs = min(
        seq[t + 1] / math.sqrt(sum(seq[k] ** 2 for k in range(t + 1)))
        for t in range(N)
    )
    rhs = 4.0 * math.sqrt(log2_plus(dN / d0)) / math.sqrt(N)
    assert lhs <= rhs, f"Lemma 1 violated: {lhs} > {rhs}"
    return lhs, rhs


def run_prodigy_vs_dadaptation(steps: int = 80) -> Tuple[float, float, float, float]:
    """Compare Algorithm 1 (Prodigy GD) vs D-Adaptation GD starting from d0 = 1e-6 on convex Lipschitz objective."""
    x_star = [3.0, -4.0]  # D = ||x0 - x*||_2 = 5.0
    D_true = math.hypot(x_star[0], x_star[1])
    G = 1.0
    d0 = 1e-6

    def grad_and_loss(x: List[float]) -> Tuple[float, List[float]]:
        dx0 = x[0] - x_star[0]
        dx1 = x[1] - x_star[1]
        dist = math.hypot(dx0, dx1)
        if dist < 1e-12:
            return 0.0, [0.0, 0.0]
        return G * dist, [G * dx0 / dist, G * dx1 / dist]

    # Algorithm 1: Prodigy (GD version)
    x_p = [0.0, 0.0]
    d_p = d0
    sum_d2_g2 = 0.0
    num_hat_p = 0.0
    x_avg_p = [0.0, 0.0]
    eta_sum_p = 0.0

    # D-Adaptation GD
    x_da = [0.0, 0.0]
    d_da = d0
    sum_g2_da = 0.0
    num_hat_da = 0.0
    x_avg_da = [0.0, 0.0]
    eta_sum_da = 0.0

    for k in range(steps):
        # Prodigy step
        _, g_p = grad_and_loss(x_p)
        g_norm_sq = g_p[0] ** 2 + g_p[1] ** 2
        sum_d2_g2 += (d_p ** 2) * g_norm_sq
        eta_p = (d_p ** 2) / math.sqrt((d_p ** 2) * (G ** 2) + sum_d2_g2)
        # Verify step-size inequality on p. 2 when G=0
        eta_p_nog = (d_p ** 2) / math.sqrt(sum_d2_g2)
        eta_da_equiv = d_p / math.sqrt(max(k + 1, 1) * g_norm_sq)
        assert eta_p_nog >= eta_da_equiv - 1e-12

        dot_p = g_p[0] * (0.0 - x_p[0]) + g_p[1] * (0.0 - x_p[1])
        num_hat_p += eta_p * dot_p
        x_avg_p[0] += eta_p * x_p[0]
        x_avg_p[1] += eta_p * x_p[1]
        eta_sum_p += eta_p
        x_p = [x_p[0] - eta_p * g_p[0], x_p[1] - eta_p * g_p[1]]
        dist_p0 = math.hypot(x_p[0], x_p[1])
        # Theorem 3 exponential boundedness: ||x_k - x_0|| <= 2^k d_0
        assert dist_p0 <= (2.0 ** (k + 1)) * d0 + 1e-9
        d_hat_p = num_hat_p / max(dist_p0, 1e-18)
        d_p = max(d_p, d_hat_p)
        # Lemma 2: d_k <= D for all k
        assert d_p <= D_true + 1e-9, f"Lemma 2 violated: d_p={d_p} > D={D_true}"

        # D-Adaptation step
        _, g_da = grad_and_loss(x_da)
        g_da_sq = g_da[0] ** 2 + g_da[1] ** 2
        sum_g2_da += g_da_sq
        eta_da = d_da / math.sqrt(G ** 2 + sum_g2_da)
        dot_da = g_da[0] * (0.0 - x_da[0]) + g_da[1] * (0.0 - x_da[1])
        num_hat_da += eta_da * dot_da
        x_avg_da[0] += eta_da * x_da[0]
        x_avg_da[1] += eta_da * x_da[1]
        eta_sum_da += eta_da
        x_da = [x_da[0] - eta_da * g_da[0], x_da[1] - eta_da * g_da[1]]
        dist_da0 = math.hypot(x_da[0], x_da[1])
        d_hat_da = num_hat_da / max(dist_da0, 1e-18)
        d_da = max(d_da, d_hat_da)

    x_hat_p = [x_avg_p[0] / eta_sum_p, x_avg_p[1] / eta_sum_p]
    x_hat_da = [x_avg_da[0] / eta_sum_da, x_avg_da[1] / eta_sum_da]
    loss_p, _ = grad_and_loss(x_hat_p)
    loss_da, _ = grad_and_loss(x_hat_da)
    assert d_p > d_da and loss_p < loss_da, (
        f"Expected Prodigy to adapt faster than D-Adaptation: d_p={d_p}, d_da={d_da}, loss_p={loss_p}, loss_da={loss_da}"
    )
    return d_p, d_da, loss_p, loss_da


def main() -> None:
    lhs, rhs = verify_lemma1_bound()
    d_p, d_da, loss_p, loss_da = run_prodigy_vs_dadaptation(steps=80)
    print(
        f"[PASS] Round 590 Prodigy verified: lemma1=({lhs:.4f}<={rhs:.4f}), "
        f"d_prodigy={d_p:.4f}>d_dadapt={d_da:.4f}, loss_prodigy={loss_p:.4f}<loss_dadapt={loss_da:.4f}"
    )


if __name__ == "__main__":
    main()
