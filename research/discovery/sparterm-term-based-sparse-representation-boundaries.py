#!/usr/bin/env python3
"""Constructed boundary verification for SparTerm (Bai et al., 2020, arXiv:2010.00768).

Verifies:
1. Factored sparse mapping p' = F(p) * G(p) in R^v (Section 3.1, Eq. 1) where:
   - Importance predictor F(p) = I = sum_{i=0}^L ReLU(Transform(h_i) E^T + b) >= 0 (Eqs. 2-3).
   - Literal-only gating G(p) = BoW(p) in {0, 1}^v.
   - Expansion-enhanced gating G_{le} = (Binarizer(G) & ~BoW(p)) + BoW(p) in {0, 1}^v (Eqs. 4-6),
     guaranteeing that literal terms are always active and expansion terms are orthogonal to literal terms.
2. Weighted binary cross-entropy expansion loss L_exp = -lambda_1 sum_{T_j=0} log(1 - G_j) - lambda_2 sum_{T_k=1} log(G_k)
   (Eq. 8) and pairwise ranking NLL loss L_rank (Eq. 7).
"""

from __future__ import annotations

import math


def relu(x: float) -> float:
    return max(0.0, x)


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def dot(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def importance_predictor(
    token_hidden: list[list[float]],
    vocab_embs: list[list[float]],
    bias: list[float],
) -> list[float]:
    """Implements Eqs. (2)-(3): I_i = h_i E^T + b, I = sum_{i=0}^L ReLU(I_i)."""
    v = len(vocab_embs)
    imp = [0.0] * v
    for h_i in token_hidden:
        for term_idx in range(v):
            logit_ij = dot(h_i, vocab_embs[term_idx]) + bias[term_idx]
            imp[term_idx] += relu(logit_ij)
    return imp


def expansion_enhanced_gating(
    gating_probs: list[float],
    bow_vec: list[int],
    threshold: float = 0.7,
) -> tuple[list[int], list[int]]:
    """Implements Eqs. (4)-(6): G' = Binarizer(G), G_e = G' & (~BoW(p)), G_le = G_e + BoW(p)."""
    assert len(gating_probs) == len(bow_vec)
    g_prime = [1 if p >= threshold else 0 for p in gating_probs]
    g_exp = [gp * (1 - b) for gp, b in zip(g_prime, bow_vec)]
    g_le = [ge + b for ge, b in zip(g_exp, bow_vec)]
    # Verify orthogonality of G_e and BoW(p) and binary range {0, 1}:
    for ge, b, gle in zip(g_exp, bow_vec, g_le):
        assert ge * b == 0
        assert gle in (0, 1)
        if b == 1:
            assert gle == 1
    return g_exp, g_le


def sparterm_representation(importance: list[float], gate: list[int]) -> list[float]:
    """Implements Eq. (1): p' = F(p) odot G(p)."""
    return [imp_j * float(g_j) for imp_j, g_j in zip(importance, gate)]


def expansion_bce_loss(
    gating_probs: list[float],
    target_bow: list[int],
    lambda_1: float = 1e-3,
    lambda_2: float = 1.0,
) -> float:
    """Implements Eq. (8): L_exp = -lambda_1 sum_{T_j=0} log(1 - G_j) - lambda_2 sum_{T_k=1} log(G_k)."""
    loss = 0.0
    for g_j, t_j in zip(gating_probs, target_bow):
        g_clipped = min(max(g_j, 1e-9), 1.0 - 1e-9)
        if t_j == 0:
            loss += -lambda_1 * math.log(1.0 - g_clipped)
        else:
            loss += -lambda_2 * math.log(g_clipped)
    return loss


def ranking_nll_loss(q_rep: list[float], p_pos_rep: list[float], p_neg_rep: list[float]) -> float:
    """Implements Eq. (7): -log(exp(sim(q', p'+)) / (exp(sim(q', p'+)) + exp(sim(q', p'-))))."""
    s_pos = dot(q_rep, p_pos_rep)
    s_neg = dot(q_rep, p_neg_rep)
    m = max(s_pos, s_neg)
    return -math.log(math.exp(s_pos - m) / (math.exp(s_pos - m) + math.exp(s_neg - m)))


def main() -> None:
    # Vocabulary of size v = 6:
    # 0="hives", 1="allergic", 2="pregnancy", 3="sign", 4="symptoms", 5="football"
    # Passage p contains literal terms {0="hives", 1="allergic", 2="pregnancy"} (Figure 1):
    bow_p = [1, 1, 1, 0, 0, 0]
    # Query q asks "Can hives be a sign of pregnancy?" -> terms {0="hives", 2="pregnancy", 3="sign"}:
    q_rep = [1.0, 0.0, 1.2, 1.5, 0.0, 0.0]

    vocab_embs = [
        [1.0, 0.2, 0.1],  # 0: hives
        [0.8, 0.3, 0.1],  # 1: allergic
        [0.3, 1.0, 0.2],  # 2: pregnancy
        [0.4, 0.9, 0.3],  # 3: sign (expansion term!)
        [0.5, 0.8, 0.2],  # 4: symptoms (expansion term!)
        [-0.5, -0.5, 0.9],  # 5: football (unrelated)
    ]
    bias = [0.1, 0.1, 0.1, 0.05, 0.05, -0.4]

    p_pos_hidden = [[0.9, 0.4, 0.1], [0.7, 0.5, 0.1], [0.4, 0.9, 0.2]]
    p_neg_hidden = [[-0.2, -0.2, 0.8], [-0.3, -0.1, 0.9]]

    imp_pos = importance_predictor(p_pos_hidden, vocab_embs, bias)
    imp_neg = importance_predictor(p_neg_hidden, vocab_embs, bias)

    # Gating probabilities G for passage p_pos (threshold = 0.7, Section 4.2):
    # Terms 3 ("sign", prob=0.91) and 4 ("symptoms", prob=1.00) exceed 0.7 and get expanded!
    g_probs_pos = [0.95, 0.88, 0.96, 0.91, 0.99, 0.02]
    g_exp_pos, g_le_pos = expansion_enhanced_gating(g_probs_pos, bow_p, threshold=0.7)
    assert g_exp_pos == [0, 0, 0, 1, 1, 0]
    assert g_le_pos == [1, 1, 1, 1, 1, 0]

    # Compare literal-only vs expansion-enhanced representations on query matching "sign":
    p_pos_literal = sparterm_representation(imp_pos, bow_p)
    p_pos_expanded = sparterm_representation(imp_pos, g_le_pos)
    p_neg_expanded = sparterm_representation(imp_neg, [0, 0, 0, 0, 0, 1])

    score_literal = dot(q_rep, p_pos_literal)
    score_expanded = dot(q_rep, p_pos_expanded)
    score_neg = dot(q_rep, p_neg_expanded)
    assert score_expanded > score_literal > score_neg

    l_rank = ranking_nll_loss(q_rep, p_pos_expanded, p_neg_expanded)
    l_exp = expansion_bce_loss(g_probs_pos, [1, 0, 1, 1, 1, 0], lambda_1=1e-3, lambda_2=1.0)
    assert l_rank < 0.01 and l_exp > 0.0

    print(
        f"[PASS] SparTerm boundaries verified: score_literal={score_literal:.4f} < score_expanded={score_expanded:.4f} "
        f"(> score_neg={score_neg:.4f}), L_rank={l_rank:.6f}, L_exp={l_exp:.4f}"
    )


if __name__ == "__main__":
    main()
