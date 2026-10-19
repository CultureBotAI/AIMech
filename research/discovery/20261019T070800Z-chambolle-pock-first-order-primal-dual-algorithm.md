# Discovery Report: Round 346 — Chambolle-Pock First-Order Primal-Dual Algorithm for Convex Saddle-Point Problems

- **Timestamp**: `2026-10-19T07:08:00Z`
- **Selected Concept**: `AIMech:ChambollePockFirstOrderPrimalDualAlgorithmForConvexSaddlePointProblems` (*Chambolle-Pock First-Order Primal-Dual Algorithm for Convex Saddle-Point Problems*)
- **Record Path**: `data/curated/ChambollePockFirstOrderPrimalDualAlgorithmForConvexSaddlePointProblems.yaml`
- **Primary Source**: Antonin Chambolle, Thomas Pock — *A First-Order Primal-Dual Algorithm for Convex Problems with Applications to Imaging* (`https://doi.org/10.1007/s10851-010-0251-1`).

## Identity & Boundary Resolution

Distinct from Iterative Bregman Projections and Bregman-Dykstra Regularized Optimal Transport (`AIMech:IterativeBregmanProjectionsAndBregmanDykstraRegularizedOptimalTransport`), which performs alternating Kullback-Leibler Bregman projections on entropically regularized transport polytopes, and from standard ADMM / Douglas-Rachford splitting, which requires inverting (I + tau^2 K^* K) at every iteration unless K = I (Section 4.2-4.3). Specifically captures the Chambolle-Pock extrapolated primal-dual recursion (Equation 7), its equivalence to preconditioned ADMM under M = (1/sigma)I - tau K K^* (Equations 32-34), the O(1/N) restricted primal-dual gap guarantee (Theorem 1), the adaptive-stepsize O(1/N^2) acceleration theta_n = 1/sqrt(1 + 2*gamma*tau_n) (Algorithm 2, Theorem 2), and the linearly convergent O(omega^{N/2}) scheme (Algorithm 3, Theorem 3).

## Constructed Boundary & Regime Verification

```text
[PASS] Chambolle-Pock boundaries verified: gap_N=1.995e-04<=d0/N=9.317e-03, 200*gamma*tau_200=0.9793, Alg3_err=6.15e-08<=omega^40*D0=4.22e-06, unstable_blowup=3.1e+20x
```
