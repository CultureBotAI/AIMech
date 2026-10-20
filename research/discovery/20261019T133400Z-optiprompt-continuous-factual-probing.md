# Discovery Report: Round 731 — OptiPrompt Continuous Factual Probing

- **Timestamp**: `2026-10-19T13:34:00Z`
- **Selected Concept**: `AIMech:OptiPromptContinuousFactualProbing` (*OptiPrompt Continuous Factual Probing*)
- **Record Path**: `data/curated/OptiPromptContinuousFactualProbing.yaml`
- **Primary Source**: Zexuan Zhong, Dan Friedman, Danqi Chen — *Factual Probing Is [MASK]: Learning vs. Learning to Recall* (`https://dblp.org/rec/conf/naacl/ZhongFC21.xml`).

## Identity & Boundary Resolution

Distinct from discrete prompt search methods such as AutoPrompt (AIMech:AutoPromptGradientGuidedDiscretePromptSearch) and mining/paraphrasing relational prompts (LPAQA) because OptiPrompt optimizes unconstrained continuous vectors v_i in R^d directly in the input embedding layer of a frozen masked language model, optionally initialized from the embeddings of manual prompt tokens. Also distinct from multi-layer deep continuous prefix tuning (AIMech:PTuningV2DeepContinuousPromptTuning), which injects trainable key-value prefixes across every transformer layer for downstream NLU supervision rather than probing factual relational knowledge and analyzing spurious target-distribution exploitation in masked language models.

## Constructed Boundary & Regime Verification

```text
OptiPrompt verification passed: loss_manual=1.1815 -> loss_opt=0.1227, P@1=1.00
```
