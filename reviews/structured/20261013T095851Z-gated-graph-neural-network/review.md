# Scientific author self-review of Gated Graph Neural Network

- Review: 20261013T095851Z-gated-graph-neural-network
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T09:54:12Z
- Finished UTC: 2026-10-13T09:58:51Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain GG-NN as a DRAFT base graph architecture with broad ANN and related GRU mappings. Six scoped claims preserve graph, gate, readout, training and evaluation boundaries; confirmed review findings are resolved after correction and fresh review; no unresolved actionable finding remains.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:GatedGraphNeuralNetwork
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 5bb7316c5ac473995273fe47fe048db13e0eb8a9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:GatedGraphNeuralNetwork | data/curated/GatedGraphNeuralNetwork.yaml | maintained | Gated Graph Neural Network |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:GatedGraphNeuralNetwork | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 133.88s (0:02:13)<br>Checked 442 record(s); 0 failed.<br>Checked 601 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 263 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 261,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:GatedGraphNeuralNetwork | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:GatedGraphNeuralNetwork | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:GatedGraphNeuralNetwork | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:GatedGraphNeuralNetwork | {"node_output": [0.05787243109932697, -0.18622460186380027, 0.47484793941790154], "node_relabelings": 6, "edge_order_invariance": true, "reversed_edges_change_result": true, "reset_before": ["8", "33/2"], "reset_after": ["3", "39/2"], "finite_step_not_fixed_point": true, "one_step_distant_change_absent": true, "two_step_change_present": true, "independent_gate_sum": 1.5, "global_readout": 0.15660780879220157, "scope": "Chosen tiny algebra only; no training, author-code audit, universal graph expressivity, convergence or benchmark claim."} |

## Scientific And Domain Assessments

### Gated Graph Neural Network

identity: supported. Targets: AIMech:GatedGraphNeuralNetwork.

Retain this distinct DRAFT architecture.

Section3 explicitly names GG-NN for non-sequential output; Section4 adds GGS-NN. Neither generic graph use, the old fixed-point GNN nor a GRU component establishes duplicate identity. Earlier pending discovery wording is accounted for without modifying its historical report.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:GatedGraphNeuralNetwork.

The declared broad and related AIO mappings are supported.

Six annotated AIO nodes, incident edges and generated records were inspected. The full architecture maps broadly to ANN; GRU is a related component, not whole-architecture equivalence. The pinned GRU target’s LSTM parentage is not adopted as scientific evidence. Static input graphs differ from the temporal-input emphasis of the pinned RNN definition, and named GCN/framework layer identities are not forced.

### typed-directed-gated-propagation

evidence: supported. Targets: AIMech:GatedGraphNeuralNetwork.

Supported within the stated primary-source and mathematical scope.

Equations1–6 initialize annotation prefixes and update hidden states through typed/directed transformed neighbors and shared GRU-style functions. Figure1 separates direction parameters. The graph is supplied, not inferred.

### gate-and-reset-conventions

evidence: supported. Targets: AIMech:GatedGraphNeuralNetwork.

Supported within the stated primary-source and mathematical scope.

Equation6 weights candidate content by z and the old hidden state by1-z. Equation5 multiplies reset before U. The exact nondiagonal example gives reset-before [8,33/2] and reset-after [3,39/2], demonstrating why source and API conventions must not be silently exchanged.

### node-and-graph-readouts

evidence: supported. Targets: AIMech:GatedGraphNeuralNetwork.

Supported within the stated primary-source and mathematical scope.

Section3.3 distinguishes softmax node selection from sigmoid-gated graph sums. Independent gates need not sum to1; the chosen three-node example sums to1.5. Relabeling commutes with node updates and leaves the symmetric global readout unchanged, within floating-point tolerance.

### finite-propagation-boundaries

evidence: supported. Targets: AIMech:GatedGraphNeuralNetwork.

Supported within the stated primary-source and mathematical scope.

Local message dependencies expand by one graph edge per update. The chosen chain example cannot carry a distance-two change in one update but can in two. Global readout separately aggregates all nodes; sum collisions and limited information radius are not a universal expressive-power theorem.

### unrolled-training-not-fixed-point

evidence: supported. Targets: AIMech:GatedGraphNeuralNetwork.

Supported within the stated primary-source and mathematical scope.

Section3 explicitly replaces the old contraction-based fixed-point procedure with finite unrolling and BPTT. The numerical fixture is not fixed after one update. AppendixA concerns the prior contraction intuition; the record does not adopt its conflicting inverse-rho prose as a new theorem.

### symbolic-task-evidence

evidence: supported. Targets: AIMech:GatedGraphNeuralNetwork.

Supported within the stated primary-source and mathematical scope.

Sections5.1–5.2 use symbolic bAbI graphs, separate task models, five steps and task-dependent training sizes. Task4 uses four models. Temporal-order and higher-arity limitations are explicit; sequence and program results require the extension.

### typed edge direction, reset placement, update convention, permutation symmetry, finite propagation and fixed-point assumptions

consistency: supported. Targets: AIMech:GatedGraphNeuralNetwork.

Constructed calculations support the stated distinctions.

Chosen scalar graph/GRU updates check all six node relabelings, edge-order invariance and edge-reversal sensitivity. Exact matrix examples separate reset-before and reset-after, and gate conventions. A two-edge chain shows finite propagation reach; sigmoid graph gates sum to1.5. No author code, training or benchmark reproduction.

### All maintained fields

provenance: supported. Targets: AIMech:GatedGraphNeuralNetwork.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all six claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. After correction and fresh capture, read the full maintained record, all six mapping YAMLs and the corrected source context. Full20page reading and post-initial-capture method/experiment/appendix reassessment remain applicable to unchanged scientific claims; final post-correction pages are listed separately. Recomputed constructed examples. Removed redundant normalized acronym.

### Resolution of issue260 findings affecting this record

evidence: supported. Targets: AIMech:GatedGraphNeuralNetwork.

Confirmed bounded defects resolved.

1 findings resolved with explicit predecessor links and corrected-input gates.

## Findings

### F1: Remove duplicate normalized acronym alias

minor / resolved / confirmed; issue key: ggnn-normalized-alias-duplicate.

The hyphenated and unhyphenated acronym aliases normalize identically within this record. The curated validator rejects this redundancy. Retain the source hyphenated acronym and remove its redundant unhyphenated spelling; the concept identity remains unchanged.

Disposition: Removed the redundant unhyphenated acronym; GGS-NN also cites Sections5.1–5.2 in the inspected manuscript. Full corrected record and source context, synchronized report mirror, EDIT history and successful corrected-input gates establish resolution.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T094422Z-gated-graph-neural-network.json | supports | Compared all 442 pinned AIO and 599 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 4, 1, 1 lines. All distinct match contents were inspected. Semantic matching covered 49 AIO and 106 native definitions, with every matched definition read. 6 full annotated AIO node/edge/generated contexts and 4 full native records were inspected. The named Section3 GG-NN combines typed directed graph propagation with fixed-depth gated recurrence and node/graph readouts. It is distinct from the Section4 GGS-NN extension, contraction-based original GNN, generic GRU units, CommNet, Interaction Network and GAT. An earlier discovery lead exists but no curated identity does; recover its addressed disposition explicitly. |
| mapping | sources/aio/aio.json | supports | Six annotated AIO nodes, incident edges and generated records were inspected. The full architecture maps broadly to ANN; GRU is a related component, not whole-architecture equivalence. The pinned GRU target’s LSTM parentage is not adopted as scientific evidence. Static input graphs differ from the temporal-input emphasis of the pinned RNN definition, and named GCN/framework layer identities are not forced. |
| li2016 | https://arxiv.org/pdf/1511.05493v4; All20pages of the primary v4 manuscript were visually read before curation; selected method, experiment and appendix pages reread after capture. Other versions and author code not inspected. No training or empirical replication. | supports | arXiv1511.05493v4,22September2017, with ICLR2016 publication header. All20PDFpages visually read, including AppendicesA–C. Author names verified against primary arXiv metadata; PDF groups the same authors by affiliation. Locators use PDF/printed page order. Other versions and author code not inspected. |
| calculation | research/discovery/gated-graph-network-boundaries.py | supports | Chosen scalar graph/GRU updates check all six node relabelings, edge-order invariance and edge-reversal sensitivity. Exact matrix examples separate reset-before and reset-after, and gate conventions. A two-edge chain shows finite propagation reach; sigmoid graph gates sum to1.5. No author code, training or benchmark reproduction. |
| predecessor | reviews/structured/20261013T095239Z-gated-graph-record-findings/review.yaml | supports | Immutable initial batch review preserves the failed alias validation and source-section finding. |
| corrected-record | data/curated/GatedGraphNeuralNetwork.yaml | supports | Fresh full record reading confirms normalized alias uniqueness and, for GGS-NN, corrected Sections5.1–5.2 locator; exact report mirror and EDIT history agree. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these are not independent gate runs.
- One new DRAFT concept, yielding 600 native and 442 unchanged generated records. The 784-entry main frontier retains 477 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All20PDFpages visually inspected before curation, including main methods, figures, tables, references and AppendicesA–C. Supplementary external material and author code not inspected.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T095851Z-gated-graph-neural-network
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Gated Graph Neural Network
started_at: '2026-10-13T09:54:12Z'
finished_at: '2026-10-13T09:58:51Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged typed edge direction, reset placement,
    update convention, permutation symmetry, finite propagation and fixed-point assumptions.
    This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain GG-NN as a DRAFT base graph architecture with broad ANN and related
  GRU mappings. Six scoped claims preserve graph, gate, readout, training and evaluation
  boundaries; confirmed review findings are resolved after correction and fresh review;
  no unresolved actionable finding remains.
source:
  git_revision: 5bb7316c5ac473995273fe47fe048db13e0eb8a9
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/GRUCellLayer.yaml
    sha256: e64b73e626933d3f94b8920401b7ee037fe7d6469a296978a0ddb2eefd751b9c
    role: context
  - path: data/aio/GRULayer.yaml
    sha256: 6ba029d8bebbbd7f2e24a8a0f495c4a51688a0ef889efd443f3831f8e971929a
    role: context
  - path: data/aio/GatedRecurrentUnit.yaml
    sha256: 16e73da5012ad3e1d3de23bb30db0a0e18464b02b038acddd1c0f07f4fe82940
    role: context
  - path: data/aio/GraphConvolutionalNetwork.yaml
    sha256: 644b6187436c10693cb547dbaa809b8c00c97ad198db201342e5bc0780c78d44
    role: context
  - path: data/aio/RecurrentNeuralNetwork.yaml
    sha256: 1ebef94d2014e9a19d4bb3ed0fed6c5d77098a5a44e00e2cbd1cfe682dfcd892
    role: context
  - path: data/curated/CommunicationNeuralNetwork.yaml
    sha256: 6da13aca3d17822181f43ddfb796a62170d2cdbb28a2e01a5d541c9a1ff8d813
    role: context
  - path: data/curated/GatedFeedbackRecurrentNeuralNetwork.yaml
    sha256: 7b26adbe3234f94c69012c3be72a9d3ca0e63ee1652caf7f2030e47566fc943b
    role: context
  - path: data/curated/GatedGraphNeuralNetwork.yaml
    sha256: 59e5d2fcccdc609c81eb621cc92a9dc47961324af087d49a70be26f55b9b08db
    role: target
  - path: data/curated/GraphAttentionNetwork.yaml
    sha256: d0c81e5f4484619861b11d40a48c4ddd2a1b677b6ad8f01b2e92ba80648af860
    role: context
  - path: data/curated/InteractionNetwork.yaml
    sha256: 4d20b7990c1854c6d10b0a35d95d81095b2842c94af14b3cee7fe3c198e7b3d0
    role: context
  - path: research/discovery/20261013T094422Z-gated-graph-neural-network.json
    sha256: 8bbbf3656f40123207cfdab725b9862cb9ccbceb1c0ae0f4b5390b91a50310e4
    role: context
  - path: research/discovery/gated-graph-network-boundaries.py
    sha256: 96a1c953ad65654b4a904f2c6f46a11d4a9c213f28624cc51f1a55e7bcefb580
    role: context
  - path: sources/aio/aio.json
    sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
    role: context
  - path: sources/aio/source.yaml
    sha256: a12f1e974c25fab2ebff5e44150fb86f64399471accdf0baeafd986f00e6f345
    role: context
  - path: src/aimech/curated.py
    sha256: 67cc03d7def5f62490cc1f5db320a7c18fdfd41cebf43a35ad2bb88c32cd40d5
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: a4b7e2f0327eb784d2c5b98c713534f644adf3a7848d4e3c2995e772425725c4
    role: context
targets:
- target_id: AIMech:GatedGraphNeuralNetwork
  path: data/curated/GatedGraphNeuralNetwork.yaml
  label: Gated Graph Neural Network
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GatedGraphNeuralNetwork.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:GatedGraphNeuralNetwork'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:GatedGraphNeuralNetwork
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: All20pages of the primary v4 manuscript were visually read before curation;
      selected method, experiment and appendix pages reread after capture. Other versions
      and author code not inspected. No training or empirical replication.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:GatedGraphNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 133.88s (0:02:13)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 601 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 263 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 261,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:GatedGraphNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
- check_id: required-2
  name: uv run --locked aimech check-source
  command: uv run --locked aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:GatedGraphNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: 'Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a

    '
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:GatedGraphNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/gated-graph-network-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:GatedGraphNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: '{"node_output": [0.05787243109932697, -0.18622460186380027, 0.47484793941790154],
    "node_relabelings": 6, "edge_order_invariance": true, "reversed_edges_change_result":
    true, "reset_before": ["8", "33/2"], "reset_after": ["3", "39/2"], "finite_step_not_fixed_point":
    true, "one_step_distant_change_absent": true, "two_step_change_present": true,
    "independent_gate_sum": 1.5, "global_readout": 0.15660780879220157, "scope": "Chosen
    tiny algebra only; no training, author-code audit, universal graph expressivity,
    convergence or benchmark claim."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T094422Z-gated-graph-neural-network.json
  accessed_at: '2026-10-13T09:54:12Z'
  support: supports
  summary: Compared all 442 pinned AIO and 599 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    4, 1, 1 lines. All distinct match contents were inspected. Semantic matching covered
    49 AIO and 106 native definitions, with every matched definition read. 6 full
    annotated AIO node/edge/generated contexts and 4 full native records were inspected.
    The named Section3 GG-NN combines typed directed graph propagation with fixed-depth
    gated recurrence and node/graph readouts. It is distinct from the Section4 GGS-NN
    extension, contraction-based original GNN, generic GRU units, CommNet, Interaction
    Network and GAT. An earlier discovery lead exists but no curated identity does;
    recover its addressed disposition explicitly.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T09:54:12Z'
  support: supports
  summary: Six annotated AIO nodes, incident edges and generated records were inspected.
    The full architecture maps broadly to ANN; GRU is a related component, not whole-architecture
    equivalence. The pinned GRU target’s LSTM parentage is not adopted as scientific
    evidence. Static input graphs differ from the temporal-input emphasis of the pinned
    RNN definition, and named GCN/framework layer identities are not forced.
- evidence_id: li2016
  kind: primary_source
  reference: https://arxiv.org/pdf/1511.05493v4
  locator: All20pages of the primary v4 manuscript were visually read before curation;
    selected method, experiment and appendix pages reread after capture. Other versions
    and author code not inspected. No training or empirical replication.
  accessed_at: '2026-10-13T09:21:48Z'
  snapshot_sha256: 7053a744926ad065e516d7cbd0d135cb0301fde01276e52fbe53c1d8e4158d0b
  support: supports
  summary: arXiv1511.05493v4,22September2017, with ICLR2016 publication header. All20PDFpages
    visually read, including AppendicesA–C. Author names verified against primary
    arXiv metadata; PDF groups the same authors by affiliation. Locators use PDF/printed
    page order. Other versions and author code not inspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/gated-graph-network-boundaries.py
  accessed_at: '2026-10-13T09:54:49Z'
  snapshot_sha256: 96a1c953ad65654b4a904f2c6f46a11d4a9c213f28624cc51f1a55e7bcefb580
  support: supports
  summary: Chosen scalar graph/GRU updates check all six node relabelings, edge-order
    invariance and edge-reversal sensitivity. Exact matrix examples separate reset-before
    and reset-after, and gate conventions. A two-edge chain shows finite propagation
    reach; sigmoid graph gates sum to1.5. No author code, training or benchmark reproduction.
- evidence_id: predecessor
  kind: record_content
  reference: reviews/structured/20261013T095239Z-gated-graph-record-findings/review.yaml
  accessed_at: '2026-10-13T09:54:49Z'
  snapshot_sha256: b372265fa70f00d165f1cc9669efdb91f04500bbedbc90ca03bf17d8de330f1b
  support: supports
  summary: Immutable initial batch review preserves the failed alias validation and
    source-section finding.
- evidence_id: corrected-record
  kind: record_content
  reference: data/curated/GatedGraphNeuralNetwork.yaml
  accessed_at: '2026-10-13T09:54:49Z'
  snapshot_sha256: 59e5d2fcccdc609c81eb621cc92a9dc47961324af087d49a70be26f55b9b08db
  support: supports
  summary: Fresh full record reading confirms normalized alias uniqueness and, for
    GGS-NN, corrected Sections5.1–5.2 locator; exact report mirror and EDIT history
    agree.
assessments:
- assessment_id: identity
  area: identity
  topic: Gated Graph Neural Network
  outcome: supported
  target_ids:
  - AIMech:GatedGraphNeuralNetwork
  evidence_ids:
  - identity
  - li2016
  summary: Retain this distinct DRAFT architecture.
  details: Section3 explicitly names GG-NN for non-sequential output; Section4 adds
    GGS-NN. Neither generic graph use, the old fixed-point GNN nor a GRU component
    establishes duplicate identity. Earlier pending discovery wording is accounted
    for without modifying its historical report.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:GatedGraphNeuralNetwork
  evidence_ids:
  - mapping
  - li2016
  summary: The declared broad and related AIO mappings are supported.
  details: Six annotated AIO nodes, incident edges and generated records were inspected.
    The full architecture maps broadly to ANN; GRU is a related component, not whole-architecture
    equivalence. The pinned GRU target’s LSTM parentage is not adopted as scientific
    evidence. Static input graphs differ from the temporal-input emphasis of the pinned
    RNN definition, and named GCN/framework layer identities are not forced.
- assessment_id: typed-directed-gated-propagation
  area: evidence
  topic: typed-directed-gated-propagation
  outcome: supported
  target_ids:
  - AIMech:GatedGraphNeuralNetwork
  evidence_ids:
  - li2016
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equations1–6 initialize annotation prefixes and update hidden states through
    typed/directed transformed neighbors and shared GRU-style functions. Figure1 separates
    direction parameters. The graph is supplied, not inferred.
- assessment_id: gate-and-reset-conventions
  area: evidence
  topic: gate-and-reset-conventions
  outcome: supported
  target_ids:
  - AIMech:GatedGraphNeuralNetwork
  evidence_ids:
  - li2016
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equation6 weights candidate content by z and the old hidden state by1-z.
    Equation5 multiplies reset before U. The exact nondiagonal example gives reset-before
    [8,33/2] and reset-after [3,39/2], demonstrating why source and API conventions
    must not be silently exchanged.
- assessment_id: node-and-graph-readouts
  area: evidence
  topic: node-and-graph-readouts
  outcome: supported
  target_ids:
  - AIMech:GatedGraphNeuralNetwork
  evidence_ids:
  - li2016
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section3.3 distinguishes softmax node selection from sigmoid-gated graph
    sums. Independent gates need not sum to1; the chosen three-node example sums to1.5.
    Relabeling commutes with node updates and leaves the symmetric global readout
    unchanged, within floating-point tolerance.
- assessment_id: finite-propagation-boundaries
  area: evidence
  topic: finite-propagation-boundaries
  outcome: supported
  target_ids:
  - AIMech:GatedGraphNeuralNetwork
  evidence_ids:
  - li2016
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Local message dependencies expand by one graph edge per update. The chosen
    chain example cannot carry a distance-two change in one update but can in two.
    Global readout separately aggregates all nodes; sum collisions and limited information
    radius are not a universal expressive-power theorem.
- assessment_id: unrolled-training-not-fixed-point
  area: evidence
  topic: unrolled-training-not-fixed-point
  outcome: supported
  target_ids:
  - AIMech:GatedGraphNeuralNetwork
  evidence_ids:
  - li2016
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section3 explicitly replaces the old contraction-based fixed-point procedure
    with finite unrolling and BPTT. The numerical fixture is not fixed after one update.
    AppendixA concerns the prior contraction intuition; the record does not adopt
    its conflicting inverse-rho prose as a new theorem.
- assessment_id: symbolic-task-evidence
  area: evidence
  topic: symbolic-task-evidence
  outcome: supported
  target_ids:
  - AIMech:GatedGraphNeuralNetwork
  evidence_ids:
  - li2016
  summary: Supported within the stated primary-source and mathematical scope.
  details: Sections5.1–5.2 use symbolic bAbI graphs, separate task models, five steps
    and task-dependent training sizes. Task4 uses four models. Temporal-order and
    higher-arity limitations are explicit; sequence and program results require the
    extension.
- assessment_id: constructed-boundaries
  area: consistency
  topic: typed edge direction, reset placement, update convention, permutation symmetry,
    finite propagation and fixed-point assumptions
  outcome: supported
  target_ids:
  - AIMech:GatedGraphNeuralNetwork
  evidence_ids:
  - li2016
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Chosen scalar graph/GRU updates check all six node relabelings, edge-order
    invariance and edge-reversal sensitivity. Exact matrix examples separate reset-before
    and reset-after, and gate conventions. A two-edge chain shows finite propagation
    reach; sigmoid graph gates sum to1.5. No author code, training or benchmark reproduction.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:GatedGraphNeuralNetwork
  evidence_ids:
  - identity
  - mapping
  - li2016
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all six claims/locators, source identities/versions/access/hashes, AIO pin and
    mapping, limitations and actual curation timestamps. Capture/source/context hashes
    and exact report mirror agree. After correction and fresh capture, read the full
    maintained record, all six mapping YAMLs and the corrected source context. Full20page
    reading and post-initial-capture method/experiment/appendix reassessment remain
    applicable to unchanged scientific claims; final post-correction pages are listed
    separately. Recomputed constructed examples. Removed redundant normalized acronym.
- assessment_id: review-remediation
  area: evidence
  topic: Resolution of issue260 findings affecting this record
  outcome: supported
  target_ids:
  - AIMech:GatedGraphNeuralNetwork
  evidence_ids:
  - predecessor
  - corrected-record
  - li2016
  summary: Confirmed bounded defects resolved.
  details: 1 findings resolved with explicit predecessor links and corrected-input
    gates.
findings:
- finding_id: F1
  issue_key: ggnn-normalized-alias-duplicate
  category: identity
  severity: minor
  status: resolved
  certainty: confirmed
  title: Remove duplicate normalized acronym alias
  description: The hyphenated and unhyphenated acronym aliases normalize identically
    within this record. The curated validator rejects this redundancy. Retain the
    source hyphenated acronym and remove its redundant unhyphenated spelling; the
    concept identity remains unchanged.
  target_ids:
  - AIMech:GatedGraphNeuralNetwork
  field_paths:
  - aliases
  evidence_ids:
  - predecessor
  - corrected-record
  - li2016
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GatedGraphNeuralNetwork.yaml
    role: maintained
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261013T095239Z-gated-graph-record-findings
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/260
  disposition_reason: Removed the redundant unhyphenated acronym; GGS-NN also cites
    Sections5.1–5.2 in the inspected manuscript. Full corrected record and source
    context, synchronized report mirror, EDIT history and successful corrected-input
    gates establish resolution.
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these
  are not independent gate runs.
- One new DRAFT concept, yielding 600 native and 442 unchanged generated records.
  The 784-entry main frontier retains 477 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- All20PDFpages visually inspected before curation, including main methods, figures,
  tables, references and AppendicesA–C. Supplementary external material and author
  code not inspected.
- No author code, training, paid service, hardware measurement or empirical replication.
  Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization
  and old round141 cleanup remain pending explicit approval after automatic review
  rejection.
related_reviews:
- repository: CultureBotAI/AIMech
  review_id: 20261013T095239Z-gated-graph-record-findings
  relationship: Resolves only the explicitly linked findings affecting this exact
    record; the companion review addresses the other target.
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
