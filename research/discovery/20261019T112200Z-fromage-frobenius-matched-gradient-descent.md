# Discovery Report: Round 599 — Fromage (Frobenius Matched Gradient Descent)

- **Timestamp**: `2026-10-19T11:22:00Z`
- **Selected Concept**: `AIMech:FromageFrobeniusMatchedGradientDescentOptimization` (*Fromage (Frobenius Matched Gradient Descent)*)
- **Record Path**: `data/curated/FromageFrobeniusMatchedGradientDescentOptimization.yaml`
- **Primary Source**: Jeremy Bernstein, Arash Vahdat, Yisong Yue, Ming-Yu Liu — *On the distance between two neural networks and the stability of learning* (`https://dblp.org/rec/conf/nips/BernsteinVY020`).

## Identity & Boundary Resolution

Distinct from LARS (Round 594) and LAMB (Round 593) by deriving layerwise relative step scaling from a multiplicative compositional perturbation bound on multilayer perceptrons and their layer-to-output Jacobians (Theorem 1 & Modelling Assumption 1: Deep Relative Trust) together with the exact Pythagorean normalization prefactor 1 / sqrt(1 + eta^2), eliminating weight-decay hyperparameter tuning for rescaling-invariant layers.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 599 Fromage verified: scalar_err=3.89e-16, thm1_ratio=0.0625<=1, lemma2_ok=True, ortho_err=1.54e-16, fromage_norm_drift=2.46e-15, lars_growth=1.1616, loss_fromage=9.7857e-04
```
