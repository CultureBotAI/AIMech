# Discovery Report: Round 588 — Shampoo (Preconditioned Stochastic Tensor Optimization)

- **Timestamp**: `2026-10-19T11:11:00Z`
- **Selected Concept**: `AIMech:ShampooPreconditionedStochasticTensorOptimization` (*Shampoo (Preconditioned Stochastic Tensor Optimization)*)
- **Record Path**: `data/curated/ShampooPreconditionedStochasticTensorOptimization.yaml`
- **Primary Source**: Vineet Gupta, Tomer Koren, Yoram Singer — *Shampoo: Preconditioned Stochastic Tensor Optimization* (`https://dblp.org/rec/conf/icml/0001KS18`).

## Identity & Boundary Resolution

Distinct from diagonal AdaGrad and Adam in that Shampoo maintains full per-mode covariance matrices H_t^i rather than purely elementwise diagonal accumulators, and distinct from full-matrix AdaGrad in that it implicitly preconditions the vectorized gradient via the Kronecker product bigotimes_{i=1}^k (H_t^i)^{1/(2k)} with O(sum_i n_i^2) storage and O(sum_i n_i^3) inversion cost instead of O(prod_i n_i^2) and O(prod_i n_i^3). Distinct from K-FAC in that Shampoo is model-oblivious and relies solely on tensor-contracted outer products of observed gradients rather than architecture-specific activation/backpropagation Fisher factorizations.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 588 Shampoo verified: lemma4_err=3.89e-16, lemma8_min_eig=9.3071e+00>=0, regret=9.7830<=121.1060
```
