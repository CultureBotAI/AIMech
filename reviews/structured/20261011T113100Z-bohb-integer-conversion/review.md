# BOHB draft count-formula self-review

- Review: 20261011T113100Z-bohb-integer-conversion
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T11:29:00Z
- Finished UTC: 2026-10-11T11:31:00Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One bounded source-transcription defect requires correction before publication.

## Scope And Provenance

The pinned bracket-count implementation claim of BOHB.

Selection: Exact maintained record and claim field.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 2f52990807e09e4f9b6fd0c498200ba6e549a76d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:BOHB | data/curated/BOHB.yaml | maintained | BOHB |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original finite bracket-count diagnostic | passed | True | AIMech:BOHB | {"product": 15.625, "implemented_count": 15} |

## Scientific And Domain Assessments

### Implemented configuration count versus untruncated product

consistency: concern. Targets: AIMech:BOHB.

The source has an outer conversion needed for noninteger reduction factors; the draft’s common eta3 example masks its omission.

## Findings

### bohb-integer-conversion: BOHB draft omits the final integer conversion in its pinned count formula.

minor / open / confirmed; issue key: CultureBotAI-AIMech-BOHB-outer-integer-conversion.

The uncommitted draft gives floor((s_max+1)/(s+1))*eta^s without the outer int conversion in the cited implementation. Noninteger eta can therefore produce a noninteger purported configuration count. Correct the transcription and add a diagnostic distinguishing the product from the implemented count. The method identity and main branch are unaffected.

## Recommended Actions And Acceptance Checks

### correct-integer-conversion

Correct the source count transcription, extend the original diagnostic, update ledger/history and save a successor review.

- For eta2.5, s_max4 and s3, distinguish the product15.625 from the implemented integer count15.
- Preserve the paper/implementation convention distinction and pass required repository checks.
- Save a successor disposition referencing this exact finding and issue68.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| pinned-code | https://raw.githubusercontent.com/automl/HpBandSter/0ec0ce23448ae7f27c0868b35a7086bc6d0fba2a/hpbandster/optimizers/bohb.py; Lines46–50 and135–141, especially outer int conversion on line138 | refutes | The source documents eta as a float and uses int(floor(max_SH_iter/(s+1))*eta**s). The draft omits the outer integer conversion; with s_max4, s3 and eta2.5, the product is15.625 but the count is15. |
| draft-record | data/curated/BOHB.yaml; claims[claim_id=pinned-implementation].statement | context_only | The draft reproduces the floor factor but omits the final integer conversion. Its eta3 diagnostic cannot expose this difference. |

## Limits And Additional Notes

- This is a partial scientific self-review of one implementation claim, not approval of the full batch.
- The required full gate is still in progress; the initial vendored check failed on sandbox DNS and passed after a network-enabled retry. No gate result is invented here.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T113100Z-bohb-integer-conversion
kind: record
repository: CultureBotAI/AIMech
title: BOHB draft count-formula self-review
started_at: '2026-10-11T11:29:00Z'
finished_at: '2026-10-11T11:31:00Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent compared its draft mathematical transcription
    against the pinned author source. This is not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: One bounded source-transcription defect requires correction before publication.
source:
  git_revision: 2f52990807e09e4f9b6fd0c498200ba6e549a76d
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/EnsembleLearning.yaml
    sha256: cf9435e5a799d84072222190c2d681c53b22bf9e7094891405008ebe398a39ed
    role: context
  - path: data/aio/EvolutionaryLLM.yaml
    sha256: d3db6adea3d8d58096c9fb5abef67273489ee719ab900b2d4adbb129e4f7362f
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/Preprocessing.yaml
    sha256: 2c4a30f4f829a757be1feabf78d15780eedf93681a62eede3e76b2304f21bb7a
    role: context
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
    role: context
  - path: data/aio/ReinforcementLearningLLM.yaml
    sha256: e386376b9b1a9c78349d66e8609a655e273620d8bc607978c728ac3b7ce3808a
    role: context
  - path: data/aio/SupervisedLearning.yaml
    sha256: 472f033f91a14c8727e525ddd30f82fcaf16a2514fa8f062667fb94fc9c9b718
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/curated/BOHB.yaml
    sha256: 1ad26b0f71fa86698ee00c434cf06590dafc5fe958bc42d84c6bec5003a0c563
    role: target
  - path: data/curated/GaussianProcessRegression.yaml
    sha256: d83d0de4a152e7db689636928f41eb5d3663281285585d835f2a5535403d6a0d
    role: context
  - path: data/curated/GeneticAlgorithm.yaml
    sha256: d40bf1a03e29a3ca6bf88f6553f18c6b1559baf56da6a21d63b54163f4752ceb
    role: context
  - path: data/curated/GridSearchFairClassification.yaml
    sha256: 2c39ead283f70921f413eaba9f53f05ac26675b77c359d690974a23eacec6eb8
    role: context
  - path: data/curated/Hyperband.yaml
    sha256: ed8dae09ccd45becb03f2e0ad41aa4c2898ecafc999e6b2ba9637c7d8b311e56
    role: target
  - path: data/curated/PopulationBasedAugmentation.yaml
    sha256: f15ab39eed88283c4cdf7b85880f4e9169299b95577eb70d9a4afa3fa14703ed
    role: context
  - path: data/curated/PopulationBasedTraining.yaml
    sha256: 4a0fff56bd5ccb2d2b21cea0c533bd0fa83e1601a035b1c0b5dbf796e7e81261
    role: context
  - path: data/curated/RandomSearchHyperparameterOptimization.yaml
    sha256: 24dde2b9d19169c383b403742ea355727c2f167ae8aa21970fbda34e832c89fd
    role: target
  - path: data/curated/TreeStructuredParzenEstimator.yaml
    sha256: bdd8130958b93502ecd3bf0cd73f411dfb4aecb5d6d2ab2e01454dee9bae2737
    role: context
  - path: research/discovery/20261011T112845Z-hyperparameter-search-and-allocation.json
    sha256: 7aef85afa5a031b658f0238a0b8a301547479f8b1ba3ac691037d36833990af2
    role: context
  - path: research/discovery/hyperparameter-search-boundaries.py
    sha256: 991e4bbcf3ccbef14f0d31e49396f45e11dfb4ccc264d217e1a0b310ba144bbc
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
- target_id: AIMech:BOHB
  path: data/curated/BOHB.yaml
  label: BOHB
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BOHB.yaml
    role: maintained
scope:
  description: The pinned bracket-count implementation claim of BOHB.
  selection: Exact maintained record and claim field.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:BOHB
  exclusions:
  - target: Complete record and batch approval
    reason: The full review and required checks will follow the corrected record;
      this finding is limited to one mathematical transcription.
checks:
- check_id: finite-count
  name: Original finite bracket-count diagnostic
  command: 'Python stdlib Fraction arithmetic: (5//4)*Fraction(5,2)**3 and int of
    that product'
  status: passed
  required: true
  target_ids:
  - AIMech:BOHB
  exit_code: 0
  expected_exit_code: 0
  summary: '{"product": 15.625, "implemented_count": 15}'
evidence:
- evidence_id: pinned-code
  kind: primary_source
  reference: https://raw.githubusercontent.com/automl/HpBandSter/0ec0ce23448ae7f27c0868b35a7086bc6d0fba2a/hpbandster/optimizers/bohb.py
  locator: Lines46–50 and135–141, especially outer int conversion on line138
  accessed_at: '2026-10-11T11:25:42Z'
  snapshot_sha256: 23e1345406791add6c67d7b8aab83cc612d56a9016c0e5715f4c4d8bf6ccddf6
  support: refutes
  summary: The source documents eta as a float and uses int(floor(max_SH_iter/(s+1))*eta**s).
    The draft omits the outer integer conversion; with s_max4, s3 and eta2.5, the
    product is15.625 but the count is15.
- evidence_id: draft-record
  kind: record_content
  reference: data/curated/BOHB.yaml
  locator: claims[claim_id=pinned-implementation].statement
  accessed_at: '2026-10-11T11:31:00Z'
  support: context_only
  summary: The draft reproduces the floor factor but omits the final integer conversion.
    Its eta3 diagnostic cannot expose this difference.
assessments:
- assessment_id: integer-conversion
  area: consistency
  topic: Implemented configuration count versus untruncated product
  outcome: concern
  target_ids:
  - AIMech:BOHB
  evidence_ids:
  - pinned-code
  - draft-record
  summary: The source has an outer conversion needed for noninteger reduction factors;
    the draft’s common eta3 example masks its omission.
findings:
- finding_id: bohb-integer-conversion
  issue_key: CultureBotAI-AIMech-BOHB-outer-integer-conversion
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  target_ids:
  - AIMech:BOHB
  field_paths:
  - claims[claim_id=pinned-implementation].statement
  evidence_ids:
  - pinned-code
  - draft-record
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BOHB.yaml
    role: maintained
  title: BOHB draft omits the final integer conversion in its pinned count formula.
  description: The uncommitted draft gives floor((s_max+1)/(s+1))*eta^s without the
    outer int conversion in the cited implementation. Noninteger eta can therefore
    produce a noninteger purported configuration count. Correct the transcription
    and add a diagnostic distinguishing the product from the implemented count. The
    method identity and main branch are unaffected.
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/68
actions:
- action_id: correct-integer-conversion
  finding_ids:
  - bohb-integer-conversion
  target_ids:
  - AIMech:BOHB
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BOHB.yaml
    role: maintained
  description: Correct the source count transcription, extend the original diagnostic,
    update ledger/history and save a successor review.
  acceptance_checks:
  - For eta2.5, s_max4 and s3, distinguish the product15.625 from the implemented
    integer count15.
  - Preserve the paper/implementation convention distinction and pass required repository
    checks.
  - Save a successor disposition referencing this exact finding and issue68.
boundary_decisions: []
limitations:
- This is a partial scientific self-review of one implementation claim, not approval
  of the full batch.
- The required full gate is still in progress; the initial vendored check failed on
  sandbox DNS and passed after a network-enabled retry. No gate result is invented
  here.
links:
- https://github.com/CultureBotAI/AIMech/issues/68
```
