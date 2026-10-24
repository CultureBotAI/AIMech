# Discovery Report: Round 491 — Power-of-Choice (Biased Loss-Based Client Selection Strategies for Federated Learning: pow-d, cpow-d, and rpow-d)

- **Timestamp**: `2026-10-19T09:34:00Z`
- **Selected Concept**: `AIMech:PowerOfChoiceBiasedLossClientSelectionForFederatedLearning` (*Power-of-Choice (Biased Loss-Based Client Selection Strategies for Federated Learning: pow-d, cpow-d, and rpow-d)*)
- **Record Path**: `data/curated/PowerOfChoiceBiasedLossClientSelectionForFederatedLearning.yaml`
- **Primary Source**: Yae Jee Cho, Jianyu Wang, Gauri Joshi — *Client Selection in Federated Learning: Convergence Analysis and Power-of-Choice Selection Strategies* (`https://arxiv.org/abs/2010.01243`).

## Identity & Boundary Resolution

Distinct from unbiased partial-participation FedAvg (McMahan et al. 2017; Li et al. 2020), which corresponds to the d = m special case (rho_bar = rho_tilde = 1, zero selection bias but no O(1/rho_bar) convergence acceleration); and distinct from q-Fair Federated Learning (AIMech:QFairFederatedLearningAlphaFairResourceAllocation, Li et al. 2020), which reweights the global objective to sum_k (p_k/(q+1)) F_k(w)^{q+1} under unbiased client sampling rather than altering the client selection policy via power-of-d highest-loss candidate filtering.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 491 Power-of-Choice (Cho et al. 2022): Gamma=6.2049, skew(d=2,3,4,6)=[1.0, 1.452, 1.864, 2.564], T=4: 0.0006 < 0.1084 < 3.1553, T=12: 0.000005 < 0.0339 < 0.6429
```
