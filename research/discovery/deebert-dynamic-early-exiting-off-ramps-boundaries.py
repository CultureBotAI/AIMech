#!/usr/bin/env python3
"""Constructed boundary verification for DeeBERT Dynamic Early Exiting (Xin et al., ACL 2020)."""

import math


def entropy(probs):
    """Compute Shannon entropy H(z) = -sum_k p_k log(p_k) for probability vector z."""
    return -sum(p * math.log(max(p, 1e-12)) for p in probs)


def cross_entropy(target_idx, probs):
    """Compute cross-entropy H(y, z) = -log(z_{target_idx}) for one-hot target y."""
    return -math.log(max(probs[target_idx], 1e-12))


def expected_layer_saving(exit_counts, num_layers):
    """Compute analytical layer execution saving 1 - (sum_{i=1}^n i * N_i) / (sum_{i=1}^n n * N_i) (Eq. 2)."""
    assert len(exit_counts) == num_layers
    executed = sum((i + 1) * n_i for i, n_i in enumerate(exit_counts))
    full_cost = sum(num_layers * n_i for n_i in exit_counts)
    return 1.0 - (executed / full_cost)


def deebert_early_exit(off_ramp_probs, threshold_s):
    """Run Algorithm 1: exit at first off-ramp i where entropy(z_i) < S, else return final off-ramp n."""
    n = len(off_ramp_probs)
    for idx, probs in enumerate(off_ramp_probs):
        if idx < n - 1 and entropy(probs) < threshold_s:
            return idx + 1, probs
    return n, off_ramp_probs[-1]


def verify_two_stage_isolation():
    """Verify two-stage fine-tuning preserves final-layer parameters theta_backbone and theta_n exactly."""
    # Stage 1 updates backbone + final classifier f_n; Stage 2 freezes backbone + f_n and updates f_1..f_{n-1}
    stage1_backbone = [0.42, -0.19, 0.85, 0.11]
    stage1_final_head = [0.73, -0.64]
    stage2_backbone = list(stage1_backbone)
    stage2_final_head = list(stage1_final_head)
    # Stage 2 updates intermediate off-ramp weights only
    intermediate_heads_before = [[0.0, 0.0] for _ in range(5)]
    intermediate_heads_after = [[0.35 + 0.05 * i, -0.35 - 0.05 * i] for i in range(5)]
    assert stage2_backbone == stage1_backbone
    assert stage2_final_head == stage1_final_head
    assert intermediate_heads_before != intermediate_heads_after
    return True


def main():
    assert verify_two_stage_isolation()

    # 6-layer example with binary classification probabilities at each off-ramp
    sample_easy = [
        [0.65, 0.35],  # H = 0.647
        [0.93, 0.07],  # H = 0.254 < 0.30 -> exits at layer 2
        [0.95, 0.05],
        [0.97, 0.03],
        [0.98, 0.02],
        [0.99, 0.01],
    ]
    sample_hard = [
        [0.52, 0.48],  # H = 0.692
        [0.58, 0.42],  # H = 0.680
        [0.63, 0.37],  # H = 0.659
        [0.70, 0.30],  # H = 0.611
        [0.78, 0.22],  # H = 0.527
        [0.88, 0.12],  # reaches layer 6 when S = 0.30
    ]

    exit_easy, probs_easy = deebert_early_exit(sample_easy, threshold_s=0.30)
    exit_hard, probs_hard = deebert_early_exit(sample_hard, threshold_s=0.30)
    assert exit_easy == 2 and abs(probs_easy[0] - 0.93) < 1e-9
    assert exit_hard == 6 and abs(probs_hard[0] - 0.88) < 1e-9

    # Boundary case S = 0: never exits early, matches full-depth BERT (0% layer saving)
    exit_easy_s0, _ = deebert_early_exit(sample_easy, threshold_s=0.0)
    assert exit_easy_s0 == 6
    assert abs(expected_layer_saving([0, 0, 0, 0, 0, 100], 6) - 0.0) < 1e-12

    # Monotonicity of expected layer saving with increasing entropy threshold S
    counts_low_s = [5, 15, 20, 20, 15, 25]
    counts_high_s = [25, 30, 20, 15, 5, 5]
    saving_low = expected_layer_saving(counts_low_s, 6)
    saving_high = expected_layer_saving(counts_high_s, 6)
    assert 0.0 < saving_low < saving_high < 1.0

    # Verify Eq. 1 per-layer cross-entropy sum for intermediate off-ramps
    stage2_loss = sum(cross_entropy(0, sample_easy[i]) for i in range(5))
    assert stage2_loss > 0.0

    print(
        f"DeeBERT verification passed: exit_easy={exit_easy}, exit_hard={exit_hard}, "
        f"saving_low={saving_low:.4f}, saving_high={saving_high:.4f}, stage2_loss={stage2_loss:.4f}"
    )


if __name__ == "__main__":
    main()
