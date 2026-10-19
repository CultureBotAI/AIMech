# Discovery Report: Round 310 — Randomly Initialized Gradient Descent and Leave-One-Out Sign-Flip Phase Retrieval Analysis

- **Timestamp**: `2026-10-19T06:12:00Z`
- **Selected Concept**: `AIMech:RandomlyInitializedGradientDescentAndLeaveOneOutSignFlipPhaseRetrievalAnalysis` (*Randomly Initialized Gradient Descent and Leave-One-Out Sign-Flip Phase Retrieval Analysis*)
- **Record Path**: `data/curated/RandomlyInitializedGradientDescentAndLeaveOneOutSignFlipPhaseRetrievalAnalysis.yaml`
- **Primary Source**: Yuxin Chen, Yuejie Chi, Jianqing Fan, Cong Ma — *Gradient Descent with Random Initialization: Fast Global Convergence for Nonconvex Phase Retrieval* (`https://doi.org/10.1007/s10107-018-1327-0`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 704 maintained AIMech concepts. Distinct from `AIMech:TruncatedAmplitudeFlowAndOrthogonalityPromotingInitializationForQuadraticEquations` and `AIMech:AltMinPhaseAndSparseAltMinPhaseAlternatingMinimizationPhaseRetrieval`, which require tailored spectral initializations (`sum y_i a_i a_i^T` or orthogonality-promoting initialization), whereas Chen-Chi-Fan-Ma prove $O(\log n + \log(1/\varepsilon))$ global convergence of randomly initialized gradient descent via the coupled leave-one-out and random-sign auxiliary sequences $x^{t,(l)}$, $x^{t,\mathrm{sgn}}$, and $x^{t,\mathrm{sgn},(l)}$.

## Constructed Boundary & Regime Verification

```text
{"concept": "RandomlyInitializedGradientDescentAndLeaveOneOutSignFlipPhaseRetrievalAnalysis", "init_snr_ratio": 0.026541, "loo_sign_double_diff_t4": 0.029292, "loo_single_diff_t4": 0.02732, "min_snr_growth_factor": 1.161131, "orthogonal_hyperplane_signal_coord": 5.3920525926710204e-18, "random_init_gd_final_dist": 1.590274191979207e-07, "sgn_flip_diff_t4": 0.059313, "stage1_basin_entry_iter": 38, "status": "VERIFIED"}
```
