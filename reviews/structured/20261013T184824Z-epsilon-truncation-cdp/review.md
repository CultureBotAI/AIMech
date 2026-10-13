# Scientific author self-review of Epsilon-truncation for Conditional Distribution Prediction

- Review: 20261013T184824Z-epsilon-truncation-cdp
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T18:39:44Z
- Finished UTC: 2026-10-13T18:48:24Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain CDP epsilon-truncation as a DRAFT native algorithm with explicit related AIO mapping and formula/evaluation limitations. All maintained fields assessed; no actionable record defect identified in this author self-review.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:EpsilonTruncationCDP
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 86a5abb61419367bc46d61da783ad1909943791e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:EpsilonTruncationCDP | data/curated/EpsilonTruncationCDP.yaml | maintained | Epsilon-truncation for Conditional Distribution Prediction |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:EpsilonTruncationCDP | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 148.84s (0:02:28)<br>Checked 442 record(s); 0 failed.<br>Checked 640 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 318 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 315,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:EpsilonTruncationCDP | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:EpsilonTruncationCDP | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:EpsilonTruncationCDP | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:EpsilonTruncationCDP | {"strict_cutoff_and_renormalization": ["0", "3/19", "16/19"], "equal_cutoff_retained": true, "empty_row_rejected": true, "guarded_common_cutoff": "3/5", "literal_arrangement_weight_sum": "3/4", "binomial_count_probability_sum": "1", "literal_pair_sum_child_count": "2", "distinct_parent_sum_child_count": "1", "homogeneous_tree_actual_and_original_prediction": 111, "truncated_prediction": "11", "same_type_budget_different_stage_predictions": ["1", "7/5"], "scope": "Constructed mathematical checks, not author-code validation or replication."} |

## Scientific And Domain Assessments

### Epsilon-truncation for Conditional Distribution Prediction

identity: supported. Targets: AIMech:EpsilonTruncationCDP.

Retain this distinct DRAFT algorithm.

Retain the CDP table-modification method as an estimator procedure. Original CDP, lookup caching, online IDA*IM search control, actual beam pruning and sparse topic-model transitions have distinct targets. The generic epsilon-truncation phrase is not a universal alias.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:EpsilonTruncationCDP.

The declared AIO mapping is supported.

MarkovChain is a related component context for normalized type-transition tables, including depth-varying tables. The estimator propagates counts with branching and pruning rather than probability mass. Twelve full AIO contexts and four full native neighbors support the bounded mapping assessment; no exact or subclass relationship is asserted.

### level-specific-table-modification

evidence: supported. Targets: AIMech:EpsilonTruncationCDP.

Supported within the stated primary-source and mathematical scope.

The strict below-cutoff removal retains equality, renormalizes positive survivors and guards against empty rows. This changes the prediction model, not the actual search policy.

### offline-cutoff-calibration

evidence: supported. Targets: AIMech:EpsilonTruncationCDP.

Supported within the stated primary-source and mathematical scope.

The source uses per-level sampled allocation outcomes and a majority-prefix rule with a row-survival guard. It is an offline heuristic approximation, not an asserted universal cutoff or exact true-error minimizer.

### printed-calibration-boundaries

evidence: supported. Targets: AIMech:EpsilonTruncationCDP.

Supported within the stated primary-source and mathematical scope.

The literal count weight lacks a binomial coefficient: forN2,p.5 its weights sum.75 rather than1. The displayed pair-indexed count repeats parent mass when multiple refined children share a coarse group. The record qualifies the printed formulas without claiming knowledge of author software.

### aggregation-and-accuracy-limits

evidence: supported. Targets: AIMech:EpsilonTruncationCDP.

Supported within the stated primary-source and mathematical scope.

An exactly counted homogeneous tree has111nodes, whereas deleting its rare child type gives11. The source itself reports metric-dependent degradation and denies unbiasedness. These facts preclude universal per-start improvement.

### finite-evaluation-and-amortization

evidence: supported. Targets: AIMech:EpsilonTruncationCDP.

Supported within the stated primary-source and mathematical scope.

Error metrics differ, preprocessing is costly and experiment regimes are finite. Same-model lookup preserves predictions only with all relevant depth/schedule context; a constructed same-type/budget case differs across stages. No universal runtime or accuracy guarantee is claimed.

### cutoff normalization, calibration formula interpretation and finite search-count evidence

consistency: supported. Targets: AIMech:EpsilonTruncationCDP.

Constructed calculations support the stated distinctions.

Exact rational constructions test strict cutoff and retained equality, empty-row prevention, missing Bernoulli count multiplicity, repeated parent mass in a literal supertype sum, a case where truncation worsens exact counting, and the state required for caching depth-varying schedules. No author code or empirical replication.

### All maintained fields

provenance: supported. Targets: AIMech:EpsilonTruncationCDP.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 5 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Assessed all maintained fields, source/hash/version, strict cutoff equality, nonempty normalization, calibration scope, literal probability and aggregation formulas, rare-descendant counterexample and finite evidence. No unseen author implementation is certified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T183932Z-epsilon-truncation-cdp.json | supports | Compared all 442 pinned AIO and 639 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 5, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered 66 AIO and 345 native definitions, with every matched definition read. 12 full annotated AIO node/edge/generated contexts and 4 full native records were inspected. Retain the named CDP probability-table modification and calibrated per-level cutoff method. It changes an estimator, not the actual IDA* search tree or solution policy. Original CDP, lookup-based reuse, IDA*IM threshold control, score-margin sequence beam pruning and pruned topic-model Gibbs transitions have distinct targets. Generic epsilon-truncation outside this search-estimation context is not asserted equivalent. |
| mapping | sources/aio/aio.json | supports | MarkovChain is a related component context for normalized type-transition tables, including depth-varying tables. The estimator propagates counts with branching and pruning rather than probability mass. Twelve full AIO contexts and four full native neighbors support the bounded mapping assessment; no exact or subclass relationship is asserted. |
| lelis2013prediction | https://webdocs.cs.ualberta.ca/~santanad/papers/2013/ARTINT2694.pdf; All25 pages of the author-hosted journal PDF inspected, including the cover, Sections1–13, Equations1–6 and unnumbered formulas, Definitions1–5, Algorithm1, Figures1–8, Tables1–17 and all28references. Earlier conference papers, author code and empirical replication excluded. | supports | Author-hosted personal-copy PDF: one cover plus 24 journal pages, Artificial Intelligence 196 (2013), pages 53–76. PDF pages 2–25 correspond to printed pages 53–76. All 25 pages visually inspected: Sections 1–13, Equations 1–6 and unnumbered formulas, Definitions 1–5, Algorithm 1, Figures 1–8, Tables 1–17 and all 28 references. Earlier conference papers and author code were not inspected. |
| calculation | research/discovery/epsilon-truncation-cdp-boundaries.py | supports | Exact rational constructions test strict cutoff and retained equality, empty-row prevention, missing Bernoulli count multiplicity, repeated parent mass in a literal supertype sum, a case where truncation worsens exact counting, and the state required for caching depth-varying schedules. No author code or empirical replication. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- One new DRAFT concept, yielding 640 native and 442 unchanged generated records. The 825-entry main frontier retains 474 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All25 author-hosted pages visually read: cover plus printed53–76; Sections1–13, Equations1–6 and unnumbered equations, Algorithm1, Definitions1–5, Figures1–8, Tables1–17, all28references. Focused rereading of PDFs8–10 and17 checked probability, aggregation and caching boundaries. Other versions and author code excluded.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T184824Z-epsilon-truncation-cdp
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Epsilon-truncation for Conditional Distribution
  Prediction
started_at: '2026-10-13T18:39:44Z'
finished_at: '2026-10-13T18:48:24Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged cutoff normalization, calibration formula
    interpretation and finite search-count evidence. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain CDP epsilon-truncation as a DRAFT native algorithm with explicit related
  AIO mapping and formula/evaluation limitations. All maintained fields assessed;
  no actionable record defect identified in this author self-review.
source:
  git_revision: 86a5abb61419367bc46d61da783ad1909943791e
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/GraphLanguageModel.yaml
    sha256: 1cdda6f7d19946e0672835185e179e2336832225c180e2b70d7860b0c96fc2a8
    role: context
  - path: data/aio/HardSigmoidFunction.yaml
    sha256: d9a78ced04a24c242291fab0c7a37082572fc33b61f8bab3f3ae6bf8e56640c6
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
  - path: data/aio/ThresholdAutoregressive.yaml
    sha256: 0cbb5a268b739a03016d947a17007d7ab1264d3ed78a90c36efeced32d4d4b19
    role: context
  - path: data/aio/ThresholdedReLULayer.yaml
    sha256: 3d36b3705b493dd73e1740fe620159932c0dc6defa38a6bf137ee2e24600c6f0
    role: context
  - path: data/curated/AbsoluteThresholdBeamPruning.yaml
    sha256: 3b04701cf946e151944243eaf7f256880d2e005049e98b64584d9916370eebe1
    role: context
  - path: data/curated/ConditionalDistributionPredictionIDAStar.yaml
    sha256: 316d4e103eb9ebc513fd94573e8d0ee3c287cc569affd4249d5815db50f6793f
    role: context
  - path: data/curated/EpsilonTruncationCDP.yaml
    sha256: fca33999517a17fae9dbb7a755302a8450fc8dd8aaa0d1fb8d2c4ff27fecbf03
    role: target
  - path: data/curated/IDAStarIncrementalModel.yaml
    sha256: 0c3ea32d9b744d1324b6c58ef06d60e5a71a0d327d8c9a880ee89490dbd02a7e
    role: context
  - path: data/curated/SparsePachinkoAllocationInference.yaml
    sha256: 106fa341abeaf8ee5543e7818a0fc293ce345c8ac64cbd3eb546d21b82d7f7c8
    role: context
  - path: research/discovery/20261013T183932Z-epsilon-truncation-cdp.json
    sha256: 9c3a2653eff2bfa3c0f4650c22ec9bed0ed2fdaad7df43c8fdb2d55789592ce9
    role: context
  - path: research/discovery/epsilon-truncation-cdp-boundaries.py
    sha256: 0775eba9b7fd9c3ca3a528d922ead0ed3afca945c06c8c74f5d6de72781469d0
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
- target_id: AIMech:EpsilonTruncationCDP
  path: data/curated/EpsilonTruncationCDP.yaml
  label: Epsilon-truncation for Conditional Distribution Prediction
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/EpsilonTruncationCDP.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:EpsilonTruncationCDP'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:EpsilonTruncationCDP
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: All25 pages of the author-hosted journal PDF inspected, including the
      cover, Sections1–13, Equations1–6 and unnumbered formulas, Definitions1–5, Algorithm1,
      Figures1–8, Tables1–17 and all28references. Earlier conference papers, author
      code and empirical replication excluded.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:EpsilonTruncationCDP
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 148.84s (0:02:28)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 640 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 318 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 315,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:EpsilonTruncationCDP
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
  - AIMech:EpsilonTruncationCDP
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
  - AIMech:EpsilonTruncationCDP
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/epsilon-truncation-cdp-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:EpsilonTruncationCDP
  exit_code: 0
  expected_exit_code: 0
  summary: '{"strict_cutoff_and_renormalization": ["0", "3/19", "16/19"], "equal_cutoff_retained":
    true, "empty_row_rejected": true, "guarded_common_cutoff": "3/5", "literal_arrangement_weight_sum":
    "3/4", "binomial_count_probability_sum": "1", "literal_pair_sum_child_count":
    "2", "distinct_parent_sum_child_count": "1", "homogeneous_tree_actual_and_original_prediction":
    111, "truncated_prediction": "11", "same_type_budget_different_stage_predictions":
    ["1", "7/5"], "scope": "Constructed mathematical checks, not author-code validation
    or replication."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T183932Z-epsilon-truncation-cdp.json
  accessed_at: '2026-10-13T18:39:44Z'
  support: supports
  summary: Compared all 442 pinned AIO and 639 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    5, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered
    66 AIO and 345 native definitions, with every matched definition read. 12 full
    annotated AIO node/edge/generated contexts and 4 full native records were inspected.
    Retain the named CDP probability-table modification and calibrated per-level cutoff
    method. It changes an estimator, not the actual IDA* search tree or solution policy.
    Original CDP, lookup-based reuse, IDA*IM threshold control, score-margin sequence
    beam pruning and pruned topic-model Gibbs transitions have distinct targets. Generic
    epsilon-truncation outside this search-estimation context is not asserted equivalent.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T18:39:44Z'
  support: supports
  summary: MarkovChain is a related component context for normalized type-transition
    tables, including depth-varying tables. The estimator propagates counts with branching
    and pruning rather than probability mass. Twelve full AIO contexts and four full
    native neighbors support the bounded mapping assessment; no exact or subclass
    relationship is asserted.
- evidence_id: lelis2013prediction
  kind: primary_source
  reference: https://webdocs.cs.ualberta.ca/~santanad/papers/2013/ARTINT2694.pdf
  locator: All25 pages of the author-hosted journal PDF inspected, including the cover,
    Sections1–13, Equations1–6 and unnumbered formulas, Definitions1–5, Algorithm1,
    Figures1–8, Tables1–17 and all28references. Earlier conference papers, author
    code and empirical replication excluded.
  accessed_at: '2026-10-13T17:23:34Z'
  snapshot_sha256: ee16910b3529eab60bc1527773d4d91d77d81778a153d33f7a8d6e80c09f6fba
  support: supports
  summary: 'Author-hosted personal-copy PDF: one cover plus 24 journal pages, Artificial
    Intelligence 196 (2013), pages 53–76. PDF pages 2–25 correspond to printed pages
    53–76. All 25 pages visually inspected: Sections 1–13, Equations 1–6 and unnumbered
    formulas, Definitions 1–5, Algorithm 1, Figures 1–8, Tables 1–17 and all 28 references.
    Earlier conference papers and author code were not inspected.'
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/epsilon-truncation-cdp-boundaries.py
  accessed_at: '2026-10-13T18:43:30Z'
  snapshot_sha256: 0775eba9b7fd9c3ca3a528d922ead0ed3afca945c06c8c74f5d6de72781469d0
  support: supports
  summary: Exact rational constructions test strict cutoff and retained equality,
    empty-row prevention, missing Bernoulli count multiplicity, repeated parent mass
    in a literal supertype sum, a case where truncation worsens exact counting, and
    the state required for caching depth-varying schedules. No author code or empirical
    replication.
assessments:
- assessment_id: identity
  area: identity
  topic: Epsilon-truncation for Conditional Distribution Prediction
  outcome: supported
  target_ids:
  - AIMech:EpsilonTruncationCDP
  evidence_ids:
  - identity
  - lelis2013prediction
  summary: Retain this distinct DRAFT algorithm.
  details: Retain the CDP table-modification method as an estimator procedure. Original
    CDP, lookup caching, online IDA*IM search control, actual beam pruning and sparse
    topic-model transitions have distinct targets. The generic epsilon-truncation
    phrase is not a universal alias.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:EpsilonTruncationCDP
  evidence_ids:
  - mapping
  - lelis2013prediction
  summary: The declared AIO mapping is supported.
  details: MarkovChain is a related component context for normalized type-transition
    tables, including depth-varying tables. The estimator propagates counts with branching
    and pruning rather than probability mass. Twelve full AIO contexts and four full
    native neighbors support the bounded mapping assessment; no exact or subclass
    relationship is asserted.
- assessment_id: level-specific-table-modification
  area: evidence
  topic: level-specific-table-modification
  outcome: supported
  target_ids:
  - AIMech:EpsilonTruncationCDP
  evidence_ids:
  - lelis2013prediction
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The strict below-cutoff removal retains equality, renormalizes positive
    survivors and guards against empty rows. This changes the prediction model, not
    the actual search policy.
- assessment_id: offline-cutoff-calibration
  area: evidence
  topic: offline-cutoff-calibration
  outcome: supported
  target_ids:
  - AIMech:EpsilonTruncationCDP
  evidence_ids:
  - lelis2013prediction
  summary: Supported within the stated primary-source and mathematical scope.
  details: The source uses per-level sampled allocation outcomes and a majority-prefix
    rule with a row-survival guard. It is an offline heuristic approximation, not
    an asserted universal cutoff or exact true-error minimizer.
- assessment_id: printed-calibration-boundaries
  area: evidence
  topic: printed-calibration-boundaries
  outcome: supported
  target_ids:
  - AIMech:EpsilonTruncationCDP
  evidence_ids:
  - lelis2013prediction
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: 'The literal count weight lacks a binomial coefficient: forN2,p.5 its weights
    sum.75 rather than1. The displayed pair-indexed count repeats parent mass when
    multiple refined children share a coarse group. The record qualifies the printed
    formulas without claiming knowledge of author software.'
- assessment_id: aggregation-and-accuracy-limits
  area: evidence
  topic: aggregation-and-accuracy-limits
  outcome: supported
  target_ids:
  - AIMech:EpsilonTruncationCDP
  evidence_ids:
  - lelis2013prediction
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: An exactly counted homogeneous tree has111nodes, whereas deleting its rare
    child type gives11. The source itself reports metric-dependent degradation and
    denies unbiasedness. These facts preclude universal per-start improvement.
- assessment_id: finite-evaluation-and-amortization
  area: evidence
  topic: finite-evaluation-and-amortization
  outcome: supported
  target_ids:
  - AIMech:EpsilonTruncationCDP
  evidence_ids:
  - lelis2013prediction
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Error metrics differ, preprocessing is costly and experiment regimes are
    finite. Same-model lookup preserves predictions only with all relevant depth/schedule
    context; a constructed same-type/budget case differs across stages. No universal
    runtime or accuracy guarantee is claimed.
- assessment_id: constructed-boundaries
  area: consistency
  topic: cutoff normalization, calibration formula interpretation and finite search-count
    evidence
  outcome: supported
  target_ids:
  - AIMech:EpsilonTruncationCDP
  evidence_ids:
  - lelis2013prediction
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Exact rational constructions test strict cutoff and retained equality,
    empty-row prevention, missing Bernoulli count multiplicity, repeated parent mass
    in a literal supertype sum, a case where truncation worsens exact counting, and
    the state required for caching depth-varying schedules. No author code or empirical
    replication.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:EpsilonTruncationCDP
  evidence_ids:
  - identity
  - mapping
  - lelis2013prediction
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 5 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. Assessed all maintained fields, source/hash/version,
    strict cutoff equality, nonempty normalization, calibration scope, literal probability
    and aggregation formulas, rare-descendant counterexample and finite evidence.
    No unseen author implementation is certified.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- One new DRAFT concept, yielding 640 native and 442 unchanged generated records.
  The 825-entry main frontier retains 474 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- 'All25 author-hosted pages visually read: cover plus printed53–76; Sections1–13,
  Equations1–6 and unnumbered equations, Algorithm1, Definitions1–5, Figures1–8, Tables1–17,
  all28references. Focused rereading of PDFs8–10 and17 checked probability, aggregation
  and caching boundaries. Other versions and author code excluded.'
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
