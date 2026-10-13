# Scientific author self-review of Neural GPU

- Review: 20261013T112202Z-neural-gpu
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T11:12:11Z
- Finished UTC: 2026-10-13T11:22:02Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Neural GPU is supported as a distinct DRAFT recurrent architecture. No unresolved findings in this author self-review; original and follow-up generalization claims remain configuration-bounded.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:NeuralGPU
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1ddc81b074ce61455a789440a8b80097a95737f0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:NeuralGPU | data/curated/NeuralGPU.yaml | maintained | Neural GPU |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:NeuralGPU | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 122.43s (0:02:02)<br>Checked 442 record(s); 0 failed.<br>Checked 609 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 276 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 272,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:NeuralGPU | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:NeuralGPU | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:NeuralGPU | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:NeuralGPU | {"averaged_outputs": 0.48201379003790845, "averaged_parameters": 0.7615941559557649, "candidate_weighted": 0.9840418038538805, "conv_shift": [1.0, 3.0, 3.0], "count10": {"cgru_parameters": 31248, "sequential_cgru_stages": 20, "updated_scalar_states": 19200}, "count20": {"cgru_parameters": 31248, "sequential_cgru_stages": 40, "updated_scalar_states": 76800}, "old_weighted": 0.9627642089923878, "reset_after": [0.6000000000000001, 2.4000000000000004], "reset_before": [1.8, 1.8], "shift_conv": [0.0, 3.0, 6.0]} |

## Scientific And Domain Assessments

### Neural GPU

identity: supported. Targets: AIMech:NeuralGPU.

Retain this distinct DRAFT architecture.

Grid state evolution is a distinct named architecture. Neither GPU hardware nor generic GRU, typed-graph message passing, episodic memory QA or an NTM controller defines the same concept. Follow-up trained configurations are evidence, not standalone identities.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:NeuralGPU.

The declared AIO mapping is supported.

RNN is a supported broad target for time-shared recurrence. GRU and convolutional layer are related components. The narrow visual definition of DeepConvolutionalNetwork and anomalous generic GRU parentage do not establish additional is-a assertions. Eight annotated AIO contexts and three native neighbors support the bounded decision.

### initial-grid-and-tied-evolution

evidence: supported. Targets: AIMech:NeuralGPU.

Supported within the stated primary-source and mathematical scope.

Section2 writes all input embeddings into the first column and zeroes the rest before repeated CGRUs. Output argmax and training softmax negative log probability are correctly separated.

### gate-and-spatial-boundaries

evidence: supported. Targets: AIMech:NeuralGPU.

Supported within the stated primary-source and mathematical scope.

The displayed u*s+(1-u)*tanh(U*(r*s)+B) directly establishes old-state weighting and reset before convolution. Chosen counterexamples distinguish the altered formulas and finite-boundary shifts without asserting implementation inspection.

### relaxation-and-training-protocol

evidence: supported. Targets: AIMech:NeuralGPU.

Supported within the stated primary-source and mathematical scope.

Section3.3.2 uses cyclic initially identical copies, a distance-to-mean penalty, increasing sharing pull, final averaging and continued shared training. The nonlinear example shows why parameter averaging is not prediction ensembling.

### parallel-depth-and-total-work

evidence: supported. Targets: AIMech:NeuralGPU.

Supported within the stated primary-source and mathematical scope.

With fixed width and kernels, n positions across n time steps give quadratic local work but linear dependent stages and constant tied parameters. The follow-up explicitly states quadratic work; neither paper proves learned universal correctness.

### original-finite-generalization-evidence

evidence: supported. Targets: AIMech:NeuralGPU.

Supported within the stated primary-source and mathematical scope.

Table1 counts fully correct outputs; selected up-to20-bit training runs reach2000-bit tests. Sections3.3–4 disclose seed/hyperparameter selection and original decimal multiplication failure, preventing an all-model or all-input interpretation.

### followup-structured-input-failures

evidence: supported. Targets: AIMech:NeuralGPU.

Supported within the stated primary-source and mathematical scope.

The follow-up changes size and base curriculum, enabling some decimal tasks while Table3 and Figure6 expose padded products and long-carry failures. These are scoped tested configurations, not an assertion about every original checkpoint.

### reset placement, gate convention, finite spatial boundaries, relaxed parameter averaging, total work and finite generalization

consistency: supported. Targets: AIMech:NeuralGPU.

Constructed calculations support the stated distinctions.

Chosen calculations distinguish reset-before-convolution from reset-after-convolution, old-state versus candidate gate weights, finite-boundary translations, parameter averaging versus output ensembling and fixed-parameter depth/work scaling. No author code, trained model or benchmark is executed.

### All maintained fields

provenance: supported. Targets: AIMech:NeuralGPU.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all six claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Confirmed complete-input initialization, old-state gate weighting and reset-before-convolution; distinguished parameter sharing from ensembling and sequential depth from total work. Rechecked selected full-output extrapolation tests, decimal curriculum changes and structured failures. All maintained fields and mappings read; source and calculation hashes rechecked.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T111119Z-neural-gpu.json | supports | Compared all 442 pinned AIO and 607 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 32, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered 70 AIO and 94 native definitions, with every matched definition read. 8 full annotated AIO node/edge/generated contexts and 3 full native records were inspected. The named Neural GPU evolves a complete input grid with time-shared convolutional gated updates. It is not GPU hardware, an NTM external read/write controller, generic GRU, DMN episodic QA or typed-graph GG-NN. Follow-up size/curriculum changes are scoped observations about the architecture rather than separate trained-model records. |
| mapping | sources/aio/aio.json | supports | RNN is a supported broad target for time-shared recurrence. GRU and convolutional layer are related components. The narrow visual definition of DeepConvolutionalNetwork and anomalous generic GRU parentage do not establish additional is-a assertions. Eight annotated AIO contexts and three native neighbors support the bounded decision. |
| kaiser2016 | https://arxiv.org/pdf/1511.08228v3; Complete nine-page arXiv1511.08228v3 and eleven-page arXiv1611.00736v2 PDFs inspected; other versions, author code, training and hardware measurements not inspected or run. | supports | arXiv1511.08228v3,15 March2016, ICLR2016 publication header. All nine PDF pages visually read, including equations, experiments and references. Locators use PDF/printed page order. Other versions and author code not inspected. |
| price2016 | https://arxiv.org/pdf/1611.00736v2; Complete nine-page arXiv1511.08228v3 and eleven-page arXiv1611.00736v2 PDFs inspected; other versions, author code, training and hardware measurements not inspected or run. | supports | arXiv1611.00736v2,4 November2016, eleven PDF pages, all visually read. The PDF says under review ICLR2016; no acceptance is inferred from that header. Locators use PDF/printed page order. Other versions and author code not inspected. |
| calculation | research/discovery/neural-gpu-boundaries.py | supports | Chosen calculations distinguish reset-before-convolution from reset-after-convolution, old-state versus candidate gate weights, finite-boundary translations, parameter averaging versus output ensembling and fixed-parameter depth/work scaling. No author code, trained model or benchmark is executed. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these are not independent gate runs.
- One new DRAFT concept, yielding 608 native and 442 unchanged generated records. The 792-entry main frontier retains 477 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All nine original and eleven follow-up PDF pages visually read; methods, tables, figures and references inspected. Other versions and author code not inspected. Follow-up configurations are not equated with every original trained model.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T112202Z-neural-gpu
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Neural GPU
started_at: '2026-10-13T11:12:11Z'
finished_at: '2026-10-13T11:22:02Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged reset placement, gate convention, finite
    spatial boundaries, relaxed parameter averaging, total work and finite generalization.
    This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Neural GPU is supported as a distinct DRAFT recurrent architecture. No unresolved
  findings in this author self-review; original and follow-up generalization claims
  remain configuration-bounded.
source:
  git_revision: 1ddc81b074ce61455a789440a8b80097a95737f0
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/ConvolutionalLayer.yaml
    sha256: 3b87e9fe798141deee846b353fa6d8530c637135eeb7e9eb4fa9f6597d7a25fd
    role: context
  - path: data/aio/DeepConvolutionalNetwork.yaml
    sha256: b2be73a895ae3890ca0ba464c1d0de55e41960f33ec53dcab4547abfe1159c62
    role: context
  - path: data/aio/DeepFeedForwardNetwork.yaml
    sha256: d66c246318687598cf762fae4b54586a312b70d143735aba5c12b2606c45c8c9
    role: context
  - path: data/aio/GatedRecurrentUnit.yaml
    sha256: 16e73da5012ad3e1d3de23bb30db0a0e18464b02b038acddd1c0f07f4fe82940
    role: context
  - path: data/aio/MemoryCellLayer.yaml
    sha256: 290f04d7838e185381b29b22e67f8765de74242d687d23b0ffae2dad9d3f7237
    role: context
  - path: data/aio/NeuralTuringMachineNetwork.yaml
    sha256: bb483a9f90d767bcae50856c6084f31fe855d510d352419a5130fa4fc036be79
    role: context
  - path: data/aio/RecurrentNeuralNetwork.yaml
    sha256: 1ebef94d2014e9a19d4bb3ed0fed6c5d77098a5a44e00e2cbd1cfe682dfcd892
    role: context
  - path: data/curated/CommunicationNeuralNetwork.yaml
    sha256: 6da13aca3d17822181f43ddfb796a62170d2cdbb28a2e01a5d541c9a1ff8d813
    role: context
  - path: data/curated/DynamicMemoryNetworkPlus.yaml
    sha256: a7360c19312b2db3e79fdebcf74908537e3d1582488646b164c9a97a6c6568d6
    role: context
  - path: data/curated/GatedGraphNeuralNetwork.yaml
    sha256: 59e5d2fcccdc609c81eb621cc92a9dc47961324af087d49a70be26f55b9b08db
    role: context
  - path: data/curated/NeuralGPU.yaml
    sha256: 0c862105dfd0351e262d4b100c99b903aaa8f146788817e8c09ee97782b26727
    role: target
  - path: research/discovery/20261013T111119Z-neural-gpu.json
    sha256: c8606585182461bfc36d427adc846406abcc15480b9db7a658ee4618eeca6228
    role: context
  - path: research/discovery/neural-gpu-boundaries.py
    sha256: d98ce76b7b9d8d4bce2360e119114e3f82b0e5e53f330f44481f1afa5479f3ed
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
- target_id: AIMech:NeuralGPU
  path: data/curated/NeuralGPU.yaml
  label: Neural GPU
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NeuralGPU.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:NeuralGPU'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:NeuralGPU
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: Complete nine-page arXiv1511.08228v3 and eleven-page arXiv1611.00736v2
      PDFs inspected; other versions, author code, training and hardware measurements
      not inspected or run.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:NeuralGPU
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 122.43s (0:02:02)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 609 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 276 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 272,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:NeuralGPU
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
  - AIMech:NeuralGPU
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
  - AIMech:NeuralGPU
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/neural-gpu-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:NeuralGPU
  exit_code: 0
  expected_exit_code: 0
  summary: '{"averaged_outputs": 0.48201379003790845, "averaged_parameters": 0.7615941559557649,
    "candidate_weighted": 0.9840418038538805, "conv_shift": [1.0, 3.0, 3.0], "count10":
    {"cgru_parameters": 31248, "sequential_cgru_stages": 20, "updated_scalar_states":
    19200}, "count20": {"cgru_parameters": 31248, "sequential_cgru_stages": 40, "updated_scalar_states":
    76800}, "old_weighted": 0.9627642089923878, "reset_after": [0.6000000000000001,
    2.4000000000000004], "reset_before": [1.8, 1.8], "shift_conv": [0.0, 3.0, 6.0]}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T111119Z-neural-gpu.json
  accessed_at: '2026-10-13T11:12:11Z'
  support: supports
  summary: Compared all 442 pinned AIO and 607 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    32, 0, 0 lines. All distinct match contents were inspected. Semantic matching
    covered 70 AIO and 94 native definitions, with every matched definition read.
    8 full annotated AIO node/edge/generated contexts and 3 full native records were
    inspected. The named Neural GPU evolves a complete input grid with time-shared
    convolutional gated updates. It is not GPU hardware, an NTM external read/write
    controller, generic GRU, DMN episodic QA or typed-graph GG-NN. Follow-up size/curriculum
    changes are scoped observations about the architecture rather than separate trained-model
    records.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T11:12:11Z'
  support: supports
  summary: RNN is a supported broad target for time-shared recurrence. GRU and convolutional
    layer are related components. The narrow visual definition of DeepConvolutionalNetwork
    and anomalous generic GRU parentage do not establish additional is-a assertions.
    Eight annotated AIO contexts and three native neighbors support the bounded decision.
- evidence_id: kaiser2016
  kind: primary_source
  reference: https://arxiv.org/pdf/1511.08228v3
  locator: Complete nine-page arXiv1511.08228v3 and eleven-page arXiv1611.00736v2
    PDFs inspected; other versions, author code, training and hardware measurements
    not inspected or run.
  accessed_at: '2026-10-13T10:40:34Z'
  snapshot_sha256: 9bc9b63e985a663420ad6dd172ec9353a79a90b16bbf3f15148a6c182dc8aefc
  support: supports
  summary: arXiv1511.08228v3,15 March2016, ICLR2016 publication header. All nine PDF
    pages visually read, including equations, experiments and references. Locators
    use PDF/printed page order. Other versions and author code not inspected.
- evidence_id: price2016
  kind: primary_source
  reference: https://arxiv.org/pdf/1611.00736v2
  locator: Complete nine-page arXiv1511.08228v3 and eleven-page arXiv1611.00736v2
    PDFs inspected; other versions, author code, training and hardware measurements
    not inspected or run.
  accessed_at: '2026-10-13T10:52:21Z'
  snapshot_sha256: 898b99d24b64306c51a934c596ff9a0188ce3c4b6470fef757355f79162d1fe7
  support: supports
  summary: arXiv1611.00736v2,4 November2016, eleven PDF pages, all visually read.
    The PDF says under review ICLR2016; no acceptance is inferred from that header.
    Locators use PDF/printed page order. Other versions and author code not inspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/neural-gpu-boundaries.py
  accessed_at: '2026-10-13T11:16:53Z'
  snapshot_sha256: d98ce76b7b9d8d4bce2360e119114e3f82b0e5e53f330f44481f1afa5479f3ed
  support: supports
  summary: Chosen calculations distinguish reset-before-convolution from reset-after-convolution,
    old-state versus candidate gate weights, finite-boundary translations, parameter
    averaging versus output ensembling and fixed-parameter depth/work scaling. No
    author code, trained model or benchmark is executed.
assessments:
- assessment_id: identity
  area: identity
  topic: Neural GPU
  outcome: supported
  target_ids:
  - AIMech:NeuralGPU
  evidence_ids:
  - identity
  - kaiser2016
  - price2016
  summary: Retain this distinct DRAFT architecture.
  details: Grid state evolution is a distinct named architecture. Neither GPU hardware
    nor generic GRU, typed-graph message passing, episodic memory QA or an NTM controller
    defines the same concept. Follow-up trained configurations are evidence, not standalone
    identities.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:NeuralGPU
  evidence_ids:
  - mapping
  - kaiser2016
  - price2016
  summary: The declared AIO mapping is supported.
  details: RNN is a supported broad target for time-shared recurrence. GRU and convolutional
    layer are related components. The narrow visual definition of DeepConvolutionalNetwork
    and anomalous generic GRU parentage do not establish additional is-a assertions.
    Eight annotated AIO contexts and three native neighbors support the bounded decision.
- assessment_id: initial-grid-and-tied-evolution
  area: evidence
  topic: initial-grid-and-tied-evolution
  outcome: supported
  target_ids:
  - AIMech:NeuralGPU
  evidence_ids:
  - kaiser2016
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section2 writes all input embeddings into the first column and zeroes the
    rest before repeated CGRUs. Output argmax and training softmax negative log probability
    are correctly separated.
- assessment_id: gate-and-spatial-boundaries
  area: evidence
  topic: gate-and-spatial-boundaries
  outcome: supported
  target_ids:
  - AIMech:NeuralGPU
  evidence_ids:
  - kaiser2016
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The displayed u*s+(1-u)*tanh(U*(r*s)+B) directly establishes old-state
    weighting and reset before convolution. Chosen counterexamples distinguish the
    altered formulas and finite-boundary shifts without asserting implementation inspection.
- assessment_id: relaxation-and-training-protocol
  area: evidence
  topic: relaxation-and-training-protocol
  outcome: supported
  target_ids:
  - AIMech:NeuralGPU
  evidence_ids:
  - kaiser2016
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section3.3.2 uses cyclic initially identical copies, a distance-to-mean
    penalty, increasing sharing pull, final averaging and continued shared training.
    The nonlinear example shows why parameter averaging is not prediction ensembling.
- assessment_id: parallel-depth-and-total-work
  area: evidence
  topic: parallel-depth-and-total-work
  outcome: supported
  target_ids:
  - AIMech:NeuralGPU
  evidence_ids:
  - kaiser2016
  - price2016
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: With fixed width and kernels, n positions across n time steps give quadratic
    local work but linear dependent stages and constant tied parameters. The follow-up
    explicitly states quadratic work; neither paper proves learned universal correctness.
- assessment_id: original-finite-generalization-evidence
  area: evidence
  topic: original-finite-generalization-evidence
  outcome: supported
  target_ids:
  - AIMech:NeuralGPU
  evidence_ids:
  - kaiser2016
  summary: Supported within the stated primary-source and mathematical scope.
  details: Table1 counts fully correct outputs; selected up-to20-bit training runs
    reach2000-bit tests. Sections3.3–4 disclose seed/hyperparameter selection and
    original decimal multiplication failure, preventing an all-model or all-input
    interpretation.
- assessment_id: followup-structured-input-failures
  area: evidence
  topic: followup-structured-input-failures
  outcome: supported
  target_ids:
  - AIMech:NeuralGPU
  evidence_ids:
  - price2016
  summary: Supported within the stated primary-source and mathematical scope.
  details: The follow-up changes size and base curriculum, enabling some decimal tasks
    while Table3 and Figure6 expose padded products and long-carry failures. These
    are scoped tested configurations, not an assertion about every original checkpoint.
- assessment_id: constructed-boundaries
  area: consistency
  topic: reset placement, gate convention, finite spatial boundaries, relaxed parameter
    averaging, total work and finite generalization
  outcome: supported
  target_ids:
  - AIMech:NeuralGPU
  evidence_ids:
  - kaiser2016
  - price2016
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Chosen calculations distinguish reset-before-convolution from reset-after-convolution,
    old-state versus candidate gate weights, finite-boundary translations, parameter
    averaging versus output ensembling and fixed-parameter depth/work scaling. No
    author code, trained model or benchmark is executed.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:NeuralGPU
  evidence_ids:
  - identity
  - mapping
  - kaiser2016
  - price2016
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all six claims/locators, source identities/versions/access/hashes, AIO pin and
    mapping, limitations and actual curation timestamps. Capture/source/context hashes
    and exact report mirror agree. Confirmed complete-input initialization, old-state
    gate weighting and reset-before-convolution; distinguished parameter sharing from
    ensembling and sequential depth from total work. Rechecked selected full-output
    extrapolation tests, decimal curriculum changes and structured failures. All maintained
    fields and mappings read; source and calculation hashes rechecked.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these
  are not independent gate runs.
- One new DRAFT concept, yielding 608 native and 442 unchanged generated records.
  The 792-entry main frontier retains 477 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- All nine original and eleven follow-up PDF pages visually read; methods, tables,
  figures and references inspected. Other versions and author code not inspected.
  Follow-up configurations are not equated with every original trained model.
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
