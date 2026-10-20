# Discovery Report: Round 740 — Promptagator Few-Shot Dense Retrieval

- **Timestamp**: `2026-10-19T13:43:00Z`
- **Selected Concept**: `AIMech:PromptagatorFewShotDenseRetrievalDataGeneration` (*Promptagator Few-Shot Dense Retrieval*)
- **Record Path**: `data/curated/PromptagatorFewShotDenseRetrievalDataGeneration.yaml`
- **Primary Source**: Zhuyun Dai, Vincent Y. Zhao, Ji Ma, Yi Luan, Jianmo Ni, Jing Lu, Anton Bakalov, Kelvin Guu, Keith B. Hall, Ming-Wei Chang — *Promptagator: Few-shot Dense Retrieval From 8 Examples* (`https://dblp.org/search/publ/api?q=Promptagator+Few-shot+Dense+Retrieval+From+8+Examples+Dai&h=5&format=xml`).

## Identity & Boundary Resolution

Distinct from InPars (AIMech:InParsInContextDataAugmentationForInformationRetrieval), which filters synthetic queries by length-normalized generation log-probability and trains only a second-stage cross-encoder reranker over BM25 candidates, whereas Promptagator conditions on task-specific search-intent role prefixes (e.g., counter-argument vs. fact-check claim), performs round-trip retrieval consistency filtering using a self-trained initial dual encoder without external QA models, and produces a standalone first-stage dense dual encoder. Also distinct from zero-shot hypothetical document embedding at query time (AIMech:HyDEHypotheticalDocumentEmbeddings), which calls an LLM online for every test query rather than distilling synthetic queries offline into a fast 110M dual encoder.

## Constructed Boundary & Regime Verification

```text
Promptagator verification passed: unfiltered=12 (sim=0.6896) -> filtered=8 (sim=0.9557)
```
