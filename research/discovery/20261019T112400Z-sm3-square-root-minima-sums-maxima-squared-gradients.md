# Discovery Report: Round 601 — SM3 (Square-root of Minima of Sums of Maxima of Squared-gradients Method)

- **Timestamp**: `2026-10-19T11:24:00Z`
- **Selected Concept**: `AIMech:SM3SquareRootMinimaSumsMaximaSquaredGradientsOptimization` (*SM3 (Square-root of Minima of Sums of Maxima of Squared-gradients Method)*)
- **Record Path**: `data/curated/SM3SquareRootMinimaSumsMaximaSquaredGradientsOptimization.yaml`
- **Primary Source**: Rohan Anil, Vineet Gupta, Tomer Koren, Yoram Singer — *Memory-Efficient Adaptive Optimization* (`https://dblp.org/rec/conf/nips/Anil0KS19`).

## Identity & Boundary Resolution

Distinct from Adafactor and CAME (Round 598), which factorize matrix second moments via rank-1 non-negative matrix factorization and act as fixed-learning-rate Adam variants, SM3 applies to arbitrary-order tensors (or any parameter cover) by maintaining O(k) set-level upper-bound accumulators that Sandwich AdaGrad's cumulative squared gradients (sum_{s=1}^t g_s^2(i) <= nu'_t(i) <= nu_t(i)) and enjoy provable online convex regret guarantees.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 601 SM3 verified: nu2_vs_nu1=0.9493<1, row_tied_err=0.00e+00, gamma_vs_nu2=0.6969, mem_ratio=0.000732, regret_ratio=0.1286<=1.0
```
