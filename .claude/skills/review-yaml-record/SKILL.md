---
name: review-yaml-record
description: Review one AIMech AIConcept against its pinned AIO source and claim evidence, saving structured YAML and rendered Markdown. Use for record review, not ontology editing or source refresh.
---

# Review an AIMech Record

Read [the common review contract](../../../docs/record-reviews.md) at
`docs/record-reviews.md` and the [AIO rubric](../../../docs/record-review-profile.md)
at `docs/record-review-profile.md` before assessing a record. They define the
required saved format, source ownership and evidence criteria.

Resolve the requested AIO ID to exactly one `data/aio/*.yaml` record. Inspect its
actual bytes, the source IRI in `sources/aio/aio.json`, `sources/aio/source.yaml`,
`src/aimech/importer.py`, and `src/aimech/schema/aimech.yaml`. Freeze these inputs
with `scripts/record_review.py inspect` before judging. Use `kind: generated` and
the exact source selector; retain the upstream ontology owner and local importer
owner in targets, findings and actions. Do not hand-edit generated data.

Assess identity, ontology relations, definition and synonym fidelity, reference
support, seed provenance and domain relevance using the profile. Run its required
checks and capture actual results. A structurally valid import does not establish
scientific support. State what was and was not scientifically assessed. Reuse a
finding's stable issue key only for the same defect, with explicit predecessor
references when changing its disposition.

For every resolved review target, ALWAYS save the timestamped structured review
YAML AND its rendered Markdown through the canonical helper's `validate`, `save`
and `check` commands. Save partial or blocked assessments when required evidence
or checks are unavailable; never manufacture a pass or a completed check. A
prose-only chat response is not a finished review. If saving is blocked, report
the blocker and leave the task explicitly incomplete.

Return links to both saved files, the target, verdict, finding counts and limits.
Review does not authorize ontology mutation, source refresh, status promotion,
fabricated curation/history events, paid provider runs or publication.
