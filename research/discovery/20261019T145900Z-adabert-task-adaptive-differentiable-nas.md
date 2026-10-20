# Discovery Report: Round 816 — AdaBERT (Task-Adaptive BERT Compression with Differentiable Neural Architecture Search)

- **Timestamp**: `2026-10-19T14:59:00Z`
- **Selected Concept**: `AIMech:AdaBERTTaskAdaptiveBERTCompressionWithDifferentiableNAS` (*AdaBERT (Task-Adaptive BERT Compression with Differentiable Neural Architecture Search)*)
- **Record Path**: `data/curated/AdaBERTTaskAdaptiveBERTCompressionWithDifferentiableNAS.yaml`
- **Primary Source**: Daoyuan Chen, Yaliang Li, Minghui Qiu, Zhen Wang, Bofang Li, Bolin Ding, Hongbo Deng, Jun Huang, Wei Lin, Jingren Zhou — *AdaBERT: Task-Adaptive BERT Compression with Differentiable Neural Architecture Search* (`https://arxiv.org/bibtex/2001.04246`).

## Identity & Boundary Resolution

Distinct from task-independent BERT distillation methods such as DistilBERT (AIMech:DistilBERTKnowledgeDistillationDuringPretraining), BERT-PKD (AIMech:BERTPKDPatientKnowledgeDistillationForBERTModelCompression), and TinyBERT (AIMech:TinyBERTTransformerDistillationForNaturalLanguageUnderstanding), which compress BERT into a fixed-structure smaller Transformer for all tasks, and distinct from HAT (AIMech:HATHardwareAwareTransformersForEfficientNLP), which performs evolutionary search over an encoder-decoder SuperTransformer rather than Gumbel-Softmax differentiable search over CNN cells guided by hierarchical teacher probe classifiers.

## Constructed Boundary & Regime Verification

```text
AdaBERT verification passed: mapped=[3, 6, 9, 12], w_im=[0.177, 0.232, 0.284, 0.306], l_e_shallow=0.2625 < l_e_deep=1.7063, y_soft_lo[1]=1.000000
```
