# Discovery Report: Round 399 — Krum and Multi-Krum Byzantine-Tolerant Gradient Descent

- **Timestamp**: `2026-10-19T08:02:00Z`
- **Selected Concept**: `AIMech:KrumAndMultiKrumByzantineTolerantGradientDescent` (*Krum and Multi-Krum Byzantine-Tolerant Gradient Descent*)
- **Record Path**: `data/curated/KrumAndMultiKrumByzantineTolerantGradientDescent.yaml`
- **Primary Source**: Peva Blanchard, El Mahdi El Mhamdi, Rachid Guerraoui, Julien Stainer — *Machine Learning with Adversaries: Byzantine Tolerant Gradient Descent* (`https://doi.org/10.48550/arXiv.1703.02757`).

## Identity & Boundary Resolution

Distinct from Coordinate-wise Median and Coordinate-wise Trimmed Mean (AIMech:CoordinateWiseMedianAndTrimmedMeanByzantineRobustDistributedLearning, which aggregate each coordinate independently in O(n d) time rather than selecting whole gradient vectors via joint d-dimensional Euclidean neighborhood distances in O(n^2 (d + log n)) time) and from RFA Smoothed Weiszfeld Geometric Median (AIMech:RfaRobustFederatedAggregationSmoothedWeiszfeldGeometricMedian, which computes an iterative smoothed l_2 geometric median across all vectors up to f < n/2 rather than selecting among submitted worker vectors for 2f + 2 < n).

## Constructed Boundary & Regime Verification

```text
{
  "concept": "AIMech:KrumAndMultiKrumByzantineTolerantGradientDescent",
  "n_workers": 11,
  "f_byzantine": 3,
  "eta_n_f": 8.3666,
  "sin_alpha_bound": 0.740959,
  "linear_avg_inner_product": -6.511023,
  "krum_inner_product": 2.568342,
  "multi_krum_inner_product": 2.568335,
  "l2_error_linear_avg": 5.67427,
  "l2_error_krum": 0.106571,
  "l2_error_multi_krum": 0.064729,
  "status": "VERIFIED"
}
```
