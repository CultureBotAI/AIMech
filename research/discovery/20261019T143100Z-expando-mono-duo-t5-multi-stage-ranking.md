# Discovery Report: Round 788 — Expando-Mono-Duo: Multi-Stage Text Ranking with Pretrained Sequence-to-Sequence Models

- **Timestamp**: `2026-10-19T14:31:00Z`
- **Selected Concept**: `AIMech:ExpandoMonoDuoT5MultiStageDocumentRanking` (*Expando-Mono-Duo: Multi-Stage Text Ranking with Pretrained Sequence-to-Sequence Models*)
- **Record Path**: `data/curated/ExpandoMonoDuoT5MultiStageDocumentRanking.yaml`
- **Primary Source**: Ronak Pradeep, Rodrigo Nogueira, Jimmy Lin — *The Expando-Mono-Duo Design Pattern for Text Ranking with Pretrained Sequence-to-Sequence Models* (`https://arxiv.org/bibtex/2101.05667`).

## Identity & Boundary Resolution

Distinct from standalone pointwise MonoT5 (AIMech:MonoT5DocumentRankingWithPretrainedSeq2SeqModels) and encoder-only BERT cascade DuoBERT (AIMech:DuoBERTMultiStageDocumentRankingWithBERT). Expando-Mono-Duo unifies pre-indexing sequence-to-sequence expansion (H_-1) with pointwise (H_1) and pairwise (H_2) sequence-to-sequence T5 reranking, introducing duoT5 on prompt 'Query: q Document0: d_i Document1: d_j Relevant:' with relative positional encoding extension to 1,024 tokens and symmetric log/probability pairwise aggregation (SYM-SUM-LOG, Eq. 8).

## Constructed Boundary & Regime Verification

```text
Expando-Mono-Duo T5 boundary verification passed:
  DuoT5 inferences for k1=50: 2450
  SUM scores:         [1.35, 1.38, 0.78]
  SYM-SUM scores:     [2.79, 2.13, 1.08]
  SYM-SUM-LOG scores: [-1.5583, -2.8418, -6.7944]
```
