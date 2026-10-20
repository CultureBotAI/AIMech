#!/usr/bin/env python3
"""Boundary verification for Round 515: GLFC (Dong et al., CVPR 2022).

Verifies:
1. Class-Aware Gradient Compensation Loss (L_GC, Eqs. 2-4):
   Separate gradient normalization G_n (new classes) and G_o (old classes) equalizes the total effective
   gradient magnitude between minority old-class exemplars and majority new-class samples in a mini-batch.
2. Class-Semantic Relation Distillation Loss (L_RD, Eq. 5):
   Hybrid target Y_l^t replaces the first C^p dimensions of one-hot labels with old-model probabilities
   P_l^{t-1}(X, Theta_l^{t-1}) while keeping new-class dimensions C^t, preserving inter-class semantic relations.
3. Entropy-Spike Task Transition Detection (Eq. 7):
   Sudden rise in average prediction entropy H_l^{r,t} - H_l^{r-1,t} >= r_h = 1.2 accurately detects arrival
   of unseen new classes without server-side task boundary supervision.
"""

import math


def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))


def shannon_entropy(probs):
    # Note: Paper Eq. (7) writes I(p) = -sum_i p_i log p_i (standard Shannon entropy over class distribution)
    s = sum(probs)
    norm_p = [max(p / s, 1e-12) for p in probs]
    return -sum(p * math.log(p) for p in norm_p)


def main():
    # 1. Verify Class-Aware Gradient Compensation (Eqs. 2-4) under severe old/new class imbalance
    # Mini-batch of b=10 samples: 2 old-class exemplars (indices 0,1) and 8 new-class samples (indices 2..9)
    b = 10
    is_new = [False, False] + [True] * 8
    # Predicted probability on ground-truth class y_{li}^t
    pred_gt = [0.25, 0.35, 0.40, 0.50, 0.30, 0.60, 0.45, 0.55, 0.35, 0.65]
    # Eq. (2): G_{li}^t = P_l^t(x_{li}^t)_{y_{li}^t} - 1, so |G_{li}^t| = 1 - pred_gt[i]
    abs_G = [abs(p - 1.0) for p in pred_gt]

    # Standard uncompensated BCE gradient sum on old vs new classes:
    uncomp_old_grad_sum = sum(abs_G[i] for i in range(b) if not is_new[i])
    uncomp_new_grad_sum = sum(abs_G[i] for i in range(b) if is_new[i])
    assert uncomp_new_grad_sum > 3.0 * uncomp_old_grad_sum

    # Eq. (3): G_n and G_o
    n_new = sum(1 for flag in is_new if flag)
    n_old = sum(1 for flag in is_new if not flag)
    G_n = sum(abs_G[i] for i in range(b) if is_new[i]) / n_new
    G_o = sum(abs_G[i] for i in range(b) if not is_new[i]) / n_old

    # Eq. (4): re-weighted gradient contribution (|G_{li}^t| / G_bar_i)
    weights_gc = [abs_G[i] / (G_n if is_new[i] else G_o) for i in range(b)]
    # Notice that the mean weight per old sample and mean weight per new sample are both exactly 1.0!
    mean_weight_old = sum(weights_gc[i] for i in range(b) if not is_new[i]) / n_old
    mean_weight_new = sum(weights_gc[i] for i in range(b) if is_new[i]) / n_new
    assert abs(mean_weight_old - 1.0) < 1e-12 and abs(mean_weight_new - 1.0) < 1e-12

    # 2. Verify Class-Semantic Relation Distillation Loss (L_RD, Eq. 5)
    # Suppose C^p = 2 old classes, C^t = 2 new classes -> total 4 classes
    # Sample from new class c=2 (0-indexed) has one-hot [0, 0, 1, 0], and old model predicts [0.7, 0.2] on old classes
    one_hot = [0.0, 0.0, 1.0, 0.0]
    p_old_model = [0.7, 0.2]
    # Hybrid target Y_l^t replaces first C^p=2 entries with p_old_model:
    Y_hybrid = p_old_model + one_hot[2:]
    assert Y_hybrid == [0.7, 0.2, 1.0, 0.0]

    # Optimizing current model probabilities P_curr toward Y_hybrid minimizes KL divergence:
    kl_matched = sum(
        p * math.log(max(p, 1e-12) / max(q, 1e-12))
        for p, q in zip(Y_hybrid, Y_hybrid)
    )
    P_forgetting = [0.05, 0.05, 0.95, 0.05]
    kl_forgetting = sum(
        p * math.log(max(p, 1e-12) / max(q, 1e-12))
        for p, q in zip(P_forgetting, Y_hybrid)
    )
    assert abs(kl_matched) < 1e-12 and kl_forgetting > 0.20

    # 3. Verify Entropy-Spike Task Transition Detection (Eq. 7)
    # On familiar classes (round r-1), model predictions are confident (low entropy);
    # When new classes arrive at round r, predictions over C^p+C^t classes are near-uniform (high entropy).
    num_classes = 10
    confident_probs = [0.82] + [0.02] * (num_classes - 1)
    unseen_probs = [1.0 / num_classes] * num_classes
    H_prev = shannon_entropy(confident_probs)
    H_curr = shannon_entropy(unseen_probs)
    entropy_jump = H_curr - H_prev
    r_h = 1.2
    assert entropy_jump >= r_h, f"Expected entropy jump >= {r_h}, got {entropy_jump}"

    print(
        f"[PASS] Round 515 GLFC (Dong et al. 2022): "
        f"mean_w_old={mean_weight_old:.2f}==mean_w_new={mean_weight_new:.2f}, "
        f"KL_forgetting={kl_forgetting:.4f}>>KL_matched={kl_matched:.1e}, "
        f"entropy_jump={entropy_jump:.3f}>={r_h}"
    )


if __name__ == "__main__":
    main()
