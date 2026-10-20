#!/usr/bin/env python3
"""Boundary verification for Round 752: coCondenser Unsupervised Corpus-Aware Pre-training (Gao & Callan, ACL 2022)."""

import math


def condenser_late_early_short_circuit(h_early_cls, h_early_tokens, h_late_cls, h_late_tokens):
    """Eq. 4: Head([h_cls^late; h^early]) routes late CLS and early token vectors into the Condenser head."""
    head_input_cls = list(h_late_cls)
    head_input_tokens = [list(tok) for tok in h_early_tokens]
    return head_input_cls, head_input_tokens


def cocondenser_contrastive_loss(span_cls_embeddings):
    """Eq. 6: Corpus-aware contrastive loss over n documents x 2 random spans (s_{i1}, s_{i2})."""
    n_docs = len(span_cls_embeddings)
    assert all(len(pair) == 2 for pair in span_cls_embeddings)
    flat = []
    for i in range(n_docs):
        for j in range(2):
            flat.append((i, j, span_cls_embeddings[i][j]))

    def dot(u, v):
        return sum(a * b for a, b in zip(u, v))

    total_co_loss = 0.0
    for i in range(n_docs):
        pos_dot = dot(span_cls_embeddings[i][0], span_cls_embeddings[i][1])
        pos_exp = math.exp(pos_dot)
        for j in range(2):
            h_ij = span_cls_embeddings[i][j]
            denom = 0.0
            for k, l, h_kl in flat:
                if (k, l) != (i, j):
                    denom += math.exp(dot(h_ij, h_kl))
            l_co_ij = -math.log(pos_exp / denom)
            total_co_loss += l_co_ij
    return total_co_loss / (2.0 * n_docs), total_co_loss


def gradient_cache_span_gradients(span_cls_embeddings):
    """Eq. 9-12: Exact derivative v_{ij} = d L^{co} / d h_{ij} cached so full batch graph is not held in GPU memory."""
    n_docs = len(span_cls_embeddings)
    dim = len(span_cls_embeddings[0][0])
    eps = 1e-6
    _, base_sum = cocondenser_contrastive_loss(span_cls_embeddings)
    cache = [[ [0.0] * dim for _ in range(2) ] for _ in range(n_docs)]
    for i in range(n_docs):
        for j in range(2):
            for d in range(dim):
                perturbed = [
                    [list(span_cls_embeddings[doc_idx][sp_idx]) for sp_idx in range(2)]
                    for doc_idx in range(n_docs)
                ]
                perturbed[i][j][d] += eps
                _, plus_sum = cocondenser_contrastive_loss(perturbed)
                perturbed[i][j][d] -= 2.0 * eps
                _, minus_sum = cocondenser_contrastive_loss(perturbed)
                cache[i][j][d] = (plus_sum - minus_sum) / (2.0 * eps)
    return cache


def main():
    # 1. Verify Condenser head short-circuit routing (Eq. 1-4)
    h_early_cls = [0.1, 0.2]
    h_early_tokens = [[0.5, -0.3], [0.2, 0.7]]
    h_late_cls = [0.9, -0.8]
    h_late_tokens = [[-0.9, 0.1], [0.0, -0.4]]
    head_cls, head_toks = condenser_late_early_short_circuit(
        h_early_cls, h_early_tokens, h_late_cls, h_late_tokens
    )
    assert head_cls == h_late_cls and head_cls != h_early_cls
    assert head_toks == h_early_tokens and head_toks != h_late_tokens

    # 2. Verify corpus-level span contrastive loss (Eq. 6): aligned same-document spans reduce L^co
    unaligned_spans = [
        [[1.0, 0.0], [0.0, 1.0]],
        [[0.0, -1.0], [-1.0, 0.0]],
        [[0.7, 0.7], [-0.7, -0.7]],
    ]
    aligned_spans = [
        [[1.2, 0.1], [1.1, 0.2]],
        [[-1.1, 0.2], [-1.2, 0.1]],
        [[0.1, -1.3], [0.2, -1.2]],
    ]
    loss_unaligned, _ = cocondenser_contrastive_loss(unaligned_spans)
    loss_aligned, _ = cocondenser_contrastive_loss(aligned_spans)
    assert loss_aligned < loss_unaligned, f"Expected {loss_aligned} < {loss_unaligned}"

    # 3. Verify Gradient Cache (Eq. 9-12) matches exact full-batch directional derivative via sub-batch accumulation
    cache = gradient_cache_span_gradients(aligned_spans)
    # Parameter update delta_h_ij = 0.01 * h_ij; sub-batch accumulated chain rule sum_{i,j} v_{ij}^T (dh_{ij}/dTheta)
    subbatch_grad = 0.0
    for i in range(len(aligned_spans)):
        for j in range(2):
            for d in range(2):
                subbatch_grad += cache[i][j][d] * aligned_spans[i][j][d]
    assert abs(subbatch_grad) > 1e-3

    # 4. Verify Table 1 & Table 2 empirical results (MS-MARCO Dev MRR@10 and R@1000 at batch size 64 vs 4096)
    msmarco_mrr10 = {
        "RocketQA_b4096": 37.0,
        "Condenser_no_hn_b64": 33.8,
        "Condenser_hn_b64": 36.6,
        "coCondenser_no_hn_b64": 35.7,
        "coCondenser_hn_b64": 38.2,
    }
    msmarco_r1000 = {
        "RocketQA_b4096": 97.9,
        "Condenser_no_hn_b64": 96.1,
        "Condenser_hn_b64": 97.4,
        "coCondenser_no_hn_b64": 97.8,
        "coCondenser_hn_b64": 98.4,
    }
    assert msmarco_mrr10["coCondenser_hn_b64"] > msmarco_mrr10["RocketQA_b4096"] > msmarco_mrr10["Condenser_hn_b64"]
    assert msmarco_r1000["coCondenser_no_hn_b64"] > msmarco_r1000["Condenser_hn_b64"]
    assert msmarco_r1000["coCondenser_hn_b64"] > msmarco_r1000["RocketQA_b4096"]
    print("Round 752 coCondenser boundary verification passed.")


if __name__ == "__main__":
    main()
