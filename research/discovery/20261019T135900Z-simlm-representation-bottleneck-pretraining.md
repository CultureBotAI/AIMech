# Discovery Report: Round 756 — SimLM Representation-Bottleneck Replaced Language Model Pre-Training

- **Timestamp**: `2026-10-19T13:59:00Z`
- **Selected Concept**: `AIMech:SimLMRepresentationBottleneckPreTraining` (*SimLM Representation-Bottleneck Replaced Language Model Pre-Training*)
- **Record Path**: `data/curated/SimLMRepresentationBottleneckPreTraining.yaml`
- **Primary Source**: Liang Wang, Nan Yang, Xiaolong Huang, Binxing Jiao, Linjun Yang, Daxin Jiang, Rangan Majumder, Furu Wei — *SimLM: Pre-training with Representation Bottleneck for Dense Passage Retrieval* (`https://arxiv.org/bibtex/2207.02578`).

## Identity & Boundary Resolution

Distinct from Condenser (AIMech:CondenserPreTrainingArchitectureForDenseRetrieval) and coCondenser (AIMech:CoCondenserUnsupervisedCorpusAwareLanguageModelPreTraining), which include a short-circuit skip connection from early encoder layers to the head and use [MASK]-based MLM; distinct from RetroMAE (AIMech:RetroMAERetrievalOrientedMaskedAutoEncoder), which uses [MASK] tokens and specialized position-specific attention masks in a 1-layer decoder; and distinct from ELECTRA (AIMech:ELECTRAReplacedTokenDetection), which trains a binary Replaced Token Detection (RTD) discriminator without a [CLS] bottleneck decoder (and performs poorly on dense retrieval: 31.9 vs. 33.7 MRR@10 in Table 1 and 36.2 vs. 38.0 in Table 7).

## Constructed Boundary & Regime Verification

```text
Round 756 SimLM boundary verification passed.
```
