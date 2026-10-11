# Scientific self-review of spatial joint Markov fields and trees

- Review: 20261011T210852Z-spatial-joint-markov
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T21:04:07Z
- Finished UTC: 2026-10-11T21:08:52Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain three DRAFT spatial/tree model families. The records distinguish paired processes from clique arity, augmented from projected posterior structure, and rooted dependence trees from decision hierarchies. Source Gaussian inconsistencies, restricted experiments, ICE assumptions and bibliographic uncertainty are explicit. No actionable curation finding remains in this cohort.

## Scope And Provenance

All fields of three explicitly selected maintained spatial/tree model families.

Selection: Exact maintained IDs HiddenObservedPairMarkovRandomField, TripletMarkovField and PairwiseMarkovTree; complete selected cohort without sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base ff3401a29c36f43fbebbf0fd419c8801a799a12f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:HiddenObservedPairMarkovRandomField | data/curated/HiddenObservedPairMarkovRandomField.yaml | maintained | Hidden–observed pair Markov random field |
| AIMech:TripletMarkovField | data/curated/TripletMarkovField.yaml | maintained | Triplet Markov field |
| AIMech:PairwiseMarkovTree | data/curated/PairwiseMarkovTree.yaml | maintained | Pairwise Markov tree |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:HiddenObservedPairMarkovRandomField, AIMech:TripletMarkovField, AIMech:PairwiseMarkovTree | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 152.82s (0:02:32)<br>Checked 442 record(s); 0 failed.<br>Checked 394 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 112 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 109,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:HiddenObservedPairMarkovRandomField, AIMech:TripletMarkovField, AIMech:PairwiseMarkovTree | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:HiddenObservedPairMarkovRandomField, AIMech:TripletMarkovField, AIMech:PairwiseMarkovTree | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:HiddenObservedPairMarkovRandomField, AIMech:TripletMarkovField, AIMech:PairwiseMarkovTree | Command exited0 with no output. |
| Spatial joint Markov boundary calculations | passed | True | AIMech:HiddenObservedPairMarkovRandomField, AIMech:TripletMarkovField, AIMech:PairwiseMarkovTree | {"pair_field": {"hidden_nonlocal": [0.6872328448923964, 0.7124057350500551], "posterior_local": [0.425557483188341, 0.42555748318834097], "joint_local": [0.6855305069216744, 0.6855305069216744]}, "triplet_field": {"pair_projection_nonlocal": [0.3889760934611998, 0.425296791613543], "target_posterior_nonlocal": [0.5115736983146513, 0.5588028228248426], "augmented_posterior_local": [0.562890226047597, 0.5628902260475969]}, "pair_tree": {"hidden_sibling_dependence": [0.613873182552504, 0.7248461259956553], "evidence": 0.0541875, "posterior": {"0": [0.8, 0.19999999999999996], "1": [0.31, 0.6900000000000002], "2": [0.8600000000000001, 0.13999999999999999], "3": [0.21199999999999997, 0.7880000000000003]}}, "gaussian": {"integral_analytic": 2.0832657167256476, "integral_quadrature": 2.0832657167256476, "conditional_variances": [1.0, 0.5], "marginal_variances": [1.0869565217391306, 0.5434782608695653], "grid_edges": 42, "constant_vector_quadratic_form": -0.8000000000000007}, "scope": "Original finite witnesses and one-dimensional quadrature; not author-code reproduction, inference convergence, fitting or empirical evaluation."} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, limitations, evidence version and AIO direction

evidence: supported. Targets: AIMech:HiddenObservedPairMarkovRandomField.

This is the hidden–observed process-pair construction called pairwise Markov random fields by Pieczynski and Tebbache. Pairwise denotes Z_s=(X_s,Y_s), not a restriction to two-site clique potentials or the generic pairwise Markov property. The descriptive local label avoids those homonyms. The existing generic MarkovRandomField record does not specify this hidden–observed partition or its conditional-field construction. Classical hidden Markov fields with a Markov label prior and independent site emissions are a constrained special case; pairwise Markov chains and trees impose different graph topologies. No normalized identity match was found across all 442 pinned AIO labels and all scoped synonyms and 391 preceding native IDs, names and aliases for the three selected concepts. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main, yielding 9 and 9 matched lines; all 7 unique contents were read. Hits are prior leads and references, not records of the proposed identities. All 89 semantic label/synonym hits and 21 fully annotated exact AIO CLASS nodes with outgoing edges were read. Twenty-two contextual YAMLs were byte-verified after prior full reading and five freshly read, totaling 21 generated and six native contextual records. Short acronym identities were compared across the complete normalized inventory. Absence is bounded to the pinned source, maintained collection and inspected semantic neighborhood.

For a finite site set and specified undirected neighborhood graph, assign clique energies phi_c(x_c,y_c) and define p(x,y)=Z^(-1)*exp(-sum_c phi_c(x_c,y_c)), with a finite positive partition function. At fixed complete y, the posterior p(x&#124;y) retains clique factors on the same graph; fixing x likewise gives a local conditional observation field. Summing over one field can introduce dependencies beyond that graph, so neither p(x) nor p(y) is required to retain its Markov structure. A classical hidden Markov field p(x)*product_s b_(x_s)(y_s) is recovered by selecting label-clique and site-emission energies. This construction permits spatially correlated observation models without separately specifying a conditional likelihood whose configuration-dependent normalization could destroy locality of the label posterior. Local conditional probabilities support Gibbs sampling of hidden labels and approximation of sitewise posterior marginals; preserving the exact model factorization does not make finite sampling exact. Limitations: The definition presupposes a proper joint distribution. For the continuous Gaussian examples, each hidden configuration needs a positive-definite observation precision matrix and a finite joint partition function; positive single-site conditional variances alone do not ensure this. The source’s Gaussian displays contain normalization, completed-square and variance inconsistencies. For a local energy alpha+beta*y+delta*y^2 with delta&gt;0, integrating exp(-energy) gives sqrt(pi/delta)*exp(-alpha+beta^2/(4*delta)); its conditional mean is -beta/(2*delta) and variance is 1/(2*delta). Off-diagonal precision makes inverse diagonal precision differ from marginal variance. This record does not certify the printed Gaussian sampling implementation. The first eight-neighbor example requires particular caution: under unit diagonal precision and -0.2 on each unordered neighbor edge, a 4-by-4 open grid has a negative constant-vector quadratic form. This is a curator calculation under explicit counting and boundary conventions, not a claim about uninspected author code. Posterior Markov structure is not a guarantee of efficient exact inference on a loopy field, Gibbs mixing, parameter identifiability or a globally optimal segmentation. Per-site marginal modes and a joint maximum-probability configuration are different objectives. Section 5 leaves observation-only parameter estimation through iterative conditional estimation as future work. The synthetic texture illustrations and inconsistent sampling-count caption do not support a universal performance claim. The inspected PDF footer says Machine GRAPHICS &amp; VISION 9(4), 2000, pp.705–718 and its proof header is dated February 13, 2001; the author bibliography and later citations say issue 3. The exact inspected bytes and this discrepancy are retained.

### Identity, definition, mechanism, limitations, evidence version and AIO direction

evidence: supported. Targets: AIMech:TripletMarkovField.

The inspected construction uses finite target labels X_s and auxiliary states U_s with observed Y_s, and imposes spatial Markov structure on T_s=(X_s,U_s,Y_s). Triplet refers to three processes at each site, not three-site clique size. A pair field embeds through a constant or redundant auxiliary coordinate; general triplet fields can have projections outside that pair-field family. This is distinct from a triplet Markov chain, a neural hidden layer or an emitted-symbol memory mechanism. No normalized identity match was found across all 442 pinned AIO labels and all scoped synonyms and 391 preceding native IDs, names and aliases for the three selected concepts. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main, yielding 9 and 9 matched lines; all 7 unique contents were read. Hits are prior leads and references, not records of the proposed identities. All 89 semantic label/synonym hits and 21 fully annotated exact AIO CLASS nodes with outgoing edges were read. Twenty-two contextual YAMLs were byte-verified after prior full reading and five freshly read, totaling 21 generated and six native contextual records. Short acronym identities were compared across the complete normalized inventory. Absence is bounded to the pinned source, maintained collection and inspected semantic neighborhood.

Choose clique energies over T=(X,U,Y) on a finite neighborhood graph and normalize p(x,u,y) proportional to exp(-sum_c phi_c(x_c,u_c,y_c)). At observed y, the augmented hidden field V_s=(X_s,U_s) has a Gibbs posterior on that graph, even when the marginalized target posterior p(x&#124;y) does not. Sample or otherwise infer that augmented posterior, then sum p(X_s=x,U_s=u&#124;y) over u at fixed x to obtain the target-site posterior; its maximizer is the sitewise marginal-posterior-mode estimate. The paper illustrates a Markov auxiliary field with local conditionally independent X and Y, and experiments with a more restricted Markov V field and independent Gaussian site observations. Neither p(x,u) nor p(x,y) is required to be Markov in the general joint-triplet definition. The proposed parameter-estimation use of ICE averages a chosen complete-data estimator under the current augmented posterior, exactly when that expectation is available or approximately from posterior samples. Limitations: The augmented joint law must be normalizable and the observed evidence positive. A finite-site Gibbs factorization does not itself make marginal likelihoods, posterior probabilities or sampling computationally easy. Marginalizing U can induce additional interactions; an implementation cannot assume p(X&#124;Y) retains the original local graph. Maximizing over U before choosing X can disagree with summing over U, and sitewise marginal decoding differs from global configuration MAP. The experiments restrict the (X,U) prior to a Potts-style field and use sitewise Gaussian observations. Those restrictions are examples, not defining requirements of every triplet field. Non-Gaussian and broader graphical extensions in the conclusion are follow-up work. ICE is conditional expectation of a complete-data estimator, whereas EM optimizes an expected complete log likelihood. The interchange needed to identify them is not automatic; likelihood monotonicity and global convergence are not guaranteed merely by the ICE name. Gibbs/Metropolis feasibility does not establish exact independent finite samples. The least-squares spatial estimator used in the example is referenced rather than fully derived here. Empty empirical classes, constrained parameter values, initialization and sampling convergence need explicit handling in an implementation. The synthetic examples and one radar-image grouping compare particular fitted or chosen baselines. They do not establish the paper’s broad suggestion of universal superiority, and no numerical performance claim or author-code reproduction is curated.

### Identity, definition, mechanism, limitations, evidence version and AIO direction

evidence: supported. Targets: AIMech:PairwiseMarkovTree.

Pairwise denotes Z_s=(X_s,Y_s), not generic pairwise edge potentials. The tree is the stochastic dependence topology across sites, rather than a decision-tree classifier, hierarchical mixture-of-experts gate structure, or hidden Markov decision tree’s within-time state hierarchy. An ordinary memoryless-emission hidden Markov tree is a constrained special case. A path is a degenerate tree, but the family permits branching dependencies absent from a sequential chain. No normalized identity match was found across all 442 pinned AIO labels and all scoped synonyms and 391 preceding native IDs, names and aliases for the three selected concepts. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main, yielding 9 and 9 matched lines; all 7 unique contents were read. Hits are prior leads and references, not records of the proposed identities. All 89 semantic label/synonym hits and 21 fully annotated exact AIO CLASS nodes with outgoing edges were read. Twenty-two contextual YAMLs were byte-verified after prior full reading and five freshly read, totaling 21 generated and six native contextual records. Short acronym identities were compared across the complete normalized inventory. Absence is bounded to the pinned source, maintained collection and inspected semantic neighborhood.

On a finite fixed rooted tree with one parent for each nonroot site, specify a normalized root law p(z_r) and normalized kernels K_s(z_s&#124;z_parent(s)); their product defines the joint paired distribution. At fixed complete y, the hidden posterior factors on the same rooted tree. Set beta_s(x_s)=1 at leaves and compute each internal beta_s(x_s) as the product over children t of sum_(x_t) K_t(x_t,y_t&#124;x_s,y_s)*beta_t(x_t). The root posterior is proportional to p(x_r,y_r)*beta_r(x_r). Each child posterior transition at fixed parent is proportional to K_t*beta_t and normalized over x_t. Propagate the root marginal downward through these conditional kernels to obtain all hidden-site marginals. Classical independent-emission hidden Markov trees result from root pi(x_r)*b(y_r&#124;x_r) and child kernels A(x_t&#124;x_s)*b(y_t&#124;x_t). General joint kernels can leave hidden siblings dependent given only their hidden parent, so the hidden marginal need not itself be a Markov tree. Limitations: The definition uses a fixed finite rooted tree; it is not a graph-structure learning algorithm, a loopy-field model or a decision-making policy. Exact tree recursions require finite hidden states or separately tractable integrals. Posterior formulas require nonzero observation evidence and valid conditional support. Numerical scaling can be needed on large trees; the factorization alone does not address parameter estimation, missing observations or arbitrary topology changes. Independence of the child hidden-state transition from the parent observation is sufficient for a hidden Markov-tree marginal. Proposition 3.2 asserts necessity under the additional hypotheses that each internal node has at least two children with identical conditional laws given its paired parent; that converse is not adopted without those hypotheses. Correlated observations can coexist with a Markov hidden marginal. Non-Markov projection is permitted, not required, and memoryless site emissions are not necessary for every hidden-Markov special case. The four-page source proves structural and inference results; it does not report a comparative empirical evaluation or establish universal segmentation superiority. Later parameter-estimation and image-processing papers remain separate evidence leads.

### Paired processes, graph locality and Gaussian normalizability

consistency: supported. Targets: AIMech:HiddenObservedPairMarkovRandomField.

Retain the disambiguated hidden–observed pair-field identity.

Pairwise means hidden–observed processes at each site, not clique cardinality. The normalized joint Gibbs model has local conditional fields but can have nonlocal marginals. Exact four-cycle probabilities witness this. The source Gaussian displays are not accepted as a certified implementation: completed-square integration and conditional/marginal variance are corrected in limitations, and the negative precision quadratic form is explicitly bounded to stated counting/boundary conventions. This does not invalidate the properly normalized generic family. Section5future fitting is not reported as achieved.

### Augmented posterior versus projected label posterior

consistency: supported. Targets: AIMech:TripletMarkovField.

Retain the auxiliary-field construction and marginalization boundary.

Given observations, (X,U) is the locally factorized hidden field. Summing U can make X nonlocal; it is incorrect to transfer augmented locality to the target marginal. Exact four-cycle examples distinguish both cases. The source Potts/Gaussian experiments restrict the generic family. ICE conditional-estimator averaging differs from an EM M-step absent additional assumptions; neither finite sampling exactness nor universal segmentation superiority is asserted.

### Rooted stochastic topology and marginal converse hypotheses

consistency: supported. Targets: AIMech:PairwiseMarkovTree.

Retain pair-tree identity with exact conditional-tree recursions.

Root and parent-child kernels define a normalized paired-state Bayesian network. Upward likelihood messages and normalized downward kernels agree with enumeration on a branching example. Hidden sibling dependence given a hidden parent establishes that projection need not preserve the tree. Proposition3.2necessity requires its extra branching and identical-conditional-law hypotheses; sufficiency does not. Tree topology differs from HMDT state hierarchies and expert gating.

### Directional AIO mappings and neighboring concepts

grounding: supported. Targets: AIMech:HiddenObservedPairMarkovRandomField, AIMech:TripletMarkovField, AIMech:PairwiseMarkovTree.

Retain the three local identities with distinct mapping scope.

The two field families have related ProbabilisticGraphicalModel mappings because the pinned target is defined and parented as a machine-learning task, whereas these are model families with undirected clique factorizations. PairwiseMarkovTree has a broad BayesianNetwork mapping for its normalized directed acyclic paired-state tree; the AIO target is broader. The tree mapping does not impose that factorization on the hidden marginal. A generic chain-rule conversion of an undirected field is not used to force a BayesianNetwork match preserving its graph. CausalGraphicalModel adds unsupported causal semantics. MarkovChain denotes sequential first-order structure, not arbitrary spatial fields or a branching tree; degenerate paths do not make the entire tree family a chain. DecisionTree, HierarchicalClassification and HierarchicalClustering denote decisions or grouping procedures, not the stochastic tree. HierarchicalLanguageModel, EnergyBasedLLM and ImplicitLanguageModel require language-model scope. BoltzmannMachineNetwork and RestrictedBoltzmannMachine denote particular stochastic neural models; a generic Gibbs field is not necessarily either. HopfieldNetwork adds content-addressable recurrent memory. SpatialRegression denotes a regression analysis, not every spatial distribution. GaussianNoiseLayer and GaussianDropoutLayer are neural regularizers and ProbabilisticHiddenLayer is a component. SupervisedLearning, UnsupervisedLearning and MachineLearningTask denote learning contexts; TrainingStrategy is preprocessing-scoped. Native generic MarkovRandomField, HMM, PMC, TMC, HME and HMDT provide context for graph topology, hidden–observed partition, stochastic augmentation and hierarchical gates/state structure. Their reading does not renew their scientific approval.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:HiddenObservedPairMarkovRandomField, AIMech:TripletMarkovField, AIMech:PairwiseMarkovTree. The pair field specifies joint hidden–observed locality on an undirected spatial graph; the triplet field permits nonlocal hidden–observed projection by introducing an auxiliary field; the pair tree specifies a rooted branching factorization with exact conditional-tree messages. Subclass embeddings and shared Bayesian inference do not make their intended identities equivalent. Preserve all three local IDs and directional AIO mappings.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T210331Z-spatial-joint-markov.json | supports | No normalized identity match was found across all 442 pinned AIO labels and all scoped synonyms and 391 preceding native IDs, names and aliases for the three selected concepts. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main, yielding 9 and 9 matched lines; all 7 unique contents were read. Hits are prior leads and references, not records of the proposed identities. All 89 semantic label/synonym hits and 21 fully annotated exact AIO CLASS nodes with outgoing edges were read. Twenty-two contextual YAMLs were byte-verified after prior full reading and five freshly read, totaling 21 generated and six native contextual records. Short acronym identities were compared across the complete normalized inventory. Absence is bounded to the pinned source, maintained collection and inspected semantic neighborhood. |
| mapping | sources/aio/aio.json; Twenty-one exact CLASS nodes with full annotations/outgoing edges and89semantic label/synonym hits in source_analysis.aio_mapping_inspection | supports | The two field families have related ProbabilisticGraphicalModel mappings because the pinned target is defined and parented as a machine-learning task, whereas these are model families with undirected clique factorizations. PairwiseMarkovTree has a broad BayesianNetwork mapping for its normalized directed acyclic paired-state tree; the AIO target is broader. The tree mapping does not impose that factorization on the hidden marginal. A generic chain-rule conversion of an undirected field is not used to force a BayesianNetwork match preserving its graph. CausalGraphicalModel adds unsupported causal semantics. MarkovChain denotes sequential first-order structure, not arbitrary spatial fields or a branching tree; degenerate paths do not make the entire tree family a chain. DecisionTree, HierarchicalClassification and HierarchicalClustering denote decisions or grouping procedures, not the stochastic tree. HierarchicalLanguageModel, EnergyBasedLLM and ImplicitLanguageModel require language-model scope. BoltzmannMachineNetwork and RestrictedBoltzmannMachine denote particular stochastic neural models; a generic Gibbs field is not necessarily either. HopfieldNetwork adds content-addressable recurrent memory. SpatialRegression denotes a regression analysis, not every spatial distribution. GaussianNoiseLayer and GaussianDropoutLayer are neural regularizers and ProbabilisticHiddenLayer is a component. SupervisedLearning, UnsupervisedLearning and MachineLearningTask denote learning contexts; TrainingStrategy is preprocessing-scoped. Native generic MarkovRandomField, HMM, PMC, TMC, HME and HMDT provide context for graph topology, hidden–observed partition, stochastic augmentation and hierarchical gates/state structure. Their reading does not renew their scientific approval. |
| neighbors | research/discovery/20261011T210331Z-spatial-joint-markov.json; source_analysis.aio_mapping_inspection.native_neighbors and context_reading | supports | Six complete native contextual records read or byte-verified after prior reading: generic MRF, HMM, PMC, TMC, HME and HMDT. They distinguish generic undirected models, sequence topology, stochastic augmentation, expert gates and within-time hidden hierarchies. This is contextual reading, not renewed scientific approval. |
| finite-conventions | research/discovery/spatial-joint-markov-boundaries.py; Four-cycle pair/triplet distributions; branching tree messages; Gaussian quadrature and precision checks | supports | Original finite positive Gibbs distributions on a four-cycle show a nonlocal hidden marginal for a pair field (conditional probabilities0.6872328449 vs0.7124057351), despite a local joint and hidden-given-observed conditional. A triplet field has a nonlocal hidden–observed projection (0.3889760935 vs0.4252967916) and target posterior (0.5115736983 vs0.5588028228), while its augmented posterior remains local. A normalized branching pair tree has hidden sibling dependence (0.6138731826 vs0.7248461260), and upward/downward posterior messages agree with complete enumeration, with observation evidence0.0541875. Gaussian completed-square integration agrees with one-dimensional Simpson quadrature; a two-variable precision matrix distinguishes conditional from marginal variances. Under explicit one-unordered-edge, open-boundary conventions, unit diagonal and -0.2 eight-neighbor precision gives a4x4constant-vector quadratic form-0.8, hence is not positive definite. This is a convention-specific mathematical witness, not verification of author code, empirical performance or a general inference theorem. |
| hiddenobservedpairmarkovrandomfield-source-0 | https://www-public.imtbs-tsp.eu/~pieczyn/A22.pdf; Sections 2.1–3.2, printed pp.706–713 / PDF pp.2–9, especially Equations(13)–(22) and Remarks 3.2–3.3; Sections 4–5, pp.713–717 / PDF pp.9–13, Gaussian examples and future parameter estimation | supports | Pairwise Markov random fields and segmentation of textured images. Author-hosted 14-page proof/journal PDF. Footer: Machine GRAPHICS &amp; VISION 9(4), 2000, pp.705–718; proof header February 13, 2001. Author bibliography cites issue 3. All 14 pages visually read; printed page=PDF page+704. All target-defining pages visually read. The ledger preserves actual inspection scope and contradictory formula/bibliographic context. |
| tripletmarkovfield-source-0 | https://www-public.imtbs-tsp.eu/~pieczyn/C50.pdf; Sections 2–3.1, PDF pp.2–4, Equations(2.1)–(3.3), Example 3.1 and Remark 3.1; Sections 3.2 and 4.1–4.2, PDF pp.4–8, Equation(3.4), ICE steps and Remark 4.1; conclusion PDF p.9 | supports | Statistical image segmentation using Triplet Markov fields. Ten-page author manuscript headed SPIE International Symposium on Remote Sensing, September 22–27, Crete, Greece, 2002. The author homepage identifies this conference version. All ten pages visually read; locators use PDF pages. Secondary metadata suggests SPIE 4885:92–101 (2003) and DOI 10.1117/12.463182, but the publisher DOI endpoint was inaccessible and is not treated as independently verified metadata. All target-defining pages visually read. The ledger preserves actual inspection scope and contradictory formula/bibliographic context. |
| pairwisemarkovtree-source-0 | https://www-public.imtbs-tsp.eu/~pieczyn/A25.pdf; Section 3, printed pp.80–82 / PDF pp.2–4: Definition 3.1, Equation(3.1), Propositions 3.1–3.2, Equations(3.2)–(3.3) and final correlated-observation discussion | supports | Arbres de Markov couple. C. R. Acad. Sci. Paris, Ser. I 335(1):79–82 (2002), author-hosted journal PDF with English abstract title Pairwise Markov trees. Received November 14, 2001; accepted after revision April 29, 2002. All four pages visually read; printed page=PDF page+78. All target-defining pages visually read. The ledger preserves actual inspection scope and contradictory formula/bibliographic context. |

## Limits And Additional Notes

- Adversarial author self-review only; all records remain DRAFT.
- A22has discrepant issue metadata and inconsistent Gaussian displays; generic model identity is supported, but author sampling code and empirical examples are not certified. The precision witness depends on explicit edge-counting and boundary conventions.
- C50was read as the author-hosted2002conference manuscript. Secondary DOI/proceedings metadata was not independently verified through the inaccessible publisher endpoint and is not used as asserted persistent source metadata.
- Initial PDF DNS failures and one timeout were followed by successful authorized public-host retries; all final inspected bytes are hashed.
- Original finite probability checks and Gaussian quadrature do not establish empirical performance, general expressivity or convergence.
- 220pending leads and unresolved dispositions remain; discovery continues.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T210852Z-spatial-joint-markov
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of spatial joint Markov fields and trees
started_at: '2026-10-11T21:04:07Z'
finished_at: '2026-10-11T21:08:52Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed all fields of three
    new records against28fully visually read primary PDF pages,21annotated AIO nodes
    and6native contextual records. Original exact finite distributions, tree recursions
    and Gaussian checks challenge identity, projection, normalization and implementation
    overclaims. This is self-review, not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain three DRAFT spatial/tree model families. The records distinguish paired
  processes from clique arity, augmented from projected posterior structure, and rooted
  dependence trees from decision hierarchies. Source Gaussian inconsistencies, restricted
  experiments, ICE assumptions and bibliographic uncertainty are explicit. No actionable
  curation finding remains in this cohort.
source:
  git_revision: ff3401a29c36f43fbebbf0fd419c8801a799a12f
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/BoltzmannMachineNetwork.yaml
    sha256: 1152d2d85c5c1c408a0420e13f211ed109b12fb289c706ee7449864e91aece03
    role: context
  - path: data/aio/CausalGraphicalModel.yaml
    sha256: 868d353893701f2b8bedc9a95ef3219c0659fe230dad792c1932be078874db8b
    role: context
  - path: data/aio/DecisionTree.yaml
    sha256: 4c2a5ed08c585f8912d66e3629aaa20e93c46ab49cfb2d128001fcd019c81bfc
    role: context
  - path: data/aio/EnergyBasedLLM.yaml
    sha256: e9e29aa4f8400ad463dfe058fade876ef36c4a2637e1ebc4b42688116896310b
    role: context
  - path: data/aio/GaussianDropoutLayer.yaml
    sha256: d709e2b88e01052b2dbb1a1e3213a79b428c3c1de4acb2e55c875528250d58d2
    role: context
  - path: data/aio/GaussianNoiseLayer.yaml
    sha256: 1d6c203daf9e9a5a450a85a7d7bf6e55bb9bffbeea7ceffcc1a8aefbd9629452
    role: context
  - path: data/aio/HierarchicalClassification.yaml
    sha256: 5e1f65090a3a9e7842b57c12410a7279d02c60baef05844fa1dd73545f1cbfc7
    role: context
  - path: data/aio/HierarchicalClustering.yaml
    sha256: 144deaecd150e22de207c11a62f19db5f8409443724bd4be4b5c95c53375b258
    role: context
  - path: data/aio/HierarchicalLanguageModel.yaml
    sha256: d37f9eda55372f4e261249cdefc3b88b036e214884ef612ced2bb40076d29622
    role: context
  - path: data/aio/HopfieldNetwork.yaml
    sha256: 042815574abb3502427a76bb970ab78fd1ef684fa5f807b41c948ddb62e63822
    role: context
  - path: data/aio/ImplicitLanguageModel.yaml
    sha256: 818c396b19757360dcdff6291a85d589c50638e0dc6d6bfcd96fdcb7bdf46ce9
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/ProbabilisticHiddenLayer.yaml
    sha256: 610c29db815f7348c5bdcdc7e7460dd2dea9ea338f3727ebb1596c51b4af41da
    role: context
  - path: data/aio/RestrictedBoltzmannMachine.yaml
    sha256: 322fcb3b1f6064d944379ed79ffdcb7360fc2c3edd300c0a5a3f46be1f48df43
    role: context
  - path: data/aio/SpatialRegression.yaml
    sha256: 88d7d2d80262e45a56d05abcff674c3240be7ea2799782c64ba7ea1740250a37
    role: context
  - path: data/aio/SupervisedLearning.yaml
    sha256: 472f033f91a14c8727e525ddd30f82fcaf16a2514fa8f062667fb94fc9c9b718
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/curated/HiddenMarkovDecisionTree.yaml
    sha256: ee90a9296d1f3fa33b29c2f0160ae5b5d54787c02893fea2cbd516e6db535d18
    role: context
  - path: data/curated/HiddenMarkovModel.yaml
    sha256: 062a31bd525cb90e8077d4889c177f55cb7b29dea4e71c33be95bae9e72a5240
    role: context
  - path: data/curated/HiddenObservedPairMarkovRandomField.yaml
    sha256: 9902ffe65520a472669667888ee091407d5a43c6885011a51eb1e6a5262ec827
    role: target
  - path: data/curated/HierarchicalMixtureOfExperts.yaml
    sha256: 726b98de332b75f77dc51f3028687650e2077216f26100a16c6fc4e8328c4e18
    role: context
  - path: data/curated/MarkovRandomField.yaml
    sha256: 03b1f2a66b2183a5bf5943bee7ec0619b9e07947d6c9187263e279ee475f9149
    role: context
  - path: data/curated/PairwiseMarkovChain.yaml
    sha256: 87196baeddf19e49cb4c7e3804336980a1bbdaa222e70815040d53f1aa222a9e
    role: context
  - path: data/curated/PairwiseMarkovTree.yaml
    sha256: f7dbda0ba922be5032e7e4f310c6dbcf0e8260c534039c8d58f67e50da1acf93
    role: target
  - path: data/curated/TripletMarkovChain.yaml
    sha256: 1b73a91285250e23b2d488d78e1dd79d4451e4943b8d0efc4dca33df619995ec
    role: context
  - path: data/curated/TripletMarkovField.yaml
    sha256: bbf17102f0cee437cfead8bea4ee3c3513b5a347accfd10f44990798f4b98512
    role: target
  - path: research/discovery/20261011T210331Z-spatial-joint-markov.json
    sha256: 6e708200c0e367c41965490df7ff7db56e2dd8af478d952e823bd5c9a21e8475
    role: context
  - path: research/discovery/spatial-joint-markov-boundaries.py
    sha256: 18df4604d95aa2127c74278813ba9b99514bcc92d1871229bbc6915523b7323c
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
- target_id: AIMech:HiddenObservedPairMarkovRandomField
  path: data/curated/HiddenObservedPairMarkovRandomField.yaml
  label: Hidden–observed pair Markov random field
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HiddenObservedPairMarkovRandomField.yaml
    role: maintained
- target_id: AIMech:TripletMarkovField
  path: data/curated/TripletMarkovField.yaml
  label: Triplet Markov field
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TripletMarkovField.yaml
    role: maintained
- target_id: AIMech:PairwiseMarkovTree
  path: data/curated/PairwiseMarkovTree.yaml
  label: Pairwise Markov tree
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PairwiseMarkovTree.yaml
    role: maintained
scope:
  description: All fields of three explicitly selected maintained spatial/tree model
    families.
  selection: Exact maintained IDs HiddenObservedPairMarkovRandomField, TripletMarkovField
    and PairwiseMarkovTree; complete selected cohort without sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:HiddenObservedPairMarkovRandomField
  - AIMech:TripletMarkovField
  - AIMech:PairwiseMarkovTree
  exclusions:
  - target: Author code, empirical performance and general convergence theorems
    reason: No author implementation, data fitting or benchmark ran. Finite witnesses
      are not general proofs or checks of MCMC convergence.
  - target: Prior records and remaining frontier
    reason: Six older records provide context without renewed scientific approval.220pending
      leads plus unresolved dispositions remain.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:HiddenObservedPairMarkovRandomField
  - AIMech:TripletMarkovField
  - AIMech:PairwiseMarkovTree
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 152.82s (0:02:32)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 394 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 112 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 109,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:HiddenObservedPairMarkovRandomField
  - AIMech:TripletMarkovField
  - AIMech:PairwiseMarkovTree
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
  - AIMech:HiddenObservedPairMarkovRandomField
  - AIMech:TripletMarkovField
  - AIMech:PairwiseMarkovTree
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
  - AIMech:HiddenObservedPairMarkovRandomField
  - AIMech:TripletMarkovField
  - AIMech:PairwiseMarkovTree
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited0 with no output.
- check_id: finite-arithmetic
  name: Spatial joint Markov boundary calculations
  command: python3 research/discovery/spatial-joint-markov-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:HiddenObservedPairMarkovRandomField
  - AIMech:TripletMarkovField
  - AIMech:PairwiseMarkovTree
  exit_code: 0
  expected_exit_code: 0
  summary: '{"pair_field": {"hidden_nonlocal": [0.6872328448923964, 0.7124057350500551],
    "posterior_local": [0.425557483188341, 0.42555748318834097], "joint_local": [0.6855305069216744,
    0.6855305069216744]}, "triplet_field": {"pair_projection_nonlocal": [0.3889760934611998,
    0.425296791613543], "target_posterior_nonlocal": [0.5115736983146513, 0.5588028228248426],
    "augmented_posterior_local": [0.562890226047597, 0.5628902260475969]}, "pair_tree":
    {"hidden_sibling_dependence": [0.613873182552504, 0.7248461259956553], "evidence":
    0.0541875, "posterior": {"0": [0.8, 0.19999999999999996], "1": [0.31, 0.6900000000000002],
    "2": [0.8600000000000001, 0.13999999999999999], "3": [0.21199999999999997, 0.7880000000000003]}},
    "gaussian": {"integral_analytic": 2.0832657167256476, "integral_quadrature": 2.0832657167256476,
    "conditional_variances": [1.0, 0.5], "marginal_variances": [1.0869565217391306,
    0.5434782608695653], "grid_edges": 42, "constant_vector_quadratic_form": -0.8000000000000007},
    "scope": "Original finite witnesses and one-dimensional quadrature; not author-code
    reproduction, inference convergence, fitting or empirical evaluation."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T210331Z-spatial-joint-markov.json
  accessed_at: '2026-10-11T21:04:07Z'
  support: supports
  summary: No normalized identity match was found across all 442 pinned AIO labels
    and all scoped synonyms and 391 preceding native IDs, names and aliases for the
    three selected concepts. Full-checkout fixed-string searches included ignored
    and hidden files in both worktree and main, yielding 9 and 9 matched lines; all
    7 unique contents were read. Hits are prior leads and references, not records
    of the proposed identities. All 89 semantic label/synonym hits and 21 fully annotated
    exact AIO CLASS nodes with outgoing edges were read. Twenty-two contextual YAMLs
    were byte-verified after prior full reading and five freshly read, totaling 21
    generated and six native contextual records. Short acronym identities were compared
    across the complete normalized inventory. Absence is bounded to the pinned source,
    maintained collection and inspected semantic neighborhood.
  search_scope: No normalized identity match was found across all 442 pinned AIO labels
    and all scoped synonyms and 391 preceding native IDs, names and aliases for the
    three selected concepts. Full-checkout fixed-string searches included ignored
    and hidden files in both worktree and main, yielding 9 and 9 matched lines; all
    7 unique contents were read. Hits are prior leads and references, not records
    of the proposed identities. All 89 semantic label/synonym hits and 21 fully annotated
    exact AIO CLASS nodes with outgoing edges were read. Twenty-two contextual YAMLs
    were byte-verified after prior full reading and five freshly read, totaling 21
    generated and six native contextual records. Short acronym identities were compared
    across the complete normalized inventory. Absence is bounded to the pinned source,
    maintained collection and inspected semantic neighborhood.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Twenty-one exact CLASS nodes with full annotations/outgoing edges and89semantic
    label/synonym hits in source_analysis.aio_mapping_inspection
  accessed_at: '2026-10-11T21:04:07Z'
  support: supports
  summary: The two field families have related ProbabilisticGraphicalModel mappings
    because the pinned target is defined and parented as a machine-learning task,
    whereas these are model families with undirected clique factorizations. PairwiseMarkovTree
    has a broad BayesianNetwork mapping for its normalized directed acyclic paired-state
    tree; the AIO target is broader. The tree mapping does not impose that factorization
    on the hidden marginal. A generic chain-rule conversion of an undirected field
    is not used to force a BayesianNetwork match preserving its graph. CausalGraphicalModel
    adds unsupported causal semantics. MarkovChain denotes sequential first-order
    structure, not arbitrary spatial fields or a branching tree; degenerate paths
    do not make the entire tree family a chain. DecisionTree, HierarchicalClassification
    and HierarchicalClustering denote decisions or grouping procedures, not the stochastic
    tree. HierarchicalLanguageModel, EnergyBasedLLM and ImplicitLanguageModel require
    language-model scope. BoltzmannMachineNetwork and RestrictedBoltzmannMachine denote
    particular stochastic neural models; a generic Gibbs field is not necessarily
    either. HopfieldNetwork adds content-addressable recurrent memory. SpatialRegression
    denotes a regression analysis, not every spatial distribution. GaussianNoiseLayer
    and GaussianDropoutLayer are neural regularizers and ProbabilisticHiddenLayer
    is a component. SupervisedLearning, UnsupervisedLearning and MachineLearningTask
    denote learning contexts; TrainingStrategy is preprocessing-scoped. Native generic
    MarkovRandomField, HMM, PMC, TMC, HME and HMDT provide context for graph topology,
    hidden–observed partition, stochastic augmentation and hierarchical gates/state
    structure. Their reading does not renew their scientific approval.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T210331Z-spatial-joint-markov.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors and context_reading
  accessed_at: '2026-10-11T21:04:07Z'
  support: supports
  summary: 'Six complete native contextual records read or byte-verified after prior
    reading: generic MRF, HMM, PMC, TMC, HME and HMDT. They distinguish generic undirected
    models, sequence topology, stochastic augmentation, expert gates and within-time
    hidden hierarchies. This is contextual reading, not renewed scientific approval.'
- evidence_id: finite-conventions
  kind: record_content
  reference: research/discovery/spatial-joint-markov-boundaries.py
  locator: Four-cycle pair/triplet distributions; branching tree messages; Gaussian
    quadrature and precision checks
  accessed_at: '2026-10-11T21:04:07Z'
  snapshot_sha256: 18df4604d95aa2127c74278813ba9b99514bcc92d1871229bbc6915523b7323c
  support: supports
  summary: Original finite positive Gibbs distributions on a four-cycle show a nonlocal
    hidden marginal for a pair field (conditional probabilities0.6872328449 vs0.7124057351),
    despite a local joint and hidden-given-observed conditional. A triplet field has
    a nonlocal hidden–observed projection (0.3889760935 vs0.4252967916) and target
    posterior (0.5115736983 vs0.5588028228), while its augmented posterior remains
    local. A normalized branching pair tree has hidden sibling dependence (0.6138731826
    vs0.7248461260), and upward/downward posterior messages agree with complete enumeration,
    with observation evidence0.0541875. Gaussian completed-square integration agrees
    with one-dimensional Simpson quadrature; a two-variable precision matrix distinguishes
    conditional from marginal variances. Under explicit one-unordered-edge, open-boundary
    conventions, unit diagonal and -0.2 eight-neighbor precision gives a4x4constant-vector
    quadratic form-0.8, hence is not positive definite. This is a convention-specific
    mathematical witness, not verification of author code, empirical performance or
    a general inference theorem.
- evidence_id: hiddenobservedpairmarkovrandomfield-source-0
  kind: primary_source
  reference: https://www-public.imtbs-tsp.eu/~pieczyn/A22.pdf
  locator: Sections 2.1–3.2, printed pp.706–713 / PDF pp.2–9, especially Equations(13)–(22)
    and Remarks 3.2–3.3; Sections 4–5, pp.713–717 / PDF pp.9–13, Gaussian examples
    and future parameter estimation
  accessed_at: '2026-10-11T20:48:48Z'
  snapshot_sha256: 6a1094681753eeaa83c164690379c35a5793164d02fe6c10fd6da13d7ec8f8b8
  support: supports
  summary: 'Pairwise Markov random fields and segmentation of textured images. Author-hosted
    14-page proof/journal PDF. Footer: Machine GRAPHICS & VISION 9(4), 2000, pp.705–718;
    proof header February 13, 2001. Author bibliography cites issue 3. All 14 pages
    visually read; printed page=PDF page+704. All target-defining pages visually read.
    The ledger preserves actual inspection scope and contradictory formula/bibliographic
    context.'
- evidence_id: tripletmarkovfield-source-0
  kind: primary_source
  reference: https://www-public.imtbs-tsp.eu/~pieczyn/C50.pdf
  locator: Sections 2–3.1, PDF pp.2–4, Equations(2.1)–(3.3), Example 3.1 and Remark
    3.1; Sections 3.2 and 4.1–4.2, PDF pp.4–8, Equation(3.4), ICE steps and Remark
    4.1; conclusion PDF p.9
  accessed_at: '2026-10-11T20:53:07Z'
  snapshot_sha256: 144192c695d952e2fe6aa0c70a1565975792fa76ea9b87d3a3ae4b11bd9b5b05
  support: supports
  summary: Statistical image segmentation using Triplet Markov fields. Ten-page author
    manuscript headed SPIE International Symposium on Remote Sensing, September 22–27,
    Crete, Greece, 2002. The author homepage identifies this conference version. All
    ten pages visually read; locators use PDF pages. Secondary metadata suggests SPIE
    4885:92–101 (2003) and DOI 10.1117/12.463182, but the publisher DOI endpoint was
    inaccessible and is not treated as independently verified metadata. All target-defining
    pages visually read. The ledger preserves actual inspection scope and contradictory
    formula/bibliographic context.
- evidence_id: pairwisemarkovtree-source-0
  kind: primary_source
  reference: https://www-public.imtbs-tsp.eu/~pieczyn/A25.pdf
  locator: 'Section 3, printed pp.80–82 / PDF pp.2–4: Definition 3.1, Equation(3.1),
    Propositions 3.1–3.2, Equations(3.2)–(3.3) and final correlated-observation discussion'
  accessed_at: '2026-10-11T20:51:27Z'
  snapshot_sha256: 7834f53dcb3b3895a8fe77939467a0a16a69dd68d8a20ce775afef6824a27b1f
  support: supports
  summary: Arbres de Markov couple. C. R. Acad. Sci. Paris, Ser. I 335(1):79–82 (2002),
    author-hosted journal PDF with English abstract title Pairwise Markov trees. Received
    November 14, 2001; accepted after revision April 29, 2002. All four pages visually
    read; printed page=PDF page+78. All target-defining pages visually read. The ledger
    preserves actual inspection scope and contradictory formula/bibliographic context.
assessments:
- assessment_id: hiddenobservedpairmarkovrandomfield
  area: evidence
  topic: Identity, definition, mechanism, limitations, evidence version and AIO direction
  outcome: supported
  target_ids:
  - AIMech:HiddenObservedPairMarkovRandomField
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - hiddenobservedpairmarkovrandomfield-source-0
  summary: This is the hidden–observed process-pair construction called pairwise Markov
    random fields by Pieczynski and Tebbache. Pairwise denotes Z_s=(X_s,Y_s), not
    a restriction to two-site clique potentials or the generic pairwise Markov property.
    The descriptive local label avoids those homonyms. The existing generic MarkovRandomField
    record does not specify this hidden–observed partition or its conditional-field
    construction. Classical hidden Markov fields with a Markov label prior and independent
    site emissions are a constrained special case; pairwise Markov chains and trees
    impose different graph topologies. No normalized identity match was found across
    all 442 pinned AIO labels and all scoped synonyms and 391 preceding native IDs,
    names and aliases for the three selected concepts. Full-checkout fixed-string
    searches included ignored and hidden files in both worktree and main, yielding
    9 and 9 matched lines; all 7 unique contents were read. Hits are prior leads and
    references, not records of the proposed identities. All 89 semantic label/synonym
    hits and 21 fully annotated exact AIO CLASS nodes with outgoing edges were read.
    Twenty-two contextual YAMLs were byte-verified after prior full reading and five
    freshly read, totaling 21 generated and six native contextual records. Short acronym
    identities were compared across the complete normalized inventory. Absence is
    bounded to the pinned source, maintained collection and inspected semantic neighborhood.
  details: 'For a finite site set and specified undirected neighborhood graph, assign
    clique energies phi_c(x_c,y_c) and define p(x,y)=Z^(-1)*exp(-sum_c phi_c(x_c,y_c)),
    with a finite positive partition function. At fixed complete y, the posterior
    p(x|y) retains clique factors on the same graph; fixing x likewise gives a local
    conditional observation field. Summing over one field can introduce dependencies
    beyond that graph, so neither p(x) nor p(y) is required to retain its Markov structure.
    A classical hidden Markov field p(x)*product_s b_(x_s)(y_s) is recovered by selecting
    label-clique and site-emission energies. This construction permits spatially correlated
    observation models without separately specifying a conditional likelihood whose
    configuration-dependent normalization could destroy locality of the label posterior.
    Local conditional probabilities support Gibbs sampling of hidden labels and approximation
    of sitewise posterior marginals; preserving the exact model factorization does
    not make finite sampling exact. Limitations: The definition presupposes a proper
    joint distribution. For the continuous Gaussian examples, each hidden configuration
    needs a positive-definite observation precision matrix and a finite joint partition
    function; positive single-site conditional variances alone do not ensure this.
    The source’s Gaussian displays contain normalization, completed-square and variance
    inconsistencies. For a local energy alpha+beta*y+delta*y^2 with delta>0, integrating
    exp(-energy) gives sqrt(pi/delta)*exp(-alpha+beta^2/(4*delta)); its conditional
    mean is -beta/(2*delta) and variance is 1/(2*delta). Off-diagonal precision makes
    inverse diagonal precision differ from marginal variance. This record does not
    certify the printed Gaussian sampling implementation. The first eight-neighbor
    example requires particular caution: under unit diagonal precision and -0.2 on
    each unordered neighbor edge, a 4-by-4 open grid has a negative constant-vector
    quadratic form. This is a curator calculation under explicit counting and boundary
    conventions, not a claim about uninspected author code. Posterior Markov structure
    is not a guarantee of efficient exact inference on a loopy field, Gibbs mixing,
    parameter identifiability or a globally optimal segmentation. Per-site marginal
    modes and a joint maximum-probability configuration are different objectives.
    Section 5 leaves observation-only parameter estimation through iterative conditional
    estimation as future work. The synthetic texture illustrations and inconsistent
    sampling-count caption do not support a universal performance claim. The inspected
    PDF footer says Machine GRAPHICS & VISION 9(4), 2000, pp.705–718 and its proof
    header is dated February 13, 2001; the author bibliography and later citations
    say issue 3. The exact inspected bytes and this discrepancy are retained.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: A probabilistic spatial-field or rooted-tree model family, distinct
      from an estimator or decoding procedure.
    evidence_ids:
    - hiddenobservedpairmarkovrandomfield-source-0
  - name: aio-assessment
    value: related_match
    definition: The two field families have related ProbabilisticGraphicalModel mappings
      because the pinned target is defined and parented as a machine-learning task,
      whereas these are model families with undirected clique factorizations. PairwiseMarkovTree
      has a broad BayesianNetwork mapping for its normalized directed acyclic paired-state
      tree; the AIO target is broader. The tree mapping does not impose that factorization
      on the hidden marginal. A generic chain-rule conversion of an undirected field
      is not used to force a BayesianNetwork match preserving its graph. CausalGraphicalModel
      adds unsupported causal semantics. MarkovChain denotes sequential first-order
      structure, not arbitrary spatial fields or a branching tree; degenerate paths
      do not make the entire tree family a chain. DecisionTree, HierarchicalClassification
      and HierarchicalClustering denote decisions or grouping procedures, not the
      stochastic tree. HierarchicalLanguageModel, EnergyBasedLLM and ImplicitLanguageModel
      require language-model scope. BoltzmannMachineNetwork and RestrictedBoltzmannMachine
      denote particular stochastic neural models; a generic Gibbs field is not necessarily
      either. HopfieldNetwork adds content-addressable recurrent memory. SpatialRegression
      denotes a regression analysis, not every spatial distribution. GaussianNoiseLayer
      and GaussianDropoutLayer are neural regularizers and ProbabilisticHiddenLayer
      is a component. SupervisedLearning, UnsupervisedLearning and MachineLearningTask
      denote learning contexts; TrainingStrategy is preprocessing-scoped. Native generic
      MarkovRandomField, HMM, PMC, TMC, HME and HMDT provide context for graph topology,
      hidden–observed partition, stochastic augmentation and hierarchical gates/state
      structure. Their reading does not renew their scientific approval.
    evidence_ids:
    - mapping
- assessment_id: tripletmarkovfield
  area: evidence
  topic: Identity, definition, mechanism, limitations, evidence version and AIO direction
  outcome: supported
  target_ids:
  - AIMech:TripletMarkovField
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - tripletmarkovfield-source-0
  summary: The inspected construction uses finite target labels X_s and auxiliary
    states U_s with observed Y_s, and imposes spatial Markov structure on T_s=(X_s,U_s,Y_s).
    Triplet refers to three processes at each site, not three-site clique size. A
    pair field embeds through a constant or redundant auxiliary coordinate; general
    triplet fields can have projections outside that pair-field family. This is distinct
    from a triplet Markov chain, a neural hidden layer or an emitted-symbol memory
    mechanism. No normalized identity match was found across all 442 pinned AIO labels
    and all scoped synonyms and 391 preceding native IDs, names and aliases for the
    three selected concepts. Full-checkout fixed-string searches included ignored
    and hidden files in both worktree and main, yielding 9 and 9 matched lines; all
    7 unique contents were read. Hits are prior leads and references, not records
    of the proposed identities. All 89 semantic label/synonym hits and 21 fully annotated
    exact AIO CLASS nodes with outgoing edges were read. Twenty-two contextual YAMLs
    were byte-verified after prior full reading and five freshly read, totaling 21
    generated and six native contextual records. Short acronym identities were compared
    across the complete normalized inventory. Absence is bounded to the pinned source,
    maintained collection and inspected semantic neighborhood.
  details: 'Choose clique energies over T=(X,U,Y) on a finite neighborhood graph and
    normalize p(x,u,y) proportional to exp(-sum_c phi_c(x_c,u_c,y_c)). At observed
    y, the augmented hidden field V_s=(X_s,U_s) has a Gibbs posterior on that graph,
    even when the marginalized target posterior p(x|y) does not. Sample or otherwise
    infer that augmented posterior, then sum p(X_s=x,U_s=u|y) over u at fixed x to
    obtain the target-site posterior; its maximizer is the sitewise marginal-posterior-mode
    estimate. The paper illustrates a Markov auxiliary field with local conditionally
    independent X and Y, and experiments with a more restricted Markov V field and
    independent Gaussian site observations. Neither p(x,u) nor p(x,y) is required
    to be Markov in the general joint-triplet definition. The proposed parameter-estimation
    use of ICE averages a chosen complete-data estimator under the current augmented
    posterior, exactly when that expectation is available or approximately from posterior
    samples. Limitations: The augmented joint law must be normalizable and the observed
    evidence positive. A finite-site Gibbs factorization does not itself make marginal
    likelihoods, posterior probabilities or sampling computationally easy. Marginalizing
    U can induce additional interactions; an implementation cannot assume p(X|Y) retains
    the original local graph. Maximizing over U before choosing X can disagree with
    summing over U, and sitewise marginal decoding differs from global configuration
    MAP. The experiments restrict the (X,U) prior to a Potts-style field and use sitewise
    Gaussian observations. Those restrictions are examples, not defining requirements
    of every triplet field. Non-Gaussian and broader graphical extensions in the conclusion
    are follow-up work. ICE is conditional expectation of a complete-data estimator,
    whereas EM optimizes an expected complete log likelihood. The interchange needed
    to identify them is not automatic; likelihood monotonicity and global convergence
    are not guaranteed merely by the ICE name. Gibbs/Metropolis feasibility does not
    establish exact independent finite samples. The least-squares spatial estimator
    used in the example is referenced rather than fully derived here. Empty empirical
    classes, constrained parameter values, initialization and sampling convergence
    need explicit handling in an implementation. The synthetic examples and one radar-image
    grouping compare particular fitted or chosen baselines. They do not establish
    the paper’s broad suggestion of universal superiority, and no numerical performance
    claim or author-code reproduction is curated.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: A probabilistic spatial-field or rooted-tree model family, distinct
      from an estimator or decoding procedure.
    evidence_ids:
    - tripletmarkovfield-source-0
  - name: aio-assessment
    value: related_match
    definition: The two field families have related ProbabilisticGraphicalModel mappings
      because the pinned target is defined and parented as a machine-learning task,
      whereas these are model families with undirected clique factorizations. PairwiseMarkovTree
      has a broad BayesianNetwork mapping for its normalized directed acyclic paired-state
      tree; the AIO target is broader. The tree mapping does not impose that factorization
      on the hidden marginal. A generic chain-rule conversion of an undirected field
      is not used to force a BayesianNetwork match preserving its graph. CausalGraphicalModel
      adds unsupported causal semantics. MarkovChain denotes sequential first-order
      structure, not arbitrary spatial fields or a branching tree; degenerate paths
      do not make the entire tree family a chain. DecisionTree, HierarchicalClassification
      and HierarchicalClustering denote decisions or grouping procedures, not the
      stochastic tree. HierarchicalLanguageModel, EnergyBasedLLM and ImplicitLanguageModel
      require language-model scope. BoltzmannMachineNetwork and RestrictedBoltzmannMachine
      denote particular stochastic neural models; a generic Gibbs field is not necessarily
      either. HopfieldNetwork adds content-addressable recurrent memory. SpatialRegression
      denotes a regression analysis, not every spatial distribution. GaussianNoiseLayer
      and GaussianDropoutLayer are neural regularizers and ProbabilisticHiddenLayer
      is a component. SupervisedLearning, UnsupervisedLearning and MachineLearningTask
      denote learning contexts; TrainingStrategy is preprocessing-scoped. Native generic
      MarkovRandomField, HMM, PMC, TMC, HME and HMDT provide context for graph topology,
      hidden–observed partition, stochastic augmentation and hierarchical gates/state
      structure. Their reading does not renew their scientific approval.
    evidence_ids:
    - mapping
- assessment_id: pairwisemarkovtree
  area: evidence
  topic: Identity, definition, mechanism, limitations, evidence version and AIO direction
  outcome: supported
  target_ids:
  - AIMech:PairwiseMarkovTree
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - pairwisemarkovtree-source-0
  summary: Pairwise denotes Z_s=(X_s,Y_s), not generic pairwise edge potentials. The
    tree is the stochastic dependence topology across sites, rather than a decision-tree
    classifier, hierarchical mixture-of-experts gate structure, or hidden Markov decision
    tree’s within-time state hierarchy. An ordinary memoryless-emission hidden Markov
    tree is a constrained special case. A path is a degenerate tree, but the family
    permits branching dependencies absent from a sequential chain. No normalized identity
    match was found across all 442 pinned AIO labels and all scoped synonyms and 391
    preceding native IDs, names and aliases for the three selected concepts. Full-checkout
    fixed-string searches included ignored and hidden files in both worktree and main,
    yielding 9 and 9 matched lines; all 7 unique contents were read. Hits are prior
    leads and references, not records of the proposed identities. All 89 semantic
    label/synonym hits and 21 fully annotated exact AIO CLASS nodes with outgoing
    edges were read. Twenty-two contextual YAMLs were byte-verified after prior full
    reading and five freshly read, totaling 21 generated and six native contextual
    records. Short acronym identities were compared across the complete normalized
    inventory. Absence is bounded to the pinned source, maintained collection and
    inspected semantic neighborhood.
  details: 'On a finite fixed rooted tree with one parent for each nonroot site, specify
    a normalized root law p(z_r) and normalized kernels K_s(z_s|z_parent(s)); their
    product defines the joint paired distribution. At fixed complete y, the hidden
    posterior factors on the same rooted tree. Set beta_s(x_s)=1 at leaves and compute
    each internal beta_s(x_s) as the product over children t of sum_(x_t) K_t(x_t,y_t|x_s,y_s)*beta_t(x_t).
    The root posterior is proportional to p(x_r,y_r)*beta_r(x_r). Each child posterior
    transition at fixed parent is proportional to K_t*beta_t and normalized over x_t.
    Propagate the root marginal downward through these conditional kernels to obtain
    all hidden-site marginals. Classical independent-emission hidden Markov trees
    result from root pi(x_r)*b(y_r|x_r) and child kernels A(x_t|x_s)*b(y_t|x_t). General
    joint kernels can leave hidden siblings dependent given only their hidden parent,
    so the hidden marginal need not itself be a Markov tree. Limitations: The definition
    uses a fixed finite rooted tree; it is not a graph-structure learning algorithm,
    a loopy-field model or a decision-making policy. Exact tree recursions require
    finite hidden states or separately tractable integrals. Posterior formulas require
    nonzero observation evidence and valid conditional support. Numerical scaling
    can be needed on large trees; the factorization alone does not address parameter
    estimation, missing observations or arbitrary topology changes. Independence of
    the child hidden-state transition from the parent observation is sufficient for
    a hidden Markov-tree marginal. Proposition 3.2 asserts necessity under the additional
    hypotheses that each internal node has at least two children with identical conditional
    laws given its paired parent; that converse is not adopted without those hypotheses.
    Correlated observations can coexist with a Markov hidden marginal. Non-Markov
    projection is permitted, not required, and memoryless site emissions are not necessary
    for every hidden-Markov special case. The four-page source proves structural and
    inference results; it does not report a comparative empirical evaluation or establish
    universal segmentation superiority. Later parameter-estimation and image-processing
    papers remain separate evidence leads.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: A probabilistic spatial-field or rooted-tree model family, distinct
      from an estimator or decoding procedure.
    evidence_ids:
    - pairwisemarkovtree-source-0
  - name: aio-assessment
    value: broad_match
    definition: The two field families have related ProbabilisticGraphicalModel mappings
      because the pinned target is defined and parented as a machine-learning task,
      whereas these are model families with undirected clique factorizations. PairwiseMarkovTree
      has a broad BayesianNetwork mapping for its normalized directed acyclic paired-state
      tree; the AIO target is broader. The tree mapping does not impose that factorization
      on the hidden marginal. A generic chain-rule conversion of an undirected field
      is not used to force a BayesianNetwork match preserving its graph. CausalGraphicalModel
      adds unsupported causal semantics. MarkovChain denotes sequential first-order
      structure, not arbitrary spatial fields or a branching tree; degenerate paths
      do not make the entire tree family a chain. DecisionTree, HierarchicalClassification
      and HierarchicalClustering denote decisions or grouping procedures, not the
      stochastic tree. HierarchicalLanguageModel, EnergyBasedLLM and ImplicitLanguageModel
      require language-model scope. BoltzmannMachineNetwork and RestrictedBoltzmannMachine
      denote particular stochastic neural models; a generic Gibbs field is not necessarily
      either. HopfieldNetwork adds content-addressable recurrent memory. SpatialRegression
      denotes a regression analysis, not every spatial distribution. GaussianNoiseLayer
      and GaussianDropoutLayer are neural regularizers and ProbabilisticHiddenLayer
      is a component. SupervisedLearning, UnsupervisedLearning and MachineLearningTask
      denote learning contexts; TrainingStrategy is preprocessing-scoped. Native generic
      MarkovRandomField, HMM, PMC, TMC, HME and HMDT provide context for graph topology,
      hidden–observed partition, stochastic augmentation and hierarchical gates/state
      structure. Their reading does not renew their scientific approval.
    evidence_ids:
    - mapping
- assessment_id: paired-field-boundary
  area: consistency
  topic: Paired processes, graph locality and Gaussian normalizability
  outcome: supported
  target_ids:
  - AIMech:HiddenObservedPairMarkovRandomField
  evidence_ids:
  - hiddenobservedpairmarkovrandomfield-source-0
  - finite-conventions
  summary: Retain the disambiguated hidden–observed pair-field identity.
  details: 'Pairwise means hidden–observed processes at each site, not clique cardinality.
    The normalized joint Gibbs model has local conditional fields but can have nonlocal
    marginals. Exact four-cycle probabilities witness this. The source Gaussian displays
    are not accepted as a certified implementation: completed-square integration and
    conditional/marginal variance are corrected in limitations, and the negative precision
    quadratic form is explicitly bounded to stated counting/boundary conventions.
    This does not invalidate the properly normalized generic family. Section5future
    fitting is not reported as achieved.'
- assessment_id: triplet-field-boundary
  area: consistency
  topic: Augmented posterior versus projected label posterior
  outcome: supported
  target_ids:
  - AIMech:TripletMarkovField
  evidence_ids:
  - tripletmarkovfield-source-0
  - finite-conventions
  summary: Retain the auxiliary-field construction and marginalization boundary.
  details: Given observations, (X,U) is the locally factorized hidden field. Summing
    U can make X nonlocal; it is incorrect to transfer augmented locality to the target
    marginal. Exact four-cycle examples distinguish both cases. The source Potts/Gaussian
    experiments restrict the generic family. ICE conditional-estimator averaging differs
    from an EM M-step absent additional assumptions; neither finite sampling exactness
    nor universal segmentation superiority is asserted.
- assessment_id: paired-tree-boundary
  area: consistency
  topic: Rooted stochastic topology and marginal converse hypotheses
  outcome: supported
  target_ids:
  - AIMech:PairwiseMarkovTree
  evidence_ids:
  - pairwisemarkovtree-source-0
  - finite-conventions
  - neighbors
  summary: Retain pair-tree identity with exact conditional-tree recursions.
  details: Root and parent-child kernels define a normalized paired-state Bayesian
    network. Upward likelihood messages and normalized downward kernels agree with
    enumeration on a branching example. Hidden sibling dependence given a hidden parent
    establishes that projection need not preserve the tree. Proposition3.2necessity
    requires its extra branching and identical-conditional-law hypotheses; sufficiency
    does not. Tree topology differs from HMDT state hierarchies and expert gating.
- assessment_id: mapping-boundary
  area: grounding
  topic: Directional AIO mappings and neighboring concepts
  outcome: supported
  target_ids:
  - AIMech:HiddenObservedPairMarkovRandomField
  - AIMech:TripletMarkovField
  - AIMech:PairwiseMarkovTree
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain the three local identities with distinct mapping scope.
  details: The two field families have related ProbabilisticGraphicalModel mappings
    because the pinned target is defined and parented as a machine-learning task,
    whereas these are model families with undirected clique factorizations. PairwiseMarkovTree
    has a broad BayesianNetwork mapping for its normalized directed acyclic paired-state
    tree; the AIO target is broader. The tree mapping does not impose that factorization
    on the hidden marginal. A generic chain-rule conversion of an undirected field
    is not used to force a BayesianNetwork match preserving its graph. CausalGraphicalModel
    adds unsupported causal semantics. MarkovChain denotes sequential first-order
    structure, not arbitrary spatial fields or a branching tree; degenerate paths
    do not make the entire tree family a chain. DecisionTree, HierarchicalClassification
    and HierarchicalClustering denote decisions or grouping procedures, not the stochastic
    tree. HierarchicalLanguageModel, EnergyBasedLLM and ImplicitLanguageModel require
    language-model scope. BoltzmannMachineNetwork and RestrictedBoltzmannMachine denote
    particular stochastic neural models; a generic Gibbs field is not necessarily
    either. HopfieldNetwork adds content-addressable recurrent memory. SpatialRegression
    denotes a regression analysis, not every spatial distribution. GaussianNoiseLayer
    and GaussianDropoutLayer are neural regularizers and ProbabilisticHiddenLayer
    is a component. SupervisedLearning, UnsupervisedLearning and MachineLearningTask
    denote learning contexts; TrainingStrategy is preprocessing-scoped. Native generic
    MarkovRandomField, HMM, PMC, TMC, HME and HMDT provide context for graph topology,
    hidden–observed partition, stochastic augmentation and hierarchical gates/state
    structure. Their reading does not renew their scientific approval.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:HiddenObservedPairMarkovRandomField
  - AIMech:TripletMarkovField
  - AIMech:PairwiseMarkovTree
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - hiddenobservedpairmarkovrandomfield-source-0
  - tripletmarkovfield-source-0
  - pairwisemarkovtree-source-0
  rationale: The pair field specifies joint hidden–observed locality on an undirected
    spatial graph; the triplet field permits nonlocal hidden–observed projection by
    introducing an auxiliary field; the pair tree specifies a rooted branching factorization
    with exact conditional-tree messages. Subclass embeddings and shared Bayesian
    inference do not make their intended identities equivalent. Preserve all three
    local IDs and directional AIO mappings.
limitations:
- Adversarial author self-review only; all records remain DRAFT.
- A22has discrepant issue metadata and inconsistent Gaussian displays; generic model
  identity is supported, but author sampling code and empirical examples are not certified.
  The precision witness depends on explicit edge-counting and boundary conventions.
- C50was read as the author-hosted2002conference manuscript. Secondary DOI/proceedings
  metadata was not independently verified through the inaccessible publisher endpoint
  and is not used as asserted persistent source metadata.
- Initial PDF DNS failures and one timeout were followed by successful authorized
  public-host retries; all final inspected bytes are hashed.
- Original finite probability checks and Gaussian quadrature do not establish empirical
  performance, general expressivity or convergence.
- 220pending leads and unresolved dispositions remain; discovery continues.
links: []
tags:
- native-concepts
- spatial-joint-markov
- self-review
- discovery-ongoing
```
