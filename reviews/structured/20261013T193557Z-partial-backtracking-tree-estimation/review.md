# Scientific author self-review of Tree-size estimation by partial backtracking

- Review: 20261013T193557Z-partial-backtracking-tree-estimation
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T19:22:31Z
- Finished UTC: 2026-10-13T19:35:57Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain partial-backtracking tree estimation as a DRAFT native algorithm with a bounded AIO no-match assessment. Basic and modified variants have explicit counting and source-version qualifications. All maintained fields assessed in author self-review.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:PartialBacktrackingTreeEstimation
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base eea7a76cf5e7d42dbe10fc709ec0e8f0da44e76b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:PartialBacktrackingTreeEstimation | data/curated/PartialBacktrackingTreeEstimation.yaml | maintained | Tree-size estimation by partial backtracking |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:PartialBacktrackingTreeEstimation | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 246.28s (0:04:06)<br>Checked 442 record(s); 0 failed.<br>Checked 646 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 325 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 318,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:PartialBacktrackingTreeEstimation | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:PartialBacktrackingTreeEstimation | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:PartialBacktrackingTreeEstimation | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:PartialBacktrackingTreeEstimation | {"basic_sampling": {"1": {"mean": "9", "variance": "27", "work": "9/4", "work_times_variance": "243/4"}, "2": {"mean": "9", "variance": "9", "work": "9/2", "work_times_variance": "81/2"}, "4": {"mean": "9", "variance": "0", "work": "9", "work_times_variance": "0"}}, "modified_mean": "9", "modified_variance": "1", "modified_work": "13/2", "full_candidate_tests": 9, "feasible_nodes_excluding_root": 7, "feasible_nodes_including_root": 8, "wrong_weight_mean": "18", "omitted_test_cost_mean": "7", "uniform_two_of_four_probability": "1/6", "full_traversal_conditional_sampling_variance": "0", "across_tree_variance": "1", "printed_variance": "5", "literal_work_probability_mass": "1/2", "separated_probability_mass": "1", "balanced_p": "1", "scope": "Fixed finite constructed trees and the stated height-two random family. Work counts candidate tests, not wall-clock time. No universal schedule optimality, author-code behavior or benchmark replication asserted."} |

## Scientific And Domain Assessments

### Tree-size estimation by partial backtracking

identity: supported. Targets: AIMech:PartialBacktrackingTreeEstimation.

Retain this distinct DRAFT algorithm.

Retain basic and modified partial-backtracking variants together with explicit test-order differences. Single-path Knuth sampling, Chen representative merging, model-based CDP, IDA*IM control and beam pruning remain separate mechanisms.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:PartialBacktrackingTreeEstimation.

The declared AIO mapping is supported.

Thirteen full AIO contexts and five full native neighbors support a bounded no-match assessment. Generic stochastic-network, learning-task, classification-tree and bias classes do not identify this subset-weighted search-cost estimator.

### basic-subset-weighting

evidence: supported. Targets: AIMech:PartialBacktrackingTreeEstimation.

Supported within the stated primary-source and mathematical scope.

Sequential r/x decisions give each two-of-four subset probability1/6. Proper a/m weighting preserves a target cost9; forgetting division by m changes it to18.

### modified-pretesting

evidence: supported. Targets: AIMech:PartialBacktrackingTreeEstimation.

Supported within the stated primary-source and mathematical scope.

All root candidate tests use the parent weight before uniform feasible-child sampling. The constructed modified estimator has mean9, variance1 and expected6.5 tests; basic sampling has different work and variance.

### count-target-and-scope

evidence: supported. Targets: AIMech:PartialBacktrackingTreeEstimation.

Supported within the stated primary-source and mathematical scope.

The same finite construction has9candidate tests,7feasible nonroot nodes and8feasible nodes including root. Dropping failed-test costs changes the target. Sampled partial traversal cannot certify absence of unvisited solutions.

### efficiency-and-variance-scope

evidence: supported. Targets: AIMech:PartialBacktrackingTreeEstimation.

Supported within the stated primary-source and mathematical scope.

Full traversal has zero conditional sampling variance, but the height-two random family retains true-size variance1. The source’s expected work-times-variance analysis and historical schedules are not a universal practical optimum.

### printed-analysis-and-version

evidence: supported. Targets: AIMech:PartialBacktrackingTreeEstimation.

Supported within the stated primary-source and mathematical scope.

Direct visual reading confirms February1977 cover and the problematic variance/work-distribution formulas. At b=.5 true height-two variance1 differs from literal5; p1 literal work-distribution mass.5 differs from1. The balance equation yields p=2-2b. No author-code or later-journal defect is inferred.

### subset inclusion weighting, candidate-test cost accounting, conditional variance and printed recurrence limits

consistency: supported. Targets: AIMech:PartialBacktrackingTreeEstimation.

Constructed calculations support the stated distinctions.

Exact finite enumeration checks uniform subsets, a/m weighting, pretest-versus-posttest accounting, work/variance tradeoffs and root conventions. A separate height-two random-tree example challenges literal printed recurrences and distinguishes conditional sampling variance from across-tree variability. No author code or benchmark replication.

### All maintained fields

provenance: supported. Targets: AIMech:PartialBacktrackingTreeEstimation.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 5 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Assessed all maintained fields, February1977 cover versus repository1978 metadata, primary hashes, basic/modified test order, a/m weights, root and failed-test conventions, random-family conditional variance, historical evaluation limits and literal printed-formula inconsistencies.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T192229Z-partial-backtracking-tree-estimation.json | supports | Compared all 442 pinned AIO and 643 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 20, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered 66 AIO and 347 native definitions, with every matched definition read. 13 full annotated AIO node/edge/generated contexts and 5 full native records were inspected. Retain the basic and modified partial-backtracking estimators as one algorithm identity with distinct candidate-testing order. Sampling several successors without replacement extends single-path tree probing without Chen-style stratum merging. Conditional-model extrapolation, search-threshold control and score-based beam pruning have different mechanisms. |
| mapping | sources/aio/aio.json | supports | Thirteen full AIO contexts and five full native neighbors support a bounded no-match assessment. Generic stochastic-network, learning-task, classification-tree and bias classes do not identify this subset-weighted search-cost estimator. |
| purdom1977tr60 | https://scholarworks.iu.edu/dspace/bitstreams/b3d3d0c0-d1d5-4ffb-952f-fac4efd0b012/download; All23 pages of the institutional February1977 TR60 scan visually inspected, including full methods, unnumbered recurrences, both tables, all four figures and all four references. Later journal full text, author code and benchmark replication excluded. | supports | Indiana University Technical Report No. 60, February 1977 as printed on the cover. Institutional 23-page scan, all pages visually inspected: Sections 1–4, Basic B1–B6 and Modified M1–M5 algorithms, unnumbered recurrences, Tables 1–2, Figures 1–4 and four references. Repository metadata lists 1978-11; the later November 1978 journal full text was not inspected or assumed equivalent. |
| calculation | research/discovery/partial-backtracking-boundaries.py | supports | Exact finite enumeration checks uniform subsets, a/m weighting, pretest-versus-posttest accounting, work/variance tradeoffs and root conventions. A separate height-two random-tree example challenges literal printed recurrences and distinguishes conditional sampling variance from across-tree variability. No author code or benchmark replication. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- One new DRAFT concept, yielding 644 native and 442 unchanged generated records. The 829-entry main frontier retains 474 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All 23 scanned technical-report pages visually inspected: cover and abstract, Sections 1–4, Basic B1–B6 and Modified M1–M5 algorithms, all unnumbered recurrences, Tables 1–2, Figures 1–4 and all four references. The later journal full text and author code were not inspected.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T193557Z-partial-backtracking-tree-estimation
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Tree-size estimation by partial backtracking
started_at: '2026-10-13T19:22:31Z'
finished_at: '2026-10-13T19:35:57Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged subset inclusion weighting, candidate-test
    cost accounting, conditional variance and printed recurrence limits. This is adversarial
    author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain partial-backtracking tree estimation as a DRAFT native algorithm with
  a bounded AIO no-match assessment. Basic and modified variants have explicit counting
  and source-version qualifications. All maintained fields assessed in author self-review.
source:
  git_revision: eea7a76cf5e7d42dbe10fc709ec0e8f0da44e76b
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/ComputationalBias.yaml
    sha256: 5a8e7fa4ce6862f3ed08a7389f4f6d746eb90c3d5ee9e54d586f9584ccce4697
    role: context
  - path: data/aio/DecisionTree.yaml
    sha256: 4c2a5ed08c585f8912d66e3629aaa20e93c46ab49cfb2d128001fcd019c81bfc
    role: context
  - path: data/aio/GraphLanguageModel.yaml
    sha256: 1cdda6f7d19946e0672835185e179e2336832225c180e2b70d7860b0c96fc2a8
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
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/ReasoningLLM.yaml
    sha256: 5ceb143da4d5ac2c3bdc430596e21d48943caaa848ae20abf92c791d69a90bfd
    role: context
  - path: data/aio/RecursiveLanguageModel.yaml
    sha256: 617d0f86964cea89a7259598acad60a111f6044fb10db598f060d42aaaecff02
    role: context
  - path: data/aio/RegressionAnalysis.yaml
    sha256: 6f5d48096556a2ec31770aab306219e9020919940b4e80554639cc97aaa94bc6
    role: context
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
    role: context
  - path: data/aio/SelectionAndSamplingBias.yaml
    sha256: 72d8ef34949942ddee1fe60d645806a2117b95207f681de923297b64f78cc477
    role: context
  - path: data/curated/AbsoluteThresholdBeamPruning.yaml
    sha256: 3b04701cf946e151944243eaf7f256880d2e005049e98b64584d9916370eebe1
    role: context
  - path: data/curated/ConditionalDistributionPredictionIDAStar.yaml
    sha256: 316d4e103eb9ebc513fd94573e8d0ee3c287cc569affd4249d5815db50f6793f
    role: context
  - path: data/curated/HeuristicTreeSampling.yaml
    sha256: a011848779d73ba8f15c0f5d1a12a911a0b3db30c0a9c378d1f2e74c3b9f9e76
    role: context
  - path: data/curated/IDAStarIncrementalModel.yaml
    sha256: 0c3ea32d9b744d1324b6c58ef06d60e5a71a0d327d8c9a880ee89490dbd02a7e
    role: context
  - path: data/curated/KnuthBacktrackTreeEstimation.yaml
    sha256: 7230cf708f8e51b2094a37d7e4bc14c29ac63b8b1421ed41d529b08146564cc6
    role: context
  - path: data/curated/PartialBacktrackingTreeEstimation.yaml
    sha256: d0d3dad85452dc350232222badac36799129515921960b8dec8f76bf7faee601
    role: target
  - path: research/discovery/20261013T192229Z-partial-backtracking-tree-estimation.json
    sha256: 69c8200cc8df6eff40da26eb159c447ef6979f1d03d8080be95477bea1d4c9ba
    role: context
  - path: research/discovery/partial-backtracking-boundaries.py
    sha256: 19a6eac239db4b06847f2b021163aec927b999715b8a100abc2656539fe3f181
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
- target_id: AIMech:PartialBacktrackingTreeEstimation
  path: data/curated/PartialBacktrackingTreeEstimation.yaml
  label: Tree-size estimation by partial backtracking
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PartialBacktrackingTreeEstimation.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:PartialBacktrackingTreeEstimation'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:PartialBacktrackingTreeEstimation
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: All23 pages of the institutional February1977 TR60 scan visually inspected,
      including full methods, unnumbered recurrences, both tables, all four figures
      and all four references. Later journal full text, author code and benchmark
      replication excluded.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:PartialBacktrackingTreeEstimation
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 246.28s (0:04:06)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 646 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 325 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 318,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:PartialBacktrackingTreeEstimation
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
  - AIMech:PartialBacktrackingTreeEstimation
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
  - AIMech:PartialBacktrackingTreeEstimation
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/partial-backtracking-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:PartialBacktrackingTreeEstimation
  exit_code: 0
  expected_exit_code: 0
  summary: '{"basic_sampling": {"1": {"mean": "9", "variance": "27", "work": "9/4",
    "work_times_variance": "243/4"}, "2": {"mean": "9", "variance": "9", "work": "9/2",
    "work_times_variance": "81/2"}, "4": {"mean": "9", "variance": "0", "work": "9",
    "work_times_variance": "0"}}, "modified_mean": "9", "modified_variance": "1",
    "modified_work": "13/2", "full_candidate_tests": 9, "feasible_nodes_excluding_root":
    7, "feasible_nodes_including_root": 8, "wrong_weight_mean": "18", "omitted_test_cost_mean":
    "7", "uniform_two_of_four_probability": "1/6", "full_traversal_conditional_sampling_variance":
    "0", "across_tree_variance": "1", "printed_variance": "5", "literal_work_probability_mass":
    "1/2", "separated_probability_mass": "1", "balanced_p": "1", "scope": "Fixed finite
    constructed trees and the stated height-two random family. Work counts candidate
    tests, not wall-clock time. No universal schedule optimality, author-code behavior
    or benchmark replication asserted."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T192229Z-partial-backtracking-tree-estimation.json
  accessed_at: '2026-10-13T19:22:31Z'
  support: supports
  summary: Compared all 442 pinned AIO and 643 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    20, 0, 0 lines. All distinct match contents were inspected. Semantic matching
    covered 66 AIO and 347 native definitions, with every matched definition read.
    13 full annotated AIO node/edge/generated contexts and 5 full native records were
    inspected. Retain the basic and modified partial-backtracking estimators as one
    algorithm identity with distinct candidate-testing order. Sampling several successors
    without replacement extends single-path tree probing without Chen-style stratum
    merging. Conditional-model extrapolation, search-threshold control and score-based
    beam pruning have different mechanisms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T19:22:31Z'
  support: supports
  summary: Thirteen full AIO contexts and five full native neighbors support a bounded
    no-match assessment. Generic stochastic-network, learning-task, classification-tree
    and bias classes do not identify this subset-weighted search-cost estimator.
- evidence_id: purdom1977tr60
  kind: primary_source
  reference: https://scholarworks.iu.edu/dspace/bitstreams/b3d3d0c0-d1d5-4ffb-952f-fac4efd0b012/download
  locator: All23 pages of the institutional February1977 TR60 scan visually inspected,
    including full methods, unnumbered recurrences, both tables, all four figures
    and all four references. Later journal full text, author code and benchmark replication
    excluded.
  accessed_at: '2026-10-13T17:56:41Z'
  snapshot_sha256: 9e6ad24e9ec6d9bfd2b9232008f1dd0bd00581cb1359274b74d0639949f3e437
  support: supports
  summary: 'Indiana University Technical Report No. 60, February 1977 as printed on
    the cover. Institutional 23-page scan, all pages visually inspected: Sections
    1–4, Basic B1–B6 and Modified M1–M5 algorithms, unnumbered recurrences, Tables
    1–2, Figures 1–4 and four references. Repository metadata lists 1978-11; the later
    November 1978 journal full text was not inspected or assumed equivalent.'
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/partial-backtracking-boundaries.py
  accessed_at: '2026-10-13T19:26:06Z'
  snapshot_sha256: 19a6eac239db4b06847f2b021163aec927b999715b8a100abc2656539fe3f181
  support: supports
  summary: Exact finite enumeration checks uniform subsets, a/m weighting, pretest-versus-posttest
    accounting, work/variance tradeoffs and root conventions. A separate height-two
    random-tree example challenges literal printed recurrences and distinguishes conditional
    sampling variance from across-tree variability. No author code or benchmark replication.
assessments:
- assessment_id: identity
  area: identity
  topic: Tree-size estimation by partial backtracking
  outcome: supported
  target_ids:
  - AIMech:PartialBacktrackingTreeEstimation
  evidence_ids:
  - identity
  - purdom1977tr60
  summary: Retain this distinct DRAFT algorithm.
  details: Retain basic and modified partial-backtracking variants together with explicit
    test-order differences. Single-path Knuth sampling, Chen representative merging,
    model-based CDP, IDA*IM control and beam pruning remain separate mechanisms.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:PartialBacktrackingTreeEstimation
  evidence_ids:
  - mapping
  - purdom1977tr60
  summary: The declared AIO mapping is supported.
  details: Thirteen full AIO contexts and five full native neighbors support a bounded
    no-match assessment. Generic stochastic-network, learning-task, classification-tree
    and bias classes do not identify this subset-weighted search-cost estimator.
- assessment_id: basic-subset-weighting
  area: evidence
  topic: basic-subset-weighting
  outcome: supported
  target_ids:
  - AIMech:PartialBacktrackingTreeEstimation
  evidence_ids:
  - purdom1977tr60
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Sequential r/x decisions give each two-of-four subset probability1/6. Proper
    a/m weighting preserves a target cost9; forgetting division by m changes it to18.
- assessment_id: modified-pretesting
  area: evidence
  topic: modified-pretesting
  outcome: supported
  target_ids:
  - AIMech:PartialBacktrackingTreeEstimation
  evidence_ids:
  - purdom1977tr60
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: All root candidate tests use the parent weight before uniform feasible-child
    sampling. The constructed modified estimator has mean9, variance1 and expected6.5
    tests; basic sampling has different work and variance.
- assessment_id: count-target-and-scope
  area: evidence
  topic: count-target-and-scope
  outcome: supported
  target_ids:
  - AIMech:PartialBacktrackingTreeEstimation
  evidence_ids:
  - purdom1977tr60
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The same finite construction has9candidate tests,7feasible nonroot nodes
    and8feasible nodes including root. Dropping failed-test costs changes the target.
    Sampled partial traversal cannot certify absence of unvisited solutions.
- assessment_id: efficiency-and-variance-scope
  area: evidence
  topic: efficiency-and-variance-scope
  outcome: supported
  target_ids:
  - AIMech:PartialBacktrackingTreeEstimation
  evidence_ids:
  - purdom1977tr60
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Full traversal has zero conditional sampling variance, but the height-two
    random family retains true-size variance1. The source’s expected work-times-variance
    analysis and historical schedules are not a universal practical optimum.
- assessment_id: printed-analysis-and-version
  area: evidence
  topic: printed-analysis-and-version
  outcome: supported
  target_ids:
  - AIMech:PartialBacktrackingTreeEstimation
  evidence_ids:
  - purdom1977tr60
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Direct visual reading confirms February1977 cover and the problematic variance/work-distribution
    formulas. At b=.5 true height-two variance1 differs from literal5; p1 literal
    work-distribution mass.5 differs from1. The balance equation yields p=2-2b. No
    author-code or later-journal defect is inferred.
- assessment_id: constructed-boundaries
  area: consistency
  topic: subset inclusion weighting, candidate-test cost accounting, conditional variance
    and printed recurrence limits
  outcome: supported
  target_ids:
  - AIMech:PartialBacktrackingTreeEstimation
  evidence_ids:
  - purdom1977tr60
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Exact finite enumeration checks uniform subsets, a/m weighting, pretest-versus-posttest
    accounting, work/variance tradeoffs and root conventions. A separate height-two
    random-tree example challenges literal printed recurrences and distinguishes conditional
    sampling variance from across-tree variability. No author code or benchmark replication.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:PartialBacktrackingTreeEstimation
  evidence_ids:
  - identity
  - mapping
  - purdom1977tr60
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 5 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. Assessed all maintained fields, February1977 cover
    versus repository1978 metadata, primary hashes, basic/modified test order, a/m
    weights, root and failed-test conventions, random-family conditional variance,
    historical evaluation limits and literal printed-formula inconsistencies.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- One new DRAFT concept, yielding 644 native and 442 unchanged generated records.
  The 829-entry main frontier retains 474 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- 'All 23 scanned technical-report pages visually inspected: cover and abstract, Sections
  1–4, Basic B1–B6 and Modified M1–M5 algorithms, all unnumbered recurrences, Tables
  1–2, Figures 1–4 and all four references. The later journal full text and author
  code were not inspected.'
- No author code, training, paid service, hardware measurement or empirical replication.
  Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization
  and old round141 cleanup remain pending explicit approval after automatic review
  rejection.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
