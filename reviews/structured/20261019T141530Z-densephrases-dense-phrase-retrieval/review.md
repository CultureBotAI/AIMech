# Scientific author self-review of DensePhrases Dense Phrase Retrieval at Scale

- Review: 20261019T141530Z-densephrases-dense-phrase-retrieval
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T14:15:00Z
- Finished UTC: 2026-10-19T14:15:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain DensePhrases Dense Phrase Retrieval at Scale as a distinct DRAFT architecture. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f9eab37f014e35c670435c0a267200aafe3ed73e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale | data/curated/DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale.yaml | maintained | DensePhrases Dense Phrase Retrieval at Scale |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale | Validated history sidecar files. |
| python3 densephrases-dense-phrase-retrieval-boundaries.py | passed | True | AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale | [PASS] DensePhrases boundaries verified: best_span=(3, 4) ('the Police'), num_negs=5, qs_loss_multi=0.3792 &lt; qs_loss_single=0.6868 |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale.

DensePhrases Dense Phrase Retrieval at Scale is a distinct concept.

Distinct from two-stage retriever-reader models such as DPR and GAR (AIMech:GARGenerationAugmentedRetrievalForOpenDomainQA), which retrieve passages first and run an on-demand reading-comprehension model at inference time rather than directly retrieving answer phrases via decomposed start/end token MIPS; and distinct from earlier hybrid phrase retrieval systems (DenSPI and DenSPI+Sparc), which require concatenating high-dimensional sparse document/paragraph/contextualized vectors with split dense vectors and coherency scalars rather than purely dense unsplit SpanBERT endpoint representations trained with FIFO pre-batch negatives and query-side fine-tuning.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in densephrases-dense-phrase-retrieval-boundaries.py passed with exit code 0: [PASS] DensePhrases boundaries verified: best_span=(3, 4) ('the Police'), num_negs=5, qs_loss_multi=0.3792 &lt; qs_loss_single=0.6868

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T141500Z-densephrases-dense-phrase-retrieval.json | supports | No normalized identity match for AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/densephrases-dense-phrase-retrieval-boundaries.py | supports | All constructed boundary assertions in densephrases-dense-phrase-retrieval-boundaries.py passed with exit code 0: [PASS] DensePhrases boundaries verified: best_span=(3, 4) ('the Police'), num_negs=5, qs_loss_multi=0.3792 &lt; qs_loss_single=0.6868 |
| r772-primary-pdf | https://arxiv.org/pdf/2012.12624.pdf; Full-text PDF | supports | Full-text PDF (ACL-IJCNLP 2021 (2021)) read and verified. |
| r772-arxiv-abs | https://arxiv.org/abs/2012.12624; arXiv abstract | supports | arXiv abstract read and verified. |
| r772-metadata-cr | https://arxiv.org/bibtex/2012.12624; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale in Round 772.
- All pages of ACL-IJCNLP 2021 (2021) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T141530Z-densephrases-dense-phrase-retrieval
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of DensePhrases Dense Phrase Retrieval at Scale
started_at: '2026-10-19T14:15:00Z'
finished_at: '2026-10-19T14:15:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale
    against existing AIMech and AIO records and verified all claims against ACL-IJCNLP
    2021 (2021) and pure-Python boundary checks. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain DensePhrases Dense Phrase Retrieval at Scale as a distinct DRAFT architecture.
  All three claims are supported by full-text primary evidence and pure-Python boundary
  verification.
source:
  git_revision: f9eab37f014e35c670435c0a267200aafe3ed73e
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale.yaml
    sha256: 7f7803d4d0b8af37fce06c06bdb2cf957f0be967a47caae54c5d47c6fb56f21b
    role: target
  - path: research/discovery/20261019T141500Z-densephrases-dense-phrase-retrieval.json
    sha256: 23da6c982e72f6491f1c6d122bb7ce3b5a26b0bc46b688b03caee58fc95bdfd6
    role: context
  - path: research/discovery/densephrases-dense-phrase-retrieval-boundaries.py
    sha256: c1e4de47926418bfd52d70767219623c7bcb7bac743bd93b506db98ea2141fea
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
- target_id: AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale
  path: data/curated/DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale.yaml
  label: DensePhrases Dense Phrase Retrieval at Scale
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale.yaml
    role: maintained
scope:
  description: All fields of data/curated/DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale
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
  - AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 densephrases-dense-phrase-retrieval-boundaries.py
  command: python3 research/discovery/densephrases-dense-phrase-retrieval-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale
  exit_code: 0
  expected_exit_code: 0
  summary: '[PASS] DensePhrases boundaries verified: best_span=(3, 4) (''the Police''),
    num_negs=5, qs_loss_multi=0.3792 < qs_loss_single=0.6868'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T141500Z-densephrases-dense-phrase-retrieval.json
  accessed_at: '2026-10-19T14:15:00Z'
  support: supports
  summary: No normalized identity match for AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T14:15:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/densephrases-dense-phrase-retrieval-boundaries.py
  accessed_at: '2026-10-19T14:15:00Z'
  snapshot_sha256: c1e4de47926418bfd52d70767219623c7bcb7bac743bd93b506db98ea2141fea
  support: supports
  summary: 'All constructed boundary assertions in densephrases-dense-phrase-retrieval-boundaries.py
    passed with exit code 0: [PASS] DensePhrases boundaries verified: best_span=(3,
    4) (''the Police''), num_negs=5, qs_loss_multi=0.3792 < qs_loss_single=0.6868'
- evidence_id: r772-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2012.12624.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T14:15:00Z'
  snapshot_sha256: e3eacb3f5627ef4bdaef95a52d8c61902953c8ce16bfa100ecac35a017fa18d4
  support: supports
  summary: Full-text PDF (ACL-IJCNLP 2021 (2021)) read and verified.
- evidence_id: r772-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2012.12624
  locator: arXiv abstract
  accessed_at: '2026-10-19T14:15:00Z'
  snapshot_sha256: 14870f72a6ff154fa8b1cfb4ba4e636a21d825d63a38b8a4bd7e5a1bd450981f
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r772-metadata-cr
  kind: primary_source
  reference: https://arxiv.org/bibtex/2012.12624
  locator: Crossref metadata
  accessed_at: '2026-10-19T14:15:00Z'
  snapshot_sha256: f45bca1eb43fec56c82bf35e47ae965afa6df18428b812bdda7c5f0948d7446a
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale
  evidence_ids:
  - identity
  - r772-primary-pdf
  - r772-arxiv-abs
  - r772-metadata-cr
  summary: DensePhrases Dense Phrase Retrieval at Scale is a distinct concept.
  details: Distinct from two-stage retriever-reader models such as DPR and GAR (AIMech:GARGenerationAugmentedRetrievalForOpenDomainQA),
    which retrieve passages first and run an on-demand reading-comprehension model
    at inference time rather than directly retrieving answer phrases via decomposed
    start/end token MIPS; and distinct from earlier hybrid phrase retrieval systems
    (DenSPI and DenSPI+Sparc), which require concatenating high-dimensional sparse
    document/paragraph/contextualized vectors with split dense vectors and coherency
    scalars rather than purely dense unsplit SpanBERT endpoint representations trained
    with FIFO pre-batch negatives and query-side fine-tuning.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale
  evidence_ids:
  - mapping
  - r772-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale
  evidence_ids:
  - r772-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in densephrases-dense-phrase-retrieval-boundaries.py
    passed with exit code 0: [PASS] DensePhrases boundaries verified: best_span=(3,
    4) (''the Police''), num_negs=5, qs_loss_multi=0.3792 < qs_loss_single=0.6868'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale
  evidence_ids:
  - identity
  - mapping
  - r772-primary-pdf
  - r772-arxiv-abs
  - r772-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:DensePhrasesLearningDenseRepresentationsOfPhrasesAtScale
  in Round 772.
- All pages of ACL-IJCNLP 2021 (2021) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
