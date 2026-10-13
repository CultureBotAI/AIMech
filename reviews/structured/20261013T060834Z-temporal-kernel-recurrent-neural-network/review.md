# Scientific author self-review of Temporal-kernel recurrent neural network

- Review: 20261013T060834Z-temporal-kernel-recurrent-neural-network
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T06:00:12Z
- Finished UTC: 2026-10-13T06:08:34Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Temporal-kernel recurrent neural network as a distinct DRAFT architecture with an explicit broader recurrent-network mapping. All fields and six claims have support within the declared manuscript and mathematical boundaries. No actionable record defect found; no author implementation or training executed.

## Scope And Provenance

All maintained fields and the complete inspected primary manuscript.

Selection: Exact maintained ID: AIMech:TemporalKernelRecurrentNeuralNetwork
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 96d5f25a9f8a9aea084e21f2b424e55c6680ae19.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:TemporalKernelRecurrentNeuralNetwork | data/curated/TemporalKernelRecurrentNeuralNetwork.yaml | maintained | Temporal-kernel recurrent neural network |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:TemporalKernelRecurrentNeuralNetwork | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 197.36s (0:03:17)<br>Checked 442 record(s); 0 failed.<br>Checked 579 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 235 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 234,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:TemporalKernelRecurrentNeuralNetwork | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:TemporalKernelRecurrentNeuralNetwork | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:TemporalKernelRecurrentNeuralNetwork | Exited 0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:TemporalKernelRecurrentNeuralNetwork | {"recursive_trace": ["1", "5/2", "1/4"], "explicit_trace": ["1", "5/2", "1/4"], "three_lag_weight_mass": "7/4", "delayed_vs_current_input": ["1", "3"], "coupled_trace_derivative": 2.4999999999973332, "combined_before_nonlinearity": 0.46211715726000974, "mean_of_independent_outputs": 0.14973849934787756, "interpretation": "Constructed geometric sums and a coupled scalar derivative, not a trained model, exact backward audit or measured complexity result."} |

## Scientific And Domain Assessments

### Temporal-kernel recurrent neural network

identity: supported. Targets: AIMech:TemporalKernelRecurrentNeuralNetwork.

Retain the distinct DRAFT architecture.

Exponential source-specific lag factors and pre-nonlinearity traces distinguish this architecture from SCRN context blocks, fixed Clockwork schedules, adaptive GF-RNN pair gates and generic finite-lag NARX models. Multiple kernel components are source-defined configurations. Earlier leaky-integrator priority is not claimed.

### Broader recurrent architecture

grounding: supported. Targets: AIMech:TemporalKernelRecurrentNeuralNetwork.

The broader mapping is supported.

RecurrentNeuralNetwork supplies the broader architecture mapping. LSTM cell/gate machinery, a simple recurrent layer and echo-state reservoir constraints do not establish exact identity or a better broader mapping.

### factored-temporal-connections

evidence: supported. Targets: AIMech:TemporalKernelRecurrentNeuralNetwork.

Supported with source and mathematical qualifications.

Equation6 factors a spatial weight and a source-specific exponential lag factor. Input and hidden lambda families are distinct despite reused notation. Histories combine before f, so this is not independent nonlinear-trajectory averaging or unrestricted per-lag matrices.

### recursive-traces-and-time-indexing

evidence: supported. Targets: AIMech:TemporalKernelRecurrentNeuralNetwork.

Supported with source and mathematical qualifications.

Equations8–11 define zero-initialized finite sums and recursive traces using t-1 inputs/states. Explicit sums match the constructed recursion. The draft notes the current-input background convention versus delayed kernel convention; lambda0 selects the latest term under the chosen indexing, not an unqualified same-time equality.

### unnormalized-memory-and-stability

evidence: supported. Targets: AIMech:TemporalKernelRecurrentNeuralNetwork.

Supported with source and mathematical qualifications.

The geometric weights lack normalization and can sum above1. The bounded-drive estimate M/(1-lambda) follows under stated fixed-lambda assumptions. Coupled state derivative in a scalar example is2.5 despite lambda.5; decay alone does not ensure whole-network contraction or stable learning.

### learned-timescales-and-multiple-kernels

evidence: supported. Targets: AIMech:TemporalKernelRecurrentNeuralNetwork.

Supported with source and mathematical qualifications.

Section3.1 uses a time-shared positive sigmoid parameter and separately discusses negative lambda. Multiple kernels sum connection contributions before nonlinearity; this is not an ensemble of independent models or necessarily positive attention weights.

### timescale-and-computation-boundaries

evidence: supported. Targets: AIMech:TemporalKernelRecurrentNeuralNetwork.

Supported with source and mathematical qualifications.

Source discussion preserves weak far-lag influence, initialization sensitivity and coarse slow summaries. Fixed-size trace updates are constant work per step, hence linear forward work in sequence length; this is not constant total training storage or measured hardware speed. The source PDF lacks figure artwork, so no unseen diagram is interpreted.

### conditional-recall-and-negative-result

evidence: supported. Targets: AIMech:TemporalKernelRecurrentNeuralNetwork.

Supported with source and mathematical qualifications.

Serial recall uses a selected TKRNN+5 configuration and top1/top2 character metrics, not perfect full-sequence recall. Page11 reports a failed quadratic-function task and speculates about another optimizer. Expressivity does not prove optimizer success; chosen capacities, truncation and settings limit comparison.

### Temporal factorization, unnormalized traces, delayed-input indexing, nonlinear coupling and source-negative results

consistency: supported. Targets: AIMech:TemporalKernelRecurrentNeuralNetwork.

Constructed calculations support the explicit boundaries.

Recursive traces equal explicit finite sums; weight mass need not normalize; delayed and current input differ; a coupled recurrent trace can have derivative above one; summing contributions before a nonlinearity differs from independent-output averaging. No backward implementation, training or runtime claim is certified.

### Complete maintained record and inspected-source scope

provenance: supported. Targets: AIMech:TemporalKernelRecurrentNeuralNetwork.

All maintained fields inspected; DRAFT remains.

Read ID/name/alias, kind, definition/citation, identity search context, six claims/locators, source identity/version/access/hash, AIO pin and mapping, six limitations and actual curation times. Capture/source/context hashes and exact report mirror agree. Source limitations remain explicit; no actionable record defect found.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T060009Z-temporal-kernel-recurrent-neural-network.json | supports | Compared all 442 pinned AIO and 578 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 3, 0, 0 lines. All distinct match contents were read and concern discovery leads and reviewed context, not an existing exact record. Semantic matching inspected 63 AIO and 150 native definitions, with unchanged preceding rows verified and new matches read. Four full annotated AIO node/edge/generated contexts and four full native records were inspected. The temporal-kernel architecture factors lag weights and filters past input and hidden activities before its nonlinear state computation. SCRN has a separate context trace and constrained recurrent block; Clockwork uses prescribed module ticks; GF-RNN uses input-dependent pair gates. The existing NARX record denotes a generic finite-lag input-output model family, not this source-specific exponential neural realization. Fast persistent contrastive divergence is a training algorithm and Oja is a weight update. Multiple exponential components remain configurations; no priority for leaky recurrence is asserted. RecurrentNeuralNetwork is the selected broader architecture mapping; none of the three other full AIO contexts establishes exact identity or a better broader target. |
| mapping | sources/aio/aio.json | supports | RecurrentNeuralNetwork supplies the broader architecture mapping. LSTM cell/gate machinery, a simple recurrent layer and echo-state reservoir constraints do not establish exact identity or a better broader mapping. |
| sutskever2009 | https://www.cs.utoronto.ca/~ilya/pubs/2008/tkrnn.pdf; All fifteen author-manuscript pages read before capture; defining equations, caveats and evaluation on pp6–8,11–12 reread after capture. Figure artwork and final journal layout unavailable in this inspected copy; no author code, training, runtime audit or independent review. | supports | Author manuscript dated 30 July 2009, fifteen PDF pages, associated with the 2010 Neural Networks23(2):239–243 article. All manuscript pages, Equations1–11 and references visually read. Figure1/2 captions are present but corresponding artwork is absent. Published-version layout and figures were not inspected. |
| calculation | research/discovery/temporal-kernel-boundaries.py | supports | Recursive traces equal explicit finite sums; weight mass need not normalize; delayed and current input differ; a coupled recurrent trace can have derivative above one; summing contributions before a nonlinearity differs from independent-output averaging. No backward implementation, training or runtime claim is certified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue manufactured for a clean record review.
- The two-record batch shares one complete repository gate run; this does not represent independent gate executions.
- One new DRAFT concept, yielding 579 native and 442 unchanged generated records. The 763-entry main frontier retains 481 pending and 57 partly addressed cohorts; discovery is incomplete.
- All15 pages of the author manuscript dated30July2009 visually read, including Equations1–11, discussion, experimental settings, negative result and references. Figure1/2 captions are present but their artwork is absent from this PDF; no graphical detail is inferred. Published article and author code not inspected.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T060834Z-temporal-kernel-recurrent-neural-network
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Temporal-kernel recurrent neural network
started_at: '2026-10-13T06:00:12Z'
finished_at: '2026-10-13T06:08:34Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged Temporal factorization, unnormalized traces,
    delayed-input indexing, nonlinear coupling and source-negative results. This is
    adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Temporal-kernel recurrent neural network as a distinct DRAFT architecture
  with an explicit broader recurrent-network mapping. All fields and six claims have
  support within the declared manuscript and mathematical boundaries. No actionable
  record defect found; no author implementation or training executed.
source:
  git_revision: 96d5f25a9f8a9aea084e21f2b424e55c6680ae19
  state: working_tree
  inputs:
  - path: data/aio/EchoStateNetwork.yaml
    sha256: f15649d74702c61b11a09550e5c5e75f6ccde67089135a4b4adb5fc9c6610905
    role: context
  - path: data/aio/LongShortTermMemory.yaml
    sha256: c78f9d7cd7fa61ec26d6964fbdd8dd17302480984df521b1a1c2b336f9768093
    role: context
  - path: data/aio/RecurrentNeuralNetwork.yaml
    sha256: 1ebef94d2014e9a19d4bb3ed0fed6c5d77098a5a44e00e2cbd1cfe682dfcd892
    role: context
  - path: data/aio/SimpleRNNLayer.yaml
    sha256: 6e93e3bd5702eb0a1109a12526138ae8aed009f30cc7cb764b0c7db4fa3f0bbe
    role: context
  - path: data/curated/ClockworkRecurrentNeuralNetwork.yaml
    sha256: 465373ea285a9c4102069b1cef3023c52328a10ccc526855aea218bcec3f41fa
    role: context
  - path: data/curated/GatedFeedbackRecurrentNeuralNetwork.yaml
    sha256: 7b26adbe3234f94c69012c3be72a9d3ca0e63ee1652caf7f2030e47566fc943b
    role: context
  - path: data/curated/NonlinearAutoregressiveExogenousModel.yaml
    sha256: 3157f6cbd735ef6792e7afbc5a0ff4e2be97305d9896e7e91452b674524fc0ec
    role: context
  - path: data/curated/StructurallyConstrainedRecurrentNeuralNetwork.yaml
    sha256: 03df44109ede633bd0f41cf2b7b355ac0708ff53411e5ef1a9f69d131380f6bc
    role: context
  - path: data/curated/TemporalKernelRecurrentNeuralNetwork.yaml
    sha256: fdb23e4953d5eb0d52410b7d7046ef95fca6c64ab677e439153f327443e441d4
    role: target
  - path: research/discovery/20261013T060009Z-temporal-kernel-recurrent-neural-network.json
    sha256: 938d77b65c4a2763efbf7052022155e7cd0506cec906629454bb4287e9959032
    role: context
  - path: research/discovery/temporal-kernel-boundaries.py
    sha256: 99b3f590c0f105d73f7fb592e5ddda66970f7ca348556fd17e67f9a0aea6706c
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
- target_id: AIMech:TemporalKernelRecurrentNeuralNetwork
  path: data/curated/TemporalKernelRecurrentNeuralNetwork.yaml
  label: Temporal-kernel recurrent neural network
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TemporalKernelRecurrentNeuralNetwork.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary manuscript.
  selection: 'Exact maintained ID: AIMech:TemporalKernelRecurrentNeuralNetwork'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:TemporalKernelRecurrentNeuralNetwork
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not full scientific rereview.
  - target: Other source versions and author implementation
    reason: All fifteen author-manuscript pages read before capture; defining equations,
      caveats and evaluation on pp6–8,11–12 reread after capture. Figure artwork and
      final journal layout unavailable in this inspected copy; no author code, training,
      runtime audit or independent review.
  - target: Training, benchmark reproduction and universal guarantees
    reason: No model execution, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:TemporalKernelRecurrentNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 197.36s (0:03:17)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 579 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 235 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 234,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:TemporalKernelRecurrentNeuralNetwork
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
  - AIMech:TemporalKernelRecurrentNeuralNetwork
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
  - AIMech:TemporalKernelRecurrentNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/temporal-kernel-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:TemporalKernelRecurrentNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: '{"recursive_trace": ["1", "5/2", "1/4"], "explicit_trace": ["1", "5/2",
    "1/4"], "three_lag_weight_mass": "7/4", "delayed_vs_current_input": ["1", "3"],
    "coupled_trace_derivative": 2.4999999999973332, "combined_before_nonlinearity":
    0.46211715726000974, "mean_of_independent_outputs": 0.14973849934787756, "interpretation":
    "Constructed geometric sums and a coupled scalar derivative, not a trained model,
    exact backward audit or measured complexity result."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T060009Z-temporal-kernel-recurrent-neural-network.json
  accessed_at: '2026-10-13T06:00:12Z'
  support: supports
  summary: Compared all 442 pinned AIO and 578 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    3, 0, 0 lines. All distinct match contents were read and concern discovery leads
    and reviewed context, not an existing exact record. Semantic matching inspected
    63 AIO and 150 native definitions, with unchanged preceding rows verified and
    new matches read. Four full annotated AIO node/edge/generated contexts and four
    full native records were inspected. The temporal-kernel architecture factors lag
    weights and filters past input and hidden activities before its nonlinear state
    computation. SCRN has a separate context trace and constrained recurrent block;
    Clockwork uses prescribed module ticks; GF-RNN uses input-dependent pair gates.
    The existing NARX record denotes a generic finite-lag input-output model family,
    not this source-specific exponential neural realization. Fast persistent contrastive
    divergence is a training algorithm and Oja is a weight update. Multiple exponential
    components remain configurations; no priority for leaky recurrence is asserted.
    RecurrentNeuralNetwork is the selected broader architecture mapping; none of the
    three other full AIO contexts establishes exact identity or a better broader target.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T06:00:12Z'
  support: supports
  summary: RecurrentNeuralNetwork supplies the broader architecture mapping. LSTM
    cell/gate machinery, a simple recurrent layer and echo-state reservoir constraints
    do not establish exact identity or a better broader mapping.
- evidence_id: sutskever2009
  kind: primary_source
  reference: https://www.cs.utoronto.ca/~ilya/pubs/2008/tkrnn.pdf
  locator: All fifteen author-manuscript pages read before capture; defining equations,
    caveats and evaluation on pp6–8,11–12 reread after capture. Figure artwork and
    final journal layout unavailable in this inspected copy; no author code, training,
    runtime audit or independent review.
  accessed_at: '2026-10-13T05:49:06Z'
  snapshot_sha256: a8d166b3b399370b84dcd02e2183ce637f34d77817cabe82a8dc344b9322a0f9
  support: supports
  summary: Author manuscript dated 30 July 2009, fifteen PDF pages, associated with
    the 2010 Neural Networks23(2):239–243 article. All manuscript pages, Equations1–11
    and references visually read. Figure1/2 captions are present but corresponding
    artwork is absent. Published-version layout and figures were not inspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/temporal-kernel-boundaries.py
  accessed_at: '2026-10-13T06:00:44Z'
  snapshot_sha256: 99b3f590c0f105d73f7fb592e5ddda66970f7ca348556fd17e67f9a0aea6706c
  support: supports
  summary: Recursive traces equal explicit finite sums; weight mass need not normalize;
    delayed and current input differ; a coupled recurrent trace can have derivative
    above one; summing contributions before a nonlinearity differs from independent-output
    averaging. No backward implementation, training or runtime claim is certified.
assessments:
- assessment_id: identity
  area: identity
  topic: Temporal-kernel recurrent neural network
  outcome: supported
  target_ids:
  - AIMech:TemporalKernelRecurrentNeuralNetwork
  evidence_ids:
  - identity
  - sutskever2009
  summary: Retain the distinct DRAFT architecture.
  details: Exponential source-specific lag factors and pre-nonlinearity traces distinguish
    this architecture from SCRN context blocks, fixed Clockwork schedules, adaptive
    GF-RNN pair gates and generic finite-lag NARX models. Multiple kernel components
    are source-defined configurations. Earlier leaky-integrator priority is not claimed.
- assessment_id: mapping
  area: grounding
  topic: Broader recurrent architecture
  outcome: supported
  target_ids:
  - AIMech:TemporalKernelRecurrentNeuralNetwork
  evidence_ids:
  - mapping
  - sutskever2009
  summary: The broader mapping is supported.
  details: RecurrentNeuralNetwork supplies the broader architecture mapping. LSTM
    cell/gate machinery, a simple recurrent layer and echo-state reservoir constraints
    do not establish exact identity or a better broader mapping.
- assessment_id: factored-temporal-connections
  area: evidence
  topic: factored-temporal-connections
  outcome: supported
  target_ids:
  - AIMech:TemporalKernelRecurrentNeuralNetwork
  evidence_ids:
  - sutskever2009
  - calculation
  summary: Supported with source and mathematical qualifications.
  details: Equation6 factors a spatial weight and a source-specific exponential lag
    factor. Input and hidden lambda families are distinct despite reused notation.
    Histories combine before f, so this is not independent nonlinear-trajectory averaging
    or unrestricted per-lag matrices.
- assessment_id: recursive-traces-and-time-indexing
  area: evidence
  topic: recursive-traces-and-time-indexing
  outcome: supported
  target_ids:
  - AIMech:TemporalKernelRecurrentNeuralNetwork
  evidence_ids:
  - sutskever2009
  - calculation
  summary: Supported with source and mathematical qualifications.
  details: Equations8–11 define zero-initialized finite sums and recursive traces
    using t-1 inputs/states. Explicit sums match the constructed recursion. The draft
    notes the current-input background convention versus delayed kernel convention;
    lambda0 selects the latest term under the chosen indexing, not an unqualified
    same-time equality.
- assessment_id: unnormalized-memory-and-stability
  area: evidence
  topic: unnormalized-memory-and-stability
  outcome: supported
  target_ids:
  - AIMech:TemporalKernelRecurrentNeuralNetwork
  evidence_ids:
  - sutskever2009
  - calculation
  summary: Supported with source and mathematical qualifications.
  details: The geometric weights lack normalization and can sum above1. The bounded-drive
    estimate M/(1-lambda) follows under stated fixed-lambda assumptions. Coupled state
    derivative in a scalar example is2.5 despite lambda.5; decay alone does not ensure
    whole-network contraction or stable learning.
- assessment_id: learned-timescales-and-multiple-kernels
  area: evidence
  topic: learned-timescales-and-multiple-kernels
  outcome: supported
  target_ids:
  - AIMech:TemporalKernelRecurrentNeuralNetwork
  evidence_ids:
  - sutskever2009
  - calculation
  summary: Supported with source and mathematical qualifications.
  details: Section3.1 uses a time-shared positive sigmoid parameter and separately
    discusses negative lambda. Multiple kernels sum connection contributions before
    nonlinearity; this is not an ensemble of independent models or necessarily positive
    attention weights.
- assessment_id: timescale-and-computation-boundaries
  area: evidence
  topic: timescale-and-computation-boundaries
  outcome: supported
  target_ids:
  - AIMech:TemporalKernelRecurrentNeuralNetwork
  evidence_ids:
  - sutskever2009
  - calculation
  summary: Supported with source and mathematical qualifications.
  details: Source discussion preserves weak far-lag influence, initialization sensitivity
    and coarse slow summaries. Fixed-size trace updates are constant work per step,
    hence linear forward work in sequence length; this is not constant total training
    storage or measured hardware speed. The source PDF lacks figure artwork, so no
    unseen diagram is interpreted.
- assessment_id: conditional-recall-and-negative-result
  area: evidence
  topic: conditional-recall-and-negative-result
  outcome: supported
  target_ids:
  - AIMech:TemporalKernelRecurrentNeuralNetwork
  evidence_ids:
  - sutskever2009
  - calculation
  summary: Supported with source and mathematical qualifications.
  details: Serial recall uses a selected TKRNN+5 configuration and top1/top2 character
    metrics, not perfect full-sequence recall. Page11 reports a failed quadratic-function
    task and speculates about another optimizer. Expressivity does not prove optimizer
    success; chosen capacities, truncation and settings limit comparison.
- assessment_id: constructed-boundaries
  area: consistency
  topic: Temporal factorization, unnormalized traces, delayed-input indexing, nonlinear
    coupling and source-negative results
  outcome: supported
  target_ids:
  - AIMech:TemporalKernelRecurrentNeuralNetwork
  evidence_ids:
  - sutskever2009
  - calculation
  summary: Constructed calculations support the explicit boundaries.
  details: Recursive traces equal explicit finite sums; weight mass need not normalize;
    delayed and current input differ; a coupled recurrent trace can have derivative
    above one; summing contributions before a nonlinearity differs from independent-output
    averaging. No backward implementation, training or runtime claim is certified.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record and inspected-source scope
  outcome: supported
  target_ids:
  - AIMech:TemporalKernelRecurrentNeuralNetwork
  evidence_ids:
  - identity
  - mapping
  - sutskever2009
  - calculation
  summary: All maintained fields inspected; DRAFT remains.
  details: Read ID/name/alias, kind, definition/citation, identity search context,
    six claims/locators, source identity/version/access/hash, AIO pin and mapping,
    six limitations and actual curation times. Capture/source/context hashes and exact
    report mirror agree. Source limitations remain explicit; no actionable record
    defect found.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue manufactured
  for a clean record review.
- The two-record batch shares one complete repository gate run; this does not represent
  independent gate executions.
- One new DRAFT concept, yielding 579 native and 442 unchanged generated records.
  The 763-entry main frontier retains 481 pending and 57 partly addressed cohorts;
  discovery is incomplete.
- All15 pages of the author manuscript dated30July2009 visually read, including Equations1–11,
  discussion, experimental settings, negative result and references. Figure1/2 captions
  are present but their artwork is absent from this PDF; no graphical detail is inferred.
  Published article and author code not inspected.
- No author code, training, paid service, hardware measurement or empirical replication.
  Constructed checks test stated boundaries only.
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
