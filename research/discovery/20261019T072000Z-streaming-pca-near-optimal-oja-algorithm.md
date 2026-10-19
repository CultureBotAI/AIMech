# Discovery Report: Round 357 — Oja's Streaming PCA Algorithm with Matrix-Bernstein-Matching Finite-Sample Guarantees

- **Timestamp**: `2026-10-19T07:20:00Z`
- **Selected Concept**: `AIMech:StreamingPCANearOptimalFiniteSampleOjaAlgorithm` (*Oja's Streaming PCA Algorithm with Matrix-Bernstein-Matching Finite-Sample Guarantees*)
- **Record Path**: `data/curated/StreamingPCANearOptimalFiniteSampleOjaAlgorithm.yaml`
- **Primary Source**: Prateek Jain, Chi Jin, Sham M. Kakade, Praneeth Netrapalli, Aaron Sidford — *Streaming PCA: Matching Matrix Bernstein and Near-Optimal Finite Sample Guarantees for Oja's Algorithm* (`https://proceedings.mlr.press/v49/jain16.html`).

## Identity & Boundary Resolution

Distinct from generic PrincipalComponentAnalysis (AIO:PrincipalComponentAnalysis) and DimensionalityReduction (AIO:DimensionalityReduction), which do not specify O(d)-space single-pass Oja updates or cumulative matrix-product operator moment bounds. Distinct from AIMech:NoisyPowerMethodForStreamingAndDifferentiallyPrivatePCA (Round 356), which groups samples into L blocks for block power iteration and incurs an extra O(lambda_1/(lambda_1 - lambda_2) * log n) sample-complexity factor (Table 1, p. 5). Also distinct from AIMech:ShiftAndInvertPreconditioningForFasterEigenvectorComputation (Round 354), which requires an O(gap)-close warm-start vector x_0 in the streaming setting, whereas Jain et al. (2016) prove global convergence from a uniform random unit vector w_0.

## Constructed Boundary & Regime Verification

```text
[PASS] Round 357 Streaming PCA Oja's Algorithm (Jain et al. 2016): op_diff=3.33e-16, E[v1^T B B^T v1]=1.0649>=L5.3(1.0647), E[Tr_perp]=3.0303<=L5.2(4.0410), E[(v1^T B B^T v1)^2]=1.1344<=L5.4(1.1352)
```
