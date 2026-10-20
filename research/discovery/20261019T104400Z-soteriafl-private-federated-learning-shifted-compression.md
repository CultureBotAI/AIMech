# Discovery Report: Round 561 — SoteriaFL Unified Framework for Private Federated Learning with Shifted Communication Compression

- **Timestamp**: `2026-10-19T10:44:00Z`
- **Selected Concept**: `AIMech:SoteriaFlUnifiedFrameworkForPrivateFederatedLearningWithShiftedCommunicationCompression` (*SoteriaFL Unified Framework for Private Federated Learning with Shifted Communication Compression*)
- **Record Path**: `data/curated/SoteriaFlUnifiedFrameworkForPrivateFederatedLearningWithShiftedCommunicationCompression.yaml`
- **Primary Source**: Zhize Li, Haoyu Zhao, Boyue Li, Yuejie Chi — *SoteriaFL: A Unified Framework for Private Federated Learning with Communication Compression* (`https://api.openalex.org/works/https://doi.org/10.52202/068431-0310`).

## Identity & Boundary Resolution

Distinct from naive Compressed-DP-SGD (which sets s_i^t = 0 and suffers an O((1+omega) sigma_p^2) noise amplification combined with unbounded gradient-norm variance) and from non-private DIANA / EF21. SoteriaFL (Li, Zhao, Li, & Chi, NeurIPS 2022, arXiv:2206.09888) unifies Soteria-SGD, Soteria-SVRG, and Soteria-SAGA under Lemma 1's shifted-compression contraction.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 561 SoteriaFL verified: gamma_t=0.3043, contraction=0.8030<=0.8333, sot_err=2.2572e-04 << cdp_err=5.9266e+00
```
