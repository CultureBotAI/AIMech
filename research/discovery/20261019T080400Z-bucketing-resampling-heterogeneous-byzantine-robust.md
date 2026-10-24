# Discovery Report: Round 401 — Bucketing Resampling for Heterogeneous Byzantine-Robust Optimization

- **Timestamp**: `2026-10-19T08:04:00Z`
- **Selected Concept**: `AIMech:BucketingResamplingForHeterogeneousByzantineRobustOptimization` (*Bucketing Resampling for Heterogeneous Byzantine-Robust Optimization*)
- **Record Path**: `data/curated/BucketingResamplingForHeterogeneousByzantineRobustOptimization.yaml`
- **Primary Source**: Sai Praneeth Karimireddy, Lie He, Martin Jaggi — *Byzantine-Robust Learning on Heterogeneous Datasets via Bucketing* (`https://doi.org/10.48550/arXiv.2006.09365`).

## Identity & Boundary Resolution

Distinct from standalone Krum (AIMech:KrumAndMultiKrumByzantineTolerantGradientDescent), Coordinate-wise Median (AIMech:CoordinateWiseMedianAndTrimmedMeanByzantineRobustDistributedLearning), and RFA (AIMech:RfaRobustFederatedAggregationSmoothedWeiszfeldGeometricMedian), all of which fail under inter-client data heterogeneity and the Mimic attack with Omega(rho^2) bias when applied directly to unbucketed worker vectors, and from Centered Clipping (AIMech:CenteredClippingAndWorkerMomentumForByzantineRobustOptimization, which is an iterative clipping rule requiring a clipping radius tau rather than a black-box resampling meta-wrapper).

## Constructed Boundary & Regime Verification

```text
{
  "concept": "AIMech:BucketingResamplingForHeterogeneousByzantineRobustOptimization",
  "s_bucket_size": 2,
  "pairwise_variance_raw": 33.6729,
  "pairwise_variance_bucketed": 17.3067,
  "mimic_mse_krum_raw": 15.4484,
  "mimic_mse_krum_bucketed": 1.1756,
  "mimic_mse_cm_raw": 14.9509,
  "mimic_mse_cm_bucketed": 0.0011,
  "status": "VERIFIED"
}
```
