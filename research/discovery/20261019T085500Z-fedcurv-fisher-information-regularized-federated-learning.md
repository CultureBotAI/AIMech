# Discovery Report: Round 452 — FedCurv (Fisher-Information-Regularized Federated Learning for Non-IID Data)

- **Timestamp**: `2026-10-19T08:55:00Z`
- **Selected Concept**: `AIMech:FedCurvFisherInformationRegularizedFederatedLearning` (*FedCurv (Fisher-Information-Regularized Federated Learning for Non-IID Data)*)
- **Record Path**: `data/curated/FedCurvFisherInformationRegularizedFederatedLearning.yaml`
- **Primary Source**: Neta Shoham, Tomer Avidor, Aviv Keren, Nadav Israel, Daniel Benditkis, Liron Mor-Yosef, Itai Zeitak — *Overcoming Forgetting in Federated Learning on Non-IID Data* (`https://arxiv.org/abs/1910.07796`).

## Identity & Boundary Resolution

Distinct from FedProx (AIMech:FedProxProximalHeterogeneousFederatedOptimization, Li et al. 2020), which penalizes isotropic Euclidean distance (mu/2)*||theta - w^{t-1}||_2^2 around the scalar-averaged global model without parameter-wise Fisher curvature weighting or peer-model decoupling; and distinct from FFL-ERL / Fisher-weighted server model fusion, as FedCurv applies the peer-summed diagonal Fisher quadratic regularizer directly during local client SGD optimization via aggregated server vectors (P_{t-1}, Q_{t-1}).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 452 FedCurv verified: eq4_eq5_grad_err=8.88e-16, err_fedcurv=0.0128 << err_fedavg=0.1619
/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/scratch/aimech-work/research/discovery/fedcurv-fisher-information-regularized-federated-learning-boundaries.py:6: SyntaxWarning: invalid escape sequence '\ '
  L_{t,s}(theta) = f_s(theta) + lambda * sum_{j in S \ {s}} (theta - theta_j)^T diag(I_j) (theta - theta_j)
```
