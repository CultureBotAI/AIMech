# Literature Discovery Report: Catoni-Style Heavy-Tailed Confidence Sequences

- **Report ID**: `20261017T125000Z-catoni-style-heavy-tailed-confidence-sequences`
- **Created At**: `2026-10-17T12:50:00Z`
- **Curated Concept**: `AIMech:CatoniStyleHeavyTailedConfidenceSequences` (`data/curated/CatoniStyleHeavyTailedConfidenceSequences.yaml`, SHA-256 `5b4dc96917166cb9c70ab7d896501c5f167f5495329e712584ff212feff5b126`)
- **Verification Script**: `research/discovery/catoni-style-heavy-tailed-confidence-sequences-boundaries.py` (SHA-256 `3eed62c6d9bf2f8041ce323b4dfb4700ac8e98e23f811bb84bfb00de7e68f0f7`)

## Primary Sources Inspected

1. **Wang & Ramdas (2023)** — *Catoni-style confidence sequences for heavy-tailed mean estimation*, *Stochastic Processes and their Applications* 163:168–202, `arXiv:2202.01250` (DOI `https://doi.org/10.1016/j.spa.2023.05.007`). Complete full-text HTML conversion read (`sha256: e80a2fc7a2a49108bd3c276657ed1864c0ad1da6f784198574b0b0a92c444fd2`).
2. **Catoni (2012)** — *Challenging the empirical mean and empirical variance: A deviation study*, *Annales de l'Institut Henri Poincaré, Probabilités et Statistiques* 48(4):1148–1185, `arXiv:1009.2048` (DOI `https://doi.org/10.1214/11-AIHP454`). Publisher Crossref bibliographic and abstract record (`sha256: af6e53dac76c890dc1f787d9fea25c0b34bc47f8a7dedf80a9e6570ac9e83334`).
3. **Howard, Ramdas, McAuliffe, & Sekhon (2021)** — *Time-uniform, nonparametric, nonasymptotic confidence sequences*, *The Annals of Statistics* 49(2):1055–1080, `arXiv:1810.08240` (DOI `https://doi.org/10.1214/20-AOS1991`). Complete full-text HTML conversion read (`sha256: aef352a6e271a2317826f200bf481b2aaf956b978323ee8a2b25b589c2ec1732`).

## Candidate Decisions

- **`AIMech:CatoniStyleHeavyTailedConfidenceSequences`** (`ADD_CURATED`): Nonasymptotic, anytime-valid sequential confidence sequence framework (Wang & Ramdas 2023) for heavy-tailed and infinite-variance conditional means using Catoni and $p$-Catoni influence supermartingales.

## Constructed Mathematical Verification Summary

```json
{
  "all_assertions_passed": true,
  "check_1_influence_and_supermartingale": {
    "max_influence_bound_violation": 0.0,
    "mc_supermartingale_factor_neg_t3": 0.947503,
    "mc_supermartingale_factor_pos_t3": 0.962479,
    "prop16_underestimated_variance_factor": 1.013879
  },
  "check_2_three_cs_comparison_and_topology": {
    "catoni_widths_by_alpha": {
      "0.0001": 1.10578,
      "0.01": 0.67182,
      "0.1": 0.45491,
      "1e-06": 1.54006
    },
    "dubins_savage_widths_by_alpha": {
      "0.0001": 1821.73855,
      "0.01": 18.458,
      "0.1": 2.06454,
      "1e-06": 182149.79306
    },
    "max_delyon_violation": 0.0,
    "sn_outlier_discriminant_pos": 62.9567
  },
  "check_3_anytime_coverage_and_theorem10": {
    "alpha": 0.1,
    "peeking_clt_miscoverage_rate": 0.564,
    "sequential_catoni_miscoverage_rate": 0.0,
    "thm10_quadratic_root_bound_holds": true
  },
  "check_4_infinite_variance_p_catoni": {
    "max_lemma21_violation": 0.0,
    "max_phi_p_violation": 0.0,
    "p_catoni_miscoverage_rate": 0.0,
    "p_exponent": 1.5,
    "p_moment_bound_v": 5.999999999999999,
    "pareto_tail_index": 1.8,
    "width_t150": 4.7246,
    "width_t20": 8.3089
  },
  "concept_id": "AIMech:CatoniStyleHeavyTailedConfidenceSequences"
}
```
