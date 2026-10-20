#!/usr/bin/env python3
"""Constructed boundary verification for DSGSUM (Augmented Abstractive Summarization With Document-Level Semantic Graph, Bi et al., arXiv:2109.06046)."""

import json
import math


def gat_entity_update(g_prev, neighbors, w1, w2):
    """Eqs. (1)-(2): Graph Attention Network node update with bilinear attention weights."""
    n_nodes = len(g_prev)
    d = len(g_prev[0])
    g_next = []
    attn_rows = []
    for i in range(n_nodes):
        w1_gi = [sum(w1[r][c] * g_prev[i][c] for c in range(d)) for r in range(d)]
        scores = []
        for j in neighbors[i]:
            w2_gj = [sum(w2[r][c] * g_prev[j][c] for c in range(d)) for r in range(d)]
            scores.append(sum(a * b for a, b in zip(w1_gi, w2_gj)))
        max_s = max(scores)
        exps = [math.exp(s - max_s) for s in scores]
        denom = sum(exps)
        alphas = [e / denom for e in exps]
        attn_rows.append(alphas)

        agg = [0.0] * d
        for alpha, j in zip(alphas, neighbors[i]):
            for c in range(d):
                agg[c] += alpha * g_prev[j][c]
        res = [g_prev[i][c] + agg[c] for c in range(d)]
        # LayerNorm over d dimensions
        mean_r = sum(res) / d
        var_r = sum((v - mean_r) ** 2 for v in res) / d
        ln = [(v - mean_r) / math.sqrt(var_r + 1e-6) for v in res]
        g_next.append(ln)
    return g_next, attn_rows


def context_to_entity_attention(s_t, g_entities, ws, wg, wsg):
    """Eqs. (5)-(6): Context-to-Entity similarity M_{ti} = alpha(s_t, g_i) and gated fusion s^g."""
    d = len(s_t)
    scores = []
    for g_i in g_entities:
        hadamard = [s_t[c] * g_i[c] for c in range(d)]
        sim = (
            sum(ws[c] * s_t[c] for c in range(d))
            + sum(wg[c] * g_i[c] for c in range(d))
            + sum(wsg[c] * hadamard[c] for c in range(d))
        )
        scores.append(sim)
    max_s = max(scores)
    exps = [math.exp(v - max_s) for v in scores]
    denom = sum(exps)
    a_ti = [e / denom for e in exps]

    g_tilde = [0.0] * d
    for weight, g_i in zip(a_ti, g_entities):
        for c in range(d):
            g_tilde[c] += weight * g_i[c]

    s_hadamard_g = [s_t[c] * g_tilde[c] for c in range(d)]
    concat_3d = s_t + g_tilde + s_hadamard_g
    return concat_3d, a_ti, g_tilde


def main():
    # 1. Verify Frequency Embedding sorting and rank assignment: g_i^0 = e_i + FE(rank_i)
    entity_counts = [("Obama", 7), ("White House", 4), ("Washington", 3), ("trivial_mention", 1)]
    # Coreference clusters with < 3 mentions are filtered out (Section 2.1, p. 4)
    kept_entities = [(name, cnt) for name, cnt in sorted(entity_counts, key=lambda x: x[1], reverse=True) if cnt >= 3]
    assert [name for name, _ in kept_entities] == ["Obama", "White House", "Washington"]

    # 2. Verify Eqs. (1)-(2) GAT neighbor attention normalization and LayerNorm
    g0 = [
        [1.0, 0.2, -0.4],
        [0.8, -0.1, 0.5],
        [-0.3, 0.9, 0.1],
    ]
    neighbors = [[0, 1, 2], [1, 0], [2, 0]]
    eye = [[1.0 if r == c else 0.0 for c in range(3)] for r in range(3)]
    g1, attn_rows = gat_entity_update(g0, neighbors, eye, eye)
    for row in attn_rows:
        assert abs(sum(row) - 1.0) < 1e-12
    for vec in g1:
        assert abs(sum(vec) / len(vec)) < 1e-6

    # 3. Verify Eqs. (5)-(6) Context-to-Entity attention vector dimensions (3d concatenation [s; g_tilde; s o g_tilde])
    s_t = [0.9, 0.3, -0.2]
    ws = [0.5, 0.2, 0.1]
    wg = [0.4, 0.1, 0.2]
    wsg = [1.2, 0.8, 0.5]
    concat_3d, a_ti, g_tilde = context_to_entity_attention(s_t, g1, ws, wg, wsg)
    assert len(concat_3d) == 9
    assert abs(sum(a_ti) - 1.0) < 1e-12
    assert a_ti[0] > a_ti[2]  # Entity 0 aligns most strongly with decoder state s_t

    summary = {
        "concept": "DSGSUMDocumentLevelSemanticGraphAbstractiveSummarization",
        "kept_salient_entities": len(kept_entities),
        "gat_attention_sum": round(sum(attn_rows[0]), 6),
        "context2entity_top_weight": round(a_ti[0], 5),
        "fused_representation_dim": len(concat_3d),
        "verification": "passed",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
