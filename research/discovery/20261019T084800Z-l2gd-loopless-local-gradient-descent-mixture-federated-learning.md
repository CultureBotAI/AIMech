# Discovery Report: Round 445 — L2GD (Loopless Local Gradient Descent for Mixture Federated Learning)

- **Timestamp**: `2026-10-19T08:48:00Z`
- **Selected Concept**: `AIMech:L2gdLooplessLocalGradientDescentForMixtureFederatedLearning` (*L2GD (Loopless Local Gradient Descent for Mixture Federated Learning)*)
- **Record Path**: `data/curated/L2gdLooplessLocalGradientDescentForMixtureFederatedLearning.yaml`
- **Primary Source**: Filip Hanzely, Peter Richtarik — *Federated Learning of a Mixture of Global and Local Models* (`https://arxiv.org/abs/2002.05516`).

## Identity & Boundary Resolution

Distinct from pFedMe (AIMech:PFedMePersonalizedFederatedLearningWithMoreauEnvelopes, T. Dinh et al. 2020), which solves nested bi-level Moreau envelope subproblems at every local step using an auxiliary global variable w, and from Local SGD / FedAvg (AIMech:FederatedAveraging, McMahan et al. 2017), which forces full consensus x_1 = ... = x_n (the lambda -> infinity limit) and suffers O(alpha) bias on heterogeneous objectives, whereas L2GD is an unbiased variance-reduced stochastic solver on the two-term sum F(x) = f(x) + lambda psi(x) that converges linearly to the exact mixture optimum x^*(lambda) for any constant step size.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 445 L2GD (Hanzely & Richtarik 2020): thm32_err=8.88e-16, grad_sum_err=1.78e-15, p_star=0.20, comm_ratio=0.20
```
