# Scientific author self-review of Doc2query Neural Document Expansion by Query Prediction

- Review: 20261019T141630Z-doc2query-document-expansion-query-prediction
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T14:16:00Z
- Finished UTC: 2026-10-19T14:16:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Doc2query Neural Document Expansion by Query Prediction as a distinct DRAFT preprocessing_method. All four claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/Doc2QueryDocumentExpansionByQueryPrediction.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:Doc2QueryDocumentExpansionByQueryPrediction
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d047360a2832d1021192e5545651c5164b9bc48b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:Doc2QueryDocumentExpansionByQueryPrediction | data/curated/Doc2QueryDocumentExpansionByQueryPrediction.yaml | maintained | Doc2query Neural Document Expansion by Query Prediction |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:Doc2QueryDocumentExpansionByQueryPrediction | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:Doc2QueryDocumentExpansionByQueryPrediction | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:Doc2QueryDocumentExpansionByQueryPrediction | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:Doc2QueryDocumentExpansionByQueryPrediction | Validated history sidecar files. |
| python3 doc2query-document-expansion-query-prediction-boundaries.py | passed | True | AIMech:Doc2QueryDocumentExpansionByQueryPrediction | [PASS] Doc2query boundaries verified: orig=1.5000 &lt; copied=2.4012, new=4.9888 &lt; full=5.6571 (&gt; distractor=4.4625) |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:Doc2QueryDocumentExpansionByQueryPrediction.

Doc2query Neural Document Expansion by Query Prediction is a distinct concept.

Distinct from query-side generation expansion methods such as GAR (AIMech:GARGenerationAugmentedRetrievalForOpenDomainQA) and HyDE (AIMech:HyDEHypotheticalDocumentEmbeddings), which generate expansion contexts from the input query at retrieval time rather than expanding corpus documents offline prior to inverted-index construction; and distinct from DeepCT (AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval), which regresses integer term frequencies for existing document tokens without generating new vocabulary terms not present in the document.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:Doc2QueryDocumentExpansionByQueryPrediction.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-4 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:Doc2QueryDocumentExpansionByQueryPrediction.

All four claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in doc2query-document-expansion-query-prediction-boundaries.py passed with exit code 0: [PASS] Doc2query boundaries verified: orig=1.5000 &lt; copied=2.4012, new=4.9888 &lt; full=5.6571 (&gt; distractor=4.4625)

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:Doc2QueryDocumentExpansionByQueryPrediction.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T141600Z-doc2query-document-expansion-query-prediction.json | supports | No normalized identity match for AIMech:Doc2QueryDocumentExpansionByQueryPrediction across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/doc2query-document-expansion-query-prediction-boundaries.py | supports | All constructed boundary assertions in doc2query-document-expansion-query-prediction-boundaries.py passed with exit code 0: [PASS] Doc2query boundaries verified: orig=1.5000 &lt; copied=2.4012, new=4.9888 &lt; full=5.6571 (&gt; distractor=4.4625) |
| r773-primary-pdf | https://arxiv.org/pdf/1904.08375.pdf; Full-text PDF | supports | Full-text PDF (arXiv (2019)) read and verified. |
| r773-arxiv-abs | https://arxiv.org/abs/1904.08375; arXiv abstract | supports | arXiv abstract read and verified. |
| r773-metadata-cr | https://arxiv.org/bibtex/1904.08375; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:Doc2QueryDocumentExpansionByQueryPrediction in Round 773.
- All pages of arXiv (2019) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T141630Z-doc2query-document-expansion-query-prediction
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Doc2query Neural Document Expansion by Query
  Prediction
started_at: '2026-10-19T14:16:00Z'
finished_at: '2026-10-19T14:16:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:Doc2QueryDocumentExpansionByQueryPrediction
    against existing AIMech and AIO records and verified all claims against arXiv
    (2019) and pure-Python boundary checks. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Doc2query Neural Document Expansion by Query Prediction as a distinct
  DRAFT preprocessing_method. All four claims are supported by full-text primary evidence
  and pure-Python boundary verification.
source:
  git_revision: d047360a2832d1021192e5545651c5164b9bc48b
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/Doc2QueryDocumentExpansionByQueryPrediction.yaml
    sha256: 0256651f266e8ec7845a5b8b640515bd1ed159d18e48b94edaef6db2273d40ae
    role: target
  - path: research/discovery/20261019T141600Z-doc2query-document-expansion-query-prediction.json
    sha256: 919c441d4b687fbcde2d6d45dc13d8a476cf3dee1543c9e28234020deab1a0e9
    role: context
  - path: research/discovery/doc2query-document-expansion-query-prediction-boundaries.py
    sha256: f5225a214b1792c63ecf454a55c6232ac557bbd8291c07ef972bf0a3daa94f82
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
- target_id: AIMech:Doc2QueryDocumentExpansionByQueryPrediction
  path: data/curated/Doc2QueryDocumentExpansionByQueryPrediction.yaml
  label: Doc2query Neural Document Expansion by Query Prediction
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Doc2QueryDocumentExpansionByQueryPrediction.yaml
    role: maintained
scope:
  description: All fields of data/curated/Doc2QueryDocumentExpansionByQueryPrediction.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:Doc2QueryDocumentExpansionByQueryPrediction'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:Doc2QueryDocumentExpansionByQueryPrediction
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
  - AIMech:Doc2QueryDocumentExpansionByQueryPrediction
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:Doc2QueryDocumentExpansionByQueryPrediction
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:Doc2QueryDocumentExpansionByQueryPrediction
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:Doc2QueryDocumentExpansionByQueryPrediction
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 doc2query-document-expansion-query-prediction-boundaries.py
  command: python3 research/discovery/doc2query-document-expansion-query-prediction-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:Doc2QueryDocumentExpansionByQueryPrediction
  exit_code: 0
  expected_exit_code: 0
  summary: '[PASS] Doc2query boundaries verified: orig=1.5000 < copied=2.4012, new=4.9888
    < full=5.6571 (> distractor=4.4625)'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T141600Z-doc2query-document-expansion-query-prediction.json
  accessed_at: '2026-10-19T14:16:00Z'
  support: supports
  summary: No normalized identity match for AIMech:Doc2QueryDocumentExpansionByQueryPrediction
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T14:16:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/doc2query-document-expansion-query-prediction-boundaries.py
  accessed_at: '2026-10-19T14:16:00Z'
  snapshot_sha256: f5225a214b1792c63ecf454a55c6232ac557bbd8291c07ef972bf0a3daa94f82
  support: supports
  summary: 'All constructed boundary assertions in doc2query-document-expansion-query-prediction-boundaries.py
    passed with exit code 0: [PASS] Doc2query boundaries verified: orig=1.5000 < copied=2.4012,
    new=4.9888 < full=5.6571 (> distractor=4.4625)'
- evidence_id: r773-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/1904.08375.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T14:16:00Z'
  snapshot_sha256: ae7ba200f53ac3beb3d9c9c6797226ffd4029b9cb6bd3495e3b65169554c55e5
  support: supports
  summary: Full-text PDF (arXiv (2019)) read and verified.
- evidence_id: r773-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1904.08375
  locator: arXiv abstract
  accessed_at: '2026-10-19T14:16:00Z'
  snapshot_sha256: 6d7b7cdaa93f9f2ca1155b3fbdf723831e319a09317df5e85c000830e972e1fa
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r773-metadata-cr
  kind: primary_source
  reference: https://arxiv.org/bibtex/1904.08375
  locator: Crossref metadata
  accessed_at: '2026-10-19T14:16:00Z'
  snapshot_sha256: d547fbca2f6c4f594d5927f02e66484734c88d2546e4ebb2a5f1d2b9c7455ef4
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:Doc2QueryDocumentExpansionByQueryPrediction
  evidence_ids:
  - identity
  - r773-primary-pdf
  - r773-arxiv-abs
  - r773-metadata-cr
  summary: Doc2query Neural Document Expansion by Query Prediction is a distinct concept.
  details: Distinct from query-side generation expansion methods such as GAR (AIMech:GARGenerationAugmentedRetrievalForOpenDomainQA)
    and HyDE (AIMech:HyDEHypotheticalDocumentEmbeddings), which generate expansion
    contexts from the input query at retrieval time rather than expanding corpus documents
    offline prior to inverted-index construction; and distinct from DeepCT (AIMech:DeepCTContextAwareTermImportanceEstimationForFirstStageRetrieval),
    which regresses integer term frequencies for existing document tokens without
    generating new vocabulary terms not present in the document.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:Doc2QueryDocumentExpansionByQueryPrediction
  evidence_ids:
  - mapping
  - r773-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-4 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:Doc2QueryDocumentExpansionByQueryPrediction
  evidence_ids:
  - r773-primary-pdf
  - calculation
  summary: All four claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in doc2query-document-expansion-query-prediction-boundaries.py
    passed with exit code 0: [PASS] Doc2query boundaries verified: orig=1.5000 < copied=2.4012,
    new=4.9888 < full=5.6571 (> distractor=4.4625)'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:Doc2QueryDocumentExpansionByQueryPrediction
  evidence_ids:
  - identity
  - mapping
  - r773-primary-pdf
  - r773-arxiv-abs
  - r773-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:Doc2QueryDocumentExpansionByQueryPrediction in Round
  773.
- All pages of arXiv (2019) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
