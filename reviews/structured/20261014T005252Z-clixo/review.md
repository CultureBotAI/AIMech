# Scientific author self-review of Clique extracted ontology

- Review: 20261014T005252Z-clixo
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-14T00:45:01Z
- Finished UTC: 2026-10-14T00:52:52Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain CliXO as a DRAFT algorithm with related AIO clustering-task mappings. Full scientific author self-review resolves issue 328 by distinguishing different distance scalings from a contradiction, while retaining printed-specification, implementation and evaluation limitations.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:CliXO
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 218dd09207afd164c9f8ec264eb44a47a81ba8fe.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:CliXO | data/curated/CliXO.yaml | maintained | Clique extracted ontology |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:CliXO | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 177.34s (0:02:57)<br>Checked 442 record(s); 0 failed.<br>Checked 666 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 353 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 352,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:CliXO | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:CliXO | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:CliXO | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:CliXO | {"imperfect_example_input_distance": "1", "imperfect_example_root_height": "2", "imperfect_example_pair_distance": "4", "imperfect_example_satisfies_lower_bound": true, "current_maximal_cliques": 8, "necessary_under_simultaneous_full_pool_predicate": 0, "single_missing_edge_clique_sizes": [4, 4], "intersection_size": 3, "minimum_normalized_degree": "3/4", "new_last_threshold_clique_passes_strict_alpha_zero": false, "scope": "Static exact source-predicate checks. No assertion about uninspected implementation ordering, terminal flushing, or general theorem correctness."} |

## Scientific And Domain Assessments

### Clique extracted ontology

identity: supported. Targets: AIMech:CliXO.

Retain this distinct DRAFT algorithm.

Retain the 2014 CliXO informative-clique, persistence and missing-edge-completion heuristic. The ignored-inclusive three-checkout identity audit and 41 AIO/228 native semantic contexts distinguish it from exact PoClustering, greedy edge-cover pruning, OHC density expansion and Llama unions. Later CliXO releases remain version-assessment leads.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:CliXO.

The declared AIO mapping is supported.

Related HierarchicalClustering and UnsupervisedClustering mappings preserve the algorithm/task distinction. The three listed generated AIO YAMLs were reread after capture. Eleven annotated AIO contexts and four full native records inform the bounded identity assessment. No exact AIO equivalence, strict-tree restriction or conditional-dependence interpretation is asserted.

### informative-clique-filter

evidence: supported. Targets: AIMech:CliXO.

Supported within the stated primary-source and mathematical scope.

Section 2.2 defines explained pairs by earlier accepted cliques, necessity by a pair unique within the current clique pool, and informativeness by both conditions. Increasing distances correspond to decreasing similarities. This is distinct from accepting all maximal cliques or merely covering graph edges.

### persistence-noise

evidence: supported. Targets: AIMech:CliXO.

Supported within the stated primary-source and mathematical scope.

Section 2.2.1 uses max pair distance strictly below current threshold minus alpha. The stated signal/noise separation depends on a true but unknown ontology, and the later experiment uses a selected GO subset and tuned parameters. The record does not generalize this to universal recovery or parameter selection.

### missing-edge-completion

evidence: supported. Targets: AIMech:CliXO.

Supported within the stated primary-source and mathematical scope.

Sections 2.2.2–2.2.3 use the minimum normalized degree in a clique union and lower M entries to complete accepted missing edges. The static K5-minus-edge case has two size-four maximal cliques sharing three vertices and minimum normalized degree 3/4. This supports the corrected k−1/k−2 interpretation, not an implementation execution claim.

### ontology-structure-scope

evidence: supported. Targets: AIMech:CliXO.

Supported within the stated primary-source and mathematical scope.

Introduction and Sections 2.1–3.1 distinguish syntactic term/group structure from biological relation meanings. Multiple-parent groups are allowed; indistinguishable terms lost from pairwise data preclude arbitrary ontology recovery. A set-inclusion DAG is not sufficient for a probabilistic-graphical-model mapping.

### printed-specification-boundaries

evidence: supported. Targets: AIMech:CliXO.

Supported within the stated primary-source and mathematical scope.

The stack pseudocode leaves lookahead and exhaustion implicit, while the strict persistence inequality needs a last-threshold policy. The imperfect condition permits output distances at least the input; input 1, root height 2 and terminal path 4 meet that bound and the printed height equation. Thus the corrected scaling wording resolves issue 328 without claiming a contradiction. The simultaneous full-pool K2,2,2 example yields eight maximal cliques but no unique pair; sequential pruning and author code remain uninspected.

### evaluation-design

evidence: supported. Targets: AIMech:CliXO.

Supported within the stated primary-source and mathematical scope.

Sections 2.3–3.3 distinguish GO-derived Resnik reconstruction from GI, expression and YeastNet inputs. Page 8 explicitly identifies GO-trained YeastNet source weights and resulting circularity. One-to-one, structurally constrained alignment uses size-binned permutation thresholds; matching does not imply exact term identity or independent biological validation.

### complexity-and-stability

evidence: supported. Targets: AIMech:CliXO.

Supported within the stated primary-source and mathematical scope.

Section 2.2 gives output-sensitive complexity for the intended dynamic procedure without bounding output size universally. Figure 5 divides matched or identical counts by the smaller ontology; complete containment can coexist with extra terms. Robustness conclusions remain specific to tested networks and parameters.

### perfect versus imperfect distance scaling, informative-clique filtering, terminal thresholds and evaluation circularity

consistency: supported. Targets: AIMech:CliXO.

Constructed calculations support the stated distinctions.

Static necessary-clique, missing-edge-size, normalized-degree and last-threshold checks. No author implementation execution, ordering assumption or general theorem certification. A positive two-terminal example shows that the printed imperfect-case scaling can satisfy its lower-bound requirement and the basic path-height convention; it does not establish perfect-case equality.

### All maintained fields

provenance: supported. Targets: AIMech:CliXO.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 7 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. All seven claims and every maintained field were assessed. Preserve the distinction between perfect-case equality and imperfect-case distance lower bounds; static predicate examples do not establish implementation behavior. Rechecked the GO-trained YeastNet qualification on page 8 and the smaller-ontology stability denominator.

## Findings

### height-scaling-scope: Qualify the height-scaling discrepancy

minor / resolved / confirmed; issue key: aimech-clixo-height-scaling-scope.

The claim and limitation overstate a difference between perfect and imperfect distance scaling as a contradiction with the basic path convention. The imperfect formulation permits enlarged pair distances; a two-terminal case is feasible.

Disposition: Both maintained fields now distinguish the perfect and imperfect formulations without asserting an inherent contradiction. The positive-distance finite example passes; the report mirror and source interpretation are synchronized, an EDIT history sidecar was appended, corrected inputs were captured before reassessment, and all post-edit required gates passed.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261014T004004Z-clixo.json | supports | Compared all 442 pinned AIO and 665 native IDs, names, aliases and scoped synonyms for CliXO, its expanded name and publication identifiers; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 14, 0, 0 lines. All matches were read: only discovery and history notes, with no existing standalone identity. A semantic search including clustering, clique, poset, hierarchy, ontology and community terms covered 41 AIO and 228 native definitions. The 41 AIO and 225 previously read native definitions were unchanged; all three new PoClustering/OHC records were read in full. Eleven complete annotated AIO node/edge/generated contexts and four full native records were assessed. Retain the 2014 informative-clique filtering, persistence and missing-edge-completion heuristic, distinct from exact PoClustering enumeration, greedy edge-cover pruning, OHC density-tolerance expansion and Llama nearest-neighbor unions. Its DAG describes syntactic set hierarchy rather than biological relation meanings. Later code releases remain version-assessment leads. |
| mapping | sources/aio/aio.json | supports | Related HierarchicalClustering and UnsupervisedClustering mappings preserve the algorithm/task distinction. The three listed generated AIO YAMLs were reread after capture. Eleven annotated AIO contexts and four full native records inform the bounded identity assessment. No exact AIO equivalence, strict-tree restriction or conditional-dependence interpretation is asserted. |
| clixo2014 | https://idekerlab.ucsd.edu/wp-content/uploads/publications/kramer_Bioinformatics2014.pdf; Sections 2.1–2.2.3 and Figure 1, PDF pp. 3–4 (printed i36–i37); Section 2.2, displayed CLIXO algorithm and informative-clique definitions, PDF p. 4 (i37); Section 2.2.1, persistence inequality and signal/noise conditions, PDF p. 4 (i37); Section 3.2 and Figure 3, pp. 5–6; Sections 2.2.2–2.2.3, degree condition and matrix update, PDF p. 4 (i37); Introduction, PDF pp. 1–2; Sections 2.1–2.2, pp. 3–4; Section 3.1, information-loss examples, p. 5; Section 2.1.2 condition 4, PDF p. 3; Section 2.2 pseudocode and informative predicate and Section 2.2.1 strict inequality, p. 4; Sections 2.3–3.3 and Figures 2–4, PDF pp. 4–8 (i37–i41); Section 2.2 complexity discussion, PDF p. 4; Section 3.3 and Figure 5, pp. 7–8 | supports | Bioinformatics 30(12), i34–i42, 2014; all nine author-hosted PDF pages, 27 references, algorithm, equations and all six figures read. PubMed confirms bibliographic metadata. Later software releases were not audited. |
| calculation | research/discovery/clixo-boundaries.py | supports | Static necessary-clique, missing-edge-size, normalized-degree and last-threshold checks. No author implementation execution, ordering assumption or general theorem certification. A positive two-terminal example shows that the printed imperfect-case scaling can satisfy its lower-bound requirement and the basic path-height convention; it does not establish perfect-case equality. |
| predecessor | reviews/structured/20261014T004251Z-clixo-height-scope-open/review.yaml | supports | Immutable initial scoped review records the overstatement and the exact maintained target; the current captured record, report mirror, calculator and EDIT history implement the correction. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- This write adds one DRAFT record, reaching 666 native and 442 unchanged AIO records. The main frontier now has 851 entries, including 473 pending and 58 partly addressed cohorts; nested leads remain.
- Read all nine PDF pages, all 27 references, algorithm, six figures and equations. Visually inspected pages3–8, covering every figure and method/metric equation. No supplementary file is cited as read.
- Primary methods were read; no author-code execution, model fitting, paid service, data upload, hardware benchmark or formal theorem certification. Constructed arithmetic examples are not experiment replication.
- Original Documents checkout synchronization and old round141 cleanup remain unapproved after automatic-review rejection; only the isolated recovery checkout is changed.
- The predecessor feasible-scaling check abbreviates its interpreter as python3. Its actual successful invocation used /private/tmp/aimech-recovery-venv/bin/python /private/tmp/aimech-clixo274-open-review.py. The current tracked calculator has no PyYAML dependency and was executed with its recorded python3 command.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T005252Z-clixo
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Clique extracted ontology
started_at: '2026-10-14T00:45:01Z'
finished_at: '2026-10-14T00:52:52Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged perfect versus imperfect distance scaling,
    informative-clique filtering, terminal thresholds and evaluation circularity.
    This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain CliXO as a DRAFT algorithm with related AIO clustering-task mappings.
  Full scientific author self-review resolves issue 328 by distinguishing different
  distance scalings from a contradiction, while retaining printed-specification, implementation
  and evaluation limitations.
source:
  git_revision: 218dd09207afd164c9f8ec264eb44a47a81ba8fe
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/CausalGraphicalModel.yaml
    sha256: 868d353893701f2b8bedc9a95ef3219c0659fe230dad792c1932be078874db8b
    role: context
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
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
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/MetricLearning.yaml
    sha256: 9497c86ecf87bce4abc89095d2b6b3e9290c15ec8a853f4f9c91a3b8d041f3fc
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/UnsupervisedClustering.yaml
    sha256: 78d3917b751b29e83802dfd2ceff6b5ee131cd64a5a3a7d40de02f5d2b9bdb1e
    role: context
  - path: data/curated/CliXO.yaml
    sha256: 68a4f69aab547e5d7c0bded8104c312b719d3f5cad62941e8c44ed697fd61fa8
    role: target
  - path: data/curated/ExactPoClustering.yaml
    sha256: 56c26981ed742c74c9cc8c659983fd47ed1290e52de5b5bfcc1ab6cc256502fa
    role: context
  - path: data/curated/LlamaClustering.yaml
    sha256: 5976b079bdaf20aff6829dbc1dda7c9f591162c54b96db7621e5e7e703ced401
    role: context
  - path: data/curated/OverlappingHierarchicalClustering.yaml
    sha256: 60b0a2241c498995af77bebacf4022732ac2c90b4ccc517b283cbe40f95a8fe4
    role: context
  - path: data/curated/PoClusteringEdgeCliqueCover.yaml
    sha256: 959126aad02a7a1acd0a0698316a0e093868b854a4ca7b9a69fbfaca3b7b5567
    role: context
  - path: research/discovery/20261014T004004Z-clixo.json
    sha256: 5b03bee121bd9700d5549d85690ea13c02ce8d9e34cb2a360e244d9076f99ddb
    role: context
  - path: research/discovery/clixo-boundaries.py
    sha256: a6a6f9323b5883f12ba5dd7eb4b42dcd6ad817943d6c4bf4c35b7de8abaf5879
    role: context
  - path: reviews/structured/20261014T004251Z-clixo-height-scope-open/review.yaml
    sha256: 39e950e27e78c33489860019486070813aacb72543394e810cfe6a0d5dfb0e46
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
- target_id: AIMech:CliXO
  path: data/curated/CliXO.yaml
  label: Clique extracted ontology
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CliXO.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:CliXO'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:CliXO
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Uninspected source versions and implementation components
    reason: All nine primary paper pages read. No author implementation, experimental
      datasets, supplementary material or alternative paper version was audited or
      executed. The version-0.3 landing page supplies provenance only; later releases
      remain leads. Finite examples are not benchmark replication or theorem certification.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:CliXO
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 177.34s (0:02:57)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 666 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 353 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 352,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:CliXO
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
  - AIMech:CliXO
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
  - AIMech:CliXO
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/clixo-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:CliXO
  exit_code: 0
  expected_exit_code: 0
  summary: '{"imperfect_example_input_distance": "1", "imperfect_example_root_height":
    "2", "imperfect_example_pair_distance": "4", "imperfect_example_satisfies_lower_bound":
    true, "current_maximal_cliques": 8, "necessary_under_simultaneous_full_pool_predicate":
    0, "single_missing_edge_clique_sizes": [4, 4], "intersection_size": 3, "minimum_normalized_degree":
    "3/4", "new_last_threshold_clique_passes_strict_alpha_zero": false, "scope": "Static
    exact source-predicate checks. No assertion about uninspected implementation ordering,
    terminal flushing, or general theorem correctness."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261014T004004Z-clixo.json
  accessed_at: '2026-10-14T00:45:01Z'
  support: supports
  summary: 'Compared all 442 pinned AIO and 665 native IDs, names, aliases and scoped
    synonyms for CliXO, its expanded name and publication identifiers; no normalized
    identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery,
    older discovery and original Documents checkouts returned 14, 0, 0 lines. All
    matches were read: only discovery and history notes, with no existing standalone
    identity. A semantic search including clustering, clique, poset, hierarchy, ontology
    and community terms covered 41 AIO and 228 native definitions. The 41 AIO and
    225 previously read native definitions were unchanged; all three new PoClustering/OHC
    records were read in full. Eleven complete annotated AIO node/edge/generated contexts
    and four full native records were assessed. Retain the 2014 informative-clique
    filtering, persistence and missing-edge-completion heuristic, distinct from exact
    PoClustering enumeration, greedy edge-cover pruning, OHC density-tolerance expansion
    and Llama nearest-neighbor unions. Its DAG describes syntactic set hierarchy rather
    than biological relation meanings. Later code releases remain version-assessment
    leads.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-14T00:45:01Z'
  support: supports
  summary: Related HierarchicalClustering and UnsupervisedClustering mappings preserve
    the algorithm/task distinction. The three listed generated AIO YAMLs were reread
    after capture. Eleven annotated AIO contexts and four full native records inform
    the bounded identity assessment. No exact AIO equivalence, strict-tree restriction
    or conditional-dependence interpretation is asserted.
- evidence_id: clixo2014
  kind: primary_source
  reference: https://idekerlab.ucsd.edu/wp-content/uploads/publications/kramer_Bioinformatics2014.pdf
  locator: Sections 2.1–2.2.3 and Figure 1, PDF pp. 3–4 (printed i36–i37); Section
    2.2, displayed CLIXO algorithm and informative-clique definitions, PDF p. 4 (i37);
    Section 2.2.1, persistence inequality and signal/noise conditions, PDF p. 4 (i37);
    Section 3.2 and Figure 3, pp. 5–6; Sections 2.2.2–2.2.3, degree condition and
    matrix update, PDF p. 4 (i37); Introduction, PDF pp. 1–2; Sections 2.1–2.2, pp.
    3–4; Section 3.1, information-loss examples, p. 5; Section 2.1.2 condition 4,
    PDF p. 3; Section 2.2 pseudocode and informative predicate and Section 2.2.1 strict
    inequality, p. 4; Sections 2.3–3.3 and Figures 2–4, PDF pp. 4–8 (i37–i41); Section
    2.2 complexity discussion, PDF p. 4; Section 3.3 and Figure 5, pp. 7–8
  accessed_at: '2026-10-14T00:19:09Z'
  snapshot_sha256: 82c7c90990c159f0b84395587611e74627df18ee2a4a2612ba53f3a06d31c509
  support: supports
  summary: Bioinformatics 30(12), i34–i42, 2014; all nine author-hosted PDF pages,
    27 references, algorithm, equations and all six figures read. PubMed confirms
    bibliographic metadata. Later software releases were not audited.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/clixo-boundaries.py
  accessed_at: '2026-10-14T00:48:42Z'
  snapshot_sha256: a6a6f9323b5883f12ba5dd7eb4b42dcd6ad817943d6c4bf4c35b7de8abaf5879
  support: supports
  summary: Static necessary-clique, missing-edge-size, normalized-degree and last-threshold
    checks. No author implementation execution, ordering assumption or general theorem
    certification. A positive two-terminal example shows that the printed imperfect-case
    scaling can satisfy its lower-bound requirement and the basic path-height convention;
    it does not establish perfect-case equality.
- evidence_id: predecessor
  kind: record_content
  reference: reviews/structured/20261014T004251Z-clixo-height-scope-open/review.yaml
  accessed_at: '2026-10-14T00:45:01Z'
  snapshot_sha256: 39e950e27e78c33489860019486070813aacb72543394e810cfe6a0d5dfb0e46
  support: supports
  summary: Immutable initial scoped review records the overstatement and the exact
    maintained target; the current captured record, report mirror, calculator and
    EDIT history implement the correction.
assessments:
- assessment_id: identity
  area: identity
  topic: Clique extracted ontology
  outcome: supported
  target_ids:
  - AIMech:CliXO
  evidence_ids:
  - identity
  - clixo2014
  summary: Retain this distinct DRAFT algorithm.
  details: Retain the 2014 CliXO informative-clique, persistence and missing-edge-completion
    heuristic. The ignored-inclusive three-checkout identity audit and 41 AIO/228
    native semantic contexts distinguish it from exact PoClustering, greedy edge-cover
    pruning, OHC density expansion and Llama unions. Later CliXO releases remain version-assessment
    leads.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:CliXO
  evidence_ids:
  - mapping
  - clixo2014
  summary: The declared AIO mapping is supported.
  details: Related HierarchicalClustering and UnsupervisedClustering mappings preserve
    the algorithm/task distinction. The three listed generated AIO YAMLs were reread
    after capture. Eleven annotated AIO contexts and four full native records inform
    the bounded identity assessment. No exact AIO equivalence, strict-tree restriction
    or conditional-dependence interpretation is asserted.
- assessment_id: informative-clique-filter
  area: evidence
  topic: informative-clique-filter
  outcome: supported
  target_ids:
  - AIMech:CliXO
  evidence_ids:
  - clixo2014
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section 2.2 defines explained pairs by earlier accepted cliques, necessity
    by a pair unique within the current clique pool, and informativeness by both conditions.
    Increasing distances correspond to decreasing similarities. This is distinct from
    accepting all maximal cliques or merely covering graph edges.
- assessment_id: persistence-noise
  area: evidence
  topic: persistence-noise
  outcome: supported
  target_ids:
  - AIMech:CliXO
  evidence_ids:
  - clixo2014
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section 2.2.1 uses max pair distance strictly below current threshold minus
    alpha. The stated signal/noise separation depends on a true but unknown ontology,
    and the later experiment uses a selected GO subset and tuned parameters. The record
    does not generalize this to universal recovery or parameter selection.
- assessment_id: missing-edge-completion
  area: evidence
  topic: missing-edge-completion
  outcome: supported
  target_ids:
  - AIMech:CliXO
  evidence_ids:
  - clixo2014
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Sections 2.2.2–2.2.3 use the minimum normalized degree in a clique union
    and lower M entries to complete accepted missing edges. The static K5-minus-edge
    case has two size-four maximal cliques sharing three vertices and minimum normalized
    degree 3/4. This supports the corrected k−1/k−2 interpretation, not an implementation
    execution claim.
- assessment_id: ontology-structure-scope
  area: evidence
  topic: ontology-structure-scope
  outcome: supported
  target_ids:
  - AIMech:CliXO
  evidence_ids:
  - clixo2014
  summary: Supported within the stated primary-source and mathematical scope.
  details: Introduction and Sections 2.1–3.1 distinguish syntactic term/group structure
    from biological relation meanings. Multiple-parent groups are allowed; indistinguishable
    terms lost from pairwise data preclude arbitrary ontology recovery. A set-inclusion
    DAG is not sufficient for a probabilistic-graphical-model mapping.
- assessment_id: printed-specification-boundaries
  area: evidence
  topic: printed-specification-boundaries
  outcome: supported
  target_ids:
  - AIMech:CliXO
  evidence_ids:
  - clixo2014
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The stack pseudocode leaves lookahead and exhaustion implicit, while the
    strict persistence inequality needs a last-threshold policy. The imperfect condition
    permits output distances at least the input; input 1, root height 2 and terminal
    path 4 meet that bound and the printed height equation. Thus the corrected scaling
    wording resolves issue 328 without claiming a contradiction. The simultaneous
    full-pool K2,2,2 example yields eight maximal cliques but no unique pair; sequential
    pruning and author code remain uninspected.
- assessment_id: evaluation-design
  area: evidence
  topic: evaluation-design
  outcome: supported
  target_ids:
  - AIMech:CliXO
  evidence_ids:
  - clixo2014
  summary: Supported within the stated primary-source and mathematical scope.
  details: Sections 2.3–3.3 distinguish GO-derived Resnik reconstruction from GI,
    expression and YeastNet inputs. Page 8 explicitly identifies GO-trained YeastNet
    source weights and resulting circularity. One-to-one, structurally constrained
    alignment uses size-binned permutation thresholds; matching does not imply exact
    term identity or independent biological validation.
- assessment_id: complexity-and-stability
  area: evidence
  topic: complexity-and-stability
  outcome: supported
  target_ids:
  - AIMech:CliXO
  evidence_ids:
  - clixo2014
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section 2.2 gives output-sensitive complexity for the intended dynamic
    procedure without bounding output size universally. Figure 5 divides matched or
    identical counts by the smaller ontology; complete containment can coexist with
    extra terms. Robustness conclusions remain specific to tested networks and parameters.
- assessment_id: constructed-boundaries
  area: consistency
  topic: perfect versus imperfect distance scaling, informative-clique filtering,
    terminal thresholds and evaluation circularity
  outcome: supported
  target_ids:
  - AIMech:CliXO
  evidence_ids:
  - clixo2014
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Static necessary-clique, missing-edge-size, normalized-degree and last-threshold
    checks. No author implementation execution, ordering assumption or general theorem
    certification. A positive two-terminal example shows that the printed imperfect-case
    scaling can satisfy its lower-bound requirement and the basic path-height convention;
    it does not establish perfect-case equality.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:CliXO
  evidence_ids:
  - identity
  - mapping
  - clixo2014
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 7 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. All seven claims and every maintained field were assessed.
    Preserve the distinction between perfect-case equality and imperfect-case distance
    lower bounds; static predicate examples do not establish implementation behavior.
    Rechecked the GO-trained YeastNet qualification on page 8 and the smaller-ontology
    stability denominator.
findings:
- finding_id: height-scaling-scope
  issue_key: aimech-clixo-height-scaling-scope
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Qualify the height-scaling discrepancy
  description: The claim and limitation overstate a difference between perfect and
    imperfect distance scaling as a contradiction with the basic path convention.
    The imperfect formulation permits enlarged pair distances; a two-terminal case
    is feasible.
  target_ids:
  - AIMech:CliXO
  field_paths:
  - claims[claim_id=printed-specification-boundaries].statement
  - limitations[2]
  evidence_ids:
  - clixo2014
  - calculation
  - predecessor
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CliXO.yaml
    role: maintained
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/328
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261014T004251Z-clixo-height-scope-open
    finding_id: height-scaling-scope
  disposition_reason: Both maintained fields now distinguish the perfect and imperfect
    formulations without asserting an inherent contradiction. The positive-distance
    finite example passes; the report mirror and source interpretation are synchronized,
    an EDIT history sidecar was appended, corrected inputs were captured before reassessment,
    and all post-edit required gates passed.
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- This write adds one DRAFT record, reaching 666 native and 442 unchanged AIO records.
  The main frontier now has 851 entries, including 473 pending and 58 partly addressed
  cohorts; nested leads remain.
- Read all nine PDF pages, all 27 references, algorithm, six figures and equations.
  Visually inspected pages3–8, covering every figure and method/metric equation. No
  supplementary file is cited as read.
- Primary methods were read; no author-code execution, model fitting, paid service,
  data upload, hardware benchmark or formal theorem certification. Constructed arithmetic
  examples are not experiment replication.
- Original Documents checkout synchronization and old round141 cleanup remain unapproved
  after automatic-review rejection; only the isolated recovery checkout is changed.
related_reviews:
- repository: CultureBotAI/AIMech
  review_id: 20261014T004251Z-clixo-height-scope-open
  relationship: Supersedes the open height-scaling-scope finding with an evidence-backed
    resolution for the same maintained target.
links:
- https://github.com/CultureBotAI/AIMech/issues/328
notes:
- The predecessor feasible-scaling check abbreviates its interpreter as python3. Its
  actual successful invocation used /private/tmp/aimech-recovery-venv/bin/python /private/tmp/aimech-clixo274-open-review.py.
  The current tracked calculator has no PyYAML dependency and was executed with its
  recorded python3 command.
tags:
- native-concepts
- self-review
- discovery-ongoing
```
