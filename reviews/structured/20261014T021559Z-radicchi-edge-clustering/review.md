# Scientific author self-review of Radicchi edge-clustering community detection

- Review: 20261014T021559Z-radicchi-edge-clustering
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-14T02:08:53Z
- Finished UTC: 2026-10-14T02:15:59Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Radicchi edge-clustering community detection as a DRAFT algorithm family with related AIO tasks. Author self-review supports the explicit triangle selector while preserving source infinity, higher-cycle implementation, timing and evaluation limits.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:RadicchiEdgeClustering
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e7270db7eb359fdf93eb7815543c52db480f040d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:RadicchiEdgeClustering | data/curated/RadicchiEdgeClustering.yaml | maintained | Radicchi edge-clustering community detection |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:RadicchiEdgeClustering | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 191.60s (0:03:11)<br>Checked 442 record(s); 0 failed.<br>Checked 677 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 364 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 362,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:RadicchiEdgeClustering | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:RadicchiEdgeClustering | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:RadicchiEdgeClustering | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:RadicchiEdgeClustering | {"original_path_children": [{"strong": false, "weak": true, "inward": {"0": 1, "1": 1}, "outward": {"0": 0, "1": 1}, "internal_degree_sum": 2, "external_degree_sum": 1}, {"strong": false, "weak": true, "inward": {"2": 1, "3": 1}, "outward": {"2": 1, "3": 0}, "internal_degree_sum": 2, "external_degree_sum": 1}], "children_on_deleted_graph": [{"strong": true, "weak": true, "inward": {"0": 1, "1": 1}, "outward": {"0": 0, "1": 0}, "internal_degree_sum": 2, "external_degree_sum": 0}, {"strong": true, "weak": true, "inward": {"2": 1, "3": 1}, "outward": {"2": 0, "3": 0}, "internal_degree_sum": 2, "external_degree_sum": 0}], "one_qualifying_weak_child_rejected": true, "modified_path_scores": {"(0, 1)": "infinity (source convention)", "(1, 2)": "1", "(2, 3)": "infinity (source convention)"}, "triangle_score": "2", "four_clique_score": "3/2", "triangle_free_cycle_scores": "all1", "scope": "Exact strong/weak degree tests on original adjacency; retention needs at least two qualifying children; explicit g3 rankings and source infinity convention. None is only an internal sentinel serialized as infinity text. No g4 denominator, author implementation, benchmark or universal structural guarantee."} |

## Scientific And Domain Assessments

### Radicchi edge-clustering community detection

identity: supported. Targets: AIMech:RadicchiEdgeClustering.

Retain this distinct DRAFT algorithm.

Retain one family record for the local modified cycle-score selector, including the explicit g3 rule and a bounded description of g4. The source distinguishes it from maximal-betweenness deletion; shared definition filtering does not collapse the identities. No separate redundant g3 record is added.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:RadicchiEdgeClustering.

The explicit AIO mapping assessment is supported within its stated scope.

Related HierarchicalClustering and UnsupervisedClustering task mappings preserve algorithm/task scope. Sixteen complete AIO contexts were verified unchanged; four generated YAMLs were reread after capture. Strong/weak graph tests do not mean weakly supervised learning, and local cycles do not make this a recurrent neural or causal model.

### modified-triangle-score

evidence: supported. Targets: AIMech:RadicchiEdgeClustering.

Supported within the stated primary-source and mathematical scope.

Equations3–4 distinguish ordinary from plus-one scores. Triangle2 and four-clique3/2 verify that the modified value is not a probability. The update paragraph supports recomputing affected current-neighborhood scores after deletion.

### leaf-and-tie-boundary

evidence: supported. Targets: AIMech:RadicchiEdgeClustering.

Supported within the stated primary-source and mathematical scope.

The source explicitly assigns infinity to a leaf edge. The finite reference uses a sentinel only internally and serializes that convention as text; it does not silently divide by zero. The four-cycle gives tied finite1 values. No never-remove or unaudited terminal behavior is asserted.

### cycle-family-boundary

evidence: supported. Targets: AIMech:RadicchiEdgeClustering.

Supported within the stated primary-source and mathematical scope.

Equation5 describes possible cycles given degrees without an explicit executable g4 denominator. The record retains the demonstrated family and its g4 comparison while leaving implementation conventions unresolved instead of supplying an invented formula.

### selector-and-filter

evidence: supported. Targets: AIMech:RadicchiEdgeClustering.

Supported within the stated primary-source and mathematical scope.

The source’s Figure4 discussion explicitly says minimum clustering and maximum betweenness edges differ. The original-adjacency at-least-two filter is a separate step applicable to either selector; shared validation does not imply identical hierarchies.

### runtime-conditions

evidence: supported. Targets: AIMech:RadicchiEdgeClustering.

Supported within the stated primary-source and mathematical scope.

The estimate assumes local updates with controlled neighborhoods. Figure5’s caption explicitly excludes the definition filter and fixes average degree5; the draft neither universalizes constant update cost nor attributes those timings to the filtered pipeline.

### evaluation-scope

evidence: supported. Targets: AIMech:RadicchiEdgeClustering.

Supported within the stated primary-source and mathematical scope.

Figure2’s strong/weak and strict-success/node-error comparisons are conditional. SectionV distinguishes all15616authors from the largest12722component, and Figure6 pools all nested weak communities rather than a single flat cut.

### domain-limits

evidence: supported. Targets: AIMech:RadicchiEdgeClustering.

Supported within the stated primary-source and mathematical scope.

SectionsV–VI acknowledge subjective collaboration labels and possible short-cycle shortages outside social networks. The source proposes future non-social applications rather than demonstrating universal biological accuracy.

### modified scores versus probabilities, current-score graph versus original-validation graph, cycle selection versus betweenness, and unfiltered timing versus filtered-pipeline cost

consistency: supported. Targets: AIMech:RadicchiEdgeClustering.

Constructed calculations support the stated distinctions.

Exact original-adjacency strong/weak tests on a four-path, rejection with only one qualifying child, modified triangle scores above one, source infinity convention on leaf edges and tied scores on a triangle-free cycle. No g4 denominator, author-code or benchmark reconstruction.

### All maintained fields

provenance: supported. Targets: AIMech:RadicchiEdgeClustering.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 7 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Every field and all seven claims were reviewed. Modified scores, source infinity convention, state-dependent graph roles, unresolved g4 denominator, conditional runtime and social-network evidence limits are explicit. No maintained defect requiring an issue was found; DRAFT remains.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261014T020828Z-radicchi-edge-clustering.json | supports | Compared all 442 pinned AIO and 675 native IDs, names, aliases and scoped synonyms before either cohort write; no normalized identity match. Ignored- and hidden-inclusive searches of all three checkouts returned 16,0,0 lines. All sixteen public matches were read: source citations, previously pending reading notes, query logs and the existing Radicchi source lead, not either maintained identity. Semantic assessment covered 64 AIO and 290 native definitions: 46 AIO and 268 native rows match prior inspected context; all 18 newly selected AIO and 22 native definitions were read. Sixteen complete AIO node/edge/generated contexts were verified unchanged and mapping rationales reassessed. Both drafts were compared for inherited betweenness plus definition filtering versus local cycle-score deletion. Retain the modified edge-clustering divisive family, with the explicit triangle rule and described higher-cycle extension. Its minimum local cycle score differs from maximal shortest-path betweenness even though either selector can use the same definition filter. This family record does not create an extra g3 duplicate or assert an inspected complete g4 implementation. |
| mapping | sources/aio/aio.json | supports | Related HierarchicalClustering and UnsupervisedClustering task mappings preserve algorithm/task scope. Sixteen complete AIO contexts were verified unchanged; four generated YAMLs were reread after capture. Strong/weak graph tests do not mean weakly supervised learning, and local cycles do not make this a recurrent neural or causal model. |
| radicchi2004 | https://arxiv.org/pdf/cond-mat/0309488v2; Section IV, PDF pp. 4–5, Equations 3–5 and edge-removal rule; Section III, p. 4; Section IV, PDF pp. 4–5, Equations 3–4 and update discussion; curator calculation in research/discovery/radicchi-boundaries.py; Section IV, PDF p. 5, paragraph following Equation 5; Figure 5 legend, pp. 8–9; curator calculation in research/discovery/radicchi-boundaries.py; Section IV, PDF p. 5, Equation 5 and g = 3/g = 4 discussion; Sections III–IV, PDF pp. 4–5; Figure 4 legend p. 8 and plot p. 12; Section IV, PDF p. 5, runtime estimate; Figure 5 legend, pp. 8–9 and plot p. 13; Sections III–V, PDF pp. 4–6; Figure 2 and Figure 6 legends, pp. 8–9, plots pp. 10 and 14; Sections V–VI, PDF pp. 6–7 | supports | arXiv cond-mat/0309488v2, 2004-02-27; related PNAS 101:2658–2663, DOI 10.1073/pnas.0400054101. All fourteen pages and 36 references read; rendered pages 3–5 and 9–14 inspected, covering all five equations, the five-step procedure and all six figures. Journal PDF, supporting community lists, author code and data uninspected. |
| calculation | research/discovery/radicchi-boundaries.py | supports | Exact original-adjacency strong/weak tests on a four-path, rejection with only one qualifying child, modified triangle scores above one, source infinity convention on leaf edges and tied scores on a triangle-free cycle. No g4 denominator, author-code or benchmark reconstruction. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- This cohort step adds one DRAFT record, reaching 677 native and 442 unchanged AIO records. The main frontier now has 862 entries, including 473 pending and 58 partly addressed cohorts; nested leads remain.
- All14pages of extractable text including full method,36references and all figure legends read; sparse-text figure pages9and11 visually inspected. All five equations, five-step criterion-filtered GN procedure and all six figures inspected visually. Other pages read in text; figure labels are source presentation, not independent per-node data verification.
- Primary methods were read; no author-code execution, model fitting, paid service, data upload, hardware benchmark or formal theorem certification. Constructed arithmetic examples are not experiment replication.
- Original Documents checkout synchronization and old round141 cleanup remain unapproved after automatic-review rejection; only the isolated recovery checkout is changed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T021559Z-radicchi-edge-clustering
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Radicchi edge-clustering community detection
started_at: '2026-10-14T02:08:53Z'
finished_at: '2026-10-14T02:15:59Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged modified scores versus probabilities,
    current-score graph versus original-validation graph, cycle selection versus betweenness,
    and unfiltered timing versus filtered-pipeline cost. This is adversarial author
    self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Radicchi edge-clustering community detection as a DRAFT algorithm
  family with related AIO tasks. Author self-review supports the explicit triangle
  selector while preserving source infinity, higher-cycle implementation, timing and
  evaluation limits.
source:
  git_revision: e7270db7eb359fdf93eb7815543c52db480f040d
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/BoltzmannMachineNetwork.yaml
    sha256: 1152d2d85c5c1c408a0420e13f211ed109b12fb289c706ee7449864e91aece03
    role: context
  - path: data/aio/CausalGraphicalModel.yaml
    sha256: 868d353893701f2b8bedc9a95ef3219c0659fe230dad792c1932be078874db8b
    role: context
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
    role: context
  - path: data/aio/EthicalLLM.yaml
    sha256: cd35ce670508ad59d04c55392e04f481415e2245c36f87185700b83bf14636f6
    role: context
  - path: data/aio/HierarchicalClassification.yaml
    sha256: 5e1f65090a3a9e7842b57c12410a7279d02c60baef05844fa1dd73545f1cbfc7
    role: context
  - path: data/aio/HierarchicalClustering.yaml
    sha256: 144deaecd150e22de207c11a62f19db5f8409443724bd4be4b5c95c53375b258
    role: context
  - path: data/aio/KnearestNeighborClassificationAlgorithm.yaml
    sha256: c45f4eca7cc4e11444cc9be90d2622f8fd37c5296b0b01ffb7a0b7e7ac17af2a
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/MetricLearning.yaml
    sha256: 9497c86ecf87bce4abc89095d2b6b3e9290c15ec8a853f4f9c91a3b8d041f3fc
    role: context
  - path: data/aio/ModularLLM.yaml
    sha256: 73d7e14187388642a79ea7756f9c4fdd9958e0882e8292b3addf4ab6167a3613
    role: context
  - path: data/aio/ModularLanguageModel.yaml
    sha256: d5de5d9786239ade0804aaa751ff93ef75b782bf61208789772bf4ad83e6595c
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/UnsupervisedClustering.yaml
    sha256: 78d3917b751b29e83802dfd2ceff6b5ee131cd64a5a3a7d40de02f5d2b9bdb1e
    role: context
  - path: data/curated/CNMCommunityDetection.yaml
    sha256: c823bf2f1720f6ceb00148192efcf0a1485d4d6e04cdb92c4751f0993fb7d7cd
    role: context
  - path: data/curated/GirvanNewmanCommunityDetection.yaml
    sha256: 0233486104552b70b0fb6cea4c4cd4cff9eb88e763025e14f1890731084b9afa
    role: context
  - path: data/curated/NewmanGreedyModularity.yaml
    sha256: 088404b5dcb49125570712690b63d3810aac442fff6d21c111a4a1d0dea7fd0c
    role: context
  - path: data/curated/RadicchiEdgeClustering.yaml
    sha256: 65bc71cf027d1693eddf4f670f8126cb84cc29aa35b7a9dfc6b307ee1f5379c9
    role: target
  - path: research/discovery/20261014T020828Z-radicchi-edge-clustering.json
    sha256: b99a1136da0a4375edb656bbdc425178f05eb4bfa481f24b7ec7fc21d557b4e2
    role: context
  - path: research/discovery/radicchi-boundaries.py
    sha256: d0503ca4298ce37dbf20acd5b1a64169bcbb68884b03e4b9b601df989ed51321
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
- target_id: AIMech:RadicchiEdgeClustering
  path: data/curated/RadicchiEdgeClustering.yaml
  label: Radicchi edge-clustering community detection
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RadicchiEdgeClustering.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:RadicchiEdgeClustering'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:RadicchiEdgeClustering
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Uninspected source versions and implementation components
    reason: Journal PDF, supporting community lists, author code and datasets uninspected.
      Higher-cycle denominator, tie and terminal conventions remain bounded uncertainties.
      Finite calculations are not benchmark replication or universal recovery guarantees.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:RadicchiEdgeClustering
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 191.60s (0:03:11)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 677 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 364 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 362,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:RadicchiEdgeClustering
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
  - AIMech:RadicchiEdgeClustering
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
  - AIMech:RadicchiEdgeClustering
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/radicchi-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:RadicchiEdgeClustering
  exit_code: 0
  expected_exit_code: 0
  summary: '{"original_path_children": [{"strong": false, "weak": true, "inward":
    {"0": 1, "1": 1}, "outward": {"0": 0, "1": 1}, "internal_degree_sum": 2, "external_degree_sum":
    1}, {"strong": false, "weak": true, "inward": {"2": 1, "3": 1}, "outward": {"2":
    1, "3": 0}, "internal_degree_sum": 2, "external_degree_sum": 1}], "children_on_deleted_graph":
    [{"strong": true, "weak": true, "inward": {"0": 1, "1": 1}, "outward": {"0": 0,
    "1": 0}, "internal_degree_sum": 2, "external_degree_sum": 0}, {"strong": true,
    "weak": true, "inward": {"2": 1, "3": 1}, "outward": {"2": 0, "3": 0}, "internal_degree_sum":
    2, "external_degree_sum": 0}], "one_qualifying_weak_child_rejected": true, "modified_path_scores":
    {"(0, 1)": "infinity (source convention)", "(1, 2)": "1", "(2, 3)": "infinity
    (source convention)"}, "triangle_score": "2", "four_clique_score": "3/2", "triangle_free_cycle_scores":
    "all1", "scope": "Exact strong/weak degree tests on original adjacency; retention
    needs at least two qualifying children; explicit g3 rankings and source infinity
    convention. None is only an internal sentinel serialized as infinity text. No
    g4 denominator, author implementation, benchmark or universal structural guarantee."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261014T020828Z-radicchi-edge-clustering.json
  accessed_at: '2026-10-14T02:08:53Z'
  support: supports
  summary: 'Compared all 442 pinned AIO and 675 native IDs, names, aliases and scoped
    synonyms before either cohort write; no normalized identity match. Ignored- and
    hidden-inclusive searches of all three checkouts returned 16,0,0 lines. All sixteen
    public matches were read: source citations, previously pending reading notes,
    query logs and the existing Radicchi source lead, not either maintained identity.
    Semantic assessment covered 64 AIO and 290 native definitions: 46 AIO and 268
    native rows match prior inspected context; all 18 newly selected AIO and 22 native
    definitions were read. Sixteen complete AIO node/edge/generated contexts were
    verified unchanged and mapping rationales reassessed. Both drafts were compared
    for inherited betweenness plus definition filtering versus local cycle-score deletion.
    Retain the modified edge-clustering divisive family, with the explicit triangle
    rule and described higher-cycle extension. Its minimum local cycle score differs
    from maximal shortest-path betweenness even though either selector can use the
    same definition filter. This family record does not create an extra g3 duplicate
    or assert an inspected complete g4 implementation.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-14T02:08:53Z'
  support: supports
  summary: Related HierarchicalClustering and UnsupervisedClustering task mappings
    preserve algorithm/task scope. Sixteen complete AIO contexts were verified unchanged;
    four generated YAMLs were reread after capture. Strong/weak graph tests do not
    mean weakly supervised learning, and local cycles do not make this a recurrent
    neural or causal model.
- evidence_id: radicchi2004
  kind: primary_source
  reference: https://arxiv.org/pdf/cond-mat/0309488v2
  locator: Section IV, PDF pp. 4–5, Equations 3–5 and edge-removal rule; Section III,
    p. 4; Section IV, PDF pp. 4–5, Equations 3–4 and update discussion; curator calculation
    in research/discovery/radicchi-boundaries.py; Section IV, PDF p. 5, paragraph
    following Equation 5; Figure 5 legend, pp. 8–9; curator calculation in research/discovery/radicchi-boundaries.py;
    Section IV, PDF p. 5, Equation 5 and g = 3/g = 4 discussion; Sections III–IV,
    PDF pp. 4–5; Figure 4 legend p. 8 and plot p. 12; Section IV, PDF p. 5, runtime
    estimate; Figure 5 legend, pp. 8–9 and plot p. 13; Sections III–V, PDF pp. 4–6;
    Figure 2 and Figure 6 legends, pp. 8–9, plots pp. 10 and 14; Sections V–VI, PDF
    pp. 6–7
  accessed_at: '2026-10-14T01:38:57Z'
  snapshot_sha256: 02467f9e119b7da54139e8df41b62f52c672aa607154951c5c868ef750f2d564
  support: supports
  summary: arXiv cond-mat/0309488v2, 2004-02-27; related PNAS 101:2658–2663, DOI 10.1073/pnas.0400054101.
    All fourteen pages and 36 references read; rendered pages 3–5 and 9–14 inspected,
    covering all five equations, the five-step procedure and all six figures. Journal
    PDF, supporting community lists, author code and data uninspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/radicchi-boundaries.py
  accessed_at: '2026-10-14T02:10:10Z'
  snapshot_sha256: d0503ca4298ce37dbf20acd5b1a64169bcbb68884b03e4b9b601df989ed51321
  support: supports
  summary: Exact original-adjacency strong/weak tests on a four-path, rejection with
    only one qualifying child, modified triangle scores above one, source infinity
    convention on leaf edges and tied scores on a triangle-free cycle. No g4 denominator,
    author-code or benchmark reconstruction.
assessments:
- assessment_id: identity
  area: identity
  topic: Radicchi edge-clustering community detection
  outcome: supported
  target_ids:
  - AIMech:RadicchiEdgeClustering
  evidence_ids:
  - identity
  - radicchi2004
  summary: Retain this distinct DRAFT algorithm.
  details: Retain one family record for the local modified cycle-score selector, including
    the explicit g3 rule and a bounded description of g4. The source distinguishes
    it from maximal-betweenness deletion; shared definition filtering does not collapse
    the identities. No separate redundant g3 record is added.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:RadicchiEdgeClustering
  evidence_ids:
  - mapping
  - radicchi2004
  summary: The explicit AIO mapping assessment is supported within its stated scope.
  details: Related HierarchicalClustering and UnsupervisedClustering task mappings
    preserve algorithm/task scope. Sixteen complete AIO contexts were verified unchanged;
    four generated YAMLs were reread after capture. Strong/weak graph tests do not
    mean weakly supervised learning, and local cycles do not make this a recurrent
    neural or causal model.
- assessment_id: modified-triangle-score
  area: evidence
  topic: modified-triangle-score
  outcome: supported
  target_ids:
  - AIMech:RadicchiEdgeClustering
  evidence_ids:
  - radicchi2004
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equations3–4 distinguish ordinary from plus-one scores. Triangle2 and four-clique3/2
    verify that the modified value is not a probability. The update paragraph supports
    recomputing affected current-neighborhood scores after deletion.
- assessment_id: leaf-and-tie-boundary
  area: evidence
  topic: leaf-and-tie-boundary
  outcome: supported
  target_ids:
  - AIMech:RadicchiEdgeClustering
  evidence_ids:
  - radicchi2004
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The source explicitly assigns infinity to a leaf edge. The finite reference
    uses a sentinel only internally and serializes that convention as text; it does
    not silently divide by zero. The four-cycle gives tied finite1 values. No never-remove
    or unaudited terminal behavior is asserted.
- assessment_id: cycle-family-boundary
  area: evidence
  topic: cycle-family-boundary
  outcome: supported
  target_ids:
  - AIMech:RadicchiEdgeClustering
  evidence_ids:
  - radicchi2004
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equation5 describes possible cycles given degrees without an explicit executable
    g4 denominator. The record retains the demonstrated family and its g4 comparison
    while leaving implementation conventions unresolved instead of supplying an invented
    formula.
- assessment_id: selector-and-filter
  area: evidence
  topic: selector-and-filter
  outcome: supported
  target_ids:
  - AIMech:RadicchiEdgeClustering
  evidence_ids:
  - radicchi2004
  summary: Supported within the stated primary-source and mathematical scope.
  details: The source’s Figure4 discussion explicitly says minimum clustering and
    maximum betweenness edges differ. The original-adjacency at-least-two filter is
    a separate step applicable to either selector; shared validation does not imply
    identical hierarchies.
- assessment_id: runtime-conditions
  area: evidence
  topic: runtime-conditions
  outcome: supported
  target_ids:
  - AIMech:RadicchiEdgeClustering
  evidence_ids:
  - radicchi2004
  summary: Supported within the stated primary-source and mathematical scope.
  details: The estimate assumes local updates with controlled neighborhoods. Figure5’s
    caption explicitly excludes the definition filter and fixes average degree5; the
    draft neither universalizes constant update cost nor attributes those timings
    to the filtered pipeline.
- assessment_id: evaluation-scope
  area: evidence
  topic: evaluation-scope
  outcome: supported
  target_ids:
  - AIMech:RadicchiEdgeClustering
  evidence_ids:
  - radicchi2004
  summary: Supported within the stated primary-source and mathematical scope.
  details: Figure2’s strong/weak and strict-success/node-error comparisons are conditional.
    SectionV distinguishes all15616authors from the largest12722component, and Figure6
    pools all nested weak communities rather than a single flat cut.
- assessment_id: domain-limits
  area: evidence
  topic: domain-limits
  outcome: supported
  target_ids:
  - AIMech:RadicchiEdgeClustering
  evidence_ids:
  - radicchi2004
  summary: Supported within the stated primary-source and mathematical scope.
  details: SectionsV–VI acknowledge subjective collaboration labels and possible short-cycle
    shortages outside social networks. The source proposes future non-social applications
    rather than demonstrating universal biological accuracy.
- assessment_id: constructed-boundaries
  area: consistency
  topic: modified scores versus probabilities, current-score graph versus original-validation
    graph, cycle selection versus betweenness, and unfiltered timing versus filtered-pipeline
    cost
  outcome: supported
  target_ids:
  - AIMech:RadicchiEdgeClustering
  evidence_ids:
  - radicchi2004
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Exact original-adjacency strong/weak tests on a four-path, rejection with
    only one qualifying child, modified triangle scores above one, source infinity
    convention on leaf edges and tied scores on a triangle-free cycle. No g4 denominator,
    author-code or benchmark reconstruction.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:RadicchiEdgeClustering
  evidence_ids:
  - identity
  - mapping
  - radicchi2004
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 7 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. Every field and all seven claims were reviewed. Modified
    scores, source infinity convention, state-dependent graph roles, unresolved g4
    denominator, conditional runtime and social-network evidence limits are explicit.
    No maintained defect requiring an issue was found; DRAFT remains.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- This cohort step adds one DRAFT record, reaching 677 native and 442 unchanged AIO
  records. The main frontier now has 862 entries, including 473 pending and 58 partly
  addressed cohorts; nested leads remain.
- All14pages of extractable text including full method,36references and all figure
  legends read; sparse-text figure pages9and11 visually inspected. All five equations,
  five-step criterion-filtered GN procedure and all six figures inspected visually.
  Other pages read in text; figure labels are source presentation, not independent
  per-node data verification.
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
