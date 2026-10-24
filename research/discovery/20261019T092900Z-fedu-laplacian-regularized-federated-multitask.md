# Discovery Report: Round 486 — FedU and dFedU (Laplacian-Regularized Federated Multi-Task Learning)

- **Timestamp**: `2026-10-19T09:29:00Z`
- **Selected Concept**: `AIMech:FedUAndDFedULaplacianRegularizedFederatedMultiTaskLearning` (*FedU and dFedU (Laplacian-Regularized Federated Multi-Task Learning)*)
- **Record Path**: `data/curated/FedUAndDFedULaplacianRegularizedFederatedMultiTaskLearning.yaml`
- **Primary Source**: Canh T. Dinh, Tung T. Vu, Nguyen H. Tran, Minh N. Dao, Hongyu Zhang — *A New Look and Convergence Rate of Federated Multi-Task Learning with Laplacian Regularization* (`https://arxiv.org/abs/2102.07148`).

## Identity & Boundary Resolution

Distinct from pFedMe (AIMech:PFedMePersonalizedFederatedLearningWithMoreauEnvelopes, Dinh, Tran, & Nguyen 2020), which is a star-graph special case of Equation 1 with a virtual central server model w_0 and no direct inter-client relational edges a_{kl} (Section III-B, Equation 5); and distinct from MOCHA (AIMech:MochaSystemsAwarePrimalDualFederatedMultiTaskLearning, Smith et al. 2017), which is restricted to convex loss functions solved via dual coordinate ascent and alternating task-matrix updates rather than primal multi-step local SGD with Laplacian regularization for both strongly convex and nonconvex deep networks.

## Constructed Boundary & Regime Verification

```text
[PASS] FedU/dFedU boundary verification passed: quad_form=16.6250==16.6250, rho=4.8229, norm_inside=1.0000, sigma2_sq=360.00
```
