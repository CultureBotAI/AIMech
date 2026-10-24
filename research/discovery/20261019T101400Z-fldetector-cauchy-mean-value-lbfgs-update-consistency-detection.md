# Discovery Report: Round 531 — FLDetector Cauchy Mean Value and L-BFGS Model-Update Consistency Detection

- **Timestamp**: `2026-10-19T10:14:00Z`
- **Selected Concept**: `AIMech:FlDetectorCauchyMeanValueLbfgsModelUpdateConsistencyDetection` (*FLDetector Cauchy Mean Value and L-BFGS Model-Update Consistency Detection*)
- **Record Path**: `data/curated/FlDetectorCauchyMeanValueLbfgsModelUpdateConsistencyDetection.yaml`
- **Primary Source**: Zaixi Zhang, Xiaoyu Cao, Jinyuan Jia, Neil Zhenqiang Gong — *FLDetector: Defending Federated Learning Against Model Poisoning Attacks via Detecting Malicious Clients* (`https://dblp.org/rec/conf/kdd/ZhangCJG22`).

## Identity & Boundary Resolution

Introduced by Zhang, Cao, Jia, and Gong (KDD 2022, pp. 2545-2555, DOI:10.1145/3534678.3539231, arXiv:2207.09209). Distinct from single-round Byzantine-robust aggregation rules such as Krum, Trimmed-Mean, Median, and FLTrust (AIMech:FlTrustByzantineRobustFederatedLearningViaTrustBootstrapping), which aggregate updates within each iteration without cross-iteration Cauchy-mean-value Hessian consistency prediction, and from VAE-based anomaly detection (Li et al. 2020), which requires a clean server validation dataset to train a reconstruction autoencoder.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 531 FLDetector (Zhang et al. 2022): benign_err_HVP=0.006326<benign_err_NoHVP=0.719307, max_benign_score=0.0002 << min_malicious_score=0.4993
```
