# Discovery Report: Round 605 — LaProp (Decoupled Momentum and Adaptivity Optimizer)

- **Timestamp**: `2026-10-19T11:28:00Z`
- **Selected Concept**: `AIMech:LaPropSeparatingMomentumAndAdaptivityInAdam` (*LaProp (Decoupled Momentum and Adaptivity Optimizer)*)
- **Record Path**: `data/curated/LaPropSeparatingMomentumAndAdaptivityInAdam.yaml`
- **Primary Source**: Liu Ziyin, Zhikang T. Wang, Masahito Ueda — *LaProp: Separating Momentum and Adaptivity in Adam* (`https://dblp.org/rec/journals/corr/abs-2002-04839`).

## Identity & Boundary Resolution

Distinct from Adam (Kingma and Ba 2015) and ADOPT (AIMech:AdoptModifiedAdamOptimalConvergenceAnyBeta2): in the generalized adaptive update theta_{t+1} = theta_t - lambda_t G_t nabla l(theta_t) + mu_t K_t (theta_t - theta_{t-1}) (Eq. 2), Adam induces K_t = H_t^{-1} H_{t-1} (reweighting past parameter momentum by the current preconditioner and diverging when nu -> 0 with mu > 0), whereas LaProp sets K_t = I by normalizing g_t with contemporaneous bias-corrected sqrt(n_t / c_n) + eps before momentum accumulation (unlike ADOPT, which uses the lagged un-bias-corrected v_{t-1}). Originally circulated as 'LaProp: a Better Way to Combine Momentum with Adaptive Gradient' (v1) and revised as 'LaProp: Separating Momentum and Adaptivity in Adam' (v3).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 605 LaProp verified: eq6_err=0.00e+00, eq7_err=2.22e-16, K_impulse=0.0276, prop1_ratio=0.8660<=1, prop2_viol=511554319.1, ssg_err=0.00e+00, rosenbrock=(LaProp:0.0901<Adam:0.3223), min_var=0.00e+00
```
