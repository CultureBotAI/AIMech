# Literature Discovery Report: Universal Inference Split Likelihood Ratio Test

- **Report ID**: `20261017T113500Z-universal-inference-split-likelihood-ratio-test`
- **Created At**: `2026-10-17T11:35:00Z`
- **Curated Concept**: `AIMech:UniversalInferenceSplitLikelihoodRatioTest` (`data/curated/UniversalInferenceSplitLikelihoodRatioTest.yaml`, SHA-256 `f5e33b1cf0e7733ebbd66e466e65044fa2b6d418a03440714eb82cc7fbff5ebb`)
- **Verification Script**: `research/discovery/universal-inference-split-likelihood-ratio-test-boundaries.py` (SHA-256 `79549673f23da64fe3c839c1aa39066f7cb504a442fd84a21ad33c8053381ac6`)

## Primary Sources Inspected

1. **Wasserman, Ramdas, & Balakrishnan (2020)** — *Universal inference*, *Proceedings of the National Academy of Sciences* 117(29):16880–16890, `arXiv:1912.11436` (DOI `https://doi.org/10.1073/pnas.1922664117`). Complete full-text HTML conversion read (`sha256: 8788c234c31afd9bdb1614119555440c6c3855125c481ee2320e671b5fa1b5ba`).
2. **Vovk & Wang (2021)** — *E-values: Calibration, combination, and applications*, *The Annals of Statistics* 49(3):1736–1754, `arXiv:1912.06116` (DOI `https://doi.org/10.1214/20-AOS2020`). Complete full-text HTML conversion read (`sha256: 9ca237ebcb8210baf90d91a42ec337bc99f9adf64612f606376e46a241184eda`).
3. **Wang & Ramdas (2022)** — *False discovery rate control with e-values*, *Journal of the Royal Statistical Society: Series B (Statistical Methodology)* 84(3):822–852, `arXiv:2009.02824` (DOI `https://doi.org/10.1111/rssb.12489`). Complete full-text HTML conversion read (`sha256: 26bd39717641ca16a7b1bbfc1d1e962853428ad3fbcbf6a82687bfa6536e901c`).

## Candidate Decisions

- **`AIMech:UniversalInferenceSplitLikelihoodRatioTest`** (`ADD_CURATED`): Regularity-free, finite-sample hypothesis testing and confidence set construction framework (Wasserman, Ramdas, & Balakrishnan 2020) based on sample-split, crossfit, reversed-information-projection (RIPR), and running-MLE sequential likelihood ratio statistics.

## Constructed Mathematical Verification Summary

```json
{
  "section_3_multivariate_normal": {
    "alpha": 0.05,
    "approx_sq_radius_full_lrt": 2.760074,
    "asymptotic_leading_ratio": 4.0,
    "d": 500,
    "expected_sq_radius_split": 10.059915,
    "finite_d_ratio": 3.644799,
    "n_per_split": 100
  },
  "section_5_uniform_crossfit": {
    "alpha": 0.05,
    "crossfit_interval": [
      9.85,
      11.845114
    ],
    "crossfit_length": 1.995114,
    "n_per_split": 20,
    "pivotal_2n_interval": [
      9.85,
      10.616026
    ],
    "pivotal_2n_length": 0.766026,
    "split_interval_degenerate_infinite": true,
    "theta_hat_0": 9.85,
    "theta_hat_1": 9.6,
    "theta_true": 10.0
  },
  "section_6_powered_likelihood": {
    "eta": 0.5,
    "mu_0": 0.0,
    "mu_1": 1.2,
    "powered_expectation_analytical": 0.83527,
    "powered_expectation_quadrature": 0.83527,
    "renyi_divergence_d_eta": 0.36
  },
  "section_8_running_mle_sequential": {
    "anytime_p_bar_t": [
      1.0,
      1.0,
      1.0,
      1.0,
      1.0,
      1.0,
      1.0,
      1.0
    ],
    "l_t_oracle_martingale": [
      0.985112,
      0.932394,
      0.843665,
      0.843665,
      0.834227,
      0.834227,
      0.833185,
      0.821786
    ],
    "m_t_running_mle": [
      0.980199,
      0.904837,
      0.843665,
      0.839457,
      0.834227,
      0.827993,
      0.827846,
      0.821786
    ],
    "max_m_t_minus_l_t": 0.0
  },
  "theorems_1_and_3_validity": {
    "alpha": 0.05,
    "mean_un_split": 0.626315,
    "mean_wn_crossfit": 0.627306,
    "n_per_split": 10,
    "type1_error_crossfit": 0.0,
    "type1_error_split": 0.0,
    "un_exceeds_tn_violations": 0
  }
}
```
