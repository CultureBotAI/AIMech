# Discovery Report: Round 765 — B-PROP Bootstrapped Pre-Training with Representative Words Prediction for Ad-Hoc Retrieval

- **Timestamp**: `2026-10-19T14:08:00Z`
- **Selected Concept**: `AIMech:BPROPBootstrappedPreTrainingWithRepresentativeWordsPrediction` (*B-PROP Bootstrapped Pre-Training with Representative Words Prediction for Ad-Hoc Retrieval*)
- **Record Path**: `data/curated/BPROPBootstrappedPreTrainingWithRepresentativeWordsPrediction.yaml`
- **Primary Source**: Xinyu Ma, Jiafeng Guo, Ruqing Zhang, Yixing Fan, Yingyan Li, Xueqi Cheng — *B-PROP: Bootstrapped Pre-training with Representative Words Prediction for Ad-hoc Retrieval* (`https://arxiv.org/bibtex/2104.09791`).

## Identity & Boundary Resolution

Distinct from PROP (AIMech:PROPPreTrainingWithRepresentativeWordsPrediction), which samples representative word sets from a term-independent Dirichlet-smoothed unigram language model rather than bootstrapping from BERT's saturated [CLS]-attention divergence-from-randomness contrastive distribution; and distinct from DeepCT, which trains a regression head to predict supervised term recall weights for inverted-index term weighting rather than bootstrapped pairwise ROP pre-training.

## Constructed Boundary & Regime Verification

```text
[PASS] B-PROP contrastive term sampling boundaries verified: P_d1(the)=0.2305 > P_d1(fibrosis)=0.2272, but P_contrastive(fibrosis)=0.2358 > P_contrastive(the)=0.1911
```
