# Discovery Report: Round 648 — TONGA Topmoumoute Online Natural Gradient Optimization

- **Timestamp**: `2026-10-19T12:11:00Z`
- **Selected Concept**: `AIMech:TongaTopmoumouteOnlineNaturalGradientOptimization` (*TONGA Topmoumoute Online Natural Gradient Optimization*)
- **Record Path**: `data/curated/TongaTopmoumouteOnlineNaturalGradientOptimization.yaml`
- **Primary Source**: Nicolas Le Roux, Pierre-Antoine Manzagol, Yoshua Bengio — *Topmoumoute online natural gradient algorithm* (`https://dblp.org/rec/conf/nips/RouxMB07`).

## Identity & Boundary Resolution

Distinct from exact Natural Gradient Descent (AIMech:NaturalGradientDescent), which requires O(p^2) covariance storage and O(n p^2 + p^3) inversion; distinct from Kronecker-factored natural gradient methods (AIMech:KFAC, AIMech:EKFACEigenvalueCorrectedKroneckerFactorizationNaturalGradient, AIMech:TensorNormalTrainingKroneckerNaturalGradientOptimization), which factorize layer curvature as Kronecker products of activations and pre-activation derivatives; and distinct from Frequent Directions sketching of AdaGrad/Shampoo preconditioners (AIMech:SketchyFrequentDirectionsAdaptiveRegularizationOptimization), which subtracts the l-th singular value squared sigma_l^2 I_r during streaming SVD updates.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 648 TONGA boundary and mathematical verification succeeded.
```
