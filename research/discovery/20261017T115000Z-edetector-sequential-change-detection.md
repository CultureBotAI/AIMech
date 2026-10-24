# Literature Discovery Report: E-Detector Nonparametric Sequential Change Detection

- **Report ID**: `20261017T115000Z-edetector-sequential-change-detection`
- **Created At**: `2026-10-17T11:50:00Z`
- **Curated Concept**: `AIMech:EDetectorSequentialChangeDetection` (`data/curated/EDetectorSequentialChangeDetection.yaml`, SHA-256 `fb34abf117f642f21e36f7f68a8f3ea10faf4ace751965b8188ef139e36f1956`)
- **Verification Script**: `research/discovery/edetector-sequential-change-detection-boundaries.py` (SHA-256 `2a262a7aec4e2ef658299ad40388851fd64cbea481fb7ed77244e6a04ba35857`)

## Primary Sources Inspected

1. **Shin, Ramdas, & Rinaldo (2024)** — *E-detectors: A nonparametric framework for sequential change detection*, *The New England Journal of Statistics in Data Science* 2(2):229–260, `arXiv:2203.03532` (DOI `https://doi.org/10.51387/23-NEJSDS51`). Complete full-text HTML conversion read (`sha256: 0c9c5ade08a826f69dd0bddfd9c25efe4fe6bcf34b7db331e2c55b90ecf50d73`).
2. **Wasserman, Ramdas, & Balakrishnan (2020)** — *Universal inference*, *Proceedings of the National Academy of Sciences* 117(29):16880–16890, `arXiv:1912.11436` (DOI `https://doi.org/10.1073/pnas.1922664117`). Complete full-text HTML conversion read (`sha256: 8788c234c31afd9bdb1614119555440c6c3855125c481ee2320e671b5fa1b5ba`).
3. **Vovk & Wang (2021)** — *E-values: Calibration, combination, and applications*, *The Annals of Statistics* 49(3):1736–1754, `arXiv:1912.06116` (DOI `https://doi.org/10.1214/20-AOS2020`). Complete full-text HTML conversion read (`sha256: 9ca237ebcb8210baf90d91a42ec337bc99f9adf64612f606376e46a241184eda`).

## Candidate Decisions

- **`AIMech:EDetectorSequentialChangeDetection`** (`ADD_CURATED`): Nonparametric, nonasymptotic sequential changepoint detection framework (Shin, Ramdas, & Rinaldo 2024) based on Shiryaev-Roberts (`e-SR`), CUSUM (`e-CUSUM`), and adaptive mixture `e`-detectors constructed from sequential `e_j`-processes and baseline increments.

## Constructed Mathematical Verification Summary

```json
{
  "all_checks_passed": true,
  "check_1_nonstationary_arl_and_recursion": {
    "fixed_tau": 15,
    "max_one_step_cond_exp": 1.0,
    "max_recursive_vs_explicit_diff": 1.7763568394002505e-15,
    "mc_arl_cu": 477.528,
    "mc_arl_sr": 42.3337,
    "mc_mean_m_sr_at_tau": 9.1734,
    "target_arl": 20.0
  },
  "check_2_adaptive_infinite_mixture": {
    "gamma_1": 2.0,
    "gamma_32": 1.000489,
    "k_sched_at_32": 11,
    "max_adaptive_recursive_vs_doublesum_diff": 1.4210854715202004e-14,
    "max_telescoping_identity_err": 3.552713678800501e-15
  },
  "check_3_convex_conjugate_and_betting": {
    "bernoulli_kl_conjugate_diff": 6.938893903907228e-17,
    "betting_strictly_dominates_subexp": true,
    "min_pointwise_betting_over_subexp_ratio": 1.0,
    "post_change_betting_drift": 0.153346,
    "post_change_subexp_drift": 0.119561
  },
  "check_4_lorden_reduction_and_supremum": {
    "mean_mixture_sr_at_tau": 19.8293,
    "mean_post_change_delay_lorden_cu": 34.4495,
    "mean_post_change_delay_sr": 16.8817,
    "mean_unpenalized_sup_sr_at_tau": 37.7737,
    "null_fixed_tau": 20,
    "sr_strictly_faster_fraction": 1.0
  },
  "concept_id": "AIMech:EDetectorSequentialChangeDetection"
}
```
