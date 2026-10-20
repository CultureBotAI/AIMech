# Discovery Report: Round 643 — FOOF (Fast First-Order Optimizer / First-Order Gradient Descent on Neurons)

- **Timestamp**: `2026-10-19T12:06:00Z`
- **Selected Concept**: `AIMech:FoofFirstOrderOnFeaturesNeuronGradientDescentOptimization` (*FOOF (Fast First-Order Optimizer / First-Order Gradient Descent on Neurons)*)
- **Record Path**: `data/curated/FoofFirstOrderOnFeaturesNeuronGradientDescentOptimization.yaml`
- **Primary Source**: Frederik Benzing — *Gradient Descent on Neurons and its Link to Approximate Second-Order Optimization* (`https://dblp.org/rec/conf/icml/Benzing22`).

## Identity & Boundary Resolution

Distinct from K-FAC (AIMech:KfacKroneckerFactoredApproximateCurvature), which preconditions weight gradients from both sides using both the input-activation covariance factor (A A^T + lambda_A I)^{-1} and the Monte-Carlo Fisher output-gradient factor (E_F E_F^T + lambda_E I)^{-1}; FOOF completely omits the second Kronecker factor (and its extra Fisher backward pass), relying strictly on zero-th order input activations A A^T and first-order gradients A E^T. Distinct from Natural Neural Networks (Desjardins et al., 2015), which reparameterize layers via explicit singular value decompositions of centered activations rather than amortizing direct damped matrix inversions (Sigma_l + lambda I)^{-1}.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 643 FOOF verified: d_FOOF=[-0.9999999999999987, 3.9999999999999956], l_toy_step1=(9.9e-32,8.9e-31), obj_eq5_opt=1.3964, cos(KFAC,FOOF)=[0.69268, 0.91788, 1.0]
```
