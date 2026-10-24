# Discovery Report: Round 760 — SEED Pre-Training a Strong Text Encoder Using a Weak Decoder

- **Timestamp**: `2026-10-19T14:03:00Z`
- **Selected Concept**: `AIMech:SEEDPreTrainingStrongTextEncoderUsingWeakDecoder` (*SEED Pre-Training a Strong Text Encoder Using a Weak Decoder*)
- **Record Path**: `data/curated/SEEDPreTrainingStrongTextEncoderUsingWeakDecoder.yaml`
- **Primary Source**: Shuqi Lu, Di He, Chenyan Xiong, Guolin Ke, Waleed Malik, Zhicheng Dou, Paul Bennett, Tie-Yan Liu, Arnold Overwijk — *Less is More: Pre-train a Strong Text Encoder for Dense Retrieval Using a Weak Decoder* (`https://arxiv.org/bibtex/2102.09206`).

## Identity & Boundary Resolution

Distinct from Condenser (AIMech:CondenserPreTrainingArchitectureForDenseRetrieval), which uses a bidirectional MLM head with late-to-early skip connections rather than an autoregressive decoder with restricted local attention span k; distinct from RetroMAE (AIMech:RetroMAERetrievalOrientedMaskedAutoEncoder) and SimLM (AIMech:SimLMRepresentationBottleneckPreTraining), which use shallow bidirectional decoders with masked or generator-replaced tokens rather than causal autoregressive decoding with restricted attention span k; and distinct from standard BART/T5 seq2seq pre-training, which passes all encoder token embeddings via cross-attention and uses a strong full-span decoder.

## Constructed Boundary & Regime Verification

```text
[PASS] SEED weak-decoder text encoder pre-training boundaries verified: |grad_cls_weak|=0.4502 > |grad_cls_full|=0.0630
```
