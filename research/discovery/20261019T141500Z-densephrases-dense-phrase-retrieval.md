# Discovery Report: Round 772 — DensePhrases Dense Phrase Retrieval at Scale

- **Timestamp**: `2026-10-19T14:15:00Z`
- **Selected Concept**: `AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale` (*DensePhrases Dense Phrase Retrieval at Scale*)
- **Record Path**: `data/curated/DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale.yaml`
- **Primary Source**: Jinhyuk Lee, Mujeen Sung, Jaewoo Kang, Danqi Chen — *Learning Dense Representations of Phrases at Scale* (`https://arxiv.org/bibtex/2012.12624`).

## Identity & Boundary Resolution

Distinct from two-stage retriever-reader models such as DPR and GAR (AIMech:GARGenerationAugmentedRetrievalForOpenDomainQA), which retrieve passages first and run an on-demand reading-comprehension model at inference time rather than directly retrieving answer phrases via decomposed start/end token MIPS; and distinct from earlier hybrid phrase retrieval systems (DenSPI and DenSPI+Sparc), which require concatenating high-dimensional sparse document/paragraph/contextualized vectors with split dense vectors and coherency scalars rather than purely dense unsplit SpanBERT endpoint representations trained with FIFO pre-batch negatives and query-side fine-tuning.

## Constructed Boundary & Regime Verification

```text
[PASS] DensePhrases boundaries verified: best_span=(3, 4) ('the Police'), num_negs=5, qs_loss_multi=0.3792 < qs_loss_single=0.6868
```
