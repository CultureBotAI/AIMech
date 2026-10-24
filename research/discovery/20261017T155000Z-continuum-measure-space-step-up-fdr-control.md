# Literature Discovery Report: Measure-Theoretic Step-Up False Discovery Rate Control over a Continuum of Null Hypotheses

- **Report ID**: `20261017T155000Z-continuum-measure-space-step-up-fdr-control`
- **Created At**: `2026-10-17T15:50:00Z`
- **Curated Concept**: `AIMech:ContinuumMeasureSpaceStepUpFDRControl` (`data/curated/ContinuumMeasureSpaceStepUpFDRControl.yaml`, SHA-256 `498a31bc6bb08aee30af0e7c6162801b1333a932df59620b4b1eb56820498444`)
- **Verification Script**: `research/discovery/continuum-measure-space-step-up-fdr-control-boundaries.py` (SHA-256 `90505e6d0a7b136c344cac46fbda4f4a89cfefecb68e0bda9f7073f01fc123a7`)

## Primary Sources Inspected

1. **Gilles Blanchard, Sylvain Delattre, & Etienne Roquain (2014)** — *Testing over a continuum of null hypotheses with False Discovery Rate control*, *Bernoulli* 20(1):304–333, `DOI:10.3150/12-BEJ488`, `arXiv:1110.3599v3`. Complete full-text HTML conversion read (`sha256: 0c5b44767d9b127b3025caf9e8635a00e8fbb3f7c30b03b14c76c32c484b86b4`), Crossref metadata (`sha256: 2909e735cb9f3519c4d2adc54538488b059d49ec2f5d2bf4ebe0a28ce31b8c51`), and arXiv abstract (`sha256: 7e9bacb4fb6ccd032391dead7b496d0e653a42ea748dc2dd3e90d2107ecd15d8`).

## Candidate Decisions

- **`AIMech:ContinuumMeasureSpaceStepUpFDRControl`** (`ADD_CURATED`): Equivalence of four infinite-dimensional weak PRDS characterizations via Strassen's theorem (Proposition 2.2), continuum step-up fixed-point measurability and Glivenko–Cantelli empirical measure discretization proof of continuum FDR control (Lemma 3.1, Theorem 4.1, Lemmas 5.1–5.3), exact finite-sum Lebesgue step-up formula `gamma(u)` for continuous c.d.f. testing (Proposition 4.2, Corollary 4.4, Remark 4.6), and exact data-dependent interval-length weighted step-up reduction for Poisson process intensity testing (Proposition 4.3, Corollary 4.5, Remark 4.6).

## Constructed Mathematical Verification Summary

```json
{
  "all_assertions_passed": true,
  "concept_id": "AIMech:ContinuumMeasureSpaceStepUpFDRControl",
  "primary_source": "Blanchard, Delattre, & Roquain (2014), Bernoulli 20(1):304-333 (arXiv:1110.3599v3, DOI:10.3150/12-BEJ488)",
  "section_4_1_and_5_1_continuum_and_discretization": {
    "alpha": 0.05,
    "continuum_leb_L_Delta_at_r_hat": 0.5,
    "continuum_r_hat_exact": 0.5,
    "discrete_grid_r_hats": {
      "100": 0.5,
      "1000": 0.5,
      "20": 0.5,
      "50": 0.5,
      "500": 0.5
    },
    "max_n_times_abs_error": 0.0
  },
  "section_4_2_1_cdf_continuum_step_up": {
    "alpha": 0.1,
    "fixed_point_abs_residual": 0.0,
    "gamma_at_alpha_r_hat": 0.647923,
    "m": 8,
    "r_hat_continuum": 0.647923,
    "riemann_quadrature_leb": 0.64795
  },
  "section_4_2_2_poisson_process_weighted_step_up": {
    "alpha": 0.05,
    "critical_q_val_at_k_hat": 0.026499,
    "k_hat_index": 10,
    "lambda_0": 5.0,
    "n_arrivals": 12,
    "r_hat_weighted_step_up": 0.95,
    "smallest_q_val": 0.000202,
    "volume_fixed_point_check": 0.95
  }
}
```
