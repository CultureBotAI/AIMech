# Scientific author self-review of Clauset–Newman–Moore community detection

- Review: 20261014T014331Z-cnm-community-detection
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-14T01:37:15Z
- Finished UTC: 2026-10-14T01:43:31Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain CNM community detection as a DRAFT algorithm with related AIO clustering tasks. Adversarial author self-review supports the sparse greedy mechanism while preserving the v2 printed normalization mismatch, documented connected-input restriction, conditional complexity and finite greedy-optimality limit.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:CNMCommunityDetection
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c38639813a553aff13485dc8e90c13629330853e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:CNMCommunityDetection | data/curated/CNMCommunityDetection.yaml | maintained | Clauset–Newman–Moore community detection |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:CNMCommunityDetection | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 160.63s (0:02:40)<br>Checked 442 record(s); 0 failed.<br>Checked 673 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 360 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 359,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:CNMCommunityDetection | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:CNMCommunityDetection | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:CNMCommunityDetection | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:CNMCommunityDetection | {"printed_initial_gain": "1/8", "definition_initial_gain": "1/4", "printed_second_gain": "0", "definition_second_gain": "1/8", "literal_accumulated_final_q": "-1/4", "definition_one_block_q": "0", "definition_based_six_path_joins": [[[0], [1], "4/25"], [[4], [5], "4/25"], [[2], [3], "3/25"], [[0, 1], [2, 3], "-1/25"], [[0, 1, 2, 3], [4, 5], "-11/50"]], "definition_based_six_path_trajectory": ["-9/50", "-1/50", "7/50", "13/50", "11/50", "0"], "greedy_peak": "13/50", "better_two_triple_partition_q": "3/10", "disconnected_remaining_groups": 2, "disconnected_adjacent_candidates": 0, "scope": "Separate checks of printed formulas, a six-node exact-definition greedy reference with fixed ties, and disconnected candidate exhaustion. No author software, benchmark data, universal failure or implementation conformance is asserted."} |

## Scientific And Domain Assessments

### Clauset–Newman–Moore community detection

identity: supported. Targets: AIMech:CNMCommunityDetection.

Retain this distinct DRAFT algorithm.

The author catalog identifies CNM with this 2004 greedy modularity method. Current identity checks cover 672 native and 442 AIO records with ignored-inclusive searches; no exact match was found. HAC-Q retains a related score for hierarchical link estimation, whereas CNM denotes the sparse community-merge procedure. The 2008 hierarchical random-graph model is a distinct pending lead.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:CNMCommunityDetection.

The explicit AIO mapping assessment is supported within its stated scope.

Related clustering-task mappings preserve the distinction between the CNM algorithm and task classes. Sixteen complete AIO contexts were assessed; four generated YAMLs were reread after capture. Modularity of graph partitions does not identify a modular language model, causal graph or probabilistic dependency structure.

### modularity-agglomeration

evidence: supported. Targets: AIMech:CNMCommunityDetection.

Supported within the stated primary-source and mathematical scope.

Equations 4–7 and algorithm steps define modularity and singleton agglomeration; the recorded merge trajectory supports selecting its maximum-Q cut. The author output documentation distinguishes merge history from a selected group partition. Approximate optimization is not global maximization.

### sparse-update-structures

evidence: supported. Targets: AIMech:CNMCommunityDetection.

Supported within the stated primary-source and mathematical scope.

The three listed data structures on page 3 store adjacent-pair sparse rows, per-row and global maxima and degree fractions; Equation 10 separates common and one-sided neighbors. An omitted nonadjacent pair has nonpositive true change, not necessarily zero.

### printed-normalization-boundary

evidence: supported. Targets: AIMech:CNMCommunityDetection.

Supported within the stated primary-source and mathematical scope.

Rendered v2 Equation 8 has 1/(2m) minus ki kj/(2m)^2 for connected singletons, half the change derived by merging terms in Equations 4/7. Equation 10 retains twice the degree-fraction product. The exact three-node path confirms gains 1/8 versus 1/4, then 0 versus 1/8 and final literal -1/4 versus objective 0. This is a version-scoped printed inconsistency; no uninspected author-code error is asserted.

### documented-input-and-output-scope

evidence: supported. Targets: AIMech:CNMCommunityDetection.

Supported within the stated primary-source and mathematical scope.

The complete author page explicitly requires a single connected component with no self-loops or multiple edges and describes the original unweighted undirected program. The disconnected-components calculation explains candidate exhaustion outside that stated domain. Merge-history and selected-step group outputs are documented; the linked weighted extension remains uninspected.

### complexity-and-ties

evidence: supported. Targets: AIMech:CNMCommunityDetection.

Supported within the stated primary-source and mathematical scope.

Pages 3–5 derive O(m d log n); the sparse balanced assumptions produce O(n log-squared n). Page 4 describes the row-scan alternative, extra worst-case factor and tie-induced hierarchy differences. The record avoids unqualified runtime or output-equivalence claims.

### greedy-optimality-boundary

evidence: supported. Targets: AIMech:CNMCommunityDetection.

Supported within the stated primary-source and mathematical scope.

The separate reference procedure recomputes exact modularity gains and uses adjacent merges with fixed lexicographic ties. On the six-node path its best value is 13/50, below the feasible consecutive-triple partition at 3/10. This shows a finite greedy failure without running author software or claiming that alternative is the global optimum.

### evaluation-scope

evidence: supported. Targets: AIMech:CNMCommunityDetection.

Supported within the stated primary-source and mathematical scope.

Pages 4–5 study the August 2003 symmetrized Amazon largest component and report peak modularity, a community visualization and informal group descriptions. Table I and Figure 3 support only the scoped case study. Neither comprehensive ground truth nor a universal distribution law is established.

### printed initialization versus objective-consistent gains, documented connected input, implementation ties and greedy versus global optimality

consistency: supported. Targets: AIMech:CNMCommunityDetection.

Constructed calculations support the stated distinctions.

Three separate exact finite checks: literal arXiv v2 initialization/update normalization on a three-node path; a definition-based six-node greedy reference with lexicographic ties whose best cut is worse than a feasible alternative; and adjacent-candidate exhaustion on two disconnected components. No author code or implementation conformance is asserted.

### All maintained fields

provenance: supported. Targets: AIMech:CNMCommunityDetection.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 7 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. All seven claims and remaining maintained fields were assessed against the inspected sources. The printed-factor discrepancy, input restriction and finite greedy counterexample are separate, explicitly bounded observations. No repository defect was identified. DRAFT remains.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261014T013706Z-cnm-community-detection.json | supports | Compared all 442 pinned AIO and 672 native IDs, names, aliases and scoped synonyms for CNM and publication identifiers; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 79, 0 and 0 lines. All 79 public matches were read and are existing HAC-Q/source/discovery context and rendered counterparts, not this maintained identity. Semantic assessment covered 46 AIO and 267 native definitions: all 46 AIO and 264 previous native rows were unchanged and three new variant definitions and full records were read. Sixteen complete annotated AIO node/edge/generated contexts were verified unchanged and candidate-specific native records assessed. The author catalog identifies CNM with the 2004 sparse greedy modularity method. It is distinct from the 2008 hierarchical random-graph model and the HAC-Q link-prediction variant. The record preserves the earlier greedy objective as context without treating every modularity optimizer as this algorithm. |
| mapping | sources/aio/aio.json | supports | Related clustering-task mappings preserve the distinction between the CNM algorithm and task classes. Sixteen complete AIO contexts were assessed; four generated YAMLs were reread after capture. Modularity of graph partitions does not identify a modular language model, causal graph or probabilistic dependency structure. |
| clauset2004 | https://arxiv.org/pdf/cond-mat/0408187v2; Sections I–II, PDF pp. 1–4, Equations 4–10 and algorithm/data-structure descriptions; Section II, PDF pp. 2–3, Equations 4–7 and algorithm steps; Section III, p. 4 and Figure 1; Section II, PDF p. 3, three data structures and Equations 8–10; Section II, PDF pp. 2–3, Equations 4, 7, 8 and 10, algorithm step 2; curator calculation in research/discovery/cnm-boundaries.py; Section II, PDF p. 3, sparse support and stopping step; curator disconnected-components example in research/discovery/cnm-boundaries.py; Section II, PDF pp. 3–4, runtime argument and scan implementation; Conclusions, p. 5; Section II, PDF p. 2, approximate optimization and Equation 4; curator reference calculation in research/discovery/cnm-boundaries.py; Section III and Conclusions, PDF pp. 4–5, Figures 1–3 and Table I; Reference note 14, p. 6 | supports | arXiv cond-mat/0408187v2, 2004-08-30. All six pages and 37 references read; pages 2–5 rendered and visually assessed, including Equations 1–10, all three figures, Table I and algorithm descriptions. Journal and v1 PDFs not compared. |
| cnm-docs | https://www.cs.unm.edu/~aaron/research/fastmodularity.htm; Mandatory file outputs: .info and .joins; optional .groups output; Introduction and October 2008 update; Input file requirements; Common error messages; File outputs | supports | Complete author HTML snapshot accessed 2026-10-14. Historical footer dated 2005-10-05 with updates through 2009; not an inspected code-release version. Input requirements and output definitions read; code archives and weighted extension uninspected. |
| calculation | research/discovery/cnm-boundaries.py | supports | Three separate exact finite checks: literal arXiv v2 initialization/update normalization on a three-node path; a definition-based six-node greedy reference with lexicographic ties whose best cut is worse than a feasible alternative; and adjacent-candidate exhaustion on two disconnected components. No author code or implementation conformance is asserted. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- This cohort step adds one DRAFT record, reaching 673 native and 442 unchanged AIO records. The main frontier now has 858 entries, including 473 pending and 58 partly addressed cohorts; nested leads remain.
- All six pages, all37 references and complete abstract read from column-order-preserving extraction. All method equations1–10, pseudocode, all three figures and TableI visually inspected. Pages1 and6 text read; not separately visually reread. Complete author HTML snapshot and all catalog entries also read.
- Primary methods were read; no author-code execution, model fitting, paid service, data upload, hardware benchmark or formal theorem certification. Constructed arithmetic examples are not experiment replication.
- Original Documents checkout synchronization and old round141 cleanup remain unapproved after automatic-review rejection; only the isolated recovery checkout is changed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T014331Z-cnm-community-detection
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Clauset–Newman–Moore community detection
started_at: '2026-10-14T01:37:15Z'
finished_at: '2026-10-14T01:43:31Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged printed initialization versus objective-consistent
    gains, documented connected input, implementation ties and greedy versus global
    optimality. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain CNM community detection as a DRAFT algorithm with related AIO clustering
  tasks. Adversarial author self-review supports the sparse greedy mechanism while
  preserving the v2 printed normalization mismatch, documented connected-input restriction,
  conditional complexity and finite greedy-optimality limit.
source:
  git_revision: c38639813a553aff13485dc8e90c13629330853e
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
    role: target
  - path: data/curated/HACE.yaml
    sha256: 25785e346c454d984ef90a3d625470586b5322b37b9b0852249f5e4655df099e
    role: context
  - path: data/curated/HACES.yaml
    sha256: 9744802e7708270aecb44a9cb0b9c39600d5629f25a3b008490353bf1d9f7d83
    role: context
  - path: data/curated/HACML.yaml
    sha256: 06a6b1b83616ce816b112084bfcfb2f29cd061a2fa0d07c3b66c6e2cfcbaae4a
    role: context
  - path: data/curated/HACQ.yaml
    sha256: f35a5f52f48d7e218b57d118c9271234b59f9858bcd9727acd3d8738f7b5ea81
    role: context
  - path: research/discovery/20261014T013706Z-cnm-community-detection.json
    sha256: 3aa3f15d85b533cc6e7b182163e32198aa490ca646d90601e59a39b771c70946
    role: context
  - path: research/discovery/cnm-boundaries.py
    sha256: 22ef5a3e88c59ad5f06bb0c73466eac3f5b2132f715406ed9a7b957146b5c333
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
- target_id: AIMech:CNMCommunityDetection
  path: data/curated/CNMCommunityDetection.yaml
  label: Clauset–Newman–Moore community detection
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CNMCommunityDetection.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:CNMCommunityDetection'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:CNMCommunityDetection
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Uninspected source versions and implementation components
    reason: Journal PDF and arXiv v1 were not compared. Author code, weighted extension,
      datasets and library implementations were not inspected or executed. The 50-page
      HSBM v3 remains abstract/metadata-only context. No full theorem certification
      or benchmark replication.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:CNMCommunityDetection
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 160.63s (0:02:40)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 673 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 360 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 359,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:CNMCommunityDetection
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
  - AIMech:CNMCommunityDetection
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
  - AIMech:CNMCommunityDetection
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/cnm-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:CNMCommunityDetection
  exit_code: 0
  expected_exit_code: 0
  summary: '{"printed_initial_gain": "1/8", "definition_initial_gain": "1/4", "printed_second_gain":
    "0", "definition_second_gain": "1/8", "literal_accumulated_final_q": "-1/4", "definition_one_block_q":
    "0", "definition_based_six_path_joins": [[[0], [1], "4/25"], [[4], [5], "4/25"],
    [[2], [3], "3/25"], [[0, 1], [2, 3], "-1/25"], [[0, 1, 2, 3], [4, 5], "-11/50"]],
    "definition_based_six_path_trajectory": ["-9/50", "-1/50", "7/50", "13/50", "11/50",
    "0"], "greedy_peak": "13/50", "better_two_triple_partition_q": "3/10", "disconnected_remaining_groups":
    2, "disconnected_adjacent_candidates": 0, "scope": "Separate checks of printed
    formulas, a six-node exact-definition greedy reference with fixed ties, and disconnected
    candidate exhaustion. No author software, benchmark data, universal failure or
    implementation conformance is asserted."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261014T013706Z-cnm-community-detection.json
  accessed_at: '2026-10-14T01:37:15Z'
  support: supports
  summary: 'Compared all 442 pinned AIO and 672 native IDs, names, aliases and scoped
    synonyms for CNM and publication identifiers; no normalized identity match. Ignored-
    and hidden-inclusive fixed-string searches of the recovery, older discovery and
    original Documents checkouts returned 79, 0 and 0 lines. All 79 public matches
    were read and are existing HAC-Q/source/discovery context and rendered counterparts,
    not this maintained identity. Semantic assessment covered 46 AIO and 267 native
    definitions: all 46 AIO and 264 previous native rows were unchanged and three
    new variant definitions and full records were read. Sixteen complete annotated
    AIO node/edge/generated contexts were verified unchanged and candidate-specific
    native records assessed. The author catalog identifies CNM with the 2004 sparse
    greedy modularity method. It is distinct from the 2008 hierarchical random-graph
    model and the HAC-Q link-prediction variant. The record preserves the earlier
    greedy objective as context without treating every modularity optimizer as this
    algorithm.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-14T01:37:15Z'
  support: supports
  summary: Related clustering-task mappings preserve the distinction between the CNM
    algorithm and task classes. Sixteen complete AIO contexts were assessed; four
    generated YAMLs were reread after capture. Modularity of graph partitions does
    not identify a modular language model, causal graph or probabilistic dependency
    structure.
- evidence_id: clauset2004
  kind: primary_source
  reference: https://arxiv.org/pdf/cond-mat/0408187v2
  locator: Sections I–II, PDF pp. 1–4, Equations 4–10 and algorithm/data-structure
    descriptions; Section II, PDF pp. 2–3, Equations 4–7 and algorithm steps; Section
    III, p. 4 and Figure 1; Section II, PDF p. 3, three data structures and Equations
    8–10; Section II, PDF pp. 2–3, Equations 4, 7, 8 and 10, algorithm step 2; curator
    calculation in research/discovery/cnm-boundaries.py; Section II, PDF p. 3, sparse
    support and stopping step; curator disconnected-components example in research/discovery/cnm-boundaries.py;
    Section II, PDF pp. 3–4, runtime argument and scan implementation; Conclusions,
    p. 5; Section II, PDF p. 2, approximate optimization and Equation 4; curator reference
    calculation in research/discovery/cnm-boundaries.py; Section III and Conclusions,
    PDF pp. 4–5, Figures 1–3 and Table I; Reference note 14, p. 6
  accessed_at: '2026-10-14T01:23:17Z'
  snapshot_sha256: a0f3adfe111be62362127e448150867a26e543d0aae22558efa6df51d94f5d1b
  support: supports
  summary: arXiv cond-mat/0408187v2, 2004-08-30. All six pages and 37 references read;
    pages 2–5 rendered and visually assessed, including Equations 1–10, all three
    figures, Table I and algorithm descriptions. Journal and v1 PDFs not compared.
- evidence_id: cnm-docs
  kind: primary_source
  reference: https://www.cs.unm.edu/~aaron/research/fastmodularity.htm
  locator: 'Mandatory file outputs: .info and .joins; optional .groups output; Introduction
    and October 2008 update; Input file requirements; Common error messages; File
    outputs'
  accessed_at: '2026-10-14T01:30:26Z'
  snapshot_sha256: 589febc769218e43e0eb83f3184b3086b1547e909366669d668558329a6a5e3f
  support: supports
  summary: Complete author HTML snapshot accessed 2026-10-14. Historical footer dated
    2005-10-05 with updates through 2009; not an inspected code-release version. Input
    requirements and output definitions read; code archives and weighted extension
    uninspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/cnm-boundaries.py
  accessed_at: '2026-10-14T01:38:01Z'
  snapshot_sha256: 22ef5a3e88c59ad5f06bb0c73466eac3f5b2132f715406ed9a7b957146b5c333
  support: supports
  summary: 'Three separate exact finite checks: literal arXiv v2 initialization/update
    normalization on a three-node path; a definition-based six-node greedy reference
    with lexicographic ties whose best cut is worse than a feasible alternative; and
    adjacent-candidate exhaustion on two disconnected components. No author code or
    implementation conformance is asserted.'
assessments:
- assessment_id: identity
  area: identity
  topic: Clauset–Newman–Moore community detection
  outcome: supported
  target_ids:
  - AIMech:CNMCommunityDetection
  evidence_ids:
  - identity
  - clauset2004
  - cnm-docs
  summary: Retain this distinct DRAFT algorithm.
  details: The author catalog identifies CNM with this 2004 greedy modularity method.
    Current identity checks cover 672 native and 442 AIO records with ignored-inclusive
    searches; no exact match was found. HAC-Q retains a related score for hierarchical
    link estimation, whereas CNM denotes the sparse community-merge procedure. The
    2008 hierarchical random-graph model is a distinct pending lead.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:CNMCommunityDetection
  evidence_ids:
  - mapping
  - clauset2004
  - cnm-docs
  summary: The explicit AIO mapping assessment is supported within its stated scope.
  details: Related clustering-task mappings preserve the distinction between the CNM
    algorithm and task classes. Sixteen complete AIO contexts were assessed; four
    generated YAMLs were reread after capture. Modularity of graph partitions does
    not identify a modular language model, causal graph or probabilistic dependency
    structure.
- assessment_id: modularity-agglomeration
  area: evidence
  topic: modularity-agglomeration
  outcome: supported
  target_ids:
  - AIMech:CNMCommunityDetection
  evidence_ids:
  - clauset2004
  - cnm-docs
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equations 4–7 and algorithm steps define modularity and singleton agglomeration;
    the recorded merge trajectory supports selecting its maximum-Q cut. The author
    output documentation distinguishes merge history from a selected group partition.
    Approximate optimization is not global maximization.
- assessment_id: sparse-update-structures
  area: evidence
  topic: sparse-update-structures
  outcome: supported
  target_ids:
  - AIMech:CNMCommunityDetection
  evidence_ids:
  - clauset2004
  summary: Supported within the stated primary-source and mathematical scope.
  details: The three listed data structures on page 3 store adjacent-pair sparse rows,
    per-row and global maxima and degree fractions; Equation 10 separates common and
    one-sided neighbors. An omitted nonadjacent pair has nonpositive true change,
    not necessarily zero.
- assessment_id: printed-normalization-boundary
  area: evidence
  topic: printed-normalization-boundary
  outcome: supported
  target_ids:
  - AIMech:CNMCommunityDetection
  evidence_ids:
  - clauset2004
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Rendered v2 Equation 8 has 1/(2m) minus ki kj/(2m)^2 for connected singletons,
    half the change derived by merging terms in Equations 4/7. Equation 10 retains
    twice the degree-fraction product. The exact three-node path confirms gains 1/8
    versus 1/4, then 0 versus 1/8 and final literal -1/4 versus objective 0. This
    is a version-scoped printed inconsistency; no uninspected author-code error is
    asserted.
- assessment_id: documented-input-and-output-scope
  area: evidence
  topic: documented-input-and-output-scope
  outcome: supported
  target_ids:
  - AIMech:CNMCommunityDetection
  evidence_ids:
  - cnm-docs
  - clauset2004
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The complete author page explicitly requires a single connected component
    with no self-loops or multiple edges and describes the original unweighted undirected
    program. The disconnected-components calculation explains candidate exhaustion
    outside that stated domain. Merge-history and selected-step group outputs are
    documented; the linked weighted extension remains uninspected.
- assessment_id: complexity-and-ties
  area: evidence
  topic: complexity-and-ties
  outcome: supported
  target_ids:
  - AIMech:CNMCommunityDetection
  evidence_ids:
  - clauset2004
  summary: Supported within the stated primary-source and mathematical scope.
  details: Pages 3–5 derive O(m d log n); the sparse balanced assumptions produce
    O(n log-squared n). Page 4 describes the row-scan alternative, extra worst-case
    factor and tie-induced hierarchy differences. The record avoids unqualified runtime
    or output-equivalence claims.
- assessment_id: greedy-optimality-boundary
  area: evidence
  topic: greedy-optimality-boundary
  outcome: supported
  target_ids:
  - AIMech:CNMCommunityDetection
  evidence_ids:
  - clauset2004
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The separate reference procedure recomputes exact modularity gains and
    uses adjacent merges with fixed lexicographic ties. On the six-node path its best
    value is 13/50, below the feasible consecutive-triple partition at 3/10. This
    shows a finite greedy failure without running author software or claiming that
    alternative is the global optimum.
- assessment_id: evaluation-scope
  area: evidence
  topic: evaluation-scope
  outcome: supported
  target_ids:
  - AIMech:CNMCommunityDetection
  evidence_ids:
  - clauset2004
  summary: Supported within the stated primary-source and mathematical scope.
  details: Pages 4–5 study the August 2003 symmetrized Amazon largest component and
    report peak modularity, a community visualization and informal group descriptions.
    Table I and Figure 3 support only the scoped case study. Neither comprehensive
    ground truth nor a universal distribution law is established.
- assessment_id: constructed-boundaries
  area: consistency
  topic: printed initialization versus objective-consistent gains, documented connected
    input, implementation ties and greedy versus global optimality
  outcome: supported
  target_ids:
  - AIMech:CNMCommunityDetection
  evidence_ids:
  - clauset2004
  - cnm-docs
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: 'Three separate exact finite checks: literal arXiv v2 initialization/update
    normalization on a three-node path; a definition-based six-node greedy reference
    with lexicographic ties whose best cut is worse than a feasible alternative; and
    adjacent-candidate exhaustion on two disconnected components. No author code or
    implementation conformance is asserted.'
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:CNMCommunityDetection
  evidence_ids:
  - identity
  - mapping
  - clauset2004
  - cnm-docs
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 7 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. All seven claims and remaining maintained fields were
    assessed against the inspected sources. The printed-factor discrepancy, input
    restriction and finite greedy counterexample are separate, explicitly bounded
    observations. No repository defect was identified. DRAFT remains.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- This cohort step adds one DRAFT record, reaching 673 native and 442 unchanged AIO
  records. The main frontier now has 858 entries, including 473 pending and 58 partly
  addressed cohorts; nested leads remain.
- All six pages, all37 references and complete abstract read from column-order-preserving
  extraction. All method equations1–10, pseudocode, all three figures and TableI visually
  inspected. Pages1 and6 text read; not separately visually reread. Complete author
  HTML snapshot and all catalog entries also read.
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
