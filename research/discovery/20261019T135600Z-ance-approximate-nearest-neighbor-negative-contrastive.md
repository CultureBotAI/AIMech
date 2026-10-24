# Discovery Report: Round 753 — ANCE Approximate Nearest Neighbor Negative Contrastive Learning

- **Timestamp**: `2026-10-19T13:56:00Z`
- **Selected Concept**: `AIMech:ANCEApproximateNearestNeighborNegativeContrastiveLearning` (*ANCE Approximate Nearest Neighbor Negative Contrastive Learning*)
- **Record Path**: `data/curated/ANCEApproximateNearestNeighborNegativeContrastiveLearning.yaml`
- **Primary Source**: Lee Xiong, Chenyan Xiong, Ye Li, Kwok-Fung Tang, Jialin Liu, Paul Bennett, Junaid Ahmed, Arnold Overwijk — *Approximate Nearest Neighbor Negative Contrastive Learning for Dense Text Retrieval* (`https://arxiv.org/bibtex/2007.00808`).

## Identity & Boundary Resolution

Distinct from Dense Passage Retrieval (Karpukhin et al., EMNLP 2020, AIMech:DensePassageRetrieval), which uses static BM25 negatives and local in-batch negatives; distinct from RocketQA (Qu et al., NAACL 2021, AIMech:RocketQADenoisedHardNegativeSampling), which uses cross-batch negatives and cross-encoder hard-negative denoising across discrete pipeline generations; and distinct from REALM (Guu et al., ICML 2020, AIMech:REALMRetrievalAugmentedLanguageModelPreTraining), which trains a masked language model jointly with a neural knowledge retriever using marginal log-likelihood over documents rather than variance-reducing global hard-negative contrastive estimation for first-stage ad-hoc and OpenQA dense retrieval.

## Constructed Boundary & Regime Verification

```text
Round 753 ANCE boundary verification passed.
```
