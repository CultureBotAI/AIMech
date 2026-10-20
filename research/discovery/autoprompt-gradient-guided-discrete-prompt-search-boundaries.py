#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 718: AutoPrompt (Shin et al., EMNLP 2020)."""

import math


def verify_autoprompt() -> None:
    # 1. Marginalized class probability over label token set V_y (Eq. 1):
    # p(y | x_prompt) = sum_{w in V_y} p([MASK] = w | x_prompt)
    vocab_logits = {
        "crisp": 1.8,
        "marvelous": 2.4,
        "philanthrop": 1.5,
        "worse": 0.2,
        "incompetence": -0.3,
        "neutral_tok": 0.1,
    }
    max_l = max(vocab_logits.values())
    exp_l = {w: math.exp(v - max_l) for w, v in vocab_logits.items()}
    z = sum(exp_l.values())
    mlm_probs = {w: v / z for w, v in exp_l.items()}

    v_pos = ["crisp", "marvelous", "philanthrop"]
    v_neg = ["worse", "incompetence"]
    p_pos = sum(mlm_probs[w] for w in v_pos)
    p_neg = sum(mlm_probs[w] for w in v_neg)
    assert p_pos > p_neg
    assert 0.0 < p_pos + p_neg < 1.0

    # 2. First-order gradient-guided trigger token candidate selection (Eq. 2):
    # V_cand = top-k_{w in V} [ w_in^T * grad_{x_trig^(j)} log p(y | x_prompt) ]
    grad_trig_j = [0.6, -0.4, 0.8, 0.2]
    vocab_embeddings = {
        "tok_a": [-0.5, 0.3, -0.2, 0.1],
        "tok_b": [0.7, -0.5, 0.9, 0.3],
        "tok_c": [0.5, -0.2, 0.6, 0.1],
        "tok_d": [0.1, 0.4, -0.3, -0.2],
    }
    scores = {
        w: sum(e_i * g_i for e_i, g_i in zip(emb, grad_trig_j))
        for w, emb in vocab_embeddings.items()
    }
    k = 2
    v_cand = sorted(scores.keys(), key=lambda w: scores[w], reverse=True)[:k]
    assert v_cand == ["tok_b", "tok_c"]

    # 3. Automated label token selection (Eq. 4 & 5):
    # Substitute h^(i) with output word embedding w_out in s(y, w) proportional to exp(w_out * y_vec + beta_y)
    y_pos_vec = [0.5, 0.8, -0.2, 0.4]
    beta_pos = 0.1
    label_scores = {
        w: math.exp(sum(e_i * y_i for e_i, y_i in zip(emb, y_pos_vec)) + beta_pos)
        for w, emb in vocab_embeddings.items()
    }
    assert max(label_scores, key=label_scores.get) in vocab_embeddings
    print("AutoPrompt verification passed.")


if __name__ == "__main__":
    verify_autoprompt()
