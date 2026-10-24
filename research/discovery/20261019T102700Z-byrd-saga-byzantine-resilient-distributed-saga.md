# Discovery Report: Round 544 — Byrd-SAGA Byzantine-Resilient Distributed SAGA with Geometric Median Aggregation

- **Timestamp**: `2026-10-19T10:27:00Z`
- **Selected Concept**: `AIMech:ByrdSagaByzantineResilientDistributedSagaWithGeometricMedianAggregation` (*Byrd-SAGA Byzantine-Resilient Distributed SAGA with Geometric Median Aggregation*)
- **Record Path**: `data/curated/ByrdSagaByzantineResilientDistributedSagaWithGeometricMedianAggregation.yaml`
- **Primary Source**: Zhaoxian Wu, Qing Ling, Tianyi Chen, Georgios B. Giannakis — *Federated Variance-Reduced Stochastic Gradient Descent With Robustness to Byzantine Attacks* (`https://api.crossref.org/works/10.1109/TSP.2020.3012952`).

## Identity & Boundary Resolution

Distinct from standard SAGA (AIMech:SagaStochasticAverageGradientAmeliore, which uses single-machine or fragile mean aggregation and fails under a single Byzantine worker) and from Byzantine-robust SGD aggregators such as Krum, Geometric Median SGD, Bulyan (AIMech:BulyanByzantineResilientGradientAggregation), RSA (AIMech:RsaByzantineRobustStochasticAggregationForHeterogeneousDatasets), and Bucketing (AIMech:BucketingForAgnosticByzantineRobustAggregationOnHeterogeneousDatasets): Byrd-SAGA (Wu, Ling, Chen, & Giannakis, IEEE TSP 2020) couples per-worker SAGA finite-sum variance reduction with server-side geometric median aggregation so that the inner stochastic gradient variance sigma^2 vanishes along the optimization trajectory, removing the O(C_alpha^2 sigma^2 / mu^2) asymptotic error floor of Byzantine-resilient SGD.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 544 Byrd-SAGA verified: err_Byrd_SAGA=1.38e-11 << err_Byrd_SGD=1.3754 << err_SAGA_Mean=72.00
```
