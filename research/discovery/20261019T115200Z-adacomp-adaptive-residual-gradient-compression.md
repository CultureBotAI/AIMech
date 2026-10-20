# Discovery Report: Round 629 — AdaComp (Adaptive Residual Gradient Compression)

- **Timestamp**: `2026-10-19T11:52:00Z`
- **Selected Concept**: `AIMech:AdaCompAdaptiveResidualGradientCompression` (*AdaComp (Adaptive Residual Gradient Compression)*)
- **Record Path**: `data/curated/AdaCompAdaptiveResidualGradientCompression.yaml`
- **Primary Source**: Chia-Yu Chen, Jungwook Choi, Daniel Brand, Ankur Agrawal, Wei Zhang, Kailash Gopalakrishnan — *AdaComp : Adaptive Residual Gradient Compression for Data-Parallel Distributed Training* (`https://dblp.org/rec/conf/aaai/ChenCBAZG18`).

## Identity & Boundary Resolution

Distinct from 1-bit SGD (AIMech:OneBitStochasticGradientDescent, Seide et al. 2014) and TernGrad (AIMech:TernGradTernaryGradients, Wen et al. 2017), which quantize dense gradient vectors without local-bin sparsity selection and either diverge on convolutional layers when combined with FC compression or cap compression at 16x. Distinct from fixed-threshold compression (Strom 2015), fixed-percentage global top-k sorting (Dryden et al. 2016), and Deep Gradient Compression (AIMech:DeepGradientCompression, Lin et al. 2018), which rely on global thresholding or sorting rather than O(N) localized bin sampling with the self-adjusting soft threshold |residue + 2 dW| >= g_max(i).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 629 AdaComp verified: cons_err=2.78e-17, c_early=13>2=c_late, conv_ratio=40.0x, fc_ratio=200.0x
```
