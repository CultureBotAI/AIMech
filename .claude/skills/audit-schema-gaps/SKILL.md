---
name: audit-schema-gaps
description: "Systematic gap-and-inconsistency audit for the AIMech LinkML schema, the YAML instance corpus, and the scripts that generate them. Uses existing validation harnesses as diagnostics and saves assessed findings and a prioritized fix backlog as a structured review. Invoke for schema drift, data-quality issues, new bulk migrations, or records silently failing validation."
category: quality
requires_database: false
requires_internet: false
version: 1.0.0
tags: [validation, linkml, schema, data-quality, audit, qc]
---

# Audit schema gaps (schema · instances · pipeline)

## Structured Audit Output

Follow [docs/record-reviews.md](../../../docs/record-reviews.md) and
[docs/record-review-profile.md](../../../docs/record-review-profile.md). New
assessed audit findings use this registered skill and `kind: repository` (or
`batch` for an explicitly bounded record set). Save authoritative YAML plus
derived Markdown under `reviews/structured/<timestamp>-<slug>/`; link both.

Keep the schema / instances / process axes in assessment dimensions named
`audit_axis`. Preserve exact record IDs, field paths, error categories, counts,
nonzero metric denominators, sampled/full coverage and unavailable checks.
Schema probes, validator TSVs and writer heuristics are diagnostic evidence,
not completed scientific review. A schema/process-only assessment uses
`scientific_review: false`; no clean scan establishes scientific approval.
Interpret each finding against inspected inputs before saving it. Distinguish
positive supported assessments from gaps and unassessed targets.

Identify the schema declaration or writer script responsible for each proposed
repair. Hash those inputs, the exact schema and scan outputs actually used.
Preserve backlog IDs, impact, effort, fix paths and dependencies in findings,
actions and assessment details.

```bash
uv run python scripts/record_review.py inspect --targets /tmp/audit-targets.yaml
uv run python scripts/record_review.py validate /tmp/completed-audit.yaml
uv run python scripts/record_review.py save --content /tmp/completed-audit.yaml
```

Use session-unique temporary paths. Audit-only work does not edit scientific
records, schema, writers, status gates or history. Missing required harnesses
are unavailable checks; implementing or applying repairs requires separate
curation intent. Existing reports stay historical and are not rewritten.

## Why this skill exists

Open-schema LinkML validation ignores undeclared fields, allowing import or
curation scripts to emit keys that `src/aimech/schema/aimech.yaml` does not declare. In AIMech,
`just validate` (`scripts/check.py`) and `just check` enforce structural and
corpus-wide invariants across `data/aio/*.yaml (generated from `sources/aio/`) and data/curated/*.yaml (maintained native `AIMech:` concepts)`. Always derive current record and
error counts from a fresh run.

The skill is built around three orthogonal lenses:

1. **Instance-record validation** — every YAML record in `data/aio/*.yaml (generated from `sources/aio/`) and data/curated/*.yaml (maintained native `AIMech:` concepts)` is
   validated against `ConceptRecord (`src/aimech/schema/aimech.yaml`)` in closed/strict mode via `just validate`.
2. **Schema audit** — structural inspection of `src/aimech/schema/aimech.yaml` for identifier
   policy (`identifier: true`), untyped `string` slots that represent controlled
   vocabularies or CURIEs, term wrapper consistency, `required:` alignment,
   orphan enums, and enum casing.
3. **Pipeline / writer audit** — inspection of YAML-writing modules in
   `scripts/` and `src/` for curation/revision history tracking, `--dry-run`
   support, pre-write validation, and `justfile` wiring.

## When to use

| Trigger | Why |
|---|---|
| User asks to "audit the schema / records / pipeline" | Direct ask for three-axis drift detection. |
| User reports records "silently fail" or "validation passes but the data is wrong" | Signature symptom of open-schema validation. |
| A new importer, enrichment script, or bulk migration is added | Confirm it did not introduce undeclared keys or bypass history tracking. |
| Schema changes (`src/aimech/schema/aimech.yaml` modified) | Refresh instance and writer checks against the updated schema. |
| Cold-start repository health check | `just validate` and `just check` quantify current drift. |

**Don't** invoke this skill for:
- Quick three-axis error triage without saving a structured review — use `schema-gap-analysis`.
- Single-record scientific review or curation — use `review-yaml-record` or `curate-yaml-record`.
- Identifier minting policy alone — use `manage-identifiers`.

## Workflow

### Step 1 — Strict instance and corpus validation

**Validator:** `scripts/check.py`
**Just targets:** `just validate`, `just check`

```bash
just validate
just check
```

Categorize any validation errors into `unexpected_field`, `missing_required`,
`enum_mismatch`, `type_mismatch`, `pattern_mismatch`, `format_mismatch`,
`range_violation`, or `other`.

### Step 2 — Schema structural audit

Inspect `src/aimech/schema/aimech.yaml` programmatically for:
- Classes missing `identifier: true` slots where cross-record citation occurs.
- Slots with `range: string` whose values form a closed vocabulary or CURIE set.
- Term/ontology wrapper consistency across all domain slots.
- Orphan enums and mixed enum value casing.

### Step 3 — Pipeline / writer audit

Inspect all Python modules in `scripts/` and `src/` that write YAML files and
verify each corpus mutator for:
- Recording curation/revision history events
- Supporting `--dry-run`
- Validating against `src/aimech/schema/aimech.yaml` before writing
- Being wired into `justfile`

### Step 4 — Prioritized fix backlog and structured review save

Synthesize the three axes (`schema`, `instances`, `process`) and save the
prioritized backlog (`G01`, `G02`, ...) into
`reviews/structured/<timestamp>-<slug>/review.yaml` (and generated `review.md`)
via `scripts/record_review.py`.

## Anti-patterns

- **Do not rely on permissive validation alone.** Always run `just validate` to catch undeclared fields.
- **Do not hardcode corpus or error counts in skill prose.** Always measure from live command runs.
- **Do not edit records, schema, or writers during an audit pass.**

## Related skills

- `schema-gap-analysis` — canonical three-axis drift classification guide.
- `manage-identifiers` — identifier assignment and hygiene policy.
- `id-label-correspondence` — ontology ID and canonical label correspondence checks.
- `curate-yaml-record` — single-record evidence-backed curation workflow.
