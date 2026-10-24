# FiLM parameter-arithmetic validation-curve scope finding

- Review: 20261013T170040Z-film-parameter-arithmetic-validation-curve
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T16:55:31Z
- Finished UTC: 2026-10-13T17:00:40Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor source-scope wording issue in the evaluation limitation.

## Scope And Provenance

Scope of the fine-tuning exclusion statement.

Selection: Exact maintained ID AIMech:FiLMParameterArithmeticInference
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3ddd0cd33930c6dbf5ca76b875149fc97e9ab9b1.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:FiLMParameterArithmeticInference | data/curated/FiLMParameterArithmeticInference.yaml | maintained | FiLM Parameter-Arithmetic Inference |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corrected-input publication gates | skipped | True | AIMech:FiLMParameterArithmeticInference | Correction and its publication gates have not yet run. |

## Scientific And Domain Assessments

### Fine-tuning example exclusion

evidence: concern. Targets: AIMech:FiLMParameterArithmeticInference.

Limit exclusion wording to the documented validation curve.

The restricted-generalization-evaluation claim says validation comparisons exclude all 30,000 fine-tuning examples. Figure 9’s caption explicitly attaches this exclusion to its validation-accuracy curve and separately describes the table. The broader wording exceeds the caption’s explicit scope; narrow it to the curve without asserting a different table protocol.

## Findings

### F1: Limit fine-tuning exclusion wording to the documented validation curve

minor / open / confirmed; issue key: film-parameter-arithmetic-validation-curve-scope.

The restricted-generalization-evaluation claim says validation comparisons exclude all 30,000 fine-tuning examples. Figure 9’s caption explicitly attaches this exclusion to its validation-accuracy curve and separately describes the table. The broader wording exceeds the caption’s explicit scope; narrow it to the curve without asserting a different table protocol.

## Recommended Actions And Acceptance Checks

### A1

Narrow the maintained claim, synchronize report, append history, recapture and reassess.

- Claim names the Figure 9 validation-accuracy curve.
- Corrected record/report agree and rendered pages are regenerated.
- Corrected-input gates and linked successor review pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/curated/FiLMParameterArithmeticInference.yaml | supports | Complete record read after capture; evaluation limitation uses broader validation comparisons wording. |
| paper | https://arxiv.org/pdf/1709.07871v2; PDF page 9, Figure 9 caption and Section 4.5. | supports | All thirteen pages previously visually read; page 9 visually reread after capture. Caption attaches exclusion to Figure, then describes Table separately. |

## Limits And Additional Notes

- Partial author self-review; DRAFT remains.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T170040Z-film-parameter-arithmetic-validation-curve
kind: record
repository: CultureBotAI/AIMech
title: FiLM parameter-arithmetic validation-curve scope finding
started_at: '2026-10-13T16:55:31Z'
finished_at: '2026-10-13T17:00:40Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Author checked evaluation wording against the primary caption;
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: One minor source-scope wording issue in the evaluation limitation.
source:
  git_revision: 3ddd0cd33930c6dbf5ca76b875149fc97e9ab9b1
  state: working_tree
  inputs:
  - path: data/aio/CompositionalGeneralizationLLM.yaml
    sha256: f2d1f09f316234e5a801870f24d8d6a58b21567bbcc5d22928923a833f04fb0f
    role: context
  - path: data/aio/KnowledgeTransfer.yaml
    sha256: d9c3efd84c05da8efb7b8eb46e15d64a1ea18fd0816c96cba9bcad85619c57bb
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/ReasoningLLM.yaml
    sha256: 5ceb143da4d5ac2c3bdc430596e21d48943caaa848ae20abf92c791d69a90bfd
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/aio/ZeroShotLearningLLM.yaml
    sha256: 41c8d572a51fdd2603b29c5af6ed7ab4dde2b7459223b21d89dea6a7636b396c
    role: context
  - path: data/aio/ZeroshotLearning.yaml
    sha256: c728c0a1c5fc27ae9e7a05437071108a66ef7784a2eab5d8952100960ac0f3ec
    role: context
  - path: data/curated/AttentionBasedConfigurableConvolutionalNeuralNetwork.yaml
    sha256: 9023f81f517d8ab9656429a53a74f9fc57d1c23c29fb3286b9662cb2e20a5f46
    role: context
  - path: data/curated/DynamicMemoryNetwork.yaml
    sha256: 0affc6bdf4fd1c02c6d423d8560b53d357f5eca0ec8d93d29176375da25636fe
    role: context
  - path: data/curated/FeatureWiseLinearModulation.yaml
    sha256: 04cdbed7b9a44ec4fc4c98b2dd6971a1fb6e4fc2c133926febe9411423836b63
    role: context
  - path: data/curated/FiLMParameterArithmeticInference.yaml
    sha256: 8c16daf0c2434ce91f9dffd601133bad98d27e2f45232512285aa1de8822e10e
    role: target
  - path: research/discovery/20261013T165529Z-film-parameter-arithmetic-inference.json
    sha256: b04ba9ba87c14b021a1096587194a17ef8a153f757def1ebf811d31174d8d7aa
    role: context
  - path: research/discovery/film-parameter-arithmetic-boundaries.py
    sha256: 4dd7a2e418501be08b4ccc2e3f3db71be5f048ec0c3b079d8e0ec68c2c46c412
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
- target_id: AIMech:FiLMParameterArithmeticInference
  path: data/curated/FiLMParameterArithmeticInference.yaml
  label: FiLM Parameter-Arithmetic Inference
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FiLMParameterArithmeticInference.yaml
    role: maintained
scope:
  description: Scope of the fine-tuning exclusion statement.
  selection: Exact maintained ID AIMech:FiLMParameterArithmeticInference
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - AIMech:FiLMParameterArithmeticInference
  exclusions:
  - target: Corrected-input complete review
    reason: Pending correction and publication gates.
checks:
- check_id: corrected-publication
  name: Corrected-input publication gates
  status: skipped
  required: true
  target_ids:
  - AIMech:FiLMParameterArithmeticInference
  summary: Correction and its publication gates have not yet run.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/curated/FiLMParameterArithmeticInference.yaml
  accessed_at: '2026-10-13T17:00:40Z'
  snapshot_sha256: 8c16daf0c2434ce91f9dffd601133bad98d27e2f45232512285aa1de8822e10e
  support: supports
  summary: Complete record read after capture; evaluation limitation uses broader
    validation comparisons wording.
- evidence_id: paper
  kind: primary_source
  reference: https://arxiv.org/pdf/1709.07871v2
  accessed_at: '2026-10-13T14:50:22Z'
  snapshot_sha256: 765acea6f2a78b1d76961392099cd0af49cb2e7d6f06d0b3d82f1dbe9cdcd363
  support: supports
  locator: PDF page 9, Figure 9 caption and Section 4.5.
  summary: All thirteen pages previously visually read; page 9 visually reread after
    capture. Caption attaches exclusion to Figure, then describes Table separately.
assessments:
- assessment_id: curve-scope
  area: evidence
  topic: Fine-tuning example exclusion
  outcome: concern
  target_ids:
  - AIMech:FiLMParameterArithmeticInference
  evidence_ids:
  - record
  - paper
  summary: Limit exclusion wording to the documented validation curve.
  details: The restricted-generalization-evaluation claim says validation comparisons
    exclude all 30,000 fine-tuning examples. Figure 9’s caption explicitly attaches
    this exclusion to its validation-accuracy curve and separately describes the table.
    The broader wording exceeds the caption’s explicit scope; narrow it to the curve
    without asserting a different table protocol.
findings:
- finding_id: F1
  issue_key: film-parameter-arithmetic-validation-curve-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Limit fine-tuning exclusion wording to the documented validation curve
  description: The restricted-generalization-evaluation claim says validation comparisons
    exclude all 30,000 fine-tuning examples. Figure 9’s caption explicitly attaches
    this exclusion to its validation-accuracy curve and separately describes the table.
    The broader wording exceeds the caption’s explicit scope; narrow it to the curve
    without asserting a different table protocol.
  target_ids:
  - AIMech:FiLMParameterArithmeticInference
  field_paths:
  - claims[restricted-generalization-evaluation].statement
  evidence_ids:
  - record
  - paper
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FiLMParameterArithmeticInference.yaml
    role: maintained
actions:
- action_id: A1
  description: Narrow the maintained claim, synchronize report, append history, recapture
    and reassess.
  finding_ids:
  - F1
  target_ids:
  - AIMech:FiLMParameterArithmeticInference
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FiLMParameterArithmeticInference.yaml
    role: maintained
  acceptance_checks:
  - Claim names the Figure 9 validation-accuracy curve.
  - Corrected record/report agree and rendered pages are regenerated.
  - Corrected-input gates and linked successor review pass.
limitations:
- Partial author self-review; DRAFT remains.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- validation-scope
```
