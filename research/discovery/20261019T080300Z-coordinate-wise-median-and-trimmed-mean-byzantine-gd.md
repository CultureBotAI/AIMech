# Discovery Report: Round 400 — Coordinate-wise Median and Trimmed Mean Byzantine-Robust Distributed Learning

- **Timestamp**: `2026-10-19T08:03:00Z`
- **Selected Concept**: `AIMech:CoordinateWiseMedianAndTrimmedMeanByzantineRobustDistributedLearning` (*Coordinate-wise Median and Trimmed Mean Byzantine-Robust Distributed Learning*)
- **Record Path**: `data/curated/CoordinateWiseMedianAndTrimmedMeanByzantineRobustDistributedLearning.yaml`
- **Primary Source**: Dong Yin, Yudong Chen, Ramchandran Kannan, Peter Bartlett — *Byzantine-Robust Distributed Learning: Towards Optimal Statistical Rates* (`https://doi.org/10.48550/arXiv.1803.01498`).

## Identity & Boundary Resolution

Distinct from Krum and Multi-Krum (AIMech:KrumAndMultiKrumByzantineTolerantGradientDescent, which select complete worker vectors via joint d-dimensional pairwise Euclidean distances in O(m^2 d) time rather than coordinate-wise 1D order statistics in O(m log m * d) or O(m d) time) and from RFA Smoothed Weiszfeld Geometric Median (AIMech:RfaRobustFederatedAggregationSmoothedWeiszfeldGeometricMedian, which computes the rotation-equivariant l_2 geometric median iteratively rather than coordinate-separable l_1 median or trimmed mean statistics).

## Constructed Boundary & Regime Verification

```text
{
  "concept": "AIMech:CoordinateWiseMedianAndTrimmedMeanByzantineRobustDistributedLearning",
  "m_machines": 25,
  "alpha_byzantine": 0.16,
  "beta_trim": 0.2,
  "l2_error_mean_gd": 233.2659,
  "l2_error_median_gd": 0.014494,
  "l2_error_trimmed_mean_gd": 0.017624,
  "status": "VERIFIED"
}
```
