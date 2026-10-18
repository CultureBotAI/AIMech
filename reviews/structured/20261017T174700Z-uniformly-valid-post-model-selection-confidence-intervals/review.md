# Scientific author self-review of Uniformly valid post-model-selection confidence intervals via consistent variance overestimation

- Review: 20261017T174700Z-uniformly-valid-post-model-selection-confidence-intervals
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T17:45:00Z
- Finished UTC: 2026-10-17T17:47:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Uniformly valid post-model-selection confidence intervals via consistent variance overestimation as a distinct DRAFT mathematical_method with related LinearRegression, LogisticRegression, and DataDredgingBias mappings. All four claims and locators across Bachoc, Preinerstorfer, &amp; Steinberger (2020, The Annals of Statistics 48(1):440-463, arXiv:1611.01043v4) are supported with explicit fixed-k/p and conservative misspecification overestimation limitations.

## Scope And Provenance

All fields of the exact maintained UniformlyValidPostModelSelectionConfidenceIntervals record and its primary evidence.

Selection: Exact maintained ID: AIMech:UniformlyValidPostModelSelectionConfidenceIntervals
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 29b2e3f4362815f9d7b62b4942929f39be9ad5b0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:UniformlyValidPostModelSelectionConfidenceIntervals | data/curated/UniformlyValidPostModelSelectionConfidenceIntervals.yaml | maintained | Uniformly valid post-model-selection confidence intervals via consistent variance overestimation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:UniformlyValidPostModelSelectionConfidenceIntervals | All 442 AIO concept records are valid. |
| aimech validate-curated | passed | True | AIMech:UniformlyValidPostModelSelectionConfidenceIntervals | All 608 curated concept records are valid. |
| aimech seed --check | passed | True | AIMech:UniformlyValidPostModelSelectionConfidenceIntervals | All 442 AIO records match the pinned source. |
| aimech validate-history | passed | True | AIMech:UniformlyValidPostModelSelectionConfidenceIntervals | All history sidecars are valid. |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:UniformlyValidPostModelSelectionConfidenceIntervals | Vendored CLAW files are in sync. |
| aimech check-source | passed | True | AIMech:UniformlyValidPostModelSelectionConfidenceIntervals | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:UniformlyValidPostModelSelectionConfidenceIntervals | Exited 0 without output. |
| Constructed Bachoc-Preinerstorfer-Steinberger 2020 consistent overestimation, Eicker sandwich, and canonical logistic rank reduction checks | passed | True | AIMech:UniformlyValidPostModelSelectionConfidenceIntervals | {<br>  "concept_id": "AIMech:UniformlyValidPostModelSelectionConfidenceIntervals",<br>  "regime_1_proposition_2_7_overestimation": {<br>    "mean_variance_ratio_well_specified": 0.99856,<br>    "mean_variance_ratio_misspecified": 1.64697,<br>    "theoretical_misspecified_limit_1_plus_dn": 1.64,<br>    "proposition_2_7_verified": true<br>  },<br>  "regime_2_homoskedastic_adaptation_and_impossibility": {<br>    "prop_3_4_misspecified_var_ratio": 3.272727,<br>    "prop_3_4_correct_var_ratio": 1.0,<br>    "thm_3_3_k_individual_xi": 1.959964,<br>    "thm_3_2_k_simultaneous_gamma": 2.236477,<br>    "prop_3_5_unconditional_var": 1.02,<br>    "prop_3_5_conditional_var": 1.0,<br>    "homoskedastic_regime_verified": true<br>  },<br>  "regime_3_heteroskedastic_eicker_and_lemma_2_9": {<br>    "q_naive": 1.644854,<br>    "b_alpha_min_k_p_k": 2.397949,<br>    "b_alpha_k_k": 2.63407,<br>    "significance_hunting_naive_coverage": 0.8275,<br>    "significance_hunting_posi_hlm_coverage": 0.9762,<br>    "heteroskedastic_eicker_verified": true<br>  },<br>  "regime_4_binary_regression_and_canonical_link": {<br>    "canonical_link_max_score_diff_error": 2.220446049250313e-16,<br>    "canonical_link_max_second_derivative": -0.045177,<br>    "b_alpha_canonical_logistic_p3_k12": 2.397949,<br>    "b_alpha_general_link_k12_k12": 2.63407,<br>    "binary_regression_canonical_reduction_verified": true<br>  },<br>  "all_passed": true<br>} |

## Scientific And Domain Assessments

### UniformlyValidPostModelSelectionConfidenceIntervals versus ValidPostSelectionInferencePoSIConstant, RestrictedIsometryPostSelectionInferenceConstantBounds, and PostModelSelectionPredictorPoSIConfidenceIntervals

identity: supported. Targets: AIMech:UniformlyValidPostModelSelectionConfidenceIntervals.

Retain Uniformly valid post-model-selection confidence intervals via consistent variance overestimation as a distinct DRAFT mathematical_method.

Bachoc, Preinerstorfer, &amp; Steinberger (2020) establish a general triangular-array asymptotic linearity framework (Condition 1, Lemma 2.2), prove impossibility of uniformly consistent variance estimation under unbounded misspecification (Proposition 3.5), introduce consistent variance overestimation (Theorem 2.6, Proposition 2.7), and derive uniformly valid post-selection confidence intervals for homoskedastic and heteroskedastic linear regression and misspecified binary regression.

### Mappings to AIO:LinearRegression, AIO:LogisticRegression, and AIO:DataDredgingBias

grounding: supported. Targets: AIMech:UniformlyValidPostModelSelectionConfidenceIntervals.

Related mappings to LinearRegression, LogisticRegression, and DataDredgingBias are supported.

Uniform post-selection intervals cover misspecified linear regression (AIO:LinearRegression) and binary/logistic regression (AIO:LogisticRegression) while preventing data-snooping invalidation (AIO:DataDredgingBias).

### asymptotic-linearity-clt-and-consistent-variance-overestimation

evidence: supported. Targets: AIMech:UniformlyValidPostModelSelectionConfidenceIntervals.

Supported by Section 2 (Condition 1, Lemma 2.2, Theorem 2.6, Proposition 2.7, Remark 2.8, Lemma 2.9) and Appendix B.

Verified consistent variance overestimation ratio 1 + d_n under misspecification and 1.0 under well-specification.

### homoskedastic-linear-model-adaptation-and-uniform-impossibility

evidence: supported. Targets: AIMech:UniformlyValidPostModelSelectionConfidenceIntervals.

Supported by Section 3.1 (Theorems 3.2-3.3, Propositions 3.4-3.5) and Appendix C.1-C.4.

Verified Proposition 3.4 variance adaptation, Theorem 3.3 vs. Theorem 3.2 constants, and Proposition 3.5 impossibility mixture.

### heteroskedastic-eicker-sandwich-post-selection-confidence-intervals

evidence: supported. Targets: AIMech:UniformlyValidPostModelSelectionConfidenceIntervals.

Supported by Section 3.2 (Theorem 3.6) and Appendix C.5.

Verified Eicker sandwich PoSI coverage &gt;= 1 - alpha under adversarial significance hunting.

### misspecified-binary-regression-fahrmeir-sandwich-and-canonical-link-reduction

evidence: supported. Targets: AIMech:UniformlyValidPostModelSelectionConfidenceIntervals.

Supported by Section 3.3 (Lemmas 3.9-3.10, Theorem 3.11, Remark 3.12) and Appendix D (Corollary D.3).

Verified canonical logistic link identity phi_dot_1 - phi_dot_2 === 1 and rank reduction from B_alpha(min(k, n), k) to B_alpha(min(k, p), k).

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:UniformlyValidPostModelSelectionConfidenceIntervals.

The full record is consistent; retain DRAFT.

Read every field of UniformlyValidPostModelSelectionConfidenceIntervals.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, three primary sources with exact SHA-256 digests, pinned AIO mappings and rationales, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T174500Z-uniformly-valid-post-model-selection-confidence-intervals.json | supports | No normalized identity match for Uniformly valid post-model-selection confidence intervals via consistent variance overestimation across 442 pinned AIO records and 607 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected LinearRegression, LogisticRegression, and DataDredgingBias in the pinned AIO snapshot (2026-07-22). All provide accurate related_match context. |
| calculation | research/discovery/uniformly-valid-post-model-selection-confidence-intervals-boundaries.py | supports | Executed pure-Python verification in research/discovery/uniformly-valid-post-model-selection-confidence-intervals-boundaries.py (SHA-256 307ff0b28db7da96de413c1416b01833009e528d28931d300fb6ff7198688486): (1) Regime 1 (Proposition 2.7 consistent overestimation): verified well-specified mean variance ratio 0.99856 ~= 1.0 and misspecified ratio 1.64697 ~= 1 + d_n = 1.64. (2) Regime 2 (Homoskedastic adaptation &amp; impossibility): verified Proposition 3.4 misspecified ratio 3.272727 vs. well-specified ratio 1.0, Theorem 3.3 K(corr(Xi_n)) = 1.959964 &lt; Theorem 3.2 K(corr(Gamma_n)) = 2.236477, and Proposition 3.5 impossibility mixture unconditional variance 1.02 vs. conditional 1.0. (3) Regime 3 (Heteroskedastic Eicker &amp; Lemma 2.9): verified q_naive = 1.644854 &lt; B_alpha(min(k, p), k) = 2.397949 &lt; B_alpha(k, k) = 2.63407, and under significance hunting naive coverage collapses to 0.8275 while CI^hlm achieves 0.9762. (4) Regime 4 (Binary regression &amp; canonical link): verified canonical logistic identity phi_dot_1 - phi_dot_2 === 1 to machine precision (2.220446049250313e-16), negative definiteness of the log-likelihood Hessian (-0.045177 &lt; 0), and rank reduction from B_alpha(12, 12) = 2.63407 to B_alpha(3, 12) = 2.397949. |
| bps2020-pdf | https://arxiv.org/pdf/1611.01043; Pages 1-70, Sections 1-4 and Appendices A-D (Condition 1, Lemma 2.2, Theorem 2.4, Proposition 2.5, Theorem 2.6, Proposition 2.7, Remark 2.8, Lemma 2.9, Theorems 3.2-3.3, Propositions 3.4-3.5, Theorem 3.6, Lemmas 3.9-3.10, Theorem 3.11, Remark 3.12, Lemmas B.1-B.4, Corollary D.3) | supports | All 70 pages of the full-text PDF of arXiv:1611.01043v4 read. Checked all conditions, lemmas, propositions, theorems, remarks, and proofs. |
| bps2020-crossref | https://api.crossref.org/works/10.1214/19-AOS1815; The Annals of Statistics 48(1):440-463 publication record | supports | Official The Annals of Statistics 48(1):440-463 Crossref record read and verified. |
| bps2020-abs | https://arxiv.org/abs/1611.01043; arXiv:1611.01043v4 abstract and metadata | supports | arXiv:1611.01043v4 abstract and metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Uniformly valid post-model-selection confidence intervals via consistent variance overestimation record, yielding 608 native and 442 unchanged generated records.
- All 70 PDF pages of arXiv:1611.01043v4 were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T174700Z-uniformly-valid-post-model-selection-confidence-intervals
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Uniformly valid post-model-selection confidence
  intervals via consistent variance overestimation
started_at: '2026-10-17T17:45:00Z'
finished_at: '2026-10-17T17:47:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from ValidPostSelectionInferencePoSIConstant
    (Berk et al. 2013), RestrictedIsometryPostSelectionInferenceConstantBounds (Bachoc,
    Blanchard, & Neuvial 2018), and PostModelSelectionPredictorPoSIConfidenceIntervals
    (Bachoc, Leeb, & Pötscher 2019), verified Proposition 2.7 consistent variance
    overestimation, Proposition 3.4/3.5 homoskedastic adaptation and impossibility,
    Theorem 3.6 heteroskedastic Eicker sandwich PoSI coverage, and Remark 3.12 / Corollary
    D.3 canonical logistic rank reduction, and documented four typographical notes
    in arXiv:1611.01043v4 (pp. 4, 28, 29-30, 61). This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Uniformly valid post-model-selection confidence intervals via consistent
  variance overestimation as a distinct DRAFT mathematical_method with related LinearRegression,
  LogisticRegression, and DataDredgingBias mappings. All four claims and locators
  across Bachoc, Preinerstorfer, & Steinberger (2020, The Annals of Statistics 48(1):440-463,
  arXiv:1611.01043v4) are supported with explicit fixed-k/p and conservative misspecification
  overestimation limitations.
source:
  git_revision: 29b2e3f4362815f9d7b62b4942929f39be9ad5b0
  state: working_tree
  inputs:
  - path: data/aio/DataDredgingBias.yaml
    sha256: 335067e88f1462e141ac5f35e697cd42f7d250ec4dde9250531babe0d96cc1d0
    role: context
  - path: data/aio/LinearRegression.yaml
    sha256: 9b6f1b2ea06d9a47e5f7cf94c66afeaa6d40c3e7d0fdb5037d2c25fabc6d8167
    role: context
  - path: data/aio/LogisticRegression.yaml
    sha256: 67dd6e8ae1bb6bfc48598b41adccbf7d48d925db8b0ee3a71f59569913b8c968
    role: context
  - path: data/curated/PostModelSelectionPredictorPoSIConfidenceIntervals.yaml
    sha256: 69249cfe00828610a5f294e4d091b12b54c6c77ac55a139f699d4d59aa625b9a
    role: context
  - path: data/curated/RestrictedIsometryPostSelectionInferenceConstantBounds.yaml
    sha256: 317e5e5fb341d3f207d90f7a9571f612a4f6115ce5c057a6ade1055f931f4b73
    role: context
  - path: data/curated/UniformlyValidPostModelSelectionConfidenceIntervals.yaml
    sha256: 939ac08492a6cc3c1f0bce260f79c2a08e93deb4ec571bc2ab0eb1c2f6821dad
    role: target
  - path: research/discovery/20261017T174500Z-uniformly-valid-post-model-selection-confidence-intervals.json
    sha256: cbd31ce6e59efaa246a99d97cf6af0827d35a12797c0240db8ca2c2e3baec570
    role: context
  - path: research/discovery/uniformly-valid-post-model-selection-confidence-intervals-boundaries.py
    sha256: 307ff0b28db7da96de413c1416b01833009e528d28931d300fb6ff7198688486
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
- target_id: AIMech:UniformlyValidPostModelSelectionConfidenceIntervals
  path: data/curated/UniformlyValidPostModelSelectionConfidenceIntervals.yaml
  label: Uniformly valid post-model-selection confidence intervals via consistent
    variance overestimation
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/UniformlyValidPostModelSelectionConfidenceIntervals.yaml
    role: maintained
scope:
  description: All fields of the exact maintained UniformlyValidPostModelSelectionConfidenceIntervals
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:UniformlyValidPostModelSelectionConfidenceIntervals'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:UniformlyValidPostModelSelectionConfidenceIntervals
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
  - AIMech:UniformlyValidPostModelSelectionConfidenceIntervals
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO concept records are valid.
- check_id: maintain-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:UniformlyValidPostModelSelectionConfidenceIntervals
  exit_code: 0
  expected_exit_code: 0
  summary: All 608 curated concept records are valid.
- check_id: maintain-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:UniformlyValidPostModelSelectionConfidenceIntervals
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO records match the pinned source.
- check_id: maintain-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:UniformlyValidPostModelSelectionConfidenceIntervals
  exit_code: 0
  expected_exit_code: 0
  summary: All history sidecars are valid.
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:UniformlyValidPostModelSelectionConfidenceIntervals
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW files are in sync.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:UniformlyValidPostModelSelectionConfidenceIntervals
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:UniformlyValidPostModelSelectionConfidenceIntervals
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed Bachoc-Preinerstorfer-Steinberger 2020 consistent overestimation,
    Eicker sandwich, and canonical logistic rank reduction checks
  command: python3 research/discovery/uniformly-valid-post-model-selection-confidence-intervals-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:UniformlyValidPostModelSelectionConfidenceIntervals
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"concept_id\": \"AIMech:UniformlyValidPostModelSelectionConfidenceIntervals\"\
    ,\n  \"regime_1_proposition_2_7_overestimation\": {\n    \"mean_variance_ratio_well_specified\"\
    : 0.99856,\n    \"mean_variance_ratio_misspecified\": 1.64697,\n    \"theoretical_misspecified_limit_1_plus_dn\"\
    : 1.64,\n    \"proposition_2_7_verified\": true\n  },\n  \"regime_2_homoskedastic_adaptation_and_impossibility\"\
    : {\n    \"prop_3_4_misspecified_var_ratio\": 3.272727,\n    \"prop_3_4_correct_var_ratio\"\
    : 1.0,\n    \"thm_3_3_k_individual_xi\": 1.959964,\n    \"thm_3_2_k_simultaneous_gamma\"\
    : 2.236477,\n    \"prop_3_5_unconditional_var\": 1.02,\n    \"prop_3_5_conditional_var\"\
    : 1.0,\n    \"homoskedastic_regime_verified\": true\n  },\n  \"regime_3_heteroskedastic_eicker_and_lemma_2_9\"\
    : {\n    \"q_naive\": 1.644854,\n    \"b_alpha_min_k_p_k\": 2.397949,\n    \"\
    b_alpha_k_k\": 2.63407,\n    \"significance_hunting_naive_coverage\": 0.8275,\n\
    \    \"significance_hunting_posi_hlm_coverage\": 0.9762,\n    \"heteroskedastic_eicker_verified\"\
    : true\n  },\n  \"regime_4_binary_regression_and_canonical_link\": {\n    \"canonical_link_max_score_diff_error\"\
    : 2.220446049250313e-16,\n    \"canonical_link_max_second_derivative\": -0.045177,\n\
    \    \"b_alpha_canonical_logistic_p3_k12\": 2.397949,\n    \"b_alpha_general_link_k12_k12\"\
    : 2.63407,\n    \"binary_regression_canonical_reduction_verified\": true\n  },\n\
    \  \"all_passed\": true\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T174500Z-uniformly-valid-post-model-selection-confidence-intervals.json
  accessed_at: '2026-10-17T17:45:00Z'
  support: supports
  summary: No normalized identity match for Uniformly valid post-model-selection confidence
    intervals via consistent variance overestimation across 442 pinned AIO records
    and 607 maintained IDs, names, aliases and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T17:45:00Z'
  support: supports
  summary: Inspected LinearRegression, LogisticRegression, and DataDredgingBias in
    the pinned AIO snapshot (2026-07-22). All provide accurate related_match context.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/uniformly-valid-post-model-selection-confidence-intervals-boundaries.py
  accessed_at: '2026-10-17T17:45:00Z'
  snapshot_sha256: 307ff0b28db7da96de413c1416b01833009e528d28931d300fb6ff7198688486
  support: supports
  summary: 'Executed pure-Python verification in research/discovery/uniformly-valid-post-model-selection-confidence-intervals-boundaries.py
    (SHA-256 307ff0b28db7da96de413c1416b01833009e528d28931d300fb6ff7198688486): (1)
    Regime 1 (Proposition 2.7 consistent overestimation): verified well-specified
    mean variance ratio 0.99856 ~= 1.0 and misspecified ratio 1.64697 ~= 1 + d_n =
    1.64. (2) Regime 2 (Homoskedastic adaptation & impossibility): verified Proposition
    3.4 misspecified ratio 3.272727 vs. well-specified ratio 1.0, Theorem 3.3 K(corr(Xi_n))
    = 1.959964 < Theorem 3.2 K(corr(Gamma_n)) = 2.236477, and Proposition 3.5 impossibility
    mixture unconditional variance 1.02 vs. conditional 1.0. (3) Regime 3 (Heteroskedastic
    Eicker & Lemma 2.9): verified q_naive = 1.644854 < B_alpha(min(k, p), k) = 2.397949
    < B_alpha(k, k) = 2.63407, and under significance hunting naive coverage collapses
    to 0.8275 while CI^hlm achieves 0.9762. (4) Regime 4 (Binary regression & canonical
    link): verified canonical logistic identity phi_dot_1 - phi_dot_2 === 1 to machine
    precision (2.220446049250313e-16), negative definiteness of the log-likelihood
    Hessian (-0.045177 < 0), and rank reduction from B_alpha(12, 12) = 2.63407 to
    B_alpha(3, 12) = 2.397949.'
- evidence_id: bps2020-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/1611.01043
  locator: Pages 1-70, Sections 1-4 and Appendices A-D (Condition 1, Lemma 2.2, Theorem
    2.4, Proposition 2.5, Theorem 2.6, Proposition 2.7, Remark 2.8, Lemma 2.9, Theorems
    3.2-3.3, Propositions 3.4-3.5, Theorem 3.6, Lemmas 3.9-3.10, Theorem 3.11, Remark
    3.12, Lemmas B.1-B.4, Corollary D.3)
  accessed_at: '2026-10-17T17:45:00Z'
  snapshot_sha256: 8cfe880631d099338a706a63a8ca5e194d4c0dd0f6aa71fb6c8b4f75a741974f
  support: supports
  summary: All 70 pages of the full-text PDF of arXiv:1611.01043v4 read. Checked all
    conditions, lemmas, propositions, theorems, remarks, and proofs.
- evidence_id: bps2020-crossref
  kind: primary_source
  reference: https://api.crossref.org/works/10.1214/19-AOS1815
  locator: The Annals of Statistics 48(1):440-463 publication record
  accessed_at: '2026-10-17T17:45:00Z'
  snapshot_sha256: 811c958acffdc11ae9fac8c19ee8ea237a1cdefb961040eccf80dfc3a86a782c
  support: supports
  summary: Official The Annals of Statistics 48(1):440-463 Crossref record read and
    verified.
- evidence_id: bps2020-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1611.01043
  locator: arXiv:1611.01043v4 abstract and metadata
  accessed_at: '2026-10-17T17:45:00Z'
  snapshot_sha256: 60d4499beb32921901fec796f2f9976c21ef87de64d9e103697ab499c3269004
  support: supports
  summary: arXiv:1611.01043v4 abstract and metadata read and verified.
assessments:
- assessment_id: identity
  area: identity
  topic: UniformlyValidPostModelSelectionConfidenceIntervals versus ValidPostSelectionInferencePoSIConstant,
    RestrictedIsometryPostSelectionInferenceConstantBounds, and PostModelSelectionPredictorPoSIConfidenceIntervals
  outcome: supported
  target_ids:
  - AIMech:UniformlyValidPostModelSelectionConfidenceIntervals
  evidence_ids:
  - identity
  - bps2020-pdf
  - bps2020-crossref
  summary: Retain Uniformly valid post-model-selection confidence intervals via consistent
    variance overestimation as a distinct DRAFT mathematical_method.
  details: Bachoc, Preinerstorfer, & Steinberger (2020) establish a general triangular-array
    asymptotic linearity framework (Condition 1, Lemma 2.2), prove impossibility of
    uniformly consistent variance estimation under unbounded misspecification (Proposition
    3.5), introduce consistent variance overestimation (Theorem 2.6, Proposition 2.7),
    and derive uniformly valid post-selection confidence intervals for homoskedastic
    and heteroskedastic linear regression and misspecified binary regression.
- assessment_id: mapping
  area: grounding
  topic: Mappings to AIO:LinearRegression, AIO:LogisticRegression, and AIO:DataDredgingBias
  outcome: supported
  target_ids:
  - AIMech:UniformlyValidPostModelSelectionConfidenceIntervals
  evidence_ids:
  - mapping
  - bps2020-pdf
  summary: Related mappings to LinearRegression, LogisticRegression, and DataDredgingBias
    are supported.
  details: Uniform post-selection intervals cover misspecified linear regression (AIO:LinearRegression)
    and binary/logistic regression (AIO:LogisticRegression) while preventing data-snooping
    invalidation (AIO:DataDredgingBias).
- assessment_id: asymptotic-linearity-clt-and-consistent-variance-overestimation
  area: evidence
  topic: asymptotic-linearity-clt-and-consistent-variance-overestimation
  outcome: supported
  target_ids:
  - AIMech:UniformlyValidPostModelSelectionConfidenceIntervals
  evidence_ids:
  - bps2020-pdf
  - bps2020-crossref
  - calculation
  summary: Supported by Section 2 (Condition 1, Lemma 2.2, Theorem 2.6, Proposition
    2.7, Remark 2.8, Lemma 2.9) and Appendix B.
  details: Verified consistent variance overestimation ratio 1 + d_n under misspecification
    and 1.0 under well-specification.
- assessment_id: homoskedastic-linear-model-adaptation-and-uniform-impossibility
  area: evidence
  topic: homoskedastic-linear-model-adaptation-and-uniform-impossibility
  outcome: supported
  target_ids:
  - AIMech:UniformlyValidPostModelSelectionConfidenceIntervals
  evidence_ids:
  - bps2020-pdf
  - bps2020-abs
  - calculation
  summary: Supported by Section 3.1 (Theorems 3.2-3.3, Propositions 3.4-3.5) and Appendix
    C.1-C.4.
  details: Verified Proposition 3.4 variance adaptation, Theorem 3.3 vs. Theorem 3.2
    constants, and Proposition 3.5 impossibility mixture.
- assessment_id: heteroskedastic-eicker-sandwich-post-selection-confidence-intervals
  area: evidence
  topic: heteroskedastic-eicker-sandwich-post-selection-confidence-intervals
  outcome: supported
  target_ids:
  - AIMech:UniformlyValidPostModelSelectionConfidenceIntervals
  evidence_ids:
  - bps2020-pdf
  - calculation
  summary: Supported by Section 3.2 (Theorem 3.6) and Appendix C.5.
  details: Verified Eicker sandwich PoSI coverage >= 1 - alpha under adversarial significance
    hunting.
- assessment_id: misspecified-binary-regression-fahrmeir-sandwich-and-canonical-link-reduction
  area: evidence
  topic: misspecified-binary-regression-fahrmeir-sandwich-and-canonical-link-reduction
  outcome: supported
  target_ids:
  - AIMech:UniformlyValidPostModelSelectionConfidenceIntervals
  evidence_ids:
  - bps2020-pdf
  - bps2020-crossref
  - calculation
  summary: Supported by Section 3.3 (Lemmas 3.9-3.10, Theorem 3.11, Remark 3.12) and
    Appendix D (Corollary D.3).
  details: Verified canonical logistic link identity phi_dot_1 - phi_dot_2 === 1 and
    rank reduction from B_alpha(min(k, n), k) to B_alpha(min(k, p), k).
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:UniformlyValidPostModelSelectionConfidenceIntervals
  evidence_ids:
  - identity
  - mapping
  - bps2020-pdf
  - bps2020-crossref
  - bps2020-abs
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of UniformlyValidPostModelSelectionConfidenceIntervals.yaml:
    stable ID, name, aliases, mathematical_method kind, definition, definition_evidence,
    identity_notes, four claims and locators, three primary sources with exact SHA-256
    digests, pinned AIO mappings and rationales, four scoped limitations, and UTC
    curation metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Uniformly valid post-model-selection confidence intervals via consistent
  variance overestimation record, yielding 608 native and 442 unchanged generated
  records.
- All 70 PDF pages of arXiv:1611.01043v4 were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- post-selection-inference
- model-misspecification
- binary-regression
- self-review
- discovery-ongoing
```
