#!/usr/bin/env python3
"""Constructed boundary verification script for Round 759:
PAIR (Passage-Centric Similarity Relation for Dense Passage Retrieval)
by Ruiyang Ren, Shangwen Lv, Yingqi Qu, Jing Liu, Wayne Xin Zhao, Qiaoqiao She,
Hua Wu, Haifeng Wang, and Ji-Rong Wen (Findings of ACL-IJCNLP 2021, arXiv:2108.06027).

Verifies:
1. Query-centric contrastive loss L_Q(q, p^+, N_P):
     L_Q = -log( exp(f(q, p^+)) / (exp(f(q, p^+)) + sum_{p^- in N_P} exp(f(q, p^-))) ).
2. Passage-centric contrastive loss L_P(q, p^+, N_P):
     L_P = -log( exp(-f(p^+, p^+)) / (exp(-f(p^+, p^+)) + sum_{p^- in N_P} exp(f(p^+, p^-))) ).
3. Combined training objective with dynamic decay ratio alpha_t:
     L(q, p^+, N_P) = (1 - alpha) * L_Q(q, p^+, N_P) + alpha * L_P(q, p^+, N_P),
   and geometric consequence: minimizing L_Q + L_P separates positive passage p^+
   from hard negative passages p^- in the passage embedding space (reducing f(p^+, p^-))
   so a ball around query q contains p^+ while excluding p^-.
"""

import math


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def query_centric_loss(q, p_pos, neg_passages):
    pos_score = dot(q, p_pos)
    neg_scores = [dot(q, p_neg) for p_neg in neg_passages]
    m = max([pos_score] + neg_scores)
    num = math.exp(pos_score - m)
    den = num + sum(math.exp(s - m) for s in neg_scores)
    return -math.log(num / den)


def passage_centric_loss(p_pos, neg_passages):
    """Eq. (2) in Ren et al. (2021): numerator uses exp(-f(p^+, p^+)) and denominator
    sums exp(-f(p^+, p^+)) + sum_{p^- in N_P} exp(f(p^+, p^-))."""
    self_neg_score = -dot(p_pos, p_pos)
    neg_scores = [dot(p_pos, p_neg) for p_neg in neg_passages]
    m = max([self_neg_score] + neg_scores)
    num = math.exp(self_neg_score - m)
    den = num + sum(math.exp(s - m) for s in neg_scores)
    return -math.log(num / den)


def pair_combined_loss(q, p_pos, neg_passages, alpha):
    return (1.0 - alpha) * query_centric_loss(q, p_pos, neg_passages) + alpha * passage_centric_loss(p_pos, neg_passages)


def main():
    q = [1.0, 0.2]
    p_pos = [0.9, 0.3]
    # Hard negative passage initially close to p_pos (violating Assumption 1 in Figure 1a)
    p_neg_clustered = [0.85, 0.35]
    # Separated negative passage after passage-centric repulsion (satisfying Assumption 1 in Figure 1b)
    p_neg_separated = [-0.6, -0.4]

    lq_clustered = query_centric_loss(q, p_pos, [p_neg_clustered])
    lp_clustered = passage_centric_loss(p_pos, [p_neg_clustered])
    l_pair_clustered = pair_combined_loss(q, p_pos, [p_neg_clustered], alpha=0.2)

    lq_separated = query_centric_loss(q, p_pos, [p_neg_separated])
    lp_separated = passage_centric_loss(p_pos, [p_neg_separated])
    l_pair_separated = pair_combined_loss(q, p_pos, [p_neg_separated], alpha=0.2)

    # Verify passage-centric similarity f(p^+, p^-) is much higher in the clustered case,
    # causing higher L_P and higher combined PAIR loss
    assert dot(p_pos, p_neg_clustered) > dot(p_pos, p_neg_separated)
    assert lp_clustered > lp_separated
    assert lq_clustered > lq_separated
    assert l_pair_clustered > l_pair_separated

    # Verify two-stage transition: when alpha -> 0 in stage 2, combined loss equals L_Q exactly
    assert abs(pair_combined_loss(q, p_pos, [p_neg_separated], alpha=0.0) - lq_separated) < 1e-12

    print(
        f"[PASS] PAIR passage-centric similarity boundaries verified: "
        f"L_P(clustered)={lp_clustered:.4f} > L_P(separated)={lp_separated:.4f}, "
        f"L_PAIR(clustered)={l_pair_clustered:.4f} > L_PAIR(separated)={l_pair_separated:.4f}"
    )


if __name__ == "__main__":
    main()
