# Discovery Report: Round 594 — LARS (Layer-wise Adaptive Rate Scaling)

- **Timestamp**: `2026-10-19T11:17:00Z`
- **Selected Concept**: `AIMech:LARSLayerwiseAdaptiveRateScaling` (*LARS (Layer-wise Adaptive Rate Scaling)*)
- **Record Path**: `data/curated/LARSLayerwiseAdaptiveRateScaling.yaml`
- **Primary Source**: Yang You, Igor Gitman, Boris Ginsburg — *Large Batch Training of Convolutional Networks* (`https://dblp.org/rec/journals/corr/abs-1708-03888`).

## Identity & Boundary Resolution

Distinct from coordinatewise adaptive optimizers such as Adam, RMSProp, and AdaGrad in that LARS computes a single scalar learning rate lambda^l per layer rather than per weight and scales the update magnitude proportionally to the layer's weight norm ||w_t^l||_2. Distinct from LAMB in that LARS normalizes raw or momentum gradients by their layerwise l2 norm without coordinatewise second-moment preconditioning 1 / sqrt(v_hat_t).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 594 LARS verified: sgd_rel=(1.73, 0.0078) vs lars_rel=0.2000, lars_loss=6.5706e-01<<init_loss=9.7212e+02
```
