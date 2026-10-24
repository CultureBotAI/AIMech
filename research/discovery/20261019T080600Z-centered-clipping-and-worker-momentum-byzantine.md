# Discovery Report: Round 403 — Centered Clipping and Worker Momentum for Byzantine-Robust Optimization

- **Timestamp**: `2026-10-19T08:06:00Z`
- **Selected Concept**: `AIMech:CenteredClippingAndWorkerMomentumForByzantineRobustOptimization` (*Centered Clipping and Worker Momentum for Byzantine-Robust Optimization*)
- **Record Path**: `data/curated/CenteredClippingAndWorkerMomentumForByzantineRobustOptimization.yaml`
- **Primary Source**: Sai Praneeth Karimireddy, Lie He, Martin Jaggi — *Learning from History for Byzantine Robust Optimization* (`https://doi.org/10.48550/arXiv.2012.10333`).

## Identity & Boundary Resolution

Distinct from memoryless middle-seeking aggregators such as Krum (AIMech:KrumAndMultiKrumByzantineTolerantGradientDescent), Coordinate-wise Median (AIMech:CoordinateWiseMedianAndTrimmedMeanByzantineRobustDistributedLearning), and RFA (AIMech:RfaRobustFederatedAggregationSmoothedWeiszfeldGeometricMedian), which Theorem I and Counterexamples 1-3 prove can fail to converge even with zero Byzantine workers (delta = 0) under asymmetric/bimodal stochastic gradient noise and suffer an Omega(delta * sigma^2 / mu^2) lower bound under time-coupled attacks (Theorem II), and from Bucketing (AIMech:BucketingResamplingForHeterogeneousByzantineRobustOptimization, which addresses inter-client data heterogeneity via random s-bucketing rather than intra-client stochastic noise via centered clipping).

## Constructed Boundary & Regime Verification

```text
{
  "concept": "AIMech:CenteredClippingAndWorkerMomentumForByzantineRobustOptimization",
  "counterexample1_true_mean": 0.0,
  "counterexample1_median": -1.0,
  "n_workers": 20,
  "delta_byzantine": 0.1,
  "alpha_momentum": 0.15,
  "tau_clip_radius": 0.35,
  "l2_error_momentum_centered_clipping": 0.077992,
  "l2_error_unclipped_mean": 5.555709,
  "status": "VERIFIED"
}
```
