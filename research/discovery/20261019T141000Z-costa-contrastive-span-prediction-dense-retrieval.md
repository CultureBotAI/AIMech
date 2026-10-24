# Discovery Report: Round 767 — COSTA Contrastive Span Prediction Pre-Training for Dense Retrieval

- **Timestamp**: `2026-10-19T14:10:00Z`
- **Selected Concept**: `AIMech:COSTAContrastiveSpanPredictionForDenseRetrieval` (*COSTA Contrastive Span Prediction Pre-Training for Dense Retrieval*)
- **Record Path**: `data/curated/COSTAContrastiveSpanPredictionForDenseRetrieval.yaml`
- **Primary Source**: Xinyu Ma, Jiafeng Guo, Ruqing Zhang, Yixing Fan, Xueqi Cheng — *Pre-train a Discriminative Text Encoder for Dense Retrieval via Contrastive Span Prediction* (`https://arxiv.org/bibtex/2204.10641`).

## Identity & Boundary Resolution

Distinct from SEED-Encoder (AIMech:SEEDPreTrainingStrongTextEncoderUsingWeakDecoder), Condenser (AIMech:CondenserPreTrainingArchitectureForDenseRetrieval), RetroMAE (AIMech:RetroMAERetrievalOrientedMaskedAutoEncoder), and CoT-MAE (AIMech:CoTMAEContextualMaskedAutoEncoderForDensePassageRetrieval), all of which attach an auxiliary decoder or head during pre-training to reconstruct tokens via generative cross-entropy rather than decoder-free multi-granularity group-wise contrastive span alignment; and distinct from coCondenser (AIMech:CoCondenserUnsupervisedCorpusAwareLanguageModelPreTraining), which contrasts pairs of random document spans using a Condenser skip-connection head rather than aligning a nonlinearly projected whole-text [CLS] vector against 4T multi-granularity pooled spans from the same encoder pass.

## Constructed Boundary & Regime Verification

```text
[PASS] COSTA contrastive span prediction boundaries verified: L_GWC(aligned)=2.7983 < L_GWC(unaligned)=18.0351 (lower_bound=2*log(4)=2.7726)
```
