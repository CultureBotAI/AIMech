# Discovery Report: Round 395 — pFedMe Personalized Federated Learning with Moreau Envelopes

- **Timestamp**: `2026-10-19T07:58:00Z`
- **Selected Concept**: `AIMech:PFedMePersonalizedFederatedLearningWithMoreauEnvelopes` (*pFedMe Personalized Federated Learning with Moreau Envelopes*)
- **Record Path**: `data/curated/PFedMePersonalizedFederatedLearningWithMoreauEnvelopes.yaml`
- **Primary Source**: Canh T. Dinh, Nguyen H. Tran, Tuan Dung Nguyen — *Personalized Federated Learning with Moreau Envelopes* (`https://doi.org/10.48550/arXiv.2006.08848`).

## Identity & Boundary Resolution

Distinct from FedProx (AIMech:FedProxProximalFederatedOptimization, which solves the same proximal subproblem to update a single shared global model w without decoupling a persistent personalized model theta_i from the global reference parameter w), from Per-FedAvg (AIMech:PerFedAvgModelAgnosticMetaLearningForPersonalizedFederatedLearning, which minimizes one-step MAML adaptation loss f_i(w - alpha nabla f_i(w)) requiring Hessian-vector products rather than first-order Moreau envelopes), and from Ditto (AIMech:DittoFairAndRobustPersonalizedFederatedMultiTaskLearning, where global optimization of w^* is completely independent of the personalized models v_k, whereas in pFedMe the outer global update depends directly on lambda * (w_{i,r}^t - theta_tilde_i)).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 395 pFedMe verified: w_err=2.380e-03, theta_err=1.587e-03, pers_loss=5.3714 < global_loss=18.6391
```
