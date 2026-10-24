# Discovery Report: Self-Concordant and Pseudo-Self-Concordant Finite-Sample M-Estimation (Round 222)

- **Report ID**: `20261018T194500Z-self-concordant-m-estimators-finite-sample`
- **Created At**: `2026-10-18T19:45:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:SelfConcordantAndPseudoSelfConcordantFiniteSampleMEstimation` (`data/curated/SelfConcordantAndPseudoSelfConcordantFiniteSampleMEstimation.yaml`)
- **Verification Script**: `research/discovery/self-concordant-m-estimators-finite-sample-boundaries.py` (SHA-256: `58dacd884323f5998f2abfc88150d7fe8672d73603a12e652f682cc19ae3b023`)

## Summary of Primary Sources Inspected

1. **Dmitrii M. Ostrovskii & Francis Bach (2021)**, *Finite-sample analysis of M-estimators using self-concordance*, *Electronic Journal of Statistics* 15(1):326-391, `arXiv:1810.06838v2`, `DOI:10.1214/20-EJS1780`.
   - Read all 55 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/bcea2e3a2e65cc86.pdf`, `2123949` bytes, SHA-256 `4cd6b917ea4081156f3b9b504b4e0eeaab6687e4ef208c011a58774d365e85fd`), arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3396/content.md`, `7223` bytes, SHA-256 `bfce471f8b0111c7770bbc4cfc3a74b42a179cb802de878c9b16c9d1b64e2882`), and Crossref metadata (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3397/content.md`, `6997` bytes, SHA-256 `fdb2c75847490720d9a1cdffe799735a74f23d799ac786646c809cdc139809c8`).

## Constructed Boundary & Regime Verification

```text
{
  "concept_id": "AIMech:SelfConcordantAndPseudoSelfConcordantFiniteSampleMEstimation",
  "all_passed": true,
  "check_1_self_concordant_losses": {
    "passed": true,
    "max_logistic_sca_ratio": 0.999909,
    "max_pseudo_huber_sca_ratio": 1.5,
    "standard_pseudo_huber_scb_ratio_at_t50": 21.2111,
    "max_fenchel_duality_err": 5.24913446042774e-13,
    "max_novel_loss_scb_ratio": 2.82832,
    "theoretical_2sqrt2_bound": 2.828427
  },
  "check_2_propositions_b3_b4": {
    "passed": true,
    "max_localization_ratio_case_a": 2.42,
    "max_localization_ratio_case_b": 2.666667,
    "proposition_b4_bound": 4.0,
    "lemma_b3_coefficients": [
      0.333333,
      1.0
    ]
  },
  "check_3_dikin_hessian_and_gaussian_logistic": {
    "passed": true,
    "dikin_hessian_factors": [
      0.444444,
      4.0
    ],
    "rho_over_1_plus_t3_grid": [
      4.0,
      3.4668,
      1.8357,
      1.0656,
      0.9015,
      0.8416
    ],
    "kappa_perp_times_1_plus_t_grid": [
      0.25,
      0.4132,
      0.4543,
      0.4559,
      0.446,
      0.4379
    ]
  }
}
```

Executed pure-Python verification in research/discovery/self-concordant-m-estimators-finite-sample-boundaries.py (SHA-256 58dacd884323f5998f2abfc88150d7fe8672d73603a12e652f682cc19ae3b023): verified (1) Section 2.1 pseudo-self-concordance for logistic and smooth pseudo-Huber losses and canonical self-concordance (<= 2 sqrt(2)) and Fenchel duality phi''(varphi'(t)) varphi''(t) = 1 for the novel loss (Eq. 21); (2) Propositions B.3-B.4 Taylor remainder bracketing and localization radius <= 4 ||nabla F(theta_0)||_{H_0^{-1}}; and (3) Theorem 4.1 Eq. (84) Dikin-ellipsoid Hessian stability factors [4/9, 4] and Proposition D.1 cubic curvature scaling rho ~ 1 + ||theta_*||_Sigma^3.
