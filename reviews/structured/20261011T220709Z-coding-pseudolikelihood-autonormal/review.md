# Scientific self-review of coding likelihood, pseudolikelihood and proper auto-normal fields

- Review: 20261011T220709Z-coding-pseudolikelihood-autonormal
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T22:06:16Z
- Finished UTC: 2026-10-11T22:07:09Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain two DRAFT parameter-estimation algorithms and one DRAFT proper finite Gaussian field family. Conditional-objective definitions, admissible parameter domains, weighted compatibility and directional mappings are supported with explicit source and asymptotic limitations. No actionable curation finding remains in this selected batch.

## Scope And Provenance

All fields of three selected maintained concepts for independent-site coding estimation, full-conditional pseudolikelihood estimation and proper finite auto-normal modeling.

Selection: Exact maintained IDs MaximumPseudolikelihoodEstimation, MaximumCodingLikelihoodEstimation and AutoNormalMarkovRandomField; complete selected batch without sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base ebdfeccba2d224d7d1637e3f4d1caca9fb14cd4c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:MaximumPseudolikelihoodEstimation | data/curated/MaximumPseudolikelihoodEstimation.yaml | maintained | Maximum pseudolikelihood estimation |
| AIMech:MaximumCodingLikelihoodEstimation | data/curated/MaximumCodingLikelihoodEstimation.yaml | maintained | Maximum coding likelihood estimation |
| AIMech:AutoNormalMarkovRandomField | data/curated/AutoNormalMarkovRandomField.yaml | maintained | Auto-normal Markov random field |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:MaximumPseudolikelihoodEstimation, AIMech:MaximumCodingLikelihoodEstimation, AIMech:AutoNormalMarkovRandomField | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 81.25s (0:01:21)<br>Checked 442 record(s); 0 failed.<br>Checked 403 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 115 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 112,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:MaximumPseudolikelihoodEstimation, AIMech:MaximumCodingLikelihoodEstimation, AIMech:AutoNormalMarkovRandomField | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:MaximumPseudolikelihoodEstimation, AIMech:MaximumCodingLikelihoodEstimation, AIMech:AutoNormalMarkovRandomField | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:MaximumPseudolikelihoodEstimation, AIMech:MaximumCodingLikelihoodEstimation, AIMech:AutoNormalMarkovRandomField | Command exited 0 with no output. |
| Binary conditional objectives and Gaussian compatibility calculations | passed | True | AIMech:MaximumPseudolikelihoodEstimation, AIMech:MaximumCodingLikelihoodEstimation, AIMech:AutoNormalMarkovRandomField | {"binary": {"pseudolikelihood_total_mass_at_lambda_2": "13/10", "observed": [1, 1, 1, 0], "parameter_grid": ["1", "3/2", "2", "21/10", "9/4", "3"], "joint_likelihood_maximizer": "2", "pseudolikelihood_maximizer": "21/10", "coding_maximizers": ["3", "3/2"], "arithmetic_mean_of_coding_maximizers": "9/4", "scores": {"1": ["1/16", "1/16", "1/4", "1/4"], "3/2": ["9/125", "27/325", "3/10", "18/65"], "2": ["2/27", "4/45", "1/3", "4/15"], "21/10": ["2205/29791", "46305/519901", "21/62", "4410/16771"], "9/4": ["162/2197", "1458/16393", "9/26", "324/1261"], "3": ["9/128", "27/320", "3/8", "9/40"]}}, "gaussian": {"precision": [["2", "-1", "0"], ["-1", "3", "-1"], ["0", "-1", "2"]], "covariance": [["5/8", "1/4", "1/8"], ["1/4", "1/2", "1/4"], ["1/8", "1/4", "5/8"]], "conditional_variances": ["1/2", "1/3", "1/2"], "conditional_coefficients": [["0", "1/2", "0"], ["1/3", "0", "1/3"], ["0", "1/2", "0"]], "marginal_covariance_0_2": "1/8", "conditional_covariance_0_2_given_1": "0", "same_coefficient_sar_precision": [["7/3", "-2", "1/3"], ["-2", "4", "-2"], ["1/3", "-2", "7/3"]], "joint_quadratic": "19", "pseudolikelihood_quadratic": "29", "gaussian_pseudolikelihood_total_mass": "3/2", "invalid_precision_determinant": "-7/25", "invalid_precision_quadratic_witness": "-2/5", "intrinsic_precision_determinant": "0"}} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, limitations, evidence version and AIO direction

evidence: supported. Targets: AIMech:MaximumPseudolikelihoodEstimation.

The classical full-conditional pseudolikelihood uses every observed site. It is an estimation objective and does not specify a unique numerical optimizer. It is distinct from full joint maximum likelihood, independent-site coding likelihood, iterative conditional modes for state optimization, and iterative conditional estimation for incomplete-data parameters. A general loss assembled from unrelated conditionals is not automatically the pseudolikelihood of a compatible joint model. The paper discusses fixed-site spatial models without assuming stationarity or homogeneity; the local graph and parameterization must still be specified. No normalized identity match was found across all 442 pinned AIO labels and all scoped synonyms and 400 preceding native IDs, names and aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, yielding 35 and 35 matched lines; all 23 unique contents were read. Hits are citations, contextual statements and discovery leads rather than records of these identities. All 182 semantic label/synonym hits were read. Thirty-one fully annotated exact CLASS nodes and outgoing edges were inspected: 23 byte-equivalent to prior inspected nodes and eight freshly read. Thirty-nine contextual YAMLs comprise 31 generated and eight native records: 29 byte-verified after prior reading and 10 freshly read. Short acronyms were included in the normalized identity comparison. Absence is bounded to the pinned snapshot, maintained corpus and inspected semantic neighborhood.

For an observed configuration x and a compatible family p_theta with well-defined full conditionals, form PL(theta;x)=product_i p_theta(x_i&#124;x_(-i)) and maximize sum_i log p_theta(x_i&#124;x_(-i)) over the admissible parameter space. In a Markov field, each factor depends only on the site’s neighbors; a global joint partition function cancels from that factor, although its local normalizer still must be evaluated. If the sites are partitioned into nonneighbor coding sets, the log pseudolikelihood is the sum of their conditional log likelihoods. This identity combines objectives, not the separately fitted parameter values. For the source’s proper common-conditional-variance Gaussian model with mean D*a, symmetric B=I-phi*H and variance sigma^2, the residual term is (x-D*a)^T B^2(x-D*a)/sigma^2. Its joint Gaussian likelihood instead includes log&#124;B&#124; and a single-B quadratic. Complete independence is a special case in which the product of full conditionals equals the joint likelihood. Limitations: The product of normalized full conditionals is generally not a normalized joint distribution over x. Its maximizer need not equal the joint-likelihood maximizer. Dividing that product by a parameter-dependent joint normalizer changes the objective. Conditionals must be compatible with the intended joint model and parameters must lie in its valid domain. Optimizing local expressions without these restrictions can produce inadmissible joint parameters. Gaussian variance positivity and precision positive definiteness remain necessary. The source gives a consistency sketch for an infinite bounded-degree site system with growing coding classes and additional regularity and boundary conditions. It is not a universal theorem for arbitrary growing graphs, fixed finite samples, misspecified models or every parameterization. Efficiency, uncertainty estimates and likelihood-ratio calibration do not automatically follow ordinary independent-sample likelihood formulas. Strong dependence, limited information, boundaries and model mismatch require separate assessment; the source offers no universal efficiency advantage. Gaussian least-squares expressions apply to the stated common-variance and compatible symmetric interaction parameterization. Design inverses, ratio denominators, finite maximizers and nonzero residual variance require checks. Alternating algebraic updates are not a proof of a global optimum. A partition into coding sets does not make the corresponding estimators or test statistics independent. The pseudolikelihood maximizer is not generally the arithmetic mean of coding-set maximizers. Original finite objective comparisons demonstrate this distinction; no empirical fitting, author code or benchmark was run.

### Identity, definition, mechanism, limitations, evidence version and AIO direction

evidence: supported. Targets: AIMech:MaximumCodingLikelihoodEstimation.

This record uses the classical independent-site coding method of Besag. Coding selects a graph-independent subset; it does not encode features, compress data or learn sparse representations. Shifted or alternative coding sets can give additional dependent estimates. Extensions using conditionally dependent blocks require their joint conditional likelihoods rather than this independent-singleton product. The method is distinct from multiplying all site conditionals as pseudolikelihood and from state updates in ICM or Gibbs sampling. No normalized identity match was found across all 442 pinned AIO labels and all scoped synonyms and 400 preceding native IDs, names and aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, yielding 35 and 35 matched lines; all 23 unique contents were read. Hits are citations, contextual statements and discovery leads rather than records of these identities. All 182 semantic label/synonym hits were read. Thirty-one fully annotated exact CLASS nodes and outgoing edges were inspected: 23 byte-equivalent to prior inspected nodes and eight freshly read. Thirty-nine contextual YAMLs comprise 31 generated and eight native records: 29 byte-verified after prior reading and 10 freshly read. Short acronyms were included in the normalized identity comparison. Absence is bounded to the pinned snapshot, maintained corpus and inspected semantic neighborhood.

For a compatible positive Markov-field model with observed configuration x, choose a nonempty set S containing no neighboring pair and let C be its complement. Conditional on X_C=x_C, the variables in S are mutually independent, so L_S(theta;x_S&#124;x_C)=product_(i in S) p_theta(x_i&#124;x_(-i)). Maximize its log over valid theta. The complement supplies conditioning values even though its own site likelihood factors are omitted. A rectangular four-neighbor graph admits checkerboard coding; adding diagonal interactions requires another independent-set design, such as the source’s four shifted patterns. Changing the selected set changes the conditional likelihood. The full-site pseudolikelihood equals the product of coding likelihoods for a partition into independent sets, but maximizing that product differs in general from averaging separately fitted parameters. Limitations: The factorization needs a valid graph and the stated joint conditional-independence property. It is not justified by spatial distance alone or by arbitrary, incompatible local distributions. Hard support constraints require separate treatment beyond the positive-model construction. Choosing a large independent set need not yield a unique selection or the most informative estimator. Conditioning omits some likelihood information while retaining the complement as covariates; it does not literally discard all white-site observations. Estimates and tests from shifted coding patterns reuse the same configuration and are generally dependent. Combining them requires a justified procedure; neither naive independent-test calibration nor an arithmetic average of estimates is automatically optimal. Conditional likelihood-ratio comparisons require comparable selected dependent sites and conditioning sets. The source warns against comparing fits based on different codings as if they were the same likelihood. Ordinary asymptotic approximations still require identifiability, information and regularity conditions. The source’s unconstrained coding estimates can violate the intended joint-model parameter restrictions. A conditional objective may be finite where the full Gaussian field is invalid, so the parameter domain must be enforced. Averaging happened to yield admissible values in some reported examples and is not a general repair. The inspected plant and wheat data illustrate estimation and model diagnostics, while exposing model inadequacy and aggregation effects. They do not prove general efficiency or spatial prediction accuracy. No empirical data fitting, author implementation or benchmark was reproduced.

### Identity, definition, mechanism, limitations, evidence version and AIO direction

evidence: supported. Targets: AIMech:AutoNormalMarkovRandomField.

The record is scoped to the proper finite auto-normal construction. It is a Gaussian conditional-autoregressive representation of a multivariate normal law with a specified conditional-dependence graph. Intrinsic improper Gaussian fields and infinite-lattice extensions require separate existence or constraint conditions and are not exact aliases here. Spatial conditional autoregression is not temporal autoregression and is not the simultaneous autoregressive model obtained by treating the same local residual equations as independent noise equations. Gaussian-process regression conditions a process prior on training observations for prediction; this record specifies the finite graphical joint law itself. It can be used as a prior but does not inherently introduce hidden labels or independent observation emissions. No normalized identity match was found across all 442 pinned AIO labels and all scoped synonyms and 400 preceding native IDs, names and aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, yielding 35 and 35 matched lines; all 23 unique contents were read. Hits are citations, contextual statements and discovery leads rather than records of these identities. All 182 semantic label/synonym hits were read. Thirty-one fully annotated exact CLASS nodes and outgoing edges were inspected: 23 byte-equivalent to prior inspected nodes and eight freshly read. Thirty-nine contextual YAMLs comprise 31 generated and eight native records: 29 byte-verified after prior reading and 10 freshly read. Short acronyms were included in the normalized identity comparison. Absence is bounded to the pinned snapshot, maintained corpus and inspected semantic neighborhood.

For site i, specify X_i given all other sites as normal with mean mu_i+sum_(j!=i) beta_ij*(x_j-mu_j) and variance v_i&gt;0 independent of the conditioning values. Let B have diagonal 1 and off-diagonal -beta_ij, and let Lambda=diag(v_i). These conditionals define the proper finite joint model when Q=Lambda^(-1)*B is symmetric positive definite. Symmetry requires beta_ij*v_j=beta_ji*v_i. The joint law is N(mu,Q^(-1)), with density proportional to &#124;Q&#124;^(1/2)*exp[-(x-mu)^T Q(x-mu)/2]. A zero off-diagonal precision entry denotes conditional independence given the other sites; marginal covariance need not vanish. With common v_i=sigma^2, compatibility reduces to symmetric positive-definite B and covariance sigma^2*B^(-1). In contrast, the simultaneous equations B*(X-mu)=epsilon with independent epsilon~N(0,Lambda) imply covariance B^(-1)*Lambda*B^(-T) and precision B^T*Lambda^(-1)*B. For the proper conditional model, a factorization Q=C^T*C allows exact Gaussian sampling as mu+C^(-1)*z with independent standard-normal z. Limitations: Every site conditional can be individually normalized while the proposed collection fails to define a proper joint law. Weighted symmetry and positive definiteness must both hold. With unequal conditional variances, raw beta coefficients need not be symmetric. A singular precision can describe an intrinsic improper construction only with additional interpretation or constraints; it is not the ordinary normalized Gaussian density stated here. An indefinite precision gives a nonintegrable quadratic model. Positive diagonal entries alone are insufficient. Finite-graph eigenvalue bounds depend on the actual graph and boundary conditions. Infinite-lattice stationarity criteria are not automatically necessary finite-graph conditions. The source’s stationary or homogeneous examples do not require every finite auto-normal model to share those assumptions. Missing precision edges encode conditional independence, not marginal independence or causal effects. A sparse simultaneous-equation matrix can induce additional precision edges. Unconstrained conditional least-squares, coding-likelihood or pseudolikelihood estimates may leave the proper joint parameter domain. The Gaussian fitting objective and parameter identifiability depend on the specified mean, graph and interaction parameterization; existence of a covariance representation does not ensure identifiable scientific parameters. The source’s wheat and plant examples expose aggregation, nonstationarity and model-fit concerns; a fitted Gaussian field does not establish a causal spatial mechanism or universal predictive adequacy. The record does not certify source implementations, empirical fits or infinite-system convergence.

### Full-conditional estimation objective versus joint likelihood

consistency: supported. Targets: AIMech:MaximumPseudolikelihoodEstimation.

Retain maximum pseudolikelihood estimation as a distinct algorithm.

The 1975 Section 3.3 objective multiplies every site full conditional of a compatible joint family. A global partition function cancels within a conditional, but local normalization and the valid joint parameter domain remain necessary. Coding partitions decompose the log objective; they do not imply averaging separately fitted estimates. Exact binary enumeration yields total pseudolikelihood mass 13/10 and different joint, pseudo and coding maximizers on the explicitly declared finite grid. Independent sites recover the joint law. Gaussian pseudolikelihood uses the B-squared residual objective, while the joint likelihood has a B quadratic and determinant term. The source consistency argument is a qualified infinite bounded-degree sketch, not a universal finite-sample guarantee.

### Independent-site conditional likelihood and admissible estimation

consistency: supported. Targets: AIMech:MaximumCodingLikelihoodEstimation.

Retain maximum coding likelihood estimation as a distinct algorithm.

An independent set is conditionally mutually independent given its complement under the stated positive compatible Markov law. The finite binary check verifies the factorization and conditional normalization for every state and every complement configuration. Complement observations remain conditioning values. Shifted coding estimates and tests reuse observations and are generally dependent. Comparisons require the same response and conditioning variables, with regularity for asymptotic likelihood tests. The 1974 wheat example exhibits inadmissible unconstrained fits; neither averaging nor finite conditional likelihood repairs general joint invalidity. Dependent-chain extensions need their own joint conditional factors and remain a separate research lead.

### Proper finite full-conditional Gaussian model versus simultaneous or intrinsic constructions

consistency: supported. Targets: AIMech:AutoNormalMarkovRandomField.

Retain the proper finite auto-normal model family.

The unequal-variance compatibility condition is beta_ij*v_j=beta_ji*v_i, so raw coefficients may be asymmetric. Q=Lambda^-1 B must be symmetric positive definite. Finite calculations verify the conditional coefficients, covariance, conditional versus marginal independence, and the distinct same-coefficient SAR precision B^T Lambda^-1 B. Positive one-site variances coexist with a nonintegrable indefinite quadratic or an improper singular Laplacian, so they do not establish a proper joint density. Cholesky simulation uses the specified orientation Q=C^T C. Finite and infinite parameter bounds, scientific parameter identification and observed empirical fit remain separate questions. Gaussian-process regression, hidden-label fields, temporal autoregression and Gaussian neural-network layers are neighboring but distinct identities.

### Directional AIO mappings and neighboring identities

grounding: supported. Targets: AIMech:MaximumPseudolikelihoodEstimation, AIMech:MaximumCodingLikelihoodEstimation, AIMech:AutoNormalMarkovRandomField.

Retain all three native identities with scoped AIO mappings.

MPLE and independent-site coding likelihood map related to ProbabilisticGraphicalModel for parameter estimation using compatible graph conditionals; the pinned class is task-scoped, not an algorithm superclass. The proper finite auto-normal family maps broad to Model and related to ProbabilisticGraphicalModel. MachineLearningTask is more generic and does not distinguish the objectives. TrainingStrategy is preprocessing-scoped; supervised or unsupervised contexts are not imposed as intrinsic identities. SpatialRegression, RegressionAnalysis, GeneralizedLinearModel, LinearRegression and LogisticRegression describe regression tasks or model contexts, not these particular estimation objectives or every Gaussian joint field. A local regression formula does not equate a compatible joint spatial law with an exogenous regression task. MarkovChain, AutoregressiveMovingAverage and VectorAutoregression require temporal/sequential structure absent from a general spatial graph. BayesianNetwork and CausalGraphicalModel do not preserve the same undirected graph by arbitrary factorization or imply causal interventions. AutoregressiveLanguageModel, EnergyBasedLLM and ImplicitLanguageModel are language-scoped. AutoEncoderNetwork, DenoisingAutoEncoder, SparseAutoEncoder and VariationalAutoEncoder denote neural architectures rather than auto-normal fields. SparseLearning refers to sparse dictionary representations, and CategoryEncodingLayer to feature encoding; neither is graph-independent-set coding likelihood. Normalization changes data scale rather than certifying a joint probability normalizer. GaussianNoiseLayer, GaussianDropoutLayer, HiddenLayer and ProbabilisticHiddenLayer are neural components. MaximumLayer is an elementwise tensor operation, not likelihood optimization. Native MRF, HMRF, HMT, EM, ICE, ICM, Gibbs sampling and Gaussian-process regression distinguish joint field, latent/observed partition, topology, parameter estimation, state optimization, sampling and predictive process conditioning. Contextual reading does not renew their scientific approval.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:MaximumPseudolikelihoodEstimation, AIMech:MaximumCodingLikelihoodEstimation, AIMech:AutoNormalMarkovRandomField. Independent-site coding is a normalized conditional likelihood given the complement; full-site pseudolikelihood multiplies overlapping conditionals and is generally not a joint density; the proper auto-normal construction defines a Gaussian joint model that either estimator could fit under validity constraints. Sharing a Markov-field application does not make the model and estimation objectives equivalent. Preserve local identities and directional AIO mappings.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T220306Z-coding-pseudolikelihood-autonormal.json | supports | No normalized identity match was found across all 442 pinned AIO labels and all scoped synonyms and 400 preceding native IDs, names and aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, yielding 35 and 35 matched lines; all 23 unique contents were read. Hits are citations, contextual statements and discovery leads rather than records of these identities. All 182 semantic label/synonym hits were read. Thirty-one fully annotated exact CLASS nodes and outgoing edges were inspected: 23 byte-equivalent to prior inspected nodes and eight freshly read. Thirty-nine contextual YAMLs comprise 31 generated and eight native records: 29 byte-verified after prior reading and 10 freshly read. Short acronyms were included in the normalized identity comparison. Absence is bounded to the pinned snapshot, maintained corpus and inspected semantic neighborhood. |
| mapping | sources/aio/aio.json; 31 exact CLASS nodes and outgoing edges, and 182 semantic label/synonym hits in source_analysis.aio_mapping_inspection | supports | MPLE and independent-site coding likelihood map related to ProbabilisticGraphicalModel for parameter estimation using compatible graph conditionals; the pinned class is task-scoped, not an algorithm superclass. The proper finite auto-normal family maps broad to Model and related to ProbabilisticGraphicalModel. MachineLearningTask is more generic and does not distinguish the objectives. TrainingStrategy is preprocessing-scoped; supervised or unsupervised contexts are not imposed as intrinsic identities. SpatialRegression, RegressionAnalysis, GeneralizedLinearModel, LinearRegression and LogisticRegression describe regression tasks or model contexts, not these particular estimation objectives or every Gaussian joint field. A local regression formula does not equate a compatible joint spatial law with an exogenous regression task. MarkovChain, AutoregressiveMovingAverage and VectorAutoregression require temporal/sequential structure absent from a general spatial graph. BayesianNetwork and CausalGraphicalModel do not preserve the same undirected graph by arbitrary factorization or imply causal interventions. AutoregressiveLanguageModel, EnergyBasedLLM and ImplicitLanguageModel are language-scoped. AutoEncoderNetwork, DenoisingAutoEncoder, SparseAutoEncoder and VariationalAutoEncoder denote neural architectures rather than auto-normal fields. SparseLearning refers to sparse dictionary representations, and CategoryEncodingLayer to feature encoding; neither is graph-independent-set coding likelihood. Normalization changes data scale rather than certifying a joint probability normalizer. GaussianNoiseLayer, GaussianDropoutLayer, HiddenLayer and ProbabilisticHiddenLayer are neural components. MaximumLayer is an elementwise tensor operation, not likelihood optimization. Native MRF, HMRF, HMT, EM, ICE, ICM, Gibbs sampling and Gaussian-process regression distinguish joint field, latent/observed partition, topology, parameter estimation, state optimization, sampling and predictive process conditioning. Contextual reading does not renew their scientific approval. |
| neighbors | research/discovery/20261011T220306Z-coding-pseudolikelihood-autonormal.json; source_analysis.aio_mapping_inspection.native_neighbors and context_reading | supports | Eight complete native contextual records read or byte-verified after prior full reading: MRF, HMRF, HMT, EM, ICE, ICM, Gibbs sampling and Gaussian-process regression. These distinguish graphical distributions, latent-state observation models, parameter estimators, conditional state optimizers, samplers and process-prior regression. Context reading does not renew scientific approval of these earlier records. |
| finite-boundaries | research/discovery/coding-pseudolikelihood-autonormal-boundaries.py; Exact four-site binary-path conditional objectives and finite parameter grid; three-site Gaussian precision, covariance, conditional and simultaneous equations | supports | Original exact finite calculations enumerate all16states of a four-site binary path with edge-agreement weight lambda. At lambda2, the joint law normalizes and both independent-site coding products equal their exact joint conditionals for every state and complement configuration. The product of all full conditionals instead sums to13/10 over configurations. For fixed observation1110 and parameter grid{1,3/2,2,21/10,9/4,3}, joint likelihood is maximized at2, pseudolikelihood at21/10, and the two coding likelihoods at3 and3/2. Their arithmetic mean9/4 is not the pseudolikelihood maximizer. The independent lambda1case recovers the joint law. For Gaussian precision[[2,-1,0],[-1,3,-1],[0,-1,2]], exact inverse covariance has marginal endpoint covariance1/8 but zero endpoint covariance conditional on the middle site. Conditional variances1/2,1/3,1/2 imply asymmetric raw neighbor coefficients that satisfy variance-weighted compatibility. The same B and Lambda in simultaneous independent-noise equations induce endpoint precision1/3 instead of0. At x=(1,-1,2), joint and pseudo quadratics are19 and29; the Gaussian conditional-product density integrates to3/2, not1. A positive-diagonal incompatible precision has determinant-7/25 and quadratic witness-2/5; a graph-Laplacian precision is singular with a flat constant direction. These are exact mathematical objective comparisons on declared synthetic configurations, not empirical fitting, author-code reproduction, benchmarks or general consistency proofs. |
| maximumpseudolikelihoodestimation-source-0 | https://www2.stat.duke.edu/~sschmid/Courses/Stat376/Papers/GibbsFieldEst/BesagPseudoLik1975.pdf; Sections 3.1–3.4, printed pp. 188–193 / PDF pp. 11–16; especially Section 3.3, pp. 190–192 / PDF pp. 13–15, Equations (3.2)–(3.10) and consistency sketch | supports | Statistical Analysis of Non-Lattice Data. The Statistician 24(3):179–195, September 1975; university-hosted 18-page scan including JSTOR wrapper. All 18 pages visually read, including all equations and references. Printed page=PDF page+177. Publisher metadata corroborates title, author, pages, date and DOI. No full extracted-text or OCR reading is asserted. All cited method pages were visually read. The source-analysis notes distinguish main-paper support, discussion context, source restrictions and access/extraction limitations. |
| maximumcodinglikelihoodestimation-source-0 | https://www2.stat.duke.edu/~sschmid/Courses/Stat376/Papers/GibbsFieldEst/BesagPseudoLik1975.pdf; Section 3.2, printed pp. 189–190 / PDF pp. 12–13, Equation (3.1); Section 3.3, p. 192 / PDF p. 15, coding-class decomposition | supports | Statistical Analysis of Non-Lattice Data. The Statistician 24(3):179–195, September 1975; university-hosted 18-page scan including JSTOR wrapper. All 18 pages visually read, including all equations and references. Printed page=PDF page+177. Publisher metadata corroborates title, author, pages, date and DOI. No full extracted-text or OCR reading is asserted. All cited method pages were visually read. The source-analysis notes distinguish main-paper support, discussion context, source restrictions and access/extraction limitations. |
| maximumcodinglikelihoodestimation-source-1 | https://www.stat.cmu.edu/~brian/720-2007-source/nice%20materials/besag-74-contains-hammersley-clifford.pdf; Section 6.1, printed pp. 211–212 / PDF pp. 21–22, Figures 1–2 and likelihood comparability; Section 7.2.4 and conclusion, pp. 222–223 / PDF pp. 32–33, inadmissible fits and model limitations | supports | Spatial Interaction and the Statistical Analysis of Lattice Systems. Journal of the Royal Statistical Society, Series B 36(2):192–225, 1974. The university-hosted 46-page scan includes a JSTOR cover and separately published discussion on pp. 225–236. All 46 pages visually read, including two main figures, 16 tables, discussion figure, references and author reply. Printed page=PDF page+190. The main-paper DOI identifies the cited method sections; discussion has DOI 10.1111/j.2517-6161.1974.tb01000.x. A later online date is not the original publication date. All cited method pages were visually read. The source-analysis notes distinguish main-paper support, discussion context, source restrictions and access/extraction limitations. |
| autonormalmarkovrandomfield-source-0 | https://www2.stat.duke.edu/~sschmid/Courses/Stat376/Papers/GibbsFieldEst/BesagPseudoLik1975.pdf; Sections 2.1–2.5, printed pp. 182–188 / PDF pp. 5–11, especially Equations (2.1)–(2.6) and precision-factor simulation; Section 3.4, p. 193 / PDF p. 16, joint Gaussian likelihood | supports | Statistical Analysis of Non-Lattice Data. The Statistician 24(3):179–195, September 1975; university-hosted 18-page scan including JSTOR wrapper. All 18 pages visually read, including all equations and references. Printed page=PDF page+177. Publisher metadata corroborates title, author, pages, date and DOI. No full extracted-text or OCR reading is asserted. All cited method pages were visually read. The source-analysis notes distinguish main-paper support, discussion context, source restrictions and access/extraction limitations. |
| autonormalmarkovrandomfield-source-1 | https://www.stat.cmu.edu/~brian/720-2007-source/nice%20materials/besag-74-contains-hammersley-clifford.pdf; Section 4.2.2, printed p. 201 / PDF p. 11, Equations (4.9)–(4.13); Sections 5.2.2–5.5, pp. 206–210 / PDF pp. 16–20; Section 7.2.4, pp. 221–223 / PDF pp. 31–33 | supports | Spatial Interaction and the Statistical Analysis of Lattice Systems. Journal of the Royal Statistical Society, Series B 36(2):192–225, 1974. The university-hosted 46-page scan includes a JSTOR cover and separately published discussion on pp. 225–236. All 46 pages visually read, including two main figures, 16 tables, discussion figure, references and author reply. Printed page=PDF page+190. The main-paper DOI identifies the cited method sections; discussion has DOI 10.1111/j.2517-6161.1974.tb01000.x. A later online date is not the original publication date. All cited method pages were visually read. The source-analysis notes distinguish main-paper support, discussion context, source restrictions and access/extraction limitations. |

## Limits And Additional Notes

- Adversarial author self-review only; all three records remain DRAFT.
- All 64 PDF pages were visually read, including wrappers and the separately published 1974 discussion. No complete extracted-text or OCR reading is asserted. The record method locators cite the main papers; discussion-specific extensions remain contextual research leads.
- Publisher search metadata corroborates publication identity. Direct Oxford main-paper access failed; the complete university-hosted PDF was inspected. The later online date is not treated as the original publication date.
- The first extraction command used an unsupported all-pages selector and failed before extraction. Explicit page ranges succeeded; both attempts remain in the discovery ledger.
- Pseudolikelihood consistency and likelihood-test approximations require the source conditions and further regularity; no universal theorem or performance guarantee is asserted.
- Original finite calculations use synthetic states, a declared finite parameter grid and exact small matrices. They are not author-code reproduction, empirical fitting, benchmarking or general consistency proofs.
- 236 pending leads plus other unresolved dispositions remain; discovery continues.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T220709Z-coding-pseudolikelihood-autonormal
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of coding likelihood, pseudolikelihood and proper auto-normal
  fields
started_at: '2026-10-11T22:06:16Z'
finished_at: '2026-10-11T22:07:09Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed all fields of three
    records against 64 fully visually read PDF pages, 31 annotated AIO nodes and eight
    native contextual records. Original exact calculations challenge conditional normalization,
    objective equivalence and Gaussian compatibility/properness. This is author self-review,
    not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain two DRAFT parameter-estimation algorithms and one DRAFT proper finite
  Gaussian field family. Conditional-objective definitions, admissible parameter domains,
  weighted compatibility and directional mappings are supported with explicit source
  and asymptotic limitations. No actionable curation finding remains in this selected
  batch.
source:
  git_revision: ebdfeccba2d224d7d1637e3f4d1caca9fb14cd4c
  state: working_tree
  inputs:
  - path: data/aio/AutoEncoderNetwork.yaml
    sha256: 7a5eb5c54dab03959ca7a19c03a4c4ece161b05618255294e61df174bcaa4521
    role: context
  - path: data/aio/AutoregressiveLanguageModel.yaml
    sha256: 1ee5824569635aab5df1b1f23eaabca463bd7ef87d1b22e9d9c42375a49ec800
    role: context
  - path: data/aio/AutoregressiveMovingAverage.yaml
    sha256: eb69aaedb34d8c9e620ef4f0d20111feaf9c3dd09236f57536561e9a6cccdf53
    role: context
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/CategoryEncodingLayer.yaml
    sha256: ca7e7f35c28bbd84a60b39be9d4b91c9d0c2015e180c0231a7ccfc2d09d50237
    role: context
  - path: data/aio/CausalGraphicalModel.yaml
    sha256: 868d353893701f2b8bedc9a95ef3219c0659fe230dad792c1932be078874db8b
    role: context
  - path: data/aio/DenoisingAutoEncoder.yaml
    sha256: f9d3ccf856e3aa3b7d01af120409640900e270f26c4e470003219d321816074f
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
  - path: data/aio/GeneralizedLinearModel.yaml
    sha256: 202002ec50c6e6207bc2fefba5baeab233514fd8f9118a623d1917b599ce2c7d
    role: context
  - path: data/aio/HiddenLayer.yaml
    sha256: 945f974c1d298a827086c3439ec3f9ae029380f6d2fa52378eb95ccad1f3b886
    role: context
  - path: data/aio/ImplicitLanguageModel.yaml
    sha256: 818c396b19757360dcdff6291a85d589c50638e0dc6d6bfcd96fdcb7bdf46ce9
    role: context
  - path: data/aio/LinearRegression.yaml
    sha256: 9b6f1b2ea06d9a47e5f7cf94c66afeaa6d40c3e7d0fdb5037d2c25fabc6d8167
    role: context
  - path: data/aio/LogisticRegression.yaml
    sha256: 67dd6e8ae1bb6bfc48598b41adccbf7d48d925db8b0ee3a71f59569913b8c968
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
  - path: data/aio/Model.yaml
    sha256: 56b85d1c6d559d9ce4172dcf9c776126e91a03649c8f4d1fa8e3f5130f0ca73b
    role: context
  - path: data/aio/Normalization.yaml
    sha256: ecdbd41476b6125c670855f1f00090047acd61f5ee16d71384f6b9ed86bea2bb
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
  - path: data/aio/SparseAutoEncoder.yaml
    sha256: 9bbb865ec227305e8ddbe8eab9546510048109d43ba3a733d25303e4780ec359
    role: context
  - path: data/aio/SparseLearning.yaml
    sha256: 0e45f464899bee39df6c8af85e3e0fccba4062f39c73e35c8e884113f78ce3c5
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
  - path: data/aio/VariationalAutoEncoder.yaml
    sha256: f8f523c5f2cecf91f1510c5ab74bfd36d717f3e683a9a8384e44a3f855e4c45e
    role: context
  - path: data/aio/VectorAutoregression.yaml
    sha256: 8a8e67b3efe79835eb5ce1edc437fe4fe9f6f6c95d7aeb22b602c97c38d3c211
    role: context
  - path: data/curated/AutoNormalMarkovRandomField.yaml
    sha256: da7cfa897744f9b67bf75a4a8f0ea7748c1a052ed6ef063f0fbceec094e0ec90
    role: target
  - path: data/curated/ExpectationMaximization.yaml
    sha256: eab2880f9e6db51aa49135ada0c3f6d1504e947e6f920d0a5913fd7ddbd069c4
    role: context
  - path: data/curated/GaussianProcessRegression.yaml
    sha256: d83d0de4a152e7db689636928f41eb5d3663281285585d835f2a5535403d6a0d
    role: context
  - path: data/curated/GibbsSampling.yaml
    sha256: 8175215986c0507e3664a3aedf8074fc067d85b4a89002091d1bcb9b637a522a
    role: context
  - path: data/curated/HiddenMarkovRandomField.yaml
    sha256: 620a68339af0155d1b1f83304dde7fed4634ec95e5a9541480f0d0b37b326327
    role: context
  - path: data/curated/HiddenMarkovTree.yaml
    sha256: ca89c267443e8b806d61b389943bd06a514fb8a95668bd604fae4ecc2d873e1b
    role: context
  - path: data/curated/IteratedConditionalModes.yaml
    sha256: e3cab6676e99fc64d8afca411250e28eec5126524709c6e67988180fa54ffc78
    role: context
  - path: data/curated/IterativeConditionalEstimation.yaml
    sha256: 98813e020f43870f725a5c1e4ab0de9197f0dc2bc85f61e66e2044ab8d87e9cc
    role: context
  - path: data/curated/MarkovRandomField.yaml
    sha256: 03b1f2a66b2183a5bf5943bee7ec0619b9e07947d6c9187263e279ee475f9149
    role: context
  - path: data/curated/MaximumCodingLikelihoodEstimation.yaml
    sha256: 7a298997509be9824c83fdfb953e01cb09ba5834be395d35237392eea4a00435
    role: target
  - path: data/curated/MaximumPseudolikelihoodEstimation.yaml
    sha256: b529f9ae03da6f4c1153a5dcc222342b9eacb0b7496273254ee66b20b366e70c
    role: target
  - path: research/discovery/20261011T220306Z-coding-pseudolikelihood-autonormal.json
    sha256: a44f800f2054edab92d7401337bdff359d8083efbc65f161ebd9898701fa31e4
    role: context
  - path: research/discovery/coding-pseudolikelihood-autonormal-boundaries.py
    sha256: 9982966cf8345ed0c6e6afac8d869b3410856e46ff2911703fd584adf0d1a532
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
- target_id: AIMech:MaximumPseudolikelihoodEstimation
  path: data/curated/MaximumPseudolikelihoodEstimation.yaml
  label: Maximum pseudolikelihood estimation
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MaximumPseudolikelihoodEstimation.yaml
    role: maintained
- target_id: AIMech:MaximumCodingLikelihoodEstimation
  path: data/curated/MaximumCodingLikelihoodEstimation.yaml
  label: Maximum coding likelihood estimation
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/MaximumCodingLikelihoodEstimation.yaml
    role: maintained
- target_id: AIMech:AutoNormalMarkovRandomField
  path: data/curated/AutoNormalMarkovRandomField.yaml
  label: Auto-normal Markov random field
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AutoNormalMarkovRandomField.yaml
    role: maintained
scope:
  description: All fields of three selected maintained concepts for independent-site
    coding estimation, full-conditional pseudolikelihood estimation and proper finite
    auto-normal modeling.
  selection: Exact maintained IDs MaximumPseudolikelihoodEstimation, MaximumCodingLikelihoodEstimation
    and AutoNormalMarkovRandomField; complete selected batch without sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:MaximumPseudolikelihoodEstimation
  - AIMech:MaximumCodingLikelihoodEstimation
  - AIMech:AutoNormalMarkovRandomField
  exclusions:
  - target: Author implementations, empirical fitting and general consistency proofs
    reason: No author code, parameter fitting, training or benchmark ran. Finite arithmetic
      establishes specific objective and properness boundaries, not general statistical
      properties.
  - target: Previous records and remaining frontier
    reason: Eight prior native records supply context without renewed scientific approval.
      236 pending inspection leads plus other unresolved dispositions remain.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:MaximumPseudolikelihoodEstimation
  - AIMech:MaximumCodingLikelihoodEstimation
  - AIMech:AutoNormalMarkovRandomField
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 81.25s (0:01:21)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 403 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 115 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 112,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:MaximumPseudolikelihoodEstimation
  - AIMech:MaximumCodingLikelihoodEstimation
  - AIMech:AutoNormalMarkovRandomField
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
  - AIMech:MaximumPseudolikelihoodEstimation
  - AIMech:MaximumCodingLikelihoodEstimation
  - AIMech:AutoNormalMarkovRandomField
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
  - AIMech:MaximumPseudolikelihoodEstimation
  - AIMech:MaximumCodingLikelihoodEstimation
  - AIMech:AutoNormalMarkovRandomField
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited 0 with no output.
- check_id: finite-arithmetic
  name: Binary conditional objectives and Gaussian compatibility calculations
  command: python3 research/discovery/coding-pseudolikelihood-autonormal-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:MaximumPseudolikelihoodEstimation
  - AIMech:MaximumCodingLikelihoodEstimation
  - AIMech:AutoNormalMarkovRandomField
  exit_code: 0
  expected_exit_code: 0
  summary: '{"binary": {"pseudolikelihood_total_mass_at_lambda_2": "13/10", "observed":
    [1, 1, 1, 0], "parameter_grid": ["1", "3/2", "2", "21/10", "9/4", "3"], "joint_likelihood_maximizer":
    "2", "pseudolikelihood_maximizer": "21/10", "coding_maximizers": ["3", "3/2"],
    "arithmetic_mean_of_coding_maximizers": "9/4", "scores": {"1": ["1/16", "1/16",
    "1/4", "1/4"], "3/2": ["9/125", "27/325", "3/10", "18/65"], "2": ["2/27", "4/45",
    "1/3", "4/15"], "21/10": ["2205/29791", "46305/519901", "21/62", "4410/16771"],
    "9/4": ["162/2197", "1458/16393", "9/26", "324/1261"], "3": ["9/128", "27/320",
    "3/8", "9/40"]}}, "gaussian": {"precision": [["2", "-1", "0"], ["-1", "3", "-1"],
    ["0", "-1", "2"]], "covariance": [["5/8", "1/4", "1/8"], ["1/4", "1/2", "1/4"],
    ["1/8", "1/4", "5/8"]], "conditional_variances": ["1/2", "1/3", "1/2"], "conditional_coefficients":
    [["0", "1/2", "0"], ["1/3", "0", "1/3"], ["0", "1/2", "0"]], "marginal_covariance_0_2":
    "1/8", "conditional_covariance_0_2_given_1": "0", "same_coefficient_sar_precision":
    [["7/3", "-2", "1/3"], ["-2", "4", "-2"], ["1/3", "-2", "7/3"]], "joint_quadratic":
    "19", "pseudolikelihood_quadratic": "29", "gaussian_pseudolikelihood_total_mass":
    "3/2", "invalid_precision_determinant": "-7/25", "invalid_precision_quadratic_witness":
    "-2/5", "intrinsic_precision_determinant": "0"}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T220306Z-coding-pseudolikelihood-autonormal.json
  accessed_at: '2026-10-11T22:06:16Z'
  support: supports
  summary: 'No normalized identity match was found across all 442 pinned AIO labels
    and all scoped synonyms and 400 preceding native IDs, names and aliases. Full-checkout
    fixed-string searches included ignored and hidden files in worktree and main,
    yielding 35 and 35 matched lines; all 23 unique contents were read. Hits are citations,
    contextual statements and discovery leads rather than records of these identities.
    All 182 semantic label/synonym hits were read. Thirty-one fully annotated exact
    CLASS nodes and outgoing edges were inspected: 23 byte-equivalent to prior inspected
    nodes and eight freshly read. Thirty-nine contextual YAMLs comprise 31 generated
    and eight native records: 29 byte-verified after prior reading and 10 freshly
    read. Short acronyms were included in the normalized identity comparison. Absence
    is bounded to the pinned snapshot, maintained corpus and inspected semantic neighborhood.'
  search_scope: 'No normalized identity match was found across all 442 pinned AIO
    labels and all scoped synonyms and 400 preceding native IDs, names and aliases.
    Full-checkout fixed-string searches included ignored and hidden files in worktree
    and main, yielding 35 and 35 matched lines; all 23 unique contents were read.
    Hits are citations, contextual statements and discovery leads rather than records
    of these identities. All 182 semantic label/synonym hits were read. Thirty-one
    fully annotated exact CLASS nodes and outgoing edges were inspected: 23 byte-equivalent
    to prior inspected nodes and eight freshly read. Thirty-nine contextual YAMLs
    comprise 31 generated and eight native records: 29 byte-verified after prior reading
    and 10 freshly read. Short acronyms were included in the normalized identity comparison.
    Absence is bounded to the pinned snapshot, maintained corpus and inspected semantic
    neighborhood.'
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: 31 exact CLASS nodes and outgoing edges, and 182 semantic label/synonym
    hits in source_analysis.aio_mapping_inspection
  accessed_at: '2026-10-11T22:06:16Z'
  support: supports
  summary: MPLE and independent-site coding likelihood map related to ProbabilisticGraphicalModel
    for parameter estimation using compatible graph conditionals; the pinned class
    is task-scoped, not an algorithm superclass. The proper finite auto-normal family
    maps broad to Model and related to ProbabilisticGraphicalModel. MachineLearningTask
    is more generic and does not distinguish the objectives. TrainingStrategy is preprocessing-scoped;
    supervised or unsupervised contexts are not imposed as intrinsic identities. SpatialRegression,
    RegressionAnalysis, GeneralizedLinearModel, LinearRegression and LogisticRegression
    describe regression tasks or model contexts, not these particular estimation objectives
    or every Gaussian joint field. A local regression formula does not equate a compatible
    joint spatial law with an exogenous regression task. MarkovChain, AutoregressiveMovingAverage
    and VectorAutoregression require temporal/sequential structure absent from a general
    spatial graph. BayesianNetwork and CausalGraphicalModel do not preserve the same
    undirected graph by arbitrary factorization or imply causal interventions. AutoregressiveLanguageModel,
    EnergyBasedLLM and ImplicitLanguageModel are language-scoped. AutoEncoderNetwork,
    DenoisingAutoEncoder, SparseAutoEncoder and VariationalAutoEncoder denote neural
    architectures rather than auto-normal fields. SparseLearning refers to sparse
    dictionary representations, and CategoryEncodingLayer to feature encoding; neither
    is graph-independent-set coding likelihood. Normalization changes data scale rather
    than certifying a joint probability normalizer. GaussianNoiseLayer, GaussianDropoutLayer,
    HiddenLayer and ProbabilisticHiddenLayer are neural components. MaximumLayer is
    an elementwise tensor operation, not likelihood optimization. Native MRF, HMRF,
    HMT, EM, ICE, ICM, Gibbs sampling and Gaussian-process regression distinguish
    joint field, latent/observed partition, topology, parameter estimation, state
    optimization, sampling and predictive process conditioning. Contextual reading
    does not renew their scientific approval.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T220306Z-coding-pseudolikelihood-autonormal.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors and context_reading
  accessed_at: '2026-10-11T22:06:16Z'
  support: supports
  summary: 'Eight complete native contextual records read or byte-verified after prior
    full reading: MRF, HMRF, HMT, EM, ICE, ICM, Gibbs sampling and Gaussian-process
    regression. These distinguish graphical distributions, latent-state observation
    models, parameter estimators, conditional state optimizers, samplers and process-prior
    regression. Context reading does not renew scientific approval of these earlier
    records.'
- evidence_id: finite-boundaries
  kind: record_content
  reference: research/discovery/coding-pseudolikelihood-autonormal-boundaries.py
  locator: Exact four-site binary-path conditional objectives and finite parameter
    grid; three-site Gaussian precision, covariance, conditional and simultaneous
    equations
  accessed_at: '2026-10-11T22:06:16Z'
  snapshot_sha256: 9982966cf8345ed0c6e6afac8d869b3410856e46ff2911703fd584adf0d1a532
  support: supports
  summary: Original exact finite calculations enumerate all16states of a four-site
    binary path with edge-agreement weight lambda. At lambda2, the joint law normalizes
    and both independent-site coding products equal their exact joint conditionals
    for every state and complement configuration. The product of all full conditionals
    instead sums to13/10 over configurations. For fixed observation1110 and parameter
    grid{1,3/2,2,21/10,9/4,3}, joint likelihood is maximized at2, pseudolikelihood
    at21/10, and the two coding likelihoods at3 and3/2. Their arithmetic mean9/4 is
    not the pseudolikelihood maximizer. The independent lambda1case recovers the joint
    law. For Gaussian precision[[2,-1,0],[-1,3,-1],[0,-1,2]], exact inverse covariance
    has marginal endpoint covariance1/8 but zero endpoint covariance conditional on
    the middle site. Conditional variances1/2,1/3,1/2 imply asymmetric raw neighbor
    coefficients that satisfy variance-weighted compatibility. The same B and Lambda
    in simultaneous independent-noise equations induce endpoint precision1/3 instead
    of0. At x=(1,-1,2), joint and pseudo quadratics are19 and29; the Gaussian conditional-product
    density integrates to3/2, not1. A positive-diagonal incompatible precision has
    determinant-7/25 and quadratic witness-2/5; a graph-Laplacian precision is singular
    with a flat constant direction. These are exact mathematical objective comparisons
    on declared synthetic configurations, not empirical fitting, author-code reproduction,
    benchmarks or general consistency proofs.
- evidence_id: maximumpseudolikelihoodestimation-source-0
  kind: primary_source
  reference: https://www2.stat.duke.edu/~sschmid/Courses/Stat376/Papers/GibbsFieldEst/BesagPseudoLik1975.pdf
  locator: Sections 3.1–3.4, printed pp. 188–193 / PDF pp. 11–16; especially Section
    3.3, pp. 190–192 / PDF pp. 13–15, Equations (3.2)–(3.10) and consistency sketch
  accessed_at: '2026-10-11T21:47:22Z'
  snapshot_sha256: 0db3c34554e1c4ce64921d70e74506f4e0a373afa91c4b89db5864499ba73724
  support: supports
  summary: Statistical Analysis of Non-Lattice Data. The Statistician 24(3):179–195,
    September 1975; university-hosted 18-page scan including JSTOR wrapper. All 18
    pages visually read, including all equations and references. Printed page=PDF
    page+177. Publisher metadata corroborates title, author, pages, date and DOI.
    No full extracted-text or OCR reading is asserted. All cited method pages were
    visually read. The source-analysis notes distinguish main-paper support, discussion
    context, source restrictions and access/extraction limitations.
- evidence_id: maximumcodinglikelihoodestimation-source-0
  kind: primary_source
  reference: https://www2.stat.duke.edu/~sschmid/Courses/Stat376/Papers/GibbsFieldEst/BesagPseudoLik1975.pdf
  locator: Section 3.2, printed pp. 189–190 / PDF pp. 12–13, Equation (3.1); Section
    3.3, p. 192 / PDF p. 15, coding-class decomposition
  accessed_at: '2026-10-11T21:47:22Z'
  snapshot_sha256: 0db3c34554e1c4ce64921d70e74506f4e0a373afa91c4b89db5864499ba73724
  support: supports
  summary: Statistical Analysis of Non-Lattice Data. The Statistician 24(3):179–195,
    September 1975; university-hosted 18-page scan including JSTOR wrapper. All 18
    pages visually read, including all equations and references. Printed page=PDF
    page+177. Publisher metadata corroborates title, author, pages, date and DOI.
    No full extracted-text or OCR reading is asserted. All cited method pages were
    visually read. The source-analysis notes distinguish main-paper support, discussion
    context, source restrictions and access/extraction limitations.
- evidence_id: maximumcodinglikelihoodestimation-source-1
  kind: primary_source
  reference: https://www.stat.cmu.edu/~brian/720-2007-source/nice%20materials/besag-74-contains-hammersley-clifford.pdf
  locator: Section 6.1, printed pp. 211–212 / PDF pp. 21–22, Figures 1–2 and likelihood
    comparability; Section 7.2.4 and conclusion, pp. 222–223 / PDF pp. 32–33, inadmissible
    fits and model limitations
  accessed_at: '2026-10-11T21:47:19Z'
  snapshot_sha256: 796199ef5d870e81750cc3fc262f140ccc7114ce916e3a23fc53f36a614bebef
  support: supports
  summary: Spatial Interaction and the Statistical Analysis of Lattice Systems. Journal
    of the Royal Statistical Society, Series B 36(2):192–225, 1974. The university-hosted
    46-page scan includes a JSTOR cover and separately published discussion on pp.
    225–236. All 46 pages visually read, including two main figures, 16 tables, discussion
    figure, references and author reply. Printed page=PDF page+190. The main-paper
    DOI identifies the cited method sections; discussion has DOI 10.1111/j.2517-6161.1974.tb01000.x.
    A later online date is not the original publication date. All cited method pages
    were visually read. The source-analysis notes distinguish main-paper support,
    discussion context, source restrictions and access/extraction limitations.
- evidence_id: autonormalmarkovrandomfield-source-0
  kind: primary_source
  reference: https://www2.stat.duke.edu/~sschmid/Courses/Stat376/Papers/GibbsFieldEst/BesagPseudoLik1975.pdf
  locator: Sections 2.1–2.5, printed pp. 182–188 / PDF pp. 5–11, especially Equations
    (2.1)–(2.6) and precision-factor simulation; Section 3.4, p. 193 / PDF p. 16,
    joint Gaussian likelihood
  accessed_at: '2026-10-11T21:47:22Z'
  snapshot_sha256: 0db3c34554e1c4ce64921d70e74506f4e0a373afa91c4b89db5864499ba73724
  support: supports
  summary: Statistical Analysis of Non-Lattice Data. The Statistician 24(3):179–195,
    September 1975; university-hosted 18-page scan including JSTOR wrapper. All 18
    pages visually read, including all equations and references. Printed page=PDF
    page+177. Publisher metadata corroborates title, author, pages, date and DOI.
    No full extracted-text or OCR reading is asserted. All cited method pages were
    visually read. The source-analysis notes distinguish main-paper support, discussion
    context, source restrictions and access/extraction limitations.
- evidence_id: autonormalmarkovrandomfield-source-1
  kind: primary_source
  reference: https://www.stat.cmu.edu/~brian/720-2007-source/nice%20materials/besag-74-contains-hammersley-clifford.pdf
  locator: Section 4.2.2, printed p. 201 / PDF p. 11, Equations (4.9)–(4.13); Sections
    5.2.2–5.5, pp. 206–210 / PDF pp. 16–20; Section 7.2.4, pp. 221–223 / PDF pp. 31–33
  accessed_at: '2026-10-11T21:47:19Z'
  snapshot_sha256: 796199ef5d870e81750cc3fc262f140ccc7114ce916e3a23fc53f36a614bebef
  support: supports
  summary: Spatial Interaction and the Statistical Analysis of Lattice Systems. Journal
    of the Royal Statistical Society, Series B 36(2):192–225, 1974. The university-hosted
    46-page scan includes a JSTOR cover and separately published discussion on pp.
    225–236. All 46 pages visually read, including two main figures, 16 tables, discussion
    figure, references and author reply. Printed page=PDF page+190. The main-paper
    DOI identifies the cited method sections; discussion has DOI 10.1111/j.2517-6161.1974.tb01000.x.
    A later online date is not the original publication date. All cited method pages
    were visually read. The source-analysis notes distinguish main-paper support,
    discussion context, source restrictions and access/extraction limitations.
assessments:
- assessment_id: maximumpseudolikelihoodestimation
  area: evidence
  topic: Identity, definition, mechanism, limitations, evidence version and AIO direction
  outcome: supported
  target_ids:
  - AIMech:MaximumPseudolikelihoodEstimation
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - maximumpseudolikelihoodestimation-source-0
  summary: 'The classical full-conditional pseudolikelihood uses every observed site.
    It is an estimation objective and does not specify a unique numerical optimizer.
    It is distinct from full joint maximum likelihood, independent-site coding likelihood,
    iterative conditional modes for state optimization, and iterative conditional
    estimation for incomplete-data parameters. A general loss assembled from unrelated
    conditionals is not automatically the pseudolikelihood of a compatible joint model.
    The paper discusses fixed-site spatial models without assuming stationarity or
    homogeneity; the local graph and parameterization must still be specified. No
    normalized identity match was found across all 442 pinned AIO labels and all scoped
    synonyms and 400 preceding native IDs, names and aliases. Full-checkout fixed-string
    searches included ignored and hidden files in worktree and main, yielding 35 and
    35 matched lines; all 23 unique contents were read. Hits are citations, contextual
    statements and discovery leads rather than records of these identities. All 182
    semantic label/synonym hits were read. Thirty-one fully annotated exact CLASS
    nodes and outgoing edges were inspected: 23 byte-equivalent to prior inspected
    nodes and eight freshly read. Thirty-nine contextual YAMLs comprise 31 generated
    and eight native records: 29 byte-verified after prior reading and 10 freshly
    read. Short acronyms were included in the normalized identity comparison. Absence
    is bounded to the pinned snapshot, maintained corpus and inspected semantic neighborhood.'
  details: 'For an observed configuration x and a compatible family p_theta with well-defined
    full conditionals, form PL(theta;x)=product_i p_theta(x_i|x_(-i)) and maximize
    sum_i log p_theta(x_i|x_(-i)) over the admissible parameter space. In a Markov
    field, each factor depends only on the site’s neighbors; a global joint partition
    function cancels from that factor, although its local normalizer still must be
    evaluated. If the sites are partitioned into nonneighbor coding sets, the log
    pseudolikelihood is the sum of their conditional log likelihoods. This identity
    combines objectives, not the separately fitted parameter values. For the source’s
    proper common-conditional-variance Gaussian model with mean D*a, symmetric B=I-phi*H
    and variance sigma^2, the residual term is (x-D*a)^T B^2(x-D*a)/sigma^2. Its joint
    Gaussian likelihood instead includes log|B| and a single-B quadratic. Complete
    independence is a special case in which the product of full conditionals equals
    the joint likelihood. Limitations: The product of normalized full conditionals
    is generally not a normalized joint distribution over x. Its maximizer need not
    equal the joint-likelihood maximizer. Dividing that product by a parameter-dependent
    joint normalizer changes the objective. Conditionals must be compatible with the
    intended joint model and parameters must lie in its valid domain. Optimizing local
    expressions without these restrictions can produce inadmissible joint parameters.
    Gaussian variance positivity and precision positive definiteness remain necessary.
    The source gives a consistency sketch for an infinite bounded-degree site system
    with growing coding classes and additional regularity and boundary conditions.
    It is not a universal theorem for arbitrary growing graphs, fixed finite samples,
    misspecified models or every parameterization. Efficiency, uncertainty estimates
    and likelihood-ratio calibration do not automatically follow ordinary independent-sample
    likelihood formulas. Strong dependence, limited information, boundaries and model
    mismatch require separate assessment; the source offers no universal efficiency
    advantage. Gaussian least-squares expressions apply to the stated common-variance
    and compatible symmetric interaction parameterization. Design inverses, ratio
    denominators, finite maximizers and nonzero residual variance require checks.
    Alternating algebraic updates are not a proof of a global optimum. A partition
    into coding sets does not make the corresponding estimators or test statistics
    independent. The pseudolikelihood maximizer is not generally the arithmetic mean
    of coding-set maximizers. Original finite objective comparisons demonstrate this
    distinction; no empirical fitting, author code or benchmark was run.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: An estimator defined by a conditional objective or a proper finite
      Gaussian graphical model family; estimation objectives and probability distributions
      are distinct concepts.
    evidence_ids:
    - maximumpseudolikelihoodestimation-source-0
  - name: aio-assessment
    value: related_match
    definition: MPLE and independent-site coding likelihood map related to ProbabilisticGraphicalModel
      for parameter estimation using compatible graph conditionals; the pinned class
      is task-scoped, not an algorithm superclass. The proper finite auto-normal family
      maps broad to Model and related to ProbabilisticGraphicalModel. MachineLearningTask
      is more generic and does not distinguish the objectives. TrainingStrategy is
      preprocessing-scoped; supervised or unsupervised contexts are not imposed as
      intrinsic identities. SpatialRegression, RegressionAnalysis, GeneralizedLinearModel,
      LinearRegression and LogisticRegression describe regression tasks or model contexts,
      not these particular estimation objectives or every Gaussian joint field. A
      local regression formula does not equate a compatible joint spatial law with
      an exogenous regression task. MarkovChain, AutoregressiveMovingAverage and VectorAutoregression
      require temporal/sequential structure absent from a general spatial graph. BayesianNetwork
      and CausalGraphicalModel do not preserve the same undirected graph by arbitrary
      factorization or imply causal interventions. AutoregressiveLanguageModel, EnergyBasedLLM
      and ImplicitLanguageModel are language-scoped. AutoEncoderNetwork, DenoisingAutoEncoder,
      SparseAutoEncoder and VariationalAutoEncoder denote neural architectures rather
      than auto-normal fields. SparseLearning refers to sparse dictionary representations,
      and CategoryEncodingLayer to feature encoding; neither is graph-independent-set
      coding likelihood. Normalization changes data scale rather than certifying a
      joint probability normalizer. GaussianNoiseLayer, GaussianDropoutLayer, HiddenLayer
      and ProbabilisticHiddenLayer are neural components. MaximumLayer is an elementwise
      tensor operation, not likelihood optimization. Native MRF, HMRF, HMT, EM, ICE,
      ICM, Gibbs sampling and Gaussian-process regression distinguish joint field,
      latent/observed partition, topology, parameter estimation, state optimization,
      sampling and predictive process conditioning. Contextual reading does not renew
      their scientific approval.
    evidence_ids:
    - mapping
- assessment_id: maximumcodinglikelihoodestimation
  area: evidence
  topic: Identity, definition, mechanism, limitations, evidence version and AIO direction
  outcome: supported
  target_ids:
  - AIMech:MaximumCodingLikelihoodEstimation
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - maximumcodinglikelihoodestimation-source-0
  - maximumcodinglikelihoodestimation-source-1
  summary: 'This record uses the classical independent-site coding method of Besag.
    Coding selects a graph-independent subset; it does not encode features, compress
    data or learn sparse representations. Shifted or alternative coding sets can give
    additional dependent estimates. Extensions using conditionally dependent blocks
    require their joint conditional likelihoods rather than this independent-singleton
    product. The method is distinct from multiplying all site conditionals as pseudolikelihood
    and from state updates in ICM or Gibbs sampling. No normalized identity match
    was found across all 442 pinned AIO labels and all scoped synonyms and 400 preceding
    native IDs, names and aliases. Full-checkout fixed-string searches included ignored
    and hidden files in worktree and main, yielding 35 and 35 matched lines; all 23
    unique contents were read. Hits are citations, contextual statements and discovery
    leads rather than records of these identities. All 182 semantic label/synonym
    hits were read. Thirty-one fully annotated exact CLASS nodes and outgoing edges
    were inspected: 23 byte-equivalent to prior inspected nodes and eight freshly
    read. Thirty-nine contextual YAMLs comprise 31 generated and eight native records:
    29 byte-verified after prior reading and 10 freshly read. Short acronyms were
    included in the normalized identity comparison. Absence is bounded to the pinned
    snapshot, maintained corpus and inspected semantic neighborhood.'
  details: 'For a compatible positive Markov-field model with observed configuration
    x, choose a nonempty set S containing no neighboring pair and let C be its complement.
    Conditional on X_C=x_C, the variables in S are mutually independent, so L_S(theta;x_S|x_C)=product_(i
    in S) p_theta(x_i|x_(-i)). Maximize its log over valid theta. The complement supplies
    conditioning values even though its own site likelihood factors are omitted. A
    rectangular four-neighbor graph admits checkerboard coding; adding diagonal interactions
    requires another independent-set design, such as the source’s four shifted patterns.
    Changing the selected set changes the conditional likelihood. The full-site pseudolikelihood
    equals the product of coding likelihoods for a partition into independent sets,
    but maximizing that product differs in general from averaging separately fitted
    parameters. Limitations: The factorization needs a valid graph and the stated
    joint conditional-independence property. It is not justified by spatial distance
    alone or by arbitrary, incompatible local distributions. Hard support constraints
    require separate treatment beyond the positive-model construction. Choosing a
    large independent set need not yield a unique selection or the most informative
    estimator. Conditioning omits some likelihood information while retaining the
    complement as covariates; it does not literally discard all white-site observations.
    Estimates and tests from shifted coding patterns reuse the same configuration
    and are generally dependent. Combining them requires a justified procedure; neither
    naive independent-test calibration nor an arithmetic average of estimates is automatically
    optimal. Conditional likelihood-ratio comparisons require comparable selected
    dependent sites and conditioning sets. The source warns against comparing fits
    based on different codings as if they were the same likelihood. Ordinary asymptotic
    approximations still require identifiability, information and regularity conditions.
    The source’s unconstrained coding estimates can violate the intended joint-model
    parameter restrictions. A conditional objective may be finite where the full Gaussian
    field is invalid, so the parameter domain must be enforced. Averaging happened
    to yield admissible values in some reported examples and is not a general repair.
    The inspected plant and wheat data illustrate estimation and model diagnostics,
    while exposing model inadequacy and aggregation effects. They do not prove general
    efficiency or spatial prediction accuracy. No empirical data fitting, author implementation
    or benchmark was reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: An estimator defined by a conditional objective or a proper finite
      Gaussian graphical model family; estimation objectives and probability distributions
      are distinct concepts.
    evidence_ids:
    - maximumcodinglikelihoodestimation-source-0
    - maximumcodinglikelihoodestimation-source-1
  - name: aio-assessment
    value: related_match
    definition: MPLE and independent-site coding likelihood map related to ProbabilisticGraphicalModel
      for parameter estimation using compatible graph conditionals; the pinned class
      is task-scoped, not an algorithm superclass. The proper finite auto-normal family
      maps broad to Model and related to ProbabilisticGraphicalModel. MachineLearningTask
      is more generic and does not distinguish the objectives. TrainingStrategy is
      preprocessing-scoped; supervised or unsupervised contexts are not imposed as
      intrinsic identities. SpatialRegression, RegressionAnalysis, GeneralizedLinearModel,
      LinearRegression and LogisticRegression describe regression tasks or model contexts,
      not these particular estimation objectives or every Gaussian joint field. A
      local regression formula does not equate a compatible joint spatial law with
      an exogenous regression task. MarkovChain, AutoregressiveMovingAverage and VectorAutoregression
      require temporal/sequential structure absent from a general spatial graph. BayesianNetwork
      and CausalGraphicalModel do not preserve the same undirected graph by arbitrary
      factorization or imply causal interventions. AutoregressiveLanguageModel, EnergyBasedLLM
      and ImplicitLanguageModel are language-scoped. AutoEncoderNetwork, DenoisingAutoEncoder,
      SparseAutoEncoder and VariationalAutoEncoder denote neural architectures rather
      than auto-normal fields. SparseLearning refers to sparse dictionary representations,
      and CategoryEncodingLayer to feature encoding; neither is graph-independent-set
      coding likelihood. Normalization changes data scale rather than certifying a
      joint probability normalizer. GaussianNoiseLayer, GaussianDropoutLayer, HiddenLayer
      and ProbabilisticHiddenLayer are neural components. MaximumLayer is an elementwise
      tensor operation, not likelihood optimization. Native MRF, HMRF, HMT, EM, ICE,
      ICM, Gibbs sampling and Gaussian-process regression distinguish joint field,
      latent/observed partition, topology, parameter estimation, state optimization,
      sampling and predictive process conditioning. Contextual reading does not renew
      their scientific approval.
    evidence_ids:
    - mapping
- assessment_id: autonormalmarkovrandomfield
  area: evidence
  topic: Identity, definition, mechanism, limitations, evidence version and AIO direction
  outcome: supported
  target_ids:
  - AIMech:AutoNormalMarkovRandomField
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - autonormalmarkovrandomfield-source-0
  - autonormalmarkovrandomfield-source-1
  summary: 'The record is scoped to the proper finite auto-normal construction. It
    is a Gaussian conditional-autoregressive representation of a multivariate normal
    law with a specified conditional-dependence graph. Intrinsic improper Gaussian
    fields and infinite-lattice extensions require separate existence or constraint
    conditions and are not exact aliases here. Spatial conditional autoregression
    is not temporal autoregression and is not the simultaneous autoregressive model
    obtained by treating the same local residual equations as independent noise equations.
    Gaussian-process regression conditions a process prior on training observations
    for prediction; this record specifies the finite graphical joint law itself. It
    can be used as a prior but does not inherently introduce hidden labels or independent
    observation emissions. No normalized identity match was found across all 442 pinned
    AIO labels and all scoped synonyms and 400 preceding native IDs, names and aliases.
    Full-checkout fixed-string searches included ignored and hidden files in worktree
    and main, yielding 35 and 35 matched lines; all 23 unique contents were read.
    Hits are citations, contextual statements and discovery leads rather than records
    of these identities. All 182 semantic label/synonym hits were read. Thirty-one
    fully annotated exact CLASS nodes and outgoing edges were inspected: 23 byte-equivalent
    to prior inspected nodes and eight freshly read. Thirty-nine contextual YAMLs
    comprise 31 generated and eight native records: 29 byte-verified after prior reading
    and 10 freshly read. Short acronyms were included in the normalized identity comparison.
    Absence is bounded to the pinned snapshot, maintained corpus and inspected semantic
    neighborhood.'
  details: 'For site i, specify X_i given all other sites as normal with mean mu_i+sum_(j!=i)
    beta_ij*(x_j-mu_j) and variance v_i>0 independent of the conditioning values.
    Let B have diagonal 1 and off-diagonal -beta_ij, and let Lambda=diag(v_i). These
    conditionals define the proper finite joint model when Q=Lambda^(-1)*B is symmetric
    positive definite. Symmetry requires beta_ij*v_j=beta_ji*v_i. The joint law is
    N(mu,Q^(-1)), with density proportional to |Q|^(1/2)*exp[-(x-mu)^T Q(x-mu)/2].
    A zero off-diagonal precision entry denotes conditional independence given the
    other sites; marginal covariance need not vanish. With common v_i=sigma^2, compatibility
    reduces to symmetric positive-definite B and covariance sigma^2*B^(-1). In contrast,
    the simultaneous equations B*(X-mu)=epsilon with independent epsilon~N(0,Lambda)
    imply covariance B^(-1)*Lambda*B^(-T) and precision B^T*Lambda^(-1)*B. For the
    proper conditional model, a factorization Q=C^T*C allows exact Gaussian sampling
    as mu+C^(-1)*z with independent standard-normal z. Limitations: Every site conditional
    can be individually normalized while the proposed collection fails to define a
    proper joint law. Weighted symmetry and positive definiteness must both hold.
    With unequal conditional variances, raw beta coefficients need not be symmetric.
    A singular precision can describe an intrinsic improper construction only with
    additional interpretation or constraints; it is not the ordinary normalized Gaussian
    density stated here. An indefinite precision gives a nonintegrable quadratic model.
    Positive diagonal entries alone are insufficient. Finite-graph eigenvalue bounds
    depend on the actual graph and boundary conditions. Infinite-lattice stationarity
    criteria are not automatically necessary finite-graph conditions. The source’s
    stationary or homogeneous examples do not require every finite auto-normal model
    to share those assumptions. Missing precision edges encode conditional independence,
    not marginal independence or causal effects. A sparse simultaneous-equation matrix
    can induce additional precision edges. Unconstrained conditional least-squares,
    coding-likelihood or pseudolikelihood estimates may leave the proper joint parameter
    domain. The Gaussian fitting objective and parameter identifiability depend on
    the specified mean, graph and interaction parameterization; existence of a covariance
    representation does not ensure identifiable scientific parameters. The source’s
    wheat and plant examples expose aggregation, nonstationarity and model-fit concerns;
    a fitted Gaussian field does not establish a causal spatial mechanism or universal
    predictive adequacy. The record does not certify source implementations, empirical
    fits or infinite-system convergence.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: An estimator defined by a conditional objective or a proper finite
      Gaussian graphical model family; estimation objectives and probability distributions
      are distinct concepts.
    evidence_ids:
    - autonormalmarkovrandomfield-source-0
    - autonormalmarkovrandomfield-source-1
  - name: aio-assessment
    value: broad_match,related_match
    definition: MPLE and independent-site coding likelihood map related to ProbabilisticGraphicalModel
      for parameter estimation using compatible graph conditionals; the pinned class
      is task-scoped, not an algorithm superclass. The proper finite auto-normal family
      maps broad to Model and related to ProbabilisticGraphicalModel. MachineLearningTask
      is more generic and does not distinguish the objectives. TrainingStrategy is
      preprocessing-scoped; supervised or unsupervised contexts are not imposed as
      intrinsic identities. SpatialRegression, RegressionAnalysis, GeneralizedLinearModel,
      LinearRegression and LogisticRegression describe regression tasks or model contexts,
      not these particular estimation objectives or every Gaussian joint field. A
      local regression formula does not equate a compatible joint spatial law with
      an exogenous regression task. MarkovChain, AutoregressiveMovingAverage and VectorAutoregression
      require temporal/sequential structure absent from a general spatial graph. BayesianNetwork
      and CausalGraphicalModel do not preserve the same undirected graph by arbitrary
      factorization or imply causal interventions. AutoregressiveLanguageModel, EnergyBasedLLM
      and ImplicitLanguageModel are language-scoped. AutoEncoderNetwork, DenoisingAutoEncoder,
      SparseAutoEncoder and VariationalAutoEncoder denote neural architectures rather
      than auto-normal fields. SparseLearning refers to sparse dictionary representations,
      and CategoryEncodingLayer to feature encoding; neither is graph-independent-set
      coding likelihood. Normalization changes data scale rather than certifying a
      joint probability normalizer. GaussianNoiseLayer, GaussianDropoutLayer, HiddenLayer
      and ProbabilisticHiddenLayer are neural components. MaximumLayer is an elementwise
      tensor operation, not likelihood optimization. Native MRF, HMRF, HMT, EM, ICE,
      ICM, Gibbs sampling and Gaussian-process regression distinguish joint field,
      latent/observed partition, topology, parameter estimation, state optimization,
      sampling and predictive process conditioning. Contextual reading does not renew
      their scientific approval.
    evidence_ids:
    - mapping
- assessment_id: pseudolikelihood-boundary
  area: consistency
  topic: Full-conditional estimation objective versus joint likelihood
  outcome: supported
  target_ids:
  - AIMech:MaximumPseudolikelihoodEstimation
  evidence_ids:
  - maximumpseudolikelihoodestimation-source-0
  - finite-boundaries
  - neighbors
  summary: Retain maximum pseudolikelihood estimation as a distinct algorithm.
  details: The 1975 Section 3.3 objective multiplies every site full conditional of
    a compatible joint family. A global partition function cancels within a conditional,
    but local normalization and the valid joint parameter domain remain necessary.
    Coding partitions decompose the log objective; they do not imply averaging separately
    fitted estimates. Exact binary enumeration yields total pseudolikelihood mass
    13/10 and different joint, pseudo and coding maximizers on the explicitly declared
    finite grid. Independent sites recover the joint law. Gaussian pseudolikelihood
    uses the B-squared residual objective, while the joint likelihood has a B quadratic
    and determinant term. The source consistency argument is a qualified infinite
    bounded-degree sketch, not a universal finite-sample guarantee.
- assessment_id: coding-boundary
  area: consistency
  topic: Independent-site conditional likelihood and admissible estimation
  outcome: supported
  target_ids:
  - AIMech:MaximumCodingLikelihoodEstimation
  evidence_ids:
  - maximumcodinglikelihoodestimation-source-0
  - maximumcodinglikelihoodestimation-source-1
  - finite-boundaries
  - neighbors
  summary: Retain maximum coding likelihood estimation as a distinct algorithm.
  details: An independent set is conditionally mutually independent given its complement
    under the stated positive compatible Markov law. The finite binary check verifies
    the factorization and conditional normalization for every state and every complement
    configuration. Complement observations remain conditioning values. Shifted coding
    estimates and tests reuse observations and are generally dependent. Comparisons
    require the same response and conditioning variables, with regularity for asymptotic
    likelihood tests. The 1974 wheat example exhibits inadmissible unconstrained fits;
    neither averaging nor finite conditional likelihood repairs general joint invalidity.
    Dependent-chain extensions need their own joint conditional factors and remain
    a separate research lead.
- assessment_id: autonormal-boundary
  area: consistency
  topic: Proper finite full-conditional Gaussian model versus simultaneous or intrinsic
    constructions
  outcome: supported
  target_ids:
  - AIMech:AutoNormalMarkovRandomField
  evidence_ids:
  - autonormalmarkovrandomfield-source-0
  - autonormalmarkovrandomfield-source-1
  - finite-boundaries
  - neighbors
  summary: Retain the proper finite auto-normal model family.
  details: The unequal-variance compatibility condition is beta_ij*v_j=beta_ji*v_i,
    so raw coefficients may be asymmetric. Q=Lambda^-1 B must be symmetric positive
    definite. Finite calculations verify the conditional coefficients, covariance,
    conditional versus marginal independence, and the distinct same-coefficient SAR
    precision B^T Lambda^-1 B. Positive one-site variances coexist with a nonintegrable
    indefinite quadratic or an improper singular Laplacian, so they do not establish
    a proper joint density. Cholesky simulation uses the specified orientation Q=C^T
    C. Finite and infinite parameter bounds, scientific parameter identification and
    observed empirical fit remain separate questions. Gaussian-process regression,
    hidden-label fields, temporal autoregression and Gaussian neural-network layers
    are neighboring but distinct identities.
- assessment_id: mapping-boundary
  area: grounding
  topic: Directional AIO mappings and neighboring identities
  outcome: supported
  target_ids:
  - AIMech:MaximumPseudolikelihoodEstimation
  - AIMech:MaximumCodingLikelihoodEstimation
  - AIMech:AutoNormalMarkovRandomField
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain all three native identities with scoped AIO mappings.
  details: MPLE and independent-site coding likelihood map related to ProbabilisticGraphicalModel
    for parameter estimation using compatible graph conditionals; the pinned class
    is task-scoped, not an algorithm superclass. The proper finite auto-normal family
    maps broad to Model and related to ProbabilisticGraphicalModel. MachineLearningTask
    is more generic and does not distinguish the objectives. TrainingStrategy is preprocessing-scoped;
    supervised or unsupervised contexts are not imposed as intrinsic identities. SpatialRegression,
    RegressionAnalysis, GeneralizedLinearModel, LinearRegression and LogisticRegression
    describe regression tasks or model contexts, not these particular estimation objectives
    or every Gaussian joint field. A local regression formula does not equate a compatible
    joint spatial law with an exogenous regression task. MarkovChain, AutoregressiveMovingAverage
    and VectorAutoregression require temporal/sequential structure absent from a general
    spatial graph. BayesianNetwork and CausalGraphicalModel do not preserve the same
    undirected graph by arbitrary factorization or imply causal interventions. AutoregressiveLanguageModel,
    EnergyBasedLLM and ImplicitLanguageModel are language-scoped. AutoEncoderNetwork,
    DenoisingAutoEncoder, SparseAutoEncoder and VariationalAutoEncoder denote neural
    architectures rather than auto-normal fields. SparseLearning refers to sparse
    dictionary representations, and CategoryEncodingLayer to feature encoding; neither
    is graph-independent-set coding likelihood. Normalization changes data scale rather
    than certifying a joint probability normalizer. GaussianNoiseLayer, GaussianDropoutLayer,
    HiddenLayer and ProbabilisticHiddenLayer are neural components. MaximumLayer is
    an elementwise tensor operation, not likelihood optimization. Native MRF, HMRF,
    HMT, EM, ICE, ICM, Gibbs sampling and Gaussian-process regression distinguish
    joint field, latent/observed partition, topology, parameter estimation, state
    optimization, sampling and predictive process conditioning. Contextual reading
    does not renew their scientific approval.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:MaximumPseudolikelihoodEstimation
  - AIMech:MaximumCodingLikelihoodEstimation
  - AIMech:AutoNormalMarkovRandomField
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - maximumpseudolikelihoodestimation-source-0
  - maximumcodinglikelihoodestimation-source-0
  - maximumcodinglikelihoodestimation-source-1
  - autonormalmarkovrandomfield-source-0
  - autonormalmarkovrandomfield-source-1
  rationale: Independent-site coding is a normalized conditional likelihood given
    the complement; full-site pseudolikelihood multiplies overlapping conditionals
    and is generally not a joint density; the proper auto-normal construction defines
    a Gaussian joint model that either estimator could fit under validity constraints.
    Sharing a Markov-field application does not make the model and estimation objectives
    equivalent. Preserve local identities and directional AIO mappings.
limitations:
- Adversarial author self-review only; all three records remain DRAFT.
- All 64 PDF pages were visually read, including wrappers and the separately published
  1974 discussion. No complete extracted-text or OCR reading is asserted. The record
  method locators cite the main papers; discussion-specific extensions remain contextual
  research leads.
- Publisher search metadata corroborates publication identity. Direct Oxford main-paper
  access failed; the complete university-hosted PDF was inspected. The later online
  date is not treated as the original publication date.
- The first extraction command used an unsupported all-pages selector and failed before
  extraction. Explicit page ranges succeeded; both attempts remain in the discovery
  ledger.
- Pseudolikelihood consistency and likelihood-test approximations require the source
  conditions and further regularity; no universal theorem or performance guarantee
  is asserted.
- Original finite calculations use synthetic states, a declared finite parameter grid
  and exact small matrices. They are not author-code reproduction, empirical fitting,
  benchmarking or general consistency proofs.
- 236 pending leads plus other unresolved dispositions remain; discovery continues.
links: []
tags:
- native-concepts
- coding-pseudolikelihood-autonormal
- self-review
- discovery-ongoing
```
