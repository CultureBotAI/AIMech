# Discovery Report: Round 774 — SPARTA Sparse Transformer Matching for Retrieval

- **Timestamp**: `2026-10-19T14:17:00Z`
- **Selected Concept**: `AIMech:SPARTASparseTransformerMatchingForRetrieval` (*SPARTA Sparse Transformer Matching for Retrieval*)
- **Record Path**: `data/curated/SPARTASparseTransformerMatchingForRetrieval.yaml`
- **Primary Source**: Tiancheng Zhao, Xiaopeng Lu, Kyusong Lee — *SPARTA: Efficient Open-Domain Question Answering via Sparse Transformer Matching Retrieval* (`https://arxiv.org/bibtex/2009.13013`).

## Identity & Boundary Resolution

Distinct from SPLADE (AIMech:SPLADESparseLexicalAndExpansionModel), which uses the Masked Language Modeling output head on contextualized query and document encoders with explicit L1/FLOPS sparsity regularization rather than non-contextualized query word embeddings max-pooled against contextualized answer+context BERT tokens with a scalar ReLU threshold b; and distinct from COIL (AIMech:COILContextualizedInvertedList) and DeepCT (AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval), which restrict index entries to exact tokens appearing in the document rather than scoring and indexing latent non-appearing vocabulary terms (such as question words 'who', 'where', and synonyms).

## Constructed Boundary & Regime Verification

```text
[PASS] SPARTA boundaries verified: s_pos=1.3614 > s_nearby=0.5331 > s_rand=0.0198, J_ltr=0.3592
```
