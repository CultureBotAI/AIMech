# Partial author self-review of KADABRA conference citation locators

- Review: 20261014T070041Z-kadabra-conference-locators
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-14T06:54:54Z
- Finished UTC: 2026-10-14T07:00:41Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Both additional conference-paper definition citations use locations from the extended manuscript. The specific conference locators need correction; the arXiv citations and concept mechanisms remain supported.

## Scope And Provenance

Conference-paper definition locators in both new KADABRA records and their report mirrors.

Selection: Both maintained KADABRA records introduced on this branch.
Coverage: partial; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base 7289b51273d1a39c08286b8e044eb52cbd68b1bd.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:KADABRAAdaptiveBetweenness | data/curated/KADABRAAdaptiveBetweenness.yaml | maintained | KADABRA adaptive betweenness approximation |
| AIMech:KADABRABalancedBidirectionalPathSampling | data/curated/KADABRABalancedBidirectionalPathSampling.yaml | maintained | KADABRA balanced bidirectional shortest-path sampling |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Captured input and mirror inspection | passed | True | AIMech:KADABRAAdaptiveBetweenness, AIMech:KADABRABalancedBidirectionalPathSampling | The seven captured input SHA-256 values match the inspected bytes. Both erroneous definition locators were read and compared with the conference pages. |
| Ignored-inclusive prior-key search | passed | True | AIMech:KADABRAAdaptiveBetweenness, AIMech:KADABRABalancedBidirectionalPathSampling | No prior observation uses this new same-defect issue key; ignored and hidden review bundles were included. |
| Final just check | skipped | True | AIMech:KADABRAAdaptiveBetweenness, AIMech:KADABRABalancedBidirectionalPathSampling | A pre-correction gate is running; the final gate will be rerun after the citation corrections. |

## Scientific And Domain Assessments

### Version-specific conference pagination

provenance: concern. Targets: AIMech:KADABRAAdaptiveBetweenness, AIMech:KADABRABalancedBidirectionalPathSampling.

Two local citation locators have been copied across differently paginated paper versions. Correct the conference fields while preserving the already appropriate arXiv references.

## Findings

### conference-definition-locators: Use the conference version’s actual definition locations

minor / open / confirmed; issue key: kadabra-conference-definition-locators.

The estimator conference definition locator incorrectly names Appendix C and early pages; the sampler points to pp.20:6–20:7 although Section4 is on pp.20:10–20:11. Correct both maintained fields and synchronized report entries. This is a curation citation defect, not a source-paper defect.

## Recommended Actions And Acceptance Checks

### correct-locators

Correct both conference locators, preserve correction provenance and history, reassess current records and save a same-key successor retaining both targets.

- Both conference citations point to the inspected content in that exact PDF version.
- Record/report mirrors and the sampler’s changed estimator context hash agree; actual correction history is saved.
- Required publication checks pass and the successor preserves the exact finding predecessor and both affected targets.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| records | data/curated/KADABRAAdaptiveBetweenness.yaml; Both captured records: definition_evidence[source_id=borassinatal2016esa] | supports | The estimator currently cites conference pp.20:4–20:6 and a nonexistent Appendix C at pp.20:14–20:15; the sampler cites Section4 at pp.20:6–20:7. The reports mirror these fields. |
| conference | https://drops.dagstuhl.de/storage/00lipics/lipics-vol057-esa2016/LIPIcs.ESA.2016.20/LIPIcs.ESA.2016.20.pdf; Section2 and Algorithms1–3, printed pp.20:5–20:7; proof pp.20:7–20:9; Section4 pp.20:10–20:11 | supports | Text and rendered conference pages place the estimator and its proof on pp.20:5–20:9 and path sampling in Section4 on pp.20:10–20:11. The shorter conference version has no Appendix C at the cited locations; pp.20:14–20:15 are experimental figures. |

## Limits And Additional Notes

- Partial author self-review; no independent approval.
- A final publication gate is pending after correction. The existing primary arXiv citations and mechanism assessments are not invalidated by this locator defect.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T070041Z-kadabra-conference-locators
kind: batch
repository: CultureBotAI/AIMech
title: Partial author self-review of KADABRA conference citation locators
started_at: '2026-10-14T06:54:54Z'
finished_at: '2026-10-14T07:00:41Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author compared both maintained definition citations with
    the paginated conference PDF. This is author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: Both additional conference-paper definition citations use locations from
  the extended manuscript. The specific conference locators need correction; the arXiv
  citations and concept mechanisms remain supported.
source:
  git_revision: 7289b51273d1a39c08286b8e044eb52cbd68b1bd
  state: working_tree
  inputs:
  - path: data/curated/KADABRAAdaptiveBetweenness.yaml
    sha256: b4428d08bde8a193dbc034cef85b0ea47cc93a3bf9f134d386271862357641b3
    role: target
  - path: data/curated/KADABRABalancedBidirectionalPathSampling.yaml
    sha256: 6f26831ebf464de94a0926282c12b7406ce654fac9e200bbe1465d7df53593fb
    role: target
  - path: research/discovery/20261014T064041Z-kadabra-adaptive-betweenness.json
    sha256: b64fc65c1be3b3263872d01f405735cf8f5764aedabaa888dddb855fd44a2d90
    role: context
  - path: research/discovery/20261014T064339Z-kadabra-balanced-path-sampling.json
    sha256: fbae126f01970a7badd29eb2a2b379c0bba87a4aeda10c627939e671f6c4829c
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/aimech/curated.py
    sha256: 67cc03d7def5f62490cc1f5db320a7c18fdfd41cebf43a35ad2bb88c32cd40d5
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: a4b7e2f0327eb784d2c5b98c713534f644adf3a7848d4e3c2995e772425725c4
    role: context
targets:
- target_id: AIMech:KADABRAAdaptiveBetweenness
  path: data/curated/KADABRAAdaptiveBetweenness.yaml
  label: KADABRA adaptive betweenness approximation
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/KADABRAAdaptiveBetweenness.yaml
    role: maintained
- target_id: AIMech:KADABRABalancedBidirectionalPathSampling
  path: data/curated/KADABRABalancedBidirectionalPathSampling.yaml
  label: KADABRA balanced bidirectional shortest-path sampling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/KADABRABalancedBidirectionalPathSampling.yaml
    role: maintained
scope:
  description: Conference-paper definition locators in both new KADABRA records and
    their report mirrors.
  selection: Both maintained KADABRA records introduced on this branch.
  coverage: partial
  population_size: 2
  reviewed_target_ids:
  - AIMech:KADABRAAdaptiveBetweenness
  - AIMech:KADABRABalancedBidirectionalPathSampling
  exclusions:
  - target: Complete scientific record reviews
    reason: Separate full record reviews will follow corrections and publication checks.
checks:
- check_id: capture
  name: Captured input and mirror inspection
  status: passed
  required: true
  target_ids:
  - AIMech:KADABRAAdaptiveBetweenness
  - AIMech:KADABRABalancedBidirectionalPathSampling
  summary: The seven captured input SHA-256 values match the inspected bytes. Both
    erroneous definition locators were read and compared with the conference pages.
- check_id: lineage-search
  name: Ignored-inclusive prior-key search
  command: rg --no-ignore --hidden -n -F kadabra-conference-definition-locators reviews/structured
  status: passed
  required: true
  target_ids:
  - AIMech:KADABRAAdaptiveBetweenness
  - AIMech:KADABRABalancedBidirectionalPathSampling
  exit_code: 1
  expected_exit_code: 1
  summary: No prior observation uses this new same-defect issue key; ignored and hidden
    review bundles were included.
- check_id: full-gate
  name: Final just check
  command: just check
  status: skipped
  required: true
  target_ids:
  - AIMech:KADABRAAdaptiveBetweenness
  - AIMech:KADABRABalancedBidirectionalPathSampling
  summary: A pre-correction gate is running; the final gate will be rerun after the
    citation corrections.
evidence:
- evidence_id: records
  kind: record_content
  reference: data/curated/KADABRAAdaptiveBetweenness.yaml
  locator: 'Both captured records: definition_evidence[source_id=borassinatal2016esa]'
  accessed_at: '2026-10-14T07:00:41Z'
  support: supports
  summary: The estimator currently cites conference pp.20:4–20:6 and a nonexistent
    Appendix C at pp.20:14–20:15; the sampler cites Section4 at pp.20:6–20:7. The
    reports mirror these fields.
- evidence_id: conference
  kind: primary_source
  reference: https://drops.dagstuhl.de/storage/00lipics/lipics-vol057-esa2016/LIPIcs.ESA.2016.20/LIPIcs.ESA.2016.20.pdf
  locator: Section2 and Algorithms1–3, printed pp.20:5–20:7; proof pp.20:7–20:9; Section4
    pp.20:10–20:11
  accessed_at: '2026-10-14T05:42:44Z'
  snapshot_sha256: c73bb488b2adef340a3a17dcc412090f488d7411920a2f95917a51227ad00a50
  support: supports
  summary: Text and rendered conference pages place the estimator and its proof on
    pp.20:5–20:9 and path sampling in Section4 on pp.20:10–20:11. The shorter conference
    version has no Appendix C at the cited locations; pp.20:14–20:15 are experimental
    figures.
assessments:
- assessment_id: version-locators
  area: provenance
  topic: Version-specific conference pagination
  outcome: concern
  target_ids:
  - AIMech:KADABRAAdaptiveBetweenness
  - AIMech:KADABRABalancedBidirectionalPathSampling
  evidence_ids:
  - records
  - conference
  summary: Two local citation locators have been copied across differently paginated
    paper versions. Correct the conference fields while preserving the already appropriate
    arXiv references.
findings:
- finding_id: conference-definition-locators
  issue_key: kadabra-conference-definition-locators
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Use the conference version’s actual definition locations
  description: The estimator conference definition locator incorrectly names Appendix
    C and early pages; the sampler points to pp.20:6–20:7 although Section4 is on
    pp.20:10–20:11. Correct both maintained fields and synchronized report entries.
    This is a curation citation defect, not a source-paper defect.
  target_ids:
  - AIMech:KADABRAAdaptiveBetweenness
  - AIMech:KADABRABalancedBidirectionalPathSampling
  field_paths:
  - definition_evidence
  evidence_ids:
  - records
  - conference
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/KADABRAAdaptiveBetweenness.yaml
    role: maintained
  - repository: CultureBotAI/AIMech
    path: data/curated/KADABRABalancedBidirectionalPathSampling.yaml
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261014T064041Z-kadabra-adaptive-betweenness.json
    role: report mirror
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261014T064339Z-kadabra-balanced-path-sampling.json
    role: report mirror
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/348
actions:
- action_id: correct-locators
  description: Correct both conference locators, preserve correction provenance and
    history, reassess current records and save a same-key successor retaining both
    targets.
  finding_ids:
  - conference-definition-locators
  target_ids:
  - AIMech:KADABRAAdaptiveBetweenness
  - AIMech:KADABRABalancedBidirectionalPathSampling
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/KADABRAAdaptiveBetweenness.yaml
    role: maintained
  - repository: CultureBotAI/AIMech
    path: data/curated/KADABRABalancedBidirectionalPathSampling.yaml
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261014T064041Z-kadabra-adaptive-betweenness.json
    role: report mirror
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261014T064339Z-kadabra-balanced-path-sampling.json
    role: report mirror
  acceptance_checks:
  - Both conference citations point to the inspected content in that exact PDF version.
  - Record/report mirrors and the sampler’s changed estimator context hash agree;
    actual correction history is saved.
  - Required publication checks pass and the successor preserves the exact finding
    predecessor and both affected targets.
limitations:
- Partial author self-review; no independent approval.
- A final publication gate is pending after correction. The existing primary arXiv
  citations and mechanism assessments are not invalidated by this locator defect.
links:
- https://github.com/CultureBotAI/AIMech/issues/348
tags:
- self-review
- citation-correction
```
