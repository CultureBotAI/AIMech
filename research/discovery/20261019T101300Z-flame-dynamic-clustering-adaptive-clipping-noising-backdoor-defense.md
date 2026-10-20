# Discovery Report: Round 530 — FLAME Dynamic Clustering and Adaptive Clipping-Noising Backdoor Defense

- **Timestamp**: `2026-10-19T10:13:00Z`
- **Selected Concept**: `AIMech:FlameDynamicClusteringAndAdaptiveClippingNoisingBackdoorDefense` (*FLAME Dynamic Clustering and Adaptive Clipping-Noising Backdoor Defense*)
- **Record Path**: `data/curated/FlameDynamicClusteringAndAdaptiveClippingNoisingBackdoorDefense.yaml`
- **Primary Source**: Thien Duc Nguyen, Phillip Rieger, Huili Chen, Hossein Yalame, Helen Mollering, Hossein Fereidooni, Samuel Marchal, Markus Miettinen, Azalia Mirhoseini, Shaza Zeitouni, Farinaz Koushanfar, Ahmad-Reza Sadeghi, Thomas Schneider — *FLAME: Taming Backdoors in Federated Learning* (`https://dblp.org/rec/conf/uss/NguyenRCYMFMMMZ22`).

## Identity & Boundary Resolution

Introduced by Nguyen et al. (USENIX Security 2022, pp. 1415-1432, arXiv:2101.02281). Distinct from fixed-two-cluster defenses such as Auror (Shen et al. 2016) and Krum, which fail when an attacker simultaneously injects multiple backdoors or honeypot outliers (pigeonhole principle), and from CRFL (AIMech:CrflCertifiablyRobustFederatedLearningViaParameterClippingAndSmoothing), which clips and perturbs the aggregated global model for randomized parameter smoothing rather than combining HDBSCAN pairwise cosine filtering with median-update-norm adaptive clipping before noise injection.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 530 FLAME (Nguyen et al. 2022): admitted=[0, 1, 2, 3, 5], S_t=1.0210<=max_benign=1.0210<<max_all=100.0, sigma_flame=0.04946<sigma_unclipped=0.77420
```
