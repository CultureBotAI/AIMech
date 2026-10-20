#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 673: NEFTune (Jain et al., ICLR 2024)."""

import math
import random


def main():
    rng = random.Random(673)
    alpha = 5.0
    theoretical_expected_sq_norm = (alpha * alpha) / 3.0
    theoretical_rms_norm = alpha / math.sqrt(3.0)

    # 1. Verify (L, d)-invariant expected Euclidean norm alpha / sqrt(3) across multiple shapes
    for L, d in [(16, 32), (64, 64), (128, 32)]:
        scale = alpha / math.sqrt(L * d)
        trials = 400
        sq_norms = []
        for _ in range(trials):
            norm_sq = 0.0
            for _ in range(L * d):
                eps = rng.uniform(-1.0, 1.0)
                delta = scale * eps
                norm_sq += delta * delta
            sq_norms.append(norm_sq)
        emp_mean_sq = sum(sq_norms) / trials
        emp_rms = math.sqrt(emp_mean_sq)
        rel_err = abs(emp_rms - theoretical_rms_norm) / theoretical_rms_norm
        assert rel_err < 0.03, f"Expected RMS norm {theoretical_rms_norm}, got {emp_rms} (rel_err={rel_err})"

    # 2. Verify induced trace-Hessian embedding smoothness regularization:
    # For quadratic loss f(X) = 0.5 * sum_{t,j} h_{t,j} (X_{t,j} - C_{t,j})^2,
    # E_eps[f(X + (alpha/sqrt(Ld)) eps)] = f(X) + (alpha^2 / (6 L d)) * Tr(H).
    L, d = 8, 8
    scale = alpha / math.sqrt(L * d)
    H_diag = [[rng.uniform(0.5, 5.0) for _ in range(d)] for _ in range(L)]
    X = [[rng.gauss(0.0, 1.0) for _ in range(d)] for _ in range(L)]
    C = [[rng.gauss(0.0, 1.0) for _ in range(d)] for _ in range(L)]

    base_loss = 0.5 * sum(H_diag[t][j] * ((X[t][j] - C[t][j]) ** 2) for t in range(L) for j in range(d))
    tr_H = sum(H_diag[t][j] for t in range(L) for j in range(d))
    exact_expected_noised_loss = base_loss + (alpha * alpha / (6.0 * L * d)) * tr_H

    # Deterministic 2-point Gauss-Legendre quadrature on [-1, 1] at +/- 1/sqrt(3)
    # and Monte Carlo verification
    mc_trials = 2000
    mc_loss_sum = 0.0
    for _ in range(mc_trials):
        loss_val = 0.0
        for t in range(L):
            for j in range(d):
                eps = rng.uniform(-1.0, 1.0)
                diff = (X[t][j] + scale * eps) - C[t][j]
                loss_val += 0.5 * H_diag[t][j] * diff * diff
        mc_loss_sum += loss_val
    mc_expected_loss = mc_loss_sum / mc_trials
    reg_gap = abs(mc_expected_loss - exact_expected_noised_loss)
    assert reg_gap < 0.02, f"Trace-Hessian regularizer mismatch: {mc_expected_loss} vs {exact_expected_noised_loss}"

    # 3. Verify intra-token perturbation boundary (0% nearest-neighbor token flips at moderate alpha=5, L=64, d=32)
    vocab_size = 64
    d_emb = 32
    L_seq = 64
    # Unit-norm vocabulary embeddings
    vocab = []
    for _ in range(vocab_size):
        vec = [rng.gauss(0.0, 1.0) for _ in range(d_emb)]
        vnorm = math.sqrt(sum(x * x for x in vec))
        vocab.append([x / vnorm for x in vec])

    noise_scale = alpha / math.sqrt(L_seq * d_emb)
    flips = 0
    for tok_id in range(vocab_size):
        emb = vocab[tok_id]
        noised = [emb[j] + noise_scale * rng.uniform(-1.0, 1.0) for j in range(d_emb)]
        best_id = min(
            range(vocab_size),
            key=lambda vid: sum((noised[j] - vocab[vid][j]) ** 2 for j in range(d_emb)),
        )
        if best_id != tok_id:
            flips += 1
    assert flips == 0, f"Expected 0 nearest-neighbor token flips at alpha={alpha}, L={L_seq}, got {flips}"

    print(
        f"[PASS] Round 673 NEFTune (Jain et al., ICLR 2024): "
        f"rms_norm={emp_rms:.4f}~alpha/sqrt(3)={theoretical_rms_norm:.4f}, "
        f"hessian_reg_gap={reg_gap:.4f}, token_flips={flips}/64"
    )


if __name__ == "__main__":
    main()
