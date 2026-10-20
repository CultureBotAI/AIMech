# Discovery Report: Round 625 — Gradient Centralization

- **Timestamp**: `2026-10-19T11:48:00Z`
- **Selected Concept**: `AIMech:GradientCentralizationOptimization` (*Gradient Centralization*)
- **Record Path**: `data/curated/GradientCentralizationOptimization.yaml`
- **Primary Source**: Hongwei Yong, Jianqiang Huang, Xiansheng Hua, Lei Zhang — *Gradient Centralization: A New Optimization Technique for Deep Neural Networks* (`https://dblp.org/rec/conf/eccv/YongHHZ20`).

## Identity & Boundary Resolution

Distinct from activation normalizations (Batch Normalization, Layer Normalization, Group Normalization) and from weight reparameterizations (Weight Normalization, Weight Standardization): whereas Weight Standardization enforces e^T w = 0 directly on weights and therefore breaks pretrained ImageNet checkpoints whose initial weights have non-zero mean e^T w^0 != 0, Gradient Centralization projects gradients onto the hyperplane e^T (w - w^0) = 0, preserving any pretrained initialization w^0 while embedding into SGDM, Adam, or AdamW in a single line of code.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 625 Gradient Centralization verified: P2_err=0.00e+00, op_err=4.44e-16, hyperplane_err=2.81e-16, thm41_err=1.78e-15, eq10_err=3.55e-15, eq11_err=7.11e-15, hessian_norm_ratio=0.5282<1
```
