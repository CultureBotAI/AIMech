# Discovery Report: Round 497 — FedDG Episodic Learning in Continuous Frequency Space for Federated Domain Generalization

- **Timestamp**: `2026-10-19T09:40:00Z`
- **Selected Concept**: `AIMech:FedDgEpisodicLearningInContinuousFrequencySpaceForFederatedDomainGeneralization` (*FedDG Episodic Learning in Continuous Frequency Space for Federated Domain Generalization*)
- **Record Path**: `data/curated/FedDgEpisodicLearningInContinuousFrequencySpaceForFederatedDomainGeneralization.yaml`
- **Primary Source**: Quande Liu, Cheng Chen, Jing Qin, Qi Dou, Pheng-Ann Heng — *FedDG: Federated Domain Generalization on Medical Image Segmentation via Episodic Learning in Continuous Frequency Space* (`https://api.crossref.org/works?query.title=FedDG+Federated+Domain+Generalization+on+Medical+Image+Segmentation+via+Episodic+Learning+in+Continuous+Frequency+Space&rows=2`).

## Identity & Boundary Resolution

Distinct from standard Federated Averaging (AIO:FederatedLearning), which optimizes average in-distribution risk over participating clients without cross-client frequency amplitude interpolation or episodic meta-updates, and distinct from FedSR (AIMech:FedSrSimpleAndEffectiveDomainGeneralizationForFederatedLearning), which enforces L2 representation norm and conditional mutual information regularizers locally without exchanging Fourier amplitude spectra or performing boundary-oriented episodic meta-learning.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 497 FedDG/ELCFS (Liu et al. 2021): phase_err=2.22e-15, mean_err=6.66e-16, L_boundary_aligned=1.3838e-04 << L_boundary_unaligned=1.4112
```
