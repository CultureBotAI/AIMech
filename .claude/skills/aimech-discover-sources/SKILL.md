---
name: aimech-discover-sources
description: Find and assess ontology releases, publications, and reusable evidence sources for AIMech cohorts and coverage gaps. Use for source inventories and update scans, not individual-concept dossiers, bulk imports, or benchmark execution.
---

# Discover AIMech Sources

Use inside AIMech and resolve paths from its repository root. Read `AGENTS.md`,
`CLAUDE.md`, `docs/sources.md`, `sources/aio/source.yaml`, and the native
`AIConcept` schema before deciding that a candidate source is usable.

## Establish scope and existing coverage

Define the question or cohort using exact AIO IDs, a reproducible graph predicate,
or an explicit representation gap. State the population and unit of coverage:
ontology classes, publications, datasets and trained models are not equivalent
counts. Search existing snapshots, research, proposals and saved reviews with
ignored/hidden files included before calling a source new or a topic uncovered.

Treat AIO's official GitHub repository as the vocabulary authority. BioPortal
AIO and the official website are discovery/navigation surfaces for that ontology,
not independent corroborating datasets. AI/AION resources are not aliases of AIO.
The Applied Ontology paper supplies construction context, not per-class empirical
validation. Other resources may support evidence research or a future overlay
without being eligible inputs to the current generated-record importer.

## Evaluate candidate sources

Inspect current primary sources and publisher/database documentation. For a
known source, compare a dated prior assessment with a specific current version;
identify changed identifiers, coverage, terms, license, access and maintenance
status. Do not silently replace a pinned input while checking for updates.

Record enough evidence to decide whether an integration is worthwhile:

- Official identity, maintainer, landing URL, immutable revision/release or DOI,
  retrieval date, artifact format and access method.
- Subject and entity types, measured or explicitly unknown coverage, and overlap
  with the defined cohort using exact identifiers or reviewed mappings.
- Primary evidence versus derived annotations, predictions, aggregations or
  ontology assertions; provenance and claim-level locators available downstream.
- License and redistribution terms as documented, versioning, update cadence and
  practical access constraints. Public access does not imply an open license.
- Fit to today's AIO projection versus a proposed overlay/schema change, needed
  transformations, validation risks and likely maintained owner.

Inspect a bounded sample when full inspection is impractical; report the sampling
method, denominator and unknowns. Do not extrapolate a source's advertised total
to verified AIO coverage. Preserve unmapped entities and ambiguous mappings as
such. A blocked download is an access limitation, not proof of missing data.

Separate candidate priorities from adoption decisions. Rank by evidence value,
coverage gain, reuse terms, identifier quality and maintenance cost relevant to
the user's question. Do not import arbitrary model instances, benchmark scores,
or external ontology IDs into `data/aio/` to make a source appear supported.

## Persist the assessment

Save a new `research/sources/<YYYYMMDDTHHMMSSZ>-<slug>.md` unless the user supplied
a destination. Use actual UTC time, preserve previous assessments, and include
the search question/scope, a candidate comparison table with evidence links,
coverage methods, unavailable checks, and a concrete curation/integration handoff.
Use dispositions such as evaluate further, suitable for research, propose source
update, needs representation work, or not suitable, with reasons. Do not report
planned adapters or downloads as implemented.

Use `aimech-research-concept` for a one-concept dossier, `aimech-refresh-aio` for
a requested ontology update, and `aimech-add-record` for a supported addition.
Assessing record correctness additionally requires the native saved-review
contract. Source discovery alone does not refresh data, enable a fleet capability,
change schemas, run paid providers/models, or publish upstream issues or PRs.
