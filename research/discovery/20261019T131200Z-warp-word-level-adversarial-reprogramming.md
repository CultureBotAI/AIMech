# Discovery Report: Round 709 — WARP (Word-level Adversarial ReProgramming)

- **Timestamp**: `2026-10-19T13:12:00Z`
- **Selected Concept**: `AIMech:WARPWordLevelAdversarialReProgramming` (*WARP (Word-level Adversarial ReProgramming)*)
- **Record Path**: `data/curated/WARPWordLevelAdversarialReProgramming.yaml`
- **Primary Source**: Karen Hambardzumyan, Hrant Khachatrian, Jonathan May — *WARP: Word-level Adversarial ReProgramming* (`https://dblp.org/search/publ/api?q=WARP+Word-level+Adversarial+ReProgramming&format=xml`).

## Identity & Boundary Resolution

Introduced by Karen Hambardzumyan, Hrant Khachatrian, and Jonathan May (ACL/IJCNLP 2021, Volume 1: Long Papers, pp. 4921-4933, arXiv:2101.00121). Inspired by image-level Adversarial Reprogramming (Elsayed et al., ICLR 2019). Distinct from discrete prompt search such as AutoPrompt (Shin et al., EMNLP 2020), which restricts triggers and verbalizers to discrete vocabulary tokens, and distinct from generative Prompt Tuning (Lester et al., EMNLP 2021; AIMech:PromptTuning), which prepends prefix prompts to sequence-to-sequence models without jointly optimizing continuous MLM verbalizer vectors Theta^V at a template [MASK] position.

## Constructed Boundary & Regime Verification

```text
[PASS] WARP boundaries verified: loss 1.0997 -> 0.9477, storage_ratio_100tasks=99.7x, input_untouched=True
```
