# Literature Discovery Report: Sub-Psi Uniform Boundary Confidence Sequences

- **Report ID**: `20261017T122000Z-sub-psi-uniform-boundary-confidence-sequences`
- **Created At**: `2026-10-17T12:20:00Z`
- **Curated Concept**: `AIMech:SubPsiUniformBoundaryConfidenceSequences` (`data/curated/SubPsiUniformBoundaryConfidenceSequences.yaml`, SHA-256 `8ad6737fae460a74a9f3c534284689f281dee04b225a5674ce91eb8488d3976a`)
- **Verification Script**: `research/discovery/sub-psi-uniform-boundary-confidence-sequences-boundaries.py` (SHA-256 `640c73a06e047f75e60eb228fb8098595fb406734c6ca1cea22a729499b6777f`)

## Primary Sources Inspected

1. **Howard, Ramdas, McAuliffe, & Sekhon (2021)** — *Time-uniform, nonparametric, nonasymptotic confidence sequences*, *The Annals of Statistics* 49(2):1055–1080, `arXiv:1810.08240` (DOI `https://doi.org/10.1214/20-AOS1991`). Complete full-text HTML conversion read (`sha256: aef352a6e271a2317826f200bf481b2aaf956b978323ee8a2b25b589c2ec1732`).
2. **Waudby-Smith & Ramdas (2024)** — *Estimating means of bounded random variables by betting*, *Journal of the Royal Statistical Society Series B: Statistical Methodology* 86(1):1–27, `arXiv:2010.09686` (DOI `https://doi.org/10.1093/jrsssb/qkad009`). Complete full-text HTML conversion read (`sha256: c41bcb5ff7e35853316a0709b17b18506ef1e4be8252a3a474ed38a4811f2495`).
3. **Shin, Ramdas, & Rinaldo (2024)** — *E-detectors: A nonparametric framework for sequential change detection*, *The New England Journal of Statistics in Data Science* 2(2):229–260, `arXiv:2203.03532` (DOI `https://doi.org/10.51387/23-NEJSDS51`). Complete full-text HTML conversion read (`sha256: 0c9c5ade08a826f69dd0bddfd9c25efe4fe6bcf34b7db331e2c55b90ecf50d73`).

## Candidate Decisions

- **`AIMech:SubPsiUniformBoundaryConfidenceSequences`** (`ADD_CURATED`): Nonparametric, nonasymptotic sub-psi exponential supermartingale uniform boundary and confidence sequence framework (Howard, Ramdas, McAuliffe, & Sekhon 2021) encompassing polynomial epoch stitching, conjugate normal/beta-binomial/gamma-exponential/gamma-Poisson mixtures with Lambert W_(-1) tuning, geometric discrete mixtures, inverted stitching, and self-normalized empirical Bernstein / adaptive IPW ATE confidence sequences.

## Constructed Mathematical Verification Summary

```json
{
  "empirical_bernstein_and_ate_cs": {
    "ipw_ate_mean_width_t80": 1.5318,
    "ipw_ate_miscover_rate": 0.0,
    "max_fan_cond_expectation": 0.99991072,
    "skewed_naive_sn_miscover_rate": 0.752,
    "skewed_theorem4_eb_miscover_rate": 0.0
  },
  "mixture_boundaries_and_lambert_tuning": {
    "abs_deriv_at_v_tilde": 2.220446049250313e-12,
    "ge_c005_bound": 14.445871,
    "ge_c02_bound": 14.774393,
    "ge_c1_bound": 16.624195,
    "max_dm_nm_ratio": 1.027949,
    "max_nm_tilde_to_exact_ratio": 1.001892,
    "min_dm_nm_ratio": 1.000381,
    "one_sided_nm_bound": 14.337634,
    "rho_opt_v100_alpha0025": 10.253321
  },
  "psi_hierarchy_and_proposition1": {
    "min_gap_b_to_n": 8e-10,
    "min_gap_e_to_g": 1.692e-07,
    "min_gap_n_to_p": 1.671e-07,
    "min_gap_p_to_e": 1.688e-07,
    "min_prop1_p_to_g13": 1e-10
  },
  "stitching_theorem1_and_theorem3": {
    "inverted_stitch_crossing_bound": 0.028983,
    "max_endpoint_asymmetry": 8.881784197001252e-16,
    "min_stitched_dominance_gap": 0.584247,
    "zeta_1_4": 3.105547
  }
}
```
