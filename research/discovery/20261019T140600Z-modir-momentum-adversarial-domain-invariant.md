# Discovery Report: Round 763 — MoDIR Momentum Adversarial Domain Invariant Representation Learning for Zero-Shot Dense Retrieval

- **Timestamp**: `2026-10-19T14:06:00Z`
- **Selected Concept**: `AIMech:MoDIRMomentumAdversarialDomainInvariantDenseRetrieval` (*MoDIR Momentum Adversarial Domain Invariant Representation Learning for Zero-Shot Dense Retrieval*)
- **Record Path**: `data/curated/MoDIRMomentumAdversarialDomainInvariantDenseRetrieval.yaml`
- **Primary Source**: Ji Xin, Chenyan Xiong, Ashwin Srinivasan, Ankita Sharma, Damien Jose, Paul N. Bennett — *Zero-Shot Dense Retrieval with Momentum Adversarial Domain Invariant Representations* (`https://arxiv.org/bibtex/2110.07581`).

## Identity & Boundary Resolution

Distinct from COCO-DR (AIMech:COCODRDenseRetrievalDistributionallyRobustContrastiveLearning), which adapts to unlabeled target corpora via implicit Continuous Contrastive Learning and queries clustered by source task without a target domain during fine-tuning; distinct from GPL (AIMech:GPLGenerativePseudoLabelingForDenseRetrieval), which generates synthetic target-domain queries and distills a cross-encoder rather than aligning source and target embedding spaces via adversarial domain confusion; and distinct from standard single-batch DANN/ADDA, which update the domain discriminator on only the current mini-batch without a multi-batch stop-gradient momentum queue Q_k and fail to capture the scattered locality of dense retrieval spaces (Table 2, Figure 3).

## Constructed Boundary & Regime Verification

```text
[PASS] MoDIR boundaries verified: L_M_init=2.4138 -> L_M_updated=1.9469 (min=1.3863), cos_momentum=1.0000 > cos_single=0.5547
```
