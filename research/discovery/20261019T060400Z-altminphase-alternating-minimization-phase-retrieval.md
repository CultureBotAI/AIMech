# Discovery Report: Round 306 — AltMinPhase and SparseAltMinPhase (Resampled Alternating Minimization for Phase Retrieval)

- **Timestamp**: `2026-10-19T06:04:00Z`
- **Selected Concept**: `AIMech:AltMinPhaseAndSparseAltMinPhaseAlternatingMinimizationPhaseRetrieval` (*AltMinPhase and SparseAltMinPhase (Resampled Alternating Minimization for Phase Retrieval)*)
- **Record Path**: `data/curated/AltMinPhaseAndSparseAltMinPhaseAlternatingMinimizationPhaseRetrieval.yaml`
- **Primary Source**: Praneeth Netrapalli, Prateek Jain, Sujay Sanghavi — *Phase Retrieval using Alternating Minimization* (`https://doi.org/10.1109/TSP.2015.2448516`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 700 maintained AIMech concepts. Distinct from `AIMech:PhaseLiftConvexSemidefiniteProgrammingPhaseRetrieval` (Candes, Strohmer, & Voroninski 2013, which lifts $x^*\in\mathbb{C}^n$ to an $n\times n$ PSD matrix $X = x x^*$ solved by convex SDP in $O(n^3)$ per-step cost) and `AIMech:TruncatedAmplitudeFlowAndOrthogonalityPromotingInitializationForQuadraticEquations` (Wang, Giannakis, & Eldar 2018, which performs single-pool truncated subgradient steps on amplitude loss rather than alternating exact phase projection $C^{t+1}$ and exact least-squares/CoSaMP minimization across resampled batches).

## Constructed Boundary & Regime Verification

```text
{
  "altminphase_spectral_init_dist": 0.20108,
  "altminphase_final_dist": 0.0,
  "sparse_theory_null_mean": 0.63662,
  "sparse_theory_active_lower_bound": 0.69218,
  "sparse_theory_active_exact_mean": 0.74602,
  "sparse_empirical_min_active_score": 0.68864,
  "sparse_empirical_max_inactive_score": 0.65982,
  "exact_support_recovered": true
}
```
