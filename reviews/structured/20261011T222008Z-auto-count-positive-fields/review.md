# Scientific self-review of auto-binomial, auto-Poisson and auto-exponential fields

- Review: 20261011T222008Z-auto-count-positive-fields
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T22:18:47Z
- Finished UTC: 2026-10-11T22:20:08Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain three DRAFT finite graphical model families with distinct supports and full conditional laws. Base measures, symmetric compatibility, interaction signs and properness restrictions are supported with explicit source and finite-model scope. No actionable curation finding remains in this selected batch.

## Scope And Provenance

All fields of three selected maintained concepts for bounded binomial, unbounded Poisson and nonnegative continuous exponential pairwise fields.

Selection: Exact maintained IDs AutoBinomialMarkovRandomField, AutoPoissonMarkovRandomField and AutoExponentialMarkovRandomField; complete selected batch without sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 41b60b6cfe86df583842fcbdbb236158fe00c526.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:AutoBinomialMarkovRandomField | data/curated/AutoBinomialMarkovRandomField.yaml | maintained | Auto-binomial Markov random field |
| AIMech:AutoPoissonMarkovRandomField | data/curated/AutoPoissonMarkovRandomField.yaml | maintained | Auto-Poisson Markov random field |
| AIMech:AutoExponentialMarkovRandomField | data/curated/AutoExponentialMarkovRandomField.yaml | maintained | Auto-exponential Markov random field |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:AutoBinomialMarkovRandomField, AIMech:AutoPoissonMarkovRandomField, AIMech:AutoExponentialMarkovRandomField | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 94.31s (0:01:34)<br>Checked 442 record(s); 0 failed.<br>Checked 406 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 116 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 113,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:AutoBinomialMarkovRandomField, AIMech:AutoPoissonMarkovRandomField, AIMech:AutoExponentialMarkovRandomField | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:AutoBinomialMarkovRandomField, AIMech:AutoPoissonMarkovRandomField, AIMech:AutoExponentialMarkovRandomField | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:AutoBinomialMarkovRandomField, AIMech:AutoPoissonMarkovRandomField, AIMech:AutoExponentialMarkovRandomField | Command exited 0 with no output. |
| Binomial conditionals, Poisson summability witnesses and exponential rate calculations | passed | True | AIMech:AutoBinomialMarkovRandomField, AIMech:AutoPoissonMarkovRandomField, AIMech:AutoExponentialMarkovRandomField | {"binomial": {"states": 24, "partition_function": "13304", "all_site_conditionals_equal_binomial": true, "interaction_odds": ["2", "1/3"], "base_measure_ratio": ["6", "2"], "incompatible_directed_cross_odds": ["2", "3"]}, "poisson": {"negative_interaction_mass_dominated_by_independent_mass": true, "conditional_successive_mass_ratio": "exp(alpha+beta*y)/(x+1)", "positive_interaction_diagonal_ratios": ["2", "2", "32/9", "8", "512/25", "512/9", "8192/49", "512", "131072/81", "131072/25", "2097152/121", "524288/9"], "bounded_cap": 4, "bounded_partition_function": "8087/36", "bounded_conditional_is_truncated_not_ordinary_poisson": true, "scope": "Finite checks illustrate the analytic domination and divergence arguments; they do not prove general summability by truncation."}, "exponential": {"conditional_rates": ["5/4", "6", "4"], "joint_energy_increment_equals_conditional_rate_times_increment": true, "independent_density_integral_upper_bound": "1/6", "wrong_sign_conditional_rate": "-1/2", "scope": "Positive alpha and nonnegative symmetric gamma give this sufficient finite-model construction; no universal necessity claim about zero-rate boundary parameterizations is made."}} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, limitations, evidence version and AIO direction

evidence: supported. Targets: AIMech:AutoBinomialMarkovRandomField.

The classical auto-binomial construction specifies a joint law for mutually dependent counts, not a collection of independent binomial regressions. Trial counts m_i are fixed nonnegative integer bounds; nondegenerate sites have m_i at least one. When every m_i is one, the model reduces to the binary auto-logistic special case. The general bounded-count family is not identical to that special case, a classification task, a sigmoid activation or a Boltzmann neural architecture with a specified visible/hidden partition. The binomial property is a full-conditional statement; it does not assert binomial marginal laws for interacting sites. No normalized identity match was found across all 442 pinned AIO labels and all scoped synonyms and 403 preceding native IDs, names and aliases. Fixed-string full-checkout searches included ignored and hidden files in worktree and main, yielding 37 and 37 matched lines; all 20 unique contents were read. Hits are citations, contextual statements and discovery leads rather than records of these identities. All 185 semantic label/synonym hits were read. Forty-three fully annotated exact CLASS nodes and outgoing edges were inspected: 38 byte-equivalent to prior inspected nodes and five freshly read. Fifty-four contextual YAMLs comprise 43 generated and 11 native records: 46 byte-verified after prior reading and eight freshly read. Absence is bounded to the pinned snapshot, maintained corpus and inspected semantic neighborhood.

On a finite graph, take X_i in {0,...,m_i}, finite real alpha_i and symmetric beta_ij=beta_ji, with beta_ij=0 on nonedges. The site full conditional is Binomial(m_i,theta_i), where log(theta_i/(1-theta_i))=alpha_i+sum_(j!=i) beta_ij*x_j. Substituting the binomial base measure into the source pairwise representation gives p(x)=Z^(-1)*product_i choose(m_i,x_i)*exp[sum_i alpha_i*x_i+sum_(i&lt;j) beta_ij*x_i*x_j]. Each undirected edge occurs once. Its finite support gives a finite positive Z for finite coefficients of either sign. Conditioning on all other sites yields the stated binomial law, with conditional mean m_i*theta_i. Setting every m_i=1 removes the combinatorial factors and recovers the auto-logistic family; setting all interactions to zero gives independent binomials. Limitations: The combinatorial factors choose(m_i,x_i) are essential when m_i exceeds one. Dropping them changes the site conditionals; a bounded geometric-type energy is not automatically auto-binomial. Finite support permits either sign of a symmetric interaction coefficient, but does not guarantee that a chosen parameterization fits observed counts. Changing trial counts, aggregation scale or support changes the model. The source develops the count construction formally. Its two detailed ecological examples concern binary and Gaussian data, so they are not empirical validation of arbitrary auto-binomial count models. The graph, site supports and any conditioning boundary values must be specified. The construction assumes compatible positive full conditionals on the stated Cartesian support; arbitrary separately fitted regressions or asymmetric neighbor coefficients do not automatically define a joint model. The finite fixed-site model does not by itself specify a random-location point process, temporal causal mechanism, hidden observation layer or infinite-lattice existence theorem. Conditional association does not establish causation. A closed-form site conditional does not make the joint partition function, maximum-likelihood fit or uncertainty calculation trivial. Estimation, sampling and model diagnostics require their own procedures. No author implementation, empirical fit or benchmark was reproduced.

### Identity, definition, mechanism, limitations, evidence version and AIO direction

evidence: supported. Targets: AIMech:AutoPoissonMarkovRandomField.

This record denotes the classical unbounded auto-Poisson joint model. A regression using neighboring counts can resemble its site formula while failing joint compatibility or normalizability. Truncated, Winsorized, transformed-statistic and other modified count graphical models require separate identities; the broad phrase Poisson graphical model is therefore not used as an exact alias. Poisson refers to each full conditional, not necessarily each marginal distribution. A finite count field is also distinct from a Poisson point process with random locations. No normalized identity match was found across all 442 pinned AIO labels and all scoped synonyms and 403 preceding native IDs, names and aliases. Fixed-string full-checkout searches included ignored and hidden files in worktree and main, yielding 37 and 37 matched lines; all 20 unique contents were read. Hits are citations, contextual statements and discovery leads rather than records of these identities. All 185 semantic label/synonym hits were read. Forty-three fully annotated exact CLASS nodes and outgoing edges were inspected: 38 byte-equivalent to prior inspected nodes and five freshly read. Fifty-four contextual YAMLs comprise 43 generated and 11 native records: 46 byte-verified after prior reading and eight freshly read. Absence is bounded to the pinned snapshot, maintained corpus and inspected semantic neighborhood.

For finite real alpha_i and symmetric beta_ij=beta_ji, the full conditional is X_i&#124;X_(-i)~Poisson(mu_i), where mu_i=exp[alpha_i+sum_(j!=i) beta_ij*x_j]. The compatible pairwise mass is p(x)=Z^(-1)*exp[sum_i(alpha_i*x_i-log(x_i!))+sum_(i&lt;j) beta_ij*x_i*x_j] on all nonnegative integer configurations, with zero coefficients on nonedges. For this unrestricted Cartesian support and finite site set, Z is finite if and only if every off-diagonal beta_ij is nonpositive. Sufficiency follows by bounding the interaction factor by one and summing the independent Poisson kernels. A positive coefficient fails summability along a two-site growing-count slice even though every proposed site Poisson conditional is individually normalized. With valid beta_ij, increasing a neighbor count cannot increase the site conditional mean when other neighbors are held fixed; zero interactions yield independent Poisson variables. Limitations: The nonpositive-interaction restriction concerns this unbounded pairwise model and its conditional dependence. It is not a theorem that every marginal pairwise correlation in every count graphical model must be negative. A finite cutoff makes the state space summable but changes the support and site conditionals to truncated laws. A successful truncated calculation or finite Gibbs run cannot certify the original unbounded positive-interaction model. The factorial base measure is part of the model. Omitting it changes conditional count laws and their existence conditions. The source presents a formal validity restriction, not a generic accuracy or efficiency result for ecological or genomic count prediction. Later modified Poisson families are research leads, not silently absorbed into this record. The graph, site supports and any conditioning boundary values must be specified. The construction assumes compatible positive full conditionals on the stated Cartesian support; arbitrary separately fitted regressions or asymmetric neighbor coefficients do not automatically define a joint model. The finite fixed-site model does not by itself specify a random-location point process, temporal causal mechanism, hidden observation layer or infinite-lattice existence theorem. Conditional association does not establish causation. A closed-form site conditional does not make the joint partition function, maximum-likelihood fit or uncertainty calculation trivial. Estimation, sampling and model diagnostics require their own procedures. No author implementation, empirical fit or benchmark was reproduced.

### Identity, definition, mechanism, limitations, evidence version and AIO direction

evidence: supported. Targets: AIMech:AutoExponentialMarkovRandomField.

The record uses the classical positive-baseline auto-exponential construction. Exponential refers to the site conditional probability law, not a generic exponential-family graphical model, an exponential activation or exponential smoothing over time. The rate-interaction sign convention is explicit: nonnegative gamma increases conditional rates and decreases conditional means. These gamma coefficients enter the joint log density with a minus sign, unlike the beta sign used in the auto-Poisson natural parameter. Gamma-shaped conditionals and alternative boundary parameter regimes need separate assessments. Interacting marginal distributions need not themselves be exponential. No normalized identity match was found across all 442 pinned AIO labels and all scoped synonyms and 403 preceding native IDs, names and aliases. Fixed-string full-checkout searches included ignored and hidden files in worktree and main, yielding 37 and 37 matched lines; all 20 unique contents were read. Hits are citations, contextual statements and discovery leads rather than records of these identities. All 185 semantic label/synonym hits were read. Forty-three fully annotated exact CLASS nodes and outgoing edges were inspected: 38 byte-equivalent to prior inspected nodes and five freshly read. Fifty-four contextual YAMLs comprise 43 generated and 11 native records: 46 byte-verified after prior reading and eight freshly read. Absence is bounded to the pinned snapshot, maintained corpus and inspected semantic neighborhood.

On a finite graph with X_i&gt;=0, choose alpha_i&gt;0 and symmetric gamma_ij=gamma_ji&gt;=0, with gamma_ij=0 on nonedges. The full-conditional density is r_i*exp(-r_i*x_i), where r_i=alpha_i+sum_(j!=i) gamma_ij*x_j and the conditional mean is 1/r_i. Combining this conditional form with the source pairwise representation gives p(x)=Z^(-1)*exp[-sum_i alpha_i*x_i-sum_(i&lt;j) gamma_ij*x_i*x_j]. Each edge is counted once. The nonnegative interaction penalty bounds the unnormalized joint density by the product of integrable exp(-alpha_i*x_i) terms, establishing a finite positive Z in this regime. Increasing a neighbor value cannot increase the site conditional mean with other neighbors fixed. Zero interactions reduce the law to independent exponentials. Limitations: The stated positive-baseline, nonnegative-rate-interaction regime is the source-supported construction. It is not asserted to classify every zero-baseline boundary case or every transformed, truncated or gamma-conditional variant. Reversing the rate-interaction sign can make a conditional rate nonpositive somewhere on the unbounded support and invalidate its exponential density. Sign restrictions cannot be transferred unchanged between rate and log-density parameterizations. The full conditional is memoryless as a univariate exponential law at fixed neighbors; this does not supply a temporal evolution model or imply an exponential marginal law after averaging over neighbors. The paper explicitly questions the practical interpretability of this construction and supplies no detailed auto-exponential empirical example. The mathematical model is not a validated mechanism of spatial competition or universal positive-data predictor. The graph, site supports and any conditioning boundary values must be specified. The construction assumes compatible positive full conditionals on the stated Cartesian support; arbitrary separately fitted regressions or asymmetric neighbor coefficients do not automatically define a joint model. The finite fixed-site model does not by itself specify a random-location point process, temporal causal mechanism, hidden observation layer or infinite-lattice existence theorem. Conditional association does not establish causation. A closed-form site conditional does not make the joint partition function, maximum-likelihood fit or uncertainty calculation trivial. Estimation, sampling and model diagnostics require their own procedures. No author implementation, empirical fit or benchmark was reproduced.

### Bounded counts and compatible binomial full conditionals

consistency: supported. Targets: AIMech:AutoBinomialMarkovRandomField.

Retain the auto-binomial model family.

Fixed trial counts define a finite Cartesian support. The symmetric bilinear interaction and binomial base measure produce binomial full conditionals with logistic success probabilities. Exact enumeration checks all conditionals in a 24-state field with unequal trial counts and both interaction signs. Removing combinatorial factors changes a probability ratio from 6 to 2. Directed cross-odds 2 and 3 cannot describe the same positive joint table even though the individual regressions normalize. The m_i=1 auto-logistic special case does not identify the entire bounded-count family with a binary neural architecture. The source ecological examples are not count-model benchmarks.

### Unbounded support and joint summability

consistency: supported. Targets: AIMech:AutoPoissonMarkovRandomField.

Retain the classical auto-Poisson family.

The source explicitly requires nonpositive symmetric interactions on unrestricted nonnegative integer support. Individual site Poisson normalization does not establish joint summability. The source analytic argument and original log(2) interaction witness show diagonal masses that fail to approach zero. Nonpositive interactions have an independent-kernel domination bound. A finite cap produces truncated full conditionals and a different model; finite calculations do not certify an unbounded positive-interaction joint law. Restrictions concern conditional interactions, not a blanket theorem about all marginal correlations. Later modified count families remain pending and are not exact aliases.

### Positive conditional rates and explicit sign convention

consistency: supported. Targets: AIMech:AutoExponentialMarkovRandomField.

Retain the classical positive-baseline auto-exponential family.

The source conditional mean is reciprocal to a linear rate. Positive baseline rates and nonnegative symmetric rate interactions give the stated finite model; interaction terms enter the joint log density with a minus sign. A product-exponential bound proves integrability in this regime, and energy increments recover the full-conditional rates. A reversed coefficient can make a rate negative at an allowed neighbor value. The record makes no universal necessity claim about zero-baseline boundaries, gamma variants or transformed statistics. It distinguishes conditional from marginal distribution names and does not convert univariate memorylessness into a temporal process. The source practical-interpretability reservation remains explicit.

### Directional AIO mappings and neighboring identities

grounding: supported. Targets: AIMech:AutoBinomialMarkovRandomField, AIMech:AutoPoissonMarkovRandomField, AIMech:AutoExponentialMarkovRandomField.

Retain all three native identities with scoped AIO mappings.

All three finite auto-model families map broad to AIO Model and related to the task-scoped ProbabilisticGraphicalModel. The mapping is a curator interpretation of scope, not an upstream assertion. The binomial, Poisson and exponential site laws distinguish bounded counts, unbounded counts and nonnegative continuous values. Their compatible joint laws are not equivalent to GeneralizedLinearModel, LogisticRegression, LinearRegression, SpatialRegression or RegressionAnalysis simply because a full conditional has a regression-like formula. BinaryClassification and MulticlassClassification are prediction tasks; ordered counts and dependent site laws are different identities. BoltzmannMachineNetwork, RestrictedBoltzmannMachine and HopfieldNetwork concern neural constructions, visible/hidden architecture or dynamics. The auto-binomial m_i=1 special case has binary pairwise structure, but this does not make the whole bounded-count family identical to those neural classes. SigmoidFunction, HardSigmoidFunction, ExponentialFunction, ELUFunction and SELUFunction are mathematical functions, not joint probability models. ExponentialSmoothingStateSpaceModel, MarkovChain, AutoregressiveMovingAverage and VectorAutoregression impose temporal structure absent from general finite site graphs. ProbabilisticTopicModel requires latent topic semantics not supplied by a count law. Model alone is broad; MachineLearningTask is generic; TrainingStrategy is preprocessing-scoped. Supervised and unsupervised learning contexts do not determine model identity. BayesianNetwork and CausalGraphicalModel do not preserve undirected graph semantics through arbitrary factorization and supply no causal guarantee. Autoencoder and language-model classes, neural hidden/noise/dropout layers, SparseLearning, CategoryEncodingLayer, Normalization and MaximumLayer do not denote these distributions despite shared vocabulary. The 11 native neighbors distinguish the general MRF, Gaussian field, hidden-state constructions, process regression, parameter estimation, state optimization and sampling. Their contextual reuse does not renew scientific approval.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:AutoBinomialMarkovRandomField, AIMech:AutoPoissonMarkovRandomField, AIMech:AutoExponentialMarkovRandomField. All three use a compatible pairwise graph construction, but binomial sites have finite bounded count support and a combinatorial base measure, Poisson sites have unbounded integer support and factorial base measure, and exponential sites have continuous nonnegative support and rate-based interactions. Their validity regimes and full conditional laws differ. Shared graphical structure does not make these families equivalent. Preserve local identities and directional AIO mappings.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T221644Z-auto-count-positive-fields.json | supports | No normalized identity match was found across all 442 pinned AIO labels and all scoped synonyms and 403 preceding native IDs, names and aliases. Fixed-string full-checkout searches included ignored and hidden files in worktree and main, yielding 37 and 37 matched lines; all 20 unique contents were read. Hits are citations, contextual statements and discovery leads rather than records of these identities. All 185 semantic label/synonym hits were read. Forty-three fully annotated exact CLASS nodes and outgoing edges were inspected: 38 byte-equivalent to prior inspected nodes and five freshly read. Fifty-four contextual YAMLs comprise 43 generated and 11 native records: 46 byte-verified after prior reading and eight freshly read. Absence is bounded to the pinned snapshot, maintained corpus and inspected semantic neighborhood. |
| mapping | sources/aio/aio.json; 43 exact CLASS nodes and outgoing edges, and 185 semantic label/synonym hits in source_analysis.aio_mapping_inspection | supports | All three finite auto-model families map broad to AIO Model and related to the task-scoped ProbabilisticGraphicalModel. The mapping is a curator interpretation of scope, not an upstream assertion. The binomial, Poisson and exponential site laws distinguish bounded counts, unbounded counts and nonnegative continuous values. Their compatible joint laws are not equivalent to GeneralizedLinearModel, LogisticRegression, LinearRegression, SpatialRegression or RegressionAnalysis simply because a full conditional has a regression-like formula. BinaryClassification and MulticlassClassification are prediction tasks; ordered counts and dependent site laws are different identities. BoltzmannMachineNetwork, RestrictedBoltzmannMachine and HopfieldNetwork concern neural constructions, visible/hidden architecture or dynamics. The auto-binomial m_i=1 special case has binary pairwise structure, but this does not make the whole bounded-count family identical to those neural classes. SigmoidFunction, HardSigmoidFunction, ExponentialFunction, ELUFunction and SELUFunction are mathematical functions, not joint probability models. ExponentialSmoothingStateSpaceModel, MarkovChain, AutoregressiveMovingAverage and VectorAutoregression impose temporal structure absent from general finite site graphs. ProbabilisticTopicModel requires latent topic semantics not supplied by a count law. Model alone is broad; MachineLearningTask is generic; TrainingStrategy is preprocessing-scoped. Supervised and unsupervised learning contexts do not determine model identity. BayesianNetwork and CausalGraphicalModel do not preserve undirected graph semantics through arbitrary factorization and supply no causal guarantee. Autoencoder and language-model classes, neural hidden/noise/dropout layers, SparseLearning, CategoryEncodingLayer, Normalization and MaximumLayer do not denote these distributions despite shared vocabulary. The 11 native neighbors distinguish the general MRF, Gaussian field, hidden-state constructions, process regression, parameter estimation, state optimization and sampling. Their contextual reuse does not renew scientific approval. |
| neighbors | research/discovery/20261011T221644Z-auto-count-positive-fields.json; source_analysis.aio_mapping_inspection.native_neighbors and context_reading | supports | Eleven complete native contextual records read or byte-verified after prior full reading: MRF, HMRF, HMT, EM, ICE, ICM, Gibbs sampling, Gaussian-process regression, proper auto-normal fields, pseudolikelihood and coding likelihood estimation. These distinguish probability models, observation layers and estimation/inference procedures. Context reading does not renew scientific approval of these earlier records. |
| finite-boundaries | research/discovery/auto-count-positive-boundaries.py; Exact 24-state binomial field, base measures and conditional cross-odds; Poisson mass ratios and truncation; exponential rate signs and integrability bounds | supports | Original exact calculations enumerate a 24-state three-site binomial field with trial counts (2,3,1), unary odds (2,3,5) and edge odds (2,1/3). The partition function is 13304; every site conditional equals the stated binomial. Omitting the binomial coefficient changes a successive-mass ratio from 6 to 2, and incompatible directed cross-odds 2 versus 3 cannot come from one positive binary joint table. For the unbounded Poisson kernel, exact pointwise ratios reproduce the conditional mean and nonpositive interactions are dominated by the independent kernel. A positive log(2) interaction has diagonal successive-mass ratio 2^(2n+1)/(n+1)^2 at least 2, using the elementary inequality 2^n&gt;=n+1; hence those terms fail to approach zero. A finite cap of 4 instead yields a different finite model with truncated site laws and partition function 8087/36. Exponential energy increments reproduce conditional rates (5/4,6,4), and the nonnegative interaction penalty bounds the unnormalized density integral by 1/6 for baselines (1,2,3). Reversing a rate coefficient gives rate -1/2 at an allowed neighbor value. These finite witnesses and stated analytic bounds are not empirical fitting, author-code reproduction, sampling convergence tests or generic performance evidence. |
| autobinomialmarkovrandomfield-source-0 | https://www.stat.cmu.edu/~brian/720-2007-source/nice%20materials/besag-74-contains-hammersley-clifford.pdf; Sections 3–4.1, printed pp. 197–200 / PDF pp. 7–10, especially Equations (3.1)–(3.3) and (4.1)–(4.6); Section 4.2.3, p. 202 / PDF p. 12; Section 4.3, pp. 202–203 / PDF pp. 12–13 | supports | Spatial Interaction and the Statistical Analysis of Lattice Systems. Journal of the Royal Statistical Society, Series B 36(2):192–225, 1974. The university-hosted 46-page scan includes a JSTOR cover and separately published discussion on pp. 225–236. All 46 pages visually read, including two main figures, 16 tables, discussion figure, references and author reply. Printed page=PDF page+190. The main-paper DOI identifies the cited method sections; discussion has DOI 10.1111/j.2517-6161.1974.tb01000.x. A later online date is not the original publication date. This batch reuses the same hash-verified PDF after the prior complete visual reading and revisits PDF pages 2, 7, 9, 10, 12, 13 and 14. No new PDF download or full extracted-text/OCR reading is claimed. All cited method pages were visually read. The source-analysis notes distinguish main-paper support, discussion context, source restrictions and access/extraction limitations. |
| autopoissonmarkovrandomfield-source-0 | https://www.stat.cmu.edu/~brian/720-2007-source/nice%20materials/besag-74-contains-hammersley-clifford.pdf; Section 4.1, printed pp. 199–200 / PDF pp. 9–10, Equations (4.1)–(4.6); Section 4.2.4, p. 202 / PDF p. 12, conditional mean, joint log mass and summability argument; Section 4.3, pp. 202–203 / PDF pp. 12–13 | supports | Spatial Interaction and the Statistical Analysis of Lattice Systems. Journal of the Royal Statistical Society, Series B 36(2):192–225, 1974. The university-hosted 46-page scan includes a JSTOR cover and separately published discussion on pp. 225–236. All 46 pages visually read, including two main figures, 16 tables, discussion figure, references and author reply. Printed page=PDF page+190. The main-paper DOI identifies the cited method sections; discussion has DOI 10.1111/j.2517-6161.1974.tb01000.x. A later online date is not the original publication date. This batch reuses the same hash-verified PDF after the prior complete visual reading and revisits PDF pages 2, 7, 9, 10, 12, 13 and 14. No new PDF download or full extracted-text/OCR reading is claimed. All cited method pages were visually read. The source-analysis notes distinguish main-paper support, discussion context, source restrictions and access/extraction limitations. |
| autoexponentialmarkovrandomfield-source-0 | https://www.stat.cmu.edu/~brian/720-2007-source/nice%20materials/besag-74-contains-hammersley-clifford.pdf; Section 4.1, printed pp. 199–200 / PDF pp. 9–10, Equations (4.1)–(4.6); Section 4.2.5, p. 202 / PDF p. 12, exponential conditional mean and validity regime; Section 4.3, pp. 202–203 / PDF pp. 12–13 | supports | Spatial Interaction and the Statistical Analysis of Lattice Systems. Journal of the Royal Statistical Society, Series B 36(2):192–225, 1974. The university-hosted 46-page scan includes a JSTOR cover and separately published discussion on pp. 225–236. All 46 pages visually read, including two main figures, 16 tables, discussion figure, references and author reply. Printed page=PDF page+190. The main-paper DOI identifies the cited method sections; discussion has DOI 10.1111/j.2517-6161.1974.tb01000.x. A later online date is not the original publication date. This batch reuses the same hash-verified PDF after the prior complete visual reading and revisits PDF pages 2, 7, 9, 10, 12, 13 and 14. No new PDF download or full extracted-text/OCR reading is claimed. All cited method pages were visually read. The source-analysis notes distinguish main-paper support, discussion context, source restrictions and access/extraction limitations. |

## Limits And Additional Notes

- Adversarial author self-review only; all three records remain DRAFT.
- The 46-page primary scan was completely visually read in the preceding round and reused with its original access time and verified checksum. Seven pages were freshly reread here; no new download or full extracted-text/OCR reading is claimed.
- Publisher metadata supports bibliographic identity, but direct Oxford access failed after a CDN redirect. The complete verified university-hosted PDF supports the record mechanisms; later online dates are not original publication dates.
- The PMC square-root page returned a browser check. Official PMLR abstracts were available. No challenge was bypassed, and no unseen full paper or supplement is claimed as read.
- Five later abstracts are provisional source/frontier context, not inspected full-method evidence or independent empirical validation of these records.
- Original finite checks and explicit analytic inequalities are not author-code reproduction, empirical fitting or generic model-performance evidence. Positive exponential baselines are a stated sufficient construction, not an exhaustive classification of boundary cases.
- 237 pending leads plus other unresolved dispositions remain; discovery continues.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T222008Z-auto-count-positive-fields
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of auto-binomial, auto-Poisson and auto-exponential
  fields
started_at: '2026-10-11T22:18:47Z'
finished_at: '2026-10-11T22:20:08Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed all fields of three
    records against the hash-verified Besag 1974 PDF, fully visually read in the preceding
    round and with seven method/abstract pages freshly reread here. Forty-three annotated
    AIO nodes and 11 native neighbors inform identity and mapping boundaries. Original
    arithmetic and analytic witnesses challenge compatibility, base measures, support
    and normalizability. This is author self-review, not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain three DRAFT finite graphical model families with distinct supports
  and full conditional laws. Base measures, symmetric compatibility, interaction signs
  and properness restrictions are supported with explicit source and finite-model
  scope. No actionable curation finding remains in this selected batch.
source:
  git_revision: 41b60b6cfe86df583842fcbdbb236158fe00c526
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
  - path: data/aio/BinaryClassification.yaml
    sha256: 4c710e70fe7e71227f0c6aa55162a3683f04ebbe6f5a4601bd4c0398329f1481
    role: context
  - path: data/aio/BoltzmannMachineNetwork.yaml
    sha256: 1152d2d85c5c1c408a0420e13f211ed109b12fb289c706ee7449864e91aece03
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
  - path: data/aio/ELUFunction.yaml
    sha256: b9e1186643ec0e53fe86064121607ea1c5b9cb8f32935ecd3f47a2e0a1d9780d
    role: context
  - path: data/aio/EnergyBasedLLM.yaml
    sha256: e9e29aa4f8400ad463dfe058fade876ef36c4a2637e1ebc4b42688116896310b
    role: context
  - path: data/aio/ExponentialFunction.yaml
    sha256: a9e6fe9954dee5c61f799631c1892a99a891468e81e725e584d1a3dc06d84239
    role: context
  - path: data/aio/ExponentialSmoothingStateSpaceModel.yaml
    sha256: e54f9504ddd176b6fc08542cdacb2ab5cdb5a25cec8501ccf071de34881ec79d
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
  - path: data/aio/HardSigmoidFunction.yaml
    sha256: d9a78ced04a24c242291fab0c7a37082572fc33b61f8bab3f3ae6bf8e56640c6
    role: context
  - path: data/aio/HiddenLayer.yaml
    sha256: 945f974c1d298a827086c3439ec3f9ae029380f6d2fa52378eb95ccad1f3b886
    role: context
  - path: data/aio/HopfieldNetwork.yaml
    sha256: 042815574abb3502427a76bb970ab78fd1ef684fa5f807b41c948ddb62e63822
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
  - path: data/aio/MulticlassClassification.yaml
    sha256: dcf165047485763fd91782b9a9ba43202d58f00fd33b8545893a5eae327de171
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
  - path: data/aio/ProbabilisticTopicModel.yaml
    sha256: a3ddfd23b511de967f562e99542d8a89109852359d286a4d707d784359ddfe32
    role: context
  - path: data/aio/RegressionAnalysis.yaml
    sha256: 6f5d48096556a2ec31770aab306219e9020919940b4e80554639cc97aaa94bc6
    role: context
  - path: data/aio/RestrictedBoltzmannMachine.yaml
    sha256: 322fcb3b1f6064d944379ed79ffdcb7360fc2c3edd300c0a5a3f46be1f48df43
    role: context
  - path: data/aio/SELUFunction.yaml
    sha256: 03f46f5941f2dc811c83ffbf1dd52cd15ea7537372f9c5ab2dd1b1ec1f85a352
    role: context
  - path: data/aio/SigmoidFunction.yaml
    sha256: e112ec27a5b6fc9de17cc2d3354b836968b6693c6902cf004b71f05a0aedb193
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
  - path: data/curated/AutoBinomialMarkovRandomField.yaml
    sha256: 603681bffd077f87a3c459b776d7c7ba0e27196edb3998666c0bce4278cfb7d1
    role: target
  - path: data/curated/AutoExponentialMarkovRandomField.yaml
    sha256: 9c385d96d6f32e163ae11fab020827dfcbbcbe07880ed18425fb7223c404ebf2
    role: target
  - path: data/curated/AutoNormalMarkovRandomField.yaml
    sha256: da7cfa897744f9b67bf75a4a8f0ea7748c1a052ed6ef063f0fbceec094e0ec90
    role: context
  - path: data/curated/AutoPoissonMarkovRandomField.yaml
    sha256: c54d99b85a9618652e078124ef40ae66e4744e61dbda5993ac4ffb5d9418f715
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
    role: context
  - path: data/curated/MaximumPseudolikelihoodEstimation.yaml
    sha256: b529f9ae03da6f4c1153a5dcc222342b9eacb0b7496273254ee66b20b366e70c
    role: context
  - path: research/discovery/20261011T221644Z-auto-count-positive-fields.json
    sha256: 22c2fbb62b057a3a603b71cbac939968ad159c8ce17c5cd9c8b01c30750c82e7
    role: context
  - path: research/discovery/auto-count-positive-boundaries.py
    sha256: f0ca145ed163a89a42401d086afe3207c6e19c81a1c1ec6f4aa80c25289e3779
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
- target_id: AIMech:AutoBinomialMarkovRandomField
  path: data/curated/AutoBinomialMarkovRandomField.yaml
  label: Auto-binomial Markov random field
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AutoBinomialMarkovRandomField.yaml
    role: maintained
- target_id: AIMech:AutoPoissonMarkovRandomField
  path: data/curated/AutoPoissonMarkovRandomField.yaml
  label: Auto-Poisson Markov random field
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AutoPoissonMarkovRandomField.yaml
    role: maintained
- target_id: AIMech:AutoExponentialMarkovRandomField
  path: data/curated/AutoExponentialMarkovRandomField.yaml
  label: Auto-exponential Markov random field
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AutoExponentialMarkovRandomField.yaml
    role: maintained
scope:
  description: All fields of three selected maintained concepts for bounded binomial,
    unbounded Poisson and nonnegative continuous exponential pairwise fields.
  selection: Exact maintained IDs AutoBinomialMarkovRandomField, AutoPoissonMarkovRandomField
    and AutoExponentialMarkovRandomField; complete selected batch without sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:AutoBinomialMarkovRandomField
  - AIMech:AutoPoissonMarkovRandomField
  - AIMech:AutoExponentialMarkovRandomField
  exclusions:
  - target: Author implementations, empirical fitting and infinite-system existence
    reason: No author code, parameter fitting, training or benchmark ran. Finite arithmetic
      and stated analytic bounds address specific compatibility and normalizability
      boundaries, not generic empirical performance or infinite-field theorems.
  - target: Previous records, later abstract-only methods and remaining frontier
    reason: Eleven prior native records supply context without renewed scientific
      approval. Five later abstracts inform pending research; their full methods and
      results have not been inspected. 237 pending inspection leads plus other unresolved
      dispositions remain.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:AutoBinomialMarkovRandomField
  - AIMech:AutoPoissonMarkovRandomField
  - AIMech:AutoExponentialMarkovRandomField
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 94.31s (0:01:34)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 406 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 116 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 113,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:AutoBinomialMarkovRandomField
  - AIMech:AutoPoissonMarkovRandomField
  - AIMech:AutoExponentialMarkovRandomField
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
  - AIMech:AutoBinomialMarkovRandomField
  - AIMech:AutoPoissonMarkovRandomField
  - AIMech:AutoExponentialMarkovRandomField
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
  - AIMech:AutoBinomialMarkovRandomField
  - AIMech:AutoPoissonMarkovRandomField
  - AIMech:AutoExponentialMarkovRandomField
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited 0 with no output.
- check_id: finite-arithmetic
  name: Binomial conditionals, Poisson summability witnesses and exponential rate
    calculations
  command: python3 research/discovery/auto-count-positive-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:AutoBinomialMarkovRandomField
  - AIMech:AutoPoissonMarkovRandomField
  - AIMech:AutoExponentialMarkovRandomField
  exit_code: 0
  expected_exit_code: 0
  summary: '{"binomial": {"states": 24, "partition_function": "13304", "all_site_conditionals_equal_binomial":
    true, "interaction_odds": ["2", "1/3"], "base_measure_ratio": ["6", "2"], "incompatible_directed_cross_odds":
    ["2", "3"]}, "poisson": {"negative_interaction_mass_dominated_by_independent_mass":
    true, "conditional_successive_mass_ratio": "exp(alpha+beta*y)/(x+1)", "positive_interaction_diagonal_ratios":
    ["2", "2", "32/9", "8", "512/25", "512/9", "8192/49", "512", "131072/81", "131072/25",
    "2097152/121", "524288/9"], "bounded_cap": 4, "bounded_partition_function": "8087/36",
    "bounded_conditional_is_truncated_not_ordinary_poisson": true, "scope": "Finite
    checks illustrate the analytic domination and divergence arguments; they do not
    prove general summability by truncation."}, "exponential": {"conditional_rates":
    ["5/4", "6", "4"], "joint_energy_increment_equals_conditional_rate_times_increment":
    true, "independent_density_integral_upper_bound": "1/6", "wrong_sign_conditional_rate":
    "-1/2", "scope": "Positive alpha and nonnegative symmetric gamma give this sufficient
    finite-model construction; no universal necessity claim about zero-rate boundary
    parameterizations is made."}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T221644Z-auto-count-positive-fields.json
  accessed_at: '2026-10-11T22:18:47Z'
  support: supports
  summary: 'No normalized identity match was found across all 442 pinned AIO labels
    and all scoped synonyms and 403 preceding native IDs, names and aliases. Fixed-string
    full-checkout searches included ignored and hidden files in worktree and main,
    yielding 37 and 37 matched lines; all 20 unique contents were read. Hits are citations,
    contextual statements and discovery leads rather than records of these identities.
    All 185 semantic label/synonym hits were read. Forty-three fully annotated exact
    CLASS nodes and outgoing edges were inspected: 38 byte-equivalent to prior inspected
    nodes and five freshly read. Fifty-four contextual YAMLs comprise 43 generated
    and 11 native records: 46 byte-verified after prior reading and eight freshly
    read. Absence is bounded to the pinned snapshot, maintained corpus and inspected
    semantic neighborhood.'
  search_scope: 'No normalized identity match was found across all 442 pinned AIO
    labels and all scoped synonyms and 403 preceding native IDs, names and aliases.
    Fixed-string full-checkout searches included ignored and hidden files in worktree
    and main, yielding 37 and 37 matched lines; all 20 unique contents were read.
    Hits are citations, contextual statements and discovery leads rather than records
    of these identities. All 185 semantic label/synonym hits were read. Forty-three
    fully annotated exact CLASS nodes and outgoing edges were inspected: 38 byte-equivalent
    to prior inspected nodes and five freshly read. Fifty-four contextual YAMLs comprise
    43 generated and 11 native records: 46 byte-verified after prior reading and eight
    freshly read. Absence is bounded to the pinned snapshot, maintained corpus and
    inspected semantic neighborhood.'
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: 43 exact CLASS nodes and outgoing edges, and 185 semantic label/synonym
    hits in source_analysis.aio_mapping_inspection
  accessed_at: '2026-10-11T22:18:47Z'
  support: supports
  summary: All three finite auto-model families map broad to AIO Model and related
    to the task-scoped ProbabilisticGraphicalModel. The mapping is a curator interpretation
    of scope, not an upstream assertion. The binomial, Poisson and exponential site
    laws distinguish bounded counts, unbounded counts and nonnegative continuous values.
    Their compatible joint laws are not equivalent to GeneralizedLinearModel, LogisticRegression,
    LinearRegression, SpatialRegression or RegressionAnalysis simply because a full
    conditional has a regression-like formula. BinaryClassification and MulticlassClassification
    are prediction tasks; ordered counts and dependent site laws are different identities.
    BoltzmannMachineNetwork, RestrictedBoltzmannMachine and HopfieldNetwork concern
    neural constructions, visible/hidden architecture or dynamics. The auto-binomial
    m_i=1 special case has binary pairwise structure, but this does not make the whole
    bounded-count family identical to those neural classes. SigmoidFunction, HardSigmoidFunction,
    ExponentialFunction, ELUFunction and SELUFunction are mathematical functions,
    not joint probability models. ExponentialSmoothingStateSpaceModel, MarkovChain,
    AutoregressiveMovingAverage and VectorAutoregression impose temporal structure
    absent from general finite site graphs. ProbabilisticTopicModel requires latent
    topic semantics not supplied by a count law. Model alone is broad; MachineLearningTask
    is generic; TrainingStrategy is preprocessing-scoped. Supervised and unsupervised
    learning contexts do not determine model identity. BayesianNetwork and CausalGraphicalModel
    do not preserve undirected graph semantics through arbitrary factorization and
    supply no causal guarantee. Autoencoder and language-model classes, neural hidden/noise/dropout
    layers, SparseLearning, CategoryEncodingLayer, Normalization and MaximumLayer
    do not denote these distributions despite shared vocabulary. The 11 native neighbors
    distinguish the general MRF, Gaussian field, hidden-state constructions, process
    regression, parameter estimation, state optimization and sampling. Their contextual
    reuse does not renew scientific approval.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T221644Z-auto-count-positive-fields.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors and context_reading
  accessed_at: '2026-10-11T22:18:47Z'
  support: supports
  summary: 'Eleven complete native contextual records read or byte-verified after
    prior full reading: MRF, HMRF, HMT, EM, ICE, ICM, Gibbs sampling, Gaussian-process
    regression, proper auto-normal fields, pseudolikelihood and coding likelihood
    estimation. These distinguish probability models, observation layers and estimation/inference
    procedures. Context reading does not renew scientific approval of these earlier
    records.'
- evidence_id: finite-boundaries
  kind: record_content
  reference: research/discovery/auto-count-positive-boundaries.py
  locator: Exact 24-state binomial field, base measures and conditional cross-odds;
    Poisson mass ratios and truncation; exponential rate signs and integrability bounds
  accessed_at: '2026-10-11T22:18:47Z'
  snapshot_sha256: f0ca145ed163a89a42401d086afe3207c6e19c81a1c1ec6f4aa80c25289e3779
  support: supports
  summary: Original exact calculations enumerate a 24-state three-site binomial field
    with trial counts (2,3,1), unary odds (2,3,5) and edge odds (2,1/3). The partition
    function is 13304; every site conditional equals the stated binomial. Omitting
    the binomial coefficient changes a successive-mass ratio from 6 to 2, and incompatible
    directed cross-odds 2 versus 3 cannot come from one positive binary joint table.
    For the unbounded Poisson kernel, exact pointwise ratios reproduce the conditional
    mean and nonpositive interactions are dominated by the independent kernel. A positive
    log(2) interaction has diagonal successive-mass ratio 2^(2n+1)/(n+1)^2 at least
    2, using the elementary inequality 2^n>=n+1; hence those terms fail to approach
    zero. A finite cap of 4 instead yields a different finite model with truncated
    site laws and partition function 8087/36. Exponential energy increments reproduce
    conditional rates (5/4,6,4), and the nonnegative interaction penalty bounds the
    unnormalized density integral by 1/6 for baselines (1,2,3). Reversing a rate coefficient
    gives rate -1/2 at an allowed neighbor value. These finite witnesses and stated
    analytic bounds are not empirical fitting, author-code reproduction, sampling
    convergence tests or generic performance evidence.
- evidence_id: autobinomialmarkovrandomfield-source-0
  kind: primary_source
  reference: https://www.stat.cmu.edu/~brian/720-2007-source/nice%20materials/besag-74-contains-hammersley-clifford.pdf
  locator: Sections 3–4.1, printed pp. 197–200 / PDF pp. 7–10, especially Equations
    (3.1)–(3.3) and (4.1)–(4.6); Section 4.2.3, p. 202 / PDF p. 12; Section 4.3, pp.
    202–203 / PDF pp. 12–13
  accessed_at: '2026-10-11T21:47:19Z'
  snapshot_sha256: 796199ef5d870e81750cc3fc262f140ccc7114ce916e3a23fc53f36a614bebef
  support: supports
  summary: Spatial Interaction and the Statistical Analysis of Lattice Systems. Journal
    of the Royal Statistical Society, Series B 36(2):192–225, 1974. The university-hosted
    46-page scan includes a JSTOR cover and separately published discussion on pp.
    225–236. All 46 pages visually read, including two main figures, 16 tables, discussion
    figure, references and author reply. Printed page=PDF page+190. The main-paper
    DOI identifies the cited method sections; discussion has DOI 10.1111/j.2517-6161.1974.tb01000.x.
    A later online date is not the original publication date. This batch reuses the
    same hash-verified PDF after the prior complete visual reading and revisits PDF
    pages 2, 7, 9, 10, 12, 13 and 14. No new PDF download or full extracted-text/OCR
    reading is claimed. All cited method pages were visually read. The source-analysis
    notes distinguish main-paper support, discussion context, source restrictions
    and access/extraction limitations.
- evidence_id: autopoissonmarkovrandomfield-source-0
  kind: primary_source
  reference: https://www.stat.cmu.edu/~brian/720-2007-source/nice%20materials/besag-74-contains-hammersley-clifford.pdf
  locator: Section 4.1, printed pp. 199–200 / PDF pp. 9–10, Equations (4.1)–(4.6);
    Section 4.2.4, p. 202 / PDF p. 12, conditional mean, joint log mass and summability
    argument; Section 4.3, pp. 202–203 / PDF pp. 12–13
  accessed_at: '2026-10-11T21:47:19Z'
  snapshot_sha256: 796199ef5d870e81750cc3fc262f140ccc7114ce916e3a23fc53f36a614bebef
  support: supports
  summary: Spatial Interaction and the Statistical Analysis of Lattice Systems. Journal
    of the Royal Statistical Society, Series B 36(2):192–225, 1974. The university-hosted
    46-page scan includes a JSTOR cover and separately published discussion on pp.
    225–236. All 46 pages visually read, including two main figures, 16 tables, discussion
    figure, references and author reply. Printed page=PDF page+190. The main-paper
    DOI identifies the cited method sections; discussion has DOI 10.1111/j.2517-6161.1974.tb01000.x.
    A later online date is not the original publication date. This batch reuses the
    same hash-verified PDF after the prior complete visual reading and revisits PDF
    pages 2, 7, 9, 10, 12, 13 and 14. No new PDF download or full extracted-text/OCR
    reading is claimed. All cited method pages were visually read. The source-analysis
    notes distinguish main-paper support, discussion context, source restrictions
    and access/extraction limitations.
- evidence_id: autoexponentialmarkovrandomfield-source-0
  kind: primary_source
  reference: https://www.stat.cmu.edu/~brian/720-2007-source/nice%20materials/besag-74-contains-hammersley-clifford.pdf
  locator: Section 4.1, printed pp. 199–200 / PDF pp. 9–10, Equations (4.1)–(4.6);
    Section 4.2.5, p. 202 / PDF p. 12, exponential conditional mean and validity regime;
    Section 4.3, pp. 202–203 / PDF pp. 12–13
  accessed_at: '2026-10-11T21:47:19Z'
  snapshot_sha256: 796199ef5d870e81750cc3fc262f140ccc7114ce916e3a23fc53f36a614bebef
  support: supports
  summary: Spatial Interaction and the Statistical Analysis of Lattice Systems. Journal
    of the Royal Statistical Society, Series B 36(2):192–225, 1974. The university-hosted
    46-page scan includes a JSTOR cover and separately published discussion on pp.
    225–236. All 46 pages visually read, including two main figures, 16 tables, discussion
    figure, references and author reply. Printed page=PDF page+190. The main-paper
    DOI identifies the cited method sections; discussion has DOI 10.1111/j.2517-6161.1974.tb01000.x.
    A later online date is not the original publication date. This batch reuses the
    same hash-verified PDF after the prior complete visual reading and revisits PDF
    pages 2, 7, 9, 10, 12, 13 and 14. No new PDF download or full extracted-text/OCR
    reading is claimed. All cited method pages were visually read. The source-analysis
    notes distinguish main-paper support, discussion context, source restrictions
    and access/extraction limitations.
assessments:
- assessment_id: autobinomialmarkovrandomfield
  area: evidence
  topic: Identity, definition, mechanism, limitations, evidence version and AIO direction
  outcome: supported
  target_ids:
  - AIMech:AutoBinomialMarkovRandomField
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - autobinomialmarkovrandomfield-source-0
  summary: 'The classical auto-binomial construction specifies a joint law for mutually
    dependent counts, not a collection of independent binomial regressions. Trial
    counts m_i are fixed nonnegative integer bounds; nondegenerate sites have m_i
    at least one. When every m_i is one, the model reduces to the binary auto-logistic
    special case. The general bounded-count family is not identical to that special
    case, a classification task, a sigmoid activation or a Boltzmann neural architecture
    with a specified visible/hidden partition. The binomial property is a full-conditional
    statement; it does not assert binomial marginal laws for interacting sites. No
    normalized identity match was found across all 442 pinned AIO labels and all scoped
    synonyms and 403 preceding native IDs, names and aliases. Fixed-string full-checkout
    searches included ignored and hidden files in worktree and main, yielding 37 and
    37 matched lines; all 20 unique contents were read. Hits are citations, contextual
    statements and discovery leads rather than records of these identities. All 185
    semantic label/synonym hits were read. Forty-three fully annotated exact CLASS
    nodes and outgoing edges were inspected: 38 byte-equivalent to prior inspected
    nodes and five freshly read. Fifty-four contextual YAMLs comprise 43 generated
    and 11 native records: 46 byte-verified after prior reading and eight freshly
    read. Absence is bounded to the pinned snapshot, maintained corpus and inspected
    semantic neighborhood.'
  details: 'On a finite graph, take X_i in {0,...,m_i}, finite real alpha_i and symmetric
    beta_ij=beta_ji, with beta_ij=0 on nonedges. The site full conditional is Binomial(m_i,theta_i),
    where log(theta_i/(1-theta_i))=alpha_i+sum_(j!=i) beta_ij*x_j. Substituting the
    binomial base measure into the source pairwise representation gives p(x)=Z^(-1)*product_i
    choose(m_i,x_i)*exp[sum_i alpha_i*x_i+sum_(i<j) beta_ij*x_i*x_j]. Each undirected
    edge occurs once. Its finite support gives a finite positive Z for finite coefficients
    of either sign. Conditioning on all other sites yields the stated binomial law,
    with conditional mean m_i*theta_i. Setting every m_i=1 removes the combinatorial
    factors and recovers the auto-logistic family; setting all interactions to zero
    gives independent binomials. Limitations: The combinatorial factors choose(m_i,x_i)
    are essential when m_i exceeds one. Dropping them changes the site conditionals;
    a bounded geometric-type energy is not automatically auto-binomial. Finite support
    permits either sign of a symmetric interaction coefficient, but does not guarantee
    that a chosen parameterization fits observed counts. Changing trial counts, aggregation
    scale or support changes the model. The source develops the count construction
    formally. Its two detailed ecological examples concern binary and Gaussian data,
    so they are not empirical validation of arbitrary auto-binomial count models.
    The graph, site supports and any conditioning boundary values must be specified.
    The construction assumes compatible positive full conditionals on the stated Cartesian
    support; arbitrary separately fitted regressions or asymmetric neighbor coefficients
    do not automatically define a joint model. The finite fixed-site model does not
    by itself specify a random-location point process, temporal causal mechanism,
    hidden observation layer or infinite-lattice existence theorem. Conditional association
    does not establish causation. A closed-form site conditional does not make the
    joint partition function, maximum-likelihood fit or uncertainty calculation trivial.
    Estimation, sampling and model diagnostics require their own procedures. No author
    implementation, empirical fit or benchmark was reproduced.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: Finite pairwise graphical model families distinguished by their site
      supports, full conditional distributions, base measures and compatible parameter
      regimes.
    evidence_ids:
    - autobinomialmarkovrandomfield-source-0
  - name: aio-assessment
    value: broad_match,related_match
    definition: All three finite auto-model families map broad to AIO Model and related
      to the task-scoped ProbabilisticGraphicalModel. The mapping is a curator interpretation
      of scope, not an upstream assertion. The binomial, Poisson and exponential site
      laws distinguish bounded counts, unbounded counts and nonnegative continuous
      values. Their compatible joint laws are not equivalent to GeneralizedLinearModel,
      LogisticRegression, LinearRegression, SpatialRegression or RegressionAnalysis
      simply because a full conditional has a regression-like formula. BinaryClassification
      and MulticlassClassification are prediction tasks; ordered counts and dependent
      site laws are different identities. BoltzmannMachineNetwork, RestrictedBoltzmannMachine
      and HopfieldNetwork concern neural constructions, visible/hidden architecture
      or dynamics. The auto-binomial m_i=1 special case has binary pairwise structure,
      but this does not make the whole bounded-count family identical to those neural
      classes. SigmoidFunction, HardSigmoidFunction, ExponentialFunction, ELUFunction
      and SELUFunction are mathematical functions, not joint probability models. ExponentialSmoothingStateSpaceModel,
      MarkovChain, AutoregressiveMovingAverage and VectorAutoregression impose temporal
      structure absent from general finite site graphs. ProbabilisticTopicModel requires
      latent topic semantics not supplied by a count law. Model alone is broad; MachineLearningTask
      is generic; TrainingStrategy is preprocessing-scoped. Supervised and unsupervised
      learning contexts do not determine model identity. BayesianNetwork and CausalGraphicalModel
      do not preserve undirected graph semantics through arbitrary factorization and
      supply no causal guarantee. Autoencoder and language-model classes, neural hidden/noise/dropout
      layers, SparseLearning, CategoryEncodingLayer, Normalization and MaximumLayer
      do not denote these distributions despite shared vocabulary. The 11 native neighbors
      distinguish the general MRF, Gaussian field, hidden-state constructions, process
      regression, parameter estimation, state optimization and sampling. Their contextual
      reuse does not renew scientific approval.
    evidence_ids:
    - mapping
- assessment_id: autopoissonmarkovrandomfield
  area: evidence
  topic: Identity, definition, mechanism, limitations, evidence version and AIO direction
  outcome: supported
  target_ids:
  - AIMech:AutoPoissonMarkovRandomField
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - autopoissonmarkovrandomfield-source-0
  summary: 'This record denotes the classical unbounded auto-Poisson joint model.
    A regression using neighboring counts can resemble its site formula while failing
    joint compatibility or normalizability. Truncated, Winsorized, transformed-statistic
    and other modified count graphical models require separate identities; the broad
    phrase Poisson graphical model is therefore not used as an exact alias. Poisson
    refers to each full conditional, not necessarily each marginal distribution. A
    finite count field is also distinct from a Poisson point process with random locations.
    No normalized identity match was found across all 442 pinned AIO labels and all
    scoped synonyms and 403 preceding native IDs, names and aliases. Fixed-string
    full-checkout searches included ignored and hidden files in worktree and main,
    yielding 37 and 37 matched lines; all 20 unique contents were read. Hits are citations,
    contextual statements and discovery leads rather than records of these identities.
    All 185 semantic label/synonym hits were read. Forty-three fully annotated exact
    CLASS nodes and outgoing edges were inspected: 38 byte-equivalent to prior inspected
    nodes and five freshly read. Fifty-four contextual YAMLs comprise 43 generated
    and 11 native records: 46 byte-verified after prior reading and eight freshly
    read. Absence is bounded to the pinned snapshot, maintained corpus and inspected
    semantic neighborhood.'
  details: 'For finite real alpha_i and symmetric beta_ij=beta_ji, the full conditional
    is X_i|X_(-i)~Poisson(mu_i), where mu_i=exp[alpha_i+sum_(j!=i) beta_ij*x_j]. The
    compatible pairwise mass is p(x)=Z^(-1)*exp[sum_i(alpha_i*x_i-log(x_i!))+sum_(i<j)
    beta_ij*x_i*x_j] on all nonnegative integer configurations, with zero coefficients
    on nonedges. For this unrestricted Cartesian support and finite site set, Z is
    finite if and only if every off-diagonal beta_ij is nonpositive. Sufficiency follows
    by bounding the interaction factor by one and summing the independent Poisson
    kernels. A positive coefficient fails summability along a two-site growing-count
    slice even though every proposed site Poisson conditional is individually normalized.
    With valid beta_ij, increasing a neighbor count cannot increase the site conditional
    mean when other neighbors are held fixed; zero interactions yield independent
    Poisson variables. Limitations: The nonpositive-interaction restriction concerns
    this unbounded pairwise model and its conditional dependence. It is not a theorem
    that every marginal pairwise correlation in every count graphical model must be
    negative. A finite cutoff makes the state space summable but changes the support
    and site conditionals to truncated laws. A successful truncated calculation or
    finite Gibbs run cannot certify the original unbounded positive-interaction model.
    The factorial base measure is part of the model. Omitting it changes conditional
    count laws and their existence conditions. The source presents a formal validity
    restriction, not a generic accuracy or efficiency result for ecological or genomic
    count prediction. Later modified Poisson families are research leads, not silently
    absorbed into this record. The graph, site supports and any conditioning boundary
    values must be specified. The construction assumes compatible positive full conditionals
    on the stated Cartesian support; arbitrary separately fitted regressions or asymmetric
    neighbor coefficients do not automatically define a joint model. The finite fixed-site
    model does not by itself specify a random-location point process, temporal causal
    mechanism, hidden observation layer or infinite-lattice existence theorem. Conditional
    association does not establish causation. A closed-form site conditional does
    not make the joint partition function, maximum-likelihood fit or uncertainty calculation
    trivial. Estimation, sampling and model diagnostics require their own procedures.
    No author implementation, empirical fit or benchmark was reproduced.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: Finite pairwise graphical model families distinguished by their site
      supports, full conditional distributions, base measures and compatible parameter
      regimes.
    evidence_ids:
    - autopoissonmarkovrandomfield-source-0
  - name: aio-assessment
    value: broad_match,related_match
    definition: All three finite auto-model families map broad to AIO Model and related
      to the task-scoped ProbabilisticGraphicalModel. The mapping is a curator interpretation
      of scope, not an upstream assertion. The binomial, Poisson and exponential site
      laws distinguish bounded counts, unbounded counts and nonnegative continuous
      values. Their compatible joint laws are not equivalent to GeneralizedLinearModel,
      LogisticRegression, LinearRegression, SpatialRegression or RegressionAnalysis
      simply because a full conditional has a regression-like formula. BinaryClassification
      and MulticlassClassification are prediction tasks; ordered counts and dependent
      site laws are different identities. BoltzmannMachineNetwork, RestrictedBoltzmannMachine
      and HopfieldNetwork concern neural constructions, visible/hidden architecture
      or dynamics. The auto-binomial m_i=1 special case has binary pairwise structure,
      but this does not make the whole bounded-count family identical to those neural
      classes. SigmoidFunction, HardSigmoidFunction, ExponentialFunction, ELUFunction
      and SELUFunction are mathematical functions, not joint probability models. ExponentialSmoothingStateSpaceModel,
      MarkovChain, AutoregressiveMovingAverage and VectorAutoregression impose temporal
      structure absent from general finite site graphs. ProbabilisticTopicModel requires
      latent topic semantics not supplied by a count law. Model alone is broad; MachineLearningTask
      is generic; TrainingStrategy is preprocessing-scoped. Supervised and unsupervised
      learning contexts do not determine model identity. BayesianNetwork and CausalGraphicalModel
      do not preserve undirected graph semantics through arbitrary factorization and
      supply no causal guarantee. Autoencoder and language-model classes, neural hidden/noise/dropout
      layers, SparseLearning, CategoryEncodingLayer, Normalization and MaximumLayer
      do not denote these distributions despite shared vocabulary. The 11 native neighbors
      distinguish the general MRF, Gaussian field, hidden-state constructions, process
      regression, parameter estimation, state optimization and sampling. Their contextual
      reuse does not renew scientific approval.
    evidence_ids:
    - mapping
- assessment_id: autoexponentialmarkovrandomfield
  area: evidence
  topic: Identity, definition, mechanism, limitations, evidence version and AIO direction
  outcome: supported
  target_ids:
  - AIMech:AutoExponentialMarkovRandomField
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - autoexponentialmarkovrandomfield-source-0
  summary: 'The record uses the classical positive-baseline auto-exponential construction.
    Exponential refers to the site conditional probability law, not a generic exponential-family
    graphical model, an exponential activation or exponential smoothing over time.
    The rate-interaction sign convention is explicit: nonnegative gamma increases
    conditional rates and decreases conditional means. These gamma coefficients enter
    the joint log density with a minus sign, unlike the beta sign used in the auto-Poisson
    natural parameter. Gamma-shaped conditionals and alternative boundary parameter
    regimes need separate assessments. Interacting marginal distributions need not
    themselves be exponential. No normalized identity match was found across all 442
    pinned AIO labels and all scoped synonyms and 403 preceding native IDs, names
    and aliases. Fixed-string full-checkout searches included ignored and hidden files
    in worktree and main, yielding 37 and 37 matched lines; all 20 unique contents
    were read. Hits are citations, contextual statements and discovery leads rather
    than records of these identities. All 185 semantic label/synonym hits were read.
    Forty-three fully annotated exact CLASS nodes and outgoing edges were inspected:
    38 byte-equivalent to prior inspected nodes and five freshly read. Fifty-four
    contextual YAMLs comprise 43 generated and 11 native records: 46 byte-verified
    after prior reading and eight freshly read. Absence is bounded to the pinned snapshot,
    maintained corpus and inspected semantic neighborhood.'
  details: 'On a finite graph with X_i>=0, choose alpha_i>0 and symmetric gamma_ij=gamma_ji>=0,
    with gamma_ij=0 on nonedges. The full-conditional density is r_i*exp(-r_i*x_i),
    where r_i=alpha_i+sum_(j!=i) gamma_ij*x_j and the conditional mean is 1/r_i. Combining
    this conditional form with the source pairwise representation gives p(x)=Z^(-1)*exp[-sum_i
    alpha_i*x_i-sum_(i<j) gamma_ij*x_i*x_j]. Each edge is counted once. The nonnegative
    interaction penalty bounds the unnormalized joint density by the product of integrable
    exp(-alpha_i*x_i) terms, establishing a finite positive Z in this regime. Increasing
    a neighbor value cannot increase the site conditional mean with other neighbors
    fixed. Zero interactions reduce the law to independent exponentials. Limitations:
    The stated positive-baseline, nonnegative-rate-interaction regime is the source-supported
    construction. It is not asserted to classify every zero-baseline boundary case
    or every transformed, truncated or gamma-conditional variant. Reversing the rate-interaction
    sign can make a conditional rate nonpositive somewhere on the unbounded support
    and invalidate its exponential density. Sign restrictions cannot be transferred
    unchanged between rate and log-density parameterizations. The full conditional
    is memoryless as a univariate exponential law at fixed neighbors; this does not
    supply a temporal evolution model or imply an exponential marginal law after averaging
    over neighbors. The paper explicitly questions the practical interpretability
    of this construction and supplies no detailed auto-exponential empirical example.
    The mathematical model is not a validated mechanism of spatial competition or
    universal positive-data predictor. The graph, site supports and any conditioning
    boundary values must be specified. The construction assumes compatible positive
    full conditionals on the stated Cartesian support; arbitrary separately fitted
    regressions or asymmetric neighbor coefficients do not automatically define a
    joint model. The finite fixed-site model does not by itself specify a random-location
    point process, temporal causal mechanism, hidden observation layer or infinite-lattice
    existence theorem. Conditional association does not establish causation. A closed-form
    site conditional does not make the joint partition function, maximum-likelihood
    fit or uncertainty calculation trivial. Estimation, sampling and model diagnostics
    require their own procedures. No author implementation, empirical fit or benchmark
    was reproduced.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: Finite pairwise graphical model families distinguished by their site
      supports, full conditional distributions, base measures and compatible parameter
      regimes.
    evidence_ids:
    - autoexponentialmarkovrandomfield-source-0
  - name: aio-assessment
    value: broad_match,related_match
    definition: All three finite auto-model families map broad to AIO Model and related
      to the task-scoped ProbabilisticGraphicalModel. The mapping is a curator interpretation
      of scope, not an upstream assertion. The binomial, Poisson and exponential site
      laws distinguish bounded counts, unbounded counts and nonnegative continuous
      values. Their compatible joint laws are not equivalent to GeneralizedLinearModel,
      LogisticRegression, LinearRegression, SpatialRegression or RegressionAnalysis
      simply because a full conditional has a regression-like formula. BinaryClassification
      and MulticlassClassification are prediction tasks; ordered counts and dependent
      site laws are different identities. BoltzmannMachineNetwork, RestrictedBoltzmannMachine
      and HopfieldNetwork concern neural constructions, visible/hidden architecture
      or dynamics. The auto-binomial m_i=1 special case has binary pairwise structure,
      but this does not make the whole bounded-count family identical to those neural
      classes. SigmoidFunction, HardSigmoidFunction, ExponentialFunction, ELUFunction
      and SELUFunction are mathematical functions, not joint probability models. ExponentialSmoothingStateSpaceModel,
      MarkovChain, AutoregressiveMovingAverage and VectorAutoregression impose temporal
      structure absent from general finite site graphs. ProbabilisticTopicModel requires
      latent topic semantics not supplied by a count law. Model alone is broad; MachineLearningTask
      is generic; TrainingStrategy is preprocessing-scoped. Supervised and unsupervised
      learning contexts do not determine model identity. BayesianNetwork and CausalGraphicalModel
      do not preserve undirected graph semantics through arbitrary factorization and
      supply no causal guarantee. Autoencoder and language-model classes, neural hidden/noise/dropout
      layers, SparseLearning, CategoryEncodingLayer, Normalization and MaximumLayer
      do not denote these distributions despite shared vocabulary. The 11 native neighbors
      distinguish the general MRF, Gaussian field, hidden-state constructions, process
      regression, parameter estimation, state optimization and sampling. Their contextual
      reuse does not renew scientific approval.
    evidence_ids:
    - mapping
- assessment_id: binomial-boundary
  area: consistency
  topic: Bounded counts and compatible binomial full conditionals
  outcome: supported
  target_ids:
  - AIMech:AutoBinomialMarkovRandomField
  evidence_ids:
  - autobinomialmarkovrandomfield-source-0
  - finite-boundaries
  - neighbors
  summary: Retain the auto-binomial model family.
  details: Fixed trial counts define a finite Cartesian support. The symmetric bilinear
    interaction and binomial base measure produce binomial full conditionals with
    logistic success probabilities. Exact enumeration checks all conditionals in a
    24-state field with unequal trial counts and both interaction signs. Removing
    combinatorial factors changes a probability ratio from 6 to 2. Directed cross-odds
    2 and 3 cannot describe the same positive joint table even though the individual
    regressions normalize. The m_i=1 auto-logistic special case does not identify
    the entire bounded-count family with a binary neural architecture. The source
    ecological examples are not count-model benchmarks.
- assessment_id: poisson-boundary
  area: consistency
  topic: Unbounded support and joint summability
  outcome: supported
  target_ids:
  - AIMech:AutoPoissonMarkovRandomField
  evidence_ids:
  - autopoissonmarkovrandomfield-source-0
  - finite-boundaries
  - neighbors
  summary: Retain the classical auto-Poisson family.
  details: The source explicitly requires nonpositive symmetric interactions on unrestricted
    nonnegative integer support. Individual site Poisson normalization does not establish
    joint summability. The source analytic argument and original log(2) interaction
    witness show diagonal masses that fail to approach zero. Nonpositive interactions
    have an independent-kernel domination bound. A finite cap produces truncated full
    conditionals and a different model; finite calculations do not certify an unbounded
    positive-interaction joint law. Restrictions concern conditional interactions,
    not a blanket theorem about all marginal correlations. Later modified count families
    remain pending and are not exact aliases.
- assessment_id: exponential-boundary
  area: consistency
  topic: Positive conditional rates and explicit sign convention
  outcome: supported
  target_ids:
  - AIMech:AutoExponentialMarkovRandomField
  evidence_ids:
  - autoexponentialmarkovrandomfield-source-0
  - finite-boundaries
  - neighbors
  summary: Retain the classical positive-baseline auto-exponential family.
  details: The source conditional mean is reciprocal to a linear rate. Positive baseline
    rates and nonnegative symmetric rate interactions give the stated finite model;
    interaction terms enter the joint log density with a minus sign. A product-exponential
    bound proves integrability in this regime, and energy increments recover the full-conditional
    rates. A reversed coefficient can make a rate negative at an allowed neighbor
    value. The record makes no universal necessity claim about zero-baseline boundaries,
    gamma variants or transformed statistics. It distinguishes conditional from marginal
    distribution names and does not convert univariate memorylessness into a temporal
    process. The source practical-interpretability reservation remains explicit.
- assessment_id: mapping-boundary
  area: grounding
  topic: Directional AIO mappings and neighboring identities
  outcome: supported
  target_ids:
  - AIMech:AutoBinomialMarkovRandomField
  - AIMech:AutoPoissonMarkovRandomField
  - AIMech:AutoExponentialMarkovRandomField
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain all three native identities with scoped AIO mappings.
  details: All three finite auto-model families map broad to AIO Model and related
    to the task-scoped ProbabilisticGraphicalModel. The mapping is a curator interpretation
    of scope, not an upstream assertion. The binomial, Poisson and exponential site
    laws distinguish bounded counts, unbounded counts and nonnegative continuous values.
    Their compatible joint laws are not equivalent to GeneralizedLinearModel, LogisticRegression,
    LinearRegression, SpatialRegression or RegressionAnalysis simply because a full
    conditional has a regression-like formula. BinaryClassification and MulticlassClassification
    are prediction tasks; ordered counts and dependent site laws are different identities.
    BoltzmannMachineNetwork, RestrictedBoltzmannMachine and HopfieldNetwork concern
    neural constructions, visible/hidden architecture or dynamics. The auto-binomial
    m_i=1 special case has binary pairwise structure, but this does not make the whole
    bounded-count family identical to those neural classes. SigmoidFunction, HardSigmoidFunction,
    ExponentialFunction, ELUFunction and SELUFunction are mathematical functions,
    not joint probability models. ExponentialSmoothingStateSpaceModel, MarkovChain,
    AutoregressiveMovingAverage and VectorAutoregression impose temporal structure
    absent from general finite site graphs. ProbabilisticTopicModel requires latent
    topic semantics not supplied by a count law. Model alone is broad; MachineLearningTask
    is generic; TrainingStrategy is preprocessing-scoped. Supervised and unsupervised
    learning contexts do not determine model identity. BayesianNetwork and CausalGraphicalModel
    do not preserve undirected graph semantics through arbitrary factorization and
    supply no causal guarantee. Autoencoder and language-model classes, neural hidden/noise/dropout
    layers, SparseLearning, CategoryEncodingLayer, Normalization and MaximumLayer
    do not denote these distributions despite shared vocabulary. The 11 native neighbors
    distinguish the general MRF, Gaussian field, hidden-state constructions, process
    regression, parameter estimation, state optimization and sampling. Their contextual
    reuse does not renew scientific approval.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:AutoBinomialMarkovRandomField
  - AIMech:AutoPoissonMarkovRandomField
  - AIMech:AutoExponentialMarkovRandomField
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - autobinomialmarkovrandomfield-source-0
  - autopoissonmarkovrandomfield-source-0
  - autoexponentialmarkovrandomfield-source-0
  rationale: All three use a compatible pairwise graph construction, but binomial
    sites have finite bounded count support and a combinatorial base measure, Poisson
    sites have unbounded integer support and factorial base measure, and exponential
    sites have continuous nonnegative support and rate-based interactions. Their validity
    regimes and full conditional laws differ. Shared graphical structure does not
    make these families equivalent. Preserve local identities and directional AIO
    mappings.
limitations:
- Adversarial author self-review only; all three records remain DRAFT.
- The 46-page primary scan was completely visually read in the preceding round and
  reused with its original access time and verified checksum. Seven pages were freshly
  reread here; no new download or full extracted-text/OCR reading is claimed.
- Publisher metadata supports bibliographic identity, but direct Oxford access failed
  after a CDN redirect. The complete verified university-hosted PDF supports the record
  mechanisms; later online dates are not original publication dates.
- The PMC square-root page returned a browser check. Official PMLR abstracts were
  available. No challenge was bypassed, and no unseen full paper or supplement is
  claimed as read.
- Five later abstracts are provisional source/frontier context, not inspected full-method
  evidence or independent empirical validation of these records.
- Original finite checks and explicit analytic inequalities are not author-code reproduction,
  empirical fitting or generic model-performance evidence. Positive exponential baselines
  are a stated sufficient construction, not an exhaustive classification of boundary
  cases.
- 237 pending leads plus other unresolved dispositions remain; discovery continues.
links: []
tags:
- native-concepts
- auto-count-positive-fields
- self-review
- discovery-ongoing
```
