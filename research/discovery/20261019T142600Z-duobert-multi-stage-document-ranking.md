# Discovery Report: Round 783 — monoBERT and duoBERT Multi-Stage Document Ranking

- **Timestamp**: `2026-10-19T14:26:00Z`
- **Selected Concept**: `AIMech:DuoBERTMultiStageDocumentRankingWithBERT` (*monoBERT and duoBERT Multi-Stage Document Ranking*)
- **Record Path**: `data/curated/DuoBERTMultiStageDocumentRankingWithBERT.yaml`
- **Primary Source**: Rodrigo Nogueira, Wei Yang, Kyunghyun Cho, Jimmy Lin — *Multi-Stage Document Ranking with BERT* (`https://arxiv.org/bibtex/1910.14424`).

## Identity & Boundary Resolution

Distinct from listwise cross-encoder fusion architectures such as HLATR (AIMech:HLATRHybridListAwareTransformerReranking), which model cross-document interactions over pre-computed pointwise [CLS] vectors in a single listwise Transformer pass rather than running k_1(k_1 - 1) full BERT forward passes over concatenated (q, d_i, d_j) token triples; and distinct from CEDR (AIMech:CEDRContextualizedEmbeddingsForDocumentRanking), which is a single-stage pointwise re-ranker fusing multi-layer token similarity matrices with [CLS].

## Constructed Boundary & Regime Verification

```text
[PASS] DuoBERT boundaries verified: sum_1=2.74 > sum_0=1.90, bin_1=3 > bin_0=2, max_0=0.98 > max_1=0.94, L_duo=0.5462
```
