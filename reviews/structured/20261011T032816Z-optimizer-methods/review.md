# Scientific self-review of twelve native optimizer methods

- Review: 20261011T032816Z-optimizer-methods
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T03:28:16Z
- Finished UTC: 2026-10-11T03:28:16Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The twelve narrow optimizer definitions, update mechanisms and identity distinctions are supported by inspected versioned official documentation. Conservative AIO mappings preserve the task/algorithm abstraction difference. No actionable unresolved finding was identified in this scope.

## Scope And Provenance

Identity, definition, documented update rule, implementation caveats and AIO mapping direction for twelve newly added optimizers.

Selection: Exactly the twelve added IDs in research/discovery/20261011T032615Z-optimizer-methods.json; no sampling.
Coverage: full; 12 reviewed / 12 in the declared population.
Source: working_tree at Git base 6be8b2a9ec84fab84393b33f4e5d474b3325f7f2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:AdamW | data/curated/AdamW.yaml | maintained | AdamW |
| AIMech:Adagrad | data/curated/Adagrad.yaml | maintained | Adagrad |
| AIMech:RMSprop | data/curated/RMSprop.yaml | maintained | RMSprop |
| AIMech:Adadelta | data/curated/Adadelta.yaml | maintained | Adadelta |
| AIMech:Adafactor | data/curated/Adafactor.yaml | maintained | Adafactor |
| AIMech:AdaMax | data/curated/AdaMax.yaml | maintained | AdaMax |
| AIMech:NAdam | data/curated/NAdam.yaml | maintained | NAdam |
| AIMech:RAdam | data/curated/RAdam.yaml | maintained | Rectified Adam |
| AIMech:AveragedStochasticGradientDescent | data/curated/AveragedStochasticGradientDescent.yaml | maintained | Averaged stochastic gradient descent |
| AIMech:LBFGS | data/curated/LBFGS.yaml | maintained | Limited-memory BFGS |
| AIMech:ResilientBackpropagation | data/curated/ResilientBackpropagation.yaml | maintained | Resilient backpropagation |
| AIMech:Muon | data/curated/Muon.yaml | maintained | Muon optimizer |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| python -m aimech check-source | passed | True | AIMech:AdamW, AIMech:Adagrad, AIMech:RMSprop, AIMech:Adadelta, AIMech:Adafactor, AIMech:AdaMax, AIMech:NAdam, AIMech:RAdam, AIMech:AveragedStochasticGradientDescent, AIMech:LBFGS, AIMech:ResilientBackpropagation, AIMech:Muon | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a |
| python -m aimech validate | passed | True | AIMech:AdamW, AIMech:Adagrad, AIMech:RMSprop, AIMech:Adadelta, AIMech:Adafactor, AIMech:AdaMax, AIMech:NAdam, AIMech:RAdam, AIMech:AveragedStochasticGradientDescent, AIMech:LBFGS, AIMech:ResilientBackpropagation, AIMech:Muon | Checked 442 record(s); 0 failed. |
| python -m aimech seed --check | passed | True | AIMech:AdamW, AIMech:Adagrad, AIMech:RMSprop, AIMech:Adadelta, AIMech:Adafactor, AIMech:AdaMax, AIMech:NAdam, AIMech:RAdam, AIMech:AveragedStochasticGradientDescent, AIMech:LBFGS, AIMech:ResilientBackpropagation, AIMech:Muon | AIO: 442 records; 0 missing, 0 changed, 0 unexpected. |
| python scripts/record_review.py check | passed | True | AIMech:AdamW, AIMech:Adagrad, AIMech:RMSprop, AIMech:Adadelta, AIMech:Adafactor, AIMech:AdaMax, AIMech:NAdam, AIMech:RAdam, AIMech:AveragedStochasticGradientDescent, AIMech:LBFGS, AIMech:ResilientBackpropagation, AIMech:Muon | {<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 3,<br>  "coverage": "declared_scopes_only"<br>} |
| PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src python -m aimech validate-curated | passed | True | AIMech:AdamW, AIMech:Adagrad, AIMech:RMSprop, AIMech:Adadelta, AIMech:Adafactor, AIMech:AdaMax, AIMech:NAdam, AIMech:RAdam, AIMech:AveragedStochasticGradientDescent, AIMech:LBFGS, AIMech:ResilientBackpropagation, AIMech:Muon | Checked 56 curated records; 0 errors. |
| PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just check | passed | True | AIMech:AdamW, AIMech:Adagrad, AIMech:RMSprop, AIMech:Adadelta, AIMech:Adafactor, AIMech:AdaMax, AIMech:NAdam, AIMech:RAdam, AIMech:AveragedStochasticGradientDescent, AIMech:LBFGS, AIMech:ResilientBackpropagation, AIMech:Muon | 209 passed, 3 skipped; 442 AIO records valid and exactly reproducible; 56 native records valid; 7 history records valid; 3 preceding review bundles valid. |
| PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just vendored-check | passed | True | AIMech:AdamW, AIMech:Adagrad, AIMech:RMSprop, AIMech:Adadelta, AIMech:Adafactor, AIMech:AdaMax, AIMech:NAdam, AIMech:RAdam, AIMech:AveragedStochasticGradientDescent, AIMech:LBFGS, AIMech:ResilientBackpropagation, AIMech:Muon | All 22 governed artifacts match the immutable public CLAW pin. |

## Scientific And Domain Assessments

### Optimizer identity and documented update mechanism

evidence: supported. Targets: AIMech:AdamW.

Decoupled weight decay distinguishes AdamW from Adam with a penalty included in its gradient moments. It is an optimization algorithm, not a new model architecture.

The cited implementation also offers an optional AMSGrad variant; that option is not required by the AdamW definition. No universal convergence or performance advantage is asserted.

### Optimizer identity and documented update mechanism

evidence: supported. Targets: AIMech:Adagrad.

This record covers the commonly implemented diagonal Adagrad algorithm. Its cumulative accumulator differs from the exponentially decayed squared-gradient estimate in RMSprop.

The definition is scoped to the inspected diagonal implementation, not every full-matrix adaptive subgradient formulation. Initialization, learning-rate decay and regularization settings are implementation choices; no benchmark or convergence claim is made.

### Optimizer identity and documented update mechanism

evidence: supported. Targets: AIMech:RMSprop.

RMSprop decays older squared-gradient information, unlike cumulative Adagrad. Centered and momentum settings are variants within this scoped record.

The cited implementation adds epsilon after the square root and documents a different ordering in TensorFlow. No universal improvement or convergence guarantee is inferred from implementation documentation.

### Optimizer identity and documented update mechanism

evidence: supported. Targets: AIMech:Adadelta.

The additional update-history scale distinguishes Adadelta from RMSprop and from Adagrad's cumulative accumulator.

The inspected implementation includes a learning-rate multiplier; this record does not describe it as parameter-free. No convergence theorem or comparative benchmark result is curated.

### Optimizer identity and documented update mechanism

evidence: supported. Targets: AIMech:Adafactor.

Adafactor factors the adaptive second-moment state; it is not low-rank adaptation of model weights such as LoRA. Vector parameters use an unfactored second-moment estimate.

PyTorch documents differences from the original paper in learning-rate control and epsilon handling; the record does not equate their exact update equations. No measured memory reduction, benchmark superiority or convergence guarantee is asserted.

### Optimizer identity and documented update mechanism

evidence: supported. Targets: AIMech:AdaMax.

AdaMax changes Adam's normalization statistic and is retained as a distinct algorithm; it is not an alias for Adam.

Epsilon placement follows the cited PyTorch implementation. No universal convergence or benchmark advantage is asserted.

### Optimizer identity and documented update mechanism

evidence: supported. Targets: AIMech:NAdam.

The Nesterov-style combination distinguishes NAdam from Adam. Optional decoupled weight decay is not required for this identity.

The source specifies a momentum schedule and an optional NAdamW configuration; other implementations need separate exact-equation comparison. No comparative performance or convergence claim is curated.

### Optimizer identity and documented update mechanism

evidence: supported. Targets: AIMech:RAdam.

RAdam's rectification and early-step branch distinguish it from unmodified Adam and from weight-decay decoupling alone.

The implementation exposes coupled and decoupled weight-decay choices; these are distinct from the rectification mechanism. The record asserts the update procedure, not a universal variance reduction, convergence result or benchmark advantage.

### Optimizer identity and documented update mechanism

evidence: supported. Targets: AIMech:AveragedStochasticGradientDescent.

ASGD adds parameter-iterate averaging to stochastic gradient descent. It is not the same operation as averaging gradients in a momentum buffer.

This record covers iterate averaging in the cited ASGD implementation, not every stochastic weight averaging schedule. No convergence rate or generalization advantage is asserted.

### Optimizer identity and documented update mechanism

evidence: supported. Targets: AIMech:LBFGS.

L-BFGS is an optimization algorithm, not a neural architecture; bounded curvature history distinguishes it from full-memory BFGS.

The cited implementation imposes parameter-group and device restrictions that are not mathematical requirements of every L-BFGS implementation. Line-search choices and termination tolerances affect a particular run; no universal convergence or speed guarantee is curated.

### Optimizer identity and documented update mechanism

evidence: supported. Targets: AIMech:ResilientBackpropagation.

Rprop is an optimizer using backpropagated gradients, not the backpropagation procedure for computing those gradients. Update magnitude is controlled by step size rather than current gradient magnitude.

Sign-reversal handling is scoped to the inspected PyTorch variant; other Rprop variants require comparison. No comparative speed or convergence claim is asserted.

### Optimizer identity and documented update mechanism

evidence: supported. Targets: AIMech:Muon.

Muon is a matrix-update optimizer distinct from coordinatewise Adam-family scaling. The name here denotes the optimization algorithm, not unrelated uses of the word muon.

The cited implementation is scoped to two-dimensional hidden-layer parameters and directs other parameters to a standard optimizer. The implementation provides alternative shape-scaling conventions; no universal exact orthogonality, convergence or performance guarantee is asserted.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:AdamW, AIMech:Adagrad, AIMech:RMSprop, AIMech:Adadelta, AIMech:Adafactor, AIMech:AdaMax, AIMech:NAdam, AIMech:RAdam, AIMech:AveragedStochasticGradientDescent, AIMech:LBFGS, AIMech:ResilientBackpropagation, AIMech:Muon. Retain distinctions in accumulation/decay, momentum, infinity-norm scaling, rectification, decoupled decay, second-moment factorization, iterate averaging, curvature history, sign-based steps and matrix orthogonalization. A shared training purpose does not imply algorithm equivalence.
- defer: AIMech:AdamW, AIMech:Adagrad, AIMech:RMSprop, AIMech:Adadelta, AIMech:Adafactor, AIMech:AdaMax, AIMech:NAdam, AIMech:RAdam, AIMech:AveragedStochasticGradientDescent, AIMech:LBFGS, AIMech:ResilientBackpropagation, AIMech:Muon. Do not infer a complete optimizer taxonomy or split every implementation flag into a new concept. AMSGrad and other exposed neighbors require their own evidence/identity assessments.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity-search | research/discovery/20261011T032615Z-optimizer-methods.json | supports | All twelve selected identities are distinct from the existing AIO and native identities. Raw textual hits are previous leads or related-optimizer mentions. |
| mapping-scope | data/aio/TrainingStrategy.yaml; definition, name and scoped synonyms | supports | TrainingStrategy uses a preprocessing genus; the new algorithm mappings are related_match, not inferred optimizer subclass edges. |
| adamw-method | https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/adamw.py; AdamW.__doc__, algorithm lines 61–97 | supports | Inspected pinned official documentation/update implementation: Parameters receive a weight-decay shrinkage step, while first and second gradient moments are updated from the objective gradient and used for the adaptive step. |
| adagrad-method | https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/adagrad.py; Adagrad.__doc__, diagonal update algorithm lines 193–218 | supports | Inspected pinned official documentation/update implementation: The diagonal variant accumulates squared gradients over iterations and divides the current gradient by the square root of that accumulator plus a numerical stabilizer. |
| rmsprop-method | https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/rmsprop.py; RMSprop.__doc__, algorithm and implementation note lines 200–243 | supports | Inspected pinned official documentation/update implementation: An exponential moving average of squared gradients supplies the update denominator; the documented centered option subtracts a squared mean-gradient estimate, and momentum is optional. |
| adadelta-method | https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/adadelta.py; Adadelta.__doc__, algorithm lines 192–219 | supports | Inspected pinned official documentation/update implementation: The update multiplies the gradient by the stabilized root-mean-square of prior updates divided by the stabilized root-mean-square of current gradient history, then updates the squared-update average. |
| adafactor-method | https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/_adafactor.py; Adafactor.__doc__, algorithm lines 178–224 and implementation differences lines 229–285 | supports | Inspected pinned official documentation/update implementation: For matrix parameters, row and column statistics reconstruct a factored second-moment estimate used to normalize gradients; the inspected implementation also clips update RMS and scales steps using parameter RMS. |
| adamax-method | https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/adamax.py; Adamax.__doc__, algorithm lines 178–203 | supports | Inspected pinned official documentation/update implementation: The first-moment estimate is bias-corrected, while the denominator takes the coordinatewise maximum of the decayed prior scale and the current absolute gradient with the implementation's stabilizer. |
| nadam-method | https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/nadam.py; NAdam.__doc__, algorithm lines 214–252 and options lines 257–266 | supports | Inspected pinned official documentation/update implementation: The documented update combines a scheduled, bias-adjusted first-moment term with a current-gradient term and divides the combination by a stabilized, bias-corrected second-moment scale. |
| radam-method | https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/radam.py; RAdam.__doc__, algorithm lines 176–218 and weight-decay note lines 220–225 | supports | Inspected pinned official documentation/update implementation: The cited implementation computes a rectification term when its effective-history statistic exceeds five; before that threshold it takes a bias-corrected first-moment step without adaptive second-moment scaling. |
| averagedstochasticgradientdescent-method | https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/asgd.py; ASGD class documentation lines 174–200 and _single_tensor_asgd averaging/update lines 248–273 | supports | Inspected pinned official documentation/update implementation: The inspected implementation updates the current parameters by a scheduled gradient step and maintains an auxiliary parameter average, with averaging weights controlled by the iteration count and a configurable starting point. |
| lbfgs-method | https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/lbfgs.py; LBFGS class documentation lines 183–220 and step curvature-history/two-loop update lines 360–408 | supports | Inspected pinned official documentation/update implementation: The implementation retains a bounded set of curvature pairs and applies a two-loop recursion to obtain a direction from the gradient without storing a dense inverse Hessian. |
| resilientbackpropagation-method | https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/rprop.py; Rprop.__doc__, algorithm lines 169–203 | supports | Inspected pinned official documentation/update implementation: Repeated gradient signs increase a coordinate's bounded step size, while a sign reversal decreases it; in the cited variant the reversal also suppresses that coordinate's current update. |
| muon-method | https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/_muon.py; Muon.__doc__, algorithm and orthogonalization lines 207–260; supported-parameter note lines 264–265 | supports | Inspected pinned official documentation/update implementation: The inspected implementation forms a momentum update, optionally uses a Nesterov combination, applies iterative matrix orthogonalization, and scales the resulting update for the parameter shape while applying decoupled weight decay. |

## Limits And Additional Notes

- This is scientific self-review of documented mechanisms, not independent peer review or experimental replication.
- Implementation versions can differ from original papers; documented Adafactor, RMSprop, Rprop and Muon scope limits remain explicit.
- The review timestamps record post-inspection assessment; evidence reading and record writes occurred earlier in the same documented session.
- All records remain DRAFT. Twelve new concepts were found; literature discovery remains active with nonempty pending leads.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T032816Z-optimizer-methods
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of twelve native optimizer methods
started_at: '2026-10-11T03:28:16Z'
finished_at: '2026-10-11T03:28:16Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The same agent researched, wrote and reviewed these records.
    This is not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The twelve narrow optimizer definitions, update mechanisms and identity distinctions
  are supported by inspected versioned official documentation. Conservative AIO mappings
  preserve the task/algorithm abstraction difference. No actionable unresolved finding
  was identified in this scope.
source:
  git_revision: 6be8b2a9ec84fab84393b33f4e5d474b3325f7f2
  state: working_tree
  inputs:
  - path: data/curated/AdaMax.yaml
    sha256: 478964da4c96b67798d39e17f2a8ac75fe07c91f121c98fd59a41441da2cf3e3
    role: target
  - path: data/curated/Adadelta.yaml
    sha256: 0995c840d5eaaa080881e3cbe2d891dff4903ea37d4b02d52f3f02920bfc626a
    role: target
  - path: data/curated/Adafactor.yaml
    sha256: 336b6d7a1be9402d4719cec42af3a6ab7ff85cf387823278001ecddc72dc6ad9
    role: target
  - path: data/curated/Adagrad.yaml
    sha256: a17b7f6adf2a89be5709802bb63d4479866c17c77645144418da24d3e5f3dcc8
    role: target
  - path: data/curated/AdamW.yaml
    sha256: 5a851955d9435629b76cb28e95d84ab6c1db16aa35df9b485254c9c76c025948
    role: target
  - path: data/curated/AveragedStochasticGradientDescent.yaml
    sha256: 8a57b2cbee2867e7511f114bf155fbffd632474f0b2c6433f7a28a90bf729d85
    role: target
  - path: data/curated/LBFGS.yaml
    sha256: bfd719c9faecc8a7e550beaab4319711af000817c6e659f919292249e923e41f
    role: target
  - path: data/curated/Muon.yaml
    sha256: 144f28dd1ef6b61afe6182227e9cdd21aee1fe9182fb161a6b7904269a0b41f1
    role: target
  - path: data/curated/NAdam.yaml
    sha256: f47e61fba3e2b5a64adaaeae123ff15a169e8e103b57bbb92cde09549e60cbd2
    role: target
  - path: data/curated/RAdam.yaml
    sha256: fc46ca6dbf5a64c1c7da89a61dedfa2922fcce8f1742d317f3ea9b358c166a68
    role: target
  - path: data/curated/RMSprop.yaml
    sha256: 25fe81add637f0323634a0860a706a201a5927826afd6783738aca2c80a7c49d
    role: target
  - path: data/curated/ResilientBackpropagation.yaml
    sha256: e0fd7cf20b05fc93ac579d5a396168891efaf96f9b31948c7152f6207f9b8e18
    role: target
  - path: research/discovery/20261011T032615Z-optimizer-methods.json
    sha256: c020eea5717a9b67f8e0cf378bc87e5451e5a036cec175cd39e220ee9defba33
    role: context
  - path: sources/aio/aio.json
    sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
    role: context
  - path: sources/aio/source.yaml
    sha256: a12f1e974c25fab2ebff5e44150fb86f64399471accdf0baeafd986f00e6f345
    role: context
  - path: src/aimech/curated.py
    sha256: 1efe838d99526a85e5b678a70bad7b796edfcc922e7b912a9d4592da78843bbe
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: 529cb70f3fa95580d6197c1581e0b3ad62c17f128d3ed1ba848f54d184f4e312
    role: context
targets:
- target_id: AIMech:AdamW
  path: data/curated/AdamW.yaml
  label: AdamW
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AdamW.yaml
    role: maintained concept, claim evidence and AIO mapping
- target_id: AIMech:Adagrad
  path: data/curated/Adagrad.yaml
  label: Adagrad
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Adagrad.yaml
    role: maintained concept, claim evidence and AIO mapping
- target_id: AIMech:RMSprop
  path: data/curated/RMSprop.yaml
  label: RMSprop
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RMSprop.yaml
    role: maintained concept, claim evidence and AIO mapping
- target_id: AIMech:Adadelta
  path: data/curated/Adadelta.yaml
  label: Adadelta
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Adadelta.yaml
    role: maintained concept, claim evidence and AIO mapping
- target_id: AIMech:Adafactor
  path: data/curated/Adafactor.yaml
  label: Adafactor
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Adafactor.yaml
    role: maintained concept, claim evidence and AIO mapping
- target_id: AIMech:AdaMax
  path: data/curated/AdaMax.yaml
  label: AdaMax
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AdaMax.yaml
    role: maintained concept, claim evidence and AIO mapping
- target_id: AIMech:NAdam
  path: data/curated/NAdam.yaml
  label: NAdam
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NAdam.yaml
    role: maintained concept, claim evidence and AIO mapping
- target_id: AIMech:RAdam
  path: data/curated/RAdam.yaml
  label: Rectified Adam
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RAdam.yaml
    role: maintained concept, claim evidence and AIO mapping
- target_id: AIMech:AveragedStochasticGradientDescent
  path: data/curated/AveragedStochasticGradientDescent.yaml
  label: Averaged stochastic gradient descent
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AveragedStochasticGradientDescent.yaml
    role: maintained concept, claim evidence and AIO mapping
- target_id: AIMech:LBFGS
  path: data/curated/LBFGS.yaml
  label: Limited-memory BFGS
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LBFGS.yaml
    role: maintained concept, claim evidence and AIO mapping
- target_id: AIMech:ResilientBackpropagation
  path: data/curated/ResilientBackpropagation.yaml
  label: Resilient backpropagation
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ResilientBackpropagation.yaml
    role: maintained concept, claim evidence and AIO mapping
- target_id: AIMech:Muon
  path: data/curated/Muon.yaml
  label: Muon optimizer
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/Muon.yaml
    role: maintained concept, claim evidence and AIO mapping
scope:
  description: Identity, definition, documented update rule, implementation caveats
    and AIO mapping direction for twelve newly added optimizers.
  selection: Exactly the twelve added IDs in research/discovery/20261011T032615Z-optimizer-methods.json;
    no sampling.
  coverage: full
  population_size: 12
  reviewed_target_ids:
  - AIMech:AdamW
  - AIMech:Adagrad
  - AIMech:RMSprop
  - AIMech:Adadelta
  - AIMech:Adafactor
  - AIMech:AdaMax
  - AIMech:NAdam
  - AIMech:RAdam
  - AIMech:AveragedStochasticGradientDescent
  - AIMech:LBFGS
  - AIMech:ResilientBackpropagation
  - AIMech:Muon
  exclusions:
  - target: The 44 preceding native and 442 generated AIO concepts
    reason: Used for identity and mapping context, not a new claim-by-claim review.
  - target: General convergence, comparative efficiency and benchmark results
    reason: No such performance or theorem claims were curated or experimentally tested.
checks:
- check_id: required-0
  name: python -m aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:AdamW
  - AIMech:Adagrad
  - AIMech:RMSprop
  - AIMech:Adadelta
  - AIMech:Adafactor
  - AIMech:AdaMax
  - AIMech:NAdam
  - AIMech:RAdam
  - AIMech:AveragedStochasticGradientDescent
  - AIMech:LBFGS
  - AIMech:ResilientBackpropagation
  - AIMech:Muon
  command: python -m aimech check-source
  exit_code: 0
  expected_exit_code: 0
  summary: Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a
- check_id: required-1
  name: python -m aimech validate
  status: passed
  required: true
  target_ids:
  - AIMech:AdamW
  - AIMech:Adagrad
  - AIMech:RMSprop
  - AIMech:Adadelta
  - AIMech:Adafactor
  - AIMech:AdaMax
  - AIMech:NAdam
  - AIMech:RAdam
  - AIMech:AveragedStochasticGradientDescent
  - AIMech:LBFGS
  - AIMech:ResilientBackpropagation
  - AIMech:Muon
  command: python -m aimech validate
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 record(s); 0 failed.
- check_id: required-2
  name: python -m aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:AdamW
  - AIMech:Adagrad
  - AIMech:RMSprop
  - AIMech:Adadelta
  - AIMech:Adafactor
  - AIMech:AdaMax
  - AIMech:NAdam
  - AIMech:RAdam
  - AIMech:AveragedStochasticGradientDescent
  - AIMech:LBFGS
  - AIMech:ResilientBackpropagation
  - AIMech:Muon
  command: python -m aimech seed --check
  exit_code: 0
  expected_exit_code: 0
  summary: 'AIO: 442 records; 0 missing, 0 changed, 0 unexpected.'
- check_id: required-3
  name: python scripts/record_review.py check
  status: passed
  required: true
  target_ids:
  - AIMech:AdamW
  - AIMech:Adagrad
  - AIMech:RMSprop
  - AIMech:Adadelta
  - AIMech:Adafactor
  - AIMech:AdaMax
  - AIMech:NAdam
  - AIMech:RAdam
  - AIMech:AveragedStochasticGradientDescent
  - AIMech:LBFGS
  - AIMech:ResilientBackpropagation
  - AIMech:Muon
  command: python scripts/record_review.py check
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 3,\n\
    \  \"coverage\": \"declared_scopes_only\"\n}"
- check_id: curated
  name: PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src python -m aimech
    validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:AdamW
  - AIMech:Adagrad
  - AIMech:RMSprop
  - AIMech:Adadelta
  - AIMech:Adafactor
  - AIMech:AdaMax
  - AIMech:NAdam
  - AIMech:RAdam
  - AIMech:AveragedStochasticGradientDescent
  - AIMech:LBFGS
  - AIMech:ResilientBackpropagation
  - AIMech:Muon
  command: PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src python -m
    aimech validate-curated
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 56 curated records; 0 errors.
- check_id: quality
  name: PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just check
  status: passed
  required: true
  target_ids:
  - AIMech:AdamW
  - AIMech:Adagrad
  - AIMech:RMSprop
  - AIMech:Adadelta
  - AIMech:Adafactor
  - AIMech:AdaMax
  - AIMech:NAdam
  - AIMech:RAdam
  - AIMech:AveragedStochasticGradientDescent
  - AIMech:LBFGS
  - AIMech:ResilientBackpropagation
  - AIMech:Muon
  command: PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just check
  exit_code: 0
  expected_exit_code: 0
  summary: 209 passed, 3 skipped; 442 AIO records valid and exactly reproducible;
    56 native records valid; 7 history records valid; 3 preceding review bundles valid.
- check_id: governance
  name: PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:AdamW
  - AIMech:Adagrad
  - AIMech:RMSprop
  - AIMech:Adadelta
  - AIMech:Adafactor
  - AIMech:AdaMax
  - AIMech:NAdam
  - AIMech:RAdam
  - AIMech:AveragedStochasticGradientDescent
  - AIMech:LBFGS
  - AIMech:ResilientBackpropagation
  - AIMech:Muon
  command: PYTHONPATH=/private/tmp/aimech-concept-discovery-20261010/src UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv
    UV_CACHE_DIR=/private/tmp/aimech-uv-cache UV_NO_SYNC=1 just vendored-check
  exit_code: 0
  expected_exit_code: 0
  summary: All 22 governed artifacts match the immutable public CLAW pin.
evidence:
- evidence_id: identity-search
  kind: search
  reference: research/discovery/20261011T032615Z-optimizer-methods.json
  accessed_at: '2026-10-11T03:28:16Z'
  support: supports
  summary: All twelve selected identities are distinct from the existing AIO and native
    identities. Raw textual hits are previous leads or related-optimizer mentions.
  search_scope: Both checkouts searched with rg --no-ignore --hidden -l -i -w -F,
    including ignored and hidden files. Normalized names, aliases and all AIO scoped
    synonyms compared across 442 AIO and 44 preceding native records.
- evidence_id: mapping-scope
  kind: record_content
  reference: data/aio/TrainingStrategy.yaml
  locator: definition, name and scoped synonyms
  accessed_at: '2026-10-11T03:28:16Z'
  support: supports
  summary: TrainingStrategy uses a preprocessing genus; the new algorithm mappings
    are related_match, not inferred optimizer subclass edges.
- evidence_id: adamw-method
  kind: primary_source
  reference: https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/adamw.py
  locator: AdamW.__doc__, algorithm lines 61–97
  accessed_at: '2026-10-11T03:19:24Z'
  snapshot_sha256: 3112d8799ef9ab608b855a5708087d5576971463923c41d4a6a227006871f551
  support: supports
  summary: 'Inspected pinned official documentation/update implementation: Parameters
    receive a weight-decay shrinkage step, while first and second gradient moments
    are updated from the objective gradient and used for the adaptive step.'
- evidence_id: adagrad-method
  kind: primary_source
  reference: https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/adagrad.py
  locator: Adagrad.__doc__, diagonal update algorithm lines 193–218
  accessed_at: '2026-10-11T03:19:24Z'
  snapshot_sha256: 8cdb9ea6c999615837165a00f9ed82b17eb8f59c3352d9b626f8ce5ddcc6b0fa
  support: supports
  summary: 'Inspected pinned official documentation/update implementation: The diagonal
    variant accumulates squared gradients over iterations and divides the current
    gradient by the square root of that accumulator plus a numerical stabilizer.'
- evidence_id: rmsprop-method
  kind: primary_source
  reference: https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/rmsprop.py
  locator: RMSprop.__doc__, algorithm and implementation note lines 200–243
  accessed_at: '2026-10-11T03:19:24Z'
  snapshot_sha256: b3aeb10dd57d05636ebd75b1f5c62c15979c5f911524d96e82673b86aafbef4f
  support: supports
  summary: 'Inspected pinned official documentation/update implementation: An exponential
    moving average of squared gradients supplies the update denominator; the documented
    centered option subtracts a squared mean-gradient estimate, and momentum is optional.'
- evidence_id: adadelta-method
  kind: primary_source
  reference: https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/adadelta.py
  locator: Adadelta.__doc__, algorithm lines 192–219
  accessed_at: '2026-10-11T03:19:24Z'
  snapshot_sha256: 6741996fc490731894c47a617d86447691247b3de95956348acb8e41d9637245
  support: supports
  summary: 'Inspected pinned official documentation/update implementation: The update
    multiplies the gradient by the stabilized root-mean-square of prior updates divided
    by the stabilized root-mean-square of current gradient history, then updates the
    squared-update average.'
- evidence_id: adafactor-method
  kind: primary_source
  reference: https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/_adafactor.py
  locator: Adafactor.__doc__, algorithm lines 178–224 and implementation differences
    lines 229–285
  accessed_at: '2026-10-11T03:19:24Z'
  snapshot_sha256: 1846d20844694cd312c6a20d2eaca3b62b679021f919b0a76545fd44d736f5cf
  support: supports
  summary: 'Inspected pinned official documentation/update implementation: For matrix
    parameters, row and column statistics reconstruct a factored second-moment estimate
    used to normalize gradients; the inspected implementation also clips update RMS
    and scales steps using parameter RMS.'
- evidence_id: adamax-method
  kind: primary_source
  reference: https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/adamax.py
  locator: Adamax.__doc__, algorithm lines 178–203
  accessed_at: '2026-10-11T03:19:24Z'
  snapshot_sha256: 4a069f9b4d56d4807960423ad77ec0f1a871c01b4c45e65a9b4a20022cd10b67
  support: supports
  summary: 'Inspected pinned official documentation/update implementation: The first-moment
    estimate is bias-corrected, while the denominator takes the coordinatewise maximum
    of the decayed prior scale and the current absolute gradient with the implementation''s
    stabilizer.'
- evidence_id: nadam-method
  kind: primary_source
  reference: https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/nadam.py
  locator: NAdam.__doc__, algorithm lines 214–252 and options lines 257–266
  accessed_at: '2026-10-11T03:19:24Z'
  snapshot_sha256: c23755060c4c7c9398d6d1e78e63b23e777bc8e701a6149431c43a1e2015f6ec
  support: supports
  summary: 'Inspected pinned official documentation/update implementation: The documented
    update combines a scheduled, bias-adjusted first-moment term with a current-gradient
    term and divides the combination by a stabilized, bias-corrected second-moment
    scale.'
- evidence_id: radam-method
  kind: primary_source
  reference: https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/radam.py
  locator: RAdam.__doc__, algorithm lines 176–218 and weight-decay note lines 220–225
  accessed_at: '2026-10-11T03:19:24Z'
  snapshot_sha256: a8776d8fee94519a385570290d8bdab86641957c5fba6694388e955b77b1d080
  support: supports
  summary: 'Inspected pinned official documentation/update implementation: The cited
    implementation computes a rectification term when its effective-history statistic
    exceeds five; before that threshold it takes a bias-corrected first-moment step
    without adaptive second-moment scaling.'
- evidence_id: averagedstochasticgradientdescent-method
  kind: primary_source
  reference: https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/asgd.py
  locator: ASGD class documentation lines 174–200 and _single_tensor_asgd averaging/update
    lines 248–273
  accessed_at: '2026-10-11T03:19:24Z'
  snapshot_sha256: 411369236bca1f875cf284df4a5fe17f4d7bfb50a5f9f171394766d2db1ef49a
  support: supports
  summary: 'Inspected pinned official documentation/update implementation: The inspected
    implementation updates the current parameters by a scheduled gradient step and
    maintains an auxiliary parameter average, with averaging weights controlled by
    the iteration count and a configurable starting point.'
- evidence_id: lbfgs-method
  kind: primary_source
  reference: https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/lbfgs.py
  locator: LBFGS class documentation lines 183–220 and step curvature-history/two-loop
    update lines 360–408
  accessed_at: '2026-10-11T03:19:24Z'
  snapshot_sha256: d15dff277f15e86a4e3666e1d048819a5ed25187c6f975c7c5a6b55cc2941ef3
  support: supports
  summary: 'Inspected pinned official documentation/update implementation: The implementation
    retains a bounded set of curvature pairs and applies a two-loop recursion to obtain
    a direction from the gradient without storing a dense inverse Hessian.'
- evidence_id: resilientbackpropagation-method
  kind: primary_source
  reference: https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/rprop.py
  locator: Rprop.__doc__, algorithm lines 169–203
  accessed_at: '2026-10-11T03:19:24Z'
  snapshot_sha256: d6cf29f225494b910a93a1e2902e866351135e2ca5d3c8eef020dd62e9ddc44e
  support: supports
  summary: 'Inspected pinned official documentation/update implementation: Repeated
    gradient signs increase a coordinate''s bounded step size, while a sign reversal
    decreases it; in the cited variant the reversal also suppresses that coordinate''s
    current update.'
- evidence_id: muon-method
  kind: primary_source
  reference: https://raw.githubusercontent.com/pytorch/pytorch/d38164a545b4a4e4e0cf73ce67173f70574890b6/torch/optim/_muon.py
  locator: Muon.__doc__, algorithm and orthogonalization lines 207–260; supported-parameter
    note lines 264–265
  accessed_at: '2026-10-11T03:19:24Z'
  snapshot_sha256: abaa98c693e0ece4f9143a6bdc49496c9c317d81b6af40939c0a197583492097
  support: supports
  summary: 'Inspected pinned official documentation/update implementation: The inspected
    implementation forms a momentum update, optionally uses a Nesterov combination,
    applies iterative matrix orthogonalization, and scales the resulting update for
    the parameter shape while applying decoupled weight decay.'
assessments:
- assessment_id: adamw-method
  area: evidence
  topic: Optimizer identity and documented update mechanism
  outcome: supported
  target_ids:
  - AIMech:AdamW
  evidence_ids:
  - adamw-method
  - identity-search
  - mapping-scope
  summary: Decoupled weight decay distinguishes AdamW from Adam with a penalty included
    in its gradient moments. It is an optimization algorithm, not a new model architecture.
  details: The cited implementation also offers an optional AMSGrad variant; that
    option is not required by the AdamW definition. No universal convergence or performance
    advantage is asserted.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Official algorithm docstring and relevant implementation inspected
      at a pinned PyTorch commit. This is not a performance experiment.
    evidence_ids:
    - adamw-method
- assessment_id: adagrad-method
  area: evidence
  topic: Optimizer identity and documented update mechanism
  outcome: supported
  target_ids:
  - AIMech:Adagrad
  evidence_ids:
  - adagrad-method
  - identity-search
  - mapping-scope
  summary: This record covers the commonly implemented diagonal Adagrad algorithm.
    Its cumulative accumulator differs from the exponentially decayed squared-gradient
    estimate in RMSprop.
  details: The definition is scoped to the inspected diagonal implementation, not
    every full-matrix adaptive subgradient formulation. Initialization, learning-rate
    decay and regularization settings are implementation choices; no benchmark or
    convergence claim is made.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Official algorithm docstring and relevant implementation inspected
      at a pinned PyTorch commit. This is not a performance experiment.
    evidence_ids:
    - adagrad-method
- assessment_id: rmsprop-method
  area: evidence
  topic: Optimizer identity and documented update mechanism
  outcome: supported
  target_ids:
  - AIMech:RMSprop
  evidence_ids:
  - rmsprop-method
  - identity-search
  - mapping-scope
  summary: RMSprop decays older squared-gradient information, unlike cumulative Adagrad.
    Centered and momentum settings are variants within this scoped record.
  details: The cited implementation adds epsilon after the square root and documents
    a different ordering in TensorFlow. No universal improvement or convergence guarantee
    is inferred from implementation documentation.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Official algorithm docstring and relevant implementation inspected
      at a pinned PyTorch commit. This is not a performance experiment.
    evidence_ids:
    - rmsprop-method
- assessment_id: adadelta-method
  area: evidence
  topic: Optimizer identity and documented update mechanism
  outcome: supported
  target_ids:
  - AIMech:Adadelta
  evidence_ids:
  - adadelta-method
  - identity-search
  - mapping-scope
  summary: The additional update-history scale distinguishes Adadelta from RMSprop
    and from Adagrad's cumulative accumulator.
  details: The inspected implementation includes a learning-rate multiplier; this
    record does not describe it as parameter-free. No convergence theorem or comparative
    benchmark result is curated.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Official algorithm docstring and relevant implementation inspected
      at a pinned PyTorch commit. This is not a performance experiment.
    evidence_ids:
    - adadelta-method
- assessment_id: adafactor-method
  area: evidence
  topic: Optimizer identity and documented update mechanism
  outcome: supported
  target_ids:
  - AIMech:Adafactor
  evidence_ids:
  - adafactor-method
  - identity-search
  - mapping-scope
  summary: Adafactor factors the adaptive second-moment state; it is not low-rank
    adaptation of model weights such as LoRA. Vector parameters use an unfactored
    second-moment estimate.
  details: PyTorch documents differences from the original paper in learning-rate
    control and epsilon handling; the record does not equate their exact update equations.
    No measured memory reduction, benchmark superiority or convergence guarantee is
    asserted.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Official algorithm docstring and relevant implementation inspected
      at a pinned PyTorch commit. This is not a performance experiment.
    evidence_ids:
    - adafactor-method
- assessment_id: adamax-method
  area: evidence
  topic: Optimizer identity and documented update mechanism
  outcome: supported
  target_ids:
  - AIMech:AdaMax
  evidence_ids:
  - adamax-method
  - identity-search
  - mapping-scope
  summary: AdaMax changes Adam's normalization statistic and is retained as a distinct
    algorithm; it is not an alias for Adam.
  details: Epsilon placement follows the cited PyTorch implementation. No universal
    convergence or benchmark advantage is asserted.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Official algorithm docstring and relevant implementation inspected
      at a pinned PyTorch commit. This is not a performance experiment.
    evidence_ids:
    - adamax-method
- assessment_id: nadam-method
  area: evidence
  topic: Optimizer identity and documented update mechanism
  outcome: supported
  target_ids:
  - AIMech:NAdam
  evidence_ids:
  - nadam-method
  - identity-search
  - mapping-scope
  summary: The Nesterov-style combination distinguishes NAdam from Adam. Optional
    decoupled weight decay is not required for this identity.
  details: The source specifies a momentum schedule and an optional NAdamW configuration;
    other implementations need separate exact-equation comparison. No comparative
    performance or convergence claim is curated.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Official algorithm docstring and relevant implementation inspected
      at a pinned PyTorch commit. This is not a performance experiment.
    evidence_ids:
    - nadam-method
- assessment_id: radam-method
  area: evidence
  topic: Optimizer identity and documented update mechanism
  outcome: supported
  target_ids:
  - AIMech:RAdam
  evidence_ids:
  - radam-method
  - identity-search
  - mapping-scope
  summary: RAdam's rectification and early-step branch distinguish it from unmodified
    Adam and from weight-decay decoupling alone.
  details: The implementation exposes coupled and decoupled weight-decay choices;
    these are distinct from the rectification mechanism. The record asserts the update
    procedure, not a universal variance reduction, convergence result or benchmark
    advantage.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Official algorithm docstring and relevant implementation inspected
      at a pinned PyTorch commit. This is not a performance experiment.
    evidence_ids:
    - radam-method
- assessment_id: averagedstochasticgradientdescent-method
  area: evidence
  topic: Optimizer identity and documented update mechanism
  outcome: supported
  target_ids:
  - AIMech:AveragedStochasticGradientDescent
  evidence_ids:
  - averagedstochasticgradientdescent-method
  - identity-search
  - mapping-scope
  summary: ASGD adds parameter-iterate averaging to stochastic gradient descent. It
    is not the same operation as averaging gradients in a momentum buffer.
  details: This record covers iterate averaging in the cited ASGD implementation,
    not every stochastic weight averaging schedule. No convergence rate or generalization
    advantage is asserted.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Official algorithm docstring and relevant implementation inspected
      at a pinned PyTorch commit. This is not a performance experiment.
    evidence_ids:
    - averagedstochasticgradientdescent-method
- assessment_id: lbfgs-method
  area: evidence
  topic: Optimizer identity and documented update mechanism
  outcome: supported
  target_ids:
  - AIMech:LBFGS
  evidence_ids:
  - lbfgs-method
  - identity-search
  - mapping-scope
  summary: L-BFGS is an optimization algorithm, not a neural architecture; bounded
    curvature history distinguishes it from full-memory BFGS.
  details: The cited implementation imposes parameter-group and device restrictions
    that are not mathematical requirements of every L-BFGS implementation. Line-search
    choices and termination tolerances affect a particular run; no universal convergence
    or speed guarantee is curated.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Official algorithm docstring and relevant implementation inspected
      at a pinned PyTorch commit. This is not a performance experiment.
    evidence_ids:
    - lbfgs-method
- assessment_id: resilientbackpropagation-method
  area: evidence
  topic: Optimizer identity and documented update mechanism
  outcome: supported
  target_ids:
  - AIMech:ResilientBackpropagation
  evidence_ids:
  - resilientbackpropagation-method
  - identity-search
  - mapping-scope
  summary: Rprop is an optimizer using backpropagated gradients, not the backpropagation
    procedure for computing those gradients. Update magnitude is controlled by step
    size rather than current gradient magnitude.
  details: Sign-reversal handling is scoped to the inspected PyTorch variant; other
    Rprop variants require comparison. No comparative speed or convergence claim is
    asserted.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Official algorithm docstring and relevant implementation inspected
      at a pinned PyTorch commit. This is not a performance experiment.
    evidence_ids:
    - resilientbackpropagation-method
- assessment_id: muon-method
  area: evidence
  topic: Optimizer identity and documented update mechanism
  outcome: supported
  target_ids:
  - AIMech:Muon
  evidence_ids:
  - muon-method
  - identity-search
  - mapping-scope
  summary: Muon is a matrix-update optimizer distinct from coordinatewise Adam-family
    scaling. The name here denotes the optimization algorithm, not unrelated uses
    of the word muon.
  details: The cited implementation is scoped to two-dimensional hidden-layer parameters
    and directs other parameters to a standard optimizer. The implementation provides
    alternative shape-scaling conventions; no universal exact orthogonality, convergence
    or performance guarantee is asserted.
  dimensions:
  - name: evidence-access
    value: documentation
    definition: Official algorithm docstring and relevant implementation inspected
      at a pinned PyTorch commit. This is not a performance experiment.
    evidence_ids:
    - muon-method
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:AdamW
  - AIMech:Adagrad
  - AIMech:RMSprop
  - AIMech:Adadelta
  - AIMech:Adafactor
  - AIMech:AdaMax
  - AIMech:NAdam
  - AIMech:RAdam
  - AIMech:AveragedStochasticGradientDescent
  - AIMech:LBFGS
  - AIMech:ResilientBackpropagation
  - AIMech:Muon
  evidence_ids:
  - identity-search
  - mapping-scope
  - adamw-method
  - adagrad-method
  - rmsprop-method
  - adadelta-method
  - adafactor-method
  - adamax-method
  - nadam-method
  - radam-method
  - averagedstochasticgradientdescent-method
  - lbfgs-method
  - resilientbackpropagation-method
  - muon-method
  rationale: Retain distinctions in accumulation/decay, momentum, infinity-norm scaling,
    rectification, decoupled decay, second-moment factorization, iterate averaging,
    curvature history, sign-based steps and matrix orthogonalization. A shared training
    purpose does not imply algorithm equivalence.
- action: defer
  target_ids:
  - AIMech:AdamW
  - AIMech:Adagrad
  - AIMech:RMSprop
  - AIMech:Adadelta
  - AIMech:Adafactor
  - AIMech:AdaMax
  - AIMech:NAdam
  - AIMech:RAdam
  - AIMech:AveragedStochasticGradientDescent
  - AIMech:LBFGS
  - AIMech:ResilientBackpropagation
  - AIMech:Muon
  evidence_ids:
  - identity-search
  - mapping-scope
  rationale: Do not infer a complete optimizer taxonomy or split every implementation
    flag into a new concept. AMSGrad and other exposed neighbors require their own
    evidence/identity assessments.
limitations:
- This is scientific self-review of documented mechanisms, not independent peer review
  or experimental replication.
- Implementation versions can differ from original papers; documented Adafactor, RMSprop,
  Rprop and Muon scope limits remain explicit.
- The review timestamps record post-inspection assessment; evidence reading and record
  writes occurred earlier in the same documented session.
- All records remain DRAFT. Twelve new concepts were found; literature discovery remains
  active with nonempty pending leads.
tags:
- native-concepts
- optimizers
- official-documentation
- self-review
- discovery-ongoing
```
