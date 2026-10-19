# Discovery Report: Round 446 — FedExP (Federated Extrapolation for Speeding Up Federated Averaging)

- **Timestamp**: `2026-10-19T08:49:00Z`
- **Selected Concept**: `AIMech:FedExpExtrapolatedServerAveragingForFederatedLearning` (*FedExP (Federated Extrapolation for Speeding Up Federated Averaging)*)
- **Record Path**: `data/curated/FedExpExtrapolatedServerAveragingForFederatedLearning.yaml`
- **Primary Source**: Divyansh Jhunjhunwala, Shiqiang Wang, Gauri Joshi — *FedExP: Speeding Up Federated Averaging via Extrapolation* (`https://openreview.net/forum?id=IieNl1vg64`).

## Identity & Boundary Resolution

Distinct from FedOpt (AIMech:FedOptAdaptiveFederatedOptimization, Reddi et al. 2021), which requires tuning both the client learning rate eta_l and server learning rate eta_g via grid search or second-moment accumulators (FedAdam, FedYogi, FedAdagrad), and from FedNova (AIMech:FedNovaNormalizedAveragingForFederatedOptimization, Wang et al. 2020), which normalizes heterogeneous local step counts tau_i rather than extrapolating the server step size via the ratio of average squared pseudo-gradient norms to the squared norm of the averaged pseudo-gradient.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 446 FedExP (Jhunjhunwala et al. 2023): Lemma1_margin=5.76e-10>=0, mean_eta_g=7.930, err_fedexp=7.4709e-04 << err_fedavg=4.4855e-01
```
