# Scientific self-review of learned and spatial mixing

- Review: 20261011T112348Z-learned-and-spatial-mixing
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T11:21:48Z
- Finished UTC: 2026-10-11T11:23:48Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Smart Augmentation, SamplePairing and CutMix with explicit generator, loss, label, schedule and patch-area boundaries. No actionable repository defect was identified in this scope.

## Scope And Provenance

All fields of the three newly maintained augmentation records.

Selection: Exact three IDs from the discovery ledger; no sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 5cd31f98eaeec174bbe24ff9bb8543b6d18df02c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SmartAugmentation | data/curated/SmartAugmentation.yaml | maintained | Smart Augmentation |
| AIMech:SamplePairing | data/curated/SamplePairing.yaml | maintained | SamplePairing |
| AIMech:CutMix | data/curated/CutMix.yaml | maintained | CutMix |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:SmartAugmentation, AIMech:SamplePairing, AIMech:CutMix | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 64.00s (0:01:03)<br>Checked 442 record(s); 0 failed.<br>Checked 256 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 59 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 56,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:SmartAugmentation, AIMech:SamplePairing, AIMech:CutMix | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| Finite example-mixing calculations | passed | True | AIMech:SmartAugmentation, AIMech:SamplePairing, AIMech:CutMix | {"pairing": {"ordered_anchor_losses": [0.2231435513142097, 1.6094379124341003], "symmetric_hard_loss": 0.916290731874155, "soft_half_loss": 0.916290731874155, "ordered_pair_choices": 9, "distinct_scalar_averages": 5}, "cutmix": {"nominal_lambda": 0.75, "actual_pasted_area": 4, "actual_lambda": 0.9375, "nominal_target_ce": 0.5697171415941824, "actual_target_ce": 0.3097869488842029}, "reference_mse": {"reference_support": [-1, 1], "midpoint_mse": 1.0, "endpoint_mse": 2.0}, "scope": "Finite illustrative inputs. Expected-loss equivalence requires exchangeable ordering and a loss linear in targets. MSE example does not assert collapse of a joint classifier/generator. No performance or author-code reproduction."} |

## Scientific And Domain Assessments

### Identity, definition, method, source conventions and AIO relations

evidence: supported. Targets: AIMech:SmartAugmentation.

Smart Augmentation denotes Lemley et al.’s learned same-class synthesis procedure, not all automatically chosen augmentation policies. It differs from fixed averaging in SamplePairing, convex input/target interpolation in MixUp, adaptive coefficient regions in AdaMixUp, and adversarial or latent-data generative formulations. The two networks cooperate through training losses; a generator does not by itself imply a GAN minimax game. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 253 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main checkout, returning 27 lines in each checkout. These were neighboring-record and review references or prior candidate leads, not existing records for these identities. Twelve exact AIO CLASS nodes with synonyms and outgoing edges and six neighboring native mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

During training, an augmentation network A takes same-class examples and produces a synthetic example of the original sample type and spatial shape. A reference example from that class supplies an augmentation loss L_A, while a target network B supplies its task loss L_B. Backpropagate through B into A using a combined objective f(L_A,L_B), which may be weighted or scheduled. A can be shared across classes or specialized into separate class-dependent networks. In the published grayscale realization, stack k same-class input images as channels, produce a one-channel image, and choose an additional same-class reference that is not one of those inputs. L_A is mean squared error to this reference; B processes the generated image and the reference as separate examples with categorical cross-entropy L_B. Figure 9 combines losses as alpha*L_A+beta*L_B. At test time discard A and use B on ordinary examples. Multi-example blending is the central construction, while the reported experiments also include a one-input setting; fixed channel counts, architectures and weights are protocol choices. Limits: Same-class input selection and a reference loss encourage class-consistent outputs but do not certify semantic label preservation or membership in the true data manifold. The paper’s optimality and convergence language describes the intended training behavior; no proof of globally optimal augmentations or universal generalization improvement is asserted. The reconstruction and classification terms can compete, and their weighting and schedule affect the learned generator. A synthetic output need not look like a natural image to be used by the method. The concrete channel-stacking, MSE and categorical-cross-entropy setup is one published realization. The record does not make the experimental architecture, alpha/beta values or number of augmenters universal requirements.

### Identity, definition, method, source conventions and AIO relations

evidence: supported. Targets: AIMech:SamplePairing.

SamplePairing is the equal-image-weight, anchor-label procedure of Inoue, distinct as a training protocol from the standard Beta-distributed input/target MixUp construction. This distinction does not imply that every expected objective differs: under exchangeable pairing and a loss linear in targets, averaging the anchor-label losses over both orders matches the half-and-half target loss for the same averaged image. The paper itself discusses this relationship. It is also distinct from learned Smart Augmentation and from spatial patch replacement in CutMix. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 253 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main checkout, returning 27 lines in each checkout. These were neighboring-record and review references or prior candidate leads, not existing records for these identities. Twelve exact AIO CLASS nodes with synonyms and outgoing edges and six neighboring native mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

For a training anchor, randomly select a partner from the training set without requiring the same class. Apply ordinary image augmentations to the inputs when used, then average corresponding pixels and channels with equal weights. Train on the mixed image using only the anchor label; the partner label is not required by this rule. The published training schedule starts without SamplePairing, enables it after a warm-up, intermittently disables it during training, and finishes with a no-pairing fine-tuning phase. The source uses one warm-up epoch for ILSVRC and 100 for the other datasets, then alternates 300,000 paired / 100,000 unpaired images for ILSVRC or eight paired / two unpaired epochs otherwise. These numerical intervals are experimental choices, not the identity of every use. A learned augmenter, a random mixing ratio, same-class pairing and label interpolation are not required by the original procedure. Limits: Averaged images can contain incompatible classes; the assigned anchor label is a training convention, not a claim that the mixture has a unique correct semantic label. The paper’s N-squared count describes ordered pairing choices. Commutativity and duplicate inputs can make different pairings produce the same averaged image, so it is not a guarantee of N-squared distinct visual samples. The expected-loss relation to half-and-half soft labels requires the stated symmetry and loss assumptions. It does not equate individual sampled gradients, arbitrary pair distributions, the full training schedules or the original randomly weighted MixUp procedure. The source’s training-accuracy ceiling discussion is idealized and does not establish a universal bound for every finite training run. No benchmark advantage, training-cost equivalence or medical-task result is imported.

### Identity, definition, method, source conventions and AIO relations

evidence: supported. Targets: AIMech:CutMix.

CutMix is spatial patch mixing with area-weighted targets. It is distinct from whole-image intensity averaging, zero masking, learned synthesis and hidden-representation interpolation. The record describes input-image CutMix; feature-level variants are not silently treated as an identical architecture or layer. Its official implementation profile is pinned separately from the proceedings formula. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 253 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main checkout, returning 27 lines in each checkout. These were neighboring-record and review references or prior candidate leads, not existing records for these identities. Twelve exact AIO CLASS nodes with synonyms and outgoing edges and six neighboring native mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Choose two training images and a binary spatial mask M. Construct M*x_A+(1−M)*x_B, preserving anchor pixels outside the rectangle and using donor pixels inside it. Train against lambda*y_A+(1−lambda)*y_B, with lambda representing the retained anchor area fraction. The paper draws a nominal coefficient from Beta(alpha,alpha), samples the rectangle center uniformly over the image, and sets nominal side lengths to the image dimensions times sqrt(1−lambda). The published experiments use alpha=1. The donor patch is taken from the same spatial coordinates as the overwritten anchor region. Unlike MixUp, individual pixels are selected from one source rather than blended throughout the image; unlike Cutout, the removed region is filled with another training image and target weights reflect both sources. On a discrete image, clipping and integer box construction can change the nominal area, so the inspected implementation recomputes the target coefficient from the actual rectangle. When beta is positive and the minibatch application draw passes cutmix_prob, the pinned implementation samples a Beta coefficient, permutes the batch, constructs a shared rectangle and replaces that region with the permuted donor pixels. rand_bbox converts each nominal side length to an integer, uses half-width floor division on each side of a random integer center and clips endpoints to the image dimensions. It then sets lambda=1−rectangle_area/image_area and sums lambda times the anchor cross-entropy with 1−lambda times the donor cross-entropy. With this shared coefficient, the objective equals cross-entropy against the correspondingly mixed targets. Training continues by backpropagation; ordinary unmodified inputs and labels are used when the application condition fails. Limits: Patch area is a heuristic for class-target contribution; it need not equal the visible object area or semantic information retained. A pasted patch may contain background or remove the discriminative object region. Integer side lengths, floor division and boundary clipping make the actual area differ from the nominal Beta draw. The realized target coefficient is not generally distributed as the original Beta variable. The pinned training code uses one application decision, rectangle and coefficient for a minibatch and a random permutation for partners. Per-example variants and feature-level CutMix require separate version-specific descriptions. The script’s beta argument controls the Beta distribution, while alpha controls PyramidNet width; these names are not the paper’s mathematical alpha convention. Default beta and cutmix_prob are zero, so the augmentation must be enabled by configuration. The implementation was read, not executed. Old API usage and unspecified runtime dependencies preclude an execution guarantee. Logged training error against the anchor labels is distinct from the mixed-target training objective. No universal localization, robustness or performance improvement is asserted.

### Cooperative synthesis and class-reference supervision

consistency: supported. Targets: AIMech:SmartAugmentation.

Retain the learned same-class synthesis identity with scoped experimental realization.

A receives same-class examples, uses a distinct same-class reference in the concrete setup, and receives task gradients through B. The concrete MSE and CE losses are positively combined in Figure9; this is not a GAN minimax game. Original and generated examples feed B separately, and A is discarded at inference. Class-specific or shared A networks are alternatives. Multi-input blending is central, while the paper includes a one-input configuration, so a universal minimum of two inputs is not asserted. Reference MSE cannot by itself guarantee naturalness or true class-manifold membership.

### Anchor targets, schedule and expected-loss equivalence

consistency: supported. Targets: AIMech:SamplePairing.

Retain the named equal-average training procedure without overstating objective differences.

The method uses equal input weights and the anchor target, with warm-up, intermittent no-pairing and final fine-tuning in the published schedule. Numeric intervals are protocol-specific. For exchangeable pair orders and a loss linear in targets, the averaged hard-anchor objective equals the half-and-half target objective; this does not equate one sampled update or the full standard random-Beta MixUp protocol. Ordered draws can share identical averaged images, and the source’s idealized training-accuracy discussion is not imported as an unconditional bound.

### Nominal Beta draw, discrete rectangle and actual target area

consistency: supported. Targets: AIMech:CutMix.

Retain spatial replacement with source-specific area correction and batch scope.

The main paper defines masked pixel replacement and target interpolation. The pinned code samples one rectangle/permutation and coefficient per minibatch, floors half-widths and clips endpoints, then recomputes the label coefficient from the realized area. Two weighted CE calls implement the mixed-target objective for the shared coefficient. Its beta option corresponds to paper alpha; its alpha option controls network width. Defaults disable augmentation, and logged anchor-label error is not the mixed-target objective. No author code was executed or modern-runtime compatibility established. Pixel area is not a measurement of semantic object contribution.

### Algorithms, preprocessing, tasks and generator architectures

grounding: supported. Targets: AIMech:SmartAugmentation, AIMech:SamplePairing, AIMech:CutMix.

Retain all three source-distinct native concepts with related AIO mappings.

All three training procedures relate to DataAugmentation and SupervisedLearning without equating an algorithm to a preprocessing category or learning task. Smart Augmentation trains a generator cooperatively with a classifier and is not a GAN minimax architecture; SamplePairing and CutMix require no learned generator. None of the three is the general BayesianNetwork, a GAN-AugmentedLLM, an image-augmentation layer or a parameter-penalty regularization layer. Their procedural scope differs from existing MixUp, Manifold Mixup, AdaMixUp, Bayesian DA, Cutout and AutoAugment.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:SmartAugmentation, AIMech:SamplePairing, AIMech:CutMix. Smart Augmentation learns same-class synthesis through reference and classifier losses; SamplePairing uses equal image averaging, an anchor target and a staged schedule; CutMix replaces spatial regions and weights targets by image area. Limited expected-loss equivalence under explicit assumptions does not collapse these distinct constructions and protocols.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T112012Z-learned-and-spatial-mixing.json | supports | All 442 AIO labels/scoped synonyms and 253 preceding native IDs/names/aliases were compared with the three candidates. No normalized identity match was found, and each candidate name/alias list was also checked for internal normalized duplicates. Full fixed-string searches included ignored and hidden files in both checkouts and returned 27 lines each after main was fast-forwarded. Every returned context was inspected: references in PBA/FAA records, saved reviews or pending discovery leads, not existing records for these identities. Twelve exact AIO CLASS nodes with all scoped synonyms/outgoing edges and six maintained neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood. |
| mapping | sources/aio/aio.json; Twelve exact CLASS nodes and their scoped synonyms/outgoing edges in source_analysis.aio_mapping_inspection | supports | All three training procedures relate to DataAugmentation and SupervisedLearning without equating an algorithm to a preprocessing category or learning task. Smart Augmentation trains a generator cooperatively with a classifier and is not a GAN minimax architecture; SamplePairing and CutMix require no learned generator. None of the three is the general BayesianNetwork, a GAN-AugmentedLLM, an image-augmentation layer or a parameter-penalty regularization layer. Their procedural scope differs from existing MixUp, Manifold Mixup, AdaMixUp, Bayesian DA, Cutout and AutoAugment. |
| neighbors | research/discovery/20261011T112012Z-learned-and-spatial-mixing.json; source_analysis.aio_mapping_inspection.native_neighbors | supports | Read MixUp, Manifold Mixup, AdaMixUp, Bayesian DA, Cutout and AutoAugment mechanisms. Component sharing and limited expected-objective equivalence do not equate the complete training procedures. |
| finite-conventions | research/discovery/example-mixing-boundaries.py; calculate(): symmetric anchor losses, distinct averages, clipped patch and reference MSE | supports | The mean of two ordered anchor cross-entropies equals the half-weight soft-target loss, although an individual anchor loss differs. Nine illustrative ordered scalar pairs produce only five averaged values. A nominal 4x4 patch on an 8x8 image centered at the corner clips to 2x2, changing the anchor weight from 0.75 to 0.9375. Squared loss to references −1/+1 is smaller at midpoint 0 than endpoint 1, so a reference loss alone cannot certify support membership. These are original diagnostics, not training or author-code execution. |
| smartaugmentation-source-0 | https://arxiv.org/pdf/1703.08383v1; Section III A–C, Figures 1–3, and the concrete training realization in Section V A / Figure 9, PDF pp. 2–6 | supports | Smart Augmentation: Learning an Optimal Data Augmentation Strategy. arXiv:1703.08383v1, 24 March 2017; twelve-page author preprint. The actual PDF/code reading scopes are declared in the ledger; extraction and rendering do not themselves attest inspection. |
| samplepairing-source-0 | https://arxiv.org/pdf/1801.02929v2; Section 3 and Figure 1, PDF pp. 2–3; relationship to MixUp and between-class learning in Section 2, PDF p. 2 | supports | Data Augmentation by Pairing Samples for Images Classification. arXiv:1801.02929v2, 11 April 2018; eight-page author preprint. The actual PDF/code reading scopes are declared in the ledger; extraction and rendering do not themselves attest inspection. |
| cutmix-source-0 | https://openaccess.thecvf.com/content_ICCV_2019/papers/Yun_CutMix_Regularization_Strategy_to_Train_Strong_Classifiers_With_Localizable_Features_ICCV_2019_paper.pdf; Section 3.1, Equations (1)–(2), and Section 3.2, PDF pp. 3–4 / printed pp. 6025–6026 | supports | CutMix: Regularization Strategy to Train Strong Classifiers with Localizable Features. ICCV 2019 official proceedings PDF; ten pages. The actual PDF/code reading scopes are declared in the ledger; extraction and rendering do not themselves attest inspection. |
| cutmix-source-1 | https://github.com/clovaai/CutMix-PyTorch/blob/2d8eb68faff7fe4962776ad51d175c3b01a25734/train.py; train.py lines 170–175, 220–255 and 279–295: cross-entropy, permutation, area correction and clipped integer box; defaults at 56–63 | supports | CutMix official PyTorch implementation: training and rectangle sampling. Official author repository at commit 2d8eb68faff7fe4962776ad51d175c3b01a25734, train.py; statically inspected, not executed. The actual PDF/code reading scopes are declared in the ledger; extraction and rendering do not themselves attest inspection. |

## Limits And Additional Notes

- Adversarial author self-review only; all three records remain DRAFT.
- Only declared source pages and code lines were inspected. No accuracy, localization, robustness, universal optimality or runtime result is reproduced.
- The CutMix HTML landing page returned403, while its official PDF and pinned author source were accessible. The arXiv sources are scoped to their exact inspected versions.
- The finite examples illustrate mathematical boundaries; they do not prove behavior of complete trained systems. SamplePairing expectation equivalence requires symmetry and target-linear loss, and a reference-MSE example does not establish collapse under a joint task loss.
- No actionable repository defect was identified after the stated source qualifications, so no review issue was manufactured. This does not change unrelated historical findings.
- Three additions and a nonempty inherited/new frontier leave discovery active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T112348Z-learned-and-spatial-mixing
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of learned and spatial mixing
started_at: '2026-10-11T11:21:48Z'
finished_at: '2026-10-11T11:23:48Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed all three records
    against the declared primary methods, rendered pages, pinned CutMix source, twelve
    exact AIO nodes and six neighboring records, and checked original finite arithmetic.
    This is not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Smart Augmentation, SamplePairing and CutMix with explicit generator,
  loss, label, schedule and patch-area boundaries. No actionable repository defect
  was identified in this scope.
source:
  git_revision: 5cd31f98eaeec174bbe24ff9bb8543b6d18df02c
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/Classification.yaml
    sha256: d97da621c5052c7ab913cda95184ea2cca274f803298fd5f2c1273a22a211219
    role: context
  - path: data/aio/DataAugmentation.yaml
    sha256: e99fd76071e8b52cbe8ed53f694b30093d7fb7a8af2e225f2f158f5cab5f11ae
    role: context
  - path: data/aio/DataEnhancement.yaml
    sha256: 89c2ba48f7ce9c45ed61f6fc7efa3fb416a0d209fd322342d388a8063945fa4f
    role: context
  - path: data/aio/GenerativeAdversarialNetwork.yaml
    sha256: 4f5080d92af8eaea513deed39c60679f0eb7a62d03e5be0d0d8d5c966a9a4544
    role: context
  - path: data/aio/GenerativeAdversarialNetworkAugmentedLLM.yaml
    sha256: d3816d7bd1a3f08e85650e82c1fee6091a8ec8635fb26fec429248a5602cc0de
    role: context
  - path: data/aio/ImageAugmentationLayer.yaml
    sha256: b9d1313742a22376bf8de6b48359beb8868e5b312e8b27cb221c6eb73e2252c0
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/Preprocessing.yaml
    sha256: 2c4a30f4f829a757be1feabf78d15780eedf93681a62eede3e76b2304f21bb7a
    role: context
  - path: data/aio/RegularizationLayer.yaml
    sha256: d4280bbc058b841655bcfcea7ef1dd1e05ac5e0211a860045f13eaa30933dbae
    role: context
  - path: data/aio/SupervisedLearning.yaml
    sha256: 472f033f91a14c8727e525ddd30f82fcaf16a2514fa8f062667fb94fc9c9b718
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/curated/AdaMixUp.yaml
    sha256: 17fe1d86137e8d199f232e6cf1f3e460dd2b5b79631d01e0b2192dba9692fa35
    role: context
  - path: data/curated/AutoAugment.yaml
    sha256: 29dec7588a9f992bb2bdaa71cde95d0bdb4d3a96353337f1149e61fa8099a9c8
    role: context
  - path: data/curated/BayesianDataAugmentation.yaml
    sha256: 4d95781fa743392ee3bcda4cf5cb3d79a35052750a01e090d2bc54b5693e14b5
    role: context
  - path: data/curated/CutMix.yaml
    sha256: 6df1e158450a1027c392eca1304ec4f0f96f83fd0be32e40d9c12a64a31211c1
    role: target
  - path: data/curated/Cutout.yaml
    sha256: 75d135f2df1b532c4752d93b7c1dac326dca3b50ea4b906fe6b3673bade3b1da
    role: context
  - path: data/curated/ManifoldMixup.yaml
    sha256: 0df5cfeb08de7758bd9cee4eba3382681f8183f6c37b2da8265e05bd49ddb915
    role: context
  - path: data/curated/MixUp.yaml
    sha256: 2f7e6cd92b02c2b258d3b1be9f541b6aa1593416032fc55da7250821d179a724
    role: context
  - path: data/curated/SamplePairing.yaml
    sha256: 17d9c1c5de57002bebfdca45e0c5691fd62bceef7fb42d63007c69e0ca996426
    role: target
  - path: data/curated/SmartAugmentation.yaml
    sha256: ece943fce492754c1915b163d1ea3e6c61b6e790ece125b2ee762198d4780b6b
    role: target
  - path: research/discovery/20261011T112012Z-learned-and-spatial-mixing.json
    sha256: e114f77fe39790abe5346cc1f55738588d686d208260acf144f3e877688f38b9
    role: context
  - path: research/discovery/example-mixing-boundaries.py
    sha256: bbd7bf12ebef2e8e697c994f758bd02beeb253532c0ff2469defeed66850bdd3
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
- target_id: AIMech:SmartAugmentation
  path: data/curated/SmartAugmentation.yaml
  label: Smart Augmentation
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SmartAugmentation.yaml
    role: maintained
- target_id: AIMech:SamplePairing
  path: data/curated/SamplePairing.yaml
  label: SamplePairing
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SamplePairing.yaml
    role: maintained
- target_id: AIMech:CutMix
  path: data/curated/CutMix.yaml
  label: CutMix
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CutMix.yaml
    role: maintained
scope:
  description: All fields of the three newly maintained augmentation records.
  selection: Exact three IDs from the discovery ledger; no sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:SmartAugmentation
  - AIMech:SamplePairing
  - AIMech:CutMix
  exclusions:
  - target: Older records and unselected candidates
    reason: Neighbors were read for identity and boundaries, not a complete new review
      of the older corpus.
  - target: Unread papers, pages, outcomes and implementation paths
    reason: Only declared source scopes were inspected; no model or downloaded implementation
      was executed.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:SmartAugmentation
  - AIMech:SamplePairing
  - AIMech:CutMix
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 64.00s (0:01:03)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 256 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 59 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 56,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:SmartAugmentation
  - AIMech:SamplePairing
  - AIMech:CutMix
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
- check_id: finite-arithmetic
  name: Finite example-mixing calculations
  command: python3 research/discovery/example-mixing-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SmartAugmentation
  - AIMech:SamplePairing
  - AIMech:CutMix
  exit_code: 0
  expected_exit_code: 0
  summary: '{"pairing": {"ordered_anchor_losses": [0.2231435513142097, 1.6094379124341003],
    "symmetric_hard_loss": 0.916290731874155, "soft_half_loss": 0.916290731874155,
    "ordered_pair_choices": 9, "distinct_scalar_averages": 5}, "cutmix": {"nominal_lambda":
    0.75, "actual_pasted_area": 4, "actual_lambda": 0.9375, "nominal_target_ce": 0.5697171415941824,
    "actual_target_ce": 0.3097869488842029}, "reference_mse": {"reference_support":
    [-1, 1], "midpoint_mse": 1.0, "endpoint_mse": 2.0}, "scope": "Finite illustrative
    inputs. Expected-loss equivalence requires exchangeable ordering and a loss linear
    in targets. MSE example does not assert collapse of a joint classifier/generator.
    No performance or author-code reproduction."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T112012Z-learned-and-spatial-mixing.json
  accessed_at: '2026-10-11T11:21:48Z'
  support: supports
  summary: 'All 442 AIO labels/scoped synonyms and 253 preceding native IDs/names/aliases
    were compared with the three candidates. No normalized identity match was found,
    and each candidate name/alias list was also checked for internal normalized duplicates.
    Full fixed-string searches included ignored and hidden files in both checkouts
    and returned 27 lines each after main was fast-forwarded. Every returned context
    was inspected: references in PBA/FAA records, saved reviews or pending discovery
    leads, not existing records for these identities. Twelve exact AIO CLASS nodes
    with all scoped synonyms/outgoing edges and six maintained neighboring mechanisms
    were inspected. Absence is bounded to this snapshot and semantic neighborhood.'
  search_scope: All 442 pinned AIO labels/scoped synonyms and 253 preceding maintained
    IDs/names/aliases; both full checkouts including ignored/hidden files; candidate-internal
    normalized identity uniqueness.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Twelve exact CLASS nodes and their scoped synonyms/outgoing edges in source_analysis.aio_mapping_inspection
  accessed_at: '2026-10-11T11:21:48Z'
  support: supports
  summary: All three training procedures relate to DataAugmentation and SupervisedLearning
    without equating an algorithm to a preprocessing category or learning task. Smart
    Augmentation trains a generator cooperatively with a classifier and is not a GAN
    minimax architecture; SamplePairing and CutMix require no learned generator. None
    of the three is the general BayesianNetwork, a GAN-AugmentedLLM, an image-augmentation
    layer or a parameter-penalty regularization layer. Their procedural scope differs
    from existing MixUp, Manifold Mixup, AdaMixUp, Bayesian DA, Cutout and AutoAugment.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T112012Z-learned-and-spatial-mixing.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors
  accessed_at: '2026-10-11T11:21:48Z'
  support: supports
  summary: Read MixUp, Manifold Mixup, AdaMixUp, Bayesian DA, Cutout and AutoAugment
    mechanisms. Component sharing and limited expected-objective equivalence do not
    equate the complete training procedures.
- evidence_id: finite-conventions
  kind: record_content
  reference: research/discovery/example-mixing-boundaries.py
  locator: 'calculate(): symmetric anchor losses, distinct averages, clipped patch
    and reference MSE'
  accessed_at: '2026-10-11T11:21:48Z'
  snapshot_sha256: bbd7bf12ebef2e8e697c994f758bd02beeb253532c0ff2469defeed66850bdd3
  support: supports
  summary: The mean of two ordered anchor cross-entropies equals the half-weight soft-target
    loss, although an individual anchor loss differs. Nine illustrative ordered scalar
    pairs produce only five averaged values. A nominal 4x4 patch on an 8x8 image centered
    at the corner clips to 2x2, changing the anchor weight from 0.75 to 0.9375. Squared
    loss to references −1/+1 is smaller at midpoint 0 than endpoint 1, so a reference
    loss alone cannot certify support membership. These are original diagnostics,
    not training or author-code execution.
- evidence_id: smartaugmentation-source-0
  kind: primary_source
  reference: https://arxiv.org/pdf/1703.08383v1
  locator: Section III A–C, Figures 1–3, and the concrete training realization in
    Section V A / Figure 9, PDF pp. 2–6
  accessed_at: '2026-10-11T11:12:20Z'
  snapshot_sha256: 56eb7e916f469627751fc76a67f0ac64aa92939f1dfdaa7f49b6a738a7dab9aa
  support: supports
  summary: 'Smart Augmentation: Learning an Optimal Data Augmentation Strategy. arXiv:1703.08383v1,
    24 March 2017; twelve-page author preprint. The actual PDF/code reading scopes
    are declared in the ledger; extraction and rendering do not themselves attest
    inspection.'
- evidence_id: samplepairing-source-0
  kind: primary_source
  reference: https://arxiv.org/pdf/1801.02929v2
  locator: Section 3 and Figure 1, PDF pp. 2–3; relationship to MixUp and between-class
    learning in Section 2, PDF p. 2
  accessed_at: '2026-10-11T11:12:20Z'
  snapshot_sha256: af0e6c947d8309962f553593dfbf9d8c9c111f977fac48a9c831e1a8e3195281
  support: supports
  summary: Data Augmentation by Pairing Samples for Images Classification. arXiv:1801.02929v2,
    11 April 2018; eight-page author preprint. The actual PDF/code reading scopes
    are declared in the ledger; extraction and rendering do not themselves attest
    inspection.
- evidence_id: cutmix-source-0
  kind: primary_source
  reference: https://openaccess.thecvf.com/content_ICCV_2019/papers/Yun_CutMix_Regularization_Strategy_to_Train_Strong_Classifiers_With_Localizable_Features_ICCV_2019_paper.pdf
  locator: Section 3.1, Equations (1)–(2), and Section 3.2, PDF pp. 3–4 / printed
    pp. 6025–6026
  accessed_at: '2026-10-11T11:12:20Z'
  snapshot_sha256: 5ba5b422109b8ac311e92dea236b1c8258975c0b819176c3b3b6294ab0641440
  support: supports
  summary: 'CutMix: Regularization Strategy to Train Strong Classifiers with Localizable
    Features. ICCV 2019 official proceedings PDF; ten pages. The actual PDF/code reading
    scopes are declared in the ledger; extraction and rendering do not themselves
    attest inspection.'
- evidence_id: cutmix-source-1
  kind: primary_source
  reference: https://github.com/clovaai/CutMix-PyTorch/blob/2d8eb68faff7fe4962776ad51d175c3b01a25734/train.py
  locator: 'train.py lines 170–175, 220–255 and 279–295: cross-entropy, permutation,
    area correction and clipped integer box; defaults at 56–63'
  accessed_at: '2026-10-11T11:16:05Z'
  snapshot_sha256: 049026c020052932ac15a998eee027ae9eb7910fbb7934c8daa22fa3cb37189c
  support: supports
  summary: 'CutMix official PyTorch implementation: training and rectangle sampling.
    Official author repository at commit 2d8eb68faff7fe4962776ad51d175c3b01a25734,
    train.py; statically inspected, not executed. The actual PDF/code reading scopes
    are declared in the ledger; extraction and rendering do not themselves attest
    inspection.'
assessments:
- assessment_id: smartaugmentation
  area: evidence
  topic: Identity, definition, method, source conventions and AIO relations
  outcome: supported
  target_ids:
  - AIMech:SmartAugmentation
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - smartaugmentation-source-0
  summary: Smart Augmentation denotes Lemley et al.’s learned same-class synthesis
    procedure, not all automatically chosen augmentation policies. It differs from
    fixed averaging in SamplePairing, convex input/target interpolation in MixUp,
    adaptive coefficient regions in AdaMixUp, and adversarial or latent-data generative
    formulations. The two networks cooperate through training losses; a generator
    does not by itself imply a GAN minimax game. No normalized identity match was
    found across all 442 pinned AIO labels/scoped synonyms and 253 preceding native
    IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden
    files in both worktree and main checkout, returning 27 lines in each checkout.
    These were neighboring-record and review references or prior candidate leads,
    not existing records for these identities. Twelve exact AIO CLASS nodes with synonyms
    and outgoing edges and six neighboring native mechanisms were inspected. Absence
    is bounded to this snapshot and semantic neighborhood.
  details: 'During training, an augmentation network A takes same-class examples and
    produces a synthetic example of the original sample type and spatial shape. A
    reference example from that class supplies an augmentation loss L_A, while a target
    network B supplies its task loss L_B. Backpropagate through B into A using a combined
    objective f(L_A,L_B), which may be weighted or scheduled. A can be shared across
    classes or specialized into separate class-dependent networks. In the published
    grayscale realization, stack k same-class input images as channels, produce a
    one-channel image, and choose an additional same-class reference that is not one
    of those inputs. L_A is mean squared error to this reference; B processes the
    generated image and the reference as separate examples with categorical cross-entropy
    L_B. Figure 9 combines losses as alpha*L_A+beta*L_B. At test time discard A and
    use B on ordinary examples. Multi-example blending is the central construction,
    while the reported experiments also include a one-input setting; fixed channel
    counts, architectures and weights are protocol choices. Limits: Same-class input
    selection and a reference loss encourage class-consistent outputs but do not certify
    semantic label preservation or membership in the true data manifold. The paper’s
    optimality and convergence language describes the intended training behavior;
    no proof of globally optimal augmentations or universal generalization improvement
    is asserted. The reconstruction and classification terms can compete, and their
    weighting and schedule affect the learned generator. A synthetic output need not
    look like a natural image to be used by the method. The concrete channel-stacking,
    MSE and categorical-cross-entropy setup is one published realization. The record
    does not make the experimental architecture, alpha/beta values or number of augmenters
    universal requirements.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A defined augmentation/training procedure, not a layer, trained checkpoint,
      classifier architecture or broad learning task.
    evidence_ids:
    - smartaugmentation-source-0
  - name: aio-relations
    value: 'related_match: AIO:DataAugmentation; related_match: AIO:SupervisedLearning'
    definition: This procedure constructs training examples and specifies how a predictor
      is trained with them. The AIO target is augmentation in a preprocessing branch;
      this related association preserves the broader training and target-handling
      scope without asserting equivalence or a subclass relation. The predictor learns
      from class labels associated with generated or combined training examples. This
      is an algorithm-to-task association, not identity with the general supervised-learning
      task.
    evidence_ids:
    - mapping
- assessment_id: samplepairing
  area: evidence
  topic: Identity, definition, method, source conventions and AIO relations
  outcome: supported
  target_ids:
  - AIMech:SamplePairing
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - samplepairing-source-0
  summary: 'SamplePairing is the equal-image-weight, anchor-label procedure of Inoue,
    distinct as a training protocol from the standard Beta-distributed input/target
    MixUp construction. This distinction does not imply that every expected objective
    differs: under exchangeable pairing and a loss linear in targets, averaging the
    anchor-label losses over both orders matches the half-and-half target loss for
    the same averaged image. The paper itself discusses this relationship. It is also
    distinct from learned Smart Augmentation and from spatial patch replacement in
    CutMix. No normalized identity match was found across all 442 pinned AIO labels/scoped
    synonyms and 253 preceding native IDs/names/aliases. Full-checkout fixed-string
    searches included ignored and hidden files in both worktree and main checkout,
    returning 27 lines in each checkout. These were neighboring-record and review
    references or prior candidate leads, not existing records for these identities.
    Twelve exact AIO CLASS nodes with synonyms and outgoing edges and six neighboring
    native mechanisms were inspected. Absence is bounded to this snapshot and semantic
    neighborhood.'
  details: 'For a training anchor, randomly select a partner from the training set
    without requiring the same class. Apply ordinary image augmentations to the inputs
    when used, then average corresponding pixels and channels with equal weights.
    Train on the mixed image using only the anchor label; the partner label is not
    required by this rule. The published training schedule starts without SamplePairing,
    enables it after a warm-up, intermittently disables it during training, and finishes
    with a no-pairing fine-tuning phase. The source uses one warm-up epoch for ILSVRC
    and 100 for the other datasets, then alternates 300,000 paired / 100,000 unpaired
    images for ILSVRC or eight paired / two unpaired epochs otherwise. These numerical
    intervals are experimental choices, not the identity of every use. A learned augmenter,
    a random mixing ratio, same-class pairing and label interpolation are not required
    by the original procedure. Limits: Averaged images can contain incompatible classes;
    the assigned anchor label is a training convention, not a claim that the mixture
    has a unique correct semantic label. The paper’s N-squared count describes ordered
    pairing choices. Commutativity and duplicate inputs can make different pairings
    produce the same averaged image, so it is not a guarantee of N-squared distinct
    visual samples. The expected-loss relation to half-and-half soft labels requires
    the stated symmetry and loss assumptions. It does not equate individual sampled
    gradients, arbitrary pair distributions, the full training schedules or the original
    randomly weighted MixUp procedure. The source’s training-accuracy ceiling discussion
    is idealized and does not establish a universal bound for every finite training
    run. No benchmark advantage, training-cost equivalence or medical-task result
    is imported.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A defined augmentation/training procedure, not a layer, trained checkpoint,
      classifier architecture or broad learning task.
    evidence_ids:
    - samplepairing-source-0
  - name: aio-relations
    value: 'related_match: AIO:DataAugmentation; related_match: AIO:SupervisedLearning'
    definition: This procedure constructs training examples and specifies how a predictor
      is trained with them. The AIO target is augmentation in a preprocessing branch;
      this related association preserves the broader training and target-handling
      scope without asserting equivalence or a subclass relation. The predictor learns
      from class labels associated with generated or combined training examples. This
      is an algorithm-to-task association, not identity with the general supervised-learning
      task.
    evidence_ids:
    - mapping
- assessment_id: cutmix
  area: evidence
  topic: Identity, definition, method, source conventions and AIO relations
  outcome: supported
  target_ids:
  - AIMech:CutMix
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - cutmix-source-0
  - cutmix-source-1
  summary: CutMix is spatial patch mixing with area-weighted targets. It is distinct
    from whole-image intensity averaging, zero masking, learned synthesis and hidden-representation
    interpolation. The record describes input-image CutMix; feature-level variants
    are not silently treated as an identical architecture or layer. Its official implementation
    profile is pinned separately from the proceedings formula. No normalized identity
    match was found across all 442 pinned AIO labels/scoped synonyms and 253 preceding
    native IDs/names/aliases. Full-checkout fixed-string searches included ignored
    and hidden files in both worktree and main checkout, returning 27 lines in each
    checkout. These were neighboring-record and review references or prior candidate
    leads, not existing records for these identities. Twelve exact AIO CLASS nodes
    with synonyms and outgoing edges and six neighboring native mechanisms were inspected.
    Absence is bounded to this snapshot and semantic neighborhood.
  details: 'Choose two training images and a binary spatial mask M. Construct M*x_A+(1−M)*x_B,
    preserving anchor pixels outside the rectangle and using donor pixels inside it.
    Train against lambda*y_A+(1−lambda)*y_B, with lambda representing the retained
    anchor area fraction. The paper draws a nominal coefficient from Beta(alpha,alpha),
    samples the rectangle center uniformly over the image, and sets nominal side lengths
    to the image dimensions times sqrt(1−lambda). The published experiments use alpha=1.
    The donor patch is taken from the same spatial coordinates as the overwritten
    anchor region. Unlike MixUp, individual pixels are selected from one source rather
    than blended throughout the image; unlike Cutout, the removed region is filled
    with another training image and target weights reflect both sources. On a discrete
    image, clipping and integer box construction can change the nominal area, so the
    inspected implementation recomputes the target coefficient from the actual rectangle.
    When beta is positive and the minibatch application draw passes cutmix_prob, the
    pinned implementation samples a Beta coefficient, permutes the batch, constructs
    a shared rectangle and replaces that region with the permuted donor pixels. rand_bbox
    converts each nominal side length to an integer, uses half-width floor division
    on each side of a random integer center and clips endpoints to the image dimensions.
    It then sets lambda=1−rectangle_area/image_area and sums lambda times the anchor
    cross-entropy with 1−lambda times the donor cross-entropy. With this shared coefficient,
    the objective equals cross-entropy against the correspondingly mixed targets.
    Training continues by backpropagation; ordinary unmodified inputs and labels are
    used when the application condition fails. Limits: Patch area is a heuristic for
    class-target contribution; it need not equal the visible object area or semantic
    information retained. A pasted patch may contain background or remove the discriminative
    object region. Integer side lengths, floor division and boundary clipping make
    the actual area differ from the nominal Beta draw. The realized target coefficient
    is not generally distributed as the original Beta variable. The pinned training
    code uses one application decision, rectangle and coefficient for a minibatch
    and a random permutation for partners. Per-example variants and feature-level
    CutMix require separate version-specific descriptions. The script’s beta argument
    controls the Beta distribution, while alpha controls PyramidNet width; these names
    are not the paper’s mathematical alpha convention. Default beta and cutmix_prob
    are zero, so the augmentation must be enabled by configuration. The implementation
    was read, not executed. Old API usage and unspecified runtime dependencies preclude
    an execution guarantee. Logged training error against the anchor labels is distinct
    from the mixed-target training objective. No universal localization, robustness
    or performance improvement is asserted.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A defined augmentation/training procedure, not a layer, trained checkpoint,
      classifier architecture or broad learning task.
    evidence_ids:
    - cutmix-source-0
    - cutmix-source-1
  - name: aio-relations
    value: 'related_match: AIO:DataAugmentation; related_match: AIO:SupervisedLearning'
    definition: This procedure constructs training examples and specifies how a predictor
      is trained with them. The AIO target is augmentation in a preprocessing branch;
      this related association preserves the broader training and target-handling
      scope without asserting equivalence or a subclass relation. The predictor learns
      from class labels associated with generated or combined training examples. This
      is an algorithm-to-task association, not identity with the general supervised-learning
      task.
    evidence_ids:
    - mapping
- assessment_id: smart-boundaries
  area: consistency
  topic: Cooperative synthesis and class-reference supervision
  outcome: supported
  target_ids:
  - AIMech:SmartAugmentation
  evidence_ids:
  - smartaugmentation-source-0
  - finite-conventions
  - neighbors
  summary: Retain the learned same-class synthesis identity with scoped experimental
    realization.
  details: A receives same-class examples, uses a distinct same-class reference in
    the concrete setup, and receives task gradients through B. The concrete MSE and
    CE losses are positively combined in Figure9; this is not a GAN minimax game.
    Original and generated examples feed B separately, and A is discarded at inference.
    Class-specific or shared A networks are alternatives. Multi-input blending is
    central, while the paper includes a one-input configuration, so a universal minimum
    of two inputs is not asserted. Reference MSE cannot by itself guarantee naturalness
    or true class-manifold membership.
- assessment_id: pairing-boundaries
  area: consistency
  topic: Anchor targets, schedule and expected-loss equivalence
  outcome: supported
  target_ids:
  - AIMech:SamplePairing
  evidence_ids:
  - samplepairing-source-0
  - finite-conventions
  - neighbors
  summary: Retain the named equal-average training procedure without overstating objective
    differences.
  details: The method uses equal input weights and the anchor target, with warm-up,
    intermittent no-pairing and final fine-tuning in the published schedule. Numeric
    intervals are protocol-specific. For exchangeable pair orders and a loss linear
    in targets, the averaged hard-anchor objective equals the half-and-half target
    objective; this does not equate one sampled update or the full standard random-Beta
    MixUp protocol. Ordered draws can share identical averaged images, and the source’s
    idealized training-accuracy discussion is not imported as an unconditional bound.
- assessment_id: cutmix-boundaries
  area: consistency
  topic: Nominal Beta draw, discrete rectangle and actual target area
  outcome: supported
  target_ids:
  - AIMech:CutMix
  evidence_ids:
  - cutmix-source-0
  - cutmix-source-1
  - finite-conventions
  - neighbors
  summary: Retain spatial replacement with source-specific area correction and batch
    scope.
  details: The main paper defines masked pixel replacement and target interpolation.
    The pinned code samples one rectangle/permutation and coefficient per minibatch,
    floors half-widths and clips endpoints, then recomputes the label coefficient
    from the realized area. Two weighted CE calls implement the mixed-target objective
    for the shared coefficient. Its beta option corresponds to paper alpha; its alpha
    option controls network width. Defaults disable augmentation, and logged anchor-label
    error is not the mixed-target objective. No author code was executed or modern-runtime
    compatibility established. Pixel area is not a measurement of semantic object
    contribution.
- assessment_id: mapping-boundaries
  area: grounding
  topic: Algorithms, preprocessing, tasks and generator architectures
  outcome: supported
  target_ids:
  - AIMech:SmartAugmentation
  - AIMech:SamplePairing
  - AIMech:CutMix
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain all three source-distinct native concepts with related AIO mappings.
  details: All three training procedures relate to DataAugmentation and SupervisedLearning
    without equating an algorithm to a preprocessing category or learning task. Smart
    Augmentation trains a generator cooperatively with a classifier and is not a GAN
    minimax architecture; SamplePairing and CutMix require no learned generator. None
    of the three is the general BayesianNetwork, a GAN-AugmentedLLM, an image-augmentation
    layer or a parameter-penalty regularization layer. Their procedural scope differs
    from existing MixUp, Manifold Mixup, AdaMixUp, Bayesian DA, Cutout and AutoAugment.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:SmartAugmentation
  - AIMech:SamplePairing
  - AIMech:CutMix
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - smartaugmentation-source-0
  - samplepairing-source-0
  - cutmix-source-0
  - cutmix-source-1
  rationale: Smart Augmentation learns same-class synthesis through reference and
    classifier losses; SamplePairing uses equal image averaging, an anchor target
    and a staged schedule; CutMix replaces spatial regions and weights targets by
    image area. Limited expected-loss equivalence under explicit assumptions does
    not collapse these distinct constructions and protocols.
limitations:
- Adversarial author self-review only; all three records remain DRAFT.
- Only declared source pages and code lines were inspected. No accuracy, localization,
  robustness, universal optimality or runtime result is reproduced.
- The CutMix HTML landing page returned403, while its official PDF and pinned author
  source were accessible. The arXiv sources are scoped to their exact inspected versions.
- The finite examples illustrate mathematical boundaries; they do not prove behavior
  of complete trained systems. SamplePairing expectation equivalence requires symmetry
  and target-linear loss, and a reference-MSE example does not establish collapse
  under a joint task loss.
- No actionable repository defect was identified after the stated source qualifications,
  so no review issue was manufactured. This does not change unrelated historical findings.
- Three additions and a nonempty inherited/new frontier leave discovery active.
tags:
- native-concepts
- augmentation
- source-conventions
- self-review
- discovery-ongoing
```
