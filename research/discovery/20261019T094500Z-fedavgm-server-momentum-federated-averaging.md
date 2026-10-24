# Discovery Report: Round 502 — Federated Averaging with Server Momentum

- **Timestamp**: `2026-10-19T09:45:00Z`
- **Selected Concept**: `AIMech:FedAvgMServerMomentumFederatedAveraging` (*Federated Averaging with Server Momentum*)
- **Record Path**: `data/curated/FedAvgMServerMomentumFederatedAveraging.yaml`
- **Primary Source**: Tzu-Ming Harry Hsu, Hang Qi, Matthew Brown — *Measuring the Effects of Non-Identical Data Distribution for Federated Visual Classification* (`https://dblp.org/rec/journals/corr/abs-1909-06335`).

## Identity & Boundary Resolution

Distinct from vanilla Federated Averaging (AIMech:FederatedAveraging; McMahan et al., 2017), which corresponds to the memoryless server update beta = 0 (w <- w - Delta w). Distinct from SlowMo (AIMech:SlowMoCommunicationEfficientDistributedSgdWithSlowMomentum; Wang et al., ICLR 2020), which formulates a two-level outer-step Nesterov/heavy-ball momentum framework with explicit outer learning rate alpha and inner base optimizer steps (covering local SGD and SGP), and from FedOpt / FedAdam / FedYogi / FedAdagrad (AIMech:AdaptiveFederatedOptimization; Reddi et al., ICLR 2021), which introduce second-moment adaptive preconditioners v_t at the server. Also distinct from Mime / MimeLite (Karimireddy et al., 2020) and FedCM (Xu et al., 2021), which apply server momentum or client-level momentum inside every local client gradient step.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 502 FedAvgM (Hsu, Qi, & Brown, 2019): Dirichlet Var(alpha=1e-6)=0.0900, Var(alpha=1e6)=9.00e-08, err_fedavg(beta=0)=0.4732 -> err_fedavgm(beta=0.9)=0.0146 (unscaled=0.3605)
```
