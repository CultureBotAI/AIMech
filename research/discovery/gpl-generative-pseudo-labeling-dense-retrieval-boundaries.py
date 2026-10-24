#!/usr/bin/env python3
"""Constructed boundary verification for GPL (Wang et al., NAACL-HLT 2022, arXiv:2112.07577).

Verifies:
1. Corpus-adaptive query budget (Section 4.1): given corpus size |C|, GPL sets
   effective corpus size |C_eff| = min(|C|, floor(250000 / 3)) and queries per passage
   q_avg = ceil(250000 / |C_eff|) so that q_avg >= 3 and total queries ~ 250K.
2. MarginMSE loss (Section 3, Eq. 1) vs. MultipleNegativesRanking loss (MNRL / QGen):
   - Teacher margin: delta_i = CE(Q_i, P_i^+) - CE(Q_i, P_i^-)
   - Student margin: hat_delta_i = f_theta(Q_i)^T f_theta(P_i^+) - f_theta(Q_i)^T f_theta(P_i^-)
   - Loss: L_MarginMSE = (1/M) sum_{i=0}^{M-1} |hat_delta_i - delta_i|^2
3. Denoising of false negatives and low-quality synthetic queries (Section 3 & Section 7, Table 5):
   when a mined hard negative P_i^- is actually relevant (false negative, CE(Q_i, P_i^-) ~ CE(Q_i, P_i^+))
   or a generated query is unanswerable by P_i^+, delta_i -> 0 so MarginMSE does not force a large
   embedding distance, whereas binary 0-1 QGen (MNRL) penalizes the student for high similarity on P_i^-.
"""

from __future__ import annotations
import math


def compute_gpl_qpp_and_corpus_size(corpus_size: int, target_total: int = 250_000) -> tuple[int, int]:
    """Compute GPL down-sampled corpus size and queries per passage q_avg (Section 4.1)."""
    if 3 * corpus_size > target_total:
        effective_corpus = math.ceil(target_total / 3)
    else:
        effective_corpus = corpus_size
    q_avg = math.ceil(target_total / effective_corpus)
    assert q_avg >= 3
    return effective_corpus, q_avg


def dot(u: list[float], v: list[float]) -> float:
    return sum(x * y for x, y in zip(u, v))


def margin_mse_loss_and_grad_wrt_neg_sim(
    pos_sim: float, neg_sim: float, ce_pos: float, ce_neg: float
) -> tuple[float, float]:
    """Return single-tuple MarginMSE loss |hat_delta - delta|^2 and dL / d(neg_sim)."""
    delta = ce_pos - ce_neg
    hat_delta = pos_sim - neg_sim
    diff = hat_delta - delta
    loss = diff * diff
    # hat_delta = pos_sim - neg_sim => d(hat_delta)/d(neg_sim) = -1
    grad_neg_sim = -2.0 * diff
    return loss, grad_neg_sim


def mnrl_loss_and_grad_wrt_neg_sim(pos_sim: float, neg_sim: float, tau: float = 1.0) -> tuple[float, float]:
    """Return binary 0-1 QGen (MNRL) loss -log(exp(tau*pos) / (exp(tau*pos) + exp(tau*neg))) and dL / d(neg_sim)."""
    a = tau * pos_sim
    b = tau * neg_sim
    m = max(a, b)
    ea = math.exp(a - m)
    eb = math.exp(b - m)
    p_neg = eb / (ea + eb)
    loss = -(a - m - math.log(ea + eb))
    grad_neg_sim = tau * p_neg
    return loss, grad_neg_sim


def main() -> None:
    # 1. Verify Section 4.1 query budget examples: FiQA (57.6K -> q_avg=5) and Robust04 (528.2K -> 83.3K, q_avg=3)
    fiqa_c, fiqa_qpp = compute_gpl_qpp_and_corpus_size(57_600)
    assert fiqa_c == 57_600 and fiqa_qpp == 5
    rob_c, rob_qpp = compute_gpl_qpp_and_corpus_size(528_200)
    assert rob_c == 83_334 and rob_qpp == 3

    # 2. Verify Table 5 FiQA case study ("what is futures contract"):
    # Positive passage CE = 10.3; Negative 2 (true irrelevant mention) CE = 0.3 (delta = 10.0);
    # Negative 3 (false negative that actually defines futures contract) CE = 8.2 (delta = 2.1).
    ce_pos = 10.3
    ce_true_neg = 0.3
    ce_false_neg = 8.2

    # Suppose the student bi-encoder currently assigns pos_sim = 10.0 and neg_sim = 8.0 to a relevant hard negative.
    pos_sim = 10.0
    neg_sim = 8.0

    # Under GPL MarginMSE, for the false negative (delta = 10.3 - 8.2 = 2.1), hat_delta = 10.0 - 8.0 = 2.0,
    # so the student margin matches the cross-encoder margin almost exactly (loss = 0.01, tiny repulsive gradient).
    loss_fn_gpl, grad_fn_gpl = margin_mse_loss_and_grad_wrt_neg_sim(pos_sim, neg_sim, ce_pos, ce_false_neg)
    # For the true negative (delta = 10.3 - 0.3 = 10.0), hat_delta = 2.0 << 10.0, so GPL strongly pushes neg_sim down.
    loss_tn_gpl, grad_tn_gpl = margin_mse_loss_and_grad_wrt_neg_sim(pos_sim, neg_sim, ce_pos, ce_true_neg)

    assert loss_fn_gpl < 0.02
    assert loss_tn_gpl > 60.0
    assert abs(grad_tn_gpl) > 70.0 * abs(grad_fn_gpl)

    # Under binary 0-1 QGen (MNRL), both true and false negatives receive label 0 and identical repulsive gradient!
    _, grad_fn_qgen = mnrl_loss_and_grad_wrt_neg_sim(pos_sim, neg_sim)
    _, grad_tn_qgen = mnrl_loss_and_grad_wrt_neg_sim(pos_sim, neg_sim)
    assert abs(grad_fn_qgen - grad_tn_qgen) < 1e-12
    assert grad_fn_qgen > 0.1

    print(
        "GPL boundary verification passed:",
        {"loss_false_neg_gpl": round(loss_fn_gpl, 4), "loss_true_neg_gpl": round(loss_tn_gpl, 4)},
    )


if __name__ == "__main__":
    main()
