#!/usr/bin/env python3
"""Constructed boundary verification for PACT (Parameterized Clipping Activation for Quantized Neural Networks, Choi et al., 2018)."""

import json


def pact_clip(x, alpha):
    """PACT clipping activation (Eq. 1): 0.5 * (|x| - |x - alpha| + alpha)."""
    return 0.5 * (abs(x) - abs(x - alpha) + alpha)


def pact_quantize(x, alpha, k):
    """Uniform k-bit activation quantization after PACT clipping (Eq. 2)."""
    y = pact_clip(x, alpha)
    levels = (1 << k) - 1
    return round(y * levels / alpha) * (alpha / levels)


def pact_grad_alpha(x, alpha):
    """Straight-Through Estimator gradient w.r.t. clipping level alpha (Eq. 3)."""
    return 1.0 if x >= alpha else 0.0


def main():
    xs = [-2.5, -0.4, 0.0, 0.35, 0.8, 1.4, 2.2, 3.8, 6.5]
    k = 2  # 2-bit activation quantization (4 levels)

    # Standard ReLU clips at max(xs) = 6.5 -> large quantization step size 6.5 / 3 = 2.167
    alpha_max = max(xs)
    mse_max_clip = sum((max(0.0, x) - pact_quantize(x, alpha_max, k)) ** 2 for x in xs) / len(xs)

    # Optimize alpha via gradient descent with L2 regularization lambda_alpha * alpha^2 (Section 2.1)
    alpha = 4.0
    lr = 0.25
    lambda_alpha = 0.02
    for _ in range(60):
        grad = 0.0
        for x in xs:
            target = max(0.0, min(x, 2.5))  # ideal bounded activation response
            y_q = pact_quantize(x, alpha, k)
            dl_dyq = 2.0 * (y_q - target) / len(xs)
            grad += dl_dyq * pact_grad_alpha(x, alpha)
        grad += 2.0 * lambda_alpha * alpha
        alpha -= lr * grad

    mse_pact = sum((max(0.0, min(x, 2.5)) - pact_quantize(x, alpha, k)) ** 2 for x in xs) / len(xs)

    # Verify Eq. 1 exact piecewise identity
    for x in xs:
        piecewise = 0.0 if x < 0.0 else (x if x < alpha else alpha)
        assert abs(pact_clip(x, alpha) - piecewise) < 1e-12

    # Verify learned alpha shrinks clipping range below outlier max and lowers quantization MSE
    assert 1.5 < alpha < 3.0, f"Expected learned alpha in (1.5, 3.0), got {alpha}"
    assert mse_pact < mse_max_clip * 0.25

    summary = {
        "concept": "PACTParameterizedClippingActivationForQuantizedNeuralNetworks",
        "bitwidth_k": k,
        "outlier_max_alpha": round(alpha_max, 4),
        "learned_pact_alpha": round(alpha, 4),
        "mse_unclipped_max_range": round(mse_max_clip, 6),
        "mse_pact_learned_alpha": round(mse_pact, 6),
        "eq1_piecewise_identity_verified": True,
        "verification": "passed",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
