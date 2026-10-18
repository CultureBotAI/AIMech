# Literature Discovery Report: Archimedean Copula Linear Step-Up False Discovery Rate Bounds and Calibration

- **Report ID**: `20261017T160500Z-archimedean-copula-step-up-fdr-bounds`
- **Created At**: `2026-10-17T16:05:00Z`
- **Curated Concept**: `AIMech:ArchimedeanCopulaStepUpFDRBounds` (`data/curated/ArchimedeanCopulaStepUpFDRBounds.yaml`, SHA-256 `8a1f1f0ef3c4ec4ac45ede2c42f6ada4aaff38b4a6c59bf4d2fc18265aef96d7`)
- **Verification Script**: `research/discovery/archimedean-copula-step-up-fdr-bounds-boundaries.py` (SHA-256 `da5b022585fa3b4817d326042847552ee57a044fb5a1b25555cc1ee7ca1a1c13`)

## Primary Sources Inspected

1. **Taras Bodnar & Thorsten Dickhaus (2014)** — *False discovery rate control under Archimedean copula*, *Electronic Journal of Statistics* 8(2):2207–2241, `DOI:10.1214/14-EJS950`, `arXiv:1305.3897v3`. Complete 33-page full-text PDF read (`sha256: 16fbee085fb678e3980d53b58c99b8b359af995fad0b9b9dd20d18b45f4329d0`), full-text ar5iv HTML conversion (`sha256: e227a5c91b327fad11af3a8af354663c481ca4f05c132d3298d522b07bdb195a`), Crossref metadata (`sha256: 56e5fff839d0f6457f478539e8d6d5f820d819d08edded5fd4d41d1834ba9f01`), and arXiv abstract (`sha256: ba7e5b4627fc554fc9289c78b0a335eadeb0b667812b56832235bbc01c13c36a`).

## Candidate Decisions

- **`AIMech:ArchimedeanCopulaStepUpFDRBounds`** (`ADD_CURATED`): Marshall–Olkin conditionally independent representation of Archimedean p-value copulae with completely monotone generators (Theorem 2.1), sharper finite-sample upper FDR bound for the Benjamini–Hochberg linear step-up test via Bolshev's order-statistic recursion (Theorem 3.1, Corollary 3.1, Equations (26)–(27)), generator-dependent lower FDR bound and Clayton incomplete-gamma closed form (Theorem 3.2, Lemma 3.1, Corollary 3.2, Equations (24)–(25)), infinite H_0-exchangeable Archimedean MTP_2 characterization (Theorem 3.3, Corollary 3.3), and Kendall's tau nominal-level calibration (Section 5, Equations (34)–(35)).

## Constructed Mathematical Verification Summary

```json
{
  "all_assertions_passed": true,
  "benchmark_parameters": {
    "classical_upper_bound": 0.04,
    "m": 20,
    "m0": 16,
    "q": 0.05
  },
  "clayton_bounds_by_eta": {
    "0.05": {
      "conservativity_reduction_b": 0.000144,
      "fz_z_star": 0.185002,
      "gamma_min": 0.738765,
      "lower_bound": 0.029551,
      "sharper_upper_bound": 0.039856,
      "z_star": 0.79802562
    },
    "0.5": {
      "conservativity_reduction_b": 0.003583,
      "fz_z_star": 0.016381,
      "gamma_min": 0.316445,
      "lower_bound": 0.012658,
      "sharper_upper_bound": 0.036417,
      "z_star": 0.09646312
    },
    "1.0": {
      "conservativity_reduction_b": 0.007506,
      "fz_z_star": 0.007853,
      "gamma_min": 0.188575,
      "lower_bound": 0.007543,
      "sharper_upper_bound": 0.032494,
      "z_star": 0.00788351
    },
    "1.7": {
      "conservativity_reduction_b": 0.009607,
      "fz_z_star": 0.005362,
      "gamma_min": 0.12503,
      "lower_bound": 0.005001,
      "sharper_upper_bound": 0.030393,
      "z_star": 0.00019325
    },
    "10.0": {
      "conservativity_reduction_b": 0.005763,
      "fz_z_star": 0.002933,
      "gamma_min": 0.060225,
      "lower_bound": 0.002409,
      "sharper_upper_bound": 0.034237,
      "z_star": 0.0
    },
    "2.0": {
      "conservativity_reduction_b": 0.009764,
      "fz_z_star": 0.004889,
      "gamma_min": 0.111783,
      "lower_bound": 0.004471,
      "sharper_upper_bound": 0.030236,
      "z_star": 3.754e-05
    },
    "3.0": {
      "conservativity_reduction_b": 0.009275,
      "fz_z_star": 0.004036,
      "gamma_min": 0.088324,
      "lower_bound": 0.003533,
      "sharper_upper_bound": 0.030725,
      "z_star": 1.4e-07
    },
    "5.0": {
      "conservativity_reduction_b": 0.007905,
      "fz_z_star": 0.003391,
      "gamma_min": 0.071541,
      "lower_bound": 0.002862,
      "sharper_upper_bound": 0.032095,
      "z_star": 0.0
    }
  },
  "clayton_large_m_lower_bound": {
    "20": {
      "fdr_lower_bound": 0.007543,
      "fz_z_star": 0.007853,
      "gamma_min": 0.188575,
      "z_star": 0.00788351
    },
    "200": {
      "fdr_lower_bound": 0.001246,
      "fz_z_star": 0.00133,
      "gamma_min": 0.031142,
      "z_star": 0.00133124
    },
    "2000": {
      "fdr_lower_bound": 0.000172,
      "fz_z_star": 0.00019,
      "gamma_min": 0.004293,
      "z_star": 0.00019012
    }
  },
  "concept_id": "AIMech:ArchimedeanCopulaStepUpFDRBounds",
  "gumbel_z_star_by_eta": {
    "1.0": 1.0,
    "10.0": 5.03e-08,
    "2.0": 0.1112694002,
    "5.0": 0.0004005219,
    "6.6": 2.23504e-05
  },
  "kendall_tau_calibration_verification": {
    "clayton_eta_2": {
      "closed_form": 0.5,
      "integral": 0.5
    },
    "gumbel_eta_2": {
      "closed_form": 0.5,
      "integral": 0.5
    }
  },
  "primary_source": "Bodnar & Dickhaus (2014), Electronic Journal of Statistics 8(2):2207-2241 (arXiv:1305.3897v3, DOI:10.1214/14-EJS950)"
}
```
