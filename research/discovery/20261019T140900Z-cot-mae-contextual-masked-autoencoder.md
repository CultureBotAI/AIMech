# Discovery Report: Round 766 — CoT-MAE Contextual Masked Auto-Encoder for Dense Passage Retrieval

- **Timestamp**: `2026-10-19T14:09:00Z`
- **Selected Concept**: `AIMech:CoTMAEContextualMaskedAutoEncoderForDensePassageRetrieval` (*CoT-MAE Contextual Masked Auto-Encoder for Dense Passage Retrieval*)
- **Record Path**: `data/curated/CoTMAEContextualMaskedAutoEncoderForDensePassageRetrieval.yaml`
- **Primary Source**: Xing Wu, Guangyuan Ma, Meng Lin, Zijia Lin, Zhongyuan Wang, Songlin Hu — *ConTextual Masked Auto-Encoder for Dense Passage Retrieval* (`https://arxiv.org/bibtex/2208.07670`).

## Identity & Boundary Resolution

Distinct from SEED-Encoder (AIMech:SEEDPreTrainingStrongTextEncoderUsingWeakDecoder), Condenser (AIMech:CondenserPreTrainingArchitectureForDenseRetrieval), RetroMAE (AIMech:RetroMAERetrievalOrientedMaskedAutoEncoder), and SimLM (AIMech:SimLMRepresentationBottleneckPreTraining), all of which perform single-span internal auto-encoding where the decoder reconstructs the same text span encoded into [CLS] rather than cross-span context-supervised masked auto-encoding over paired neighboring spans (T_A, T_B); and distinct from coCondenser (AIMech:CoCondenserUnsupervisedCorpusAwareLanguageModelPreTraining), which uses a discriminative corpus-level contrastive loss across spans rather than generative context-MLM reconstruction.

## Constructed Boundary & Regime Verification

```text
[PASS] CoT-MAE boundaries verified: masked_enc=6 < masked_dec=9, L_total(aligned)=4.8813 < L_total(unaligned)=13.8491
```
