# Scientific author self-review of Model-robust nonlinearity-consistent sandwich variance and Ratio of Asymptotic Variances (RAV) specification test

- Review: 20261017T175700Z-model-robust-nonlinearity-sandwich-and-rav-test
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T17:55:00Z
- Finished UTC: 2026-10-17T17:57:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Model-robust nonlinearity-consistent sandwich variance and Ratio of Asymptotic Variances (RAV) specification test as a distinct DRAFT mathematical_method with related LinearRegression mapping. All four claims and locators across Buja et al. (2019, Statistical Science 34(4):523-544, arXiv:1404.1578v4) are supported with explicit fourth-moment and RAV=1 cancellation limitations.

## Scope And Provenance

All fields of the exact maintained ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest record and its primary evidence.

Selection: Exact maintained ID: AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 31cad4777c52a0cf671de01dfeec27a408b46b06.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest | data/curated/ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest.yaml | maintained | Model-robust nonlinearity-consistent sandwich variance and Ratio of Asymptotic Variances (RAV) specification test |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest | All 442 AIO concept records are valid. |
| aimech validate-curated | passed | True | AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest | All 609 curated concept records are valid. |
| aimech seed --check | passed | True | AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest | All 442 AIO records match the pinned source. |
| aimech validate-history | passed | True | AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest | All history sidecars are valid. |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest | Vendored CLAW files are in sync. |
| aimech check-source | passed | True | AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest | Exited 0 without output. |
| Constructed Buja et al. 2019 Part I Estimation Offset, M-of-N bootstrap limit, and RAV specification test checks | passed | True | AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest | {<br>  "concept_id": "AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest",<br>  "regime_1_ancillarity_and_decomposition": {<br>    "nonlinear_slope_p1": 0.0,<br>    "nonlinear_slope_p2": 2.0,<br>    "linear_slope_p1": 2.0,<br>    "linear_slope_p2": 2.0,<br>    "max_orthogonality_error": 0.0,<br>    "expected_m2": 0.525,<br>    "proposition_4_1_verified": true<br>  },<br>  "regime_2_estimation_offsets_and_bootstrap_limit": {<br>    "var_noise_eo": 0.003204,<br>    "var_approx_eo": 0.013707,<br>    "var_total_eo": 0.015723,<br>    "cov_noise_approx_eo": -0.000547,<br>    "av_sandwich_b1": 1.029159,<br>    "m_of_n_bootstrap_scaled_var_b1": 1.100014,<br>    "bootstrap_sandwich_rel_error": 0.068848,<br>    "offsets_and_bootstrap_limit_verified": true<br>  },<br>  "regime_3_adjusted_slopes_and_rav_bounds": {<br>    "beta1_matrix": 1.768122,<br>    "beta1_casewise": 1.768122,<br>    "beta1_pairwise": 1.768122,<br>    "rav_protective_sigma2": 0.357143,<br>    "rav_antiprotective_eta2": 2.028571,<br>    "rav_combined_m2": 1.348668,<br>    "rav_lower_bound": 0.142857,<br>    "rav_upper_bound": 2.285714,<br>    "slopes_and_rav_bounds_verified": true<br>  },<br>  "regime_4_rav_specification_test": {<br>    "gaussian_null_asymptotic_variance": 8.0,<br>    "gaussian_null_asymptotic_sd": 2.828427,<br>    "rav_hat_1_misspecified": 3.319706,<br>    "rav_hat_2_well_behaved": 0.804898,<br>    "perm_pval_1": 0.0025,<br>    "perm_pval_2": 0.3775,<br>    "rav_specification_test_verified": true<br>  },<br>  "all_passed": true<br>} |

## Scientific And Domain Assessments

### ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest versus ValidPostSelectionInferencePoSIConstant and UniformlyValidPostModelSelectionConfidenceIntervals

identity: supported. Targets: AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest.

Retain Model-robust nonlinearity-consistent sandwich variance and Ratio of Asymptotic Variances (RAV) specification test as a distinct DRAFT mathematical_method.

Buja et al. (2019, Part I) establish the model-robust theory of linear OLS under nonlinearity and random regressors, proving Proposition 4.1, the Noise/Approximation Estimation Offset decomposition, Proposition 8.2 M-of-N bootstrap limit, Section 10 weighted slope representations, and the RAV_j specification test.

### Mapping to AIO:LinearRegression

grounding: supported. Targets: AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest.

Related mapping to LinearRegression is supported.

Reconstructs linear OLS as a population functional (AIO:LinearRegression) and characterizes how misspecification bias eta(X_vec) induces O_P(N^{-1/2}) Approximation Estimation Offset variance.

### regressor-ancillarity-failure-and-canonical-noise-nonlinearity-decomposition

evidence: supported. Targets: AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest.

Supported by Sections 3-5 (Equations 1-9, Proposition 4.1) and Appendix E.1.

Verified regressor-distribution slope dependence under nonlinearity vs. invariance under linearity.

### estimation-offset-pythagorean-clt-and-pairs-bootstrap-sandwich-limit

evidence: supported. Targets: AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest.

Supported by Sections 5-8 (Equations 10-20, Proposition 7, Propositions 8.1-8.2) and Appendix C.

Verified finite-sample orthogonality of Noise and Approximation EOs and convergence of M * V[beta^*_M] to AV_hat_sand[beta].

### adjusted-regressor-weighted-slopes-and-rav-convex-bounds

evidence: supported. Targets: AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest.

Supported by Sections 9-11 (Equations 21-28, Definition 11.4, Proposition 11.5) and Appendix E.2-E.4.

Verified exact equality of matrix, case-wise, and pairwise OLS slopes and Lemma E.2 convex combination and sharp bounds for RAV.

### regressor-specific-rav-specification-test-and-null-asymptotics

evidence: supported. Targets: AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest.

Supported by Section 12 (Definition 12.1, Proposition 12.2, Section 12.3) and Appendix F.

Verified Gaussian null variance = 8 and permutation test detection of regressor-specific nonlinearity.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest.

The full record is consistent; retain DRAFT.

Read every field of ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, three primary sources with exact SHA-256 digests, pinned AIO mappings and rationales, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T175500Z-model-robust-nonlinearity-sandwich-and-rav-test.json | supports | No normalized identity match for Model-robust nonlinearity-consistent sandwich variance and Ratio of Asymptotic Variances (RAV) specification test across 442 pinned AIO records and 608 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected LinearRegression in the pinned AIO snapshot (2026-07-22). Provides accurate related_match context. |
| calculation | research/discovery/model-robust-nonlinearity-sandwich-and-rav-test-boundaries.py | supports | Executed pure-Python verification in research/discovery/model-robust-nonlinearity-sandwich-and-rav-test-boundaries.py (SHA-256 3fb7db63bdb7f99b0781cc32c64afa1f9b9f0f55060057e25d68d46ffc49da49): (1) Regime 1 (Proposition 4.1 &amp; canonical decomposition): verified nonlinear slope shift from 0.0 under P_{X,1} to 2.0 under P_{X,2} vs. linear invariance 2.0 = 2.0, and exact orthogonality error 0.0. (2) Regime 2 (Estimation Offsets &amp; Proposition 8.2 bootstrap limit): verified Var(Noise EO) = 0.003204, Var(Approx EO) = 0.013707, Var(Total EO) = 0.015723, Cov(Noise, Approx) = -0.000547, and M-of-N bootstrap scaled variance 1.100014 matching plug-in sandwich 1.029159 (rel error 0.068848). (3) Regime 3 (Section 10 weighted slopes &amp; Section 11 RAV bounds): verified exact equality of matrix (1.768122), case-wise (1.768122), and pairwise (1.768122) OLS slopes, and Lemma E.2 convex combination RAV[m^2] = 1.348668 from protective RAV[sigma^2] = 0.357143 &lt; 1 and anti-protective RAV[eta^2] = 2.028571 &gt; 1 within sharp bounds [0.142857, 2.285714]. (4) Regime 4 (Section 12 RAV_hat_j test): verified Proposition 12.2 Gaussian null variance = 8.0 (SD = 2.828427) and permutation test detection of nonlinear X_1 (RAV_hat_1 = 3.319706, p = 0.0025) while linear X_2 is unrejected (RAV_hat_2 = 0.804898, p = 0.3775). |
| buja2019p1-pdf | https://arxiv.org/pdf/1404.1578; Pages 1-43, Sections 1-14 and Appendices A-F (Equations 1-30, Proposition 4.1, Proposition 7, Propositions 8.1-8.2, Proposition 9.1, Definition 11.4, Proposition 11.5, Definition 12.1, Proposition 12.2, Lemma E.2, Proposition E.3) | supports | All 43 pages of the full-text PDF of arXiv:1404.1578v4 read. Checked all definitions, propositions, lemmas, equations, and proofs. |
| buja2019p1-crossref | https://api.crossref.org/works/10.1214/18-STS693; Statistical Science 34(4):523-544 publication record | supports | Official Statistical Science 34(4):523-544 Crossref record read and verified. |
| buja2019p1-abs | https://arxiv.org/abs/1404.1578; arXiv:1404.1578v4 abstract and metadata | supports | arXiv:1404.1578v4 abstract and metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Model-robust nonlinearity-consistent sandwich variance and Ratio of Asymptotic Variances (RAV) specification test record, yielding 609 native and 442 unchanged generated records.
- All 43 PDF pages of arXiv:1404.1578v4 were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T175700Z-model-robust-nonlinearity-sandwich-and-rav-test
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Model-robust nonlinearity-consistent sandwich
  variance and Ratio of Asymptotic Variances (RAV) specification test
started_at: '2026-10-17T17:55:00Z'
finished_at: '2026-10-17T17:57:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from ValidPostSelectionInferencePoSIConstant
    (Berk et al. 2013) and UniformlyValidPostModelSelectionConfidenceIntervals (Bachoc
    et al. 2020), verified Proposition 4.1 regressor-distribution dependence, Estimation
    Offset orthogonality, Proposition 8.2 M-of-N bootstrap limit, Section 10 weighted
    slope representations, and Section 11-12 RAV bounds and specification test, and
    documented four typographical notes in arXiv:1404.1578v4 (pp. 11, 28, 29, 36).
    This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Model-robust nonlinearity-consistent sandwich variance and Ratio of
  Asymptotic Variances (RAV) specification test as a distinct DRAFT mathematical_method
  with related LinearRegression mapping. All four claims and locators across Buja
  et al. (2019, Statistical Science 34(4):523-544, arXiv:1404.1578v4) are supported
  with explicit fourth-moment and RAV=1 cancellation limitations.
source:
  git_revision: 31cad4777c52a0cf671de01dfeec27a408b46b06
  state: working_tree
  inputs:
  - path: data/aio/LinearRegression.yaml
    sha256: 9b6f1b2ea06d9a47e5f7cf94c66afeaa6d40c3e7d0fdb5037d2c25fabc6d8167
    role: context
  - path: data/curated/ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest.yaml
    sha256: c8c5f645da2f3ac808a0e5e84edf89ef3d5a2ba9f1b5df765a2a3a1a5a2c9c67
    role: target
  - path: data/curated/UniformlyValidPostModelSelectionConfidenceIntervals.yaml
    sha256: 939ac08492a6cc3c1f0bce260f79c2a08e93deb4ec571bc2ab0eb1c2f6821dad
    role: context
  - path: research/discovery/20261017T175500Z-model-robust-nonlinearity-sandwich-and-rav-test.json
    sha256: 986a1e9089b48c768fea21fd615cc4ebc9f8c12e91c36c35a822bf261978894e
    role: context
  - path: research/discovery/model-robust-nonlinearity-sandwich-and-rav-test-boundaries.py
    sha256: 3fb7db63bdb7f99b0781cc32c64afa1f9b9f0f55060057e25d68d46ffc49da49
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
- target_id: AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest
  path: data/curated/ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest.yaml
  label: Model-robust nonlinearity-consistent sandwich variance and Ratio of Asymptotic
    Variances (RAV) specification test
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest.yaml
    role: maintained
scope:
  description: All fields of the exact maintained ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest
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
  - AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO concept records are valid.
- check_id: maintain-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest
  exit_code: 0
  expected_exit_code: 0
  summary: All 609 curated concept records are valid.
- check_id: maintain-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO records match the pinned source.
- check_id: maintain-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest
  exit_code: 0
  expected_exit_code: 0
  summary: All history sidecars are valid.
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW files are in sync.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed Buja et al. 2019 Part I Estimation Offset, M-of-N bootstrap limit,
    and RAV specification test checks
  command: python3 research/discovery/model-robust-nonlinearity-sandwich-and-rav-test-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"concept_id\": \"AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest\"\
    ,\n  \"regime_1_ancillarity_and_decomposition\": {\n    \"nonlinear_slope_p1\"\
    : 0.0,\n    \"nonlinear_slope_p2\": 2.0,\n    \"linear_slope_p1\": 2.0,\n    \"\
    linear_slope_p2\": 2.0,\n    \"max_orthogonality_error\": 0.0,\n    \"expected_m2\"\
    : 0.525,\n    \"proposition_4_1_verified\": true\n  },\n  \"regime_2_estimation_offsets_and_bootstrap_limit\"\
    : {\n    \"var_noise_eo\": 0.003204,\n    \"var_approx_eo\": 0.013707,\n    \"\
    var_total_eo\": 0.015723,\n    \"cov_noise_approx_eo\": -0.000547,\n    \"av_sandwich_b1\"\
    : 1.029159,\n    \"m_of_n_bootstrap_scaled_var_b1\": 1.100014,\n    \"bootstrap_sandwich_rel_error\"\
    : 0.068848,\n    \"offsets_and_bootstrap_limit_verified\": true\n  },\n  \"regime_3_adjusted_slopes_and_rav_bounds\"\
    : {\n    \"beta1_matrix\": 1.768122,\n    \"beta1_casewise\": 1.768122,\n    \"\
    beta1_pairwise\": 1.768122,\n    \"rav_protective_sigma2\": 0.357143,\n    \"\
    rav_antiprotective_eta2\": 2.028571,\n    \"rav_combined_m2\": 1.348668,\n   \
    \ \"rav_lower_bound\": 0.142857,\n    \"rav_upper_bound\": 2.285714,\n    \"slopes_and_rav_bounds_verified\"\
    : true\n  },\n  \"regime_4_rav_specification_test\": {\n    \"gaussian_null_asymptotic_variance\"\
    : 8.0,\n    \"gaussian_null_asymptotic_sd\": 2.828427,\n    \"rav_hat_1_misspecified\"\
    : 3.319706,\n    \"rav_hat_2_well_behaved\": 0.804898,\n    \"perm_pval_1\": 0.0025,\n\
    \    \"perm_pval_2\": 0.3775,\n    \"rav_specification_test_verified\": true\n\
    \  },\n  \"all_passed\": true\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T175500Z-model-robust-nonlinearity-sandwich-and-rav-test.json
  accessed_at: '2026-10-17T17:55:00Z'
  support: supports
  summary: No normalized identity match for Model-robust nonlinearity-consistent sandwich
    variance and Ratio of Asymptotic Variances (RAV) specification test across 442
    pinned AIO records and 608 maintained IDs, names, aliases and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T17:55:00Z'
  support: supports
  summary: Inspected LinearRegression in the pinned AIO snapshot (2026-07-22). Provides
    accurate related_match context.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/model-robust-nonlinearity-sandwich-and-rav-test-boundaries.py
  accessed_at: '2026-10-17T17:55:00Z'
  snapshot_sha256: 3fb7db63bdb7f99b0781cc32c64afa1f9b9f0f55060057e25d68d46ffc49da49
  support: supports
  summary: 'Executed pure-Python verification in research/discovery/model-robust-nonlinearity-sandwich-and-rav-test-boundaries.py
    (SHA-256 3fb7db63bdb7f99b0781cc32c64afa1f9b9f0f55060057e25d68d46ffc49da49): (1)
    Regime 1 (Proposition 4.1 & canonical decomposition): verified nonlinear slope
    shift from 0.0 under P_{X,1} to 2.0 under P_{X,2} vs. linear invariance 2.0 =
    2.0, and exact orthogonality error 0.0. (2) Regime 2 (Estimation Offsets & Proposition
    8.2 bootstrap limit): verified Var(Noise EO) = 0.003204, Var(Approx EO) = 0.013707,
    Var(Total EO) = 0.015723, Cov(Noise, Approx) = -0.000547, and M-of-N bootstrap
    scaled variance 1.100014 matching plug-in sandwich 1.029159 (rel error 0.068848).
    (3) Regime 3 (Section 10 weighted slopes & Section 11 RAV bounds): verified exact
    equality of matrix (1.768122), case-wise (1.768122), and pairwise (1.768122) OLS
    slopes, and Lemma E.2 convex combination RAV[m^2] = 1.348668 from protective RAV[sigma^2]
    = 0.357143 < 1 and anti-protective RAV[eta^2] = 2.028571 > 1 within sharp bounds
    [0.142857, 2.285714]. (4) Regime 4 (Section 12 RAV_hat_j test): verified Proposition
    12.2 Gaussian null variance = 8.0 (SD = 2.828427) and permutation test detection
    of nonlinear X_1 (RAV_hat_1 = 3.319706, p = 0.0025) while linear X_2 is unrejected
    (RAV_hat_2 = 0.804898, p = 0.3775).'
- evidence_id: buja2019p1-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/1404.1578
  locator: Pages 1-43, Sections 1-14 and Appendices A-F (Equations 1-30, Proposition
    4.1, Proposition 7, Propositions 8.1-8.2, Proposition 9.1, Definition 11.4, Proposition
    11.5, Definition 12.1, Proposition 12.2, Lemma E.2, Proposition E.3)
  accessed_at: '2026-10-17T17:55:00Z'
  snapshot_sha256: 11d501663ce1861ce2fd446b367d12360456fe6a1f4d0b8ffef1a49b5674a61d
  support: supports
  summary: All 43 pages of the full-text PDF of arXiv:1404.1578v4 read. Checked all
    definitions, propositions, lemmas, equations, and proofs.
- evidence_id: buja2019p1-crossref
  kind: primary_source
  reference: https://api.crossref.org/works/10.1214/18-STS693
  locator: Statistical Science 34(4):523-544 publication record
  accessed_at: '2026-10-17T17:55:00Z'
  snapshot_sha256: 72ef24d405646eeaed1810f783df3afe2bc62ac2fc2d50b082bd873c165ea715
  support: supports
  summary: Official Statistical Science 34(4):523-544 Crossref record read and verified.
- evidence_id: buja2019p1-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1404.1578
  locator: arXiv:1404.1578v4 abstract and metadata
  accessed_at: '2026-10-17T17:55:00Z'
  snapshot_sha256: 38a840a331cdab71ed15d55946e521ee7bbbdd73a77a5d06f9b6b6aa248e55ca
  support: supports
  summary: arXiv:1404.1578v4 abstract and metadata read and verified.
assessments:
- assessment_id: identity
  area: identity
  topic: ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest versus ValidPostSelectionInferencePoSIConstant
    and UniformlyValidPostModelSelectionConfidenceIntervals
  outcome: supported
  target_ids:
  - AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest
  evidence_ids:
  - identity
  - buja2019p1-pdf
  - buja2019p1-crossref
  summary: Retain Model-robust nonlinearity-consistent sandwich variance and Ratio
    of Asymptotic Variances (RAV) specification test as a distinct DRAFT mathematical_method.
  details: Buja et al. (2019, Part I) establish the model-robust theory of linear
    OLS under nonlinearity and random regressors, proving Proposition 4.1, the Noise/Approximation
    Estimation Offset decomposition, Proposition 8.2 M-of-N bootstrap limit, Section
    10 weighted slope representations, and the RAV_j specification test.
- assessment_id: mapping
  area: grounding
  topic: Mapping to AIO:LinearRegression
  outcome: supported
  target_ids:
  - AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest
  evidence_ids:
  - mapping
  - buja2019p1-pdf
  summary: Related mapping to LinearRegression is supported.
  details: Reconstructs linear OLS as a population functional (AIO:LinearRegression)
    and characterizes how misspecification bias eta(X_vec) induces O_P(N^{-1/2}) Approximation
    Estimation Offset variance.
- assessment_id: regressor-ancillarity-failure-and-canonical-noise-nonlinearity-decomposition
  area: evidence
  topic: regressor-ancillarity-failure-and-canonical-noise-nonlinearity-decomposition
  outcome: supported
  target_ids:
  - AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest
  evidence_ids:
  - buja2019p1-pdf
  - buja2019p1-crossref
  - calculation
  summary: Supported by Sections 3-5 (Equations 1-9, Proposition 4.1) and Appendix
    E.1.
  details: Verified regressor-distribution slope dependence under nonlinearity vs.
    invariance under linearity.
- assessment_id: estimation-offset-pythagorean-clt-and-pairs-bootstrap-sandwich-limit
  area: evidence
  topic: estimation-offset-pythagorean-clt-and-pairs-bootstrap-sandwich-limit
  outcome: supported
  target_ids:
  - AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest
  evidence_ids:
  - buja2019p1-pdf
  - buja2019p1-abs
  - calculation
  summary: Supported by Sections 5-8 (Equations 10-20, Proposition 7, Propositions
    8.1-8.2) and Appendix C.
  details: Verified finite-sample orthogonality of Noise and Approximation EOs and
    convergence of M * V[beta^*_M] to AV_hat_sand[beta].
- assessment_id: adjusted-regressor-weighted-slopes-and-rav-convex-bounds
  area: evidence
  topic: adjusted-regressor-weighted-slopes-and-rav-convex-bounds
  outcome: supported
  target_ids:
  - AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest
  evidence_ids:
  - buja2019p1-pdf
  - calculation
  summary: Supported by Sections 9-11 (Equations 21-28, Definition 11.4, Proposition
    11.5) and Appendix E.2-E.4.
  details: Verified exact equality of matrix, case-wise, and pairwise OLS slopes and
    Lemma E.2 convex combination and sharp bounds for RAV.
- assessment_id: regressor-specific-rav-specification-test-and-null-asymptotics
  area: evidence
  topic: regressor-specific-rav-specification-test-and-null-asymptotics
  outcome: supported
  target_ids:
  - AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest
  evidence_ids:
  - buja2019p1-pdf
  - buja2019p1-crossref
  - calculation
  summary: Supported by Section 12 (Definition 12.1, Proposition 12.2, Section 12.3)
    and Appendix F.
  details: Verified Gaussian null variance = 8 and permutation test detection of regressor-specific
    nonlinearity.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest
  evidence_ids:
  - identity
  - mapping
  - buja2019p1-pdf
  - buja2019p1-crossref
  - buja2019p1-abs
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of ModelRobustNonlinearityConsistentSandwichAndRAVSpecificationTest.yaml:
    stable ID, name, aliases, mathematical_method kind, definition, definition_evidence,
    identity_notes, four claims and locators, three primary sources with exact SHA-256
    digests, pinned AIO mappings and rationales, four scoped limitations, and UTC
    curation metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Model-robust nonlinearity-consistent sandwich variance and Ratio
  of Asymptotic Variances (RAV) specification test record, yielding 609 native and
  442 unchanged generated records.
- All 43 PDF pages of arXiv:1404.1578v4 were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- model-misspecification
- sandwich-estimator
- linear-regression
- self-review
- discovery-ongoing
```
