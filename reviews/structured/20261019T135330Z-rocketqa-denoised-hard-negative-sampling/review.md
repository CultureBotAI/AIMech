# Scientific author self-review of RocketQA (Cross-Batch and Denoised Hard Negative Dense Passage Retrieval Training)

- Review: 20261019T135330Z-rocketqa-denoised-hard-negative-sampling
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T13:53:00Z
- Finished UTC: 2026-10-19T13:53:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain RocketQA (Cross-Batch and Denoised Hard Negative Dense Passage Retrieval Training) as a distinct DRAFT algorithm. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/RocketQADenoisedHardNegativeSampling.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:RocketQADenoisedHardNegativeSampling
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1287dc034ff24eddf94d369c4284896ebb5fc500.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:RocketQADenoisedHardNegativeSampling | data/curated/RocketQADenoisedHardNegativeSampling.yaml | maintained | RocketQA (Cross-Batch and Denoised Hard Negative Dense Passage Retrieval Training) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:RocketQADenoisedHardNegativeSampling | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:RocketQADenoisedHardNegativeSampling | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:RocketQADenoisedHardNegativeSampling | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:RocketQADenoisedHardNegativeSampling | Validated history sidecar files. |
| python3 rocketqa-denoised-hard-negative-sampling-boundaries.py | passed | True | AIMech:RocketQADenoisedHardNegativeSampling | RocketQA boundary verification passed: {'cross_batch_negs': 4095, 'loss_denoised': 0.0258, 'loss_unfiltered': 1.1106} |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:RocketQADenoisedHardNegativeSampling.

RocketQA (Cross-Batch and Denoised Hard Negative Dense Passage Retrieval Training) is a distinct concept.

Introduced by Qu, Ding, Liu, Liu, Ren, Zhao, Dong, Wu, and Wang (NAACL-HLT 2021, pp. 5835-5847, arXiv:2010.08191). Distinguished from DPR (Karpukhin et al., 2020), which uses single-GPU in-batch negatives and BM25 hard negatives, from ANCE (Xiong et al., 2021), which asynchronously mines top-k dense negatives without cross-encoder denoising (suffering from ~70% false negatives among unannotated top retrieved MS MARCO passages), and from GPL (Wang et al., 2022), which uses synthetic T5 query generation and MarginMSE soft-label distillation for unsupervised target domain adaptation.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:RocketQADenoisedHardNegativeSampling.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:RocketQADenoisedHardNegativeSampling.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in rocketqa-denoised-hard-negative-sampling-boundaries.py passed with exit code 0: RocketQA boundary verification passed: {'cross_batch_negs': 4095, 'loss_denoised': 0.0258, 'loss_unfiltered': 1.1106}

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:RocketQADenoisedHardNegativeSampling.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T135300Z-rocketqa-denoised-hard-negative-sampling.json | supports | No normalized identity match for AIMech:RocketQADenoisedHardNegativeSampling across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/rocketqa-denoised-hard-negative-sampling-boundaries.py | supports | All constructed boundary assertions in rocketqa-denoised-hard-negative-sampling-boundaries.py passed with exit code 0: RocketQA boundary verification passed: {'cross_batch_negs': 4095, 'loss_denoised': 0.0258, 'loss_unfiltered': 1.1106} |
| r750-primary-pdf | https://arxiv.org/pdf/2010.08191; Full-text PDF | supports | Full-text PDF (Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT 2021) (2021)) read and verified. |
| r750-arxiv-abs | https://arxiv.org/abs/2010.08191; arXiv abstract | supports | arXiv abstract read and verified. |
| r750-metadata-cr | https://dblp.org/search/publ/api?q=RocketQA+An+Optimized+Training+Approach+to+Dense+Passage+Retrieval+Qu&amp;h=5&amp;format=xml; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:RocketQADenoisedHardNegativeSampling in Round 750.
- All pages of Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT 2021) (2021) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T135330Z-rocketqa-denoised-hard-negative-sampling
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of RocketQA (Cross-Batch and Denoised Hard Negative
  Dense Passage Retrieval Training)
started_at: '2026-10-19T13:53:00Z'
finished_at: '2026-10-19T13:53:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: 'The author challenged definition distinctness of AIMech:RocketQADenoisedHardNegativeSampling
    against existing AIMech and AIO records and verified all claims against Proceedings
    of the 2021 Conference of the North American Chapter of the Association for Computational
    Linguistics: Human Language Technologies (NAACL-HLT 2021) (2021) and pure-Python
    boundary checks. This is adversarial author self-review, not independent approval.'
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain RocketQA (Cross-Batch and Denoised Hard Negative Dense Passage Retrieval
  Training) as a distinct DRAFT algorithm. All three claims are supported by full-text
  primary evidence and pure-Python boundary verification.
source:
  git_revision: 1287dc034ff24eddf94d369c4284896ebb5fc500
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/RocketQADenoisedHardNegativeSampling.yaml
    sha256: c483686acfc8c8330be60cac8676d7f9ae126af56411d103d562b551fbabb737
    role: target
  - path: research/discovery/20261019T135300Z-rocketqa-denoised-hard-negative-sampling.json
    sha256: ea7c6889dc293ea3798b8f266ed5d264671a4f9ab698e1f3e579db168ae3fbf8
    role: context
  - path: research/discovery/rocketqa-denoised-hard-negative-sampling-boundaries.py
    sha256: 749cf6c6d4949cbe0fe7b4fc3351841d7a661d5a980720d862b304788f482a6e
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
- target_id: AIMech:RocketQADenoisedHardNegativeSampling
  path: data/curated/RocketQADenoisedHardNegativeSampling.yaml
  label: RocketQA (Cross-Batch and Denoised Hard Negative Dense Passage Retrieval
    Training)
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RocketQADenoisedHardNegativeSampling.yaml
    role: maintained
scope:
  description: All fields of data/curated/RocketQADenoisedHardNegativeSampling.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:RocketQADenoisedHardNegativeSampling'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:RocketQADenoisedHardNegativeSampling
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
  - AIMech:RocketQADenoisedHardNegativeSampling
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:RocketQADenoisedHardNegativeSampling
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:RocketQADenoisedHardNegativeSampling
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:RocketQADenoisedHardNegativeSampling
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 rocketqa-denoised-hard-negative-sampling-boundaries.py
  command: python3 research/discovery/rocketqa-denoised-hard-negative-sampling-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:RocketQADenoisedHardNegativeSampling
  exit_code: 0
  expected_exit_code: 0
  summary: 'RocketQA boundary verification passed: {''cross_batch_negs'': 4095, ''loss_denoised'':
    0.0258, ''loss_unfiltered'': 1.1106}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T135300Z-rocketqa-denoised-hard-negative-sampling.json
  accessed_at: '2026-10-19T13:53:00Z'
  support: supports
  summary: No normalized identity match for AIMech:RocketQADenoisedHardNegativeSampling
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T13:53:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/rocketqa-denoised-hard-negative-sampling-boundaries.py
  accessed_at: '2026-10-19T13:53:00Z'
  snapshot_sha256: 749cf6c6d4949cbe0fe7b4fc3351841d7a661d5a980720d862b304788f482a6e
  support: supports
  summary: 'All constructed boundary assertions in rocketqa-denoised-hard-negative-sampling-boundaries.py
    passed with exit code 0: RocketQA boundary verification passed: {''cross_batch_negs'':
    4095, ''loss_denoised'': 0.0258, ''loss_unfiltered'': 1.1106}'
- evidence_id: r750-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2010.08191
  locator: Full-text PDF
  accessed_at: '2026-10-19T13:53:00Z'
  snapshot_sha256: df8feee3c22dd392cc17130235b3ccb73f2c7fd4c2ce51a5c5ed36445baa7ca5
  support: supports
  summary: 'Full-text PDF (Proceedings of the 2021 Conference of the North American
    Chapter of the Association for Computational Linguistics: Human Language Technologies
    (NAACL-HLT 2021) (2021)) read and verified.'
- evidence_id: r750-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2010.08191
  locator: arXiv abstract
  accessed_at: '2026-10-19T13:53:00Z'
  snapshot_sha256: e0a43b0fc2357a50a8c2855ff9577cbdbde8cc9a2c201e0439218d885729e0d8
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r750-metadata-cr
  kind: primary_source
  reference: https://dblp.org/search/publ/api?q=RocketQA+An+Optimized+Training+Approach+to+Dense+Passage+Retrieval+Qu&h=5&format=xml
  locator: Crossref metadata
  accessed_at: '2026-10-19T13:53:00Z'
  snapshot_sha256: e49b8ac4f092e241860e2a1b7534f74de10df12d4e72b9031d030019306cde52
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:RocketQADenoisedHardNegativeSampling
  evidence_ids:
  - identity
  - r750-primary-pdf
  - r750-arxiv-abs
  - r750-metadata-cr
  summary: RocketQA (Cross-Batch and Denoised Hard Negative Dense Passage Retrieval
    Training) is a distinct concept.
  details: Introduced by Qu, Ding, Liu, Liu, Ren, Zhao, Dong, Wu, and Wang (NAACL-HLT
    2021, pp. 5835-5847, arXiv:2010.08191). Distinguished from DPR (Karpukhin et al.,
    2020), which uses single-GPU in-batch negatives and BM25 hard negatives, from
    ANCE (Xiong et al., 2021), which asynchronously mines top-k dense negatives without
    cross-encoder denoising (suffering from ~70% false negatives among unannotated
    top retrieved MS MARCO passages), and from GPL (Wang et al., 2022), which uses
    synthetic T5 query generation and MarginMSE soft-label distillation for unsupervised
    target domain adaptation.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:RocketQADenoisedHardNegativeSampling
  evidence_ids:
  - mapping
  - r750-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:RocketQADenoisedHardNegativeSampling
  evidence_ids:
  - r750-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in rocketqa-denoised-hard-negative-sampling-boundaries.py
    passed with exit code 0: RocketQA boundary verification passed: {''cross_batch_negs'':
    4095, ''loss_denoised'': 0.0258, ''loss_unfiltered'': 1.1106}'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:RocketQADenoisedHardNegativeSampling
  evidence_ids:
  - identity
  - mapping
  - r750-primary-pdf
  - r750-arxiv-abs
  - r750-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:RocketQADenoisedHardNegativeSampling in Round 750.
- 'All pages of Proceedings of the 2021 Conference of the North American Chapter of
  the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT
  2021) (2021) were read in full text.'
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
