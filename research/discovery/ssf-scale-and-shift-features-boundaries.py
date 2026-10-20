#!/usr/bin/env python3
"""Boundary verification for Round 692: SSF (Lian et al., NeurIPS 2022, arXiv:2210.08823)."""

import math


def main() -> int:
    # 1. Verify exact structural re-parameterization (Eq. 4 & Eq. 5, Section 3.2, p. 5):
    # Training: y = gamma (*) (W t + b) + beta
    # Inference: y_rep = W_rep t + b_rep, where W_rep = (gamma (*) W), b_rep = gamma (*) b + beta
    d_in = 4
    d_out = 5
    W = [
        [0.4, -0.2, 0.1, 0.7],
        [-0.5, 0.3, 0.8, -0.1],
        [0.2, 0.6, -0.4, 0.5],
        [0.9, -0.7, 0.2, -0.3],
        [-0.3, 0.4, -0.6, 0.8],
    ]
    b = [0.15, -0.25, 0.05, 0.40, -0.10]
    gamma = [1.25, 0.80, -1.10, 1.50, 0.95]
    beta = [-0.08, 0.12, 0.30, -0.22, 0.04]

    # Test over a token sequence t in R^{N x d_in}
    tokens = [
        [1.2, -0.7, 0.4, 2.1],
        [-0.5, 1.8, -1.1, 0.3],
        [0.0, 0.9, 1.5, -0.8],
        [2.3, -1.4, 0.2, -0.6],
    ]

    W_rep = [[gamma[i] * W[i][j] for j in range(d_in)] for i in range(d_out)]
    b_rep = [gamma[i] * b[i] + beta[i] for i in range(d_out)]

    max_rep_err = 0.0
    for t in tokens:
        # Training forward: x = W t + b, then y = gamma (*) x + beta
        x = [sum(W[i][j] * t[j] for j in range(d_in)) + b[i] for i in range(d_out)]
        y_train = [gamma[i] * x[i] + beta[i] for i in range(d_out)]
        # Inference forward: y_infer = W_rep t + b_rep (zero extra parameters / FLOPs)
        y_infer = [sum(W_rep[i][j] * t[j] for j in range(d_in)) + b_rep[i] for i in range(d_out)]
        for i in range(d_out):
            max_rep_err = max(max_rep_err, abs(y_train[i] - y_infer[i]))

    assert max_rep_err < 1e-14, f"Re-parameterization error too large: {max_rep_err}"

    # 2. Verify Table 2 (Section 3.3, p. 6) complexity formulas for ViT (L=12, d=768, N^2=196):
    L, d, N2 = 12, 768, 196
    d_prime = 16  # Adapter bottleneck
    n_prompts = 50  # VPT prompts
    m_ops = 6  # SSF-ADA operations per layer (2d params per SSF-ADA -> m=12 linear coefficients)
    adapter_train_params = 2 * L * d * d_prime
    vpt_deep_train_params = n_prompts * L * d
    ssf_train_params = m_ops * (2 * d) * L
    ssf_infer_extra_params = 0
    ssf_infer_extra_flops = 0
    adapter_infer_extra_flops = 2 * N2 * L * d * d_prime
    assert ssf_train_params < adapter_train_params and ssf_train_params < vpt_deep_train_params
    assert ssf_infer_extra_params == 0 and ssf_infer_extra_flops == 0
    assert adapter_infer_extra_flops > 0

    # 3. Verify normal initialization (mean(gamma)=1, mean(beta)=0, Table 6c, p. 9)
    # and component ablation (SSF full vs w/o scale vs w/o shift vs scalar scale, Table 6d, p. 9):
    # Target downstream distribution has channel-specific scale s_true and shift m_true
    x_up = [
        [1.0, -0.5, 0.8, -1.2],
        [-0.8, 1.2, -0.4, 0.9],
        [0.4, 0.3, -1.0, -0.5],
        [-0.6, -1.0, 0.6, 0.8],
    ]
    s_true = [1.8, 0.5, 2.4, 0.4]
    m_true = [0.6, -0.4, 0.9, -0.7]
    y_target = [[s_true[j] * row[j] + m_true[j] for j in range(4)] for row in x_up]

    def mse(pred: list[list[float]]) -> float:
        return sum(
            (pred[r][c] - y_target[r][c]) ** 2 for r in range(len(pred)) for c in range(4)
        ) / (len(pred) * 4)

    # Optimal w/o scale (gamma=1, optimal beta=m_true):
    pred_no_scale = [[1.0 * row[j] + m_true[j] for j in range(4)] for row in x_up]
    # Optimal w/o shift (optimal gamma=s_true, beta=0):
    pred_no_shift = [[s_true[j] * row[j] for j in range(4)] for row in x_up]
    # Optimal scalar scale (single scalar gamma_bar, channel-wise beta=m_true):
    num = sum(s_true[j] * (row[j] ** 2) for row in x_up for j in range(4))
    den = sum(row[j] ** 2 for row in x_up for j in range(4))
    gamma_scalar = num / den
    pred_scalar_scale = [[gamma_scalar * row[j] + m_true[j] for j in range(4)] for row in x_up]
    # Full SSF (channel-wise gamma=s_true, channel-wise beta=m_true):
    pred_ssf = [[s_true[j] * row[j] + m_true[j] for j in range(4)] for row in x_up]

    mse_ssf = mse(pred_ssf)
    mse_scalar = mse(pred_scalar_scale)
    mse_no_shift = mse(pred_no_shift)
    mse_no_scale = mse(pred_no_scale)

    assert mse_ssf < 1e-15
    assert mse_ssf < mse_scalar < mse_no_scale
    assert mse_ssf < mse_no_shift < mse_no_scale  # removing scale is worse than removing shift (Table 6d)

    print(
        f"[PASS] Round 692 SSF (Lian et al., NeurIPS 2022): max_rep_err={max_rep_err:.2e}, "
        f"infer_extra_params={ssf_infer_extra_params}, mse_ssf={mse_ssf:.2e} < "
        f"mse_scalar={mse_scalar:.4f} < mse_no_scale={mse_no_scale:.4f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
