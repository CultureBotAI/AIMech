# Scientific author self-review of FiLM Parameter-Arithmetic Inference

- Review: 20261013T170726Z-film-parameter-arithmetic-inference
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T17:01:34Z
- Finished UTC: 2026-10-13T17:07:26Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain FiLM Parameter-Arithmetic Inference as a DRAFT native algorithm with a bounded AIO no-match assessment. All maintained fields were assessed against complete primary evidence and a constructed counterexample. The corrected evaluation wording resolves issue 294 and the linked predecessor finding. No unresolved actionable defect remains; author self-review only.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:FiLMParameterArithmeticInference
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3ddd0cd33930c6dbf5ca76b875149fc97e9ab9b1.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:FiLMParameterArithmeticInference | data/curated/FiLMParameterArithmeticInference.yaml | maintained | FiLM Parameter-Arithmetic Inference |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:FiLMParameterArithmeticInference | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 163.22s (0:02:43)<br>Checked 442 record(s); 0 failed.<br>Checked 634 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 311 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 308,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:FiLMParameterArithmeticInference | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:FiLMParameterArithmeticInference | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:FiLMParameterArithmeticInference | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:FiLMParameterArithmeticInference | {"interpretation": "Parameter-space arithmetic neither proves output-space arithmetic nor semantic analogy correctness.", "multilayer_counterexample": {"combination_of_outputs": 5.0, "parameter_combination_output": 9.0}, "single_fixed_feature_affine_identity": {"composed_parameters": [2.5, 0.7000000000000001], "output": 8.2, "output_combination": 8.200000000000001}} |

## Scientific And Domain Assessments

### FiLM Parameter-Arithmetic Inference

identity: supported. Targets: AIMech:FiLMParameterArithmeticInference.

Retain this distinct DRAFT algorithm.

Retain the locally described inference procedure from FiLM Section 4.5, not the FiLM layer or complete neural architecture. The label is descriptive rather than claimed as the authors’ formal name. Question-conditioned architectures and answer ensembles do not implement the same generated-parameter analogy.

### Bounded AIO no-match assessment

grounding: supported. Targets: AIMech:FiLMParameterArithmeticInference.

The bounded no-match assessment is supported for the inspected snapshot.

The no-match assessment is bounded to the inspected AIO pin. Seven full annotated node/edge/YAML contexts and three native records were inspected. The nearest zero-shot class concerns unseen output classes; other candidates are LLM categories, training strategies or the arithmetic component. None supports an appropriate mapping for the full parser-assisted inference algorithm.

### generated-parameter-combination

evidence: supported. Targets: AIMech:FiLMParameterArithmeticInference.

Supported within the stated primary-source and mathematical scope.

Section 4.5 and Figure 10 combine generated gamma/beta vectors for three attribute-swapped questions as theta1+theta2-theta3. This does not add model weights, tokens or answer logits.

### parser-dependency

evidence: supported. Targets: AIMech:FiLMParameterArithmeticInference.

Supported within the stated primary-source and mathematical scope.

The inspected experiment uses a parser to construct related questions. A learned replacement and explicit training for analogies are future work. The source does not establish applicability to arbitrary language.

### post-training-inference-stage

evidence: supported. Targets: AIMech:FiLMParameterArithmeticInference.

Supported within the stated primary-source and mathematical scope.

The arithmetic is applied to an already trained model without fitting its weights per analogy. Separate before/after Condition B fine-tuning comparisons use different trained model states; the underlying training remains supervised.

### linear-parameter-nonlinear-output

evidence: supported. Targets: AIMech:FiLMParameterArithmeticInference.

Supported within the stated primary-source and mathematical scope.

A fixed-feature affine layer obeys the arithmetic identity, but a two-layer example yields 9 from composed parameters versus 5 from composed outputs. The source’s qualified observations are not a general semantic-composition theorem.

### restricted-generalization-evaluation

evidence: supported. Targets: AIMech:FiLMParameterArithmeticInference.

Supported within the stated primary-source and mathematical scope.

The source’s parser construction applies to one third of Condition B questions. The corrected claim scopes exclusion of 30,000 fine-tuning examples to the Figure 9 Condition B validation-accuracy curve, matching the caption without generalizing its statement to every comparison. Color-shape combination changes are not proof of unseen answer-class prediction or universal zero-shot reasoning.

### parser-assisted generated-parameter analogies, fixed-weight inference and nonlinear output boundaries

consistency: supported. Targets: AIMech:FiLMParameterArithmeticInference.

Constructed calculations support the stated distinctions.

A fixed-feature affine example preserves the parameter-combination identity, but a two-layer model gives 9 from combined parameters versus 5 from combined outputs. This refutes a general output-arithmetic guarantee, without testing semantic analogies or replicating CLEVR results.

### All maintained fields

provenance: supported. Targets: AIMech:FiLMParameterArithmeticInference.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 5 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Assessed all fields, no-match rationale and examined-target rejections, source hashes/locators, algorithm identity and limitations. Challenged generated coefficients versus model weights or answers, parser dependency, fixed learned parameters, multilayer arithmetic and the limited CoGenT question scope.

## Findings

### F1: Limit fine-tuning exclusion wording to the documented validation curve

minor / resolved / confirmed; issue key: film-parameter-arithmetic-validation-curve-scope.

The restricted-generalization-evaluation claim says validation comparisons exclude all 30,000 fine-tuning examples. Figure 9’s caption explicitly attaches this exclusion to its validation-accuracy curve and separately describes the table. The broader wording exceeds the caption’s explicit scope; narrow it to the curve without asserting a different table protocol.

Disposition: The maintained claim now scopes the fine-tuning exclusion to the Figure 9 Condition B validation-accuracy curve. Complete corrected record, seven mapping YAMLs and primary pages 2–3 and 8–9 were reread after capture. Report mirror and EDIT history agree; corrected-input gates pass.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T165529Z-film-parameter-arithmetic-inference.json | supports | Compared all 442 pinned AIO and 633 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 52, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered 39 AIO and 41 native definitions, with every matched definition read. 7 full annotated AIO node/edge/generated contexts and 3 full native records were inspected. The local descriptive name denotes the parser-assisted FiLM parameter-combination inference procedure in Section 4.5, not a claimed verbatim author method name. It differs from the FiLM layer, an entire question-answering architecture, answer ensembling and model-weight arithmetic. |
| mapping | sources/aio/aio.json | supports | The no-match assessment is bounded to the inspected AIO pin. Seven full annotated node/edge/YAML contexts and three native records were inspected. The nearest zero-shot class concerns unseen output classes; other candidates are LLM categories, training strategies or the arithmetic component. None supports an appropriate mapping for the full parser-assisted inference algorithm. |
| perez2017film | https://arxiv.org/pdf/1709.07871v2; Complete thirteen-page arXiv 1709.07871v2 visually inspected, including equations, Figures 1–18, Tables 1–4, references and Appendix Sections 7.1–7.3. Other versions, author implementation, model fitting and empirical replication excluded. | supports | arXiv:1709.07871v2, 18 December 2017, thirteen PDF pages with AAAI 2018 copyright. All pages visually read, including Equations 1–3, Tables 1–4, Figures 1–18, references and Appendix Sections 7.1–7.3. Other versions and author implementation not inspected. |
| calculation | research/discovery/film-parameter-arithmetic-boundaries.py | supports | A fixed-feature affine example preserves the parameter-combination identity, but a two-layer model gives 9 from combined parameters versus 5 from combined outputs. This refutes a general output-arithmetic guarantee, without testing semantic analogies or replicating CLEVR results. |
| corrected-record | data/curated/FiLMParameterArithmeticInference.yaml | supports | Complete corrected record read after capture. The exclusion statement now names only the Figure 9 Condition B validation-accuracy curve. |
| predecessor | reviews/structured/20261013T170040Z-film-parameter-arithmetic-validation-curve/review.yaml | supports | Immutable partial review preserves the original minor evaluation-scope finding. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- One new DRAFT concept, yielding 634 native and 442 unchanged generated records. The 819-entry main frontier retains 475 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- Complete thirteen-page primaryv2 visually inspected, including appendix, equations, tables, all18figures and references. No author implementation or empirical replication.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T170726Z-film-parameter-arithmetic-inference
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of FiLM Parameter-Arithmetic Inference
started_at: '2026-10-13T17:01:34Z'
finished_at: '2026-10-13T17:07:26Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged parser-assisted generated-parameter analogies,
    fixed-weight inference and nonlinear output boundaries. This is adversarial author
    self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain FiLM Parameter-Arithmetic Inference as a DRAFT native algorithm with
  a bounded AIO no-match assessment. All maintained fields were assessed against complete
  primary evidence and a constructed counterexample. The corrected evaluation wording
  resolves issue 294 and the linked predecessor finding. No unresolved actionable
  defect remains; author self-review only.
source:
  git_revision: 3ddd0cd33930c6dbf5ca76b875149fc97e9ab9b1
  state: working_tree
  inputs:
  - path: data/aio/CompositionalGeneralizationLLM.yaml
    sha256: f2d1f09f316234e5a801870f24d8d6a58b21567bbcc5d22928923a833f04fb0f
    role: context
  - path: data/aio/KnowledgeTransfer.yaml
    sha256: d9c3efd84c05da8efb7b8eb46e15d64a1ea18fd0816c96cba9bcad85619c57bb
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/ReasoningLLM.yaml
    sha256: 5ceb143da4d5ac2c3bdc430596e21d48943caaa848ae20abf92c791d69a90bfd
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/aio/ZeroShotLearningLLM.yaml
    sha256: 41c8d572a51fdd2603b29c5af6ed7ab4dde2b7459223b21d89dea6a7636b396c
    role: context
  - path: data/aio/ZeroshotLearning.yaml
    sha256: c728c0a1c5fc27ae9e7a05437071108a66ef7784a2eab5d8952100960ac0f3ec
    role: context
  - path: data/curated/AttentionBasedConfigurableConvolutionalNeuralNetwork.yaml
    sha256: 9023f81f517d8ab9656429a53a74f9fc57d1c23c29fb3286b9662cb2e20a5f46
    role: context
  - path: data/curated/DynamicMemoryNetwork.yaml
    sha256: 0affc6bdf4fd1c02c6d423d8560b53d357f5eca0ec8d93d29176375da25636fe
    role: context
  - path: data/curated/FeatureWiseLinearModulation.yaml
    sha256: 04cdbed7b9a44ec4fc4c98b2dd6971a1fb6e4fc2c133926febe9411423836b63
    role: context
  - path: data/curated/FiLMParameterArithmeticInference.yaml
    sha256: 420a52d8357fcdcab5d14702811949382a89f3ba7bf6c6baabf14f92f39cebce
    role: target
  - path: research/discovery/20261013T165529Z-film-parameter-arithmetic-inference.json
    sha256: 6b4c31ab4e22ba8d354a565c76c69bfb589b673aa41d7273b72e1a60e70a6d65
    role: context
  - path: research/discovery/film-parameter-arithmetic-boundaries.py
    sha256: 4dd7a2e418501be08b4ccc2e3f3db71be5f048ec0c3b079d8e0ec68c2c46c412
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
- target_id: AIMech:FiLMParameterArithmeticInference
  path: data/curated/FiLMParameterArithmeticInference.yaml
  label: FiLM Parameter-Arithmetic Inference
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FiLMParameterArithmeticInference.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:FiLMParameterArithmeticInference'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:FiLMParameterArithmeticInference
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: Complete thirteen-page arXiv 1709.07871v2 visually inspected, including
      equations, Figures 1–18, Tables 1–4, references and Appendix Sections 7.1–7.3.
      Other versions, author implementation, model fitting and empirical replication
      excluded.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:FiLMParameterArithmeticInference
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 163.22s (0:02:43)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 634 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 311 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 308,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:FiLMParameterArithmeticInference
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
  - AIMech:FiLMParameterArithmeticInference
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
  - AIMech:FiLMParameterArithmeticInference
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/film-parameter-arithmetic-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:FiLMParameterArithmeticInference
  exit_code: 0
  expected_exit_code: 0
  summary: '{"interpretation": "Parameter-space arithmetic neither proves output-space
    arithmetic nor semantic analogy correctness.", "multilayer_counterexample": {"combination_of_outputs":
    5.0, "parameter_combination_output": 9.0}, "single_fixed_feature_affine_identity":
    {"composed_parameters": [2.5, 0.7000000000000001], "output": 8.2, "output_combination":
    8.200000000000001}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T165529Z-film-parameter-arithmetic-inference.json
  accessed_at: '2026-10-13T17:01:34Z'
  support: supports
  summary: Compared all 442 pinned AIO and 633 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    52, 0, 0 lines. All distinct match contents were inspected. Semantic matching
    covered 39 AIO and 41 native definitions, with every matched definition read.
    7 full annotated AIO node/edge/generated contexts and 3 full native records were
    inspected. The local descriptive name denotes the parser-assisted FiLM parameter-combination
    inference procedure in Section 4.5, not a claimed verbatim author method name.
    It differs from the FiLM layer, an entire question-answering architecture, answer
    ensembling and model-weight arithmetic.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T17:01:34Z'
  support: supports
  summary: The no-match assessment is bounded to the inspected AIO pin. Seven full
    annotated node/edge/YAML contexts and three native records were inspected. The
    nearest zero-shot class concerns unseen output classes; other candidates are LLM
    categories, training strategies or the arithmetic component. None supports an
    appropriate mapping for the full parser-assisted inference algorithm.
- evidence_id: perez2017film
  kind: primary_source
  reference: https://arxiv.org/pdf/1709.07871v2
  locator: Complete thirteen-page arXiv 1709.07871v2 visually inspected, including
    equations, Figures 1–18, Tables 1–4, references and Appendix Sections 7.1–7.3.
    Other versions, author implementation, model fitting and empirical replication
    excluded.
  accessed_at: '2026-10-13T14:50:22Z'
  snapshot_sha256: 765acea6f2a78b1d76961392099cd0af49cb2e7d6f06d0b3d82f1dbe9cdcd363
  support: supports
  summary: arXiv:1709.07871v2, 18 December 2017, thirteen PDF pages with AAAI 2018
    copyright. All pages visually read, including Equations 1–3, Tables 1–4, Figures
    1–18, references and Appendix Sections 7.1–7.3. Other versions and author implementation
    not inspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/film-parameter-arithmetic-boundaries.py
  accessed_at: '2026-10-13T17:02:03Z'
  snapshot_sha256: 4dd7a2e418501be08b4ccc2e3f3db71be5f048ec0c3b079d8e0ec68c2c46c412
  support: supports
  summary: A fixed-feature affine example preserves the parameter-combination identity,
    but a two-layer model gives 9 from combined parameters versus 5 from combined
    outputs. This refutes a general output-arithmetic guarantee, without testing semantic
    analogies or replicating CLEVR results.
- evidence_id: corrected-record
  kind: record_content
  reference: data/curated/FiLMParameterArithmeticInference.yaml
  accessed_at: '2026-10-13T17:02:03Z'
  snapshot_sha256: 420a52d8357fcdcab5d14702811949382a89f3ba7bf6c6baabf14f92f39cebce
  support: supports
  summary: Complete corrected record read after capture. The exclusion statement now
    names only the Figure 9 Condition B validation-accuracy curve.
- evidence_id: predecessor
  kind: record_content
  reference: reviews/structured/20261013T170040Z-film-parameter-arithmetic-validation-curve/review.yaml
  accessed_at: '2026-10-13T17:02:03Z'
  support: supports
  summary: Immutable partial review preserves the original minor evaluation-scope
    finding.
assessments:
- assessment_id: identity
  area: identity
  topic: FiLM Parameter-Arithmetic Inference
  outcome: supported
  target_ids:
  - AIMech:FiLMParameterArithmeticInference
  evidence_ids:
  - identity
  - perez2017film
  summary: Retain this distinct DRAFT algorithm.
  details: Retain the locally described inference procedure from FiLM Section 4.5,
    not the FiLM layer or complete neural architecture. The label is descriptive rather
    than claimed as the authors’ formal name. Question-conditioned architectures and
    answer ensembles do not implement the same generated-parameter analogy.
- assessment_id: mapping
  area: grounding
  topic: Bounded AIO no-match assessment
  outcome: supported
  target_ids:
  - AIMech:FiLMParameterArithmeticInference
  evidence_ids:
  - mapping
  - perez2017film
  summary: The bounded no-match assessment is supported for the inspected snapshot.
  details: The no-match assessment is bounded to the inspected AIO pin. Seven full
    annotated node/edge/YAML contexts and three native records were inspected. The
    nearest zero-shot class concerns unseen output classes; other candidates are LLM
    categories, training strategies or the arithmetic component. None supports an
    appropriate mapping for the full parser-assisted inference algorithm.
- assessment_id: generated-parameter-combination
  area: evidence
  topic: generated-parameter-combination
  outcome: supported
  target_ids:
  - AIMech:FiLMParameterArithmeticInference
  evidence_ids:
  - perez2017film
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Section 4.5 and Figure 10 combine generated gamma/beta vectors for three
    attribute-swapped questions as theta1+theta2-theta3. This does not add model weights,
    tokens or answer logits.
- assessment_id: parser-dependency
  area: evidence
  topic: parser-dependency
  outcome: supported
  target_ids:
  - AIMech:FiLMParameterArithmeticInference
  evidence_ids:
  - perez2017film
  summary: Supported within the stated primary-source and mathematical scope.
  details: The inspected experiment uses a parser to construct related questions.
    A learned replacement and explicit training for analogies are future work. The
    source does not establish applicability to arbitrary language.
- assessment_id: post-training-inference-stage
  area: evidence
  topic: post-training-inference-stage
  outcome: supported
  target_ids:
  - AIMech:FiLMParameterArithmeticInference
  evidence_ids:
  - perez2017film
  summary: Supported within the stated primary-source and mathematical scope.
  details: The arithmetic is applied to an already trained model without fitting its
    weights per analogy. Separate before/after Condition B fine-tuning comparisons
    use different trained model states; the underlying training remains supervised.
- assessment_id: linear-parameter-nonlinear-output
  area: evidence
  topic: linear-parameter-nonlinear-output
  outcome: supported
  target_ids:
  - AIMech:FiLMParameterArithmeticInference
  evidence_ids:
  - perez2017film
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: A fixed-feature affine layer obeys the arithmetic identity, but a two-layer
    example yields 9 from composed parameters versus 5 from composed outputs. The
    source’s qualified observations are not a general semantic-composition theorem.
- assessment_id: restricted-generalization-evaluation
  area: evidence
  topic: restricted-generalization-evaluation
  outcome: supported
  target_ids:
  - AIMech:FiLMParameterArithmeticInference
  evidence_ids:
  - perez2017film
  summary: Supported within the stated primary-source and mathematical scope.
  details: The source’s parser construction applies to one third of Condition B questions.
    The corrected claim scopes exclusion of 30,000 fine-tuning examples to the Figure
    9 Condition B validation-accuracy curve, matching the caption without generalizing
    its statement to every comparison. Color-shape combination changes are not proof
    of unseen answer-class prediction or universal zero-shot reasoning.
- assessment_id: constructed-boundaries
  area: consistency
  topic: parser-assisted generated-parameter analogies, fixed-weight inference and
    nonlinear output boundaries
  outcome: supported
  target_ids:
  - AIMech:FiLMParameterArithmeticInference
  evidence_ids:
  - perez2017film
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: A fixed-feature affine example preserves the parameter-combination identity,
    but a two-layer model gives 9 from combined parameters versus 5 from combined
    outputs. This refutes a general output-arithmetic guarantee, without testing semantic
    analogies or replicating CLEVR results.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:FiLMParameterArithmeticInference
  evidence_ids:
  - identity
  - mapping
  - perez2017film
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 5 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. Assessed all fields, no-match rationale and examined-target
    rejections, source hashes/locators, algorithm identity and limitations. Challenged
    generated coefficients versus model weights or answers, parser dependency, fixed
    learned parameters, multilayer arithmetic and the limited CoGenT question scope.
findings:
- finding_id: F1
  issue_key: film-parameter-arithmetic-validation-curve-scope
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Limit fine-tuning exclusion wording to the documented validation curve
  description: The restricted-generalization-evaluation claim says validation comparisons
    exclude all 30,000 fine-tuning examples. Figure 9’s caption explicitly attaches
    this exclusion to its validation-accuracy curve and separately describes the table.
    The broader wording exceeds the caption’s explicit scope; narrow it to the curve
    without asserting a different table protocol.
  target_ids:
  - AIMech:FiLMParameterArithmeticInference
  field_paths:
  - claims[restricted-generalization-evaluation].statement
  evidence_ids:
  - perez2017film
  - corrected-record
  - predecessor
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FiLMParameterArithmeticInference.yaml
    role: maintained
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/294
  disposition_reason: The maintained claim now scopes the fine-tuning exclusion to
    the Figure 9 Condition B validation-accuracy curve. Complete corrected record,
    seven mapping YAMLs and primary pages 2–3 and 8–9 were reread after capture. Report
    mirror and EDIT history agree; corrected-input gates pass.
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261013T170040Z-film-parameter-arithmetic-validation-curve
    finding_id: F1
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- One new DRAFT concept, yielding 634 native and 442 unchanged generated records.
  The 819-entry main frontier retains 475 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- Complete thirteen-page primaryv2 visually inspected, including appendix, equations,
  tables, all18figures and references. No author implementation or empirical replication.
- No author code, training, paid service, hardware measurement or empirical replication.
  Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization
  and old round141 cleanup remain pending explicit approval after automatic review
  rejection.
related_reviews:
- repository: CultureBotAI/AIMech
  review_id: 20261013T170040Z-film-parameter-arithmetic-validation-curve
  relationship: Resolves the explicitly linked validation-curve scope finding.
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
