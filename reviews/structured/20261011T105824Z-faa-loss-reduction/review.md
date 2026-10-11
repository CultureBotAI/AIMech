# Source audit of Fast AutoAugment logged-loss reduction

- Review: 20261011T105824Z-faa-loss-reduction
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T10:56:14Z
- Finished UTC: 2026-10-11T10:58:24Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One confirmed source-interpretation defect requires correction before publication.

## Scope And Provenance

The implementation-profile reduction claim of the new Fast AutoAugment draft.

Selection: Exact maintained record and affected claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 39f3cb95076153e00596b3af21c2b91e60acb4a5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:FastAutoAugment | data/curated/FastAutoAugment.yaml | maintained | Fast AutoAugment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Required source, corpus and saved-review checks | skipped | True | AIMech:FastAutoAugment | Deferred until the identified source-interpretation defect is corrected; this is not a passing review. |

## Scientific And Domain Assessments

### Logged loss aggregation

evidence: concern. Targets: AIMech:FastAutoAugment.

Correctness and loss arrays have different dimensions and reductions; the draft conflates them.

## Findings

### faa-loss-reduction: Pinned-code loss reduction was described with the wrong array axis.

major / open / confirmed; issue key: CultureBotAI-AIMech-FastAutoAugment-logged-loss-reduction.

Each unreduced CE array has shape(batch,), so concatenation makes shape(views*batch,), and min(axis=0) is a scalar. For non-singleton batches the logged minus_loss is negative sum of batch-wide minima divided by total example count. It is not the negative mean of per-example best-view CE. The any-view correctness calculation uses shape(views,batch) and remains per-example. The source audit found this error in the newly authored, uncommitted draft; main is unaffected.

## Recommended Actions And Acceptance Checks

### correct-source-reduction

Correct the maintained record and discovery ledger, add a shape-aware finite calculation, and reinspect changed bytes before saving a successor review.

- Trace concatenation, minimum, accumulation and denominator against the pinned files.
- Finite arithmetic distinguishes ordinary mean CE, per-example best-view CE and the batch-global logged score.
- Run required repository gates and save an evidence-backed successor disposition.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| faa-search | https://github.com/kakaobrain/fast-autoaugment/blob/2424224291616a2158a2265069ee95a78a2d13d9/FastAutoAugment/search.py; lines95–133 | refutes | Unreduced cross-entropy arrays concatenate into a single vector; the code takes one minimum per batch. Accumulator sums those scalar minima and divides by total example count. Correctness arrays instead retain a view and example axis. |
| faa-metrics | https://github.com/kakaobrain/fast-autoaugment/blob/2424224291616a2158a2265069ee95a78a2d13d9/FastAutoAugment/metrics.py; Accumulator class, lines49–85 | refutes | Unreduced cross-entropy arrays concatenate into a single vector; the code takes one minimum per batch. Accumulator sums those scalar minima and divides by total example count. Correctness arrays instead retain a view and example axis. |
| draft-record | data/curated/FastAutoAugment.yaml; claims[implementation-profile].statement | context_only | The draft incorrectly states a negative mean of per-example minimum cross-entropy across views. |

## Limits And Additional Notes

- Author self-review of a new draft only; no execution of author code or benchmark result.
- Repository publication gates have not yet been run for this batch; this review identifies a defect rather than approving publication.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T105824Z-faa-loss-reduction
kind: record
repository: CultureBotAI/AIMech
title: Source audit of Fast AutoAugment logged-loss reduction
started_at: '2026-10-11T10:56:14Z'
finished_at: '2026-10-11T10:58:24Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent traced shapes in the pinned source while
    adversarially reviewing its draft. This is not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: One confirmed source-interpretation defect requires correction before publication.
source:
  git_revision: 39f3cb95076153e00596b3af21c2b91e60acb4a5
  state: working_tree
  inputs:
  - path: data/aio/Classification.yaml
    sha256: d97da621c5052c7ab913cda95184ea2cca274f803298fd5f2c1273a22a211219
    role: context
  - path: data/aio/DataAugmentation.yaml
    sha256: e99fd76071e8b52cbe8ed53f694b30093d7fb7a8af2e225f2f158f5cab5f11ae
    role: context
  - path: data/aio/DataEnhancement.yaml
    sha256: 89c2ba48f7ce9c45ed61f6fc7efa3fb416a0d209fd322342d388a8063945fa4f
    role: context
  - path: data/aio/EvolutionaryLLM.yaml
    sha256: d3db6adea3d8d58096c9fb5abef67273489ee719ab900b2d4adbb129e4f7362f
    role: context
  - path: data/aio/GenerativeAdversarialNetworkAugmentedLLM.yaml
    sha256: d3816d7bd1a3f08e85650e82c1fee6091a8ec8635fb26fec429248a5602cc0de
    role: context
  - path: data/aio/ImageAugmentationLayer.yaml
    sha256: b9d1313742a22376bf8de6b48359beb8868e5b312e8b27cb221c6eb73e2252c0
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/Preprocessing.yaml
    sha256: 2c4a30f4f829a757be1feabf78d15780eedf93681a62eede3e76b2304f21bb7a
    role: context
  - path: data/aio/RegularizationLayer.yaml
    sha256: d4280bbc058b841655bcfcea7ef1dd1e05ac5e0211a860045f13eaa30933dbae
    role: context
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
    role: context
  - path: data/aio/SupervisedLearning.yaml
    sha256: 472f033f91a14c8727e525ddd30f82fcaf16a2514fa8f062667fb94fc9c9b718
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/curated/AdaMixUp.yaml
    sha256: 17fe1d86137e8d199f232e6cf1f3e460dd2b5b79631d01e0b2192dba9692fa35
    role: target
  - path: data/curated/AutoAugment.yaml
    sha256: 29dec7588a9f992bb2bdaa71cde95d0bdb4d3a96353337f1149e61fa8099a9c8
    role: context
  - path: data/curated/CTAugment.yaml
    sha256: 65e7e2a863e1498bdcce99c8c2cd1b40e27e4c1cd566cb234e474d9a9b821ab2
    role: context
  - path: data/curated/FastAutoAugment.yaml
    sha256: 7a65762b6c994587a810666b1405ac7b07cfa0d3c59519de94df718c951609be
    role: target
  - path: data/curated/ManifoldMixup.yaml
    sha256: 0df5cfeb08de7758bd9cee4eba3382681f8183f6c37b2da8265e05bd49ddb915
    role: context
  - path: data/curated/MixUp.yaml
    sha256: 2f7e6cd92b02c2b258d3b1be9f541b6aa1593416032fc55da7250821d179a724
    role: context
  - path: data/curated/PopulationBasedAugmentation.yaml
    sha256: f15ab39eed88283c4cdf7b85880f4e9169299b95577eb70d9a4afa3fa14703ed
    role: target
  - path: data/curated/RandAugment.yaml
    sha256: 7519701242b083459bb532442c090d22d7dc812da035990ad34f13802fe8b3c4
    role: context
  - path: data/curated/UnsupervisedDataAugmentation.yaml
    sha256: ff6252f6e7faf47476926ce63b4ef07cb1b644ad211cc3d82fc9f2f1c832699c
    role: context
  - path: research/discovery/20261011T105600Z-adaptive-augmentation-search.json
    sha256: 86fa1e90ec82bacd349c8d5930faba4e9abb6aa07326ab750c985721178fb7b8
    role: context
  - path: research/discovery/adaptive-augmentation-boundaries.py
    sha256: efd2b90cf0c3b478e3c9d83e36f052458106df5205cd96cb717d8644a41539d4
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
- target_id: AIMech:FastAutoAugment
  path: data/curated/FastAutoAugment.yaml
  label: Fast AutoAugment
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FastAutoAugment.yaml
    role: maintained
scope:
  description: The implementation-profile reduction claim of the new Fast AutoAugment
    draft.
  selection: Exact maintained record and affected claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:FastAutoAugment
  exclusions:
  - target: Other records and full implementation execution
    reason: This is a scoped source-shape audit; publication gates and final full-batch
      review follow the correction.
checks:
- check_id: publication-gates
  name: Required source, corpus and saved-review checks
  command: just check
  status: skipped
  required: true
  target_ids:
  - AIMech:FastAutoAugment
  summary: Deferred until the identified source-interpretation defect is corrected;
    this is not a passing review.
evidence:
- evidence_id: faa-search
  kind: primary_source
  reference: https://github.com/kakaobrain/fast-autoaugment/blob/2424224291616a2158a2265069ee95a78a2d13d9/FastAutoAugment/search.py
  locator: lines95–133
  accessed_at: '2026-10-11T10:51:59Z'
  snapshot_sha256: adc734216013b6612de7fcb83147851b3a66298d291c4f5e24f96f5e6ffadb1f
  support: refutes
  summary: Unreduced cross-entropy arrays concatenate into a single vector; the code
    takes one minimum per batch. Accumulator sums those scalar minima and divides
    by total example count. Correctness arrays instead retain a view and example axis.
- evidence_id: faa-metrics
  kind: primary_source
  reference: https://github.com/kakaobrain/fast-autoaugment/blob/2424224291616a2158a2265069ee95a78a2d13d9/FastAutoAugment/metrics.py
  locator: Accumulator class, lines49–85
  accessed_at: '2026-10-11T10:56:43Z'
  snapshot_sha256: e719b40f593b891b02ab11a98a192a4524f9c4056a40b5ef99e73f4bf62a0a3c
  support: refutes
  summary: Unreduced cross-entropy arrays concatenate into a single vector; the code
    takes one minimum per batch. Accumulator sums those scalar minima and divides
    by total example count. Correctness arrays instead retain a view and example axis.
- evidence_id: draft-record
  kind: record_content
  reference: data/curated/FastAutoAugment.yaml
  locator: claims[implementation-profile].statement
  accessed_at: '2026-10-11T10:58:24Z'
  support: context_only
  summary: The draft incorrectly states a negative mean of per-example minimum cross-entropy
    across views.
assessments:
- assessment_id: source-reduction
  area: evidence
  topic: Logged loss aggregation
  outcome: concern
  target_ids:
  - AIMech:FastAutoAugment
  evidence_ids:
  - faa-search
  - faa-metrics
  - draft-record
  summary: Correctness and loss arrays have different dimensions and reductions; the
    draft conflates them.
findings:
- finding_id: faa-loss-reduction
  issue_key: CultureBotAI-AIMech-FastAutoAugment-logged-loss-reduction
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  target_ids:
  - AIMech:FastAutoAugment
  field_paths:
  - claims[implementation-profile].statement
  evidence_ids:
  - faa-search
  - faa-metrics
  - draft-record
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FastAutoAugment.yaml
    role: maintained
  title: Pinned-code loss reduction was described with the wrong array axis.
  description: Each unreduced CE array has shape(batch,), so concatenation makes shape(views*batch,),
    and min(axis=0) is a scalar. For non-singleton batches the logged minus_loss is
    negative sum of batch-wide minima divided by total example count. It is not the
    negative mean of per-example best-view CE. The any-view correctness calculation
    uses shape(views,batch) and remains per-example. The source audit found this error
    in the newly authored, uncommitted draft; main is unaffected.
actions:
- action_id: correct-source-reduction
  finding_ids:
  - faa-loss-reduction
  target_ids:
  - AIMech:FastAutoAugment
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FastAutoAugment.yaml
    role: maintained
  description: Correct the maintained record and discovery ledger, add a shape-aware
    finite calculation, and reinspect changed bytes before saving a successor review.
  acceptance_checks:
  - Trace concatenation, minimum, accumulation and denominator against the pinned
    files.
  - Finite arithmetic distinguishes ordinary mean CE, per-example best-view CE and
    the batch-global logged score.
  - Run required repository gates and save an evidence-backed successor disposition.
boundary_decisions: []
limitations:
- Author self-review of a new draft only; no execution of author code or benchmark
  result.
- Repository publication gates have not yet been run for this batch; this review identifies
  a defect rather than approving publication.
links:
- https://github.com/CultureBotAI/AIMech/issues/63
```
