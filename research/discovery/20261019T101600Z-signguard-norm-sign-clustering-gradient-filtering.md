# Discovery Report: Round 533 — SignGuard Norm-Based and Sign-Clustering Malicious Gradient Filtering

- **Timestamp**: `2026-10-19T10:16:00Z`
- **Selected Concept**: `AIMech:SignGuardNormAndSignClusteringMaliciousGradientFiltering` (*SignGuard Norm-Based and Sign-Clustering Malicious Gradient Filtering*)
- **Record Path**: `data/curated/SignGuardNormAndSignClusteringMaliciousGradientFiltering.yaml`
- **Primary Source**: Jian Xu, Shao-Lun Huang, Linqi Song, Tian Lan — *Byzantine-robust Federated Learning through Collaborative Malicious Gradient Filtering* (`https://dblp.org/rec/journals/corr/abs-2109-05872.xml`).

## Identity & Boundary Resolution

Distinct from SignSGD with majority vote (AIMech:SignSgdCompressedOptimisationWithMajorityVote, which transmits 1-bit gradient signs without full-precision norm filtering or clustering), from Robust Learning Rate / RLR (AIMech:RlrRobustLearningRateSignVotingBackdoorDefenseForFederatedLearning, which flips coordinate-wise server learning rates based on a sign-sum threshold theta), from Centered Clipping (AIMech:CenteredClippingIterativeByzantineRobustAggregationWithMomentum), and from FLAME (AIMech:FlameDynamicClusteringAndAdaptiveClippingNoisingBackdoorDefense, which applies HDBSCAN to pairwise cosine distances and adds differential-privacy noise). SignGuard (Xu et al., ICDCS 2022 / arXiv:2109.05872, Algorithm 2, p. 5) operates in three stages: (1) Norm-based Filtering computes the median Euclidean norm M = med({||g_t^(i)||_2}_{i=1}^n) and admits the candidate set S_1 = {i in [n] : L <= ||g_t^(i)||_2 / M <= R} (with default bounds L = 0.1, R = 3.0) to eliminate extreme high-norm and near-zero gradient outliers; (2) Sign-based Clustering samples a random subset of gradient coordinates to form a low-dimensional normalized sign-proportion feature vector v_i = [p_i^+, p_i^0, p_i^-] counting positive, zero, and negative gradient entries (augmented in SignGuard-Sim and SignGuard-Dist with cosine or Euclidean similarity to a reference gradient), and partitions clients via Mean-Shift or K-Means clustering to select the largest cluster S_2; and (3) Median-Clipped Intersection Aggregation forms the trusted set S_t' = S_1 cap S_2 and outputs tilde{g}_t = (1 / |S_t'|) sum_{i in S_t'} g_t^(i) * min(1, M / ||g_t^(i)||_2).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 533 SignGuard verified: S1=[0, 1, 2, 3, 4, 5, 6, 7], S2=[0, 1, 2, 3, 4, 5, 8, 9], S_trusted=[0, 1, 2, 3, 4, 5], err_sg=0.0978 << err_norm_only=1.4948 << err_sign_only=14.7531
```
