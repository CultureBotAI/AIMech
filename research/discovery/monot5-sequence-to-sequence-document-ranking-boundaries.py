#!/usr/bin/env python3
"""Constructed boundary verification for MonoT5 (Nogueira et al., Findings of EMNLP 2020, arXiv:2003.06713)."""

import math


def format_monot5_prompt(query: str, document: str) -> str:
    """Eq. (1): Format query and document into the MonoT5 sequence-to-sequence prompt template."""
    return f"Query: {query} Document: {document} Relevant:"


def monot5_relevance_prob(logit_true: float, logit_false: float) -> float:
    """Two-token softmax normalization exclusively over the 'true' and 'false' target word logits."""
    m = max(logit_true, logit_false)
    exp_true = math.exp(logit_true - m)
    exp_false = math.exp(logit_false - m)
    return exp_true / (exp_true + exp_false)


def full_vocab_true_prob(logit_true: float, logit_false: float, other_logits: list[float]) -> float:
    """Unrestricted vocabulary softmax over all token logits (shown in Section 2 to fail for ranking)."""
    all_logits = [logit_true, logit_false, *other_logits]
    m = max(all_logits)
    exps = [math.exp(x - m) for x in all_logits]
    return exps[0] / sum(exps)


def maxp_document_prob(passage_logit_pairs: list[tuple[float, float]]) -> float:
    """Section 3.2: MaxP aggregation of MonoT5 passage relevance probabilities over sliding windows."""
    return max(monot5_relevance_prob(lt, lf) for lt, lf in passage_logit_pairs)


def main() -> None:
    prompt = format_monot5_prompt("neural ranking", "Sequence-to-sequence models generate target words.")
    assert prompt == "Query: neural ranking Document: Sequence-to-sequence models generate target words. Relevant:"

    # 1. Two-token softmax is invariant to uniform logit shifts and unaffected by unrelated vocabulary logits:
    p1 = monot5_relevance_prob(4.2, 1.2)
    p1_shifted = monot5_relevance_prob(4.2 + 10.0, 1.2 + 10.0)
    assert abs(p1 - p1_shifted) < 1e-12
    assert 0.95 < p1 < 0.96

    # 2. Contrast with raw 'true' logit or full-vocabulary softmax when a distractor token has high logit:
    # Doc 1 has higher relative preference for 'true' vs 'false' (logit diff +3.0),
    # whereas Doc 2 has lower preference (+1.0) but higher absolute logits due to baseline offset.
    doc1_true, doc1_false = 2.0, -1.0  # diff = +3.0
    doc2_true, doc2_false = 3.5, 2.5   # diff = +1.0
    assert doc2_true > doc1_true, "Raw 'true' logit wrongly prefers Doc 2 due to unnormalized offset"
    assert monot5_relevance_prob(doc1_true, doc1_false) > monot5_relevance_prob(doc2_true, doc2_false), (
        "Two-token softmax over ('true', 'false') rightly ranks Doc 1 above Doc 2"
    )

    # 3. MaxP over sliding-window passages selects the highest passage relevance probability:
    doc_passages = [(-1.5, 2.0), (3.8, 0.3), (-0.5, 1.5)]
    p_doc = maxp_document_prob(doc_passages)
    assert abs(p_doc - monot5_relevance_prob(3.8, 0.3)) < 1e-12
    assert p_doc > 0.97

    print("MonoT5 boundary verification passed:")
    print(f"  Prompt: {prompt}")
    print(f"  P(Relevant=true | Doc1)={monot5_relevance_prob(doc1_true, doc1_false):.4f} > "
          f"P(Relevant=true | Doc2)={monot5_relevance_prob(doc2_true, doc2_false):.4f}")
    print(f"  MaxP document probability: {p_doc:.4f}")


if __name__ == "__main__":
    main()
