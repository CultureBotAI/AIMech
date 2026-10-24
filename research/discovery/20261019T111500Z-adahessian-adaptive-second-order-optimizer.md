# Discovery Report: Round 592 — AdaHessian (Adaptive Second-Order Optimizer)

- **Timestamp**: `2026-10-19T11:15:00Z`
- **Selected Concept**: `AIMech:AdaHessianAdaptiveSecondOrderOptimizer` (*AdaHessian (Adaptive Second-Order Optimizer)*)
- **Record Path**: `data/curated/AdaHessianAdaptiveSecondOrderOptimizer.yaml`
- **Primary Source**: Zhewei Yao, Amir Gholami, Sheng Shen, Mustafa Mustafa, Kurt Keutzer, Michael W. Mahoney — *ADAHESSIAN: An Adaptive Second Order Optimizer for Machine Learning* (`https://dblp.org/rec/conf/aaai/YaoGSMKM21`).

## Identity & Boundary Resolution

Distinct from Adam, AdamW, and RMSProp in that AdaHessian replaces the elementwise squared gradient g_i odot g_i in the second-moment accumulator with the squared spatially averaged Hutchinson Hessian diagonal D_i^{(s)} odot D_i^{(s)} raised to power k in [0, 1]. Distinct from Sophia in that AdaHessian performs block-diagonal spatial averaging across convolutional/attention blocks of size b, accumulates an RMS (L2) moving average of the Hessian diagonal rather than a linear EMA of max(h_t, 0), and applies unclipped power preconditioning m_t / (D_bar_t)^k.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 592 AdaHessian verified: hutch_err=8.88e-16, spatial_var=1.8850<raw_var=3.7700, x_ada=0.0052<<x_nomom=2.4718
```
