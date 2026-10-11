# Scientific self-review of channel and spatial feature gating

- Review: 20261011T124701Z-channel-and-spatial-feature-gating
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T12:43:39Z
- Finished UTC: 2026-10-11T12:47:01Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain SE blocks, channel-first CBAM and paper-version bottleneck attention with explicit component, gate, source-version, acronym and mapping boundaries. No actionable record defect was found in this scope.

## Scope And Provenance

All fields of the three newly maintained channel/spatial attention components.

Selection: Exact three IDs in the discovery ledger; no sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base e31cea02f2a4486b461872337e03685af1aaa9fa.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SqueezeAndExcitationBlock | data/curated/SqueezeAndExcitationBlock.yaml | maintained | Squeeze-and-Excitation block |
| AIMech:ConvolutionalBlockAttentionModule | data/curated/ConvolutionalBlockAttentionModule.yaml | maintained | Convolutional Block Attention Module |
| AIMech:BottleneckAttentionModule | data/curated/BottleneckAttentionModule.yaml | maintained | Bottleneck Attention Module |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:SqueezeAndExcitationBlock, AIMech:ConvolutionalBlockAttentionModule, AIMech:BottleneckAttentionModule | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 83.95s (0:01:23)<br>Checked 442 record(s); 0 failed.<br>Checked 282 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 69 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 67,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:SqueezeAndExcitationBlock, AIMech:ConvolutionalBlockAttentionModule, AIMech:BottleneckAttentionModule | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| Finite channel and spatial gating calculations | passed | True | AIMech:SqueezeAndExcitationBlock, AIMech:ConvolutionalBlockAttentionModule, AIMech:BottleneckAttentionModule | {"se": {"zero_logit_channel_gates": [0.5, 0.5, 0.5], "gate_sum": 1.5, "interpretation": "Independent sigmoid gates are not a normalized channel distribution."}, "cbam_order": {"channel_then_spatial": [[0.956905095733617, 2.926733543982767], [1.7805489823386014, -0.9076470342685989]], "spatial_then_channel": [[0.9635442008848872, 2.924360610762908], [1.7829960484609204, -0.9019000561462824]], "largest_absolute_difference": 0.006639105151270197, "interpretation": "Input-dependent stages need not commute; immediate gate products attenuate magnitudes."}, "bam_fusion": {"channel_logit": 2.0, "spatial_logit": -1.0, "paper_sum_gate": 0.7310585786300049, "pinned_code_product_gate": 0.11920292202211755, "paper_residual_multiplier": 1.7310585786300048, "code_residual_multiplier": 1.1192029220221176, "interpretation": "SUM and product fusion differ; both residual multipliers exceed one for finite logits."}} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, source conventions and AIO relations

evidence: supported. Targets: AIMech:SqueezeAndExcitationBlock.

This is the SE component from the 2018 paper, not a complete SENet architecture or its trained checkpoints. The component receives the feature tensor produced by a preceding transformation. Its channel weights vary with the input but are shared over spatial positions within each channel. SE block is the scoped alias; the paper title denotes networks assembled using these units. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 279 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 6 and 6 lines respectively. Every text hit was a prior candidate lead or a closely related variant lead. Seven exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and three native neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

For each channel of a spatial feature tensor, average all spatial values to obtain a channel descriptor. Pass that descriptor through a fully connected dimensionality reduction, ReLU, fully connected expansion to the original channel count and elementwise sigmoid. Broadcast each resulting weight across its corresponding spatial feature map and multiply elementwise. The reduction ratio controls the bottleneck capacity; the paper uses 16 in its main experiments rather than requiring that value for the concept. In its residual-network integration, this recalibration operates on the non-identity transformation before addition of the skip path. The module has learned parameters and remains part of the network during inference. Limits: The sigmoid gates are independent weights, not a softmax distribution or guaranteed class probabilities. For finite real logits they lie strictly between zero and one, so the immediate scaling cannot increase absolute input-feature magnitudes; emphasis is relative to other channels and the surrounding network. Floating-point saturation can reach numerical endpoints. Global averaging discards spatial arrangement in the descriptor. Channel gating therefore does not itself supply a location-specific attention map, although the spatial feature tensor is retained in the output. Reduction ratio, placement and surrounding architecture affect cost and behavior. Additional learned weights and operations do not imply negligible cost on every device. The source’s interpretation of particular channel activations is not a causal explanation or a universal accuracy claim. No author implementation or trained model was executed.

### Identity, definition, mechanism, source conventions and AIO relations

evidence: supported. Targets: AIMech:ConvolutionalBlockAttentionModule.

This record covers the canonical channel-first CBAM configuration from the 2018 paper. It is a reusable component rather than a complete CNN, detector or gradient-based explanation method. Spatial-first, parallel, channel-only and alternative pooling configurations are separately assessed variants, not silent replacements of this selected procedure. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 279 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 6 and 6 lines respectively. Every text hit was a prior candidate lead or a closely related variant lead. Seven exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and three native neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Compute global spatial average and maximum descriptors for every channel. Pass both through the same two-layer bottleneck MLP, with ReLU after its reduction layer, sum the resulting channel logits and apply sigmoid. Broadcast the channel weights over space and multiply them into the input tensor. From this channel-refined tensor, compute average and maximum maps over the channel axis, concatenate these two spatial maps, apply a convolution with a 7-by-7 kernel and sigmoid, then multiply the spatial weights across all channels. Thus the second attention stage depends on the output of the first, rather than being computed in parallel from the original tensor. The paper’s residual example applies the component before skip addition; the learned component also operates during inference. The pinned author implementation follows channel-then-spatial gating with average/max channel descriptors sharing one MLP. Its spatial path uses a bias-free 7-by-7 convolution followed by batch normalization and sigmoid, with no intervening ReLU. Optional pooling choices and no_spatial are exposed as code configurations. This static inspection does not establish runtime compatibility or reproduction of a trained checkpoint. Limits: Average and maximum channel descriptors share the same MLP parameters. The sum occurs before sigmoid, not between independently sigmoid-normalized channel weights. Spatial pooling runs over channels, whereas the channel stage pools over spatial positions. Reversing the stages or computing both from the original input generally changes the transformation. The spatial kernel and reduction ratio were selected empirically; the pinned implementation exposes alternative pooling and a channel-only switch, which are not the canonical configuration asserted here. Independent sigmoid gates need not sum to one. Each multiplicative gate attenuates immediate feature magnitude; relative emphasis is not an absolute amplification guarantee. The learned weights add parameters and computation. The source’s Grad-CAM visualizations and selected-image user study do not certify causal faithfulness, calibrated object probabilities or universal interpretability. CBAM itself is not Grad-CAM or a complete object detector, and no benchmark improvement or hardware-independent speed claim is curated.

### Identity, definition, mechanism, source conventions and AIO relations

evidence: supported. Targets: AIMech:BottleneckAttentionModule.

This record denotes Park and colleagues’ 2018 bottleneck attention module, scoped to the summation convention of arXiv1807.06514v2. The pinned author implementation uses a different fusion operation, recorded explicitly below. BAM is an ambiguous acronym also used by the 2021 Balanced Attention Mechanism paper; only the qualified bottleneck alias is assigned here. The module is distinct from sequential CBAM, channel-only SE and a complete CNN. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 279 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 6 and 6 lines respectively. Every text hit was a prior candidate lead or a closely related variant lead. Seven exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and three native neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

From the same input feature tensor, form a channel branch using global spatial averaging and a bottleneck MLP, and a spatial branch using a 1-by-1 channel reduction, two dilated 3-by-3 convolutions and a 1-by-1 projection to one spatial map. The selected paper equations place batch normalization at the outputs of both branches. Broadcast the channel and spatial logits to the input tensor shape, sum them and apply sigmoid to obtain the attention map. Multiply that map by the input and add the result back to the input. The source commonly places modules at downsampling bottlenecks and also studies other placements; its reduction ratio 16 and dilation 4 are experimental settings. The learned attention computation operates in both training and inference. The selected paper adds broadcast channel and spatial branch logits before sigmoid. The inspected BAM.forward instead multiplies those branch outputs before applying sigmoid and adding one. The code places batch normalization and ReLU in intermediate branch blocks rather than the terminal batch-normalization positions displayed in the paper equations. These are explicit source-version differences, not equivalent rewritings; the concept record uses the paper convention and does not certify the code as an exact implementation of it. Limits: The record distinguishes the selected paper’s SUM fusion from the pinned author code’s product fusion and normalization placement. These yield different attention maps; neither the repository README nor a shared module name proves that code reproduces the selected paper equations. For finite real logits the residual multiplier 1+sigmoid(logit) lies between one and two. The module therefore cannot directly attenuate the absolute magnitude of a nonzero input element; suppression in source prose is relative to other features or downstream computation. Floating-point sigmoid can reach numerical endpoints. The branch maps are constrained by their channel/spatial structure rather than arbitrary independent attention values at every tensor position. Learned attention is not automatically a calibrated explanation or semantic object mask. Placement and hyperparameters affect overhead and empirical results. The inspected standalone bam.py references gate_activation in ChannelGate without a parameter or binding for that name in the module. Its average-pooling call also assumes square spatial maps to produce a single descriptor. Static reading is not a successful runtime validation; no author code, model or supplementary benchmark was executed. The final BMVC PDF was inaccessible during this assessment.

### Global channel descriptors, independent gates and residual placement

consistency: supported. Targets: AIMech:SqueezeAndExcitationBlock.

Retain the SE block as a component.

Global spatial means feed a reduction/expansion MLP with ReLU and sigmoid. Gate values are independent rather than softmax-normalized, are shared spatially and do not amplify immediate feature magnitudes. Spatial arrangement is discarded in the descriptor, not in the entire output feature tensor. The residual example gates before adding the skip. The complete SENet and empirical performance are different scopes.

### Shared MLP, pooling axes and sequential refinement

consistency: supported. Targets: AIMech:ConvolutionalBlockAttentionModule.

Retain canonical channel-first CBAM.

The same MLP maps spatial average/max descriptors before logit addition and sigmoid. The spatial gate is computed from the channel-refined tensor by channel average/max pooling and a spatial convolution. Reversed or parallel computation is not equivalent. The pinned code adds spatial batch normalization and exposes alternative configurations; static reading does not certify execution. Grad-CAM pictures and a selected-image user study do not establish causal explanation.

### Parallel branches, residual gain, acronym and source disagreement

consistency: supported. Targets: AIMech:BottleneckAttentionModule.

Retain the paper-version bottleneck attention module with qualified alias.

Paper SUM fusion and pinned-code product fusion yield different gates; batch-normalization placement also differs. The finite residual factor exceeds one, so direct absolute attenuation would be false. The inspected module has an unbound gate_activation reference and square-spatial pooling assumption; no runtime validity is claimed. The 2021 Balanced Attention Mechanism is an abstract-only acronym-disambiguation lead, not a synonym or a newly asserted mechanism.

### Composite feature-map components versus specific attention operations

grounding: supported. Targets: AIMech:SqueezeAndExcitationBlock, AIMech:ConvolutionalBlockAttentionModule, AIMech:BottleneckAttentionModule.

Retain three distinct components with Layer broad matches.

All three specific feature-map components map broadly to Layer. Seven exact AIO nodes were inspected. AttentionLayer is dot-product/Luong-style; AdditiveAttentionLayer is Bahdanau-style, not merely summing channel/spatial maps. ConvolutionalLayer, global average/max pooling and SigmoidFunction denote ingredients rather than the composite component. Three native neighbors distinguish training-only parameter-free ADL, exact query/key attention computation in FlashAttention, and gradient-based post-hoc Grad-CAM localization. No acronym, attention wording or shared operation establishes identity.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:SqueezeAndExcitationBlock, AIMech:ConvolutionalBlockAttentionModule, AIMech:BottleneckAttentionModule. Channel-only recalibration, sequential channel/spatial gating and parallel residual attention have distinct transformations. The broad word attention, shared sigmoid operations or similar benchmarks do not establish equivalence.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T124335Z-channel-and-spatial-feature-gating.json | supports | Compared all 442 pinned AIO labels/scoped synonyms and 279 preceding native IDs/names/aliases, including candidate-internal normalized uniqueness. No identity match was found. Full-checkout fixed-string searches included ignored/hidden files and returned 6 worktree and 6 main lines; every hit was a candidate or related-variant lead. Seven exact AIO CLASS nodes with scoped synonyms/comments/outgoing edges and three native neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood. |
| mapping | sources/aio/aio.json; Seven exact CLASS nodes and their scoped synonyms/outgoing edges in source_analysis.aio_mapping_inspection | supports | All three specific feature-map components map broadly to Layer. Seven exact AIO nodes were inspected. AttentionLayer is dot-product/Luong-style; AdditiveAttentionLayer is Bahdanau-style, not merely summing channel/spatial maps. ConvolutionalLayer, global average/max pooling and SigmoidFunction denote ingredients rather than the composite component. Three native neighbors distinguish training-only parameter-free ADL, exact query/key attention computation in FlashAttention, and gradient-based post-hoc Grad-CAM localization. No acronym, attention wording or shared operation establishes identity. |
| neighbors | research/discovery/20261011T124335Z-channel-and-spatial-feature-gating.json; source_analysis.aio_mapping_inspection.native_neighbors | supports | Read the attention-based dropout layer, FlashAttention and Grad-CAM. Training-only stochastic spatial suppression, exact query/key attention computation and gradient-based localization differ from learned channel/spatial feature gates. |
| acronym | research/discovery/20261011T124335Z-channel-and-spatial-feature-gating.json; queries.acronym-check and BottleneckAttentionModule.identity_notes | context_only | The primary arXiv2104.07566v3 abstract names a distinct 2021 Balanced Attention Mechanism for super-resolution. Only its abstract was inspected for acronym disambiguation; the full method remains on the frontier. |
| finite-conventions | research/discovery/channel-spatial-gating-boundaries.py; calculate(): independent sigmoid gates, noncommuting channel/spatial stages, SUM versus product branch fusion and residual multipliers | supports | Original finite examples distinguish independent sigmoid gates from normalized distributions, demonstrate order-dependent channel/spatial gating, and compare SUM/product BAM fusion and residual multipliers. No author algorithm or model was executed. |
| squeezeandexcitationblock-source-0 | https://openaccess.thecvf.com/content_cvpr_2018/papers/Hu_Squeeze-and-Excitation_Networks_CVPR_2018_paper.pdf; Section3, Equations2–4, PDF pp.2–3 (printed7133–7134); Figures2–3 and complexity, PDFp.4; Section6.4/7, PDF pp.7–8 | supports | Squeeze-and-Excitation Networks. CVPR 2018, pp.7132–7141; 10-page proceedings PDF. Actual PDF and static-code reading scopes are declared in the ledger. Source rendering alone does not attest inspection. |
| convolutionalblockattentionmodule-source-0 | https://openaccess.thecvf.com/content_ECCV_2018/papers/Sanghyun_Woo_Convolutional_Block_Attention_ECCV_2018_paper.pdf; Section3, Equations1–3 and Figure2, PDF pp.4–6; residual placement Figure3, PDFp.7; arrangement discussion PDFp.9; interpretability scope Sections4.3–4.4, PDF pp.10–13; conclusion PDFp.14 | supports | CBAM: Convolutional Block Attention Module. ECCV 2018; 17-page CVF proceedings PDF. Actual PDF and static-code reading scopes are declared in the ledger. Source rendering alone does not attest inspection. |
| convolutionalblockattentionmodule-source-1 | https://github.com/Jongchan/attention-module/blob/459efad0e05ee7dde50c41ca10a3d0800bc3792a/MODELS/cbam.py; ChannelGate, ChannelPool, SpatialGate, BasicConv and CBAM classes, complete MODELS/cbam.py at the cited commit; ChannelGate.forward, SpatialGate.__init__/forward, BasicConv and CBAM.forward in MODELS/cbam.py | supports | Official attention-module implementation: MODELS/cbam.py. Jongchan/attention-module commit459efad0e05ee7dde50c41ca10a3d0800bc3792a. Actual PDF and static-code reading scopes are declared in the ledger. Source rendering alone does not attest inspection. |
| bottleneckattentionmodule-source-0 | https://arxiv.org/pdf/1807.06514v2; Section3 Equations2–4 and Section4.1 Combining methods, PDF pp.4–5,7; Section3, Equations1–4, PDF pp.3–5; branch fusion and placement comparisons Section4.1, PDF pp.6–8; other placements Section4.6 and conclusion, PDF pp.9–10 | supports | BAM: Bottleneck Attention Module. arXiv1807.06514v2, 18 July 2018; 14-page author PDF, metadata states accepted to BMVC 2018. Actual PDF and static-code reading scopes are declared in the ledger. Source rendering alone does not attest inspection. |
| bottleneckattentionmodule-source-1 | https://github.com/Jongchan/attention-module/blob/459efad0e05ee7dde50c41ca10a3d0800bc3792a/MODELS/bam.py; ChannelGate.__init__, SpatialGate.__init__ and BAM.forward in MODELS/bam.py | supports | Official attention-module implementation: MODELS/bam.py. Jongchan/attention-module commit459efad0e05ee7dde50c41ca10a3d0800bc3792a. Actual PDF and static-code reading scopes are declared in the ledger. Source rendering alone does not attest inspection. |

## Limits And Additional Notes

- Adversarial author self-review only; every record remains DRAFT.
- Only declared PDF pages and the two pinned author modules were inspected statically. No training, benchmark or author-code execution was performed.
- The final BAM proceedings PDF was inaccessible; the specified arXiv version was inspected. Paper/code fusion and normalization differences remain explicit. No code execution, universal efficacy or causal-interpretation guarantee is claimed.
- Three additions and a nonempty inherited/new frontier leave discovery active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T124701Z-channel-and-spatial-feature-gating
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of channel and spatial feature gating
started_at: '2026-10-11T12:43:39Z'
finished_at: '2026-10-11T12:47:01Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed all three records
    against the declared primary methods, rendered pages, two pinned author implementation
    modules, seven exact AIO nodes, three native neighbors and original finite arithmetic.
    This is not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain SE blocks, channel-first CBAM and paper-version bottleneck attention
  with explicit component, gate, source-version, acronym and mapping boundaries. No
  actionable record defect was found in this scope.
source:
  git_revision: e31cea02f2a4486b461872337e03685af1aaa9fa
  state: working_tree
  inputs:
  - path: data/aio/AdditiveAttentionLayer.yaml
    sha256: 324937d052d667b100dd912b82f777a5dbcb8cb9c78a2860dd20f0b86082b1bc
    role: context
  - path: data/aio/AttentionLayer.yaml
    sha256: ace47f724bab8a1aec9f963f7d8121f148134e5bbcce7c23a3a1f62c9c83619b
    role: context
  - path: data/aio/ConvolutionalLayer.yaml
    sha256: 3b87e9fe798141deee846b353fa6d8530c637135eeb7e9eb4fa9f6597d7a25fd
    role: context
  - path: data/aio/GlobalAveragePooling2DLayer.yaml
    sha256: 092db3c9424ae2796082e850845716356673a157d37fbdf1cf8656a957b1c110
    role: context
  - path: data/aio/GlobalMaxPooling2DLayer.yaml
    sha256: 092a7378dcab4319c82fa1f3897ea00482e1987ea878c40527e21b52aea58927
    role: context
  - path: data/aio/Layer.yaml
    sha256: 46b533d2f0afcbdeadb7c35f8c382d66e51e0f5edf90b0c3552767687d34fa87
    role: context
  - path: data/aio/SigmoidFunction.yaml
    sha256: e112ec27a5b6fc9de17cc2d3354b836968b6693c6902cf004b71f05a0aedb193
    role: context
  - path: data/curated/AttentionBasedDropoutLayer.yaml
    sha256: 10b68514c413e53862800a861b26a0909cc56fc66b1783cc6ca7e416ad2d8684
    role: context
  - path: data/curated/BottleneckAttentionModule.yaml
    sha256: 465518e5c03eba3a2922b8e5494ebfd5ad945e4dfdfb159f997dc120786500b9
    role: target
  - path: data/curated/ConvolutionalBlockAttentionModule.yaml
    sha256: ece8d0432112916c5f158b484b24e6f316a9c3edfe07233fefeae5b454a96b96
    role: target
  - path: data/curated/FlashAttention.yaml
    sha256: 227618e46e070c5d5aa6f78f8587763b3d1bc739b457adcc0621779c5b89930d
    role: context
  - path: data/curated/GradCAM.yaml
    sha256: 7a6a87057b93ca219687f6707f42ecf05ed8d597c461c6ed7e24c1086a4374e8
    role: context
  - path: data/curated/SqueezeAndExcitationBlock.yaml
    sha256: e91da402137dfbda2cc38257b36587771d8a9b924488690dfeeb5bf70625fac8
    role: target
  - path: research/discovery/20261011T124335Z-channel-and-spatial-feature-gating.json
    sha256: 176086f5cb6df9e4e5c3fcc55f1e0da347b7d7cd19cf7405e95420c8d8da345f
    role: context
  - path: research/discovery/channel-spatial-gating-boundaries.py
    sha256: 61d04c89a86e9babf634622a1c6fedad8ee4a9e0fbf1e6e7c868dbdde18957c3
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
- target_id: AIMech:SqueezeAndExcitationBlock
  path: data/curated/SqueezeAndExcitationBlock.yaml
  label: Squeeze-and-Excitation block
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SqueezeAndExcitationBlock.yaml
    role: maintained
- target_id: AIMech:ConvolutionalBlockAttentionModule
  path: data/curated/ConvolutionalBlockAttentionModule.yaml
  label: Convolutional Block Attention Module
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ConvolutionalBlockAttentionModule.yaml
    role: maintained
- target_id: AIMech:BottleneckAttentionModule
  path: data/curated/BottleneckAttentionModule.yaml
  label: Bottleneck Attention Module
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BottleneckAttentionModule.yaml
    role: maintained
scope:
  description: All fields of the three newly maintained channel/spatial attention
    components.
  selection: Exact three IDs in the discovery ledger; no sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:SqueezeAndExcitationBlock
  - AIMech:ConvolutionalBlockAttentionModule
  - AIMech:BottleneckAttentionModule
  exclusions:
  - target: Older records and unselected candidates
    reason: Neighbors were inspected for boundaries, not a complete new review of
      the earlier corpus.
  - target: Unread pages, proofs, outcomes and implementations
    reason: Only declared primary-source pages, two static implementation modules
      and finite curator calculations were inspected. No author code or model was
      executed.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:SqueezeAndExcitationBlock
  - AIMech:ConvolutionalBlockAttentionModule
  - AIMech:BottleneckAttentionModule
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 83.95s (0:01:23)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 282 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 69 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 67,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:SqueezeAndExcitationBlock
  - AIMech:ConvolutionalBlockAttentionModule
  - AIMech:BottleneckAttentionModule
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
- check_id: finite-arithmetic
  name: Finite channel and spatial gating calculations
  command: python3 research/discovery/channel-spatial-gating-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SqueezeAndExcitationBlock
  - AIMech:ConvolutionalBlockAttentionModule
  - AIMech:BottleneckAttentionModule
  exit_code: 0
  expected_exit_code: 0
  summary: '{"se": {"zero_logit_channel_gates": [0.5, 0.5, 0.5], "gate_sum": 1.5,
    "interpretation": "Independent sigmoid gates are not a normalized channel distribution."},
    "cbam_order": {"channel_then_spatial": [[0.956905095733617, 2.926733543982767],
    [1.7805489823386014, -0.9076470342685989]], "spatial_then_channel": [[0.9635442008848872,
    2.924360610762908], [1.7829960484609204, -0.9019000561462824]], "largest_absolute_difference":
    0.006639105151270197, "interpretation": "Input-dependent stages need not commute;
    immediate gate products attenuate magnitudes."}, "bam_fusion": {"channel_logit":
    2.0, "spatial_logit": -1.0, "paper_sum_gate": 0.7310585786300049, "pinned_code_product_gate":
    0.11920292202211755, "paper_residual_multiplier": 1.7310585786300048, "code_residual_multiplier":
    1.1192029220221176, "interpretation": "SUM and product fusion differ; both residual
    multipliers exceed one for finite logits."}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T124335Z-channel-and-spatial-feature-gating.json
  accessed_at: '2026-10-11T12:43:39Z'
  support: supports
  summary: Compared all 442 pinned AIO labels/scoped synonyms and 279 preceding native
    IDs/names/aliases, including candidate-internal normalized uniqueness. No identity
    match was found. Full-checkout fixed-string searches included ignored/hidden files
    and returned 6 worktree and 6 main lines; every hit was a candidate or related-variant
    lead. Seven exact AIO CLASS nodes with scoped synonyms/comments/outgoing edges
    and three native neighboring mechanisms were inspected. Absence is bounded to
    this snapshot and semantic neighborhood.
  search_scope: All 442 pinned AIO labels/scoped synonyms and 279 preceding maintained
    IDs/names/aliases; full checkouts including ignored/hidden files; candidate-internal
    normalized uniqueness.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Seven exact CLASS nodes and their scoped synonyms/outgoing edges in source_analysis.aio_mapping_inspection
  accessed_at: '2026-10-11T12:43:39Z'
  support: supports
  summary: All three specific feature-map components map broadly to Layer. Seven exact
    AIO nodes were inspected. AttentionLayer is dot-product/Luong-style; AdditiveAttentionLayer
    is Bahdanau-style, not merely summing channel/spatial maps. ConvolutionalLayer,
    global average/max pooling and SigmoidFunction denote ingredients rather than
    the composite component. Three native neighbors distinguish training-only parameter-free
    ADL, exact query/key attention computation in FlashAttention, and gradient-based
    post-hoc Grad-CAM localization. No acronym, attention wording or shared operation
    establishes identity.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T124335Z-channel-and-spatial-feature-gating.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors
  accessed_at: '2026-10-11T12:43:39Z'
  support: supports
  summary: Read the attention-based dropout layer, FlashAttention and Grad-CAM. Training-only
    stochastic spatial suppression, exact query/key attention computation and gradient-based
    localization differ from learned channel/spatial feature gates.
- evidence_id: acronym
  kind: search
  search_scope: Primary arXiv2104.07566v3 title, author metadata and abstract only;
    not a complete acronym survey or full-method assessment.
  reference: research/discovery/20261011T124335Z-channel-and-spatial-feature-gating.json
  locator: queries.acronym-check and BottleneckAttentionModule.identity_notes
  accessed_at: '2026-10-11T12:43:39Z'
  support: context_only
  summary: The primary arXiv2104.07566v3 abstract names a distinct 2021 Balanced Attention
    Mechanism for super-resolution. Only its abstract was inspected for acronym disambiguation;
    the full method remains on the frontier.
- evidence_id: finite-conventions
  kind: record_content
  reference: research/discovery/channel-spatial-gating-boundaries.py
  locator: 'calculate(): independent sigmoid gates, noncommuting channel/spatial stages,
    SUM versus product branch fusion and residual multipliers'
  accessed_at: '2026-10-11T12:43:39Z'
  snapshot_sha256: 61d04c89a86e9babf634622a1c6fedad8ee4a9e0fbf1e6e7c868dbdde18957c3
  support: supports
  summary: Original finite examples distinguish independent sigmoid gates from normalized
    distributions, demonstrate order-dependent channel/spatial gating, and compare
    SUM/product BAM fusion and residual multipliers. No author algorithm or model
    was executed.
- evidence_id: squeezeandexcitationblock-source-0
  kind: primary_source
  reference: https://openaccess.thecvf.com/content_cvpr_2018/papers/Hu_Squeeze-and-Excitation_Networks_CVPR_2018_paper.pdf
  locator: Section3, Equations2–4, PDF pp.2–3 (printed7133–7134); Figures2–3 and complexity,
    PDFp.4; Section6.4/7, PDF pp.7–8
  accessed_at: '2026-10-11T12:33:17Z'
  snapshot_sha256: 2acc7faca912aa54cb4759f933c40df02efcf77f2b3cfe2f4162e38d170f277e
  support: supports
  summary: Squeeze-and-Excitation Networks. CVPR 2018, pp.7132–7141; 10-page proceedings
    PDF. Actual PDF and static-code reading scopes are declared in the ledger. Source
    rendering alone does not attest inspection.
- evidence_id: convolutionalblockattentionmodule-source-0
  kind: primary_source
  reference: https://openaccess.thecvf.com/content_ECCV_2018/papers/Sanghyun_Woo_Convolutional_Block_Attention_ECCV_2018_paper.pdf
  locator: Section3, Equations1–3 and Figure2, PDF pp.4–6; residual placement Figure3,
    PDFp.7; arrangement discussion PDFp.9; interpretability scope Sections4.3–4.4,
    PDF pp.10–13; conclusion PDFp.14
  accessed_at: '2026-10-11T12:33:17Z'
  snapshot_sha256: 40bdff61acdd66859313712892c4481610edb3180750ce6aaec570a1d20235fb
  support: supports
  summary: 'CBAM: Convolutional Block Attention Module. ECCV 2018; 17-page CVF proceedings
    PDF. Actual PDF and static-code reading scopes are declared in the ledger. Source
    rendering alone does not attest inspection.'
- evidence_id: convolutionalblockattentionmodule-source-1
  kind: primary_source
  reference: https://github.com/Jongchan/attention-module/blob/459efad0e05ee7dde50c41ca10a3d0800bc3792a/MODELS/cbam.py
  locator: ChannelGate, ChannelPool, SpatialGate, BasicConv and CBAM classes, complete
    MODELS/cbam.py at the cited commit; ChannelGate.forward, SpatialGate.__init__/forward,
    BasicConv and CBAM.forward in MODELS/cbam.py
  accessed_at: '2026-10-11T12:35:24Z'
  snapshot_sha256: 6a2115f71541c77ab09c666e4cf32ab9928520f9c2bba9c1ceab8edc8fdd8ac5
  support: supports
  summary: 'Official attention-module implementation: MODELS/cbam.py. Jongchan/attention-module
    commit459efad0e05ee7dde50c41ca10a3d0800bc3792a. Actual PDF and static-code reading
    scopes are declared in the ledger. Source rendering alone does not attest inspection.'
- evidence_id: bottleneckattentionmodule-source-0
  kind: primary_source
  reference: https://arxiv.org/pdf/1807.06514v2
  locator: Section3 Equations2–4 and Section4.1 Combining methods, PDF pp.4–5,7; Section3,
    Equations1–4, PDF pp.3–5; branch fusion and placement comparisons Section4.1,
    PDF pp.6–8; other placements Section4.6 and conclusion, PDF pp.9–10
  accessed_at: '2026-10-11T12:33:17Z'
  snapshot_sha256: 56235ca5361284431b5b78aa03aa4ffb9035283409f8edc40d71967c4b0b5a52
  support: supports
  summary: 'BAM: Bottleneck Attention Module. arXiv1807.06514v2, 18 July 2018; 14-page
    author PDF, metadata states accepted to BMVC 2018. Actual PDF and static-code
    reading scopes are declared in the ledger. Source rendering alone does not attest
    inspection.'
- evidence_id: bottleneckattentionmodule-source-1
  kind: primary_source
  reference: https://github.com/Jongchan/attention-module/blob/459efad0e05ee7dde50c41ca10a3d0800bc3792a/MODELS/bam.py
  locator: ChannelGate.__init__, SpatialGate.__init__ and BAM.forward in MODELS/bam.py
  accessed_at: '2026-10-11T12:35:24Z'
  snapshot_sha256: e2efa83e0e084b199938097656c825734e7ab962a7ead8afe2d61099abd06227
  support: supports
  summary: 'Official attention-module implementation: MODELS/bam.py. Jongchan/attention-module
    commit459efad0e05ee7dde50c41ca10a3d0800bc3792a. Actual PDF and static-code reading
    scopes are declared in the ledger. Source rendering alone does not attest inspection.'
assessments:
- assessment_id: squeezeandexcitationblock
  area: evidence
  topic: Identity, definition, mechanism, source conventions and AIO relations
  outcome: supported
  target_ids:
  - AIMech:SqueezeAndExcitationBlock
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - squeezeandexcitationblock-source-0
  summary: This is the SE component from the 2018 paper, not a complete SENet architecture
    or its trained checkpoints. The component receives the feature tensor produced
    by a preceding transformation. Its channel weights vary with the input but are
    shared over spatial positions within each channel. SE block is the scoped alias;
    the paper title denotes networks assembled using these units. No normalized identity
    match was found across all 442 pinned AIO labels/scoped synonyms and 279 preceding
    native IDs/names/aliases. Full-checkout fixed-string searches included ignored
    and hidden files in worktree and main, returning 6 and 6 lines respectively. Every
    text hit was a prior candidate lead or a closely related variant lead. Seven exact
    AIO CLASS nodes with scoped synonyms/comments and outgoing edges and three native
    neighboring mechanisms were inspected. Absence is bounded to this snapshot and
    semantic neighborhood.
  details: 'For each channel of a spatial feature tensor, average all spatial values
    to obtain a channel descriptor. Pass that descriptor through a fully connected
    dimensionality reduction, ReLU, fully connected expansion to the original channel
    count and elementwise sigmoid. Broadcast each resulting weight across its corresponding
    spatial feature map and multiply elementwise. The reduction ratio controls the
    bottleneck capacity; the paper uses 16 in its main experiments rather than requiring
    that value for the concept. In its residual-network integration, this recalibration
    operates on the non-identity transformation before addition of the skip path.
    The module has learned parameters and remains part of the network during inference.
    Limits: The sigmoid gates are independent weights, not a softmax distribution
    or guaranteed class probabilities. For finite real logits they lie strictly between
    zero and one, so the immediate scaling cannot increase absolute input-feature
    magnitudes; emphasis is relative to other channels and the surrounding network.
    Floating-point saturation can reach numerical endpoints. Global averaging discards
    spatial arrangement in the descriptor. Channel gating therefore does not itself
    supply a location-specific attention map, although the spatial feature tensor
    is retained in the output. Reduction ratio, placement and surrounding architecture
    affect cost and behavior. Additional learned weights and operations do not imply
    negligible cost on every device. The source’s interpretation of particular channel
    activations is not a causal explanation or a universal accuracy claim. No author
    implementation or trained model was executed.'
  dimensions:
  - name: concept-kind
    value: layer
    definition: A defined learned feature-map component, distinguished from a complete
      convolutional architecture, trained checkpoint or post-hoc explanation algorithm.
    evidence_ids:
    - squeezeandexcitationblock-source-0
  - name: aio-relations
    value: 'broad_match: AIO:Layer'
    definition: The native concept is a particular learned input-to-output feature-map
      component inside a neural network. The pinned generic Layer class is broader;
      the pinned AttentionLayer specifically denotes dot-product attention and is
      not used as a generic attention parent.
    evidence_ids:
    - mapping
- assessment_id: convolutionalblockattentionmodule
  area: evidence
  topic: Identity, definition, mechanism, source conventions and AIO relations
  outcome: supported
  target_ids:
  - AIMech:ConvolutionalBlockAttentionModule
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - convolutionalblockattentionmodule-source-0
  - convolutionalblockattentionmodule-source-1
  summary: This record covers the canonical channel-first CBAM configuration from
    the 2018 paper. It is a reusable component rather than a complete CNN, detector
    or gradient-based explanation method. Spatial-first, parallel, channel-only and
    alternative pooling configurations are separately assessed variants, not silent
    replacements of this selected procedure. No normalized identity match was found
    across all 442 pinned AIO labels/scoped synonyms and 279 preceding native IDs/names/aliases.
    Full-checkout fixed-string searches included ignored and hidden files in worktree
    and main, returning 6 and 6 lines respectively. Every text hit was a prior candidate
    lead or a closely related variant lead. Seven exact AIO CLASS nodes with scoped
    synonyms/comments and outgoing edges and three native neighboring mechanisms were
    inspected. Absence is bounded to this snapshot and semantic neighborhood.
  details: 'Compute global spatial average and maximum descriptors for every channel.
    Pass both through the same two-layer bottleneck MLP, with ReLU after its reduction
    layer, sum the resulting channel logits and apply sigmoid. Broadcast the channel
    weights over space and multiply them into the input tensor. From this channel-refined
    tensor, compute average and maximum maps over the channel axis, concatenate these
    two spatial maps, apply a convolution with a 7-by-7 kernel and sigmoid, then multiply
    the spatial weights across all channels. Thus the second attention stage depends
    on the output of the first, rather than being computed in parallel from the original
    tensor. The paper’s residual example applies the component before skip addition;
    the learned component also operates during inference. The pinned author implementation
    follows channel-then-spatial gating with average/max channel descriptors sharing
    one MLP. Its spatial path uses a bias-free 7-by-7 convolution followed by batch
    normalization and sigmoid, with no intervening ReLU. Optional pooling choices
    and no_spatial are exposed as code configurations. This static inspection does
    not establish runtime compatibility or reproduction of a trained checkpoint. Limits:
    Average and maximum channel descriptors share the same MLP parameters. The sum
    occurs before sigmoid, not between independently sigmoid-normalized channel weights.
    Spatial pooling runs over channels, whereas the channel stage pools over spatial
    positions. Reversing the stages or computing both from the original input generally
    changes the transformation. The spatial kernel and reduction ratio were selected
    empirically; the pinned implementation exposes alternative pooling and a channel-only
    switch, which are not the canonical configuration asserted here. Independent sigmoid
    gates need not sum to one. Each multiplicative gate attenuates immediate feature
    magnitude; relative emphasis is not an absolute amplification guarantee. The learned
    weights add parameters and computation. The source’s Grad-CAM visualizations and
    selected-image user study do not certify causal faithfulness, calibrated object
    probabilities or universal interpretability. CBAM itself is not Grad-CAM or a
    complete object detector, and no benchmark improvement or hardware-independent
    speed claim is curated.'
  dimensions:
  - name: concept-kind
    value: layer
    definition: A defined learned feature-map component, distinguished from a complete
      convolutional architecture, trained checkpoint or post-hoc explanation algorithm.
    evidence_ids:
    - convolutionalblockattentionmodule-source-0
    - convolutionalblockattentionmodule-source-1
  - name: aio-relations
    value: 'broad_match: AIO:Layer'
    definition: The native concept is a particular learned input-to-output feature-map
      component inside a neural network. The pinned generic Layer class is broader;
      the pinned AttentionLayer specifically denotes dot-product attention and is
      not used as a generic attention parent.
    evidence_ids:
    - mapping
- assessment_id: bottleneckattentionmodule
  area: evidence
  topic: Identity, definition, mechanism, source conventions and AIO relations
  outcome: supported
  target_ids:
  - AIMech:BottleneckAttentionModule
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - bottleneckattentionmodule-source-0
  - bottleneckattentionmodule-source-1
  summary: This record denotes Park and colleagues’ 2018 bottleneck attention module,
    scoped to the summation convention of arXiv1807.06514v2. The pinned author implementation
    uses a different fusion operation, recorded explicitly below. BAM is an ambiguous
    acronym also used by the 2021 Balanced Attention Mechanism paper; only the qualified
    bottleneck alias is assigned here. The module is distinct from sequential CBAM,
    channel-only SE and a complete CNN. No normalized identity match was found across
    all 442 pinned AIO labels/scoped synonyms and 279 preceding native IDs/names/aliases.
    Full-checkout fixed-string searches included ignored and hidden files in worktree
    and main, returning 6 and 6 lines respectively. Every text hit was a prior candidate
    lead or a closely related variant lead. Seven exact AIO CLASS nodes with scoped
    synonyms/comments and outgoing edges and three native neighboring mechanisms were
    inspected. Absence is bounded to this snapshot and semantic neighborhood.
  details: 'From the same input feature tensor, form a channel branch using global
    spatial averaging and a bottleneck MLP, and a spatial branch using a 1-by-1 channel
    reduction, two dilated 3-by-3 convolutions and a 1-by-1 projection to one spatial
    map. The selected paper equations place batch normalization at the outputs of
    both branches. Broadcast the channel and spatial logits to the input tensor shape,
    sum them and apply sigmoid to obtain the attention map. Multiply that map by the
    input and add the result back to the input. The source commonly places modules
    at downsampling bottlenecks and also studies other placements; its reduction ratio
    16 and dilation 4 are experimental settings. The learned attention computation
    operates in both training and inference. The selected paper adds broadcast channel
    and spatial branch logits before sigmoid. The inspected BAM.forward instead multiplies
    those branch outputs before applying sigmoid and adding one. The code places batch
    normalization and ReLU in intermediate branch blocks rather than the terminal
    batch-normalization positions displayed in the paper equations. These are explicit
    source-version differences, not equivalent rewritings; the concept record uses
    the paper convention and does not certify the code as an exact implementation
    of it. Limits: The record distinguishes the selected paper’s SUM fusion from the
    pinned author code’s product fusion and normalization placement. These yield different
    attention maps; neither the repository README nor a shared module name proves
    that code reproduces the selected paper equations. For finite real logits the
    residual multiplier 1+sigmoid(logit) lies between one and two. The module therefore
    cannot directly attenuate the absolute magnitude of a nonzero input element; suppression
    in source prose is relative to other features or downstream computation. Floating-point
    sigmoid can reach numerical endpoints. The branch maps are constrained by their
    channel/spatial structure rather than arbitrary independent attention values at
    every tensor position. Learned attention is not automatically a calibrated explanation
    or semantic object mask. Placement and hyperparameters affect overhead and empirical
    results. The inspected standalone bam.py references gate_activation in ChannelGate
    without a parameter or binding for that name in the module. Its average-pooling
    call also assumes square spatial maps to produce a single descriptor. Static reading
    is not a successful runtime validation; no author code, model or supplementary
    benchmark was executed. The final BMVC PDF was inaccessible during this assessment.'
  dimensions:
  - name: concept-kind
    value: layer
    definition: A defined learned feature-map component, distinguished from a complete
      convolutional architecture, trained checkpoint or post-hoc explanation algorithm.
    evidence_ids:
    - bottleneckattentionmodule-source-0
    - bottleneckattentionmodule-source-1
  - name: aio-relations
    value: 'broad_match: AIO:Layer'
    definition: The native concept is a particular learned input-to-output feature-map
      component inside a neural network. The pinned generic Layer class is broader;
      the pinned AttentionLayer specifically denotes dot-product attention and is
      not used as a generic attention parent.
    evidence_ids:
    - mapping
- assessment_id: se-boundaries
  area: consistency
  topic: Global channel descriptors, independent gates and residual placement
  outcome: supported
  target_ids:
  - AIMech:SqueezeAndExcitationBlock
  evidence_ids:
  - squeezeandexcitationblock-source-0
  - finite-conventions
  - neighbors
  summary: Retain the SE block as a component.
  details: Global spatial means feed a reduction/expansion MLP with ReLU and sigmoid.
    Gate values are independent rather than softmax-normalized, are shared spatially
    and do not amplify immediate feature magnitudes. Spatial arrangement is discarded
    in the descriptor, not in the entire output feature tensor. The residual example
    gates before adding the skip. The complete SENet and empirical performance are
    different scopes.
- assessment_id: cbam-boundaries
  area: consistency
  topic: Shared MLP, pooling axes and sequential refinement
  outcome: supported
  target_ids:
  - AIMech:ConvolutionalBlockAttentionModule
  evidence_ids:
  - convolutionalblockattentionmodule-source-0
  - convolutionalblockattentionmodule-source-1
  - finite-conventions
  - neighbors
  summary: Retain canonical channel-first CBAM.
  details: The same MLP maps spatial average/max descriptors before logit addition
    and sigmoid. The spatial gate is computed from the channel-refined tensor by channel
    average/max pooling and a spatial convolution. Reversed or parallel computation
    is not equivalent. The pinned code adds spatial batch normalization and exposes
    alternative configurations; static reading does not certify execution. Grad-CAM
    pictures and a selected-image user study do not establish causal explanation.
- assessment_id: bam-boundaries
  area: consistency
  topic: Parallel branches, residual gain, acronym and source disagreement
  outcome: supported
  target_ids:
  - AIMech:BottleneckAttentionModule
  evidence_ids:
  - bottleneckattentionmodule-source-0
  - bottleneckattentionmodule-source-1
  - finite-conventions
  - neighbors
  - acronym
  summary: Retain the paper-version bottleneck attention module with qualified alias.
  details: Paper SUM fusion and pinned-code product fusion yield different gates;
    batch-normalization placement also differs. The finite residual factor exceeds
    one, so direct absolute attenuation would be false. The inspected module has an
    unbound gate_activation reference and square-spatial pooling assumption; no runtime
    validity is claimed. The 2021 Balanced Attention Mechanism is an abstract-only
    acronym-disambiguation lead, not a synonym or a newly asserted mechanism.
- assessment_id: mapping-boundaries
  area: grounding
  topic: Composite feature-map components versus specific attention operations
  outcome: supported
  target_ids:
  - AIMech:SqueezeAndExcitationBlock
  - AIMech:ConvolutionalBlockAttentionModule
  - AIMech:BottleneckAttentionModule
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain three distinct components with Layer broad matches.
  details: All three specific feature-map components map broadly to Layer. Seven exact
    AIO nodes were inspected. AttentionLayer is dot-product/Luong-style; AdditiveAttentionLayer
    is Bahdanau-style, not merely summing channel/spatial maps. ConvolutionalLayer,
    global average/max pooling and SigmoidFunction denote ingredients rather than
    the composite component. Three native neighbors distinguish training-only parameter-free
    ADL, exact query/key attention computation in FlashAttention, and gradient-based
    post-hoc Grad-CAM localization. No acronym, attention wording or shared operation
    establishes identity.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:SqueezeAndExcitationBlock
  - AIMech:ConvolutionalBlockAttentionModule
  - AIMech:BottleneckAttentionModule
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - acronym
  - finite-conventions
  - squeezeandexcitationblock-source-0
  - convolutionalblockattentionmodule-source-0
  - convolutionalblockattentionmodule-source-1
  - bottleneckattentionmodule-source-0
  - bottleneckattentionmodule-source-1
  rationale: Channel-only recalibration, sequential channel/spatial gating and parallel
    residual attention have distinct transformations. The broad word attention, shared
    sigmoid operations or similar benchmarks do not establish equivalence.
limitations:
- Adversarial author self-review only; every record remains DRAFT.
- Only declared PDF pages and the two pinned author modules were inspected statically.
  No training, benchmark or author-code execution was performed.
- The final BAM proceedings PDF was inaccessible; the specified arXiv version was
  inspected. Paper/code fusion and normalization differences remain explicit. No code
  execution, universal efficacy or causal-interpretation guarantee is claimed.
- Three additions and a nonempty inherited/new frontier leave discovery active.
tags:
- native-concepts
- channel-attention
- spatial-attention
- feature-gating
- source-conventions
- self-review
- discovery-ongoing
```
