# Literature Discovery Report: Betting Confidence Sequences for Bounded Random Variables

- **Report ID**: `20261017T120500Z-betting-confidence-sequences-bounded-means`
- **Created At**: `2026-10-17T12:05:00Z`
- **Curated Concept**: `AIMech:BettingConfidenceSequencesForBoundedMeans` (`data/curated/BettingConfidenceSequencesForBoundedMeans.yaml`, SHA-256 `b7a7f4290f77d5f8152269f60afdaa354defb0251adccd88be92f055839249c7`)
- **Verification Script**: `research/discovery/betting-confidence-sequences-bounded-means-boundaries.py` (SHA-256 `4b0517ad99853a9c3e7acc869f676d86cb99040030f3afbad8918aa97c90c994`)

## Primary Sources Inspected

1. **Waudby-Smith & Ramdas (2024)** — *Estimating means of bounded random variables by betting*, *Journal of the Royal Statistical Society Series B: Statistical Methodology* 86(1):1–27, `arXiv:2010.09686` (DOI `https://doi.org/10.1093/jrsssb/qkad009`). Complete full-text HTML conversion read (`sha256: c41bcb5ff7e35853316a0709b17b18506ef1e4be8252a3a474ed38a4811f2495`).
2. **Shin, Ramdas, & Rinaldo (2024)** — *E-detectors: A nonparametric framework for sequential change detection*, *The New England Journal of Statistics in Data Science* 2(2):229–260, `arXiv:2203.03532` (DOI `https://doi.org/10.51387/23-NEJSDS51`). Complete full-text HTML conversion read (`sha256: 0c9c5ade08a826f69dd0bddfd9c25efe4fe6bcf34b7db331e2c55b90ecf50d73`).
3. **Vovk & Wang (2021)** — *E-values: Calibration, combination, and applications*, *The Annals of Statistics* 49(3):1736–1754, `arXiv:1912.06116` (DOI `https://doi.org/10.1214/20-AOS2020`). Complete full-text HTML conversion read (`sha256: 9ca237ebcb8210baf90d91a42ec337bc99f9adf64612f606376e46a241184eda`).

## Candidate Decisions

- **`AIMech:BettingConfidenceSequencesForBoundedMeans`** (`ADD_CURATED`): Nonparametric, nonasymptotic betting martingale and predictable plug-in empirical Bernstein confidence sequence framework (Waudby-Smith & Ramdas 2024) for estimating means of bounded random variables with and without replacement.

## Constructed Mathematical Verification Summary

```json
{
  "hoeffding_dominance_and_el_duality": {
    "duality_err": 2.220446049250313e-16,
    "k_hs": 1.341183,
    "lam_hs": 1.53092,
    "max_abs_gamma_lam045": 0.541779,
    "min_hoeffding_dominance_gap": 2.632767e-06,
    "owen_el_reciprocal": 1.341183,
    "weight_sum_err": 0.0,
    "weighted_mean_err": 5.551115123125783e-17
  },
  "proposition2_and_theorem2": {
    "max_fan_diff": 0.243085,
    "max_martingale_err": 0.0,
    "mean_width_eb_t60": 0.2489,
    "mean_width_h_t60": 0.3762,
    "mean_width_hedged_t60": 0.1105,
    "min_eb_supermartingale_gap": 7.8e-05,
    "miscoverage_rate_eb": 0.0,
    "miscoverage_rate_h": 0.0,
    "miscoverage_rate_hedged": 0.0
  },
  "quasiconvexity_and_agrapa_counterexample": {
    "agrapa_k2_m003": 0.888166,
    "agrapa_k2_m008": 0.715576,
    "agrapa_k2_m040": 0.533333,
    "min_second_diff_hgkelly": 0.00021072
  },
  "without_replacement_cs": {
    "mean_width_wor_t20": 0.2137,
    "mean_width_wor_t35": 0.0776,
    "mean_width_wor_t40": 0.0205,
    "mean_width_wr_t20": 0.2932,
    "mean_width_wr_t35": 0.187,
    "mean_width_wr_t40": 0.1685,
    "miscover_wor": 0,
    "wor_martingale_err": 0.0
  }
}
```
