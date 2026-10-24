# Discovery Report: Round 291 — Truncated Wirtinger Flow and Truncated Spectral Initialization for Random Quadratic Systems

- **Timestamp**: `2026-10-19T05:34:00Z`
- **Selected Concept**: `AIMech:TruncatedWirtingerFlowAndTruncatedSpectralInitializationForQuadraticSystems` (*Truncated Wirtinger Flow and Truncated Spectral Initialization for Random Quadratic Systems*)
- **Record Path**: `data/curated/TruncatedWirtingerFlowAndTruncatedSpectralInitializationForQuadraticSystems.yaml`
- **Primary Source**: Yuxin Chen, Emmanuel J. Candes — *Solving Random Quadratic Systems of Equations Is Nearly as Easy as Solving Linear Systems* (`https://doi.org/10.1002/cpa.21638`).

## Identity & Boundary Resolution

Resolved against all 442 pinned AIO concepts and 685 maintained AIMech concepts. Distinct from `AIMech:WirtingerFlowPhaseRetrievalAndSpectralInitialization` (Candès, Li, & Soltanolkotabi 2015, which minimizes the untruncated quartic intensity loss with untruncated spectral initialization, requiring $m \gtrsim n\log n$ samples and vanishing step size $\mu \lesssim 1/n$ due to fourth-moment heavy tails, whereas Chen & Candès 2017 introduce the Poisson log-likelihood formulation, Truncated Spectral Initialization $\mathbb{I}_{\{|y_i| \le \alpha_y^2\lambda_0^2\}}$, and the dual-event gradient truncation rules $\mathcal{E}_1^{(t)} \cap \mathcal{E}_2^{(t)}$ achieving $O(n)$ sample complexity and $O(1)$ step size).

## Constructed Boundary & Regime Verification

```text
{
  "table1_and_lemma2_verification": {
    "zeta1": 0.236434,
    "zeta2": 0.133222,
    "eq30_lhs_bound_lt_1_99": 0.845696,
    "mu_0_step_size_bound": 0.247681,
    "truncated_spectral_beta1_signal_gap": 1.702099,
    "truncated_spectral_beta2_identity": 0.970709,
    "lemma2_lb": 0.072065,
    "lemma2_frob": 0.098522,
    "lemma2_ub": 0.111768
  },
  "twf_simulation": {
    "n": 12,
    "m": 72,
    "dist_init_untruncated": 0.702429,
    "dist_init_truncated": 0.702429,
    "twf_err_trajectory_0_30_60_90_120": [
      0.702429,
      0.001402397069,
      7.047753e-06,
      2.9308e-08,
      1.22e-10
    ],
    "final_twf_dist": 1.2189317000606886e-10
  },
  "all_assertions_passed": true
}
```
