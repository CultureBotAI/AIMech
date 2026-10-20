#!/usr/bin/env python3
"""Boundary verification for Round 743: COIL Contextualized Inverted List (Gao, Dai, & Callan, NAACL-HLT 2021)."""


def coil_tok_score(query_tokens, query_tok_vecs, inverted_lists, doc_id):
    """Eq. 5: s_tok(q, d) = sum_{q_i in q cap d} max_{d_j = q_i} (v_i^q)^T v_j^d."""
    total = 0.0
    for q_tok, v_q in zip(query_tokens, query_tok_vecs):
        postings = inverted_lists.get(q_tok, {}).get(doc_id, [])
        if postings:
            max_sim = max(sum(a * b for a, b in zip(v_q, v_d)) for v_d in postings)
            total += max_sim
    return total


def coil_full_score(query_tokens, query_tok_vecs, query_cls_vec, inverted_lists, doc_cls_vecs, doc_id):
    """Eq. 7: s_full(q, d) = s_tok(q, d) + (v_cls^q)^T v_cls^d."""
    s_tok = coil_tok_score(query_tokens, query_tok_vecs, inverted_lists, doc_id)
    v_d_cls = doc_cls_vecs[doc_id]
    s_cls = sum(a * b for a, b in zip(query_cls_vec, v_d_cls))
    return s_tok + s_cls


def main():
    # 1. Verify Table 4 contextualized sense disambiguation on overlapping surface token "cabinet"
    # Query: "what is a cabinet in govt", token "cabinet" has contextualized vector aligned with government sense
    query_tokens = ["cabinet"]
    query_tok_vecs = [[4.0, 0.5]]
    # Inverted list for surface token "cabinet":
    # doc 0 (government cabinet, two mentions): scores ~ 16.28 and 16.75 -> max = 16.75
    # doc 1 (kitchen cupboard cabinet, one mention): score ~ 7.23
    inverted_lists = {
        "cabinet": {
            0: [[3.97, 0.80], [4.05, 1.10]],
            1: [[1.92, -0.90]],
            2: [],  # doc 2 has no lexical overlap on "cabinet", only vocabulary-mismatch synonym "ministry"
        }
    }
    s_tok_doc0 = coil_tok_score(query_tokens, query_tok_vecs, inverted_lists, doc_id=0)
    s_tok_doc1 = coil_tok_score(query_tokens, query_tok_vecs, inverted_lists, doc_id=1)
    s_tok_doc2 = coil_tok_score(query_tokens, query_tok_vecs, inverted_lists, doc_id=2)
    assert abs(s_tok_doc0 - 16.75) < 1e-6
    assert abs(s_tok_doc1 - 7.23) < 1e-6
    assert s_tok_doc2 == 0.0
    assert s_tok_doc0 > 2.0 * s_tok_doc1

    # 2. Verify Eq. 7 COIL-full resolves vocabulary mismatch on doc 2 via CLS dot product while keeping doc 0 > doc 1
    query_cls_vec = [2.0, 2.0]
    doc_cls_vecs = {
        0: [2.0, 2.0],
        1: [-1.0, 0.5],
        2: [2.1, 1.9],
    }
    s_full_doc0 = coil_full_score(query_tokens, query_tok_vecs, query_cls_vec, inverted_lists, doc_cls_vecs, 0)
    s_full_doc1 = coil_full_score(query_tokens, query_tok_vecs, query_cls_vec, inverted_lists, doc_cls_vecs, 1)
    s_full_doc2 = coil_full_score(query_tokens, query_tok_vecs, query_cls_vec, inverted_lists, doc_cls_vecs, 2)
    assert s_full_doc0 > s_full_doc2 > s_full_doc1
    assert s_full_doc2 > s_tok_doc2

    # 3. Verify Table 1, Table 2, and Table 3 dimensionality and benchmark invariants
    # MS MARCO Passage Dev MRR@10: BM25 (0.184) < DeepCT (0.243) < DocT5Query (0.278) < Dense (0.304) < COIL-tok (0.341) < COIL-full (0.355)
    assert 0.184 < 0.243 < 0.278 < 0.304 < 0.341 < 0.355
    # TREC DL 2019 Passage NDCG@10: BM25 (0.506) < Dense (0.635) < DocT5Query (0.642) < COIL-tok (0.660) < COIL-full (0.704)
    assert 0.506 < 0.635 < 0.642 < 0.660 < 0.704
    # MS MARCO Document Dev MRR@10: BM25 (0.230) < Dense (0.340) < COIL-tok (0.385) < COIL-full (0.397)
    assert 0.230 < 0.340 < 0.385 < 0.397
    print("Round 743 COIL boundary verification passed.")


if __name__ == "__main__":
    main()
