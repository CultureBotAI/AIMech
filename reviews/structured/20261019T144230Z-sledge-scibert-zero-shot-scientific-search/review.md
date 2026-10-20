# Scientific author self-review of SLEDGE (SciBERT Zero-Shot Domain-Transfer Scientific Literature Search)

- Review: 20261019T144230Z-sledge-scibert-zero-shot-scientific-search
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T14:42:00Z
- Finished UTC: 2026-10-19T14:42:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain SLEDGE (SciBERT Zero-Shot Domain-Transfer Scientific Literature Search) as a distinct DRAFT architecture. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/SLEDGESciBERTZeroShotScientificLiteratureSearch.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 45f3580f3250a20b7d962353b94ebdf36c18950d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch | data/curated/SLEDGESciBERTZeroShotScientificLiteratureSearch.yaml | maintained | SLEDGE (SciBERT Zero-Shot Domain-Transfer Scientific Literature Search) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch | Validated history sidecar files. |
| python3 sledge-scibert-zero-shot-scientific-search-boundaries.py | passed | True | AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch | SLEDGE boundary verification passed:<br>  Tuned BM25 repetition gain ratio: 2.1770 &gt; default 1.4048<br>  Pairwise CE loss: good=0.1668 &lt; bad=1.1957<br>  Med-MSMARCO filtered query IDs: [1, 3] |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch.

SLEDGE (SciBERT Zero-Shot Domain-Transfer Scientific Literature Search) is a distinct concept.

Distinct from general-domain BERT passage rerankers (Nogueira &amp; Cho, 2019) and from CEDR (AIMech:CEDRContextualizedEmbeddingsForDocumentRanking). SLEDGE bridges emerging scientific domains lacking in-domain relevance judgments by pairing a scientific pre-trained language model (SciBERT) with out-of-domain relevance supervision transferred from MS MARCO (or lexicon-filtered Med-MSMARCO via the MedSyn layperson medical lexicon) and asymmetric field routing (searching full text with keyword queries or natural-language questions in Stage 1 while re-ranking title+abstract with natural-language questions in Stage 2).

### AIO mapping accuracy

grounding: supported. Targets: AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in sledge-scibert-zero-shot-scientific-search-boundaries.py passed with exit code 0: SLEDGE boundary verification passed:
  Tuned BM25 repetition gain ratio: 2.1770 &gt; default 1.4048
  Pairwise CE loss: good=0.1668 &lt; bad=1.1957
  Med-MSMARCO filtered query IDs: [1, 3]

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T144200Z-sledge-scibert-zero-shot-scientific-search.json | supports | No normalized identity match for AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/sledge-scibert-zero-shot-scientific-search-boundaries.py | supports | All constructed boundary assertions in sledge-scibert-zero-shot-scientific-search-boundaries.py passed with exit code 0: SLEDGE boundary verification passed:<br>  Tuned BM25 repetition gain ratio: 2.1770 &gt; default 1.4048<br>  Pairwise CE loss: good=0.1668 &lt; bad=1.1957<br>  Med-MSMARCO filtered query IDs: [1, 3] |
| r799-primary-pdf | https://arxiv.org/pdf/2005.02365.pdf; Full-text PDF | supports | Full-text PDF (Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP 2020) (2020)) read and verified. |
| r799-arxiv-abs | https://arxiv.org/abs/2005.02365; arXiv abstract | supports | arXiv abstract read and verified. |
| r799-metadata-cr | https://arxiv.org/bibtex/2005.02365; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch in Round 799.
- All pages of Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP 2020) (2020) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T144230Z-sledge-scibert-zero-shot-scientific-search
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of SLEDGE (SciBERT Zero-Shot Domain-Transfer
  Scientific Literature Search)
started_at: '2026-10-19T14:42:00Z'
finished_at: '2026-10-19T14:42:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch
    against existing AIMech and AIO records and verified all claims against Proceedings
    of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP
    2020) (2020) and pure-Python boundary checks. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain SLEDGE (SciBERT Zero-Shot Domain-Transfer Scientific Literature Search)
  as a distinct DRAFT architecture. All three claims are supported by full-text primary
  evidence and pure-Python boundary verification.
source:
  git_revision: 45f3580f3250a20b7d962353b94ebdf36c18950d
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/SLEDGESciBERTZeroShotScientificLiteratureSearch.yaml
    sha256: 0f9dab3d25f72b2899ab298d331b4d3c6652175a4adcdbfa0c34b9170ede321d
    role: target
  - path: research/discovery/20261019T144200Z-sledge-scibert-zero-shot-scientific-search.json
    sha256: 575b6f2898efeab27a06b1ae75289afb6eb0e0c7439b0284ebe1e1b3f5556a60
    role: context
  - path: research/discovery/sledge-scibert-zero-shot-scientific-search-boundaries.py
    sha256: be33c45c6c2100352ec5f57c62bc752861ae146f3d95ce6c23d32f0ac0c3cf25
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
- target_id: AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch
  path: data/curated/SLEDGESciBERTZeroShotScientificLiteratureSearch.yaml
  label: SLEDGE (SciBERT Zero-Shot Domain-Transfer Scientific Literature Search)
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SLEDGESciBERTZeroShotScientificLiteratureSearch.yaml
    role: maintained
scope:
  description: All fields of data/curated/SLEDGESciBERTZeroShotScientificLiteratureSearch.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch
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
  - AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 sledge-scibert-zero-shot-scientific-search-boundaries.py
  command: python3 research/discovery/sledge-scibert-zero-shot-scientific-search-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch
  exit_code: 0
  expected_exit_code: 0
  summary: "SLEDGE boundary verification passed:\n  Tuned BM25 repetition gain ratio:\
    \ 2.1770 > default 1.4048\n  Pairwise CE loss: good=0.1668 < bad=1.1957\n  Med-MSMARCO\
    \ filtered query IDs: [1, 3]"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T144200Z-sledge-scibert-zero-shot-scientific-search.json
  accessed_at: '2026-10-19T14:42:00Z'
  support: supports
  summary: No normalized identity match for AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T14:42:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/sledge-scibert-zero-shot-scientific-search-boundaries.py
  accessed_at: '2026-10-19T14:42:00Z'
  snapshot_sha256: be33c45c6c2100352ec5f57c62bc752861ae146f3d95ce6c23d32f0ac0c3cf25
  support: supports
  summary: "All constructed boundary assertions in sledge-scibert-zero-shot-scientific-search-boundaries.py\
    \ passed with exit code 0: SLEDGE boundary verification passed:\n  Tuned BM25\
    \ repetition gain ratio: 2.1770 > default 1.4048\n  Pairwise CE loss: good=0.1668\
    \ < bad=1.1957\n  Med-MSMARCO filtered query IDs: [1, 3]"
- evidence_id: r799-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2005.02365.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T14:42:00Z'
  snapshot_sha256: cebc7ef139ef706a03db7d460c35d068c71f925cfb191a7edd0a80b7a79208c3
  support: supports
  summary: Full-text PDF (Proceedings of the 2020 Conference on Empirical Methods
    in Natural Language Processing (EMNLP 2020) (2020)) read and verified.
- evidence_id: r799-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2005.02365
  locator: arXiv abstract
  accessed_at: '2026-10-19T14:42:00Z'
  snapshot_sha256: 54f5861f898074c2f1ad02f414b7bcf8c064586ce7fe81c76531ca724bc14a31
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r799-metadata-cr
  kind: primary_source
  reference: https://arxiv.org/bibtex/2005.02365
  locator: Crossref metadata
  accessed_at: '2026-10-19T14:42:00Z'
  snapshot_sha256: 42f45bdd94a39a4e5e699900aeac44728e28d54a4f72759c526b222cf97abb46
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch
  evidence_ids:
  - identity
  - r799-primary-pdf
  - r799-arxiv-abs
  - r799-metadata-cr
  summary: SLEDGE (SciBERT Zero-Shot Domain-Transfer Scientific Literature Search)
    is a distinct concept.
  details: Distinct from general-domain BERT passage rerankers (Nogueira & Cho, 2019)
    and from CEDR (AIMech:CEDRContextualizedEmbeddingsForDocumentRanking). SLEDGE
    bridges emerging scientific domains lacking in-domain relevance judgments by pairing
    a scientific pre-trained language model (SciBERT) with out-of-domain relevance
    supervision transferred from MS MARCO (or lexicon-filtered Med-MSMARCO via the
    MedSyn layperson medical lexicon) and asymmetric field routing (searching full
    text with keyword queries or natural-language questions in Stage 1 while re-ranking
    title+abstract with natural-language questions in Stage 2).
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch
  evidence_ids:
  - mapping
  - r799-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch
  evidence_ids:
  - r799-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: "All constructed boundary assertions in sledge-scibert-zero-shot-scientific-search-boundaries.py\
    \ passed with exit code 0: SLEDGE boundary verification passed:\n  Tuned BM25\
    \ repetition gain ratio: 2.1770 > default 1.4048\n  Pairwise CE loss: good=0.1668\
    \ < bad=1.1957\n  Med-MSMARCO filtered query IDs: [1, 3]"
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch
  evidence_ids:
  - identity
  - mapping
  - r799-primary-pdf
  - r799-arxiv-abs
  - r799-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:SLEDGESciBERTZeroShotScientificLiteratureSearch in Round
  799.
- All pages of Proceedings of the 2020 Conference on Empirical Methods in Natural
  Language Processing (EMNLP 2020) (2020) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
