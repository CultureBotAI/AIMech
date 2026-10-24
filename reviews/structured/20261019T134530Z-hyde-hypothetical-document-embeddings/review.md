# Scientific author self-review of HyDE Hypothetical Document Embeddings

- Review: 20261019T134530Z-hyde-hypothetical-document-embeddings
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T13:45:00Z
- Finished UTC: 2026-10-19T13:45:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain HyDE Hypothetical Document Embeddings as a distinct DRAFT algorithm. All four claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/HyDEHypotheticalDocumentEmbeddings.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:HyDEHypotheticalDocumentEmbeddings
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 437962b4a9a2284242b6e6c46df05c3c20e8fc64.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:HyDEHypotheticalDocumentEmbeddings | data/curated/HyDEHypotheticalDocumentEmbeddings.yaml | maintained | HyDE Hypothetical Document Embeddings |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:HyDEHypotheticalDocumentEmbeddings | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:HyDEHypotheticalDocumentEmbeddings | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:HyDEHypotheticalDocumentEmbeddings | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:HyDEHypotheticalDocumentEmbeddings | Validated history sidecar files. |
| python3 hyde-hypothetical-document-embeddings-boundaries.py | passed | True | AIMech:HyDEHypotheticalDocumentEmbeddings | HyDE verification passed: raw_margin=-0.3771 -&gt; hyde_margin=0.3170, hyde8_scores=[0.7954, 0.4784, 0.2244] |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:HyDEHypotheticalDocumentEmbeddings.

HyDE Hypothetical Document Embeddings is a distinct concept.

Distinct from document-to-query data augmentation methods such as Promptagator (AIMech:PromptagatorFewShotDenseRetrievalDataGeneration) and InPars (AIMech:InParsInContextDataAugmentationForInformationRetrieval), which generate synthetic queries from real documents offline to train retrievers or rerankers, whereas HyDE requires no model training or corpus access beforehand and instead translates each incoming query online into hypothetical documents so that retrieval occurs purely in an unsupervised document-document contrastive embedding space.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:HyDEHypotheticalDocumentEmbeddings.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-4 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:HyDEHypotheticalDocumentEmbeddings.

All four claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in hyde-hypothetical-document-embeddings-boundaries.py passed with exit code 0: HyDE verification passed: raw_margin=-0.3771 -&gt; hyde_margin=0.3170, hyde8_scores=[0.7954, 0.4784, 0.2244]

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:HyDEHypotheticalDocumentEmbeddings.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T134500Z-hyde-hypothetical-document-embeddings.json | supports | No normalized identity match for AIMech:HyDEHypotheticalDocumentEmbeddings across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/hyde-hypothetical-document-embeddings-boundaries.py | supports | All constructed boundary assertions in hyde-hypothetical-document-embeddings-boundaries.py passed with exit code 0: HyDE verification passed: raw_margin=-0.3771 -&gt; hyde_margin=0.3170, hyde8_scores=[0.7954, 0.4784, 0.2244] |
| r742-primary-pdf | https://arxiv.org/pdf/2212.10496.pdf; Full-text PDF | supports | Full-text PDF (Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) (ACL 2023) (2023)) read and verified. |
| r742-arxiv-abs | https://arxiv.org/abs/2212.10496; arXiv abstract | supports | arXiv abstract read and verified. |
| r742-metadata-cr | https://dblp.org/search/publ/api?q=Precise+Zero-Shot+Dense+Retrieval+without+Relevance+Labels+Gao&amp;h=5&amp;format=xml; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:HyDEHypotheticalDocumentEmbeddings in Round 742.
- All pages of Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) (ACL 2023) (2023) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T134530Z-hyde-hypothetical-document-embeddings
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of HyDE Hypothetical Document Embeddings
started_at: '2026-10-19T13:45:00Z'
finished_at: '2026-10-19T13:45:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: 'The author challenged definition distinctness of AIMech:HyDEHypotheticalDocumentEmbeddings
    against existing AIMech and AIO records and verified all claims against Proceedings
    of the 61st Annual Meeting of the Association for Computational Linguistics (Volume
    1: Long Papers) (ACL 2023) (2023) and pure-Python boundary checks. This is adversarial
    author self-review, not independent approval.'
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain HyDE Hypothetical Document Embeddings as a distinct DRAFT algorithm.
  All four claims are supported by full-text primary evidence and pure-Python boundary
  verification.
source:
  git_revision: 437962b4a9a2284242b6e6c46df05c3c20e8fc64
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/HyDEHypotheticalDocumentEmbeddings.yaml
    sha256: ee279b15c55fadfa7893ce2abecd12a2d428a65fbb386ca454eef5d01976d547
    role: target
  - path: research/discovery/20261019T134500Z-hyde-hypothetical-document-embeddings.json
    sha256: 4a46d50a7584cdfba4c2e9cf5b499c7abcc2a197fa9600a6814fc1bef84e6676
    role: context
  - path: research/discovery/hyde-hypothetical-document-embeddings-boundaries.py
    sha256: c6bc1908267dc2f18751c0b450ae4a2653572e33ed6c2d0fd38b7c623fd70807
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
- target_id: AIMech:HyDEHypotheticalDocumentEmbeddings
  path: data/curated/HyDEHypotheticalDocumentEmbeddings.yaml
  label: HyDE Hypothetical Document Embeddings
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HyDEHypotheticalDocumentEmbeddings.yaml
    role: maintained
scope:
  description: All fields of data/curated/HyDEHypotheticalDocumentEmbeddings.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:HyDEHypotheticalDocumentEmbeddings'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:HyDEHypotheticalDocumentEmbeddings
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
  - AIMech:HyDEHypotheticalDocumentEmbeddings
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:HyDEHypotheticalDocumentEmbeddings
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:HyDEHypotheticalDocumentEmbeddings
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:HyDEHypotheticalDocumentEmbeddings
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 hyde-hypothetical-document-embeddings-boundaries.py
  command: python3 research/discovery/hyde-hypothetical-document-embeddings-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:HyDEHypotheticalDocumentEmbeddings
  exit_code: 0
  expected_exit_code: 0
  summary: 'HyDE verification passed: raw_margin=-0.3771 -> hyde_margin=0.3170, hyde8_scores=[0.7954,
    0.4784, 0.2244]'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T134500Z-hyde-hypothetical-document-embeddings.json
  accessed_at: '2026-10-19T13:45:00Z'
  support: supports
  summary: No normalized identity match for AIMech:HyDEHypotheticalDocumentEmbeddings
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T13:45:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/hyde-hypothetical-document-embeddings-boundaries.py
  accessed_at: '2026-10-19T13:45:00Z'
  snapshot_sha256: c6bc1908267dc2f18751c0b450ae4a2653572e33ed6c2d0fd38b7c623fd70807
  support: supports
  summary: 'All constructed boundary assertions in hyde-hypothetical-document-embeddings-boundaries.py
    passed with exit code 0: HyDE verification passed: raw_margin=-0.3771 -> hyde_margin=0.3170,
    hyde8_scores=[0.7954, 0.4784, 0.2244]'
- evidence_id: r742-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2212.10496.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T13:45:00Z'
  snapshot_sha256: dc0ae3c5584ed146beee122e6a9ad9c48547dde048d53e9be8435d8f1d354531
  support: supports
  summary: 'Full-text PDF (Proceedings of the 61st Annual Meeting of the Association
    for Computational Linguistics (Volume 1: Long Papers) (ACL 2023) (2023)) read
    and verified.'
- evidence_id: r742-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2212.10496
  locator: arXiv abstract
  accessed_at: '2026-10-19T13:45:00Z'
  snapshot_sha256: 52600703c77c08137c7f7346ed194d2158358b6c14d7f52c74bfb4a5edfcb275
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r742-metadata-cr
  kind: primary_source
  reference: https://dblp.org/search/publ/api?q=Precise+Zero-Shot+Dense+Retrieval+without+Relevance+Labels+Gao&h=5&format=xml
  locator: Crossref metadata
  accessed_at: '2026-10-19T13:45:00Z'
  snapshot_sha256: be5331ed507741d427296cd261c0b15d33616d2140b85e9da1d735e46ec20385
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:HyDEHypotheticalDocumentEmbeddings
  evidence_ids:
  - identity
  - r742-primary-pdf
  - r742-arxiv-abs
  - r742-metadata-cr
  summary: HyDE Hypothetical Document Embeddings is a distinct concept.
  details: Distinct from document-to-query data augmentation methods such as Promptagator
    (AIMech:PromptagatorFewShotDenseRetrievalDataGeneration) and InPars (AIMech:InParsInContextDataAugmentationForInformationRetrieval),
    which generate synthetic queries from real documents offline to train retrievers
    or rerankers, whereas HyDE requires no model training or corpus access beforehand
    and instead translates each incoming query online into hypothetical documents
    so that retrieval occurs purely in an unsupervised document-document contrastive
    embedding space.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:HyDEHypotheticalDocumentEmbeddings
  evidence_ids:
  - mapping
  - r742-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-4 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:HyDEHypotheticalDocumentEmbeddings
  evidence_ids:
  - r742-primary-pdf
  - calculation
  summary: All four claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in hyde-hypothetical-document-embeddings-boundaries.py
    passed with exit code 0: HyDE verification passed: raw_margin=-0.3771 -> hyde_margin=0.3170,
    hyde8_scores=[0.7954, 0.4784, 0.2244]'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:HyDEHypotheticalDocumentEmbeddings
  evidence_ids:
  - identity
  - mapping
  - r742-primary-pdf
  - r742-arxiv-abs
  - r742-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:HyDEHypotheticalDocumentEmbeddings in Round 742.
- 'All pages of Proceedings of the 61st Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers) (ACL 2023) (2023) were read in full text.'
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
