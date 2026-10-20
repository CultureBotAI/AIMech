# Discovery Report: Round 702 — MPT (Multitask Prompt Tuning)

- **Timestamp**: `2026-10-19T13:05:00Z`
- **Selected Concept**: `AIMech:MPTMultitaskPromptTuning` (*MPT (Multitask Prompt Tuning)*)
- **Record Path**: `data/curated/MPTMultitaskPromptTuning.yaml`
- **Primary Source**: Zhen Wang, Rameswar Panda, Leonid Karlinsky, Rogerio Feris, Huan Sun, Yoon Kim — *Multitask Prompt Tuning Enables Parameter-Efficient Transfer Learning* (`https://dblp.org/search/publ/api?q=Multitask+Prompt+Tuning+Enables+Parameter-Efficient+Transfer+Learning&format=xml`).

## Identity & Boundary Resolution

Introduced by Zhen Wang, Rameswar Panda, Leonid Karlinsky, Rogerio Feris, Huan Sun, and Yoon Kim (ICLR 2023, arXiv:2303.02861). Distinct from SPoT (Vu et al., ACL 2022; AIMech Round 698), which trains a single unfactorized prompt on a source mixture or retrieves top-k source prompts by cosine similarity without multiplicative rank-one prompt decomposition or knowledge distillation from per-task teacher prompts. Both single-target adaptation (MPT, tuning (l x d) + (l + d) parameters per task) and multitask target group adaptation (MPT*, sharing P^* across tau target tasks for (l x d)/tau + (l + d) parameters per task) are covered within this record.

## Constructed Boundary & Regime Verification

```text
[PASS] MPT boundary verification passed: single_task_params=77,668 (0.035%), mpt_star_params=10,468, distill_loss: 21.8634 -> 0.000000
```
