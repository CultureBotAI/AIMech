# Discovery Report: Round 364 — Projection-Cost Preserving Sketches for k-Means Clustering and Constrained Low-Rank Approximation

- **Timestamp**: `2026-10-19T07:27:00Z`
- **Selected Concept**: `AIMech:ProjectionCostPreservingSketchesForKMeansAndConstrainedLowRankApproximation` (*Projection-Cost Preserving Sketches for k-Means Clustering and Constrained Low-Rank Approximation*)
- **Record Path**: `data/curated/ProjectionCostPreservingSketchesForKMeansAndConstrainedLowRankApproximation.yaml`
- **Primary Source**: Michael B. Cohen, Sam Elder, Cameron Musco, Christopher Musco, Madalina Persu — *Dimensionality Reduction for k-Means Clustering and Low Rank Approximation* (`https://api.crossref.org/works/10.1145/2746539.2746569`).

## Identity & Boundary Resolution

Distinct from AIMech:FrequentDirectionsDeterministicMatrixSketching (Round 363), which compresses n rows into ell rows in R^{ell x d} to approximate the row space A^T A in row-update streams, whereas a Projection-Cost Preserving Sketch reduces column dimension from d to d' = O(k/epsilon) or O(k/epsilon^2) in R^{n x d'} so that left rank-k projections P in R^{n x n} (such as k-means cluster indicator projections X_C X_C^T) preserve ||(I - P)A||_F^2 up to a P-independent shift c. Also distinct from AIMech:KMeansPlusPlusSeeding (Round 194), which seeds k-means cluster centers in the ambient dimension d rather than reducing feature dimension d' prior to clustering.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 364 Projection-Cost Preserving Sketches (Cohen et al. 2015): min_one_sided_diff=1.57e-01>=0, max_rel_err=0.0308<=0.50, eq10_err=7.11e-15, eq27_margin=3.2345>=0
```
