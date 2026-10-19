# Discovery Report: Round 335 — Volume Sampling for Matrix Approximation and Projective Clustering

- **Timestamp**: `2026-10-19T06:58:00Z`
- **Selected Concept**: `AIMech:VolumeSamplingForMatrixApproximationAndProjectiveClustering` (*Volume Sampling for Matrix Approximation and Projective Clustering*)
- **Record Path**: `data/curated/VolumeSamplingForMatrixApproximationAndProjectiveClustering.yaml`
- **Primary Source**: Amit Deshpande, Luis Rademacher, Santosh Vempala, Grant Wang — *Matrix Approximation and Projective Clustering via Volume Sampling* (`https://doi.org/10.4086/toc.2006.v002a012`).

## Identity & Boundary Resolution

Distinct from Relative-Error CUR Matrix Decomposition via Subspace Leverage Sampling (`AIMech:RelativeErrorCURMatrixDecompositionViaSubspaceLeverageSampling`), which samples O(k log k / epsilon^2) columns/rows i.i.d. using precomputed SVD leverage scores rather than joint k-subset volume sampling of exactly k rows with multiplicative factor (k + 1), and from k-Determinantal Point Processes for Fixed-Size Subset Selection (`AIMech:KDeterminantalPointProcessesForFixedSizeSubsetSelection`), which addresses exact two-phase sampling and conditional L-ensemble inference in machine learning rather than the Cauchy-Binet ratio bound E[||A - pi_{H_S}(A)||_F^2] <= (k+1)||A - A_k||_F^2, Proposition 4.1 simplex lower bound, and projective clustering PTAS of Deshpande et al. (2006).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 335 Volume Sampling (Deshpande et al. 2006): lemma33_k_err=2.84e-14, eq37_err=4.44e-15, exp_frob_sq=6.9575 <= thm12_bound=11.0734, tight_ratio=3.000000, vol_expected_err=0.00e+00
```
