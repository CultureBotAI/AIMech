# Discovery Report: Round 813 — HAT (Hardware-Aware Transformers for Efficient Natural Language Processing)

- **Timestamp**: `2026-10-19T14:56:00Z`
- **Selected Concept**: `AIMech:HATHardwareAwareTransformersForEfficientNLP` (*HAT (Hardware-Aware Transformers for Efficient Natural Language Processing)*)
- **Record Path**: `data/curated/HATHardwareAwareTransformersForEfficientNLP.yaml`
- **Primary Source**: Hanrui Wang, Zhanghao Wu, Zhijian Liu, Han Cai, Ligeng Zhu, Chuang Gan, Song Han — *HAT: Hardware-Aware Transformers for Efficient Natural Language Processing* (`https://arxiv.org/bibtex/2005.14187`).

## Identity & Boundary Resolution

Distinct from Evolved Transformer (So et al., 2019), which searches homogeneous cell structures without hardware latency feedback at >10,000x higher GPU cost, distinct from Once-for-All (Cai et al., 2020), which targets convolutional neural networks via progressive shrinking rather than encoder-decoder Transformers with arbitrary cross-attention spans, and distinct from DynaBERT (AIMech:DynaBERTDynamicBERTWithAdaptiveWidthAndDepth), which adapts encoder-only BERT width and depth via importance-ordered head/neuron rewiring and distillation.

## Constructed Boundary & Regime Verification

```text
HAT verification passed: cardinality=1.310e+16, kv_lengths=(2,4,6), arm_deep_thin=1062.6<1425.2, gpu_shallow_wide=73.9<136.1
```
