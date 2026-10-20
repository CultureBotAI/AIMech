# Discovery Report: Round 717 — P-Tuning v2 Deep Continuous Prompt Tuning

- **Timestamp**: `2026-10-19T13:20:00Z`
- **Selected Concept**: `AIMech:PTuningV2DeepContinuousPromptTuning` (*P-Tuning v2 Deep Continuous Prompt Tuning*)
- **Record Path**: `data/curated/PTuningV2DeepContinuousPromptTuning.yaml`
- **Primary Source**: Xiao Liu, Kaixuan Ji, Yicheng Fu, Weng Lam Tam, Zhengxiao Du, Zhilin Yang, Jie Tang — *P-Tuning v2: Prompt Tuning Can Be Comparable to Fine-tuning Universally Across Scales and Tasks* (`https://dblp.org/search/publ/api?q=P-Tuning+v2+Prompt+Tuning+Can+Be+Comparable+Liu&format=xml`).

## Identity & Boundary Resolution

Distinct from single-layer Prompt Tuning (Lester et al., EMNLP 2021, AIMech:PromptTuning) and original P-Tuning (Liu et al., 2021), which insert continuous prompts only in the input embedding layer with verbalizers and underperform on models below 10B parameters and on sequence tagging tasks; also distinct from Prefix-Tuning (Li & Liang, ACL 2021, AIMech:PrefixTuning), which targets autoregressive natural language generation with mandatory MLP reparameterization rather than bidirectional NLU and token-level sequence tagging with task-dependent reparameterization and linear token classification heads.

## Constructed Boundary & Regime Verification

```text
P-Tuning v2 verification passed.
```
