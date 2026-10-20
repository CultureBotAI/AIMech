# Discovery Report: Round 781 — CEDR Contextualized Embeddings for Document Ranking

- **Timestamp**: `2026-10-19T14:24:00Z`
- **Selected Concept**: `AIMech:CEDRContextualizedEmbeddingsForDocumentRanking` (*CEDR Contextualized Embeddings for Document Ranking*)
- **Record Path**: `data/curated/CEDRContextualizedEmbeddingsForDocumentRanking.yaml`
- **Primary Source**: Sean MacAvaney, Andrew Yates, Arman Cohan, Nazli Goharian — *CEDR: Contextualized Embeddings for Document Ranking* (`https://arxiv.org/bibtex/1904.07094`).

## Identity & Boundary Resolution

Distinct from Vanilla BERT cross-encoder re-rankers, which predict relevance solely from a linear projection of the final-layer [CLS] vector without computing token-to-token cosine similarity matrices or soft term-counting kernels across intermediate layers; and distinct from static-embedding interaction rankers (KNRM, PACRR, DRMM with GloVe/Word2Vec), where identical surface words always receive cosine similarity 1.0 regardless of polysemous context.

## Constructed Boundary & Regime Verification

```text
[PASS] CEDR boundaries verified: sim_curb_pos=0.9969 > sim_curb_neg=0.0514, cedr_margin=35.2568 > non_cedr_margin=33.7618
```
