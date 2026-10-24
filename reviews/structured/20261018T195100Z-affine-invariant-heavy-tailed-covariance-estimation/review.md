# Scientific author self-review of affine-invariant calibrated covariance estimation and heavy-tailed ridge regression

- Review: 20261018T195100Z-affine-invariant-heavy-tailed-covariance-estimation
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-18T19:50:00Z
- Finished UTC: 2026-10-18T19:51:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Affine-Invariant Calibrated Covariance Estimation and Heavy-Tailed Ridge Regression as a distinct DRAFT mathematical_method with related RidgeRegression and LinearRegression mappings. All four claims and locators across Ostrovskii &amp; Rudi (2019, COLT PMLR 99:2531-2550, arXiv:1902.03086v2) are supported with explicit sample-splitting logarithmic overhead, fourth-moment kurtosis, and ambient-dimension concentration limitations.

## Scope And Provenance

All fields of the exact maintained AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression record and its primary evidence.

Selection: Exact maintained ID: AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 5a5b356763bccaa1084722987b0f2610d7e3f1d9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression | data/curated/AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression.yaml | maintained | Affine-Invariant Calibrated Covariance Estimation and Heavy-Tailed Ridge Regression |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression | All 442 AIO concept records are valid. |
| aimech validate-curated | passed | True | AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression | All 618 curated concept records are valid. |
| aimech seed --check | passed | True | AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression | All 442 AIO records match the pinned source. |
| aimech validate-history | passed | True | AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression | All history sidecars are valid. |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression | Vendored CLAW files are in sync. |
| aimech check-source | passed | True | AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression | Exited 0 without output. |
| Constructed Ostrovskii &amp; Rudi 2019 dyadic regularization halving, Lepskii selection, and heavy-tailed ridge regression checks | passed | True | AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression | {<br>  "concept_id": "AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression",<br>  "all_passed": true,<br>  "check_1_lemmas_14_and_6": {<br>    "passed": true,<br>    "max_df_halving_ratio": 1.487357,<br>    "similarity_eigenvalue_range": [<br>      0.675676,<br>      1.923077<br>    ],<br>    "theoretical_similarity_bounds": [<br>      0.666667,<br>      2.0<br>    ],<br>    "max_trace_surrogate_diff_ratio": 0.475552<br>  },<br>  "check_2_algorithm1_and_lepskii": {<br>    "passed": true,<br>    "calibrated_error_alg1": 0.1238,<br>    "calibrated_error_wei_minsker_uncalibrated": 1.299639,<br>    "max_relative_diagonal_error_alg1": 0.092035,<br>    "lepskii_selected_theta": 4.0,<br>    "calibrated_error_lepskii": 0.157731<br>  },<br>  "check_3_theorem13_ridge_decomposition": {<br>    "passed": true,<br>    "E3_fixed_design_bias": 0.454459,<br>    "Eq47_bias_upper_bound": 0.753434,<br>    "E2_covariance_estimation_term": 0.444905,<br>    "Eq48_upper_bound": 0.467981<br>  }<br>} |

## Scientific And Domain Assessments

### Distinctness of affine-invariant calibrated covariance estimation and heavy-tailed ridge regression

identity: supported. Targets: AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression.

Distinct from Catoni operator-norm Gram matrix estimation, tournament/median-of-means ERM, and self-concordant M-estimation.

Confirmed via normalized identity check and full-text reading of Ostrovskii &amp; Rudi (2019, COLT PMLR 99:2531-2550).

### AIO mappings for AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression

grounding: supported. Targets: AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression.

related_match to AIO:RidgeRegression and AIO:LinearRegression are accurate.

Pinned AIO (2026-07-22) contains RidgeRegression and LinearRegression broadly without affine-invariant calibrated heavy-tailed covariance preconditioning.

### Definition and scope

evidence: supported. Targets: AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression.

Definition accurately captures Condition (HT), calibrated Loewner-order covariance bounds, Algorithm 1 dyadic regularization halving, Algorithm 2 Lepskii adaptation, and Theorem 13 heavy-tailed ridge regression.

All equations and claims verified against Sections 1-6 and Appendices A-D of Ostrovskii &amp; Rudi (2019).

### calibrated-covariance-problem-and-failure-of-uncalibrated-norm-clipping

evidence: supported. Targets: AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression.

Supported by Section 1 (Equations 1-5), Section 2.3 (Equations 6-13), and boundary script.

Verified failure of uncalibrated Wei-Minsker clipping (calibrated error 1.2996) vs. calibrated Algorithm 1 (calibrated error 0.1238) when lambda = 0.01 &lt;&lt; &#124;&#124;S&#124;&#124; = 100.

### dyadic-regularization-halving-single-step-and-multistage-calibrated-bounds

evidence: supported. Targets: AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression.

Supported by Sections 3-4 (Algorithm 1, Lemma 6, Theorem 7, Corollary 8), Appendices A-B (Lemma 14, Equations 35-38), and boundary script.

Verified Lemma 14 max df halving ratio 1.4874 &lt;= 2.0, Lemma 6 similarity eigenvalues [0.6757, 1.9231] subset [2/3, 2], and trace surrogate ratio 0.4756 &lt;= 3.0.

### lepskii-adaptive-threshold-selection-for-unknown-kurtosis-and-effective-dimension

evidence: supported. Targets: AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression.

Supported by Section 5 (Algorithm 2, Theorem 10, Corollary 11), Appendix C (Equations 39-43), and boundary script.

Verified Lepskii selection rule (Eq. 28) selecting theta_hat = 4.0 with calibrated error 0.1577.

### relative-eigenvalue-recovery-and-heavy-tailed-ridge-regression-excess-risk

evidence: supported. Targets: AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression.

Supported by Section 6 (Corollary 12, Theorem 13, Equations 31-34), Appendix D (Equations 44-50), and boundary script.

Verified Appendix D excess-risk decomposition E3 = 0.4545 &lt;= 0.7534 (Eq. 47) and E2 = 0.4449 &lt;= 0.4680 (Eq. 48).

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression.

The full record is consistent; retain DRAFT.

Read every field of AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, three primary sources with exact SHA-256 digests, two pinned AIO mappings and rationales, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261018T195000Z-affine-invariant-heavy-tailed-covariance-estimation.json | supports | No normalized identity match for affine-invariant calibrated covariance estimation and heavy-tailed ridge regression across 442 pinned AIO records and 617 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected RidgeRegression and LinearRegression in the pinned AIO snapshot (2026-07-22). Provide accurate related_match context. |
| calculation | research/discovery/affine-invariant-heavy-tailed-covariance-estimation-boundaries.py | supports | Executed pure-Python verification in research/discovery/affine-invariant-heavy-tailed-covariance-estimation-boundaries.py (SHA-256 03b4668927afa69c9a210edc2bde246dc70e21657c042c4779bc5149d60f9416): verified (1) Lemma 14 dyadic effective-dimension doubling df_{lambda/2}(S) &lt;= 2 df_lambda(S) (max ratio 1.4874 &lt;= 2.0) and Lemma 6 similarity eigenvalue bounds [0.6757, 1.9231] subset [2/3, 2] and trace surrogate control (ratio 0.4756 &lt;= 3.0); (2) Algorithm 1 multi-stage dyadic regularization halving vs. uncalibrated Wei-Minsker clipping on a heavy-tailed Student-t_5 covariance with spectrum {100, 10, 0.1, 0.01} at lambda = 0.01 (calibrated error 0.1238 vs. 1.2996, and Lepskii Algorithm 2 adaptive selection error 0.1577); and (3) Theorem 13 / Appendix D ridge regression excess-risk decomposition. |
| ostrovskii2019-affine-invariant-cov-pdf | https://proceedings.mlr.press/v99/ostrovskii19a/ostrovskii19a.pdf; Pages 1-20, Sections 1-6 and Appendices A-D (Algorithms 1-2, Lemmas 5, 6, 14, Theorems 7, 10, 13, Corollaries 8, 11, 12) | supports | All 20 pages of the full-text PDF of Ostrovskii &amp; Rudi (2019, COLT PMLR 99:2531-2550) read. Checked all definitions, algorithms, lemmas, theorems, corollaries, and proofs. |
| ostrovskii2019-affine-invariant-cov-abs | https://arxiv.org/abs/1902.03086; arXiv:1902.03086v2 abstract | supports | arXiv abstract and submission metadata read and verified. |
| ostrovskii2019-affine-invariant-cov-pmlr | https://proceedings.mlr.press/v99/ostrovskii19a.html; PMLR v99:2531-2550 record | supports | PMLR metadata record read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT affine-invariant calibrated covariance estimation and heavy-tailed ridge regression record, yielding 618 native and 442 unchanged generated records.
- All 20 PDF pages of Ostrovskii &amp; Rudi (2019) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261018T195100Z-affine-invariant-heavy-tailed-covariance-estimation
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of affine-invariant calibrated covariance estimation
  and heavy-tailed ridge regression
started_at: '2026-10-18T19:50:00Z'
finished_at: '2026-10-18T19:51:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from CatoniInfluenceFunctionTailRobustMeanAndGramMatrixEstimation,
    SubGaussianTournamentAndMedianOfMeansEmpiricalRiskMinimization, and SelfConcordantAndPseudoSelfConcordantFiniteSampleMEstimation,
    verified Lemma 14 dyadic effective-dimension doubling, Lemma 6 similarity and
    trace bounds, Algorithm 1 dyadic regularization halving vs. uncalibrated Wei-Minsker
    clipping, Algorithm 2 Lepskii selection, and Theorem 13 ridge regression bounds,
    and documented five typographical/notational notes in Ostrovskii & Rudi (2019,
    COLT PMLR 99:2531-2550, pp. 1-3, 5, 10-12, 16, 19). This is adversarial author
    self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Affine-Invariant Calibrated Covariance Estimation and Heavy-Tailed
  Ridge Regression as a distinct DRAFT mathematical_method with related RidgeRegression
  and LinearRegression mappings. All four claims and locators across Ostrovskii &
  Rudi (2019, COLT PMLR 99:2531-2550, arXiv:1902.03086v2) are supported with explicit
  sample-splitting logarithmic overhead, fourth-moment kurtosis, and ambient-dimension
  concentration limitations.
source:
  git_revision: 5a5b356763bccaa1084722987b0f2610d7e3f1d9
  state: working_tree
  inputs:
  - path: data/aio/LinearRegression.yaml
    sha256: 9b6f1b2ea06d9a47e5f7cf94c66afeaa6d40c3e7d0fdb5037d2c25fabc6d8167
    role: context
  - path: data/aio/RidgeRegression.yaml
    sha256: 7ee3be4552041e1ee2194a78eb0cbefe25283907027a6680395973dbf98636bb
    role: context
  - path: data/curated/AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression.yaml
    sha256: d556ea353e24718124a93f090878e7f8216e93b4afbdae3081a1b97c17b275b8
    role: target
  - path: data/curated/SelfConcordantAndPseudoSelfConcordantFiniteSampleMEstimation.yaml
    sha256: c761874a688223c4e3b5febdfd064a1b9369889dfeb89edcaab4944bf0328802
    role: context
  - path: research/discovery/20261018T195000Z-affine-invariant-heavy-tailed-covariance-estimation.json
    sha256: 4e9d24c1881800625ca68c78d325d4c71df428966daa94e11bac48aeb639aaa8
    role: context
  - path: research/discovery/affine-invariant-heavy-tailed-covariance-estimation-boundaries.py
    sha256: 03b4668927afa69c9a210edc2bde246dc70e21657c042c4779bc5149d60f9416
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
- target_id: AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
  path: data/curated/AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression.yaml
  label: Affine-Invariant Calibrated Covariance Estimation and Heavy-Tailed Ridge
    Regression
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression.yaml
    role: maintained
scope:
  description: All fields of the exact maintained AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
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
  - AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO concept records are valid.
- check_id: maintain-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
  exit_code: 0
  expected_exit_code: 0
  summary: All 618 curated concept records are valid.
- check_id: maintain-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO records match the pinned source.
- check_id: maintain-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
  exit_code: 0
  expected_exit_code: 0
  summary: All history sidecars are valid.
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW files are in sync.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed Ostrovskii & Rudi 2019 dyadic regularization halving, Lepskii
    selection, and heavy-tailed ridge regression checks
  command: python3 research/discovery/affine-invariant-heavy-tailed-covariance-estimation-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"concept_id\": \"AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression\"\
    ,\n  \"all_passed\": true,\n  \"check_1_lemmas_14_and_6\": {\n    \"passed\":\
    \ true,\n    \"max_df_halving_ratio\": 1.487357,\n    \"similarity_eigenvalue_range\"\
    : [\n      0.675676,\n      1.923077\n    ],\n    \"theoretical_similarity_bounds\"\
    : [\n      0.666667,\n      2.0\n    ],\n    \"max_trace_surrogate_diff_ratio\"\
    : 0.475552\n  },\n  \"check_2_algorithm1_and_lepskii\": {\n    \"passed\": true,\n\
    \    \"calibrated_error_alg1\": 0.1238,\n    \"calibrated_error_wei_minsker_uncalibrated\"\
    : 1.299639,\n    \"max_relative_diagonal_error_alg1\": 0.092035,\n    \"lepskii_selected_theta\"\
    : 4.0,\n    \"calibrated_error_lepskii\": 0.157731\n  },\n  \"check_3_theorem13_ridge_decomposition\"\
    : {\n    \"passed\": true,\n    \"E3_fixed_design_bias\": 0.454459,\n    \"Eq47_bias_upper_bound\"\
    : 0.753434,\n    \"E2_covariance_estimation_term\": 0.444905,\n    \"Eq48_upper_bound\"\
    : 0.467981\n  }\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261018T195000Z-affine-invariant-heavy-tailed-covariance-estimation.json
  accessed_at: '2026-10-18T19:50:00Z'
  support: supports
  summary: No normalized identity match for affine-invariant calibrated covariance
    estimation and heavy-tailed ridge regression across 442 pinned AIO records and
    617 maintained IDs, names, aliases and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-18T19:50:00Z'
  support: supports
  summary: Inspected RidgeRegression and LinearRegression in the pinned AIO snapshot
    (2026-07-22). Provide accurate related_match context.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/affine-invariant-heavy-tailed-covariance-estimation-boundaries.py
  accessed_at: '2026-10-18T19:50:00Z'
  snapshot_sha256: 03b4668927afa69c9a210edc2bde246dc70e21657c042c4779bc5149d60f9416
  support: supports
  summary: 'Executed pure-Python verification in research/discovery/affine-invariant-heavy-tailed-covariance-estimation-boundaries.py
    (SHA-256 03b4668927afa69c9a210edc2bde246dc70e21657c042c4779bc5149d60f9416): verified
    (1) Lemma 14 dyadic effective-dimension doubling df_{lambda/2}(S) <= 2 df_lambda(S)
    (max ratio 1.4874 <= 2.0) and Lemma 6 similarity eigenvalue bounds [0.6757, 1.9231]
    subset [2/3, 2] and trace surrogate control (ratio 0.4756 <= 3.0); (2) Algorithm
    1 multi-stage dyadic regularization halving vs. uncalibrated Wei-Minsker clipping
    on a heavy-tailed Student-t_5 covariance with spectrum {100, 10, 0.1, 0.01} at
    lambda = 0.01 (calibrated error 0.1238 vs. 1.2996, and Lepskii Algorithm 2 adaptive
    selection error 0.1577); and (3) Theorem 13 / Appendix D ridge regression excess-risk
    decomposition.'
- evidence_id: ostrovskii2019-affine-invariant-cov-pdf
  kind: primary_source
  reference: https://proceedings.mlr.press/v99/ostrovskii19a/ostrovskii19a.pdf
  locator: Pages 1-20, Sections 1-6 and Appendices A-D (Algorithms 1-2, Lemmas 5,
    6, 14, Theorems 7, 10, 13, Corollaries 8, 11, 12)
  accessed_at: '2026-10-18T12:51:00Z'
  snapshot_sha256: 65feb9f97b0b40a86339c6a59207072dcfa5debb4a0ab3ce41446a5600fa0e46
  support: supports
  summary: All 20 pages of the full-text PDF of Ostrovskii & Rudi (2019, COLT PMLR
    99:2531-2550) read. Checked all definitions, algorithms, lemmas, theorems, corollaries,
    and proofs.
- evidence_id: ostrovskii2019-affine-invariant-cov-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1902.03086
  locator: arXiv:1902.03086v2 abstract
  accessed_at: '2026-10-18T12:56:00Z'
  snapshot_sha256: 6a55c4b48442cddb485274a6cdba50c3bbe5a5dc029164f6b14a90cb50036f4f
  support: supports
  summary: arXiv abstract and submission metadata read and verified.
- evidence_id: ostrovskii2019-affine-invariant-cov-pmlr
  kind: primary_source
  reference: https://proceedings.mlr.press/v99/ostrovskii19a.html
  locator: PMLR v99:2531-2550 record
  accessed_at: '2026-10-18T12:51:00Z'
  snapshot_sha256: b1a61c2001fe6e95b4d36f18a3ba793f6ed1a457fdb5a3cd09c2e5f73cab2c57
  support: supports
  summary: PMLR metadata record read and verified.
assessments:
- assessment_id: identity-boundary
  area: identity
  topic: Distinctness of affine-invariant calibrated covariance estimation and heavy-tailed
    ridge regression
  outcome: supported
  target_ids:
  - AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
  evidence_ids:
  - identity
  - ostrovskii2019-affine-invariant-cov-pdf
  - ostrovskii2019-affine-invariant-cov-abs
  - ostrovskii2019-affine-invariant-cov-pmlr
  summary: Distinct from Catoni operator-norm Gram matrix estimation, tournament/median-of-means
    ERM, and self-concordant M-estimation.
  details: Confirmed via normalized identity check and full-text reading of Ostrovskii
    & Rudi (2019, COLT PMLR 99:2531-2550).
- assessment_id: aio-mappings
  area: grounding
  topic: AIO mappings for AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
  outcome: supported
  target_ids:
  - AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
  evidence_ids:
  - mapping
  - ostrovskii2019-affine-invariant-cov-pdf
  summary: related_match to AIO:RidgeRegression and AIO:LinearRegression are accurate.
  details: Pinned AIO (2026-07-22) contains RidgeRegression and LinearRegression broadly
    without affine-invariant calibrated heavy-tailed covariance preconditioning.
- assessment_id: definition
  area: evidence
  topic: Definition and scope
  outcome: supported
  target_ids:
  - AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
  evidence_ids:
  - ostrovskii2019-affine-invariant-cov-pdf
  - ostrovskii2019-affine-invariant-cov-abs
  - ostrovskii2019-affine-invariant-cov-pmlr
  summary: Definition accurately captures Condition (HT), calibrated Loewner-order
    covariance bounds, Algorithm 1 dyadic regularization halving, Algorithm 2 Lepskii
    adaptation, and Theorem 13 heavy-tailed ridge regression.
  details: All equations and claims verified against Sections 1-6 and Appendices A-D
    of Ostrovskii & Rudi (2019).
- assessment_id: calibrated-covariance-problem-and-failure-of-uncalibrated-norm-clipping
  area: evidence
  topic: calibrated-covariance-problem-and-failure-of-uncalibrated-norm-clipping
  outcome: supported
  target_ids:
  - AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
  evidence_ids:
  - ostrovskii2019-affine-invariant-cov-pdf
  - calculation
  summary: Supported by Section 1 (Equations 1-5), Section 2.3 (Equations 6-13), and
    boundary script.
  details: Verified failure of uncalibrated Wei-Minsker clipping (calibrated error
    1.2996) vs. calibrated Algorithm 1 (calibrated error 0.1238) when lambda = 0.01
    << ||S|| = 100.
- assessment_id: dyadic-regularization-halving-single-step-and-multistage-calibrated-bounds
  area: evidence
  topic: dyadic-regularization-halving-single-step-and-multistage-calibrated-bounds
  outcome: supported
  target_ids:
  - AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
  evidence_ids:
  - ostrovskii2019-affine-invariant-cov-pdf
  - calculation
  summary: Supported by Sections 3-4 (Algorithm 1, Lemma 6, Theorem 7, Corollary 8),
    Appendices A-B (Lemma 14, Equations 35-38), and boundary script.
  details: Verified Lemma 14 max df halving ratio 1.4874 <= 2.0, Lemma 6 similarity
    eigenvalues [0.6757, 1.9231] subset [2/3, 2], and trace surrogate ratio 0.4756
    <= 3.0.
- assessment_id: lepskii-adaptive-threshold-selection-for-unknown-kurtosis-and-effective-dimension
  area: evidence
  topic: lepskii-adaptive-threshold-selection-for-unknown-kurtosis-and-effective-dimension
  outcome: supported
  target_ids:
  - AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
  evidence_ids:
  - ostrovskii2019-affine-invariant-cov-pdf
  - calculation
  summary: Supported by Section 5 (Algorithm 2, Theorem 10, Corollary 11), Appendix
    C (Equations 39-43), and boundary script.
  details: Verified Lepskii selection rule (Eq. 28) selecting theta_hat = 4.0 with
    calibrated error 0.1577.
- assessment_id: relative-eigenvalue-recovery-and-heavy-tailed-ridge-regression-excess-risk
  area: evidence
  topic: relative-eigenvalue-recovery-and-heavy-tailed-ridge-regression-excess-risk
  outcome: supported
  target_ids:
  - AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
  evidence_ids:
  - ostrovskii2019-affine-invariant-cov-pdf
  - calculation
  summary: Supported by Section 6 (Corollary 12, Theorem 13, Equations 31-34), Appendix
    D (Equations 44-50), and boundary script.
  details: Verified Appendix D excess-risk decomposition E3 = 0.4545 <= 0.7534 (Eq.
    47) and E2 = 0.4449 <= 0.4680 (Eq. 48).
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression
  evidence_ids:
  - identity
  - mapping
  - ostrovskii2019-affine-invariant-cov-pdf
  - ostrovskii2019-affine-invariant-cov-abs
  - ostrovskii2019-affine-invariant-cov-pmlr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of AffineInvariantCalibratedCovarianceEstimationAndHeavyTailedRidgeRegression.yaml:
    stable ID, name, aliases, mathematical_method kind, definition, definition_evidence,
    identity_notes, four claims and locators, three primary sources with exact SHA-256
    digests, two pinned AIO mappings and rationales, four scoped limitations, and
    UTC curation metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT affine-invariant calibrated covariance estimation and heavy-tailed
  ridge regression record, yielding 618 native and 442 unchanged generated records.
- All 20 PDF pages of Ostrovskii & Rudi (2019) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- covariance-estimation
- heavy-tailed-statistics
- ridge-regression
- self-review
- discovery-ongoing
```
