# Discovery Report: Round 762 — LaPraDoR Iterative Contrastive Learning and Lexicon-Enhanced Dense Retrieval

- **Timestamp**: `2026-10-19T14:05:00Z`
- **Selected Concept**: `AIMech:LaPraDoRUnsupervisedPretrainedDenseRetrieverZeroShot` (*LaPraDoR Iterative Contrastive Learning and Lexicon-Enhanced Dense Retrieval*)
- **Record Path**: `data/curated/LaPraDoRUnsupervisedPretrainedDenseRetrieverZeroShot.yaml`
- **Primary Source**: Canwen Xu, Daya Guo, Nan Duan, Julian McAuley — *LaPraDoR: Unsupervised Pretrained Dense Retriever for Zero-Shot Text Retrieval* (`https://arxiv.org/bibtex/2203.06169`).

## Identity & Boundary Resolution

Distinct from MoCo (AIMech:MomentumContrastiveLearning) and xMoCo, which maintain slow momentum-updated target encoders whose older queued representations drift across different hidden spaces over training steps; distinct from Contriever (AIMech:ContrieverUnsupervisedDenseInformationRetrievalWithContrastiveLearning), which uses a MoCo momentum queue with random cropping and inverse cloze without alternating frozen-encoder cache clearing or multiplicative BM25 scoring; and distinct from COIL (AIMech:COILContextualizedInvertedList), which stores contextualized token vectors in an inverted list rather than multiplying a single global mean-pooled cosine similarity with BM25.

## Constructed Boundary & Regime Verification

```text
[PASS] LaPraDoR boundaries verified: L_ICoL(cache)=0.4410 > L_ICoL(no_cache)=0.0000, LEDR(gt)=6.5687 > max(LEDR(lex)=4.2900, LEDR(dense_noise)=3.4505)
```
