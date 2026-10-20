# Discovery Report: Round 796 — TwinBERT (Distilling Knowledge to Twin-Structured BERT Models for Efficient Retrieval)

- **Timestamp**: `2026-10-19T14:39:00Z`
- **Selected Concept**: `AIMech:TwinBERTDistillingKnowledgeToTwinStructuredBERTModels` (*TwinBERT (Distilling Knowledge to Twin-Structured BERT Models for Efficient Retrieval)*)
- **Record Path**: `data/curated/TwinBERTDistillingKnowledgeToTwinStructuredBERTModels.yaml`
- **Primary Source**: Wenhao Lu, Jian Jiao, Ruofei Zhang — *TwinBERT: Distilling Knowledge to Twin-Structured BERT Models for Efficient Retrieval* (`https://arxiv.org/bibtex/2002.06275`).

## Identity & Boundary Resolution

Distinct from Sentence-BERT (AIMech:SentenceBERT, which fine-tunes pre-trained WordPiece BERT towers with mean/max/[CLS] pooling on NLI/STS labels) and from MORES/DC-BERT (which retain token-level document matrices for upper-layer Transformer attention). TwinBERT replaces recursive WordPiece tokenization with independent 50K character tri-letter embeddings, pools each 6-layer encoder output into a single vector via learned per-position weighted-average pooling, defines both TwinBERT_cos (logistic regression over cos(q, k), Eq. 1) and TwinBERT_res (elementwise max x = max(q, k) followed by residual block y = F(x, W, b) + x, Eq. 2), and distills a 12-layer BERT teacher on 500M search impressions using temperature T=2 soft targets followed by actual-label fine-tuning and asymmetric encoder training.

## Constructed Boundary & Regime Verification

```text
TwinBERT boundary verification passed:
  TwinBERT_cos: cos_pos=0.9313 (p=0.9765) > cos_neg=-0.9408 (p=0.0227)
  TwinBERT_res: p_res_pos=0.9607 > p_res_neg=0.9065
  Teacher soft target at T=2: 0.8176 vs T=1: 0.9526
```
