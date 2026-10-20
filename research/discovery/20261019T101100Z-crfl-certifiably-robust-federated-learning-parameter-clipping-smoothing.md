# Discovery Report: Round 528 — CRFL Certifiably Robust Federated Learning via Parameter Clipping and Smoothing

- **Timestamp**: `2026-10-19T10:11:00Z`
- **Selected Concept**: `AIMech:CrflCertifiablyRobustFederatedLearningViaParameterClippingAndSmoothing` (*CRFL Certifiably Robust Federated Learning via Parameter Clipping and Smoothing*)
- **Record Path**: `data/curated/CrflCertifiablyRobustFederatedLearningViaParameterClippingAndSmoothing.yaml`
- **Primary Source**: Chulin Xie, Minghao Chen, Pin-Yu Chen, Bo Li — *CRFL: Certifiably Robust Federated Learning against Backdoor Attacks* (`https://dblp.org/rec/conf/icml/Xie0CL21`).

## Identity & Boundary Resolution

Introduced by Xie, Chen, Chen, and Li (ICML 2021, PMLR 139:11372-11382, arXiv:2106.08283). Distinct from input-space randomized smoothing (Cohen et al. 2019), which perturbs test inputs rather than model parameters, and from centralized bagged backdoor certification RAB (Weber et al. 2020), which trains M separate models on M noise-corrupted datasets rather than a single federated model evaluated under M parameter-smoothed copies. Also distinct from heuristic norm-clipping and DP-FL defenses (Sun et al. 2019; Geyer et al. 2017), which lack test-time parameter smoothing and pointwise backdoor radius certificates.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 528 CRFL (Xie et al. 2021): eta_TV=0.6827<1, L_Z=1.4500, kl_budget=0.4069, RAD(T=5)=8.0784 < RAD(T=15)=54.4762, RAD(N=50)/RAD(N=20)=2.50
```
