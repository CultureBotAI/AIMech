#!/usr/bin/env python3
"""Constructed boundary verification for AdaBERT (Chen et al., IJCAI 2020, arXiv:2001.04246)."""

import math


def proportional_layer_index(student_layer_i, total_teacher_layers_j, student_layers_k):
    """Compute proportional teacher probe layer j = ceil(i * J / K) (Section 2.3)."""
    return math.ceil(student_layer_i * total_teacher_layers_j / student_layers_k)


def attentive_hierarchical_weights(teacher_probe_true_class_probs):
    """Compute Attentive Hierarchical Transfer weights w_{i,m} = exp(log P_j^T) / sum_{i'} exp(log P_{j'}^T) (Eq. 4)."""
    # Note: y_m is one-hot ground-truth label, so y_m * log P_j^T(C_{j,m}^S) = log p_{j, true}
    exps = [math.exp(math.log(max(p, 1e-12))) for p in teacher_probe_true_class_probs]
    denom = sum(exps)
    return [e / denom for e in exps]


def efficiency_aware_loss(num_layers_k, k_max, op_sizes, op_flops):
    """Compute L_E = (K / K_max) * sum_{o_{i,j} in alpha_c} (SIZE(o_{i,j}) + FLOPs(o_{i,j})) (Eq. 5)."""
    assert len(op_sizes) == len(op_flops)
    return (num_layers_k / k_max) * sum(s + f for s, f in zip(op_sizes, op_flops))


def gumbel_softmax_sample(theta_probs, gumbel_noise, tau):
    """Compute continuous Gumbel-Softmax proxy y_i = exp((log(theta_i) + g_i)/tau) / sum_j exp((log(theta_j) + g_j)/tau) (Eq. 6)."""
    logits = [(math.log(max(th, 1e-12)) + g) / tau for th, g in zip(theta_probs, gumbel_noise)]
    m = max(logits)
    exps = [math.exp(l - m) for l in logits]
    denom = sum(exps)
    y_soft = [e / denom for e in exps]
    argmax_idx = max(range(len(y_soft)), key=lambda idx: y_soft[idx])
    y_hard = [1.0 if idx == argmax_idx else 0.0 for idx in range(len(y_soft))]
    return y_soft, y_hard


def main():
    # Verify proportional layer mapping j = ceil(i * J / K) for J=12 BERT-base layers and K=4 student layers
    mapped = [proportional_layer_index(i, 12, 4) for i in range(1, 5)]
    assert mapped == [3, 6, 9, 12]

    # Verify Eq. 4 attentive weights assign higher weight to teacher probes with lower cross-entropy loss (higher true-class prob)
    probe_probs = [0.55, 0.72, 0.88, 0.95]
    w_im = attentive_hierarchical_weights(probe_probs)
    assert abs(sum(w_im) - 1.0) < 1e-12
    assert w_im[0] < w_im[1] < w_im[2] < w_im[3]

    # Verify Eq. 5 efficiency-aware loss scales linearly with searched depth K and operation footprint
    l_e_shallow = efficiency_aware_loss(3, 8, [0.1, 0.2, 0.0], [0.15, 0.25, 0.0])
    l_e_deep = efficiency_aware_loss(7, 8, [0.3, 0.4, 0.2], [0.35, 0.45, 0.25])
    assert 0.0 < l_e_shallow < l_e_deep

    # Verify Eq. 6 Gumbel-Softmax approaches one-hot argmax as temperature tau -> 0
    theta = [0.1, 0.7, 0.2]
    g_noise = [0.05, 0.12, -0.03]
    y_soft_hi, y_hard_hi = gumbel_softmax_sample(theta, g_noise, tau=2.0)
    y_soft_lo, y_hard_lo = gumbel_softmax_sample(theta, g_noise, tau=0.05)
    assert y_hard_hi == [0.0, 1.0, 0.0] and y_hard_lo == [0.0, 1.0, 0.0]
    assert y_soft_lo[1] > 0.999 and y_soft_hi[1] < 0.80

    print(
        f"AdaBERT verification passed: mapped={mapped}, w_im={[round(x, 3) for x in w_im]}, "
        f"l_e_shallow={l_e_shallow:.4f} < l_e_deep={l_e_deep:.4f}, y_soft_lo[1]={y_soft_lo[1]:.6f}"
    )


if __name__ == "__main__":
    main()
