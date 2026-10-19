# Discovery Report: Round 260 — Corrupted Sensing Convex Signal-Corruption Demixing and Subdifferential Distance Bounds

- **Timestamp**: `2026-10-19T02:28:00Z`
- **Selected Concept**: `AIMech:CorruptedSensingConvexSignalCorruptionDemixingAndSubdifferentialDistanceBounds` (*Corrupted Sensing Convex Signal-Corruption Demixing and Subdifferential Distance Bounds*)
- **Record Path**: `data/curated/CorruptedSensingConvexSignalCorruptionDemixingAndSubdifferentialDistanceBounds.yaml`
- **Primary Source**: Rina Foygel and Lester Mackey (2014), *Corrupted Sensing: Novel Guarantees for Separating Structured Signals*, *IEEE Transactions on Information Theory* 60(2):1223–1247 (`DOI:10.1109/TIT.2013.2293654`, `arXiv:1305.2524v2`).

## Identity & Boundary Resolution

`AIMech:CorruptedSensingConvexSignalCorruptionDemixingAndSubdifferentialDistanceBounds` was checked against all 442 pinned AIO concepts and 654 maintained AIMech concepts:

1. **`AIMech:AtomicNormConvexGeometryAndTangentConeGaussianWidthForLinearInverseProblems`**: Analyzes uncorrupted linear inverse problems $y = \Phi x^\star + \omega$, whereas Foygel & Mackey (2014) formulate corrupted sensing $y = \Phi x^\star + v^\star + z$ for simultaneous signal-corruption separation via constrained and penalized convex programs and prove dense-regime subdifferential squared-distance bounds strictly below $p$.
2. **`AIMech:ConicStatisticalDimensionIntrinsicVolumeConcentrationAndPhaseTransitions`**: Analyzes noiseless orthogonal conic demixing $z_0 = x_0 + U y_0$ ($U \in O(d)$), whereas Foygel & Mackey (2014) analyze noisy rectangular Gaussian sensing $y = \Phi x^\star + v^\star + z$ and penalized demixing with $\lambda = t_{\text{cor}}/t_{\text{sig}}$.
3. **`AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance`**: Characterizes proximal denoising NMSE and uncorrupted projected LASSO risk, whereas Foygel & Mackey (2014) establish Propositions 1 and 3–5 and Theorems 1–4 for signal-corruption separation.

## Constructed Boundary & Regime Verification

```text
{
  "l1_subdifferential_bounds": {
    "rho_0.02": {
      "t_eq8": 2.79715,
      "bound_eq8_normalized": 0.186481,
      "t_eq9": 0.781927,
      "bound_eq9_normalized": 0.38859,
      "t_eq10": 1.717437,
      "bound_eq10_normalized": 0.104181
    },
    "rho_0.05": {
      "t_eq8": 2.447747,
      "bound_eq8_normalized": 0.374573,
      "t_eq9": 0.75799,
      "bound_eq9_normalized": 0.425451,
      "t_eq10": 1.398377,
      "bound_eq10_normalized": 0.2039
    },
    "rho_0.07": {
      "t_eq8": 2.306192,
      "bound_eq8_normalized": 0.477296,
      "t_eq9": 0.742033,
      "bound_eq9_normalized": 0.449388,
      "t_eq10": 1.275131,
      "bound_eq10_normalized": 0.258104
    },
    "rho_0.10": {
      "t_eq8": 2.145966,
      "bound_eq8_normalized": 0.610517,
      "t_eq9": 0.718096,
      "bound_eq9_normalized": 0.484338,
      "t_eq10": 1.140171,
      "bound_eq10_normalized": 0.328794
    },
    "rho_0.25": {
      "t_eq8": 1.665109,
      "bound_eq8_normalized": 1.068147,
      "t_eq9": 0.598413,
      "bound_eq9_normalized": 0.641901,
      "t_eq10": 0.765775,
      "bound_eq10_normalized": 0.582858
    },
    "rho_0.50": {
      "t_eq8": 1.17741,
      "bound_eq8_normalized": 1.443147,
      "t_eq9": 0.398942,
      "bound_eq9_normalized": 0.840845,
      "t_eq10": 0.436327,
      "bound_eq10_normalized": 0.8313
    }
  },
  "block_sparse_and_nuclear_bounds": {
    "block_sparse_k5_m200_s40": {
      "mu_k": 2.127692,
      "t_eq24": 4.030191,
      "bound_eq24_normalized": 0.87751,
      "t_eq25": 1.702154,
      "bound_eq25_normalized": 0.420535,
      "mc_mean_normalized": 0.413873
    },
    "nuclear_norm_50x40_r4": {
      "t_prop5": 0.904311,
      "bound_prop5_normalized": 0.983644,
      "bound_crpw_normalized": 0.516
    }
  },
  "corrupted_sensing_thresholds": {
    "wyner_coding_max_corruption_fraction_gamma0": 0.192845,
    "demixing_p500_ssig5_n1200_gamma002": {
      "t_sig": 1.945111,
      "t_cor": 1.717437,
      "lambda_penalized_ratio": 0.88295,
      "eta_sig": 5.533713,
      "eta_cor": 11.18113,
      "tau_theorem1_constrained": 13.581611,
      "tau_theorem2_penalized": 30.87449,
      "mu_n_lower_bound": 34.626591
    }
  }
}
```

Verified in pure Python: (1) for l_1 subdifferential squared distance in R^p (p=1000), Foygel & Mackey's dense-regime bound Eq. (9) p*(1 - (2/pi)*(1 - s/p)^2) is strictly below p for all s/p < 1 and strictly tighter than Chandrasekaran et al.'s bound Eq. (8) 2s*log(p/s) + 1.5*s for all s/p >= 0.07 (at s/p = 0.07: 0.449388 vs 0.477296; at s/p = 0.25: 0.641901 vs 1.068147); (2) Proposition 4 block-sparse l_1/l_2 dense bound Eq. (25) at k=5, m=200, s=40 evaluates to 0.420535*p (Monte Carlo mean: 0.413873*p) vs sparse bound Eq. (24) 0.877510*p, and Proposition 5 nuclear-norm bound at m1=50, m2=40, r=4 evaluates to 0.983644*m1*m2 < m1*m2; and (3) Corollary 1 Wyner coding max corruption fraction where psi_l1(gamma_0) = 0.5 solves to gamma_0 = 0.192845 (~= 19.3%), and Theorems 1 & 2 recovery thresholds at p=500, s_sig=5, n=1200, gamma_cor=0.02 satisfy tau_thm1 = 13.5816 < tau_thm2 = 30.8745 < mu_n = 34.6266 with penalty ratio lambda = t_cor/t_sig = 0.88295.
