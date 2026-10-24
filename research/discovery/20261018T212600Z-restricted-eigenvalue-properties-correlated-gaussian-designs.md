# Discovery Report: Restricted Eigenvalue Properties for Correlated Gaussian Designs (Round 231)

- **Report ID**: `20261018T212600Z-restricted-eigenvalue-properties-correlated-gaussian-designs`
- **Created At**: `2026-10-18T21:26:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:RestrictedEigenvaluePropertiesForCorrelatedGaussianDesigns` (`data/curated/RestrictedEigenvaluePropertiesForCorrelatedGaussianDesigns.yaml`)
- **Verification Script**: `research/discovery/restricted-eigenvalue-properties-correlated-gaussian-designs-boundaries.py` (SHA-256: `b3b186a30560deeebdcab3422efa07c2b1764a9b90f4690d5441c76113246b46`)

## Summary of Primary Sources Inspected

1. **Garvesh Raskutti, Martin J. Wainwright, & Bin Yu (2010)**, *Restricted Eigenvalue Properties for Correlated Gaussian Designs*, *Journal of Machine Learning Research* 11:2241-2259.
   - Read all 19 pages of the full-text JMLR PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/29b83a210f1059e9.pdf`, `153447` bytes, SHA-256 `6d4ad6baf930abe80799b6a09539e2a3b723b9b34c21b015a1b46e44322758fa`) and JMLR v11 metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3674/content.md`, `6481` bytes, SHA-256 `906be5efecb9205bc6956ea6c875e8a07419b2e8da63025d44b7e50ea160f401`).

## Constructed Boundary & Regime Verification

```text
{
  "concept_id": "AIMech:RestrictedEigenvaluePropertiesForCorrelatedGaussianDesigns",
  "Check1_gordon_comparison_and_re_transfer": {
    "max_eq6_identity_error": 2.6645352591003757e-15,
    "min_z_minus_y_variance_gap": 0.4526264032507925,
    "max_equal_v_variance_error": 3.1086244689504383e-15,
    "n_critical_for_gamma_over_8": 3433309.6535231275,
    "n_sample": 4291638,
    "transferred_re_constant": 0.11055729062341194,
    "target_gamma_over_8": 0.1,
    "passed": true
  },
  "Check2_re_vs_rip_and_rank_degenerate_examples": {
    "spiked_condition_numbers": [
      13.0,
      49.0,
      193.0,
      769.0
    ],
    "min_spiked_re_ratio": 0.5000007648379385,
    "theoretical_spiked_gamma": 0.5,
    "rank_degenerate_null_residual": 3.7601811162233617e-16,
    "null_vector_sc_over_s_l1_ratio": 12.683601190739575,
    "min_cone_gain_on_rank_degenerate_design": 0.615489879946578,
    "passed": true
  },
  "Check3_lipschitz_concentration_and_peeling": {
    "max_scaled_lipschitz_ratio": 0.1302400374144608,
    "exact_dyadic_peeling_sum": 0.04703610351665924,
    "linearized_geometric_peeling_bound": 0.04816830158705827,
    "passed": true
  },
  "all_passed": true
}
```

Executed pure-Python verification in research/discovery/restricted-eigenvalue-properties-correlated-gaussian-designs-boundaries.py (SHA-256 b3b186a30560deeebdcab3422efa07c2b1764a9b90f4690d5441c76113246b46): verified (1) the Gordon-Slepian variance identity and inequality in Equation (6) (max identity error 2.66e-15, min variance gap 0.4526 >= 0, exact equality error 3.11e-15 when v = v') and Corollary 1 RE transfer constant 0.1106 >= gamma / 8 = 0.10; (2) Example 2 spiked-identity submatrix condition numbers [13.0, 49.0, 193.0, 769.0] diverging as k grows (violating RIP) while satisfying RE with gamma = 0.5, and Example 3 rank-degenerate covariance (n = 14 < p = 28) having a nullspace vector outside C(S; 1) (ratio 12.68 > 1) while maintaining positive gain >= 0.615 on C(S; 1); and (3) Lemma 2 Frobenius-Lipschitz scaling ratio 0.1302 <= 1.0 and Lemma 3 dyadic peeling geometric series bound (0.047036 <= 0.048168).
