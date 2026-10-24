#!/usr/bin/env python3
"""Boundary verification for Round 756: SimLM Pre-training with Representation Bottleneck for Dense Passage Retrieval (Wang et al., ACL 2023)."""

import math


def nested_electra_replacement_masks(seq_len, enc_mask_indices, extra_dec_mask_indices):
    """Eq. 1: Any replaced token in x_enc (p_enc=30%) is also replaced in x_dec (p_dec=50%) to prevent trivial copying."""
    enc_mask = set(enc_mask_indices)
    dec_mask = set(enc_mask_indices) | set(extra_dec_mask_indices)
    assert enc_mask.issubset(dec_mask)
    return len(enc_mask) / float(seq_len), len(dec_mask) / float(seq_len), enc_mask.issubset(dec_mask)


def all_position_replaced_lm_loss(true_token_probs_enc, true_token_probs_dec):
    """Eq. 2: L_pt = L_enc + L_dec where L_enc = -(1/|x|) sum_{i=1}^{|x|} log p(x[i] | x_enc) over ALL positions."""
    n_tok = len(true_token_probs_enc)
    assert len(true_token_probs_dec) == n_tok
    l_enc = -sum(math.log(p) for p in true_token_probs_enc) / float(n_tok)
    l_dec = -sum(math.log(p) for p in true_token_probs_dec) / float(n_tok)
    return l_enc, l_dec, l_enc + l_dec


def simlm_biencoder_contrastive_and_kl_loss(q_vec, d_pos_vec, neg_vecs, teacher_logits, tau=0.02, alpha=0.2):
    """Eq. 3 & Eq. 5: L_cont uses both query-negative and passage-negative scaled cosine terms phi(q+, n_i) + phi(d+, n_i); L = L_kl + alpha * L_cont."""
    def cos_sim(u, v):
        dot = sum(a * b for a, b in zip(u, v))
        nu = math.sqrt(sum(a * a for a in u))
        nv = math.sqrt(sum(b * b for b in v))
        return dot / (nu * nv)

    def phi(u, v):
        return math.exp(cos_sim(u, v) / tau)

    pos_phi = phi(q_vec, d_pos_vec)
    neg_phi_sum = sum(phi(q_vec, n_v) + phi(d_pos_vec, n_v) for n_v in neg_vecs)
    l_cont = -math.log(pos_phi / (pos_phi + neg_phi_sum))

    # Eq. 5 KL divergence between normalized teacher probabilities and student probabilities over [d+, n_1, ..., n_{m}]
    cand_vecs = [d_pos_vec] + list(neg_vecs)
    student_scores = [cos_sim(q_vec, c_v) / tau for c_v in cand_vecs]
    max_s = max(student_scores)
    exp_s = [math.exp(s - max_s) for s in student_scores]
    z_s = sum(exp_s)
    p_ret = [e / z_s for e in exp_s]

    max_t = max(teacher_logits)
    exp_t = [math.exp(t - max_t) for t in teacher_logits]
    z_t = sum(exp_t)
    p_ranker = [e / z_t for e in exp_t]

    l_kl = sum(p_r * math.log(p_r / p_s) for p_r, p_s in zip(p_ranker, p_ret))
    return l_cont, l_kl, l_kl + alpha * l_cont


def main():
    # 1. Verify Eq. 1 nested replacement rates (30% encoder, 50% decoder)
    r_enc, r_dec, is_subset = nested_electra_replacement_masks(
        seq_len=10, enc_mask_indices=[1, 4, 7], extra_dec_mask_indices=[2, 9]
    )
    assert abs(r_enc - 0.30) < 1e-9 and abs(r_dec - 0.50) < 1e-9 and is_subset

    # 2. Verify Eq. 2 all-position replaced language modeling loss
    l_enc, l_dec, l_pt = all_position_replaced_lm_loss(
        [0.9, 0.7, 0.85, 0.6, 0.95], [0.88, 0.65, 0.80, 0.55, 0.92]
    )
    assert l_enc > 0.0 and l_dec > l_enc and abs(l_pt - (l_enc + l_dec)) < 1e-12

    # 3. Verify Eq. 3 & Eq. 5 fine-tuning loss with query-negative + passage-negative terms and KL distillation
    l_cont, l_kl, l_total = simlm_biencoder_contrastive_and_kl_loss(
        q_vec=[1.0, 0.2],
        d_pos_vec=[0.98, 0.22],
        neg_vecs=[[0.94, 0.30], [0.92, 0.34]],
        teacher_logits=[5.0, 1.0, 0.5],
        tau=0.02,
        alpha=0.2,
    )
    assert l_cont > 0.0 and l_kl > 0.0 and abs(l_total - (l_kl + 0.2 * l_cont)) < 1e-12

    # 4. Verify Table 2, Table 3, Table 6, Table 7, and Table 8 benchmark and ablation invariants
    # Table 6 progression on MS-MARCO Dev MRR@10: Retriever_1 BM25 neg (38.0) < Retriever_2 mined neg (39.1) < Retriever_distill (41.1)
    assert 38.0 < 39.1 < 41.1
    # Table 2 MS-MARCO Dev MRR@10: Condenser (36.6) < RocketQA (37.0) < coCondenser (38.2) < AR2 (39.5) < ColBERTv2 (39.7) < SimLM (41.1)
    assert 36.6 < 37.0 < 38.2 < 39.5 < 39.7 < 41.1
    # Table 7 pre-training objective ablation (BM25 negatives MRR@10): AutoEncoder (32.8) < BERT_base (33.7) < Enc-Dec RTD (36.2) < MLM (36.7) < Condenser (36.9) < Enc-Dec MLM (37.7) < SimLM (38.0)
    assert 32.8 < 33.7 < 36.2 < 36.7 < 36.9 < 37.7 < 38.0
    # Table 8 extreme 100% decoder replace rate drops MRR@10 from 38.0 (30%/50%) to 36.6 (30%/100%)
    assert 36.6 < 38.0
    print("Round 756 SimLM boundary verification passed.")


if __name__ == "__main__":
    main()
