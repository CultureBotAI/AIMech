# Discovery Report: Round 613 — AdaMod

- **Timestamp**: `2026-10-19T11:36:00Z`
- **Selected Concept**: `AIMech:AdaMod` (*AdaMod*)
- **Record Path**: `data/curated/AdaMod.yaml`
- **Primary Source**: Jianbang Ding, Xuancheng Ren, Ruixuan Luo, Xu Sun — *An Adaptive and Momental Bound Method for Stochastic Learning* (`https://dblp.org/rec/journals/corr/abs-1910-12249.xml`).

## Identity & Boundary Resolution

Distinct from AdaBound/AMSBound (AIMech:AdaBoundAndAMSBound, which clips step sizes to a deterministic scalar schedule [eta_l(t), eta_u(t)] converging to vanilla SGD) and from RAdam (AIMech:RectifiedAdam, which uses an analytical tractable-variance switch at rho_t > 4). AdaMod preserves per-coordinate adaptive step-size heterogeneity throughout training while using the uncorrected EMA s_t = (1 - beta_3) sum_{k=0}^{t-1} beta_3^k eta_{t-k} both as an automatic early-stage warmup ramp and as a dynamic momental upper bound against anomalous gradient-induced learning-rate spikes.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 613 AdaMod verified: adam_equiv_err=0.00e+00, unrolled_err=1.36e-20, spike_lr_ratio=1.0000e-03<<1, err_adamod=6.4301e-04, var_err=0.00e+00
```
