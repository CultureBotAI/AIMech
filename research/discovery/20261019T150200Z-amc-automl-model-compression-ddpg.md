# Discovery Report: Round 819 — AMC (AutoML for Model Compression and Acceleration on Mobile Devices)

- **Timestamp**: `2026-10-19T15:02:00Z`
- **Selected Concept**: `AIMech:AMCAccelerationAndModelCompressionOnMobileDevicesWithRL` (*AMC (AutoML for Model Compression and Acceleration on Mobile Devices)*)
- **Record Path**: `data/curated/AMCAccelerationAndModelCompressionOnMobileDevicesWithRL.yaml`
- **Primary Source**: Yihui He, Ji Lin, Zhijian Liu, Hanrui Wang, Li-Jia Li, Song Han — *AMC: AutoML for Model Compression and Acceleration on Mobile Devices* (`https://arxiv.org/bibtex/1802.03494`).

## Identity & Boundary Resolution

Distinct from hand-crafted sensitivity pruning heuristics (Li et al., 2016; He et al., 2017) that ignore cross-layer dependencies, distinct from Runtime Neural Pruning (Lin et al., 2017) which selects coarse 4-action dynamic channel groups per input image without reducing static model size, and distinct from HAQ (AIMech:HAQHardwareAwareAutomatedQuantizationWithMixedPrecision) which allocates mixed-precision quantization bitwidths rather than pruning sparsity ratios.

## Constructed Boundary & Regime Verification

```text
AMC verification passed: bounded=[0.1, 0.1, 0.5, 0.8], achieved=0.5000, r_small_flops=-1.9337 > r_large_flops=-2.0030
```
