# Discovery Report: Round 500 — Gradient Masked Averaging for Federated Learning

- **Timestamp**: `2026-10-19T09:43:00Z`
- **Selected Concept**: `AIMech:FedGmaGradientMaskedAveragingForFederatedLearning` (*Gradient Masked Averaging for Federated Learning*)
- **Record Path**: `data/curated/FedGmaGradientMaskedAveragingForFederatedLearning.yaml`
- **Primary Source**: Irene Tenison, Sai Aravind Sreeramadas, Vaikkunth Mugunthan, Edouard Oyallon, Irina Rish, Eugene Belilovsky — *Gradient Masked Averaging for Federated Learning* (`https://dblp.org/rec/journals/tmlr/TenisonSMORB23`).

## Identity & Boundary Resolution

Distinct from centralized sample-level hard binary AND-Mask (Parascandolo et al., 2020) and SAND-Mask (Shahtalebi et al., 2021), which mask single-step sample or environment gradients with hard zeroing or tanh-based magnitude scaling in centralized training; FedGMA operates at the federated server aggregation stage across client multi-step pseudo-gradients Delta_t^n and uses a piecewise-linear soft agreement mask [m_tilde_tau]_j = 1 if A_j >= tau else A_j compatible with non-adaptive (FedAvg, FedProx) and adaptive (FedAdam, FedYogi) server optimizers. Distinct from FedAvg (AIMech:FederatedAveraging), which corresponds to the unmasked degenerate limit tau = 0 where m_tilde_0 = 1.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 500 FedGMA (Tenison et al., TMLR 2023): A=[1.0, 0.6, 0.2, 0.2], mask=[1.0, 1.0, 0.2, 0.2], ood_loss_avg=1.7791 -> ood_loss_gma=1.7764, spurious_bias_avg=1.8863 -> spurious_bias_gma=1.8849
```
