# Discovery Report: Round 318 — Stochastic Block Model Exact Recovery Phase Transition and Semidefinite Programming

- **Timestamp**: `2026-10-19T06:28:00Z`
- **Selected Concept**: `AIMech:StochasticBlockModelExactRecoveryPhaseTransitionAndSemidefiniteProgramming` (*Stochastic Block Model Exact Recovery Phase Transition and Semidefinite Programming*)
- **Record Path**: `data/curated/StochasticBlockModelExactRecoveryPhaseTransitionAndSemidefiniteProgramming.yaml`
- **Primary Source**: Emmanuel Abbe, Afonso S. Bandeira, Georgina Hall — *Exact Recovery in the Stochastic Block Model* (`https://doi.org/10.1109/TIT.2015.2490670`).

## Identity & Boundary Resolution

Distinct from generic graph clustering (AIO:Clustering, AIO:UnsupervisedClustering), normalized spectral clustering (AIMech:NormalizedSpectralClusteringNgJordanWeiss), and spectral regularization of sparse random graphs. Specifically captures the Abbe-Bandeira-Hall (2016) logarithmic-degree exact recovery threshold (sqrt(alpha) - sqrt(beta))^2 = 2 (Theorems 1-2), the binomial large-deviation bound P(Z_1 - Z_2 >= 0) = n^{-(sqrt(alpha)+sqrt(beta))^2/2 + o(1)} (Lemma 2), and the SDP dual-certificate Laplacian analysis S = 2 L_SBM + 1 1^T >= 0 with lambda_2(S) > 0 (Lemma 6, Lemma 11, and Theorem 4).

## Constructed Boundary & Regime Verification

```text
{"concept": "StochasticBlockModelExactRecoveryPhaseTransitionAndSemidefiniteProgramming", "dual_certificate_nullspace_err": 0.0, "dual_certificate_orth_rayleigh": [4.0, 6.0], "lemma11_eigenvalues": [5.920558, 0.0, 11.436928], "sdp_primal_dual_gap": 0.0, "status": "VERIFIED", "subcritical_chernoff_hellinger": 0.325255, "supercritical_chernoff_hellinger": 1.517949}
```
