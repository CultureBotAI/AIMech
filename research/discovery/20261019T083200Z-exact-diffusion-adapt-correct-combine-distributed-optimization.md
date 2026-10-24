# Discovery Report: Round 429 — Exact Diffusion (Adapt-Correct-Combine Distributed Optimization)

- **Timestamp**: `2026-10-19T08:32:00Z`
- **Selected Concept**: `AIMech:ExactDiffusionAdaptCorrectCombineDistributedOptimization` (*Exact Diffusion (Adapt-Correct-Combine Distributed Optimization)*)
- **Record Path**: `data/curated/ExactDiffusionAdaptCorrectCombineDistributedOptimization.yaml`
- **Primary Source**: Kun Yuan, Bicheng Ying, Xiaochuan Zhao, Ali H. Sayed — *Exact Diffusion for Distributed Optimization and Learning — Part I: Algorithm Development* (`https://doi.org/10.1109/TSP.2018.2875898`).

## Identity & Boundary Resolution

Distinct from EXTRA (Shi et al. 2015) and D2 (AIMech:D2VarianceReducedDecentralizedTrainingOverHeterogeneousData, Tang et al. 2018), which apply a Combine-Then-Adapt (CTA) update without mixing the gradient difference through bar_A^T and require symmetric doubly stochastic matrices, whereas Exact Diffusion uses an Adapt-Then-Combine structure W_i = bar_A^T (2 W_{i-1} - W_{i-2} - M(nabla J^o(W_{i-1}) - nabla J^o(W_{i-2}))) (Eq. 103) that operates directly on non-symmetric locally balanced left-stochastic combination policies without known Perron eigenvectors when q_k = p_k.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 429 Exact Diffusion (Yuan et al. 2019): p_inv_err=1.29e-16, ed_err_sq=2.44e-31 vs atc_bias_sq=0.4740, non_balanced_imbalance=0.2028
```
