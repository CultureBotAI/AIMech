---
name: aimech-research-concept
description: Research an AIMech AI concept's identity, mechanism, applications, limitations, and primary evidence. Use for a concept dossier or evidence gathering, not an AIO source refresh, record creation, or a formal record review.
---

# Research an AIMech Concept

Use inside AIMech. Resolve paths from the AIMech repository root, not from this
skill's installed location. Read `AGENTS.md`, `CLAUDE.md`, `docs/sources.md`, and
`docs/record-review-profile.md`. Research can support curation; it does not itself
change generated records or establish that they have been scientifically reviewed.

## Resolve the question

Identify the requested AIO ID/IRI, label, or proposed concept and the research
question. Compare exact definitions, scoped synonyms and direct relationships in
`sources/aio/aio.json`, its `source.yaml`, and relevant `data/aio/*.yaml` records.
Search hidden and ignored files too before reporting absence; use fixed-string
searches for supplied identifiers. Record the bounded search scope and revisions.

Distinguish ontology classes from particular trained models, software releases,
datasets, benchmark results and applications. Shared acronyms, implementations
or performance do not establish identity. Resolve ambiguous names before
attaching evidence to a record. An unrepresented concept may have a research
dossier with an unresolved AIO ID; it must not receive a fabricated identifier.

## Gather and assess evidence

Use the pinned ontology to establish what AIO asserts. Follow its definition
citations to the actual sources, and search primary publications, supplements,
versioned implementation documentation and reproducible artifacts for the
requested question. Verify current external sources when researching rather than
treating a local reference download or search snippet as current evidence.

For each substantive claim, retain the source identity/version, inspected
passage, equation, figure, table or code location, access time, and whether it
supports, contradicts or merely contextualizes the claim. Separate:

- Formal definitions and mathematical properties from empirical measurements.
- Architecture and training procedure from a particular model's trained weights.
- Benchmark results from general claims about a method or category.
- Biological applications from evidence for an AI mechanism itself.
- Upstream ontology assertions from independently checked scientific evidence.

For empirical results, retain task, dataset/version and split, model/version,
training or inference conditions, baseline, metric definition, units, sample
size and uncertainty where reported. Identify leakage, comparability and external
validity limitations when the evidence supports them; do not infer a defect
merely because an abstract omits those details. Preserve conflicting results and
negative evidence with their conditions. Mark inaccessible full text and
unverified references explicitly. AIO's general publication is not blanket
experimental support for every concept.

## Save and hand off

Save a dated dossier to the user's requested destination or a new
`research/concepts/<YYYYMMDDTHHMMSSZ>-<slug>.md`, using real UTC time and avoiding
collisions. Include the question and exact identity, inspected source revision,
search scope/date, an evidence-linked claim table, contradictions and limitations,
and concrete next actions with their maintained owners. Add useful sections for
the subject rather than forcing empty headings. Keep source quotations limited
and clearly attributed; use precise citations and paraphrase the synthesis.

Return the file link and what the evidence does and does not establish. Use
`aimech-add-record` for a requested addition. If the task also asks for a verdict
on an existing record or category, follow its native review skill and save the
schema-validated YAML/Markdown pair; a dossier cannot substitute for that review.

Do not hand-edit `data/aio/`, promote `review_status`, modify snapshots, invent
curation events, execute/train models, upload data, use paid providers, or publish
issues/PRs as a side effect of research. Those actions require their own task scope.
