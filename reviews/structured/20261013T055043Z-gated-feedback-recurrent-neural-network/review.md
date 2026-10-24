# Scientific author self-review of GF-RNN

- Review: 20261013T055043Z-gated-feedback-recurrent-neural-network
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T05:44:12Z
- Finished UTC: 2026-10-13T05:50:43Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain GF-RNN as a distinct DRAFT architecture with a broader recurrent-network mapping. All six claims and fields have support with scalar layer-pair gates, delayed/current update order, candidate placement, soft-weight/gradient and conditional evaluation boundaries. No actionable record defect found; no author implementation or training execution occurred.

## Scope And Provenance

All fields of the maintained GF-RNN and complete primary conference paper.

Selection: Exact maintained ID: AIMech:GatedFeedbackRecurrentNeuralNetwork
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ad51f25aadec1d16f60d1fb225a41e7e47a76ce2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:GatedFeedbackRecurrentNeuralNetwork | data/curated/GatedFeedbackRecurrentNeuralNetwork.yaml | maintained | Gated-feedback recurrent neural network |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:GatedFeedbackRecurrentNeuralNetwork | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 144.14s (0:02:24)<br>Checked 442 record(s); 0 failed.<br>Checked 577 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 233 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 231,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:GatedFeedbackRecurrentNeuralNetwork | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:GatedFeedbackRecurrentNeuralNetwork | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:GatedFeedbackRecurrentNeuralNetwork | Exited 0 without output. |
| Constructed gated-feedback boundaries | passed | True | AIMech:GatedFeedbackRecurrentNeuralNetwork | {"pair_gate_sum": 1.5, "scalar_transition_derivative_at_zero": 1.9999999999973335, "current_lower_state": 0.26362483547220333, "current_upper_state": 0.23634553248127574, "upper_using_old_lower": 0.18774620586828544, "interpretation": "Independent sigmoid pair gates need not sum to one or guarantee contraction; current bottom-up input differs from previous recurrent inputs."} |

## Scientific And Domain Assessments

### Global layer-pair gates and delayed inter-layer recurrence

identity: supported. Targets: AIMech:GatedFeedbackRecurrentNeuralNetwork.

Retain GF-RNN as a distinct DRAFT architecture.

No normalized maintained identity matched. Ignored-inclusive matches were read. Data-dependent scalar gates on every previous-to-current layer pair differ from unit-wise GRU/LSTM gates, initialized identity recurrence, fixed linear SCRN context, generic stacked cells and top-down Helmholtz generative/recognition models.

### Broader recurrent architecture

grounding: supported. Targets: AIMech:GatedFeedbackRecurrentNeuralNetwork.

The broader mapping is supported.

The complete architecture fits RecurrentNeuralNetwork. GRU/LSTM and cell targets describe components or configurations and exclude the complete tanh/GRU/LSTM family as exact identity. FeedbackNetwork is less explicit about the needed recurrent layer/gate scope, so the clearer recurrent target is selected; no forced additional mapping.

### global-layer-pair-gate

evidence: supported. Targets: AIMech:GatedFeedbackRecurrentNeuralNetwork.

Supported with gate-placement, timing and evaluation boundaries.

Section3 p4 defines one scalar g for each source/destination layer pair from current lower-layer input and concatenated previous states. Tanh recurrence sums gated projections across all previous layers. The record distinguishes global scalar scope from unit-coordinate gates.

### delayed-feedback-and-order

evidence: supported. Targets: AIMech:GatedFeedbackRecurrentNeuralNetwork.

Supported with gate-placement, timing and evaluation boundaries.

Figure1 and equations use previous states for recurrent top-down feedback and current lower-layer values for bottom-up input. The displayed order is acyclic within a timestep; L-squared pair counting follows the fully connected recurrent form. The caption omits skip connections, so no complete implementation topology is certified.

### placement-in-lstm-and-gru

evidence: supported. Targets: AIMech:GatedFeedbackRecurrentNeuralNetwork.

Supported with gate-placement, timing and evaluation boundaries.

Section3.1 explicitly leaves ordinary gate equations unmodified and applies global gates to candidate content. Its GRU reset vector multiplies aggregated projected recurrent content. No claim that global gates replace ordinary unit gates or directly modulate every cell carry path is imported.

### soft-connectivity-and-gradient-limits

evidence: supported. Targets: AIMech:GatedFeedbackRecurrentNeuralNetwork.

Supported with gate-placement, timing and evaluation boundaries.

Independent sigmoid gates with finite logits in real arithmetic lie in(0,1) but need not normalize, hard-route or zero edges. Adaptive weights are distinct from fixed clockwork rates. Projection norms and gate/current-layer derivative paths prevent contraction or indefinite gradient preservation from following solely from gate bounds.

### unit-dependent-language-evidence

evidence: supported. Targets: AIMech:GatedFeedbackRecurrentNeuralNetwork.

Supported with gate-placement, timing and evaluation boundaries.

Table2 and conclusion retain worse tanh results alongside selected GRU/LSTM improvements. Matched parameter counts differ from larger same-hidden-count models. Gate-fixed ablation and wall-clock curves are bounded evidence; vocabulary differences obstruct a direct comparison to one older large model.

### program-task-and-metric

evidence: supported. Targets: AIMech:GatedFeedbackRecurrentNeuralNetwork.

Supported with gate-placement, timing and evaluation boundaries.

The generated-script encoder-decoder task has selected capacities, lengths, nesting and curriculum. The stated next-symbol metric conditions on correct preceding outputs, not guaranteed autonomous program execution. Figure3 has a negative GRU cell despite mostly favorable gaps. No numerical benchmark or reproduction is asserted.

### Independent gates, non-contraction and update timing

consistency: supported. Targets: AIMech:GatedFeedbackRecurrentNeuralNetwork.

Constructed algebra confirms the stated distinctions.

Three zero-logit pair gates sum to1.5. A scalar tanh(sigmoid(h)*4*h) transition has derivative2 at zero, so gate bounds do not ensure contraction. A two-layer example using current lower input differs from substituting the previous lower state. These are transparent curator constructions, not trained or implementation evidence.

### Complete maintained record and source-scope accounting

provenance: supported. Targets: AIMech:GatedFeedbackRecurrentNeuralNetwork.

All maintained fields inspected; DRAFT remains.

Read ID/name/alias, architecture kind, definition/citation, identity context, six claims and locators, primary source identity/version/access/hash, AIO pin, mapping, six limitations and actual curation times. Source/context/capture hashes and exact report mirror agree. Full conference-paper reading is distinguished from uninspected code/supplement and training. No actionable record defect identified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T054233Z-gated-feedback-recurrent-neural-network.json | supports | Compared all 442 pinned AIO and 575 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 4, 0, 0 lines. All matches were read and classified before curation. Semantic matching inspected 63 AIO and140 native definitions, with unchanged preceding rows verified and new matches read. Seven full annotated AIO node/edge/generated contexts and four full native records were inspected. The complete architecture is distinct from unit-wise GRU/LSTM gates, a generic RNN-cell stack, initialized identity recurrence and fixed decaying SCRN context. Full nodes for FeedbackNetwork, GRUCellLayer, LSTMCellLayer, LongShortTermMemory, GatedRecurrentUnit and StackedRNNCellsLayer do not supply exact identity. LSTM/GRU targets describe possible configurations or components, not the entire tanh/GRU/LSTM feedback family. Generic iterative-feedback wording alone does not resolve the required inter-layer temporal/gate scope; RecurrentNeuralNetwork is the selected broader architecture target. Top-down generative/recognition Helmholtz models and feedback-based augmentation/diagnostic procedures are different concepts. Unit-type variants remain within GF-RNN. |
| mapping | sources/aio/aio.json | supports | Sixty-three AIO and140 native semantic rows read or verified unchanged; seven full AIO node/edge/generated contexts and four full native records inspected. RecurrentNeuralNetwork is broader. Generic FeedbackNetwork wording, unit-specific GRU/LSTM targets and stacked-cell wrappers do not establish exact global pair-gate identity; the recurrent category is the selected mapping. |
| chung2015 | https://proceedings.mlr.press/v37/chung15.pdf; Complete nine-page conference paper visually read; defining gates and source-negative/evaluation pp3–8 reread after capture. | supports | ICML2015, PMLR37:2067–2075. All nine conference PDF pages, Figures1–3, Tables1–4, background Equations1–10 and defining unnumbered equations on p4 visually inspected; locators use PDF page order. |
| calculation | research/discovery/gated-feedback-boundaries.py | supports | Constructed independent sigmoid gates summing above one, a gated scalar transition with derivative above one, and current-versus-previous lower-layer input. No author code, training, benchmark or full architecture verification. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue manufactured for a clean record review.
- The three-record batch shares one complete repository gate run; this does not represent three independent gate executions.
- One new DRAFT concept, yielding 576 native and 442 unchanged generated records. The 761-entry main frontier retains 482 pending and 57 partly addressed cohorts; discovery is incomplete.
- Displayed equations and a figure that omits skip connections do not certify every implementation detail. Constructed scalar checks are not trained-model evidence.
- All nine conference-paper pages were read, including equations, figures, tables and negative results. No author implementation, supplement, training or empirical replication inspected.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T055043Z-gated-feedback-recurrent-neural-network
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of GF-RNN
started_at: '2026-10-13T05:44:12Z'
finished_at: '2026-10-13T05:50:43Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged global versus unit gate identity, delayed/current
    update order, candidate placement, normalization/gradient limits and adverse or
    metric-qualified evaluation evidence. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain GF-RNN as a distinct DRAFT architecture with a broader recurrent-network
  mapping. All six claims and fields have support with scalar layer-pair gates, delayed/current
  update order, candidate placement, soft-weight/gradient and conditional evaluation
  boundaries. No actionable record defect found; no author implementation or training
  execution occurred.
source:
  git_revision: ad51f25aadec1d16f60d1fb225a41e7e47a76ce2
  state: working_tree
  inputs:
  - path: data/aio/FeedbackNetwork.yaml
    sha256: 74d1e22e6d446bd06278d8503785333cd4ae97c00cb4831a0c482347965ef0ba
    role: context
  - path: data/aio/GRUCellLayer.yaml
    sha256: e64b73e626933d3f94b8920401b7ee037fe7d6469a296978a0ddb2eefd751b9c
    role: context
  - path: data/aio/GatedRecurrentUnit.yaml
    sha256: 16e73da5012ad3e1d3de23bb30db0a0e18464b02b038acddd1c0f07f4fe82940
    role: context
  - path: data/aio/LSTMCellLayer.yaml
    sha256: 3d2dba1fbcce253281204550c144d7c19ad5476ac421c2697ad5913a8adf44c6
    role: context
  - path: data/aio/LongShortTermMemory.yaml
    sha256: c78f9d7cd7fa61ec26d6964fbdd8dd17302480984df521b1a1c2b336f9768093
    role: context
  - path: data/aio/RecurrentNeuralNetwork.yaml
    sha256: 1ebef94d2014e9a19d4bb3ed0fed6c5d77098a5a44e00e2cbd1cfe682dfcd892
    role: context
  - path: data/aio/StackedRNNCellsLayer.yaml
    sha256: e2fdefc9152c3607a8bfc70334431ce65a3d82ad75760fd0f747c42b5c47eee9
    role: context
  - path: data/curated/GatedFeedbackRecurrentNeuralNetwork.yaml
    sha256: 7b26adbe3234f94c69012c3be72a9d3ca0e63ee1652caf7f2030e47566fc943b
    role: target
  - path: data/curated/HelmholtzMachine.yaml
    sha256: 9b582e184b171ae372dca219cd6704318a9287150dcbf540f95a8b4cc6405cac
    role: context
  - path: data/curated/IdentityInitializedRecurrentNeuralNetwork.yaml
    sha256: cfa1543605f0046f0c2bbbffc294d7cead0a444f1db5cb955bdf8971a7ae9d62
    role: context
  - path: data/curated/StructurallyConstrainedRecurrentNeuralNetwork.yaml
    sha256: 03df44109ede633bd0f41cf2b7b355ac0708ff53411e5ef1a9f69d131380f6bc
    role: context
  - path: data/curated/Zoneout.yaml
    sha256: 25f1c0e8bfaa491a871c780730358be99aa37f44933aefc466b1ca0024563ae6
    role: context
  - path: research/discovery/20261013T054233Z-gated-feedback-recurrent-neural-network.json
    sha256: 4b58294184d36a6bed6d6ed3909713fe0cea0fcf22a9bd9e64ffb20861fe3c4f
    role: context
  - path: research/discovery/gated-feedback-boundaries.py
    sha256: 631bad810f49c0d14e966197382747074460762fde6564356781c6bb7bb5d6b1
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
- target_id: AIMech:GatedFeedbackRecurrentNeuralNetwork
  path: data/curated/GatedFeedbackRecurrentNeuralNetwork.yaml
  label: Gated-feedback recurrent neural network
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GatedFeedbackRecurrentNeuralNetwork.yaml
    role: maintained
scope:
  description: All fields of the maintained GF-RNN and complete primary conference
    paper.
  selection: 'Exact maintained ID: AIMech:GatedFeedbackRecurrentNeuralNetwork'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:GatedFeedbackRecurrentNeuralNetwork
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not full scientific rereview.
  - target: Supplement, author implementation and dependencies
    reason: No author code, runtime, data generator or training implementation inspected.
  - target: Training, benchmark reproduction and universal guarantees
    reason: No source execution, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:GatedFeedbackRecurrentNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 144.14s (0:02:24)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 577 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 233 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 231,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:GatedFeedbackRecurrentNeuralNetwork
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
  - AIMech:GatedFeedbackRecurrentNeuralNetwork
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
  - AIMech:GatedFeedbackRecurrentNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed gated-feedback boundaries
  command: python3 research/discovery/gated-feedback-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:GatedFeedbackRecurrentNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: '{"pair_gate_sum": 1.5, "scalar_transition_derivative_at_zero": 1.9999999999973335,
    "current_lower_state": 0.26362483547220333, "current_upper_state": 0.23634553248127574,
    "upper_using_old_lower": 0.18774620586828544, "interpretation": "Independent sigmoid
    pair gates need not sum to one or guarantee contraction; current bottom-up input
    differs from previous recurrent inputs."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T054233Z-gated-feedback-recurrent-neural-network.json
  accessed_at: '2026-10-13T05:44:12Z'
  support: supports
  summary: Compared all 442 pinned AIO and 575 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    4, 0, 0 lines. All matches were read and classified before curation. Semantic
    matching inspected 63 AIO and140 native definitions, with unchanged preceding
    rows verified and new matches read. Seven full annotated AIO node/edge/generated
    contexts and four full native records were inspected. The complete architecture
    is distinct from unit-wise GRU/LSTM gates, a generic RNN-cell stack, initialized
    identity recurrence and fixed decaying SCRN context. Full nodes for FeedbackNetwork,
    GRUCellLayer, LSTMCellLayer, LongShortTermMemory, GatedRecurrentUnit and StackedRNNCellsLayer
    do not supply exact identity. LSTM/GRU targets describe possible configurations
    or components, not the entire tanh/GRU/LSTM feedback family. Generic iterative-feedback
    wording alone does not resolve the required inter-layer temporal/gate scope; RecurrentNeuralNetwork
    is the selected broader architecture target. Top-down generative/recognition Helmholtz
    models and feedback-based augmentation/diagnostic procedures are different concepts.
    Unit-type variants remain within GF-RNN.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T05:44:12Z'
  support: supports
  summary: Sixty-three AIO and140 native semantic rows read or verified unchanged;
    seven full AIO node/edge/generated contexts and four full native records inspected.
    RecurrentNeuralNetwork is broader. Generic FeedbackNetwork wording, unit-specific
    GRU/LSTM targets and stacked-cell wrappers do not establish exact global pair-gate
    identity; the recurrent category is the selected mapping.
- evidence_id: chung2015
  kind: primary_source
  reference: https://proceedings.mlr.press/v37/chung15.pdf
  locator: Complete nine-page conference paper visually read; defining gates and source-negative/evaluation
    pp3–8 reread after capture.
  accessed_at: '2026-10-13T05:11:09Z'
  snapshot_sha256: fd5e0a4f6f3b862e83a93942c459f8df39c2d524effbc670b6cd4778a3fb5c46
  support: supports
  summary: ICML2015, PMLR37:2067–2075. All nine conference PDF pages, Figures1–3,
    Tables1–4, background Equations1–10 and defining unnumbered equations on p4 visually
    inspected; locators use PDF page order.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/gated-feedback-boundaries.py
  accessed_at: '2026-10-13T05:44:46Z'
  snapshot_sha256: 631bad810f49c0d14e966197382747074460762fde6564356781c6bb7bb5d6b1
  support: supports
  summary: Constructed independent sigmoid gates summing above one, a gated scalar
    transition with derivative above one, and current-versus-previous lower-layer
    input. No author code, training, benchmark or full architecture verification.
assessments:
- assessment_id: identity
  area: identity
  topic: Global layer-pair gates and delayed inter-layer recurrence
  outcome: supported
  target_ids:
  - AIMech:GatedFeedbackRecurrentNeuralNetwork
  evidence_ids:
  - identity
  - chung2015
  summary: Retain GF-RNN as a distinct DRAFT architecture.
  details: No normalized maintained identity matched. Ignored-inclusive matches were
    read. Data-dependent scalar gates on every previous-to-current layer pair differ
    from unit-wise GRU/LSTM gates, initialized identity recurrence, fixed linear SCRN
    context, generic stacked cells and top-down Helmholtz generative/recognition models.
- assessment_id: mapping
  area: grounding
  topic: Broader recurrent architecture
  outcome: supported
  target_ids:
  - AIMech:GatedFeedbackRecurrentNeuralNetwork
  evidence_ids:
  - mapping
  - chung2015
  summary: The broader mapping is supported.
  details: The complete architecture fits RecurrentNeuralNetwork. GRU/LSTM and cell
    targets describe components or configurations and exclude the complete tanh/GRU/LSTM
    family as exact identity. FeedbackNetwork is less explicit about the needed recurrent
    layer/gate scope, so the clearer recurrent target is selected; no forced additional
    mapping.
- assessment_id: global-layer-pair-gate
  area: evidence
  topic: global-layer-pair-gate
  outcome: supported
  target_ids:
  - AIMech:GatedFeedbackRecurrentNeuralNetwork
  evidence_ids:
  - chung2015
  - calculation
  summary: Supported with gate-placement, timing and evaluation boundaries.
  details: Section3 p4 defines one scalar g for each source/destination layer pair
    from current lower-layer input and concatenated previous states. Tanh recurrence
    sums gated projections across all previous layers. The record distinguishes global
    scalar scope from unit-coordinate gates.
- assessment_id: delayed-feedback-and-order
  area: evidence
  topic: delayed-feedback-and-order
  outcome: supported
  target_ids:
  - AIMech:GatedFeedbackRecurrentNeuralNetwork
  evidence_ids:
  - chung2015
  - calculation
  summary: Supported with gate-placement, timing and evaluation boundaries.
  details: Figure1 and equations use previous states for recurrent top-down feedback
    and current lower-layer values for bottom-up input. The displayed order is acyclic
    within a timestep; L-squared pair counting follows the fully connected recurrent
    form. The caption omits skip connections, so no complete implementation topology
    is certified.
- assessment_id: placement-in-lstm-and-gru
  area: evidence
  topic: placement-in-lstm-and-gru
  outcome: supported
  target_ids:
  - AIMech:GatedFeedbackRecurrentNeuralNetwork
  evidence_ids:
  - chung2015
  - calculation
  summary: Supported with gate-placement, timing and evaluation boundaries.
  details: Section3.1 explicitly leaves ordinary gate equations unmodified and applies
    global gates to candidate content. Its GRU reset vector multiplies aggregated
    projected recurrent content. No claim that global gates replace ordinary unit
    gates or directly modulate every cell carry path is imported.
- assessment_id: soft-connectivity-and-gradient-limits
  area: evidence
  topic: soft-connectivity-and-gradient-limits
  outcome: supported
  target_ids:
  - AIMech:GatedFeedbackRecurrentNeuralNetwork
  evidence_ids:
  - chung2015
  - calculation
  summary: Supported with gate-placement, timing and evaluation boundaries.
  details: Independent sigmoid gates with finite logits in real arithmetic lie in(0,1)
    but need not normalize, hard-route or zero edges. Adaptive weights are distinct
    from fixed clockwork rates. Projection norms and gate/current-layer derivative
    paths prevent contraction or indefinite gradient preservation from following solely
    from gate bounds.
- assessment_id: unit-dependent-language-evidence
  area: evidence
  topic: unit-dependent-language-evidence
  outcome: supported
  target_ids:
  - AIMech:GatedFeedbackRecurrentNeuralNetwork
  evidence_ids:
  - chung2015
  - calculation
  summary: Supported with gate-placement, timing and evaluation boundaries.
  details: Table2 and conclusion retain worse tanh results alongside selected GRU/LSTM
    improvements. Matched parameter counts differ from larger same-hidden-count models.
    Gate-fixed ablation and wall-clock curves are bounded evidence; vocabulary differences
    obstruct a direct comparison to one older large model.
- assessment_id: program-task-and-metric
  area: evidence
  topic: program-task-and-metric
  outcome: supported
  target_ids:
  - AIMech:GatedFeedbackRecurrentNeuralNetwork
  evidence_ids:
  - chung2015
  - calculation
  summary: Supported with gate-placement, timing and evaluation boundaries.
  details: The generated-script encoder-decoder task has selected capacities, lengths,
    nesting and curriculum. The stated next-symbol metric conditions on correct preceding
    outputs, not guaranteed autonomous program execution. Figure3 has a negative GRU
    cell despite mostly favorable gaps. No numerical benchmark or reproduction is
    asserted.
- assessment_id: constructed-boundaries
  area: consistency
  topic: Independent gates, non-contraction and update timing
  outcome: supported
  target_ids:
  - AIMech:GatedFeedbackRecurrentNeuralNetwork
  evidence_ids:
  - chung2015
  - calculation
  summary: Constructed algebra confirms the stated distinctions.
  details: Three zero-logit pair gates sum to1.5. A scalar tanh(sigmoid(h)*4*h) transition
    has derivative2 at zero, so gate bounds do not ensure contraction. A two-layer
    example using current lower input differs from substituting the previous lower
    state. These are transparent curator constructions, not trained or implementation
    evidence.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record and source-scope accounting
  outcome: supported
  target_ids:
  - AIMech:GatedFeedbackRecurrentNeuralNetwork
  evidence_ids:
  - identity
  - mapping
  - chung2015
  - calculation
  summary: All maintained fields inspected; DRAFT remains.
  details: Read ID/name/alias, architecture kind, definition/citation, identity context,
    six claims and locators, primary source identity/version/access/hash, AIO pin,
    mapping, six limitations and actual curation times. Source/context/capture hashes
    and exact report mirror agree. Full conference-paper reading is distinguished
    from uninspected code/supplement and training. No actionable record defect identified.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue manufactured
  for a clean record review.
- The three-record batch shares one complete repository gate run; this does not represent
  three independent gate executions.
- One new DRAFT concept, yielding 576 native and 442 unchanged generated records.
  The 761-entry main frontier retains 482 pending and 57 partly addressed cohorts;
  discovery is incomplete.
- Displayed equations and a figure that omits skip connections do not certify every
  implementation detail. Constructed scalar checks are not trained-model evidence.
- All nine conference-paper pages were read, including equations, figures, tables
  and negative results. No author implementation, supplement, training or empirical
  replication inspected.
- Only the isolated recovery checkout is changed; original-checkout synchronization
  and old round141 cleanup remain pending explicit approval after automatic review
  rejection.
related_reviews: []
links: []
tags:
- native-concepts
- recurrent-architectures
- self-review
- discovery-ongoing
```
