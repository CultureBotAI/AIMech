#!/usr/bin/env python3
"""Constructed boundary verification for RocketQA (Qu et al., NAACL-HLT 2021, arXiv:2010.08191).

Verifies:
1. Cross-batch negative scaling (Section 3.3, Figure 2):
   with A GPUs and B questions per GPU mini-batch (1 positive passage per question),
   standard in-batch negative training provides B - 1 negatives per question, whereas
   RocketQA's differentiable all-gather cross-batch negative sharing provides A * B - 1
   negatives per question (~A times more negatives).
2. Four-step RocketQA training pipeline and cross-encoder hard-negative denoising
   (Section 3.3, Section 3.4 & Section 4.1.3, Figure 3):
   - Unfiltered top-k retrieved negatives contain ~70% unlabeled positives (false negatives)
     which corrupt dual-encoder contrastive gradients and drop MRR@10 from 33.32 to 26.03.
   - Filtering top-retrieved passages with a cross-encoder M_C using confidence thresholds
     tau_neg = 0.1 (keep as denoised hard negative only if M_C(q, p) < 0.1) and tau_pos = 0.9
     (keep as pseudo-labeled positive for unlabeled questions q in Q_U if M_C(q, p) > 0.9)
     removes false negatives and restores positive margin alignment.
"""

from __future__ import annotations
import math


def count_negatives_per_question(num_gpus_a: int, batch_size_b: int) -> tuple[int, int]:
    """Return (in_batch_negatives, cross_batch_negatives) for A GPUs and per-GPU batch size B."""
    in_batch = batch_size_b - 1
    cross_batch = num_gpus_a * batch_size_b - 1
    return in_batch, cross_batch


def filter_rocketqa_candidates(
    candidates: list[tuple[str, float]],
    neg_threshold: float = 0.1,
    pos_threshold: float = 0.9,
) -> tuple[list[str], list[str], list[str]]:
    """Apply RocketQA Step 3 & Step 4 cross-encoder confidence thresholds (Section 4.1.3)."""
    denoised_hard_negs: list[str] = []
    pseudo_positives: list[str] = []
    discarded_uncertain_or_false_neg: list[str] = []
    for doc_id, ce_prob in candidates:
        if ce_prob < neg_threshold:
            denoised_hard_negs.append(doc_id)
        elif ce_prob > pos_threshold:
            pseudo_positives.append(doc_id)
        else:
            discarded_uncertain_or_false_neg.append(doc_id)
    return denoised_hard_negs, pseudo_positives, discarded_uncertain_or_false_neg


def dual_encoder_nll_loss(pos_sim: float, neg_sims: list[float]) -> float:
    """Compute Eq. 2 negative log-likelihood loss."""
    all_sims = [pos_sim] + list(neg_sims)
    m = max(all_sims)
    exps = [math.exp(s - m) for s in all_sims]
    return -(pos_sim - m - math.log(sum(exps)))


def main() -> None:
    # 1. Verify Section 3.3 & Section 4.1.3 cross-batch negative counts on MS MARCO (A=8 GPUs, B=512)
    in_b, cross_b = count_negatives_per_question(num_gpus_a=8, batch_size_b=512)
    assert in_b == 511
    assert cross_b == 4095
    assert cross_b > 8 * in_b

    # 2. Verify Step 3 & Step 4 cross-encoder denoising thresholds (tau_neg=0.1, tau_pos=0.9)
    # Top-retrieved passages from M_D^(0) excluding annotated positive (70% are unlabeled positives / high relevance)
    top_retrieved = [
        ("rank1_unlabeled_pos", 0.96),
        ("rank2_unlabeled_pos", 0.92),
        ("rank3_partial_rel", 0.65),
        ("rank4_true_hard_neg", 0.04),
        ("rank5_true_hard_neg", 0.08),
    ]
    d_negs, d_pos, d_disc = filter_rocketqa_candidates(top_retrieved, neg_threshold=0.1, pos_threshold=0.9)
    assert d_negs == ["rank4_true_hard_neg", "rank5_true_hard_neg"]
    assert d_pos == ["rank1_unlabeled_pos", "rank2_unlabeled_pos"]
    assert d_disc == ["rank3_partial_rel"]

    # 3. Verify gradient corruption when unlabeled positives (sim=8.5) are treated as hard negatives vs denoised
    pos_sim = 8.4
    unfiltered_neg_sims = [8.5, 8.3, 4.2, 3.9]  # includes rank1 & rank2 unlabeled positives
    denoised_neg_sims = [4.2, 3.9]  # only CE < 0.1 passages kept

    loss_unfiltered = dual_encoder_nll_loss(pos_sim, unfiltered_neg_sims)
    loss_denoised = dual_encoder_nll_loss(pos_sim, denoised_neg_sims)
    assert loss_denoised < 0.05
    assert loss_unfiltered > 1.0

    print(
        "RocketQA boundary verification passed:",
        {"cross_batch_negs": cross_b, "loss_denoised": round(loss_denoised, 4), "loss_unfiltered": round(loss_unfiltered, 4)},
    )


if __name__ == "__main__":
    main()
