#!/usr/bin/env python3
"""Constructed boundary verification for UPR (Sachan et al., EMNLP 2022, arXiv:2204.07496).

Verifies:
1. Bayes' rule decomposition with uniform passage prior (Section 2.2):
   log p(z_i | q) = log p(q | z_i) + log p(z_i) + c, which under a uniform prior
   log p(z_i) = const reduces to ranking passages strictly by log p(q | z_i).
2. Length-normalized zero-shot question generation score (Section 2.2):
   s_UPR(z_i, q) = (1 / |q|) * sum_{t=1}^{|q|} log p(q_t | q_{<t}, z_i; Theta).
3. Boundary contrast against lexical overlap (BM25-like) and passage-generation likelihood
   log p(z_i | q) (Section 4.2.1): a distractor passage with high background token probability
   or lexical repetition can score higher under unnormalized p(z_i | q) or lexical overlap,
   whereas UPR's conditional question likelihood p(q | z_i) ranks the answer-bearing passage first.
"""

from __future__ import annotations
import math


def upr_question_log_likelihood(question_token_probs_given_passage: list[float]) -> float:
    """Compute (1 / |q|) sum_{t=1}^{|q|} log p(q_t | q_{<t}, z_i; Theta)."""
    assert len(question_token_probs_given_passage) > 0
    return sum(math.log(p) for p in question_token_probs_given_passage) / len(
        question_token_probs_given_passage
    )


def passage_generation_log_likelihood(passage_token_probs_given_question: list[float]) -> float:
    """Compute (1 / |z_i|) sum_{t=1}^{|z_i|} log p(z_{i,t} | z_{i,<t}, q; Theta) (Section 4.2.1 ablation)."""
    assert len(passage_token_probs_given_question) > 0
    return sum(math.log(p) for p in passage_token_probs_given_question) / len(
        passage_token_probs_given_question
    )


def main() -> None:
    # Candidate passage z_1: lexical distractor (high first-stage BM25 score and generic fluent passage tokens,
    # but low probability of generating the specific question tokens).
    # Candidate passage z_2: ground-truth answer-bearing passage (lower first-stage BM25 score,
    # but high conditional probability of generating every token in the input question q).
    first_stage_bm25 = {"z1_distractor": 14.2, "z2_answer": 11.8}

    # Conditional token probabilities p(q_t | q_{<t}, z_i; Theta) for |q| = 5 tokens
    q_given_z = {
        "z1_distractor": [0.15, 0.08, 0.04, 0.05, 0.10],
        "z2_answer": [0.45, 0.52, 0.38, 0.60, 0.50],
    }

    # Ablation (Section 4.2.1): conditional passage token probabilities p(z_{i,t} | z_{i,<t}, q; Theta)
    # where z1_distractor consists of high-frequency boilerplate tokens and z2_answer has rare entity tokens.
    z_given_q = {
        "z1_distractor": [0.40, 0.35, 0.42, 0.38, 0.45, 0.41],
        "z2_answer": [0.12, 0.09, 0.25, 0.18, 0.14, 0.20],
    }

    upr_scores = {k: upr_question_log_likelihood(v) for k, v in q_given_z.items()}
    pgen_scores = {k: passage_generation_log_likelihood(v) for k, v in z_given_q.items()}

    # 1. Verify Bayes' rule rank equivalence under uniform prior log p(z_i) = log(1/K)
    k_candidates = 2
    uniform_prior = math.log(1.0 / k_candidates)
    norm_const = -1.2345
    posterior_z1 = len(q_given_z["z1_distractor"]) * upr_scores["z1_distractor"] + uniform_prior + norm_const
    posterior_z2 = len(q_given_z["z2_answer"]) * upr_scores["z2_answer"] + uniform_prior + norm_const
    assert (posterior_z2 - posterior_z1) == len(q_given_z["z2_answer"]) * (
        upr_scores["z2_answer"] - upr_scores["z1_distractor"]
    )

    # 2. Verify first-stage BM25 and passage-generation ablation p(z|q) both rank distractor z1 > z2
    assert first_stage_bm25["z1_distractor"] > first_stage_bm25["z2_answer"]
    assert pgen_scores["z1_distractor"] > pgen_scores["z2_answer"]

    # 3. Verify UPR question-generation re-ranking flips the ordering so answer passage z2 > z1
    assert upr_scores["z2_answer"] > upr_scores["z1_distractor"]

    print(
        "UPR boundary verification passed:",
        {"upr_z2": round(upr_scores["z2_answer"], 4), "upr_z1": round(upr_scores["z1_distractor"], 4)},
    )


if __name__ == "__main__":
    main()
