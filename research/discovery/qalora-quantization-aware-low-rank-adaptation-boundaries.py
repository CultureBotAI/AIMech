#!/usr/bin/env python3
"""Constructed boundary verification for Round 661:
QA-LoRA: Quantization-Aware Low-Rank Adaptation of Large Language Models
(Xu, Xie, Gu, Chen, Chang, Zhang, Chen, Zhang, & Tian, ICLR 2024, arXiv:2309.14717).

Verifies:
1. Group-wise asymmetric quantization W_tilde = A_scale (o) (W_hat - B_zero) with
   L groups along D_in (group size g = D_in // L) and N-bit integers W_hat in {0, ..., 2^N - 1}.
2. Group-wise input summation A(x)_l = sum_{r=1}^g x_{(l-1)g + r} (Algorithm 1 & Equation 3)
   paired with low-rank adapter L_1 in R^{L x D_int}, L_2 in R^{D_int x D_out}.
3. Exact lossless inference merging (Algorithm 1 `merge_with_quantization` & Equation 7):
   updating only the group-wise zero-point matrix B_new = B_zero - s * (L_1 L_2) / A_scale
   keeps W_hat in N-bit integer format and reproduces the unmerged forward pass
   y = x^T W_tilde + s * A(x)^T L_1 L_2 to machine precision (0 PTQ discrepancy),
   whereas unconstrained LoRA + post-training re-quantization (QLoRA w/ PTQ) incurs
   non-zero quantization error.
"""

from __future__ import annotations
import math
import random


def groupwise_quantize(
    W: list[list[float]], L: int, bits: int
) -> tuple[list[list[int]], list[list[float]], list[list[float]]]:
    """Quantize W in R^{D_in x D_out} with L groups per column (group size g = D_in // L).
    Follows Appendix B.1 Equation (2): W_tilde_{i,j} = alpha_{i//g, j} * (W_hat_{i,j} - beta_{i//g, j})."""
    D_in = len(W)
    D_out = len(W[0])
    g = D_in // L
    qmax = (1 << bits) - 1

    W_hat = [[0] * D_out for _ in range(D_in)]
    alpha = [[0.0] * D_out for _ in range(L)]
    beta = [[0.0] * D_out for _ in range(L)]

    for l in range(L):
        r_start = l * g
        r_end = r_start + g
        for j in range(D_out):
            col_slice = [W[i][j] for i in range(r_start, r_end)]
            w_min = min(col_slice)
            w_max = max(col_slice)
            scale = (w_max - w_min) / qmax if w_max > w_min else 1e-8
            zero = -w_min / scale
            alpha[l][j] = scale
            beta[l][j] = zero
            for i in range(r_start, r_end):
                q = int(round(W[i][j] / scale + zero))
                q = max(0, min(qmax, q))
                W_hat[i][j] = q
    return W_hat, alpha, beta


def dequantize_forward(
    x: list[float],
    W_hat: list[list[int]],
    alpha: list[list[float]],
    beta: list[list[float]],
) -> list[float]:
    """Compute y = x^T W_tilde where W_tilde_{i,j} = alpha_{i//g, j} * (W_hat_{i,j} - beta_{i//g, j})."""
    D_in = len(W_hat)
    D_out = len(W_hat[0])
    L = len(alpha)
    g = D_in // L
    y = [0.0] * D_out
    for j in range(D_out):
        acc = 0.0
        for i in range(D_in):
            l = i // g
            w_tilde_ij = alpha[l][j] * (W_hat[i][j] - beta[l][j])
            acc += x[i] * w_tilde_ij
        y[j] = acc
    return y


def main() -> None:
    rng = random.Random(20230914)
    D_in, D_out, D_int = 32, 16, 4
    L = 8  # group size g = 32 // 8 = 4
    g = D_in // L
    bits = 4
    s = 0.5

    W = [[rng.gauss(0.0, 1.0) for _ in range(D_out)] for _ in range(D_in)]
    W_hat, alpha, beta = groupwise_quantize(W, L=L, bits=bits)

    # QA-LoRA parameters: L1 in R^{L x D_int}, L2 in R^{D_int x D_out}
    L1 = [[rng.gauss(0.0, 0.2) for _ in range(D_int)] for _ in range(L)]
    L2 = [[rng.gauss(0.0, 0.2) for _ in range(D_out)] for _ in range(D_int)]
    P = [
        [sum(L1[l][k] * L2[k][j] for k in range(D_int)) for j in range(D_out)]
        for l in range(L)
    ]

    x = [rng.uniform(-1.0, 1.0) for _ in range(D_in)]

    # 1. Unmerged QA-LoRA training forward pass (Algorithm 1 `qalora_forward` & Equation 4)
    y_base = dequantize_forward(x, W_hat, alpha, beta)
    # Group-wise input aggregation h^a_l = sum_{r=0}^{g-1} x_{l*g + r}
    h_agg = [sum(x[l * g + r] for r in range(g)) for l in range(L)]
    y_unmerged = [
        y_base[j] + s * sum(h_agg[l] * P[l][j] for l in range(L))
        for j in range(D_out)
    ]

    # 2. Merged QA-LoRA inference forward pass (Algorithm 1 `merge_with_quantization` & Equation 7)
    # beta_new[l][j] = beta[l][j] - s * P[l][j] / alpha[l][j]
    beta_new = [
        [beta[l][j] - s * P[l][j] / alpha[l][j] for j in range(D_out)]
        for l in range(L)
    ]
    y_merged = dequantize_forward(x, W_hat, alpha, beta_new)

    max_merge_err = max(abs(a - b) for a, b in zip(y_unmerged, y_merged))
    assert max_merge_err < 1e-12, f"Expected lossless QA-LoRA merge, got {max_merge_err}"

    # 3. Compare against unconstrained LoRA + Post-Training Quantization (PTQ)
    A_unc = [[rng.gauss(0.0, 0.2) for _ in range(D_int)] for _ in range(D_in)]
    W_merged_fp = [
        [
            alpha[i // g][j] * (W_hat[i][j] - beta[i // g][j])
            + s * sum(A_unc[i][k] * L2[k][j] for k in range(D_int))
            for j in range(D_out)
        ]
        for i in range(D_in)
    ]
    y_unc_fp = [sum(x[i] * W_merged_fp[i][j] for i in range(D_in)) for j in range(D_out)]
    W_hat_ptq, alpha_ptq, beta_ptq = groupwise_quantize(W_merged_fp, L=L, bits=bits)
    y_unc_ptq = dequantize_forward(x, W_hat_ptq, alpha_ptq, beta_ptq)
    ptq_err = math.sqrt(sum((a - b) ** 2 for a, b in zip(y_unc_fp, y_unc_ptq)))
    assert ptq_err > 0.05, f"Expected non-zero PTQ error for unconstrained LoRA, got {ptq_err}"

    # 4. Verify parameter count reduction of A from D_in * D_int to L * D_int
    params_qlora_adapter = D_in * D_int + D_int * D_out
    params_qalora_adapter = L * D_int + D_int * D_out
    assert params_qalora_adapter < params_qlora_adapter

    print(
        f"[PASS] Round 661 QA-LoRA (Xu et al. 2024): "
        f"max_merge_err={max_merge_err:.2e} << ptq_err={ptq_err:.4f}, "
        f"adapter_params={params_qalora_adapter}<{params_qlora_adapter}"
    )


if __name__ == "__main__":
    main()
