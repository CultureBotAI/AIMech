# Scientific self-review of HashCRBM, CD-PercLoss and spectral hashing

- Review: 20261011T191043Z-structured-hashing
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T19:06:06Z
- Finished UTC: 2026-10-11T19:10:43Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain three DRAFT algorithms with distinct restricted-support, prediction-search and binary-code scopes. Source mathematical conventions and approximation limits are explicit. No actionable curation finding remains within the declared scope.

## Scope And Provenance

All fields of three explicitly selected algorithms: two conditional prediction/training procedures and a separately reusable retrieval component.

Selection: Three exact maintained IDs in the discovery ledger; heterogeneous explicit batch, no sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base cefab853bf8dd7787c2c1f2996cc862206eff103.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:HashCRBM | data/curated/HashCRBM.yaml | maintained | HashCRBM |
| AIMech:CDPercLoss | data/curated/CDPercLoss.yaml | maintained | CD-PercLoss |
| AIMech:SpectralHashing | data/curated/SpectralHashing.yaml | maintained | Spectral hashing |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:HashCRBM, AIMech:CDPercLoss, AIMech:SpectralHashing | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 69.85s (0:01:09)<br>Checked 442 record(s); 0 failed.<br>Checked 370 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 104 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 101,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:HashCRBM, AIMech:CDPercLoss, AIMech:SpectralHashing | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:HashCRBM, AIMech:CDPercLoss, AIMech:SpectralHashing | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:HashCRBM, AIMech:CDPercLoss, AIMech:SpectralHashing | Command exited 0 with no output. |
| Structured prediction and spectral hashing boundary calculations | passed | True | AIMech:HashCRBM, AIMech:CDPercLoss, AIMech:SpectralHashing | {"hashcrbm": {"normalized_mass": 1.0, "maximum_gradient_error": 1.5541568032517716e-11, "marginal_mode": [1, 1, 1], "marginal_mode_hamming_risk": 1.0, "support_mode_hamming_risk": 1.3333333333333333, "deduplicated_equal_energy_probability": 0.3333333333333333, "duplicate_weighted_probability": 0.5}, "cd_percloss": {"searched_prediction": [1, 0], "global_mode": [1, 1], "maximum_frozen_gradient_error": 8.739897694454157e-12, "negative_approximate_loss": -0.8320853829376804, "zero_update_despite_missed_mode": [0, 0, 0.0, 0.0, 0.0], "frozen_prediction_gradient": [1, 0, 0.14014048381513455, 0.6899744811276125, 0.0], "likelihood_gradient": [0.6820188832424265, 0.6977451355621331, 0.07969418050192956, 0.4602219748805378, 0.4343583778427072]}, "spectral_hashing": {"selected_modes": [[0.1111111111111111, 0, 1], [0.4444444444444444, 0, 2], [1.0, 0, 3], [1.0, 1, 1]], "binary_code_gram": [[4, 0], [0, 4]], "single_axis_thresholded_mode_correlation": -0.3333333333333333, "product_bit_joint_support_size": 4}} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, limitations, source provenance and AIO mapping

evidence: supported. Targets: AIMech:HashCRBM.

This is the HashCRBM method of Mnih, Larochelle and Hinton. It combines a fixed learned input hash with restricted-support conditional energy modeling; neither a generic conditional RBM nor spectral hashing alone defines the method. Retrieval supplies possible output configurations, while learned free energies determine their conditional weights. It is not ordinary k-nearest-neighbor voting or a categorical feature hashing layer. The source allows analogous restricted-support learning for other computable energy models; this record describes its named conditional-RBM construction. All 442 pinned AIO labels/scoped synonyms and 367 preceding native IDs/names/aliases were compared, with no normalized identity match. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main, returning 37 lines each. All 27 unique matched contents were read: conditional-RBM source references, contrasting method descriptions, pending leads and saved review context, rather than existing candidate identities. All 45 semantic label/synonym hits and 23 exact annotated AIO nodes were inspected, alongside corresponding generated records and three complete native neighbors. Previously read contextual files were checked for byte identity. Absence is bounded to this snapshot and inspected neighborhood.

From paired training examples (u,v), learn spectral binary codes for the inputs u and store their associated output vectors v under the code keys. For a query input, the paper retrieves its code bucket and every bucket at Hamming distance one: n+1 bucket accesses for an n-bit code. Union the returned output configurations and remove duplicates to obtain V(u). For nonempty V(u), define p(v&#124;u)=1[v in V(u)] exp(-F(v,u))/sum_(z in V(u)) exp(-F(z,u)), where F is the conditional RBM free energy after summing its hidden units. Fit the conditional energy parameters by exact gradients of this restricted-model negative log likelihood; for a training target in V(u), the gradient is grad F(v,u) minus the restricted-model expectation of grad F(z,u). The hash map and support are fixed during this differentiation. Joint-mode prediction selects the lowest-free-energy retrieved configuration. Alternatively, compute each output-bit marginal by summing the restricted probabilities and choose its mode, which minimizes additive bit-error risk and can produce a vector outside V(u). Limitations: Exact normalization and gradients refer to the deliberately restricted conditional model, not the original full-output-space CRBM. Outputs outside V(u) have zero joint probability, and a joint-mode predictor cannot return them. Coordinate-wise marginal decisions can lie outside the joint support; this is a loss-dependent prediction decision, not positive model probability for the assembled vector or evidence of factorized output variables. The retrieved set must be nonempty. The displayed formula supplies no distribution for an empty test-time set; any fallback needs an explicit additional convention. Finite training likelihood also requires the observed target in the support, as occurs when its own stored input is retrieved. Repeated output configurations across buckets must be deduplicated. Counting occurrences instead changes the base weighting and therefore the distribution and gradients. The n+1 lookup count does not bound the number of retrieved outputs or make their scoring cost constant. The input code uses a rectangular spectral-hashing approximation; retrieval can omit useful outputs, and coverage assumptions suit limited output variability. A larger Hamming ball is a separate cost/coverage choice. No universal prediction quality, convergence or author-code behavior is certified.

### Identity, definition, mechanism, limitations, source provenance and AIO mapping

evidence: supported. Targets: AIMech:CDPercLoss.

This is the CD-PercLoss algorithm defined by Mnih, Larochelle and Hinton as a practical approximation to generalized perceptron-loss training. Unlike standard data-started contrastive divergence, its search begins from the conditioning input and chooses the best free-energy state among its search steps. The training algorithm, the generalized perceptron objective and the conditional RBM architecture are distinct identities. The name does not identify the AIO single-layer linear Perceptron architecture. The paper also allows extension to other models with computable energy or free energy and Gibbs sampling; this record states its conditional-RBM procedure. All 442 pinned AIO labels/scoped synonyms and 367 preceding native IDs/names/aliases were compared, with no normalized identity match. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main, returning 37 lines each. All 27 unique matched contents were read: conditional-RBM source references, contrasting method descriptions, pending leads and saved review context, rather than existing candidate identities. All 45 semantic label/synonym hits and 23 exact annotated AIO nodes were inspected, alongside corresponding generated records and three complete native neighbors. Previously read contextual files were checked for byte identity. Absence is bounded to this snapshot and inspected neighborhood.

For training pair (u,v), initialize each visible value from the logistic input-to-visible prediction sigmoid(b_v+W_uv^T u) when those connections exist; without them, draw independent Bernoulli(0.5) visible values. Holding u fixed, perform k Gibbs updates and retain the k resulting visible configurations. Choose a configuration v_hat with the lowest conditional free energy among those candidates. Update model parameters using the derivative of F(v,u)-F(v_hat,u) with v_hat held constant, contrasting the observed and searched free-energy derivatives. This replaces the generally intractable global minimum in the generalized perceptron loss by a finite stochastic search. The source uses k mean-field updates instead of sampled Gibbs updates for test-time predictions. No partition function enters the frozen-prediction free-energy-difference gradient. Limitations: Finite search does not certify the global conditional mode. Its approximate free-energy difference can be negative, and its update can be zero when the searched prediction equals the observed target even though another output has lower free energy. Holding the prediction fixed is an explicit surrogate-update convention. It does not differentiate the sampling/selection process or produce the exact conditional log-likelihood gradient, and it does not guarantee calibrated conditional probabilities. The selected candidate is the lowest-free-energy state among k generated configurations, not necessarily the last chain state. Search initialization uses the conditioning input rather than the observed target; substituting ordinary data-started CD changes the procedure. Mean visible initialization and mean-field test updates are deterministic probability-valued computations, distinct from binary equilibrium samples or exact MAP inference. Tie-breaking and any final hard-decision convention need to be specified by an implementation; this record does not infer undocumented author-code behavior. The displayed loss has no explicit margin. The paper proposes margin-based extensions as future work; those are not silently part of CD-PercLoss. Results for the inspected denoising settings do not establish universal suitability, global convergence or equivalence to the linear perceptron.

### Identity, definition, mechanism, limitations, source provenance and AIO mapping

evidence: supported. Targets: AIMech:SpectralHashing.

This is the original Weiss–Torralba–Fergus spectral hashing algorithm. Its graph-based relaxation motivates the method, while the efficient out-of-sample algorithm uses a fitted rectangular distribution instead of eigendecomposing the complete empirical graph for every query. It differs from neural semantic hashing, random-projection locality-sensitive hashing, Laplacian Eigenmaps and the later multidimensional spectral hashing formulation. The ambiguous abbreviation SH is not claimed as an exclusive alias. All 442 pinned AIO labels/scoped synonyms and 367 preceding native IDs/names/aliases were compared, with no normalized identity match. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main, returning 37 lines each. All 27 unique matched contents were read: conditional-RBM source references, contrasting method descriptions, pending leads and saved review context, rather than existing candidate identities. All 45 semantic label/synonym hits and 23 exact annotated AIO nodes were inspected, alongside corresponding generated records and three complete native neighbors. Previously read contextual files were checked for byte identity. Absence is bounded to this snapshot and inspected neighborhood.

The motivation minimizes affinity-weighted squared distances between binary codes, subject to balanced bits and pairwise decorrelation; dropping the binary restriction yields low nonconstant graph-Laplacian modes. The practical algorithm first computes PCA coordinates and fits an interval [a_j,b_j] along each retained nondegenerate axis. Under its uniform-rectangle approximation, enumerate nonconstant single-axis modes with positive integer frequency m, represented in shifted coordinates by cos(m*pi*(x_j-a_j)/(b_j-a_j)). Rank these modes by their analytic eigenvalue order, equivalently increasing squared frequency (m/(b_j-a_j))^2 for a common positive bandwidth, and select the required number of bits. Exclude the constant mode and multidimensional outer-product modes. Threshold each selected function at zero to form binary codes. A new point is projected into the same PCA coordinates and evaluated by these selected functions; hash-table retrieval then compares codes within a chosen Hamming radius. Limitations: The uniform rectangular model is an approximation to the data distribution. The resulting code is not the exact optimum of the discrete balanced-partition problem or necessarily the thresholded eigenvectors of the finite empirical affinity graph. Equation (2) prints Y^T Y=I while retaining unscaled plus/minus-one entries. Equation (1) instead implies Y^T Y=nI for n observations; an identity normalization requires rescaled real-valued relaxed coordinates. The record preserves this distinction rather than copying the incompatible constraints. Equation (4) gives the interval width but omits the origin shift unless its x already denotes a shifted coordinate. The mechanism states that shift explicitly. Degenerate axes, zero-threshold ties and points outside fitted intervals require explicit numerical conventions. Continuous orthogonality does not guarantee empirical balance, decorrelation or independence after thresholding. Excluding outer-product modes avoids one explicit source of deterministic redundancy but does not ensure independent bits; even first and third thresholded modes on one uniform axis are correlated. The number of bits need not be smaller than the input dimension. Compact storage and approximate-neighbor retrieval are not a guarantee of dimension reduction, exact semantic similarity, universal retrieval accuracy or collision resistance for cryptography. No benchmark ranking, general spectral-convergence theorem or author-code behavior is certified.

### Restricted model versus prediction decisions

consistency: supported. Targets: AIMech:HashCRBM.

Retain HashCRBM with explicit support, retrieval and loss boundaries.

The original finite calculation normalizes only over three distinct retrieved outputs and checks every restricted-likelihood parameter gradient by central differences (maximum error 1.56e-11). For equal energies on 110, 101 and 011, the marginal-mode prediction is 111, outside the joint support, with expected bit-error count 1 rather than 4/3 for any support mode. Duplicating one output changes its probability from 1/3 to 1/2 if not removed. These checks support the distinction between restricted probability, joint-mode prediction and additive-loss marginal decisions. The record specifies nonempty support, target inclusion for finite likelihood and the difference between bucket accesses and candidate-scoring cost.

### Searched prediction versus exact mode and likelihood gradient

consistency: supported. Targets: AIMech:CDPercLoss.

Retain CD-PercLoss as a specified approximate prediction-based training procedure.

The source defines input-derived mean initialization or random initialization when input-visible links are absent, k sampled visible candidates, lowest-free-energy selection and a frozen-prediction difference. Every toy frozen-gradient component passes finite differences (maximum error 8.74e-12), while the full conditional likelihood gradient differs. A possible finite candidate pool selects 10 and misses the exact 11 mode. With target 11 the approximate loss is -0.8320853829; with target 10 the update is zero despite the missed global mode. These are witnesses for limits, not a frequency or performance claim. Mean-field test predictions and future margin extensions are separately scoped.

### Spectral relaxation versus final binary-code construction

consistency: supported. Targets: AIMech:SpectralHashing.

Retain original spectral hashing with source normalization and coordinate qualifications.

The complete source specifies PCA axes, a uniform rectangle approximation, nonconstant single-axis analytic modes, eigenvalue ordering and zero thresholding. The original examples check that mode ordering depends on frequency divided by interval width, that translating an interval requires translating its coordinate, and that an unscaled four-row balanced binary code has Gram matrix 4I rather than I. Pairwise-uncorrelated product bits are deterministically dependent, and first/third thresholded single-axis modes have correlation -1/3. Thus dropping outer-product modes does not guarantee independent or exactly decorrelated bits. The record does not promote approximate rectangle modes to exact finite-graph eigenvectors or universal optimal codes.

### Algorithm/component mapping direction

grounding: supported. Targets: AIMech:HashCRBM, AIMech:CDPercLoss, AIMech:SpectralHashing.

Retain related mappings to conditional model and PCA components.

All 45 semantic hits and 23 exact annotated AIO CLASS nodes with outgoing edges were read. Eleven corresponding generated records were previously fully read and verified byte-identical; twelve were fully read this batch. Three complete native neighbors were inspected: conditional RBM (previous full reading with byte verification), Laplacian Eigenmaps and stochastic gradient descent (read this batch). HashCRBM and CD-PercLoss relate to RestrictedBoltzmannMachine through the conditional energy model they train or use for prediction; neither algorithm is itself the AIO architecture. Spectral hashing relates to PrincipalComponentAnalysis through its defining coordinate-construction component, not equivalence or subclass identity. ArtificialNeuralNetwork and BoltzmannMachineNetwork are architecture-scoped; Perceptron is a linear single-layer binary classifier, not generalized free-energy loss. HashingLayer bins categorical integers/strings and does not learn geometric binary retrieval codes. SupervisedLearning and UnsupervisedLearning are task-scoped, and Classification, BinaryClassification, MulticlassClassification and RegressionAnalysis do not identify these algorithms. DimensionalityReduction is not universally entailed by a bit code whose length can exceed the original coordinate dimension. K-nearest-neighbor classification and regression use voting/averaging, not distinct-output retrieval followed by conditional free-energy weighting. ContrastiveLearning denotes a deep self-supervised representation architecture in this pin, not the contrastive-divergence or perceptron update. ContrastiveLearningLLM, EnergyBasedLLM and ImplicitLanguageModel require language scope. UnsupervisedClustering, MultidimensionalScaling and t-SNE do not define the rectangle-mode binary hashing procedure. Native conditional RBM supplies the full conditional model; SGD is a generic update framework; Laplacian Eigenmaps produces graph-based continuous generalized-eigenvector coordinates rather than the fitted-rectangle binary out-of-sample rule. Contextual records are not newly scientifically approved by this boundary comparison.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:HashCRBM, AIMech:CDPercLoss, AIMech:SpectralHashing. HashCRBM restricts a conditional energy model to a deduplicated input-retrieved support. CD-PercLoss contrasts observed and finitely searched predictions with a frozen-prediction derivative. Spectral hashing learns a reusable binary input code from PCA-aligned rectangle modes. Component use, shared free energies or retrieval applications do not establish equivalent identities, and algorithm-to-architecture mappings remain related.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T190547Z-structured-hashing.json | supports | All 442 pinned AIO labels/scoped synonyms and 367 preceding native IDs/names/aliases were compared, with no normalized identity match. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main, returning 37 lines each. All 27 unique matched contents were read: conditional-RBM source references, contrasting method descriptions, pending leads and saved review context, rather than existing candidate identities. All 45 semantic label/synonym hits and 23 exact annotated AIO nodes were inspected, alongside corresponding generated records and three complete native neighbors. Previously read contextual files were checked for byte identity. Absence is bounded to this snapshot and inspected neighborhood. |
| mapping | sources/aio/aio.json; Twenty-three exact CLASS nodes with full annotations and outgoing edges in source_analysis.aio_mapping_inspection; corresponding generated records | supports | All 45 semantic hits and 23 exact annotated AIO CLASS nodes with outgoing edges were read. Eleven corresponding generated records were previously fully read and verified byte-identical; twelve were fully read this batch. Three complete native neighbors were inspected: conditional RBM (previous full reading with byte verification), Laplacian Eigenmaps and stochastic gradient descent (read this batch). HashCRBM and CD-PercLoss relate to RestrictedBoltzmannMachine through the conditional energy model they train or use for prediction; neither algorithm is itself the AIO architecture. Spectral hashing relates to PrincipalComponentAnalysis through its defining coordinate-construction component, not equivalence or subclass identity. ArtificialNeuralNetwork and BoltzmannMachineNetwork are architecture-scoped; Perceptron is a linear single-layer binary classifier, not generalized free-energy loss. HashingLayer bins categorical integers/strings and does not learn geometric binary retrieval codes. SupervisedLearning and UnsupervisedLearning are task-scoped, and Classification, BinaryClassification, MulticlassClassification and RegressionAnalysis do not identify these algorithms. DimensionalityReduction is not universally entailed by a bit code whose length can exceed the original coordinate dimension. K-nearest-neighbor classification and regression use voting/averaging, not distinct-output retrieval followed by conditional free-energy weighting. ContrastiveLearning denotes a deep self-supervised representation architecture in this pin, not the contrastive-divergence or perceptron update. ContrastiveLearningLLM, EnergyBasedLLM and ImplicitLanguageModel require language scope. UnsupervisedClustering, MultidimensionalScaling and t-SNE do not define the rectangle-mode binary hashing procedure. Native conditional RBM supplies the full conditional model; SGD is a generic update framework; Laplacian Eigenmaps produces graph-based continuous generalized-eigenvector coordinates rather than the fitted-rectangle binary out-of-sample rule. Contextual records are not newly scientifically approved by this boundary comparison. |
| neighbors | research/discovery/20261011T190547Z-structured-hashing.json; source_analysis.aio_mapping_inspection.native_neighbors | supports | Three complete native records provide boundaries: generic conditional RBM (previous full reading with byte verification), Laplacian Eigenmaps and stochastic gradient descent (fully read in this batch). They distinguish the full conditional architecture, continuous graph embeddings and a generic optimization framework, without renewed scientific approval. |
| finite-conventions | research/discovery/structured-hashing-boundaries.py; Restricted-support normalization and gradients; frozen-prediction gradients and incomplete-search counterexamples; spectral mode ordering, coordinate shifts, binary normalization and dependence | supports | Original finite calculations check all restricted-support CRBM parameter gradients against central differences, and reproduce a coordinate-wise marginal prediction outside the joint support with lower additive bit-error risk. Duplicate support weighting changes an equal-energy probability from one third to one half. Frozen-prediction CD-PercLoss gradients match finite differences but differ from full conditional likelihood gradients; a finite candidate pool misses the global mode, permits negative approximate loss and can yield a zero update. Spectral examples check rectangle-mode ordering, interval-translation handling and binary Gram-matrix normalization. Product bits are pairwise uncorrelated but deterministically dependent; first and third single-axis thresholded modes have correlation minus one third. These are original curator examples, not author-code or benchmark verification. |
| hashcrbm-source-0 | https://www.cs.toronto.edu/~hinton/absps/uai_crbms.pdf; Section 6.1, Equations (14)–(16), spectral-hash retrieval and Training and Inference, PDF p.5; marginal-mode example and loss discussion, p.6 | supports | Conditional Restricted Boltzmann Machines for Structured Output Prediction. Nine-page author-hosted UAI 2011 paper, report UAI-P-2011-PG-514-522; arXiv upload 14 February 2012. No printed page numbers. Complete PDF visually read in the preceding batch and verified byte-identical; PDF pages 3–8 reread for these algorithms. Actual visual reading scopes are declared in the ledger; retrieval and conversion do not certify reading of other pages. |
| hashcrbm-source-1 | https://proceedings.neurips.cc/paper_files/paper/2008/file/d58072be2820e8682c0a27c0518e805e-Paper.pdf; Sections 2.1–2.2 and algorithm summary, printed/PDF pp.4–6; PCA/rectangle construction and zero-thresholded single-axis modes | supports | Spectral Hashing. NIPS 2008, Advances in Neural Information Processing Systems 21, publisher PDF. All eight pages visually inspected; printed page numbers equal PDF pages. The later proceedings publication is cited as 2009 in the conditional-RBM paper. Actual visual reading scopes are declared in the ledger; retrieval and conversion do not certify reading of other pages. |
| cdpercloss-source-0 | https://www.cs.toronto.edu/~hinton/absps/uai_crbms.pdf; Section 6.2, Equation (17), generalized perceptron loss and finite prediction search, PDF pp.6–7; test-time mean-field substitution, p.7; future margin discussion, Section 7, p.8 | supports | Conditional Restricted Boltzmann Machines for Structured Output Prediction. Nine-page author-hosted UAI 2011 paper, report UAI-P-2011-PG-514-522; arXiv upload 14 February 2012. No printed page numbers. Complete PDF visually read in the preceding batch and verified byte-identical; PDF pages 3–8 reread for these algorithms. Actual visual reading scopes are declared in the ledger; retrieval and conversion do not certify reading of other pages. |
| spectralhashing-source-0 | https://proceedings.neurips.cc/paper_files/paper/2008/file/d58072be2820e8682c0a27c0518e805e-Paper.pdf; Section 2 and Equations (1)–(3), printed/PDF pp.3–4; Section 2.2, Equations (4)–(5) and algorithm summary, pp.5–6; limitations, p.6 and discussion, p.7 | supports | Spectral Hashing. NIPS 2008, Advances in Neural Information Processing Systems 21, publisher PDF. All eight pages visually inspected; printed page numbers equal PDF pages. The later proceedings publication is cited as 2009 in the conditional-RBM paper. Actual visual reading scopes are declared in the ledger; retrieval and conversion do not certify reading of other pages. |

## Limits And Additional Notes

- Adversarial author self-review only; all targets remain DRAFT.
- All eight printed/PDF pages of Weiss2008 were visually read. Mnih2011 was fully read in the preceding batch and verified unchanged, with pages 3–8 visually reread here.
- Original access timestamps and hashes are preserved. Mnih2011 has no printed page numbers; Weiss2008 uses printed pages 1–8. Other source versions and code were not certified.
- Finite examples are mathematical checks and counterexamples in stated settings, not training runs, empirical comparisons or universal behavior claims.
- 201 pending inspection leads plus unresolved dispositions remain; discovery is active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T191043Z-structured-hashing
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of HashCRBM, CD-PercLoss and spectral hashing
started_at: '2026-10-11T19:06:06Z'
finished_at: '2026-10-11T19:10:43Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially checked all target fields
    against the complete spectral-hashing paper and the verified previously fully
    read conditional-RBM paper, rereading its pages 3–8. Twenty-three exact AIO CLASS
    nodes and corresponding generated records, three complete native neighbors and
    original finite calculations informed the review. Restricted support, prediction
    loss, finite search, spectral normalization, code dependence and mapping direction
    were examined. This is author self-review.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain three DRAFT algorithms with distinct restricted-support, prediction-search
  and binary-code scopes. Source mathematical conventions and approximation limits
  are explicit. No actionable curation finding remains within the declared scope.
source:
  git_revision: cefab853bf8dd7787c2c1f2996cc862206eff103
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/BinaryClassification.yaml
    sha256: 4c710e70fe7e71227f0c6aa55162a3683f04ebbe6f5a4601bd4c0398329f1481
    role: context
  - path: data/aio/BoltzmannMachineNetwork.yaml
    sha256: 1152d2d85c5c1c408a0420e13f211ed109b12fb289c706ee7449864e91aece03
    role: context
  - path: data/aio/Classification.yaml
    sha256: d97da621c5052c7ab913cda95184ea2cca274f803298fd5f2c1273a22a211219
    role: context
  - path: data/aio/ContrastiveLearning.yaml
    sha256: f8100e15621b6dd3335dc0bc8253da0197719faf6ac00f1369ebbc455a6fa645
    role: context
  - path: data/aio/ContrastiveLearningLLM.yaml
    sha256: fd0efaea0912b19d5d109e47c941ac5d983329be78bc702e3920e78387a596ee
    role: context
  - path: data/aio/DimensionalityReduction.yaml
    sha256: 99eb0714b362a98a9e704e5ef2ac370cb7a900fbe97da43de790c3ec67ed812e
    role: context
  - path: data/aio/EnergyBasedLLM.yaml
    sha256: e9e29aa4f8400ad463dfe058fade876ef36c4a2637e1ebc4b42688116896310b
    role: context
  - path: data/aio/HashingLayer.yaml
    sha256: a54a2804b0fe6dde37475887d0a8fd3ad8e1f1e335af5d0e7a7ec784e359082d
    role: context
  - path: data/aio/ImplicitLanguageModel.yaml
    sha256: 818c396b19757360dcdff6291a85d589c50638e0dc6d6bfcd96fdcb7bdf46ce9
    role: context
  - path: data/aio/KnearestNeighborClassificationAlgorithm.yaml
    sha256: c45f4eca7cc4e11444cc9be90d2622f8fd37c5296b0b01ffb7a0b7e7ac17af2a
    role: context
  - path: data/aio/KnearestNeighborRegressionAlgorithm.yaml
    sha256: d601b4b9fe609add6e8f9fad5cd43c623bbae548ec8eb36b1b75515fa58d56d2
    role: context
  - path: data/aio/LogisticRegression.yaml
    sha256: 67dd6e8ae1bb6bfc48598b41adccbf7d48d925db8b0ee3a71f59569913b8c968
    role: context
  - path: data/aio/MulticlassClassification.yaml
    sha256: dcf165047485763fd91782b9a9ba43202d58f00fd33b8545893a5eae327de171
    role: context
  - path: data/aio/MultidimensionalScaling.yaml
    sha256: b8e28ac7a39e438cd6fc6ac93d90f62628d209c84193a72fe88a5cf50d4ef3ff
    role: context
  - path: data/aio/Perceptron.yaml
    sha256: 6b1cc7cb96bfe03ed8720cca04490657976eea656fab6674d7ef685c34216915
    role: context
  - path: data/aio/PrincipalComponentAnalysis.yaml
    sha256: 7b45b5c558b7e984abb44e1610fb8d829409ae391a151ed0dc0e5cd95023e8d4
    role: context
  - path: data/aio/RegressionAnalysis.yaml
    sha256: 6f5d48096556a2ec31770aab306219e9020919940b4e80554639cc97aaa94bc6
    role: context
  - path: data/aio/RestrictedBoltzmannMachine.yaml
    sha256: 322fcb3b1f6064d944379ed79ffdcb7360fc2c3edd300c0a5a3f46be1f48df43
    role: context
  - path: data/aio/SupervisedLearning.yaml
    sha256: 472f033f91a14c8727e525ddd30f82fcaf16a2514fa8f062667fb94fc9c9b718
    role: context
  - path: data/aio/UnsupervisedClustering.yaml
    sha256: 78d3917b751b29e83802dfd2ceff6b5ee131cd64a5a3a7d40de02f5d2b9bdb1e
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/aio/tDistributedStochasticNeighborembedding.yaml
    sha256: 3ffae8e4f79f2959698d8569bf599bca13b08b0e602230e5f1ebb11ef5212822
    role: context
  - path: data/curated/CDPercLoss.yaml
    sha256: 539f7f595acaa9fcab30c0139dd9a3dc13137e365110b18b52f7812e56850f71
    role: target
  - path: data/curated/ConditionalRestrictedBoltzmannMachine.yaml
    sha256: b9e246890f7706a7e65be9f1d9611f06c462b36ab675e9441ca1f7702337aa80
    role: context
  - path: data/curated/HashCRBM.yaml
    sha256: f72661f701390a04e5dfe5e2860c371ed47d4b3338353f9d8f02e6f6b1f91dcf
    role: target
  - path: data/curated/LaplacianEigenmaps.yaml
    sha256: a9a641dc989b2031a8f3ae71a8e9c974a5fed6d31ef1b4f8bab58e05b21279c6
    role: context
  - path: data/curated/SpectralHashing.yaml
    sha256: db90a881a13cbebad6083cb7534f8f0719c4a56fd136f5f3dc17e8c1ba8833c8
    role: target
  - path: data/curated/StochasticGradientDescent.yaml
    sha256: 5c57fc809ae8667d5be8cda421cc9f0bd1f0c668f64ba3d7b23d788528b46e97
    role: context
  - path: research/discovery/20261011T190547Z-structured-hashing.json
    sha256: 2688cef0d1e3b7bd192c9274355040f352e89c45fd99d91cdee9aa60d2f97ec6
    role: context
  - path: research/discovery/structured-hashing-boundaries.py
    sha256: 649c172eeacbb95795436545f6fc1ad98f2d16ebe29f4825d5c2d594cd005d78
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
- target_id: AIMech:HashCRBM
  path: data/curated/HashCRBM.yaml
  label: HashCRBM
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HashCRBM.yaml
    role: maintained
- target_id: AIMech:CDPercLoss
  path: data/curated/CDPercLoss.yaml
  label: CD-PercLoss
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CDPercLoss.yaml
    role: maintained
- target_id: AIMech:SpectralHashing
  path: data/curated/SpectralHashing.yaml
  label: Spectral hashing
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SpectralHashing.yaml
    role: maintained
scope:
  description: 'All fields of three explicitly selected algorithms: two conditional
    prediction/training procedures and a separately reusable retrieval component.'
  selection: Three exact maintained IDs in the discovery ledger; heterogeneous explicit
    batch, no sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:HashCRBM
  - AIMech:CDPercLoss
  - AIMech:SpectralHashing
  exclusions:
  - target: Author code, empirical performance and general convergence proofs
    reason: The inspected papers and finite calculations do not certify implementations,
      benchmark rankings or every theoretical setting.
  - target: Prior records and remaining discovery leads
    reason: Prior records supply boundaries. Multidimensional/neural hashing and CD/persistent
      training require separate source and identity reviews; earlier frontier dispositions
      are retained.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:HashCRBM
  - AIMech:CDPercLoss
  - AIMech:SpectralHashing
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 69.85s (0:01:09)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 370 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 104 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 101,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:HashCRBM
  - AIMech:CDPercLoss
  - AIMech:SpectralHashing
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
  - AIMech:HashCRBM
  - AIMech:CDPercLoss
  - AIMech:SpectralHashing
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
  - AIMech:HashCRBM
  - AIMech:CDPercLoss
  - AIMech:SpectralHashing
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited 0 with no output.
- check_id: finite-arithmetic
  name: Structured prediction and spectral hashing boundary calculations
  command: python3 research/discovery/structured-hashing-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:HashCRBM
  - AIMech:CDPercLoss
  - AIMech:SpectralHashing
  exit_code: 0
  expected_exit_code: 0
  summary: '{"hashcrbm": {"normalized_mass": 1.0, "maximum_gradient_error": 1.5541568032517716e-11,
    "marginal_mode": [1, 1, 1], "marginal_mode_hamming_risk": 1.0, "support_mode_hamming_risk":
    1.3333333333333333, "deduplicated_equal_energy_probability": 0.3333333333333333,
    "duplicate_weighted_probability": 0.5}, "cd_percloss": {"searched_prediction":
    [1, 0], "global_mode": [1, 1], "maximum_frozen_gradient_error": 8.739897694454157e-12,
    "negative_approximate_loss": -0.8320853829376804, "zero_update_despite_missed_mode":
    [0, 0, 0.0, 0.0, 0.0], "frozen_prediction_gradient": [1, 0, 0.14014048381513455,
    0.6899744811276125, 0.0], "likelihood_gradient": [0.6820188832424265, 0.6977451355621331,
    0.07969418050192956, 0.4602219748805378, 0.4343583778427072]}, "spectral_hashing":
    {"selected_modes": [[0.1111111111111111, 0, 1], [0.4444444444444444, 0, 2], [1.0,
    0, 3], [1.0, 1, 1]], "binary_code_gram": [[4, 0], [0, 4]], "single_axis_thresholded_mode_correlation":
    -0.3333333333333333, "product_bit_joint_support_size": 4}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T190547Z-structured-hashing.json
  accessed_at: '2026-10-11T19:06:06Z'
  support: supports
  summary: 'All 442 pinned AIO labels/scoped synonyms and 367 preceding native IDs/names/aliases
    were compared, with no normalized identity match. Full-checkout fixed-string searches
    included ignored and hidden files in both worktree and main, returning 37 lines
    each. All 27 unique matched contents were read: conditional-RBM source references,
    contrasting method descriptions, pending leads and saved review context, rather
    than existing candidate identities. All 45 semantic label/synonym hits and 23
    exact annotated AIO nodes were inspected, alongside corresponding generated records
    and three complete native neighbors. Previously read contextual files were checked
    for byte identity. Absence is bounded to this snapshot and inspected neighborhood.'
  search_scope: 'All 442 pinned AIO labels/scoped synonyms and 367 preceding native
    IDs/names/aliases were compared, with no normalized identity match. Full-checkout
    fixed-string searches included ignored and hidden files in both worktree and main,
    returning 37 lines each. All 27 unique matched contents were read: conditional-RBM
    source references, contrasting method descriptions, pending leads and saved review
    context, rather than existing candidate identities. All 45 semantic label/synonym
    hits and 23 exact annotated AIO nodes were inspected, alongside corresponding
    generated records and three complete native neighbors. Previously read contextual
    files were checked for byte identity. Absence is bounded to this snapshot and
    inspected neighborhood.'
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Twenty-three exact CLASS nodes with full annotations and outgoing edges
    in source_analysis.aio_mapping_inspection; corresponding generated records
  accessed_at: '2026-10-11T19:06:06Z'
  support: supports
  summary: 'All 45 semantic hits and 23 exact annotated AIO CLASS nodes with outgoing
    edges were read. Eleven corresponding generated records were previously fully
    read and verified byte-identical; twelve were fully read this batch. Three complete
    native neighbors were inspected: conditional RBM (previous full reading with byte
    verification), Laplacian Eigenmaps and stochastic gradient descent (read this
    batch). HashCRBM and CD-PercLoss relate to RestrictedBoltzmannMachine through
    the conditional energy model they train or use for prediction; neither algorithm
    is itself the AIO architecture. Spectral hashing relates to PrincipalComponentAnalysis
    through its defining coordinate-construction component, not equivalence or subclass
    identity. ArtificialNeuralNetwork and BoltzmannMachineNetwork are architecture-scoped;
    Perceptron is a linear single-layer binary classifier, not generalized free-energy
    loss. HashingLayer bins categorical integers/strings and does not learn geometric
    binary retrieval codes. SupervisedLearning and UnsupervisedLearning are task-scoped,
    and Classification, BinaryClassification, MulticlassClassification and RegressionAnalysis
    do not identify these algorithms. DimensionalityReduction is not universally entailed
    by a bit code whose length can exceed the original coordinate dimension. K-nearest-neighbor
    classification and regression use voting/averaging, not distinct-output retrieval
    followed by conditional free-energy weighting. ContrastiveLearning denotes a deep
    self-supervised representation architecture in this pin, not the contrastive-divergence
    or perceptron update. ContrastiveLearningLLM, EnergyBasedLLM and ImplicitLanguageModel
    require language scope. UnsupervisedClustering, MultidimensionalScaling and t-SNE
    do not define the rectangle-mode binary hashing procedure. Native conditional
    RBM supplies the full conditional model; SGD is a generic update framework; Laplacian
    Eigenmaps produces graph-based continuous generalized-eigenvector coordinates
    rather than the fitted-rectangle binary out-of-sample rule. Contextual records
    are not newly scientifically approved by this boundary comparison.'
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T190547Z-structured-hashing.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors
  accessed_at: '2026-10-11T19:06:06Z'
  support: supports
  summary: 'Three complete native records provide boundaries: generic conditional
    RBM (previous full reading with byte verification), Laplacian Eigenmaps and stochastic
    gradient descent (fully read in this batch). They distinguish the full conditional
    architecture, continuous graph embeddings and a generic optimization framework,
    without renewed scientific approval.'
- evidence_id: finite-conventions
  kind: record_content
  reference: research/discovery/structured-hashing-boundaries.py
  locator: Restricted-support normalization and gradients; frozen-prediction gradients
    and incomplete-search counterexamples; spectral mode ordering, coordinate shifts,
    binary normalization and dependence
  accessed_at: '2026-10-11T19:06:06Z'
  snapshot_sha256: 649c172eeacbb95795436545f6fc1ad98f2d16ebe29f4825d5c2d594cd005d78
  support: supports
  summary: Original finite calculations check all restricted-support CRBM parameter
    gradients against central differences, and reproduce a coordinate-wise marginal
    prediction outside the joint support with lower additive bit-error risk. Duplicate
    support weighting changes an equal-energy probability from one third to one half.
    Frozen-prediction CD-PercLoss gradients match finite differences but differ from
    full conditional likelihood gradients; a finite candidate pool misses the global
    mode, permits negative approximate loss and can yield a zero update. Spectral
    examples check rectangle-mode ordering, interval-translation handling and binary
    Gram-matrix normalization. Product bits are pairwise uncorrelated but deterministically
    dependent; first and third single-axis thresholded modes have correlation minus
    one third. These are original curator examples, not author-code or benchmark verification.
- evidence_id: hashcrbm-source-0
  kind: primary_source
  reference: https://www.cs.toronto.edu/~hinton/absps/uai_crbms.pdf
  locator: Section 6.1, Equations (14)–(16), spectral-hash retrieval and Training
    and Inference, PDF p.5; marginal-mode example and loss discussion, p.6
  accessed_at: '2026-10-11T18:43:08Z'
  snapshot_sha256: e7811677aa0f48e97931e1a5b60497d7ec0f2a22c19ab06ce1e15b8f366df4ac
  support: supports
  summary: Conditional Restricted Boltzmann Machines for Structured Output Prediction.
    Nine-page author-hosted UAI 2011 paper, report UAI-P-2011-PG-514-522; arXiv upload
    14 February 2012. No printed page numbers. Complete PDF visually read in the preceding
    batch and verified byte-identical; PDF pages 3–8 reread for these algorithms.
    Actual visual reading scopes are declared in the ledger; retrieval and conversion
    do not certify reading of other pages.
- evidence_id: hashcrbm-source-1
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper_files/paper/2008/file/d58072be2820e8682c0a27c0518e805e-Paper.pdf
  locator: Sections 2.1–2.2 and algorithm summary, printed/PDF pp.4–6; PCA/rectangle
    construction and zero-thresholded single-axis modes
  accessed_at: '2026-10-11T18:56:10Z'
  snapshot_sha256: 3ad2470d89ee32e21a111175fa9314e058d0ae3b91541da5e7e5b9321270af9d
  support: supports
  summary: Spectral Hashing. NIPS 2008, Advances in Neural Information Processing
    Systems 21, publisher PDF. All eight pages visually inspected; printed page numbers
    equal PDF pages. The later proceedings publication is cited as 2009 in the conditional-RBM
    paper. Actual visual reading scopes are declared in the ledger; retrieval and
    conversion do not certify reading of other pages.
- evidence_id: cdpercloss-source-0
  kind: primary_source
  reference: https://www.cs.toronto.edu/~hinton/absps/uai_crbms.pdf
  locator: Section 6.2, Equation (17), generalized perceptron loss and finite prediction
    search, PDF pp.6–7; test-time mean-field substitution, p.7; future margin discussion,
    Section 7, p.8
  accessed_at: '2026-10-11T18:43:08Z'
  snapshot_sha256: e7811677aa0f48e97931e1a5b60497d7ec0f2a22c19ab06ce1e15b8f366df4ac
  support: supports
  summary: Conditional Restricted Boltzmann Machines for Structured Output Prediction.
    Nine-page author-hosted UAI 2011 paper, report UAI-P-2011-PG-514-522; arXiv upload
    14 February 2012. No printed page numbers. Complete PDF visually read in the preceding
    batch and verified byte-identical; PDF pages 3–8 reread for these algorithms.
    Actual visual reading scopes are declared in the ledger; retrieval and conversion
    do not certify reading of other pages.
- evidence_id: spectralhashing-source-0
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper_files/paper/2008/file/d58072be2820e8682c0a27c0518e805e-Paper.pdf
  locator: Section 2 and Equations (1)–(3), printed/PDF pp.3–4; Section 2.2, Equations
    (4)–(5) and algorithm summary, pp.5–6; limitations, p.6 and discussion, p.7
  accessed_at: '2026-10-11T18:56:10Z'
  snapshot_sha256: 3ad2470d89ee32e21a111175fa9314e058d0ae3b91541da5e7e5b9321270af9d
  support: supports
  summary: Spectral Hashing. NIPS 2008, Advances in Neural Information Processing
    Systems 21, publisher PDF. All eight pages visually inspected; printed page numbers
    equal PDF pages. The later proceedings publication is cited as 2009 in the conditional-RBM
    paper. Actual visual reading scopes are declared in the ledger; retrieval and
    conversion do not certify reading of other pages.
assessments:
- assessment_id: hashcrbm
  area: evidence
  topic: Identity, definition, mechanism, limitations, source provenance and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:HashCRBM
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - hashcrbm-source-0
  - hashcrbm-source-1
  summary: 'This is the HashCRBM method of Mnih, Larochelle and Hinton. It combines
    a fixed learned input hash with restricted-support conditional energy modeling;
    neither a generic conditional RBM nor spectral hashing alone defines the method.
    Retrieval supplies possible output configurations, while learned free energies
    determine their conditional weights. It is not ordinary k-nearest-neighbor voting
    or a categorical feature hashing layer. The source allows analogous restricted-support
    learning for other computable energy models; this record describes its named conditional-RBM
    construction. All 442 pinned AIO labels/scoped synonyms and 367 preceding native
    IDs/names/aliases were compared, with no normalized identity match. Full-checkout
    fixed-string searches included ignored and hidden files in both worktree and main,
    returning 37 lines each. All 27 unique matched contents were read: conditional-RBM
    source references, contrasting method descriptions, pending leads and saved review
    context, rather than existing candidate identities. All 45 semantic label/synonym
    hits and 23 exact annotated AIO nodes were inspected, alongside corresponding
    generated records and three complete native neighbors. Previously read contextual
    files were checked for byte identity. Absence is bounded to this snapshot and
    inspected neighborhood.'
  details: 'From paired training examples (u,v), learn spectral binary codes for the
    inputs u and store their associated output vectors v under the code keys. For
    a query input, the paper retrieves its code bucket and every bucket at Hamming
    distance one: n+1 bucket accesses for an n-bit code. Union the returned output
    configurations and remove duplicates to obtain V(u). For nonempty V(u), define
    p(v|u)=1[v in V(u)] exp(-F(v,u))/sum_(z in V(u)) exp(-F(z,u)), where F is the
    conditional RBM free energy after summing its hidden units. Fit the conditional
    energy parameters by exact gradients of this restricted-model negative log likelihood;
    for a training target in V(u), the gradient is grad F(v,u) minus the restricted-model
    expectation of grad F(z,u). The hash map and support are fixed during this differentiation.
    Joint-mode prediction selects the lowest-free-energy retrieved configuration.
    Alternatively, compute each output-bit marginal by summing the restricted probabilities
    and choose its mode, which minimizes additive bit-error risk and can produce a
    vector outside V(u). Limitations: Exact normalization and gradients refer to the
    deliberately restricted conditional model, not the original full-output-space
    CRBM. Outputs outside V(u) have zero joint probability, and a joint-mode predictor
    cannot return them. Coordinate-wise marginal decisions can lie outside the joint
    support; this is a loss-dependent prediction decision, not positive model probability
    for the assembled vector or evidence of factorized output variables. The retrieved
    set must be nonempty. The displayed formula supplies no distribution for an empty
    test-time set; any fallback needs an explicit additional convention. Finite training
    likelihood also requires the observed target in the support, as occurs when its
    own stored input is retrieved. Repeated output configurations across buckets must
    be deduplicated. Counting occurrences instead changes the base weighting and therefore
    the distribution and gradients. The n+1 lookup count does not bound the number
    of retrieved outputs or make their scoring cost constant. The input code uses
    a rectangular spectral-hashing approximation; retrieval can omit useful outputs,
    and coverage assumptions suit limited output variability. A larger Hamming ball
    is a separate cost/coverage choice. No universal prediction quality, convergence
    or author-code behavior is certified.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A learning or prediction algorithm, distinguished from its model,
      objective, task and component algorithms.
    evidence_ids:
    - hashcrbm-source-0
    - hashcrbm-source-1
  - name: aio-assessment
    value: related_match
    definition: 'All 45 semantic hits and 23 exact annotated AIO CLASS nodes with
      outgoing edges were read. Eleven corresponding generated records were previously
      fully read and verified byte-identical; twelve were fully read this batch. Three
      complete native neighbors were inspected: conditional RBM (previous full reading
      with byte verification), Laplacian Eigenmaps and stochastic gradient descent
      (read this batch). HashCRBM and CD-PercLoss relate to RestrictedBoltzmannMachine
      through the conditional energy model they train or use for prediction; neither
      algorithm is itself the AIO architecture. Spectral hashing relates to PrincipalComponentAnalysis
      through its defining coordinate-construction component, not equivalence or subclass
      identity. ArtificialNeuralNetwork and BoltzmannMachineNetwork are architecture-scoped;
      Perceptron is a linear single-layer binary classifier, not generalized free-energy
      loss. HashingLayer bins categorical integers/strings and does not learn geometric
      binary retrieval codes. SupervisedLearning and UnsupervisedLearning are task-scoped,
      and Classification, BinaryClassification, MulticlassClassification and RegressionAnalysis
      do not identify these algorithms. DimensionalityReduction is not universally
      entailed by a bit code whose length can exceed the original coordinate dimension.
      K-nearest-neighbor classification and regression use voting/averaging, not distinct-output
      retrieval followed by conditional free-energy weighting. ContrastiveLearning
      denotes a deep self-supervised representation architecture in this pin, not
      the contrastive-divergence or perceptron update. ContrastiveLearningLLM, EnergyBasedLLM
      and ImplicitLanguageModel require language scope. UnsupervisedClustering, MultidimensionalScaling
      and t-SNE do not define the rectangle-mode binary hashing procedure. Native
      conditional RBM supplies the full conditional model; SGD is a generic update
      framework; Laplacian Eigenmaps produces graph-based continuous generalized-eigenvector
      coordinates rather than the fitted-rectangle binary out-of-sample rule. Contextual
      records are not newly scientifically approved by this boundary comparison.'
    evidence_ids:
    - mapping
- assessment_id: cdpercloss
  area: evidence
  topic: Identity, definition, mechanism, limitations, source provenance and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:CDPercLoss
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - cdpercloss-source-0
  summary: 'This is the CD-PercLoss algorithm defined by Mnih, Larochelle and Hinton
    as a practical approximation to generalized perceptron-loss training. Unlike standard
    data-started contrastive divergence, its search begins from the conditioning input
    and chooses the best free-energy state among its search steps. The training algorithm,
    the generalized perceptron objective and the conditional RBM architecture are
    distinct identities. The name does not identify the AIO single-layer linear Perceptron
    architecture. The paper also allows extension to other models with computable
    energy or free energy and Gibbs sampling; this record states its conditional-RBM
    procedure. All 442 pinned AIO labels/scoped synonyms and 367 preceding native
    IDs/names/aliases were compared, with no normalized identity match. Full-checkout
    fixed-string searches included ignored and hidden files in both worktree and main,
    returning 37 lines each. All 27 unique matched contents were read: conditional-RBM
    source references, contrasting method descriptions, pending leads and saved review
    context, rather than existing candidate identities. All 45 semantic label/synonym
    hits and 23 exact annotated AIO nodes were inspected, alongside corresponding
    generated records and three complete native neighbors. Previously read contextual
    files were checked for byte identity. Absence is bounded to this snapshot and
    inspected neighborhood.'
  details: 'For training pair (u,v), initialize each visible value from the logistic
    input-to-visible prediction sigmoid(b_v+W_uv^T u) when those connections exist;
    without them, draw independent Bernoulli(0.5) visible values. Holding u fixed,
    perform k Gibbs updates and retain the k resulting visible configurations. Choose
    a configuration v_hat with the lowest conditional free energy among those candidates.
    Update model parameters using the derivative of F(v,u)-F(v_hat,u) with v_hat held
    constant, contrasting the observed and searched free-energy derivatives. This
    replaces the generally intractable global minimum in the generalized perceptron
    loss by a finite stochastic search. The source uses k mean-field updates instead
    of sampled Gibbs updates for test-time predictions. No partition function enters
    the frozen-prediction free-energy-difference gradient. Limitations: Finite search
    does not certify the global conditional mode. Its approximate free-energy difference
    can be negative, and its update can be zero when the searched prediction equals
    the observed target even though another output has lower free energy. Holding
    the prediction fixed is an explicit surrogate-update convention. It does not differentiate
    the sampling/selection process or produce the exact conditional log-likelihood
    gradient, and it does not guarantee calibrated conditional probabilities. The
    selected candidate is the lowest-free-energy state among k generated configurations,
    not necessarily the last chain state. Search initialization uses the conditioning
    input rather than the observed target; substituting ordinary data-started CD changes
    the procedure. Mean visible initialization and mean-field test updates are deterministic
    probability-valued computations, distinct from binary equilibrium samples or exact
    MAP inference. Tie-breaking and any final hard-decision convention need to be
    specified by an implementation; this record does not infer undocumented author-code
    behavior. The displayed loss has no explicit margin. The paper proposes margin-based
    extensions as future work; those are not silently part of CD-PercLoss. Results
    for the inspected denoising settings do not establish universal suitability, global
    convergence or equivalence to the linear perceptron.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A learning or prediction algorithm, distinguished from its model,
      objective, task and component algorithms.
    evidence_ids:
    - cdpercloss-source-0
  - name: aio-assessment
    value: related_match
    definition: 'All 45 semantic hits and 23 exact annotated AIO CLASS nodes with
      outgoing edges were read. Eleven corresponding generated records were previously
      fully read and verified byte-identical; twelve were fully read this batch. Three
      complete native neighbors were inspected: conditional RBM (previous full reading
      with byte verification), Laplacian Eigenmaps and stochastic gradient descent
      (read this batch). HashCRBM and CD-PercLoss relate to RestrictedBoltzmannMachine
      through the conditional energy model they train or use for prediction; neither
      algorithm is itself the AIO architecture. Spectral hashing relates to PrincipalComponentAnalysis
      through its defining coordinate-construction component, not equivalence or subclass
      identity. ArtificialNeuralNetwork and BoltzmannMachineNetwork are architecture-scoped;
      Perceptron is a linear single-layer binary classifier, not generalized free-energy
      loss. HashingLayer bins categorical integers/strings and does not learn geometric
      binary retrieval codes. SupervisedLearning and UnsupervisedLearning are task-scoped,
      and Classification, BinaryClassification, MulticlassClassification and RegressionAnalysis
      do not identify these algorithms. DimensionalityReduction is not universally
      entailed by a bit code whose length can exceed the original coordinate dimension.
      K-nearest-neighbor classification and regression use voting/averaging, not distinct-output
      retrieval followed by conditional free-energy weighting. ContrastiveLearning
      denotes a deep self-supervised representation architecture in this pin, not
      the contrastive-divergence or perceptron update. ContrastiveLearningLLM, EnergyBasedLLM
      and ImplicitLanguageModel require language scope. UnsupervisedClustering, MultidimensionalScaling
      and t-SNE do not define the rectangle-mode binary hashing procedure. Native
      conditional RBM supplies the full conditional model; SGD is a generic update
      framework; Laplacian Eigenmaps produces graph-based continuous generalized-eigenvector
      coordinates rather than the fitted-rectangle binary out-of-sample rule. Contextual
      records are not newly scientifically approved by this boundary comparison.'
    evidence_ids:
    - mapping
- assessment_id: spectralhashing
  area: evidence
  topic: Identity, definition, mechanism, limitations, source provenance and AIO mapping
  outcome: supported
  target_ids:
  - AIMech:SpectralHashing
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - spectralhashing-source-0
  summary: 'This is the original Weiss–Torralba–Fergus spectral hashing algorithm.
    Its graph-based relaxation motivates the method, while the efficient out-of-sample
    algorithm uses a fitted rectangular distribution instead of eigendecomposing the
    complete empirical graph for every query. It differs from neural semantic hashing,
    random-projection locality-sensitive hashing, Laplacian Eigenmaps and the later
    multidimensional spectral hashing formulation. The ambiguous abbreviation SH is
    not claimed as an exclusive alias. All 442 pinned AIO labels/scoped synonyms and
    367 preceding native IDs/names/aliases were compared, with no normalized identity
    match. Full-checkout fixed-string searches included ignored and hidden files in
    both worktree and main, returning 37 lines each. All 27 unique matched contents
    were read: conditional-RBM source references, contrasting method descriptions,
    pending leads and saved review context, rather than existing candidate identities.
    All 45 semantic label/synonym hits and 23 exact annotated AIO nodes were inspected,
    alongside corresponding generated records and three complete native neighbors.
    Previously read contextual files were checked for byte identity. Absence is bounded
    to this snapshot and inspected neighborhood.'
  details: 'The motivation minimizes affinity-weighted squared distances between binary
    codes, subject to balanced bits and pairwise decorrelation; dropping the binary
    restriction yields low nonconstant graph-Laplacian modes. The practical algorithm
    first computes PCA coordinates and fits an interval [a_j,b_j] along each retained
    nondegenerate axis. Under its uniform-rectangle approximation, enumerate nonconstant
    single-axis modes with positive integer frequency m, represented in shifted coordinates
    by cos(m*pi*(x_j-a_j)/(b_j-a_j)). Rank these modes by their analytic eigenvalue
    order, equivalently increasing squared frequency (m/(b_j-a_j))^2 for a common
    positive bandwidth, and select the required number of bits. Exclude the constant
    mode and multidimensional outer-product modes. Threshold each selected function
    at zero to form binary codes. A new point is projected into the same PCA coordinates
    and evaluated by these selected functions; hash-table retrieval then compares
    codes within a chosen Hamming radius. Limitations: The uniform rectangular model
    is an approximation to the data distribution. The resulting code is not the exact
    optimum of the discrete balanced-partition problem or necessarily the thresholded
    eigenvectors of the finite empirical affinity graph. Equation (2) prints Y^T Y=I
    while retaining unscaled plus/minus-one entries. Equation (1) instead implies
    Y^T Y=nI for n observations; an identity normalization requires rescaled real-valued
    relaxed coordinates. The record preserves this distinction rather than copying
    the incompatible constraints. Equation (4) gives the interval width but omits
    the origin shift unless its x already denotes a shifted coordinate. The mechanism
    states that shift explicitly. Degenerate axes, zero-threshold ties and points
    outside fitted intervals require explicit numerical conventions. Continuous orthogonality
    does not guarantee empirical balance, decorrelation or independence after thresholding.
    Excluding outer-product modes avoids one explicit source of deterministic redundancy
    but does not ensure independent bits; even first and third thresholded modes on
    one uniform axis are correlated. The number of bits need not be smaller than the
    input dimension. Compact storage and approximate-neighbor retrieval are not a
    guarantee of dimension reduction, exact semantic similarity, universal retrieval
    accuracy or collision resistance for cryptography. No benchmark ranking, general
    spectral-convergence theorem or author-code behavior is certified.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A learning or prediction algorithm, distinguished from its model,
      objective, task and component algorithms.
    evidence_ids:
    - spectralhashing-source-0
  - name: aio-assessment
    value: related_match
    definition: 'All 45 semantic hits and 23 exact annotated AIO CLASS nodes with
      outgoing edges were read. Eleven corresponding generated records were previously
      fully read and verified byte-identical; twelve were fully read this batch. Three
      complete native neighbors were inspected: conditional RBM (previous full reading
      with byte verification), Laplacian Eigenmaps and stochastic gradient descent
      (read this batch). HashCRBM and CD-PercLoss relate to RestrictedBoltzmannMachine
      through the conditional energy model they train or use for prediction; neither
      algorithm is itself the AIO architecture. Spectral hashing relates to PrincipalComponentAnalysis
      through its defining coordinate-construction component, not equivalence or subclass
      identity. ArtificialNeuralNetwork and BoltzmannMachineNetwork are architecture-scoped;
      Perceptron is a linear single-layer binary classifier, not generalized free-energy
      loss. HashingLayer bins categorical integers/strings and does not learn geometric
      binary retrieval codes. SupervisedLearning and UnsupervisedLearning are task-scoped,
      and Classification, BinaryClassification, MulticlassClassification and RegressionAnalysis
      do not identify these algorithms. DimensionalityReduction is not universally
      entailed by a bit code whose length can exceed the original coordinate dimension.
      K-nearest-neighbor classification and regression use voting/averaging, not distinct-output
      retrieval followed by conditional free-energy weighting. ContrastiveLearning
      denotes a deep self-supervised representation architecture in this pin, not
      the contrastive-divergence or perceptron update. ContrastiveLearningLLM, EnergyBasedLLM
      and ImplicitLanguageModel require language scope. UnsupervisedClustering, MultidimensionalScaling
      and t-SNE do not define the rectangle-mode binary hashing procedure. Native
      conditional RBM supplies the full conditional model; SGD is a generic update
      framework; Laplacian Eigenmaps produces graph-based continuous generalized-eigenvector
      coordinates rather than the fitted-rectangle binary out-of-sample rule. Contextual
      records are not newly scientifically approved by this boundary comparison.'
    evidence_ids:
    - mapping
- assessment_id: hashcrbm-boundaries
  area: consistency
  topic: Restricted model versus prediction decisions
  outcome: supported
  target_ids:
  - AIMech:HashCRBM
  evidence_ids:
  - hashcrbm-source-0
  - hashcrbm-source-1
  - finite-conventions
  summary: Retain HashCRBM with explicit support, retrieval and loss boundaries.
  details: The original finite calculation normalizes only over three distinct retrieved
    outputs and checks every restricted-likelihood parameter gradient by central differences
    (maximum error 1.56e-11). For equal energies on 110, 101 and 011, the marginal-mode
    prediction is 111, outside the joint support, with expected bit-error count 1
    rather than 4/3 for any support mode. Duplicating one output changes its probability
    from 1/3 to 1/2 if not removed. These checks support the distinction between restricted
    probability, joint-mode prediction and additive-loss marginal decisions. The record
    specifies nonempty support, target inclusion for finite likelihood and the difference
    between bucket accesses and candidate-scoring cost.
- assessment_id: cd-percloss-boundaries
  area: consistency
  topic: Searched prediction versus exact mode and likelihood gradient
  outcome: supported
  target_ids:
  - AIMech:CDPercLoss
  evidence_ids:
  - cdpercloss-source-0
  - finite-conventions
  summary: Retain CD-PercLoss as a specified approximate prediction-based training
    procedure.
  details: The source defines input-derived mean initialization or random initialization
    when input-visible links are absent, k sampled visible candidates, lowest-free-energy
    selection and a frozen-prediction difference. Every toy frozen-gradient component
    passes finite differences (maximum error 8.74e-12), while the full conditional
    likelihood gradient differs. A possible finite candidate pool selects 10 and misses
    the exact 11 mode. With target 11 the approximate loss is -0.8320853829; with
    target 10 the update is zero despite the missed global mode. These are witnesses
    for limits, not a frequency or performance claim. Mean-field test predictions
    and future margin extensions are separately scoped.
- assessment_id: spectral-hashing-boundaries
  area: consistency
  topic: Spectral relaxation versus final binary-code construction
  outcome: supported
  target_ids:
  - AIMech:SpectralHashing
  evidence_ids:
  - spectralhashing-source-0
  - finite-conventions
  summary: Retain original spectral hashing with source normalization and coordinate
    qualifications.
  details: The complete source specifies PCA axes, a uniform rectangle approximation,
    nonconstant single-axis analytic modes, eigenvalue ordering and zero thresholding.
    The original examples check that mode ordering depends on frequency divided by
    interval width, that translating an interval requires translating its coordinate,
    and that an unscaled four-row balanced binary code has Gram matrix 4I rather than
    I. Pairwise-uncorrelated product bits are deterministically dependent, and first/third
    thresholded single-axis modes have correlation -1/3. Thus dropping outer-product
    modes does not guarantee independent or exactly decorrelated bits. The record
    does not promote approximate rectangle modes to exact finite-graph eigenvectors
    or universal optimal codes.
- assessment_id: mapping-boundaries
  area: grounding
  topic: Algorithm/component mapping direction
  outcome: supported
  target_ids:
  - AIMech:HashCRBM
  - AIMech:CDPercLoss
  - AIMech:SpectralHashing
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain related mappings to conditional model and PCA components.
  details: 'All 45 semantic hits and 23 exact annotated AIO CLASS nodes with outgoing
    edges were read. Eleven corresponding generated records were previously fully
    read and verified byte-identical; twelve were fully read this batch. Three complete
    native neighbors were inspected: conditional RBM (previous full reading with byte
    verification), Laplacian Eigenmaps and stochastic gradient descent (read this
    batch). HashCRBM and CD-PercLoss relate to RestrictedBoltzmannMachine through
    the conditional energy model they train or use for prediction; neither algorithm
    is itself the AIO architecture. Spectral hashing relates to PrincipalComponentAnalysis
    through its defining coordinate-construction component, not equivalence or subclass
    identity. ArtificialNeuralNetwork and BoltzmannMachineNetwork are architecture-scoped;
    Perceptron is a linear single-layer binary classifier, not generalized free-energy
    loss. HashingLayer bins categorical integers/strings and does not learn geometric
    binary retrieval codes. SupervisedLearning and UnsupervisedLearning are task-scoped,
    and Classification, BinaryClassification, MulticlassClassification and RegressionAnalysis
    do not identify these algorithms. DimensionalityReduction is not universally entailed
    by a bit code whose length can exceed the original coordinate dimension. K-nearest-neighbor
    classification and regression use voting/averaging, not distinct-output retrieval
    followed by conditional free-energy weighting. ContrastiveLearning denotes a deep
    self-supervised representation architecture in this pin, not the contrastive-divergence
    or perceptron update. ContrastiveLearningLLM, EnergyBasedLLM and ImplicitLanguageModel
    require language scope. UnsupervisedClustering, MultidimensionalScaling and t-SNE
    do not define the rectangle-mode binary hashing procedure. Native conditional
    RBM supplies the full conditional model; SGD is a generic update framework; Laplacian
    Eigenmaps produces graph-based continuous generalized-eigenvector coordinates
    rather than the fitted-rectangle binary out-of-sample rule. Contextual records
    are not newly scientifically approved by this boundary comparison.'
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:HashCRBM
  - AIMech:CDPercLoss
  - AIMech:SpectralHashing
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - hashcrbm-source-0
  - hashcrbm-source-1
  - cdpercloss-source-0
  - spectralhashing-source-0
  rationale: HashCRBM restricts a conditional energy model to a deduplicated input-retrieved
    support. CD-PercLoss contrasts observed and finitely searched predictions with
    a frozen-prediction derivative. Spectral hashing learns a reusable binary input
    code from PCA-aligned rectangle modes. Component use, shared free energies or
    retrieval applications do not establish equivalent identities, and algorithm-to-architecture
    mappings remain related.
limitations:
- Adversarial author self-review only; all targets remain DRAFT.
- All eight printed/PDF pages of Weiss2008 were visually read. Mnih2011 was fully
  read in the preceding batch and verified unchanged, with pages 3–8 visually reread
  here.
- Original access timestamps and hashes are preserved. Mnih2011 has no printed page
  numbers; Weiss2008 uses printed pages 1–8. Other source versions and code were not
  certified.
- Finite examples are mathematical checks and counterexamples in stated settings,
  not training runs, empirical comparisons or universal behavior claims.
- 201 pending inspection leads plus unresolved dispositions remain; discovery is active.
links: []
tags:
- native-concepts
- structured-hashing
- self-review
- discovery-ongoing
```
