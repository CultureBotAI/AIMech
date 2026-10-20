# Discovery Report: Round 751 — Condenser (Pre-Training Architecture for Dense Retrieval)

- **Timestamp**: `2026-10-19T13:54:00Z`
- **Selected Concept**: `AIMech:CondenserPreTrainingArchitectureForDenseRetrieval` (*Condenser (Pre-Training Architecture for Dense Retrieval)*)
- **Record Path**: `data/curated/CondenserPreTrainingArchitectureForDenseRetrieval.yaml`
- **Primary Source**: Luyu Gao, Jamie Callan — *Condenser: a Pre-training Architecture for Dense Retrieval* (`https://dblp.org/search/publ/api?q=Condenser+a+Pre-training+Architecture+for+Dense+Retrieval+Gao&h=5&format=xml`).

## Identity & Boundary Resolution

Introduced by Gao and Callan (EMNLP 2021, pp. 981-993, arXiv:2104.08253). Distinguished from standard BERT MLM/NSP pre-training (Devlin et al., 2019), where the [CLS] token remains dormant in middle layers and lacks structural readiness for dense aggregation, from RetroMAE (Xiao et al., 2022), which uses dual independent asymmetric masks (30% encoder, 50-70% decoder) and two-stream position-specific enhanced decoding without an early-layer skip connection, and from Funnel Transformer (Dai et al., 2020), which pools sequence length by 4x for compute speedup rather than routing global semantics through a single [CLS] vector.

## Constructed Boundary & Regime Verification

```text
Condenser boundary verification passed: {'loss_informative_cls': 0.0898, 'loss_dormant_cls': 1.0242}
```
