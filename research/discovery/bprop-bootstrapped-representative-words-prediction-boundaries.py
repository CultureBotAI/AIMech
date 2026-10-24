#!/usr/bin/env python3
"""Constructed boundary verification script for Round 765:
B-PROP (Bootstrapped Pre-training with Representative Words Prediction for Ad-hoc Retrieval)
by Xinyu Ma, Jiafeng Guo, Ruqing Zhang, Yixing Fan, Yingyan Li, and Xueqi Cheng
(SIGIR 2021, arXiv:2104.09791, doi:10.1145/3404835.3462869).

Verifies:
1. Saturated distinct term attention weight (Section 3.2.1, Eq. 5):
     beta^_{w_k} = sum_{x_t = w_k} alpha^t,
     beta_{w_k} = beta^_{w_k} / (b + beta^_{w_k}),
     P(w_k | theta_d) = exp(beta_{w_k}) / sum_{w' in V} exp(beta_{w'}).
2. Collection-averaged random term distribution (Section 3.2.2, Eq. 6):
     P(w_k | theta_random) = (1 / |D|) sum_{d in D} P(w_k | theta_d).
3. Divergence-from-randomness cross-entropy contrastive term distribution (Section 3.2.3, Eqs. 7-8):
     gamma^_{w_k} = -P(w_k | theta_d) * log2 P(w_k | theta_random),
     P(w_k | theta_contrastive) = exp(gamma^_{w_k}) / sum_{w' in V} exp(gamma^_{w'}),
   which suppresses high-attention collection stopwords ("the", "in") while promoting
   document-specific informative terms ("fibrosis", "pulmonary") as in Table 1.
"""

import math


def softmax_dict(scores):
    m = max(scores.values())
    exps = {k: math.exp(v - m) for k, v in scores.items()}
    total = sum(exps.values())
    return {k: v / total for k, v in exps.items()}


def compute_doc_term_dist(raw_attn_sums, vocab, b=0.01):
    """Computes saturated term weights beta_{w_k} and softmax distribution P(w_k | theta_d) (Eq. 5)."""
    betas = {}
    for w in vocab:
        beta_hat = raw_attn_sums.get(w, 0.0)
        betas[w] = (beta_hat / (b + beta_hat)) if beta_hat > 0.0 else 0.0
    return softmax_dict(betas), betas


def main():
    vocab = ["fibrosis", "pulmonary", "the", "in", "unrelated"]

    # Document d_1 (about pulmonary fibrosis): BERT vanilla [CLS] attention gives high weight
    # to both topical terms ("fibrosis", "pulmonary") AND common stopwords ("the", "in")
    d1_attn = {"fibrosis": 0.18, "pulmonary": 0.16, "the": 0.25, "in": 0.20}
    # Other documents d_2, d_3, d_4 in collection D: stopwords "the" and "in" have high attention
    # everywhere, whereas "fibrosis" and "pulmonary" are absent (0.0)
    d2_attn = {"the": 0.28, "in": 0.22, "unrelated": 0.30}
    d3_attn = {"the": 0.26, "in": 0.24, "unrelated": 0.25}
    d4_attn = {"the": 0.27, "in": 0.21, "unrelated": 0.28}

    docs_attn = [d1_attn, d2_attn, d3_attn, d4_attn]
    doc_dists = [compute_doc_term_dist(da, vocab, b=0.01)[0] for da in docs_attn]
    p_d1 = doc_dists[0]

    # 1. In vanilla document term distribution P(w | theta_{d1}), stopword "the" >= "fibrosis"
    assert p_d1["the"] > p_d1["fibrosis"]

    # 2. Compute collection random term distribution P(w | theta_random) (Eq. 6)
    p_random = {
        w: sum(dd[w] for dd in doc_dists) / len(doc_dists) for w in vocab
    }
    assert abs(sum(p_random.values()) - 1.0) < 1e-12
    # Stopwords have higher collection-wide random probability than rare topical terms
    assert p_random["the"] > p_random["fibrosis"]
    assert p_random["in"] > p_random["pulmonary"]

    # 3. Compute cross-entropy divergence gamma^_{w_k} = -P(w_k | theta_d) log2 P(w_k | theta_random) (Eq. 7)
    # and contrastive term distribution P(w_k | theta_contrastive) (Eq. 8)
    gamma_hat = {
        w: -p_d1[w] * math.log2(p_random[w]) for w in vocab
    }
    p_contrastive = softmax_dict(gamma_hat)

    # Verify that contrastive term distribution reverses the ranking: topical terms "fibrosis"
    # and "pulmonary" now strictly outrank common stopwords "the" and "in"!
    assert p_contrastive["fibrosis"] > p_contrastive["the"]
    assert p_contrastive["pulmonary"] > p_contrastive["in"]

    print(
        f"[PASS] B-PROP contrastive term sampling boundaries verified: "
        f"P_d1(the)={p_d1['the']:.4f} > P_d1(fibrosis)={p_d1['fibrosis']:.4f}, "
        f"but P_contrastive(fibrosis)={p_contrastive['fibrosis']:.4f} > "
        f"P_contrastive(the)={p_contrastive['the']:.4f}"
    )


if __name__ == "__main__":
    main()
