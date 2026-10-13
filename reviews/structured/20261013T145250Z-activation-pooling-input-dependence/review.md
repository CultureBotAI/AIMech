# Activation-value pooling nonlinearity finding

- Review: 20261013T145250Z-activation-pooling-input-dependence
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T14:51:06Z
- Finished UTC: 2026-10-13T14:52:50Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor nonlinearity-explanation inconsistency; the detailed claim already gives the correct input-dependent mechanism.

## Scope And Provenance

Cause and scope of nonlinearity in the limitations summary.

Selection: Exact maintained ID AIMech:ActivationValueGaussianPooling
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base cb7b73403f37eada1e7d30137cbb040faf30f5d7.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ActivationValueGaussianPooling | data/curated/ActivationValueGaussianPooling.yaml | maintained | Activation-Value Gaussian Pooling |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corrected-input publication gates | skipped | True | AIMech:ActivationValueGaussianPooling | Corrected inputs do not yet exist; pre-correction checks do not validate them. |

## Scientific And Domain Assessments

### Cause of nonlinear aggregation

evidence: concern. Targets: AIMech:ActivationValueGaussianPooling.

Attribute nonlinear aggregation to input-dependent weights and preserve the linear zero-precision limit.

The limitations field says trainable weights make pooling nonlinear. Trainability alone is neither the defining cause nor sufficient: a learned fixed weighted sum is linear, and beta=0 gives an arithmetic mean. Here nonlinear aggregation generally arises from weights depending on input activation values, even after learned parameters are fixed. Align this summary with the already qualified precision-limits-and-nonlinearity claim and constructed scaling counterexample.

## Findings

### F1: Attribute pooling nonlinearity to input dependence

minor / open / confirmed; issue key: activation-pooling-input-dependence.

The limitations field says trainable weights make pooling nonlinear. Trainability alone is neither the defining cause nor sufficient: a learned fixed weighted sum is linear, and beta=0 gives an arithmetic mean. Here nonlinear aggregation generally arises from weights depending on input activation values, even after learned parameters are fixed. Align this summary with the already qualified precision-limits-and-nonlinearity claim and constructed scaling counterexample.

## Recommended Actions And Acceptance Checks

### A1

Correct the limitation, synchronize the report, append history, recapture and reassess.

- The limitation names input dependence and states general nonlinearity even with fixed parameters.
- Corrected-input gates and successor review pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/curated/ActivationValueGaussianPooling.yaml | supports | Complete record read after capture; one limitation attributes nonlinearity to trainability rather than input-dependent weights. |
| paper | https://arxiv.org/pdf/1603.09630v2; SectionIII-B, PDFpage3, Equations5–8; constructed activation-gaussian-pooling-boundaries.py scaling and zero-precision examples. | supports | Complete eleven-page primary paper visually read; pages3–8 reread after capture. Equations7–8 make weights depend on input values; beta=0 gives the mean. |

## Limits And Additional Notes

- Partial author self-review; DRAFT remains.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T145250Z-activation-pooling-input-dependence
kind: record
repository: CultureBotAI/AIMech
title: Activation-value pooling nonlinearity finding
started_at: '2026-10-13T14:51:06Z'
finished_at: '2026-10-13T14:52:50Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Author challenged the nonlinearity explanation against equations
    and counterexamples; not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: One minor nonlinearity-explanation inconsistency; the detailed claim already
  gives the correct input-dependent mechanism.
source:
  git_revision: cb7b73403f37eada1e7d30137cbb040faf30f5d7
  state: working_tree
  inputs:
  - path: data/aio/LPPool1DLayer.yaml
    sha256: 5ffd0db4838efd447eebc325435b5712dfd9c4f81706aa895cc652087f098819
    role: context
  - path: data/aio/LPPool2DLayer.yaml
    sha256: c5dc28f53ee24d6668e48f99d9013117914608ee01761d7fc1a4139d9cbdf9c8
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/PoolingLayer.yaml
    sha256: 2a5cc182b52109a337a926a42bd715d5f1142e2a0876a8bfbc41890846e84246
    role: context
  - path: data/curated/ActivationValueGaussianPooling.yaml
    sha256: d580f4e783f45ee0bc6a07945a33e4dc94046d6bba7205da34a76eadb9e97099
    role: target
  - path: data/curated/GaussianDifferentiablePooling.yaml
    sha256: 85ea11fb153f768aa31eaf690df7769e3696fb0f7be80a86650dcf564bf1a900
    role: context
  - path: data/curated/LearnedNormPoolingUnit.yaml
    sha256: fb36da3270a145c8813181b645d14efff155cc08999e17f49a67e49a4d156337
    role: context
  - path: data/curated/StochasticPooling.yaml
    sha256: 5e70a56403aae673f3d0d41f0a4c2bc546335b54d948c229e44c1d2e7d7458ad
    role: context
  - path: research/discovery/20261013T145054Z-activation-value-gaussian-pooling.json
    sha256: 912f5477ab5fc0fe8ee596d4956bbaa7f3b805d094de65defa2bd612fd451f08
    role: context
  - path: research/discovery/activation-gaussian-pooling-boundaries.py
    sha256: c90721141dbc535fbd7f9bc740c393b277f474c6cd2bc6890a7ccca6527eac43
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
- target_id: AIMech:ActivationValueGaussianPooling
  path: data/curated/ActivationValueGaussianPooling.yaml
  label: Activation-Value Gaussian Pooling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ActivationValueGaussianPooling.yaml
    role: maintained
scope:
  description: Cause and scope of nonlinearity in the limitations summary.
  selection: Exact maintained ID AIMech:ActivationValueGaussianPooling
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - AIMech:ActivationValueGaussianPooling
  exclusions:
  - target: Corrected-input complete scientific review
    reason: Pending correction and final gates.
checks:
- check_id: corrected-publication
  name: Corrected-input publication gates
  status: skipped
  required: true
  target_ids:
  - AIMech:ActivationValueGaussianPooling
  summary: Corrected inputs do not yet exist; pre-correction checks do not validate
    them.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/curated/ActivationValueGaussianPooling.yaml
  accessed_at: '2026-10-13T14:52:50Z'
  snapshot_sha256: d580f4e783f45ee0bc6a07945a33e4dc94046d6bba7205da34a76eadb9e97099
  support: supports
  summary: Complete record read after capture; one limitation attributes nonlinearity
    to trainability rather than input-dependent weights.
- evidence_id: paper
  kind: primary_source
  reference: https://arxiv.org/pdf/1603.09630v2
  accessed_at: '2026-10-13T14:20:35Z'
  snapshot_sha256: 9cbd9b822c6e709284e32b2b083ba3ffa86f8595fe6e34d1f7652f747f9e68dc
  support: supports
  locator: SectionIII-B, PDFpage3, Equations5–8; constructed activation-gaussian-pooling-boundaries.py
    scaling and zero-precision examples.
  summary: Complete eleven-page primary paper visually read; pages3–8 reread after
    capture. Equations7–8 make weights depend on input values; beta=0 gives the mean.
assessments:
- assessment_id: input-dependence
  area: evidence
  topic: Cause of nonlinear aggregation
  outcome: concern
  target_ids:
  - AIMech:ActivationValueGaussianPooling
  evidence_ids:
  - record
  - paper
  summary: Attribute nonlinear aggregation to input-dependent weights and preserve
    the linear zero-precision limit.
  details: 'The limitations field says trainable weights make pooling nonlinear. Trainability
    alone is neither the defining cause nor sufficient: a learned fixed weighted sum
    is linear, and beta=0 gives an arithmetic mean. Here nonlinear aggregation generally
    arises from weights depending on input activation values, even after learned parameters
    are fixed. Align this summary with the already qualified precision-limits-and-nonlinearity
    claim and constructed scaling counterexample.'
findings:
- finding_id: F1
  issue_key: activation-pooling-input-dependence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Attribute pooling nonlinearity to input dependence
  description: 'The limitations field says trainable weights make pooling nonlinear.
    Trainability alone is neither the defining cause nor sufficient: a learned fixed
    weighted sum is linear, and beta=0 gives an arithmetic mean. Here nonlinear aggregation
    generally arises from weights depending on input activation values, even after
    learned parameters are fixed. Align this summary with the already qualified precision-limits-and-nonlinearity
    claim and constructed scaling counterexample.'
  target_ids:
  - AIMech:ActivationValueGaussianPooling
  field_paths:
  - limitations[1]
  evidence_ids:
  - record
  - paper
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ActivationValueGaussianPooling.yaml
    role: maintained
actions:
- action_id: A1
  description: Correct the limitation, synchronize the report, append history, recapture
    and reassess.
  finding_ids:
  - F1
  target_ids:
  - AIMech:ActivationValueGaussianPooling
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ActivationValueGaussianPooling.yaml
    role: maintained
  acceptance_checks:
  - The limitation names input dependence and states general nonlinearity even with
    fixed parameters.
  - Corrected-input gates and successor review pass.
limitations:
- Partial author self-review; DRAFT remains.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- input-dependence
```
