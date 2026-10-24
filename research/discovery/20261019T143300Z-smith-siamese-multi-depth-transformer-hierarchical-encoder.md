# Discovery Report: Round 790 — SMITH: Siamese Multi-depth Transformer-based Hierarchical Encoder for Long-Form Document Matching

- **Timestamp**: `2026-10-19T14:33:00Z`
- **Selected Concept**: `AIMech:SMITHSiameseMultiDepthTransformerBasedHierarchicalEncoder` (*SMITH: Siamese Multi-depth Transformer-based Hierarchical Encoder for Long-Form Document Matching*)
- **Record Path**: `data/curated/SMITHSiameseMultiDepthTransformerBasedHierarchicalEncoder.yaml`
- **Primary Source**: Liu Yang, Mingyang Zhang, Cheng Li, Michael Bendersky, Marc Najork — *Beyond 512 Tokens: Siamese Multi-depth Transformer-based Hierarchical Encoder for Long-Form Document Matching* (`https://arxiv.org/bibtex/2004.12297`).

## Identity & Boundary Resolution

Distinct from cross-encoder passage aggregation rankers such as PARADE (AIMech:PARADEPassageRepresentationAggregationForDocumentReranking, which jointly encodes query-passage pairs) and from RNN-based hierarchical document matchers such as HAN and SMASH RNN. SMITH is a representation-focused Siamese dual encoder supporting offline vector indexing up to 2,048 tokens, reducing self-attention memory complexity from O(b * A * L * N^2) to O(b * A * L * (L_s * N + (N / L_s)^2)) via greedy sentence filling and two-level Transformers.

## Constructed Boundary & Regime Verification

```text
SMITH boundary verification passed:
  Greedy blocks=3 (pad=5) vs Naive blocks=5 (pad=21)
  Attention ops (N=2048, L_s=32): full=4194304 vs SMITH=69632 (60.2x reduction)
  Masked sentence block loss: aligned=0.1525 < swapped=1.7525
```
