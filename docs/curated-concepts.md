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

Use `concept_kind: layer` for a defined neural-network component, such as the
H3 sequence layer, when the primary source distinguishes it from the complete
network. State its input/output transformation and boundary from the surrounding
architecture. A layer still needs full method evidence, an identity search and
an explicit AIO mapping assessment; the kind does not establish an AIO relation.

Use `concept_kind: evaluation_criterion` for a defined condition on predictions,
models or behavior, such as equalized odds. Distinguish the condition from a
procedure for estimating it, an algorithm that enforces it, and a bias or risk.
State the population, conditioning variables or causal assumptions that define
its scope. Satisfying a formal criterion does not by itself establish overall
fairness, usefulness or legal compliance. Evidence and AIO mapping requirements
apply as for other native concepts.

Use `concept_kind: coordination_mechanism` for a source-defined computational
coordination design. State the participating actions or agents, the mediating
state or information pathway, and how it affects subsequent activity. Distinguish
the mechanism from its implementing algorithms, complete architectures, learning
objectives and application domains. A shared metaphor or the word "coordination"
is insufficient: inspected primary methods must support the mediating relationship
and its computational relevance. Qualify any scheduling, response or convergence
conditions; the kind itself establishes no performance guarantee or AIO relation.
A biological observation or a broad field such as swarm intelligence does not
qualify solely by sharing the terminology. Existing evidence, identity, mapping,
review and history requirements apply unchanged.

Use `concept_kind: computational_paradigm` for a source-defined approach to
organizing computation or computational problem solving. State the organizing
principles, the roles of constituent entities and their information or interaction
relationships, and the boundary from specific implementing algorithms, architectures
and learning objectives. A field name, biological metaphor or application domain
alone is insufficient; inspected primary text must explain the computational
design principles. Do not use this kind to avoid stating an available common
algorithmic procedure, or to reclassify existing algorithms automatically. Distinguish
a broad organizing approach from a particular coordination mechanism. The kind
establishes neither a performance guarantee nor an AIO relation; all existing
evidence, identity, mapping, review and history requirements still apply.

Evidence records distinguish abstracts, full text and versioned implementation
documentation. Definitions and asserted claims require inspected full text or
documentation. Abstracts are useful for discovery and can be retained as
context, but they do not certify unseen methods or tables. Each citation names
a source and a precise page/section/equation/table locator; each source names
its version and actual UTC access time. Preserve supporting and contradictory
evidence with their scope. SHA-256 values identify the bytes actually inspected
when a source was downloaded; a hash alone is not an assessment of its meaning.

Use `source_type: primary_monograph` for a scholarly book or monograph that is
direct evidence for its authors' definitions, methods or analyses. Record the
edition or version and the exact acquired artifact. When only an excerpt or
preview was inspected, state its page/section extent in `version`, use precise
citation locators, and preserve material access limits. `access_level: full_text`
then refers to the inspected text artifact, not access to the complete book.
An abstract remains `abstract_only` and cannot support a definition or asserted
claim by itself. A book's bibliography does not establish inspection of its cited
sources. This source type does not turn secondary summaries into original methods
or relax the evidence, identity or review requirements.

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

Identity comparison ignores case, spaces and ordinary punctuation, but preserves
Unicode letters, digits and combining marks with canonical Unicode normalization.
Thus `Π-model` differs from `Model`; Greek letters are not automatically
transliterated to Latin spellings. It also retains ASCII plus signs: `PointNet`,
`PointNet+` and `PointNet++` are different keys.
Names still need a Unicode letter or digit. A matching key is a collision check, not a
semantic equivalence assessment; inspect aliases and mechanisms even when keys
differ. Spelling out `plus` does not automatically alias the `+` symbol.

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

A supported concept may have no suitable AIO counterpart. In that case, provide
`aio_no_match` instead of `aio_mappings`: record the searched scope, the rationale,
and nonempty `examined_targets` with valid AIO IDs and individual rejection
reasons. Exactly one representation is required. Shared words or an incidental
application are insufficient reasons for a related match. This is a bounded
assessment of the pinned snapshot, not a claim that the concept is absent from
all ontologies. The same source, identity, evidence and review checks still apply;
a later snapshot requires reassessment of both positive and no-match decisions.

## Validation, review and history

Run `uv run --locked aimech validate-curated` for the complete maintained
collection. It rejects an absent or empty collection, unknown fields, unresolved
citations, invalid mapping targets, stale mapping snapshots, identity collisions,
missing or contradictory mapping assessments, misnamed files and symlink aliases.
This gate is included in `just check`, alongside
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
