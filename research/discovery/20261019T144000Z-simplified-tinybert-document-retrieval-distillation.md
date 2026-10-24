# Discovery Report: Round 797 — Simplified TinyBERT (Knowledge Distillation for Document Retrieval)

- **Timestamp**: `2026-10-19T14:40:00Z`
- **Selected Concept**: `AIMech:SimplifiedTinyBERTKnowledgeDistillationForDocumentRetrieval` (*Simplified TinyBERT (Knowledge Distillation for Document Retrieval)*)
- **Record Path**: `data/curated/SimplifiedTinyBERTKnowledgeDistillationForDocumentRetrieval.yaml`
- **Primary Source**: Xuanang Chen, Ben He, Kai Hui, Le Sun, Yingfei Sun — *Simplified TinyBERT: Knowledge Distillation for Document Retrieval* (`https://arxiv.org/bibtex/2009.07531`).

## Identity & Boundary Resolution

Distinct from original TinyBERT (Jiao et al., 2020, which splits task-specific distillation into two sequential steps—first optimizing L_attn + L_hidn + L_emb and then optimizing L_soft alone without hard labels) and from Margin-MSE (AIMech:MarginMSECrossArchitectureKnowledgeDistillationForNeuralRanking, which distills pairwise score margins across heterogeneous ranking architectures without intermediate layer matching). Simplified TinyBERT jointly optimizes all five losses L_h = L_attn + L_hidn + L_emb + L_soft + L_hard in one task-specific step over top-5 teacher-filtered positive passages per relevant document.

## Constructed Boundary & Regime Verification

```text
Simplified TinyBERT boundary verification passed:
  L_h(student=0.88)=0.7569 < L_h(student=0.75)=0.8532
  Top-5 teacher-filtered positive passages: [11, 12, 14, 15, 16]
  Second-stage training time savings: [52.0, 44.7, 46.9, 41.9]%
```
