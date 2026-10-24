# Discovery Report: Round 645 — Sketchy (Frequent-Directions Sketched Adaptive Regularization / S-AdaGrad and S-Shampoo)

- **Timestamp**: `2026-10-19T12:08:00Z`
- **Selected Concept**: `AIMech:SketchyFrequentDirectionsAdaptiveRegularizationOptimization` (*Sketchy (Frequent-Directions Sketched Adaptive Regularization / S-AdaGrad and S-Shampoo)*)
- **Record Path**: `data/curated/SketchyFrequentDirectionsAdaptiveRegularizationOptimization.yaml`
- **Primary Source**: Vladimir Feinberg, Xinyi Chen, Y. Jennifer Sun, Rohan Anil, Elad Hazan — *Sketchy: Memory-efficient Adaptive Regularization with Frequent Directions* (`https://dblp.org/rec/conf/nips/FeinbergCSAH23`).

## Identity & Boundary Resolution

Distinct from Shampoo (AIMech:ShampooPreconditionedStochasticTensorOptimization), which materializes full m x m and n x n left and right Kronecker covariance factors in O(m^2 + n^2) memory. Distinct from GGT (AIMech:GgtEfficientFullMatrixAdaptiveRegularization), which stores a sliding window of r full-model gradient copies in O(m n r) superlinear memory. Distinct from Ada-FD and FD-SON, which add a static diagonal perturbation delta I rather than the dynamic cumulative escaped spectral mass rho_{1:t} I and suffer Omega(T^{3/4}) or Omega(T) worst-case regret on general online convex problems.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 645 Sketchy verified: op_err=4.1052<=rho_1:T=4.1060<=Omega_l=4.1233<=tail=4.1233, mem_ratio(S-Shampoo/Adam)=0.3125, mem_ratio(S-Shampoo/Shampoo)=0.0735
```
