# Discovery Report: Round 787 — MonoT5: Document Ranking with a Pretrained Sequence-to-Sequence Model

- **Timestamp**: `2026-10-19T14:30:00Z`
- **Selected Concept**: `AIMech:MonoT5DocumentRankingWithPretrainedSeq2SeqModels` (*MonoT5: Document Ranking with a Pretrained Sequence-to-Sequence Model*)
- **Record Path**: `data/curated/MonoT5DocumentRankingWithPretrainedSeq2SeqModels.yaml`
- **Primary Source**: Rodrigo Nogueira, Zhiying Jiang, Ronak Pradeep, Jimmy Lin — *Document Ranking with a Pretrained Sequence-to-Sequence Model* (`https://arxiv.org/bibtex/2003.06713`).

## Identity & Boundary Resolution

Distinct from encoder-only classification-based rerankers such as monoBERT (which attach a randomly initialized linear classification head to the [CLS] token representation) and pairwise rerankers such as duoBERT (AIMech:DuoBERTMultiStageDocumentRankingWithBERT). By mapping relevance decisions onto pretrained single-token vocabulary logits ('true' and 'false') via the T5 language modeling head, MonoT5 exploits latent semantic and polarity knowledge from pretraining, yielding substantially higher data efficiency in low-resource regimes.

## Constructed Boundary & Regime Verification

```text
MonoT5 boundary verification passed:
  Prompt: Query: neural ranking Document: Sequence-to-sequence models generate target words. Relevant:
  P(Relevant=true | Doc1)=0.9526 > P(Relevant=true | Doc2)=0.7311
  MaxP document probability: 0.9707
```
