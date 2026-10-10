# AIMech

AIO-grounded records for artificial intelligence concepts, their relationships,
and evidence-backed review. AIMech extends the Mech curation workflow to AI;
it is not a fork of the upstream ontology or a claim that ontology membership
demonstrates a model's performance, safety, or causal mechanism.

## Sources

- [Artificial Intelligence Ontology on GitHub](https://github.com/berkeleybop/artificial-intelligence-ontology)
- [AIO on BioPortal](https://bioportal.bioontology.org/ontologies/AIO)
- [AIO documentation](https://berkeleybop.org/artificial-intelligence-ontology/)
- Joachimiak et al., *The Artificial Intelligence Ontology: LLM-Assisted
  Construction of AI Concept Hierarchies*, Applied Ontology 19(4),
  [doi:10.1177/15705838241304103](https://doi.org/10.1177/15705838241304103).

The bootstrap pins AIO release `2026-07-22`, upstream commit
`397851c547d1c4d8f06ef184f63c1d40bc86937a`. It contains 442 named AIO
classes spanning Bias, Layer, Machine Learning Task, Mathematical Function,
Model, Network, Preprocessing, and Training Strategy. BioPortal's total may
include external classes; AIMech counts only class IRIs in the AIO namespace.

Every generated record is `NOT_REVIEWED`. This is a deterministic import of
terminology, not an independent scientific review. The paper supplies ontology
context, not blanket evidence for every imported claim. The retained source
snapshot preserves the complete original export; the projection is not an OWL
reasoner and does not replace that export.

## Work Locally

```bash
uv sync --locked --extra dev
just check
just vendored-check                     # verify the public, immutable CLAW pin
uv run --locked aimech seed              # read-only preview
uv run --locked aimech seed --check      # verify byte-for-byte reproduction
uv run --locked aimech validate
```

`just check` is the offline local and CI quality gate. CI additionally runs
`just vendored-check`, which compares shared artifacts with the public CLAW
revision in `scripts/.vendored_canon_ref`. No API keys or live research
providers are needed. `seed --write` creates missing files only; it refuses to
overwrite changed records or delete unexpected files. Source upgrades are
explicit, reviewed changes to the snapshot and manifest, not automatic pulls.

## Ownership

| Path | Purpose |
| --- | --- |
| `sources/aio/` | Pinned upstream JSON, checksum, citation, and license |
| `src/aimech/schema/aimech.yaml` | Native LinkML contract |
| `src/aimech/importer.py` | Deterministic source-to-record projection |
| `data/aio/*.yaml` | Generated per-concept records; do not hand-edit |
| `.claude/skills/` | Record/category review and repository workflows |
| `reviews/structured/` | Timestamped schema-validated review YAML and derived Markdown |
| `history/` | Append-only curation-session sidecars created when work occurs |

Review issues belong to the upstream concept, importer, or future maintained
curation layer, not hand-edits to generated outputs. See
[the review profile](docs/record-review-profile.md) and
[source policy](docs/sources.md). No website, benchmark evaluator, or live
model-execution capability is claimed by this bootstrap.

Use [$aimech-add-record](.claude/skills/aimech-add-record/SKILL.md) to resolve a
concept, check for duplicates, and add a missing record from the pinned source
or prepare an upstream-term/source-update proposal. The skill is also exposed
through the repository's `.agents/skills` link.

## Licensing

New AIMech code is BSD-3-Clause. AIO source data and derived concept records
remain **CC-BY-4.0**, attributed to the AIO authors. See [LICENSE-DATA](LICENSE-DATA)
and the unchanged upstream files under `sources/aio/`. Shared CLAW artifacts
retain their own notices and are governed by the pinned upstream manifest.
