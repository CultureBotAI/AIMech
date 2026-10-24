# Discovery Report: Round 611 — NovoGrad

- **Timestamp**: `2026-10-19T11:34:00Z`
- **Selected Concept**: `AIMech:NovoGrad` (*NovoGrad*)
- **Record Path**: `data/curated/NovoGrad.yaml`
- **Primary Source**: Boris Ginsburg, Patrice Castonguay, Oleksii Hrinchuk, Olivier Kuchaiev, Vitaly Lavrukhin, Ryan Leary, Jason Li, Huyen Nguyen, Yang Zhang, Jonathan M. Cohen — *Stochastic Gradient Methods with Layer-wise Adaptive Moments for Training of Deep Networks* (`https://dblp.org/rec/journals/corr/abs-1905-11286.xml`).

## Identity & Boundary Resolution

Distinct from Adam and AdamW (which maintain a full per-parameter second-moment tensor v_t of dimension p^l per layer and normalize the first moment after accumulation), from LaProp (AIMech:LaProp, which normalizes coordinates before momentum using per-coordinate second moments), and from LARS/LAMB (AIMech:LARSAndLAMBLayerWiseAdaptiveRateScaling, which rescale updates by the weight-to-update trust ratio ||w^l||_2 / ||u^l||_2). NovoGrad requires only one scalar v_t^l per layer, reducing optimizer state memory from 2P to P + L floats.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 611 NovoGrad verified: t1_unit_err=1.11e-16, sngd_equiv_err=0.00e+00, spike_norm=1.154701<=cap=1.154701, mem_ratio=0.500000
```
