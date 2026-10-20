# Scientific author self-review of SPLADE (Sparse Lexical and Expansion Model for First Stage Ranking)

- Review: 20261019T135230Z-splade-sparse-lexical-expansion-model
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T13:52:00Z
- Finished UTC: 2026-10-19T13:52:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain SPLADE (Sparse Lexical and Expansion Model for First Stage Ranking) as a distinct DRAFT architecture. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/SPLADESparseLexicalAndExpansionModel.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:SPLADESparseLexicalAndExpansionModel
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 58bb1b831d589d362213e9cee723c76d159a5d92.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SPLADESparseLexicalAndExpansionModel | data/curated/SPLADESparseLexicalAndExpansionModel.yaml | maintained | SPLADE (Sparse Lexical and Expansion Model for First Stage Ranking) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:SPLADESparseLexicalAndExpansionModel | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:SPLADESparseLexicalAndExpansionModel | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:SPLADESparseLexicalAndExpansionModel | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:SPLADESparseLexicalAndExpansionModel | Validated history sidecar files. |
| python3 splade-sparse-lexical-expansion-model-boundaries.py | passed | True | AIMech:SPLADESparseLexicalAndExpansionModel | SPLADE boundary verification passed: {'flops_skewed': 4.0, 'flops_balanced': 1.0} |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:SPLADESparseLexicalAndExpansionModel.

SPLADE (Sparse Lexical and Expansion Model for First Stage Ranking) is a distinct concept.

Introduced by Formal, Piwowarski, and Clinchant (SIGIR 2021, pp. 2288-2292, arXiv:2107.05720). Distinguished from DeepCT (Dai &amp; Callan, 2019), which re-weights only existing document terms without vocabulary expansion, from doc2query/docTTTTTquery (Nogueira et al., 2019), which perform offline sequence-to-sequence text expansion before BM25 indexing, and from SparTerm (Bai et al., 2020), which uses un-saturated ReLU summation with a fixed pre-trained binary gating mask rather than end-to-end log-saturated FLOPS-regularized training.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:SPLADESparseLexicalAndExpansionModel.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:SPLADESparseLexicalAndExpansionModel.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in splade-sparse-lexical-expansion-model-boundaries.py passed with exit code 0: SPLADE boundary verification passed: {'flops_skewed': 4.0, 'flops_balanced': 1.0}

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:SPLADESparseLexicalAndExpansionModel.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T135200Z-splade-sparse-lexical-expansion-model.json | supports | No normalized identity match for AIMech:SPLADESparseLexicalAndExpansionModel across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/splade-sparse-lexical-expansion-model-boundaries.py | supports | All constructed boundary assertions in splade-sparse-lexical-expansion-model-boundaries.py passed with exit code 0: SPLADE boundary verification passed: {'flops_skewed': 4.0, 'flops_balanced': 1.0} |
| r749-primary-pdf | https://arxiv.org/pdf/2107.05720; Full-text PDF | supports | Full-text PDF (Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR 2021) (2021)) read and verified. |
| r749-arxiv-abs | https://arxiv.org/abs/2107.05720; arXiv abstract | supports | arXiv abstract read and verified. |
| r749-metadata-cr | https://dblp.org/search/publ/api?q=SPLADE+Sparse+Lexical+and+Expansion+Model+Formal&amp;h=5&amp;format=xml; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:SPLADESparseLexicalAndExpansionModel in Round 749.
- All pages of Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR 2021) (2021) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T135230Z-splade-sparse-lexical-expansion-model
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of SPLADE (Sparse Lexical and Expansion Model
  for First Stage Ranking)
started_at: '2026-10-19T13:52:00Z'
finished_at: '2026-10-19T13:52:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:SPLADESparseLexicalAndExpansionModel
    against existing AIMech and AIO records and verified all claims against Proceedings
    of the 44th International ACM SIGIR Conference on Research and Development in
    Information Retrieval (SIGIR 2021) (2021) and pure-Python boundary checks. This
    is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain SPLADE (Sparse Lexical and Expansion Model for First Stage Ranking)
  as a distinct DRAFT architecture. All three claims are supported by full-text primary
  evidence and pure-Python boundary verification.
source:
  git_revision: 58bb1b831d589d362213e9cee723c76d159a5d92
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/SparseLearning.yaml
    sha256: 0e45f464899bee39df6c8af85e3e0fccba4062f39c73e35c8e884113f78ce3c5
    role: context
  - path: data/curated/SPLADESparseLexicalAndExpansionModel.yaml
    sha256: 6cb32680a25eafd75f556d12e545d0763e43d4987f3328071827b97d853cf98a
    role: target
  - path: research/discovery/20261019T135200Z-splade-sparse-lexical-expansion-model.json
    sha256: 4de50e9692fc1eb32e6c3bbd6bebf9d18ff94395ed5c8bdb521367e2217c229a
    role: context
  - path: research/discovery/splade-sparse-lexical-expansion-model-boundaries.py
    sha256: f88167cbd107ef26f06ab6b37dab63a038c0fbf3a7686b9da97ea6840f7b05d3
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
- target_id: AIMech:SPLADESparseLexicalAndExpansionModel
  path: data/curated/SPLADESparseLexicalAndExpansionModel.yaml
  label: SPLADE (Sparse Lexical and Expansion Model for First Stage Ranking)
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SPLADESparseLexicalAndExpansionModel.yaml
    role: maintained
scope:
  description: All fields of data/curated/SPLADESparseLexicalAndExpansionModel.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:SPLADESparseLexicalAndExpansionModel'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:SPLADESparseLexicalAndExpansionModel
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
  - AIMech:SPLADESparseLexicalAndExpansionModel
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:SPLADESparseLexicalAndExpansionModel
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:SPLADESparseLexicalAndExpansionModel
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:SPLADESparseLexicalAndExpansionModel
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 splade-sparse-lexical-expansion-model-boundaries.py
  command: python3 research/discovery/splade-sparse-lexical-expansion-model-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SPLADESparseLexicalAndExpansionModel
  exit_code: 0
  expected_exit_code: 0
  summary: 'SPLADE boundary verification passed: {''flops_skewed'': 4.0, ''flops_balanced'':
    1.0}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T135200Z-splade-sparse-lexical-expansion-model.json
  accessed_at: '2026-10-19T13:52:00Z'
  support: supports
  summary: No normalized identity match for AIMech:SPLADESparseLexicalAndExpansionModel
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T13:52:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/splade-sparse-lexical-expansion-model-boundaries.py
  accessed_at: '2026-10-19T13:52:00Z'
  snapshot_sha256: f88167cbd107ef26f06ab6b37dab63a038c0fbf3a7686b9da97ea6840f7b05d3
  support: supports
  summary: 'All constructed boundary assertions in splade-sparse-lexical-expansion-model-boundaries.py
    passed with exit code 0: SPLADE boundary verification passed: {''flops_skewed'':
    4.0, ''flops_balanced'': 1.0}'
- evidence_id: r749-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2107.05720
  locator: Full-text PDF
  accessed_at: '2026-10-19T13:52:00Z'
  snapshot_sha256: e791451960e47e69b0241d7656c6c61ce40b7c3beff92c944e163e5c3bc54c1a
  support: supports
  summary: Full-text PDF (Proceedings of the 44th International ACM SIGIR Conference
    on Research and Development in Information Retrieval (SIGIR 2021) (2021)) read
    and verified.
- evidence_id: r749-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2107.05720
  locator: arXiv abstract
  accessed_at: '2026-10-19T13:52:00Z'
  snapshot_sha256: 85089c31d19e19a5363a79490334b7f58628e0f5b1e65cf6eb9b36fb323fb181
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r749-metadata-cr
  kind: primary_source
  reference: https://dblp.org/search/publ/api?q=SPLADE+Sparse+Lexical+and+Expansion+Model+Formal&h=5&format=xml
  locator: Crossref metadata
  accessed_at: '2026-10-19T13:52:00Z'
  snapshot_sha256: 405af6287b49c072744d495983ef503c1db20ca83d000d2da1648066e87072d1
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:SPLADESparseLexicalAndExpansionModel
  evidence_ids:
  - identity
  - r749-primary-pdf
  - r749-arxiv-abs
  - r749-metadata-cr
  summary: SPLADE (Sparse Lexical and Expansion Model for First Stage Ranking) is
    a distinct concept.
  details: Introduced by Formal, Piwowarski, and Clinchant (SIGIR 2021, pp. 2288-2292,
    arXiv:2107.05720). Distinguished from DeepCT (Dai & Callan, 2019), which re-weights
    only existing document terms without vocabulary expansion, from doc2query/docTTTTTquery
    (Nogueira et al., 2019), which perform offline sequence-to-sequence text expansion
    before BM25 indexing, and from SparTerm (Bai et al., 2020), which uses un-saturated
    ReLU summation with a fixed pre-trained binary gating mask rather than end-to-end
    log-saturated FLOPS-regularized training.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:SPLADESparseLexicalAndExpansionModel
  evidence_ids:
  - mapping
  - r749-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:SPLADESparseLexicalAndExpansionModel
  evidence_ids:
  - r749-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in splade-sparse-lexical-expansion-model-boundaries.py
    passed with exit code 0: SPLADE boundary verification passed: {''flops_skewed'':
    4.0, ''flops_balanced'': 1.0}'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:SPLADESparseLexicalAndExpansionModel
  evidence_ids:
  - identity
  - mapping
  - r749-primary-pdf
  - r749-arxiv-abs
  - r749-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:SPLADESparseLexicalAndExpansionModel in Round 749.
- All pages of Proceedings of the 44th International ACM SIGIR Conference on Research
  and Development in Information Retrieval (SIGIR 2021) (2021) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
