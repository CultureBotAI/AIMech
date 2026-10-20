# Discovery Report: Round 719 — LM-BFF Better Few-Shot Fine-Tuning of Language Models

- **Timestamp**: `2026-10-19T13:22:00Z`
- **Selected Concept**: `AIMech:LMBFFBetterFewShotFineTuning` (*LM-BFF Better Few-Shot Fine-Tuning of Language Models*)
- **Record Path**: `data/curated/LMBFFBetterFewShotFineTuning.yaml`
- **Primary Source**: Tianyu Gao, Adam Fisch, Danqi Chen — *Making Pre-trained Language Models Better Few-shot Learners* (`https://dblp.org/search/publ/api?q=Making+Pre-trained+Language+Models+Better+Few-shot+Learners+Gao&format=xml`).

## Identity & Boundary Resolution

Distinct from Pattern-Exploiting Training (PET, Schick & Schütze, EACL 2021, AIMech:PatternExploitingTraining), which uses manually crafted patterns and unlabeled data distillation, from AutoPrompt (Shin et al., EMNLP 2020, AIMech:AutoPromptGradientGuidedDiscretePromptSearch), which performs gradient-guided discrete trigger token search on frozen MLMs requiring large training sets, and from frozen GPT-3 In-Context Learning (AIMech:InContextLearning), which concatenates up to 32 random examples without parameter updates or class-balanced similarity filtering.

## Constructed Boundary & Regime Verification

```text
LM-BFF verification passed.
```
