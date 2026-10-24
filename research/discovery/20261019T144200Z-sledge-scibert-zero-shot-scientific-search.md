# Discovery Report: Round 799 — SLEDGE (SciBERT Zero-Shot Domain-Transfer Scientific Literature Search)

- **Timestamp**: `2026-10-19T14:42:00Z`
- **Selected Concept**: `AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch` (*SLEDGE (SciBERT Zero-Shot Domain-Transfer Scientific Literature Search)*)
- **Record Path**: `data/curated/SLEDGESciBERTZeroShotScientificLiteratureSearch.yaml`
- **Primary Source**: Sean MacAvaney, Arman Cohan, Nazli Goharian — *SLEDGE: A Simple Yet Effective Baseline for COVID-19 Scientific Knowledge Search* (`https://arxiv.org/bibtex/2005.02365`).

## Identity & Boundary Resolution

Distinct from general-domain BERT passage rerankers (Nogueira & Cho, 2019) and from CEDR (AIMech:CEDRContextualizedEmbeddingsForDocumentRanking). SLEDGE bridges emerging scientific domains lacking in-domain relevance judgments by pairing a scientific pre-trained language model (SciBERT) with out-of-domain relevance supervision transferred from MS MARCO (or lexicon-filtered Med-MSMARCO via the MedSyn layperson medical lexicon) and asymmetric field routing (searching full text with keyword queries or natural-language questions in Stage 1 while re-ranking title+abstract with natural-language questions in Stage 2).

## Constructed Boundary & Regime Verification

```text
SLEDGE boundary verification passed:
  Tuned BM25 repetition gain ratio: 2.1770 > default 1.4048
  Pairwise CE loss: good=0.1668 < bad=1.1957
  Med-MSMARCO filtered query IDs: [1, 3]
```
