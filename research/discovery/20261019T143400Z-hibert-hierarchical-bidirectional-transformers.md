# Discovery Report: Round 791 — HIBERT (Hierarchical Bidirectional Transformers for Document Summarization)

- **Timestamp**: `2026-10-19T14:34:00Z`
- **Selected Concept**: `AIMech:HIBERTHierarchicalBidirectionalTransformersForDocumentSummarization` (*HIBERT (Hierarchical Bidirectional Transformers for Document Summarization)*)
- **Record Path**: `data/curated/HIBERTHierarchicalBidirectionalTransformersForDocumentSummarization.yaml`
- **Primary Source**: Xingxing Zhang, Furu Wei, Ming Zhou — *HIBERT: Document Level Pre-training of Hierarchical Bidirectional Transformers for Document Summarization* (`https://arxiv.org/bibtex/1905.06566`).

## Identity & Boundary Resolution

Distinct from flat BERT/RoBERTa encoders (which concatenate tokens into a single sequence and pre-train with token-level MLM and next-sentence prediction) and from SMITH (AIMech:SMITHSiameseMultiDepthTransformerBasedHierarchicalEncoder, which replaces autoregressive masked-sentence decoding with masked sentence-block projection classification in a Siamese dual-encoder retrieval architecture). HIBERT pre-trains a two-level hierarchical Transformer encoder by masking 15% of sentences (80% all-[MASK] tokens, 10% unchanged, 10% random sentence replacement) and predicting each masked sentence word-by-word via an auxiliary Transformer decoder that injects the context-sensitive sentence representation d_tilde_k into the two-layer feed-forward network after multi-head self-attention.

## Constructed Boundary & Regime Verification

```text
HIBERT boundary verification passed:
  Masked sentence 1:   ['[MASK]', '[MASK]', '[MASK]', '[MASK]', '[MASK]']
  Replaced sentence 1: ['Birds', 'can', 'fly', '.']
  P(target word | d_tilde_k)=0.9985 > P(target word | 0)=0.4803
```
