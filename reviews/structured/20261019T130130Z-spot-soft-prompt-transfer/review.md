# Scientific author self-review of SPoT (Soft Prompt Transfer)

- Review: 20261019T130130Z-spot-soft-prompt-transfer
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T13:01:00Z
- Finished UTC: 2026-10-19T13:01:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain SPoT (Soft Prompt Transfer) as a distinct DRAFT algorithm. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/SPoTSoftPromptTransfer.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:SPoTSoftPromptTransfer
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base cf366267dc8eeee224e64a765b06ef7821cbf7d3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SPoTSoftPromptTransfer | data/curated/SPoTSoftPromptTransfer.yaml | maintained | SPoT (Soft Prompt Transfer) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:SPoTSoftPromptTransfer | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:SPoTSoftPromptTransfer | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:SPoTSoftPromptTransfer | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:SPoTSoftPromptTransfer | Validated history sidecar files. |
| python3 spot-soft-prompt-transfer-boundaries.py | passed | True | AIMech:SPoTSoftPromptTransfer | [PASS] SPoT boundary verification passed: reduction_ratio=26855.5x, s_tok=(0.9985&gt;0.9404&gt;0.2829), alphas=[0.515, 0.485], mse_top1=0.00018 &lt; mse_spot_wavg=0.00680 &lt;&lt; mse_scratch=0.34499 |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:SPoTSoftPromptTransfer.

SPoT (Soft Prompt Transfer) is a distinct concept.

Introduced by Tu Vu, Brian Lester, Noah Constant, Rami Al-Rfou, and Daniel Cer (ACL 2022, arXiv:2110.07904). Distinct from vanilla Prompt Tuning (Lester et al., EMNLP 2021; AIMech Round 675), which initializes soft prompts from sampled vocabulary or class-label tokens directly on each target task without cross-task prompt transfer or prompt-based task embedding retrieval. Both generic SPoT (transferring a single multi-task or single-task source prompt to all target tasks) and targeted SPoT (retrieving top-k source prompts from a prompt library via Average-Token or Per-Token Average Cosine Similarity of 10K-step prompt checkpoints using Best of Top-k, Top-k Weighted Average, or Top-k Multi-task Mixture) are lumping-cohesive variants within this single record.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:SPoTSoftPromptTransfer.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:SPoTSoftPromptTransfer.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in spot-soft-prompt-transfer-boundaries.py passed with exit code 0: [PASS] SPoT boundary verification passed: reduction_ratio=26855.5x, s_tok=(0.9985&gt;0.9404&gt;0.2829), alphas=[0.515, 0.485], mse_top1=0.00018 &lt; mse_spot_wavg=0.00680 &lt;&lt; mse_scratch=0.34499

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:SPoTSoftPromptTransfer.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T130100Z-spot-soft-prompt-transfer.json | supports | No normalized identity match for AIMech:SPoTSoftPromptTransfer across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/spot-soft-prompt-transfer-boundaries.py | supports | All constructed boundary assertions in spot-soft-prompt-transfer-boundaries.py passed with exit code 0: [PASS] SPoT boundary verification passed: reduction_ratio=26855.5x, s_tok=(0.9985&gt;0.9404&gt;0.2829), alphas=[0.515, 0.485], mse_top1=0.00018 &lt; mse_spot_wavg=0.00680 &lt;&lt; mse_scratch=0.34499 |
| r698-primary-pdf | https://arxiv.org/pdf/2110.07904.pdf; Full-text PDF | supports | Full-text PDF (Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL 2022) (2022)) read and verified. |
| r698-arxiv-abs | https://arxiv.org/abs/2110.07904; arXiv abstract | supports | arXiv abstract read and verified. |
| r698-metadata-cr | https://dblp.org/search/publ/api?q=SPoT+Better+Frozen+Model+Adaptation+through+Soft+Prompt+Transfer&amp;format=xml; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:SPoTSoftPromptTransfer in Round 698.
- All pages of Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (ACL 2022) (2022) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T130130Z-spot-soft-prompt-transfer
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of SPoT (Soft Prompt Transfer)
started_at: '2026-10-19T13:01:00Z'
finished_at: '2026-10-19T13:01:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:SPoTSoftPromptTransfer
    against existing AIMech and AIO records and verified all claims against Proceedings
    of the 60th Annual Meeting of the Association for Computational Linguistics (ACL
    2022) (2022) and pure-Python boundary checks. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain SPoT (Soft Prompt Transfer) as a distinct DRAFT algorithm. All three
  claims are supported by full-text primary evidence and pure-Python boundary verification.
source:
  git_revision: cf366267dc8eeee224e64a765b06ef7821cbf7d3
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/SPoTSoftPromptTransfer.yaml
    sha256: ee8669280e1a99850841143e455760bb7fe18a526893d9528b318473b7473d08
    role: target
  - path: research/discovery/20261019T130100Z-spot-soft-prompt-transfer.json
    sha256: 1658fc8a7abdfe3b1a676ed47505bab4460793a7f24eb47208dbc868a9956a23
    role: context
  - path: research/discovery/spot-soft-prompt-transfer-boundaries.py
    sha256: 601f5955c143fca730f8e50e0a50a18827c25c71a085fd492f3d1b5ec717b26e
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
- target_id: AIMech:SPoTSoftPromptTransfer
  path: data/curated/SPoTSoftPromptTransfer.yaml
  label: SPoT (Soft Prompt Transfer)
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SPoTSoftPromptTransfer.yaml
    role: maintained
scope:
  description: All fields of data/curated/SPoTSoftPromptTransfer.yaml and its primary
    evidence.
  selection: 'Exact maintained ID: AIMech:SPoTSoftPromptTransfer'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:SPoTSoftPromptTransfer
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
  - AIMech:SPoTSoftPromptTransfer
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:SPoTSoftPromptTransfer
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:SPoTSoftPromptTransfer
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:SPoTSoftPromptTransfer
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 spot-soft-prompt-transfer-boundaries.py
  command: python3 research/discovery/spot-soft-prompt-transfer-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SPoTSoftPromptTransfer
  exit_code: 0
  expected_exit_code: 0
  summary: '[PASS] SPoT boundary verification passed: reduction_ratio=26855.5x, s_tok=(0.9985>0.9404>0.2829),
    alphas=[0.515, 0.485], mse_top1=0.00018 < mse_spot_wavg=0.00680 << mse_scratch=0.34499'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T130100Z-spot-soft-prompt-transfer.json
  accessed_at: '2026-10-19T13:01:00Z'
  support: supports
  summary: No normalized identity match for AIMech:SPoTSoftPromptTransfer across AIO
    and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T13:01:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/spot-soft-prompt-transfer-boundaries.py
  accessed_at: '2026-10-19T13:01:00Z'
  snapshot_sha256: 601f5955c143fca730f8e50e0a50a18827c25c71a085fd492f3d1b5ec717b26e
  support: supports
  summary: 'All constructed boundary assertions in spot-soft-prompt-transfer-boundaries.py
    passed with exit code 0: [PASS] SPoT boundary verification passed: reduction_ratio=26855.5x,
    s_tok=(0.9985>0.9404>0.2829), alphas=[0.515, 0.485], mse_top1=0.00018 < mse_spot_wavg=0.00680
    << mse_scratch=0.34499'
- evidence_id: r698-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2110.07904.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T13:01:00Z'
  snapshot_sha256: 3f5883a38122b162c89b7c82b23ac769982749f32599a816d7f79f4bc37ed458
  support: supports
  summary: Full-text PDF (Proceedings of the 60th Annual Meeting of the Association
    for Computational Linguistics (ACL 2022) (2022)) read and verified.
- evidence_id: r698-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2110.07904
  locator: arXiv abstract
  accessed_at: '2026-10-19T13:01:00Z'
  snapshot_sha256: 8e98e6708015d4226292f7a52305474c688c74e2197964197121afdfb1245a44
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r698-metadata-cr
  kind: primary_source
  reference: https://dblp.org/search/publ/api?q=SPoT+Better+Frozen+Model+Adaptation+through+Soft+Prompt+Transfer&format=xml
  locator: Crossref metadata
  accessed_at: '2026-10-19T13:01:00Z'
  snapshot_sha256: 75581cad4e0531377d1fd65da01d7aa48154094a7935cdd4fc838e7a8f183a90
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:SPoTSoftPromptTransfer
  evidence_ids:
  - identity
  - r698-primary-pdf
  - r698-arxiv-abs
  - r698-metadata-cr
  summary: SPoT (Soft Prompt Transfer) is a distinct concept.
  details: Introduced by Tu Vu, Brian Lester, Noah Constant, Rami Al-Rfou, and Daniel
    Cer (ACL 2022, arXiv:2110.07904). Distinct from vanilla Prompt Tuning (Lester
    et al., EMNLP 2021; AIMech Round 675), which initializes soft prompts from sampled
    vocabulary or class-label tokens directly on each target task without cross-task
    prompt transfer or prompt-based task embedding retrieval. Both generic SPoT (transferring
    a single multi-task or single-task source prompt to all target tasks) and targeted
    SPoT (retrieving top-k source prompts from a prompt library via Average-Token
    or Per-Token Average Cosine Similarity of 10K-step prompt checkpoints using Best
    of Top-k, Top-k Weighted Average, or Top-k Multi-task Mixture) are lumping-cohesive
    variants within this single record.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:SPoTSoftPromptTransfer
  evidence_ids:
  - mapping
  - r698-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:SPoTSoftPromptTransfer
  evidence_ids:
  - r698-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in spot-soft-prompt-transfer-boundaries.py
    passed with exit code 0: [PASS] SPoT boundary verification passed: reduction_ratio=26855.5x,
    s_tok=(0.9985>0.9404>0.2829), alphas=[0.515, 0.485], mse_top1=0.00018 < mse_spot_wavg=0.00680
    << mse_scratch=0.34499'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:SPoTSoftPromptTransfer
  evidence_ids:
  - identity
  - mapping
  - r698-primary-pdf
  - r698-arxiv-abs
  - r698-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:SPoTSoftPromptTransfer in Round 698.
- All pages of Proceedings of the 60th Annual Meeting of the Association for Computational
  Linguistics (ACL 2022) (2022) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
