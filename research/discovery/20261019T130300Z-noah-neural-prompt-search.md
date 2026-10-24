# Discovery Report: Round 700 — NOAH (Neural Prompt Search)

- **Timestamp**: `2026-10-19T13:03:00Z`
- **Selected Concept**: `AIMech:NOAHNeuralPromptSearch` (*NOAH (Neural Prompt Search)*)
- **Record Path**: `data/curated/NOAHNeuralPromptSearch.yaml`
- **Primary Source**: Yuanhan Zhang, Kaiyang Zhou, Ziwei Liu — *Neural Prompt Search* (`https://dblp.org/search/publ/api?q=Neural+Prompt+Search+Yuanhan+Zhang&format=xml`).

## Identity & Boundary Resolution

Introduced by Yuanhan Zhang, Kaiyang Zhou, and Ziwei Liu (2022, arXiv:2206.04673; published in IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 47, no. 7, pp. 5268-5280). Distinct from UniPELT (Mao et al., ACL 2022; AIMech Round 693), which combines fixed-dimension Adapter, Prefix-Tuning, and LoRA submodules via continuous sigmoid gates in language models, and distinct from individual hand-crafted prompt modules (VPT, Adapter, LoRA). Both inherited (retraining-free) and retrained NOAH subnet deployment modes are covered within this record.

## Constructed Boundary & Regime Verification

```text
[PASS] NOAH boundary verification passed: len(x_m3)=9, len(x_m6)=12, vpt_depth3=[10, 5, 5, 0, 0, 0], valid_subnets=50/50 (sample_params=211,968 <= 640,000)
```
