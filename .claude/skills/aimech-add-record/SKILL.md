---
name: aimech-add-record
description: Discover and add evidence-backed AI concepts to AIMech using web searches, publication abstracts, and full-text PDFs. Restore generated AIO records or curate AIMech-native concepts with explicit AIO mapping assessments. Use for concept additions and iterative discovery, not standalone trained-model instances or read-only reviews.
---

# Add an AIMech Record

Use inside AIMech. `AIConcept` records in `data/aio/` are generated from the
pinned AIO source. `CuratedAIConcept` records in `data/curated/` are maintained
locally with `AIMech:` IDs, inspected evidence and explicit AIO mapping assessments. Keep
these ownership and identity systems distinct. A local concept does not receive
an AIO ID or become an accepted upstream class.

For web/literature discovery, abstracts, PDFs, or an open-ended addition loop,
read [literature discovery](references/literature-discovery.md). For a native
record, also read `docs/curated-concepts.md` and
`src/aimech/schema/curated_concept.yaml` from the repository root.

## Establish the target and source

Read `AGENTS.md`, `CLAUDE.md`, `docs/sources.md`, the native schema at
`src/aimech/schema/aimech.yaml`, and `src/aimech/importer.py`. Inspect
`sources/aio/source.yaml` and the closest existing generated record. Resolve
repository paths from the AIMech root, including when invoked through
`.agents/skills`.

Check branch, origin, status and existing worktrees before writing; use the
repository's isolated-worktree workflow and preserve unrelated changes.

Accept an AIO CURIE/IRI, label, or sufficiently specified AI concept. For an
ambiguous label, inspect candidate definitions, exact/related synonyms and
parents before choosing an identity. Ask for the missing distinction only when
the available evidence cannot resolve it. Never treat a shared acronym or
similar model performance as concept equivalence.

Search exact IDs, labels, synonyms and relevant reference identifiers across
the repository with ignored and hidden files included. Use fixed-string
searches for user-supplied strings, for example:

```bash
rg --no-ignore --hidden -n -F -e 'AIO:TransformerLanguageModel' \
  -e 'https://w3id.org/aio/TransformerLanguageModel' -e 'Transformer LM' .
uv run --locked aimech check-source
uv run --locked aimech seed
```

Replace the example terms with the actual target. Inspect the exact `CLASS`
node, its synonyms and edges in the pinned JSON; a text hit in a reference or
proposal is not a class match. State the searched scope for an absence finding.
Do not interpret a failure to access an upstream source as absence there.

## Choose the supported addition path

| Finding | Action |
| --- | --- |
| Exact concept already has a matching generated record | Return its ID and path as already present; do not create a duplicate. Use a record-review skill only when review is requested. |
| Exact class is in the pin, but its generated file is missing | Generate the missing record from the pinned source using the procedure below. |
| Class exists only in a different upstream revision | Prepare a pinned source update using [source updates](references/source-updates.md). Its effects extend beyond the new class. |
| Exact concept already has a matching maintained record in `data/curated/` | Reuse its stable local ID; assess new evidence without creating a duplicate. |
| Concept is absent from AIO and supported by inspected evidence | Curate a native record in `data/curated/` with an `AIMech:` ID and justified AIO mappings, or an explicit no-match assessment when no target fits; an upstream-term proposal is optional follow-up. |
| Concept identity, scope, or evidence remains unresolved | Retain the candidate and the missing discriminating evidence in the discovery ledger; do not turn it into an asserted record. |
| Request is for a particular trained model, dataset, benchmark result or empirical claim | Explain the representation gap and prepare a scoped schema/overlay proposal if needed; these are not currently standalone AIConcept records. |

Downloaded OWL files, BioPortal pages and the AIO paper provide reference
context. The importer reads the pinned JSON and its manifest. Do not silently
replace that authority with `data/aio-full.owl`, a live BioPortal response, a
paper passage, or another ontology named AI/AION.

## Generate a missing pinned record

Inspect the expected filename and exact bytes through
`aimech.importer.build_records(Path.cwd())`. This validates the source and
constructs the complete expected corpus. Compare that mapping with the actual
files: the seed preview prints counts, not the individual missing IDs.

Use `uv run --locked aimech seed --write` only when every missing file is within
the authorized scope and there are no changed or unexpected files. The command
creates **all** missing records; it has no per-ID or overwrite option.

For a request limited to one class when unrelated files are also missing,
select only that resolved class's bytes from `build_records`. First apply the
same changed/unexpected-file and symlink checks as `seed` in the current
importer. Then write those generated UTF-8 bytes to the canonical filename with
exclusive creation (`open("xb")`). Do not reserialize or hand-author a record.
Report remaining pre-existing corpus gaps and any resulting failed full-corpus
check; do not silently repair them or claim a clean corpus.

If the destination already exists, compare it with the generated bytes. A
matching record is a no-op; a changed file, symlink or unexpected corpus entry
requires diagnosis, not a force write. A checksum/version mismatch must be
investigated; do not recompute a checksum merely to bless altered source data.

Preserve the upstream IRI, definitions, synonym scopes, parents, subsets,
exported relationships, CC BY 4.0 attribution, and manifest-derived provenance.
Retain `review_status: NOT_REVIEWED`. Import timestamps come from the pinned
manifest; the current session time belongs in history, not in rewritten import
provenance. Never add literature conclusions, discussions or `history_refs` to
generated YAML merely because the schema has slots for them.

## Curate a new native concept

Resolve identity against both record collections and existing proposals,
including aliases, related synonyms and semantic scope. Read the full primary
method description or versioned implementation documentation before asserting
a mechanism; a search snippet or abstract alone is not that inspection.

Write the maintained record through the native schema. Include a narrow
definition, typed concept scope, claim-specific evidence citations and locators,
source versions/access levels, limitations, actual curation provenance and the
searched identity context. Use `DRAFT`; a schema check is not scientific review.
Record AIO mapping direction explicitly: a broad match means the AIO target is
broader than the local concept. Use a related match when abstraction levels
differ, and explain it; do not force an algorithm beneath a task as an is-a
assertion. Preserve the AIO snapshot used for mapping. When no suitable target
exists, use `aio_no_match` instead of a forced link. Record the ignored-inclusive
identity search, semantic search scope, examined AIO targets and why each was
rejected. Shared words or an incidental application do not establish a mapping.
Keep the no-match assessment bounded to the inspected snapshot and review it
scientifically alongside positive mappings.

Use stable local IDs and canonical filenames with exclusive creation. Never
overwrite an existing record to make an addition succeed. Validate the complete
curated collection with `aimech validate-curated`; it checks cross-record
identity, references and mappings as well as individual record structure.
If review is requested, save a scientific record/category review using the native
review contract, with the curated YAML as its maintained target.

## Propose an unresolved or upstream addition

Complete the useful identity and evidence work before requesting a decision.
Save a clearly labeled proposal in the user's chosen destination, or
`docs/proposals/aio/<slug>.md` for a new local proposal. This documentation path
is not an importer input or a structured record review.

Record the candidate label and scope, searched revisions and nearest concepts,
why existing classes do not cover it, a proposed definition and parent rationale,
primary evidence with precise locators, contradictions or uncertainty, and the
maintained upstream owner. Verify that owner from the upstream revision; a
release export is not necessarily the maintained ontology file or template.
Keep an unassigned AIO ID explicitly unresolved. A proposal is not a native
record; a curated `AIMech:` record is not an AIO release addition. Do not put
either kind of maintained content under generated `data/aio/`.

For mechanism, bias, limitation or evaluation claims, inspect primary papers
or versioned implementation documentation. Distinguish ontology terminology
from experimental evidence and preserve evaluation context. The general AIO
paper is not blanket support for every class. Research supports the requested
addition; it does not require paid services or execution of models.

## History, checks and delivery

Record an actual write session with `just new-history`, using
the real actor, model/tool when applicable, event, outcome, summary and details.
Quote free-text arguments normally; the recipe preserves their boundaries and
literal contents. The target must already exist. A single-record addition can
target that record; a source update should have a session sidecar for its source
manifest rather than invented scientific curation events for every regenerated
term. Use a report target for
an actual saved proposal. Keep sidecars append-only and separate from generated
record bytes. Consult `uv run --locked aimech new-history --help` for arguments.

After record writes, run:

```bash
uv run --locked aimech check-source
uv run --locked aimech validate
uv run --locked aimech validate-curated
uv run --locked aimech seed --check
uv run --locked aimech validate-history --base HEAD
git diff --check
```

Use the actual reviewed base instead of `HEAD` when the changes are already
committed. For code/schema changes and before publication, run `just check`;
also run `just vendored-check` before publication as required by `CLAUDE.md`.
Capture failures honestly and distinguish existing defects from this change.
Do not edit vendored CLAW files to make a gate pass.

Return the exact ID/label, record collection, disposition (added, already present, proposed, or
blocked), file and history links, source revision, checks performed, and any
remaining scope or evidence limitations. An import is not a scientific review.
If a review is requested, use the native review skill and save its required
structured YAML/Markdown pair. Creating this skill or invoking it does not
itself request commits, upstream issue submission, PR publication or merging;
follow the user's actual publication instructions without re-asking for actions
already authorized.
