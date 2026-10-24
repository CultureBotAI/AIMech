# Discovery Report: Round 802 — BERT-PKD (Patient Knowledge Distillation for BERT Model Compression)

- **Timestamp**: `2026-10-19T14:45:00Z`
- **Selected Concept**: `AIMech:BERTPKDPatientKnowledgeDistillationForBERTModelCompression` (*BERT-PKD (Patient Knowledge Distillation for BERT Model Compression)*)
- **Record Path**: `data/curated/BERTPKDPatientKnowledgeDistillationForBERTModelCompression.yaml`
- **Primary Source**: Siqi Sun, Yu Cheng, Zhe Gan, Jingjing Liu — *Patient Knowledge Distillation for BERT Model Compression* (`https://arxiv.org/bibtex/1908.09355`).

## Identity & Boundary Resolution

Distinct from TinyBERT (AIMech:TinyBERTTransformerDistillationForNaturalLanguageUnderstanding) and MiniLM (AIMech:MiniLMDeepSelfAttentionDistillationForTaskAgnosticCompression), which match full sequence token hidden states or multi-head attention/value-relation matrices across all tokens. To avoid the computational cost and noise of distilling all token positions during task-specific fine-tuning, BERT-PKD initializes the n-layer student with the first n layers of pre-trained BERT and aligns only the L2-normalized [CLS] token embeddings across k = n - 1 intermediate layers via PKD-Skip (e.g., I_pt = {2, 4, 6, 8, 10} for 12->6) or PKD-Last (e.g., I_pt = {7, 8, 9, 10, 11}).

## Constructed Boundary & Regime Verification

```text
BERT-PKD boundary verification passed:
  PKD-Skip I_pt (12->6): [2, 4, 6, 8, 10]
  PKD-Last I_pt (12->6): [7, 8, 9, 10, 11]
  L_PT (collinear scaled vs antipodal): 0.000000 vs 20.00
```
