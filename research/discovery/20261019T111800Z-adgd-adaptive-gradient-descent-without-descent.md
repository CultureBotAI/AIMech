# Discovery Report: Round 595 — AdGD (Adaptive Gradient Descent without Descent)

- **Timestamp**: `2026-10-19T11:18:00Z`
- **Selected Concept**: `AIMech:AdGDAdaptiveGradientDescentWithoutDescent` (*AdGD (Adaptive Gradient Descent without Descent)*)
- **Record Path**: `data/curated/AdGDAdaptiveGradientDescentWithoutDescent.yaml`
- **Primary Source**: Yura Malitsky, Konstantin Mishchenko — *Adaptive Gradient Descent without Descent* (`https://dblp.org/rec/conf/icml/MalitskyM20`).

## Identity & Boundary Resolution

Distinct from backtracking line search (Armijo/Goldstein) in that AdGD never evaluates f(x) or backtracks with extra gradient evaluations per step. Distinct from Polyak's step size in that it requires no knowledge or estimate of f_*. Distinct from the Barzilai-Borwein method in that AdGD caps step-size growth by sqrt(1 + theta_{k-1}) lambda_{k-1} and uses the l2 ratio ||x^k - x^{k-1}|| / (2 ||nabla f(x^k) - nabla f(x^{k-1})||), providing provable convergence for arbitrary locally smooth convex functions where Barzilai-Borwein can diverge.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 595 AdGD verified: lyap_diff=1.30e-16<=0, ergodic=(2.5215e-05<=5.1876e-02), loss_adgd=2.7374e-35<<loss_gd=3.1151e-05
```
