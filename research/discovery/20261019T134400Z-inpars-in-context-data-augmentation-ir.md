# Discovery Report: Round 741 — InPars In-Context Data Augmentation for Information Retrieval

- **Timestamp**: `2026-10-19T13:44:00Z`
- **Selected Concept**: `AIMech:InParsInContextDataAugmentationForInformationRetrieval` (*InPars In-Context Data Augmentation for Information Retrieval*)
- **Record Path**: `data/curated/InParsInContextDataAugmentationForInformationRetrieval.yaml`
- **Primary Source**: Luiz Bonifacio, Hugo Abonizio, Marzieh Fadaee, Rodrigo Nogueira — *InPars: Data Augmentation for Information Retrieval using Large Language Models* (`https://dblp.org/search/publ/api?q=InPars+Data+Augmentation+for+Information+Retrieval+Bonifacio&h=5&format=xml`).

## Identity & Boundary Resolution

Distinct from Promptagator (AIMech:PromptagatorFewShotDenseRetrievalDataGeneration), which filters synthetic pairs via round-trip top-1 retrieval consistency using an initial dual encoder and trains a first-stage dense dual encoder, whereas InPars filters synthetic pairs directly by their length-normalized autoregressive generation log-probability p_q under the generator LM and trains a monoT5 sequence-to-sequence reranker over BM25 candidates.

## Constructed Boundary & Regime Verification

```text
InPars verification passed: topK_ids=[2, 0, 1], mean_quality_all=0.578 -> mean_quality_topK=0.940
```
