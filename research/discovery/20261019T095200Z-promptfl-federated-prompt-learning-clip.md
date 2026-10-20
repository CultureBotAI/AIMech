# Discovery Report: Round 509 — PromptFL: Federated Continuous Prompt Learning for Foundation Models

- **Timestamp**: `2026-10-19T09:52:00Z`
- **Selected Concept**: `AIMech:PromptFlFederatedPromptLearningForFoundationModels` (*PromptFL: Federated Continuous Prompt Learning for Foundation Models*)
- **Record Path**: `data/curated/PromptFlFederatedPromptLearningForFoundationModels.yaml`
- **Primary Source**: Tao Guo, Song Guo, Junxiao Wang, Xueyang Tang, Wenchao Xu — *PromptFL: Let Federated Participants Cooperatively Learn Prompts Instead of Models -- Federated Learning in Age of Foundation Model* (`https://doi.org/10.1109/tmc.2023.3302410`).

## Identity & Boundary Resolution

Distinct from full-model Federated Averaging (AIMech:FederatedAveraging; McMahan et al., 2017), which updates and communicates 100% of the neural network weights across clients and server. Distinct from centralized vision-language prompt tuning (CoOp; Zhou et al., 2022) and NLP continuous prefix/prompt tuning (Li & Liang, 2021; Lester et al., 2021), which optimize continuous prompts on a single centralized dataset rather than aggregating input-agnostic soft prompt updates across distributed non-IID clients or API-queried frozen backbones. Distinct from federated low-rank weight adapters such as FFA-LoRA (AIMech:FfaLoraFederatedFreezeALowRankAdaptation; Sun et al., ICLR 2024) and FLoRA (AIMech:FloraStackingBasedFederatedHeterogeneousLowRankAdaptation; Wang et al., NeurIPS 2024), which inject low-rank matrix increments into internal linear layers rather than prepending continuous prompt vectors to the text encoder input space.

## Constructed Boundary & Regime Verification

```text
PromptFL boundary verification passed: {'prompt_params': 8192, 'ratio_rn50_pct': 0.0214, 'ratio_vit_pct': 0.0095, 'init_loss': 0.24734, 'final_loss': 0.09083}
```
