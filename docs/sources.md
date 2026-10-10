# AIO Source Policy

## Authoritative Inputs

The vocabulary comes from the [AIO repository](https://github.com/berkeleybop/artificial-intelligence-ontology),
not a generated web scrape. `sources/aio/source.yaml` binds a committed
`aio.json` snapshot to an exact upstream Git revision, release IRI, checksum,
license, and actual retrieval timestamp. Validation and seeding are offline.

[BioPortal AIO](https://bioportal.bioontology.org/ontologies/AIO) is the discovery
and navigation endpoint, not a separately curated source. At bootstrap its
indexed metadata reports release `2026-07-22`. Direct browser access returned
403; indexed BioPortal metadata was inspected, and the release was independently
verified in the GitHub snapshot. No BioPortal API key was used.

The [official documentation](https://berkeleybop.org/artificial-intelligence-ontology/)
describes ontology maintenance. The [Applied Ontology publication](https://doi.org/10.1177/15705838241304103)
describes scope and construction. Its citation uses the journal's 2024 volume;
the publisher reports first online publication on March 2, 2025. Retain the DOI
instead of guessing a different paper from the date discrepancy.

## Projection

Import all named `CLASS` nodes in the AIO namespace, their definitions and
definition-source references, scoped synonyms, comments, subsets, named
superclasses, and exported `BFO:0000051` (has part) links. Calculate branch
membership by walking exported superclass edges to declared top-level terms.
Reject unresolved edges, cycles, unhandled relation types, missing definitions,
and source-count/checksum/version mismatches. External `owl:Thing` is a parent,
not an AIMech record. No OWL inference or evaluation of executable models occurs.

The full source snapshot remains the authority for metadata beyond this
projection. An upstream definition or cross-reference is not independently
revalidated evidence. LLM-assisted source construction must not be mistaken for
an experimental result. Generated records remain `NOT_REVIEWED`; reviews are
separate immutable observations.

## Updating

1. Inspect a specific upstream revision, license, release metadata, and diff.
2. In an isolated worktree, replace the snapshot and update its manifest with
   measured SHA-256, expected class count, and real UTC retrieval time.
3. Run `aimech seed` as a dry run. It will not overwrite changed existing files.
4. Review identity additions, removals, definitions, synonym scopes, and edges.
   Use a separately reviewed migration for replacement/removal of existing
   generated records; the bootstrap writer deliberately has no overwrite flag.
5. Run `just check`, save structured review findings, append actual session
   history, and publish through the normal PR process.

Future evidence enrichment should use a maintained overlay rather than edits
to generated records. New model-instance, benchmark, or intervention schemas
need their own evidence rules and scope decision; this bootstrap does not
silently reinterpret ontology classes as those entities.
