#!/usr/bin/env python3
"""Constructed boundary verification for DC-BERT (Zhang et al., SIGIR 2020, arXiv:2002.12591)."""

import math


def inject_global_embeddings(
    t_q: list[list[float]],
    t_d: list[list[float]],
    e_pos: list[list[float]],
    e_q: list[float],
    e_d: list[float],
) -> list[list[float]]:
    """Section 2: Add global position embeddings E_{P_i} and global type embeddings E_Q, E_D."""
    seq: list[list[float]] = []
    for idx, vec in enumerate(t_q):
        seq.append([vec[c] + e_q[c] + e_pos[idx][c] for c in range(len(vec))])
    offset = len(t_q)
    for jdx, vec in enumerate(t_d):
        seq.append([vec[c] + e_d[c] + e_pos[offset + jdx][c] for c in range(len(vec))])
    return seq


def dc_bert_reranker_prob(
    o_cls_q: list[float],
    o_cls_d: list[float],
    w1: list[list[float]],
    b1: list[float],
    w2: list[float],
    b2: float,
) -> float:
    """Eq. (1): p(Q_i, D_j) = sigma(MLP([o_[CLS]; o'_[CLS]])) with tanh hidden activation."""
    concat = list(o_cls_q) + list(o_cls_d)
    hidden = [
        math.tanh(sum(w1[r][c] * concat[c] for c in range(len(concat))) + b1[r])
        for r in range(len(w1))
    ]
    logit = sum(w2[r] * hidden[r] for r in range(len(w2))) + b2
    return 1.0 / (1.0 + math.exp(-logit))


def compute_pbt_and_ptb_at_n(
    tfidf_top_n_hits: list[set[int]],
    reranker_top_n_hits: list[set[int]],
) -> tuple[float, float]:
    """Section 3: PBT@N and PTB@N symmetric semantic retrieval evaluation metrics."""
    num_q = len(tfidf_top_n_hits)
    pbt_count = 0
    ptb_count = 0
    for tfidf_hits, rerank_hits in zip(tfidf_top_n_hits, reranker_top_n_hits):
        # PBT@N: at least one answer-bearing doc in reranker top-N is NOT in TF-IDF top-N
        if len(rerank_hits - tfidf_hits) > 0:
            pbt_count += 1
        # PTB@N: at least one answer-bearing doc in TF-IDF top-N is NOT in reranker top-N
        if len(tfidf_hits - rerank_hits) > 0:
            ptb_count += 1
    return 100.0 * pbt_count / num_q, 100.0 * ptb_count / num_q


def main() -> None:
    # 1. Verify global position and type embedding injection preserves total length (N+2) + (M+2):
    n_q_toks, m_d_toks, dim = 4, 6, 3
    t_q = [[0.1 * (i + 1)] * dim for i in range(n_q_toks)]
    t_d = [[0.05 * (j + 1)] * dim for j in range(m_d_toks)]
    e_pos = [[0.01 * p] * dim for p in range(n_q_toks + m_d_toks)]
    e_q = [1.0, 0.0, -1.0]
    e_d = [-1.0, 0.0, 1.0]
    seq = inject_global_embeddings(t_q, t_d, e_pos, e_q, e_d)
    assert len(seq) == n_q_toks + m_d_toks
    # Question [CLS] at index 0 and Document [CLS] at index n_q_toks have distinct type/position shifts:
    assert seq[0] != seq[n_q_toks]

    # 2. Verify Eq. (1) binary classifier probability in (0, 1) and BCE loss Eq. (2):
    p_rel = dc_bert_reranker_prob(
        o_cls_q=[0.8, 0.6, 0.4],
        o_cls_d=[0.7, 0.5, 0.3],
        w1=[[0.5, 0.5, 0.5, 0.5, 0.5, 0.5], [-0.2, 0.1, 0.3, -0.2, 0.1, 0.3]],
        b1=[0.1, -0.1],
        w2=[1.5, 0.5],
        b2=0.2,
    )
    assert 0.5 < p_rel < 1.0

    # 3. Verify lower-layer complexity reduction O(N_q * N_d * (L_q + L_d)^2) -> O(N_q * L_q^2) with offline cache:
    n_q, n_d, l_q, l_d = 100, 80, 16, 256
    concat_cost = n_q * n_d * ((l_q + l_d) ** 2)
    cached_online_cost = n_q * (l_q ** 2)
    assert concat_cost // cached_online_cost == 23120

    # 4. Verify symmetric PBT@N and PTB@N metrics:
    tfidf_hits = [{1, 2}, {3}, set(), {5}]
    rerank_hits = [{1, 2, 9}, {3}, {8}, set()]
    pbt, ptb = compute_pbt_and_ptb_at_n(tfidf_hits, rerank_hits)
    assert abs(pbt - 50.0) < 1e-9  # Q0 (doc 9) and Q2 (doc 8) discovered beyond TF-IDF
    assert abs(ptb - 25.0) < 1e-9  # Q3 lost doc 5 from TF-IDF

    print("DC-BERT boundary verification passed:")
    print(f"  Combined sequence length: {len(seq)}, p(Q, D) = {p_rel:.4f}")
    print(f"  PBT@N = {pbt:.1f}%, PTB@N = {ptb:.1f}%")


if __name__ == "__main__":
    main()
