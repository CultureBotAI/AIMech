# Discovery Report: Round 630 — 1-bit LAMB (Error-Compensated LAMB-Preconditioned Large-Batch Compressed Optimization)

- **Timestamp**: `2026-10-19T11:53:00Z`
- **Selected Concept**: `AIMech:OneBitLambAdaptiveLayerwiseCompressedTraining` (*1-bit LAMB (Error-Compensated LAMB-Preconditioned Large-Batch Compressed Optimization)*)
- **Record Path**: `data/curated/OneBitLambAdaptiveLayerwiseCompressedTraining.yaml`
- **Primary Source**: Conglong Li, Ammar Ahmad Awan, Hanlin Tang, Samyam Rajbhandari, Yuxiong He — *1-bit LAMB: Communication Efficient Large-Scale Large-Batch Training with LAMB's Convergence Speed* (`https://dblp.org/rec/conf/hipc/LiATRH22`).

## Identity & Boundary Resolution

Distinct from uncompressed LAMB (AIMech:LAMBLayerwiseAdaptiveMomentsBatchOptimization, You et al. 2020), which requires full-precision gradient allreduce and up-to-date uncompressed momentum and variance to compute layerwise trust ratios c_t^{(l)} = clip(||x_{t-1}^{(l)}|| / ||u_t^{(l)}||, c_min, c_max). Distinct from 1-bit Adam (AIMech:OneBitAdamErrorCompensatedPreconditionedMomentum, Tang et al. 2021), which freezes variance globally without layerwise scaling or fresh-variance tracking and suffers convergence degradation at large batch sizes (16K-64K), and from naive 'LAMB + basic 1-bit' (Section 3.4), which freezes both variance and c_t^{(l)} and degrades accuracy because LAMB's per-layer variance norms decay by up to two orders of magnitude during training.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 630 1-bit LAMB verified: rec_err=3.89e-16, r_last=1.0145, c_final=0.1826, id_err=6.94e-18, red_128=4.57x, red_512=4.11x
```
