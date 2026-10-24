# Discovery Report: Round 795 — DC-BERT (Decoupling Question and Document for Efficient Contextual Encoding)

- **Timestamp**: `2026-10-19T14:38:00Z`
- **Selected Concept**: `AIMech:DCBERTDecouplingQuestionAndDocumentForEfficientContextualEncoding` (*DC-BERT (Decoupling Question and Document for Efficient Contextual Encoding)*)
- **Record Path**: `data/curated/DCBERTDecouplingQuestionAndDocumentForEfficientContextualEncoding.yaml`
- **Primary Source**: Yuyu Zhang, Ping Nie, Xiubo Geng, Arun Ramamurthy, Le Song, Daxin Jiang — *DC-BERT: Decoupling Question and Document for Efficient Contextual Encoding* (`https://arxiv.org/bibtex/2002.12591`).

## Identity & Boundary Resolution

Distinct from MORES (AIMech:MORESModularizedTransformerBasedRankingFramework, which uses asymmetric query-to-document cross-attention Interaction Blocks leaving D unchanged) and from TwinBERT (AIMech:TwinBERTDistillingKnowledgeToTwinStructuredBERTModels, which pools each tower into a single vector before a cosine or max-residual crossing layer). DC-BERT retains token-level encodings T and T' from the dual BERT encoders, re-indexes their concatenation with trainable global position embeddings E_{P_i} and type embeddings E_Q, E_D initialized from pre-trained BERT, passes the sequence through K configurable upper Transformer layers (initialized from the last K layers of BERT), and concatenates both [CLS] outputs [o_[CLS]; o'_[CLS]] for binary reranking.

## Constructed Boundary & Regime Verification

```text
DC-BERT boundary verification passed:
  Combined sequence length: 10, p(Q, D) = 0.8281
  PBT@N = 50.0%, PTB@N = 25.0%
```
