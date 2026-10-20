# Discovery Report: Round 597 — AdEMAMix (Adaptive EMA Mixture Optimizer)

- **Timestamp**: `2026-10-19T11:20:00Z`
- **Selected Concept**: `AIMech:AdEMAMixAdaptiveEMAMixtureOptimization` (*AdEMAMix (Adaptive EMA Mixture Optimizer)*)
- **Record Path**: `data/curated/AdEMAMixAdaptiveEMAMixtureOptimization.yaml`
- **Primary Source**: Matteo Pagliardini, Pierre Ablin, David Grangier — *The AdEMAMix Optimizer: Better, Faster, Older* (`https://dblp.org/rec/conf/iclr/PagliardiniAG25`).

## Identity & Boundary Resolution

Distinct from standard AdamW in that a single EMA cannot simultaneously assign high weight to recent gradients and non-negligible weight to gradients thousands of steps old; AdEMAMix maintains two separate first-moment buffers m_1 and m_2 (or sets beta_1 = 0 so m_hat_1^(t) = g^(t) without extra memory) and schedules beta_3^(t) = exp(ln(beta_start) ln(beta_3) / ((1 - t/T) ln(beta_3) + (t/T) ln(beta_start))). Distinct from nested-EMA methods (DEMA, AdMeta) which attenuate rather than preserve very old gradients.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 597 AdEMAMix verified: halflife_lin_err=4.40e-13 (t_half: 5.6->6930.1), dist_ade=3.7582e-02<<dist_adam=8.5933e-01
```
