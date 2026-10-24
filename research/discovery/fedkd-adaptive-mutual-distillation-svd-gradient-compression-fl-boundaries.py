#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 504: FedKD (Wu et al., Nature Communications 2022 / arXiv:2108.13323)."""

import math


def kl_div(p: list[float], q: list[float]) -> float:
    return sum(pi * math.log(pi / qi) for pi, qi in zip(p, q) if pi > 0.0)


def cross_entropy(gold_idx: int, probs: list[float]) -> float:
    return -math.log(probs[gold_idx])


def adaptive_mutual_losses(
    gold_idx: int,
    y_t: list[float],
    y_s: list[float],
    mse_hidden_att: float,
) -> tuple[float, float, float]:
    """Compute unified teacher and student losses and adaptive weight 1/(L_t^t + L_s^t) (Eqs. 1-7, p. 4)."""
    l_t_task = cross_entropy(gold_idx, y_t)
    l_s_task = cross_entropy(gold_idx, y_s)
    denom = l_t_task + l_s_task
    weight = 1.0 / denom
    l_t_distill = kl_div(y_s, y_t) / denom
    l_s_distill = kl_div(y_t, y_s) / denom
    l_hidden = mse_hidden_att / denom
    l_t_total = l_t_distill + l_hidden + l_t_task
    l_s_total = l_s_distill + l_hidden + l_s_task
    return l_t_total, l_s_total, weight


def dynamic_svd_rank(singular_values: list[float], t_progress: float, t_start: float = 0.95, t_end: float = 0.98) -> tuple[int, float]:
    """Compute minimum retained singular values K satisfying cumulative energy > T(t) (Eqs. 8-9, p. 5)."""
    threshold = t_start + (t_end - t_start) * t_progress
    total_energy = sum(s * s for s in singular_values)
    cum = 0.0
    for k, s in enumerate(singular_values, start=1):
        cum += s * s
        if (cum / total_energy) > threshold:
            return k, threshold
    return len(singular_values), threshold


def main() -> None:
    # 1. Verify Adaptive Mutual Distillation weighting (Eqs. 1-7, p. 4):
    # Early in training when teacher and student predictions are inaccurate (low probability on gold class 0),
    # task losses L_t^t + L_s^t are large, so distillation intensity weight = 1/(L_t^t + L_s^t) is small.
    # Later in training when both predictions are accurate, task losses are small and distillation weight increases.
    _, _, w_early = adaptive_mutual_losses(
        gold_idx=0,
        y_t=[0.20, 0.80],
        y_s=[0.25, 0.75],
        mse_hidden_att=0.5,
    )
    _, _, w_late = adaptive_mutual_losses(
        gold_idx=0,
        y_t=[0.90, 0.10],
        y_s=[0.85, 0.15],
        mse_hidden_att=0.5,
    )
    assert w_late > 4.0 * w_early

    # 2. Verify Dynamic SVD Gradient Approximation schedule and parameter compression condition (Eqs. 8-9, p. 5):
    # Gradient matrix g in R^{P x Q} with P=128, Q=64 and decaying singular spectrum
    P, Q = 128, 64
    sigmas = [1.0 / (i ** 1.3) for i in range(1, Q + 1)]
    k_start, thresh_start = dynamic_svd_rank(sigmas, t_progress=0.0, t_start=0.95, t_end=0.98)
    k_end, thresh_end = dynamic_svd_rank(sigmas, t_progress=1.0, t_start=0.95, t_end=0.98)

    assert math.isclose(thresh_start, 0.95, abs_tol=1e-12)
    assert math.isclose(thresh_end, 0.98, abs_tol=1e-12)
    # More singular values are retained at the end of training than at the start (Section 4.6, Fig. 7, p. 8)
    assert k_end > k_start

    # Check compression condition PK + K^2 + KQ < PQ (Section 3.3, p. 5)
    compressed_size_end = P * k_end + (k_end ** 2) + k_end * Q
    full_size = P * Q
    compression_ratio = full_size / compressed_size_end
    assert compressed_size_end < full_size
    assert compression_ratio > 1.5

    print(
        f"[PASS] Round 504 FedKD (Wu et al., Nat. Commun. 2022): "
        f"w_early={w_early:.4f} -> w_late={w_late:.4f}, "
        f"K(t=0)={k_start} (T={thresh_start:.2f}) -> K(t=1)={k_end} (T={thresh_end:.2f}), "
        f"compression_ratio={compression_ratio:.2f}x"
    )


if __name__ == "__main__":
    main()
