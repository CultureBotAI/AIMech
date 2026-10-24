# Discovery Report: Round 421 — Deep Gradient Compression (DGC with Momentum Correction and Momentum Factor Masking)

- **Timestamp**: `2026-10-19T08:24:00Z`
- **Selected Concept**: `AIMech:DeepGradientCompressionWithMomentumCorrection` (*Deep Gradient Compression (DGC with Momentum Correction and Momentum Factor Masking)*)
- **Record Path**: `data/curated/DeepGradientCompressionWithMomentumCorrection.yaml`
- **Primary Source**: Yujun Lin, Song Han, Huizi Mao, Yu Wang, William J. Dally — *Deep Gradient Compression: Reducing the Communication Bandwidth for Distributed Training* (`https://openreview.net/forum?id=SkhQHMW0W`).

## Identity & Boundary Resolution

Distinct from vanilla error-compensated Top-k SGD (AIMech:SparsifiedSgdWithErrorMemoryForKContractiveGradientCompression, Stich, Cordonnier, & Jaggi 2018), which analyses momentum-free local error memory e_{t+1} = e_t + eta g_t - C(e_t + eta g_t) without Momentum Correction (Eq. 6) or Momentum Factor Masking (Eq. 8).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 421 Deep Gradient Compression (Lin et al. 2018): disp_dense=-0.154403 == disp_dgc=-0.154403 (err=0.0e+00), naive_err=0.090403 > 0, masked_residual=0.0 vs unmasked_phantom_velocity=0.4856
```
