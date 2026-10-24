# Discovery Report: Round 402 — RFA Robust Federated Aggregation via Smoothed Weiszfeld Geometric Median

- **Timestamp**: `2026-10-19T08:05:00Z`
- **Selected Concept**: `AIMech:RfaRobustFederatedAggregationSmoothedWeiszfeldGeometricMedian` (*RFA Robust Federated Aggregation via Smoothed Weiszfeld Geometric Median*)
- **Record Path**: `data/curated/RfaRobustFederatedAggregationSmoothedWeiszfeldGeometricMedian.yaml`
- **Primary Source**: Krishna Pillutla, Sham M. Kakade, Zaid Harchaoui — *Robust Aggregation for Federated Learning* (`https://doi.org/10.1109/TSP.2022.3153135`).

## Identity & Boundary Resolution

Distinct from Coordinate-wise Median and Trimmed Mean (AIMech:CoordinateWiseMedianAndTrimmedMeanByzantineRobustDistributedLearning, which compute coordinate-separable l_1 medians or trimmed means that cannot be implemented via a small number of linear Secure Aggregation sum queries and lack rotation equivariance) and from Krum (AIMech:KrumAndMultiKrumByzantineTolerantGradientDescent, which requires server inspection of all O(m^2) pairwise client model distances, incompatible with cryptographic Secure Average oracles).

## Constructed Boundary & Regime Verification

```text
{
  "concept": "AIMech:RfaRobustFederatedAggregationSmoothedWeiszfeldGeometricMedian",
  "m_clients": 15,
  "rho_corruption": 0.4,
  "nu_smoothing": 0.05,
  "g_nu_initial": 30.603243,
  "g_nu_final": 30.159309,
  "round0_max_normalized_weight": 0.116326,
  "proposition3_upper_bound": 0.99067,
  "l2_error_rfa": 0.100707,
  "l2_error_fedavg": 30.128965,
  "status": "VERIFIED"
}
```
