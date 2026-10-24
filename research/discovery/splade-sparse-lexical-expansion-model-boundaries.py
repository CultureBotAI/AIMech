#!/usr/bin/env python3
"""Constructed boundary verification for SPLADE (Formal, Piwowarski, & Clinchant, SIGIR 2021, arXiv:2107.05720).

Verifies:
1. Log-saturated vocabulary-space term importance aggregation (Section 3.2, Eq. 1 & Eq. 4):
   w_j = sum_{i in t} log(1 + ReLU(w_{ij})), contrasting with SparTerm's un-saturated sum
   w_j^{SparTerm} = g_j * sum_{i in t} ReLU(w_{ij}) (Eq. 2), where log(1 + ReLU(.)) prevents
   high-logit repeated tokens from dominating the representation.
2. FLOPS regularization vs. L1 regularization (Section 3.2):
   - l_FLOPS = sum_{j in V} ( (1/N) sum_{i=1}^N w_j^{(d_i)} )^2
   - l_1 = sum_{j in V} ( (1/N) sum_{i=1}^N w_j^{(d_i)} )
   Demonstrates that for two document batches with identical L1 norm, a batch where all documents
   activate the same high-frequency posting list has strictly higher l_FLOPS than a batch with
   evenly distributed posting lists, explaining why l_FLOPS yields a balanced inverted index and
   lower expected query-document FLOPS E[sum_{j in V} p_j^{(q)} p_j^{(d)}].
"""

from __future__ import annotations
import math


def sparterm_weights(token_vocab_logits: list[list[float]], gate: list[int] | None = None) -> list[float]:
    """Compute Eq. 2 SparTerm representation w_j = g_j * sum_{i in t} ReLU(w_{ij})."""
    v_size = len(token_vocab_logits[0])
    if gate is None:
        gate = [1] * v_size
    return [
        gate[j] * sum(max(0.0, token_vocab_logits[i][j]) for i in range(len(token_vocab_logits)))
        for j in range(v_size)
    ]


def splade_weights(token_vocab_logits: list[list[float]]) -> list[float]:
    """Compute Eq. 4 SPLADE representation w_j = sum_{i in t} log(1 + ReLU(w_{ij}))."""
    v_size = len(token_vocab_logits[0])
    return [
        sum(math.log(1.0 + max(0.0, token_vocab_logits[i][j])) for i in range(len(token_vocab_logits)))
        for j in range(v_size)
    ]


def l1_reg(batch_weights: list[list[float]]) -> float:
    """Compute batch-mean L1 regularization sum_{j in V} bar{a}_j."""
    n = len(batch_weights)
    v_size = len(batch_weights[0])
    return sum(sum(batch_weights[i][j] for i in range(n)) / n for j in range(v_size))


def flops_reg(batch_weights: list[list[float]]) -> float:
    """Compute Section 3.2 FLOPS regularizer l_FLOPS = sum_{j in V} bar{a}_j^2."""
    n = len(batch_weights)
    v_size = len(batch_weights[0])
    return sum((sum(batch_weights[i][j] for i in range(n)) / n) ** 2 for j in range(v_size))


def expected_posting_ops(batch_weights: list[list[float]]) -> float:
    """Compute empirical posting-list intersection cost sum_{j in V} p_j^2 where p_j is non-zero fraction."""
    n = len(batch_weights)
    v_size = len(batch_weights[0])
    return sum(
        (sum(1.0 for i in range(n) if batch_weights[i][j] > 0.0) / n) ** 2
        for j in range(v_size)
    )


def main() -> None:
    # 1. Verify log-saturation sub-additivity: a single noisy bursty logit (e.g., 20.0) vs distributed moderate logits
    logits = [
        [20.0, 2.0, -1.5, 0.0],
        [0.0, 2.0, -0.5, 1.5],
        [0.0, 2.0, -2.0, 0.0],
    ]
    w_st = sparterm_weights(logits)
    w_sp = splade_weights(logits)

    # Dimension 2 has all negative logits -> strictly 0.0 in both
    assert w_st[2] == 0.0 and w_sp[2] == 0.0
    # In SparTerm, dim 0 (20.0) dwarfs dim 1 (6.0) by > 3.3x; in SPLADE, log(1+20)=3.0445 < 3*log(1+2)=3.2958!
    assert w_st[0] > 3.0 * w_st[1]
    assert w_sp[1] > w_sp[0]

    # 2. Verify FLOPS vs L1 on skewed (Zipfian concentrated) vs balanced posting lists with identical L1
    # Skewed batch: all 4 documents put weight 2.0 into vocabulary term 0
    skewed_batch = [
        [2.0, 0.0, 0.0, 0.0],
        [2.0, 0.0, 0.0, 0.0],
        [2.0, 0.0, 0.0, 0.0],
        [2.0, 0.0, 0.0, 0.0],
    ]
    # Balanced batch: each of the 4 documents puts weight 2.0 into a distinct vocabulary term
    balanced_batch = [
        [2.0, 0.0, 0.0, 0.0],
        [0.0, 2.0, 0.0, 0.0],
        [0.0, 0.0, 2.0, 0.0],
        [0.0, 0.0, 0.0, 2.0],
    ]

    assert abs(l1_reg(skewed_batch) - l1_reg(balanced_batch)) < 1e-12
    assert flops_reg(skewed_batch) == 4.0 * flops_reg(balanced_batch)
    assert expected_posting_ops(skewed_batch) == 4.0 * expected_posting_ops(balanced_batch)

    print(
        "SPLADE boundary verification passed:",
        {"flops_skewed": flops_reg(skewed_batch), "flops_balanced": flops_reg(balanced_batch)},
    )


if __name__ == "__main__":
    main()
