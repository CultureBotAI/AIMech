# Discovery Report: Round 833 — AMIS Adaptive Multiple Importance Sampling with Past-Weight Recycling

- **Timestamp**: `2026-10-19T15:16:00Z`
- **Selected Concept**: `AIMech:AMISAdaptiveMultipleImportanceSamplingWithPastWeightRecycling` (*AMIS Adaptive Multiple Importance Sampling with Past-Weight Recycling*)
- **Record Path**: `data/curated/AMISAdaptiveMultipleImportanceSamplingWithPastWeightRecycling.yaml`
- **Primary Source**: Jean-Marie Cornuet, Jean-Michel Marin, Antonietta Mira, Christian P. Robert — *Adaptive Multiple Importance Sampling* (`https://arxiv.org/abs/0907.1254`).

## Identity & Boundary Resolution

No AIO class represents Adaptive Multiple Importance Sampling (AMIS); MarkovChain (AIO:MarkovChain) is the closest broad match covering iterative stochastic simulation and Monte Carlo sampling processes.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 833 AMIS boundary verification passed: dm_unbiased_err=1.29e-14, dm_var_ratio=0.0019, delta_rec_err=1.42e-14, omega_rec_err=4.44e-16, eval_count=2800, ess_init=400.0 (sigma=1.00), lemma1_mse=0.0032<0.3041, banana_ess=274.1>214.8, banana_mse=0.1150<0.1288
```
