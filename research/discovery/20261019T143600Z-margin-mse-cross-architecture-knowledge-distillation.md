# Discovery Report: Round 793 — Margin-MSE Cross-Architecture Knowledge Distillation for Neural Ranking

- **Timestamp**: `2026-10-19T14:36:00Z`
- **Selected Concept**: `AIMech:MarginMSECrossArchitectureKnowledgeDistillationForNeuralRanking` (*Margin-MSE Cross-Architecture Knowledge Distillation for Neural Ranking*)
- **Record Path**: `data/curated/MarginMSECrossArchitectureKnowledgeDistillationForNeuralRanking.yaml`
- **Primary Source**: Sebastian Hofstätter, Sophia Althammer, Michael Schröder, Mete Sertkan, Allan Hanbury — *Improving Efficient Neural Ranking Models with Cross-Architecture Knowledge Distillation* (`https://arxiv.org/bibtex/2010.02666`).

## Identity & Boundary Resolution

Distinct from homogeneous model-compression knowledge distillation (such as DistilBERT, TinyBERT, or TwinBERT, which compress a teacher into a smaller student of the same architectural family or match hidden states/attention matrices) and from pointwise score MSE distillation (Equation 13). Because different ranking architectures exhibit vastly different raw output score ranges and offsets (e.g., BERT_CAT scores centered near 0 vs. BERT_DOT/ColBERT dot-product scores centered around +70 to +160 vs. TK scores centered below 0), pointwise MSE forces unnatural score shifts, whereas Margin-MSE optimizes only the relative pairwise margin M(Q, P^+) - M(Q, P^-) and seamlessly corrects false negatives whenever the teacher assigns a negative margin M_t(Q, P^+) - M_t(Q, P^-) < 0.

## Constructed Boundary & Regime Verification

```text
Margin-MSE Cross-Architecture KD boundary verification passed:
  ColBERT vs BERT_CAT Margin-MSE:    0.000000
  ColBERT vs BERT_CAT Pointwise-MSE: 45000.00
  Top-3 Teacher Ensemble margins:    [10.0, 8.0]
```
