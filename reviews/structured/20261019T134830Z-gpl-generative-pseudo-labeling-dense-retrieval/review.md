# Scientific author self-review of GPL (Generative Pseudo Labeling for Unsupervised Domain Adaptation of Dense Retrieval)

- Review: 20261019T134830Z-gpl-generative-pseudo-labeling-dense-retrieval
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T13:48:00Z
- Finished UTC: 2026-10-19T13:48:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain GPL (Generative Pseudo Labeling for Unsupervised Domain Adaptation of Dense Retrieval) as a distinct DRAFT algorithm. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/GPLGenerativePseudoLabelingForDenseRetrieval.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:GPLGenerativePseudoLabelingForDenseRetrieval
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6c3fb293aa6cbb720dd024f8d66024d368e98ec6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:GPLGenerativePseudoLabelingForDenseRetrieval | data/curated/GPLGenerativePseudoLabelingForDenseRetrieval.yaml | maintained | GPL (Generative Pseudo Labeling for Unsupervised Domain Adaptation of Dense Retrieval) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:GPLGenerativePseudoLabelingForDenseRetrieval | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:GPLGenerativePseudoLabelingForDenseRetrieval | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:GPLGenerativePseudoLabelingForDenseRetrieval | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:GPLGenerativePseudoLabelingForDenseRetrieval | Validated history sidecar files. |
| python3 gpl-generative-pseudo-labeling-dense-retrieval-boundaries.py | passed | True | AIMech:GPLGenerativePseudoLabelingForDenseRetrieval | GPL boundary verification passed: {'loss_false_neg_gpl': 0.01, 'loss_true_neg_gpl': 64.0} |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:GPLGenerativePseudoLabelingForDenseRetrieval.

GPL (Generative Pseudo Labeling for Unsupervised Domain Adaptation of Dense Retrieval) is a distinct concept.

Introduced by Wang, Thakur, Reimers, and Gurevych (NAACL-HLT 2022, pp. 2345-2360, arXiv:2112.07577). Distinguished from QGen (Ma et al., 2021; Thakur et al., 2021), which trains on generated queries with binary 0-1 MultipleNegativesRanking loss (MNRL) and degrades when combined with hard negatives, and from InPars (Bonifacio et al., 2022) or Promptagator (Dai et al., 2023), which rely on few-shot LLM prompt generation and top-k likelihood or dual-encoder consistency filtering rather than cross-encoder MarginMSE soft-margin distillation.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:GPLGenerativePseudoLabelingForDenseRetrieval.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:GPLGenerativePseudoLabelingForDenseRetrieval.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in gpl-generative-pseudo-labeling-dense-retrieval-boundaries.py passed with exit code 0: GPL boundary verification passed: {'loss_false_neg_gpl': 0.01, 'loss_true_neg_gpl': 64.0}

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:GPLGenerativePseudoLabelingForDenseRetrieval.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T134800Z-gpl-generative-pseudo-labeling-dense-retrieval.json | supports | No normalized identity match for AIMech:GPLGenerativePseudoLabelingForDenseRetrieval across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/gpl-generative-pseudo-labeling-dense-retrieval-boundaries.py | supports | All constructed boundary assertions in gpl-generative-pseudo-labeling-dense-retrieval-boundaries.py passed with exit code 0: GPL boundary verification passed: {'loss_false_neg_gpl': 0.01, 'loss_true_neg_gpl': 64.0} |
| r745-primary-pdf | https://arxiv.org/pdf/2112.07577; Full-text PDF | supports | Full-text PDF (Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT 2022) (2022)) read and verified. |
| r745-arxiv-abs | https://arxiv.org/abs/2112.07577; arXiv abstract | supports | arXiv abstract read and verified. |
| r745-metadata-cr | https://dblp.org/search/publ/api?q=GPL+Generative+Pseudo+Labeling+for+Unsupervised+Domain+Adaptation+Wang&amp;h=5&amp;format=xml; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:GPLGenerativePseudoLabelingForDenseRetrieval in Round 745.
- All pages of Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT 2022) (2022) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T134830Z-gpl-generative-pseudo-labeling-dense-retrieval
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of GPL (Generative Pseudo Labeling for Unsupervised
  Domain Adaptation of Dense Retrieval)
started_at: '2026-10-19T13:48:00Z'
finished_at: '2026-10-19T13:48:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: 'The author challenged definition distinctness of AIMech:GPLGenerativePseudoLabelingForDenseRetrieval
    against existing AIMech and AIO records and verified all claims against Proceedings
    of the 2022 Conference of the North American Chapter of the Association for Computational
    Linguistics: Human Language Technologies (NAACL-HLT 2022) (2022) and pure-Python
    boundary checks. This is adversarial author self-review, not independent approval.'
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain GPL (Generative Pseudo Labeling for Unsupervised Domain Adaptation
  of Dense Retrieval) as a distinct DRAFT algorithm. All three claims are supported
  by full-text primary evidence and pure-Python boundary verification.
source:
  git_revision: 6c3fb293aa6cbb720dd024f8d66024d368e98ec6
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/GPLGenerativePseudoLabelingForDenseRetrieval.yaml
    sha256: 0cf6920a0b1a90c18b8d4fe3c1f7aac632efe5ee53c46d4414f335fd8988fba1
    role: target
  - path: research/discovery/20261019T134800Z-gpl-generative-pseudo-labeling-dense-retrieval.json
    sha256: 1fbe2cfdd457f5298cfdd4bb278197338207ddc3aabad6f8b3459235194c0b54
    role: context
  - path: research/discovery/gpl-generative-pseudo-labeling-dense-retrieval-boundaries.py
    sha256: dc97a21473a4dc36a56fe8ca8dffa1c83662a9eefdea28a83b1be059c05294b0
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
- target_id: AIMech:GPLGenerativePseudoLabelingForDenseRetrieval
  path: data/curated/GPLGenerativePseudoLabelingForDenseRetrieval.yaml
  label: GPL (Generative Pseudo Labeling for Unsupervised Domain Adaptation of Dense
    Retrieval)
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GPLGenerativePseudoLabelingForDenseRetrieval.yaml
    role: maintained
scope:
  description: All fields of data/curated/GPLGenerativePseudoLabelingForDenseRetrieval.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:GPLGenerativePseudoLabelingForDenseRetrieval'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:GPLGenerativePseudoLabelingForDenseRetrieval
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
  - AIMech:GPLGenerativePseudoLabelingForDenseRetrieval
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:GPLGenerativePseudoLabelingForDenseRetrieval
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:GPLGenerativePseudoLabelingForDenseRetrieval
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:GPLGenerativePseudoLabelingForDenseRetrieval
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 gpl-generative-pseudo-labeling-dense-retrieval-boundaries.py
  command: python3 research/discovery/gpl-generative-pseudo-labeling-dense-retrieval-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:GPLGenerativePseudoLabelingForDenseRetrieval
  exit_code: 0
  expected_exit_code: 0
  summary: 'GPL boundary verification passed: {''loss_false_neg_gpl'': 0.01, ''loss_true_neg_gpl'':
    64.0}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T134800Z-gpl-generative-pseudo-labeling-dense-retrieval.json
  accessed_at: '2026-10-19T13:48:00Z'
  support: supports
  summary: No normalized identity match for AIMech:GPLGenerativePseudoLabelingForDenseRetrieval
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T13:48:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/gpl-generative-pseudo-labeling-dense-retrieval-boundaries.py
  accessed_at: '2026-10-19T13:48:00Z'
  snapshot_sha256: dc97a21473a4dc36a56fe8ca8dffa1c83662a9eefdea28a83b1be059c05294b0
  support: supports
  summary: 'All constructed boundary assertions in gpl-generative-pseudo-labeling-dense-retrieval-boundaries.py
    passed with exit code 0: GPL boundary verification passed: {''loss_false_neg_gpl'':
    0.01, ''loss_true_neg_gpl'': 64.0}'
- evidence_id: r745-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2112.07577
  locator: Full-text PDF
  accessed_at: '2026-10-19T13:48:00Z'
  snapshot_sha256: 7aa2a27bfa303bdedbba10a0542e8acdb6c78cfdcff0e872d3024973a08e2b1e
  support: supports
  summary: 'Full-text PDF (Proceedings of the 2022 Conference of the North American
    Chapter of the Association for Computational Linguistics: Human Language Technologies
    (NAACL-HLT 2022) (2022)) read and verified.'
- evidence_id: r745-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2112.07577
  locator: arXiv abstract
  accessed_at: '2026-10-19T13:48:00Z'
  snapshot_sha256: ff9479cfab7467249422b704bb9a959e47978ae03528aba04ca153c8f4659513
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r745-metadata-cr
  kind: primary_source
  reference: https://dblp.org/search/publ/api?q=GPL+Generative+Pseudo+Labeling+for+Unsupervised+Domain+Adaptation+Wang&h=5&format=xml
  locator: Crossref metadata
  accessed_at: '2026-10-19T13:48:00Z'
  snapshot_sha256: 6f2a60158a07a14e1ebf706f6e59df1362d981469e06eecc1bf8342e415e8fbc
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:GPLGenerativePseudoLabelingForDenseRetrieval
  evidence_ids:
  - identity
  - r745-primary-pdf
  - r745-arxiv-abs
  - r745-metadata-cr
  summary: GPL (Generative Pseudo Labeling for Unsupervised Domain Adaptation of Dense
    Retrieval) is a distinct concept.
  details: Introduced by Wang, Thakur, Reimers, and Gurevych (NAACL-HLT 2022, pp.
    2345-2360, arXiv:2112.07577). Distinguished from QGen (Ma et al., 2021; Thakur
    et al., 2021), which trains on generated queries with binary 0-1 MultipleNegativesRanking
    loss (MNRL) and degrades when combined with hard negatives, and from InPars (Bonifacio
    et al., 2022) or Promptagator (Dai et al., 2023), which rely on few-shot LLM prompt
    generation and top-k likelihood or dual-encoder consistency filtering rather than
    cross-encoder MarginMSE soft-margin distillation.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:GPLGenerativePseudoLabelingForDenseRetrieval
  evidence_ids:
  - mapping
  - r745-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:GPLGenerativePseudoLabelingForDenseRetrieval
  evidence_ids:
  - r745-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in gpl-generative-pseudo-labeling-dense-retrieval-boundaries.py
    passed with exit code 0: GPL boundary verification passed: {''loss_false_neg_gpl'':
    0.01, ''loss_true_neg_gpl'': 64.0}'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:GPLGenerativePseudoLabelingForDenseRetrieval
  evidence_ids:
  - identity
  - mapping
  - r745-primary-pdf
  - r745-arxiv-abs
  - r745-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:GPLGenerativePseudoLabelingForDenseRetrieval in Round
  745.
- 'All pages of Proceedings of the 2022 Conference of the North American Chapter of
  the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT
  2022) (2022) were read in full text.'
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
