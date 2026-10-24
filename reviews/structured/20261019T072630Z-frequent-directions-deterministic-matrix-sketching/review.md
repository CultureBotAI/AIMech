# Scientific author self-review of Frequent Directions Deterministic Row-Update Matrix Sketching via Singular-Value Shrinkage

- Review: 20261019T072630Z-frequent-directions-deterministic-matrix-sketching
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T07:26:00Z
- Finished UTC: 2026-10-19T07:26:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Frequent Directions Deterministic Row-Update Matrix Sketching via Singular-Value Shrinkage as a distinct DRAFT algorithm. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/FrequentDirectionsDeterministicMatrixSketching.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:FrequentDirectionsDeterministicMatrixSketching
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 92c1f9c2c25d641994fbd6b5d671664c405cc988.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:FrequentDirectionsDeterministicMatrixSketching | data/curated/FrequentDirectionsDeterministicMatrixSketching.yaml | maintained | Frequent Directions Deterministic Row-Update Matrix Sketching via Singular-Value Shrinkage |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:FrequentDirectionsDeterministicMatrixSketching | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:FrequentDirectionsDeterministicMatrixSketching | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:FrequentDirectionsDeterministicMatrixSketching | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:FrequentDirectionsDeterministicMatrixSketching | Validated history sidecar files. |
| python3 frequent-directions-deterministic-matrix-sketching-boundaries.py | passed | True | AIMech:FrequentDirectionsDeterministicMatrixSketching | [PASS] Round 363 Frequent Directions (Ghashami et al. 2016): prop1_min=2.87e+00, Delta=12.3685&lt;=14.9785, prop3_err=1.49e-13, merge_err=7.82e-14, adv_cov_fd=4.0000&lt;&lt;inc=32.4000 |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:FrequentDirectionsDeterministicMatrixSketching.

Frequent Directions Deterministic Row-Update Matrix Sketching via Singular-Value Shrinkage is a distinct concept.

Distinct from AIMech:FrequentDirectionsDeterministicStreamingMatrixSketching (Round 330, Liberty KDD 2013), which established only the flat-spectrum Frobenius covariance error bound &#124;&#124;A^T A - B^T B&#124;&#124;_2 &lt;= 2&#124;&#124;A&#124;&#124;_F^2/ell without rank-k tail residuals or relative-error projection bounds; this record captures Ghashami, Liberty, Phillips, and Woodruff's (2015, 2016) tail-residual relative-error covariance and rank-k projection analysis (&#124;&#124;A^T A - B^T B&#124;&#124;_2 &lt;= &#124;&#124;A - A_k&#124;&#124;_F^2/(ell - k), &#124;&#124;A - pi_B^k(A)&#124;&#124;_F^2 &lt;= (ell/(ell - k))&#124;&#124;A - A_k&#124;&#124;_F^2) and matching Grassmannian/Index space-optimality lower bounds. Also distinct from AIMech:NoisyPowerMethodForStreamingAndDifferentiallyPrivatePCA (Round 356) and AIMech:StreamingPCANearOptimalFiniteSampleOjaAlgorithm (Round 357), which are randomized iterative subspace estimators rather than deterministic Misra-Gries-style singular-value shrinkage sketches.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:FrequentDirectionsDeterministicMatrixSketching.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:FrequentDirectionsDeterministicMatrixSketching.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in frequent-directions-deterministic-matrix-sketching-boundaries.py passed with exit code 0: [PASS] Round 363 Frequent Directions (Ghashami et al. 2016): prop1_min=2.87e+00, Delta=12.3685&lt;=14.9785, prop3_err=1.49e-13, merge_err=7.82e-14, adv_cov_fd=4.0000&lt;&lt;inc=32.4000

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:FrequentDirectionsDeterministicMatrixSketching.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T072600Z-frequent-directions-deterministic-matrix-sketching.json | supports | No normalized identity match for AIMech:FrequentDirectionsDeterministicMatrixSketching across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/frequent-directions-deterministic-matrix-sketching-boundaries.py | supports | All constructed boundary assertions in frequent-directions-deterministic-matrix-sketching-boundaries.py passed with exit code 0: [PASS] Round 363 Frequent Directions (Ghashami et al. 2016): prop1_min=2.87e+00, Delta=12.3685&lt;=14.9785, prop3_err=1.49e-13, merge_err=7.82e-14, adv_cov_fd=4.0000&lt;&lt;inc=32.4000 |
| r363-primary-pdf | https://arxiv.org/pdf/1501.01711.pdf; Full-text PDF | supports | Full-text PDF (SIAM Journal on Computing 45(5):1762-1792 (arXiv:1501.01711) (2016)) read and verified. |
| r363-arxiv-abs | https://arxiv.org/abs/1501.01711; arXiv abstract | supports | arXiv abstract read and verified. |
| r363-metadata-cr | https://api.crossref.org/works/10.1137/15m1009718; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:FrequentDirectionsDeterministicMatrixSketching in Round 363.
- All pages of SIAM Journal on Computing 45(5):1762-1792 (arXiv:1501.01711) (2016) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T072630Z-frequent-directions-deterministic-matrix-sketching
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Frequent Directions Deterministic Row-Update
  Matrix Sketching via Singular-Value Shrinkage
started_at: '2026-10-19T07:26:00Z'
finished_at: '2026-10-19T07:26:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:FrequentDirectionsDeterministicMatrixSketching
    against existing AIMech and AIO records and verified all claims against SIAM Journal
    on Computing 45(5):1762-1792 (arXiv:1501.01711) (2016) and pure-Python boundary
    checks. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Frequent Directions Deterministic Row-Update Matrix Sketching via
  Singular-Value Shrinkage as a distinct DRAFT algorithm. All three claims are supported
  by full-text primary evidence and pure-Python boundary verification.
source:
  git_revision: 92c1f9c2c25d641994fbd6b5d671664c405cc988
  state: working_tree
  inputs:
  - path: data/aio/DimensionalityReduction.yaml
    sha256: 99eb0714b362a98a9e704e5ef2ac370cb7a900fbe97da43de790c3ec67ed812e
    role: context
  - path: data/aio/PrincipalComponentAnalysis.yaml
    sha256: 7b45b5c558b7e984abb44e1610fb8d829409ae391a151ed0dc0e5cd95023e8d4
    role: context
  - path: data/curated/FrequentDirectionsDeterministicMatrixSketching.yaml
    sha256: 926dbb927475a6ce9aba7cab3fcecf188e2aa6cc68f9f3722cb1f7071540fbc8
    role: target
  - path: research/discovery/20261019T072600Z-frequent-directions-deterministic-matrix-sketching.json
    sha256: 91cf78cc6aefa8a061a0a961ca50c9e82283f4ba7d02ddd3b26ea32f3d8270eb
    role: context
  - path: research/discovery/frequent-directions-deterministic-matrix-sketching-boundaries.py
    sha256: a74cf0f6eff3141fb6442f7bba548daad7aa1c3726a9700fed27c8a7c0bbcc81
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
- target_id: AIMech:FrequentDirectionsDeterministicMatrixSketching
  path: data/curated/FrequentDirectionsDeterministicMatrixSketching.yaml
  label: Frequent Directions Deterministic Row-Update Matrix Sketching via Singular-Value
    Shrinkage
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FrequentDirectionsDeterministicMatrixSketching.yaml
    role: maintained
scope:
  description: All fields of data/curated/FrequentDirectionsDeterministicMatrixSketching.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:FrequentDirectionsDeterministicMatrixSketching'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:FrequentDirectionsDeterministicMatrixSketching
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
  - AIMech:FrequentDirectionsDeterministicMatrixSketching
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:FrequentDirectionsDeterministicMatrixSketching
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:FrequentDirectionsDeterministicMatrixSketching
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:FrequentDirectionsDeterministicMatrixSketching
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 frequent-directions-deterministic-matrix-sketching-boundaries.py
  command: python3 research/discovery/frequent-directions-deterministic-matrix-sketching-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:FrequentDirectionsDeterministicMatrixSketching
  exit_code: 0
  expected_exit_code: 0
  summary: '[PASS] Round 363 Frequent Directions (Ghashami et al. 2016): prop1_min=2.87e+00,
    Delta=12.3685<=14.9785, prop3_err=1.49e-13, merge_err=7.82e-14, adv_cov_fd=4.0000<<inc=32.4000'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T072600Z-frequent-directions-deterministic-matrix-sketching.json
  accessed_at: '2026-10-19T07:26:00Z'
  support: supports
  summary: No normalized identity match for AIMech:FrequentDirectionsDeterministicMatrixSketching
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T07:26:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/frequent-directions-deterministic-matrix-sketching-boundaries.py
  accessed_at: '2026-10-19T07:26:00Z'
  snapshot_sha256: a74cf0f6eff3141fb6442f7bba548daad7aa1c3726a9700fed27c8a7c0bbcc81
  support: supports
  summary: 'All constructed boundary assertions in frequent-directions-deterministic-matrix-sketching-boundaries.py
    passed with exit code 0: [PASS] Round 363 Frequent Directions (Ghashami et al.
    2016): prop1_min=2.87e+00, Delta=12.3685<=14.9785, prop3_err=1.49e-13, merge_err=7.82e-14,
    adv_cov_fd=4.0000<<inc=32.4000'
- evidence_id: r363-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/1501.01711.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T07:26:00Z'
  snapshot_sha256: 8c4a9578f1924787b8d9ea10f4537973423b8b67d7089c0101506bb69cf2d263
  support: supports
  summary: Full-text PDF (SIAM Journal on Computing 45(5):1762-1792 (arXiv:1501.01711)
    (2016)) read and verified.
- evidence_id: r363-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1501.01711
  locator: arXiv abstract
  accessed_at: '2026-10-19T07:26:00Z'
  snapshot_sha256: a203efbfa173ca6e738285f5c9359cf8a3da142094a3fd7aeaa842f6349a0d38
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r363-metadata-cr
  kind: primary_source
  reference: https://api.crossref.org/works/10.1137/15m1009718
  locator: Crossref metadata
  accessed_at: '2026-10-19T07:26:00Z'
  snapshot_sha256: cefaa27b99c66b5f0217932ed220b939a5c82afa22d05b6f2f5e002306c9b119
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:FrequentDirectionsDeterministicMatrixSketching
  evidence_ids:
  - identity
  - r363-primary-pdf
  - r363-arxiv-abs
  - r363-metadata-cr
  summary: Frequent Directions Deterministic Row-Update Matrix Sketching via Singular-Value
    Shrinkage is a distinct concept.
  details: Distinct from AIMech:FrequentDirectionsDeterministicStreamingMatrixSketching
    (Round 330, Liberty KDD 2013), which established only the flat-spectrum Frobenius
    covariance error bound ||A^T A - B^T B||_2 <= 2||A||_F^2/ell without rank-k tail
    residuals or relative-error projection bounds; this record captures Ghashami,
    Liberty, Phillips, and Woodruff's (2015, 2016) tail-residual relative-error covariance
    and rank-k projection analysis (||A^T A - B^T B||_2 <= ||A - A_k||_F^2/(ell -
    k), ||A - pi_B^k(A)||_F^2 <= (ell/(ell - k))||A - A_k||_F^2) and matching Grassmannian/Index
    space-optimality lower bounds. Also distinct from AIMech:NoisyPowerMethodForStreamingAndDifferentiallyPrivatePCA
    (Round 356) and AIMech:StreamingPCANearOptimalFiniteSampleOjaAlgorithm (Round
    357), which are randomized iterative subspace estimators rather than deterministic
    Misra-Gries-style singular-value shrinkage sketches.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:FrequentDirectionsDeterministicMatrixSketching
  evidence_ids:
  - mapping
  - r363-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:FrequentDirectionsDeterministicMatrixSketching
  evidence_ids:
  - r363-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in frequent-directions-deterministic-matrix-sketching-boundaries.py
    passed with exit code 0: [PASS] Round 363 Frequent Directions (Ghashami et al.
    2016): prop1_min=2.87e+00, Delta=12.3685<=14.9785, prop3_err=1.49e-13, merge_err=7.82e-14,
    adv_cov_fd=4.0000<<inc=32.4000'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:FrequentDirectionsDeterministicMatrixSketching
  evidence_ids:
  - identity
  - mapping
  - r363-primary-pdf
  - r363-arxiv-abs
  - r363-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:FrequentDirectionsDeterministicMatrixSketching in Round
  363.
- All pages of SIAM Journal on Computing 45(5):1762-1792 (arXiv:1501.01711) (2016)
  were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
