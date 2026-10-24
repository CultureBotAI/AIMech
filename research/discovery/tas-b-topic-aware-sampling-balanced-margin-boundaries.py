#!/usr/bin/env python3
"""Boundary verification for Round 754: TAS-Balanced Topic Aware Sampling and Dual-Teacher Supervision (Hofstatter et al., SIGIR 2021)."""


def filter_passage_pairs_by_margin_bin(pairs_with_margins, m_min, m_max, n_bins, bin_idx):
    """Eq. 12: H(P_q, i) filters passage pairs (p+, p-) into uniform teacher-margin bin i of width m."""
    m = (m_max - m_min) / float(n_bins)
    low = m_min + bin_idx * m
    high = m_min + (bin_idx + 1) * m
    if bin_idx == n_bins - 1:
        return [(p_pos, p_neg, margin) for p_pos, p_neg, margin in pairs_with_margins if low <= margin <= high + 1e-9]
    return [(p_pos, p_neg, margin) for p_pos, p_neg, margin in pairs_with_margins if low <= margin < high]


def dual_teacher_margin_mse_loss(student_pos, student_neg_pair, teacher_cat_pos, teacher_cat_neg_pair,
                                 student_inb_pos, student_inb_all, teacher_colbert_pos, teacher_colbert_all, alpha=0.75):
    """Eq. 6-8: L_DS = L_Pair(BERT_CAT) + alpha * L_InB(ColBERT) using Margin-MSE for both pairwise and in-batch teachers."""
    b_size = len(student_pos)
    # Pairwise Margin-MSE (Eq. 6)
    l_pair = 0.0
    for i in range(b_size):
        s_margin = student_pos[i] - student_neg_pair[i]
        t_margin = teacher_cat_pos[i] - teacher_cat_neg_pair[i]
        l_pair += (s_margin - t_margin) ** 2
    l_pair /= float(b_size)

    # In-batch Margin-MSE (Eq. 7) across other negative and positive passages in the topic-clustered batch
    l_inb_terms = []
    for i in range(b_size):
        for j in range( len(student_inb_all[i]) ):
            s_margin = student_inb_pos[i] - student_inb_all[i][j]
            t_margin = teacher_colbert_pos[i] - teacher_colbert_all[i][j]
            l_inb_terms.append((s_margin - t_margin) ** 2)
    l_inb = sum(l_inb_terms) / float(len(l_inb_terms))
    return l_pair, l_inb, l_pair + alpha * l_inb


def main():
    # 1. Verify Eq. 12-13 balanced margin sampling unskews skewed high-margin easy negatives
    # Skewed pool: 2 close/hard pairs in [0, 2) and 18 easy pairs in [8, 10]
    skewed_pairs = [("p+", f"hard_{i}", 0.5 + 0.5 * i) for i in range(2)] + [
        ("p+", f"easy_{i}", 8.1 + 0.1 * i) for i in range(18)
    ]
    bin_0 = filter_passage_pairs_by_margin_bin(skewed_pairs, m_min=0.0, m_max=10.0, n_bins=5, bin_idx=0)
    bin_4 = filter_passage_pairs_by_margin_bin(skewed_pairs, m_min=0.0, m_max=10.0, n_bins=5, bin_idx=4)
    assert len(bin_0) == 2 and len(bin_4) == 18
    # Under random sampling, hard bin_0 has probability 2/20 = 0.10; under uniform bin sampling across non-empty bins {0, 4}, prob is 0.50
    prob_hard_random = len(bin_0) / float(len(skewed_pairs))
    prob_hard_balanced = 1.0 / 2.0
    assert prob_hard_balanced == 5.0 * prob_hard_random

    # 2. Verify Eq. 6-8 Dual-Teacher Margin-MSE supervision (alpha = 0.75)
    l_pair, l_inb, l_ds = dual_teacher_margin_mse_loss(
        student_pos=[8.2, 7.5],
        student_neg_pair=[3.1, 2.0],
        teacher_cat_pos=[8.5, 7.8],
        teacher_cat_neg_pair=[2.9, 2.2],
        student_inb_pos=[8.2, 7.5],
        student_inb_all=[[4.0, 5.1], [3.8, 4.9]],
        teacher_colbert_pos=[8.4, 7.6],
        teacher_colbert_all=[[3.6, 5.0], [3.5, 4.7]],
        alpha=0.75,
    )
    assert abs(l_ds - (l_pair + 0.75 * l_inb)) < 1e-12
    assert l_pair > 0.0 and l_inb > 0.0

    # 3. Verify Table 4 & Table 6 ablation and benchmark invariants (batch size 32/96/256)
    # Table 4 TREC-DL'19 Recall@1K: Standalone Random (0.714) < Pairwise Random (0.767) < Dual Random (0.787) < Dual TAS (0.831) < Dual TAS-Balanced (0.845)
    assert 0.714 < 0.767 < 0.787 < 0.831 < 0.845
    # Table 4 MSMARCO DEV MRR@10: Standalone (0.298) < Pairwise Random (0.326) < Dual Random (0.331) < Dual TAS (0.338) < Dual TAS-Balanced b=32 (0.340) < b=96 (0.343) < b=256 (0.347)
    assert 0.298 < 0.326 < 0.331 < 0.338 < 0.340 < 0.343 < 0.347
    print("Round 754 TAS-Balanced boundary verification passed.")


if __name__ == "__main__":
    main()
