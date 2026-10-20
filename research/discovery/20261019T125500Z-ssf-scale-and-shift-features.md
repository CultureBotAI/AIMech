# Discovery Report: Round 692 — Scaling & Shifting Your Features

- **Timestamp**: `2026-10-19T12:55:00Z`
- **Selected Concept**: `AIMech:SSFScaleAndShiftFeatures` (*Scaling & Shifting Your Features*)
- **Record Path**: `data/curated/SSFScaleAndShiftFeatures.yaml`
- **Primary Source**: Dongze Lian, Daquan Zhou, Jiashi Feng, Xinchao Wang — *Scaling & Shifting Your Features: A New Baseline for Efficient Model Tuning* (`https://dblp.org/search/publ/api?q=Scaling+Shifting+Your+Features+Lian&format=xml`).

## Identity & Boundary Resolution

Distinct from Batch Normalization (AIO:BatchNormalizationLayer), Layer Normalization, FiLM, and AdaIN: SSF-ADA modulates outputs of general backbone operations (MSA, MLP, and normalization layers) rather than only normalization layers, and uses task-level input-independent parameters (gamma, beta) so they can be folded into preceding linear weights at inference time without conditional generator networks or nonlinear activations. Distinct from BitFit (AIMech:BitFit), which only tunes existing bias terms without multiplicative channel scaling or post-operation residual shifts, and from Adapter / VPT methods that retain unmergeable modules or extra tokens at inference time.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 692 SSF (Lian et al., NeurIPS 2022): max_rep_err=8.88e-16, infer_extra_params=0, mse_ssf=0.00e+00 < mse_scalar=0.4518 < mse_no_scale=0.4651
```
