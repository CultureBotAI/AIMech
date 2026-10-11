# AIMech Record Review Profile

The [common contract](record-reviews.md) governs structured output. AIMech uses
`review-yaml-record` for one `AIConcept` and `review-category` for a coherent AIO
cohort. Every review saves both `review.yaml` and rendered `review.md` under
`reviews/structured/<UTC-timestamp>-<slug>/` through the canonical helper, including
resolved-target reviews with partial or blocked outcomes. Never invent reviewed
state because an import, check, or review-document validator passed.

## Inputs and Ownership

### Maintained AIMech-native concepts

For `data/curated/*.yaml`, use `record_class: CuratedAIConcept` and
`kind: maintained`; the local record is the maintained owner. Inspect and hash
the selected YAML, `src/aimech/schema/curated_concept.yaml`,
`src/aimech/curated.py`, the pinned AIO source/manifest used for mappings, and
any local evidence inputs. Read `docs/curated-concepts.md`. Validate with
`uv run --locked aimech validate-curated` in addition to the checks below.

Review claim-to-source support, precise locators, access level, source version,
definition distinctness, concept kind and mapping direction. For `aio_no_match`,
inspect the searched scope, rejected targets and reasons rather than treating
no match as a validated mapping. Resolve primary
evidence and inspect the cited method/definition passages; an abstract does
not establish unseen PDF contents. Mapping rationale is a curator inference,
not an upstream AIO assertion. Preserve limitations and contradictory evidence.
Keep `DRAFT`; a saved passing review does not implement a status-promotion gate.
For native fixes, record `CultureBotAI/AIMech:data/curated/<local-ID>.yaml` as
owner rather than redirecting scientific changes to the AIO importer.

### Generated AIO concepts

`data/aio/*.yaml` is generated from the pinned `sources/aio/aio.json` snapshot.
`sources/aio/source.yaml` owns its version and integrity metadata;
`src/aimech/importer.py` owns AIMech's transformation;
`src/aimech/schema/aimech.yaml` owns the `AIConcept` representation.

For each target record, record `kind: generated`, its stable AIO ID, YAML path,
label, and an exact source IRI selector identifying the node in the pinned JSON
graph. Hash all reviewed YAMLs, the snapshot, source manifest, importer and native
schema with the helper. Read the source manifest and record provenance to identify
the exact upstream revision and source file. The source repository is
`berkeleybop/artificial-intelligence-ontology`; the pinned `aio.json` is a release
artifact, not necessarily the maintained ontology source.

Trace upstream fixes to the actual maintained ontology file or template at that
revision (for example `src/ontology/aio-edit.owl` or the generating template,
only after verifying ownership). Record that repository/path/role in
`owner_paths`, alongside `CultureBotAI/AIMech:src/aimech/importer.py` for generated
mapping behavior. An ontology defect belongs to its upstream maintainer; a
mapping defect belongs to AIMech's importer. Keep the frozen snapshot as evidence
and propose an explicit upstream correction or reviewed snapshot update. If the
maintained upstream owner cannot be established, preserve that uncertainty in an
`ownership_note` and a limitation; do not redirect an ontology fix to generated
YAML or claim the upstream release is a hand-maintained source.

Findings and action plans retain this ownership chain. Generation commands are
proposed acceptance checks, not evidence that a fix was executed. Never mutate
the ontology, snapshot or generated YAML as part of a read-only review.

## Required Checks

On a fresh checkout, first run `just fetch-review-bases`. This explicit setup
step retrieves missing full commit IDs named by saved reviews from `origin` and
retains them under local `refs/aimech/review-bases/` refs. A squash merge followed
by branch deletion can otherwise leave a review's historical base outside normal
branch history. The helper validates all revision strings before fetching and
fails if a requested commit cannot be retrieved. It does not change review bytes,
branches, tags, the trusted event base, or the checkout.

CI performs this preparation before the same offline `just check` gate used
locally. The preparation is not validation: the canonical review checker still
verifies provenance, input hashes, rendering and append-only history. Publishing
reviews whose bases were never pushed to the repository can remain unverifiable;
use an available published base when possible.

From the repository root, capture actual exit codes and meaningful output:

```bash
uv run --locked aimech check-source
uv run --locked aimech validate
uv run --locked aimech seed --check
uv run --locked python scripts/record_review.py check
```

`validate` is strict and requires a nonempty corpus. `seed --check` verifies exact
reproduction without writing records. For code/schema changes, also run
`just check`, the same gate used by CI. Record skipped, failed or unavailable
checks honestly; missing required checks preclude a completed passing review.
Before an absence finding, search ignored and hidden files too (`rg -uu`) and
record the bounded search scope. No coverage is not evidence of absence.

Inspect before assessing, then validate and save through
`scripts/record_review.py`. Use actual UTC timestamps and actual reviewer/model
identity. YAML is authoritative and Markdown must be rendered by the helper.
On changed inputs, re-inspect and reassess; never merely replace input hashes.

## AIO Rubric

- Identity: exact AIO ID/IRI, label and source node agree. Distinguish obsolete,
  replaced or external entities where the source declares them. Missing source
  context is a limitation, not permission to infer a replacement.
- Definitions: compare imported text with the exact source annotation and check
  each substantive claim against the cited primary evidence. Preserve the
  distinction between an ontology definition and empirical mechanism support.
  A language-model-authored definition is not independently verified evidence.
- Names: distinguish labels, exact synonyms, related synonyms and merely similar
  terms. Shared acronyms or wording do not establish concept identity.
- Relations: preserve predicate, direction and scope. Asserted subclass, part-of,
  subset membership, equivalence and computed ancestry are different claims.
  Check references and report cycles or inappropriate category mixing with the
  actual edges and evidence, without altering upstream assertions.
- Evidence: resolve cited references and inspect the actual supporting passage,
  figure, table or formal definition. Record precise locators and access times;
  distinguish support, contradiction and background. Benchmark performance is
  conditional on task, data, metric and evaluation protocol, not a general
  property of every method bearing a related label.
- Scope: distinguish algorithms, architectures, layers, tasks, data, metrics,
  model instances and bias concepts. Keep biological use cases separate from
  claims about the AI method itself. Citation availability or microbial relevance
  does not imply mechanistic validation or category membership.
- Provenance: compare the snapshot revision/hash, source IRI and importer
  mapping. Preserve source-only import status and optional curation history;
  never create an event or scientific status just to fill an empty field.

Map these topics to the shared assessment areas and preserve important context
as evidence-linked dimensions. A provenance-only review sets
`scientific_review: false`, states that literature support was not reassessed,
and must not present deterministic seed checks as scientific validation.

## Category Boundaries

A maintained-concept cohort can use an explicit local-ID set or concept-kind
predicate. Account for every selected native target and compare relevant AIO
neighbors, without assuming a mapping is an asserted subclass edge. The same
evidence, coverage and lump/split/defer requirements apply to both collections.

Use a reproducible cohort predicate and state its denominator. Assess within-
category coherence, distinction from neighboring concepts, intended abstraction
level, and evidence for each disputed boundary. Direct parents, descendants and
subsets need separate membership predicates; multi-parent placement is not by
itself a duplicate.

Always include an explicit `retain`, `lump`, `split` or `defer` boundary decision.
Lumping needs at least two targets and evidence of the same intended concept;
overlap in implementation or similar performance is insufficient. Splitting
requires a complete disjoint partition of the selected targets, with positive
criteria for every group. A proposed refinement of a single polysemous term is
an upstream action with unresolved new IDs, not fabricated existing membership.
Retain well-supported distinctions; defer when evidence cannot decide. State
sample limitations and never silently extrapolate a boundary to unreviewed IDs.

Boundary decisions propose work for the maintained owner. They do not change
AIO identifiers, assertions, generated files, or scientific status. Preserve
stable issue keys and predecessor references when a later review changes a
finding's disposition. Paid research and publication are separate actions.

## History

`aimech new-history` writes a canonical `HistoryRecord` sidecar for an actual
session and never edits its target. Supply the real actor, explicit event type,
outcome, summary and details; AI actors also require their model and agent tool.
Use `--path` for non-record targets. `validate-history --base <revision>` checks
schema, paths, session identity and append-only history against a reviewed base.
Inline `curation_history` events are optional canonical `CurationEvent` objects,
not sidecar paths. No review or bootstrap step manufactures either kind of event.
