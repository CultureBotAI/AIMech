# Discovery Report: Round 704 — ATTEMPT (Attentional Mixtures of Prompt Tuning)

- **Timestamp**: `2026-10-19T13:07:00Z`
- **Selected Concept**: `AIMech:ATTEMPTAttentionalMixturesOfSoftPrompts` (*ATTEMPT (Attentional Mixtures of Prompt Tuning)*)
- **Record Path**: `data/curated/ATTEMPTAttentionalMixturesOfSoftPrompts.yaml`
- **Primary Source**: Akari Asai, Mohammadreza Salehi, Matthew E. Peters, Hannaneh Hajishirzi — *ATTEMPT: Parameter-Efficient Multi-task Tuning via Attentional Mixtures of Soft Prompts* (`https://dblp.org/search/publ/api?q=ATTEMPT+Parameter-Efficient+Multi-task+Tuning&format=xml`).

## Identity & Boundary Resolution

Introduced by Akari Asai, Mohammadreza Salehi, Matthew E. Peters, and Hannaneh Hajishirzi (EMNLP 2022, arXiv:2205.11961). Distinct from SPoT (Vu et al., ACL 2022; AIMech Round 698), which uses a single source prompt only as a static initialization and overwrites its parameters during target fine-tuning, and distinct from MPT (Wang et al., ICLR 2023; AIMech Round 702), which learns a single shared prompt factorized with rank-one multiplicative task vectors rather than an instance-wise attention gate over modular frozen source prompts. Both single-target-task ATTEMPT and multi-task ATTEMPT-m (which shares the attention module G across N target tasks) are covered within this single record.

## Constructed Boundary & Regime Verification

```text
[PASS] ATTEMPT boundaries verified: params(N=1)=231936, params(N=8)=96192, eff_target_weight=1.2697, max_decomp_err=2.22e-16
```
