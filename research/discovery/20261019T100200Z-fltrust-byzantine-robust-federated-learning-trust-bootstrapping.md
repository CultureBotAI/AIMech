# Discovery Report: Round 519 — FLTrust (Byzantine-Robust Federated Learning via Trust Bootstrapping)

- **Timestamp**: `2026-10-19T10:02:00Z`
- **Selected Concept**: `AIMech:FlTrustByzantineRobustFederatedLearningViaTrustBootstrapping` (*FLTrust (Byzantine-Robust Federated Learning via Trust Bootstrapping)*)
- **Record Path**: `data/curated/FlTrustByzantineRobustFederatedLearningViaTrustBootstrapping.yaml`
- **Primary Source**: Xiaoyu Cao, Minghong Fang, Jia Liu, Neil Zhenqiang Gong — *FLTrust: Byzantine-robust Federated Learning via Trust Bootstrapping* (`https://dblp.org/rec/conf/ndss/CaoF0G21`).

## Identity & Boundary Resolution

Introduced by Xiaoyu Cao, Minghong Fang, Jia Liu, and Neil Zhenqiang Gong in 'FLTrust: Byzantine-robust Federated Learning via Trust Bootstrapping' (NDSS 2021, DOI:10.14722/ndss.2021.24434; arXiv:2012.13995). Distinct from client-only statistical outlier defenses (Krum, Blanchard et al. 2017; Coordinate-Wise Median and Trimmed Mean, Yin et al. 2018; Bulyan, El Mhamdi et al. 2018), which have no server root of trust and break down when malicious clients reach >= 50% (or >= 25% for Bulyan) or craft adaptive local model poisoning updates.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 519 FLTrust (Cao et al. 2021): err_fltrust=0.5502<<err_no_norm=561.6, Lemma1_lhs=0.5502<=rhs=4.0465
```
