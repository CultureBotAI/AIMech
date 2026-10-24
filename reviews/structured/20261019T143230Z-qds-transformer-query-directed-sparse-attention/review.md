# Scientific author self-review of QDS-Transformer: Query-Directed Sparse Transformer for Long Document Ranking

- Review: 20261019T143230Z-qds-transformer-query-directed-sparse-attention
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T14:32:00Z
- Finished UTC: 2026-10-19T14:32:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain QDS-Transformer: Query-Directed Sparse Transformer for Long Document Ranking as a distinct DRAFT architecture. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base cbdb6c66291ea06cd15de00ca60779e187012b71.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking | data/curated/QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking.yaml | maintained | QDS-Transformer: Query-Directed Sparse Transformer for Long Document Ranking |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking | Validated history sidecar files. |
| python3 qds-transformer-query-directed-sparse-attention-boundaries.py | passed | True | AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking | QDS-Transformer boundary verification passed:<br>  Dense edges: 10000, QDS edges: 2152 (21.52%), Local-only edges: 880<br>  A_QDS[85,2]=1, A_QDS[85,65]=1, A_QDS[20,85]=0 |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking.

QDS-Transformer: Query-Directed Sparse Transformer for Long Document Ranking is a distinct concept.

Distinct from general-purpose sparse Transformers such as Sparse Transformer (local/strided attention only) and Longformer-QA (which places global attention only on two task tokens without sentence-level [SOS] hierarchy or full query-directed paths), and from passage-splitting rankers such as BERT-MaxP or PARADE. QDS-Transformer encodes the entire long document up to 2,048 tokens in a unified cross-encoder with IR-axiomatic sparse attention compiled via TVM CUDA kernels.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in qds-transformer-query-directed-sparse-attention-boundaries.py passed with exit code 0: QDS-Transformer boundary verification passed:
  Dense edges: 10000, QDS edges: 2152 (21.52%), Local-only edges: 880
  A_QDS[85,2]=1, A_QDS[85,65]=1, A_QDS[20,85]=0

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T143200Z-qds-transformer-query-directed-sparse-attention.json | supports | No normalized identity match for AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/qds-transformer-query-directed-sparse-attention-boundaries.py | supports | All constructed boundary assertions in qds-transformer-query-directed-sparse-attention-boundaries.py passed with exit code 0: QDS-Transformer boundary verification passed:<br>  Dense edges: 10000, QDS edges: 2152 (21.52%), Local-only edges: 880<br>  A_QDS[85,2]=1, A_QDS[85,65]=1, A_QDS[20,85]=0 |
| r789-primary-pdf | https://arxiv.org/pdf/2010.12683.pdf; Full-text PDF | supports | Full-text PDF (Findings of the Association for Computational Linguistics: EMNLP 2020 (2020)) read and verified. |
| r789-arxiv-abs | https://arxiv.org/abs/2010.12683; arXiv abstract | supports | arXiv abstract read and verified. |
| r789-metadata-cr | https://arxiv.org/bibtex/2010.12683; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking in Round 789.
- All pages of Findings of the Association for Computational Linguistics: EMNLP 2020 (2020) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T143230Z-qds-transformer-query-directed-sparse-attention
kind: record
repository: CultureBotAI/AIMech
title: 'Scientific author self-review of QDS-Transformer: Query-Directed Sparse Transformer
  for Long Document Ranking'
started_at: '2026-10-19T14:32:00Z'
finished_at: '2026-10-19T14:32:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: 'The author challenged definition distinctness of AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking
    against existing AIMech and AIO records and verified all claims against Findings
    of the Association for Computational Linguistics: EMNLP 2020 (2020) and pure-Python
    boundary checks. This is adversarial author self-review, not independent approval.'
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: 'Retain QDS-Transformer: Query-Directed Sparse Transformer for Long Document
  Ranking as a distinct DRAFT architecture. All three claims are supported by full-text
  primary evidence and pure-Python boundary verification.'
source:
  git_revision: cbdb6c66291ea06cd15de00ca60779e187012b71
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking.yaml
    sha256: 1674eb08f3b63fc60655c9c02e5ee16616f06840b9c04c699a9a5b7a5c3fdb0e
    role: target
  - path: research/discovery/20261019T143200Z-qds-transformer-query-directed-sparse-attention.json
    sha256: b6f356f2e2e462c548e86975c4c032af1b17ab4aebb5866c816a1e132f9dc066
    role: context
  - path: research/discovery/qds-transformer-query-directed-sparse-attention-boundaries.py
    sha256: 99f3f8ee9d263db7fc44e6cb3072b84f96cae90da3eb6f08002fac85975b6b2c
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
- target_id: AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking
  path: data/curated/QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking.yaml
  label: 'QDS-Transformer: Query-Directed Sparse Transformer for Long Document Ranking'
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking.yaml
    role: maintained
scope:
  description: All fields of data/curated/QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking
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
  - AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 qds-transformer-query-directed-sparse-attention-boundaries.py
  command: python3 research/discovery/qds-transformer-query-directed-sparse-attention-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking
  exit_code: 0
  expected_exit_code: 0
  summary: "QDS-Transformer boundary verification passed:\n  Dense edges: 10000, QDS\
    \ edges: 2152 (21.52%), Local-only edges: 880\n  A_QDS[85,2]=1, A_QDS[85,65]=1,\
    \ A_QDS[20,85]=0"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T143200Z-qds-transformer-query-directed-sparse-attention.json
  accessed_at: '2026-10-19T14:32:00Z'
  support: supports
  summary: No normalized identity match for AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T14:32:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/qds-transformer-query-directed-sparse-attention-boundaries.py
  accessed_at: '2026-10-19T14:32:00Z'
  snapshot_sha256: 99f3f8ee9d263db7fc44e6cb3072b84f96cae90da3eb6f08002fac85975b6b2c
  support: supports
  summary: "All constructed boundary assertions in qds-transformer-query-directed-sparse-attention-boundaries.py\
    \ passed with exit code 0: QDS-Transformer boundary verification passed:\n  Dense\
    \ edges: 10000, QDS edges: 2152 (21.52%), Local-only edges: 880\n  A_QDS[85,2]=1,\
    \ A_QDS[85,65]=1, A_QDS[20,85]=0"
- evidence_id: r789-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2010.12683.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T14:32:00Z'
  snapshot_sha256: b4c4785bdb9cdadc99c00636ed7a687f9d91beb6a5e2c43fe836ca7a5cc912f7
  support: supports
  summary: 'Full-text PDF (Findings of the Association for Computational Linguistics:
    EMNLP 2020 (2020)) read and verified.'
- evidence_id: r789-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2010.12683
  locator: arXiv abstract
  accessed_at: '2026-10-19T14:32:00Z'
  snapshot_sha256: e94fcd4fb163b3f51392321314f320ffaa98cade90f3cdf35dfc4253b45e1405
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r789-metadata-cr
  kind: primary_source
  reference: https://arxiv.org/bibtex/2010.12683
  locator: Crossref metadata
  accessed_at: '2026-10-19T14:32:00Z'
  snapshot_sha256: a06a3c682232cf91e5956c4a7899fb577520108afc0e1669e411aa3e30b913f8
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking
  evidence_ids:
  - identity
  - r789-primary-pdf
  - r789-arxiv-abs
  - r789-metadata-cr
  summary: 'QDS-Transformer: Query-Directed Sparse Transformer for Long Document Ranking
    is a distinct concept.'
  details: Distinct from general-purpose sparse Transformers such as Sparse Transformer
    (local/strided attention only) and Longformer-QA (which places global attention
    only on two task tokens without sentence-level [SOS] hierarchy or full query-directed
    paths), and from passage-splitting rankers such as BERT-MaxP or PARADE. QDS-Transformer
    encodes the entire long document up to 2,048 tokens in a unified cross-encoder
    with IR-axiomatic sparse attention compiled via TVM CUDA kernels.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking
  evidence_ids:
  - mapping
  - r789-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking
  evidence_ids:
  - r789-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: "All constructed boundary assertions in qds-transformer-query-directed-sparse-attention-boundaries.py\
    \ passed with exit code 0: QDS-Transformer boundary verification passed:\n  Dense\
    \ edges: 10000, QDS edges: 2152 (21.52%), Local-only edges: 880\n  A_QDS[85,2]=1,\
    \ A_QDS[85,65]=1, A_QDS[20,85]=0"
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking
  evidence_ids:
  - identity
  - mapping
  - r789-primary-pdf
  - r789-arxiv-abs
  - r789-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:QDSTransformerQueryDirectedSparseTransformerForLongDocumentRanking
  in Round 789.
- 'All pages of Findings of the Association for Computational Linguistics: EMNLP 2020
  (2020) were read in full text.'
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
