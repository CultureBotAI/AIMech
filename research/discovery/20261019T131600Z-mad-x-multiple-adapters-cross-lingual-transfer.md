# Discovery Report: Round 713 — MAD-X Multiple Adapters for Cross-Lingual Transfer

- **Timestamp**: `2026-10-19T13:16:00Z`
- **Selected Concept**: `AIMech:MADXMultipleAdaptersForCrossLingualTransfer` (*MAD-X Multiple Adapters for Cross-Lingual Transfer*)
- **Record Path**: `data/curated/MADXMultipleAdaptersForCrossLingualTransfer.yaml`
- **Primary Source**: Jonas Pfeiffer, Ivan Vulic, Iryna Gurevych, Sebastian Ruder — *MAD-X: An Adapter-Based Framework for Multi-Task Cross-Lingual Transfer* (`https://dblp.org/search/publ/api?q=MAD-X+An+Adapter-Based+Framework+for+Multi-Task+Cross-Lingual+Transfer&h=5&format=xml`).

## Identity & Boundary Resolution

Introduced by Jonas Pfeiffer, Ivan Vulic, Iryna Gurevych, and Sebastian Ruder (EMNLP 2020, pp. 7654-7673, arXiv:2005.00052) as MAD-X (Multiple ADapters for Cross-lingual transfer). Distinct from AdapterFusion (AIMech:AdapterFusion), which combines multiple task adapters via a softmax attention layer rather than stacking language, task, and invertible adapters for cross-lingual transfer; and from LT-SFT (AIMech:LTSFTLotteryTicketSparseFineTuning), which composes sparse parameter difference vectors in weight space without adding adapter layers.

## Constructed Boundary & Regime Verification

```text
[PASS] MAD-X boundaries verified: max_inv_err=6.66e-16 (<1e-15), diff_transfer=4.4733, residual_identity=exact
```
