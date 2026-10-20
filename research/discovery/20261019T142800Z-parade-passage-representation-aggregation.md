# Discovery Report: Round 785 — PARADE: Passage Representation Aggregation for Document Reranking

- **Timestamp**: `2026-10-19T14:28:00Z`
- **Selected Concept**: `AIMech:PARADEPassageRepresentationAggregationForDocumentReranking` (*PARADE: Passage Representation Aggregation for Document Reranking*)
- **Record Path**: `data/curated/PARADEPassageRepresentationAggregationForDocumentReranking.yaml`
- **Primary Source**: Canjia Li, Andrew Yates, Sean MacAvaney, Ben He, Yingfei Sun — *PARADE: Passage Representation Aggregation for Document Reranking* (`https://arxiv.org/bibtex/2008.09093`).

## Identity & Boundary Resolution

Distinct from passage score aggregation methods such as BERT-MaxP and Birch (which collapse each passage representation p_i^cls into a scalar relevance score s_i before pooling across passages) and from CEDR (which averages token/CLS similarity matrices into kernel-pooling neural rankers). PARADE aggregates the high-dimensional passage [CLS] representation vectors themselves via hierarchical Transformer or CNN layers and supports logit-level MSE knowledge distillation L = alpha * L_CE + (1 - alpha) * ||z^t - z^s||^2 into compact student backbones.

## Constructed Boundary & Regime Verification

```text
PARADE boundary verification passed:
  Score-MaxP:          broad=2.3000 < single=2.4000
  PARADE-Max:          broad=4.2200 > single=2.4000
  PARADE-Transformer:  broad=8.4527 > single=7.7724
  Distill loss:        match=0.0243 < mismatch=3.3620
```
