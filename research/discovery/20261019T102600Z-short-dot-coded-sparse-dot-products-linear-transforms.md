# Discovery Report: Round 543 — Short-Dot Coded Sparse Dot Products for Straggler-Resilient Linear Transforms

- **Timestamp**: `2026-10-19T10:26:00Z`
- **Selected Concept**: `AIMech:ShortDotCodedSparseDotProductsForStragglerResilientLinearTransforms` (*Short-Dot Coded Sparse Dot Products for Straggler-Resilient Linear Transforms*)
- **Record Path**: `data/curated/ShortDotCodedSparseDotProductsForStragglerResilientLinearTransforms.yaml`
- **Primary Source**: Sanghamitra Dutta, Viveck Cadambe, Pulkit Grover — *"Short-Dot": Computing Large Linear Transforms Distributedly Using Coded Short Dot Products* (`https://dblp.org/rec/journals/tit/DuttaCG19`).

## Identity & Boundary Resolution

Distinct from Maximum Distance Separable (MDS) coded matrix-vector multiplication (Lee et al., 2015/2018, which requires K = M processors to finish but forces every processor to store and compute a full N-length dot product) and from Polynomial / MatDot / Entangled Polynomial Codes (AIMech:PolynomialCodesForStragglerResilientHighDimensionalCodedMatrixMultiplication, AIMech:MatDotAndPolyDotCodesForStragglerResilientCodedMatrixMultiplication, AIMech:EntangledPolynomialCodesForStragglerResilientDistributedMatrixMultiplication, which encode dense block submatrices of two matrices A and B): Short-Dot (Dutta, Cadambe, & Grover, NeurIPS 2016 / IEEE TIT 2019) jointly encodes M rows into P sparse vectors of length s = (N/P)(P - K + M) by solving for K - M padded rows Z that annihilate cyclic (K - M)-subsets of rows in B A_tilde, trading a slightly higher recovery threshold K >= M for shorter per-worker dot products, reduced worker memory, and reduced input communication.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 543 Short-Dot verified: row_sparsity=8/12, max_err=5.39e-12 across all 15 K-subsets, E[T_SD]/N=0.500 < E[T_MDS]/N=1.078
```
