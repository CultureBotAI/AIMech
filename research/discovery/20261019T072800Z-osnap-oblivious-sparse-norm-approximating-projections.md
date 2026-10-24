# Discovery Report: Round 365 — Oblivious Sparse Norm-Approximating Projections (OSNAP) for Fast Numerical Linear Algebra

- **Timestamp**: `2026-10-19T07:28:00Z`
- **Selected Concept**: `AIMech:ObliviousSparseNormApproximatingProjectionsForNumericalLinearAlgebra` (*Oblivious Sparse Norm-Approximating Projections (OSNAP) for Fast Numerical Linear Algebra*)
- **Record Path**: `data/curated/ObliviousSparseNormApproximatingProjectionsForNumericalLinearAlgebra.yaml`
- **Primary Source**: Jelani Nelson, Huy L. Nguyen — *OSNAP: Faster numerical linear algebra algorithms via sparser subspace embeddings* (`https://api.crossref.org/works/10.1109/focs.2013.21`).

## Identity & Boundary Resolution

Distinct from AIMech:ProjectionCostPreservingSketchesForKMeansAndConstrainedLowRankApproximation (Round 364), which preserves rank-k left projection costs ||(I - P)A||_F^2 + c in O(k/varepsilon^2) dimensions (and uses OSNAP as an underlying sketching primitive), whereas OSNAP is a sparse oblivious subspace embedding preserving ||Pi U y||_2 in (1 +- varepsilon)*||y||_2 for all y in R^d simultaneously—equivalently bounding all singular values of Pi U in [1 - varepsilon, 1 + varepsilon] via a Bai-Yin moment method on generalized dot-product multigraphs. Also distinct from AIMech:FrequentDirectionsDeterministicMatrixSketching (Round 363), which is a deterministic SVD-shrinkage sketch requiring O(n*d*ell) time rather than O(s*nnz(A)) sparse hashing time.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 365 OSNAP Sparse Subspace Embeddings (Nelson & Nguyen 2013): max_eq3_err=9.99e-16, theo_l2=0.6325<=0.7500, emp_s1=0.6223, m4_s4=0.1226<<m4_s1=0.4233
```
