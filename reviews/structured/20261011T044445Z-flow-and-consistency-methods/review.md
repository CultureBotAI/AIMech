# Scientific self-review of flow and consistency methods

- Review: 20261011T044445Z-flow-and-consistency-methods
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T04:44:45Z
- Finished UTC: 2026-10-11T04:44:45Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

All four additions have inspected primary-method support and justified AIO mapping directions. The review checked flow-objective overlap, model-versus-training boundaries, conditional versus marginal optimal transport, teacher versus inference EMA, and interval versus grid-point counts. The records retain the inspected theoretical corrections without generalizing them into unrelated refutations; no actionable unresolved record defect was identified.

## Scope And Provenance

Identity, definition, claim evidence, versions, limitations and AIO mappings of four native generative-method additions.

Selection: Exactly the four maintained targets in the flow-and-consistency-methods discovery ledger, with no sampling.
Coverage: full; 4 reviewed / 4 in the declared population.
Source: working_tree at Git base f0ec6d0cc8cebeb47e253028b1b50bd237d5df93.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:FlowMatching | data/curated/FlowMatching.yaml | maintained | Flow matching |
| AIMech:RectifiedFlow | data/curated/RectifiedFlow.yaml | maintained | Rectified flow |
| AIMech:ConsistencyModel | data/curated/ConsistencyModel.yaml | maintained | Consistency model |
| AIMech:ImprovedConsistencyTraining | data/curated/ImprovedConsistencyTraining.yaml | maintained | Improved consistency training |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli check-source | passed | True | AIMech:FlowMatching, AIMech:RectifiedFlow, AIMech:ConsistencyModel, AIMech:ImprovedConsistencyTraining | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate | passed | True | AIMech:FlowMatching, AIMech:RectifiedFlow, AIMech:ConsistencyModel, AIMech:ImprovedConsistencyTraining | Checked 442 record(s); 0 failed.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-curated | passed | True | AIMech:FlowMatching, AIMech:RectifiedFlow, AIMech:ConsistencyModel, AIMech:ImprovedConsistencyTraining | Checked 94 curated concept record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli seed --check | passed | True | AIMech:FlowMatching, AIMech:RectifiedFlow, AIMech:ConsistencyModel, AIMech:ImprovedConsistencyTraining | AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli validate-history --base HEAD | passed | True | AIMech:FlowMatching, AIMech:RectifiedFlow, AIMech:ConsistencyModel, AIMech:ImprovedConsistencyTraining | Checked 17 history record(s); 0 error(s).<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python scripts/record_review.py check | passed | True | AIMech:FlowMatching, AIMech:RectifiedFlow, AIMech:ConsistencyModel, AIMech:ImprovedConsistencyTraining | {<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 16,<br>  "coverage": "declared_scopes_only"<br>}<br>topClass is deprecated - use top_class<br> |
| just check | passed | True | AIMech:FlowMatching, AIMech:RectifiedFlow, AIMech:ConsistencyModel, AIMech:ImprovedConsistencyTraining | All checks passed!<br>........................................................................ [ 31%]<br>........................................................................ [ 63%]<br>........................................................................ [ 94%]<br>.........sss                                                             [100%]<br>225 passed, 3 skipped in 54.82s<br>Checked 442 record(s); 0 failed.<br>Checked 94 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 17 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 16,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:FlowMatching, AIMech:RectifiedFlow, AIMech:ConsistencyModel, AIMech:ImprovedConsistencyTraining | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |

## Scientific And Domain Assessments

### Identity, definition, mechanism, correction scope and mapping direction

evidence: supported. Targets: AIMech:FlowMatching.

The 442 pinned AIO identities and 90 preceding native identities, including scoped synonyms and aliases, were compared alongside ignored-inclusive searches of both checkouts. This record denotes the general probability-path training method of Lipman and colleagues. Conditional flow matching is its tractable objective construction, not an asserted synonym for every use of the general method. Straight conditional paths overlap with the training construction used in rectified flow; that overlap does not make the general path family and the rectification/reflow procedure identical.

The equality of conditional and marginal objective gradients is conditional on the paper's density and integrability assumptions, including positive path density in Theorem 2; finite neural training does not guarantee the ideal field. The Gaussian construction with positive terminal noise leaves a smoothed approximation to the data distribution. Training without ODE simulation does not remove numerical ODE solving from sampling. The optimal-transport conditional Gaussian path in Section 4 does not imply that the resulting marginal flow is a globally optimal transport map, as the paper explicitly notes on PDF p. 6. No benchmark superiority, universal sampling-step count or independently checked theorem proof is asserted.

### Identity, definition, mechanism, correction scope and mapping direction

evidence: supported. Targets: AIMech:RectifiedFlow.

The ignored-inclusive identity search covered both checkouts, all 442 AIO labels and scoped synonyms, and 90 preceding native identities. This record denotes the straight-interpolation regression and rectification procedure of Liu, Gong and Liu, including optional reflow. It overlaps with particular conditional flow-matching objectives, but does not denote every probability-path choice in flow matching, a particular trained image generator, or mandatory distillation.

Marginal preservation and transport-cost statements concern ideal regression with a well-posed ODE, not arbitrary finite neural estimates or numerical solvers. Straight training interpolations do not make the learned marginal trajectories exactly straight; one-step accuracy is not universal. Reflow and distillation are optional. The original paper explicitly does not guarantee a globally cost-optimal coupling in general. Later analysis also gives nonoptimal zero-loss fixed points for a gradient-constrained rectification variant when required support or regularity assumptions are absent. The later optimal-transport counterexamples limit stronger equivalence claims; they do not refute the original least-squares construction. No executable solver, numerical benchmark or full proof verification is supplied.

### Identity, definition, mechanism, correction scope and mapping direction

evidence: supported. Targets: AIMech:ConsistencyModel.

All 442 pinned AIO labels and scoped synonyms and 90 preceding native identities were checked, with ignored-inclusive text searches of both checkouts. The identity is the endpoint-map model family introduced by Song and colleagues, not generic logical consistency, a trained checkpoint, or one particular training loss. Original consistency distillation, original consistency training and improved consistency training are procedures for learning this family and are not aliases for the model family itself.

The learned consistency model is not required to be invertible. Ideal probability-flow properties do not establish exact data recovery or perfect self-consistency for a finite trained model. The original direct consistency-training teacher uses EMA; the later inspected correction identifies a failure of its original asymptotic justification when teacher and student parameters differ. This record does not endorse that original training argument as generally valid. The correction concerns consistency training and does not remove EMA from all distillation procedures or from the separate inference-time averaged model. One-evaluation generation is an available procedure, not a universal image-quality guarantee. No benchmark reproduction or independently verified convergence proof is claimed.

### Identity, definition, mechanism, correction scope and mapping direction

evidence: supported. Targets: AIMech:ImprovedConsistencyTraining.

The identity search included 442 AIO records, 90 preceding native identities, all scoped synonyms and aliases, and ignored-inclusive text in both checkouts. This is the named improved consistency-training procedure, not the consistency-model family, the original EMA-teacher training procedure, diffusion-model distillation, or a particular iCT-deep architecture/checkpoint. The acronym is qualified to avoid claiming an unscoped abbreviation.

Removing teacher EMA retains stop-gradient and does not remove inference-time parameter averaging; it is not a blanket recommendation to eliminate EMA from consistency distillation. The paper's counterexample diagnoses a flaw in an earlier asymptotic argument. Its correction and finite-noise curriculum do not establish universal finite-training convergence. Noise distribution, loss scale, discretization cap, dropout and embedding settings are choices evaluated in particular image-generation settings, not universal hyperparameters. The interval count doubles; the number of noise grid points is that count plus one. The record describes the inspected training procedure and retains DRAFT status; it does not reproduce performance comparisons, certify every proof, or identify all future variants with this version.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:FlowMatching, AIMech:RectifiedFlow, AIMech:ConsistencyModel, AIMech:ImprovedConsistencyTraining. Retain flow matching as a general path-based velocity-training algorithm and rectified flow as straight-interpolation rectification with optional reflow. Their special-case overlap does not erase the scoped distinction. Retain the consistency endpoint-map family separately from the improved procedure used to train it.
- defer: AIMech:FlowMatching, AIMech:RectifiedFlow, AIMech:ConsistencyModel, AIMech:ImprovedConsistencyTraining. Conditional-objective variants, original CT/CD and gradient-constrained rectification need distinct identity and method assessments before standalone records. No exact-equivalence merge follows from shared objectives or reported sample quality.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity-search | research/discovery/20261011T044233Z-flow-and-consistency-methods.json | supports | All 442 AIO labels/scoped synonyms and 90 preceding native identities were compared; hidden/ignored-inclusive text searches of both checkouts returned three hits each, all prior flow-matching search/variant leads. No exact record identity matched. Flow matching and rectified flow share special-case objectives without denoting the same general procedure. The consistency model family and improved training procedure have different abstraction levels. |
| mapping | sources/aio/aio.json; RegressionAnalysis, Model, TrainingStrategy, Distillation and considered generative/pretraining neighbors | supports | Flow matching and rectified flow related_match RegressionAnalysis because their defining velocity estimators use regression but the local concepts are algorithms rather than tasks. Consistency model broad_match Model. Improved consistency training related_match TrainingStrategy; its pinned preprocessing wording does not justify unqualified subclassing. Distillation, GenerativeAdversarialNetwork and UnsupervisedPretrainedNetwork were inspected/considered and do not cover these identities. |
| flowmatching-method | https://arxiv.org/pdf/2210.02747v2; Sections 3–3.2, equations (5)–(9) and Theorems 1–2, PDF pp. 3–4; Section 4, equations (10)–(24), PDF pp. 4–6 | supports | The method regresses a neural vector field on a target velocity under a prescribed time-indexed density. Conditional flow matching samples a data-conditioned path and its known conditional velocity; under the paper's assumptions its loss has the same parameter gradient as the marginal flow-matching loss. For the illustrated Gaussian conditional paths, the mean and standard deviation define an affine transformation of base noise. Training avoids integrating the learned ODE, while generation integrates that vector field from the base distribution. Rendered pages actually inspected: 3, 4, 6. |
| rectifiedflow-method | https://arxiv.org/pdf/2209.03003v1; Sections 2.1–2.2, equations (1)–(2), Algorithm 1 and transport-cost discussion, PDF pp. 4–6 | supports | Given coupled endpoints X0 and X1, training samples t and regresses v((1−t)X0+tX1,t) toward X1−X0 using squared error. The ideal minimizer is the conditional mean endpoint difference at the interpolated state. Integrating dZt/dt=v(Zt,t) from the source sample induces a new endpoint coupling. Reflow optionally trains another rectified flow on that coupling; endpoint-map distillation is a separate optional step. Rendered pages actually inspected: 4, 5, 6. |
| rectifiedflow-method-optimal-transport-analysis | https://arxiv.org/pdf/2505.19712v3; Sections 3.1–3.2, PDF pp. 5–6; Section 4.1, Proposition 10, Theorem 11 and Remark 12, PDF pp. 7–8 | supports | A later analysis of gradient-constrained rectification exhibits nonoptimal zero-loss fixed points with disconnected intermediate supports; its corrected equivalence theorem additionally requires full intermediate support, rectifiability and smooth potential fields. Straightness or imposing a potential alone does not establish globally optimal transport. This supports the stated limitation; it is not falsely recorded as a refutation of the original model identity. Rendered pages actually inspected: 7, 8. |
| consistencymodel-method | https://proceedings.mlr.press/v202/song23a/song23a.pdf; Section 3, equation (5), Algorithm 1 and boundary-condition discussion, PDF pp. 3–4; Sections 4–5, Algorithms 2–3, PDF pp. 4–6 | supports | A consistency function assigns the same low-noise endpoint to states on the same probability-flow trajectory. The paper's skip-connected parameterization combines an input skip term and a learned term whose coefficients enforce the identity boundary at the minimum noise level. Generation applies the model to high-noise input; multistep generation interleaves model evaluation with noise injection. The original paper describes both diffusion-model-assisted distillation and direct consistency training with shared-noise adjacent perturbations of a data sample. Rendered pages actually inspected: 3, 4, 5, 6. |
| consistencymodel-method-training-correction | https://arxiv.org/pdf/2310.14189v1; Section 2, teacher versus inference EMA, PDF p. 3; Section 3.2, Proposition 1 and equations (6)–(7), PDF pp. 5–6 | supports | The later paper gives a point-mass-data counterexample in which the limiting consistency-training/matching objective with unequal teacher and student parameters loses dependence on the data location. It motivates zero teacher EMA decay, with a stop-gradient teacher sharing current student parameters, for consistency training; this is distinct from averaging the model used for inference. This supports the stated limitation; it is not falsely recorded as a refutation of the original model identity. Rendered pages actually inspected: 4, 5, 6, 7, 8. |
| improvedconsistencytraining-method | https://arxiv.org/pdf/2310.14189v1; Section 2, equations (3)–(5), PDF p. 3; Table 1 and Sections 3.1–3.5, equations (6)–(10), PDF pp. 4–8 | supports | The student and stop-gradient teacher evaluate the same data sample plus the same Gaussian noise scaled to adjacent noise levels, with teacher EMA decay set to zero. The revised objective uses a Pseudo-Huber discrepancy and inverse adjacent-noise-gap weighting. Training samples adjacent intervals according to discretized lognormal masses and doubles the interval count at scheduled milestones up to a cap. Noise-embedding sensitivity and shared dropout randomness are additional prescribed training choices; the separate inference-time EMA remains distinct. Rendered pages actually inspected: 4, 5, 6, 7, 8. |

## Limits And Additional Notes

- Scientific adversarial self-review, not independent approval; all four records remain DRAFT.
- Original direct consistency-training theory is qualified by the inspected point-mass counterexample; teacher and inference EMA remain separate.
- Conditional optimal transport and trajectory straightness do not certify globally optimal marginal transport.
- No numerical benchmark reproduction or complete theorem-proof validation was performed.
- The first vendored-check attempt failed on sandbox DNS resolution. A network-enabled rerun passed against the pinned public CLAW revision; no governed artifact was changed.
- Exact follow-up query times were not retained; the discovery ledger preserves the known time bound and exact PDF access times.
- Discovery continues with unresolved leads; this pass is not a saturation claim.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T044445Z-flow-and-consistency-methods
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of flow and consistency methods
started_at: '2026-10-11T04:44:45Z'
finished_at: '2026-10-11T04:44:45Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed its own research
    and records; this is not independent scientific approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: All four additions have inspected primary-method support and justified AIO
  mapping directions. The review checked flow-objective overlap, model-versus-training
  boundaries, conditional versus marginal optimal transport, teacher versus inference
  EMA, and interval versus grid-point counts. The records retain the inspected theoretical
  corrections without generalizing them into unrelated refutations; no actionable
  unresolved record defect was identified.
source:
  git_revision: f0ec6d0cc8cebeb47e253028b1b50bd237d5df93
  state: working_tree
  inputs:
  - path: data/curated/ConsistencyModel.yaml
    sha256: 470ef7b7d9fe04a7db5f99625181659e131bbe5fe3d236644723bf5729a17c9c
    role: target
  - path: data/curated/FlowMatching.yaml
    sha256: 3e7122ee85f438483256afcce7b4621b4701d10a0022b8efa1f0eb86c6a02887
    role: target
  - path: data/curated/ImprovedConsistencyTraining.yaml
    sha256: 3cddfa58b1bfd52cd449e069ce1400aaddfcca8ec5bc91eacdc4dc05cba19359
    role: target
  - path: data/curated/RectifiedFlow.yaml
    sha256: 10025e94e6142cb77cc95f963afb4c5c70c96a7cdaac208a02420bd30245bd01
    role: target
  - path: research/discovery/20261011T044233Z-flow-and-consistency-methods.json
    sha256: 1efa09e3896278d035b838cf5ee1152a70ea383c014c93d3763b6482f41b1d0b
    role: context
  - path: sources/aio/aio.json
    sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
    role: context
  - path: sources/aio/source.yaml
    sha256: a12f1e974c25fab2ebff5e44150fb86f64399471accdf0baeafd986f00e6f345
    role: context
  - path: src/aimech/curated.py
    sha256: 0600ec8ca628d2dac611f2a068074ebcd4b83b6b5f31832a32dbc4f4bfa35b06
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: f47a2fa70fc2ff16a2bfdead30472068afa1133710819831b081b4bb6224825a
    role: context
targets:
- target_id: AIMech:FlowMatching
  path: data/curated/FlowMatching.yaml
  label: Flow matching
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FlowMatching.yaml
    role: maintained native concept
- target_id: AIMech:RectifiedFlow
  path: data/curated/RectifiedFlow.yaml
  label: Rectified flow
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RectifiedFlow.yaml
    role: maintained native concept
- target_id: AIMech:ConsistencyModel
  path: data/curated/ConsistencyModel.yaml
  label: Consistency model
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ConsistencyModel.yaml
    role: maintained native concept
- target_id: AIMech:ImprovedConsistencyTraining
  path: data/curated/ImprovedConsistencyTraining.yaml
  label: Improved consistency training
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ImprovedConsistencyTraining.yaml
    role: maintained native concept
scope:
  description: Identity, definition, claim evidence, versions, limitations and AIO
    mappings of four native generative-method additions.
  selection: Exactly the four maintained targets in the flow-and-consistency-methods
    discovery ledger, with no sampling.
  coverage: full
  population_size: 4
  reviewed_target_ids:
  - AIMech:FlowMatching
  - AIMech:RectifiedFlow
  - AIMech:ConsistencyModel
  - AIMech:ImprovedConsistencyTraining
  exclusions:
  - target: Benchmark results, appendix proof verification and executable implementation
      correctness
    reason: Records describe the inspected methods and bounded theoretical limitations;
      no such validation is asserted.
  - target: Standalone original CT/CD, gradient-constrained rectification and other
      named variants
    reason: These remain separately scoped frontier items rather than automatic duplicates
      or additions.
checks:
- check_id: required-0
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  status: passed
  required: true
  target_ids:
  - AIMech:FlowMatching
  - AIMech:RectifiedFlow
  - AIMech:ConsistencyModel
  - AIMech:ImprovedConsistencyTraining
  exit_code: 0
  expected_exit_code: 0
  summary: 'Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a

    '
- check_id: required-1
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate
  status: passed
  required: true
  target_ids:
  - AIMech:FlowMatching
  - AIMech:RectifiedFlow
  - AIMech:ConsistencyModel
  - AIMech:ImprovedConsistencyTraining
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 442 record(s); 0 failed.

    '
- check_id: required-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-curated
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:FlowMatching
  - AIMech:RectifiedFlow
  - AIMech:ConsistencyModel
  - AIMech:ImprovedConsistencyTraining
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 94 curated concept record(s); 0 error(s).

    '
- check_id: required-3
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:FlowMatching
  - AIMech:RectifiedFlow
  - AIMech:ConsistencyModel
  - AIMech:ImprovedConsistencyTraining
  exit_code: 0
  expected_exit_code: 0
  summary: 'AIO: 442 records; 0 missing, 0 changed, 0 unexpected.

    '
- check_id: required-4
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-history --base HEAD
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli validate-history --base HEAD
  status: passed
  required: true
  target_ids:
  - AIMech:FlowMatching
  - AIMech:RectifiedFlow
  - AIMech:ConsistencyModel
  - AIMech:ImprovedConsistencyTraining
  exit_code: 0
  expected_exit_code: 0
  summary: 'Checked 17 history record(s); 0 error(s).

    '
- check_id: required-5
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    scripts/record_review.py check
  status: passed
  required: true
  target_ids:
  - AIMech:FlowMatching
  - AIMech:RectifiedFlow
  - AIMech:ConsistencyModel
  - AIMech:ImprovedConsistencyTraining
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 16,\n\
    \  \"coverage\": \"declared_scopes_only\"\n}\ntopClass is deprecated - use top_class\n"
- check_id: required-6
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:FlowMatching
  - AIMech:RectifiedFlow
  - AIMech:ConsistencyModel
  - AIMech:ImprovedConsistencyTraining
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 31%]\n........................................................................\
    \ [ 63%]\n........................................................................\
    \ [ 94%]\n.........sss                                                       \
    \      [100%]\n225 passed, 3 skipped in 54.82s\nChecked 442 record(s); 0 failed.\n\
    Checked 94 curated concept record(s); 0 error(s).\nAIO: 442 records; 0 missing,\
    \ 0 changed, 0 unexpected.\nChecked 17 history record(s); 0 error(s).\n{\n  \"\
    repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 16,\n  \"coverage\"\
    : \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-7
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:FlowMatching
  - AIMech:RectifiedFlow
  - AIMech:ConsistencyModel
  - AIMech:ImprovedConsistencyTraining
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
evidence:
- evidence_id: identity-search
  kind: search
  reference: research/discovery/20261011T044233Z-flow-and-consistency-methods.json
  accessed_at: '2026-10-11T04:44:45Z'
  support: supports
  summary: All 442 AIO labels/scoped synonyms and 90 preceding native identities were
    compared; hidden/ignored-inclusive text searches of both checkouts returned three
    hits each, all prior flow-matching search/variant leads. No exact record identity
    matched. Flow matching and rectified flow share special-case objectives without
    denoting the same general procedure. The consistency model family and improved
    training procedure have different abstraction levels.
  search_scope: All 442 AIO labels and scoped synonyms, 90 preceding native identities,
    and hidden/ignored-inclusive text searches of both checkouts.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: RegressionAnalysis, Model, TrainingStrategy, Distillation and considered
    generative/pretraining neighbors
  accessed_at: '2026-10-11T04:44:45Z'
  support: supports
  summary: Flow matching and rectified flow related_match RegressionAnalysis because
    their defining velocity estimators use regression but the local concepts are algorithms
    rather than tasks. Consistency model broad_match Model. Improved consistency training
    related_match TrainingStrategy; its pinned preprocessing wording does not justify
    unqualified subclassing. Distillation, GenerativeAdversarialNetwork and UnsupervisedPretrainedNetwork
    were inspected/considered and do not cover these identities.
- evidence_id: flowmatching-method
  kind: primary_source
  reference: https://arxiv.org/pdf/2210.02747v2
  locator: Sections 3–3.2, equations (5)–(9) and Theorems 1–2, PDF pp. 3–4; Section
    4, equations (10)–(24), PDF pp. 4–6
  accessed_at: '2026-10-11T04:35:23Z'
  snapshot_sha256: 5eeb39ba516396924aba4787452f9d0abdee88467a4d0c264d9f66cad0c5ee14
  support: supports
  summary: 'The method regresses a neural vector field on a target velocity under
    a prescribed time-indexed density. Conditional flow matching samples a data-conditioned
    path and its known conditional velocity; under the paper''s assumptions its loss
    has the same parameter gradient as the marginal flow-matching loss. For the illustrated
    Gaussian conditional paths, the mean and standard deviation define an affine transformation
    of base noise. Training avoids integrating the learned ODE, while generation integrates
    that vector field from the base distribution. Rendered pages actually inspected:
    3, 4, 6.'
- evidence_id: rectifiedflow-method
  kind: primary_source
  reference: https://arxiv.org/pdf/2209.03003v1
  locator: Sections 2.1–2.2, equations (1)–(2), Algorithm 1 and transport-cost discussion,
    PDF pp. 4–6
  accessed_at: '2026-10-11T04:35:22Z'
  snapshot_sha256: d81790cb6988ef480002adcc84000d4f44855b11fb868001fd53aad133bc3a74
  support: supports
  summary: 'Given coupled endpoints X0 and X1, training samples t and regresses v((1−t)X0+tX1,t)
    toward X1−X0 using squared error. The ideal minimizer is the conditional mean
    endpoint difference at the interpolated state. Integrating dZt/dt=v(Zt,t) from
    the source sample induces a new endpoint coupling. Reflow optionally trains another
    rectified flow on that coupling; endpoint-map distillation is a separate optional
    step. Rendered pages actually inspected: 4, 5, 6.'
- evidence_id: rectifiedflow-method-optimal-transport-analysis
  kind: primary_source
  reference: https://arxiv.org/pdf/2505.19712v3
  locator: Sections 3.1–3.2, PDF pp. 5–6; Section 4.1, Proposition 10, Theorem 11
    and Remark 12, PDF pp. 7–8
  accessed_at: '2026-10-11T04:40:15Z'
  snapshot_sha256: 8aca06c9392765e6f4a196ca011576b126a9dd01eee6f7a586fbf296facad6c3
  support: supports
  summary: 'A later analysis of gradient-constrained rectification exhibits nonoptimal
    zero-loss fixed points with disconnected intermediate supports; its corrected
    equivalence theorem additionally requires full intermediate support, rectifiability
    and smooth potential fields. Straightness or imposing a potential alone does not
    establish globally optimal transport. This supports the stated limitation; it
    is not falsely recorded as a refutation of the original model identity. Rendered
    pages actually inspected: 7, 8.'
- evidence_id: consistencymodel-method
  kind: primary_source
  reference: https://proceedings.mlr.press/v202/song23a/song23a.pdf
  locator: Section 3, equation (5), Algorithm 1 and boundary-condition discussion,
    PDF pp. 3–4; Sections 4–5, Algorithms 2–3, PDF pp. 4–6
  accessed_at: '2026-10-11T04:35:23Z'
  snapshot_sha256: 8f65127c770a8e8994777010ed36dfcf64fc38f840042778eef7fe8ab2c12e10
  support: supports
  summary: 'A consistency function assigns the same low-noise endpoint to states on
    the same probability-flow trajectory. The paper''s skip-connected parameterization
    combines an input skip term and a learned term whose coefficients enforce the
    identity boundary at the minimum noise level. Generation applies the model to
    high-noise input; multistep generation interleaves model evaluation with noise
    injection. The original paper describes both diffusion-model-assisted distillation
    and direct consistency training with shared-noise adjacent perturbations of a
    data sample. Rendered pages actually inspected: 3, 4, 5, 6.'
- evidence_id: consistencymodel-method-training-correction
  kind: primary_source
  reference: https://arxiv.org/pdf/2310.14189v1
  locator: Section 2, teacher versus inference EMA, PDF p. 3; Section 3.2, Proposition
    1 and equations (6)–(7), PDF pp. 5–6
  accessed_at: '2026-10-11T04:40:16Z'
  snapshot_sha256: 2c77b5ae689be478b2afe9f3a8149b4e4755a357c67be0a0c96fa06ac0d45b31
  support: supports
  summary: 'The later paper gives a point-mass-data counterexample in which the limiting
    consistency-training/matching objective with unequal teacher and student parameters
    loses dependence on the data location. It motivates zero teacher EMA decay, with
    a stop-gradient teacher sharing current student parameters, for consistency training;
    this is distinct from averaging the model used for inference. This supports the
    stated limitation; it is not falsely recorded as a refutation of the original
    model identity. Rendered pages actually inspected: 4, 5, 6, 7, 8.'
- evidence_id: improvedconsistencytraining-method
  kind: primary_source
  reference: https://arxiv.org/pdf/2310.14189v1
  locator: Section 2, equations (3)–(5), PDF p. 3; Table 1 and Sections 3.1–3.5, equations
    (6)–(10), PDF pp. 4–8
  accessed_at: '2026-10-11T04:40:16Z'
  snapshot_sha256: 2c77b5ae689be478b2afe9f3a8149b4e4755a357c67be0a0c96fa06ac0d45b31
  support: supports
  summary: 'The student and stop-gradient teacher evaluate the same data sample plus
    the same Gaussian noise scaled to adjacent noise levels, with teacher EMA decay
    set to zero. The revised objective uses a Pseudo-Huber discrepancy and inverse
    adjacent-noise-gap weighting. Training samples adjacent intervals according to
    discretized lognormal masses and doubles the interval count at scheduled milestones
    up to a cap. Noise-embedding sensitivity and shared dropout randomness are additional
    prescribed training choices; the separate inference-time EMA remains distinct.
    Rendered pages actually inspected: 4, 5, 6, 7, 8.'
assessments:
- assessment_id: flowmatching-method
  area: evidence
  topic: Identity, definition, mechanism, correction scope and mapping direction
  outcome: supported
  target_ids:
  - AIMech:FlowMatching
  evidence_ids:
  - flowmatching-method
  - identity-search
  - mapping
  summary: The 442 pinned AIO identities and 90 preceding native identities, including
    scoped synonyms and aliases, were compared alongside ignored-inclusive searches
    of both checkouts. This record denotes the general probability-path training method
    of Lipman and colleagues. Conditional flow matching is its tractable objective
    construction, not an asserted synonym for every use of the general method. Straight
    conditional paths overlap with the training construction used in rectified flow;
    that overlap does not make the general path family and the rectification/reflow
    procedure identical.
  details: The equality of conditional and marginal objective gradients is conditional
    on the paper's density and integrability assumptions, including positive path
    density in Theorem 2; finite neural training does not guarantee the ideal field.
    The Gaussian construction with positive terminal noise leaves a smoothed approximation
    to the data distribution. Training without ODE simulation does not remove numerical
    ODE solving from sampling. The optimal-transport conditional Gaussian path in
    Section 4 does not imply that the resulting marginal flow is a globally optimal
    transport map, as the paper explicitly notes on PDF p. 6. No benchmark superiority,
    universal sampling-step count or independently checked theorem proof is asserted.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: 'The source-defined abstraction level: velocity-learning algorithm,
      endpoint-map model family or training procedure.'
    evidence_ids:
    - flowmatching-method
  - name: mapping-direction
    value: related_match to AIO:RegressionAnalysis
    definition: Flow matching uses regression of time- and state-dependent velocity
      targets. RegressionAnalysis describes the corresponding statistical estimation
      task, whereas this local concept denotes a generative training algorithm; the
      mapping does not assert an algorithm is a task.
    evidence_ids:
    - flowmatching-method
    - mapping
- assessment_id: rectifiedflow-method
  area: evidence
  topic: Identity, definition, mechanism, correction scope and mapping direction
  outcome: supported
  target_ids:
  - AIMech:RectifiedFlow
  evidence_ids:
  - rectifiedflow-method
  - identity-search
  - mapping
  - rectifiedflow-method-optimal-transport-analysis
  summary: The ignored-inclusive identity search covered both checkouts, all 442 AIO
    labels and scoped synonyms, and 90 preceding native identities. This record denotes
    the straight-interpolation regression and rectification procedure of Liu, Gong
    and Liu, including optional reflow. It overlaps with particular conditional flow-matching
    objectives, but does not denote every probability-path choice in flow matching,
    a particular trained image generator, or mandatory distillation.
  details: Marginal preservation and transport-cost statements concern ideal regression
    with a well-posed ODE, not arbitrary finite neural estimates or numerical solvers.
    Straight training interpolations do not make the learned marginal trajectories
    exactly straight; one-step accuracy is not universal. Reflow and distillation
    are optional. The original paper explicitly does not guarantee a globally cost-optimal
    coupling in general. Later analysis also gives nonoptimal zero-loss fixed points
    for a gradient-constrained rectification variant when required support or regularity
    assumptions are absent. The later optimal-transport counterexamples limit stronger
    equivalence claims; they do not refute the original least-squares construction.
    No executable solver, numerical benchmark or full proof verification is supplied.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: 'The source-defined abstraction level: velocity-learning algorithm,
      endpoint-map model family or training procedure.'
    evidence_ids:
    - rectifiedflow-method
  - name: mapping-direction
    value: related_match to AIO:RegressionAnalysis
    definition: The defining velocity-learning objective estimates conditional endpoint
      differences by least-squares regression. RegressionAnalysis is the related estimation
      task, while rectified flow is the transport-learning algorithm and may include
      iterative reflow; no task/algorithm subclass assertion is made.
    evidence_ids:
    - rectifiedflow-method
    - mapping
- assessment_id: consistencymodel-method
  area: evidence
  topic: Identity, definition, mechanism, correction scope and mapping direction
  outcome: supported
  target_ids:
  - AIMech:ConsistencyModel
  evidence_ids:
  - consistencymodel-method
  - identity-search
  - mapping
  - consistencymodel-method-training-correction
  summary: All 442 pinned AIO labels and scoped synonyms and 90 preceding native identities
    were checked, with ignored-inclusive text searches of both checkouts. The identity
    is the endpoint-map model family introduced by Song and colleagues, not generic
    logical consistency, a trained checkpoint, or one particular training loss. Original
    consistency distillation, original consistency training and improved consistency
    training are procedures for learning this family and are not aliases for the model
    family itself.
  details: The learned consistency model is not required to be invertible. Ideal probability-flow
    properties do not establish exact data recovery or perfect self-consistency for
    a finite trained model. The original direct consistency-training teacher uses
    EMA; the later inspected correction identifies a failure of its original asymptotic
    justification when teacher and student parameters differ. This record does not
    endorse that original training argument as generally valid. The correction concerns
    consistency training and does not remove EMA from all distillation procedures
    or from the separate inference-time averaged model. One-evaluation generation
    is an available procedure, not a universal image-quality guarantee. No benchmark
    reproduction or independently verified convergence proof is claimed.
  dimensions:
  - name: concept-kind
    value: model_family
    definition: 'The source-defined abstraction level: velocity-learning algorithm,
      endpoint-map model family or training procedure.'
    evidence_ids:
    - consistencymodel-method
  - name: mapping-direction
    value: broad_match to AIO:Model
    definition: The consistency-model family is a specific learned representation
      of a generative distribution/endpoint transformation, within the broader scope
      of AIO Model. The mapping does not assert equivalence to a distillation procedure
      or to an adversarial network.
    evidence_ids:
    - consistencymodel-method
    - mapping
- assessment_id: improvedconsistencytraining-method
  area: evidence
  topic: Identity, definition, mechanism, correction scope and mapping direction
  outcome: supported
  target_ids:
  - AIMech:ImprovedConsistencyTraining
  evidence_ids:
  - improvedconsistencytraining-method
  - identity-search
  - mapping
  summary: The identity search included 442 AIO records, 90 preceding native identities,
    all scoped synonyms and aliases, and ignored-inclusive text in both checkouts.
    This is the named improved consistency-training procedure, not the consistency-model
    family, the original EMA-teacher training procedure, diffusion-model distillation,
    or a particular iCT-deep architecture/checkpoint. The acronym is qualified to
    avoid claiming an unscoped abbreviation.
  details: Removing teacher EMA retains stop-gradient and does not remove inference-time
    parameter averaging; it is not a blanket recommendation to eliminate EMA from
    consistency distillation. The paper's counterexample diagnoses a flaw in an earlier
    asymptotic argument. Its correction and finite-noise curriculum do not establish
    universal finite-training convergence. Noise distribution, loss scale, discretization
    cap, dropout and embedding settings are choices evaluated in particular image-generation
    settings, not universal hyperparameters. The interval count doubles; the number
    of noise grid points is that count plus one. The record describes the inspected
    training procedure and retains DRAFT status; it does not reproduce performance
    comparisons, certify every proof, or identify all future variants with this version.
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: 'The source-defined abstraction level: velocity-learning algorithm,
      endpoint-map model family or training procedure.'
    evidence_ids:
    - improvedconsistencytraining-method
  - name: mapping-direction
    value: related_match to AIO:TrainingStrategy
    definition: The procedure is directly related to choosing how a model is trained.
      The pinned TrainingStrategy definition calls its subject a preprocessing, whereas
      iCT is the actual optimization/training procedure; related_match preserves this
      scope discrepancy instead of asserting an unqualified subclass relation. Distillation
      is not an equivalent target because this procedure learns directly from data
      without a separately pretrained diffusion teacher.
    evidence_ids:
    - improvedconsistencytraining-method
    - mapping
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:FlowMatching
  - AIMech:RectifiedFlow
  - AIMech:ConsistencyModel
  - AIMech:ImprovedConsistencyTraining
  evidence_ids:
  - identity-search
  - mapping
  - flowmatching-method
  - rectifiedflow-method
  - rectifiedflow-method-optimal-transport-analysis
  - consistencymodel-method
  - consistencymodel-method-training-correction
  - improvedconsistencytraining-method
  rationale: Retain flow matching as a general path-based velocity-training algorithm
    and rectified flow as straight-interpolation rectification with optional reflow.
    Their special-case overlap does not erase the scoped distinction. Retain the consistency
    endpoint-map family separately from the improved procedure used to train it.
- action: defer
  target_ids:
  - AIMech:FlowMatching
  - AIMech:RectifiedFlow
  - AIMech:ConsistencyModel
  - AIMech:ImprovedConsistencyTraining
  evidence_ids:
  - flowmatching-method
  - rectifiedflow-method
  - rectifiedflow-method-optimal-transport-analysis
  - consistencymodel-method
  - consistencymodel-method-training-correction
  - improvedconsistencytraining-method
  rationale: Conditional-objective variants, original CT/CD and gradient-constrained
    rectification need distinct identity and method assessments before standalone
    records. No exact-equivalence merge follows from shared objectives or reported
    sample quality.
limitations:
- Scientific adversarial self-review, not independent approval; all four records remain
  DRAFT.
- Original direct consistency-training theory is qualified by the inspected point-mass
  counterexample; teacher and inference EMA remain separate.
- Conditional optimal transport and trajectory straightness do not certify globally
  optimal marginal transport.
- No numerical benchmark reproduction or complete theorem-proof validation was performed.
- The first vendored-check attempt failed on sandbox DNS resolution. A network-enabled
  rerun passed against the pinned public CLAW revision; no governed artifact was changed.
- Exact follow-up query times were not retained; the discovery ledger preserves the
  known time bound and exact PDF access times.
- Discovery continues with unresolved leads; this pass is not a saturation claim.
tags:
- native-concepts
- primary-papers
- generative-methods
- theory-corrections
- self-review
- discovery-ongoing
```
