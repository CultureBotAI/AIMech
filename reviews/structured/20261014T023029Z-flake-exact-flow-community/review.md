# Scientific author self-review of Flake exact-flow community identification

- Review: 20261014T023029Z-flake-exact-flow-community
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-14T02:25:06Z
- Finished UTC: 2026-10-14T02:30:29Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Flake exact-flow community identification as DRAFT with a related AIO Clustering mapping. Author self-review supports the explicit augmentation and cut objective while preserving source ambiguity, seed and preselected-community guarantee limits.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:FlakeExactFlowCommunity
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 4968938afc2cc83ec9ba5099004750b06e87121a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:FlakeExactFlowCommunity | data/curated/FlakeExactFlowCommunity.yaml | maintained | Flake exact-flow community identification |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:FlakeExactFlowCommunity | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 163.77s (0:02:43)<br>Checked 442 record(s); 0 failed.<br>Checked 679 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 366 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 364,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:FlakeExactFlowCommunity | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:FlakeExactFlowCommunity | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:FlakeExactFlowCommunity | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:FlakeExactFlowCommunity | {"ieee2002_star": {"k": 1, "seed": [0], "minimum_cut_value": 3, "minimum_cuts": [[0], [0, 1], [0, 2], [0, 1, 2], [0, 3], [0, 1, 3], [0, 2, 3], [0, 1, 2, 3]], "minimal_source_side": [0], "seed_internal_external": [0, 3], "scope": "Forced seeds are exempt from the ordinary one-vertex improvement argument; no claim that every cut policy returns the same source side."}, "literal_source_arc_rescaling": {"minimum_cut_value": 1, "source_side_original_vertices": [], "scope": "Conditional interpretation of Figure2\u2019s all-E rescaling after source arcs are inserted; differs from the prose preexisting-edge convention, not a claim about author software."}, "kdd2000_nested_cliques": {"proposed_community": [0, 1, 2, 3, 4, 5, 6, 7], "source": 0, "sink": 11, "proposed_boundary": 2, "source_internal_degree": 3, "sink_internal_degree": 3, "minimum_cut_value": 1, "unique_minimum_source_side": [0, 1, 2, 3], "scope": "The stated local inequalities and source/sink degree bounds alone do not force exact recovery of this prechosen community; a valid nested subcommunity has a smaller cut."}, "limitations": "Finite exhaustive cut calculations under explicitly stated graph conventions; no author-code execution, web crawl, benchmark replication or universal theorem certification."} |

## Scientific And Domain Assessments

### Flake exact-flow community identification

identity: supported. Targets: AIMech:FlakeExactFlowCommunity.

Retain this distinct DRAFT algorithm.

Retain the 2002 prose augmented-graph exact core separately from repeated graph acquisition/reseeding. Its three arc classes and residual extraction specify an algorithm; optimal cut capacity does not imply any uniquely intended semantic community.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:FlakeExactFlowCommunity.

The explicit AIO mapping assessment is supported within its stated scope.

The related Clustering task mapping preserves the seeded algorithm/task distinction. Eleven full AIO node/edge/generated contexts were assessed; four generated YAMLs were reread after capture. Positive seeds prevent an unqualified unsupervised mapping, while a seeded flat cut and repeated acquisition do not establish hierarchical clustering. The supervised-clustering definition is also not equivalent to this positive-example graph grouping.

### augmentation-convention

evidence: supported. Targets: AIMech:FlakeExactFlowCommunity.

Supported within the stated primary-source and mathematical scope.

The 2002 prose assigns infinity to source arcs, k to original bidirected edges and one to nonseed sink arcs. Figure 2a subsequently loops over all E, creating a presentation ambiguity. The finite alternative is explicitly conditional and no uninspected software bug is asserted.

### cut-objective

evidence: supported. Targets: AIMech:FlakeExactFlowCommunity.

Supported within the stated primary-source and mathematical scope.

Counting the augmented arcs crossing a finite seed-containing cut yields k times original boundary size plus included nonseed count. This is a curator derivation from the displayed construction, not a new author experiment or modularity claim.

### seed-guarantee-boundary

evidence: supported. Targets: AIMech:FlakeExactFlowCommunity.

Supported within the stated primary-source and mathematical scope.

Infinite source arcs force seeds, so they cannot be removed using the same finite-cost single-vertex argument as nonseeds. The enumerated star has eight optimal seed-containing cuts and a minimal source side consisting only of the center, which violates its own strict degree criterion. Scope remains arbitrary supplied inputs rather than an assertion about the historical examples.

### preselected-community-boundary

evidence: supported. Targets: AIMech:FlakeExactFlowCommunity.

Supported within the stated primary-source and mathematical scope.

The explicit three-clique example satisfies the stated local degrees and community condition for the proposed two-clique group, yet the unique minimum cut returns a nested single clique. It refutes the broad exact-preselected-recovery reading of Theorem 1, not max-flow/min-cut optimality or Theorem 2.

### version-and-input-scope

evidence: supported. Targets: AIMech:FlakeExactFlowCommunity.

Supported within the stated primary-source and mathematical scope.

KDD Definition 1 is non-strict and its practical boundary graph differs from the 2002 construction. The draft identifies the 2002 prose core and cites both papers for version and input limits; no conflated executable implementation is inferred.

### evaluation-boundary

evidence: supported. Targets: AIMech:FlakeExactFlowCommunity.

Supported within the stated primary-source and mathematical scope.

The 2002 scientist experiments use the approximate wrapper and posthoc text characterization. They do not independently test this core on the complete Web or establish unbiased semantics.

### source-arc preservation, fixed-graph versus crawling scope, optimal cuts versus seed degree guarantees, and nested communities versus a preselected target

consistency: supported. Targets: AIMech:FlakeExactFlowCommunity.

Constructed calculations support the stated distinctions.

Finite exhaustive cuts: forced-seed star with eight tied minimum cuts, a different result under literal source-arc rescaling, and a twelve-vertex nested-clique counterexample to recovering a prechosen community from the2000local degree conditions alone. No author implementation, web crawl or benchmark execution.

### All maintained fields

provenance: supported. Targets: AIMech:FlakeExactFlowCommunity.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. All fields and six claims inspected, including every evidence locator, source version, seed constraint, algebraic cut objective, source ambiguity and finite counterexample. The record retains DRAFT and distinguishes author presentation from uninspected implementation.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261014T022450Z-flake-exact-flow-community.json | supports | Compared all 442 pinned AIO and 677 native IDs, names, aliases and scoped synonyms before either cohort write; no normalized identity match. Ignored- and hidden-inclusive searches of all three checkouts returned 20,0,0 lines, all read: prior source-deduplication logs and the Flake source lead, not either maintained concept. Semantic search covered 70 AIO and 318 native definitions; 64 AIO and 290 native rows match prior inspected context, and all six newly selected AIO and 28 native definitions were read. Eleven complete AIO node/edge/generated contexts were assessed, five verified unchanged and six newly read. The full EM record and previously inspected GN/Radicchi records provide native identity context. Both drafts were compared for a fixed-graph exact core versus a versioned crawl/reseed family. The maintained target is the2002 exact augmented-graph procedure, using the prose convention that only original graph edges are rescaled. The2000 theorem discussion is context with explicit limits, not an asserted universal exact-recovery guarantee. This core solves one supplied graph and is distinct from repeated crawl/reseed acquisition. |
| mapping | sources/aio/aio.json | supports | The related Clustering task mapping preserves the seeded algorithm/task distinction. Eleven full AIO node/edge/generated contexts were assessed; four generated YAMLs were reread after capture. Positive seeds prevent an unqualified unsupervised mapping, while a seeded flat cut and repeated acquisition do not establish hierarchical clustering. The supervised-clustering definition is also not equivalent to this positive-example graph grouping. |
| flake2002 | https://clgiles.ist.psu.edu/papers/Computer-2002-web-communities.pdf; Augmenting the Web Graph and Figure 2a, printed p. 68 / PDF p. 3; Augmenting the Web Graph, Figure 2a and its caption, printed p. 68 / PDF p. 3; curator calculation in research/discovery/flow-community-boundaries.py; Augmenting the Web Graph and Figure 2a, printed p. 68 / PDF p. 3; curator cut-capacity calculation in research/discovery/flow-community-boundaries.py; Web Communities, printed p. 66 / PDF p. 1; exact-flow guarantee discussion and Figure 2a, printed p. 68 / PDF p. 3; curator calculation in research/discovery/flow-community-boundaries.py; Figure 2 and exact-flow versus approximate-flow discussion, printed p. 68 / PDF p. 3; Experimental Results and Table 1 discussion, printed pp. 69–70 / PDF pp. 4–5 | supports | IEEE Computer 35(3):66–71, March2002; DOI10.1109/2.989932; author-hosted publisher PDF. All six pages and renders read, including three figures, two algorithms, one table, ten main references and nine sidebar references. Author code and historical web data uninspected. |
| flake2000 | https://clgiles.ist.psu.edu/papers/KDD-2000-web-communities.pdf; Section 3.1, Definitions 1–2 and Theorem 1, printed p. 152 / PDF p. 3; curator calculation in research/discovery/flow-community-boundaries.py; Sections 3.1–3.3, printed pp. 152–154 / PDF pp. 3–5 | supports | ACM KDD2000, pp150–160; DOI10.1145/347090.347121; author-hosted proceedings PDF. Complete eleven-page text and25references read. Rendered pages3–6,8–10 cover all figures, definitions, theorem conditions and five tables, including both algorithms; rotated result tables were rendered upright. Author code and historical data uninspected. |
| calculation | research/discovery/flow-community-boundaries.py | supports | Finite exhaustive cuts: forced-seed star with eight tied minimum cuts, a different result under literal source-arc rescaling, and a twelve-vertex nested-clique counterexample to recovering a prechosen community from the2000local degree conditions alone. No author implementation, web crawl or benchmark execution. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- The first vendored-check attempt failed because sandbox DNS could not resolve raw.githubusercontent.com. The failure was retained in the temporary check journal; the required check was rerun with network access and all 22 pinned artifacts matched.
- This cohort step adds one DRAFT record, reaching 678 native and 442 unchanged AIO records. The main frontier now has 863 entries, including 473 pending and 58 partly addressed cohorts; nested leads remain.
- All six pages, ten main references and nine sidebar references read. All three figures including both Figure2 algorithms, Table1, three-column sidebar, body and references visually read. The extraction reversed the subset symbol; render confirms S is a subset of V. Complete eleven-page article read, including all25references. Garbled rotated table extraction was resolved through upright renders of pages6,8,9. All three figures, both definitions, Theorems1–2, five tables including two algorithms, all displayed conditions and ranked URL/description rows inspected. Other pages read in text. URL listings were not visited and their author-provided descriptions were not independently verified.
- Primary methods were read; no author-code execution, model fitting, paid service, data upload, hardware benchmark or formal theorem certification. Constructed arithmetic examples are not experiment replication.
- Original Documents checkout synchronization and old round141 cleanup remain unapproved after automatic-review rejection; only the isolated recovery checkout is changed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T023029Z-flake-exact-flow-community
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Flake exact-flow community identification
started_at: '2026-10-14T02:25:06Z'
finished_at: '2026-10-14T02:30:29Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged source-arc preservation, fixed-graph versus
    crawling scope, optimal cuts versus seed degree guarantees, and nested communities
    versus a preselected target. This is adversarial author self-review, not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Flake exact-flow community identification as DRAFT with a related
  AIO Clustering mapping. Author self-review supports the explicit augmentation and
  cut objective while preserving source ambiguity, seed and preselected-community
  guarantee limits.
source:
  git_revision: 4968938afc2cc83ec9ba5099004750b06e87121a
  state: working_tree
  inputs:
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
    role: context
  - path: data/aio/HierarchicalClustering.yaml
    sha256: 144deaecd150e22de207c11a62f19db5f8409443724bd4be4b5c95c53375b258
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/RetrievalAugmentedLLM.yaml
    sha256: 05511e7f4671c2940df670a17ac14f579560dba5b45794d4c9f40e300ba17a8f
    role: context
  - path: data/aio/SelfsupervisedLearning.yaml
    sha256: ad9a98dfee5629f6433f13470f56e333316f8f03847df2c5678faf023d979c0e
    role: context
  - path: data/aio/SemiSupervisedLLM.yaml
    sha256: 4ee601313a6cdaa7134207fa384702f0e92d2b93906e379c2b0ef5cfe6eef9ee
    role: context
  - path: data/aio/SupervisedClustering.yaml
    sha256: d8d9f49b7b975d8217fe675e9c670fd0246af4abcdebce2483fa773a441ee83e
    role: context
  - path: data/aio/SupervisedLearning.yaml
    sha256: 472f033f91a14c8727e525ddd30f82fcaf16a2514fa8f062667fb94fc9c9b718
    role: context
  - path: data/aio/UnsupervisedClustering.yaml
    sha256: 78d3917b751b29e83802dfd2ceff6b5ee131cd64a5a3a7d40de02f5d2b9bdb1e
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/curated/ExpectationMaximization.yaml
    sha256: eab2880f9e6db51aa49135ada0c3f6d1504e947e6f920d0a5913fd7ddbd069c4
    role: context
  - path: data/curated/FlakeExactFlowCommunity.yaml
    sha256: ad366962177627bc246459f4e4d9a8214f5ee1ac4ccf9a4c63db2ef77f272c9e
    role: target
  - path: data/curated/GirvanNewmanCommunityDetection.yaml
    sha256: 0233486104552b70b0fb6cea4c4cd4cff9eb88e763025e14f1890731084b9afa
    role: context
  - path: data/curated/RadicchiEdgeClustering.yaml
    sha256: 65bc71cf027d1693eddf4f670f8126cb84cc29aa35b7a9dfc6b307ee1f5379c9
    role: context
  - path: research/discovery/20261014T022450Z-flake-exact-flow-community.json
    sha256: 9117989b09beb589bf2fed8867f2a6b3e02f5b828efb220f0eb63cfbc8722351
    role: context
  - path: research/discovery/flow-community-boundaries.py
    sha256: a72ff8ac18c3cb392ffd4a47629430d0b344514c4bd1f631d26c413e8fbc45b2
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
- target_id: AIMech:FlakeExactFlowCommunity
  path: data/curated/FlakeExactFlowCommunity.yaml
  label: Flake exact-flow community identification
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FlakeExactFlowCommunity.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:FlakeExactFlowCommunity'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:FlakeExactFlowCommunity
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Uninspected source versions and implementation components
    reason: Author software, historical web data and modern crawling services were
      not inspected. Source pseudocode and guarantee ambiguities are retained; candidate-pool,
      tie and promotion-count conventions remain unresolved. Finite calculations are
      not benchmark replication.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:FlakeExactFlowCommunity
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 163.77s (0:02:43)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 679 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 366 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 364,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:FlakeExactFlowCommunity
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
  - AIMech:FlakeExactFlowCommunity
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
  - AIMech:FlakeExactFlowCommunity
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/flow-community-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:FlakeExactFlowCommunity
  exit_code: 0
  expected_exit_code: 0
  summary: '{"ieee2002_star": {"k": 1, "seed": [0], "minimum_cut_value": 3, "minimum_cuts":
    [[0], [0, 1], [0, 2], [0, 1, 2], [0, 3], [0, 1, 3], [0, 2, 3], [0, 1, 2, 3]],
    "minimal_source_side": [0], "seed_internal_external": [0, 3], "scope": "Forced
    seeds are exempt from the ordinary one-vertex improvement argument; no claim that
    every cut policy returns the same source side."}, "literal_source_arc_rescaling":
    {"minimum_cut_value": 1, "source_side_original_vertices": [], "scope": "Conditional
    interpretation of Figure2\u2019s all-E rescaling after source arcs are inserted;
    differs from the prose preexisting-edge convention, not a claim about author software."},
    "kdd2000_nested_cliques": {"proposed_community": [0, 1, 2, 3, 4, 5, 6, 7], "source":
    0, "sink": 11, "proposed_boundary": 2, "source_internal_degree": 3, "sink_internal_degree":
    3, "minimum_cut_value": 1, "unique_minimum_source_side": [0, 1, 2, 3], "scope":
    "The stated local inequalities and source/sink degree bounds alone do not force
    exact recovery of this prechosen community; a valid nested subcommunity has a
    smaller cut."}, "limitations": "Finite exhaustive cut calculations under explicitly
    stated graph conventions; no author-code execution, web crawl, benchmark replication
    or universal theorem certification."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261014T022450Z-flake-exact-flow-community.json
  accessed_at: '2026-10-14T02:25:06Z'
  support: supports
  summary: 'Compared all 442 pinned AIO and 677 native IDs, names, aliases and scoped
    synonyms before either cohort write; no normalized identity match. Ignored- and
    hidden-inclusive searches of all three checkouts returned 20,0,0 lines, all read:
    prior source-deduplication logs and the Flake source lead, not either maintained
    concept. Semantic search covered 70 AIO and 318 native definitions; 64 AIO and
    290 native rows match prior inspected context, and all six newly selected AIO
    and 28 native definitions were read. Eleven complete AIO node/edge/generated contexts
    were assessed, five verified unchanged and six newly read. The full EM record
    and previously inspected GN/Radicchi records provide native identity context.
    Both drafts were compared for a fixed-graph exact core versus a versioned crawl/reseed
    family. The maintained target is the2002 exact augmented-graph procedure, using
    the prose convention that only original graph edges are rescaled. The2000 theorem
    discussion is context with explicit limits, not an asserted universal exact-recovery
    guarantee. This core solves one supplied graph and is distinct from repeated crawl/reseed
    acquisition.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-14T02:25:06Z'
  support: supports
  summary: The related Clustering task mapping preserves the seeded algorithm/task
    distinction. Eleven full AIO node/edge/generated contexts were assessed; four
    generated YAMLs were reread after capture. Positive seeds prevent an unqualified
    unsupervised mapping, while a seeded flat cut and repeated acquisition do not
    establish hierarchical clustering. The supervised-clustering definition is also
    not equivalent to this positive-example graph grouping.
- evidence_id: flake2002
  kind: primary_source
  reference: https://clgiles.ist.psu.edu/papers/Computer-2002-web-communities.pdf
  locator: Augmenting the Web Graph and Figure 2a, printed p. 68 / PDF p. 3; Augmenting
    the Web Graph, Figure 2a and its caption, printed p. 68 / PDF p. 3; curator calculation
    in research/discovery/flow-community-boundaries.py; Augmenting the Web Graph and
    Figure 2a, printed p. 68 / PDF p. 3; curator cut-capacity calculation in research/discovery/flow-community-boundaries.py;
    Web Communities, printed p. 66 / PDF p. 1; exact-flow guarantee discussion and
    Figure 2a, printed p. 68 / PDF p. 3; curator calculation in research/discovery/flow-community-boundaries.py;
    Figure 2 and exact-flow versus approximate-flow discussion, printed p. 68 / PDF
    p. 3; Experimental Results and Table 1 discussion, printed pp. 69–70 / PDF pp.
    4–5
  accessed_at: '2026-10-14T02:04:10Z'
  snapshot_sha256: 104f1461e3005c47850c380fd2f9a55434d9851bdae5d1a3cd5e1d2fdf5b2d68
  support: supports
  summary: IEEE Computer 35(3):66–71, March2002; DOI10.1109/2.989932; author-hosted
    publisher PDF. All six pages and renders read, including three figures, two algorithms,
    one table, ten main references and nine sidebar references. Author code and historical
    web data uninspected.
- evidence_id: flake2000
  kind: primary_source
  reference: https://clgiles.ist.psu.edu/papers/KDD-2000-web-communities.pdf
  locator: Section 3.1, Definitions 1–2 and Theorem 1, printed p. 152 / PDF p. 3;
    curator calculation in research/discovery/flow-community-boundaries.py; Sections
    3.1–3.3, printed pp. 152–154 / PDF pp. 3–5
  accessed_at: '2026-10-14T02:06:18Z'
  snapshot_sha256: 016ffe67913e080e9f86ef536667353a9cd4410c389db5d8373079a63fadb7dc
  support: supports
  summary: ACM KDD2000, pp150–160; DOI10.1145/347090.347121; author-hosted proceedings
    PDF. Complete eleven-page text and25references read. Rendered pages3–6,8–10 cover
    all figures, definitions, theorem conditions and five tables, including both algorithms;
    rotated result tables were rendered upright. Author code and historical data uninspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/flow-community-boundaries.py
  accessed_at: '2026-10-14T02:26:11Z'
  snapshot_sha256: a72ff8ac18c3cb392ffd4a47629430d0b344514c4bd1f631d26c413e8fbc45b2
  support: supports
  summary: 'Finite exhaustive cuts: forced-seed star with eight tied minimum cuts,
    a different result under literal source-arc rescaling, and a twelve-vertex nested-clique
    counterexample to recovering a prechosen community from the2000local degree conditions
    alone. No author implementation, web crawl or benchmark execution.'
assessments:
- assessment_id: identity
  area: identity
  topic: Flake exact-flow community identification
  outcome: supported
  target_ids:
  - AIMech:FlakeExactFlowCommunity
  evidence_ids:
  - identity
  - flake2002
  - flake2000
  summary: Retain this distinct DRAFT algorithm.
  details: Retain the 2002 prose augmented-graph exact core separately from repeated
    graph acquisition/reseeding. Its three arc classes and residual extraction specify
    an algorithm; optimal cut capacity does not imply any uniquely intended semantic
    community.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:FlakeExactFlowCommunity
  evidence_ids:
  - mapping
  - flake2002
  - flake2000
  summary: The explicit AIO mapping assessment is supported within its stated scope.
  details: The related Clustering task mapping preserves the seeded algorithm/task
    distinction. Eleven full AIO node/edge/generated contexts were assessed; four
    generated YAMLs were reread after capture. Positive seeds prevent an unqualified
    unsupervised mapping, while a seeded flat cut and repeated acquisition do not
    establish hierarchical clustering. The supervised-clustering definition is also
    not equivalent to this positive-example graph grouping.
- assessment_id: augmentation-convention
  area: evidence
  topic: augmentation-convention
  outcome: supported
  target_ids:
  - AIMech:FlakeExactFlowCommunity
  evidence_ids:
  - flake2002
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The 2002 prose assigns infinity to source arcs, k to original bidirected
    edges and one to nonseed sink arcs. Figure 2a subsequently loops over all E, creating
    a presentation ambiguity. The finite alternative is explicitly conditional and
    no uninspected software bug is asserted.
- assessment_id: cut-objective
  area: evidence
  topic: cut-objective
  outcome: supported
  target_ids:
  - AIMech:FlakeExactFlowCommunity
  evidence_ids:
  - flake2002
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Counting the augmented arcs crossing a finite seed-containing cut yields
    k times original boundary size plus included nonseed count. This is a curator
    derivation from the displayed construction, not a new author experiment or modularity
    claim.
- assessment_id: seed-guarantee-boundary
  area: evidence
  topic: seed-guarantee-boundary
  outcome: supported
  target_ids:
  - AIMech:FlakeExactFlowCommunity
  evidence_ids:
  - flake2002
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Infinite source arcs force seeds, so they cannot be removed using the same
    finite-cost single-vertex argument as nonseeds. The enumerated star has eight
    optimal seed-containing cuts and a minimal source side consisting only of the
    center, which violates its own strict degree criterion. Scope remains arbitrary
    supplied inputs rather than an assertion about the historical examples.
- assessment_id: preselected-community-boundary
  area: evidence
  topic: preselected-community-boundary
  outcome: supported
  target_ids:
  - AIMech:FlakeExactFlowCommunity
  evidence_ids:
  - flake2000
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The explicit three-clique example satisfies the stated local degrees and
    community condition for the proposed two-clique group, yet the unique minimum
    cut returns a nested single clique. It refutes the broad exact-preselected-recovery
    reading of Theorem 1, not max-flow/min-cut optimality or Theorem 2.
- assessment_id: version-and-input-scope
  area: evidence
  topic: version-and-input-scope
  outcome: supported
  target_ids:
  - AIMech:FlakeExactFlowCommunity
  evidence_ids:
  - flake2000
  - flake2002
  summary: Supported within the stated primary-source and mathematical scope.
  details: KDD Definition 1 is non-strict and its practical boundary graph differs
    from the 2002 construction. The draft identifies the 2002 prose core and cites
    both papers for version and input limits; no conflated executable implementation
    is inferred.
- assessment_id: evaluation-boundary
  area: evidence
  topic: evaluation-boundary
  outcome: supported
  target_ids:
  - AIMech:FlakeExactFlowCommunity
  evidence_ids:
  - flake2002
  summary: Supported within the stated primary-source and mathematical scope.
  details: The 2002 scientist experiments use the approximate wrapper and posthoc
    text characterization. They do not independently test this core on the complete
    Web or establish unbiased semantics.
- assessment_id: constructed-boundaries
  area: consistency
  topic: source-arc preservation, fixed-graph versus crawling scope, optimal cuts
    versus seed degree guarantees, and nested communities versus a preselected target
  outcome: supported
  target_ids:
  - AIMech:FlakeExactFlowCommunity
  evidence_ids:
  - flake2002
  - flake2000
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: 'Finite exhaustive cuts: forced-seed star with eight tied minimum cuts,
    a different result under literal source-arc rescaling, and a twelve-vertex nested-clique
    counterexample to recovering a prechosen community from the2000local degree conditions
    alone. No author implementation, web crawl or benchmark execution.'
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:FlakeExactFlowCommunity
  evidence_ids:
  - identity
  - mapping
  - flake2002
  - flake2000
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. All fields and six claims inspected, including every
    evidence locator, source version, seed constraint, algebraic cut objective, source
    ambiguity and finite counterexample. The record retains DRAFT and distinguishes
    author presentation from uninspected implementation.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- The first vendored-check attempt failed because sandbox DNS could not resolve raw.githubusercontent.com.
  The failure was retained in the temporary check journal; the required check was
  rerun with network access and all 22 pinned artifacts matched.
- This cohort step adds one DRAFT record, reaching 678 native and 442 unchanged AIO
  records. The main frontier now has 863 entries, including 473 pending and 58 partly
  addressed cohorts; nested leads remain.
- All six pages, ten main references and nine sidebar references read. All three figures
  including both Figure2 algorithms, Table1, three-column sidebar, body and references
  visually read. The extraction reversed the subset symbol; render confirms S is a
  subset of V. Complete eleven-page article read, including all25references. Garbled
  rotated table extraction was resolved through upright renders of pages6,8,9. All
  three figures, both definitions, Theorems1–2, five tables including two algorithms,
  all displayed conditions and ranked URL/description rows inspected. Other pages
  read in text. URL listings were not visited and their author-provided descriptions
  were not independently verified.
- Primary methods were read; no author-code execution, model fitting, paid service,
  data upload, hardware benchmark or formal theorem certification. Constructed arithmetic
  examples are not experiment replication.
- Original Documents checkout synchronization and old round141 cleanup remain unapproved
  after automatic-review rejection; only the isolated recovery checkout is changed.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
