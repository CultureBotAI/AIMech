# Discovery Report: Uniform-in-Submodel Deterministic Linear Regression and Functional Dependence Bounds (Round 219)

- **Report ID**: `20261018T192000Z-uniform-in-submodel-deterministic-linear-regression`
- **Created At**: `2026-10-18T19:20:00Z`
- **Skill**: `aimech-add-record`
- **Curated Concept**: `AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds` (`data/curated/UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds.yaml`)
- **Verification Script**: `research/discovery/uniform-in-submodel-deterministic-linear-regression-boundaries.py` (SHA-256: `33976ceb4a86ff7dbf216bae8075e43707c7750cf81b5a6bc08ba4f282a06641`)

## Summary of Primary Sources Inspected

1. **Kuchibhotla, Brown, Buja, George, & Zhao (2021)**, *Uniform-in-Submodel Bounds for Linear Regression in a Model Free Framework*, `arXiv:1802.05801v3`.
   - Read all 41 pages of the full-text PDF (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.tempmediaStorage/d5abb55950567864.pdf`, `473519` bytes, SHA-256 `9c5fdee6bbe4f85bdf03189e7e3d117235d38bbd6b51bca135eccaec8bc1ae4d`) and arXiv abstract (`/Users/marcin/.gemini/antigravity-cli/brain/955ab368-54c8-4c45-92dc-87b17d66740f/.system_generated/steps/3305/content.md`, `6389` bytes, SHA-256 `6b632e53f4daf2cb078d0170c85aa4de1dd7ef8d50962a206844765105ef3726`).

## Constructed Boundary & Regime Verification

```text
{
  "concept_id": "AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds",
  "regime_1_and_2_deterministic_uniform_submodel_bounds": {
    "num_submodels_checked": 25,
    "rip_k": 0.044466,
    "lambda_k": 0.618356,
    "s_2_k": 1.033686,
    "eq24_target_bound_rhs": 1.463597,
    "max_thm1_lhs_to_rhs_ratio": 0.280772,
    "max_thm3_bahadur_ratio": 0.628329,
    "theorem_1_3_eq24_and_remark_3_3_verified": true
  },
  "regime_3_fixed_design_and_covering": {
    "max_fixed_design_bahadur_remainder": 0.0,
    "stirling_subset_bound_holds": true,
    "remark_4_3_and_eq26_verified": true
  },
  "regime_4_functional_dependence_sub_weibull": {
    "alpha_prod": 0.666667,
    "s_alpha_prod": 0.5,
    "omega_fast_nu_gt_half": 1.0,
    "omega_crit_nu_eq_half": 79.06031,
    "omega_slow_nu_lt_half": 100.0,
    "lemma4_lhs_over_rhs": 1.0,
    "functional_dependence_verified": true
  },
  "all_passed": true
}
```

Executed pure-Python verification in research/discovery/uniform-in-submodel-deterministic-linear-regression-boundaries.py (SHA-256 33976ceb4a86ff7dbf216bae8075e43707c7750cf81b5a6bc08ba4f282a06641): verified (1) Theorem 1 deterministic uniform-in-submodel l2 estimation error bound and Equation (24) moving-target bound across all 25 submodels M in M(k); (2) Theorem 3 deterministic uniform-in-submodel Bahadur linear representation bound and Remark 3.3 factor-of-2 sandwiching; (3) Remark 4.3 identically zero Bahadur remainder under fixed design and Equation (26) k-sparse unit-sphere covering bound; and (4) Section 5 / Theorem 12 / Lemma 4 functional dependence norms, effective tail exponent s(alpha) = (1/2 + 1/alpha)^{-1}, three Omega_n(nu) regimes, and product persistence.
