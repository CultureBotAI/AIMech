# Discovery Report: Round 649 — LocoProp Layerwise Local Loss Backpropagation Optimization

- **Timestamp**: `2026-10-19T12:12:00Z`
- **Selected Concept**: `AIMech:LocoPropLayerwiseLocalLossBackpropagationOptimization` (*LocoProp Layerwise Local Loss Backpropagation Optimization*)
- **Record Path**: `data/curated/LocoPropLayerwiseLocalLossBackpropagationOptimization.yaml`
- **Primary Source**: Ehsan Amid, Rohan Anil, Manfred K. Warmuth — *LocoProp: Enhancing BackProp via Local Loss Optimization* (`https://dblp.org/rec/conf/aistats/AmidAW22`).

## Identity & Boundary Resolution

Distinct from Kronecker-factored second-order optimizers (AIMech:KFAC, AIMech:Shampoo), which explicitly store O(sum_i d_i^2) covariance matrices and compute O(sum_i d_i^3) matrix inverses or inverse p-th roots; and distinct from First-Order-On-Features (AIMech:FoofFirstOrderOnFeaturesNeuronGradientDescentOptimization), which explicitly maintains and inverts an exponentially averaged input activation covariance matrix (A_l + lambda I)^{-1} rather than running T iterative first-order steps on a layerwise Bregman matching loss.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 649 LocoProp boundary and mathematical verification succeeded.
```
