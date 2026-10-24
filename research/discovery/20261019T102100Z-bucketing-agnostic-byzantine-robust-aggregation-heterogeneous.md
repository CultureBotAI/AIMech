# Discovery Report: Round 538 — s-Bucketing for Agnostic Byzantine-Robust Aggregation on Heterogeneous Datasets

- **Timestamp**: `2026-10-19T10:21:00Z`
- **Selected Concept**: `AIMech:BucketingForAgnosticByzantineRobustAggregationOnHeterogeneousDatasets` (*s-Bucketing for Agnostic Byzantine-Robust Aggregation on Heterogeneous Datasets*)
- **Record Path**: `data/curated/BucketingForAgnosticByzantineRobustAggregationOnHeterogeneousDatasets.yaml`
- **Primary Source**: Sai Praneeth Karimireddy, Lie He, Martin Jaggi — *Byzantine-Robust Learning on Heterogeneous Datasets via Bucketing* (`https://dblp.org/rec/conf/iclr/KarimireddyHJ22.xml`).

## Identity & Boundary Resolution

Distinct from DETOX (AIMech:DetoxRedundancyBasedHierarchicalByzantineRobustGradientAggregation, which assigns redundant data partitions to fixed worker groups in an IID cloud setting and takes within-group majority/mean over identical gradients) and from unbucketed Krum (AIMech:KrumAndMultiKrumByzantineResilientGradientAggregation), Coordinate-Wise Median (AIMech:CoordinateWiseMedianAndTrimmedMeanByzantineRobustGradientAggregation), and RFA (AIMech:RobustFederatedAggregationViaSmoothedWeiszfeldGeometricMedian), which fail on imbalanced non-IID data even with delta = 0 Byzantine workers or under the Mimic attack (Section 3.1-3.2). Bucketing (Karimireddy, He, & Jaggi, ICLR 2022 / arXiv:2006.09365, Algorithms 1-2, Lemma 1, Definition A, Theorems I-IV, pp. 4-8) randomly reshuffles the n worker momentum vectors m_i^t = beta m_i^{t-1} + (1 - beta) g_i(x^{t-1}) via a fresh random permutation pi of [n] at every step, computes bucket averages y_i = (1/s) sum_{k=(i-1)s+1}^{min(n, i s)} m_{pi(k)}^t for i = 1, ..., ceil(n/s), and outputs hat{m} = AGGR(y_1, ..., y_{ceil(n/s)}) with bucket size s = floor(delta_{max} / delta).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 538 Bucketing verified: raw_var=10.91->bucket_var=3.70 (s=3), err_cm_unbucketed=2.00->bucketed=0.035, err_krum_unbucketed=2.00->bucketed=0.673
```
