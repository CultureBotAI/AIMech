# Literature Discovery Report: Hadamard-Differentiable Threshold Functional False Discovery Proportion Central Limit Theorems and Adaptive Fixed-Point Iteration Duality

- **Report ID**: `20261017T164500Z-hadamard-differentiable-threshold-fdp-asymptotics-and-fixed-point-duality`
- **Created At**: `2026-10-17T16:45:00Z`
- **Curated Concept**: `AIMech:HadamardDifferentiableThresholdFDPAsymptoticsAndFixedPointDuality` (`data/curated/HadamardDifferentiableThresholdFDPAsymptoticsAndFixedPointDuality.yaml`, SHA-256 `6e35c0df6b71a10d35d4bfc2b25558014c91114141256210ef1fa9d1a78424c4`)
- **Verification Script**: `research/discovery/hadamard-differentiable-threshold-fdp-asymptotics-and-fixed-point-duality-boundaries.py` (SHA-256 `61f04d706936a8e688debd34c8272be725e0cf3245799f5846cc5dc18b0ed72c`)

## Primary Sources Inspected

1. **Pierre Neuvial (2008)** — *Asymptotic properties of false discovery rate controlling procedures under independence*, *Electronic Journal of Statistics* 2:1065–1110, `DOI:10.1214/08-EJS207`, `arXiv:0803.2111v2`. Complete 46-page full-text PDF read (`sha256: 2cceab6ae1b177b6f1d8545d7141e999b2f72b1ce1e0d3acc818186d8b597083`), Crossref metadata (`sha256: 7a40c41d638fa35910d669421226664235107cf1305da7563b6d50c7840074d9`), and arXiv abstract (`sha256: d2d2a7c0253fe0ebcb0d169776391f1c4e92855ff554e749e838f2c3ad7eb488`).

## Candidate Decisions

- **`AIMech:HadamardDifferentiableThresholdFDPAsymptoticsAndFixedPointDuality`** (`ADD_CURATED`): Functional Delta-method Central Limit Theorem for the random rejection threshold $\mathcal{T}(\widehat{\mathbb{G}}_m)$ and False Discovery Proportion $\mathrm{FDP}_m(\mathcal{T}(\widehat{\mathbb{G}}_m))$ of Hadamard-differentiable threshold functionals $\mathcal{T}(F) = \mathcal{U}(F, \mathcal{A}(F))$ (Theorems 3.2, 7.3, 7.13), $o(m^{-1/2})$ perturbation asymptotic equivalence (Proposition 3.6), explicit Gaussian limit laws and variances for $\mathrm{BH95}$, $\mathrm{BH95o}$, $\mathrm{FDR08}(\lambda)$, $\mathrm{BR08}(\lambda)$, $\mathrm{Sto02}(\lambda)/\mathrm{STS04}(\lambda)$, and $\mathrm{BKY06}(\lambda)$ (Theorems 4.2, 4.7, 4.10, 4.12, 4.15, Corollary 4.16, Theorem 4.20), and fixed-point iteration duality linking $\mathrm{Sto02}(\lambda) \to \mathrm{FDR08}$ and $\mathrm{BKY06}(\lambda) \to \mathrm{BR08}(\lambda)$ (Theorems 5.2, 5.4, 5.6, Corollaries 5.3, 5.5, 5.7).

## Constructed Mathematical Verification Summary

```json
{
  "all_assertions_passed": true,
  "concept_id": "AIMech:HadamardDifferentiableThresholdFDPAsymptoticsAndFixedPointDuality",
  "primary_source": "Neuvial (2008), Electronic Journal of Statistics 2:1065-1110 (arXiv:0803.2111v2, DOI:10.1214/08-EJS207)",
  "section_4_1_figure_2_laplace_criticality": {
    "alpha_star_critical_value": 0.23840584,
    "g_at_0": 4.19452805,
    "pi0": 0.5,
    "tau_star_at_alpha_0_20_subcritical": 0.0,
    "tau_star_at_alpha_0_35_supercritical": 0.16987268,
    "theta": 2.0
  },
  "section_4_and_table_1_gaussian_location_benchmark": {
    "alpha": 0.1,
    "bky06_power_reversal_when_G_le_sqrt_x": {
      "bh95_dominates_bky06": true,
      "tau_bh95": 0.00277008,
      "tau_bky06": 0.00110293
    },
    "kappa_fdr08": 0.07407407,
    "lambda": 0.5,
    "mu": 2.5,
    "pi0": 0.6,
    "procedures": {
      "BH95": {
        "asymptotic_fdp_variance": 0.11089207,
        "asymptotic_fdr": 0.06,
        "tau_star": 0.03144323
      },
      "BH95o_oracle": {
        "asymptotic_fdp_variance": 0.15245313,
        "asymptotic_fdr": 0.1,
        "tau_star": 0.06155622
      },
      "BKY06_lambda": {
        "asymptotic_fdp_variance": 0.13053507,
        "asymptotic_fdr": 0.0674767,
        "tau_star": 0.03671522,
        "u_lambda": 0.27770105
      },
      "BR08_lambda": {
        "asymptotic_fdp_variance": 0.0925982,
        "asymptotic_fdr": 0.04156844,
        "tau_star": 0.01928073
      },
      "FDR08": {
        "asymptotic_fdp_variance": 0.16057545,
        "asymptotic_fdr": 0.08818369,
        "tau_star": 0.05219201
      },
      "Sto02_STS04_lambda": {
        "asymptotic_fdp_variance": 0.18099179,
        "asymptotic_fdr": 0.09917884,
        "tau_star": 0.0608935
      }
    }
  },
  "section_5_fixed_point_duality_verification": {
    "bky06_to_br08_fixed_point_at_lambda_alpha_over_1_plus_alpha": {
      "abs_error": 0.0,
      "iterated_limit": 0.0488615394,
      "lambda_orig": 0.09090909,
      "tau_bky06_first_stage": 0.04477524,
      "tau_br08_exact": 0.0488615394,
      "u_lambda_init": 0.02771361
    },
    "sto02_to_fdr08_fixed_point": {
      "abs_error": 0.0,
      "iterated_from_t0_0_01": 0.052192013,
      "iterated_from_t0_0_50": 0.052192013,
      "tau_fdr08_exact": 0.052192013
    }
  }
}
```
