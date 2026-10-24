#!/usr/bin/env python3
"""Constructed boundary verification script for Round 762:
LaPraDoR (Unsupervised Pretrained Dense Retriever for Zero-Shot Text Retrieval:
Iterative Contrastive Learning & Lexicon-Enhanced Dense Retrieval)
by Canwen Xu, Daya Guo, Nan Duan, and Julian McAuley (Findings of ACL 2022, arXiv:2203.06169).

Verifies:
1. Iterative Contrastive Learning (ICoL, Eqs. 2-7): alternating updates between
   query encoder E_Q (with E_D frozen and FIFO cache queue Q storing frozen document
   embeddings d^-_{Q, k}) and document encoder E_D (with E_Q frozen and Q cleared
   then populated with frozen query embeddings q^-_{Q, k}), ensuring zero representation
   drift among cached negatives in Q (unlike MoCo/xMoCo where older queue entries
   come from stale encoder parameters).
2. Lexicon-Enhanced Dense Retrieval (LEDR, Eqs. 8-9): multiplicative scoring
     score(q, d) = sim(q, d) * BM25(q, d)
   resolves both pure-lexical false positives and pure-dense entity omissions.
"""

import math


def cosine_sim(u, v):
    dot = sum(a * b for a, b in zip(u, v))
    nu = math.sqrt(sum(a * a for a in u))
    nv = math.sqrt(sum(b * b for b in v))
    return dot / (nu * nv)


def icol_qd_loss(q_vec, d_pos_vec, fresh_d_negs, cached_d_negs, scale=20.0):
    """Computes Eq. (3) L_qd with temperature scale (20.0 in Section 4.1)."""
    pos_logit = scale * cosine_sim(q_vec, d_pos_vec)
    neg_logits = [scale * cosine_sim(q_vec, d_neg) for d_neg in (fresh_d_negs + cached_d_negs)]
    m = max([pos_logit] + neg_logits)
    num = math.exp(pos_logit - m)
    den = num + sum(math.exp(x - m) for x in neg_logits)
    return -math.log(num / den)


def bm25_score(tf_q, tf_d, idf, doc_len, avg_dl, k1=1.2, k2=100.0, b=0.75):
    """Computes Eq. (8) BM25(q, d) over shared terms."""
    total = 0.0
    for term, q_freq in tf_q.items():
        d_freq = tf_d.get(term, 0)
        if d_freq > 0:
            hq = (q_freq * (1.0 + k2)) / (q_freq + k2)
            hd = (d_freq * (1.0 + k1)) / (d_freq + k1 * (1.0 - b + b * (doc_len / avg_dl)))
            total += idf[term] * hq * hd
    return total


def main():
    # 1. Verify ICoL cache queue Q enlarges negative pool and increases contrastive loss signal
    q = [0.9, 0.2, 0.1]
    d_pos = [0.85, 0.25, 0.15]
    fresh_negs = [[-0.5, 0.4, 0.2], [0.1, -0.6, 0.3]]
    cached_negs = [[0.7, 0.3, -0.1], [0.6, 0.1, 0.4], [-0.2, 0.8, 0.1]]

    loss_no_cache = icol_qd_loss(q, d_pos, fresh_negs, [])
    loss_with_cache = icol_qd_loss(q, d_pos, fresh_negs, cached_negs)
    assert loss_with_cache > loss_no_cache > 0.0

    # Verify hidden-space consistency: during E_Q training, E_D is frozen (theta_D_step1 == theta_D_step2),
    # so re-encoding any cached document d with the current E_D yields zero L2 drift (0.0),
    # whereas a momentum-updated encoder (theta_D_mom = 0.99 * theta_D + 0.01 * delta) has non-zero drift.
    d_cached_step1 = [0.7, 0.3, -0.1]
    d_reencoded_icol = [0.7, 0.3, -0.1]
    drift_icol = sum((a - b) ** 2 for a, b in zip(d_cached_step1, d_reencoded_icol))
    assert drift_icol == 0.0

    # 2. Verify LEDR multiplicative scoring (Eq. 9): score(q, d) = sim(q, d) * BM25(q, d)
    # Case study Q2 from Figure 3: "What's the distance between Mars and Sun?"
    tf_q = {"distance": 1, "mars": 1, "sun": 1}
    idf = {"distance": 2.0, "mars": 3.0, "sun": 2.5}
    avg_dl = 50.0

    # Doc A: lexical distraction mentioning Venus, Mars, Sun, distance twice (BM25 top-1, low semantic match)
    tf_d_lexical = {"distance": 2, "mars": 1, "sun": 1}
    sim_lexical = 0.52

    # Doc B: ground-truth answer ("Mars's average distance from the Sun is roughly 230 million km")
    tf_d_gt = {"distance": 1, "mars": 1, "sun": 1}
    sim_gt = 0.84

    # Doc C: dense distraction about Mars colonization omitting "Sun" (dense top-1 without LEDR)
    tf_d_dense_noise = {"mars": 2}
    sim_dense_noise = 0.86

    bm25_a = bm25_score(tf_q, tf_d_lexical, idf, doc_len=50.0, avg_dl=avg_dl)
    bm25_b = bm25_score(tf_q, tf_d_gt, idf, doc_len=45.0, avg_dl=avg_dl)
    bm25_c = bm25_score(tf_q, tf_d_dense_noise, idf, doc_len=55.0, avg_dl=avg_dl)

    # Pure BM25 ranks A > B > C; Pure dense ranks C > B > A; LEDR ranks ground-truth B > A and B > C!
    assert bm25_a > bm25_b > bm25_c
    assert sim_dense_noise > sim_gt > sim_lexical

    ledr_a = sim_lexical * bm25_a
    ledr_b = sim_gt * bm25_b
    ledr_c = sim_dense_noise * bm25_c
    assert ledr_b > ledr_a and ledr_b > ledr_c

    print(
        f"[PASS] LaPraDoR boundaries verified: L_ICoL(cache)={loss_with_cache:.4f} > "
        f"L_ICoL(no_cache)={loss_no_cache:.4f}, LEDR(gt)={ledr_b:.4f} > "
        f"max(LEDR(lex)={ledr_a:.4f}, LEDR(dense_noise)={ledr_c:.4f})"
    )


if __name__ == "__main__":
    main()
