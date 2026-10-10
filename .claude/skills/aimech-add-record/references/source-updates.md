# Add a concept through an AIO source update

Read this when the requested class exists upstream but not in AIMech's pinned
snapshot. The current source-update contract is `docs/sources.md`; re-read it
before executing a migration.

## Pin and assess the candidate revision

- Locate the exact named AIO class in the authoritative upstream repository.
  Inspect its definition, identity, parents, annotations and maintained source.
  BioPortal discovery is useful, but similarly named AI/AION ontologies are not
  interchangeable with AIO.
- Select an exact Git commit and its release JSON. Verify repository, source
  path, release IRI and license. Preserve the raw upstream bytes and calculate
  their SHA-256; record the actual retrieval time. Do not edit a release export
  locally and call it an upstream artifact.
- Prepare the proposed `sources/aio/aio.json` and `sources/aio/source.yaml` in an
  isolated candidate workspace. Update all relevant manifest fields, including
  class count, commit, checksum, version and retrieval time. Derive the expected
  count from named `CLASS` nodes in `https://w3id.org/aio/`, not BioPortal's total.
- Compare old and candidate graphs by exact IRI. List added/removed IDs and
  changes to definitions, labels, synonym scopes, direct edges, subsets,
  branches and deprecations. Keep semantic changes distinct from provenance-only
  changes. Identify the requested class and the affected existing concepts.

## Account for the whole-corpus migration

Every generated record carries the source commit, release, hash and retrieval
time. Changing the snapshot or its manifest can therefore change **all** record
bytes, even when only one ontology class was added. Mixing an old corpus with
one record from the new revision does not satisfy `seed --check`.

The stock writer has no overwrite, force, prune or per-ID flag. It refuses
changed/unexpected files. Do not delete the existing corpus to make `seed
--write` appear safe or bypass that refusal by copying unreviewed outputs.

Use `aimech.importer.build_records(candidate_root)` to calculate candidate
outputs in a separate staging directory. This must succeed under the current
schema and importer before proposing installation. New branches, unsupported
predicates, synonym annotations, deprecations, unresolved edges or cycles can
require a reviewed importer/schema change. Do not omit those assertions, weaken
validation, or drop source concepts merely to obtain a passing import.

Prepare a concrete migration manifest: old/new source hashes and revisions,
added/changed/removed record paths, expected output hashes, proposed writes,
scientific/identity concerns, validation results and rollback source. Preserve
local edits and record removals as explicit decisions. Apply only a migration
whose scope has been authorized and reviewed under the source policy.

Persist the required source-update review findings through the native record
or category review skill and `docs/record-reviews.md`. Use the appropriate
affected targets and retain upstream/importer ownership. Save the structured
YAML and rendered Markdown; a migration diff alone is not that review. Where
candidate inputs change after review, re-inspect and reassess them.

If the user already requested the source refresh and corresponding migration,
continue within that scope. Otherwise present the completed candidate diff and
explain that adding this class requires replacing the pinned source and
regenerating affected records. Ask only for the additional decision actually
needed; a proposal or review is not permission to delete concepts, publish an
upstream issue, or merge a PR.

After applying an authorized migration, require byte-for-byte reproduction with
`aimech seed --check`, native validation, actual session history, and the quality
gates from `CLAUDE.md`. Preserve `NOT_REVIEWED` for imported concepts.

## Expected dispositions

- A class already in the local corpus: return the existing record, even if the
  user supplied a synonym or a newer paper about it.
- An upstream-only class without source-refresh scope: save the candidate
  update and report that no authoritative AIMech record was added yet.
- A class absent upstream: use the entrypoint's proposal workflow; do not invent
  a Git revision, AIO IRI, definition citation or import provenance.
- An unsupported model-instance or benchmark request: identify the missing
  representation rather than disguising it as a generic ontology class.
