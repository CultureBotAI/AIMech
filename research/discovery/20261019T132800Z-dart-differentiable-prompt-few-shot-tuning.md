# Discovery Report: Round 725 — DART Differentiable Prompt Few-Shot Tuning

- **Timestamp**: `2026-10-19T13:28:00Z`
- **Selected Concept**: `AIMech:DARTDifferentiablePromptFewShotTuning` (*DART Differentiable Prompt Few-Shot Tuning*)
- **Record Path**: `data/curated/DARTDifferentiablePromptFewShotTuning.yaml`
- **Primary Source**: Ningyu Zhang, Luoqiu Li, Xiang Chen, Shumin Deng, Zhen Bi, Chuanqi Tan, Fei Huang, Huajun Chen — *Differentiable Prompt Makes Pre-trained Language Models Better Few-shot Learners* (`https://dblp.org/search/publ/api?q=Differentiable+Prompt+Makes+Pre-trained+Language+Models+Better+Few-shot+Learners+Zhang&format=xml`).

## Identity & Boundary Resolution

Distinct from LM-BFF (Gao et al., ACL 2021, AIMech:LMBFFBetterFewShotFineTuning), which performs brute-force discrete verbalizer search and external T5 template generation, from P-Tuning (Liu et al., 2021), which relies on an external bidirectional LSTM to induce template token co-dependence and uses fixed discrete verbalizers, and from WARP (AIMech:WARPWordLevelAdversarialReProgramming), which freezes the backbone Transformer and does not enforce an auxiliary MLM fluency constraint.

## Constructed Boundary & Regime Verification

```text
DART verification passed.
```
