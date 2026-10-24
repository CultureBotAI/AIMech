# Scientific author self-review of AdEMAMix (Adaptive EMA Mixture Optimizer)

- Review: 20261019T112030Z-ademamix-adaptive-ema-mixture-optimizer
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T11:20:00Z
- Finished UTC: 2026-10-19T11:20:30Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain AdEMAMix (Adaptive EMA Mixture Optimizer) as a distinct DRAFT algorithm. All three claims are supported by full-text primary evidence and pure-Python boundary verification.

## Scope And Provenance

All fields of data/curated/AdEMAMixAdaptiveEMAMixtureOptimization.yaml and its primary evidence.

Selection: Exact maintained ID: AIMech:AdEMAMixAdaptiveEMAMixtureOptimization
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d70d066fa8928afe886dd7deae2564d36c47238f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:AdEMAMixAdaptiveEMAMixtureOptimization | data/curated/AdEMAMixAdaptiveEMAMixtureOptimization.yaml | maintained | AdEMAMix (Adaptive EMA Mixture Optimizer) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:AdEMAMixAdaptiveEMAMixtureOptimization | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:AdEMAMixAdaptiveEMAMixtureOptimization | Validated curated concept records with 0 errors. |
| aimech seed --check | passed | True | AIMech:AdEMAMixAdaptiveEMAMixtureOptimization | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:AdEMAMixAdaptiveEMAMixtureOptimization | Validated history sidecar files. |
| python3 ademamix-adaptive-ema-mixture-optimizer-boundaries.py | passed | True | AIMech:AdEMAMixAdaptiveEMAMixtureOptimization | [PASS] Round 597 AdEMAMix verified: halflife_lin_err=4.40e-13 (t_half: 5.6-&gt;6930.1), dist_ade=3.7582e-02&lt;&lt;dist_adam=8.5933e-01 |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:AdEMAMixAdaptiveEMAMixtureOptimization.

AdEMAMix (Adaptive EMA Mixture Optimizer) is a distinct concept.

Distinct from standard AdamW in that a single EMA cannot simultaneously assign high weight to recent gradients and non-negligible weight to gradients thousands of steps old; AdEMAMix maintains two separate first-moment buffers m_1 and m_2 (or sets beta_1 = 0 so m_hat_1^(t) = g^(t) without extra memory) and schedules beta_3^(t) = exp(ln(beta_start) ln(beta_3) / ((1 - t/T) ln(beta_3) + (t/T) ln(beta_start))). Distinct from nested-EMA methods (DEMA, AdMeta) which attenuate rather than preserve very old gradients.

### AIO mapping accuracy

grounding: supported. Targets: AIMech:AdEMAMixAdaptiveEMAMixtureOptimization.

AIO mappings accurately situate the concept.

Verified target existence in data/aio/.

### Verification of Claims 1-3 against full-text primary source and boundary script

evidence: supported. Targets: AIMech:AdEMAMixAdaptiveEMAMixtureOptimization.

All three claims are directly supported by full-text theorem/lemma locators and pure-Python verification.

All constructed boundary assertions in ademamix-adaptive-ema-mixture-optimizer-boundaries.py passed with exit code 0: [PASS] Round 597 AdEMAMix verified: halflife_lin_err=4.40e-13 (t_half: 5.6-&gt;6930.1), dist_ade=3.7582e-02&lt;&lt;dist_adam=8.5933e-01

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:AdEMAMixAdaptiveEMAMixtureOptimization.

The full record is consistent; retain DRAFT.

Verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T112000Z-ademamix-adaptive-ema-mixture-optimizer.json | supports | No normalized identity match for AIMech:AdEMAMixAdaptiveEMAMixtureOptimization across AIO and curated corpus. |
| mapping | sources/aio/aio.json | supports | Inspected mapped AIO targets in the pinned AIO snapshot. |
| calculation | research/discovery/ademamix-adaptive-ema-mixture-optimizer-boundaries.py | supports | All constructed boundary assertions in ademamix-adaptive-ema-mixture-optimizer-boundaries.py passed with exit code 0: [PASS] Round 597 AdEMAMix verified: halflife_lin_err=4.40e-13 (t_half: 5.6-&gt;6930.1), dist_ade=3.7582e-02&lt;&lt;dist_adam=8.5933e-01 |
| r597-primary-pdf | https://arxiv.org/pdf/2409.03137.pdf; Full-text PDF | supports | Full-text PDF (13th International Conference on Learning Representations (ICLR 2025) (2025)) read and verified. |
| r597-arxiv-abs | https://arxiv.org/abs/2409.03137; arXiv abstract | supports | arXiv abstract read and verified. |
| r597-metadata-cr | https://dblp.org/rec/conf/iclr/PagliardiniAG25; Crossref metadata | supports | Crossref publication metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:AdEMAMixAdaptiveEMAMixtureOptimization in Round 597.
- All pages of 13th International Conference on Learning Representations (ICLR 2025) (2025) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T112030Z-ademamix-adaptive-ema-mixture-optimizer
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of AdEMAMix (Adaptive EMA Mixture Optimizer)
started_at: '2026-10-19T11:20:00Z'
finished_at: '2026-10-19T11:20:30Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness of AIMech:AdEMAMixAdaptiveEMAMixtureOptimization
    against existing AIMech and AIO records and verified all claims against 13th International
    Conference on Learning Representations (ICLR 2025) (2025) and pure-Python boundary
    checks. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain AdEMAMix (Adaptive EMA Mixture Optimizer) as a distinct DRAFT algorithm.
  All three claims are supported by full-text primary evidence and pure-Python boundary
  verification.
source:
  git_revision: d70d066fa8928afe886dd7deae2564d36c47238f
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/curated/AdEMAMixAdaptiveEMAMixtureOptimization.yaml
    sha256: 2fbe4dddbf9fc9a73b591090df9c6e94ad927b1bf259783767c2b52375ad917a
    role: target
  - path: research/discovery/20261019T112000Z-ademamix-adaptive-ema-mixture-optimizer.json
    sha256: f3b9ef5b7e0a425282a3319159c1f99bb6beccda8993420803d1c4122d8f4f92
    role: context
  - path: research/discovery/ademamix-adaptive-ema-mixture-optimizer-boundaries.py
    sha256: c7bbcdc7f94a7d4760be47dee40cc9a1b8cb69f5023a909274761f5d883a99a0
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
- target_id: AIMech:AdEMAMixAdaptiveEMAMixtureOptimization
  path: data/curated/AdEMAMixAdaptiveEMAMixtureOptimization.yaml
  label: AdEMAMix (Adaptive EMA Mixture Optimizer)
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AdEMAMixAdaptiveEMAMixtureOptimization.yaml
    role: maintained
scope:
  description: All fields of data/curated/AdEMAMixAdaptiveEMAMixtureOptimization.yaml
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:AdEMAMixAdaptiveEMAMixtureOptimization'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:AdEMAMixAdaptiveEMAMixtureOptimization
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
  - AIMech:AdEMAMixAdaptiveEMAMixtureOptimization
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:AdEMAMixAdaptiveEMAMixtureOptimization
  exit_code: 0
  expected_exit_code: 0
  summary: Validated curated concept records with 0 errors.
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:AdEMAMixAdaptiveEMAMixtureOptimization
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:AdEMAMixAdaptiveEMAMixtureOptimization
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 ademamix-adaptive-ema-mixture-optimizer-boundaries.py
  command: python3 research/discovery/ademamix-adaptive-ema-mixture-optimizer-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:AdEMAMixAdaptiveEMAMixtureOptimization
  exit_code: 0
  expected_exit_code: 0
  summary: '[PASS] Round 597 AdEMAMix verified: halflife_lin_err=4.40e-13 (t_half:
    5.6->6930.1), dist_ade=3.7582e-02<<dist_adam=8.5933e-01'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T112000Z-ademamix-adaptive-ema-mixture-optimizer.json
  accessed_at: '2026-10-19T11:20:00Z'
  support: supports
  summary: No normalized identity match for AIMech:AdEMAMixAdaptiveEMAMixtureOptimization
    across AIO and curated corpus.
  search_scope: All maintained/generated IDs, labels, and aliases normalized.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T11:20:00Z'
  support: supports
  summary: Inspected mapped AIO targets in the pinned AIO snapshot.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/ademamix-adaptive-ema-mixture-optimizer-boundaries.py
  accessed_at: '2026-10-19T11:20:00Z'
  snapshot_sha256: c7bbcdc7f94a7d4760be47dee40cc9a1b8cb69f5023a909274761f5d883a99a0
  support: supports
  summary: 'All constructed boundary assertions in ademamix-adaptive-ema-mixture-optimizer-boundaries.py
    passed with exit code 0: [PASS] Round 597 AdEMAMix verified: halflife_lin_err=4.40e-13
    (t_half: 5.6->6930.1), dist_ade=3.7582e-02<<dist_adam=8.5933e-01'
- evidence_id: r597-primary-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/2409.03137.pdf
  locator: Full-text PDF
  accessed_at: '2026-10-19T11:20:00Z'
  snapshot_sha256: f3502dffb8758859fc17f2bdaa113852a0c68c2a9a54c0c83fbe5fc572ce184e
  support: supports
  summary: Full-text PDF (13th International Conference on Learning Representations
    (ICLR 2025) (2025)) read and verified.
- evidence_id: r597-arxiv-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2409.03137
  locator: arXiv abstract
  accessed_at: '2026-10-19T11:20:00Z'
  snapshot_sha256: 6d191babee12f40a07ab1be50f3b822340c1723a6229b7e839906771f6518256
  support: supports
  summary: arXiv abstract read and verified.
- evidence_id: r597-metadata-cr
  kind: primary_source
  reference: https://dblp.org/rec/conf/iclr/PagliardiniAG25
  locator: Crossref metadata
  accessed_at: '2026-10-19T11:20:00Z'
  snapshot_sha256: f4d5fa655e429d10a4b5b726773c7ffb8b0fcb50c458f6e2cdd0c0b9bf90bd1b
  support: supports
  summary: Crossref publication metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:AdEMAMixAdaptiveEMAMixtureOptimization
  evidence_ids:
  - identity
  - r597-primary-pdf
  - r597-arxiv-abs
  - r597-metadata-cr
  summary: AdEMAMix (Adaptive EMA Mixture Optimizer) is a distinct concept.
  details: Distinct from standard AdamW in that a single EMA cannot simultaneously
    assign high weight to recent gradients and non-negligible weight to gradients
    thousands of steps old; AdEMAMix maintains two separate first-moment buffers m_1
    and m_2 (or sets beta_1 = 0 so m_hat_1^(t) = g^(t) without extra memory) and schedules
    beta_3^(t) = exp(ln(beta_start) ln(beta_3) / ((1 - t/T) ln(beta_3) + (t/T) ln(beta_start))).
    Distinct from nested-EMA methods (DEMA, AdMeta) which attenuate rather than preserve
    very old gradients.
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:AdEMAMixAdaptiveEMAMixtureOptimization
  evidence_ids:
  - mapping
  - r597-primary-pdf
  summary: AIO mappings accurately situate the concept.
  details: Verified target existence in data/aio/.
- assessment_id: claims-verification
  area: evidence
  topic: Verification of Claims 1-3 against full-text primary source and boundary
    script
  outcome: supported
  target_ids:
  - AIMech:AdEMAMixAdaptiveEMAMixtureOptimization
  evidence_ids:
  - r597-primary-pdf
  - calculation
  summary: All three claims are directly supported by full-text theorem/lemma locators
    and pure-Python verification.
  details: 'All constructed boundary assertions in ademamix-adaptive-ema-mixture-optimizer-boundaries.py
    passed with exit code 0: [PASS] Round 597 AdEMAMix verified: halflife_lin_err=4.40e-13
    (t_half: 5.6->6930.1), dist_ade=3.7582e-02<<dist_adam=8.5933e-01'
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:AdEMAMixAdaptiveEMAMixtureOptimization
  evidence_ids:
  - identity
  - mapping
  - r597-primary-pdf
  - r597-arxiv-abs
  - r597-metadata-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Curated DRAFT record AIMech:AdEMAMixAdaptiveEMAMixtureOptimization in Round 597.
- All pages of 13th International Conference on Learning Representations (ICLR 2025)
  (2025) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
