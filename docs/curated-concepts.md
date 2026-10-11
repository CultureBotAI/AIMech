# Curated AIMech concepts

`data/curated/<local-ID>.yaml` contains maintained `CuratedAIConcept` records for
well-supported concepts missing from the pinned AIO vocabulary. Their stable
`AIMech:` identifiers belong to AIMech, not AIO. An identifier denotes a concept,
not a particular trained checkpoint, software package or benchmark score.
The `AIMech:` prefix is a local identifier namespace; HTTP resolution is not
claimed by this implementation.

The user authorized this native record layer on 2026-10-10 (local date).
Generated `data/aio/` records and their pinned source remain governed by the
existing reproduction contract. Native curation must not edit them, manufacture
AIO identifiers, or imply that upstream AIO has accepted a local definition.

## Evidence and identity

The closed LinkML contract is `src/aimech/schema/curated_concept.yaml`.
Each native record has a narrowly scoped definition, concept kind, identity
notes, supporting definition citations, claim-level evidence, source metadata,
limitations, mapping provenance, and actual curation provenance.

Evidence records distinguish abstracts, full text and versioned implementation
documentation. Definitions and asserted claims require inspected full text or
documentation. Abstracts are useful for discovery and can be retained as
context, but they do not certify unseen methods or tables. Each citation names
a source and a precise page/section/equation/table locator; each source names
its version and actual UTC access time. Preserve supporting and contradictory
evidence with their scope. SHA-256 values identify the bytes actually inspected
when a source was downloaded; a hash alone is not an assessment of its meaning.

Performance claims additionally require task, dataset/split, model/version,
metric/units, result, baseline, conditions and uncertainty. Write `not reported`
when the inspected source genuinely omits a contextual detail; never fill it
with an invented value. Avoid a performance claim when context cannot support
its intended interpretation.

Search AIO records, native records, aliases and existing proposals before
creating a stable ID. The validator rejects normalized name/alias collisions
against AIO labels/exact synonyms and other native records. Related synonyms
remain contextual evidence requiring semantic review. Ambiguous acronym hits
must be resolved before a bare acronym is asserted as an identity alias.

## AIO mappings

Every native record records the AIO commit and SHA-256 against which its mappings
were assessed. Mappings are local-subject to AIO-target:

| Relation | Meaning |
| --- | --- |
| `broad_match` | The AIO target has broader conceptual scope. |
| `narrow_match` | The AIO target has narrower conceptual scope. |
| `related_match` | A useful conceptual relationship without equivalence or subclass assertion. |

Every mapping needs a rationale, and its target must exist in the pinned AIO
source. An exact match normally means the AIO record should be reused rather
than duplicated locally. Do not use a broad match merely because a convenient
AIO branch name sounds relevant; AIO's task/model/architecture distinctions
must be inspected. A source update requires mapping reassessment rather than
silently rewriting snapshot hashes. No OWL axiom is added by this mapping format.

## Validation, review and history

Run `uv run --locked aimech validate-curated` for the complete maintained
collection. It rejects an absent or empty collection, unknown fields, unresolved
citations, invalid mapping targets, stale mapping snapshots, identity collisions,
misnamed files and symlink aliases. This gate is included in `just check`, alongside
unchanged AIO schema validation and exact seed reproduction.

All curated records start and remain `DRAFT`; structural validation does not
establish scientific truth. Save scientific review observations using the native
record/category review workflow, with `kind: maintained` targets, exact file
hashes, the native schema/validator and relevant source context. A review can
support scoped claims while recording limitations; it does not automatically
promote the record's status.

Use `just new-history --kind record --slug <local-ID> --path
data/curated/<local-ID>.yaml ...` for actual record writes. This creates a
canonical append-only sidecar. `history_refs` may point to matching record
sidecars, but do not fabricate sessions to fill a field. Batch write sessions
may use an actual report target listing every written record.

If AIO later accepts the concept, assess identity and the source migration before
retiring the local representation. Preserve its stable-ID history and explicit
mapping; do not delete or repurpose the identifier as an automatic import effect.
