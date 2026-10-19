# Discovery Report: Round 413 — MOON (Model-Contrastive Federated Learning)

- **Timestamp**: `2026-10-19T08:16:00Z`
- **Selected Concept**: `AIMech:MoonModelContrastiveFederatedLearning` (*MOON (Model-Contrastive Federated Learning)*)
- **Record Path**: `data/curated/MoonModelContrastiveFederatedLearning.yaml`
- **Primary Source**: Qinbin Li, Bingsheng He, Dawn Song — *Model-Contrastive Federated Learning* (`https://doi.org/10.1109/CVPR46437.2021.01057`).

## Identity & Boundary Resolution

Distinct from parameter-space drift regularization methods such as FedProx (AIMech:FedProxProximalHeterogeneousFederatedOptimization, which penalizes the Euclidean parameter distance (mu / 2) ||w_i^t - w^t||_2^2 without using feature representations or previous-round negative models w_i^{t-1}) and SCAFFOLD (AIMech:ScaffoldStochasticControlledAveragingForFederatedLearning, which applies gradient control variates), and from data-level contrastive learning methods such as SimCLR and MoCo, which contrast augmented views of different input samples rather than representations of the same input x across three distinct models (w_i^t, w^t, w_i^{t-1}).

## Constructed Boundary & Regime Verification

```text
[PASS] MOON boundaries verified: l_con(z_glob=z_prev)=0.693147 (log2=0.693147), grad_fd_err=1.51e-09, sim_glob: 0.570->0.989, sim_prev: 0.515->-0.346
```
