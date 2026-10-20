# Discovery Report: Round 764 — PROP Pre-Training with Representative Words Prediction for Ad-Hoc Retrieval

- **Timestamp**: `2026-10-19T14:07:00Z`
- **Selected Concept**: `AIMech:PROPPreTrainingWithRepresentativeWordsPrediction` (*PROP Pre-Training with Representative Words Prediction for Ad-Hoc Retrieval*)
- **Record Path**: `data/curated/PROPPreTrainingWithRepresentativeWordsPrediction.yaml`
- **Primary Source**: Xinyu Ma, Jiafeng Guo, Ruqing Zhang, Yixing Fan, Xiang Ji, Xueqi Cheng — *PROP: Pre-training with Representative Words Prediction for Ad-hoc Retrieval* (`https://arxiv.org/bibtex/2010.10137`).

## Identity & Boundary Resolution

Distinct from B-PROP (AIMech:BPROPBootstrappedPreTrainingWithRepresentativeWordsPrediction), which replaces the term-independent Dirichlet unigram language model with a bootstrapped BERT [CLS]-attention divergence-from-randomness contrastive term distribution; and distinct from Inverse Cloze Task (ICT), which extracts a contiguous natural-language sentence from a passage rather than sampling keyword sets from a statistical document language model.

## Constructed Boundary & Regime Verification

```text
[PASS] PROP representative words prediction boundaries verified: log P(S_1|D)=-3.6031 > log P(S_2|D)=-7.6991, L_ROP(init)=1.3000 -> L_ROP(trained)=0.0000
```
