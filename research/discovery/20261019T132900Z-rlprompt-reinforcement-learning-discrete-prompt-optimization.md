# Discovery Report: Round 726 — RLPrompt Reinforcement Learning Discrete Prompt Optimization

- **Timestamp**: `2026-10-19T13:29:00Z`
- **Selected Concept**: `AIMech:RLPromptReinforcementLearningDiscretePromptOptimization` (*RLPrompt Reinforcement Learning Discrete Prompt Optimization*)
- **Record Path**: `data/curated/RLPromptReinforcementLearningDiscretePromptOptimization.yaml`
- **Primary Source**: Mingkai Deng, Jianyu Wang, Cheng-Ping Hsieh, Yihan Wang, Han Guo, Tianmin Shu, Meng Song, Eric P. Xing, Zhiting Hu — *RLPrompt: Optimizing Discrete Text Prompts with Reinforcement Learning* (`https://dblp.org/search/publ/api?q=RLPrompt+Optimizing+Discrete+Text+Prompts+with+Reinforcement+Learning+Deng&format=xml`).

## Identity & Boundary Resolution

Distinct from AutoPrompt (Shin et al., EMNLP 2020, AIMech:AutoPromptGradientGuidedDiscretePromptSearch), which requires white-box gradients from the target LM, from Black-Box Tuning (Sun et al., ICML 2022, AIMech:BBTBlackBoxTuningForLanguageModelAsAService), which optimizes continuous soft prompt embeddings via CMA-ES in a random linear subspace and requires server-side continuous embedding injection, and from heuristic discrete prompt enumeration/editing methods such as GrIPS (Prasad et al., 2022).

## Constructed Boundary & Regime Verification

```text
RLPrompt verification passed.
```
