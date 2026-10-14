# Author self-review of two preliminary Brandes source notes

- Review: 20261014T035231Z-brandes-proof-reading
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-14T03:52:16Z
- Finished UTC: 2026-10-14T03:52:31Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Two preliminary discovery notes misidentify a correctly printed ratio as inverted. Correct this curator misreading before using it as concept evidence.

## Scope And Provenance

Only the embedded Brandes source-discrepancy assertion in the two named discovery reports.

Selection: Exact source_analysis.reading.context_reading.brandes.source_discrepancy fields.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base f2fe23fddacc70eebe898916adebc38bf6f4a1e1.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| research:20261014T024328Z-chakrabarti-focused-crawler | research/discovery/20261014T024328Z-chakrabarti-focused-crawler.json # source_analysis.reading.context_reading.brandes.source_discrepancy | maintained | 20261014T024328Z-chakrabarti-focused-crawler |
| research:20261014T024330Z-relevance-weighted-topic-distillation | research/discovery/20261014T024330Z-relevance-weighted-topic-distillation.json # source_analysis.reading.context_reading.brandes.source_discrepancy | maintained | 20261014T024330Z-relevance-weighted-topic-distillation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Report bytes, JSON and source identity | passed | True | research:20261014T024328Z-chakrabarti-focused-crawler, research:20261014T024330Z-relevance-weighted-topic-distillation | Both reports parse, captured input hashes agree, and both refer to the same fully inspected Brandes PDF. |

## Scientific And Domain Assessments

### Primary equation transcription

provenance: concern. Targets: research:20261014T024328Z-chakrabarti-focused-crawler, research:20261014T024330Z-relevance-weighted-topic-distillation.

Both source-discrepancy claims are unsupported by the actual printed fraction.

## Findings

### proof-ratio-reading: Correct the preliminary Brandes ratio reading

minor / open / confirmed; issue key: brandes-proof-ratio-reading.

Both report notes allege that the proof prose reverses sigma(s,v)/sigma(s,w). The rendered source uses the correct ratio. The maintained notes need correction with provenance of the earlier misreading.

## Recommended Actions And Acceptance Checks

### correct-reading

Correct both note fields, retain the earlier wording in a marked correction record, append actual history and save a linked successor after checking the source and publication gates.

- Both current note fields state the correctly printed sigma(s,v)/sigma(s,w).
- Correction metadata identifies the previous misreading, current evidence and actual UTC edit time.
- A successor preserves the issue key and both affected targets; full publication and canonical checks pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | https://snap.stanford.edu/class/cs224w-readings/brandes01centrality.pdf; PDF/printed pages 7–10, Theorem 6, page 8 proof prose and Algorithm 1. | refutes | The rendered inline fraction on page 8 is sigma(s,v)/sigma(s,w), agreeing with the displayed recurrence and Algorithm 1. A higher-resolution rendering confirms numerator and denominator. The alleged source inconsistency arose from a curator misreading. |
| occurrences | research/; reviews/; data/; pages/ | supports | The sentence occurs in the two named JSON report fields. No other occurrence was returned in these searched trees; unrelated ratio phrases were not claimed exhaustively assessed. |

## Limits And Additional Notes

- This is a bounded source-reading review, not a new scientific review of either crawler or distillation record.
- No author implementation or benchmark was run; no claim of a Brandes paper or software defect is supported.
- Two initial document validations rejected an unsupported evidence enum and a manual inspection encoded as a command without an exit code. The unsaved author input now uses refutes and identifies the manual check correctly; no schema or saved review was changed.
- An initial save refused the previous working-tree base after the preceding PR merged. The current base was captured anew, all unchanged input hashes compared, and both note fields and the primary equation reread before this replacement unsaved observation. No saved bundle was overwritten.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T035231Z-brandes-proof-reading
kind: batch
repository: CultureBotAI/AIMech
title: Author self-review of two preliminary Brandes source notes
started_at: '2026-10-14T03:52:16Z'
finished_at: '2026-10-14T03:52:31Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author rechecked a previous source interpretation against
    the rendered primary equation; this is not independent review.
skill: aimech-add-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Two preliminary discovery notes misidentify a correctly printed ratio as
  inverted. Correct this curator misreading before using it as concept evidence.
source:
  git_revision: f2fe23fddacc70eebe898916adebc38bf6f4a1e1
  state: working_tree
  inputs:
  - path: research/discovery/20261014T024328Z-chakrabarti-focused-crawler.json
    sha256: f46c21799af3e2a69a1e96ec57d231e766d80bc0e74c3ce0fd1afd1c2facbacf
    role: target
  - path: research/discovery/20261014T024330Z-relevance-weighted-topic-distillation.json
    sha256: 927f679d47db843fe86b8972c1a23da90fae9b1c09295b57e3a13517c61da58b
    role: target
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
targets:
- target_id: research:20261014T024328Z-chakrabarti-focused-crawler
  path: research/discovery/20261014T024328Z-chakrabarti-focused-crawler.json
  label: 20261014T024328Z-chakrabarti-focused-crawler
  kind: maintained
  selector: source_analysis.reading.context_reading.brandes.source_discrepancy
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261014T024328Z-chakrabarti-focused-crawler.json
    role: maintained
- target_id: research:20261014T024330Z-relevance-weighted-topic-distillation
  path: research/discovery/20261014T024330Z-relevance-weighted-topic-distillation.json
  label: 20261014T024330Z-relevance-weighted-topic-distillation
  kind: maintained
  selector: source_analysis.reading.context_reading.brandes.source_discrepancy
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261014T024330Z-relevance-weighted-topic-distillation.json
    role: maintained
scope:
  description: Only the embedded Brandes source-discrepancy assertion in the two named
    discovery reports.
  selection: Exact source_analysis.reading.context_reading.brandes.source_discrepancy
    fields.
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - research:20261014T024328Z-chakrabarti-focused-crawler
  - research:20261014T024330Z-relevance-weighted-topic-distillation
  exclusions:
  - target: Other report claims and associated curated crawler/distillation records
    reason: Not scientifically rereviewed; this finding concerns a preliminary neighboring-method
      note only.
checks:
- check_id: report-inputs
  name: Report bytes, JSON and source identity
  status: passed
  required: true
  target_ids:
  - research:20261014T024328Z-chakrabarti-focused-crawler
  - research:20261014T024330Z-relevance-weighted-topic-distillation
  summary: Both reports parse, captured input hashes agree, and both refer to the
    same fully inspected Brandes PDF.
  scope_note: Manual evidence assessment supported by parsing and byte comparisons;
    this is not a named CLI acceptance command.
evidence:
- evidence_id: primary
  kind: primary_source
  reference: https://snap.stanford.edu/class/cs224w-readings/brandes01centrality.pdf
  locator: PDF/printed pages 7–10, Theorem 6, page 8 proof prose and Algorithm 1.
  accessed_at: '2026-10-14T02:04:11Z'
  snapshot_sha256: a4af39425ef88fc83ce71dde1d300c2ec9fd2f5e15fb0ba006a7a7d20260818f
  support: refutes
  summary: The rendered inline fraction on page 8 is sigma(s,v)/sigma(s,w), agreeing
    with the displayed recurrence and Algorithm 1. A higher-resolution rendering confirms
    numerator and denominator. The alleged source inconsistency arose from a curator
    misreading.
- evidence_id: occurrences
  kind: search
  reference: research/; reviews/; data/; pages/
  accessed_at: '2026-10-14T03:52:16Z'
  support: supports
  search_scope: Ignored- and hidden-inclusive fixed-string search of all four repository
    trees for the exact erroneous sentence.
  summary: The sentence occurs in the two named JSON report fields. No other occurrence
    was returned in these searched trees; unrelated ratio phrases were not claimed
    exhaustively assessed.
assessments:
- assessment_id: ratio-reading
  area: provenance
  topic: Primary equation transcription
  outcome: concern
  target_ids:
  - research:20261014T024328Z-chakrabarti-focused-crawler
  - research:20261014T024330Z-relevance-weighted-topic-distillation
  evidence_ids:
  - primary
  - occurrences
  summary: Both source-discrepancy claims are unsupported by the actual printed fraction.
findings:
- finding_id: proof-ratio-reading
  issue_key: brandes-proof-ratio-reading
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the preliminary Brandes ratio reading
  description: Both report notes allege that the proof prose reverses sigma(s,v)/sigma(s,w).
    The rendered source uses the correct ratio. The maintained notes need correction
    with provenance of the earlier misreading.
  target_ids:
  - research:20261014T024328Z-chakrabarti-focused-crawler
  - research:20261014T024330Z-relevance-weighted-topic-distillation
  field_paths:
  - source_analysis.reading.context_reading.brandes.source_discrepancy
  evidence_ids:
  - primary
  - occurrences
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261014T024328Z-chakrabarti-focused-crawler.json
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261014T024330Z-relevance-weighted-topic-distillation.json
    role: maintained
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/340
actions:
- action_id: correct-reading
  description: Correct both note fields, retain the earlier wording in a marked correction
    record, append actual history and save a linked successor after checking the source
    and publication gates.
  finding_ids:
  - proof-ratio-reading
  target_ids:
  - research:20261014T024328Z-chakrabarti-focused-crawler
  - research:20261014T024330Z-relevance-weighted-topic-distillation
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261014T024328Z-chakrabarti-focused-crawler.json
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261014T024330Z-relevance-weighted-topic-distillation.json
    role: maintained
  acceptance_checks:
  - Both current note fields state the correctly printed sigma(s,v)/sigma(s,w).
  - Correction metadata identifies the previous misreading, current evidence and actual
    UTC edit time.
  - A successor preserves the issue key and both affected targets; full publication
    and canonical checks pass.
limitations:
- This is a bounded source-reading review, not a new scientific review of either crawler
  or distillation record.
- No author implementation or benchmark was run; no claim of a Brandes paper or software
  defect is supported.
- Two initial document validations rejected an unsupported evidence enum and a manual
  inspection encoded as a command without an exit code. The unsaved author input now
  uses refutes and identifies the manual check correctly; no schema or saved review
  was changed.
- An initial save refused the previous working-tree base after the preceding PR merged.
  The current base was captured anew, all unchanged input hashes compared, and both
  note fields and the primary equation reread before this replacement unsaved observation.
  No saved bundle was overwritten.
links:
- https://github.com/CultureBotAI/AIMech/issues/340
tags:
- self-review
- source-correction
```
