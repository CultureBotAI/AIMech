# Discovery Report: Round 397 — Ditto Fair and Robust Personalized Federated Multi-Task Learning

- **Timestamp**: `2026-10-19T08:00:00Z`
- **Selected Concept**: `AIMech:DittoFairAndRobustPersonalizedFederatedMultiTaskLearning` (*Ditto Fair and Robust Personalized Federated Multi-Task Learning*)
- **Record Path**: `data/curated/DittoFairAndRobustPersonalizedFederatedMultiTaskLearning.yaml`
- **Primary Source**: Tian Li, Shengyuan Hu, Ahmad Beirami, Virginia Smith — *Ditto: Fair and Robust Federated Learning Through Personalization* (`https://doi.org/10.48550/arXiv.2012.04221`).

## Identity & Boundary Resolution

Distinct from pFedMe (AIMech:PFedMePersonalizedFederatedLearningWithMoreauEnvelopes, where the global model w minimizes the sum of Moreau envelopes F_i(w) and therefore depends directly on the local personalized iterates theta_i, making w vulnerable to local personalization state changes and requiring extra inner-loop steps before updating w) and from q-FFL (AIMech:QFairFederatedLearningAlphaFairResourceAllocation, which learns a single global model w whose fairness-oriented reweighting of high-loss devices degrades robustness under Byzantine corruption).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 397 Ditto verified: lambda*=0.1525, mse_ditto=0.1083 < min(local=0.1249, global=0.7562); var_ditto=0.0215 < var_global=0.8099
```
