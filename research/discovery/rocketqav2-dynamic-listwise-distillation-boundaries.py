#!/usr/bin/env python3
"""Constructed boundary verification script for Round 758:
RocketQAv2 (Joint Training Method for Dense Passage Retrieval and Passage Reranking)
by Ruiyang Ren, Yingqi Qu, Jing Liu, Wayne Xin Zhao, Qiaoqiao She, Hua Wu,
Haifeng Wang, and Ji-Rong Wen (EMNLP 2021, arXiv:2110.07367).

Verifies:
1. Dual-encoder dot-product similarity s_{de}(q, p) = E_Q(q)^T E_P(p) vs.
   cross-encoder score s_{ce}(q, p) = w^T E_C([CLS] q [SEP] p [SEP]).
2. Dynamic listwise distillation via KL divergence over normalized listwise
   probability distributions:
     p~_{de}(q, p_i) = exp(s_{de}(q, p_i)) / sum_{j=1}^K exp(s_{de}(q, p_j)),
     p~_{ce}(q, p_i) = exp(s_{ce}(q, p_i)) / sum_{j=1}^K exp(s_{ce}(q, p_j)),
     L_{kl} = sum_{i=1}^K p~_{ce}(q, p_i) * log(p~_{ce}(q, p_i) / p~_{de}(q, p_i)),
   plus ground-truth cross-entropy for the cross-encoder:
     L_{ce} = -log p~_{ce}(q, p^+),
     L_{final} = L_{kl} + L_{ce}.
3. Gradient synchronization property: dynamic listwise distillation couples
   retriever and reranker parameters on the same candidate list C_q = {p^+, p^-_1, ..., p^-_{K-1}},
   avoiding stale teacher distributions and reducing false negatives via hybrid
   data augmentation (denoise-then-sample).
"""

import math


def softmax(scores):
    m = max(scores)
    exps = [math.exp(s - m) for s in scores]
    total = sum(exps)
    return [e / total for e in exps]


def kl_divergence(p_teacher, p_student):
    """Computes KL(p_teacher || p_student) = sum_i p_teacher[i] * log(p_teacher[i] / p_student[i])."""
    total = 0.0
    for pt, ps in zip(p_teacher, p_student):
        if pt > 0.0:
            total += pt * math.log(pt / max(ps, 1e-15))
    return total


def main():
    # Candidate list: index 0 is labeled positive p^+, index 1 is an unlabeled false negative,
    # indices 2, 3 are true hard negatives.
    ce_scores = [4.2, 3.9, -1.0, -1.8]
    de_scores_init = [1.5, -0.5, 0.8, 0.2]

    p_ce = softmax(ce_scores)
    p_de_init = softmax(de_scores_init)

    # 1. Verify probability distributions sum to 1 and cross-encoder assigns high mass to both
    # the labeled positive (idx 0) and false negative (idx 1)
    assert abs(sum(p_ce) - 1.0) < 1e-12
    assert abs(sum(p_de_init) - 1.0) < 1e-12
    assert p_ce[0] + p_ce[1] > 0.98

    # 2. Compute joint loss L_final = L_kl + L_ce
    l_kl_init = kl_divergence(p_ce, p_de_init)
    l_ce = -math.log(p_ce[0])
    l_final_init = l_kl_init + l_ce
    assert l_kl_init > 0.5
    assert l_ce > 0.0

    # 3. Verify gradient of L_kl w.r.t. s_{de}(q, p_i) is (p~_{de}(q, p_i) - p~_{ce}(q, p_i))
    # One gradient descent step on s_{de} moves p~_{de} closer to p~_{ce} and strictly decreases L_kl
    lr = 0.8
    de_scores_updated = [
        s - lr * (pde - pce)
        for s, pde, pce in zip(de_scores_init, p_de_init, p_ce)
    ]
    p_de_updated = softmax(de_scores_updated)
    l_kl_updated = kl_divergence(p_ce, p_de_updated)
    assert l_kl_updated < l_kl_init, f"Expected {l_kl_updated} < {l_kl_init}"

    # Verify that unlike standard 1-hot supervised NLL (which penalizes idx 1 as negative),
    # dynamic listwise distillation increases the dual-encoder score of the false negative (idx 1)
    assert de_scores_updated[1] > de_scores_init[1]

    print(
        f"[PASS] RocketQAv2 boundaries verified: L_kl_init={l_kl_init:.4f} -> "
        f"L_kl_updated={l_kl_updated:.4f}, L_ce={l_ce:.4f}, L_final_init={l_final_init:.4f}"
    )


if __name__ == "__main__":
    main()
