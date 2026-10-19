# Scientific author self-review of HeteroPCA Iterative Diagonal Imputation and Robust Subspace Perturbation for Heteroskedastic PCA

- Review: 20261019T054230Z-heteropca-iterative-diagonal-imputation-heteroskedastic-pca
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T05:42:00Z
- Finished UTC: 2026-10-19T05:42:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain HeteroPCA Iterative Diagonal Imputation and Robust Subspace Perturbation for Heteroskedastic PCA as a distinct DRAFT algorithm. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 51a72ad8f2a686bc9cdd479906593e195eef70f5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA | data/curated/HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA.yaml | maintained | HeteroPCA Iterative Diagonal Imputation and Robust Subspace Perturbation for Heteroskedastic PCA |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA | Validated history sidecar files. |
| python3 heteropca-iterative-diagonal-imputation-heteroskedastic-pca-boundaries.py | passed | True | AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA | {<br>  "lemma4_sharp_factor_2": {<br>    "p": 10,<br>    "empirical_ratio": 1.8,<br>    "exact_2_minus_2_over_p": 1.8<br>  },<br>  "lemma1_contraction": {<br>    "incoherence_I_U": 1.915976,<br>    "lhs_D_PU_D_A_norm": 0.418701,<br>    "rhs_bound_I_r_over_p": 0.603291<br>  },<br>  "theorem3_and_theorem1_heteropca": {<br>    "pure_diag_perturbation_t0_err": 0.111015,<br>    "pure_diag_perturbation_t8_err": 1.2016e-06,<br>    "heteroskedastic_sample_err_regular_svd": 0.32001,<br>    "heteroskedastic_sample_err_diag_deletion": 0.13466,<br>    "heteroskedastic_sample_err_heteropca_T10": 0.05914<br>  },<br>  "all_assertions_passed": true<br>} |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA.

HeteroPCA Iterative Diagonal Imputation and Robust Subspace Perturbation for Heteroskedastic PCA is a distinct concept.

Resolved against all 442 pinned AIO concepts and 689 maintained AIMech concepts. Distinct from &#96;AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData&#96; (Yan, Chen, &amp; Fan 2024, which develops distributional asymptotic normality and $\chi_r^2$ confidence regions for subspace rows and linear forms by building upon the HeteroPCA estimator) and from &#96;AIMech:EntrywiseFirstOrderEigenvectorApproximationAndLeaveOneOutPerturbationAnalysisForLowExpectedRankRandomMatrices&#96; (Abbe, Fan, Wang, &amp; Zhong 2020, which analyzes un-imputed symmetric random matrices).

### AIO mapping accuracy

grounding: supported. Targets: AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in heteropca-iterative-diagonal-imputation-heteroskedastic-pca-boundaries.py passed with exit code 0: {
  "lemma4_sharp_factor_2": {
    "p": 10,
    "empirical_ratio": 1.8,
    "exact_2_minus_2_over_p": 1.8
  },
  "lemma1_contraction": {
    "incoherence_I_U": 1.915976,
    "lhs_D_PU_D_A_norm": 0.418701,
    "rhs_bound_I_r_over_p": 0.603291
  },
  "theorem3_and_theorem1_heteropca": {
    "pure_diag_perturbation_t0_err": 0.111015,
    "pure_diag_perturbation_t8_err": 1.2016e-06,
    "heteroskedastic_sample_err_regular_svd": 0.32001,
    "heteroskedastic_sample_err_diag_deletion": 0.13466,
    "heteroskedastic_sample_err_heteropca_T10": 0.05914
  },
  "all_assertions_passed": true
}

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T054200Z-heteropca-iterative-diagonal-imputation-heteroskedastic-pca.json | supports | No normalized identity match for AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/heteropca-iterative-diagonal-imputation-heteroskedastic-pca-boundaries.py | supports | All constructed boundary assertions in heteropca-iterative-diagonal-imputation-heteroskedastic-pca-boundaries.py passed with exit code 0: {<br>  "lemma4_sharp_factor_2": {<br>    "p": 10,<br>    "empirical_ratio": 1.8,<br>    "exact_2_minus_2_over_p": 1.8<br>  },<br>  "lemma1_contraction": {<br>    "incoherence_I_U": 1.915976,<br>    "lhs_D_PU_D_A_norm": 0.418701,<br>    "rhs_bound_I_r_over_p": 0.603291<br>  },<br>  "theorem3_and_theorem1_heteropca": {<br>    "pure_diag_perturbation_t0_err": 0.111015,<br>    "pure_diag_perturbation_t8_err": 1.2016e-06,<br>    "heteroskedastic_sample_err_regular_svd": 0.32001,<br>    "heteroskedastic_sample_err_diag_deletion": 0.13466,<br>    "heteroskedastic_sample_err_heteropca_T10": 0.05914<br>  },<br>  "all_assertions_passed": true<br>} |
| zcw2022-heteropca-pdf | https://arxiv.org/pdf/1810.08316.pdf; Full-text PDF | supports | Full-text PDF (arXiv:1810.08316v3 full-text PDF (56 pages), published in The Annals of Statistics 50(1):53-80 (2022).) read and verified. |
| zcw2022-heteropca-abs | https://arxiv.org/abs/1810.08316; arXiv abstract | supports | arXiv abstract read and verified. |
| zcw2022-heteropca-cr | https://api.crossref.org/works/10.1214/21-AOS2074; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA in Round 295.
- All pages of arXiv:1810.08316v3 full-text PDF (56 pages), published in The Annals of Statistics 50(1):53-80 (2022). were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T054230Z-heteropca-iterative-diagonal-imputation-heteroskedastic-pca
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of HeteroPCA Iterative Diagonal Imputation and
  Robust Subspace Perturbation for Heteroskedastic PCA
started_at: '2026-10-19T05:42:00Z'
finished_at: '2026-10-19T05:42:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA
    against existing AIMech and AIO records and verified all claims against arXiv:1810.08316v3
    full-text PDF (56 pages), published in The Annals of Statistics 50(1):53-80 (2022).
    and pure-Python boundary checks. This is adversarial author self-review, not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain HeteroPCA Iterative Diagonal Imputation and Robust Subspace Perturbation
  for Heteroskedastic PCA as a distinct DRAFT algorithm. All three claims are supported
  by full-text primary evidence and pure-Python boundary verification.
source:
  git_revision: 51a72ad8f2a686bc9cdd479906593e195eef70f5
  state: working_tree
  inputs:
  - path: data/aio/DimensionalityReduction.yaml
    sha256: 99eb0714b362a98a9e704e5ef2ac370cb7a900fbe97da43de790c3ec67ed812e
    role: context
  - path: data/aio/PrincipalComponentAnalysis.yaml
    sha256: 7b45b5c558b7e984abb44e1610fb8d829409ae391a151ed0dc0e5cd95023e8d4
    role: context
  - path: data/curated/HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA.yaml
    sha256: 323d5c8c4abecc7a0dd54e474be7d1fe36adae363666280df97a93884bbfe265
    role: target
  - path: research/discovery/20261019T054200Z-heteropca-iterative-diagonal-imputation-heteroskedastic-pca.json
    sha256: c171355d5ad0a261610789acabbf94b9c0b8e061d6354c8dac1bf06378e337f1
    role: context
  - path: research/discovery/heteropca-iterative-diagonal-imputation-heteroskedastic-pca-boundaries.py
    sha256: f6873389131cd18407a62742def94b1387cd1dd48f156301007d77d315637211
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
- target_id: AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA
  path: data/curated/HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA.yaml
  label: HeteroPCA Iterative Diagonal Imputation and Robust Subspace Perturbation
    for Heteroskedastic PCA
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA.yaml
    role: maintained
scope:
  description: All fields of data/curated/HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA
  exclusions:
  - target: Existing native and AIO neighbors
    reason: Identity and mapping context, not full scientific rereview.
checks:
- check_id: validation-1
  name: aimech validate
  command: aimech validate
  status: passed
  required: true
  target_ids:
  - AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 heteropca-iterative-diagonal-imputation-heteroskedastic-pca-boundaries.py
  command: python3 research/discovery/heteropca-iterative-diagonal-imputation-heteroskedastic-pca-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"lemma4_sharp_factor_2\": {\n    \"p\": 10,\n    \"empirical_ratio\"\
    : 1.8,\n    \"exact_2_minus_2_over_p\": 1.8\n  },\n  \"lemma1_contraction\": {\n\
    \    \"incoherence_I_U\": 1.915976,\n    \"lhs_D_PU_D_A_norm\": 0.418701,\n  \
    \  \"rhs_bound_I_r_over_p\": 0.603291\n  },\n  \"theorem3_and_theorem1_heteropca\"\
    : {\n    \"pure_diag_perturbation_t0_err\": 0.111015,\n    \"pure_diag_perturbation_t8_err\"\
    : 1.2016e-06,\n    \"heteroskedastic_sample_err_regular_svd\": 0.32001,\n    \"\
    heteroskedastic_sample_err_diag_deletion\": 0.13466,\n    \"heteroskedastic_sample_err_heteropca_T10\"\
    : 0.05914\n  },\n  \"all_assertions_passed\": true\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T054200Z-heteropca-iterative-diagonal-imputation-heteroskedastic-pca.json
  accessed_at: '2026-10-19T05:42:00Z'
  support: supports
  summary: No normalized identity match for AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T05:42:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/heteropca-iterative-diagonal-imputation-heteroskedastic-pca-boundaries.py
  accessed_at: '2026-10-19T05:42:00Z'
  snapshot_sha256: f6873389131cd18407a62742def94b1387cd1dd48f156301007d77d315637211
  support: supports
  summary: "All constructed boundary assertions in heteropca-iterative-diagonal-imputation-heteroskedastic-pca-boundaries.py\
    \ passed with exit code 0: {\n  \"lemma4_sharp_factor_2\": {\n    \"p\": 10,\n\
    \    \"empirical_ratio\": 1.8,\n    \"exact_2_minus_2_over_p\": 1.8\n  },\n  \"\
    lemma1_contraction\": {\n    \"incoherence_I_U\": 1.915976,\n    \"lhs_D_PU_D_A_norm\"\
    : 0.418701,\n    \"rhs_bound_I_r_over_p\": 0.603291\n  },\n  \"theorem3_and_theorem1_heteropca\"\
    : {\n    \"pure_diag_perturbation_t0_err\": 0.111015,\n    \"pure_diag_perturbation_t8_err\"\
    : 1.2016e-06,\n    \"heteroskedastic_sample_err_regular_svd\": 0.32001,\n    \"\
    heteroskedastic_sample_err_diag_deletion\": 0.13466,\n    \"heteroskedastic_sample_err_heteropca_T10\"\
    : 0.05914\n  },\n  \"all_assertions_passed\": true\n}"
- evidence_id: zcw2022-heteropca-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/1810.08316.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T05:42:00Z'
  snapshot_sha256: 45e13fbed3d9ce23cf1de41de4688f17fafdf0b46dbddc1960d634a7e5a1c58f
  support: supports
  summary: Full-text PDF (arXiv:1810.08316v3 full-text PDF (56 pages), published in
    The Annals of Statistics 50(1):53-80 (2022).) read and verified.
- evidence_id: zcw2022-heteropca-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1810.08316
  locator: arXiv abstract
  accessed_at: '2026-10-19T05:42:00Z'
  snapshot_sha256: 1e2b02ae49631e04421342b175d789c98f6cda3482b2c7b991bab919a19556c4
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: zcw2022-heteropca-cr
  kind: primary_source
  reference: https://api.crossref.org/works/10.1214/21-AOS2074
  locator: Crossref metadata
  accessed_at: '2026-10-19T05:42:00Z'
  snapshot_sha256: 4e4b4cfd258b9a50ff30816730bf5065b488eed77c3d5d3de61ce09b8b702629
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA
  evidence_ids:
  - identity
  - zcw2022-heteropca-pdf
  - zcw2022-heteropca-abs
  - zcw2022-heteropca-cr
  summary: HeteroPCA Iterative Diagonal Imputation and Robust Subspace Perturbation
    for Heteroskedastic PCA is a distinct concept.
  details: Resolved against all 442 pinned AIO concepts and 689 maintained AIMech
    concepts. Distinct from `AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData`
    (Yan, Chen, & Fan 2024, which develops distributional asymptotic normality and
    $\chi_r^2$ confidence regions for subspace rows and linear forms by building upon
    the HeteroPCA estimator) and from `AIMech:EntrywiseFirstOrderEigenvectorApproximationAndLeaveOneOutPerturbationAnalysisForLowExpectedRankRandomMatrices`
    (Abbe, Fan, Wang, & Zhong 2020, which analyzes un-imputed symmetric random matrices).
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA
  evidence_ids:
  - mapping
  - zcw2022-heteropca-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA
  evidence_ids:
  - zcw2022-heteropca-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: "All constructed boundary assertions in heteropca-iterative-diagonal-imputation-heteroskedastic-pca-boundaries.py\
    \ passed with exit code 0: {\n  \"lemma4_sharp_factor_2\": {\n    \"p\": 10,\n\
    \    \"empirical_ratio\": 1.8,\n    \"exact_2_minus_2_over_p\": 1.8\n  },\n  \"\
    lemma1_contraction\": {\n    \"incoherence_I_U\": 1.915976,\n    \"lhs_D_PU_D_A_norm\"\
    : 0.418701,\n    \"rhs_bound_I_r_over_p\": 0.603291\n  },\n  \"theorem3_and_theorem1_heteropca\"\
    : {\n    \"pure_diag_perturbation_t0_err\": 0.111015,\n    \"pure_diag_perturbation_t8_err\"\
    : 1.2016e-06,\n    \"heteroskedastic_sample_err_regular_svd\": 0.32001,\n    \"\
    heteroskedastic_sample_err_diag_deletion\": 0.13466,\n    \"heteroskedastic_sample_err_heteropca_T10\"\
    : 0.05914\n  },\n  \"all_assertions_passed\": true\n}"
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA
  evidence_ids:
  - identity
  - mapping
  - zcw2022-heteropca-pdf
  - zcw2022-heteropca-abs
  - zcw2022-heteropca-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:HeteroPCAIterativeDiagonalImputationAndRobustSubspacePerturbationForHeteroskedasticPCA
  in Round 295.
- All pages of arXiv:1810.08316v3 full-text PDF (56 pages), published in The Annals
  of Statistics 50(1):53-80 (2022). were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
