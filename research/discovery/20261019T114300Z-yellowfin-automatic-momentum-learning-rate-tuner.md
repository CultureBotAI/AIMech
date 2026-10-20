# Discovery Report: Round 620 — YellowFin Automatic Momentum and Learning Rate Tuner

- **Timestamp**: `2026-10-19T11:43:00Z`
- **Selected Concept**: `AIMech:YellowFinAutomaticMomentumAndLearningRateTuner` (*YellowFin Automatic Momentum and Learning Rate Tuner*)
- **Record Path**: `data/curated/YellowFinAutomaticMomentumAndLearningRateTuner.yaml`
- **Primary Source**: Jian Zhang, Ioannis Mitliagkas, Christopher Ré — *YellowFin and the Art of Momentum Tuning* (`https://dblp.org/rec/conf/mlsys/ZhangM19`).

## Identity & Boundary Resolution

Distinct from per-coordinate adaptive learning-rate methods (AdaGrad, RMSProp, Adam) and from Lookahead or SWATS: YellowFin tunes a single global learning rate alpha_t and a single global Polyak momentum parameter mu_t at every step by enforcing the momentum operator's robust-region invariants (1 - sqrt(mu_t))^2 <= alpha_t h <= (1 + sqrt(mu_t))^2 across the dynamic range nu = h_max / h_min of generalized curvatures so that the bias operator A_t has homogeneous spectral radius sqrt(mu_t) and the variance operator B_t has spectral radius mu_t.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 620 YellowFin verified: rhoA_err=1.11e-16, rhoB_err=5.55e-17, mse_rec_err=0.00e+00, cubic_res=1.33e-15, mu_opt=0.5102, alpha_opt=0.1633, closed_loop_err_ratio=3.51e-05
```
