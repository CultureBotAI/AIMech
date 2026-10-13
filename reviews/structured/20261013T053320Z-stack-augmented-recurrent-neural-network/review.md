# Scientific author self-review of Stack RNN

- Review: 20261013T053320Z-stack-augmented-recurrent-neural-network
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T05:26:05Z
- Finished UTC: 2026-10-13T05:33:20Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Stack RNN as a distinct DRAFT architecture with a broader recurrent-network mapping. All six claims and fields have support with continuous-memory, capacity, hard-action and conditional evaluation boundaries. The saved arithmetic-qualification finding is resolved; no additional actionable defect found. No author code or training execution occurred.

## Scope And Provenance

All fields of the maintained Stack RNN, complete conference paper and declared pinned author-file inspection.

Selection: Exact maintained ID: AIMech:StackAugmentedRecurrentNeuralNetwork
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 80fc2f8b95e90c0601a598d593dad73d2ecedb99.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:StackAugmentedRecurrentNeuralNetwork | data/curated/StackAugmentedRecurrentNeuralNetwork.yaml | maintained | Stack-augmented recurrent neural network |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:StackAugmentedRecurrentNeuralNetwork | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 163.03s (0:02:43)<br>Checked 442 record(s); 0 failed.<br>Checked 574 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 230 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 230,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:StackAugmentedRecurrentNeuralNetwork | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:StackAugmentedRecurrentNeuralNetwork | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:StackAugmentedRecurrentNeuralNetwork | Exited 0 without output. |
| Constructed stack-memory boundaries | passed | True | AIMech:StackAugmentedRecurrentNeuralNetwork | {"finite_logits": [0.0, -1000.0], "binary64_softmax": [1.0, 0.0], "push": [0.9, 0.2, 0.7], "mixed_update": [0.8, -0.4, -0.15000000000000002], "overflow_then_pop": [0.2, 0.7, -1.0], "nonlinear_controller_of_mean": 0.9608342772032357, "mean_of_discrete_controllers": 0.9580394152621327, "tied_softmax_under_any_positive_scale": [0.5, 0.5], "scope": "Elementary finite-capacity operator and nonlinear-mixture calculations; no training, full gradient audit or author source execution."} |

## Scientific And Domain Assessments

### Neural recurrent controller with external stack operations

identity: supported. Targets: AIMech:StackAugmentedRecurrentNeuralNetwork.

Retain Stack RNN as a distinct DRAFT architecture.

No normalized maintained identity matched. Ignored-inclusive source/lead matches were read. Push/pop external memory differs from layered RNN-cell composition, ensemble stacking, beam-stack search and fixed linear context. List-memory directional movement remains a separate topology lead; read depth, count, no-op and recurrence choices stay within the stack record.

### Broader recurrent architecture

grounding: supported. Targets: AIMech:StackAugmentedRecurrentNeuralNetwork.

The broader mapping is supported.

The recurrent controller and evolving external memory fit the pinned recurrent architecture definition. Neither a generic stack-of-layers target, LLM-only memory scope nor the pinned feedforward/spiking NTM target establishes exact equivalence or an appropriate broader mapping.

### controller-and-stack-transition

evidence: supported. Targets: AIMech:StackAugmentedRecurrentNeuralNetwork.

Supported with memory, implementation and evaluation qualifications.

Equations3–6 and forward code agree on reading old top entries, softmax actions, sigmoid proposal, push/pop shifts and optional no-op. The -1 sentinel and capacity/read-depth choices are stated without implying one universal benchmark configuration.

### continuous-versus-discrete-state

evidence: supported. Targets: AIMech:StackAugmentedRecurrentNeuralNetwork.

Supported with memory, implementation and evaluation qualifications.

The memory update is an affine blend of proposed transitions. One-hot behavior has capacity and sentinel qualifications. Subsequent nonlinear controller outputs need not equal expectations of discrete trajectories; no stochastic sampling semantics is imported.

### capacity-paper-and-code

evidence: supported. Targets: AIMech:StackAugmentedRecurrentNeuralNetwork.

Supported with memory, implementation and evaluation qualifications.

Paper allows growing depth, while constructor fixes stack_capacity. Forward push loses a full bottom entry and pop inserts the sentinel. The record explicitly distinguishes theoretical expandable memory, bounded implementation and physical/numerical limits.

### hard-actions-versus-rounding

evidence: supported. Targets: AIMech:StackAugmentedRecurrentNeuralNetwork.

Supported with memory, implementation and evaluation qualifications.

The pinned ishard path selects a maximal action with first-index ties. Paper rounding additionally sharpens, refines and prunes. In ideal real arithmetic finite softmax weights are not hard selection and tied maxima remain mixed under scaling alone. Corrected text explicitly permits finite-precision zero/one outputs; the constructed binary64 example is not an execution of the author code.

### multiple-stacks-and-recurrence

evidence: supported. Targets: AIMech:StackAugmentedRecurrentNeuralNetwork.

Supported with memory, implementation and evaluation qualifications.

Shared hidden state couples stack controllers. The toy R=0 choice is not inherent to all models; paper language modeling uses hidden recurrence and code exposes modes. List left/right/insert topology is distinguished from stack push/pop.

### optimization-and-evaluation-boundaries

evidence: supported. Targets: AIMech:StackAugmentedRecurrentNeuralNetwork.

Supported with memory, implementation and evaluation qualifications.

The paper reports nonconvex controller-learning difficulty, restarts and long-sequence numerical imprecision. Task-specific supervision, predictable-token evaluation, sequence lengths and conditional language-model results do not support universal algorithm learning or an independent benchmark claim.

### Stack transitions, finite loss and soft/hard distinctions

consistency: supported. Targets: AIMech:StackAugmentedRecurrentNeuralNetwork.

Constructed algebra confirms the distinctions.

Pure push and a half push/pop blend produce the specified different states. A full finite stack loses its bottom after push/pop. Nonlinear propagation of a blended state differs from mean propagation of separate branches. Equal maximal logits remain tied under sharpening. These are constructed checks, not training or complete backward-code certification.

### Complete maintained record and bounded implementation reading

provenance: supported. Targets: AIMech:StackAugmentedRecurrentNeuralNetwork.

All maintained fields inspected; DRAFT remains.

Read ID/name/alias, architecture kind, definition/citations, identity context, six claims and locators, three source identities/versions/access/hashes, AIO pin, mapping, six limitations and actual curation times. Source/context/capture hashes and exact report mirror agree. All-paper and selected-file reading are distinguished from uninspected supplement, drivers and dependencies. No actionable record defect identified.

### Ideal versus finite-precision softmax

evidence: supported. Targets: AIMech:StackAugmentedRecurrentNeuralNetwork.

Saved F1 is resolved.

The corrected statement explicitly distinguishes ideal real positivity from possible floating-point underflow or rounding. The maintained example computes max-shift softmax for finite [0,-1000] as [1,0] in Python binary64, without running or certifying C++ author code. Three source records, exact report mirror and actual EDIT history agree.

## Findings

### F1: Qualify finite-softmax claims by arithmetic model

minor / resolved / confirmed; issue key: stack-rnn-finite-softmax-qualification.

The hard-actions-versus-rounding claim says finite sharpening remains soft without specifying ideal real arithmetic. Floating-point exponentiation can underflow at finite logit gaps; the constructed binary64 example [0,-1000] yields [1,0]. The pinned Softmax::forward uses max-shift exponentiation and normalization. Preserve the mathematical distinction from hard argmax while allowing finite-precision zero/one outputs; do not certify author-runtime behavior.

Disposition: The corrected maintained claim explicitly limits strict finite-softmax positivity to ideal real arithmetic, permits finite-precision zero/one outputs and distinguishes the constructed binary64 example from author-code execution. The pinned nonlinearity source, report mirror, calculation and EDIT history were updated; corrected bytes were freshly captured and reread and required post-edit gates passed.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T052159Z-stack-augmented-recurrent-neural-network.json | supports | Compared all 442 pinned AIO and 573 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 6, 0, 0 lines. All matches were inspected as source/candidate entries in the preceding SCRN discovery report, not an existing maintained Stack RNN record. Semantic matching inspected 54 AIO and134 native definitions, with unchanged preceding rows verified and new matches read. Four full annotated AIO node/edge/generated contexts and four full native records were inspected. StackedRNNCellsLayer describes layer composition, not external push/pop memory; MemoryAugmentedLLM requires large-language-model scope not inherent to this architecture; the pinned NeuralTuringMachineNetwork feedforward/spiking description does not identify stack addressing. None establishes an exact or broader match. RecurrentNeuralNetwork supplies the broader architecture mapping. Beam-stack search and ensemble stacking have different identity and operations. The paper list-memory topology remains a separate lead; stack count, read depth, no-op, recurrence and capacity configurations stay within this record. |
| mapping | sources/aio/aio.json | supports | Fifty-four AIO and134 native semantic rows read or verified unchanged; four full AIO node/edge/generated contexts and four full native records inspected. RecurrentNeuralNetwork is broader. StackedRNNCellsLayer is layer composition; MemoryAugmentedLLM requires a different model scope; the pinned NTM description does not establish stack-controller identity or an appropriate superclass. |
| joulin2015 | https://proceedings.neurips.cc/paper_files/paper/2015/file/26657d5ff9020d2abefe558796b99584-Paper.pdf; Complete nine-page conference paper visually read; defining memory operations and rounding on pp4–5 reread after capture. | supports | NeurIPS2015 proceedings, volume28. All nine printed/PDF pages, Figures1–3, Tables1–4, Equations1–6 and references visually inspected. |
| authorcode | https://raw.githubusercontent.com/facebookarchive/Stack-RNN/95efe9031aa473e3b0b1750f5e055aac5a2b2599/StackRNN.h; Complete 651-line StackRNN.h read; allocation and forward41–84/125–252 reread after capture. | supports | Pinned author commit 95efe9031aa473e3b0b1750f5e055aac5a2b2599 (2015-06-14T19:32:44Z). Complete 651-line header read, including forward, backward, allocation and persistence. Static inspection only; no compilation or runtime execution. |
| authornonlinearity | https://raw.githubusercontent.com/facebookarchive/Stack-RNN/95efe9031aa473e3b0b1750f5e055aac5a2b2599/Nonlinearity.h; Complete Nonlinearity.h read and reread after corrected capture; Softmax::forward exponentiation and normalization checked without executing source. | supports | Pinned author commit 95efe9031aa473e3b0b1750f5e055aac5a2b2599 (2015-06-14T19:32:44Z). Complete file inspected; Softmax::forward uses max-shift exponentiation and normalization. Static inspection only; no author source execution. |
| calculation | research/discovery/stack-rnn-boundaries.py | supports | Constructed pure stack transitions, finite-capacity loss, soft mixtures, nonlinear mean propagation and tied softmax sharpening. No author source compilation, training, benchmark or complete backward verification. The binary64 finite-logit example distinguishes numerical underflow from ideal-real softmax positivity; it does not execute the pinned C++ implementation. |
| predecessor | reviews/structured/20261013T052406Z-stack-rnn-finite-softmax-qualification-open/review.yaml | supports | Saved partial author review identified the missing arithmetic-model qualification. Current record/report/calculation were checked against its acceptance criteria. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. One confirmed minor finding is resolved; issue242 tracks the correction.
- One new DRAFT concept, yielding 574 native and 442 unchanged generated records. The 759-entry main frontier retains 482 pending and 57 partly addressed cohorts; discovery is incomplete.
- Source tasks, sequence lengths, supervision and tuning constrain the reported generalization. No unlimited exact memory, universal LSTM replacement or independently verified performance claim is made.
- All nine primary conference-paper pages and three pinned author files were read completely. No supplement, task driver or full dependency audit, compilation, training or empirical replication.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T053320Z-stack-augmented-recurrent-neural-network
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Stack RNN
started_at: '2026-10-13T05:26:05Z'
finished_at: '2026-10-13T05:33:20Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged identity/mapping, continuous memory semantics,
    capacity loss, hard-action versus paper-rounding procedures and conditional evaluation.
    This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Stack RNN as a distinct DRAFT architecture with a broader recurrent-network
  mapping. All six claims and fields have support with continuous-memory, capacity,
  hard-action and conditional evaluation boundaries. The saved arithmetic-qualification
  finding is resolved; no additional actionable defect found. No author code or training
  execution occurred.
source:
  git_revision: 80fc2f8b95e90c0601a598d593dad73d2ecedb99
  state: working_tree
  inputs:
  - path: data/aio/MemoryAugmentedLLM.yaml
    sha256: 8727073cb355b965f54a2f0e58997f862f6b734c9143511008c26f9d31a965fd
    role: context
  - path: data/aio/NeuralTuringMachineNetwork.yaml
    sha256: bb483a9f90d767bcae50856c6084f31fe855d510d352419a5130fa4fc036be79
    role: context
  - path: data/aio/RecurrentNeuralNetwork.yaml
    sha256: 1ebef94d2014e9a19d4bb3ed0fed6c5d77098a5a44e00e2cbd1cfe682dfcd892
    role: context
  - path: data/aio/StackedRNNCellsLayer.yaml
    sha256: e2fdefc9152c3607a8bfc70334431ce65a3d82ad75760fd0f747c42b5c47eee9
    role: context
  - path: data/curated/BeamStackSearch.yaml
    sha256: 161a74d1afbe844b276989df5e068268ffa239e62799523221b56a626b4f4861
    role: context
  - path: data/curated/IdentityInitializedRecurrentNeuralNetwork.yaml
    sha256: cfa1543605f0046f0c2bbbffc294d7cead0a444f1db5cb955bdf8971a7ae9d62
    role: context
  - path: data/curated/StackAugmentedRecurrentNeuralNetwork.yaml
    sha256: f544aaabf56c79e2d2a66c37c3e357854ee751d00e05f890a4324f366e52055d
    role: target
  - path: data/curated/Stacking.yaml
    sha256: 5271ce4094a5beec8dc87500e64d9c779ec4aec9bbcb20d0efcc22d26e62706b
    role: context
  - path: data/curated/StructurallyConstrainedRecurrentNeuralNetwork.yaml
    sha256: 03df44109ede633bd0f41cf2b7b355ac0708ff53411e5ef1a9f69d131380f6bc
    role: context
  - path: research/discovery/20261013T052159Z-stack-augmented-recurrent-neural-network.json
    sha256: 98a0966c92f5e9bda2308206f2e2958e3646e2217434fdebff1319ed0c7dfe02
    role: context
  - path: research/discovery/stack-rnn-boundaries.py
    sha256: a6600e3938dff3ef0ac10d75620a62431a39aaf605ea34568af870264a46f3db
    role: context
  - path: reviews/structured/20261013T052406Z-stack-rnn-finite-softmax-qualification-open/review.md
    sha256: 2a7dade96a814e05d248fbaeaabc42008873add5cee81751ec26a1f0f15b0de1
    role: context
  - path: reviews/structured/20261013T052406Z-stack-rnn-finite-softmax-qualification-open/review.yaml
    sha256: a77a39057fd38b4beaeb523285c2eb68e7be59ce3cb240d44773f8b65244c608
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
- target_id: AIMech:StackAugmentedRecurrentNeuralNetwork
  path: data/curated/StackAugmentedRecurrentNeuralNetwork.yaml
  label: Stack-augmented recurrent neural network
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/StackAugmentedRecurrentNeuralNetwork.yaml
    role: maintained
scope:
  description: All fields of the maintained Stack RNN, complete conference paper and
    declared pinned author-file inspection.
  selection: 'Exact maintained ID: AIMech:StackAugmentedRecurrentNeuralNetwork'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:StackAugmentedRecurrentNeuralNetwork
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not full scientific rereview.
  - target: Supplement, task drivers and other dependencies
    reason: Three selected author files read completely; no complete repository/dependency
      or executable runtime audit.
  - target: Training, benchmark reproduction and universal guarantees
    reason: No source execution, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:StackAugmentedRecurrentNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 163.03s (0:02:43)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 574 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 230 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 230,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:StackAugmentedRecurrentNeuralNetwork
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
  - AIMech:StackAugmentedRecurrentNeuralNetwork
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
  - AIMech:StackAugmentedRecurrentNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed stack-memory boundaries
  command: python3 research/discovery/stack-rnn-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:StackAugmentedRecurrentNeuralNetwork
  exit_code: 0
  expected_exit_code: 0
  summary: '{"finite_logits": [0.0, -1000.0], "binary64_softmax": [1.0, 0.0], "push":
    [0.9, 0.2, 0.7], "mixed_update": [0.8, -0.4, -0.15000000000000002], "overflow_then_pop":
    [0.2, 0.7, -1.0], "nonlinear_controller_of_mean": 0.9608342772032357, "mean_of_discrete_controllers":
    0.9580394152621327, "tied_softmax_under_any_positive_scale": [0.5, 0.5], "scope":
    "Elementary finite-capacity operator and nonlinear-mixture calculations; no training,
    full gradient audit or author source execution."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T052159Z-stack-augmented-recurrent-neural-network.json
  accessed_at: '2026-10-13T05:26:05Z'
  support: supports
  summary: Compared all 442 pinned AIO and 573 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    6, 0, 0 lines. All matches were inspected as source/candidate entries in the preceding
    SCRN discovery report, not an existing maintained Stack RNN record. Semantic matching
    inspected 54 AIO and134 native definitions, with unchanged preceding rows verified
    and new matches read. Four full annotated AIO node/edge/generated contexts and
    four full native records were inspected. StackedRNNCellsLayer describes layer
    composition, not external push/pop memory; MemoryAugmentedLLM requires large-language-model
    scope not inherent to this architecture; the pinned NeuralTuringMachineNetwork
    feedforward/spiking description does not identify stack addressing. None establishes
    an exact or broader match. RecurrentNeuralNetwork supplies the broader architecture
    mapping. Beam-stack search and ensemble stacking have different identity and operations.
    The paper list-memory topology remains a separate lead; stack count, read depth,
    no-op, recurrence and capacity configurations stay within this record.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T05:26:05Z'
  support: supports
  summary: Fifty-four AIO and134 native semantic rows read or verified unchanged;
    four full AIO node/edge/generated contexts and four full native records inspected.
    RecurrentNeuralNetwork is broader. StackedRNNCellsLayer is layer composition;
    MemoryAugmentedLLM requires a different model scope; the pinned NTM description
    does not establish stack-controller identity or an appropriate superclass.
- evidence_id: joulin2015
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper_files/paper/2015/file/26657d5ff9020d2abefe558796b99584-Paper.pdf
  locator: Complete nine-page conference paper visually read; defining memory operations
    and rounding on pp4–5 reread after capture.
  accessed_at: '2026-10-13T04:41:24Z'
  snapshot_sha256: 8c9bbbbf4e919d877a24b48b0859a13bcdc36ac8ecad3d8cd502c510a08a8f40
  support: supports
  summary: NeurIPS2015 proceedings, volume28. All nine printed/PDF pages, Figures1–3,
    Tables1–4, Equations1–6 and references visually inspected.
- evidence_id: authorcode
  kind: primary_source
  reference: https://raw.githubusercontent.com/facebookarchive/Stack-RNN/95efe9031aa473e3b0b1750f5e055aac5a2b2599/StackRNN.h
  locator: Complete 651-line StackRNN.h read; allocation and forward41–84/125–252
    reread after capture.
  accessed_at: '2026-10-13T04:44:29Z'
  snapshot_sha256: 409c1ac526dc566810f56459236afbe57e3643f02bd783a476b076d9b09361d0
  support: supports
  summary: Pinned author commit 95efe9031aa473e3b0b1750f5e055aac5a2b2599 (2015-06-14T19:32:44Z).
    Complete 651-line header read, including forward, backward, allocation and persistence.
    Static inspection only; no compilation or runtime execution.
- evidence_id: authornonlinearity
  kind: primary_source
  reference: https://raw.githubusercontent.com/facebookarchive/Stack-RNN/95efe9031aa473e3b0b1750f5e055aac5a2b2599/Nonlinearity.h
  locator: Complete Nonlinearity.h read and reread after corrected capture; Softmax::forward
    exponentiation and normalization checked without executing source.
  accessed_at: '2026-10-13T04:44:29Z'
  snapshot_sha256: b011fac8894a99a37cbeafcd21467ebaab00911e63acd7edf9a07f515f397cb7
  support: supports
  summary: Pinned author commit 95efe9031aa473e3b0b1750f5e055aac5a2b2599 (2015-06-14T19:32:44Z).
    Complete file inspected; Softmax::forward uses max-shift exponentiation and normalization.
    Static inspection only; no author source execution.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/stack-rnn-boundaries.py
  accessed_at: '2026-10-13T05:26:47Z'
  snapshot_sha256: a6600e3938dff3ef0ac10d75620a62431a39aaf605ea34568af870264a46f3db
  support: supports
  summary: Constructed pure stack transitions, finite-capacity loss, soft mixtures,
    nonlinear mean propagation and tied softmax sharpening. No author source compilation,
    training, benchmark or complete backward verification. The binary64 finite-logit
    example distinguishes numerical underflow from ideal-real softmax positivity;
    it does not execute the pinned C++ implementation.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261013T052406Z-stack-rnn-finite-softmax-qualification-open/review.yaml
  accessed_at: '2026-10-13T05:26:47Z'
  snapshot_sha256: a77a39057fd38b4beaeb523285c2eb68e7be59ce3cb240d44773f8b65244c608
  support: supports
  summary: Saved partial author review identified the missing arithmetic-model qualification.
    Current record/report/calculation were checked against its acceptance criteria.
assessments:
- assessment_id: identity
  area: identity
  topic: Neural recurrent controller with external stack operations
  outcome: supported
  target_ids:
  - AIMech:StackAugmentedRecurrentNeuralNetwork
  evidence_ids:
  - identity
  - joulin2015
  - authorcode
  summary: Retain Stack RNN as a distinct DRAFT architecture.
  details: No normalized maintained identity matched. Ignored-inclusive source/lead
    matches were read. Push/pop external memory differs from layered RNN-cell composition,
    ensemble stacking, beam-stack search and fixed linear context. List-memory directional
    movement remains a separate topology lead; read depth, count, no-op and recurrence
    choices stay within the stack record.
- assessment_id: mapping
  area: grounding
  topic: Broader recurrent architecture
  outcome: supported
  target_ids:
  - AIMech:StackAugmentedRecurrentNeuralNetwork
  evidence_ids:
  - mapping
  - joulin2015
  summary: The broader mapping is supported.
  details: The recurrent controller and evolving external memory fit the pinned recurrent
    architecture definition. Neither a generic stack-of-layers target, LLM-only memory
    scope nor the pinned feedforward/spiking NTM target establishes exact equivalence
    or an appropriate broader mapping.
- assessment_id: controller-and-stack-transition
  area: evidence
  topic: controller-and-stack-transition
  outcome: supported
  target_ids:
  - AIMech:StackAugmentedRecurrentNeuralNetwork
  evidence_ids:
  - joulin2015
  - authorcode
  - calculation
  summary: Supported with memory, implementation and evaluation qualifications.
  details: Equations3–6 and forward code agree on reading old top entries, softmax
    actions, sigmoid proposal, push/pop shifts and optional no-op. The -1 sentinel
    and capacity/read-depth choices are stated without implying one universal benchmark
    configuration.
- assessment_id: continuous-versus-discrete-state
  area: evidence
  topic: continuous-versus-discrete-state
  outcome: supported
  target_ids:
  - AIMech:StackAugmentedRecurrentNeuralNetwork
  evidence_ids:
  - joulin2015
  - authorcode
  - calculation
  summary: Supported with memory, implementation and evaluation qualifications.
  details: The memory update is an affine blend of proposed transitions. One-hot behavior
    has capacity and sentinel qualifications. Subsequent nonlinear controller outputs
    need not equal expectations of discrete trajectories; no stochastic sampling semantics
    is imported.
- assessment_id: capacity-paper-and-code
  area: evidence
  topic: capacity-paper-and-code
  outcome: supported
  target_ids:
  - AIMech:StackAugmentedRecurrentNeuralNetwork
  evidence_ids:
  - joulin2015
  - authorcode
  - calculation
  summary: Supported with memory, implementation and evaluation qualifications.
  details: Paper allows growing depth, while constructor fixes stack_capacity. Forward
    push loses a full bottom entry and pop inserts the sentinel. The record explicitly
    distinguishes theoretical expandable memory, bounded implementation and physical/numerical
    limits.
- assessment_id: hard-actions-versus-rounding
  area: evidence
  topic: hard-actions-versus-rounding
  outcome: supported
  target_ids:
  - AIMech:StackAugmentedRecurrentNeuralNetwork
  evidence_ids:
  - joulin2015
  - authorcode
  - authornonlinearity
  - calculation
  summary: Supported with memory, implementation and evaluation qualifications.
  details: The pinned ishard path selects a maximal action with first-index ties.
    Paper rounding additionally sharpens, refines and prunes. In ideal real arithmetic
    finite softmax weights are not hard selection and tied maxima remain mixed under
    scaling alone. Corrected text explicitly permits finite-precision zero/one outputs;
    the constructed binary64 example is not an execution of the author code.
- assessment_id: multiple-stacks-and-recurrence
  area: evidence
  topic: multiple-stacks-and-recurrence
  outcome: supported
  target_ids:
  - AIMech:StackAugmentedRecurrentNeuralNetwork
  evidence_ids:
  - joulin2015
  - authorcode
  - calculation
  summary: Supported with memory, implementation and evaluation qualifications.
  details: Shared hidden state couples stack controllers. The toy R=0 choice is not
    inherent to all models; paper language modeling uses hidden recurrence and code
    exposes modes. List left/right/insert topology is distinguished from stack push/pop.
- assessment_id: optimization-and-evaluation-boundaries
  area: evidence
  topic: optimization-and-evaluation-boundaries
  outcome: supported
  target_ids:
  - AIMech:StackAugmentedRecurrentNeuralNetwork
  evidence_ids:
  - joulin2015
  - calculation
  summary: Supported with memory, implementation and evaluation qualifications.
  details: The paper reports nonconvex controller-learning difficulty, restarts and
    long-sequence numerical imprecision. Task-specific supervision, predictable-token
    evaluation, sequence lengths and conditional language-model results do not support
    universal algorithm learning or an independent benchmark claim.
- assessment_id: constructed-boundaries
  area: consistency
  topic: Stack transitions, finite loss and soft/hard distinctions
  outcome: supported
  target_ids:
  - AIMech:StackAugmentedRecurrentNeuralNetwork
  evidence_ids:
  - joulin2015
  - authorcode
  - calculation
  summary: Constructed algebra confirms the distinctions.
  details: Pure push and a half push/pop blend produce the specified different states.
    A full finite stack loses its bottom after push/pop. Nonlinear propagation of
    a blended state differs from mean propagation of separate branches. Equal maximal
    logits remain tied under sharpening. These are constructed checks, not training
    or complete backward-code certification.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record and bounded implementation reading
  outcome: supported
  target_ids:
  - AIMech:StackAugmentedRecurrentNeuralNetwork
  evidence_ids:
  - identity
  - mapping
  - joulin2015
  - authorcode
  - authornonlinearity
  - calculation
  summary: All maintained fields inspected; DRAFT remains.
  details: Read ID/name/alias, architecture kind, definition/citations, identity context,
    six claims and locators, three source identities/versions/access/hashes, AIO pin,
    mapping, six limitations and actual curation times. Source/context/capture hashes
    and exact report mirror agree. All-paper and selected-file reading are distinguished
    from uninspected supplement, drivers and dependencies. No actionable record defect
    identified.
- assessment_id: resolved-finite-softmax
  area: evidence
  topic: Ideal versus finite-precision softmax
  outcome: supported
  target_ids:
  - AIMech:StackAugmentedRecurrentNeuralNetwork
  evidence_ids:
  - predecessor
  - authornonlinearity
  - calculation
  summary: Saved F1 is resolved.
  details: The corrected statement explicitly distinguishes ideal real positivity
    from possible floating-point underflow or rounding. The maintained example computes
    max-shift softmax for finite [0,-1000] as [1,0] in Python binary64, without running
    or certifying C++ author code. Three source records, exact report mirror and actual
    EDIT history agree.
findings:
- finding_id: F1
  issue_key: stack-rnn-finite-softmax-qualification
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Qualify finite-softmax claims by arithmetic model
  description: The hard-actions-versus-rounding claim says finite sharpening remains
    soft without specifying ideal real arithmetic. Floating-point exponentiation can
    underflow at finite logit gaps; the constructed binary64 example [0,-1000] yields
    [1,0]. The pinned Softmax::forward uses max-shift exponentiation and normalization.
    Preserve the mathematical distinction from hard argmax while allowing finite-precision
    zero/one outputs; do not certify author-runtime behavior.
  target_ids:
  - AIMech:StackAugmentedRecurrentNeuralNetwork
  field_paths:
  - claims[claim_id=hard-actions-versus-rounding].statement
  evidence_ids:
  - predecessor
  - authornonlinearity
  - calculation
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/StackAugmentedRecurrentNeuralNetwork.yaml
    role: maintained
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261013T052406Z-stack-rnn-finite-softmax-qualification-open
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/242
  disposition_reason: The corrected maintained claim explicitly limits strict finite-softmax
    positivity to ideal real arithmetic, permits finite-precision zero/one outputs
    and distinguishes the constructed binary64 example from author-code execution.
    The pinned nonlinearity source, report mirror, calculation and EDIT history were
    updated; corrected bytes were freshly captured and reread and required post-edit
    gates passed.
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. One confirmed
  minor finding is resolved; issue242 tracks the correction.
- One new DRAFT concept, yielding 574 native and 442 unchanged generated records.
  The 759-entry main frontier retains 482 pending and 57 partly addressed cohorts;
  discovery is incomplete.
- Source tasks, sequence lengths, supervision and tuning constrain the reported generalization.
  No unlimited exact memory, universal LSTM replacement or independently verified
  performance claim is made.
- All nine primary conference-paper pages and three pinned author files were read
  completely. No supplement, task driver or full dependency audit, compilation, training
  or empirical replication.
- Only the isolated recovery checkout is changed; original-checkout synchronization
  and old round141 cleanup remain pending explicit approval after automatic review
  rejection.
related_reviews:
- repository: CultureBotAI/AIMech
  review_id: 20261013T052406Z-stack-rnn-finite-softmax-qualification-open
  relationship: Resolves F1 after corrected-input capture, arithmetic/source comparison
    and publication checks.
links: []
tags:
- native-concepts
- recurrent-architectures
- self-review
- discovery-ongoing
```
