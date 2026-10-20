# Discovery Report: Round 501 — HarmoFL: Harmonizing Local and Global Drifts in Federated Learning on Heterogeneous Medical Images

- **Timestamp**: `2026-10-19T09:44:00Z`
- **Selected Concept**: `AIMech:HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning` (*HarmoFL: Harmonizing Local and Global Drifts in Federated Learning on Heterogeneous Medical Images*)
- **Record Path**: `data/curated/HarmoFlHarmonizingLocalAndGlobalDriftsInFederatedLearning.yaml`
- **Primary Source**: Meirui Jiang, Zirui Wang, Qi Dou — *HarmoFL: Harmonizing Local and Global Drifts in Federated Learning on Heterogeneous Medical Images* (`https://doi.org/10.1609/aaai.v36i1.19993`).

## Identity & Boundary Resolution

Distinct from FedDG / ELCFS (AIMech:FedDgEpisodicLearningInContinuousFrequencySpaceForFederatedDomainGeneralization; Liu et al., CVPR 2021), which shares per-client frequency amplitude banks for episodic continuous interpolation and boundary-oriented meta-learning; HarmoFL maintains a single server-averaged moving-average amplitude template A_bar^t without sharing individual image amplitude banks and couples frequency harmonization with SAM-style local Euclidean weight perturbation delta_k = alpha * g / ||g||_2. Distinct from FedBN (Li et al., ICLR 2021), which keeps Batch Normalization parameters local without frequency-space amplitude harmonization or local weight perturbation.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 501 HarmoFL (Jiang et al., AAAI 2022): raw_diff=1480.00 -> harmo_diff=3.55e-29, gamma_raw=0.18317 -> gamma_harmo=0.04344, g_unpert=0.0235 vs g_pert=-0.7158
```
