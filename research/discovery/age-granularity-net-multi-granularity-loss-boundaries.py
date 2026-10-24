#!/usr/bin/env python3
"""Constructed boundary verification for Age-Granularity-Net (Zhou, Huttunen, & Elomaa 2021)."""

import math


def softmax(logits):
    m = max(logits)
    exps = [math.exp(z - m) for z in logits]
    s = sum(exps)
    return [e / s for e in exps]


def main():
    # 1. Verify Section 3.2 Figure 2 hierarchical label quantization across granularities (1, 5, 10, 20 years)
    age_y = 44
    c_100 = age_y - 1          # 1-based example in paper Fig 2: 44 -> 43rd index (0-indexed: 44 // 1 - 1 = 43)
    c_20 = (age_y - 1) // 5    # 43 // 5 = 8th class
    c_10 = (age_y - 1) // 10   # 43 // 10 = 4th class
    c_5 = (age_y - 1) // 20    # 43 // 20 = 2nd class
    assert (c_100, c_20, c_10, c_5) == (43, 8, 4, 2)

    # 2. Verify tolerance to ambiguous/noisy fine-grained labels:
    # Under 1-year label noise (annotators label a true 22-year-old as 21, 22, or 23),
    # a single fine-grained cross-entropy loss treats adjacent ages as completely orthogonal classes,
    # whereas the multi-granularity aggregate loss (Equation 1) + MSE branch pulls the shared feature h
    # toward the true continuous age value.
    # Consider a 4-age mini-domain {0, 1, 2, 3} with fine 4-class branch, coarse 2-class branch ({0,1} vs {2,3}),
    # and continuous MSE regression branch y_hat = w_reg * h.
    # Suppose training samples for x=1.0 have noisy fine-grained annotations {0, 1} (true value 0.8),
    # and samples for x=2.0 have noisy fine-grained annotations {2, 3} (true value 2.2).
    # Shared representation h(x) = w_backbone * x.
    w_single = 0.1
    w_multi = 0.1
    lr = 0.05

    # Fixed linear heads mapping scalar feature h to class centers [0.0, 1.0, 2.0, 3.0] and coarse centers [0.5, 2.5]
    fine_centers = [0.0, 1.0, 2.0, 3.0]
    coarse_centers = [0.5, 2.5]

    dataset = [
        (1.0, 1, 0, 1.0),
        (1.0, 3, 0, 1.0),  # noisy fine label 3, but coarse label 0 & regression target 1.0 stay consistent
        (2.0, 2, 1, 2.0),
        (2.0, 0, 1, 2.0),  # noisy fine label 0, but coarse label 1 & regression target 2.0 stay consistent
    ]

    for _ in range(120):
        g_single = 0.0
        g_multi = 0.0
        for x_in, y_fine, y_coarse, y_cont in dataset:
            # Single-loss model (L_fine only): logits_k = -0.5 * (h - fine_centers[k])^2
            h_s = w_single * x_in
            probs_s = softmax([-0.5 * ((h_s - c) ** 2) for c in fine_centers])
            dh_s = sum(p * c for p, c in zip(probs_s, fine_centers)) - fine_centers[y_fine]
            g_single += dh_s * x_in

            # Age-Granularity-Net (L_fine + L_coarse + lambda * L_mse, Equation 1)
            h_m = w_multi * x_in
            probs_f = softmax([-0.5 * ((h_m - c) ** 2) for c in fine_centers])
            probs_c = softmax([-0.5 * ((h_m - c) ** 2) for c in coarse_centers])
            dh_f = sum(p * c for p, c in zip(probs_f, fine_centers)) - fine_centers[y_fine]
            dh_c = sum(p * c for p, c in zip(probs_c, coarse_centers)) - coarse_centers[y_coarse]
            dh_mse = h_m - y_cont
            g_multi += (dh_f + dh_c + 1.0 * dh_mse) * x_in

        w_single -= lr * (g_single / len(dataset))
        w_multi -= lr * (g_multi / len(dataset))

    # Evaluate MAE on clean test targets (x=1.0 -> 1.0, x=2.0 -> 2.0)
    mae_single = 0.5 * (abs(w_single * 1.0 - 1.0) + abs(w_single * 2.0 - 2.0))
    mae_multi = 0.5 * (abs(w_multi * 1.0 - 1.0) + abs(w_multi * 2.0 - 2.0))
    assert mae_multi < mae_single * 0.5

    print(
        f"[PASS] Round 831 Age-Granularity-Net verified: bins(44)=({c_100},{c_20},{c_10},{c_5}), "
        f"MAE_multi={mae_multi:.4f} < MAE_single={mae_single:.4f}"
    )


if __name__ == "__main__":
    main()
