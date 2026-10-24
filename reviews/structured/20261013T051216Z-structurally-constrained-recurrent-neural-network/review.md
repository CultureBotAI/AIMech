# Scientific author self-review of SCRN

- Review: 20261013T051216Z-structurally-constrained-recurrent-neural-network
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T05:05:30Z
- Finished UTC: 2026-10-13T05:12:16Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain SCRN as a distinct DRAFT architecture with a broader recurrent-network mapping and related sigmoid mapping. All six claims and fields have support with structural, trace-memory, paper/code parameterization and fresh fixed-code boundaries. No actionable record defect found; no Torch or training execution occurred.

## Scope And Provenance

All fields of the maintained SCRN, complete primary v2 paper and declared pinned author-file inspection.

Selection: Exact maintained ID: AIMech:StructurallyConstrainedRecurrentNeuralNetwork
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 31098635124949298736e64be54d48964a49e8d8.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:StructurallyConstrainedRecurrentNeuralNetwork | data/curated/StructurallyConstrainedRecurrentNeuralNetwork.yaml | maintained | Structurally constrained recurrent neural network |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:StructurallyConstrainedRecurrentNeuralNetwork | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 210.81s (0:03:30)<br>Checked 442 record(s); 0 failed.<br>Checked 573 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 228 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 228,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:StructurallyConstrainedRecurrentNeuralNetwork | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:StructurallyConstrainedRecurrentNeuralNetwork | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:StructurallyConstrainedRecurrentNeuralNetwork | Exited 0 without output. |
| Constructed SCRN trace and parameterization boundaries | passed | True | AIMech:StructurallyConstrainedRecurrentNeuralNetwork | {"trace_unrolled": 2.25, "permutation_outputs": [1.75, 1.25], "carry_after_100_steps": 0.0059205292203339975, "paper_preactivation": 12.419999999999998, "unchanged_lagged_preactivation": 13.02, "transformed_lagged_preactivation": 12.42, "largest_bounded_context": 2.05, "scope": "Constructed scalar trace and affine-substitution checks only; no Torch or training execution."} |

## Scientific And Domain Assessments

### Coupled nonlinear recurrence and constrained linear context

identity: supported. Targets: AIMech:StructurallyConstrainedRecurrentNeuralNetwork.

Retain SCRN as a distinct DRAFT architecture.

No normalized maintained identity matched. All current ignored-inclusive matches were the preceding report’s SCRN candidate/URL and one semantic expression, read completely. A persistent zero hidden-to-context block and scalar/diagonal linear context distinguish SCRN from IRNN initialization, generic sigmoid belief networks, diagonal state-space families and unrelated diagonal objectives.

### Broader recurrent architecture and component sigmoid

grounding: supported. Targets: AIMech:StructurallyConstrainedRecurrentNeuralNetwork.

Both mapping directions are supported.

SCRN is a recurrent network, supporting a broader AIO recurrent architecture mapping. The fast-state component uses the named sigmoid operation and pinned nn.Sigmoid, supporting related SigmoidFunction. The whole architecture is neither a mathematical-function subclass nor identified by the generic SimpleRNN layer or sparse echo-state target.

### linear-context-and-fast-state

evidence: supported. Targets: AIMech:StructurallyConstrainedRecurrentNeuralNetwork.

Supported with explicit structural and source-convention boundaries.

Equations4–6 give a linear scalar-decay context, nonlinear fast recurrence and joint output. The context has no fast-state feedback. The record clearly assigns current-context h to the paper formulation and warns that the pinned graph uses lagged context.

### persistent-structure-and-adaptive-variant

evidence: supported. Targets: AIMech:StructurallyConstrainedRecurrentNeuralNetwork.

Supported with explicit structural and source-convention boundaries.

Equations7–8 identify structural zero/diagonal blocks and optional learned per-coordinate sigmoid decays. These parameters are shared through time rather than input-dependent gates. The adaptive configuration is preserved within the architecture, not conflated with unconstrained dense initialization or claimed as implemented in the selected fixed-code path.

### trace-memory-and-boundaries

evidence: supported. Targets: AIMech:StructurallyConstrainedRecurrentNeuralNetwork.

Supported with explicit structural and source-convention boundaries.

Expanding the scalar recurrence yields geometric recency weights and alpha^k direct carry. It is not permutation invariant or unlimited exact memory. Convex-combination bounds require bounded embeddings and a fixed scalar in(0,1); no bound on the separate fast Jacobian follows.

### current-versus-lagged-context

evidence: supported. Targets: AIMech:StructurallyConstrainedRecurrentNeuralNetwork.

Supported with explicit structural and source-convention boundaries.

Visual paper Equation5 uses s_t while mfactory.lua193 uses prev_hid_slow despite the nearby comment. Substituting Equation4 yields coupling alpha*P and input A+(1-alpha)*P*B. The record preserves equivalence of parameterized forms with transformation rather than identity at unchanged raw parameters or optimization.

### pinned-fixed-context-implementation

evidence: supported. Targets: AIMech:StructurallyConstrainedRecurrentNeuralNetwork.

Supported with explicit structural and source-convention boundaries.

The inspected initializer uses zero off-diagonal slow weights and diagonal1-semb_scale. Builder scales slow embedding; zeroSomeGradients clears slow recurrent gradients before the shown update. With fresh zero momentum and the stated update path the slow matrix remains fixed. The record explicitly excludes arbitrary loaded optimizer state, other mutations, dependencies and an adaptive-Q implementation claim.

### evaluation-and-finite-memory

evidence: supported. Targets: AIMech:StructurallyConstrainedRecurrentNeuralNetwork.

Supported with explicit structural and source-convention boundaries.

PTB and Text8 use selected capacities, BPTT settings and output parameterizations. Text8 reporting is a development split, not asserted independent test. Learned decays have conditional benefits; the conclusion acknowledges finite memory. No numeric benchmark, unconditional LSTM advantage or runtime replication is imported.

### Trace recurrence and parameter transformation

consistency: supported. Targets: AIMech:StructurallyConstrainedRecurrentNeuralNetwork.

Constructed algebra confirms the distinctions.

Trace expansion agrees at2.25; reversing inputs yields1.75 versus1.25, showing recency order matters. A .95 direct carry is about.00592 after100 steps. Paper preactivation12.42 differs from unchanged lagged13.02, while the transformed lagged form restores12.42. A bounded scalar context stays within its assumed input/initial bound. No training or complete gradient theorem is claimed.

### Complete maintained record and bounded code inspection

provenance: supported. Targets: AIMech:StructurallyConstrainedRecurrentNeuralNetwork.

All maintained fields inspected; DRAFT remains.

Read stable ID/name/aliases, architecture kind, definition/citations, identity context, six claims and source locators, five source identities/versions/access/hashes, AIO pin, mappings, six limitations and actual curation times. Source/context/capture hashes and exact report mirror agree. Full-paper and selected-file inspection are distinguished from partial rnn.lua scope and unexecuted dependencies. No actionable record defect identified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T050519Z-structurally-constrained-recurrent-neural-network.json | supports | Compared all 442 pinned AIO and 572 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 7, 0, 0 lines. The current matches were inspected as the preceding IRNN report’s SCRN source/lead notes and one semantic-search expression, not an existing maintained record. The semantic search covers 47 AIO rows and 128 native definitions; preceding 44 AIO and118 native rows were verified unchanged and the additional three activation-function rows plus ten native definitions read. Sigmoid-based belief networks, diagonal state-space models and unrelated diagonal clustering/representation objectives do not match this coupled recurrent architecture. Four full annotated AIO node/edge/generated contexts and four full adjacent native records were inspected. RecurrentNeuralNetwork is the broader architecture category and SigmoidFunction is a related component. SimpleRNNLayer lacks this coupled context structure; EchoStateNetwork’s sparse recurrent/output-learning definition does not establish equivalence or a superclass relation for jointly learned fast/input/context-output parameters. Unlike IRNN initialization, SCRN retains structural zero and diagonal context blocks. Fixed and adaptive per-unit decay configurations are preserved within the record, as are current-versus-lagged context conventions. |
| mapping | sources/aio/aio.json | supports | Forty-seven AIO and128 native semantic rows were read or verified unchanged. Four full AIO node/edge/generated contexts and four full native records support identity distinctions. Both mapping YAMLs reread after capture. RecurrentNeuralNetwork is the broader architecture category; SigmoidFunction is a related component. Generic layer and echo-state definitions do not establish the defining coupled context structure. |
| mikolov2015 | https://arxiv.org/pdf/1412.7753v2; Complete nine-page v2 paper visually read; defining Equations4–8 on pp4–5 reread after capture. | supports | April16,2015 v2; accepted-as-ICLR2015-workshop header. All nine printed/PDF pages, including Figure1, four tables, eight equations and references, visually inspected. |
| authorgraph | https://raw.githubusercontent.com/facebookarchive/SCRNNs/75582d4371d72dc789929b7076777bd5b3e38f1b/mfactory.lua; Complete mfactory.lua read; lines150–221 reread after capture. | supports | Pinned author commit 75582d4371d72dc789929b7076777bd5b3e38f1b (2018-01-03T00:15:58Z). Complete file read; SCRN graph at lines150–221. Static inspection only; no Torch/runtime execution. |
| authorinit | https://raw.githubusercontent.com/facebookarchive/SCRNNs/75582d4371d72dc789929b7076777bd5b3e38f1b/util.lua; Complete util.lua read; orthInit/initSCRNN reread after capture. | supports | Pinned author commit 75582d4371d72dc789929b7076777bd5b3e38f1b (2018-01-03T00:15:58Z). Complete file read; orthInit and initSCRNN checked. Static inspection only; no Torch/runtime execution. |
| authortrain | https://raw.githubusercontent.com/facebookarchive/SCRNNs/75582d4371d72dc789929b7076777bd5b3e38f1b/scrnn.lua; Complete scrnn.lua read; zero initial momentum and suppression/update call order reread after capture. | supports | Pinned author commit 75582d4371d72dc789929b7076777bd5b3e38f1b (2018-01-03T00:15:58Z). Complete file read; zero initial momentum, gradient suppression and call order checked. Static inspection only; no Torch/runtime execution. |
| authorupdate | https://raw.githubusercontent.com/facebookarchive/SCRNNs/75582d4371d72dc789929b7076777bd5b3e38f1b/rnn.lua; Only rnn.lua230–285 read; updateParams247–255 reread after capture. | supports | Pinned author commit 75582d4371d72dc789929b7076777bd5b3e38f1b (2018-01-03T00:15:58Z). Only lines230–285 inspected; updateParams at247–255. Remaining file not read. Static inspection only; no Torch/runtime execution. |
| calculation | research/discovery/scrn-boundaries.py | supports | Constructed trace expansion, permutation, decaying derivative and scalar bounded-input checks accompany exact affine substitution between current- and previous-context parameterizations. No Torch, training, benchmark or whole-network stability verification. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue manufactured for a clean record review.
- One new DRAFT concept, yielding 573 native and 442 unchanged generated records. The 758-entry main frontier retains 482 pending and 57 partly addressed cohorts; discovery is incomplete.
- The source evaluations use specific capacities, splits and training choices. No current best performance, unconditional LSTM advantage or independent scientific approval is asserted.
- All nine primary paper pages and six selected author files were read completely; only lines230–285 of rnn.lua were inspected. No full repository/dependency audit, Torch execution, training or empirical replication.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T051216Z-structurally-constrained-recurrent-neural-network
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of SCRN
started_at: '2026-10-13T05:05:30Z'
finished_at: '2026-10-13T05:12:16Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged identity/mapping, persistent structure,
    geometric memory limits, current-versus-lagged context, source parameterization
    and static fixed-code/evaluation boundaries. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain SCRN as a distinct DRAFT architecture with a broader recurrent-network
  mapping and related sigmoid mapping. All six claims and fields have support with
  structural, trace-memory, paper/code parameterization and fresh fixed-code boundaries.
  No actionable record defect found; no Torch or training execution occurred.
source:
  git_revision: 31098635124949298736e64be54d48964a49e8d8
  state: working_tree
  inputs:
  - path: data/aio/EchoStateNetwork.yaml
    sha256: f15649d74702c61b11a09550e5c5e75f6ccde67089135a4b4adb5fc9c6610905
    role: context
  - path: data/aio/RecurrentNeuralNetwork.yaml
    sha256: 1ebef94d2014e9a19d4bb3ed0fed6c5d77098a5a44e00e2cbd1cfe682dfcd892
    role: context
  - path: data/aio/SigmoidFunction.yaml
    sha256: e112ec27a5b6fc9de17cc2d3354b836968b6693c6902cf004b71f05a0aedb193
    role: context
  - path: data/aio/SimpleRNNLayer.yaml
    sha256: 6e93e3bd5702eb0a1109a12526138ae8aed009f30cc7cb764b0c7db4fa3f0bbe
    role: context
  - path: data/curated/GradientNormClipping.yaml
    sha256: f17c409240f4de8a4fc3a19847cb9eadd18bfc99113bfa2f39d976f01603654a
    role: context
  - path: data/curated/IdentityInitializedRecurrentNeuralNetwork.yaml
    sha256: cfa1543605f0046f0c2bbbffc294d7cead0a444f1db5cb955bdf8971a7ae9d62
    role: context
  - path: data/curated/NormStabilizer.yaml
    sha256: 534daa42c9584cefc836a8e5299b1b61e3e57957f153c3f5a0cd9d4c46202ecb
    role: context
  - path: data/curated/StructurallyConstrainedRecurrentNeuralNetwork.yaml
    sha256: 03df44109ede633bd0f41cf2b7b355ac0708ff53411e5ef1a9f69d131380f6bc
    role: target
  - path: data/curated/Zoneout.yaml
    sha256: 25f1c0e8bfaa491a871c780730358be99aa37f44933aefc466b1ca0024563ae6
    role: context
  - path: research/discovery/20261013T050519Z-structurally-constrained-recurrent-neural-network.json
    sha256: 80bc8455eff4c55a187dee41fe973d40520bd598a5e61c6a7fca3b6c4833aebf
    role: context
  - path: research/discovery/scrn-boundaries.py
    sha256: 0e54f2038bd89dbb3cef4dad37b51ea07372e48c2b5139d35b6ce75bec129895
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
- target_id: AIMech:StructurallyConstrainedRecurrentNeuralNetwork
  path: data/curated/StructurallyConstrainedRecurrentNeuralNetwork.yaml
  label: Structurally constrained recurrent neural network
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/StructurallyConstrainedRecurrentNeuralNetwork.yaml
    role: maintained
scope:
  description: All fields of the maintained SCRN, complete primary v2 paper and declared
    pinned author-file inspection.
  selection: 'Exact maintained ID: AIMech:StructurallyConstrainedRecurrentNeuralNetwork'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:StructurallyConstrainedRecurrentNeuralNetwork
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not full scientific rereview.
  - target: Other author files, uninspected rnn.lua lines and dependencies
    reason: Six selected author files and only rnn.lua230–285 were read; no complete
      repository/dependency or executable runtime audit.
  - target: Training, benchmark reproduction and universal guarantees
    reason: No source execution, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:StructurallyConstrainedRecurrentNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 210.81s (0:03:30)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 573 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 228 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 228,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:StructurallyConstrainedRecurrentNeuralNetwork
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
  - AIMech:StructurallyConstrainedRecurrentNeuralNetwork
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
  - AIMech:StructurallyConstrainedRecurrentNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed SCRN trace and parameterization boundaries
  command: python3 research/discovery/scrn-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:StructurallyConstrainedRecurrentNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: '{"trace_unrolled": 2.25, "permutation_outputs": [1.75, 1.25], "carry_after_100_steps":
    0.0059205292203339975, "paper_preactivation": 12.419999999999998, "unchanged_lagged_preactivation":
    13.02, "transformed_lagged_preactivation": 12.42, "largest_bounded_context": 2.05,
    "scope": "Constructed scalar trace and affine-substitution checks only; no Torch
    or training execution."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T050519Z-structurally-constrained-recurrent-neural-network.json
  accessed_at: '2026-10-13T05:05:30Z'
  support: supports
  summary: Compared all 442 pinned AIO and 572 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    7, 0, 0 lines. The current matches were inspected as the preceding IRNN report’s
    SCRN source/lead notes and one semantic-search expression, not an existing maintained
    record. The semantic search covers 47 AIO rows and 128 native definitions; preceding
    44 AIO and118 native rows were verified unchanged and the additional three activation-function
    rows plus ten native definitions read. Sigmoid-based belief networks, diagonal
    state-space models and unrelated diagonal clustering/representation objectives
    do not match this coupled recurrent architecture. Four full annotated AIO node/edge/generated
    contexts and four full adjacent native records were inspected. RecurrentNeuralNetwork
    is the broader architecture category and SigmoidFunction is a related component.
    SimpleRNNLayer lacks this coupled context structure; EchoStateNetwork’s sparse
    recurrent/output-learning definition does not establish equivalence or a superclass
    relation for jointly learned fast/input/context-output parameters. Unlike IRNN
    initialization, SCRN retains structural zero and diagonal context blocks. Fixed
    and adaptive per-unit decay configurations are preserved within the record, as
    are current-versus-lagged context conventions.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T05:05:30Z'
  support: supports
  summary: Forty-seven AIO and128 native semantic rows were read or verified unchanged.
    Four full AIO node/edge/generated contexts and four full native records support
    identity distinctions. Both mapping YAMLs reread after capture. RecurrentNeuralNetwork
    is the broader architecture category; SigmoidFunction is a related component.
    Generic layer and echo-state definitions do not establish the defining coupled
    context structure.
- evidence_id: mikolov2015
  kind: primary_source
  reference: https://arxiv.org/pdf/1412.7753v2
  locator: Complete nine-page v2 paper visually read; defining Equations4–8 on pp4–5
    reread after capture.
  accessed_at: '2026-10-13T04:28:03Z'
  snapshot_sha256: 5326cbf36d998a17720bbe2801779352751b0d35fac61afdf6a81e26836efa50
  support: supports
  summary: April16,2015 v2; accepted-as-ICLR2015-workshop header. All nine printed/PDF
    pages, including Figure1, four tables, eight equations and references, visually
    inspected.
- evidence_id: authorgraph
  kind: primary_source
  reference: https://raw.githubusercontent.com/facebookarchive/SCRNNs/75582d4371d72dc789929b7076777bd5b3e38f1b/mfactory.lua
  locator: Complete mfactory.lua read; lines150–221 reread after capture.
  accessed_at: '2026-10-13T04:30:07Z'
  snapshot_sha256: ff3e00fddb9ff5bc07170e7f0dd5621d466351f45adf26378355d38cb4dd8d81
  support: supports
  summary: Pinned author commit 75582d4371d72dc789929b7076777bd5b3e38f1b (2018-01-03T00:15:58Z).
    Complete file read; SCRN graph at lines150–221. Static inspection only; no Torch/runtime
    execution.
- evidence_id: authorinit
  kind: primary_source
  reference: https://raw.githubusercontent.com/facebookarchive/SCRNNs/75582d4371d72dc789929b7076777bd5b3e38f1b/util.lua
  locator: Complete util.lua read; orthInit/initSCRNN reread after capture.
  accessed_at: '2026-10-13T04:31:22Z'
  snapshot_sha256: d578f925f7cac1396c2694d30f28d4758a1956b9bfadfd6fe64113cf48ff2cd4
  support: supports
  summary: Pinned author commit 75582d4371d72dc789929b7076777bd5b3e38f1b (2018-01-03T00:15:58Z).
    Complete file read; orthInit and initSCRNN checked. Static inspection only; no
    Torch/runtime execution.
- evidence_id: authortrain
  kind: primary_source
  reference: https://raw.githubusercontent.com/facebookarchive/SCRNNs/75582d4371d72dc789929b7076777bd5b3e38f1b/scrnn.lua
  locator: Complete scrnn.lua read; zero initial momentum and suppression/update call
    order reread after capture.
  accessed_at: '2026-10-13T04:30:07Z'
  snapshot_sha256: 41a366ac2291037eeea78be69ddce8765af9f4fd9a7db219ce416e615f9243ba
  support: supports
  summary: Pinned author commit 75582d4371d72dc789929b7076777bd5b3e38f1b (2018-01-03T00:15:58Z).
    Complete file read; zero initial momentum, gradient suppression and call order
    checked. Static inspection only; no Torch/runtime execution.
- evidence_id: authorupdate
  kind: primary_source
  reference: https://raw.githubusercontent.com/facebookarchive/SCRNNs/75582d4371d72dc789929b7076777bd5b3e38f1b/rnn.lua
  locator: Only rnn.lua230–285 read; updateParams247–255 reread after capture.
  accessed_at: '2026-10-13T04:31:22Z'
  snapshot_sha256: 0974765546e116c887c263a9e267c61c36c4f8436022214d849c9af275275f6c
  support: supports
  summary: Pinned author commit 75582d4371d72dc789929b7076777bd5b3e38f1b (2018-01-03T00:15:58Z).
    Only lines230–285 inspected; updateParams at247–255. Remaining file not read.
    Static inspection only; no Torch/runtime execution.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/scrn-boundaries.py
  accessed_at: '2026-10-13T05:06:08Z'
  snapshot_sha256: 0e54f2038bd89dbb3cef4dad37b51ea07372e48c2b5139d35b6ce75bec129895
  support: supports
  summary: Constructed trace expansion, permutation, decaying derivative and scalar
    bounded-input checks accompany exact affine substitution between current- and
    previous-context parameterizations. No Torch, training, benchmark or whole-network
    stability verification.
assessments:
- assessment_id: identity
  area: identity
  topic: Coupled nonlinear recurrence and constrained linear context
  outcome: supported
  target_ids:
  - AIMech:StructurallyConstrainedRecurrentNeuralNetwork
  evidence_ids:
  - identity
  - mikolov2015
  - authorgraph
  summary: Retain SCRN as a distinct DRAFT architecture.
  details: No normalized maintained identity matched. All current ignored-inclusive
    matches were the preceding report’s SCRN candidate/URL and one semantic expression,
    read completely. A persistent zero hidden-to-context block and scalar/diagonal
    linear context distinguish SCRN from IRNN initialization, generic sigmoid belief
    networks, diagonal state-space families and unrelated diagonal objectives.
- assessment_id: mapping
  area: grounding
  topic: Broader recurrent architecture and component sigmoid
  outcome: supported
  target_ids:
  - AIMech:StructurallyConstrainedRecurrentNeuralNetwork
  evidence_ids:
  - mapping
  - mikolov2015
  - authorgraph
  summary: Both mapping directions are supported.
  details: SCRN is a recurrent network, supporting a broader AIO recurrent architecture
    mapping. The fast-state component uses the named sigmoid operation and pinned
    nn.Sigmoid, supporting related SigmoidFunction. The whole architecture is neither
    a mathematical-function subclass nor identified by the generic SimpleRNN layer
    or sparse echo-state target.
- assessment_id: linear-context-and-fast-state
  area: evidence
  topic: linear-context-and-fast-state
  outcome: supported
  target_ids:
  - AIMech:StructurallyConstrainedRecurrentNeuralNetwork
  evidence_ids:
  - mikolov2015
  - authorgraph
  - calculation
  summary: Supported with explicit structural and source-convention boundaries.
  details: Equations4–6 give a linear scalar-decay context, nonlinear fast recurrence
    and joint output. The context has no fast-state feedback. The record clearly assigns
    current-context h to the paper formulation and warns that the pinned graph uses
    lagged context.
- assessment_id: persistent-structure-and-adaptive-variant
  area: evidence
  topic: persistent-structure-and-adaptive-variant
  outcome: supported
  target_ids:
  - AIMech:StructurallyConstrainedRecurrentNeuralNetwork
  evidence_ids:
  - mikolov2015
  - calculation
  summary: Supported with explicit structural and source-convention boundaries.
  details: Equations7–8 identify structural zero/diagonal blocks and optional learned
    per-coordinate sigmoid decays. These parameters are shared through time rather
    than input-dependent gates. The adaptive configuration is preserved within the
    architecture, not conflated with unconstrained dense initialization or claimed
    as implemented in the selected fixed-code path.
- assessment_id: trace-memory-and-boundaries
  area: evidence
  topic: trace-memory-and-boundaries
  outcome: supported
  target_ids:
  - AIMech:StructurallyConstrainedRecurrentNeuralNetwork
  evidence_ids:
  - mikolov2015
  - calculation
  summary: Supported with explicit structural and source-convention boundaries.
  details: Expanding the scalar recurrence yields geometric recency weights and alpha^k
    direct carry. It is not permutation invariant or unlimited exact memory. Convex-combination
    bounds require bounded embeddings and a fixed scalar in(0,1); no bound on the
    separate fast Jacobian follows.
- assessment_id: current-versus-lagged-context
  area: evidence
  topic: current-versus-lagged-context
  outcome: supported
  target_ids:
  - AIMech:StructurallyConstrainedRecurrentNeuralNetwork
  evidence_ids:
  - mikolov2015
  - authorgraph
  - calculation
  summary: Supported with explicit structural and source-convention boundaries.
  details: Visual paper Equation5 uses s_t while mfactory.lua193 uses prev_hid_slow
    despite the nearby comment. Substituting Equation4 yields coupling alpha*P and
    input A+(1-alpha)*P*B. The record preserves equivalence of parameterized forms
    with transformation rather than identity at unchanged raw parameters or optimization.
- assessment_id: pinned-fixed-context-implementation
  area: evidence
  topic: pinned-fixed-context-implementation
  outcome: supported
  target_ids:
  - AIMech:StructurallyConstrainedRecurrentNeuralNetwork
  evidence_ids:
  - authorgraph
  - authorinit
  - authortrain
  - authorupdate
  - calculation
  summary: Supported with explicit structural and source-convention boundaries.
  details: The inspected initializer uses zero off-diagonal slow weights and diagonal1-semb_scale.
    Builder scales slow embedding; zeroSomeGradients clears slow recurrent gradients
    before the shown update. With fresh zero momentum and the stated update path the
    slow matrix remains fixed. The record explicitly excludes arbitrary loaded optimizer
    state, other mutations, dependencies and an adaptive-Q implementation claim.
- assessment_id: evaluation-and-finite-memory
  area: evidence
  topic: evaluation-and-finite-memory
  outcome: supported
  target_ids:
  - AIMech:StructurallyConstrainedRecurrentNeuralNetwork
  evidence_ids:
  - mikolov2015
  - calculation
  summary: Supported with explicit structural and source-convention boundaries.
  details: PTB and Text8 use selected capacities, BPTT settings and output parameterizations.
    Text8 reporting is a development split, not asserted independent test. Learned
    decays have conditional benefits; the conclusion acknowledges finite memory. No
    numeric benchmark, unconditional LSTM advantage or runtime replication is imported.
- assessment_id: constructed-boundaries
  area: consistency
  topic: Trace recurrence and parameter transformation
  outcome: supported
  target_ids:
  - AIMech:StructurallyConstrainedRecurrentNeuralNetwork
  evidence_ids:
  - mikolov2015
  - authorgraph
  - calculation
  summary: Constructed algebra confirms the distinctions.
  details: Trace expansion agrees at2.25; reversing inputs yields1.75 versus1.25,
    showing recency order matters. A .95 direct carry is about.00592 after100 steps.
    Paper preactivation12.42 differs from unchanged lagged13.02, while the transformed
    lagged form restores12.42. A bounded scalar context stays within its assumed input/initial
    bound. No training or complete gradient theorem is claimed.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record and bounded code inspection
  outcome: supported
  target_ids:
  - AIMech:StructurallyConstrainedRecurrentNeuralNetwork
  evidence_ids:
  - identity
  - mapping
  - mikolov2015
  - authorgraph
  - authorinit
  - authortrain
  - authorupdate
  - calculation
  summary: All maintained fields inspected; DRAFT remains.
  details: Read stable ID/name/aliases, architecture kind, definition/citations, identity
    context, six claims and source locators, five source identities/versions/access/hashes,
    AIO pin, mappings, six limitations and actual curation times. Source/context/capture
    hashes and exact report mirror agree. Full-paper and selected-file inspection
    are distinguished from partial rnn.lua scope and unexecuted dependencies. No actionable
    record defect identified.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue manufactured
  for a clean record review.
- One new DRAFT concept, yielding 573 native and 442 unchanged generated records.
  The 758-entry main frontier retains 482 pending and 57 partly addressed cohorts;
  discovery is incomplete.
- The source evaluations use specific capacities, splits and training choices. No
  current best performance, unconditional LSTM advantage or independent scientific
  approval is asserted.
- All nine primary paper pages and six selected author files were read completely;
  only lines230–285 of rnn.lua were inspected. No full repository/dependency audit,
  Torch execution, training or empirical replication.
- Only the isolated recovery checkout is changed; original-checkout synchronization
  and old round141 cleanup remain pending explicit approval after automatic review
  rejection.
related_reviews: []
links: []
tags:
- native-concepts
- optimization
- recurrent-architectures
- self-review
- discovery-ongoing
```
