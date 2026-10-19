# Discovery Report: Round 334 — k-Determinantal Point Processes for Fixed-Size Subset Selection

- **Timestamp**: `2026-10-19T06:57:00Z`
- **Selected Concept**: `AIMech:KDeterminantalPointProcessesForFixedSizeSubsetSelection` (*k-Determinantal Point Processes for Fixed-Size Subset Selection*)
- **Record Path**: `data/curated/KDeterminantalPointProcessesForFixedSizeSubsetSelection.yaml`
- **Primary Source**: Alex Kulesza, Ben Taskar — *k-DPPs: Fixed-Size Determinantal Point Processes* (`https://doi.org/10.1561/2200000044`).

## Identity & Boundary Resolution

Distinct from Volume Sampling for Matrix Approximation and Projective Clustering (`AIMech:VolumeSamplingForMatrixApproximationAndProjectiveClustering`), which analyzes the multiplicative (k+1)! ||A - A_k||_F^2 row-span projection error of simplex-volume sampling for low-rank matrix approximation and projective clustering rather than conditional L-ensemble inference, quality-diversity decompositions L_{ij} = q_i phi_i^T phi_j q_j, and the elementary symmetric polynomial DP sampler of Kulesza and Taskar (2011). Also distinct from standard unconditioned DPPs, which cannot enforce a hard cardinality budget |Y| = k.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 334 k-DPPs (Kulesza & Taskar 2011): prop31_det_err=7.11e-15, max_phase1_err=5.55e-17, max_phase2_lemma21_err=2.22e-16, max_k_dpp_err=5.55e-17, std_dpp_prob_wrong_size=0.6385
```
