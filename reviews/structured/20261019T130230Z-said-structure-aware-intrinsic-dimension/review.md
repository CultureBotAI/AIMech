# Scientific author self-review of Structure-Aware Intrinsic Dimension (SAID)

- Review: 20261019T130230Z-said-structure-aware-intrinsic-dimension
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T13:02:00Z
- Finished UTC: 2026-10-19T13:02:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Structure-Aware Intrinsic Dimension (SAID) as a distinct DRAFT algorithm. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/SAIDStructureAwareIntrinsicDimension.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:SAIDStructureAwareIntrinsicDimension
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 588bf046a93e3d29ffe7b128b30e84cdc8411421.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SAIDStructureAwareIntrinsicDimension | data/curated/SAIDStructureAwareIntrinsicDimension.yaml | maintained | Structure-Aware Intrinsic Dimension (SAID) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:SAIDStructureAwareIntrinsicDimension | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:SAIDStructureAwareIntrinsicDimension | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:SAIDStructureAwareIntrinsicDimension | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:SAIDStructureAwareIntrinsicDimension | Validated history sidecar files. |
| python3 said-structure-aware-intrinsic-dimension-boundaries.py | passed | True | AIMech:SAIDStructureAwareIntrinsicDimension | [PASS] SAID boundary verification passed: fwht_err=8.9e-16, mse_SAID=0.0e+00 &lt;&lt; mse_DID=0.2511, bound_RoBERTa_Large(d90=207)=0.7877 &lt; bound_RoBERTa_Base(d90=896)=1.6388 |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:SAIDStructureAwareIntrinsicDimension.

Structure-Aware Intrinsic Dimension (SAID) is a distinct concept.

Introduced by Armen Aghajanyan, Luke Zettlemoyer, and Sonal Gupta (ACL/IJCNLP 2021, pp. 7319-7328, arXiv:2012.13255). Extends the layer-unaware Direct Intrinsic Dimension (DID) objective-landscape subspace method of Li et al. (ICLR 2018, theta^D = theta^D_0 + theta^d M with Fastfood matrix M = H G Pi H B) by trading m subspace parameters for m layer-wise scaling weights lambda_i across m layers so capacity concentrates on task-relevant layers. Both SAID and its layer-unaware baseline DID for pre-trained model fine-tuning are covered together in this record.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:SAIDStructureAwareIntrinsicDimension.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:SAIDStructureAwareIntrinsicDimension.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in said-structure-aware-intrinsic-dimension-boundaries.py passed with exit code 0: [PASS] SAID boundary verification passed: fwht_err=8.9e-16, mse_SAID=0.0e+00 &lt;&lt; mse_DID=0.2511, bound_RoBERTa_Large(d90=207)=0.7877 &lt; bound_RoBERTa_Base(d90=896)=1.6388

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:SAIDStructureAwareIntrinsicDimension.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T130200Z-said-structure-aware-intrinsic-dimension.json | supports | No normalized identity match for AIMech:SAIDStructureAwareIntrinsicDimension across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/said-structure-aware-intrinsic-dimension-boundaries.py | supports | All constructed boundary assertions in said-structure-aware-intrinsic-dimension-boundaries.py passed with exit code 0: [PASS] SAID boundary verification passed: fwht_err=8.9e-16, mse_SAID=0.0e+00 &lt;&lt; mse_DID=0.2511, bound_RoBERTa_Large(d90=207)=0.7877 &lt; bound_RoBERTa_Base(d90=896)=1.6388 |
| r699-primary-pdf | https://arxiv.org/pdf/2012.13255.pdf; Full-text PDF | supports | Full-text PDF (Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (ACL/IJCNLP 2021) (2021)) read and verified. |
| r699-arxiv-abs | https://arxiv.org/abs/2012.13255; arXiv abstract | supports | arXiv abstract read and verified. |
| r699-metadata-cr | https://dblp.org/search/publ/api?q=Intrinsic+Dimensionality+Explains+the+Effectiveness+of+Language+Model+Fine-Tuning&amp;format=xml; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:SAIDStructureAwareIntrinsicDimension in Round 699.
- All pages of Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (ACL/IJCNLP 2021) (2021) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T130230Z-said-structure-aware-intrinsic-dimension
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Structure-Aware Intrinsic Dimension (SAID)
started_at: '2026-10-19T13:02:00Z'
finished_at: '2026-10-19T13:02:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:SAIDStructureAwareIntrinsicDimension
    against existing AIMech and AIO records and verified all claims against Proceedings
    of the 59th Annual Meeting of the Association for Computational Linguistics and
    the 11th International Joint Conference on Natural Language Processing (ACL/IJCNLP
    2021) (2021) and pure-Python boundary checks. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Structure-Aware Intrinsic Dimension (SAID) as a distinct DRAFT algorithm.
  All three claims are supported by full-text primary evidence and pure-Python boundary
  verification.
source:
  git_revision: 588bf046a93e3d29ffe7b128b30e84cdc8411421
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/DimensionalityReduction.yaml
    sha256: 99eb0714b362a98a9e704e5ef2ac370cb7a900fbe97da43de790c3ec67ed812e
    role: context
  - path: data/curated/SAIDStructureAwareIntrinsicDimension.yaml
    sha256: a944bbf812fd0ef20608797275a9330e52bd5d0437f194917912c57befa59e33
    role: target
  - path: research/discovery/20261019T130200Z-said-structure-aware-intrinsic-dimension.json
    sha256: e595fdabfd132ddf5088123fc1ac507cf1530c862f58a1a2ba1877cdc19733ad
    role: context
  - path: research/discovery/said-structure-aware-intrinsic-dimension-boundaries.py
    sha256: 8747165a61a2c2d57f956ef55dfc427fb4f43d60bb5750e53d8dddee383e3261
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
- target_id: AIMech:SAIDStructureAwareIntrinsicDimension
  path: data/curated/SAIDStructureAwareIntrinsicDimension.yaml
  label: Structure-Aware Intrinsic Dimension (SAID)
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SAIDStructureAwareIntrinsicDimension.yaml
    role: maintained
scope:
  description: All fields of data/curated/SAIDStructureAwareIntrinsicDimension.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:SAIDStructureAwareIntrinsicDimension'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:SAIDStructureAwareIntrinsicDimension
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
  - AIMech:SAIDStructureAwareIntrinsicDimension
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:SAIDStructureAwareIntrinsicDimension
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:SAIDStructureAwareIntrinsicDimension
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:SAIDStructureAwareIntrinsicDimension
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 said-structure-aware-intrinsic-dimension-boundaries.py
  command: python3 research/discovery/said-structure-aware-intrinsic-dimension-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SAIDStructureAwareIntrinsicDimension
  exit_code: 0
  expected_exit_code: 0
  summary: '[PASS] SAID boundary verification passed: fwht_err=8.9e-16, mse_SAID=0.0e+00
    << mse_DID=0.2511, bound_RoBERTa_Large(d90=207)=0.7877 < bound_RoBERTa_Base(d90=896)=1.6388'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T130200Z-said-structure-aware-intrinsic-dimension.json
  accessed_at: '2026-10-19T13:02:00Z'
  support: supports
  summary: No normalized identity match for AIMech:SAIDStructureAwareIntrinsicDimension
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T13:02:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/said-structure-aware-intrinsic-dimension-boundaries.py
  accessed_at: '2026-10-19T13:02:00Z'
  snapshot_sha256: 8747165a61a2c2d57f956ef55dfc427fb4f43d60bb5750e53d8dddee383e3261
  support: supports
  summary: 'All constructed boundary assertions in said-structure-aware-intrinsic-dimension-boundaries.py
    passed with exit code 0: [PASS] SAID boundary verification passed: fwht_err=8.9e-16,
    mse_SAID=0.0e+00 << mse_DID=0.2511, bound_RoBERTa_Large(d90=207)=0.7877 < bound_RoBERTa_Base(d90=896)=1.6388'
- evidence_id: r699-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2012.13255.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T13:02:00Z'
  snapshot_sha256: e3205485a4222770dd73705495cbce0a27afdec63d6c21fa27f2a165e7f805f1
  support: supports
  summary: Full-text PDF (Proceedings of the 59th Annual Meeting of the Association
    for Computational Linguistics and the 11th International Joint Conference on Natural
    Language Processing (ACL/IJCNLP 2021) (2021)) read and verified.
- evidence_id: r699-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2012.13255
  locator: arXiv abstract
  accessed_at: '2026-10-19T13:02:00Z'
  snapshot_sha256: f1dfd7354de3dcc566571fbbaa4c32c7ad50e490d4e6680fd0d948319eba87db
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r699-metadata-cr
  kind: primary_source
  reference: https://dblp.org/search/publ/api?q=Intrinsic+Dimensionality+Explains+the+Effectiveness+of+Language+Model+Fine-Tuning&format=xml
  locator: Crossref metadata
  accessed_at: '2026-10-19T13:02:00Z'
  snapshot_sha256: 03438c362be48b5f9007745b156f234e2ff8bc518ecaa1904f81781bf3b7c5fd
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:SAIDStructureAwareIntrinsicDimension
  evidence_ids:
  - identity
  - r699-primary-pdf
  - r699-arxiv-abs
  - r699-metadata-cr
  summary: Structure-Aware Intrinsic Dimension (SAID) is a distinct concept.
  details: Introduced by Armen Aghajanyan, Luke Zettlemoyer, and Sonal Gupta (ACL/IJCNLP
    2021, pp. 7319-7328, arXiv:2012.13255). Extends the layer-unaware Direct Intrinsic
    Dimension (DID) objective-landscape subspace method of Li et al. (ICLR 2018, theta^D
    = theta^D_0 + theta^d M with Fastfood matrix M = H G Pi H B) by trading m subspace
    parameters for m layer-wise scaling weights lambda_i across m layers so capacity
    concentrates on task-relevant layers. Both SAID and its layer-unaware baseline
    DID for pre-trained model fine-tuning are covered together in this record.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:SAIDStructureAwareIntrinsicDimension
  evidence_ids:
  - mapping
  - r699-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:SAIDStructureAwareIntrinsicDimension
  evidence_ids:
  - r699-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in said-structure-aware-intrinsic-dimension-boundaries.py
    passed with exit code 0: [PASS] SAID boundary verification passed: fwht_err=8.9e-16,
    mse_SAID=0.0e+00 << mse_DID=0.2511, bound_RoBERTa_Large(d90=207)=0.7877 < bound_RoBERTa_Base(d90=896)=1.6388'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:SAIDStructureAwareIntrinsicDimension
  evidence_ids:
  - identity
  - mapping
  - r699-primary-pdf
  - r699-arxiv-abs
  - r699-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:SAIDStructureAwareIntrinsicDimension in Round 699.
- All pages of Proceedings of the 59th Annual Meeting of the Association for Computational
  Linguistics and the 11th International Joint Conference on Natural Language Processing
  (ACL/IJCNLP 2021) (2021) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
