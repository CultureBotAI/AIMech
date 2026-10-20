# Discovery Report: Round 732 — GrIPS Gradient-Free Edit-Based Instruction Search

- **Timestamp**: `2026-10-19T13:35:00Z`
- **Selected Concept**: `AIMech:GrIPSGradientFreeEditBasedInstructionSearch` (*GrIPS Gradient-Free Edit-Based Instruction Search*)
- **Record Path**: `data/curated/GrIPSGradientFreeEditBasedInstructionSearch.yaml`
- **Primary Source**: Archiki Prasad, Peter Hase, Xiang Zhou, Mohit Bansal — *GrIPS: Gradient-free, Edit-based Instruction Search for Prompting Large Language Models* (`https://dblp.org/rec/conf/eacl/PrasadHZB23.xml`).

## Identity & Boundary Resolution

Distinct from gradient-guided discrete trigger search (AIMech:AutoPromptGradientGuidedDiscretePromptSearch), which requires first-order embedding gradients to rank vocabulary token replacements, and from reinforcement-learning token generation (AIMech:RLPromptReinforcementLearningDiscretePromptOptimization), which trains a continuous policy head over token sequences. Also distinct from derivative-free continuous subspace prompt optimization (AIMech:BBTBlackBoxTuningForLanguageModelAsAService), which optimizes continuous vectors via CMA-ES rather than human-interpretable phrase-level text edits.

## Constructed Boundary & Regime Verification

```text
GrIPS verification passed: init_acc=0.55 -> final_acc=0.95, final_instruction='Classify this review determine accurately whether it is positive or negative'
```
