# Discovery Report: Round 801 — MiniLM (Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers)

- **Timestamp**: `2026-10-19T14:44:00Z`
- **Selected Concept**: `AIMech:MiniLMDeepSelfAttentionDistillationForTaskAgnosticCompression` (*MiniLM (Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers)*)
- **Record Path**: `data/curated/MiniLMDeepSelfAttentionDistillationForTaskAgnosticCompression.yaml`
- **Primary Source**: Wenhui Wang, Furu Wei, Li Dong, Hangbo Bao, Nan Yang, Ming Zhou — *MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers* (`https://arxiv.org/bibtex/2002.10957`).

## Identity & Boundary Resolution

Distinct from TinyBERT (AIMech:TinyBERTTransformerDistillationForNaturalLanguageUnderstanding, which performs layer-to-layer distillation across all student layers using a mapping function g(m) and learnable projection matrices W_h in R^{d' x d}) and from MobileBERT (Sun et al., 2020, which requires student and teacher to have identical layer counts L=24 and bottleneck-matched outer dimensions). MiniLM distills only the teacher's final Transformer layer and converts value vectors V_{M,a}^S in R^{|x| x d'_k} into sequence-by-sequence relation matrices VR_{M,a}^S in R^{|x| x |x|} whose dimensions are invariant to d'_k, eliminating both layer-mapping tuning and linear projection matrices.

## Constructed Boundary & Regime Verification

```text
MiniLM boundary verification passed:
  VR shape (teacher d_k=4 vs student d'_k=2): (3, 3)
  L_AT + L_VR (aligned vs mismatched): 0.00229 < 0.11495
```
