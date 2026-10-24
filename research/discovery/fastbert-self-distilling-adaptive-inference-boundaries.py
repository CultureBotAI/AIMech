#!/usr/bin/env python3
"""Constructed boundary and mathematical verification for Round 807:
FastBERT: a Self-distilling BERT with Adaptive Inference Time
(Liu, Zhou, Zhao, Wang, Deng, & Ju, ACL 2020, arXiv:2004.02178).

Verifies:
1. Normalized entropy Uncertainty measure (Eq. 7):
   Uncertainty(p_s) = (sum_{i=1}^N p_s(i) log p_s(i)) / log(1 / N) in [0, 1]
   attains 0.0 on one-hot (deterministic) class distributions, 1.0 on the uniform distribution p_s(i) = 1/N,
   and increases monotonically as class probability mass spreads across N classes.
2. Self-distillation branch objective (Eqs. 5-6):
   Loss(p_{s_0}, ..., p_{s_{L-2}}, p_t) = sum_{i=0}^{L-2} D_KL(p_{s_i}, p_t)
   is non-negative and equals zero if and only if every intermediate branch classifier i = 0..L-2 matches
   the frozen top-layer teacher classifier distribution p_t.
3. Sample-wise adaptive inference FLOPs accounting (Section 3.3 & Table 1):
   With per-layer Transformer FLOPs F_tr = 1809.9M and branch classifier FLOPs F_cls = 46.1M (only 2.55% of
   a Transformer block), increasing the Speed threshold in [0, 1] monotonically decreases expected executed
   layers and total FLOPs, achieving up to ~11.7x speedup when samples exit at layer 0.
"""

import json
import math


def normalized_entropy_uncertainty(probs):
    """Eq. 7: Uncertainty = (sum_{i=1}^N p_s(i) log p_s(i)) / log(1/N)."""
    N = len(probs)
    assert N >= 2
    assert abs(sum(probs) - 1.0) < 1e-9
    num = sum(p * math.log(p) for p in probs if p > 0.0)
    den = math.log(1.0 / N)
    return num / den


def self_distillation_loss(student_branch_dists, teacher_dist):
    """Eqs. 5-6: sum_{i=0}^{L-2} sum_{c=1}^N p_{s_i}(c) log(p_{s_i}(c) / p_t(c))."""
    total = 0.0
    for ps in student_branch_dists:
        kl = sum(ps_c * math.log(max(ps_c, 1e-15) / max(pt_c, 1e-15)) for ps_c, pt_c in zip(ps, teacher_dist) if ps_c > 0)
        total += kl
    return total


def sample_adaptive_flops(sample_uncertainties_per_layer, speed_threshold, f_tr=1809.9, f_cls=46.1):
    """Compute per-sample exit layer (0..L-1) and total FLOPs in millions (Table 1)."""
    L = len(sample_uncertainties_per_layer) + 1  # L-1 student branches + 1 teacher layer
    for layer_idx, u in enumerate(sample_uncertainties_per_layer):
        if u < speed_threshold:
            # Exits at layer_idx after running (layer_idx + 1) Transformer blocks and (layer_idx + 1) classifiers
            flops = (layer_idx + 1) * (f_tr + f_cls)
            return layer_idx, flops
    # Reaches final layer L-1 (runs all L Transformer blocks and all L classifiers)
    return L - 1, L * (f_tr + f_cls)


def main():
    # 1. Verify Eq. 7 normalized entropy boundary values for N = 3 classes
    u_one_hot = normalized_entropy_uncertainty([1.0, 0.0, 0.0])
    u_low = normalized_entropy_uncertainty([0.92, 0.05, 0.03])
    u_high = normalized_entropy_uncertainty([0.45, 0.35, 0.20])
    u_uniform = normalized_entropy_uncertainty([1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0])

    assert abs(u_one_hot - 0.0) < 1e-12
    assert 0.0 < u_low < 0.31
    assert 0.85 < u_high < 1.0
    assert abs(u_uniform - 1.0) < 1e-12

    # 2. Verify Eqs. 5-6 branch self-distillation loss
    p_t = [0.85, 0.10, 0.05]
    branches_untrained = [[1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0] for _ in range(11)]
    branches_distilled = [[0.84, 0.11, 0.05] for _ in range(11)]
    loss_untrained = self_distillation_loss(branches_untrained, p_t)
    loss_distilled = self_distillation_loss(branches_distilled, p_t)
    loss_exact = self_distillation_loss([p_t for _ in range(11)], p_t)
    assert loss_untrained > 6.0
    assert loss_distilled < 0.01
    assert abs(loss_exact) < 1e-15

    # 3. Verify Table 1 FLOPs and monotonic speedup across Speed thresholds
    # Full 12-layer BERT FLOPs reported in Table 2 = 21785M; 12 * 1809.9M + 46.1M = 21764.9M
    # Single-layer exit FLOPs = 1809.9M + 46.1M = 1856.0M (~11.74x speedup vs 21785M)
    batch_uncertainties = [
        [0.05, 0.04, 0.03, 0.02, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01],  # easy sample
        [0.42, 0.28, 0.18, 0.08, 0.06, 0.05, 0.04, 0.03, 0.02, 0.02, 0.01],  # medium sample
        [0.75, 0.68, 0.60, 0.52, 0.44, 0.35, 0.25, 0.19, 0.14, 0.09, 0.07],  # hard sample
        [0.88, 0.82, 0.79, 0.74, 0.69, 0.64, 0.58, 0.53, 0.48, 0.42, 0.38],  # very hard sample
    ]

    avg_flops_by_speed = {}
    for speed in [0.0, 0.1, 0.5, 0.8, 1.0]:
        total_f = sum(sample_adaptive_flops(u_seq, speed)[1] for u_seq in batch_uncertainties)
        avg_flops_by_speed[speed] = total_f / len(batch_uncertainties)

    assert avg_flops_by_speed[0.0] > avg_flops_by_speed[0.1] > avg_flops_by_speed[0.5] > avg_flops_by_speed[0.8] >= avg_flops_by_speed[1.0]
    max_speedup = 21785.0 / avg_flops_by_speed[1.0]
    assert 11.70 < max_speedup < 11.80

    summary = {
        "concept": "FastBERTSelfDistillingBERTWithAdaptiveInferenceTime",
        "uncertainty_one_hot": u_one_hot,
        "uncertainty_low": round(u_low, 6),
        "uncertainty_uniform": u_uniform,
        "self_distill_loss_untrained": round(loss_untrained, 4),
        "self_distill_loss_distilled": round(loss_distilled, 6),
        "avg_flops_speed_01": round(avg_flops_by_speed[0.1], 2),
        "avg_flops_speed_05": round(avg_flops_by_speed[0.5], 2),
        "avg_flops_speed_08": round(avg_flops_by_speed[0.8], 2),
        "layer0_exit_speedup": round(max_speedup, 2),
        "status": "ok",
    }
    print(json.dumps(summary))


if __name__ == "__main__":
    main()
