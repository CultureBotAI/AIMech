# Scientific self-review of hidden fields, trees and conditional estimation

- Review: 20261011T212447Z-hidden-fields-trees-ice
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T21:21:25Z
- Finished UTC: 2026-10-11T21:24:47Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain two DRAFT latent graphical-model families and one DRAFT parameter-estimation algorithm. Independent-emission scope, local versus marginal probabilities, exact tree inference, approximate fitting and parameterization-sensitive ICE/EM equivalence are explicit. Source display errors and version uncertainty remain qualified. No actionable curation finding remains in this selected batch.

## Scope And Provenance

All fields of three explicitly selected maintained hidden-data model/estimator concepts.

Selection: Exact maintained IDs HiddenMarkovRandomField, HiddenMarkovTree and IterativeConditionalEstimation; complete selected batch without sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 9fd1a762ff0f5240d00b8dfed84dbb2c1bd49686.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:HiddenMarkovRandomField | data/curated/HiddenMarkovRandomField.yaml | maintained | Hidden Markov random field |
| AIMech:HiddenMarkovTree | data/curated/HiddenMarkovTree.yaml | maintained | Hidden Markov tree |
| AIMech:IterativeConditionalEstimation | data/curated/IterativeConditionalEstimation.yaml | maintained | Iterative conditional estimation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:HiddenMarkovRandomField, AIMech:HiddenMarkovTree, AIMech:IterativeConditionalEstimation | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 103.54s (0:01:43)<br>Checked 442 record(s); 0 failed.<br>Checked 397 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 113 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 110,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:HiddenMarkovRandomField, AIMech:HiddenMarkovTree, AIMech:IterativeConditionalEstimation | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:HiddenMarkovRandomField, AIMech:HiddenMarkovTree, AIMech:IterativeConditionalEstimation | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:HiddenMarkovRandomField, AIMech:HiddenMarkovTree, AIMech:IterativeConditionalEstimation | Command exited0 with no output. |
| Hidden-field, tree and conditional-estimation calculations | passed | True | AIMech:HiddenMarkovRandomField, AIMech:HiddenMarkovTree, AIMech:IterativeConditionalEstimation | {"hidden_field": {"evidence": 0.04510340749192034, "local_conditionals": [0.9730458613332204, 0.9730458613332204], "map_labels": [1, 0, 0, 1], "exact_site_marginal": 0.7197232667240863, "fixed_neighbor_responsibility": 0.7999999999999999, "independent_mixture_evidence": 0.06250000000000001}, "hidden_tree": {"evidence": 0.06548839, "state_one_marginals": [0.2520730315709396, 0.3370102700646634, 0.3370102700646634, 0.3370102700646634, 0.5196678373067349], "joint_map": [0, 0, 0, 0, 0], "marginal_modes": [0, 0, 0, 0, 1], "expected_same_edge_fraction": 0.6671631414362151, "incorrectly_divided_by_state_count": 0.33358157071810757}, "conditional_estimation": {"current_p": 0.4, "ice_p": 0.7, "em_p": 0.7, "ice_in_squared_coordinate": 0.55, "em_in_squared_coordinate": 0.48999999999999994, "expected_complete_class_mean": 3.5, "expected_sum_over_expected_count": 4.0}} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, limitations, evidence version and AIO direction

evidence: supported. Targets: AIMech:HiddenMarkovRandomField.

The classical independent-emission construction specifies a hidden label field X and observed field Y, rather than only a generic MRF. It is a restricted hidden–observed pair Markov field: its hidden prior must retain the stated graph and its conditional observation law factors by site. A chain-shaped hidden graph recovers an ordinary HMM, but general spatial graphs are not subtypes of sequential Markov chains. A Gaussian observation distribution does not make the discrete hidden label field a continuous Gaussian random field. This model identity is separate from Gibbs sampling, ICM, EM and the paper’s HMRF-EM fitting framework. No normalized identity match was found across all 442 pinned AIO labels and all scoped synonyms and 394 preceding native IDs, names and aliases for these three concepts. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, yielding 64 and 64 matched lines; all 44 unique contents were read. Hits represent neighboring records, citations and discovery leads rather than records of these identities. All 97 semantic label/synonym hits were read. Twenty-one fully annotated exact CLASS nodes and outgoing edges were verified identical to the preceding inspection, and three additional nodes were read. Twenty-eight contextual YAMLs were byte-verified after prior full reading and four freshly read, totaling 24 generated and eight native contextual records. Short acronyms were included in the complete normalized identity comparison. The absence assessment is bounded to the pin, native collection and inspected semantic neighborhood.

On a finite graph, choose a proper hidden prior p(x)=Z^(-1)*exp(-sum_c V_c(x_c)) and normalized site emission laws b_i(y_i&#124;x_i). Their joint law is p(x,y)=p(x)*product_i b_i(y_i&#124;x_i). At fixed observed y with positive evidence, p(x&#124;y) is proportional to the same clique prior times the local emission factors. Its negative log density is the prior energy plus sum_i[-log b_i(y_i&#124;x_i)] up to a constant, preserving the hidden neighborhood graph. A local conditional label update conditions on neighboring hidden labels and the local observation. A site posterior marginal instead sums over all other labels given the complete observation field. With independent hidden labels and common class weights the model reduces to independent finite-mixture observations. MAP estimates a joint labeling. In loopy graphs these inference objectives need not admit the exact noniterative recursions available for a tree. Limitations: The finite-state Gibbs prior needs a finite positive partition function, and emissions must be normalized with valid support. Gaussian emissions require positive variance. Conditional independence is a modeling restriction, not a demonstrated property of every image or downsampled observation. The report’s Equation(2) gives independence across paired sites for its finite-mixture setup; applying that product to an interacting HMRF would discard the defining label dependencies. The later Equation(8) and Section2.3 joint factorization specify the supported HMRF model. The expanded Gaussian likelihood on PDF p.8 contains a quadratic-sign inconsistency. Equation(18) gives the consistent negative log-emission energy. Figure5 step4 adds likelihood and prior although MAP requires their product, or a sum of log terms as in Equation(14). These printed algorithm displays are not certified implementations. The report’s fitted HMRF-EM uses ICM-estimated neighboring labels in local responsibilities. Those plug-in responsibilities generally differ from exact full-field posterior marginals. Ideal EM monotonicity and exact global MAP are not guaranteed for this approximation. ICM can stop at a local optimum; initialization, empty classes and vanishing Gaussian variances require care. The bias-field correction framework adds assumptions and alternating updates beyond the generic model. A positive multiplicative bias before logarithms and an additive log-bias must be distinguished. No clinical validity, universal segmentation advantage, runtime guarantee or author-code reproduction is asserted. The inspected source is the 20-page FMRIB technical report TR00YZ1, not the later 2001 journal article. Its self-description as novel does not establish first invention; earlier hidden-field literature and the existing pair-field record supply historical context.

### Identity, definition, mechanism, limitations, evidence version and AIO direction

evidence: supported. Targets: AIMech:HiddenMarkovTree.

This record uses the classical independent-emission meaning of hidden Markov tree, exemplified by the inspected quadtree image model. The tree describes stochastic dependencies between sites or scales; it is not a decision tree, a hierarchical mixture-of-experts gate tree or the within-time hierarchy of a hidden Markov decision tree. It is a restricted pairwise Markov tree with kernels A(x_child&#124;x_parent)*b(y_child&#124;x_child). Some pairwise-tree literature uses hidden Markov tree more broadly for a Markov hidden marginal with correlated observations; that broader usage is not equated with this independent-emission definition. A path is an HMM special case; branching is permitted. No normalized identity match was found across all 442 pinned AIO labels and all scoped synonyms and 394 preceding native IDs, names and aliases for these three concepts. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, yielding 64 and 64 matched lines; all 44 unique contents were read. Hits represent neighboring records, citations and discovery leads rather than records of these identities. All 97 semantic label/synonym hits were read. Twenty-one fully annotated exact CLASS nodes and outgoing edges were verified identical to the preceding inspection, and three additional nodes were read. Twenty-eight contextual YAMLs were byte-verified after prior full reading and four freshly read, totaling 24 generated and eight native contextual records. Short acronyms were included in the complete normalized identity comparison. The absence assessment is bounded to the pin, native collection and inspected semantic neighborhood.

Specify a normalized root law pi(x_r), normalized transitions A_s(x_s&#124;x_parent(s)) and normalized local emissions b_s(y_s&#124;x_s). Then p(x,y)=pi(x_r)*product_nonroot A_s*product_s b_s. At a site without an observation use emission factor1. For finite hidden states, an upward likelihood message is L_s(x_s)=b_s(y_s&#124;x_s)*product_child_t sum_(x_t) A_t(x_t&#124;x_s)*L_t(x_t). The root posterior is proportional to pi*L_r, and each child posterior conditional is proportional to A_t*L_t for fixed parent. Propagating the root posterior downward gives node and edge marginals. Replacing child sums with maxima and retaining maximizing states yields joint MAP by backtracking; independently maximizing node marginals gives MPM and can select a different configuration. Exact node and edge posterior expectations permit an EM parameter update for a specified, properly normalized tree model. The source instantiates the tree as a quadtree, with optional observation levels and optional parameter tying across scales. Limitations: The record is scoped to independent child transitions and independent site emissions on a fixed finite rooted tree. Coupled siblings, loopy graphs, correlated emissions and learned topology require additional constructions. A causal tree factorization here expresses conditional probability, not intervention semantics. Generic dense transitions with K hidden states require O(number_of_edges*K^2) arithmetic for the sum-product pass; linearity in sites assumes a fixed state count. Source complexity statements linear in K are not adopted for arbitrary dense kernels. Positive evidence and careful support handling are required; numerical scaling reduces but does not eliminate all numerical risks. The source’s Equation(10) omits the complement needed for a minimized Hamming loss, and Figure4 prints argmin where Equation(11) correctly uses argmax of a posterior. Its preliminary prior pass requires root-to-leaf order. This record uses consistent sum-product/max-product semantics rather than those literal displays. For Equation(17)’s shared same-state transition probability theta, the unconstrained EM update is expected same-state edge count divided by edge count. Equations(26)–(27) print an extra state-count divisor, conflicting with the earlier theta&gt;1/K restriction. Active parameter constraints, zero expected counts and emission degeneracy need separate treatment. The exact posterior factorization in Equation(29) supports ancestral sampling after subtree messages. The experimental H-MCEM uses a local-observation conditioning shortcut and constructed coarse observations; those samples are not certified exact draws from the original posterior. SMAP is a different loss with an approximate procedure, not an alias for exact joint MAP or MPM. Quadtree image priors can create location-dependent block artifacts. EM remains initialization-sensitive and need not find a global optimum. The selected synthetic, flood and microscopy examples establish application context, not universal segmentation superiority, a modern benchmark or a reproduced implementation.

### Identity, definition, mechanism, limitations, evidence version and AIO direction

evidence: supported. Targets: AIMech:IterativeConditionalEstimation.

ICE specifies expectation of an estimator, not maximization of an expected complete-data log likelihood as in EM. The estimator may be maximum likelihood, least squares or another supported complete-data estimator. Shared applications to hidden Markov models do not make ICE a model family, an ICM label optimizer or a synonym for every stochastic EM method. Its behavior depends on the selected estimator and parameterization. The short acronym is scoped to this estimation procedure. No normalized identity match was found across all 442 pinned AIO labels and all scoped synonyms and 394 preceding native IDs, names and aliases for these three concepts. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, yielding 64 and 64 matched lines; all 44 unique contents were read. Hits represent neighboring records, citations and discovery leads rather than records of these identities. All 97 semantic label/synonym hits were read. Twenty-one fully annotated exact CLASS nodes and outgoing edges were verified identical to the preceding inspection, and three additional nodes were read. Twenty-eight contextual YAMLs were byte-verified after prior full reading and four freshly read, totaling 24 generated and eight native contextual records. Short acronyms were included in the complete normalized identity comparison. The absence assessment is bounded to the pin, native collection and inspected semantic neighborhood.

Let observed data be y and hidden data h, and choose a complete-data estimator T(h,y) of a parameter theta. From a valid current theta_k, set theta_(k+1)=E_(theta_k)[T(H,y)&#124;Y=y], when this expectation exists and remains admissible. A finite hidden space permits a posterior-weighted sum; otherwise average T over appropriate posterior samples as a Monte Carlo approximation. This average is taken after evaluating the estimator on each completed datum. It generally differs from applying a nonlinear estimator to expected sufficient statistics. With a complete-data maximum-likelihood estimator, ICE averages an argmax, whereas EM takes an argmax after averaging the log likelihood. For a regular full identifiable exponential family with a valid finite interior complete-data MLE and an invertible mean-parameter map, the expectation coordinate psi=E_theta[s(H,Y)] has complete-data estimator s(H,Y), so ICE and EM coincide in that coordinate. Nonlinear reparameterization need not preserve equality of their updates. Limitations: The complete-data estimator must be defined on posterior-supported completed data and have the required moments. Empty mixture components, boundary or infinite MLEs, constrained parameter spaces and nonidentifiability need explicit conventions; a conditional mean can leave a nonconvex parameter space. Conditional expectation is the least-squares approximation to an integrable squared-error target under a fixed law. That fact does not prove decreasing true parameter error, observed-likelihood monotonicity or global convergence across ICE iterations with changing laws. The Delmas equivalence uses the mean/expectation parameter psi, although the source calls it canonical; its natural parameter phi is distinct. The claim is not automatic for arbitrary coordinates, curved/constrained exponential families or boundary estimates. A nonlinear transformation does not generally commute with conditional expectation. For Gaussian mixtures, expectation of a complete-data class mean or variance containing a random class count differs in general from a ratio of expected sufficient statistics. The usual Gaussian-parameter ICE update therefore cannot simply be replaced by an EM update without checking the conditions. Monte Carlo approximation requires valid posterior sampling and appropriate convergence conditions. Correlated Gibbs samples, finite sample counts and apparently steady parameters do not by themselves certify exact expectations or convergence. A one-sample version can resemble stochastic EM for a specific complete-data estimator; it is not every stochastic-approximation EM algorithm. The inspected examples in Delmas contain scaling/covariance notation issues, and its introductory suggestion that mixed discrete-continuous data make likelihood irrelevant is not adopted. The definition and qualified coordinate comparison do not certify all printed example formulas. Neither inspected paper provides a universal empirical performance guarantee; no fitting, benchmark or author-code run was performed.

### Latent field identity versus approximate fitting

consistency: supported. Targets: AIMech:HiddenMarkovRandomField.

Retain the classical hidden-field model.

A Gibbs label prior with independent site emissions defines a proper latent graphical model. The local conditional graph is preserved after conditioning on observations, but a local conditional with fixed estimated neighbors is not a full posterior marginal; the finite cycle gives0.8 versus0.7197232667. The reported ICM/EM loop is approximate and is not an intrinsic model definition. Gaussian-sign and MAP-sum displays are explicitly qualified. The report version is not conflated with the2001journal article. The definition was clarified and an unnecessary uncited MPM-risk sentence removed before this formal inspection.

### Independent-emission tree model and inference objectives

consistency: supported. Targets: AIMech:HiddenMarkovTree.

Retain the explicitly scoped hidden-tree identity.

Independent child transitions and site emissions are the supported classical construction. The record acknowledges broader hidden-tree terminology in pairwise-tree literature rather than treating correlated-emission variants as equivalent. Sum-product node/edge marginals and max-product backtracking agree with complete enumeration, while MPM differs from joint MAP in the original finite example. Printed Hamming-loss/argmin and shared-transition denominator errors are not adopted. Exact posterior ancestral sampling is distinguished from the experimental local-observation shortcut. Quadtree artifacts and local fitting limits remain explicit.

### Estimator expectations, EM and nonlinear coordinates

consistency: supported. Targets: AIMech:IterativeConditionalEstimation.

Retain ICE as a distinct algorithm.

ICE averages a specified complete-data estimator under the current conditional hidden-data law; EM optimizes expected complete log likelihood. Their agreement in a regular full family’s mean coordinates has estimator existence, admissibility and invertibility conditions. A finite Bernoulli example gives p-update.7 for both but squared-coordinate updates.55 for ICE and.49 for EM, so nonlinear coordinate equality is not assumed. Random-count ratios and finite sampling require separate handling. The scanned source was visually read with checked method OCR; original1990precedence and later convergence literature are not falsely claimed inspected.

### Directional AIO mappings and neighboring concepts

grounding: supported. Targets: AIMech:HiddenMarkovRandomField, AIMech:HiddenMarkovTree, AIMech:IterativeConditionalEstimation.

Retain all three native identities with qualified mapping directions.

HMRF has a related ProbabilisticGraphicalModel mapping because the pinned class is defined and parented as a machine-learning task. The independent-emission HMT has a broad BayesianNetwork mapping: a rooted hidden tree with emitted observation leaves is a restricted normalized directed acyclic probability model, without causal-intervention semantics. ICE has a related MachineLearningTask mapping for its parameter-learning role; it is an estimator iteration, not a subtype of a learning task. SupervisedLearning and UnsupervisedLearning impose contexts not required by every ICE application. TrainingStrategy is preprocessing-scoped. A generic undirected field does not justify a BayesianNetwork map that preserves its graph merely because arbitrary chain-rule conversion is possible. MarkovChain requires sequential structure rather than a generic spatial graph or branching tree. DecisionTree, HierarchicalClassification and HierarchicalClustering concern decisions/grouping rather than latent stochastic topology. HierarchicalLanguageModel, EnergyBasedLLM and ImplicitLanguageModel are language-scoped. BoltzmannMachineNetwork, RestrictedBoltzmannMachine and HopfieldNetwork add particular neural/state semantics. SpatialRegression and RegressionAnalysis are regression-scoped, not generic latent-label models or incomplete-data estimators. GaussianNoiseLayer, GaussianDropoutLayer, HiddenLayer and ProbabilisticHiddenLayer are neural components. MaximumLayer is an elementwise tensor merger, not MAP, EM or ICE. Native MRF, HMM, paired field, triplet field, paired tree, EM, HME and HMDT distinguish generic graph scope, hidden-observed partition, topology, augmentation, estimator iteration and gating. Contextual reading does not renew their scientific approval.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:HiddenMarkovRandomField, AIMech:HiddenMarkovTree, AIMech:IterativeConditionalEstimation. HMRF imposes local latent-field dependencies and independent site observations; HMT restricts hidden topology to a rooted tree with independent child transitions; ICE specifies a conditional-estimator update applicable to incomplete-data models. Structural special cases and shared applications do not make a general spatial model, a tree specialization and a fitting procedure equivalent. Preserve their local IDs and explicit AIO mappings.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T212023Z-hidden-fields-trees-ice.json | supports | No normalized identity match was found across all 442 pinned AIO labels and all scoped synonyms and 394 preceding native IDs, names and aliases for these three concepts. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, yielding 64 and 64 matched lines; all 44 unique contents were read. Hits represent neighboring records, citations and discovery leads rather than records of these identities. All 97 semantic label/synonym hits were read. Twenty-one fully annotated exact CLASS nodes and outgoing edges were verified identical to the preceding inspection, and three additional nodes were read. Twenty-eight contextual YAMLs were byte-verified after prior full reading and four freshly read, totaling 24 generated and eight native contextual records. Short acronyms were included in the complete normalized identity comparison. The absence assessment is bounded to the pin, native collection and inspected semantic neighborhood. |
| mapping | sources/aio/aio.json; 24 exact CLASS nodes and outgoing edges, and97 semantic label/synonym hits in source_analysis.aio_mapping_inspection | supports | HMRF has a related ProbabilisticGraphicalModel mapping because the pinned class is defined and parented as a machine-learning task. The independent-emission HMT has a broad BayesianNetwork mapping: a rooted hidden tree with emitted observation leaves is a restricted normalized directed acyclic probability model, without causal-intervention semantics. ICE has a related MachineLearningTask mapping for its parameter-learning role; it is an estimator iteration, not a subtype of a learning task. SupervisedLearning and UnsupervisedLearning impose contexts not required by every ICE application. TrainingStrategy is preprocessing-scoped. A generic undirected field does not justify a BayesianNetwork map that preserves its graph merely because arbitrary chain-rule conversion is possible. MarkovChain requires sequential structure rather than a generic spatial graph or branching tree. DecisionTree, HierarchicalClassification and HierarchicalClustering concern decisions/grouping rather than latent stochastic topology. HierarchicalLanguageModel, EnergyBasedLLM and ImplicitLanguageModel are language-scoped. BoltzmannMachineNetwork, RestrictedBoltzmannMachine and HopfieldNetwork add particular neural/state semantics. SpatialRegression and RegressionAnalysis are regression-scoped, not generic latent-label models or incomplete-data estimators. GaussianNoiseLayer, GaussianDropoutLayer, HiddenLayer and ProbabilisticHiddenLayer are neural components. MaximumLayer is an elementwise tensor merger, not MAP, EM or ICE. Native MRF, HMM, paired field, triplet field, paired tree, EM, HME and HMDT distinguish generic graph scope, hidden-observed partition, topology, augmentation, estimator iteration and gating. Contextual reading does not renew their scientific approval. |
| neighbors | research/discovery/20261011T212023Z-hidden-fields-trees-ice.json; source_analysis.aio_mapping_inspection.native_neighbors and context_reading | supports | Eight complete native contextual records read or byte-verified after prior reading: MRF, HMM, hidden-observed pair field, triplet field, paired tree, EM, HME and HMDT. They distinguish graph structure, latent/observed partition, augmentation, estimator iteration and expert gating. Contextual reading does not renew scientific approval. |
| finite-conventions | research/discovery/hidden-fields-trees-ice-boundaries.py; Finite four-cycle hidden field; five-site quadtree; Bernoulli estimator coordinate example | supports | Original finite calculations verify a four-cycle HMRF joint normalization and local posterior conditionals while showing an exact site marginal0.7197232667 differs from a fixed-neighbor responsibility0.8. Removing coupling recovers independent-mixture evidence0.0625. A five-site quadtree with a missing root observation has sum-product likelihood0.06548839 and node marginals agreeing with enumeration; max-product backtracking returns00000 while marginal modes are00001. Its unconstrained expected self-transition fraction0.6671631414 differs from the incorrectly state-count-divided0.3335815707, which violates the source’s theta&gt;1/2 restriction. For two Bernoulli trials with the first observed as1 and current p=.4, ICE and EM in p both give.7, but in theta=p^2 exact EM gives.49 and ICE gives.55. A random-count illustration gives expectation of a ratio3.5 versus ratio of expectations4. These are fixed mathematical examples, not author code, parameter fitting, model evaluation or general convergence theorems. |
| hiddenmarkovrandomfield-source-0 | https://www.fmrib.ox.ac.uk/datasets/techrep/tr00yz1/tr00yz1.pdf; Sections2.2–2.3, PDF/printed pp.4–6, Equations(5)–(10); Sections4–5, pp.7–9, Equations(14)–(28); Sections7–9, pp.12–16, especially Figure5 and approximation/initialization discussion | supports | Hidden Markov Random Field Model and Segmentation of Brain MR Images. FMRIB Technical Report TR00YZ1, listed under 2000 in the Oxford repository. Title page says a related paper was submitted to IEEE Transactions on Medical Imaging. All20 PDF pages visually read; PDF and printed pages agree. The related 2001 journal paper has a different title, author order and pagination and is not substituted for these bytes. All target-defining pages visually read. Source-analysis notes preserve interpretation, formula errors, OCR limitations and version distinctions. |
| hiddenmarkovtree-source-0 | https://web.engr.oregonstate.edu/~sinisa/courses/OSU/CS559/lectures/QuadTreeInference.pdf; SectionsII–III, printed pp.390–393 / PDF pp.1–4, Equations(1)–(4); SectionsIVA–C, pp.393–396 / PDF pp.4–7; SectionsV–VI, pp.398–403 / PDF pp.9–14, especially Equations(21)–(29) | supports | Discrete Markov Image Modeling and Inference on the Quadtree. IEEE Transactions on Image Processing9(3):390–404, March2000; university-hosted journal PDF. Received July21,1998; revised July23,1999. All15 pages visually read; printed page=PDF page+389. DOI and bibliographic metadata corroborated by PubMed. All target-defining pages visually read. Source-analysis notes preserve interpretation, formula errors, OCR limitations and version distinctions. |
| iterativeconditionalestimation-source-0 | https://www-public.imtbs-tsp.eu/~pieczyn/C7.pdf; Section3, printed pp.263–265 / PDF pp.3–5, Equations(3)–(9); Sections4–5, pp.265–267 / PDF pp.5–7, complete estimators, simulation approximation and limited asymptotic results | supports | Statistical image segmentation. Machine GRAPHICS and VISION1(1/2):261–268,1992, proceedings of the second GKiPO92 meeting, Naleczow, May18–23,1992. Author-hosted scanned PDF; all8 pages visually read. Tesseract5.5.3 OCR generated for all pages, with method pages3–6 read and compared visually; mathematical OCR was not trusted alone. Printed page=PDF page+260. Reference20 cites an earlier1990 technical report; no first-invention date is asserted. All target-defining pages visually read. Source-analysis notes preserve interpretation, formula errors, OCR limitations and version distinctions. |
| iterativeconditionalestimation-source-1 | https://www-public.imtbs-tsp.eu/~delmas/articlesPDF.JPD/IEEE/2-1997.pdf; SectionsII–III, printed pp.2613–2615 / PDF pp.1–3, Equations(1)–(4), Propositions1–2 and the parameterization discussion | supports | An Equivalence of the EM and ICE Algorithm for Exponential Family. IEEE Transactions on Signal Processing45(10):2613–2615, October1997; author-hosted journal PDF. All3 pages visually read; printed page=PDF page+2612. The author bibliography links these bytes under the alternate title An extension to the EM Algorithm for exponential family. Secondary metadata suggests DOI10.1109/78.640732, but its endpoint was inaccessible; no independently verified DOI is asserted. All target-defining pages visually read. Source-analysis notes preserve interpretation, formula errors, OCR limitations and version distinctions. |

## Limits And Additional Notes

- Adversarial author self-review only; all three records remain DRAFT.
- TR00YZ1 was read as an Oxford technical report, not the later journal article. Its printed errors and approximate fitting procedure are qualified.
- The quadtree source has formula and algorithm-display inconsistencies; consistent normalized model/inference identities are supported, but experimental H-MCEM is not certified exact posterior sampling.
- ICE/EM agreement is stated only with its coordinate and regularity restrictions. Delmas DOI access failed; exact PDF identity is supported by printed metadata and the author-hosted copy, without asserting independently verified DOI metadata.
- The scanned1992paper was fully viewed, with OCR method pages checked visually; garbled extraction was not treated as evidence of absence.
- Original finite calculations are not author-code reproduction, training, benchmarking or general convergence proofs.
- 225 pending leads and unresolved dispositions remain; discovery continues.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T212447Z-hidden-fields-trees-ice
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of hidden fields, trees and conditional estimation
started_at: '2026-10-11T21:21:25Z'
finished_at: '2026-10-11T21:24:47Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed all fields of three
    new records against46 fully visually read primary PDF pages,24 annotated AIO nodes
    and8 native contextual records. Original finite distributions and estimator-coordinate
    checks challenge local-marginal, decoder, normalization and equivalence overclaims.
    This is self-review, not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain two DRAFT latent graphical-model families and one DRAFT parameter-estimation
  algorithm. Independent-emission scope, local versus marginal probabilities, exact
  tree inference, approximate fitting and parameterization-sensitive ICE/EM equivalence
  are explicit. Source display errors and version uncertainty remain qualified. No
  actionable curation finding remains in this selected batch.
source:
  git_revision: 9fd1a762ff0f5240d00b8dfed84dbb2c1bd49686
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
  - path: data/aio/HiddenLayer.yaml
    sha256: 945f974c1d298a827086c3439ec3f9ae029380f6d2fa52378eb95ccad1f3b886
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
  - path: data/aio/MaximumLayer.yaml
    sha256: 7e034921f50c25cba46a261fc2f30b638ec7c5129fb150ee8d26373b4a6f3d54
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/ProbabilisticHiddenLayer.yaml
    sha256: 610c29db815f7348c5bdcdc7e7460dd2dea9ea338f3727ebb1596c51b4af41da
    role: context
  - path: data/aio/RegressionAnalysis.yaml
    sha256: 6f5d48096556a2ec31770aab306219e9020919940b4e80554639cc97aaa94bc6
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
  - path: data/curated/ExpectationMaximization.yaml
    sha256: eab2880f9e6db51aa49135ada0c3f6d1504e947e6f920d0a5913fd7ddbd069c4
    role: context
  - path: data/curated/HiddenMarkovDecisionTree.yaml
    sha256: ee90a9296d1f3fa33b29c2f0160ae5b5d54787c02893fea2cbd516e6db535d18
    role: context
  - path: data/curated/HiddenMarkovModel.yaml
    sha256: 062a31bd525cb90e8077d4889c177f55cb7b29dea4e71c33be95bae9e72a5240
    role: context
  - path: data/curated/HiddenMarkovRandomField.yaml
    sha256: 620a68339af0155d1b1f83304dde7fed4634ec95e5a9541480f0d0b37b326327
    role: target
  - path: data/curated/HiddenMarkovTree.yaml
    sha256: ca89c267443e8b806d61b389943bd06a514fb8a95668bd604fae4ecc2d873e1b
    role: target
  - path: data/curated/HiddenObservedPairMarkovRandomField.yaml
    sha256: 9902ffe65520a472669667888ee091407d5a43c6885011a51eb1e6a5262ec827
    role: context
  - path: data/curated/HierarchicalMixtureOfExperts.yaml
    sha256: 726b98de332b75f77dc51f3028687650e2077216f26100a16c6fc4e8328c4e18
    role: context
  - path: data/curated/IterativeConditionalEstimation.yaml
    sha256: 98813e020f43870f725a5c1e4ab0de9197f0dc2bc85f61e66e2044ab8d87e9cc
    role: target
  - path: data/curated/MarkovRandomField.yaml
    sha256: 03b1f2a66b2183a5bf5943bee7ec0619b9e07947d6c9187263e279ee475f9149
    role: context
  - path: data/curated/PairwiseMarkovTree.yaml
    sha256: f7dbda0ba922be5032e7e4f310c6dbcf0e8260c534039c8d58f67e50da1acf93
    role: context
  - path: data/curated/TripletMarkovField.yaml
    sha256: bbf17102f0cee437cfead8bea4ee3c3513b5a347accfd10f44990798f4b98512
    role: context
  - path: research/discovery/20261011T212023Z-hidden-fields-trees-ice.json
    sha256: 169d461ff4998ddb7345a74b38e67a4fc0ad74100649d0d59becf233df9c70c9
    role: context
  - path: research/discovery/hidden-fields-trees-ice-boundaries.py
    sha256: 46962762e076e1e8a41e5b3bbc7ac147fc181d8cd48072d4416f558be7724a55
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
- target_id: AIMech:HiddenMarkovRandomField
  path: data/curated/HiddenMarkovRandomField.yaml
  label: Hidden Markov random field
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HiddenMarkovRandomField.yaml
    role: maintained
- target_id: AIMech:HiddenMarkovTree
  path: data/curated/HiddenMarkovTree.yaml
  label: Hidden Markov tree
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/HiddenMarkovTree.yaml
    role: maintained
- target_id: AIMech:IterativeConditionalEstimation
  path: data/curated/IterativeConditionalEstimation.yaml
  label: Iterative conditional estimation
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/IterativeConditionalEstimation.yaml
    role: maintained
scope:
  description: All fields of three explicitly selected maintained hidden-data model/estimator
    concepts.
  selection: Exact maintained IDs HiddenMarkovRandomField, HiddenMarkovTree and IterativeConditionalEstimation;
    complete selected batch without sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:HiddenMarkovRandomField
  - AIMech:HiddenMarkovTree
  - AIMech:IterativeConditionalEstimation
  exclusions:
  - target: Author code, empirical performance and general convergence theorems
    reason: No author implementation, data fitting or benchmark ran. Finite witnesses
      do not establish global convergence or universal performance.
  - target: Prior records and remaining frontier
    reason: Eight older records provide context without renewed scientific approval.225
      pending leads plus unresolved dispositions remain.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:HiddenMarkovRandomField
  - AIMech:HiddenMarkovTree
  - AIMech:IterativeConditionalEstimation
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 103.54s (0:01:43)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 397 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 113 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 110,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:HiddenMarkovRandomField
  - AIMech:HiddenMarkovTree
  - AIMech:IterativeConditionalEstimation
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
  - AIMech:HiddenMarkovRandomField
  - AIMech:HiddenMarkovTree
  - AIMech:IterativeConditionalEstimation
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
  - AIMech:HiddenMarkovRandomField
  - AIMech:HiddenMarkovTree
  - AIMech:IterativeConditionalEstimation
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited0 with no output.
- check_id: finite-arithmetic
  name: Hidden-field, tree and conditional-estimation calculations
  command: python3 research/discovery/hidden-fields-trees-ice-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:HiddenMarkovRandomField
  - AIMech:HiddenMarkovTree
  - AIMech:IterativeConditionalEstimation
  exit_code: 0
  expected_exit_code: 0
  summary: '{"hidden_field": {"evidence": 0.04510340749192034, "local_conditionals":
    [0.9730458613332204, 0.9730458613332204], "map_labels": [1, 0, 0, 1], "exact_site_marginal":
    0.7197232667240863, "fixed_neighbor_responsibility": 0.7999999999999999, "independent_mixture_evidence":
    0.06250000000000001}, "hidden_tree": {"evidence": 0.06548839, "state_one_marginals":
    [0.2520730315709396, 0.3370102700646634, 0.3370102700646634, 0.3370102700646634,
    0.5196678373067349], "joint_map": [0, 0, 0, 0, 0], "marginal_modes": [0, 0, 0,
    0, 1], "expected_same_edge_fraction": 0.6671631414362151, "incorrectly_divided_by_state_count":
    0.33358157071810757}, "conditional_estimation": {"current_p": 0.4, "ice_p": 0.7,
    "em_p": 0.7, "ice_in_squared_coordinate": 0.55, "em_in_squared_coordinate": 0.48999999999999994,
    "expected_complete_class_mean": 3.5, "expected_sum_over_expected_count": 4.0}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T212023Z-hidden-fields-trees-ice.json
  accessed_at: '2026-10-11T21:21:25Z'
  support: supports
  summary: No normalized identity match was found across all 442 pinned AIO labels
    and all scoped synonyms and 394 preceding native IDs, names and aliases for these
    three concepts. Full-checkout fixed-string searches included ignored and hidden
    files in worktree and main, yielding 64 and 64 matched lines; all 44 unique contents
    were read. Hits represent neighboring records, citations and discovery leads rather
    than records of these identities. All 97 semantic label/synonym hits were read.
    Twenty-one fully annotated exact CLASS nodes and outgoing edges were verified
    identical to the preceding inspection, and three additional nodes were read. Twenty-eight
    contextual YAMLs were byte-verified after prior full reading and four freshly
    read, totaling 24 generated and eight native contextual records. Short acronyms
    were included in the complete normalized identity comparison. The absence assessment
    is bounded to the pin, native collection and inspected semantic neighborhood.
  search_scope: No normalized identity match was found across all 442 pinned AIO labels
    and all scoped synonyms and 394 preceding native IDs, names and aliases for these
    three concepts. Full-checkout fixed-string searches included ignored and hidden
    files in worktree and main, yielding 64 and 64 matched lines; all 44 unique contents
    were read. Hits represent neighboring records, citations and discovery leads rather
    than records of these identities. All 97 semantic label/synonym hits were read.
    Twenty-one fully annotated exact CLASS nodes and outgoing edges were verified
    identical to the preceding inspection, and three additional nodes were read. Twenty-eight
    contextual YAMLs were byte-verified after prior full reading and four freshly
    read, totaling 24 generated and eight native contextual records. Short acronyms
    were included in the complete normalized identity comparison. The absence assessment
    is bounded to the pin, native collection and inspected semantic neighborhood.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: 24 exact CLASS nodes and outgoing edges, and97 semantic label/synonym hits
    in source_analysis.aio_mapping_inspection
  accessed_at: '2026-10-11T21:21:25Z'
  support: supports
  summary: 'HMRF has a related ProbabilisticGraphicalModel mapping because the pinned
    class is defined and parented as a machine-learning task. The independent-emission
    HMT has a broad BayesianNetwork mapping: a rooted hidden tree with emitted observation
    leaves is a restricted normalized directed acyclic probability model, without
    causal-intervention semantics. ICE has a related MachineLearningTask mapping for
    its parameter-learning role; it is an estimator iteration, not a subtype of a
    learning task. SupervisedLearning and UnsupervisedLearning impose contexts not
    required by every ICE application. TrainingStrategy is preprocessing-scoped. A
    generic undirected field does not justify a BayesianNetwork map that preserves
    its graph merely because arbitrary chain-rule conversion is possible. MarkovChain
    requires sequential structure rather than a generic spatial graph or branching
    tree. DecisionTree, HierarchicalClassification and HierarchicalClustering concern
    decisions/grouping rather than latent stochastic topology. HierarchicalLanguageModel,
    EnergyBasedLLM and ImplicitLanguageModel are language-scoped. BoltzmannMachineNetwork,
    RestrictedBoltzmannMachine and HopfieldNetwork add particular neural/state semantics.
    SpatialRegression and RegressionAnalysis are regression-scoped, not generic latent-label
    models or incomplete-data estimators. GaussianNoiseLayer, GaussianDropoutLayer,
    HiddenLayer and ProbabilisticHiddenLayer are neural components. MaximumLayer is
    an elementwise tensor merger, not MAP, EM or ICE. Native MRF, HMM, paired field,
    triplet field, paired tree, EM, HME and HMDT distinguish generic graph scope,
    hidden-observed partition, topology, augmentation, estimator iteration and gating.
    Contextual reading does not renew their scientific approval.'
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T212023Z-hidden-fields-trees-ice.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors and context_reading
  accessed_at: '2026-10-11T21:21:25Z'
  support: supports
  summary: 'Eight complete native contextual records read or byte-verified after prior
    reading: MRF, HMM, hidden-observed pair field, triplet field, paired tree, EM,
    HME and HMDT. They distinguish graph structure, latent/observed partition, augmentation,
    estimator iteration and expert gating. Contextual reading does not renew scientific
    approval.'
- evidence_id: finite-conventions
  kind: record_content
  reference: research/discovery/hidden-fields-trees-ice-boundaries.py
  locator: Finite four-cycle hidden field; five-site quadtree; Bernoulli estimator
    coordinate example
  accessed_at: '2026-10-11T21:21:25Z'
  snapshot_sha256: 46962762e076e1e8a41e5b3bbc7ac147fc181d8cd48072d4416f558be7724a55
  support: supports
  summary: Original finite calculations verify a four-cycle HMRF joint normalization
    and local posterior conditionals while showing an exact site marginal0.7197232667
    differs from a fixed-neighbor responsibility0.8. Removing coupling recovers independent-mixture
    evidence0.0625. A five-site quadtree with a missing root observation has sum-product
    likelihood0.06548839 and node marginals agreeing with enumeration; max-product
    backtracking returns00000 while marginal modes are00001. Its unconstrained expected
    self-transition fraction0.6671631414 differs from the incorrectly state-count-divided0.3335815707,
    which violates the source’s theta>1/2 restriction. For two Bernoulli trials with
    the first observed as1 and current p=.4, ICE and EM in p both give.7, but in theta=p^2
    exact EM gives.49 and ICE gives.55. A random-count illustration gives expectation
    of a ratio3.5 versus ratio of expectations4. These are fixed mathematical examples,
    not author code, parameter fitting, model evaluation or general convergence theorems.
- evidence_id: hiddenmarkovrandomfield-source-0
  kind: primary_source
  reference: https://www.fmrib.ox.ac.uk/datasets/techrep/tr00yz1/tr00yz1.pdf
  locator: Sections2.2–2.3, PDF/printed pp.4–6, Equations(5)–(10); Sections4–5, pp.7–9,
    Equations(14)–(28); Sections7–9, pp.12–16, especially Figure5 and approximation/initialization
    discussion
  accessed_at: '2026-10-11T21:07:09Z'
  snapshot_sha256: b88c2018ec008ae15e6f902a564084a2d5ba086b79a8b9d3e83744ebb39b7c99
  support: supports
  summary: Hidden Markov Random Field Model and Segmentation of Brain MR Images. FMRIB
    Technical Report TR00YZ1, listed under 2000 in the Oxford repository. Title page
    says a related paper was submitted to IEEE Transactions on Medical Imaging. All20
    PDF pages visually read; PDF and printed pages agree. The related 2001 journal
    paper has a different title, author order and pagination and is not substituted
    for these bytes. All target-defining pages visually read. Source-analysis notes
    preserve interpretation, formula errors, OCR limitations and version distinctions.
- evidence_id: hiddenmarkovtree-source-0
  kind: primary_source
  reference: https://web.engr.oregonstate.edu/~sinisa/courses/OSU/CS559/lectures/QuadTreeInference.pdf
  locator: SectionsII–III, printed pp.390–393 / PDF pp.1–4, Equations(1)–(4); SectionsIVA–C,
    pp.393–396 / PDF pp.4–7; SectionsV–VI, pp.398–403 / PDF pp.9–14, especially Equations(21)–(29)
  accessed_at: '2026-10-11T21:07:05Z'
  snapshot_sha256: ec6f929d2ddf492b67539e8c22e49d6f6666aa1aedc4b0340370ceca2e015c01
  support: supports
  summary: Discrete Markov Image Modeling and Inference on the Quadtree. IEEE Transactions
    on Image Processing9(3):390–404, March2000; university-hosted journal PDF. Received
    July21,1998; revised July23,1999. All15 pages visually read; printed page=PDF
    page+389. DOI and bibliographic metadata corroborated by PubMed. All target-defining
    pages visually read. Source-analysis notes preserve interpretation, formula errors,
    OCR limitations and version distinctions.
- evidence_id: iterativeconditionalestimation-source-0
  kind: primary_source
  reference: https://www-public.imtbs-tsp.eu/~pieczyn/C7.pdf
  locator: Section3, printed pp.263–265 / PDF pp.3–5, Equations(3)–(9); Sections4–5,
    pp.265–267 / PDF pp.5–7, complete estimators, simulation approximation and limited
    asymptotic results
  accessed_at: '2026-10-11T21:05:52Z'
  snapshot_sha256: 3fd1eb9cfae006ffcfcc37e1709ecba52c057169fcd06a6502ae0dee9443b2ce
  support: supports
  summary: Statistical image segmentation. Machine GRAPHICS and VISION1(1/2):261–268,1992,
    proceedings of the second GKiPO92 meeting, Naleczow, May18–23,1992. Author-hosted
    scanned PDF; all8 pages visually read. Tesseract5.5.3 OCR generated for all pages,
    with method pages3–6 read and compared visually; mathematical OCR was not trusted
    alone. Printed page=PDF page+260. Reference20 cites an earlier1990 technical report;
    no first-invention date is asserted. All target-defining pages visually read.
    Source-analysis notes preserve interpretation, formula errors, OCR limitations
    and version distinctions.
- evidence_id: iterativeconditionalestimation-source-1
  kind: primary_source
  reference: https://www-public.imtbs-tsp.eu/~delmas/articlesPDF.JPD/IEEE/2-1997.pdf
  locator: SectionsII–III, printed pp.2613–2615 / PDF pp.1–3, Equations(1)–(4), Propositions1–2
    and the parameterization discussion
  accessed_at: '2026-10-11T21:06:35Z'
  snapshot_sha256: 065593e02a66acf0456c8b3a1e4ea5d4170eab1056c1f2e3929d82a1aed35346
  support: supports
  summary: An Equivalence of the EM and ICE Algorithm for Exponential Family. IEEE
    Transactions on Signal Processing45(10):2613–2615, October1997; author-hosted
    journal PDF. All3 pages visually read; printed page=PDF page+2612. The author
    bibliography links these bytes under the alternate title An extension to the EM
    Algorithm for exponential family. Secondary metadata suggests DOI10.1109/78.640732,
    but its endpoint was inaccessible; no independently verified DOI is asserted.
    All target-defining pages visually read. Source-analysis notes preserve interpretation,
    formula errors, OCR limitations and version distinctions.
assessments:
- assessment_id: hiddenmarkovrandomfield
  area: evidence
  topic: Identity, definition, mechanism, limitations, evidence version and AIO direction
  outcome: supported
  target_ids:
  - AIMech:HiddenMarkovRandomField
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - hiddenmarkovrandomfield-source-0
  summary: 'The classical independent-emission construction specifies a hidden label
    field X and observed field Y, rather than only a generic MRF. It is a restricted
    hidden–observed pair Markov field: its hidden prior must retain the stated graph
    and its conditional observation law factors by site. A chain-shaped hidden graph
    recovers an ordinary HMM, but general spatial graphs are not subtypes of sequential
    Markov chains. A Gaussian observation distribution does not make the discrete
    hidden label field a continuous Gaussian random field. This model identity is
    separate from Gibbs sampling, ICM, EM and the paper’s HMRF-EM fitting framework.
    No normalized identity match was found across all 442 pinned AIO labels and all
    scoped synonyms and 394 preceding native IDs, names and aliases for these three
    concepts. Full-checkout fixed-string searches included ignored and hidden files
    in worktree and main, yielding 64 and 64 matched lines; all 44 unique contents
    were read. Hits represent neighboring records, citations and discovery leads rather
    than records of these identities. All 97 semantic label/synonym hits were read.
    Twenty-one fully annotated exact CLASS nodes and outgoing edges were verified
    identical to the preceding inspection, and three additional nodes were read. Twenty-eight
    contextual YAMLs were byte-verified after prior full reading and four freshly
    read, totaling 24 generated and eight native contextual records. Short acronyms
    were included in the complete normalized identity comparison. The absence assessment
    is bounded to the pin, native collection and inspected semantic neighborhood.'
  details: 'On a finite graph, choose a proper hidden prior p(x)=Z^(-1)*exp(-sum_c
    V_c(x_c)) and normalized site emission laws b_i(y_i|x_i). Their joint law is p(x,y)=p(x)*product_i
    b_i(y_i|x_i). At fixed observed y with positive evidence, p(x|y) is proportional
    to the same clique prior times the local emission factors. Its negative log density
    is the prior energy plus sum_i[-log b_i(y_i|x_i)] up to a constant, preserving
    the hidden neighborhood graph. A local conditional label update conditions on
    neighboring hidden labels and the local observation. A site posterior marginal
    instead sums over all other labels given the complete observation field. With
    independent hidden labels and common class weights the model reduces to independent
    finite-mixture observations. MAP estimates a joint labeling. In loopy graphs these
    inference objectives need not admit the exact noniterative recursions available
    for a tree. Limitations: The finite-state Gibbs prior needs a finite positive
    partition function, and emissions must be normalized with valid support. Gaussian
    emissions require positive variance. Conditional independence is a modeling restriction,
    not a demonstrated property of every image or downsampled observation. The report’s
    Equation(2) gives independence across paired sites for its finite-mixture setup;
    applying that product to an interacting HMRF would discard the defining label
    dependencies. The later Equation(8) and Section2.3 joint factorization specify
    the supported HMRF model. The expanded Gaussian likelihood on PDF p.8 contains
    a quadratic-sign inconsistency. Equation(18) gives the consistent negative log-emission
    energy. Figure5 step4 adds likelihood and prior although MAP requires their product,
    or a sum of log terms as in Equation(14). These printed algorithm displays are
    not certified implementations. The report’s fitted HMRF-EM uses ICM-estimated
    neighboring labels in local responsibilities. Those plug-in responsibilities generally
    differ from exact full-field posterior marginals. Ideal EM monotonicity and exact
    global MAP are not guaranteed for this approximation. ICM can stop at a local
    optimum; initialization, empty classes and vanishing Gaussian variances require
    care. The bias-field correction framework adds assumptions and alternating updates
    beyond the generic model. A positive multiplicative bias before logarithms and
    an additive log-bias must be distinguished. No clinical validity, universal segmentation
    advantage, runtime guarantee or author-code reproduction is asserted. The inspected
    source is the 20-page FMRIB technical report TR00YZ1, not the later 2001 journal
    article. Its self-description as novel does not establish first invention; earlier
    hidden-field literature and the existing pair-field record supply historical context.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: Graphical model family or complete-data estimator iteration; a model
      and its fitting procedure have distinct identities.
    evidence_ids:
    - hiddenmarkovrandomfield-source-0
  - name: aio-assessment
    value: related_match
    definition: 'HMRF has a related ProbabilisticGraphicalModel mapping because the
      pinned class is defined and parented as a machine-learning task. The independent-emission
      HMT has a broad BayesianNetwork mapping: a rooted hidden tree with emitted observation
      leaves is a restricted normalized directed acyclic probability model, without
      causal-intervention semantics. ICE has a related MachineLearningTask mapping
      for its parameter-learning role; it is an estimator iteration, not a subtype
      of a learning task. SupervisedLearning and UnsupervisedLearning impose contexts
      not required by every ICE application. TrainingStrategy is preprocessing-scoped.
      A generic undirected field does not justify a BayesianNetwork map that preserves
      its graph merely because arbitrary chain-rule conversion is possible. MarkovChain
      requires sequential structure rather than a generic spatial graph or branching
      tree. DecisionTree, HierarchicalClassification and HierarchicalClustering concern
      decisions/grouping rather than latent stochastic topology. HierarchicalLanguageModel,
      EnergyBasedLLM and ImplicitLanguageModel are language-scoped. BoltzmannMachineNetwork,
      RestrictedBoltzmannMachine and HopfieldNetwork add particular neural/state semantics.
      SpatialRegression and RegressionAnalysis are regression-scoped, not generic
      latent-label models or incomplete-data estimators. GaussianNoiseLayer, GaussianDropoutLayer,
      HiddenLayer and ProbabilisticHiddenLayer are neural components. MaximumLayer
      is an elementwise tensor merger, not MAP, EM or ICE. Native MRF, HMM, paired
      field, triplet field, paired tree, EM, HME and HMDT distinguish generic graph
      scope, hidden-observed partition, topology, augmentation, estimator iteration
      and gating. Contextual reading does not renew their scientific approval.'
    evidence_ids:
    - mapping
- assessment_id: hiddenmarkovtree
  area: evidence
  topic: Identity, definition, mechanism, limitations, evidence version and AIO direction
  outcome: supported
  target_ids:
  - AIMech:HiddenMarkovTree
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - hiddenmarkovtree-source-0
  summary: This record uses the classical independent-emission meaning of hidden Markov
    tree, exemplified by the inspected quadtree image model. The tree describes stochastic
    dependencies between sites or scales; it is not a decision tree, a hierarchical
    mixture-of-experts gate tree or the within-time hierarchy of a hidden Markov decision
    tree. It is a restricted pairwise Markov tree with kernels A(x_child|x_parent)*b(y_child|x_child).
    Some pairwise-tree literature uses hidden Markov tree more broadly for a Markov
    hidden marginal with correlated observations; that broader usage is not equated
    with this independent-emission definition. A path is an HMM special case; branching
    is permitted. No normalized identity match was found across all 442 pinned AIO
    labels and all scoped synonyms and 394 preceding native IDs, names and aliases
    for these three concepts. Full-checkout fixed-string searches included ignored
    and hidden files in worktree and main, yielding 64 and 64 matched lines; all 44
    unique contents were read. Hits represent neighboring records, citations and discovery
    leads rather than records of these identities. All 97 semantic label/synonym hits
    were read. Twenty-one fully annotated exact CLASS nodes and outgoing edges were
    verified identical to the preceding inspection, and three additional nodes were
    read. Twenty-eight contextual YAMLs were byte-verified after prior full reading
    and four freshly read, totaling 24 generated and eight native contextual records.
    Short acronyms were included in the complete normalized identity comparison. The
    absence assessment is bounded to the pin, native collection and inspected semantic
    neighborhood.
  details: 'Specify a normalized root law pi(x_r), normalized transitions A_s(x_s|x_parent(s))
    and normalized local emissions b_s(y_s|x_s). Then p(x,y)=pi(x_r)*product_nonroot
    A_s*product_s b_s. At a site without an observation use emission factor1. For
    finite hidden states, an upward likelihood message is L_s(x_s)=b_s(y_s|x_s)*product_child_t
    sum_(x_t) A_t(x_t|x_s)*L_t(x_t). The root posterior is proportional to pi*L_r,
    and each child posterior conditional is proportional to A_t*L_t for fixed parent.
    Propagating the root posterior downward gives node and edge marginals. Replacing
    child sums with maxima and retaining maximizing states yields joint MAP by backtracking;
    independently maximizing node marginals gives MPM and can select a different configuration.
    Exact node and edge posterior expectations permit an EM parameter update for a
    specified, properly normalized tree model. The source instantiates the tree as
    a quadtree, with optional observation levels and optional parameter tying across
    scales. Limitations: The record is scoped to independent child transitions and
    independent site emissions on a fixed finite rooted tree. Coupled siblings, loopy
    graphs, correlated emissions and learned topology require additional constructions.
    A causal tree factorization here expresses conditional probability, not intervention
    semantics. Generic dense transitions with K hidden states require O(number_of_edges*K^2)
    arithmetic for the sum-product pass; linearity in sites assumes a fixed state
    count. Source complexity statements linear in K are not adopted for arbitrary
    dense kernels. Positive evidence and careful support handling are required; numerical
    scaling reduces but does not eliminate all numerical risks. The source’s Equation(10)
    omits the complement needed for a minimized Hamming loss, and Figure4 prints argmin
    where Equation(11) correctly uses argmax of a posterior. Its preliminary prior
    pass requires root-to-leaf order. This record uses consistent sum-product/max-product
    semantics rather than those literal displays. For Equation(17)’s shared same-state
    transition probability theta, the unconstrained EM update is expected same-state
    edge count divided by edge count. Equations(26)–(27) print an extra state-count
    divisor, conflicting with the earlier theta>1/K restriction. Active parameter
    constraints, zero expected counts and emission degeneracy need separate treatment.
    The exact posterior factorization in Equation(29) supports ancestral sampling
    after subtree messages. The experimental H-MCEM uses a local-observation conditioning
    shortcut and constructed coarse observations; those samples are not certified
    exact draws from the original posterior. SMAP is a different loss with an approximate
    procedure, not an alias for exact joint MAP or MPM. Quadtree image priors can
    create location-dependent block artifacts. EM remains initialization-sensitive
    and need not find a global optimum. The selected synthetic, flood and microscopy
    examples establish application context, not universal segmentation superiority,
    a modern benchmark or a reproduced implementation.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: Graphical model family or complete-data estimator iteration; a model
      and its fitting procedure have distinct identities.
    evidence_ids:
    - hiddenmarkovtree-source-0
  - name: aio-assessment
    value: broad_match
    definition: 'HMRF has a related ProbabilisticGraphicalModel mapping because the
      pinned class is defined and parented as a machine-learning task. The independent-emission
      HMT has a broad BayesianNetwork mapping: a rooted hidden tree with emitted observation
      leaves is a restricted normalized directed acyclic probability model, without
      causal-intervention semantics. ICE has a related MachineLearningTask mapping
      for its parameter-learning role; it is an estimator iteration, not a subtype
      of a learning task. SupervisedLearning and UnsupervisedLearning impose contexts
      not required by every ICE application. TrainingStrategy is preprocessing-scoped.
      A generic undirected field does not justify a BayesianNetwork map that preserves
      its graph merely because arbitrary chain-rule conversion is possible. MarkovChain
      requires sequential structure rather than a generic spatial graph or branching
      tree. DecisionTree, HierarchicalClassification and HierarchicalClustering concern
      decisions/grouping rather than latent stochastic topology. HierarchicalLanguageModel,
      EnergyBasedLLM and ImplicitLanguageModel are language-scoped. BoltzmannMachineNetwork,
      RestrictedBoltzmannMachine and HopfieldNetwork add particular neural/state semantics.
      SpatialRegression and RegressionAnalysis are regression-scoped, not generic
      latent-label models or incomplete-data estimators. GaussianNoiseLayer, GaussianDropoutLayer,
      HiddenLayer and ProbabilisticHiddenLayer are neural components. MaximumLayer
      is an elementwise tensor merger, not MAP, EM or ICE. Native MRF, HMM, paired
      field, triplet field, paired tree, EM, HME and HMDT distinguish generic graph
      scope, hidden-observed partition, topology, augmentation, estimator iteration
      and gating. Contextual reading does not renew their scientific approval.'
    evidence_ids:
    - mapping
- assessment_id: iterativeconditionalestimation
  area: evidence
  topic: Identity, definition, mechanism, limitations, evidence version and AIO direction
  outcome: supported
  target_ids:
  - AIMech:IterativeConditionalEstimation
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - iterativeconditionalestimation-source-0
  - iterativeconditionalestimation-source-1
  summary: ICE specifies expectation of an estimator, not maximization of an expected
    complete-data log likelihood as in EM. The estimator may be maximum likelihood,
    least squares or another supported complete-data estimator. Shared applications
    to hidden Markov models do not make ICE a model family, an ICM label optimizer
    or a synonym for every stochastic EM method. Its behavior depends on the selected
    estimator and parameterization. The short acronym is scoped to this estimation
    procedure. No normalized identity match was found across all 442 pinned AIO labels
    and all scoped synonyms and 394 preceding native IDs, names and aliases for these
    three concepts. Full-checkout fixed-string searches included ignored and hidden
    files in worktree and main, yielding 64 and 64 matched lines; all 44 unique contents
    were read. Hits represent neighboring records, citations and discovery leads rather
    than records of these identities. All 97 semantic label/synonym hits were read.
    Twenty-one fully annotated exact CLASS nodes and outgoing edges were verified
    identical to the preceding inspection, and three additional nodes were read. Twenty-eight
    contextual YAMLs were byte-verified after prior full reading and four freshly
    read, totaling 24 generated and eight native contextual records. Short acronyms
    were included in the complete normalized identity comparison. The absence assessment
    is bounded to the pin, native collection and inspected semantic neighborhood.
  details: 'Let observed data be y and hidden data h, and choose a complete-data estimator
    T(h,y) of a parameter theta. From a valid current theta_k, set theta_(k+1)=E_(theta_k)[T(H,y)|Y=y],
    when this expectation exists and remains admissible. A finite hidden space permits
    a posterior-weighted sum; otherwise average T over appropriate posterior samples
    as a Monte Carlo approximation. This average is taken after evaluating the estimator
    on each completed datum. It generally differs from applying a nonlinear estimator
    to expected sufficient statistics. With a complete-data maximum-likelihood estimator,
    ICE averages an argmax, whereas EM takes an argmax after averaging the log likelihood.
    For a regular full identifiable exponential family with a valid finite interior
    complete-data MLE and an invertible mean-parameter map, the expectation coordinate
    psi=E_theta[s(H,Y)] has complete-data estimator s(H,Y), so ICE and EM coincide
    in that coordinate. Nonlinear reparameterization need not preserve equality of
    their updates. Limitations: The complete-data estimator must be defined on posterior-supported
    completed data and have the required moments. Empty mixture components, boundary
    or infinite MLEs, constrained parameter spaces and nonidentifiability need explicit
    conventions; a conditional mean can leave a nonconvex parameter space. Conditional
    expectation is the least-squares approximation to an integrable squared-error
    target under a fixed law. That fact does not prove decreasing true parameter error,
    observed-likelihood monotonicity or global convergence across ICE iterations with
    changing laws. The Delmas equivalence uses the mean/expectation parameter psi,
    although the source calls it canonical; its natural parameter phi is distinct.
    The claim is not automatic for arbitrary coordinates, curved/constrained exponential
    families or boundary estimates. A nonlinear transformation does not generally
    commute with conditional expectation. For Gaussian mixtures, expectation of a
    complete-data class mean or variance containing a random class count differs in
    general from a ratio of expected sufficient statistics. The usual Gaussian-parameter
    ICE update therefore cannot simply be replaced by an EM update without checking
    the conditions. Monte Carlo approximation requires valid posterior sampling and
    appropriate convergence conditions. Correlated Gibbs samples, finite sample counts
    and apparently steady parameters do not by themselves certify exact expectations
    or convergence. A one-sample version can resemble stochastic EM for a specific
    complete-data estimator; it is not every stochastic-approximation EM algorithm.
    The inspected examples in Delmas contain scaling/covariance notation issues, and
    its introductory suggestion that mixed discrete-continuous data make likelihood
    irrelevant is not adopted. The definition and qualified coordinate comparison
    do not certify all printed example formulas. Neither inspected paper provides
    a universal empirical performance guarantee; no fitting, benchmark or author-code
    run was performed.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: Graphical model family or complete-data estimator iteration; a model
      and its fitting procedure have distinct identities.
    evidence_ids:
    - iterativeconditionalestimation-source-0
    - iterativeconditionalestimation-source-1
  - name: aio-assessment
    value: related_match
    definition: 'HMRF has a related ProbabilisticGraphicalModel mapping because the
      pinned class is defined and parented as a machine-learning task. The independent-emission
      HMT has a broad BayesianNetwork mapping: a rooted hidden tree with emitted observation
      leaves is a restricted normalized directed acyclic probability model, without
      causal-intervention semantics. ICE has a related MachineLearningTask mapping
      for its parameter-learning role; it is an estimator iteration, not a subtype
      of a learning task. SupervisedLearning and UnsupervisedLearning impose contexts
      not required by every ICE application. TrainingStrategy is preprocessing-scoped.
      A generic undirected field does not justify a BayesianNetwork map that preserves
      its graph merely because arbitrary chain-rule conversion is possible. MarkovChain
      requires sequential structure rather than a generic spatial graph or branching
      tree. DecisionTree, HierarchicalClassification and HierarchicalClustering concern
      decisions/grouping rather than latent stochastic topology. HierarchicalLanguageModel,
      EnergyBasedLLM and ImplicitLanguageModel are language-scoped. BoltzmannMachineNetwork,
      RestrictedBoltzmannMachine and HopfieldNetwork add particular neural/state semantics.
      SpatialRegression and RegressionAnalysis are regression-scoped, not generic
      latent-label models or incomplete-data estimators. GaussianNoiseLayer, GaussianDropoutLayer,
      HiddenLayer and ProbabilisticHiddenLayer are neural components. MaximumLayer
      is an elementwise tensor merger, not MAP, EM or ICE. Native MRF, HMM, paired
      field, triplet field, paired tree, EM, HME and HMDT distinguish generic graph
      scope, hidden-observed partition, topology, augmentation, estimator iteration
      and gating. Contextual reading does not renew their scientific approval.'
    evidence_ids:
    - mapping
- assessment_id: hidden-field-boundary
  area: consistency
  topic: Latent field identity versus approximate fitting
  outcome: supported
  target_ids:
  - AIMech:HiddenMarkovRandomField
  evidence_ids:
  - hiddenmarkovrandomfield-source-0
  - finite-conventions
  - neighbors
  summary: Retain the classical hidden-field model.
  details: A Gibbs label prior with independent site emissions defines a proper latent
    graphical model. The local conditional graph is preserved after conditioning on
    observations, but a local conditional with fixed estimated neighbors is not a
    full posterior marginal; the finite cycle gives0.8 versus0.7197232667. The reported
    ICM/EM loop is approximate and is not an intrinsic model definition. Gaussian-sign
    and MAP-sum displays are explicitly qualified. The report version is not conflated
    with the2001journal article. The definition was clarified and an unnecessary uncited
    MPM-risk sentence removed before this formal inspection.
- assessment_id: hidden-tree-boundary
  area: consistency
  topic: Independent-emission tree model and inference objectives
  outcome: supported
  target_ids:
  - AIMech:HiddenMarkovTree
  evidence_ids:
  - hiddenmarkovtree-source-0
  - finite-conventions
  - neighbors
  summary: Retain the explicitly scoped hidden-tree identity.
  details: Independent child transitions and site emissions are the supported classical
    construction. The record acknowledges broader hidden-tree terminology in pairwise-tree
    literature rather than treating correlated-emission variants as equivalent. Sum-product
    node/edge marginals and max-product backtracking agree with complete enumeration,
    while MPM differs from joint MAP in the original finite example. Printed Hamming-loss/argmin
    and shared-transition denominator errors are not adopted. Exact posterior ancestral
    sampling is distinguished from the experimental local-observation shortcut. Quadtree
    artifacts and local fitting limits remain explicit.
- assessment_id: ice-boundary
  area: consistency
  topic: Estimator expectations, EM and nonlinear coordinates
  outcome: supported
  target_ids:
  - AIMech:IterativeConditionalEstimation
  evidence_ids:
  - iterativeconditionalestimation-source-0
  - iterativeconditionalestimation-source-1
  - finite-conventions
  - neighbors
  summary: Retain ICE as a distinct algorithm.
  details: ICE averages a specified complete-data estimator under the current conditional
    hidden-data law; EM optimizes expected complete log likelihood. Their agreement
    in a regular full family’s mean coordinates has estimator existence, admissibility
    and invertibility conditions. A finite Bernoulli example gives p-update.7 for
    both but squared-coordinate updates.55 for ICE and.49 for EM, so nonlinear coordinate
    equality is not assumed. Random-count ratios and finite sampling require separate
    handling. The scanned source was visually read with checked method OCR; original1990precedence
    and later convergence literature are not falsely claimed inspected.
- assessment_id: mapping-boundary
  area: grounding
  topic: Directional AIO mappings and neighboring concepts
  outcome: supported
  target_ids:
  - AIMech:HiddenMarkovRandomField
  - AIMech:HiddenMarkovTree
  - AIMech:IterativeConditionalEstimation
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain all three native identities with qualified mapping directions.
  details: 'HMRF has a related ProbabilisticGraphicalModel mapping because the pinned
    class is defined and parented as a machine-learning task. The independent-emission
    HMT has a broad BayesianNetwork mapping: a rooted hidden tree with emitted observation
    leaves is a restricted normalized directed acyclic probability model, without
    causal-intervention semantics. ICE has a related MachineLearningTask mapping for
    its parameter-learning role; it is an estimator iteration, not a subtype of a
    learning task. SupervisedLearning and UnsupervisedLearning impose contexts not
    required by every ICE application. TrainingStrategy is preprocessing-scoped. A
    generic undirected field does not justify a BayesianNetwork map that preserves
    its graph merely because arbitrary chain-rule conversion is possible. MarkovChain
    requires sequential structure rather than a generic spatial graph or branching
    tree. DecisionTree, HierarchicalClassification and HierarchicalClustering concern
    decisions/grouping rather than latent stochastic topology. HierarchicalLanguageModel,
    EnergyBasedLLM and ImplicitLanguageModel are language-scoped. BoltzmannMachineNetwork,
    RestrictedBoltzmannMachine and HopfieldNetwork add particular neural/state semantics.
    SpatialRegression and RegressionAnalysis are regression-scoped, not generic latent-label
    models or incomplete-data estimators. GaussianNoiseLayer, GaussianDropoutLayer,
    HiddenLayer and ProbabilisticHiddenLayer are neural components. MaximumLayer is
    an elementwise tensor merger, not MAP, EM or ICE. Native MRF, HMM, paired field,
    triplet field, paired tree, EM, HME and HMDT distinguish generic graph scope,
    hidden-observed partition, topology, augmentation, estimator iteration and gating.
    Contextual reading does not renew their scientific approval.'
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:HiddenMarkovRandomField
  - AIMech:HiddenMarkovTree
  - AIMech:IterativeConditionalEstimation
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - hiddenmarkovrandomfield-source-0
  - hiddenmarkovtree-source-0
  - iterativeconditionalestimation-source-0
  - iterativeconditionalestimation-source-1
  rationale: HMRF imposes local latent-field dependencies and independent site observations;
    HMT restricts hidden topology to a rooted tree with independent child transitions;
    ICE specifies a conditional-estimator update applicable to incomplete-data models.
    Structural special cases and shared applications do not make a general spatial
    model, a tree specialization and a fitting procedure equivalent. Preserve their
    local IDs and explicit AIO mappings.
limitations:
- Adversarial author self-review only; all three records remain DRAFT.
- TR00YZ1 was read as an Oxford technical report, not the later journal article. Its
  printed errors and approximate fitting procedure are qualified.
- The quadtree source has formula and algorithm-display inconsistencies; consistent
  normalized model/inference identities are supported, but experimental H-MCEM is
  not certified exact posterior sampling.
- ICE/EM agreement is stated only with its coordinate and regularity restrictions.
  Delmas DOI access failed; exact PDF identity is supported by printed metadata and
  the author-hosted copy, without asserting independently verified DOI metadata.
- The scanned1992paper was fully viewed, with OCR method pages checked visually; garbled
  extraction was not treated as evidence of absence.
- Original finite calculations are not author-code reproduction, training, benchmarking
  or general convergence proofs.
- 225 pending leads and unresolved dispositions remain; discovery continues.
links: []
tags:
- native-concepts
- hidden-fields-trees-ice
- self-review
- discovery-ongoing
```
