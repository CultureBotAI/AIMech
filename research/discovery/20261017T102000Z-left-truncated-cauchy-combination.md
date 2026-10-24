# Literature Discovery Report: Left-Truncated Cauchy Combination Test

- **Report ID**: `20261017T102000Z-left-truncated-cauchy-combination`
- **Created At**: `2026-10-17T10:20:00Z`
- **Curated Concept**: `AIMech:LeftTruncatedCauchyCombinationTest` (`data/curated/LeftTruncatedCauchyCombinationTest.yaml`, SHA-256 `6f330e91bd1f1994411c626759aee135f6dc781c2b3107e2c9db78e26c5685f6`)
- **Verification Script**: `research/discovery/left-truncated-cauchy-combination-boundaries.py` (SHA-256 `2d6f6f20afe04fc73872e4aaa7f71759ecb7a53d27dc59ded13b76302c9b91ea`)

## Primary Sources Inspected

1. **Fang, Chang, Park, & Tseng (2023)** — *Heavy-tailed distribution for combining dependent p-values with asymptotic robustness*, `arXiv:2103.12967` (*Statistica Sinica* 33, 1115–1142, DOI `https://doi.org/10.5705/ss.202021.0078`). Complete full-text HTML conversion read (`sha256: 432b18ec119b33e5b3cd66b32bb71015a243bb7dd28362cf7c9557f0e78a8402`).
2. **Gui, Jiang, & Wang (2023)** — *Aggregating Dependent Signals with Heavy-Tailed Combination Tests*, `arXiv:2310.20460v1` (DOI `https://doi.org/10.48550/arXiv.2310.20460`). Complete full-text HTML conversion read (`sha256: 3f487fc6bca4b5db326053b80a172ec71bee5387faa78dc2605e6bf91c795f71`).

## Candidate Decisions

- **`AIMech:LeftTruncatedCauchyCombinationTest`** (`ADD_CURATED`): Statistical $p$-value combination method bounding the left tail of the standard Cauchy transformation via Winsorized truncation $p_i^{\text{tr}} = \min(p_i, 1 - \delta)$ (Fang et al. 2023, Section 2.2, Propositions 3–4) or conditional left-truncation $Q_{F^{\text{trunc}}}(1 - p_i) = \tan(\pi(0.5 - p_0 p_i))$ (Gui, Jiang, & Wang 2023, Section 2.2, Table 1), eliminating unbounded negative score cancellation as $p_i \to 1$ while preserving regularly varying index $\gamma = 1$ asymptotic dependence robustness.

## Constructed Mathematical Verification Summary

```json
{
  "boundary_limits": {
    "cond_lower_bound_p0_09": -3.077683537175253,
    "max_rel_diff_p0_05_vs_half_cauchy": 6.104540043087295e-13,
    "max_rel_diff_p0_10_vs_standard_cauchy": 0.0,
    "winsorized_lower_bound_delta_001": -31.820515953773857
  },
  "cancellation_immunity_p1_1e-4_p2_1-1e-6": {
    "cond_left_truncated_combined_p_p0_09": 0.0002001741888014842,
    "cond_left_truncated_sum_stat_p0_09": 3533.6987649768485,
    "standard_cct_combined_p": 0.9999979797979806,
    "standard_cct_mean_stat": -157563.39371035108,
    "winsorized_left_truncated_combined_p_delta_001": 0.00020201951023418596,
    "winsorized_left_truncated_mean_stat_delta_001": 1575.6391205815275
  },
  "concept_id": "AIMech:LeftTruncatedCauchyCombinationTest",
  "fang_prop3_prop4_verification": {
    "mc_empirical_tail_prob": 0.00326,
    "n_tests": 10,
    "prop3_gclt_n50_delta001": {
      "f1n": 3.074140806502033,
      "f2n": 0.019411035201823756,
      "n_theta_n": 0.00889722814470506,
      "nu_delta": -31.820515953773857,
      "theta_n": 0.0001779445628941012
    },
    "prop4_binomial_upper_bound": 0.003516004233141369,
    "prop4_lower_bound": 0.003182992764908188,
    "prop4_sharp_upper_bound": 0.003471650826855522,
    "t_thresh": 100.0
  }
}
```
