# Scientific self-review of four semi-supervised classifier procedures

- Review: 20261011T101529Z-semi-supervised-consistency
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T10:13:09Z
- Finished UTC: 2026-10-11T10:15:29Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Pi-model, Temporal ensembling, Mean Teacher and MixMatch as distinct DRAFT algorithms with source-backed gradient and target-update boundaries. Review issue58 is fixed and regression-tested; no actionable record finding remains in the selected four-record scope.

## Scope And Provenance

All fields of the four newly added semi-supervised classifier-training records, including their Unicode identity representation.

Selection: Exact four maintained IDs listed in the discovery report; no sampling.
Coverage: full; 4 reviewed / 4 in the declared population.
Source: working_tree at Git base 27428817e50e8c599ee7b76586983eb978f307d6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:PiModel | data/curated/PiModel.yaml | maintained | Pi-model |
| AIMech:TemporalEnsembling | data/curated/TemporalEnsembling.yaml | maintained | Temporal ensembling |
| AIMech:MeanTeacher | data/curated/MeanTeacher.yaml | maintained | Mean Teacher |
| AIMech:MixMatch | data/curated/MixMatch.yaml | maintained | MixMatch |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:PiModel, AIMech:TemporalEnsembling, AIMech:MeanTeacher, AIMech:MixMatch | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 67.14s (0:01:07)<br>Checked 442 record(s); 0 failed.<br>Checked 234 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 51 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 48,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:PiModel, AIMech:TemporalEnsembling, AIMech:MeanTeacher, AIMech:MixMatch | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |

## Scientific And Domain Assessments

### Identity, definition, complete asserted method and source scope

evidence: supported. Targets: AIMech:PiModel.

The Greek Π notation is an identity alias for the Pi-model in Laine and Aila, not the generic AIO Model class. Its two contemporaneous stochastic predictions and two-sided gradient differ from temporal ensembling’s stored predictions, Mean Teacher’s weight-averaged stopped-gradient teacher, and SimSiam’s asymmetric stopped-gradient representation targets. This record describes a training algorithm, not a trained checkpoint or fixed network architecture. The inspected AIO SemiSupervisedLLM class specifically combines LLM pretraining with supervised fine-tuning; its related synonym self-training is not an exact identity for this method. AIO SelfsupervisedLearning excludes human-annotated labels, Distillation describes large-to-small compression, and RegularizationLayer is a layer: none supplies an equivalent class for this algorithm. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 230 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main checkout; matches concern prior discovery leads and the Pi-model normalization regression. Ten exact AIO CLASS nodes, their scoped synonyms and outgoing edges, plus five neighboring native records were inspected. The corrected Unicode-aware normalizer preserves Π; the previous Pi-model/Model collision was a lexical defect, not semantic identity (review issue #58).

For each minibatch B, run each input twice through the same classifier parameters with independently sampled input augmentation and network noise, producing C-class probability vectors z_i and z_tilde_i. Minimize −(1/&#124;B&#124;) sum over labeled i in B of log z_i[y_i], plus w(t)/(C&#124;B&#124;) times sum over all i in B of &#124;&#124;z_i−z_tilde_i&#124;&#124;². Algorithm 1 normalizes the labeled sum by the complete minibatch size, not the number of labeled examples. Both prediction branches contribute gradients to the shared parameters. Start the consistency weight at zero and ramp it up; the reported Gaussian schedule is an experimental choice. There is no persistent per-example target or separately EMA-updated teacher in this core procedure. Limits: The consistency objective assumes the chosen perturbations should preserve class identity; incorrect augmentations can impose inappropriate targets. Agreement alone does not identify the correct classes; the stated classifier objective includes labeled cross-entropy and a consistency-weight ramp. Architecture, augmentation strength, batch composition and weight schedule affect the instantiated training procedure; no accuracy improvement or universal schedule is asserted. Only the declared source pages were inspected; this record does not claim a complete implementation or benchmark reproduction.

### Identity, definition, complete asserted method and source scope

evidence: supported. Targets: AIMech:TemporalEnsembling.

This is the prediction-ensemble algorithm in Laine and Aila, distinguished from the same paper’s Pi-model. Its dataset-indexed stored targets and epoch-based refresh differ from Mean Teacher’s per-step weight averaging. The name does not imply an ensemble of separately trained classifiers at inference. This record describes a training algorithm, not a trained checkpoint or fixed network architecture. The inspected AIO SemiSupervisedLLM class specifically combines LLM pretraining with supervised fine-tuning; its related synonym self-training is not an exact identity for this method. AIO SelfsupervisedLearning excludes human-annotated labels, Distillation describes large-to-small compression, and RegularizationLayer is a layer: none supplies an equivalent class for this algorithm. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 230 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main checkout; matches concern prior discovery leads and the Pi-model normalization regression. Ten exact AIO CLASS nodes, their scoped synonyms and outgoing edges, plus five neighboring native records were inspected. The corrected Unicode-aware normalizer preserves Π; the previous Pi-model/Model collision was a lexical defect, not semantic identity (review issue #58).

Maintain zero-initialized N-by-C arrays Z and target z_tilde for N indexed examples and C classes. During epoch t, obtain one stochastic prediction z_i for each example when its minibatch is processed. Minimize labeled cross-entropy divided by the full minibatch size plus w(t)/(C&#124;B&#124;) sum over all i in B of &#124;&#124;z_i−z_tilde_i&#124;&#124;², holding the stored targets constant during differentiation. After predictions have been used for that epoch, update each accumulated prediction Z_i←alpha Z_i+(1−alpha)z_i and set the next target to Z_i/(1−alpha^t), with fixed 0≤alpha&lt;1 and t starting at 1. Set the first epoch’s consistency weight to zero and ramp it up. Algorithm 2 displays the target update after the epoch; its caption permits per-example updates within a minibatch after the old target has been used. Predictions gathered within an epoch can come from different current parameter states. The exponential average is over example predictions, not model parameters. Limits: Per-example prediction memory scales with the number of indexed examples and classes; targets depend on preserving example identity across visits. The stated bias correction assumes zero initialization and a fixed alpha; arbitrary momentum schedules or missing-example update schedules need their own accounting. Old predictions can remain incorrect or become stale, and input perturbations must preserve the intended class; no unconditional improvement is implied by averaging. The record covers the original classifier procedure, not an online-streaming extension, a claim of doubled speed, or reported benchmark accuracy.

### Identity, definition, complete asserted method and source scope

evidence: supported. Targets: AIMech:MeanTeacher.

Mean Teacher averages weights, whereas temporal ensembling averages predictions and the Pi-model shares current parameters across two gradient-bearing branches. Sharing an EMA component does not make this labeled classifier-training objective identical to BYOL or DINO, which use different representation targets and objectives without the labeled cross-entropy term. This record describes a training algorithm, not a trained checkpoint or fixed network architecture. The inspected AIO SemiSupervisedLLM class specifically combines LLM pretraining with supervised fine-tuning; its related synonym self-training is not an exact identity for this method. AIO SelfsupervisedLearning excludes human-annotated labels, Distillation describes large-to-small compression, and RegularizationLayer is a layer: none supplies an equivalent class for this algorithm. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 230 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main checkout; matches concern prior discovery leads and the Pi-model normalization regression. Ten exact AIO CLASS nodes, their scoped synonyms and outgoing edges, plus five neighboring native records were inspected. The corrected Unicode-aware normalizer preserves Π; the previous Pi-model/Model collision was a lexical defect, not semantic identity (review issue #58).

Evaluate each input with independently perturbed student and teacher networks of the same architecture. Train the student with cross-entropy on labeled examples and a weighted squared-probability consistency cost between student and teacher predictions on labeled and unlabeled examples. Treat teacher predictions as constant during the gradient update. After obtaining the updated student parameters theta_t, update teacher parameters theta_prime_t←alpha theta_prime_(t−1)+(1−alpha)theta_t. Thus the teacher changes by parameter averaging after training steps, not by backpropagation through its consistency branch. Choose the averaging coefficient and consistency-weight schedule as part of the training setup. The core description does not require a particular initialization or warm-up formula. Unlike temporal ensembling, it does not require a persistent target array indexed by the training set. Limits: Teacher initialization, coefficient schedules, loss scaling and network state management remain implementation choices; the record does not assert a universal initialization, alpha value or handling of nonparameter buffers. Consistency relies on class-preserving perturbations and can propagate wrong targets; the EMA teacher is not guaranteed to improve every prediction. The original experiments include architecture and dataset-specific settings. No benchmark score, universal performance ordering, or large-to-small compression claim is asserted. The read supplementary pages cover the convolutional setup and branch gradients, not all later supplement experiments or source code.

### Identity, definition, complete asserted method and source scope

evidence: supported. Targets: AIMech:MixMatch.

MixMatch combines averaged augmented-view label guessing, probability sharpening and the modified MixUp pairing rule. These components define a distinct training algorithm rather than an alias for MixUp, Mean Teacher or a hard pseudo-label confidence filter. Its classification soft targets differ from representation matching in BYOL, DINO and SimSiam. This record describes a training algorithm, not a trained checkpoint or fixed network architecture. The inspected AIO SemiSupervisedLLM class specifically combines LLM pretraining with supervised fine-tuning; its related synonym self-training is not an exact identity for this method. AIO SelfsupervisedLearning excludes human-annotated labels, Distillation describes large-to-small compression, and RegularizationLayer is a layer: none supplies an equivalent class for this algorithm. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 230 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main checkout; matches concern prior discovery leads and the Pi-model normalization regression. Ten exact AIO CLASS nodes, their scoped synonyms and outgoing edges, plus five neighboring native records were inspected. The corrected Unicode-aware normalizer preserves Π; the previous Pi-model/Model collision was a lexical defect, not semantic identity (review issue #58).

Given B labeled examples with one-hot labels and B unlabeled examples, augment each labeled input once and each unlabeled input K times. Average the current classifier probabilities across the K views of each unlabeled input, then sharpen the average q_bar using q_c=q_bar_c^(1/T)/sum_j q_bar_j^(1/T), for T&gt;0; treat these guessed labels as constants during differentiation. Create augmented labeled pairs X_hat of size B and unlabeled pairs U_hat of size KB, then shuffle their concatenation into W. Mix each X_hat pair with the corresponding first B pairs in W, and each U_hat pair with the corresponding remaining KB pairs. For each MixUp operation draw lambda from Beta(alpha,alpha), alpha&gt;0, set lambda_prime=max(lambda,1−lambda), and combine both inputs and targets with weights lambda_prime and 1−lambda_prime, keeping at least half of the first pair. For the resulting X_prime and U_prime, minimize average soft-target cross-entropy over X_prime plus lambda_u/(C&#124;U_prime&#124;) times sum over U_prime of squared target/prediction differences, where C is the number of classes. The reported implementation ramps lambda_u linearly. Guessed labels use current-model predictions; the evaluation-only weight EMA in Section 4.1 is not a Mean Teacher target generator. Limits: The original setup pairs B labeled examples with B unlabeled examples and K augmentations per unlabeled input. Alternative batching or interpolation rules require an explicit variant scope. For 0&lt;T&lt;1 sharpening concentrates probability. As a curator consequence of the formula, the T→0 limit is one-hot only with a unique maximum; tied maxima retain equal limiting mass. T&gt;1 smooths rather than sharpens. Correct label-preserving augmentation and useful interpolation are assumptions; guessed labels can be wrong and the algorithm has no defining hard confidence threshold. The record does not assert published error rates or universal superiority. Reported T, K, alpha, lambda_u and evaluation-EMA settings are experimental choices, not fixed constants of every implementation.

### Which quantities receive gradients or are averaged

consistency: supported. Targets: AIMech:PiModel, AIMech:TemporalEnsembling, AIMech:MeanTeacher, AIMech:MixMatch.

Two-sided Pi gradients, stored temporal targets, EMA weights and guessed/mixed soft targets remain distinct.

Pi-model propagates gradients through both stochastic outputs; temporal ensembling uses fixed stored targets and fixed-alpha zero-initialized bias correction; Mean Teacher differentiates only the student and averages parameters after its step. MixMatch stops label-guessing gradients and uses current predictions for those guesses. Its separate evaluation EMA is not a Mean Teacher target rule. Temporal targets can be updated in the minibatch loop after their old values are used, as Algorithm2 explicitly permits.

### Minibatch denominators, interpolation and sharpening

consistency: supported. Targets: AIMech:PiModel, AIMech:TemporalEnsembling, AIMech:MeanTeacher, AIMech:MixMatch.

Keep the original classifier-loss normalization and avoid unsupported limiting claims.

The Pi and temporal pseudocode divides the labeled sum by the full batch count and squared consistency by classes times batch size. Mean Teacher loss coefficients and initialization are not forced to those conventions. MixMatch partitions a single shuffled concatenation, keeps lambda_prime=max(lambda,1-lambda), and applies different losses to its labeled and unlabeled outputs. At tied maxima the temperature-to-zero limit retains equal mass on the maxima; the one-hot special case requires uniqueness. This is a curator consequence of the formula, not a claimed author erratum or benchmark.

### Resolved review issue58: Unicode identity comparison

consistency: supported. Targets: AIMech:PiModel.

The Pi alias is now faithfully representable without weakening real collision checks.

The actual synthetic corpus rejected Π-model as AIO:Model under ASCII filtering. The revised normalizer retains meaningful Unicode letters and marks while preserving plus variants; it does not transliterate Greek into Latin. Schema-independent letter/digit validation rejects mark-only and symbol-only names. Whole-collection regression tests and the current complete corpus gate pass. The issue is fixed in maintained code/tests/docs before this final self-review; no generated AIO record changed.

### Supervision, model/task and teacher-student scope

grounding: supported. Targets: AIMech:PiModel, AIMech:TemporalEnsembling, AIMech:MeanTeacher, AIMech:MixMatch.

Inspected mappings are related algorithm-to-task links.

All four algorithms relate to AIO Classification and MachineLearningTask as algorithm-to-task associations. SemiSupervisedLLM is a different LLM pretraining/fine-tuning model class despite its related self-training synonym. SelfsupervisedLearning is specifically without human labels. Distillation describes large-to-small compression, EnsembleLearning implies multiple learning algorithms, RegularizationLayer is a layer, and Model is generic: none is an equivalent identity or justified subclass mapping. Native VAT, IMSAT, BYOL, DINO and SimSiam preserve different objectives, supervision and gradient/teacher conventions.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:PiModel, AIMech:TemporalEnsembling, AIMech:MeanTeacher, AIMech:MixMatch. Contemporaneous shared-parameter predictions, per-example historical prediction averages, teacher parameter EMA, and averaged/sharpened/mixed guessed labels define different algorithms. The neighboring VAT/IMSAT/BYOL/DINO/SimSiam objectives do not collapse these boundaries. No AIO rewrite, name merge or DRAFT promotion is warranted.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T101248Z-semi-supervised-consistency.json | supports | All 442 AIO labels/scoped synonyms and 230 preceding native IDs/names/aliases were compared, plus ignored/hidden-inclusive full-text searches in both complete checkouts. The first search produced a false Π-model/Model collision caused by ASCII filtering. After the documented fix, no candidate identity matches remained. Ten exact AIO nodes and five neighboring native mechanisms were inspected. The 1,348-string audit includes all scoped synonyms; its existing keys and cross-record collision sets are unchanged. |
| mapping | sources/aio/aio.json; Ten exact CLASS nodes with definitions, scoped synonyms and outgoing edges in source_analysis.aio_mapping_inspection | supports | All four algorithms relate to AIO Classification and MachineLearningTask as algorithm-to-task associations. SemiSupervisedLLM is a different LLM pretraining/fine-tuning model class despite its related self-training synonym. SelfsupervisedLearning is specifically without human labels. Distillation describes large-to-small compression, EnsembleLearning implies multiple learning algorithms, RegularizationLayer is a layer, and Model is generic: none is an equivalent identity or justified subclass mapping. Native VAT, IMSAT, BYOL, DINO and SimSiam preserve different objectives, supervision and gradient/teacher conventions. |
| neighbors | research/discovery/20261011T101248Z-semi-supervised-consistency.json; source_analysis.aio_mapping_inspection.native_neighbors | supports | Compared the actual definitions and mechanisms of VAT, IMSAT, BYOL, DINO and SimSiam. Target generation, labeled supervision, output space and branch gradients retain separate identities; shared EMA or consistency components do not establish equivalence. |
| unicode-fix | research/discovery/20261011T101248Z-semi-supervised-consistency.json; review_refinements[0]; maintained code, regression tests and identity documentation | supports | Review issue58 reproduced the false Π-model/Model collision. NFC/casefold now retains Unicode letters, digits, marks and ASCII plus signs. The 1348-string pre-addition audit changes no existing key and introduces no collision. Regression tests keep Greek/accent duplicates rejected while distinguishing Pi from Model, preserving a noncomposable accent, accepting Greek letters and rejecting mark/symbol-only labels. |
| pimodel-source-0 | https://users.aalto.fi/~ailat1/publications/laine2017iclr_paper.pdf; Section 2.1, Figure 1 and Algorithm 1, PDF/printed pp. 2–3 | supports | Temporal Ensembling for Semi-Supervised Learning. ICLR 2017 conference paper, author-hosted PDF; 13 pages. Read scope is declared in the discovery report; main method pages and, where cited, Mean Teacher supplemental PDF pages1–2 were actually viewed. |
| pimodel-source-1 | https://papers.neurips.cc/paper_files/paper/2017/file/68053af2923e00204c3ca7c6a3150cf7-Paper.pdf; Section 2, PDF/printed p. 3: Pi-model gradients flow through both branches, unlike Temporal Ensembling and Mean Teacher | supports | Mean teachers are better role models: Weight-averaged consistency targets improve semi-supervised deep learning results. NIPS 2017 proceedings paper; 10 pages. Read scope is declared in the discovery report; main method pages and, where cited, Mean Teacher supplemental PDF pages1–2 were actually viewed. |
| temporalensembling-source-0 | https://users.aalto.fi/~ailat1/publications/laine2017iclr_paper.pdf; Section 2.2, Figure 1 and Algorithm 2, PDF/printed pp. 2–4 | supports | Temporal Ensembling for Semi-Supervised Learning. ICLR 2017 conference paper, author-hosted PDF; 13 pages. Read scope is declared in the discovery report; main method pages and, where cited, Mean Teacher supplemental PDF pages1–2 were actually viewed. |
| temporalensembling-source-1 | https://papers.neurips.cc/paper_files/paper/2017/file/68053af2923e00204c3ca7c6a3150cf7-Paper.pdf; Section 2, PDF/printed pp. 2–3: prediction-averaging versus weight-averaging targets and constant targets in gradient updates | supports | Mean teachers are better role models: Weight-averaged consistency targets improve semi-supervised deep learning results. NIPS 2017 proceedings paper; 10 pages. Read scope is declared in the discovery report; main method pages and, where cited, Mean Teacher supplemental PDF pages1–2 were actually viewed. |
| meanteacher-source-0 | https://papers.neurips.cc/paper_files/paper/2017/file/68053af2923e00204c3ca7c6a3150cf7-Paper.pdf; Section 2, Figure 2 and the consistency/weight-EMA equations, PDF/printed pp. 2–3; Section 3.1, p. 4 | supports | Mean teachers are better role models: Weight-averaged consistency targets improve semi-supervised deep learning results. NIPS 2017 proceedings paper; 10 pages. Read scope is declared in the discovery report; main method pages and, where cited, Mean Teacher supplemental PDF pages1–2 were actually viewed. |
| meanteacher-source-1 | https://papers.neurips.cc/paper_files/paper/2017/file/68053af2923e00204c3ca7c6a3150cf7-Supplemental.zip; Appendix B.1, supplementary PDF pp. 1–2 / printed pp. 11–12: same architecture, branch gradients, cross-entropy/MSE and per-step EMA | supports | Mean teachers are better role models: Weight-averaged consistency targets improve semi-supervised deep learning results — supplementary material. NIPS 2017 proceedings supplement; ZIP member Paper 789\mean-teacher-supplementary.pdf; 6 PDF pages, printed 11–16; SHA-256 identifies extracted PDF bytes, not the ZIP. Read scope is declared in the discovery report; main method pages and, where cited, Mean Teacher supplemental PDF pages1–2 were actually viewed. |
| mixmatch-source-0 | https://proceedings.neurips.cc/paper_files/paper/2019/file/1cd138d0499a68f4bb72bee04bbec2d7-Paper.pdf; Sections 3.1–3.5, Algorithm 1 and Equations (2)–(13), PDF/printed pp. 3–5; Section 4.1, p. 5 | supports | MixMatch: A Holistic Approach to Semi-Supervised Learning. NeurIPS 2019 proceedings paper; 11 pages; author order follows the PDF. Read scope is declared in the discovery report; main method pages and, where cited, Mean Teacher supplemental PDF pages1–2 were actually viewed. |

## Limits And Additional Notes

- Adversarial author self-review, not independent approval. All four records remain DRAFT.
- Primary full-text access was achieved, but only the declared method/abstract/context pages were read; unseen pages are not reviewed evidence.
- The vendored check initially failed because sandbox DNS was unavailable; the authorized network-enabled rerun passed. This was a tool-access failure, not a source or curation defect.
- Issue58 concerns the maintained Unicode normalizer, tests and documentation, not an AIO ontology error. It was fixed before this final assessment.
- No new empirical performance claim, training execution or model-instance record.
- Four positive additions and a nonempty accounted discovery frontier leave the ongoing goal active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T101529Z-semi-supervised-consistency
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of four semi-supervised classifier procedures
started_at: '2026-10-11T10:13:09Z'
finished_at: '2026-10-11T10:15:29Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent checked all four records against original
    method pages, the Mean Teacher supplement, exact AIO mappings and five maintained
    neighbors; regression tests and the complete collection gate verify the Unicode
    fix. This adversarial author review is not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Pi-model, Temporal ensembling, Mean Teacher and MixMatch as distinct
  DRAFT algorithms with source-backed gradient and target-update boundaries. Review
  issue58 is fixed and regression-tested; no actionable record finding remains in
  the selected four-record scope.
source:
  git_revision: 27428817e50e8c599ee7b76586983eb978f307d6
  state: working_tree
  inputs:
  - path: data/aio/Classification.yaml
    sha256: d97da621c5052c7ab913cda95184ea2cca274f803298fd5f2c1273a22a211219
    role: context
  - path: data/aio/Distillation.yaml
    sha256: 02faf8db468fca6adfe257a141c98c7b13f85dc301e856a1f9622dfdb68ae5c9
    role: context
  - path: data/aio/EnsembleLearning.yaml
    sha256: cf9435e5a799d84072222190c2d681c53b22bf9e7094891405008ebe398a39ed
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/Model.yaml
    sha256: 56b85d1c6d559d9ce4172dcf9c776126e91a03649c8f4d1fa8e3f5130f0ca73b
    role: context
  - path: data/aio/RegularizationLayer.yaml
    sha256: d4280bbc058b841655bcfcea7ef1dd1e05ac5e0211a860045f13eaa30933dbae
    role: context
  - path: data/aio/SelfsupervisedLearning.yaml
    sha256: ad9a98dfee5629f6433f13470f56e333316f8f03847df2c5678faf023d979c0e
    role: context
  - path: data/aio/SemiSupervisedLLM.yaml
    sha256: 4ee601313a6cdaa7134207fa384702f0e92d2b93906e379c2b0ef5cfe6eef9ee
    role: context
  - path: data/aio/SupervisedLearning.yaml
    sha256: 472f033f91a14c8727e525ddd30f82fcaf16a2514fa8f062667fb94fc9c9b718
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/curated/BootstrapYourOwnLatent.yaml
    sha256: 4ed2bebb46d3199f192dcb7e53012a22c7bd96d7b41f015db762dd41f545e307
    role: context
  - path: data/curated/DINOSelfDistillation.yaml
    sha256: 66ac3400efd5deda6468cb7e8ae53f3c7f6f0cf942557b634ef3a7bdafc93516
    role: context
  - path: data/curated/InformationMaximizingSelfAugmentedTraining.yaml
    sha256: cd1a3bf10ff09203c9ac3271d82257aeb14ec0bb43064e5a604a0e5eef47196a
    role: context
  - path: data/curated/MeanTeacher.yaml
    sha256: 606e863163715f48b89fb35dc090bb32d5d2ca70c099d1fdfac563104ada27b7
    role: target
  - path: data/curated/MixMatch.yaml
    sha256: 38a2afca506c874d077eec42cf8b36dbe2afbf6fb07323228ace6d00d12b20b3
    role: target
  - path: data/curated/PiModel.yaml
    sha256: 907c6f768dda1363fc20bfa6c045c08761449fc7163b1c5177172c130eb4789f
    role: target
  - path: data/curated/SimSiam.yaml
    sha256: 283a7d1d5f9bbd6bff853294b71e26d5489a412568bfff0846bef831d9019fe3
    role: context
  - path: data/curated/TemporalEnsembling.yaml
    sha256: 87c0afa3d17eded7887a2c25d439b08abf0ce769b4b15e1b490c382c5b9491cc
    role: target
  - path: data/curated/VirtualAdversarialTraining.yaml
    sha256: 448041d823d47b52bb5ea340e84257dbf09f20659d5c2f1e2dfd1c36a29799ec
    role: context
  - path: docs/curated-concepts.md
    sha256: 1a3db0915791b0e90b02cd1f83c35850bfc3c97b18edfd8b946c91030578ccb8
    role: context
  - path: research/discovery/20261011T101248Z-semi-supervised-consistency.json
    sha256: fe8d816adb9c6cd2c8fcf8f288643830077b35b1d4d9a9c41126ded67e1b98ce
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
  - path: tests/test_curated.py
    sha256: 40cfc130d55b17944373a9705a28cf9d191b58a86aa6363d9ffdcb3619145482
    role: context
targets:
- target_id: AIMech:PiModel
  path: data/curated/PiModel.yaml
  label: Pi-model
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PiModel.yaml
    role: maintained
- target_id: AIMech:TemporalEnsembling
  path: data/curated/TemporalEnsembling.yaml
  label: Temporal ensembling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TemporalEnsembling.yaml
    role: maintained
- target_id: AIMech:MeanTeacher
  path: data/curated/MeanTeacher.yaml
  label: Mean Teacher
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MeanTeacher.yaml
    role: maintained
- target_id: AIMech:MixMatch
  path: data/curated/MixMatch.yaml
  label: MixMatch
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MixMatch.yaml
    role: maintained
scope:
  description: All fields of the four newly added semi-supervised classifier-training
    records, including their Unicode identity representation.
  selection: Exact four maintained IDs listed in the discovery report; no sampling.
  coverage: full
  population_size: 4
  reviewed_target_ids:
  - AIMech:PiModel
  - AIMech:TemporalEnsembling
  - AIMech:MeanTeacher
  - AIMech:MixMatch
  exclusions:
  - target: Older native neighbors and the rest of the collection
    reason: Compared for identity and boundary context; this review does not claim
      full scientific reassessment of their current records.
  - target: Uninspected source pages, source-code variants and empirical results
    reason: Only declared pages were read. Initialization/buffer handling and later
      supplement details are not inferred; no training or benchmark was run.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:PiModel
  - AIMech:TemporalEnsembling
  - AIMech:MeanTeacher
  - AIMech:MixMatch
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 67.14s (0:01:07)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 234 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 51 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 48,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:PiModel
  - AIMech:TemporalEnsembling
  - AIMech:MeanTeacher
  - AIMech:MixMatch
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T101248Z-semi-supervised-consistency.json
  accessed_at: '2026-10-11T10:13:09Z'
  support: supports
  summary: All 442 AIO labels/scoped synonyms and 230 preceding native IDs/names/aliases
    were compared, plus ignored/hidden-inclusive full-text searches in both complete
    checkouts. The first search produced a false Π-model/Model collision caused by
    ASCII filtering. After the documented fix, no candidate identity matches remained.
    Ten exact AIO nodes and five neighboring native mechanisms were inspected. The
    1,348-string audit includes all scoped synonyms; its existing keys and cross-record
    collision sets are unchanged.
  search_scope: All 442 AIO labels/scoped synonyms and 230 preceding native IDs/names/aliases;
    whole-checkout ignored/hidden-inclusive fixed-string searches in main and worktree.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Ten exact CLASS nodes with definitions, scoped synonyms and outgoing edges
    in source_analysis.aio_mapping_inspection
  accessed_at: '2026-10-11T10:13:09Z'
  support: supports
  summary: 'All four algorithms relate to AIO Classification and MachineLearningTask
    as algorithm-to-task associations. SemiSupervisedLLM is a different LLM pretraining/fine-tuning
    model class despite its related self-training synonym. SelfsupervisedLearning
    is specifically without human labels. Distillation describes large-to-small compression,
    EnsembleLearning implies multiple learning algorithms, RegularizationLayer is
    a layer, and Model is generic: none is an equivalent identity or justified subclass
    mapping. Native VAT, IMSAT, BYOL, DINO and SimSiam preserve different objectives,
    supervision and gradient/teacher conventions.'
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T101248Z-semi-supervised-consistency.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors
  accessed_at: '2026-10-11T10:13:09Z'
  support: supports
  summary: Compared the actual definitions and mechanisms of VAT, IMSAT, BYOL, DINO
    and SimSiam. Target generation, labeled supervision, output space and branch gradients
    retain separate identities; shared EMA or consistency components do not establish
    equivalence.
- evidence_id: unicode-fix
  kind: record_content
  reference: research/discovery/20261011T101248Z-semi-supervised-consistency.json
  locator: review_refinements[0]; maintained code, regression tests and identity documentation
  accessed_at: '2026-10-11T10:13:09Z'
  support: supports
  summary: Review issue58 reproduced the false Π-model/Model collision. NFC/casefold
    now retains Unicode letters, digits, marks and ASCII plus signs. The 1348-string
    pre-addition audit changes no existing key and introduces no collision. Regression
    tests keep Greek/accent duplicates rejected while distinguishing Pi from Model,
    preserving a noncomposable accent, accepting Greek letters and rejecting mark/symbol-only
    labels.
- evidence_id: pimodel-source-0
  kind: primary_source
  reference: https://users.aalto.fi/~ailat1/publications/laine2017iclr_paper.pdf
  locator: Section 2.1, Figure 1 and Algorithm 1, PDF/printed pp. 2–3
  accessed_at: '2026-10-11T10:00:57Z'
  snapshot_sha256: d19ea2ecc468a4dcb4d6e540ec981d1031cb4f0c38a9de69664a91b344bb6990
  support: supports
  summary: Temporal Ensembling for Semi-Supervised Learning. ICLR 2017 conference
    paper, author-hosted PDF; 13 pages. Read scope is declared in the discovery report;
    main method pages and, where cited, Mean Teacher supplemental PDF pages1–2 were
    actually viewed.
- evidence_id: pimodel-source-1
  kind: primary_source
  reference: https://papers.neurips.cc/paper_files/paper/2017/file/68053af2923e00204c3ca7c6a3150cf7-Paper.pdf
  locator: 'Section 2, PDF/printed p. 3: Pi-model gradients flow through both branches,
    unlike Temporal Ensembling and Mean Teacher'
  accessed_at: '2026-10-11T10:00:55Z'
  snapshot_sha256: 86c2ad510ea207cbaac324ebf441c034ddd9612140f5a191406c6826a337e8a8
  support: supports
  summary: 'Mean teachers are better role models: Weight-averaged consistency targets
    improve semi-supervised deep learning results. NIPS 2017 proceedings paper; 10
    pages. Read scope is declared in the discovery report; main method pages and,
    where cited, Mean Teacher supplemental PDF pages1–2 were actually viewed.'
- evidence_id: temporalensembling-source-0
  kind: primary_source
  reference: https://users.aalto.fi/~ailat1/publications/laine2017iclr_paper.pdf
  locator: Section 2.2, Figure 1 and Algorithm 2, PDF/printed pp. 2–4
  accessed_at: '2026-10-11T10:00:57Z'
  snapshot_sha256: d19ea2ecc468a4dcb4d6e540ec981d1031cb4f0c38a9de69664a91b344bb6990
  support: supports
  summary: Temporal Ensembling for Semi-Supervised Learning. ICLR 2017 conference
    paper, author-hosted PDF; 13 pages. Read scope is declared in the discovery report;
    main method pages and, where cited, Mean Teacher supplemental PDF pages1–2 were
    actually viewed.
- evidence_id: temporalensembling-source-1
  kind: primary_source
  reference: https://papers.neurips.cc/paper_files/paper/2017/file/68053af2923e00204c3ca7c6a3150cf7-Paper.pdf
  locator: 'Section 2, PDF/printed pp. 2–3: prediction-averaging versus weight-averaging
    targets and constant targets in gradient updates'
  accessed_at: '2026-10-11T10:00:55Z'
  snapshot_sha256: 86c2ad510ea207cbaac324ebf441c034ddd9612140f5a191406c6826a337e8a8
  support: supports
  summary: 'Mean teachers are better role models: Weight-averaged consistency targets
    improve semi-supervised deep learning results. NIPS 2017 proceedings paper; 10
    pages. Read scope is declared in the discovery report; main method pages and,
    where cited, Mean Teacher supplemental PDF pages1–2 were actually viewed.'
- evidence_id: meanteacher-source-0
  kind: primary_source
  reference: https://papers.neurips.cc/paper_files/paper/2017/file/68053af2923e00204c3ca7c6a3150cf7-Paper.pdf
  locator: Section 2, Figure 2 and the consistency/weight-EMA equations, PDF/printed
    pp. 2–3; Section 3.1, p. 4
  accessed_at: '2026-10-11T10:00:55Z'
  snapshot_sha256: 86c2ad510ea207cbaac324ebf441c034ddd9612140f5a191406c6826a337e8a8
  support: supports
  summary: 'Mean teachers are better role models: Weight-averaged consistency targets
    improve semi-supervised deep learning results. NIPS 2017 proceedings paper; 10
    pages. Read scope is declared in the discovery report; main method pages and,
    where cited, Mean Teacher supplemental PDF pages1–2 were actually viewed.'
- evidence_id: meanteacher-source-1
  kind: primary_source
  reference: https://papers.neurips.cc/paper_files/paper/2017/file/68053af2923e00204c3ca7c6a3150cf7-Supplemental.zip
  locator: 'Appendix B.1, supplementary PDF pp. 1–2 / printed pp. 11–12: same architecture,
    branch gradients, cross-entropy/MSE and per-step EMA'
  accessed_at: '2026-10-11T10:06:37Z'
  snapshot_sha256: be823265a22f919a23089265c62fc506495345cc7a47f0e1febe3ed07a36f4f3
  support: supports
  summary: 'Mean teachers are better role models: Weight-averaged consistency targets
    improve semi-supervised deep learning results — supplementary material. NIPS 2017
    proceedings supplement; ZIP member Paper 789\mean-teacher-supplementary.pdf; 6
    PDF pages, printed 11–16; SHA-256 identifies extracted PDF bytes, not the ZIP.
    Read scope is declared in the discovery report; main method pages and, where cited,
    Mean Teacher supplemental PDF pages1–2 were actually viewed.'
- evidence_id: mixmatch-source-0
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper_files/paper/2019/file/1cd138d0499a68f4bb72bee04bbec2d7-Paper.pdf
  locator: Sections 3.1–3.5, Algorithm 1 and Equations (2)–(13), PDF/printed pp. 3–5;
    Section 4.1, p. 5
  accessed_at: '2026-10-11T10:00:55Z'
  snapshot_sha256: 096c017ec11f5324d5d4cd2124e39b71d3f95ac7441a16ffd8dfa394c3424bea
  support: supports
  summary: 'MixMatch: A Holistic Approach to Semi-Supervised Learning. NeurIPS 2019
    proceedings paper; 11 pages; author order follows the PDF. Read scope is declared
    in the discovery report; main method pages and, where cited, Mean Teacher supplemental
    PDF pages1–2 were actually viewed.'
assessments:
- assessment_id: pimodel
  area: evidence
  topic: Identity, definition, complete asserted method and source scope
  outcome: supported
  target_ids:
  - AIMech:PiModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - pimodel-source-0
  - pimodel-source-1
  summary: 'The Greek Π notation is an identity alias for the Pi-model in Laine and
    Aila, not the generic AIO Model class. Its two contemporaneous stochastic predictions
    and two-sided gradient differ from temporal ensembling’s stored predictions, Mean
    Teacher’s weight-averaged stopped-gradient teacher, and SimSiam’s asymmetric stopped-gradient
    representation targets. This record describes a training algorithm, not a trained
    checkpoint or fixed network architecture. The inspected AIO SemiSupervisedLLM
    class specifically combines LLM pretraining with supervised fine-tuning; its related
    synonym self-training is not an exact identity for this method. AIO SelfsupervisedLearning
    excludes human-annotated labels, Distillation describes large-to-small compression,
    and RegularizationLayer is a layer: none supplies an equivalent class for this
    algorithm. No normalized identity match was found across all 442 pinned AIO labels/scoped
    synonyms and 230 preceding native IDs/names/aliases. Full-checkout fixed-string
    searches included ignored and hidden files in both worktree and main checkout;
    matches concern prior discovery leads and the Pi-model normalization regression.
    Ten exact AIO CLASS nodes, their scoped synonyms and outgoing edges, plus five
    neighboring native records were inspected. The corrected Unicode-aware normalizer
    preserves Π; the previous Pi-model/Model collision was a lexical defect, not semantic
    identity (review issue #58).'
  details: 'For each minibatch B, run each input twice through the same classifier
    parameters with independently sampled input augmentation and network noise, producing
    C-class probability vectors z_i and z_tilde_i. Minimize −(1/|B|) sum over labeled
    i in B of log z_i[y_i], plus w(t)/(C|B|) times sum over all i in B of ||z_i−z_tilde_i||².
    Algorithm 1 normalizes the labeled sum by the complete minibatch size, not the
    number of labeled examples. Both prediction branches contribute gradients to the
    shared parameters. Start the consistency weight at zero and ramp it up; the reported
    Gaussian schedule is an experimental choice. There is no persistent per-example
    target or separately EMA-updated teacher in this core procedure. Limits: The consistency
    objective assumes the chosen perturbations should preserve class identity; incorrect
    augmentations can impose inappropriate targets. Agreement alone does not identify
    the correct classes; the stated classifier objective includes labeled cross-entropy
    and a consistency-weight ramp. Architecture, augmentation strength, batch composition
    and weight schedule affect the instantiated training procedure; no accuracy improvement
    or universal schedule is asserted. Only the declared source pages were inspected;
    this record does not claim a complete implementation or benchmark reproduction.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A reusable classifier-training procedure, not a trained instance,
      layer, generic task or result.
    evidence_ids:
    - pimodel-source-0
    - pimodel-source-1
  - name: aio-relations
    value: 'related_match: AIO:Classification; related_match: AIO:MachineLearningTask'
    definition: Algorithm-to-task associations only; local identity and semi-supervised
      scope are preserved.
    evidence_ids:
    - mapping
- assessment_id: temporalensembling
  area: evidence
  topic: Identity, definition, complete asserted method and source scope
  outcome: supported
  target_ids:
  - AIMech:TemporalEnsembling
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - temporalensembling-source-0
  - temporalensembling-source-1
  summary: 'This is the prediction-ensemble algorithm in Laine and Aila, distinguished
    from the same paper’s Pi-model. Its dataset-indexed stored targets and epoch-based
    refresh differ from Mean Teacher’s per-step weight averaging. The name does not
    imply an ensemble of separately trained classifiers at inference. This record
    describes a training algorithm, not a trained checkpoint or fixed network architecture.
    The inspected AIO SemiSupervisedLLM class specifically combines LLM pretraining
    with supervised fine-tuning; its related synonym self-training is not an exact
    identity for this method. AIO SelfsupervisedLearning excludes human-annotated
    labels, Distillation describes large-to-small compression, and RegularizationLayer
    is a layer: none supplies an equivalent class for this algorithm. No normalized
    identity match was found across all 442 pinned AIO labels/scoped synonyms and
    230 preceding native IDs/names/aliases. Full-checkout fixed-string searches included
    ignored and hidden files in both worktree and main checkout; matches concern prior
    discovery leads and the Pi-model normalization regression. Ten exact AIO CLASS
    nodes, their scoped synonyms and outgoing edges, plus five neighboring native
    records were inspected. The corrected Unicode-aware normalizer preserves Π; the
    previous Pi-model/Model collision was a lexical defect, not semantic identity
    (review issue #58).'
  details: 'Maintain zero-initialized N-by-C arrays Z and target z_tilde for N indexed
    examples and C classes. During epoch t, obtain one stochastic prediction z_i for
    each example when its minibatch is processed. Minimize labeled cross-entropy divided
    by the full minibatch size plus w(t)/(C|B|) sum over all i in B of ||z_i−z_tilde_i||²,
    holding the stored targets constant during differentiation. After predictions
    have been used for that epoch, update each accumulated prediction Z_i←alpha Z_i+(1−alpha)z_i
    and set the next target to Z_i/(1−alpha^t), with fixed 0≤alpha<1 and t starting
    at 1. Set the first epoch’s consistency weight to zero and ramp it up. Algorithm
    2 displays the target update after the epoch; its caption permits per-example
    updates within a minibatch after the old target has been used. Predictions gathered
    within an epoch can come from different current parameter states. The exponential
    average is over example predictions, not model parameters. Limits: Per-example
    prediction memory scales with the number of indexed examples and classes; targets
    depend on preserving example identity across visits. The stated bias correction
    assumes zero initialization and a fixed alpha; arbitrary momentum schedules or
    missing-example update schedules need their own accounting. Old predictions can
    remain incorrect or become stale, and input perturbations must preserve the intended
    class; no unconditional improvement is implied by averaging. The record covers
    the original classifier procedure, not an online-streaming extension, a claim
    of doubled speed, or reported benchmark accuracy.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A reusable classifier-training procedure, not a trained instance,
      layer, generic task or result.
    evidence_ids:
    - temporalensembling-source-0
    - temporalensembling-source-1
  - name: aio-relations
    value: 'related_match: AIO:Classification; related_match: AIO:MachineLearningTask'
    definition: Algorithm-to-task associations only; local identity and semi-supervised
      scope are preserved.
    evidence_ids:
    - mapping
- assessment_id: meanteacher
  area: evidence
  topic: Identity, definition, complete asserted method and source scope
  outcome: supported
  target_ids:
  - AIMech:MeanTeacher
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - meanteacher-source-0
  - meanteacher-source-1
  summary: 'Mean Teacher averages weights, whereas temporal ensembling averages predictions
    and the Pi-model shares current parameters across two gradient-bearing branches.
    Sharing an EMA component does not make this labeled classifier-training objective
    identical to BYOL or DINO, which use different representation targets and objectives
    without the labeled cross-entropy term. This record describes a training algorithm,
    not a trained checkpoint or fixed network architecture. The inspected AIO SemiSupervisedLLM
    class specifically combines LLM pretraining with supervised fine-tuning; its related
    synonym self-training is not an exact identity for this method. AIO SelfsupervisedLearning
    excludes human-annotated labels, Distillation describes large-to-small compression,
    and RegularizationLayer is a layer: none supplies an equivalent class for this
    algorithm. No normalized identity match was found across all 442 pinned AIO labels/scoped
    synonyms and 230 preceding native IDs/names/aliases. Full-checkout fixed-string
    searches included ignored and hidden files in both worktree and main checkout;
    matches concern prior discovery leads and the Pi-model normalization regression.
    Ten exact AIO CLASS nodes, their scoped synonyms and outgoing edges, plus five
    neighboring native records were inspected. The corrected Unicode-aware normalizer
    preserves Π; the previous Pi-model/Model collision was a lexical defect, not semantic
    identity (review issue #58).'
  details: 'Evaluate each input with independently perturbed student and teacher networks
    of the same architecture. Train the student with cross-entropy on labeled examples
    and a weighted squared-probability consistency cost between student and teacher
    predictions on labeled and unlabeled examples. Treat teacher predictions as constant
    during the gradient update. After obtaining the updated student parameters theta_t,
    update teacher parameters theta_prime_t←alpha theta_prime_(t−1)+(1−alpha)theta_t.
    Thus the teacher changes by parameter averaging after training steps, not by backpropagation
    through its consistency branch. Choose the averaging coefficient and consistency-weight
    schedule as part of the training setup. The core description does not require
    a particular initialization or warm-up formula. Unlike temporal ensembling, it
    does not require a persistent target array indexed by the training set. Limits:
    Teacher initialization, coefficient schedules, loss scaling and network state
    management remain implementation choices; the record does not assert a universal
    initialization, alpha value or handling of nonparameter buffers. Consistency relies
    on class-preserving perturbations and can propagate wrong targets; the EMA teacher
    is not guaranteed to improve every prediction. The original experiments include
    architecture and dataset-specific settings. No benchmark score, universal performance
    ordering, or large-to-small compression claim is asserted. The read supplementary
    pages cover the convolutional setup and branch gradients, not all later supplement
    experiments or source code.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A reusable classifier-training procedure, not a trained instance,
      layer, generic task or result.
    evidence_ids:
    - meanteacher-source-0
    - meanteacher-source-1
  - name: aio-relations
    value: 'related_match: AIO:Classification; related_match: AIO:MachineLearningTask'
    definition: Algorithm-to-task associations only; local identity and semi-supervised
      scope are preserved.
    evidence_ids:
    - mapping
- assessment_id: mixmatch
  area: evidence
  topic: Identity, definition, complete asserted method and source scope
  outcome: supported
  target_ids:
  - AIMech:MixMatch
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - mixmatch-source-0
  summary: 'MixMatch combines averaged augmented-view label guessing, probability
    sharpening and the modified MixUp pairing rule. These components define a distinct
    training algorithm rather than an alias for MixUp, Mean Teacher or a hard pseudo-label
    confidence filter. Its classification soft targets differ from representation
    matching in BYOL, DINO and SimSiam. This record describes a training algorithm,
    not a trained checkpoint or fixed network architecture. The inspected AIO SemiSupervisedLLM
    class specifically combines LLM pretraining with supervised fine-tuning; its related
    synonym self-training is not an exact identity for this method. AIO SelfsupervisedLearning
    excludes human-annotated labels, Distillation describes large-to-small compression,
    and RegularizationLayer is a layer: none supplies an equivalent class for this
    algorithm. No normalized identity match was found across all 442 pinned AIO labels/scoped
    synonyms and 230 preceding native IDs/names/aliases. Full-checkout fixed-string
    searches included ignored and hidden files in both worktree and main checkout;
    matches concern prior discovery leads and the Pi-model normalization regression.
    Ten exact AIO CLASS nodes, their scoped synonyms and outgoing edges, plus five
    neighboring native records were inspected. The corrected Unicode-aware normalizer
    preserves Π; the previous Pi-model/Model collision was a lexical defect, not semantic
    identity (review issue #58).'
  details: 'Given B labeled examples with one-hot labels and B unlabeled examples,
    augment each labeled input once and each unlabeled input K times. Average the
    current classifier probabilities across the K views of each unlabeled input, then
    sharpen the average q_bar using q_c=q_bar_c^(1/T)/sum_j q_bar_j^(1/T), for T>0;
    treat these guessed labels as constants during differentiation. Create augmented
    labeled pairs X_hat of size B and unlabeled pairs U_hat of size KB, then shuffle
    their concatenation into W. Mix each X_hat pair with the corresponding first B
    pairs in W, and each U_hat pair with the corresponding remaining KB pairs. For
    each MixUp operation draw lambda from Beta(alpha,alpha), alpha>0, set lambda_prime=max(lambda,1−lambda),
    and combine both inputs and targets with weights lambda_prime and 1−lambda_prime,
    keeping at least half of the first pair. For the resulting X_prime and U_prime,
    minimize average soft-target cross-entropy over X_prime plus lambda_u/(C|U_prime|)
    times sum over U_prime of squared target/prediction differences, where C is the
    number of classes. The reported implementation ramps lambda_u linearly. Guessed
    labels use current-model predictions; the evaluation-only weight EMA in Section
    4.1 is not a Mean Teacher target generator. Limits: The original setup pairs B
    labeled examples with B unlabeled examples and K augmentations per unlabeled input.
    Alternative batching or interpolation rules require an explicit variant scope.
    For 0<T<1 sharpening concentrates probability. As a curator consequence of the
    formula, the T→0 limit is one-hot only with a unique maximum; tied maxima retain
    equal limiting mass. T>1 smooths rather than sharpens. Correct label-preserving
    augmentation and useful interpolation are assumptions; guessed labels can be wrong
    and the algorithm has no defining hard confidence threshold. The record does not
    assert published error rates or universal superiority. Reported T, K, alpha, lambda_u
    and evaluation-EMA settings are experimental choices, not fixed constants of every
    implementation.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A reusable classifier-training procedure, not a trained instance,
      layer, generic task or result.
    evidence_ids:
    - mixmatch-source-0
  - name: aio-relations
    value: 'related_match: AIO:Classification; related_match: AIO:MachineLearningTask'
    definition: Algorithm-to-task associations only; local identity and semi-supervised
      scope are preserved.
    evidence_ids:
    - mapping
- assessment_id: gradient-boundaries
  area: consistency
  topic: Which quantities receive gradients or are averaged
  outcome: supported
  target_ids:
  - AIMech:PiModel
  - AIMech:TemporalEnsembling
  - AIMech:MeanTeacher
  - AIMech:MixMatch
  evidence_ids:
  - pimodel-source-0
  - pimodel-source-1
  - temporalensembling-source-0
  - temporalensembling-source-1
  - meanteacher-source-0
  - meanteacher-source-1
  - mixmatch-source-0
  - neighbors
  summary: Two-sided Pi gradients, stored temporal targets, EMA weights and guessed/mixed
    soft targets remain distinct.
  details: Pi-model propagates gradients through both stochastic outputs; temporal
    ensembling uses fixed stored targets and fixed-alpha zero-initialized bias correction;
    Mean Teacher differentiates only the student and averages parameters after its
    step. MixMatch stops label-guessing gradients and uses current predictions for
    those guesses. Its separate evaluation EMA is not a Mean Teacher target rule.
    Temporal targets can be updated in the minibatch loop after their old values are
    used, as Algorithm2 explicitly permits.
- assessment_id: normalizations-and-limits
  area: consistency
  topic: Minibatch denominators, interpolation and sharpening
  outcome: supported
  target_ids:
  - AIMech:PiModel
  - AIMech:TemporalEnsembling
  - AIMech:MeanTeacher
  - AIMech:MixMatch
  evidence_ids:
  - pimodel-source-0
  - temporalensembling-source-0
  - mixmatch-source-0
  - meanteacher-source-0
  - meanteacher-source-1
  summary: Keep the original classifier-loss normalization and avoid unsupported limiting
    claims.
  details: The Pi and temporal pseudocode divides the labeled sum by the full batch
    count and squared consistency by classes times batch size. Mean Teacher loss coefficients
    and initialization are not forced to those conventions. MixMatch partitions a
    single shuffled concatenation, keeps lambda_prime=max(lambda,1-lambda), and applies
    different losses to its labeled and unlabeled outputs. At tied maxima the temperature-to-zero
    limit retains equal mass on the maxima; the one-hot special case requires uniqueness.
    This is a curator consequence of the formula, not a claimed author erratum or
    benchmark.
- assessment_id: unicode-remediation
  area: consistency
  topic: 'Resolved review issue58: Unicode identity comparison'
  outcome: supported
  target_ids:
  - AIMech:PiModel
  evidence_ids:
  - unicode-fix
  - identity
  - mapping
  summary: The Pi alias is now faithfully representable without weakening real collision
    checks.
  details: The actual synthetic corpus rejected Π-model as AIO:Model under ASCII filtering.
    The revised normalizer retains meaningful Unicode letters and marks while preserving
    plus variants; it does not transliterate Greek into Latin. Schema-independent
    letter/digit validation rejects mark-only and symbol-only names. Whole-collection
    regression tests and the current complete corpus gate pass. The issue is fixed
    in maintained code/tests/docs before this final self-review; no generated AIO
    record changed.
- assessment_id: mapping-boundaries
  area: grounding
  topic: Supervision, model/task and teacher-student scope
  outcome: supported
  target_ids:
  - AIMech:PiModel
  - AIMech:TemporalEnsembling
  - AIMech:MeanTeacher
  - AIMech:MixMatch
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Inspected mappings are related algorithm-to-task links.
  details: 'All four algorithms relate to AIO Classification and MachineLearningTask
    as algorithm-to-task associations. SemiSupervisedLLM is a different LLM pretraining/fine-tuning
    model class despite its related self-training synonym. SelfsupervisedLearning
    is specifically without human labels. Distillation describes large-to-small compression,
    EnsembleLearning implies multiple learning algorithms, RegularizationLayer is
    a layer, and Model is generic: none is an equivalent identity or justified subclass
    mapping. Native VAT, IMSAT, BYOL, DINO and SimSiam preserve different objectives,
    supervision and gradient/teacher conventions.'
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:PiModel
  - AIMech:TemporalEnsembling
  - AIMech:MeanTeacher
  - AIMech:MixMatch
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - unicode-fix
  - pimodel-source-0
  - pimodel-source-1
  - temporalensembling-source-0
  - temporalensembling-source-1
  - meanteacher-source-0
  - meanteacher-source-1
  - mixmatch-source-0
  rationale: Contemporaneous shared-parameter predictions, per-example historical
    prediction averages, teacher parameter EMA, and averaged/sharpened/mixed guessed
    labels define different algorithms. The neighboring VAT/IMSAT/BYOL/DINO/SimSiam
    objectives do not collapse these boundaries. No AIO rewrite, name merge or DRAFT
    promotion is warranted.
limitations:
- Adversarial author self-review, not independent approval. All four records remain
  DRAFT.
- Primary full-text access was achieved, but only the declared method/abstract/context
  pages were read; unseen pages are not reviewed evidence.
- The vendored check initially failed because sandbox DNS was unavailable; the authorized
  network-enabled rerun passed. This was a tool-access failure, not a source or curation
  defect.
- Issue58 concerns the maintained Unicode normalizer, tests and documentation, not
  an AIO ontology error. It was fixed before this final assessment.
- No new empirical performance claim, training execution or model-instance record.
- Four positive additions and a nonempty accounted discovery frontier leave the ongoing
  goal active.
tags:
- native-concepts
- semi-supervised-learning
- consistency
- unicode-identities
- self-review
- discovery-ongoing
```
