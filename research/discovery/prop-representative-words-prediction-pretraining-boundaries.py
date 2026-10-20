#!/usr/bin/env python3
"""Constructed boundary verification script for Round 764:
PROP (Pre-training with Representative Words Prediction for Ad-hoc Retrieval)
by Xinyu Ma, Jiafeng Guo, Ruqing Zhang, Yixing Fan, Xiang Ji, and Xueqi Cheng
(WSDM 2021, arXiv:2010.10137, doi:10.1145/3437963.3441777).

Verifies:
1. Multinomial unigram document language model with Dirichlet prior smoothing (Eq. 3):
     P(w | D) = (c(w, D) + mu * P(w | C)) / (|D| + mu),
   which forms a valid probability distribution over vocabulary V (sum_{w in V} P(w | D) = 1)
   and assigns non-zero probability to unseen collection words (c(w, D) = 0).
2. Query likelihood score of a sampled word set S of length l (Eq. 2 & Algorithm 1):
     P(S | theta_D) = prod_{i=1}^l P(w_i | D) = prod_{w in V} P(w | D)^{c(w, S)}.
3. Representative Words Prediction (ROP) pairwise margin hinge loss (Eq. 5):
     L_ROP = max(0, 1 - s(S^+ | D) + s(S^- | D)),
   where S^+ is the sampled word set with higher query likelihood P(S^+ | theta_D) > P(S^- | theta_D).
"""

import math


def dirichlet_doc_lm(doc_counts, coll_probs, mu):
    """Computes Eq. (3): P(w | D) = (c(w, D) + mu * P(w | C)) / (|D| + mu)."""
    doc_len = sum(doc_counts.values())
    probs = {}
    for w, p_c in coll_probs.items():
        c_wd = doc_counts.get(w, 0)
        probs[w] = (c_wd + mu * p_c) / (doc_len + mu)
    return probs


def log_query_likelihood(word_set, doc_lm):
    """Computes log P(S | theta_D) = sum_{w in S} log P(w | D) (Eq. 2)."""
    return sum(math.log(doc_lm[w]) for w in word_set)


def rop_hinge_loss(score_pos, score_neg):
    """Computes Eq. (5): L_ROP = max(0, 1 - P(S_1 | D) + s(S_2 | D))."""
    return max(0.0, 1.0 - score_pos + score_neg)


def main():
    # Vocabulary of 5 terms with collection probabilities P(w | C) summing to 1.0
    coll_probs = {
        "retrieval": 0.05,
        "dirichlet": 0.02,
        "language": 0.08,
        "model": 0.15,
        "unrelated": 0.70,
    }
    assert abs(sum(coll_probs.values()) - 1.0) < 1e-12

    # Document D has topical occurrences of "retrieval", "dirichlet", "language", "model",
    # and zero occurrences of "unrelated"
    doc_counts = {"retrieval": 12, "dirichlet": 9, "language": 8, "model": 1}
    mu = 2.0

    doc_lm = dirichlet_doc_lm(doc_counts, coll_probs, mu=mu)

    # 1. Verify valid probability distribution and positive smoothing for unseen words
    assert abs(sum(doc_lm.values()) - 1.0) < 1e-12
    assert doc_lm["unrelated"] > 0.0

    # 2. Verify paired word sets of equal length l = 3 (Algorithm 1):
    # S_1 contains topical document terms; S_2 contains less frequent/background terms
    s1 = ["retrieval", "dirichlet", "language"]
    s2 = ["model", "unrelated", "language"]
    assert len(s1) == len(s2) == 3

    ll_s1 = log_query_likelihood(s1, doc_lm)
    ll_s2 = log_query_likelihood(s2, doc_lm)
    assert ll_s1 > ll_s2  # S_1 is deemed S^+ (more representative of D)

    # 3. Verify ROP pairwise hinge loss (Eq. 5) before and after preference learning
    loss_init = rop_hinge_loss(score_pos=0.3, score_neg=0.6)
    loss_trained = rop_hinge_loss(score_pos=1.5, score_neg=0.2)
    assert abs(loss_init - 1.3) < 1e-12
    assert loss_trained == 0.0

    print(
        f"[PASS] PROP representative words prediction boundaries verified: "
        f"log P(S_1|D)={ll_s1:.4f} > log P(S_2|D)={ll_s2:.4f}, "
        f"L_ROP(init)={loss_init:.4f} -> L_ROP(trained)={loss_trained:.4f}"
    )


if __name__ == "__main__":
    main()
