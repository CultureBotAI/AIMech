# Literature Discovery Report: Exchangeable Largest Crossing Point Asymptotic False Discovery Rate and Global-Null Independence Limit Discontinuity

- **Report ID**: `20261017T163500Z-exchangeable-lcp-asymptotic-fdr-and-independence-limit`
- **Created At**: `2026-10-17T16:35:00Z`
- **Curated Concept**: `AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit` (`data/curated/ExchangeableLCPAsymptoticFDRAndIndependenceLimit.yaml`, SHA-256 `5a5948219058695b6b9d05e01f7285fa8bbcd1e34f823569989125e9eeeb6f89`)
- **Verification Script**: `research/discovery/exchangeable-lcp-asymptotic-fdr-and-independence-limit-boundaries.py` (SHA-256 `f7ec7aa036a9b8ddb765aaf850463eafbb2045eb21ad6232747b4708b5740865`)

## Primary Sources Inspected

1. **Helmut Finner, Thorsten Dickhaus, & Markus Roters (2007)** — *Dependency and false discovery rate: Asymptotics*, *The Annals of Statistics* 35(4):1432–1455, `DOI:10.1214/009053607000000046`, `arXiv:0710.3171v1`. Complete 24-page full-text PDF read (`sha256: 4ccb7542eb74ebb0671426a33e69e1d491f85aa9550fddea15ce7734825e2ad5`), Crossref metadata (`sha256: e64def78de013934ccd4465c4a5b758a1de6c233e8ab4a78e7fd361952eceeaf`), and arXiv abstract (`sha256: 734f9e1d24f8ddd31d65202b4704a69a15b311cc42377a9cf4cdc52f7187e911`).

## Candidate Decisions

- **`AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit`** (`ADD_CURATED`): Conditional empirical c.d.f. $F_\infty(t \mid z, \zeta)$ and Largest Crossing Point (LCP) $t(z \mid \zeta)$ representation of exchangeable multiple testing under $\mathrm{D\text{-}EX}(\zeta_n)$ (Lemma 2.1, Theorems 2.1–2.2), complete-null boundary derivative law $\mathrm{FDR}_\infty(1) = P^Z(E_1) + \alpha \int_{E_0} \gamma(z)\,dP^Z(z)$ and shifted exponential $\mathrm{MTP}_2$ invariance (Lemma 2.2, Example 2.3, Theorems 2.3–2.4), equicorrelated normal tangent-point jump $(t_1, t_2)$ and global-null double-limit discontinuity $\lim_{\rho\to 0^+} \mathrm{FDR}_\infty(1) = \Phi(-\sqrt{-2\ln(\alpha)}) < \alpha$ (Theorems 3.1–3.3, Remark 3.1), and jointly studentized normal $\mathrm{D\text{-}EX\text{-}t}(\zeta_n)$ crossing interval and $\nu \to \infty$ global-null limit (Lemma 4.1, Theorems 4.1–4.3).

## Constructed Mathematical Verification Summary

```json
{
  "all_assertions_passed": true,
  "concept_id": "AIMech:ExchangeableLCPAsymptoticFDRAndIndependenceLimit",
  "lemma_2_2_and_example_2_3_verification": {
    "alpha": 0.2,
    "fdr_cond_exact_steck": 0.11982106,
    "fdr_cond_lemma_2_2": 0.11982106,
    "gamma_z": 0.89865793,
    "n": 6,
    "n0": 4,
    "unconditional_fdr_example_2_3": 0.13333333,
    "z": 0.8
  },
  "lemma_4_1_and_theorem_4_3_studentized_t_scaling": {
    "a2_times_1_minus_s2": 11.98535,
    "a4_over_nu": 11.989846,
    "clt_quantile_at_nu_100000": -2.447535,
    "exact_clt_limit": -2.447747,
    "exact_minus_4_ln_alpha": 11.982929,
    "nu": 100000000
  },
  "primary_source": "Finner, Dickhaus, & Roters (2007), Annals of Statistics 35(4):1432-1455 (arXiv:0710.3171v1, DOI:10.1214/009053607000000046)",
  "theorem_3_1_zeta_0_5_verification": {
    "alpha": 0.05,
    "eer_at_rho_0_001": 0.01282205,
    "eer_at_rho_0_5": 0.01423388,
    "eer_independent_limit": 0.01282051,
    "fdr_at_rho_0_001": 0.02499943,
    "fdr_at_rho_0_5": 0.02371742,
    "fdr_independent_limit": 0.025,
    "zeta": 0.5
  },
  "theorem_3_2_and_3_3_global_null_discontinuity": {
    "alpha": 0.05,
    "discontinuity_ratio_alpha_over_limit": 6.9564,
    "fdr_infty_1_limit_as_rho_to_0": 0.00718763,
    "independent_global_null_fdr": 0.05,
    "rho_grid_evaluations": {
      "0.0001": {
        "fdr_infty_1": 0.007188,
        "fdr_remark31_upper_bound": 0.007188,
        "x0_remark31_upper_bound": -2.447726,
        "x0_tp": -2.447726
      },
      "0.001": {
        "fdr_infty_1": 0.007192,
        "fdr_remark31_upper_bound": 0.007192,
        "x0_remark31_upper_bound": -2.447542,
        "x0_tp": -2.447542
      },
      "0.01": {
        "fdr_infty_1": 0.007229,
        "fdr_remark31_upper_bound": 0.007229,
        "x0_remark31_upper_bound": -2.445693,
        "x0_tp": -2.445696
      },
      "0.1": {
        "fdr_infty_1": 0.007623,
        "fdr_remark31_upper_bound": 0.00763,
        "x0_remark31_upper_bound": -2.426129,
        "x0_tp": -2.426493
      },
      "0.5": {
        "fdr_infty_1": 0.010288,
        "fdr_remark31_upper_bound": 0.010673,
        "x0_remark31_upper_bound": -2.301807,
        "x0_tp": -2.315686
      }
    },
    "x0_limit_minus_sqrt_minus_2ln_alpha": -2.44774683
  }
}
```
