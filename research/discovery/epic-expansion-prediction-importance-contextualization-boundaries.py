#!/usr/bin/env python3
"""Constructed boundary verification for EPIC (MacAvaney et al., SIGIR 2020, arXiv:2004.14245).

Verifies:
1. Sparse query representation phi_q in R^{|V|} with log-softplus term importance
   w_q(t_i) = ln(1 + softplus(theta_1^T f_i(q))) summed over repeated query occurrences (Eq. 1).
2. Lexicon-grounded dense document representation phi_d in R^{|V|} combining:
   - Lexicon expansion projection psi_j = Theta_2 f_j(d) in R^{|V|}
   - Term importance w_d(t_j) = ln(1 + softplus(theta_3^T f_j(d))) (Eq. 2)
   - Document quality gating c(d) = sigmoid(theta_4^T d_[CLS]) (Eq. 3)
   - Max-pooling over document tokens phi_d(tau) = c(d) * max_{t_j in d} (w_d(t_j) * psi_j(tau)) (Eq. 4).
3. Query-length-proportional dot-product scoring sim(q, d) = sum_{tau in q} phi_q(tau) * phi_d(tau) (Eq. 5)
   and top-r document vector pruning preserving ranking order.
"""

from __future__ import annotations

import math


def softplus(x: float) -> float:
    if x > 20.0:
        return x
    return math.log(1.0 + math.exp(x))


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def term_importance(theta: list[float], f_vec: list[float]) -> float:
    """Implements Eqs. (1)-(2): w(t) = ln(1 + softplus(theta^T f(s)))."""
    val = math.log(1.0 + softplus(dot(theta, f_vec)))
    assert val > 0.0
    return val


def build_query_vector(
    query_token_ids: list[int],
    query_embs: list[list[float]],
    theta_1: list[float],
    vocab_size: int,
) -> dict[int, float]:
    """Implements Section 2 Query Representation (Eq. 1) with additive aggregation for repeated terms."""
    phi_q: dict[int, float] = {}
    for tok_id, f_i in zip(query_token_ids, query_embs):
        assert 0 <= tok_id < vocab_size
        w_i = term_importance(theta_1, f_i)
        phi_q[tok_id] = phi_q.get(tok_id, 0.0) + w_i
    return phi_q


def build_doc_vector(
    doc_embs: list[list[float]],
    cls_emb: list[float],
    theta_2: list[list[float]],
    theta_3: list[float],
    theta_4: list[float],
) -> list[float]:
    """Implements Section 2 Document Representation (Eqs. 2-4)."""
    vocab_size = len(theta_2)
    c_d = sigmoid(dot(theta_4, cls_emb))
    assert 0.0 < c_d < 1.0
    w_d = [term_importance(theta_3, f_j) for f_j in doc_embs]
    # psi_j(tau) = dot(theta_2[tau], f_j)
    phi_d = [0.0] * vocab_size
    for tau in range(vocab_size):
        max_val = max(w_d[j] * dot(theta_2[tau], doc_embs[j]) for j in range(len(doc_embs)))
        phi_d[tau] = c_d * max_val
    return phi_d


def prune_top_r(phi_d: list[float], r: int) -> list[float]:
    """Retains only the top-r largest entries of phi_d and zeros out the rest (Section 3)."""
    indexed = sorted(enumerate(phi_d), key=lambda kv: kv[1], reverse=True)
    keep = {idx for idx, _ in indexed[:r]}
    return [val if idx in keep else 0.0 for idx, val in enumerate(phi_d)]


def epic_similarity(phi_q: dict[int, float], phi_d: list[float]) -> float:
    """Implements Eq. (5): sim(q, d) = sum_{tau in q} phi_q(tau) * phi_d(tau)."""
    return sum(w_q * phi_d[tau] for tau, w_q in phi_q.items())


def main() -> None:
    # Vocabulary: 0="cost", 1="endless", 2="pool", 3="price", 4="swim", 5="baking"
    vocab_size = 6
    theta_1 = [0.8, 0.6, 0.4]
    theta_3 = [0.7, 0.5, 0.3]
    theta_4 = [0.9, 0.4, 0.2]

    # Lexicon projection matrix Theta_2 in R^{6 x 3}:
    # Notice "price" (dim 0 high) expands strongly to both "cost" (tau=0) and "price" (tau=3)!
    theta_2 = [
        [1.2, 0.3, 0.1],  # tau=0: "cost" (expanded from price/pool embeddings)
        [0.2, 1.1, 0.2],  # tau=1: "endless"
        [0.3, 0.9, 0.4],  # tau=2: "pool"
        [1.1, 0.2, 0.1],  # tau=3: "price"
        [0.2, 0.7, 0.8],  # tau=4: "swim"
        [0.0, 0.1, 1.2],  # tau=5: "baking"
    ]

    # Query: "cost endless pool pool" (term 2 appears twice -> additive importance)
    q_ids = [0, 1, 2, 2]
    q_embs = [
        [1.0, 0.3, 0.1],  # cost
        [0.2, 1.0, 0.2],  # endless
        [0.3, 0.8, 0.3],  # pool (1st)
        [0.3, 0.8, 0.3],  # pool (2nd)
    ]
    phi_q = build_query_vector(q_ids, q_embs, theta_1, vocab_size)
    assert len(phi_q) == 3  # Only 3 unique query terms non-zero
    assert abs(phi_q[2] - 2.0 * term_importance(theta_1, q_embs[2])) < 1e-12

    # Relevant passage mentions "endless", "pool", "price" (no literal "cost", but expands to tau=0="cost"):
    d_pos_embs = [
        [0.2, 1.1, 0.2],  # endless
        [0.3, 0.9, 0.4],  # pool
        [1.3, 0.4, 0.1],  # price -> projects strongly onto tau=0 ("cost")
    ]
    d_pos_cls = [1.0, 0.8, 0.5]  # High quality passage

    # Non-relevant passage with lower quality and baking context:
    d_neg_embs = [
        [0.1, 0.1, 1.1],  # baking
        [0.1, 0.2, 0.9],
    ]
    d_neg_cls = [-0.8, -0.5, 0.1]  # Low quality passage

    phi_d_pos = build_doc_vector(d_pos_embs, d_pos_cls, theta_2, theta_3, theta_4)
    phi_d_neg = build_doc_vector(d_neg_embs, d_neg_cls, theta_2, theta_3, theta_4)

    # Check that expansion gave tau=0 ("cost") a high weight in d_pos despite "cost" not appearing literally:
    assert phi_d_pos[0] > 1.0

    score_pos_full = epic_similarity(phi_q, phi_d_pos)
    score_neg_full = epic_similarity(phi_q, phi_d_neg)
    assert score_pos_full > score_neg_full

    # Prune document vectors to top r = 4 terms:
    phi_d_pos_pruned = prune_top_r(phi_d_pos, r=4)
    phi_d_neg_pruned = prune_top_r(phi_d_neg, r=4)
    score_pos_pruned = epic_similarity(phi_q, phi_d_pos_pruned)
    score_neg_pruned = epic_similarity(phi_q, phi_d_neg_pruned)
    assert score_pos_pruned > score_neg_pruned
    assert abs(score_pos_pruned - score_pos_full) < 1e-12

    print(
        f"[PASS] EPIC boundaries verified: phi_d_pos['cost']={phi_d_pos[0]:.4f}, "
        f"score_pos={score_pos_full:.4f} (pruned={score_pos_pruned:.4f}) > score_neg={score_neg_full:.4f}"
    )


if __name__ == "__main__":
    main()
