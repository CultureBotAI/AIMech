# Scientific author self-review of Heteroskedastic PCA Principal Subspace Confidence Regions and Spiked Covariance Inference with Missing Data

- Review: 20261019T053830Z-heteroskedastic-pca-missing-data-subspace-inference
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T05:38:00Z
- Finished UTC: 2026-10-19T05:38:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Heteroskedastic PCA Principal Subspace Confidence Regions and Spiked Covariance Inference with Missing Data as a distinct DRAFT mathematical_method. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ac20721ede7cb38a7c51a7d3f111585d9d933b14.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData | data/curated/HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData.yaml | maintained | Heteroskedastic PCA Principal Subspace Confidence Regions and Spiked Covariance Inference with Missing Data |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData | Validated history sidecar files. |
| python3 heteroskedastic-pca-missing-data-subspace-inference-boundaries.py | passed | True | AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData | {<br>  "dimension_d": 16,<br>  "sample_size_n": 450,<br>  "observation_prob_p": 0.65,<br>  "mean_vanilla_sin_theta": 0.21321,<br>  "mean_deflated_sin_theta": 0.07536,<br>  "bias_reduction_ratio": 2.829,<br>  "coordinate_0_wald_95_coverage": 0.9667,<br>  "linear_form_95_coverage": 0.875<br>} |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData.

Heteroskedastic PCA Principal Subspace Confidence Regions and Spiked Covariance Inference with Missing Data is a distinct concept.

Resolved against all 442 pinned AIO concepts and 687 maintained AIMech concepts. Distinct from &#96;AIMech:AsymmetricLowRankEigenvalueAndLinearFormEigenvectorPerturbationAnalysis&#96; (Chen, Cheng, &amp; Fan 2021, which analyzes a single $n \times n$ asymmetric noisy matrix with independent entries rather than sample Gram matrices $\frac{1}{n}\sum_{t=1}^n \boldsymbol{z}_t\boldsymbol{z}_t^\top$ whose entries have dependent Wishart-type products across $n$ observations, diagonal noise-variance inflation, and multi-rank $\chi_r^2$ Wald subspace confidence regions) and from &#96;AIMech:DebiasedNoisyMatrixCompletionInferenceAndUncertaintyQuantification&#96; (Chen, Fan, Ma, &amp; Yan 2019, which addresses homoskedastic matrix completion where $d_1 \asymp d_2$ rather than spiked covariance PCA with $d \ll n$ or $d \gtrsim n$ under heteroskedastic column observations).

### AIO mapping accuracy

grounding: supported. Targets: AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in heteroskedastic-pca-missing-data-subspace-inference-boundaries.py passed with exit code 0: {
  "dimension_d": 16,
  "sample_size_n": 450,
  "observation_prob_p": 0.65,
  "mean_vanilla_sin_theta": 0.21321,
  "mean_deflated_sin_theta": 0.07536,
  "bias_reduction_ratio": 2.829,
  "coordinate_0_wald_95_coverage": 0.9667,
  "linear_form_95_coverage": 0.875
}

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T053800Z-heteroskedastic-pca-missing-data-subspace-inference.json | supports | No normalized identity match for AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/heteroskedastic-pca-missing-data-subspace-inference-boundaries.py | supports | All constructed boundary assertions in heteroskedastic-pca-missing-data-subspace-inference-boundaries.py passed with exit code 0: {<br>  "dimension_d": 16,<br>  "sample_size_n": 450,<br>  "observation_prob_p": 0.65,<br>  "mean_vanilla_sin_theta": 0.21321,<br>  "mean_deflated_sin_theta": 0.07536,<br>  "bias_reduction_ratio": 2.829,<br>  "coordinate_0_wald_95_coverage": 0.9667,<br>  "linear_form_95_coverage": 0.875<br>} |
| ycf2024-hpca-pdf | https://arxiv.org/pdf/2107.12365.pdf; Full-text PDF | supports | Full-text PDF (arXiv:2107.12365v2 full-text PDF (69 pages), published in The Annals of Statistics 52(2):729-756 (2024).) read and verified. |
| ycf2024-hpca-abs | https://arxiv.org/abs/2107.12365; arXiv abstract | supports | arXiv abstract read and verified. |
| ycf2024-hpca-cr | https://api.crossref.org/works/10.1214/24-AOS2366; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData in Round 293.
- All pages of arXiv:2107.12365v2 full-text PDF (69 pages), published in The Annals of Statistics 52(2):729-756 (2024). were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T053830Z-heteroskedastic-pca-missing-data-subspace-inference
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Heteroskedastic PCA Principal Subspace Confidence
  Regions and Spiked Covariance Inference with Missing Data
started_at: '2026-10-19T05:38:00Z'
finished_at: '2026-10-19T05:38:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData
    against existing AIMech and AIO records and verified all claims against arXiv:2107.12365v2
    full-text PDF (69 pages), published in The Annals of Statistics 52(2):729-756
    (2024). and pure-Python boundary checks. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Heteroskedastic PCA Principal Subspace Confidence Regions and Spiked
  Covariance Inference with Missing Data as a distinct DRAFT mathematical_method.
  All three claims are supported by full-text primary evidence and pure-Python boundary
  verification.
source:
  git_revision: ac20721ede7cb38a7c51a7d3f111585d9d933b14
  state: working_tree
  inputs:
  - path: data/aio/DimensionalityReduction.yaml
    sha256: 99eb0714b362a98a9e704e5ef2ac370cb7a900fbe97da43de790c3ec67ed812e
    role: context
  - path: data/aio/PrincipalComponentAnalysis.yaml
    sha256: 7b45b5c558b7e984abb44e1610fb8d829409ae391a151ed0dc0e5cd95023e8d4
    role: context
  - path: data/curated/HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData.yaml
    sha256: 49622f6b4848ecc199efe78d1e2fc3e12d6246f5f0f4b38e08761c5da5ed7fc9
    role: target
  - path: research/discovery/20261019T053800Z-heteroskedastic-pca-missing-data-subspace-inference.json
    sha256: 962229eb80c2aad5479c9ad92dd23f3b0960d049cb569fce64b15791ea4bdc27
    role: context
  - path: research/discovery/heteroskedastic-pca-missing-data-subspace-inference-boundaries.py
    sha256: bbcfbb470f4fd43d1b2d784d034c2184ee294b9eeaafaef1bed4d177f3d7eade
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
- target_id: AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData
  path: data/curated/HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData.yaml
  label: Heteroskedastic PCA Principal Subspace Confidence Regions and Spiked Covariance
    Inference with Missing Data
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData.yaml
    role: maintained
scope:
  description: All fields of data/curated/HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData
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
  - AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 heteroskedastic-pca-missing-data-subspace-inference-boundaries.py
  command: python3 research/discovery/heteroskedastic-pca-missing-data-subspace-inference-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"dimension_d\": 16,\n  \"sample_size_n\": 450,\n  \"observation_prob_p\"\
    : 0.65,\n  \"mean_vanilla_sin_theta\": 0.21321,\n  \"mean_deflated_sin_theta\"\
    : 0.07536,\n  \"bias_reduction_ratio\": 2.829,\n  \"coordinate_0_wald_95_coverage\"\
    : 0.9667,\n  \"linear_form_95_coverage\": 0.875\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T053800Z-heteroskedastic-pca-missing-data-subspace-inference.json
  accessed_at: '2026-10-19T05:38:00Z'
  support: supports
  summary: No normalized identity match for AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T05:38:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/heteroskedastic-pca-missing-data-subspace-inference-boundaries.py
  accessed_at: '2026-10-19T05:38:00Z'
  snapshot_sha256: bbcfbb470f4fd43d1b2d784d034c2184ee294b9eeaafaef1bed4d177f3d7eade
  support: supports
  summary: "All constructed boundary assertions in heteroskedastic-pca-missing-data-subspace-inference-boundaries.py\
    \ passed with exit code 0: {\n  \"dimension_d\": 16,\n  \"sample_size_n\": 450,\n\
    \  \"observation_prob_p\": 0.65,\n  \"mean_vanilla_sin_theta\": 0.21321,\n  \"\
    mean_deflated_sin_theta\": 0.07536,\n  \"bias_reduction_ratio\": 2.829,\n  \"\
    coordinate_0_wald_95_coverage\": 0.9667,\n  \"linear_form_95_coverage\": 0.875\n\
    }"
- evidence_id: ycf2024-hpca-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2107.12365.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T05:38:00Z'
  snapshot_sha256: 2aaf20e127117dbcdf09b4a83a123e8b4bfc6adac75c0d0d759d17e3c18e5a95
  support: supports
  summary: Full-text PDF (arXiv:2107.12365v2 full-text PDF (69 pages), published in
    The Annals of Statistics 52(2):729-756 (2024).) read and verified.
- evidence_id: ycf2024-hpca-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2107.12365
  locator: arXiv abstract
  accessed_at: '2026-10-19T05:38:00Z'
  snapshot_sha256: d92dcee36dd492336729939f327066e9c7835536496f95134d41251e42e0ba07
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: ycf2024-hpca-cr
  kind: primary_source
  reference: https://api.crossref.org/works/10.1214/24-AOS2366
  locator: Crossref metadata
  accessed_at: '2026-10-19T05:38:00Z'
  snapshot_sha256: 9d30bd3ca31be5afb779d88ebb419e0628abbd468c997025e8538a6e3f85910f
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData
  evidence_ids:
  - identity
  - ycf2024-hpca-pdf
  - ycf2024-hpca-abs
  - ycf2024-hpca-cr
  summary: Heteroskedastic PCA Principal Subspace Confidence Regions and Spiked Covariance
    Inference with Missing Data is a distinct concept.
  details: Resolved against all 442 pinned AIO concepts and 687 maintained AIMech
    concepts. Distinct from `AIMech:AsymmetricLowRankEigenvalueAndLinearFormEigenvectorPerturbationAnalysis`
    (Chen, Cheng, & Fan 2021, which analyzes a single $n \times n$ asymmetric noisy
    matrix with independent entries rather than sample Gram matrices $\frac{1}{n}\sum_{t=1}^n
    \boldsymbol{z}_t\boldsymbol{z}_t^\top$ whose entries have dependent Wishart-type
    products across $n$ observations, diagonal noise-variance inflation, and multi-rank
    $\chi_r^2$ Wald subspace confidence regions) and from `AIMech:DebiasedNoisyMatrixCompletionInferenceAndUncertaintyQuantification`
    (Chen, Fan, Ma, & Yan 2019, which addresses homoskedastic matrix completion where
    $d_1 \asymp d_2$ rather than spiked covariance PCA with $d \ll n$ or $d \gtrsim
    n$ under heteroskedastic column observations).
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData
  evidence_ids:
  - mapping
  - ycf2024-hpca-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData
  evidence_ids:
  - ycf2024-hpca-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: "All constructed boundary assertions in heteroskedastic-pca-missing-data-subspace-inference-boundaries.py\
    \ passed with exit code 0: {\n  \"dimension_d\": 16,\n  \"sample_size_n\": 450,\n\
    \  \"observation_prob_p\": 0.65,\n  \"mean_vanilla_sin_theta\": 0.21321,\n  \"\
    mean_deflated_sin_theta\": 0.07536,\n  \"bias_reduction_ratio\": 2.829,\n  \"\
    coordinate_0_wald_95_coverage\": 0.9667,\n  \"linear_form_95_coverage\": 0.875\n\
    }"
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData
  evidence_ids:
  - identity
  - mapping
  - ycf2024-hpca-pdf
  - ycf2024-hpca-abs
  - ycf2024-hpca-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:HeteroskedasticPCAPrincipalSubspaceConfidenceRegionsAndSpikedCovarianceInferenceWithMissingData
  in Round 293.
- All pages of arXiv:2107.12365v2 full-text PDF (69 pages), published in The Annals
  of Statistics 52(2):729-756 (2024). were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
