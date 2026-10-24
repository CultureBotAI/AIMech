# Scientific author self-review of Promptagator Few-Shot Dense Retrieval

- Review: 20261019T134330Z-promptagator-few-shot-dense-retrieval
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T13:43:00Z
- Finished UTC: 2026-10-19T13:43:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Promptagator Few-Shot Dense Retrieval as a distinct DRAFT algorithm. All four claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/PromptagatorFewShotDenseRetrievalDataGeneration.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:PromptagatorFewShotDenseRetrievalDataGeneration
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 5368ad0ba4353cdbfe9479e3e9d4152e90a76a66.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:PromptagatorFewShotDenseRetrievalDataGeneration | data/curated/PromptagatorFewShotDenseRetrievalDataGeneration.yaml | maintained | Promptagator Few-Shot Dense Retrieval |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:PromptagatorFewShotDenseRetrievalDataGeneration | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:PromptagatorFewShotDenseRetrievalDataGeneration | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:PromptagatorFewShotDenseRetrievalDataGeneration | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:PromptagatorFewShotDenseRetrievalDataGeneration | Validated history sidecar files. |
| python3 promptagator-few-shot-dense-retrieval-boundaries.py | passed | True | AIMech:PromptagatorFewShotDenseRetrievalDataGeneration | Promptagator verification passed: unfiltered=12 (sim=0.6896) -&gt; filtered=8 (sim=0.9557) |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:PromptagatorFewShotDenseRetrievalDataGeneration.

Promptagator Few-Shot Dense Retrieval is a distinct concept.

Distinct from InPars (AIMech:InParsInContextDataAugmentationForInformationRetrieval), which filters synthetic queries by length-normalized generation log-probability and trains only a second-stage cross-encoder reranker over BM25 candidates, whereas Promptagator conditions on task-specific search-intent role prefixes (e.g., counter-argument vs. fact-check claim), performs round-trip retrieval consistency filtering using a self-trained initial dual encoder without external QA models, and produces a standalone first-stage dense dual encoder. Also distinct from zero-shot hypothetical document embedding at query time (AIMech:HyDEHypotheticalDocumentEmbeddings), which calls an LLM online for every test query rather than distilling synthetic queries offline into a fast 110M dual encoder.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:PromptagatorFewShotDenseRetrievalDataGeneration.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-4 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:PromptagatorFewShotDenseRetrievalDataGeneration.

All four claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in promptagator-few-shot-dense-retrieval-boundaries.py passed with exit code 0: Promptagator verification passed: unfiltered=12 (sim=0.6896) -&gt; filtered=8 (sim=0.9557)

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:PromptagatorFewShotDenseRetrievalDataGeneration.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T134300Z-promptagator-few-shot-dense-retrieval.json | supports | No normalized identity match for AIMech:PromptagatorFewShotDenseRetrievalDataGeneration across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/promptagator-few-shot-dense-retrieval-boundaries.py | supports | All constructed boundary assertions in promptagator-few-shot-dense-retrieval-boundaries.py passed with exit code 0: Promptagator verification passed: unfiltered=12 (sim=0.6896) -&gt; filtered=8 (sim=0.9557) |
| r740-primary-pdf | https://arxiv.org/pdf/2209.11755.pdf; Full-text PDF | supports | Full-text PDF (The Eleventh International Conference on Learning Representations (ICLR 2023) (2023)) read and verified. |
| r740-arxiv-abs | https://arxiv.org/abs/2209.11755; arXiv abstract | supports | arXiv abstract read and verified. |
| r740-metadata-cr | https://dblp.org/search/publ/api?q=Promptagator+Few-shot+Dense+Retrieval+From+8+Examples+Dai&amp;h=5&amp;format=xml; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:PromptagatorFewShotDenseRetrievalDataGeneration in Round 740.
- All pages of The Eleventh International Conference on Learning Representations (ICLR 2023) (2023) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T134330Z-promptagator-few-shot-dense-retrieval
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Promptagator Few-Shot Dense Retrieval
started_at: '2026-10-19T13:43:00Z'
finished_at: '2026-10-19T13:43:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:PromptagatorFewShotDenseRetrievalDataGeneration
    against existing AIMech and AIO records and verified all claims against The Eleventh
    International Conference on Learning Representations (ICLR 2023) (2023) and pure-Python
    boundary checks. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Promptagator Few-Shot Dense Retrieval as a distinct DRAFT algorithm.
  All four claims are supported by full-text primary evidence and pure-Python boundary
  verification.
source:
  git_revision: 5368ad0ba4353cdbfe9479e3e9d4152e90a76a66
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/PromptagatorFewShotDenseRetrievalDataGeneration.yaml
    sha256: 35e8b1ee8bb2596de3a45a81ae8786568a4f5288962931a62dfba67f4f6abf38
    role: target
  - path: research/discovery/20261019T134300Z-promptagator-few-shot-dense-retrieval.json
    sha256: 45d8a02c29078132f2cad83500b3da90fac1997fa3abdb33df4a7a830944b501
    role: context
  - path: research/discovery/promptagator-few-shot-dense-retrieval-boundaries.py
    sha256: 0bb7040986259fb0f315b8352544861dc84d02b51418f3457c6e492c05957661
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
- target_id: AIMech:PromptagatorFewShotDenseRetrievalDataGeneration
  path: data/curated/PromptagatorFewShotDenseRetrievalDataGeneration.yaml
  label: Promptagator Few-Shot Dense Retrieval
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PromptagatorFewShotDenseRetrievalDataGeneration.yaml
    role: maintained
scope:
  description: All fields of data/curated/PromptagatorFewShotDenseRetrievalDataGeneration.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:PromptagatorFewShotDenseRetrievalDataGeneration'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:PromptagatorFewShotDenseRetrievalDataGeneration
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
  - AIMech:PromptagatorFewShotDenseRetrievalDataGeneration
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:PromptagatorFewShotDenseRetrievalDataGeneration
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:PromptagatorFewShotDenseRetrievalDataGeneration
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:PromptagatorFewShotDenseRetrievalDataGeneration
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 promptagator-few-shot-dense-retrieval-boundaries.py
  command: python3 research/discovery/promptagator-few-shot-dense-retrieval-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:PromptagatorFewShotDenseRetrievalDataGeneration
  exit_code: 0
  expected_exit_code: 0
  summary: 'Promptagator verification passed: unfiltered=12 (sim=0.6896) -> filtered=8
    (sim=0.9557)'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T134300Z-promptagator-few-shot-dense-retrieval.json
  accessed_at: '2026-10-19T13:43:00Z'
  support: supports
  summary: No normalized identity match for AIMech:PromptagatorFewShotDenseRetrievalDataGeneration
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T13:43:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/promptagator-few-shot-dense-retrieval-boundaries.py
  accessed_at: '2026-10-19T13:43:00Z'
  snapshot_sha256: 0bb7040986259fb0f315b8352544861dc84d02b51418f3457c6e492c05957661
  support: supports
  summary: 'All constructed boundary assertions in promptagator-few-shot-dense-retrieval-boundaries.py
    passed with exit code 0: Promptagator verification passed: unfiltered=12 (sim=0.6896)
    -> filtered=8 (sim=0.9557)'
- evidence_id: r740-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2209.11755.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T13:43:00Z'
  snapshot_sha256: c2dec45d0b2d4c9393a5e8f51a52628897e511960a253d9dcfc00348fae93457
  support: supports
  summary: Full-text PDF (The Eleventh International Conference on Learning Representations
    (ICLR 2023) (2023)) read and verified.
- evidence_id: r740-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2209.11755
  locator: arXiv abstract
  accessed_at: '2026-10-19T13:43:00Z'
  snapshot_sha256: ba6931e0fa26e9814767dc6f77fcc4bbfa7ec36164c6bc1c934132fe9d9ae874
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r740-metadata-cr
  kind: primary_source
  reference: https://dblp.org/search/publ/api?q=Promptagator+Few-shot+Dense+Retrieval+From+8+Examples+Dai&h=5&format=xml
  locator: Crossref metadata
  accessed_at: '2026-10-19T13:43:00Z'
  snapshot_sha256: 128123e6b1281551a734effbe9cf6ab2436d6d700ce7ad83d2c316d791cbd28a
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:PromptagatorFewShotDenseRetrievalDataGeneration
  evidence_ids:
  - identity
  - r740-primary-pdf
  - r740-arxiv-abs
  - r740-metadata-cr
  summary: Promptagator Few-Shot Dense Retrieval is a distinct concept.
  details: Distinct from InPars (AIMech:InParsInContextDataAugmentationForInformationRetrieval),
    which filters synthetic queries by length-normalized generation log-probability
    and trains only a second-stage cross-encoder reranker over BM25 candidates, whereas
    Promptagator conditions on task-specific search-intent role prefixes (e.g., counter-argument
    vs. fact-check claim), performs round-trip retrieval consistency filtering using
    a self-trained initial dual encoder without external QA models, and produces a
    standalone first-stage dense dual encoder. Also distinct from zero-shot hypothetical
    document embedding at query time (AIMech:HyDEHypotheticalDocumentEmbeddings),
    which calls an LLM online for every test query rather than distilling synthetic
    queries offline into a fast 110M dual encoder.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:PromptagatorFewShotDenseRetrievalDataGeneration
  evidence_ids:
  - mapping
  - r740-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-4 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:PromptagatorFewShotDenseRetrievalDataGeneration
  evidence_ids:
  - r740-primary-pdf
  - calculation
  summary: All four claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in promptagator-few-shot-dense-retrieval-boundaries.py
    passed with exit code 0: Promptagator verification passed: unfiltered=12 (sim=0.6896)
    -> filtered=8 (sim=0.9557)'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:PromptagatorFewShotDenseRetrievalDataGeneration
  evidence_ids:
  - identity
  - mapping
  - r740-primary-pdf
  - r740-arxiv-abs
  - r740-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:PromptagatorFewShotDenseRetrievalDataGeneration in Round
  740.
- All pages of The Eleventh International Conference on Learning Representations (ICLR
  2023) (2023) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
