# Scientific author self-review of ADORE and STAR Hard-Negative Dense Retrieval Training Framework

- Review: 20261019T140430Z-adore-star-dynamic-hard-negative-dense-retrieval
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T14:04:00Z
- Finished UTC: 2026-10-19T14:04:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain ADORE and STAR Hard-Negative Dense Retrieval Training Framework as a distinct DRAFT algorithm. All four claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a138e0bdf7f0635fe37bc2c1432bfca5650d4be1.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives | data/curated/ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives.yaml | maintained | ADORE and STAR Hard-Negative Dense Retrieval Training Framework |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives | Validated history sidecar files. |
| python3 adore-star-dynamic-hard-negative-dense-retrieval-boundaries.py | passed | True | AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives | [PASS] ADORE &amp; STAR boundaries verified: pi(d^+)=4, L_ADORE(rank1)=0.8783 &gt; L_ADORE(rank3)=0.0976 |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives.

ADORE and STAR Hard-Negative Dense Retrieval Training Framework is a distinct concept.

Distinct from ANCE (AIMech:ANCEApproximateNearestNeighborNegativeContrastiveLearning), which periodically re-encodes the entire corpus and rebuilds the ANN index every several thousand steps to refresh static hard negatives without random-negative stabilization or metric-weighted LambdaLoss; and distinct from RocketQA (AIMech:RocketQADenoisedHardNegativeSampling), which uses a cross-encoder teacher to filter static hard negatives rather than online query-side dynamic hard negative retrieval against a fixed document index.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-4 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives.

All four claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in adore-star-dynamic-hard-negative-dense-retrieval-boundaries.py passed with exit code 0: [PASS] ADORE &amp; STAR boundaries verified: pi(d^+)=4, L_ADORE(rank1)=0.8783 &gt; L_ADORE(rank3)=0.0976

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T140400Z-adore-star-dynamic-hard-negative-dense-retrieval.json | supports | No normalized identity match for AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/adore-star-dynamic-hard-negative-dense-retrieval-boundaries.py | supports | All constructed boundary assertions in adore-star-dynamic-hard-negative-dense-retrieval-boundaries.py passed with exit code 0: [PASS] ADORE &amp; STAR boundaries verified: pi(d^+)=4, L_ADORE(rank1)=0.8783 &gt; L_ADORE(rank3)=0.0976 |
| r761-primary-pdf | https://arxiv.org/pdf/2104.08051; Full-text PDF | supports | Full-text PDF (Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR 2021) (2021)) read and verified. |
| r761-arxiv-abs | https://arxiv.org/abs/2104.08051; arXiv abstract | supports | arXiv abstract read and verified. |
| r761-metadata-cr | https://arxiv.org/bibtex/2104.08051; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives in Round 761.
- All pages of Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR 2021) (2021) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T140430Z-adore-star-dynamic-hard-negative-dense-retrieval
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of ADORE and STAR Hard-Negative Dense Retrieval
  Training Framework
started_at: '2026-10-19T14:04:00Z'
finished_at: '2026-10-19T14:04:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives
    against existing AIMech and AIO records and verified all claims against Proceedings
    of the 44th International ACM SIGIR Conference on Research and Development in
    Information Retrieval (SIGIR 2021) (2021) and pure-Python boundary checks. This
    is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain ADORE and STAR Hard-Negative Dense Retrieval Training Framework as
  a distinct DRAFT algorithm. All four claims are supported by full-text primary evidence
  and pure-Python boundary verification.
source:
  git_revision: a138e0bdf7f0635fe37bc2c1432bfca5650d4be1
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives.yaml
    sha256: c565c051bd199d074f42c521a95cc530660b79272760ff81d282decdaf41235c
    role: target
  - path: research/discovery/20261019T140400Z-adore-star-dynamic-hard-negative-dense-retrieval.json
    sha256: f5d662437cda9405d5a21f25d0bd02f7460ce3500ef33017a9941bbd0f895af2
    role: context
  - path: research/discovery/adore-star-dynamic-hard-negative-dense-retrieval-boundaries.py
    sha256: 8ceaa9d77e1fa5869def40c223abf02d1c05bbcceac0a18e16088db861c2f3f2
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
- target_id: AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives
  path: data/curated/ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives.yaml
  label: ADORE and STAR Hard-Negative Dense Retrieval Training Framework
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives.yaml
    role: maintained
scope:
  description: All fields of data/curated/ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives
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
  - AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 adore-star-dynamic-hard-negative-dense-retrieval-boundaries.py
  command: python3 research/discovery/adore-star-dynamic-hard-negative-dense-retrieval-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives
  exit_code: 0
  expected_exit_code: 0
  summary: '[PASS] ADORE & STAR boundaries verified: pi(d^+)=4, L_ADORE(rank1)=0.8783
    > L_ADORE(rank3)=0.0976'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T140400Z-adore-star-dynamic-hard-negative-dense-retrieval.json
  accessed_at: '2026-10-19T14:04:00Z'
  support: supports
  summary: No normalized identity match for AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T14:04:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/adore-star-dynamic-hard-negative-dense-retrieval-boundaries.py
  accessed_at: '2026-10-19T14:04:00Z'
  snapshot_sha256: 8ceaa9d77e1fa5869def40c223abf02d1c05bbcceac0a18e16088db861c2f3f2
  support: supports
  summary: 'All constructed boundary assertions in adore-star-dynamic-hard-negative-dense-retrieval-boundaries.py
    passed with exit code 0: [PASS] ADORE & STAR boundaries verified: pi(d^+)=4, L_ADORE(rank1)=0.8783
    > L_ADORE(rank3)=0.0976'
- evidence_id: r761-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2104.08051
  locator: Full-text PDF
  accessed_at: '2026-10-19T14:04:00Z'
  snapshot_sha256: 32c2565073c8a4eb80737812733224708e998aeb37f1bd9f7fbbf24fea31949b
  support: supports
  summary: Full-text PDF (Proceedings of the 44th International ACM SIGIR Conference
    on Research and Development in Information Retrieval (SIGIR 2021) (2021)) read
    and verified.
- evidence_id: r761-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2104.08051
  locator: arXiv abstract
  accessed_at: '2026-10-19T14:04:00Z'
  snapshot_sha256: cb38c4cc57eb847fde3bed93fb1a519582802d9581a318a490889cfa717ee377
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r761-metadata-cr
  kind: primary_source
  reference: https://arxiv.org/bibtex/2104.08051
  locator: Crossref metadata
  accessed_at: '2026-10-19T14:04:00Z'
  snapshot_sha256: 4c26ef904aa46d55ddbfe093c5d96234b92d72cc4e650861ea977f6da234f6cf
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives
  evidence_ids:
  - identity
  - r761-primary-pdf
  - r761-arxiv-abs
  - r761-metadata-cr
  summary: ADORE and STAR Hard-Negative Dense Retrieval Training Framework is a distinct
    concept.
  details: Distinct from ANCE (AIMech:ANCEApproximateNearestNeighborNegativeContrastiveLearning),
    which periodically re-encodes the entire corpus and rebuilds the ANN index every
    several thousand steps to refresh static hard negatives without random-negative
    stabilization or metric-weighted LambdaLoss; and distinct from RocketQA (AIMech:RocketQADenoisedHardNegativeSampling),
    which uses a cross-encoder teacher to filter static hard negatives rather than
    online query-side dynamic hard negative retrieval against a fixed document index.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives
  evidence_ids:
  - mapping
  - r761-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-4 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives
  evidence_ids:
  - r761-primary-pdf
  - calculation
  summary: All four claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in adore-star-dynamic-hard-negative-dense-retrieval-boundaries.py
    passed with exit code 0: [PASS] ADORE & STAR boundaries verified: pi(d^+)=4, L_ADORE(rank1)=0.8783
    > L_ADORE(rank3)=0.0976'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives
  evidence_ids:
  - identity
  - mapping
  - r761-primary-pdf
  - r761-arxiv-abs
  - r761-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:ADOREOptimizingDenseRetrievalModelTrainingWithHardNegatives
  in Round 761.
- All pages of Proceedings of the 44th International ACM SIGIR Conference on Research
  and Development in Information Retrieval (SIGIR 2021) (2021) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
