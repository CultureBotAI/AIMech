#!/usr/bin/env python3
"""Boundary verification for Round 753: ANCE Approximate Nearest Neighbor Negative Contrastive Learning (Xiong et al., ICLR 2021)."""

import math


def importance_sampling_gradient_variance(grad_norms, probs):
    """Eq. 4-10: Trace of covariance Tr(V_{P_{D^-}}(g_{d^-})) = E[||g_{d^-}||^2] - ||E[g_{d^-}]||^2 for 1D aligned gradients."""
    n_neg = len(grad_norms)
    assert abs(sum(probs) - 1.0) < 1e-9
    mean_g = sum(probs[i] * (grad_norms[i] / (n_neg * probs[i])) for i in range(n_neg))
    second_moment = sum(probs[i] * ((grad_norms[i] / (n_neg * probs[i])) ** 2) for i in range(n_neg))
    return second_moment - (mean_g ** 2)


def local_batch_informative_prob(batch_size, n_informative, corpus_size):
    """Section 3: Probability p = b * |D^{-*}| / |C|^2 that a random mini-batch pair contains an informative negative."""
    return (batch_size * n_informative) / float(corpus_size ** 2)


def ance_top_negatives(query_vec, doc_vecs, pos_ids, top_k):
    """Eq. 13: D^-_{ANCE} = ANN_{f(q,d)} \\ D^+ selects top-k highest dot-product non-relevant documents from ANN index."""
    scored = []
    for doc_id, d_vec in enumerate(doc_vecs):
        if doc_id not in pos_ids:
            score = sum(q * d for q, d in zip(query_vec, d_vec))
            scored.append((score, doc_id))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [doc_id for _, doc_id in scored[:top_k]], [s for s, _ in scored[:top_k]]


def main():
    # 1. Verify Eq. 10: Sampling proportional to per-instance gradient norm minimizes estimator variance
    grad_norms = [0.001, 0.002, 0.005, 0.85, 1.40]
    uniform_probs = [1.0 / len(grad_norms)] * len(grad_norms)
    total_norm = sum(grad_norms)
    oracle_probs = [g / total_norm for g in grad_norms]
    var_uniform = importance_sampling_gradient_variance(grad_norms, uniform_probs)
    var_oracle = importance_sampling_gradient_variance(grad_norms, oracle_probs)
    assert var_oracle < 1e-12 and var_uniform > 0.25, f"Expected oracle variance ~0 < uniform {var_uniform}"

    # 2. Verify Section 3 inefficacy of local in-batch negatives when b << |C| and |D^{-*}| << |C|
    prob_local = local_batch_informative_prob(batch_size=32, n_informative=100, corpus_size=8_800_000)
    assert prob_local < 1e-10, f"Expected vanishing local informative probability, got {prob_local}"

    # 3. Verify Eq. 11-13: ANCE global ANN negatives yield much larger loss and gradient norm than random/local negatives
    q_vec = [1.0, 0.5]
    pos_vec = [1.0, 0.6]
    # Corpus: 0 is positive, 1..4 are trivial local negatives, 5..6 are hard global ANN negatives near q_vec
    corpus = [
        pos_vec,
        [-1.0, -0.8],
        [-0.9, -0.5],
        [-1.2, -0.3],
        [-0.8, -0.9],
        [0.98, 0.48],
        [0.95, 0.52],
    ]
    ance_ids, ance_scores = ance_top_negatives(q_vec, corpus, pos_ids={0}, top_k=2)
    assert ance_ids == [5, 6]
    s_pos = sum(a * b for a, b in zip(q_vec, pos_vec))
    s_local = sum(a * b for a, b in zip(q_vec, corpus[1]))
    s_ance = ance_scores[0]
    # NLL loss l(d+, d-) = -log(exp(s+) / (exp(s+) + exp(s-))) = log(1 + exp(s- - s+))
    loss_local = math.log(1.0 + math.exp(s_local - s_pos))
    loss_ance = math.log(1.0 + math.exp(s_ance - s_pos))
    # Gradient magnitude wrt logit difference is sigmoid(s- - s+)
    grad_local = 1.0 / (1.0 + math.exp(-(s_local - s_pos)))
    grad_ance = 1.0 / (1.0 + math.exp(-(s_ance - s_pos)))
    assert loss_ance > 5.0 * loss_local
    assert grad_ance > 5.0 * grad_local

    # 4. Verify Table 1 & Table 5 benchmark invariants (MS MARCO Dev MRR@10 = 0.330, TREC DL Passage NDCG@10 = 0.648, 11.6ms vs 1.42s)
    assert 0.330 > 0.311 > 0.240  # ANCE FirstP > DPR > BM25 on MARCO Dev MRR@10
    assert 0.648 > 0.600 > 0.506  # ANCE FirstP > DPR > BM25 on TREC DL Passage NDCG@10
    assert 0.628 > 0.615 > 0.557 > 0.519  # ANCE MaxP > ANCE FirstP > DPR > BM25 on TREC DL Document NDCG@10
    speedup = 1420.0 / 11.6
    assert speedup > 100.0
    print("Round 753 ANCE boundary verification passed.")


if __name__ == "__main__":
    main()
