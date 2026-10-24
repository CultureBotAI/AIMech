# Discovery Report: Round 757 — AR2 Adversarial Retriever-Ranker for Dense Text Retrieval

- **Timestamp**: `2026-10-19T14:00:00Z`
- **Selected Concept**: `AIMech:AR2AdversarialRetrieverRankerForDenseTextRetrieval` (*AR2 Adversarial Retriever-Ranker for Dense Text Retrieval*)
- **Record Path**: `data/curated/AR2AdversarialRetrieverRankerForDenseTextRetrieval.yaml`
- **Primary Source**: Hang Zhang, Yeyun Gong, Yelong Shen, Jiancheng Lv, Nan Duan, Weizhu Chen — *Adversarial Retriever-Ranker for Dense Text Retrieval* (`https://arxiv.org/bibtex/2110.03611`).

## Identity & Boundary Resolution

Distinct from ANCE (Xiong et al., ICLR 2021, AIMech:ANCEApproximateNearestNeighborNegativeContrastiveLearning), which iteratively mines hard negatives from an ANN index without a cross-encoder ranker or adversarial minimax reward; distinct from RocketQA (Qu et al., NAACL 2021, AIMech:RocketQADenoisedHardNegativeSampling), which uses a static cross-encoder to filter hard negatives offline across separate pipeline stages rather than interactive minimax co-training; and distinct from IRGAN (Wang et al., SIGIR 2017), which uses a binary GAN discriminator objective log D_phi(d, q) + log(1 - D_phi(d^-, q)) rather than a listwise contrastive cross-encoder likelihood with entropy-smoothing distillation regularization.

## Constructed Boundary & Regime Verification

```text
Round 757 AR2 boundary verification passed.
```
