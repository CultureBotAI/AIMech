# Literature Discovery Report: Selectively Traversed Accumulation Rules for Structured False Discovery Rate Control

- **Report ID**: `20261017T143500Z-selectively-traversed-accumulation-rules-for-structured-fdr-control`
- **Created At**: `2026-10-17T14:35:00Z`
- **Curated Concept**: `AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl` (`data/curated/SelectivelyTraversedAccumulationRulesForStructuredFDRControl.yaml`, SHA-256 `d701f5a7c2cc640bfc6cfa0d3fd87253f9f6a5f231a80bcaa14901dbf52486a9`)
- **Verification Script**: `research/discovery/selectively-traversed-accumulation-rules-for-structured-fdr-control-boundaries.py` (SHA-256 `744b9e21b9908f3caaf31e3db9c1b5deb95d1c587578b6cb799e1e890b7b6ea9`)

## Primary Sources Inspected

1. **Lei, Ramdas, & Fithian (2021)** — *A general interactive framework for false discovery rate control under structural constraints*, *Biometrika* 108(2):253–267, `DOI:10.1093/biomet/asaa064`, `arXiv:1710.02776v2`. Complete full-text HTML conversion read (`sha256: 0aca9bd13ad69478f54a7497ca753df3b5b0fc7304c8304e0e8287292dbb76fa`), Crossref metadata (`sha256: f2e31895442898d6f0b6b6cdf46fc6bce259ed9304652a2694f7ba10d70c65ba`), and arXiv abstract (`sha256: 64ad42aee0a91894f831dc3d3206c4009c4a8eca793a8ae966c3876770962de2`).

## Candidate Decisions

- **`AIMech:SelectivelyTraversedAccumulationRulesForStructuredFDRControl`** (`ADD_CURATED`): Interactive partial-masking and accumulation-function peeling framework (STAR) for finite-sample FDR control under arbitrary structural constraints (Lei, Ramdas, & Fithian 2021).

## Constructed Mathematical Verification Summary

```json
{
  "claim1_accumulation_masking_and_prop21": {
    "forwardstop_max_H_inversion_err": 0.0,
    "seqstep_max_H_symmetry_err": 0.0,
    "seqstep_max_unif_cond_exp_err": 0.0,
    "seqstep_min_beta21_cond_exp": 1.155556
  },
  "claim2_tree_heredity_fdr_and_bottom_up_power": {
    "bh_subtree_constraint_valid_rate": 0.0,
    "fdr_star_tree": 0.049024,
    "power_star_bottom_up": 0.839,
    "power_topdown_hierarchical": 0.271,
    "star_subtree_constraint_valid_rate": 1.0
  },
  "claim3_one_group_em_and_structured_knockoffs": {
    "em_vs_oracle_initial_corr": 0.971733,
    "fdr_em_convex_interval": 0.067853,
    "fdr_structured_knockoffs": 0.050822,
    "power_canonical_convex_interval": 0.864286,
    "power_em_convex_interval": 0.965476,
    "power_structured_knockoffs": 0.783333
  },
  "claim4_asymptotic_power_and_small_alpha_boundary": {
    "fdr_filtration_violating_peeking_global_null": 1.0,
    "min_rejections_alpha_0_10_pstar_0_20": 12,
    "min_rejections_alpha_0_10_pstar_0_50": 19,
    "plain_accumulation_critical_pi1": 0.804109,
    "power_masked_star_uninformative_order": 0.819583,
    "power_plain_accumulation_uninformative_order": 0.0
  }
}
```
