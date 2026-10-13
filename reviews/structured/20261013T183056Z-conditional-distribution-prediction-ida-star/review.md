# Scientific author self-review of Conditional Distribution Prediction for IDA*

- Review: 20261013T183056Z-conditional-distribution-prediction-ida-star
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T18:21:24Z
- Finished UTC: 2026-10-13T18:30:56Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Conditional Distribution Prediction for IDA* as a DRAFT algorithm with a qualified related MarkovChain mapping. Recursive count estimation is supported within explicit context, pruning and sampling limits. All maintained fields assessed in author self-review; no independent approval.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:ConditionalDistributionPredictionIDAStar
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 75f886473002e00f04ce340ac0b9b8c4c57b1430.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ConditionalDistributionPredictionIDAStar | data/curated/ConditionalDistributionPredictionIDAStar.yaml | maintained | Conditional Distribution Prediction for IDA* |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:ConditionalDistributionPredictionIDAStar | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 183.05s (0:03:03)<br>Checked 442 record(s); 0 failed.<br>Checked 639 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 317 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 314,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:ConditionalDistributionPredictionIDAStar | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:ConditionalDistributionPredictionIDAStar | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:ConditionalDistributionPredictionIDAStar | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:ConditionalDistributionPredictionIDAStar | {"ancestor_pruning": {"actually_expanded": 1, "potential_nodes": 2}, "correlated_bpmx_sibling_survival": {"expected_generated": 2.0, "power_approximation": 0.25, "power_based_expected_generated": 1.75, "third_child_joint_survival": 0.5}, "heterogeneous_start_context": {"actual_counts": [1, 2], "pooled_prediction": 1.5}, "homogeneous_context": {"early_stop_expansions_with_goal_test_before_expansion": 1, "early_stop_nodes_visited": 2, "expanded_by_depth": [1.0, 2.0, 4.0], "total": 7}, "independence_is_not_a_universal_lower_bound": {"anticorrelated_count": 1.0, "independent_prediction": 1.5}, "interpretation": "Exactness requires matched context and counting conventions; sampled or independence-based predictions are not certified bounds.", "variable_branching_weighting": {"actual_mean_low_children": 0.5, "mean_branching": 2.0, "mean_parent_fraction": 0.5, "pooled_child_fraction": 0.25}} |

## Scientific And Domain Assessments

### Conditional Distribution Prediction for IDA*

identity: supported. Targets: AIMech:ConditionalDistributionPredictionIDAStar.

Retain this distinct DRAFT algorithm.

Retain the conditional count estimator, distinct from solution-returning IDA*, IDA*IM online threshold control and latent-state tree probability models. CDP1 and richer conditioning variants do not need duplicate records; the ambiguous bare acronym is not an alias.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:ConditionalDistributionPredictionIDAStar.

The declared AIO mapping is supported.

MarkovChain is a related mapping for the conditional transition-law component, explicitly a curator inference. The complete method propagates non-normalized expected counts with branching and threshold pruning. Nine complete annotated AIO contexts and four full native neighbors were inspected; no equivalence, subclass or real-state Markov guarantee is asserted.

### complete-contour-counting

evidence: supported. Targets: AIMech:ConditionalDistributionPredictionIDAStar.

Supported within the stated primary-source and mathematical scope.

The target is a complete fixed-threshold IDA* expansion count, with unit-cost depth and nonnegative discrete h. A low-f descendant can remain unreachable after an inconsistent parent is pruned. Early goal termination changes the counting target.

### conditional-count-recurrence

evidence: supported. Targets: AIMech:ConditionalDistributionPredictionIDAStar.

Supported within the stated primary-source and mathematical scope.

Normalized conditional frequencies are multiplied by matched conditional offspring counts. The resulting mass is expected nodes, not a normalized path distribution. Root or frontier initialization, pruning and population weighting matter; averaging parent fractions and pooling children differ for unequal degrees.

### context-and-exactness-boundary

evidence: supported. Targets: AIMech:ConditionalDistributionPredictionIDAStar.

Supported within the stated primary-source and mathematical scope.

The source gives homogeneous-context sufficient conditions and explicit failure cases. Exact pooled tables do not imply exact individual-start counts; finite sampling can make a richer context worse. The record retains both ideal conditions and approximation limits.

### shallow-search-and-bpmx

evidence: supported. Targets: AIMech:ConditionalDistributionPredictionIDAStar.

Supported within the stated primary-source and mathematical scope.

Explicit shallow search supplies additional start-specific context at a cost. The inspected BPMX extension uses one-level upward propagation and a sibling-order survival model. Equal marginal survival probabilities do not determine joint survival for dependent siblings.

### evaluation-and-boundary-estimates

evidence: supported. Targets: AIMech:ConditionalDistributionPredictionIDAStar.

Supported within the stated primary-source and mathematical scope.

Finite studies do not establish uniform superiority. Exact potential counts bound expansions but approximate sampled estimates need not. Independent-neighbor lower estimates are empirically motivated and can fail with anticorrelation. The record retains additional work needed for variable costs and graph duplicates.

### conditional count propagation, complete-contour scope, context exactness and dependence assumptions

consistency: supported. Targets: AIMech:ConditionalDistributionPredictionIDAStar.

Constructed calculations support the stated distinctions.

Constructed finite examples distinguish complete-contour counts from early stopping, potential nodes from generated descendants, pooled accuracy from individual-start accuracy, and a proposed independence-based lower estimate from a certified bound. Additional examples challenge sibling-survival independence and unequal-degree conditional weighting. No author code or benchmark executed.

### All maintained fields

provenance: supported. Targets: AIMech:ConditionalDistributionPredictionIDAStar.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 5 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Assessed all maintained fields and locators. Challenged complete-contour versus early-stop counts, ancestor pruning, offspring-count versus probability normalization, unequal-degree weighting, context exactness, start heterogeneity, shallow-search costs, BPMX sibling dependence and uncertified empirical bounds.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T182122Z-conditional-distribution-prediction-ida-star.json | supports | Compared all 442 pinned AIO and 638 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 4, 0, 1 lines. All distinct match contents were inspected. Semantic matching covered 63 AIO and 302 native definitions, with every matched definition read. 9 full annotated AIO node/edge/generated contexts and 4 full native records were inspected. Retain the recursive expanded-node estimator for a complete IDA* threshold iteration. It is distinct from the solution-returning IDA* search, IDA*IM online threshold-control integration, and latent-state tree models with observation emissions. The generic acronym CDP is not adopted as a global alias. |
| mapping | sources/aio/aio.json | supports | MarkovChain is a related mapping for the conditional transition-law component, explicitly a curator inference. The complete method propagates non-normalized expected counts with branching and threshold pruning. Nine complete annotated AIO contexts and four full native neighbors were inspected; no equivalence, subclass or real-state Markov guarantee is asserted. |
| zahavi2010cdp | https://tzin.bgu.ac.il/~felner/2010/JAIR_Pred.pdf; All 43 pages of the author-hosted JAIR 2010 PDF visually inspected, including Sections 1–13, Equations 1–20, Figures 1–9, Tables 1–17, footnotes and references. Alternate PDF versions, 2008 conference full text, author code and benchmark replication excluded. | supports | Author-hosted JAIR 37 (2010), pages 41–83, 43-page PDF. All pages visually inspected, including Sections 1–13, Equations 1–20, Figures 1–9, Tables 1–17, footnotes and complete references. ArXiv abstract deposited in 2014 and primary institutional metadata also inspected; alternate PDFs and author implementation excluded. |
| calculation | research/discovery/cdp-ida-star-boundaries.py | supports | Constructed finite examples distinguish complete-contour counts from early stopping, potential nodes from generated descendants, pooled accuracy from individual-start accuracy, and a proposed independence-based lower estimate from a certified bound. Additional examples challenge sibling-survival independence and unequal-degree conditional weighting. No author code or benchmark executed. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- One new DRAFT concept, yielding 639 native and 442 unchanged generated records. The 824-entry main frontier retains 474 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All43 primary author-hosted PDF pages visually inspected, printed41–83: Sections1–13, Equations1–20, Figures1–9, Tables1–17, footnotes and complete references. Other versions, author code and empirical replication excluded.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T183056Z-conditional-distribution-prediction-ida-star
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Conditional Distribution Prediction for IDA*
started_at: '2026-10-13T18:21:24Z'
finished_at: '2026-10-13T18:30:56Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged conditional count propagation, complete-contour
    scope, context exactness and dependence assumptions. This is adversarial author
    self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Conditional Distribution Prediction for IDA* as a DRAFT algorithm
  with a qualified related MarkovChain mapping. Recursive count estimation is supported
  within explicit context, pruning and sampling limits. All maintained fields assessed
  in author self-review; no independent approval.
source:
  git_revision: 75f886473002e00f04ce340ac0b9b8c4c57b1430
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
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
  - path: data/aio/NeuroSymbolicLLM.yaml
    sha256: d82fe65db45394cc57d77160a5a2176b1244d54000acff6f9362809c8c8524fb
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/ReasoningLLM.yaml
    sha256: 5ceb143da4d5ac2c3bdc430596e21d48943caaa848ae20abf92c791d69a90bfd
    role: context
  - path: data/aio/RegressionAnalysis.yaml
    sha256: 6f5d48096556a2ec31770aab306219e9020919940b4e80554639cc97aaa94bc6
    role: context
  - path: data/curated/ConditionalDistributionPredictionIDAStar.yaml
    sha256: 316d4e103eb9ebc513fd94573e8d0ee3c287cc569affd4249d5815db50f6793f
    role: target
  - path: data/curated/HiddenMarkovTree.yaml
    sha256: ca89c267443e8b806d61b389943bd06a514fb8a95668bd604fae4ecc2d873e1b
    role: context
  - path: data/curated/IDAStarIncrementalModel.yaml
    sha256: 0c3ea32d9b744d1324b6c58ef06d60e5a71a0d327d8c9a880ee89490dbd02a7e
    role: context
  - path: data/curated/IterativeDeepeningAStar.yaml
    sha256: 0a9b9b571f3e7179658db63ce60f2e4febac10c4470212b5b0270b86b9eeac6c
    role: context
  - path: data/curated/PairwiseMarkovTree.yaml
    sha256: f7dbda0ba922be5032e7e4f310c6dbcf0e8260c534039c8d58f67e50da1acf93
    role: context
  - path: research/discovery/20261013T182122Z-conditional-distribution-prediction-ida-star.json
    sha256: 2dd711cbe503e35ab36eacc8c55e764985dd5d19801b626b9c8ede977c34aaec
    role: context
  - path: research/discovery/cdp-ida-star-boundaries.py
    sha256: 6a23bfb4436102c728405d26b60165051ac7ec5d2172f68e16b91ddefe2e14e8
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
- target_id: AIMech:ConditionalDistributionPredictionIDAStar
  path: data/curated/ConditionalDistributionPredictionIDAStar.yaml
  label: Conditional Distribution Prediction for IDA*
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ConditionalDistributionPredictionIDAStar.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:ConditionalDistributionPredictionIDAStar'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:ConditionalDistributionPredictionIDAStar
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: All 43 pages of the author-hosted JAIR 2010 PDF visually inspected, including
      Sections 1–13, Equations 1–20, Figures 1–9, Tables 1–17, footnotes and references.
      Alternate PDF versions, 2008 conference full text, author code and benchmark
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
  - AIMech:ConditionalDistributionPredictionIDAStar
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 183.05s (0:03:03)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 639 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 317 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 314,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:ConditionalDistributionPredictionIDAStar
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
  - AIMech:ConditionalDistributionPredictionIDAStar
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
  - AIMech:ConditionalDistributionPredictionIDAStar
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/cdp-ida-star-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:ConditionalDistributionPredictionIDAStar
  exit_code: 0
  expected_exit_code: 0
  summary: '{"ancestor_pruning": {"actually_expanded": 1, "potential_nodes": 2}, "correlated_bpmx_sibling_survival":
    {"expected_generated": 2.0, "power_approximation": 0.25, "power_based_expected_generated":
    1.75, "third_child_joint_survival": 0.5}, "heterogeneous_start_context": {"actual_counts":
    [1, 2], "pooled_prediction": 1.5}, "homogeneous_context": {"early_stop_expansions_with_goal_test_before_expansion":
    1, "early_stop_nodes_visited": 2, "expanded_by_depth": [1.0, 2.0, 4.0], "total":
    7}, "independence_is_not_a_universal_lower_bound": {"anticorrelated_count": 1.0,
    "independent_prediction": 1.5}, "interpretation": "Exactness requires matched
    context and counting conventions; sampled or independence-based predictions are
    not certified bounds.", "variable_branching_weighting": {"actual_mean_low_children":
    0.5, "mean_branching": 2.0, "mean_parent_fraction": 0.5, "pooled_child_fraction":
    0.25}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T182122Z-conditional-distribution-prediction-ida-star.json
  accessed_at: '2026-10-13T18:21:24Z'
  support: supports
  summary: Compared all 442 pinned AIO and 638 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    4, 0, 1 lines. All distinct match contents were inspected. Semantic matching covered
    63 AIO and 302 native definitions, with every matched definition read. 9 full
    annotated AIO node/edge/generated contexts and 4 full native records were inspected.
    Retain the recursive expanded-node estimator for a complete IDA* threshold iteration.
    It is distinct from the solution-returning IDA* search, IDA*IM online threshold-control
    integration, and latent-state tree models with observation emissions. The generic
    acronym CDP is not adopted as a global alias.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T18:21:24Z'
  support: supports
  summary: MarkovChain is a related mapping for the conditional transition-law component,
    explicitly a curator inference. The complete method propagates non-normalized
    expected counts with branching and threshold pruning. Nine complete annotated
    AIO contexts and four full native neighbors were inspected; no equivalence, subclass
    or real-state Markov guarantee is asserted.
- evidence_id: zahavi2010cdp
  kind: primary_source
  reference: https://tzin.bgu.ac.il/~felner/2010/JAIR_Pred.pdf
  locator: All 43 pages of the author-hosted JAIR 2010 PDF visually inspected, including
    Sections 1–13, Equations 1–20, Figures 1–9, Tables 1–17, footnotes and references.
    Alternate PDF versions, 2008 conference full text, author code and benchmark replication
    excluded.
  accessed_at: '2026-10-13T17:05:16Z'
  snapshot_sha256: d66f9db3b41c22e08295a638ffa05f12d90a0305242e293653d5675f391dfa67
  support: supports
  summary: Author-hosted JAIR 37 (2010), pages 41–83, 43-page PDF. All pages visually
    inspected, including Sections 1–13, Equations 1–20, Figures 1–9, Tables 1–17,
    footnotes and complete references. ArXiv abstract deposited in 2014 and primary
    institutional metadata also inspected; alternate PDFs and author implementation
    excluded.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/cdp-ida-star-boundaries.py
  accessed_at: '2026-10-13T18:25:12Z'
  snapshot_sha256: 6a23bfb4436102c728405d26b60165051ac7ec5d2172f68e16b91ddefe2e14e8
  support: supports
  summary: Constructed finite examples distinguish complete-contour counts from early
    stopping, potential nodes from generated descendants, pooled accuracy from individual-start
    accuracy, and a proposed independence-based lower estimate from a certified bound.
    Additional examples challenge sibling-survival independence and unequal-degree
    conditional weighting. No author code or benchmark executed.
assessments:
- assessment_id: identity
  area: identity
  topic: Conditional Distribution Prediction for IDA*
  outcome: supported
  target_ids:
  - AIMech:ConditionalDistributionPredictionIDAStar
  evidence_ids:
  - identity
  - zahavi2010cdp
  summary: Retain this distinct DRAFT algorithm.
  details: Retain the conditional count estimator, distinct from solution-returning
    IDA*, IDA*IM online threshold control and latent-state tree probability models.
    CDP1 and richer conditioning variants do not need duplicate records; the ambiguous
    bare acronym is not an alias.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:ConditionalDistributionPredictionIDAStar
  evidence_ids:
  - mapping
  - zahavi2010cdp
  summary: The declared AIO mapping is supported.
  details: MarkovChain is a related mapping for the conditional transition-law component,
    explicitly a curator inference. The complete method propagates non-normalized
    expected counts with branching and threshold pruning. Nine complete annotated
    AIO contexts and four full native neighbors were inspected; no equivalence, subclass
    or real-state Markov guarantee is asserted.
- assessment_id: complete-contour-counting
  area: evidence
  topic: complete-contour-counting
  outcome: supported
  target_ids:
  - AIMech:ConditionalDistributionPredictionIDAStar
  evidence_ids:
  - zahavi2010cdp
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The target is a complete fixed-threshold IDA* expansion count, with unit-cost
    depth and nonnegative discrete h. A low-f descendant can remain unreachable after
    an inconsistent parent is pruned. Early goal termination changes the counting
    target.
- assessment_id: conditional-count-recurrence
  area: evidence
  topic: conditional-count-recurrence
  outcome: supported
  target_ids:
  - AIMech:ConditionalDistributionPredictionIDAStar
  evidence_ids:
  - zahavi2010cdp
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Normalized conditional frequencies are multiplied by matched conditional
    offspring counts. The resulting mass is expected nodes, not a normalized path
    distribution. Root or frontier initialization, pruning and population weighting
    matter; averaging parent fractions and pooling children differ for unequal degrees.
- assessment_id: context-and-exactness-boundary
  area: evidence
  topic: context-and-exactness-boundary
  outcome: supported
  target_ids:
  - AIMech:ConditionalDistributionPredictionIDAStar
  evidence_ids:
  - zahavi2010cdp
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The source gives homogeneous-context sufficient conditions and explicit
    failure cases. Exact pooled tables do not imply exact individual-start counts;
    finite sampling can make a richer context worse. The record retains both ideal
    conditions and approximation limits.
- assessment_id: shallow-search-and-bpmx
  area: evidence
  topic: shallow-search-and-bpmx
  outcome: supported
  target_ids:
  - AIMech:ConditionalDistributionPredictionIDAStar
  evidence_ids:
  - zahavi2010cdp
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Explicit shallow search supplies additional start-specific context at a
    cost. The inspected BPMX extension uses one-level upward propagation and a sibling-order
    survival model. Equal marginal survival probabilities do not determine joint survival
    for dependent siblings.
- assessment_id: evaluation-and-boundary-estimates
  area: evidence
  topic: evaluation-and-boundary-estimates
  outcome: supported
  target_ids:
  - AIMech:ConditionalDistributionPredictionIDAStar
  evidence_ids:
  - zahavi2010cdp
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Finite studies do not establish uniform superiority. Exact potential counts
    bound expansions but approximate sampled estimates need not. Independent-neighbor
    lower estimates are empirically motivated and can fail with anticorrelation. The
    record retains additional work needed for variable costs and graph duplicates.
- assessment_id: constructed-boundaries
  area: consistency
  topic: conditional count propagation, complete-contour scope, context exactness
    and dependence assumptions
  outcome: supported
  target_ids:
  - AIMech:ConditionalDistributionPredictionIDAStar
  evidence_ids:
  - zahavi2010cdp
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Constructed finite examples distinguish complete-contour counts from early
    stopping, potential nodes from generated descendants, pooled accuracy from individual-start
    accuracy, and a proposed independence-based lower estimate from a certified bound.
    Additional examples challenge sibling-survival independence and unequal-degree
    conditional weighting. No author code or benchmark executed.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:ConditionalDistributionPredictionIDAStar
  evidence_ids:
  - identity
  - mapping
  - zahavi2010cdp
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 5 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. Assessed all maintained fields and locators. Challenged
    complete-contour versus early-stop counts, ancestor pruning, offspring-count versus
    probability normalization, unequal-degree weighting, context exactness, start
    heterogeneity, shallow-search costs, BPMX sibling dependence and uncertified empirical
    bounds.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- One new DRAFT concept, yielding 639 native and 442 unchanged generated records.
  The 824-entry main frontier retains 474 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- 'All43 primary author-hosted PDF pages visually inspected, printed41–83: Sections1–13,
  Equations1–20, Figures1–9, Tables1–17, footnotes and complete references. Other
  versions, author code and empirical replication excluded.'
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
