# Discovery Report: Round 724 — PTR Prompt Tuning with Rules

- **Timestamp**: `2026-10-19T13:27:00Z`
- **Selected Concept**: `AIMech:PTRPromptTuningWithRules` (*PTR Prompt Tuning with Rules*)
- **Record Path**: `data/curated/PTRPromptTuningWithRules.yaml`
- **Primary Source**: Xu Han, Weilin Zhao, Ning Ding, Zhiyuan Liu, Maosong Sun — *PTR: Prompt Tuning with Rules for Text Classification* (`https://dblp.org/search/publ/api?q=PTR+Prompt+Tuning+with+Rules+for+Text+Classification+Han&format=xml`).

## Identity & Boundary Resolution

Distinct from single-mask prompt tuning methods such as PET (AIMech:PatternExploitingTraining), LM-BFF (AIMech:LMBFFBetterFewShotFineTuning), and KPT (AIMech:KPTKnowledgeablePromptTuningVerbalizer), which predict a single [MASK] position and cannot factorize many-class relation labels into composable entity-type and relational sub-prompts, and from TYP MARKER fine-tuning (Zhou & Chen, 2021), which requires gold human entity-type annotations and an extra task-specific classification layer.

## Constructed Boundary & Regime Verification

```text
PTR verification passed.
```
