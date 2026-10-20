#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 728: Calibrate Before Use (Zhao et al., ICML 2021)."""

import math


def verify_contextual_calibration() -> None:
    # 1. Contextual Calibration via diagonal vector scaling W = diag(p_hat_cf)^{-1} (Section 5, Eq. 1):
    # Average content-free probabilities across {"N/A", "[MASK]", ""}
    p_cf_samples = [
        [0.62, 0.38],  # "N/A"
        [0.60, 0.40],  # "[MASK]"
        [0.64, 0.36],  # ""
    ]
    n_classes = 2
    p_hat_cf = [
        sum(s[c] for s in p_cf_samples) / len(p_cf_samples)
        for c in range(n_classes)
    ]
    assert math.isclose(p_hat_cf[0], 0.62, rel_tol=1e-12)
    assert math.isclose(p_hat_cf[1], 0.38, rel_tol=1e-12)

    # Diagonal calibration matrix W = diag(p_hat_cf)^{-1}, b = 0
    w_diag = [1.0 / p_hat_cf[c] for c in range(n_classes)]

    # Verify content-free input produces uniform calibrated scores:
    q_cf_unnorm = [w_diag[c] * p_hat_cf[c] for c in range(n_classes)]
    assert all(math.isclose(v, 1.0, rel_tol=1e-12) for v in q_cf_unnorm)

    # Test example where uncalibrated p_hat = [0.58, 0.42] falsely predicts class 0 (Positive) due to recency/majority bias,
    # whereas calibrated W * p_hat = [0.58/0.62, 0.42/0.38] = [0.9355, 1.1053] rightly predicts class 1 (Negative)!
    p_test = [0.58, 0.42]
    assert p_test[0] > p_test[1]  # uncalibrated false positive
    q_test = [w_diag[c] * p_test[c] for c in range(n_classes)]
    assert q_test[1] > q_test[0]  # calibrated correct negative prediction
    print("Contextual Calibration verification passed.")


if __name__ == "__main__":
    verify_contextual_calibration()
