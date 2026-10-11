---
name: review-category
description: Review an AIMech AIO category or maintained-concept cohort, evaluate lump/split/retain/defer boundaries, and save structured YAML and rendered Markdown without mutating records or the ontology.
---

# Review an AIMech Category

For maintained `AIMech:` concepts, follow the native-concept section of
`docs/record-review-profile.md`. Select the exact local IDs, use maintained
targets and their actual YAML owners, inspect claim evidence and AIO mapping
scope, and run `aimech validate-curated`. The generated-AIO source-node
instructions below apply to imported targets; do not fabricate source nodes
for local concepts.

Read [the common review contract](../../../docs/record-reviews.md) at
`docs/record-reviews.md` and the [AIO rubric](../../../docs/record-review-profile.md)
at `docs/record-review-profile.md`. Apply their record criteria to every reviewed
target and their category criteria to the proposed boundary.

Define the cohort by exact IDs, subset membership, explicit parent relation or
another reproducible predicate over the pinned snapshot. Declare its population,
selection rule, reviewed IDs and exclusions. Distinguish exported direct parents
from a computed descendant closure; do not infer membership from a filename or
label. Retain all selected targets, even those not assessed. If sampling, declare
the method, seed/strata where used, denominator and limits on inference.

Inspect the selected generated YAMLs, `sources/aio/aio.json`,
`sources/aio/source.yaml`, `src/aimech/importer.py` and the native schema before
judging; record exact IRI selectors and input hashes with the canonical helper.
Preserve both upstream ontology ownership and local importer ownership for
generated terms. Run the profile's required checks and capture actual results.

Save `kind: category` for a coherent category, or `kind: batch` for an explicitly
selected heterogeneous record cohort. Include evidence-backed `boundary_decisions`
when assessing identities across either kind of cohort:
`retain` preserves distinctions; `lump` needs at least two demonstrably equivalent
targets; `split` needs a complete, nonempty, disjoint partition of its selected
targets; `defer` records unresolved evidence and the next discriminating check.
Labels, shared parents, benchmarks, citations, or similar performance alone do
not establish equivalence. Every recommendation remains a proposal. Never merge,
rename, split or reparent AIO terms as a consequence of reviewing them.

ALWAYS persist the timestamped structured YAML AND helper-rendered Markdown using
`scripts/record_review.py validate`, `save`, and `check`. Save partial or blocked
assessments when checks or evidence are unavailable. Do not drop unreviewed
targets or imply a cohort-wide pass from a sample. A prose-only response is
incomplete; explicitly report a saving blocker if the pair cannot be persisted.

Return both file links, coverage, verdict, boundary recommendations, finding
counts and limitations. Do not refresh sources, hand-edit generated data, promote
status, fabricate curation/history events, run paid providers or publish Git
changes without authorization for those actions.
