# Discovery Report: Round 742 — HyDE Hypothetical Document Embeddings

- **Timestamp**: `2026-10-19T13:45:00Z`
- **Selected Concept**: `AIMech:HyDEHypotheticalDocumentEmbeddings` (*HyDE Hypothetical Document Embeddings*)
- **Record Path**: `data/curated/HyDEHypotheticalDocumentEmbeddings.yaml`
- **Primary Source**: Luyu Gao, Xueguang Ma, Jimmy Lin, Jamie Callan — *Precise Zero-Shot Dense Retrieval without Relevance Labels* (`https://dblp.org/search/publ/api?q=Precise+Zero-Shot+Dense+Retrieval+without+Relevance+Labels+Gao&h=5&format=xml`).

## Identity & Boundary Resolution

Distinct from document-to-query data augmentation methods such as Promptagator (AIMech:PromptagatorFewShotDenseRetrievalDataGeneration) and InPars (AIMech:InParsInContextDataAugmentationForInformationRetrieval), which generate synthetic queries from real documents offline to train retrievers or rerankers, whereas HyDE requires no model training or corpus access beforehand and instead translates each incoming query online into hypothetical documents so that retrieval occurs purely in an unsupervised document-document contrastive embedding space.

## Constructed Boundary & Regime Verification

```text
HyDE verification passed: raw_margin=-0.3771 -> hyde_margin=0.3170, hyde8_scores=[0.7954, 0.4784, 0.2244]
```
