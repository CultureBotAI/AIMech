# Discovery Report: Round 831 — Prior-Expansion Marginal Likelihood Score Prior-Data Conflict Check

- **Timestamp**: `2026-10-19T15:14:00Z`
- **Selected Concept**: `AIMech:PriorExpansionMarginalLikelihoodScorePriorDataConflictCheck` (*Prior-Expansion Marginal Likelihood Score Prior-Data Conflict Check*)
- **Record Path**: `data/curated/PriorExpansionMarginalLikelihoodScorePriorDataConflictCheck.yaml`
- **Primary Source**: David J. Nott, Micheal Seah, Luai Al-Labadi, Michael Evans, Hui Khoon Ng, Berthold-Georg Englert — *Using prior expansions for prior-data conflict checking* (`https://arxiv.org/abs/1902.10393`).

## Identity & Boundary Resolution

No AIO class represents Bayesian prior-data conflict diagnostics; MachineLearningTask (AIO:MachineLearningTask) is the closest broad match covering model criticism and diagnostic evaluation tasks.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 831 Prior-Expansion Score Check verified: |S_marg - E_post|=0.0, Q=2.250->10.240, p_S=0.1336->0.00137
```
