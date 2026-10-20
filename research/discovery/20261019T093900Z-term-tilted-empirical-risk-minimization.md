# Discovery Report: Round 496 — TERM (Tilted Empirical Risk Minimization and Hierarchical Multi-Objective Tilting)

- **Timestamp**: `2026-10-19T09:39:00Z`
- **Selected Concept**: `AIMech:TermTiltedEmpiricalRiskMinimizationAndHierarchicalMultiObjectiveTilting` (*TERM (Tilted Empirical Risk Minimization and Hierarchical Multi-Objective Tilting)*)
- **Record Path**: `data/curated/TermTiltedEmpiricalRiskMinimizationAndHierarchicalMultiObjectiveTilting.yaml`
- **Primary Source**: Tian Li, Ahmad Beirami, Maziar Sanjabi, Virginia Smith — *Tilted Empirical Risk Minimization* (`https://openreview.net/forum?id=K5YasWXZT3O`).

## Identity & Boundary Resolution

Distinct from q-FFL (AIMech:QFairFederatedLearningAlphaFairResourceAllocation, Li et al. 2020), which raises positive losses to a polynomial power (1/(q+1)) F_k^{q+1}(w) for q >= 0 only and cannot take negative exponents to suppress outliers or nest hierarchical group/sample tilts; and distinct from Agnostic Federated Learning (AIMech:AgnosticFederatedLearningMinimaxDistributionallyRobustOptimization, Mohri et al. 2019), which solves a hard minimax saddle-point problem min_w max_{lambda in Lambda} L_lambda(w) rather than a smooth, tunable cumulant-generating log-sum-exp objective spanning min-loss (t -> -inf), average-loss (t -> 0), and max-loss (t -> +inf).

## Constructed Boundary & Regime Verification

```text
[PASS] Round 496 TERM (Li et al. 2021): theta(-1)=1.0000 vs ERM=2.8000 (w_outlier=6.51e-19), var(t=-0.2)=0.09->var(t=2.0)=0.03, cos(1_N)=0.6602->0.8551, Lemma7_err=0.00e+00
```
