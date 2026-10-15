# Perspective Transformer Nets and compositional spatial transformers

2026-10-15T09:56:01Z

- AIMech:PerspectiveTransformerNets
- AIMech:CompositionalSpatialTransformer
- AIMech:InverseCompositionalSpatialTransformerNetwork

Perspective Transformer Nets is retained as the original image-to-volume architecture, with a convolutional image encoder, volume decoder and supplied-camera projection component. The main paper and its correctly attributed supplement support the trilinear tent-factor sampling, max projection, silhouette and combined objective regimes, and the distinction between multiview camera-supervised training and single-image reconstruction at inference. The printed camera convention is retained as an unresolved interpretation boundary; no inverse convention is silently repaired, and silhouettes do not establish a unique three-dimensional reconstruction.

The compositional spatial transformer is the reusable retained-source and geometric-state module. It composes a predicted incremental transform with the current state in the printed order and can be used in a cascade. The inverse compositional spatial transformer network is the shared recurrent specialization, with a reused predictor and feedback through accumulated geometry. One-step and tied-cascade overlap is explicit: these are distinct scopes, not disjoint computations or aliases. An inverse increment may be absorbed into the learned predictor; no extra runtime inverse is imposed.

The affine composition partials are distinguished from the full derivative through predictor and sampler. Small direct-state partials alone do not prove long-horizon gradient stability, descent or convergence. Retaining the original image avoids replacing it with intermediate crops, but cannot restore unseen source pixels or eliminate finite-grid interpolation, boundaries or numerical error. Finite unrolling and the source’s selected alignment and classification protocols remain explicit limitations.

All three records retain their accepted DRAFT scientific payloads, with 16 source-linked claims and 19 individual limitations. PTN has a qualified related mapping to DeepConvolutionalNetwork; the reusable compositional module is related to Layer; shared IC-STN is related to RecurrentNeuralNetwork through alignment iterations, not necessarily a temporal observation sequence. These mappings assert neither equivalence nor subclass membership, and the word transformer is not treated as an attention-architecture match.

Exact acquired source versions, original fractional access times and their native whole-second projections remain bound. The CVPR PDF and metadata page-numbering contexts are distinguished; the failed supplementary access is not treated as inspected evidence. No author code, trained-model evaluation or calculator was executed for this assembly. Historical source readings and analytical witnesses retain their separate author and root scopes.

Preparation lineage preserves the PTN root reading-scope clarification and actual preview assertion failure followed by its successful corrected attempt. The STN drafts retain explicit domain and finite-grid refinements, the source-faithful L2 objective wording, and a support-only spacing refinement with exact preimages and diffs. The original disabled cohort structure is also retained; its overly restrictive empty-match guard was corrected before invocation to allow an explicitly assessed context-only SpatialTransformer match while rejecting candidate collisions. These are preparation histories, not findings against previously curated records.

Existing owners 236 and 908 were updated in place, with historical discovery source pointers retained and qualified separately from acquired evidence. All 907 other main and all 393 nested objects remain unchanged. No new frontier leaf was appended. Records remain DRAFT; no gate or formal review completion is claimed.
