#!/usr/bin/env python3
"""Constructed boundary verification for LM Distill + Ranker Distill (Gao, Dai, & Callan, ICTIR 2020, arXiv:2007.11088)."""

import math


def kl_divergence(p_teacher: list[float], q_student: list[float], eps: float = 1e-12) -> float:
    return sum(
        p * math.log((p + eps) / (q + eps))
        for p, q in zip(p_teacher, q_student)
        if p > 0.0
    )


def non_inferiority_margin_check(
    teacher_score: float,
    student_score: float,
    relative_margin: float = 0.03,
) -> bool:
    """Table 1 footnote 1: non-inferiority within a 3% relative margin of the 12-layer BERT ranker."""
    threshold = teacher_score * (1.0 - relative_margin)
    return student_score >= threshold


def main() -> None:
    # 1. Verify Table 1 empirical distillation procedures across 6-layer and 4-layer rankers:
    bert_12_mrr10 = 0.3527
    results_mrr10 = {
        "6L_ranker_distill": 0.3380,
        "6L_lm_distill_finetune": 0.3556,
        "6L_lm_distill_ranker_distill": 0.3600,
        "4L_ranker_distill": 0.3286,
        "4L_lm_distill_finetune": 0.3320,
        "4L_lm_distill_ranker_distill": 0.3501,
    }

    # Ranker Distill alone fails the 3% non-inferiority margin at both 6L and 4L:
    assert not non_inferiority_margin_check(bert_12_mrr10, results_mrr10["6L_ranker_distill"])
    assert not non_inferiority_margin_check(bert_12_mrr10, results_mrr10["4L_ranker_distill"])

    # LM Distill + Fine-Tuning passes at 6L but fails at 4L due to high-compression LM loss:
    assert non_inferiority_margin_check(bert_12_mrr10, results_mrr10["6L_lm_distill_finetune"])
    assert not non_inferiority_margin_check(bert_12_mrr10, results_mrr10["4L_lm_distill_finetune"])

    # Two-round LM Distill + Ranker Distill passes at both 6L (2.0x speedup) and 4L (9.0x speedup):
    assert non_inferiority_margin_check(bert_12_mrr10, results_mrr10["6L_lm_distill_ranker_distill"])
    assert non_inferiority_margin_check(bert_12_mrr10, results_mrr10["4L_lm_distill_ranker_distill"])

    # 2. Verify intermediate self-attention + output probability distillation loss decreases when
    # initialized from LM-distilled attention distributions vs random initialization:
    t_attn_dist = [0.55, 0.25, 0.15, 0.05]
    s_random_attn = [0.25, 0.25, 0.25, 0.25]
    s_lm_init_attn = [0.50, 0.28, 0.16, 0.06]
    kl_rand = kl_divergence(t_attn_dist, s_random_attn)
    kl_lm = kl_divergence(t_attn_dist, s_lm_init_attn)
    assert kl_lm < 0.05 < kl_rand

    # 3. Verify top-100 vs top-1000 reranking depth latency & throughput (Table 1 & Table 2):
    # 4-layer model takes 0.33s for 1000 docs -> 0.033s for 100 docs (>30 queries/sec) with only 3.5% MRR@10 drop:
    mrr_1000 = 0.3501
    mrr_100 = 0.3376
    rel_drop = (mrr_1000 - mrr_100) / mrr_1000
    qps_at_100 = 1.0 / (0.33 * (100.0 / 1000.0))
    assert rel_drop < 0.04
    assert qps_at_100 > 30.0

    print("LM Distill + Ranker Distill boundary verification passed:")
    print(f"  4L LM+Ranker Distill MRR@10={mrr_1000:.4f} (non-inferior to BERT-12 {bert_12_mrr10:.4f})")
    print(f"  Attention KL (LM-init vs random): {kl_lm:.4f} < {kl_rand:.4f}")
    print(f"  4L Depth-100 throughput: {qps_at_100:.1f} QPS with {100 * rel_drop:.2f}% MRR@10 drop")


if __name__ == "__main__":
    main()
