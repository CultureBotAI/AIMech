# Discovery Report: Round 602 — Adan (Adaptive Nesterov Momentum Algorithm)

- **Timestamp**: `2026-10-19T11:25:00Z`
- **Selected Concept**: `AIMech:AdanAdaptiveNesterovMomentumAlgorithm` (*Adan (Adaptive Nesterov Momentum Algorithm)*)
- **Record Path**: `data/curated/AdanAdaptiveNesterovMomentumAlgorithm.yaml`
- **Primary Source**: Xingyu Xie, Pan Zhou, Huan Li, Zhouchen Lin, Shuicheng Yan — *Adan: Adaptive Nesterov Momentum Algorithm for Faster Optimizing Deep Models* (`https://dblp.org/rec/journals/pami/XieZLLY24`).

## Identity & Boundary Resolution

Distinct from Nadam (Dozat 2016), AdamW (Loshchilov and Hutter 2019), Lion (AIMech:LionEvoSignMomentumOptimizer), and AdEMAMix (AIMech:AdEMAMixDualExponentialMovingAverageOptimizer): Adan derives its update from an algebraic rearrangement of Nesterov's extrapolated gradient (Lemma 1, Eq. 4) that maintains a dedicated gradient-difference EMA v_k with its own decay coefficient beta_2, preconditioning the combined vector m_k + (1 - beta_2) v_k by the RMS of the composite Nesterov perturbation g_k + (1 - beta_2)(g_k - g_{k-1}) and applying exact proximal scaling (1 + lambda_k eta)^{-1} for decoupled L2 regularization.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 602 Adan verified: lemma1_err=4.44e-16, eq4_err=1.67e-16, prox_err=1.64e-14, prop3_ratio=0.0001<=1, loss_adan=6.5814e-05<loss_adamw=1.6414e-04
```
