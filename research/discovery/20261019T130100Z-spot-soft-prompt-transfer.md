# Discovery Report: Round 698 — SPoT (Soft Prompt Transfer)

- **Timestamp**: `2026-10-19T13:01:00Z`
- **Selected Concept**: `AIMech:SPoTSoftPromptTransfer` (*SPoT (Soft Prompt Transfer)*)
- **Record Path**: `data/curated/SPoTSoftPromptTransfer.yaml`
- **Primary Source**: Tu Vu, Brian Lester, Noah Constant, Rami Al-Rfou, Daniel Cer — *SPoT: Better Frozen Model Adaptation through Soft Prompt Transfer* (`https://dblp.org/search/publ/api?q=SPoT+Better+Frozen+Model+Adaptation+through+Soft+Prompt+Transfer&format=xml`).

## Identity & Boundary Resolution

Introduced by Tu Vu, Brian Lester, Noah Constant, Rami Al-Rfou, and Daniel Cer (ACL 2022, arXiv:2110.07904). Distinct from vanilla Prompt Tuning (Lester et al., EMNLP 2021; AIMech Round 675), which initializes soft prompts from sampled vocabulary or class-label tokens directly on each target task without cross-task prompt transfer or prompt-based task embedding retrieval. Both generic SPoT (transferring a single multi-task or single-task source prompt to all target tasks) and targeted SPoT (retrieving top-k source prompts from a prompt library via Average-Token or Per-Token Average Cosine Similarity of 10K-step prompt checkpoints using Best of Top-k, Top-k Weighted Average, or Top-k Multi-task Mixture) are lumping-cohesive variants within this single record.

## Constructed Boundary & Regime Verification

```text
[PASS] SPoT boundary verification passed: reduction_ratio=26855.5x, s_tok=(0.9985>0.9404>0.2829), alphas=[0.515, 0.485], mse_top1=0.00018 < mse_spot_wavg=0.00680 << mse_scratch=0.34499
```
