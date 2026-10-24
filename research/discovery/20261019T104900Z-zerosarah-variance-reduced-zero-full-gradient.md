# Discovery Report: Round 566 — ZeroSARAH and D-ZeroSARAH Variance-Reduced Nonconvex Optimization without Full Gradient Computations

- **Timestamp**: `2026-10-19T10:49:00Z`
- **Selected Concept**: `AIMech:ZeroSarahAndDZeroSarahVarianceReducedNonconvexOptimizationWithoutFullGradientComputations` (*ZeroSARAH and D-ZeroSARAH Variance-Reduced Nonconvex Optimization without Full Gradient Computations*)
- **Record Path**: `data/curated/ZeroSarahAndDZeroSarahVarianceReducedNonconvexOptimizationWithoutFullGradientComputations.yaml`
- **Primary Source**: Zhize Li, Slavomír Hanzely, Peter Richtárik — *ZeroSARAH: Efficient Nonconvex Finite-Sum Optimization with Zero Full Gradient Computation* (`https://api.openalex.org/works/W3135176055`).

## Identity & Boundary Resolution

Distinct from classical SARAH, SPIDER, SpiderBoost, and PAGE (which require an initial full gradient computation nabla f(x^0) and/or periodic full-batch checkpoints of cost O(n) every epoch or with probability p_k), and distinct from SAGA (which achieves O(n^{2/3}/epsilon^2) nonconvex gradient complexity rather than O(sqrt(n)/epsilon^2)): ZeroSARAH combines SARAH's recursive difference update with a SAGA-style historical table correction weighted by lambda_k = b_k / (2n) so that E_k[v^k - nabla f(x^k)] = (1 - lambda_k)(v^{k-1} - nabla f(x^{k-1})), never computing any full gradient across all iterations.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 566 ZeroSARAH verified: M=8.0000, full_grads=0, gn_init=1.822e+01 -> gn_zs=1.250e-16 << gn_sgd=5.414e-02
```
