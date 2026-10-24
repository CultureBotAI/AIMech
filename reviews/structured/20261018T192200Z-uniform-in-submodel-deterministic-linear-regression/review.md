# Scientific author self-review of Uniform-in-submodel deterministic linear regression and functional dependence bounds

- Review: 20261018T192200Z-uniform-in-submodel-deterministic-linear-regression
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-18T19:20:00Z
- Finished UTC: 2026-10-18T19:22:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Uniform-in-submodel deterministic linear regression and functional dependence bounds as a distinct DRAFT mathematical_method with related LinearRegression mapping. All four claims and locators across Kuchibhotla et al. (2021, arXiv:1802.05801v3) are supported with explicit k-sparse eigenvalue and functional-dependence tail-exponent limitations.

## Scope And Provenance

All fields of the exact maintained UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds record and its primary evidence.

Selection: Exact maintained ID: AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 37fd7d487c56bb239087f03743b2b316c9572238.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds | data/curated/UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds.yaml | maintained | Uniform-in-submodel deterministic linear regression and functional dependence bounds |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds | All 442 AIO concept records are valid. |
| aimech validate-curated | passed | True | AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds | All 614 curated concept records are valid. |
| aimech seed --check | passed | True | AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds | All 442 AIO records match the pinned source. |
| aimech validate-history | passed | True | AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds | All history sidecars are valid. |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds | Vendored CLAW files are in sync. |
| aimech check-source | passed | True | AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds | Exited 0 without output. |
| Constructed Kuchibhotla et al. 2021 deterministic uniform-in-submodel l2/Bahadur bounds, fixed-design exact linearity, and functional dependence checks | passed | True | AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds | {<br>  "concept_id": "AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds",<br>  "regime_1_and_2_deterministic_uniform_submodel_bounds": {<br>    "num_submodels_checked": 25,<br>    "rip_k": 0.044466,<br>    "lambda_k": 0.618356,<br>    "s_2_k": 1.033686,<br>    "eq24_target_bound_rhs": 1.463597,<br>    "max_thm1_lhs_to_rhs_ratio": 0.280772,<br>    "max_thm3_bahadur_ratio": 0.628329,<br>    "theorem_1_3_eq24_and_remark_3_3_verified": true<br>  },<br>  "regime_3_fixed_design_and_covering": {<br>    "max_fixed_design_bahadur_remainder": 0.0,<br>    "stirling_subset_bound_holds": true,<br>    "remark_4_3_and_eq26_verified": true<br>  },<br>  "regime_4_functional_dependence_sub_weibull": {<br>    "alpha_prod": 0.666667,<br>    "s_alpha_prod": 0.5,<br>    "omega_fast_nu_gt_half": 1.0,<br>    "omega_crit_nu_eq_half": 79.06031,<br>    "omega_slow_nu_lt_half": 100.0,<br>    "lemma4_lhs_over_rhs": 1.0,<br>    "functional_dependence_verified": true<br>  },<br>  "all_passed": true<br>} |

## Scientific And Domain Assessments

### Distinctness of Uniform-in-submodel deterministic linear regression and functional dependence bounds

identity: supported. Targets: AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds.

Distinct from normal-equation PoSI confidence regions, GBO sub-Weibull Lasso, and single-model moving-target OLS.

Confirmed via normalized identity check and full-text reading of Kuchibhotla et al. (2021, arXiv:1802.05801v3).

### AIO mapping for AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds

grounding: supported. Targets: AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds.

related_match to AIO:LinearRegression is accurate.

Pinned AIO (2026-07-22) contains LinearRegression broadly without uniform-in-submodel deterministic Bahadur bounds or functional dependence sub-Weibull concentration.

### Definition and scope

evidence: supported. Targets: AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds.

Definition accurately captures the general regression map beta_M(Sigma, Gamma), deterministic uniform l2 and Bahadur linear representation bounds, epsilon-net discretization, and functional dependence sub-Weibull concentration.

All equations and claims verified against Sections 1-5 and Appendices A-B of arXiv:1802.05801v3.

### deterministic-uniform-in-submodel-l2-and-l1-consistency-bounds

evidence: supported. Targets: AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds.

Supported by Sections 3.1-3.3 (Theorems 1-2, Remark 3.1, Equation 24) and boundary script.

Verified Theorem 1 across all 25 submodels (max ratio 0.280772 &lt;= 1.0) and Equation (24) moving-target bound (1.033686 &lt;= 1.463597).

### deterministic-uniform-in-submodel-bahadur-linear-representation-and-sandwiching

evidence: supported. Targets: AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds.

Supported by Section 3.2 (Theorems 3-4, Corollary 1, Remarks 3.2-3.3) and boundary script.

Verified Theorem 3 Bahadur linear representation bound across all 25 submodels (max ratio 0.628329 &lt;= 1.0) and Remark 3.3 factor-of-2 sandwiching.

### epsilon-net-sparse-sphere-discretization-and-fixed-design-exact-linearity

evidence: supported. Targets: AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds.

Supported by Section 4 (Theorems 5-6, Remark 4.3, Equations 25-27) and boundary script.

Verified Remark 4.3 identically zero Bahadur remainder (0.0) under fixed covariates and Equation (26) covering bound.

### functional-dependence-adjusted-sub-weibull-concentration-for-time-series

evidence: supported. Targets: AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds.

Supported by Section 5 and Appendix B (Theorems 7-12, Lemmas 1-4, Equations 28-45) and boundary script.

Verified effective tail exponent s(alpha), three Omega_n(nu) growth regimes, and Lemma 4 product persistence.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds.

The full record is consistent; retain DRAFT.

Read every field of UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, two primary sources with exact SHA-256 digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261018T192000Z-uniform-in-submodel-deterministic-linear-regression.json | supports | No normalized identity match for Uniform-in-submodel deterministic linear regression and functional dependence bounds across 442 pinned AIO records and 613 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected LinearRegression in the pinned AIO snapshot (2026-07-22). Provides accurate related_match context. |
| calculation | research/discovery/uniform-in-submodel-deterministic-linear-regression-boundaries.py | supports | Executed pure-Python verification in research/discovery/uniform-in-submodel-deterministic-linear-regression-boundaries.py (SHA-256 33976ceb4a86ff7dbf216bae8075e43707c7750cf81b5a6bc08ba4f282a06641): verified (1) Theorem 1 deterministic uniform-in-submodel l2 estimation error bound and Equation (24) moving-target bound across all 25 submodels M in M(k); (2) Theorem 3 deterministic uniform-in-submodel Bahadur linear representation bound and Remark 3.3 factor-of-2 sandwiching; (3) Remark 4.3 identically zero Bahadur remainder under fixed design and Equation (26) k-sparse unit-sphere covering bound; and (4) Section 5 / Theorem 12 / Lemma 4 functional dependence norms, effective tail exponent s(alpha) = (1/2 + 1/alpha)^{-1}, three Omega_n(nu) regimes, and product persistence. |
| kuchibhotla2021-unif-submodel-pdf | https://arxiv.org/pdf/1802.05801; Pages 1-41, Sections 1-5 and Appendices A-B (Theorems 1-12, Corollary 1, Lemmas 1-4) | supports | All 41 pages of the full-text PDF of arXiv:1802.05801v3 read. Checked all definitions, theorems, lemmas, and proofs. |
| kuchibhotla2021-unif-submodel-abs | https://arxiv.org/abs/1802.05801; arXiv:1802.05801v3 abstract | supports | arXiv abstract and submission metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Uniform-in-submodel deterministic linear regression and functional dependence bounds record, yielding 614 native and 442 unchanged generated records.
- All 41 PDF pages of arXiv:1802.05801v3 were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261018T192200Z-uniform-in-submodel-deterministic-linear-regression
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Uniform-in-submodel deterministic linear regression
  and functional dependence bounds
started_at: '2026-10-18T19:20:00Z'
finished_at: '2026-10-18T19:22:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from SimultaneousNormalEquationPostSelectionConfidenceRegions,
    GeneralizedBernsteinOrliczSubWeibullConcentrationAndHighDimensionalLasso, and
    UnifiedAssumptionLeanMovingTargetLinearRegressionAndScoreBootstrap, verified Theorems
    1-4 deterministic uniform-in-submodel consistency and Bahadur linear representation
    bounds, Equation 24 moving-target bound, Remark 4.3 fixed-design exact zero Bahadur
    remainder, and Theorem 12 / Lemmas 1-4 functional dependence sub-Weibull concentration,
    and documented five typographical notes in arXiv:1802.05801v3 (pp. 10, 19, 25,
    31, 31/36/37). This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Uniform-in-submodel deterministic linear regression and functional
  dependence bounds as a distinct DRAFT mathematical_method with related LinearRegression
  mapping. All four claims and locators across Kuchibhotla et al. (2021, arXiv:1802.05801v3)
  are supported with explicit k-sparse eigenvalue and functional-dependence tail-exponent
  limitations.
source:
  git_revision: 37fd7d487c56bb239087f03743b2b316c9572238
  state: working_tree
  inputs:
  - path: data/aio/LinearRegression.yaml
    sha256: 9b6f1b2ea06d9a47e5f7cf94c66afeaa6d40c3e7d0fdb5037d2c25fabc6d8167
    role: context
  - path: data/curated/GeneralizedBernsteinOrliczSubWeibullConcentrationAndHighDimensionalLasso.yaml
    sha256: 8df5e9c9871f408d2708a2e4b45b9912ffa056933a9735cb65259d56fd7cb36b
    role: context
  - path: data/curated/SimultaneousNormalEquationPostSelectionConfidenceRegions.yaml
    sha256: 50d7b68b232bb3e4e37990bc59735d2b4982e758bf384b286217cfa25ac49c4d
    role: context
  - path: data/curated/UnifiedAssumptionLeanMovingTargetLinearRegressionAndScoreBootstrap.yaml
    sha256: 1d198602c98642314bc45566f4085b7861709858658de496e302580fd8657b8d
    role: context
  - path: data/curated/UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds.yaml
    sha256: 8c72d372e3af847143da742562b9064a9421a6fccf403ed4b44f7dba25eda63c
    role: target
  - path: research/discovery/20261018T192000Z-uniform-in-submodel-deterministic-linear-regression.json
    sha256: 02d6228fdb6d8f35781f5f9cbdf020c6aa2478e0e83db7a041d82b432dfe26db
    role: context
  - path: research/discovery/uniform-in-submodel-deterministic-linear-regression-boundaries.py
    sha256: 33976ceb4a86ff7dbf216bae8075e43707c7750cf81b5a6bc08ba4f282a06641
    role: context
  - path: sources/aio/aio.json
    sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
    role: context
  - path: sources/aio/source.yaml
    sha256: a12f1e974c25fab2ebff5e44150fb86f64399471accdf0baeafd986f00e6f345
    role: context
  - path: src/aimech/curated.py
    sha256: 67cc03d7def5f62490cc1f5db320a7c18fdfd41cebf43a35ad2bb88c32cd40d5
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: a4b7e2f0327eb784d2c5b98c713534f644adf3a7848d4e3c2995e772425725c4
    role: context
targets:
- target_id: AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds
  path: data/curated/UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds.yaml
  label: Uniform-in-submodel deterministic linear regression and functional dependence
    bounds
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds.yaml
    role: maintained
scope:
  description: All fields of the exact maintained UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds
  exclusions:
  - target: Existing native and AIO neighbors
    reason: Identity and mapping context, not full scientific rereview.
checks:
- check_id: maintain-1
  name: aimech validate
  command: aimech validate
  status: passed
  required: true
  target_ids:
  - AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO concept records are valid.
- check_id: maintain-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: All 614 curated concept records are valid.
- check_id: maintain-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO records match the pinned source.
- check_id: maintain-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: All history sidecars are valid.
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW files are in sync.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed Kuchibhotla et al. 2021 deterministic uniform-in-submodel l2/Bahadur
    bounds, fixed-design exact linearity, and functional dependence checks
  command: python3 research/discovery/uniform-in-submodel-deterministic-linear-regression-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"concept_id\": \"AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds\"\
    ,\n  \"regime_1_and_2_deterministic_uniform_submodel_bounds\": {\n    \"num_submodels_checked\"\
    : 25,\n    \"rip_k\": 0.044466,\n    \"lambda_k\": 0.618356,\n    \"s_2_k\": 1.033686,\n\
    \    \"eq24_target_bound_rhs\": 1.463597,\n    \"max_thm1_lhs_to_rhs_ratio\":\
    \ 0.280772,\n    \"max_thm3_bahadur_ratio\": 0.628329,\n    \"theorem_1_3_eq24_and_remark_3_3_verified\"\
    : true\n  },\n  \"regime_3_fixed_design_and_covering\": {\n    \"max_fixed_design_bahadur_remainder\"\
    : 0.0,\n    \"stirling_subset_bound_holds\": true,\n    \"remark_4_3_and_eq26_verified\"\
    : true\n  },\n  \"regime_4_functional_dependence_sub_weibull\": {\n    \"alpha_prod\"\
    : 0.666667,\n    \"s_alpha_prod\": 0.5,\n    \"omega_fast_nu_gt_half\": 1.0,\n\
    \    \"omega_crit_nu_eq_half\": 79.06031,\n    \"omega_slow_nu_lt_half\": 100.0,\n\
    \    \"lemma4_lhs_over_rhs\": 1.0,\n    \"functional_dependence_verified\": true\n\
    \  },\n  \"all_passed\": true\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261018T192000Z-uniform-in-submodel-deterministic-linear-regression.json
  accessed_at: '2026-10-18T19:20:00Z'
  support: supports
  summary: No normalized identity match for Uniform-in-submodel deterministic linear
    regression and functional dependence bounds across 442 pinned AIO records and
    613 maintained IDs, names, aliases and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-18T19:20:00Z'
  support: supports
  summary: Inspected LinearRegression in the pinned AIO snapshot (2026-07-22). Provides
    accurate related_match context.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/uniform-in-submodel-deterministic-linear-regression-boundaries.py
  accessed_at: '2026-10-18T19:20:00Z'
  snapshot_sha256: 33976ceb4a86ff7dbf216bae8075e43707c7750cf81b5a6bc08ba4f282a06641
  support: supports
  summary: 'Executed pure-Python verification in research/discovery/uniform-in-submodel-deterministic-linear-regression-boundaries.py
    (SHA-256 33976ceb4a86ff7dbf216bae8075e43707c7750cf81b5a6bc08ba4f282a06641): verified
    (1) Theorem 1 deterministic uniform-in-submodel l2 estimation error bound and
    Equation (24) moving-target bound across all 25 submodels M in M(k); (2) Theorem
    3 deterministic uniform-in-submodel Bahadur linear representation bound and Remark
    3.3 factor-of-2 sandwiching; (3) Remark 4.3 identically zero Bahadur remainder
    under fixed design and Equation (26) k-sparse unit-sphere covering bound; and
    (4) Section 5 / Theorem 12 / Lemma 4 functional dependence norms, effective tail
    exponent s(alpha) = (1/2 + 1/alpha)^{-1}, three Omega_n(nu) regimes, and product
    persistence.'
- evidence_id: kuchibhotla2021-unif-submodel-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/1802.05801
  locator: Pages 1-41, Sections 1-5 and Appendices A-B (Theorems 1-12, Corollary 1,
    Lemmas 1-4)
  accessed_at: '2026-10-18T11:55:00Z'
  snapshot_sha256: 9c5fdee6bbe4f85bdf03189e7e3d117235d38bbd6b51bca135eccaec8bc1ae4d
  support: supports
  summary: All 41 pages of the full-text PDF of arXiv:1802.05801v3 read. Checked all
    definitions, theorems, lemmas, and proofs.
- evidence_id: kuchibhotla2021-unif-submodel-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1802.05801
  locator: arXiv:1802.05801v3 abstract
  accessed_at: '2026-10-18T11:54:00Z'
  snapshot_sha256: 6b632e53f4daf2cb078d0170c85aa4de1dd7ef8d50962a206844765105ef3726
  support: supports
  summary: arXiv abstract and submission metadata read and verified.
assessments:
- assessment_id: identity-boundary
  area: identity
  topic: Distinctness of Uniform-in-submodel deterministic linear regression and functional
    dependence bounds
  outcome: supported
  target_ids:
  - AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds
  evidence_ids:
  - identity
  - kuchibhotla2021-unif-submodel-pdf
  - kuchibhotla2021-unif-submodel-abs
  summary: Distinct from normal-equation PoSI confidence regions, GBO sub-Weibull
    Lasso, and single-model moving-target OLS.
  details: Confirmed via normalized identity check and full-text reading of Kuchibhotla
    et al. (2021, arXiv:1802.05801v3).
- assessment_id: aio-mappings
  area: grounding
  topic: AIO mapping for AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds
  outcome: supported
  target_ids:
  - AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds
  evidence_ids:
  - mapping
  - kuchibhotla2021-unif-submodel-pdf
  summary: related_match to AIO:LinearRegression is accurate.
  details: Pinned AIO (2026-07-22) contains LinearRegression broadly without uniform-in-submodel
    deterministic Bahadur bounds or functional dependence sub-Weibull concentration.
- assessment_id: definition
  area: evidence
  topic: Definition and scope
  outcome: supported
  target_ids:
  - AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds
  evidence_ids:
  - kuchibhotla2021-unif-submodel-pdf
  - kuchibhotla2021-unif-submodel-abs
  summary: Definition accurately captures the general regression map beta_M(Sigma,
    Gamma), deterministic uniform l2 and Bahadur linear representation bounds, epsilon-net
    discretization, and functional dependence sub-Weibull concentration.
  details: All equations and claims verified against Sections 1-5 and Appendices A-B
    of arXiv:1802.05801v3.
- assessment_id: deterministic-uniform-in-submodel-l2-and-l1-consistency-bounds
  area: evidence
  topic: deterministic-uniform-in-submodel-l2-and-l1-consistency-bounds
  outcome: supported
  target_ids:
  - AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds
  evidence_ids:
  - kuchibhotla2021-unif-submodel-pdf
  - calculation
  summary: Supported by Sections 3.1-3.3 (Theorems 1-2, Remark 3.1, Equation 24) and
    boundary script.
  details: Verified Theorem 1 across all 25 submodels (max ratio 0.280772 <= 1.0)
    and Equation (24) moving-target bound (1.033686 <= 1.463597).
- assessment_id: deterministic-uniform-in-submodel-bahadur-linear-representation-and-sandwiching
  area: evidence
  topic: deterministic-uniform-in-submodel-bahadur-linear-representation-and-sandwiching
  outcome: supported
  target_ids:
  - AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds
  evidence_ids:
  - kuchibhotla2021-unif-submodel-pdf
  - calculation
  summary: Supported by Section 3.2 (Theorems 3-4, Corollary 1, Remarks 3.2-3.3) and
    boundary script.
  details: Verified Theorem 3 Bahadur linear representation bound across all 25 submodels
    (max ratio 0.628329 <= 1.0) and Remark 3.3 factor-of-2 sandwiching.
- assessment_id: epsilon-net-sparse-sphere-discretization-and-fixed-design-exact-linearity
  area: evidence
  topic: epsilon-net-sparse-sphere-discretization-and-fixed-design-exact-linearity
  outcome: supported
  target_ids:
  - AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds
  evidence_ids:
  - kuchibhotla2021-unif-submodel-pdf
  - calculation
  summary: Supported by Section 4 (Theorems 5-6, Remark 4.3, Equations 25-27) and
    boundary script.
  details: Verified Remark 4.3 identically zero Bahadur remainder (0.0) under fixed
    covariates and Equation (26) covering bound.
- assessment_id: functional-dependence-adjusted-sub-weibull-concentration-for-time-series
  area: evidence
  topic: functional-dependence-adjusted-sub-weibull-concentration-for-time-series
  outcome: supported
  target_ids:
  - AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds
  evidence_ids:
  - kuchibhotla2021-unif-submodel-pdf
  - calculation
  summary: Supported by Section 5 and Appendix B (Theorems 7-12, Lemmas 1-4, Equations
    28-45) and boundary script.
  details: Verified effective tail exponent s(alpha), three Omega_n(nu) growth regimes,
    and Lemma 4 product persistence.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds
  evidence_ids:
  - identity
  - mapping
  - kuchibhotla2021-unif-submodel-pdf
  - kuchibhotla2021-unif-submodel-abs
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of UniformInSubmodelDeterministicLinearRegressionAndFunctionalDependenceBounds.yaml:
    stable ID, name, aliases, mathematical_method kind, definition, definition_evidence,
    identity_notes, four claims and locators, two primary sources with exact SHA-256
    digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation
    metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Uniform-in-submodel deterministic linear regression and functional
  dependence bounds record, yielding 614 native and 442 unchanged generated records.
- All 41 PDF pages of arXiv:1802.05801v3 were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- uniform-in-submodel
- functional-dependence
- bahadur-representation
- self-review
- discovery-ongoing
```
