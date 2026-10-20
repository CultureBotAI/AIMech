# Discovery Report: Round 800 — TinyBERT (Two-Stage Transformer Distillation for Natural Language Understanding)

- **Timestamp**: `2026-10-19T14:43:00Z`
- **Selected Concept**: `AIMech:TinyBERTTransformerDistillationForNaturalLanguageUnderstanding` (*TinyBERT (Two-Stage Transformer Distillation for Natural Language Understanding)*)
- **Record Path**: `data/curated/TinyBERTTransformerDistillationForNaturalLanguageUnderstanding.yaml`
- **Primary Source**: Xiaoqi Jiao, Yichun Yin, Lifeng Shang, Xin Jiang, Xiao Chen, Linlin Li, Fang Wang, Qun Liu — *TinyBERT: Distilling BERT for Natural Language Understanding* (`https://arxiv.org/bibtex/1909.10351`).

## Identity & Boundary Resolution

Distinct from DistilBERT (Sanh et al., 2019, which distills only at the pre-training stage and requires identical hidden dimensions d' = d to initialize from teacher layers), from BERT-PKD (AIMech:BERTPKDPatientKnowledgeDistillationForBERTModelCompression, which matches only L2-normalized [CLS] hidden states at the fine-tuning stage), and from Simplified TinyBERT (AIMech:SimplifiedTinyBERTKnowledgeDistillationForDocumentRetrieval, which merges the two task-specific steps into one step and adds hard-label cross-entropy for document retrieval). TinyBERT fits unnormalized pre-softmax attention matrices A_i = Q K^T / sqrt(d_k), projects smaller student hidden states via learnable matrices W_e, W_h in R^{d' x d}, and expands task datasets 20x via single-piece BERT [MASK] prediction and multi-piece GloVe nearest-neighbor word replacement (Algorithm 1).

## Constructed Boundary & Regime Verification

```text
TinyBERT boundary verification passed:
  Uniform mapping (M=4, N=12): [0, 3, 6, 9, 12, 13]
  Matched L_embd=0.000000, L_attn=0.000000, L_hidn=0.000000, L_pred=0.3653
```
