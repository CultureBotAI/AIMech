# Discovery Report: Round 812 — DeeBERT (Dynamic Early Exiting for Accelerating BERT Inference)

- **Timestamp**: `2026-10-19T14:55:00Z`
- **Selected Concept**: `AIMech:DeeBERTDynamicEarlyExitingForAcceleratingBERTInference` (*DeeBERT (Dynamic Early Exiting for Accelerating BERT Inference)*)
- **Record Path**: `data/curated/DeeBERTDynamicEarlyExitingForAcceleratingBERTInference.yaml`
- **Primary Source**: Ji Xin, Raphael Tang, Jaejun Lee, Yaoliang Yu, Jimmy Lin — *DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference* (`https://arxiv.org/bibtex/2004.12993`).

## Identity & Boundary Resolution

Distinct from static layer-dropping and distillation methods (DistilBERT, TinyBERT, BERT-PKD, LayerDrop) that apply fixed depth reduction to all inputs regardless of difficulty, distinct from FastBERT (AIMech:FastBERTSelfDistillingBERTWithAdaptiveInferenceTime) which trains student branches via KL self-distillation from the final classifier's soft labels rather than supervised ground-truth cross-entropy in Stage 2, and distinct from PABEE (AIMech:PABEEPatienceBasedEarlyExitForBERT) which exits based on consecutive cross-layer prediction agreement (patience) rather than single-layer entropy H(z_i) < S.

## Constructed Boundary & Regime Verification

```text
DeeBERT verification passed: exit_easy=2, exit_hard=6, saving_low=0.3333, saving_high=0.5667, stage2_loss=0.6053
```
