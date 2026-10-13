# Fast-dropout primary page locator finding

- Review: 20261013T131528Z-fast-dropout-evidence-locator
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T13:13:11Z
- Finished UTC: 2026-10-13T13:15:28Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor source-page locator finding; the definition and qualified mathematical claims remain supported.

## Scope And Provenance

Sparse-feature evidence page reference in the fast-dropout masked-sum claim.

Selection: Exact maintained ID AIMech:FastDropoutTraining
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 646f2520b634b844eb2a1bdd28ee9576f47fb827.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:FastDropoutTraining | data/curated/FastDropoutTraining.yaml | maintained | Fast Dropout Training |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Corrected-input publication gates | skipped | True | AIMech:FastDropoutTraining | Corrected inputs do not yet exist; pre-correction checks do not validate them. |

## Scientific And Domain Assessments

### Primary source page reference

evidence: concern. Targets: AIMech:FastDropoutTraining.

Correct the sparse-feature prose page reference.

The masked-sum-moments claim cites the sparse-feature limitation in Section6.2 as PDFpage7. The actual Section6.2 prose, including the MPQA sparse-feature Gaussian-assumption caveat, is on PDFpage6; page7 contains the associated results table. The moment formula and qualified claim remain supported. Correct this precise page locator.

## Findings

### F1: Correct fast-dropout sparse-feature page locator

minor / open / confirmed; issue key: fast-dropout-sparse-feature-page-locator.

The masked-sum-moments claim cites the sparse-feature limitation in Section6.2 as PDFpage7. The actual Section6.2 prose, including the MPQA sparse-feature Gaussian-assumption caveat, is on PDFpage6; page7 contains the associated results table. The moment formula and qualified claim remain supported. Correct this precise page locator.

## Recommended Actions And Acceptance Checks

### A1

Correct locators, synchronize the discovery report, append history, recapture and reassess.

- Sparse-feature limitation cites Section6.2 on PDFpage6.
- Corrected-input gates and successor review pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/curated/FastDropoutTraining.yaml | supports | Complete maintained record read after capture; one locator points to the table page instead of the sparse-feature discussion page. |
| paper | https://proceedings.mlr.press/v28/wang13a.pdf; PDF p.6, Section6.2 discussion of sparse MPQA features; compare Table1 on PDFp.7. | supports | The full9-page original paper was read before curation; pages6 and7 were visually reread after capture and the prose/table location difference verified. |

## Limits And Additional Notes

- Partial author self-review; DRAFT remains.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T131528Z-fast-dropout-evidence-locator
kind: record
repository: CultureBotAI/AIMech
title: Fast-dropout primary page locator finding
started_at: '2026-10-13T13:13:11Z'
finished_at: '2026-10-13T13:15:28Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: Author compared maintained evidence locators with primary-page
    headings; not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: One minor source-page locator finding; the definition and qualified mathematical
  claims remain supported.
source:
  git_revision: 646f2520b634b844eb2a1bdd28ee9576f47fb827
  state: working_tree
  inputs:
  - path: data/aio/DropoutLayer.yaml
    sha256: f1d1f2ad44ecf177e8c5d16bf1fb72388712d25f499583feab23e5fb65a71e24
    role: context
  - path: data/aio/GaussianDropoutLayer.yaml
    sha256: d709e2b88e01052b2dbb1a1e3213a79b428c3c1de4acb2e55c875528250d58d2
    role: context
  - path: data/aio/GaussianNoiseLayer.yaml
    sha256: 1d6c203daf9e9a5a450a85a7d7bf6e55bb9bffbeea7ceffcc1a8aefbd9629452
    role: context
  - path: data/aio/RegularizationLayer.yaml
    sha256: d4280bbc058b841655bcfcea7ef1dd1e05ac5e0211a860045f13eaa30933dbae
    role: context
  - path: data/curated/DropConnect.yaml
    sha256: 4785777508a6f24792c7533279a08eb66977144b62a260eb26f1d0fbdad1b356
    role: context
  - path: data/curated/FastDropoutTraining.yaml
    sha256: 61cbedd01395abcec37d55b88bcd4ab67f974622196785272bf7b333a19c5ad5
    role: target
  - path: data/curated/NoisyRectifier.yaml
    sha256: fb65c10663835e61629f05d55866248e00aed07a28cc00eb444499d0f4936f28
    role: context
  - path: data/curated/NormStabilizer.yaml
    sha256: 534daa42c9584cefc836a8e5299b1b61e3e57957f153c3f5a0cd9d4c46202ecb
    role: context
  - path: research/discovery/20261013T131205Z-fast-dropout-training.json
    sha256: 13fe26486b6497b9a6075750f45d6dfb3c074e3fa63d9960a70156d23674200d
    role: context
  - path: research/discovery/fast-dropout-boundaries.py
    sha256: 9c70a1950b6b353e0fa31c472454f9a274eaff149f2b72238c9dae3a9f71dbbd
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
- target_id: AIMech:FastDropoutTraining
  path: data/curated/FastDropoutTraining.yaml
  label: Fast Dropout Training
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FastDropoutTraining.yaml
    role: maintained
scope:
  description: Sparse-feature evidence page reference in the fast-dropout masked-sum
    claim.
  selection: Exact maintained ID AIMech:FastDropoutTraining
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - AIMech:FastDropoutTraining
  exclusions:
  - target: Corrected-input complete scientific review
    reason: Pending correction and final gates.
checks:
- check_id: corrected-publication
  name: Corrected-input publication gates
  status: skipped
  required: true
  target_ids:
  - AIMech:FastDropoutTraining
  summary: Corrected inputs do not yet exist; pre-correction checks do not validate
    them.
evidence:
- evidence_id: record
  kind: record_content
  reference: data/curated/FastDropoutTraining.yaml
  accessed_at: '2026-10-13T13:15:28Z'
  snapshot_sha256: 61cbedd01395abcec37d55b88bcd4ab67f974622196785272bf7b333a19c5ad5
  support: supports
  summary: Complete maintained record read after capture; one locator points to the
    table page instead of the sparse-feature discussion page.
- evidence_id: paper
  kind: primary_source
  reference: https://proceedings.mlr.press/v28/wang13a.pdf
  accessed_at: '2026-10-13T12:55:49Z'
  snapshot_sha256: a5a8f1efb4381963188ad3bcd5e0525d7f95e7106255c1019445ad16f6bb2c63
  support: supports
  locator: PDF p.6, Section6.2 discussion of sparse MPQA features; compare Table1
    on PDFp.7.
  summary: The full9-page original paper was read before curation; pages6 and7 were
    visually reread after capture and the prose/table location difference verified.
assessments:
- assessment_id: section-locators
  area: evidence
  topic: Primary source page reference
  outcome: concern
  target_ids:
  - AIMech:FastDropoutTraining
  evidence_ids:
  - record
  - paper
  summary: Correct the sparse-feature prose page reference.
  details: The masked-sum-moments claim cites the sparse-feature limitation in Section6.2
    as PDFpage7. The actual Section6.2 prose, including the MPQA sparse-feature Gaussian-assumption
    caveat, is on PDFpage6; page7 contains the associated results table. The moment
    formula and qualified claim remain supported. Correct this precise page locator.
findings:
- finding_id: F1
  issue_key: fast-dropout-sparse-feature-page-locator
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct fast-dropout sparse-feature page locator
  description: The masked-sum-moments claim cites the sparse-feature limitation in
    Section6.2 as PDFpage7. The actual Section6.2 prose, including the MPQA sparse-feature
    Gaussian-assumption caveat, is on PDFpage6; page7 contains the associated results
    table. The moment formula and qualified claim remain supported. Correct this precise
    page locator.
  target_ids:
  - AIMech:FastDropoutTraining
  field_paths:
  - claims[claim_id=masked-sum-moments].evidence[0].locator
  evidence_ids:
  - record
  - paper
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FastDropoutTraining.yaml
    role: maintained
actions:
- action_id: A1
  description: Correct locators, synchronize the discovery report, append history,
    recapture and reassess.
  finding_ids:
  - F1
  target_ids:
  - AIMech:FastDropoutTraining
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FastDropoutTraining.yaml
    role: maintained
  acceptance_checks:
  - Sparse-feature limitation cites Section6.2 on PDFpage6.
  - Corrected-input gates and successor review pass.
limitations:
- Partial author self-review; DRAFT remains.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- evidence-locators
```
