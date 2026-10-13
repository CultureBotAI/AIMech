# Scientific author self-review of Real-time recurrent learning

- Review: 20261013T063032Z-real-time-recurrent-learning
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T06:19:36Z
- Finished UTC: 2026-10-13T06:30:32Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain RTRL as a distinct DRAFT algorithm with a related TrainingStrategy mapping. All fields and six claims are supported within the fixed-parameter, online-update, target-substitution and resource boundaries. No actionable finding; no author implementation or training executed.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:RealTimeRecurrentLearning
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base cbcef8ab980d8f92922f715e9f3659e05b648f47.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:RealTimeRecurrentLearning | data/curated/RealTimeRecurrentLearning.yaml | maintained | Real-time recurrent learning |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:RealTimeRecurrentLearning | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 165.44s (0:02:45)<br>Checked 442 record(s); 0 failed.<br>Checked 581 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 238 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 237,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:RealTimeRecurrentLearning | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:RealTimeRecurrentLearning | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:RealTimeRecurrentLearning | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:RealTimeRecurrentLearning | {"fixed_trajectory_loss": 0.0326118204301201, "forward_gradient": [[0.020378748144974472, -0.019151726249093844, 0.038699419380119976, 0.10718488124821322], [0.07627133529082336, 0.03695519553768801, 0.09667546798438109, 0.37035223824912894]], "reverse_gradient": [[0.020378748144974472, -0.019151726249093844, 0.03869941938011998, 0.10718488124821324], [0.07627133529082336, 0.036955195537688, 0.0966754679843811, 0.37035223824912883]], "max_finite_difference_error": 6.1923521865736575e-12, "changing_weights": {"weights": ["1/2", "3/5"], "propagated_sensitivity": "11/10", "fixed_current_weight_trajectory_derivative": "6/5", "current_weight_partial_holding_past_fixed": "1/2"}, "teacher_forcing": {"first_output_derivative_before_reset": 0.049755798116734, "next_forced_derivative": 0.20407226752815083, "next_free_derivative": 0.13756406796109258}, "dense_sensitivity_values": 16, "naive_recurrent_multiplications_per_step": 32} |

## Scientific And Domain Assessments

### Real-time recurrent learning

identity: supported. Targets: AIMech:RealTimeRecurrentLearning.

Retain this distinct DRAFT algorithm.

Retain RTRL as a forward sensitivity training algorithm, distinct from SGD update sampling, sign-based Rprop, raw-regressor pseudo-linear estimation and NNPDA architecture. Fixed-weight accumulation and teacher-forced online variants remain source-defined configurations.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:RealTimeRecurrentLearning.

Mapping direction and scope are supported.

TrainingStrategy supports a related training context, not an inferred algorithm superclass under its preprocessing definition. RecurrentNeuralNetwork is the trained architecture; LLM and supervised-task categories do not supply exact identity.

### forward-state-sensitivities

evidence: supported. Targets: AIMech:RealTimeRecurrentLearning.

Supported within the stated primary-source and mathematical scope.

Equations10–14 differentiate synchronous recurrence with direct weight and recurrent-state terms. Zero initial sensitivities require weight-independent initial state; supplied signal dependence requires additional derivatives. The full tensor is propagated, not only observed outputs.

### fixed-trajectory-gradient

evidence: supported. Targets: AIMech:RealTimeRecurrentLearning.

Supported within the stated primary-source and mathematical scope.

The target-minus-output contraction has negative-gradient sign. Fixed-weight contributions accumulate for the same loss; missing targets mask direct error, not hidden sensitivities. Forward and reverse calculations plus finite differences agree in the constructed example.

### online-weight-drift

evidence: supported. Targets: AIMech:RealTimeRecurrentLearning.

Supported within the stated primary-source and mathematical scope.

Section2.2 explicitly qualifies online updates as not exact total-trajectory gradient. The rational two-weight example distinguishes propagated sensitivity from rerunning at a common current weight; a smaller rate is not a convergence theorem.

### teacher-forced-variant

evidence: supported. Targets: AIMech:RealTimeRecurrentLearning.

Supported within the stated primary-source and mathematical scope.

Target substitution removes future dependence through forced outputs while preserving the current discrepancy update. Equations17–19 assume exogenous targets. The distinct scalar derivatives support the path difference without claiming free-running success.

### storage-and-nonlocality

evidence: supported. Targets: AIMech:RealTimeRecurrentLearning.

Supported within the stated primary-source and mathematical scope.

Section2.4 requires n*r sensitivities and gives dense n^2*(n+m) storage. Direct recurrence counts yield n^2*r work; fixed sequence-length storage is not fixed network-size cost or a measured speed. Discussion identifies nonlocal information.

### experimental-scope

evidence: supported. Targets: AIMech:RealTimeRecurrentLearning.

Supported within the stated primary-source and mathematical scope.

All five demonstration sections and Discussion were read. Finite controller imitation is not proof of an internal unbounded tape. Oscillation success is qualified by teacher forcing and near-zero-gradient difficulty; no universal or reproduced benchmark claim is retained.

### fixed-parameter derivative exactness, online weight drift, target substitution, tensor dimensions and empirical scope

consistency: supported. Targets: AIMech:RealTimeRecurrentLearning.

Constructed calculations support the stated distinctions.

A fixed two-unit three-step tanh recurrence gives matching forward sensitivities, reverse derivatives and centered finite differences. Exact rational changing-weight and scalar teacher-forcing examples distinguish derivative scopes. Direct dense tensor and recurrence counts are arithmetic, not measured performance. No fitting or author implementation executed.

### All maintained fields

provenance: supported. Targets: AIMech:RealTimeRecurrentLearning.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all six claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Fixed versus drifting weights, supplied-signal derivatives, missing targets, teacher-forcing update order and tensor cost were challenged. All record fields and the selected mapping were read after capture. No actionable defect found.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T061904Z-real-time-recurrent-learning.json | supports | Compared all 442 pinned AIO and 579 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 11, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered 64 AIO and 155 native definitions, with unchanged preceding rows verified and new matches read. 4 full annotated AIO node/edge/generated contexts and 4 full native records were inspected. Matches concern prior RTRL discovery leads and NNPDA derivative context, not an exact record. RTRL propagates full recurrent state sensitivities; generic SGD describes sampled-gradient parameter updates, Rprop controls sign-based step sizes, and pseudo-linear regression substitutes a raw regressor for a total sensitivity. NNPDA is a recurrent controller architecture whose augmented stack-read derivative is approximate. TrainingStrategy is related because its preprocessing definition does not supply an algorithm superclass. RecurrentNeuralNetwork is a training subject, DifferentiableLLM is an LLM architecture and SupervisedLearning a task category. None establishes exact identity. Fixed-weight accumulated and online-update forms, including the teacher-forced configuration, remain within this source-defined algorithm family. |
| mapping | sources/aio/aio.json | supports | TrainingStrategy supports a related training context, not an inferred algorithm superclass under its preprocessing definition. RecurrentNeuralNetwork is the trained architecture; LLM and supervised-task categories do not supply exact identity. |
| williams1989 | https://gwern.net/doc/ai/nn/rnn/1989-williams-2.pdf; All ten manuscript pages read before capture; defining sensitivity, online-update and teacher-forcing/storage passages on pp4–6 reread after capture. No final publisher layout, author code, fitting or empirical replication. | supports | Ten-page manuscript copy openly hosted by Gwern, identifying the Neural Computation1:270–280 publication (1989). All ten PDF pages, Equations1–19, experiments and references visually read. PDF page numbers are used; final publisher layout was not inspected. |
| calculation | research/discovery/rtrl-boundaries.py | supports | A fixed two-unit three-step tanh recurrence gives matching forward sensitivities, reverse derivatives and centered finite differences. Exact rational changing-weight and scalar teacher-forcing examples distinguish derivative scopes. Direct dense tensor and recurrence counts are arithmetic, not measured performance. No fitting or author implementation executed. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined corrected-input repository gate execution; these are not independent gate runs.
- One new DRAFT concept, yielding 580 native and 442 unchanged generated records. The 764-entry main frontier retains 481 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All ten manuscript pages visually read, including Equations1–19, optional teacher forcing, storage analysis, all five experimental sections, discussion and references. This openly hosted manuscript copy identifies the 1989 Neural Computation publication; its pagination differs from journal pages270–280. No author code, later algorithm variant or final publisher layout inspected.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T063032Z-real-time-recurrent-learning
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Real-time recurrent learning
started_at: '2026-10-13T06:19:36Z'
finished_at: '2026-10-13T06:30:32Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged fixed-parameter derivative exactness,
    online weight drift, target substitution, tensor dimensions and empirical scope.
    This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain RTRL as a distinct DRAFT algorithm with a related TrainingStrategy
  mapping. All fields and six claims are supported within the fixed-parameter, online-update,
  target-substitution and resource boundaries. No actionable finding; no author implementation
  or training executed.
source:
  git_revision: cbcef8ab980d8f92922f715e9f3659e05b648f47
  state: working_tree
  inputs:
  - path: data/aio/DifferentiableLLM.yaml
    sha256: b8a40c81f74e60c62abed98282803859d0f00ad7e3b9c3d161d63002575f50a3
    role: context
  - path: data/aio/RecurrentNeuralNetwork.yaml
    sha256: 1ebef94d2014e9a19d4bb3ed0fed6c5d77098a5a44e00e2cbd1cfe682dfcd892
    role: context
  - path: data/aio/SupervisedLearning.yaml
    sha256: 472f033f91a14c8727e525ddd30f82fcaf16a2514fa8f062667fb94fc9c9b718
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/curated/NeuralNetworkPushdownAutomaton.yaml
    sha256: 71b3ba6474d3a8fca545d1f33c4a46da156d419ffe82e21ca048114967663f2c
    role: context
  - path: data/curated/PseudoLinearRegressionEstimation.yaml
    sha256: 70f7a23a68a1248b2aaf11252bdaffb5e72c61d805eed6e7099ec2d4ddeaaffc
    role: context
  - path: data/curated/RealTimeRecurrentLearning.yaml
    sha256: 56d96389c192a6a7e40852add607c729c48ac19aeb4cc5ef6c44b1a5c3190e7c
    role: target
  - path: data/curated/ResilientBackpropagation.yaml
    sha256: e0fd7cf20b05fc93ac579d5a396168891efaf96f9b31948c7152f6207f9b8e18
    role: context
  - path: data/curated/StochasticGradientDescent.yaml
    sha256: 5c57fc809ae8667d5be8cda421cc9f0bd1f0c668f64ba3d7b23d788528b46e97
    role: context
  - path: research/discovery/20261013T061904Z-real-time-recurrent-learning.json
    sha256: 747366975c24962a403cd941e182b0f48d2464a13f4c6c334a2f992ea5f80d07
    role: context
  - path: research/discovery/rtrl-boundaries.py
    sha256: f20b011e958a991a1657294fc4a561538bee21a215c88565fcfc072daa2f4112
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
- target_id: AIMech:RealTimeRecurrentLearning
  path: data/curated/RealTimeRecurrentLearning.yaml
  label: Real-time recurrent learning
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RealTimeRecurrentLearning.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:RealTimeRecurrentLearning'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:RealTimeRecurrentLearning
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: All ten manuscript pages read before capture; defining sensitivity, online-update
      and teacher-forcing/storage passages on pp4–6 reread after capture. No final
      publisher layout, author code, fitting or empirical replication.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:RealTimeRecurrentLearning
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 165.44s (0:02:45)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 581 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 238 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 237,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:RealTimeRecurrentLearning
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
  - AIMech:RealTimeRecurrentLearning
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
  - AIMech:RealTimeRecurrentLearning
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/rtrl-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:RealTimeRecurrentLearning
  exit_code: 0
  expected_exit_code: 0
  summary: '{"fixed_trajectory_loss": 0.0326118204301201, "forward_gradient": [[0.020378748144974472,
    -0.019151726249093844, 0.038699419380119976, 0.10718488124821322], [0.07627133529082336,
    0.03695519553768801, 0.09667546798438109, 0.37035223824912894]], "reverse_gradient":
    [[0.020378748144974472, -0.019151726249093844, 0.03869941938011998, 0.10718488124821324],
    [0.07627133529082336, 0.036955195537688, 0.0966754679843811, 0.37035223824912883]],
    "max_finite_difference_error": 6.1923521865736575e-12, "changing_weights": {"weights":
    ["1/2", "3/5"], "propagated_sensitivity": "11/10", "fixed_current_weight_trajectory_derivative":
    "6/5", "current_weight_partial_holding_past_fixed": "1/2"}, "teacher_forcing":
    {"first_output_derivative_before_reset": 0.049755798116734, "next_forced_derivative":
    0.20407226752815083, "next_free_derivative": 0.13756406796109258}, "dense_sensitivity_values":
    16, "naive_recurrent_multiplications_per_step": 32}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T061904Z-real-time-recurrent-learning.json
  accessed_at: '2026-10-13T06:19:36Z'
  support: supports
  summary: Compared all 442 pinned AIO and 579 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    11, 0, 0 lines. All distinct match contents were inspected. Semantic matching
    covered 64 AIO and 155 native definitions, with unchanged preceding rows verified
    and new matches read. 4 full annotated AIO node/edge/generated contexts and 4
    full native records were inspected. Matches concern prior RTRL discovery leads
    and NNPDA derivative context, not an exact record. RTRL propagates full recurrent
    state sensitivities; generic SGD describes sampled-gradient parameter updates,
    Rprop controls sign-based step sizes, and pseudo-linear regression substitutes
    a raw regressor for a total sensitivity. NNPDA is a recurrent controller architecture
    whose augmented stack-read derivative is approximate. TrainingStrategy is related
    because its preprocessing definition does not supply an algorithm superclass.
    RecurrentNeuralNetwork is a training subject, DifferentiableLLM is an LLM architecture
    and SupervisedLearning a task category. None establishes exact identity. Fixed-weight
    accumulated and online-update forms, including the teacher-forced configuration,
    remain within this source-defined algorithm family.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T06:19:36Z'
  support: supports
  summary: TrainingStrategy supports a related training context, not an inferred algorithm
    superclass under its preprocessing definition. RecurrentNeuralNetwork is the trained
    architecture; LLM and supervised-task categories do not supply exact identity.
- evidence_id: williams1989
  kind: primary_source
  reference: https://gwern.net/doc/ai/nn/rnn/1989-williams-2.pdf
  locator: All ten manuscript pages read before capture; defining sensitivity, online-update
    and teacher-forcing/storage passages on pp4–6 reread after capture. No final publisher
    layout, author code, fitting or empirical replication.
  accessed_at: '2026-10-13T06:06:26Z'
  snapshot_sha256: 348ca1d75163d1fa2412f4fc2c3d73531051ba14ce9bdc51a098da19f869fc2a
  support: supports
  summary: Ten-page manuscript copy openly hosted by Gwern, identifying the Neural
    Computation1:270–280 publication (1989). All ten PDF pages, Equations1–19, experiments
    and references visually read. PDF page numbers are used; final publisher layout
    was not inspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/rtrl-boundaries.py
  accessed_at: '2026-10-13T06:26:32Z'
  snapshot_sha256: f20b011e958a991a1657294fc4a561538bee21a215c88565fcfc072daa2f4112
  support: supports
  summary: A fixed two-unit three-step tanh recurrence gives matching forward sensitivities,
    reverse derivatives and centered finite differences. Exact rational changing-weight
    and scalar teacher-forcing examples distinguish derivative scopes. Direct dense
    tensor and recurrence counts are arithmetic, not measured performance. No fitting
    or author implementation executed.
assessments:
- assessment_id: identity
  area: identity
  topic: Real-time recurrent learning
  outcome: supported
  target_ids:
  - AIMech:RealTimeRecurrentLearning
  evidence_ids:
  - identity
  - williams1989
  summary: Retain this distinct DRAFT algorithm.
  details: Retain RTRL as a forward sensitivity training algorithm, distinct from
    SGD update sampling, sign-based Rprop, raw-regressor pseudo-linear estimation
    and NNPDA architecture. Fixed-weight accumulation and teacher-forced online variants
    remain source-defined configurations.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:RealTimeRecurrentLearning
  evidence_ids:
  - mapping
  - williams1989
  summary: Mapping direction and scope are supported.
  details: TrainingStrategy supports a related training context, not an inferred algorithm
    superclass under its preprocessing definition. RecurrentNeuralNetwork is the trained
    architecture; LLM and supervised-task categories do not supply exact identity.
- assessment_id: forward-state-sensitivities
  area: evidence
  topic: forward-state-sensitivities
  outcome: supported
  target_ids:
  - AIMech:RealTimeRecurrentLearning
  evidence_ids:
  - williams1989
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equations10–14 differentiate synchronous recurrence with direct weight
    and recurrent-state terms. Zero initial sensitivities require weight-independent
    initial state; supplied signal dependence requires additional derivatives. The
    full tensor is propagated, not only observed outputs.
- assessment_id: fixed-trajectory-gradient
  area: evidence
  topic: fixed-trajectory-gradient
  outcome: supported
  target_ids:
  - AIMech:RealTimeRecurrentLearning
  evidence_ids:
  - williams1989
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The target-minus-output contraction has negative-gradient sign. Fixed-weight
    contributions accumulate for the same loss; missing targets mask direct error,
    not hidden sensitivities. Forward and reverse calculations plus finite differences
    agree in the constructed example.
- assessment_id: online-weight-drift
  area: evidence
  topic: online-weight-drift
  outcome: supported
  target_ids:
  - AIMech:RealTimeRecurrentLearning
  evidence_ids:
  - williams1989
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section2.2 explicitly qualifies online updates as not exact total-trajectory
    gradient. The rational two-weight example distinguishes propagated sensitivity
    from rerunning at a common current weight; a smaller rate is not a convergence
    theorem.
- assessment_id: teacher-forced-variant
  area: evidence
  topic: teacher-forced-variant
  outcome: supported
  target_ids:
  - AIMech:RealTimeRecurrentLearning
  evidence_ids:
  - williams1989
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Target substitution removes future dependence through forced outputs while
    preserving the current discrepancy update. Equations17–19 assume exogenous targets.
    The distinct scalar derivatives support the path difference without claiming free-running
    success.
- assessment_id: storage-and-nonlocality
  area: evidence
  topic: storage-and-nonlocality
  outcome: supported
  target_ids:
  - AIMech:RealTimeRecurrentLearning
  evidence_ids:
  - williams1989
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section2.4 requires n*r sensitivities and gives dense n^2*(n+m) storage.
    Direct recurrence counts yield n^2*r work; fixed sequence-length storage is not
    fixed network-size cost or a measured speed. Discussion identifies nonlocal information.
- assessment_id: experimental-scope
  area: evidence
  topic: experimental-scope
  outcome: supported
  target_ids:
  - AIMech:RealTimeRecurrentLearning
  evidence_ids:
  - williams1989
  summary: Supported within the stated primary-source and mathematical scope.
  details: All five demonstration sections and Discussion were read. Finite controller
    imitation is not proof of an internal unbounded tape. Oscillation success is qualified
    by teacher forcing and near-zero-gradient difficulty; no universal or reproduced
    benchmark claim is retained.
- assessment_id: constructed-boundaries
  area: consistency
  topic: fixed-parameter derivative exactness, online weight drift, target substitution,
    tensor dimensions and empirical scope
  outcome: supported
  target_ids:
  - AIMech:RealTimeRecurrentLearning
  evidence_ids:
  - williams1989
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: A fixed two-unit three-step tanh recurrence gives matching forward sensitivities,
    reverse derivatives and centered finite differences. Exact rational changing-weight
    and scalar teacher-forcing examples distinguish derivative scopes. Direct dense
    tensor and recurrence counts are arithmetic, not measured performance. No fitting
    or author implementation executed.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:RealTimeRecurrentLearning
  evidence_ids:
  - identity
  - mapping
  - williams1989
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all six claims/locators, source identities/versions/access/hashes, AIO pin and
    mapping, limitations and actual curation timestamps. Capture/source/context hashes
    and exact report mirror agree. Fixed versus drifting weights, supplied-signal
    derivatives, missing targets, teacher-forcing update order and tensor cost were
    challenged. All record fields and the selected mapping were read after capture.
    No actionable defect found.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined corrected-input repository gate execution; these
  are not independent gate runs.
- One new DRAFT concept, yielding 580 native and 442 unchanged generated records.
  The 764-entry main frontier retains 481 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- All ten manuscript pages visually read, including Equations1–19, optional teacher
  forcing, storage analysis, all five experimental sections, discussion and references.
  This openly hosted manuscript copy identifies the 1989 Neural Computation publication;
  its pagination differs from journal pages270–280. No author code, later algorithm
  variant or final publisher layout inspected.
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
