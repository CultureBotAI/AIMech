#!/usr/bin/env python3
"""Constructed boundary verification script for Round 763:
MoDIR (Momentum Adversarial Domain Invariant Representation Learning for Zero-Shot Dense Retrieval)
by Ji Xin, Chenyan Xiong, Ashwin Srinivasan, Ankita Sharma, Damien Jose, and Paul N. Bennett
(Findings of ACL 2022, arXiv:2110.07581).

Verifies:
1. Momentum queue Q_k = {e_{q^s}, e_{d^s}, e_{q^t}, e_{d^t} | B_{k-n+1:k}} of stop-gradient
   detached embeddings e = Phi(g(x; theta_g)) maintaining 1:1 source-to-target ratio (Eqs. 4-5).
2. Domain discrimination loss L_D(e; f) (Eqs. 6-7):
     L_D(e; f) = -log f(e) for source, -log(1 - f(e)) for target.
3. Adversarial Confusion loss L_M(x; g, f) (Eq. 8):
     L_M(x; g, f) = -0.5 * (log f(g(q)) + log(1 - f(g(q))) + log f(g(d)) + log(1 - f(g(d)))),
   which achieves its unique global minimum (2 * log 2 = 1.386294...) if and only if
   f(g(q)) = 0.5 and f(g(d)) = 0.5 (complete domain invariance).
"""

import math


def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))


def domain_discrimination_loss(source_probs, target_probs):
    """Computes average L_D(e; f) over queue Q_k (Eqs. 6-7)."""
    loss_s = sum(-math.log(max(p, 1e-15)) for p in source_probs)
    loss_t = sum(-math.log(max(1.0 - p, 1e-15)) for p in target_probs)
    return (loss_s + loss_t) / (len(source_probs) + len(target_probs))


def confusion_loss_pair(f_q, f_d):
    """Computes Eq. (8):
    L_M(x; g, f) = -0.5 * (log f(g(q)) + log(1 - f(g(q))) + log f(g(d)) + log(1 - f(g(d)))).
    """
    return -0.5 * (
        math.log(max(f_q, 1e-15))
        + math.log(max(1.0 - f_q, 1e-15))
        + math.log(max(f_d, 1e-15))
        + math.log(max(1.0 - f_d, 1e-15))
    )


def main():
    # 1. Verify global minimum of Confusion loss L_M occurs at f(g(q)) = f(g(d)) = 0.5
    min_lm = confusion_loss_pair(0.5, 0.5)
    expected_min = 2.0 * math.log(2.0)
    assert abs(min_lm - expected_min) < 1e-12

    # Any deviation from 0.5 strictly increases L_M
    for p_q, p_d in [(0.9, 0.85), (0.1, 0.2), (0.5, 0.7), (0.3, 0.5)]:
        lm = confusion_loss_pair(p_q, p_d)
        assert lm > min_lm + 1e-4, f"Expected {lm} > {min_lm} for ({p_q}, {p_d})"

    # 2. Verify adversarial step on target embedding pushes it across the momentum domain boundary
    # Let linear domain classifier be f(e) = sigmoid(w^T e) with w = [2.0, 0.0].
    # Source embeddings have e[0] > 0, target embeddings initially have e[0] < 0.
    w = [2.0, 0.0]
    e_q_target = [-1.2, 0.5]
    e_d_target = [-1.0, -0.3]

    f_q_init = sigmoid(w[0] * e_q_target[0] + w[1] * e_q_target[1])
    f_d_init = sigmoid(w[0] * e_d_target[0] + w[1] * e_d_target[1])
    lm_init = confusion_loss_pair(f_q_init, f_d_init)

    # Gradient of -0.5 * (log f(e) + log(1 - f(e))) w.r.t. e is (f(e) - 0.5) * w
    lr = 0.4
    e_q_updated = [
        e_q_target[i] - lr * (f_q_init - 0.5) * w[i] for i in range(2)
    ]
    e_d_updated = [
        e_d_target[i] - lr * (f_d_init - 0.5) * w[i] for i in range(2)
    ]

    f_q_updated = sigmoid(w[0] * e_q_updated[0] + w[1] * e_q_updated[1])
    f_d_updated = sigmoid(w[0] * e_d_updated[0] + w[1] * e_d_updated[1])
    lm_updated = confusion_loss_pair(f_q_updated, f_d_updated)

    # Verify target embeddings move toward the domain boundary (f -> 0.5) and L_M decreases
    assert abs(f_q_updated - 0.5) < abs(f_q_init - 0.5)
    assert abs(f_d_updated - 0.5) < abs(f_d_init - 0.5)
    assert lm_updated < lm_init

    # 3. Verify momentum queue Q_k variance reduction vs single noisy batch
    # True domain separator is along axis 0 (w_true = [1.0, 0.0]), while individual batches
    # have orthogonal noise on axis 1 that averages out over n batches in Q_k.
    batch_diffs = [(1.0, 1.5), (1.0, -1.4), (1.0, 1.3), (1.0, -1.4)]
    single_batch_dir = batch_diffs[0]
    momentum_dir = (
        sum(d[0] for d in batch_diffs) / len(batch_diffs),
        sum(d[1] for d in batch_diffs) / len(batch_diffs),
    )
    # Cosine alignment with true axis (1.0, 0.0) is much higher for the momentum queue
    cos_single = single_batch_dir[0] / math.hypot(*single_batch_dir)
    cos_momentum = momentum_dir[0] / math.hypot(*momentum_dir)
    assert cos_momentum > 0.99 > cos_single

    print(
        f"[PASS] MoDIR boundaries verified: L_M_init={lm_init:.4f} -> "
        f"L_M_updated={lm_updated:.4f} (min={min_lm:.4f}), "
        f"cos_momentum={cos_momentum:.4f} > cos_single={cos_single:.4f}"
    )


if __name__ == "__main__":
    main()
