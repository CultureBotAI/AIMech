# Discovery Report: Round 773 — Doc2query Neural Document Expansion by Query Prediction

- **Timestamp**: `2026-10-19T14:16:00Z`
- **Selected Concept**: `AIMech:Doc2QueryDocumentExpansionByQueryPrediction` (*Doc2query Neural Document Expansion by Query Prediction*)
- **Record Path**: `data/curated/Doc2QueryDocumentExpansionByQueryPrediction.yaml`
- **Primary Source**: Rodrigo Nogueira, Wei Yang, Jimmy Lin, Kyunghyun Cho — *Document Expansion by Query Prediction* (`https://arxiv.org/bibtex/1904.08375`).

## Identity & Boundary Resolution

Distinct from query-side generation expansion methods such as GAR (AIMech:GARGenerationAugmentedRetrievalForOpenDomainQA) and HyDE (AIMech:HyDEHypotheticalDocumentEmbeddings), which generate expansion contexts from the input query at retrieval time rather than expanding corpus documents offline prior to inverted-index construction; and distinct from DeepCT (AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval), which regresses integer term frequencies for existing document tokens without generating new vocabulary terms not present in the document.

## Constructed Boundary & Regime Verification

```text
[PASS] Doc2query boundaries verified: orig=1.5000 < copied=2.4012, new=4.9888 < full=5.6571 (> distractor=4.4625)
```
