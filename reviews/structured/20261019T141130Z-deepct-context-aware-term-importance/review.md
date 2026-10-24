# Scientific author self-review of DeepCT Deep Contextualized Term Weighting for First-Stage Retrieval

- Review: 20261019T141130Z-deepct-context-aware-term-importance
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T14:11:00Z
- Finished UTC: 2026-10-19T14:11:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain DeepCT Deep Contextualized Term Weighting for First-Stage Retrieval as a distinct DRAFT algorithm. All four claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b991589c6de9f44e0d31623e1273695fc69b40ba.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval | data/curated/DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval.yaml | maintained | DeepCT Deep Contextualized Term Weighting for First-Stage Retrieval |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval | Validated history sidecar files. |
| python3 deepct-context-aware-term-importance-boundaries.py | passed | True | AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval | [PASS] DeepCT boundaries verified: QTR(stomach,d1)=1.00, TF_DeepCT(p1)=78 &gt; TF_DeepCT(p2)=6, BM25_DeepCT(p1)=5.4167 &gt; BM25_DeepCT(p2)=4.5833 |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval.

DeepCT Deep Contextualized Term Weighting for First-Stage Retrieval is a distinct concept.

Distinct from SPLADE (AIMech:SPLADESparseLexicalAndExpansionModel), which projects over the entire MLM vocabulary to perform term expansion and trains end-to-end with contrastive ranking and FLOPS regularization; and distinct from COIL (AIMech:COILContextualizedInvertedList), which stores multi-dimensional contextualized vectors per token in inverted lists rather than scalar integer pseudo-frequencies TF_DeepCT(t, d) compatible with unmodified BM25 and Query Likelihood inverted indexes.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-4 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval.

All four claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in deepct-context-aware-term-importance-boundaries.py passed with exit code 0: [PASS] DeepCT boundaries verified: QTR(stomach,d1)=1.00, TF_DeepCT(p1)=78 &gt; TF_DeepCT(p2)=6, BM25_DeepCT(p1)=5.4167 &gt; BM25_DeepCT(p2)=4.5833

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T141100Z-deepct-context-aware-term-importance.json | supports | No normalized identity match for AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/deepct-context-aware-term-importance-boundaries.py | supports | All constructed boundary assertions in deepct-context-aware-term-importance-boundaries.py passed with exit code 0: [PASS] DeepCT boundaries verified: QTR(stomach,d1)=1.00, TF_DeepCT(p1)=78 &gt; TF_DeepCT(p2)=6, BM25_DeepCT(p1)=5.4167 &gt; BM25_DeepCT(p2)=4.5833 |
| r768-primary-pdf | https://arxiv.org/pdf/1910.10687; Full-text PDF | supports | Full-text PDF (arXiv (cs.IR) (2019)) read and verified. |
| r768-arxiv-abs | https://arxiv.org/abs/1910.10687; arXiv abstract | supports | arXiv abstract read and verified. |
| r768-metadata-cr | https://arxiv.org/bibtex/1910.10687; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval in Round 768.
- All pages of arXiv (cs.IR) (2019) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T141130Z-deepct-context-aware-term-importance
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of DeepCT Deep Contextualized Term Weighting
  for First-Stage Retrieval
started_at: '2026-10-19T14:11:00Z'
finished_at: '2026-10-19T14:11:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval
    against existing AIMech and AIO records and verified all claims against arXiv
    (cs.IR) (2019) and pure-Python boundary checks. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain DeepCT Deep Contextualized Term Weighting for First-Stage Retrieval
  as a distinct DRAFT algorithm. All four claims are supported by full-text primary
  evidence and pure-Python boundary verification.
source:
  git_revision: b991589c6de9f44e0d31623e1273695fc69b40ba
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval.yaml
    sha256: 485481fc2b523a401985c32d93a0345de7457d02a545c54bc7dddbf1e3be537b
    role: target
  - path: research/discovery/20261019T141100Z-deepct-context-aware-term-importance.json
    sha256: 8fa6a7819ea158d5f2997c0c20caed6888f38639ad651b54a329c2ded28c9b07
    role: context
  - path: research/discovery/deepct-context-aware-term-importance-boundaries.py
    sha256: f348a0c3230b724638aa5d22f3dca7658cbf13a7e164e086a2a94ff8123f96a7
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
- target_id: AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval
  path: data/curated/DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval.yaml
  label: DeepCT Deep Contextualized Term Weighting for First-Stage Retrieval
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval.yaml
    role: maintained
scope:
  description: All fields of data/curated/DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval
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
  - AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 deepct-context-aware-term-importance-boundaries.py
  command: python3 research/discovery/deepct-context-aware-term-importance-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval
  exit_code: 0
  expected_exit_code: 0
  summary: '[PASS] DeepCT boundaries verified: QTR(stomach,d1)=1.00, TF_DeepCT(p1)=78
    > TF_DeepCT(p2)=6, BM25_DeepCT(p1)=5.4167 > BM25_DeepCT(p2)=4.5833'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T141100Z-deepct-context-aware-term-importance.json
  accessed_at: '2026-10-19T14:11:00Z'
  support: supports
  summary: No normalized identity match for AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T14:11:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/deepct-context-aware-term-importance-boundaries.py
  accessed_at: '2026-10-19T14:11:00Z'
  snapshot_sha256: f348a0c3230b724638aa5d22f3dca7658cbf13a7e164e086a2a94ff8123f96a7
  support: supports
  summary: 'All constructed boundary assertions in deepct-context-aware-term-importance-boundaries.py
    passed with exit code 0: [PASS] DeepCT boundaries verified: QTR(stomach,d1)=1.00,
    TF_DeepCT(p1)=78 > TF_DeepCT(p2)=6, BM25_DeepCT(p1)=5.4167 > BM25_DeepCT(p2)=4.5833'
- evidence_id: r768-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/1910.10687
  locator: Full-text PDF
  accessed_at: '2026-10-19T14:11:00Z'
  snapshot_sha256: 29ba94d6129934734f1d810aebd5a436e59a33d38f7e08cddd7fc77d41d9b2b6
  support: supports
  summary: Full-text PDF (arXiv (cs.IR) (2019)) read and verified.
- evidence_id: r768-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1910.10687
  locator: arXiv abstract
  accessed_at: '2026-10-19T14:11:00Z'
  snapshot_sha256: 9f48a51548d597926b00838ec4e8ba1be265e8bd14d3a9a08a1253ebe9709975
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r768-metadata-cr
  kind: primary_source
  reference: https://arxiv.org/bibtex/1910.10687
  locator: Crossref metadata
  accessed_at: '2026-10-19T14:11:00Z'
  snapshot_sha256: 2ca42cdc5b25420e10575a79549801590cda7cbd372aa9b42a03f46d1eb438e2
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval
  evidence_ids:
  - identity
  - r768-primary-pdf
  - r768-arxiv-abs
  - r768-metadata-cr
  summary: DeepCT Deep Contextualized Term Weighting for First-Stage Retrieval is
    a distinct concept.
  details: Distinct from SPLADE (AIMech:SPLADESparseLexicalAndExpansionModel), which
    projects over the entire MLM vocabulary to perform term expansion and trains end-to-end
    with contrastive ranking and FLOPS regularization; and distinct from COIL (AIMech:COILContextualizedInvertedList),
    which stores multi-dimensional contextualized vectors per token in inverted lists
    rather than scalar integer pseudo-frequencies TF_DeepCT(t, d) compatible with
    unmodified BM25 and Query Likelihood inverted indexes.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval
  evidence_ids:
  - mapping
  - r768-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-4 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval
  evidence_ids:
  - r768-primary-pdf
  - calculation
  summary: All four claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in deepct-context-aware-term-importance-boundaries.py
    passed with exit code 0: [PASS] DeepCT boundaries verified: QTR(stomach,d1)=1.00,
    TF_DeepCT(p1)=78 > TF_DeepCT(p2)=6, BM25_DeepCT(p1)=5.4167 > BM25_DeepCT(p2)=4.5833'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval
  evidence_ids:
  - identity
  - mapping
  - r768-primary-pdf
  - r768-arxiv-abs
  - r768-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval
  in Round 768.
- All pages of arXiv (cs.IR) (2019) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
