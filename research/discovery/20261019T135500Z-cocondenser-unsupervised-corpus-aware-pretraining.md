# Discovery Report: Round 752 — coCondenser Unsupervised Corpus-Aware Language Model Pre-Training

- **Timestamp**: `2026-10-19T13:55:00Z`
- **Selected Concept**: `AIMech:CoCondenserUnsupervisedCorpusAwareLanguageModelPreTraining` (*coCondenser Unsupervised Corpus-Aware Language Model Pre-Training*)
- **Record Path**: `data/curated/CoCondenserUnsupervisedCorpusAwareLanguageModelPreTraining.yaml`
- **Primary Source**: Luyu Gao, Jamie Callan — *Unsupervised Corpus Aware Language Model Pre-training for Dense Passage Retrieval* (`https://dblp.org/rec/conf/acl/GaoC22.xml`).

## Identity & Boundary Resolution

Distinct from Condenser (Gao & Callan, EMNLP 2021, AIMech:CondenserPreTrainingArchitectureForDenseRetrieval), which uses the late-early short-circuit MLM architecture without any corpus-level contrastive loss over [CLS] inner products; distinct from RocketQA (Qu et al., NAACL 2021, AIMech:RocketQADenoisedHardNegativeSampling), which relies on supervised cross-batch negatives, cross-encoder hard-negative denoising, and synthetic data augmentation during fine-tuning; and distinct from ICT (Lee et al., ACL 2019, AIMech:InverseClozeTask), which contrasts pseudo-queries against context passages using standard Transformer encoders without Condenser short-circuit heads or gradient-cached skip-span contrastive pre-training.

## Constructed Boundary & Regime Verification

```text
Round 752 coCondenser boundary verification passed.
```
