#!/usr/bin/env python3
"""Boundary and mathematical verification for Round 719: LM-BFF (Gao, Fisch, & Chen, ACL 2021)."""

import math


def verify_lm_bff() -> None:
    # 1. Prompt-based classification probability over verbalizer M: Y -> V (Eq. 1):
    # p(y | x_in) = exp(w_{M(y)} . h_{[MASK]}) / sum_{y' in Y} exp(w_{M(y')} . h_{[MASK]})
    h_mask = [0.8, -0.3, 0.5, 0.4]
    w_great = [0.9, -0.2, 0.6, 0.3]
    w_terrible = [-0.5, 0.4, -0.3, -0.2]
    logit_pos = sum(w * h for w, h in zip(w_great, h_mask))
    logit_neg = sum(w * h for w, h in zip(w_terrible, h_mask))
    p_pos = math.exp(logit_pos) / (math.exp(logit_pos) + math.exp(logit_neg))
    p_neg = 1.0 - p_pos
    assert p_pos > 0.85

    # 2. Prompt-based bounded-interval regression as two-pole mixture model (Eq. 2):
    # y_hat = v_l * p(y_l | x_in) + v_u * p(y_u | x_in) over [v_l, v_u] = [0.0, 5.0]
    v_l, v_u = 0.0, 5.0
    y_hat = v_l * p_neg + v_u * p_pos
    assert v_l <= y_hat <= v_u
    # Observed mixture weight (y_gold - v_l) / (v_u - v_l) for KL divergence loss:
    y_gold = 4.2
    obs_u = (y_gold - v_l) / (v_u - v_l)
    obs_l = 1.0 - obs_u
    kl_div = obs_u * math.log(obs_u / p_pos) + obs_l * math.log(obs_l / p_neg)
    assert kl_div >= 0.0

    # 3. Selective demonstration sampling via SBERT cosine similarity (Section 6.2):
    # Sort D_train^c by cos(e(x_in), e(x)) and sample from top r = 50% per class
    q_emb = [1.0, 0.0, 0.0]
    class_embs = [
        [0.95, 0.31, 0.0],
        [0.80, 0.60, 0.0],
        [0.10, 0.99, 0.0],
        [-0.50, 0.86, 0.0],
    ]
    sims = [sum(q * x for q, x in zip(q_emb, emb)) for emb in class_embs]
    top_half = sorted(range(len(sims)), key=lambda i: sims[i], reverse=True)[: len(sims) // 2]
    assert top_half == [0, 1]
    print("LM-BFF verification passed.")


if __name__ == "__main__":
    verify_lm_bff()
