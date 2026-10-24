# Discovery Report: Round 681 — LoraHub

- **Timestamp**: `2026-10-19T12:44:00Z`
- **Selected Concept**: `AIMech:LoraHub` (*LoraHub*)
- **Record Path**: `data/curated/LoraHub.yaml`
- **Primary Source**: Chengsong Huang, Qian Liu, Bill Yuchen Lin, Tianyu Pang, Chao Du, Min Lin — *LoraHub: Efficient Cross-Task Generalization via Dynamic LoRA Composition* (`https://dblp.org/rec/journals/corr/abs-2307-13269.xml`).

## Identity & Boundary Resolution

Distinct from standard LoRA (AIMech:LoRA, which trains a single low-rank adapter via gradient descent on a target task), from HydraLoRA (AIMech:HydraLoRA, which jointly trains a shared down-projection matrix A and multiple routed up-projection heads B_k end-to-end with backpropagation), and from S-LoRA (AIMech:SLoRA, an inference serving system that batches heterogeneous LoRA adapters in unified paging memory rather than composing multiple upstream adapters into a single synthesized module for unseen tasks). Formulated by Huang et al. (COLM 2024, arXiv:2307.13269).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 681 LoraHub (Huang et al., COLM 2024): bilinear_err=1.11e-15, loss_zeroshot=13.3323 -> loss_retrieval=6.6536 -> loss_lorahub=0.0032
```
