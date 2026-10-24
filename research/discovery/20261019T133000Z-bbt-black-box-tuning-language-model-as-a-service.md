# Discovery Report: Round 727 — Black-Box Tuning (BBT) for Language-Model-as-a-Service

- **Timestamp**: `2026-10-19T13:30:00Z`
- **Selected Concept**: `AIMech:BBTBlackBoxTuningForLanguageModelAsAService` (*Black-Box Tuning (BBT) for Language-Model-as-a-Service*)
- **Record Path**: `data/curated/BBTBlackBoxTuningForLanguageModelAsAService.yaml`
- **Primary Source**: Tianxiang Sun, Yunfan Shao, Hong Qian, Xuanjing Huang, Xipeng Qiu — *Black-Box Tuning for Language-Model-as-a-Service* (`https://dblp.org/search/publ/api?q=Black-Box+Tuning+for+Language-Model-as-a-Service+Sun&format=xml`).

## Identity & Boundary Resolution

Distinct from gradient-based Prompt Tuning (Lester et al., EMNLP 2021, AIMech:PromptTuning) and P-Tuning v2 (AIMech:PTuningV2DeepContinuousPromptTuning), which require backward-pass gradient access to the language model, and from RLPrompt (Deng et al., EMNLP 2022, AIMech:RLPromptReinforcementLearningDiscretePromptOptimization), which optimizes discrete vocabulary tokens via a policy network and Soft Q-Learning rather than continuous prompt increments in a random linear subspace via CMA-ES.

## Constructed Boundary & Regime Verification

```text
Black-Box Tuning verification passed.
```
