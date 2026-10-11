# Scientific self-review of square-root graphical models and Poisson/exponential specializations

- Review: 20261011T224743Z-square-root-graphical-models
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T22:43:27Z
- Finished UTC: 2026-10-11T22:47:43Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the general SQR construction and its distinct Poisson and exponential specializations as DRAFT concepts. Exact support/base-measure differences, root conventions and direct normalization bounds are supported. Specific printed source errors and measure limitations remain explicit. No actionable curation finding remains in the selected batch.

## Scope And Provenance

All fields of the general square-root graphical construction and its Poisson and exponential specializations.

Selection: Exact maintained IDs SquareRootGraphicalModel, PoissonSquareRootGraphicalModel and ExponentialSquareRootGraphicalModel; complete selected batch without sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base b01e15acfe35f2718d7b725f66b27f0b4b63dc4c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SquareRootGraphicalModel | data/curated/SquareRootGraphicalModel.yaml | maintained | Square root graphical model |
| AIMech:PoissonSquareRootGraphicalModel | data/curated/PoissonSquareRootGraphicalModel.yaml | maintained | Poisson square root graphical model |
| AIMech:ExponentialSquareRootGraphicalModel | data/curated/ExponentialSquareRootGraphicalModel.yaml | maintained | Exponential square root graphical model |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:SquareRootGraphicalModel, AIMech:PoissonSquareRootGraphicalModel, AIMech:ExponentialSquareRootGraphicalModel | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 128.16s (0:02:08)<br>Checked 442 record(s); 0 failed.<br>Checked 412 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 118 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 115,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:SquareRootGraphicalModel, AIMech:PoissonSquareRootGraphicalModel, AIMech:ExponentialSquareRootGraphicalModel | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:SquareRootGraphicalModel, AIMech:PoissonSquareRootGraphicalModel, AIMech:ExponentialSquareRootGraphicalModel | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:SquareRootGraphicalModel, AIMech:PoissonSquareRootGraphicalModel, AIMech:ExponentialSquareRootGraphicalModel | Command exited 0 with no output. |
| SQR conditional laws, root conventions, direct normalization, printed normalizer and radial measure | passed | True | AIMech:SquareRootGraphicalModel, AIMech:PoissonSquareRootGraphicalModel, AIMech:ExponentialSquareRootGraphicalModel | {"conditionals": {"full_conditional_energy_increments_verified": true, "poisson_scaled_successive_ratios": [2.718281828459045, 0.8423388801235393, 0.6946650377923315, 0.6286996658179782], "gaussian_signed_root_distinction": true, "binary_indicator_root_is_unchanged": true, "scope": "Finite pointwise checks and algebraic identities; no infinite partition is numerically estimated."}, "exponential": {"strict_orthant_decay": "u^T Phi u &lt;= -(u^2+v^2)/4", "indefinite_but_valid_strict_example": true, "positive_diagonal_fails_strict_condition": true, "uniform_envelope": "exp(sum theta_i^2/(4 epsilon))*exp(-(c-epsilon)*sum x_i), 0&lt;epsilon&lt;c", "printed_independent_exponential_partition": 1.886226925452758, "actual_independent_exponential_partition": 1.0, "zero_linear_negative_root_partition": "1/2", "scope": "The printed conditional partition fails an exact independent special case. Boundary example is one-dimensional; it is not a complete multivariate classification."}, "poisson": {"unrestricted_example_diagonal": ["1", "2"], "unrestricted_example_edge_matrix": "4", "domination_constant": "5", "domination_linear_coefficients": ["7", "9"], "analytic_partition_bound": "Z &lt;= exp(C + sum_i exp(d_i)) &lt; infinity", "independent_poisson_special_case_verified": true, "scope": "Direct factorial domination, not a finite-cutoff estimate or a radial-measure argument."}, "radial_measure": {"jacobian": "z in two dimensions; z^(p-1) in p dimensions", "rate": "2", "actual_joint_partition": "1/4", "ray_kernel_integral_without_jacobian": "1/2", "actual_radius_mean": "1", "exponential_ray_kernel_mean": "1/2", "scope": "The continuous L1 radius of independent exponentials is not distributed as the bare one-dimensional ray kernel. Discrete count directions require a different counting-measure treatment."}} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, limitations, evidence version and AIO direction

evidence: supported. Targets: AIMech:SquareRootGraphicalModel.

SQR denotes the interaction construction of Inouye et al., not a square-root preprocessing pipeline or a radial-basis neural network. Its Poisson and exponential instantiations retain distinct supports, base measures and validity regimes. For ordinary nonnegative statistics the root is nonnegative; the paper explicitly adopts the signed convention s(x)=x when T(x)=x^2 to recover the Gaussian family. That convention is part of the specification, not the identity sqrt(x^2)=x for arbitrary real x. Indicator statistics remain unchanged by their nonnegative root, so the binary/discrete special case is not automatically a new identity. No normalized identity match was found across all 442 pinned AIO labels and all scoped synonyms and 409 preceding native IDs, names and aliases. Fixed-string full-checkout searches included ignored and hidden files in worktree and main, yielding 15 and 12 matched lines; all nine unique contents were read. They describe prior square-root/temporal-square-root leads and publication links, not existing records of these identities. Search preparation included the three preceding modified-count records before their merge; their bytes are retained unchanged. All 186 semantic label/synonym hits were read. Forty-six fully annotated exact CLASS nodes and outgoing edges were inspected: 45 byte-equivalent to prior inspected nodes and one freshly read. Sixty-four contextual YAMLs comprise 46 generated and 18 native records: 59 byte-verified after prior reading and five fully read during this preparation. The three-character SQR acronym was checked in normalized identities and omitted from broad text searches. Absence is bounded to the pinned snapshot, maintained corpus and inspected semantic neighborhood.

For a finite product domain with specified univariate measure mu, log base measure B and nonnegative scalar sufficient statistic T, set s(x)=sqrt(T(x)). The paper makes one explicit signed-root exception: use s(x)=x for T(x)=x^2 on the real line to recover its Gaussian special case. Let Phi be a finite symmetric matrix, including its diagonal. Define p(x)=Z^(-1)*exp[sum_i theta_i*s(x_i)+sum_(i,j) Phi_ij*s(x_i)*s(x_j)+sum_i B(x_i)] with 0&lt;Z&lt;infinity relative to the product measure. The log partition is A=log Z. The site-i full-conditional kernel is exp[Phi_ii*T(t)+(theta_i+2*sum_(j!=i) Phi_ij*s(x_j))*s(t)+B(t)]. Nonedge matrix entries vanish. With theta=0 and diagonal Phi, the law factors into the original independent univariate exponential family at valid diagonal parameters. Normalizability otherwise depends on the chosen base measure and parameter regime. Limitations: This is a construction with an explicit finite-partition requirement, not a theorem that every exponential-family base allows all finite interactions. The unrestricted Poisson case and the restricted continuous exponential case require separate arguments. Using the ordinary nonnegative root of x^2 gives &#124;x&#124; and does not recover a general Gaussian with a linear x term. The documented signed convention is essential for that special case. Several displayed definitions in the source omit log even while calling A a log partition. The record uses Z for the integral or sum and A=log Z, preventing confusion between a normalizer and its logarithm. The graph is finite and Phi is symmetric; an off-diagonal matrix entry contributes twice in the quadratic form. Separately estimated node regressions need not agree on one symmetric joint parameterization. The node conditionals usually have two sufficient statistics and differ from the original univariate base family. A base-family name is not a claim about every conditional or marginal distribution, and an edge parameter is not a universal marginal-correlation or causal-effect statement. The printed radial formulas omit the Jacobian needed to interpret x=z*v as a change of continuous coordinates. In p dimensions the L1-radius transformation contributes z^(p-1); a bare ray kernel is not generally the radius distribution. Discrete directions require a counting-measure treatment. The normalization arguments stated here use direct joint domination instead. The paper proposes nodewise l1-penalized fitting, numerical conditional partitions and annealed importance sampling. Model existence does not establish finite-data graph recovery, sampler mixing, numerical accuracy or optimizer convergence; no author code, empirical fitting or benchmark was reproduced. Reported synthetic and airport-delay experiments are contextual. The paper’s synthetic description prints a positive diagonal while calling the matrix negative definite, an inconsistent sign convention that must be resolved before reproducing that generator. Airport associations and fitted likelihoods do not establish causal effects or held-out predictive performance.

### Identity, definition, mechanism, limitations, evidence version and AIO direction

evidence: supported. Targets: AIMech:PoissonSquareRootGraphicalModel.

Poisson SQR is the Poisson-base specialization of the SQR construction. It preserves the factorial count base measure and changes the interaction statistic to square roots. It is distinct from the classical auto-Poisson field, finite TPGM, factorial-free QPGM and bounded-statistic SPGM. Taking square roots of observed counts and fitting a Gaussian is a different model: the sample space, base measure and conditional law must be retained. No normalized identity match was found across all 442 pinned AIO labels and all scoped synonyms and 409 preceding native IDs, names and aliases. Fixed-string full-checkout searches included ignored and hidden files in worktree and main, yielding 15 and 12 matched lines; all nine unique contents were read. They describe prior square-root/temporal-square-root leads and publication links, not existing records of these identities. Search preparation included the three preceding modified-count records before their merge; their bytes are retained unchanged. All 186 semantic label/synonym hits were read. Forty-six fully annotated exact CLASS nodes and outgoing edges were inspected: 45 byte-equivalent to prior inspected nodes and one freshly read. Sixty-four contextual YAMLs comprise 46 generated and 18 native records: 59 byte-verified after prior reading and five fully read during this preparation. The three-character SQR acronym was checked in normalized identities and omitted from broad text searches. Absence is bounded to the pinned snapshot, maintained corpus and inspected semantic neighborhood.

For X_i in {0,1,...}, a finite symmetric matrix Phi and finite theta, define p(x)=Z^(-1)*exp[sum_i theta_i*sqrt(x_i)+sum_i Phi_ii*x_i+2*sum_(i&lt;j) Phi_ij*sqrt(x_i*x_j)-sum_i log(x_i!)]. The full conditional at i is proportional to exp[Phi_ii*k+eta_i*sqrt(k)]/k!, k&gt;=0, where eta_i=theta_i+2*sum_(j!=i) Phi_ij*sqrt(x_j). All finite parameters are admissible on a finite graph. To see this directly, use 2*sqrt(x_i*x_j)&lt;=x_i+x_j and sqrt(x_i)&lt;=1+x_i to bound the parameter-dependent exponent by C+sum_i d_i*x_i for finite C,d_i. The joint kernel is then bounded by exp(C)*product_i exp(d_i*x_i)/x_i!, whose sum is exp(C+sum_i exp(d_i)). For theta=0 and diagonal Phi, the independent Poisson means are exp(Phi_ii). For nonzero eta_i the conditional is generally not an ordinary Poisson law. Limitations: The factorial base measure is essential to the unrestricted finite-parameter normalization result. Removing it or changing support requires a new validity analysis. No statement about infinite graphs or unbounded parameter limits follows. The conditional normalizer is generally an infinite sum, and existence alone does not certify any cutoff or numerical approximation. exp(eta_i) is not its general conditional mean. The direct factorial-domination argument avoids treating the paper’s directional summations as a complete change-of-measure proof. It is a curator derivation consistent with the stated finite-parameter model, not an empirical reproduction. The graph is finite and Phi is symmetric; an off-diagonal matrix entry contributes twice in the quadratic form. Separately estimated node regressions need not agree on one symmetric joint parameterization. The node conditionals usually have two sufficient statistics and differ from the original univariate base family. A base-family name is not a claim about every conditional or marginal distribution, and an edge parameter is not a universal marginal-correlation or causal-effect statement. The printed radial formulas omit the Jacobian needed to interpret x=z*v as a change of continuous coordinates. In p dimensions the L1-radius transformation contributes z^(p-1); a bare ray kernel is not generally the radius distribution. Discrete directions require a counting-measure treatment. The normalization arguments stated here use direct joint domination instead. The paper proposes nodewise l1-penalized fitting, numerical conditional partitions and annealed importance sampling. Model existence does not establish finite-data graph recovery, sampler mixing, numerical accuracy or optimizer convergence; no author code, empirical fitting or benchmark was reproduced. Reported synthetic and airport-delay experiments are contextual. The paper’s synthetic description prints a positive diagonal while calling the matrix negative definite, an inconsistent sign convention that must be resolved before reproducing that generator. Airport associations and fitted likelihoods do not establish causal effects or held-out predictive performance.

### Identity, definition, mechanism, limitations, evidence version and AIO direction

evidence: supported. Targets: AIMech:ExponentialSquareRootGraphicalModel.

Exponential SQR is the continuous exponential-base specialization of SQR, not the classical auto-exponential model with bilinear raw-variable interactions and exponential full conditionals. It is also distinct from Poisson SQR because it uses Lebesgue measure without factorial weights. The change of variables y_i=sqrt(x_i) introduces a product Jacobian, so the resulting law is not simply a truncated Gaussian on y. No normalized identity match was found across all 442 pinned AIO labels and all scoped synonyms and 409 preceding native IDs, names and aliases. Fixed-string full-checkout searches included ignored and hidden files in worktree and main, yielding 15 and 12 matched lines; all nine unique contents were read. They describe prior square-root/temporal-square-root leads and publication links, not existing records of these identities. Search preparation included the three preceding modified-count records before their merge; their bytes are retained unchanged. All 186 semantic label/synonym hits were read. Forty-six fully annotated exact CLASS nodes and outgoing edges were inspected: 45 byte-equivalent to prior inspected nodes and one freshly read. Sixty-four contextual YAMLs comprise 46 generated and 18 native records: 59 byte-verified after prior reading and five fully read during this preparation. The three-character SQR acronym was checked in normalized identities and omitted from broad text searches. Absence is bounded to the pinned snapshot, maintained corpus and inspected semantic neighborhood.

On X_i&gt;=0 relative to product Lebesgue measure, define p(x)=Z^(-1)*exp[sum_i theta_i*sqrt(x_i)+sum_i Phi_ii*x_i+2*sum_(i&lt;j) Phi_ij*sqrt(x_i*x_j)], with symmetric Phi and finite positive Z. The site conditional has kernel exp[Phi_ii*t+eta_i*sqrt(t)], t&gt;=0, with eta_i=theta_i+2*sum_(j!=i) Phi_ij*sqrt(x_j). A sufficient regime for every finite theta is u^T Phi u&lt;0 for every nonzero u&gt;=0. Continuity on the compact nonnegative unit sphere then gives u^T Phi u&lt;=-c*&#124;&#124;u&#124;&#124;^2 for some c&gt;0. With u_i=sqrt(x_i), Young’s inequality bounds theta_i*u_i by epsilon*x_i+theta_i^2/(4*epsilon), where 0&lt;epsilon&lt;c; the joint kernel is dominated by an integrable constant times exp[-(c-epsilon)*sum_i x_i]. Whole-space negative definiteness is sufficient, not necessary. With theta=0 and diagonal negative Phi, the variables are independent exponentials of rates -Phi_ii. Flat quadratic boundary cases require separate linear-in-root tail analysis. Limitations: Strict negativity on nonnegative directions is sufficient, not an exhaustive characterization of boundary parameters. For example, in one dimension Phi=0 and theta&lt;0 still gives a finite integral 2/theta^2. This example does not classify all multivariate boundary cases. An indefinite matrix can satisfy the restricted negative-quadratic condition. A positive-definite matrix cannot; the paper’s speculation to that effect is not adopted. Its condition includes coordinate axes and therefore requires negative diagonals in the strict regime. The displayed conditional-partition formula on PDF p. 7 fails its independent exponential special case: at eta1=-1 and eta2=0 it gives a partition of 1+sqrt(pi)/2, whereas the integral of exp(-t) on t&gt;=0 is 1. The record retains the defining integral and the explicit valid tail argument rather than that printed closed form. Outside the independent special case, node conditionals need not be ordinary exponential distributions and their means are not generally reciprocals of simple linear rates. This model does not by itself define a temporal waiting-time process. The graph is finite and Phi is symmetric; an off-diagonal matrix entry contributes twice in the quadratic form. Separately estimated node regressions need not agree on one symmetric joint parameterization. The node conditionals usually have two sufficient statistics and differ from the original univariate base family. A base-family name is not a claim about every conditional or marginal distribution, and an edge parameter is not a universal marginal-correlation or causal-effect statement. The printed radial formulas omit the Jacobian needed to interpret x=z*v as a change of continuous coordinates. In p dimensions the L1-radius transformation contributes z^(p-1); a bare ray kernel is not generally the radius distribution. Discrete directions require a counting-measure treatment. The normalization arguments stated here use direct joint domination instead. The paper proposes nodewise l1-penalized fitting, numerical conditional partitions and annealed importance sampling. Model existence does not establish finite-data graph recovery, sampler mixing, numerical accuracy or optimizer convergence; no author code, empirical fitting or benchmark was reproduced. Reported synthetic and airport-delay experiments are contextual. The paper’s synthetic description prints a positive diagonal while calling the matrix negative definite, an inconsistent sign convention that must be resolved before reproducing that generator. Airport associations and fitted likelihoods do not establish causal effects or held-out predictive performance.

### Root conventions, base measures and construction scope

consistency: supported. Targets: AIMech:SquareRootGraphicalModel.

Retain the general SQR model construction.

The joint kernel uses unary roots and a symmetric quadratic form of roots while preserving the univariate log base measure. The diagonal supplies the original sufficient statistic. The record uses the ordinary nonnegative root and makes the paper's signed Gaussian exception explicit, rather than silently treating sqrt(x^2) as x on the real line. Indicator statistics are unchanged, and the Gaussian special case overlaps the existing proper auto-normal family; neither warrants a duplicate subtype record here. Z is the normalizing integral or sum and A=log Z. The finite-partition requirement is explicit, so unrestricted Poisson parameters are not generalized to every base family. Supplementary tail cases are contextual evidence for this general construction.

### Unbounded counts, factorial domination and conditional laws

consistency: supported. Targets: AIMech:PoissonSquareRootGraphicalModel.

Retain Poisson SQR as a distinct specialization.

The record retains unbounded integer support, factorial weights, unary square-root terms, diagonal linear count terms and the factor of two for off-diagonal matrix entries. Direct inequalities bound the parameter exponent by C+sum d_i*x_i, after which independent factorial sums prove finiteness for all finite parameters on a finite graph. This proof avoids the source radial measure and uniformity gaps. Conditional mass ratios generally differ from Poisson ratios when the square-root coefficient is nonzero. The theta=0 diagonal case gives independent Poisson means exp(Phi_ii). Truncated, quadratic, bounded-statistic and raw-count auto-Poisson models have different supports or potentials and are not aliases.

### Continuous measure, strict orthant decay and source-formula qualifications

consistency: supported. Targets: AIMech:ExponentialSquareRootGraphicalModel.

Retain exponential SQR as a distinct specialization.

The continuous kernel has no factorial weights. Strict negativity on nonnegative directions gives a uniform quadratic bound by compactness; Young's inequality then yields an integrable product-exponential envelope for any finite theta. Whole-space negative definiteness is sufficient, but an indefinite example also works. Positive definiteness cannot satisfy negative values on these directions. The record preserves one-dimensional flat-quadratic boundary examples without claiming a complete multivariate classification. The printed conditional partition formula fails at eta1=-1,eta2=0, producing approximately 1.886 instead of 1; the defining integral is retained. The synthetic positive-diagonal description is inconsistent with its negative-definite claim and is not reproduced as valid.

### Ray kernels versus distributions under a coordinate change

consistency: supported. Targets: AIMech:SquareRootGraphicalModel, AIMech:PoissonSquareRootGraphicalModel, AIMech:ExponentialSquareRootGraphicalModel.

Keep radial-measure limitations explicit.

For the continuous L1 transformation x=z*v, the Jacobian contributes z^(p-1). An exact two-dimensional rate-2 independent exponential example has joint partition 1/4 with the factor and 1/2 without it. Thus the bare ray kernel is not the conditional distribution of radius under the transformed joint law. Discrete count directions require separate counting-measure treatment. The records use direct joint domination and do not elevate the bounded-direction-set argument to a universal normalizability theorem.

### Directional AIO mappings and neighboring identities

grounding: supported. Targets: AIMech:SquareRootGraphicalModel, AIMech:PoissonSquareRootGraphicalModel, AIMech:ExponentialSquareRootGraphicalModel.

Retain all three native identities with scoped AIO mappings.

The general SQR construction, Poisson specialization and exponential specialization each map broad to Model and related to the task-scoped ProbabilisticGraphicalModel. This is a curator assessment, not an upstream AIO assertion. The general construction is broader than either specialization; integer support with factorial weights and continuous support without those weights distinguish the two named cases. The classical auto-Poisson and auto-exponential families use different raw-variable interactions, while TPGM, QPGM and SPGM respectively change support, quadratic penalties or a bounded statistic. The signed-Gaussian special case is covered by an existing proper auto-normal family rather than asserted as another new record. RadialBasisNetwork uses radial neural activations; a radial normalization argument does not identify SQR with that architecture. GeneralizedLinearModel, LinearRegression, LogisticRegression, SpatialRegression and RegressionAnalysis are regression contexts, while LassoRegression and RidgeRegression do not identify a model merely because its parameters can be fitted with a penalty. BinaryClassification, MulticlassClassification and ProbabilisticTopicModel impose tasks or latent-topic semantics absent from the generic joint law. Boltzmann, restricted Boltzmann and Hopfield classes add particular architectures or dynamics; equality in selected binary cases is not equality of the whole SQR construction. Gaussian neural noise/dropout layers, sigmoid/exponential/ELU/SELU activation functions, preprocessing, normalization and tensor-maximum layers do not define these joint families. Temporal smoothing, autoregressive classes and MarkovChain impose ordering not inherent in an arbitrary undirected graph. BayesianNetwork and CausalGraphicalModel do not preserve the same graph or causal semantics under arbitrary factorization. Language-model, autoencoder, hidden-layer and sparse-representation classes are not justified mappings from a count or continuous base measure. Eighteen native neighbors distinguish general and latent graphical models, classical/modified site laws, Gaussian process regression, estimation, state optimization and sampling. Gibbs and slice algorithms can fit or sample a model without being its identity. Contextual inspection does not renew scientific approval of previous records.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:SquareRootGraphicalModel, AIMech:PoissonSquareRootGraphicalModel, AIMech:ExponentialSquareRootGraphicalModel. The generic SQR construction is broader than either specialization. Poisson SQR has integer support and factorial weights permitting all finite parameters; exponential SQR has continuous measure and requires a joint-integrability regime. Shared root interactions do not make the general family and its distinct specializations equivalent. Preserve all three identities and their directional mappings; do not duplicate the signed-Gaussian or indicator special cases.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T224304Z-square-root-graphical-models.json | supports | No normalized identity match was found across all 442 pinned AIO labels and all scoped synonyms and 409 preceding native IDs, names and aliases. Fixed-string full-checkout searches included ignored and hidden files in worktree and main, yielding 15 and 12 matched lines; all nine unique contents were read. They describe prior square-root/temporal-square-root leads and publication links, not existing records of these identities. Search preparation included the three preceding modified-count records before their merge; their bytes are retained unchanged. All 186 semantic label/synonym hits were read. Forty-six fully annotated exact CLASS nodes and outgoing edges were inspected: 45 byte-equivalent to prior inspected nodes and one freshly read. Sixty-four contextual YAMLs comprise 46 generated and 18 native records: 59 byte-verified after prior reading and five fully read during this preparation. The three-character SQR acronym was checked in normalized identities and omitted from broad text searches. Absence is bounded to the pinned snapshot, maintained corpus and inspected semantic neighborhood. |
| mapping | sources/aio/aio.json; 46 exact CLASS nodes and outgoing edges, and 186 semantic label/synonym hits in source_analysis.aio_mapping_inspection | supports | The general SQR construction, Poisson specialization and exponential specialization each map broad to Model and related to the task-scoped ProbabilisticGraphicalModel. This is a curator assessment, not an upstream AIO assertion. The general construction is broader than either specialization; integer support with factorial weights and continuous support without those weights distinguish the two named cases. The classical auto-Poisson and auto-exponential families use different raw-variable interactions, while TPGM, QPGM and SPGM respectively change support, quadratic penalties or a bounded statistic. The signed-Gaussian special case is covered by an existing proper auto-normal family rather than asserted as another new record. RadialBasisNetwork uses radial neural activations; a radial normalization argument does not identify SQR with that architecture. GeneralizedLinearModel, LinearRegression, LogisticRegression, SpatialRegression and RegressionAnalysis are regression contexts, while LassoRegression and RidgeRegression do not identify a model merely because its parameters can be fitted with a penalty. BinaryClassification, MulticlassClassification and ProbabilisticTopicModel impose tasks or latent-topic semantics absent from the generic joint law. Boltzmann, restricted Boltzmann and Hopfield classes add particular architectures or dynamics; equality in selected binary cases is not equality of the whole SQR construction. Gaussian neural noise/dropout layers, sigmoid/exponential/ELU/SELU activation functions, preprocessing, normalization and tensor-maximum layers do not define these joint families. Temporal smoothing, autoregressive classes and MarkovChain impose ordering not inherent in an arbitrary undirected graph. BayesianNetwork and CausalGraphicalModel do not preserve the same graph or causal semantics under arbitrary factorization. Language-model, autoencoder, hidden-layer and sparse-representation classes are not justified mappings from a count or continuous base measure. Eighteen native neighbors distinguish general and latent graphical models, classical/modified site laws, Gaussian process regression, estimation, state optimization and sampling. Gibbs and slice algorithms can fit or sample a model without being its identity. Contextual inspection does not renew scientific approval of previous records. |
| neighbors | research/discovery/20261011T224304Z-square-root-graphical-models.json; source_analysis.aio_mapping_inspection.native_neighbors and context_reading | supports | Eighteen complete native contextual records read or byte-verified after prior full reading: MRF, HMRF, HMT, EM, ICE, ICM, Gibbs and slice sampling, Gaussian-process regression, proper auto-normal fields, pseudolikelihood, coding likelihood, auto-binomial, auto-Poisson, auto-exponential, truncated Poisson, quadratic Poisson and sublinear Poisson fields. These distinguish probability models, observation layers and estimation/inference procedures. Context reading does not renew scientific approval of these earlier records. |
| finite-boundaries | research/discovery/square-root-boundaries.py; Conditional energy increments and matrix conventions; signed-root and indicator special cases; direct joint normalization; printed exponential normalizer and radial-Jacobian counterexamples | supports | Original pointwise calculations check the factor-of-two matrix convention and both node-conditional energy increments. Nonconstant scaled successive-mass ratios show why a Poisson SQR conditional with a square-root term is not an ordinary Poisson law. The signed Gaussian-root convention differs from absolute value, while binary indicators are unchanged. An explicit positive-interaction quadratic is uniformly negative on nonnegative directions, and an indefinite matrix gives another admissible strict example; positive diagonals fail that regime. Young’s inequality supplies a uniform exponential envelope. At eta1=-1,eta2=0 the printed exponential conditional formula gives 1+sqrt(pi)/2, approximately 1.886, whereas the defining integral is 1. The one-dimensional zero-linear negative-root boundary gives integral 2/b^2. Direct inequalities bound a Poisson SQR kernel by exp(C+sum d_i*x_i)/product(x_i!), proving finite normalization for finite parameters. Finally, the two-dimensional L1-radius transformation has Jacobian z: a rate-2 independent exponential kernel has true joint partition 1/4, compared with 1/2 if that factor is omitted. These are original mathematical witnesses and stated analytic arguments, not author-code reproduction, empirical fitting, infinite-sum numerical certification or general recovery guarantees. |
| squarerootgraphicalmodel-source-0 | https://proceedings.mlr.press/v48/inouye16.pdf; Section 3, PDF p. 3, Equation (3) and root-convention footnote; Section 3.1, pp. 4–5, node conditionals; Section 4, p. 6, discrete and signed-Gaussian special cases; Sections 3.2–3.4, pp. 5–6, normalization and estimation scope | supports | Square Root Graphical Models: Multivariate Generalizations of Univariate Exponential Families that Permit Positive Dependencies. ICML 2016, PMLR 48:2445–2453; official nine-page proceedings PDF. All nine PDF pages, all five figures and the bibliography visually read; extracted text of PDF pages 6 and 7 also read. Locators use PDF pages because printed page numbers are not visible. The separately downloaded author version is comparison context, not substituted for this hashed proceedings file. All cited method pages were visually read. The source-analysis notes distinguish main-paper support, discussion context, source restrictions and access/extraction limitations. |
| squarerootgraphicalmodel-source-1 | https://proceedings.mlr.press/v48/inouye16-supp.pdf; Appendices A–B, supplemental PDF pp. 1–2, base-specific tail arguments and notation differences | context_only | Square Root Graphical Models — Supplementary Material. Official two-page ICML 2016 supplement; both pages visually read. Appendix A reverses the main text’s eta1/eta2 roles: its eta1 multiplies the square root and eta2 the linear term. Some expressions call raw integrals log partitions. Locators and formulas in the records keep explicit conventions. All cited method pages were visually read. The source-analysis notes distinguish main-paper support, discussion context, source restrictions and access/extraction limitations. |
| poissonsquarerootgraphicalmodel-source-0 | https://proceedings.mlr.press/v48/inouye16.pdf; Section 3, PDF pp. 3–4, joint and node-conditional definitions; Section 4.2, p. 7, Poisson SQR and unrestricted finite-parameter normalization; Section 2, pp. 2–3, comparison with modified Poisson fields | supports | Square Root Graphical Models: Multivariate Generalizations of Univariate Exponential Families that Permit Positive Dependencies. ICML 2016, PMLR 48:2445–2453; official nine-page proceedings PDF. All nine PDF pages, all five figures and the bibliography visually read; extracted text of PDF pages 6 and 7 also read. Locators use PDF pages because printed page numbers are not visible. The separately downloaded author version is comparison context, not substituted for this hashed proceedings file. All cited method pages were visually read. The source-analysis notes distinguish main-paper support, discussion context, source restrictions and access/extraction limitations. |
| poissonsquarerootgraphicalmodel-source-1 | https://proceedings.mlr.press/v48/inouye16-supp.pdf; Appendix B, supplemental PDF p. 2, Poisson tail comparison and gamma-ratio asymptotic | supports | Square Root Graphical Models — Supplementary Material. Official two-page ICML 2016 supplement; both pages visually read. Appendix A reverses the main text’s eta1/eta2 roles: its eta1 multiplies the square root and eta2 the linear term. Some expressions call raw integrals log partitions. Locators and formulas in the records keep explicit conventions. All cited method pages were visually read. The source-analysis notes distinguish main-paper support, discussion context, source restrictions and access/extraction limitations. |
| exponentialsquarerootgraphicalmodel-source-0 | https://proceedings.mlr.press/v48/inouye16.pdf; Section 3, PDF pp. 3–4, joint and node-conditional laws; Section 4.1, pp. 6–7, Equation (13), sufficient parameter regime and printed conditional partition; Section 5.1, pp. 7–8, synthetic-description limitation | supports | Square Root Graphical Models: Multivariate Generalizations of Univariate Exponential Families that Permit Positive Dependencies. ICML 2016, PMLR 48:2445–2453; official nine-page proceedings PDF. All nine PDF pages, all five figures and the bibliography visually read; extracted text of PDF pages 6 and 7 also read. Locators use PDF pages because printed page numbers are not visible. The separately downloaded author version is comparison context, not substituted for this hashed proceedings file. All cited method pages were visually read. The source-analysis notes distinguish main-paper support, discussion context, source restrictions and access/extraction limitations. |
| exponentialsquarerootgraphicalmodel-source-1 | https://proceedings.mlr.press/v48/inouye16-supp.pdf; Appendix A, supplemental PDF pp. 1–2, one-dimensional exponential/square-root tail cases; note its reversed parameter order | supports | Square Root Graphical Models — Supplementary Material. Official two-page ICML 2016 supplement; both pages visually read. Appendix A reverses the main text’s eta1/eta2 roles: its eta1 multiplies the square root and eta2 the linear term. Some expressions call raw integrals log partitions. Locators and formulas in the records keep explicit conventions. All cited method pages were visually read. The source-analysis notes distinguish main-paper support, discussion context, source restrictions and access/extraction limitations. |

## Limits And Additional Notes

- Adversarial author self-review only; all records remain DRAFT.
- All nine proceedings PDF pages and both official supplemental pages were visually read. Main extracted text pages 6 and 7 were also read to resolve symbols; no complete extracted-text reading is claimed.
- Both official PDFs downloaded and rendered successfully. The author-hosted 11-page file differs in bytes, but its main pages 1–7 have identical extracted text. All extracted-text differences on later main/appendix pages were read: they adjust citation labels, bibliography and equation numbering/cross-references. No full visual inspection of that alternate file is asserted.
- The displayed exponential conditional normalizer fails an independent special case. The synthetic positive-diagonal description conflicts with negative definiteness. The source radial coordinates omit a required continuous Jacobian and cannot be used as a literal radius law. These limitations are retained; direct finite-graph domination supports the narrower definitions.
- Two initial visual suspicions were corrected after complete extracted-text reading of pages 6 and 7: the Gaussian mean parameter does include mu, and Equation 14 does contain an exponential. Neither mistaken suspicion becomes a record claim.
- Original finite calculations and stated analytic bounds are not author-code reproduction, fitting, benchmark evaluation or a complete classification of boundary parameters. The public author-code landing page was located, but no implementation was read or run.
- The GRM abstract and bibliography/author links provide provisional frontier context. Their full methods have not been read in this round. A bounded erratum search did not establish an author correction; mathematical qualifications are identified as curator calculations.
- All additions remain DRAFT and require saved adversarial author self-review. The discovery frontier remains nonempty.
- The ordinary-root convention and the Poisson unary terms were clarified before this formal review; the review assesses the final inspected bytes.
- The author-file comparison establishes matching extracted method text and read citation/numbering differences, not complete visual equivalence or an independently published erratum.
- 243 pending leads plus other unresolved dispositions remain; discovery continues.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T224743Z-square-root-graphical-models
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of square-root graphical models and Poisson/exponential
  specializations
started_at: '2026-10-11T22:43:27Z'
finished_at: '2026-10-11T22:47:43Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed every field of three
    records against all nine proceedings pages and both supplemental pages, visually
    read in this round, with extracted main pages 6 and 7 read for formula disambiguation.
    Forty-six annotated AIO nodes and 18 native neighbors inform identity and mapping
    boundaries. Original calculations test root conventions, conditional laws, direct
    joint bounds, printed normalization and radial measure. This is author self-review,
    not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the general SQR construction and its distinct Poisson and exponential
  specializations as DRAFT concepts. Exact support/base-measure differences, root
  conventions and direct normalization bounds are supported. Specific printed source
  errors and measure limitations remain explicit. No actionable curation finding remains
  in the selected batch.
source:
  git_revision: b01e15acfe35f2718d7b725f66b27f0b4b63dc4c
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
  - path: data/aio/LassoRegression.yaml
    sha256: c62e7ffd00a16f5a82d514687b094aee5f6796d19a7d16200bdb10498c024949
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
  - path: data/aio/RadialBasisNetwork.yaml
    sha256: 67023f07d0faf5c76e4ef59d1be8b78edf40775223592ab94324607e5403a489
    role: context
  - path: data/aio/RegressionAnalysis.yaml
    sha256: 6f5d48096556a2ec31770aab306219e9020919940b4e80554639cc97aaa94bc6
    role: context
  - path: data/aio/RestrictedBoltzmannMachine.yaml
    sha256: 322fcb3b1f6064d944379ed79ffdcb7360fc2c3edd300c0a5a3f46be1f48df43
    role: context
  - path: data/aio/RidgeRegression.yaml
    sha256: 7ee3be4552041e1ee2194a78eb0cbefe25283907027a6680395973dbf98636bb
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
    role: context
  - path: data/curated/AutoExponentialMarkovRandomField.yaml
    sha256: 9c385d96d6f32e163ae11fab020827dfcbbcbe07880ed18425fb7223c404ebf2
    role: context
  - path: data/curated/AutoNormalMarkovRandomField.yaml
    sha256: da7cfa897744f9b67bf75a4a8f0ea7748c1a052ed6ef063f0fbceec094e0ec90
    role: context
  - path: data/curated/AutoPoissonMarkovRandomField.yaml
    sha256: c54d99b85a9618652e078124ef40ae66e4744e61dbda5993ac4ffb5d9418f715
    role: context
  - path: data/curated/ExpectationMaximization.yaml
    sha256: eab2880f9e6db51aa49135ada0c3f6d1504e947e6f920d0a5913fd7ddbd069c4
    role: context
  - path: data/curated/ExponentialSquareRootGraphicalModel.yaml
    sha256: 3232ba2ac723a29320bec3c7572f53bebc7409d758806aa106be68d441b85965
    role: target
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
  - path: data/curated/PoissonSquareRootGraphicalModel.yaml
    sha256: 958e290563924700f26b69d577fbd1b562a21c052fdbd1565a85c0c08971b4bf
    role: target
  - path: data/curated/QuadraticPoissonGraphicalModel.yaml
    sha256: 04f1aab815e8f5daaefa32be6471d1582159d0a1463a41b36da9d6e9dce5fc34
    role: context
  - path: data/curated/SliceSampling.yaml
    sha256: a87319788a5d2966dd1484b6672a968642fb5514cc6f81184908576304bf6aaa
    role: context
  - path: data/curated/SquareRootGraphicalModel.yaml
    sha256: 34125cf7fce0580e388de4cb4805c18712679fcd842c4bce48cae7a29728b89f
    role: target
  - path: data/curated/SublinearPoissonGraphicalModel.yaml
    sha256: cbf7f98fc65669883f6483ddda096cb6ca1b2d82de6a5bcfbcd6ecf58dce14a7
    role: context
  - path: data/curated/TruncatedPoissonGraphicalModel.yaml
    sha256: e97a5d978fb8f45a4de75ca9d1e5061c68fc956b93d6ca9ec8cfc519d2c08f4a
    role: context
  - path: research/discovery/20261011T224304Z-square-root-graphical-models.json
    sha256: 1c38466f970f8d34a454a36f681b92c0e0b889954b3bd09a6035f781b2d5abcf
    role: context
  - path: research/discovery/square-root-boundaries.py
    sha256: 1d94302c936bc8fa832a91ee0af2d433d50184bd6dd37377049d146f8a92f91c
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
- target_id: AIMech:SquareRootGraphicalModel
  path: data/curated/SquareRootGraphicalModel.yaml
  label: Square root graphical model
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SquareRootGraphicalModel.yaml
    role: maintained
- target_id: AIMech:PoissonSquareRootGraphicalModel
  path: data/curated/PoissonSquareRootGraphicalModel.yaml
  label: Poisson square root graphical model
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PoissonSquareRootGraphicalModel.yaml
    role: maintained
- target_id: AIMech:ExponentialSquareRootGraphicalModel
  path: data/curated/ExponentialSquareRootGraphicalModel.yaml
  label: Exponential square root graphical model
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ExponentialSquareRootGraphicalModel.yaml
    role: maintained
scope:
  description: All fields of the general square-root graphical construction and its
    Poisson and exponential specializations.
  selection: Exact maintained IDs SquareRootGraphicalModel, PoissonSquareRootGraphicalModel
    and ExponentialSquareRootGraphicalModel; complete selected batch without sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:SquareRootGraphicalModel
  - AIMech:PoissonSquareRootGraphicalModel
  - AIMech:ExponentialSquareRootGraphicalModel
  exclusions:
  - target: Author implementations, empirical performance and exhaustive boundary
      classification
    reason: No author code, fitting, training or benchmark ran. Original arithmetic
      and analytic bounds address the stated finite-model definitions and specific
      source qualifications; they do not classify every multivariate boundary parameter
      set or validate generic graph-recovery claims.
  - target: Previous records and pending frontier
    reason: Eighteen native contextual records inform boundaries without renewed scientific
      approval. GRM and related bibliography leads require full-method inspection.
      243 pending leads plus other unresolved dispositions remain.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:SquareRootGraphicalModel
  - AIMech:PoissonSquareRootGraphicalModel
  - AIMech:ExponentialSquareRootGraphicalModel
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 128.16s (0:02:08)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 412 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 118 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 115,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:SquareRootGraphicalModel
  - AIMech:PoissonSquareRootGraphicalModel
  - AIMech:ExponentialSquareRootGraphicalModel
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
  - AIMech:SquareRootGraphicalModel
  - AIMech:PoissonSquareRootGraphicalModel
  - AIMech:ExponentialSquareRootGraphicalModel
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
  - AIMech:SquareRootGraphicalModel
  - AIMech:PoissonSquareRootGraphicalModel
  - AIMech:ExponentialSquareRootGraphicalModel
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited 0 with no output.
- check_id: finite-arithmetic
  name: SQR conditional laws, root conventions, direct normalization, printed normalizer
    and radial measure
  command: python3 research/discovery/square-root-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SquareRootGraphicalModel
  - AIMech:PoissonSquareRootGraphicalModel
  - AIMech:ExponentialSquareRootGraphicalModel
  exit_code: 0
  expected_exit_code: 0
  summary: '{"conditionals": {"full_conditional_energy_increments_verified": true,
    "poisson_scaled_successive_ratios": [2.718281828459045, 0.8423388801235393, 0.6946650377923315,
    0.6286996658179782], "gaussian_signed_root_distinction": true, "binary_indicator_root_is_unchanged":
    true, "scope": "Finite pointwise checks and algebraic identities; no infinite
    partition is numerically estimated."}, "exponential": {"strict_orthant_decay":
    "u^T Phi u <= -(u^2+v^2)/4", "indefinite_but_valid_strict_example": true, "positive_diagonal_fails_strict_condition":
    true, "uniform_envelope": "exp(sum theta_i^2/(4 epsilon))*exp(-(c-epsilon)*sum
    x_i), 0<epsilon<c", "printed_independent_exponential_partition": 1.886226925452758,
    "actual_independent_exponential_partition": 1.0, "zero_linear_negative_root_partition":
    "1/2", "scope": "The printed conditional partition fails an exact independent
    special case. Boundary example is one-dimensional; it is not a complete multivariate
    classification."}, "poisson": {"unrestricted_example_diagonal": ["1", "2"], "unrestricted_example_edge_matrix":
    "4", "domination_constant": "5", "domination_linear_coefficients": ["7", "9"],
    "analytic_partition_bound": "Z <= exp(C + sum_i exp(d_i)) < infinity", "independent_poisson_special_case_verified":
    true, "scope": "Direct factorial domination, not a finite-cutoff estimate or a
    radial-measure argument."}, "radial_measure": {"jacobian": "z in two dimensions;
    z^(p-1) in p dimensions", "rate": "2", "actual_joint_partition": "1/4", "ray_kernel_integral_without_jacobian":
    "1/2", "actual_radius_mean": "1", "exponential_ray_kernel_mean": "1/2", "scope":
    "The continuous L1 radius of independent exponentials is not distributed as the
    bare one-dimensional ray kernel. Discrete count directions require a different
    counting-measure treatment."}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T224304Z-square-root-graphical-models.json
  accessed_at: '2026-10-11T22:43:27Z'
  support: supports
  summary: 'No normalized identity match was found across all 442 pinned AIO labels
    and all scoped synonyms and 409 preceding native IDs, names and aliases. Fixed-string
    full-checkout searches included ignored and hidden files in worktree and main,
    yielding 15 and 12 matched lines; all nine unique contents were read. They describe
    prior square-root/temporal-square-root leads and publication links, not existing
    records of these identities. Search preparation included the three preceding modified-count
    records before their merge; their bytes are retained unchanged. All 186 semantic
    label/synonym hits were read. Forty-six fully annotated exact CLASS nodes and
    outgoing edges were inspected: 45 byte-equivalent to prior inspected nodes and
    one freshly read. Sixty-four contextual YAMLs comprise 46 generated and 18 native
    records: 59 byte-verified after prior reading and five fully read during this
    preparation. The three-character SQR acronym was checked in normalized identities
    and omitted from broad text searches. Absence is bounded to the pinned snapshot,
    maintained corpus and inspected semantic neighborhood.'
  search_scope: 'No normalized identity match was found across all 442 pinned AIO
    labels and all scoped synonyms and 409 preceding native IDs, names and aliases.
    Fixed-string full-checkout searches included ignored and hidden files in worktree
    and main, yielding 15 and 12 matched lines; all nine unique contents were read.
    They describe prior square-root/temporal-square-root leads and publication links,
    not existing records of these identities. Search preparation included the three
    preceding modified-count records before their merge; their bytes are retained
    unchanged. All 186 semantic label/synonym hits were read. Forty-six fully annotated
    exact CLASS nodes and outgoing edges were inspected: 45 byte-equivalent to prior
    inspected nodes and one freshly read. Sixty-four contextual YAMLs comprise 46
    generated and 18 native records: 59 byte-verified after prior reading and five
    fully read during this preparation. The three-character SQR acronym was checked
    in normalized identities and omitted from broad text searches. Absence is bounded
    to the pinned snapshot, maintained corpus and inspected semantic neighborhood.'
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: 46 exact CLASS nodes and outgoing edges, and 186 semantic label/synonym
    hits in source_analysis.aio_mapping_inspection
  accessed_at: '2026-10-11T22:43:27Z'
  support: supports
  summary: The general SQR construction, Poisson specialization and exponential specialization
    each map broad to Model and related to the task-scoped ProbabilisticGraphicalModel.
    This is a curator assessment, not an upstream AIO assertion. The general construction
    is broader than either specialization; integer support with factorial weights
    and continuous support without those weights distinguish the two named cases.
    The classical auto-Poisson and auto-exponential families use different raw-variable
    interactions, while TPGM, QPGM and SPGM respectively change support, quadratic
    penalties or a bounded statistic. The signed-Gaussian special case is covered
    by an existing proper auto-normal family rather than asserted as another new record.
    RadialBasisNetwork uses radial neural activations; a radial normalization argument
    does not identify SQR with that architecture. GeneralizedLinearModel, LinearRegression,
    LogisticRegression, SpatialRegression and RegressionAnalysis are regression contexts,
    while LassoRegression and RidgeRegression do not identify a model merely because
    its parameters can be fitted with a penalty. BinaryClassification, MulticlassClassification
    and ProbabilisticTopicModel impose tasks or latent-topic semantics absent from
    the generic joint law. Boltzmann, restricted Boltzmann and Hopfield classes add
    particular architectures or dynamics; equality in selected binary cases is not
    equality of the whole SQR construction. Gaussian neural noise/dropout layers,
    sigmoid/exponential/ELU/SELU activation functions, preprocessing, normalization
    and tensor-maximum layers do not define these joint families. Temporal smoothing,
    autoregressive classes and MarkovChain impose ordering not inherent in an arbitrary
    undirected graph. BayesianNetwork and CausalGraphicalModel do not preserve the
    same graph or causal semantics under arbitrary factorization. Language-model,
    autoencoder, hidden-layer and sparse-representation classes are not justified
    mappings from a count or continuous base measure. Eighteen native neighbors distinguish
    general and latent graphical models, classical/modified site laws, Gaussian process
    regression, estimation, state optimization and sampling. Gibbs and slice algorithms
    can fit or sample a model without being its identity. Contextual inspection does
    not renew scientific approval of previous records.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T224304Z-square-root-graphical-models.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors and context_reading
  accessed_at: '2026-10-11T22:43:27Z'
  support: supports
  summary: 'Eighteen complete native contextual records read or byte-verified after
    prior full reading: MRF, HMRF, HMT, EM, ICE, ICM, Gibbs and slice sampling, Gaussian-process
    regression, proper auto-normal fields, pseudolikelihood, coding likelihood, auto-binomial,
    auto-Poisson, auto-exponential, truncated Poisson, quadratic Poisson and sublinear
    Poisson fields. These distinguish probability models, observation layers and estimation/inference
    procedures. Context reading does not renew scientific approval of these earlier
    records.'
- evidence_id: finite-boundaries
  kind: record_content
  reference: research/discovery/square-root-boundaries.py
  locator: Conditional energy increments and matrix conventions; signed-root and indicator
    special cases; direct joint normalization; printed exponential normalizer and
    radial-Jacobian counterexamples
  accessed_at: '2026-10-11T22:43:27Z'
  snapshot_sha256: 1d94302c936bc8fa832a91ee0af2d433d50184bd6dd37377049d146f8a92f91c
  support: supports
  summary: 'Original pointwise calculations check the factor-of-two matrix convention
    and both node-conditional energy increments. Nonconstant scaled successive-mass
    ratios show why a Poisson SQR conditional with a square-root term is not an ordinary
    Poisson law. The signed Gaussian-root convention differs from absolute value,
    while binary indicators are unchanged. An explicit positive-interaction quadratic
    is uniformly negative on nonnegative directions, and an indefinite matrix gives
    another admissible strict example; positive diagonals fail that regime. Young’s
    inequality supplies a uniform exponential envelope. At eta1=-1,eta2=0 the printed
    exponential conditional formula gives 1+sqrt(pi)/2, approximately 1.886, whereas
    the defining integral is 1. The one-dimensional zero-linear negative-root boundary
    gives integral 2/b^2. Direct inequalities bound a Poisson SQR kernel by exp(C+sum
    d_i*x_i)/product(x_i!), proving finite normalization for finite parameters. Finally,
    the two-dimensional L1-radius transformation has Jacobian z: a rate-2 independent
    exponential kernel has true joint partition 1/4, compared with 1/2 if that factor
    is omitted. These are original mathematical witnesses and stated analytic arguments,
    not author-code reproduction, empirical fitting, infinite-sum numerical certification
    or general recovery guarantees.'
- evidence_id: squarerootgraphicalmodel-source-0
  kind: primary_source
  reference: https://proceedings.mlr.press/v48/inouye16.pdf
  locator: Section 3, PDF p. 3, Equation (3) and root-convention footnote; Section
    3.1, pp. 4–5, node conditionals; Section 4, p. 6, discrete and signed-Gaussian
    special cases; Sections 3.2–3.4, pp. 5–6, normalization and estimation scope
  accessed_at: '2026-10-11T22:33:38Z'
  snapshot_sha256: e864091d4bed528de7d855d66f63fe667138690d075a339f8562f6413783b7a7
  support: supports
  summary: 'Square Root Graphical Models: Multivariate Generalizations of Univariate
    Exponential Families that Permit Positive Dependencies. ICML 2016, PMLR 48:2445–2453;
    official nine-page proceedings PDF. All nine PDF pages, all five figures and the
    bibliography visually read; extracted text of PDF pages 6 and 7 also read. Locators
    use PDF pages because printed page numbers are not visible. The separately downloaded
    author version is comparison context, not substituted for this hashed proceedings
    file. All cited method pages were visually read. The source-analysis notes distinguish
    main-paper support, discussion context, source restrictions and access/extraction
    limitations.'
- evidence_id: squarerootgraphicalmodel-source-1
  kind: primary_source
  reference: https://proceedings.mlr.press/v48/inouye16-supp.pdf
  locator: Appendices A–B, supplemental PDF pp. 1–2, base-specific tail arguments
    and notation differences
  accessed_at: '2026-10-11T22:33:40Z'
  snapshot_sha256: 0e6e7115b6dcb209090fa36f0b4fa60f6c8f17c4381f313021af53cb22da0f57
  support: context_only
  summary: 'Square Root Graphical Models — Supplementary Material. Official two-page
    ICML 2016 supplement; both pages visually read. Appendix A reverses the main text’s
    eta1/eta2 roles: its eta1 multiplies the square root and eta2 the linear term.
    Some expressions call raw integrals log partitions. Locators and formulas in the
    records keep explicit conventions. All cited method pages were visually read.
    The source-analysis notes distinguish main-paper support, discussion context,
    source restrictions and access/extraction limitations.'
- evidence_id: poissonsquarerootgraphicalmodel-source-0
  kind: primary_source
  reference: https://proceedings.mlr.press/v48/inouye16.pdf
  locator: Section 3, PDF pp. 3–4, joint and node-conditional definitions; Section
    4.2, p. 7, Poisson SQR and unrestricted finite-parameter normalization; Section
    2, pp. 2–3, comparison with modified Poisson fields
  accessed_at: '2026-10-11T22:33:38Z'
  snapshot_sha256: e864091d4bed528de7d855d66f63fe667138690d075a339f8562f6413783b7a7
  support: supports
  summary: 'Square Root Graphical Models: Multivariate Generalizations of Univariate
    Exponential Families that Permit Positive Dependencies. ICML 2016, PMLR 48:2445–2453;
    official nine-page proceedings PDF. All nine PDF pages, all five figures and the
    bibliography visually read; extracted text of PDF pages 6 and 7 also read. Locators
    use PDF pages because printed page numbers are not visible. The separately downloaded
    author version is comparison context, not substituted for this hashed proceedings
    file. All cited method pages were visually read. The source-analysis notes distinguish
    main-paper support, discussion context, source restrictions and access/extraction
    limitations.'
- evidence_id: poissonsquarerootgraphicalmodel-source-1
  kind: primary_source
  reference: https://proceedings.mlr.press/v48/inouye16-supp.pdf
  locator: Appendix B, supplemental PDF p. 2, Poisson tail comparison and gamma-ratio
    asymptotic
  accessed_at: '2026-10-11T22:33:40Z'
  snapshot_sha256: 0e6e7115b6dcb209090fa36f0b4fa60f6c8f17c4381f313021af53cb22da0f57
  support: supports
  summary: 'Square Root Graphical Models — Supplementary Material. Official two-page
    ICML 2016 supplement; both pages visually read. Appendix A reverses the main text’s
    eta1/eta2 roles: its eta1 multiplies the square root and eta2 the linear term.
    Some expressions call raw integrals log partitions. Locators and formulas in the
    records keep explicit conventions. All cited method pages were visually read.
    The source-analysis notes distinguish main-paper support, discussion context,
    source restrictions and access/extraction limitations.'
- evidence_id: exponentialsquarerootgraphicalmodel-source-0
  kind: primary_source
  reference: https://proceedings.mlr.press/v48/inouye16.pdf
  locator: Section 3, PDF pp. 3–4, joint and node-conditional laws; Section 4.1, pp.
    6–7, Equation (13), sufficient parameter regime and printed conditional partition;
    Section 5.1, pp. 7–8, synthetic-description limitation
  accessed_at: '2026-10-11T22:33:38Z'
  snapshot_sha256: e864091d4bed528de7d855d66f63fe667138690d075a339f8562f6413783b7a7
  support: supports
  summary: 'Square Root Graphical Models: Multivariate Generalizations of Univariate
    Exponential Families that Permit Positive Dependencies. ICML 2016, PMLR 48:2445–2453;
    official nine-page proceedings PDF. All nine PDF pages, all five figures and the
    bibliography visually read; extracted text of PDF pages 6 and 7 also read. Locators
    use PDF pages because printed page numbers are not visible. The separately downloaded
    author version is comparison context, not substituted for this hashed proceedings
    file. All cited method pages were visually read. The source-analysis notes distinguish
    main-paper support, discussion context, source restrictions and access/extraction
    limitations.'
- evidence_id: exponentialsquarerootgraphicalmodel-source-1
  kind: primary_source
  reference: https://proceedings.mlr.press/v48/inouye16-supp.pdf
  locator: Appendix A, supplemental PDF pp. 1–2, one-dimensional exponential/square-root
    tail cases; note its reversed parameter order
  accessed_at: '2026-10-11T22:33:40Z'
  snapshot_sha256: 0e6e7115b6dcb209090fa36f0b4fa60f6c8f17c4381f313021af53cb22da0f57
  support: supports
  summary: 'Square Root Graphical Models — Supplementary Material. Official two-page
    ICML 2016 supplement; both pages visually read. Appendix A reverses the main text’s
    eta1/eta2 roles: its eta1 multiplies the square root and eta2 the linear term.
    Some expressions call raw integrals log partitions. Locators and formulas in the
    records keep explicit conventions. All cited method pages were visually read.
    The source-analysis notes distinguish main-paper support, discussion context,
    source restrictions and access/extraction limitations.'
assessments:
- assessment_id: squarerootgraphicalmodel
  area: evidence
  topic: Identity, definition, mechanism, limitations, evidence version and AIO direction
  outcome: supported
  target_ids:
  - AIMech:SquareRootGraphicalModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - squarerootgraphicalmodel-source-0
  - squarerootgraphicalmodel-source-1
  summary: 'SQR denotes the interaction construction of Inouye et al., not a square-root
    preprocessing pipeline or a radial-basis neural network. Its Poisson and exponential
    instantiations retain distinct supports, base measures and validity regimes. For
    ordinary nonnegative statistics the root is nonnegative; the paper explicitly
    adopts the signed convention s(x)=x when T(x)=x^2 to recover the Gaussian family.
    That convention is part of the specification, not the identity sqrt(x^2)=x for
    arbitrary real x. Indicator statistics remain unchanged by their nonnegative root,
    so the binary/discrete special case is not automatically a new identity. No normalized
    identity match was found across all 442 pinned AIO labels and all scoped synonyms
    and 409 preceding native IDs, names and aliases. Fixed-string full-checkout searches
    included ignored and hidden files in worktree and main, yielding 15 and 12 matched
    lines; all nine unique contents were read. They describe prior square-root/temporal-square-root
    leads and publication links, not existing records of these identities. Search
    preparation included the three preceding modified-count records before their merge;
    their bytes are retained unchanged. All 186 semantic label/synonym hits were read.
    Forty-six fully annotated exact CLASS nodes and outgoing edges were inspected:
    45 byte-equivalent to prior inspected nodes and one freshly read. Sixty-four contextual
    YAMLs comprise 46 generated and 18 native records: 59 byte-verified after prior
    reading and five fully read during this preparation. The three-character SQR acronym
    was checked in normalized identities and omitted from broad text searches. Absence
    is bounded to the pinned snapshot, maintained corpus and inspected semantic neighborhood.'
  details: 'For a finite product domain with specified univariate measure mu, log
    base measure B and nonnegative scalar sufficient statistic T, set s(x)=sqrt(T(x)).
    The paper makes one explicit signed-root exception: use s(x)=x for T(x)=x^2 on
    the real line to recover its Gaussian special case. Let Phi be a finite symmetric
    matrix, including its diagonal. Define p(x)=Z^(-1)*exp[sum_i theta_i*s(x_i)+sum_(i,j)
    Phi_ij*s(x_i)*s(x_j)+sum_i B(x_i)] with 0<Z<infinity relative to the product measure.
    The log partition is A=log Z. The site-i full-conditional kernel is exp[Phi_ii*T(t)+(theta_i+2*sum_(j!=i)
    Phi_ij*s(x_j))*s(t)+B(t)]. Nonedge matrix entries vanish. With theta=0 and diagonal
    Phi, the law factors into the original independent univariate exponential family
    at valid diagonal parameters. Normalizability otherwise depends on the chosen
    base measure and parameter regime. Limitations: This is a construction with an
    explicit finite-partition requirement, not a theorem that every exponential-family
    base allows all finite interactions. The unrestricted Poisson case and the restricted
    continuous exponential case require separate arguments. Using the ordinary nonnegative
    root of x^2 gives |x| and does not recover a general Gaussian with a linear x
    term. The documented signed convention is essential for that special case. Several
    displayed definitions in the source omit log even while calling A a log partition.
    The record uses Z for the integral or sum and A=log Z, preventing confusion between
    a normalizer and its logarithm. The graph is finite and Phi is symmetric; an off-diagonal
    matrix entry contributes twice in the quadratic form. Separately estimated node
    regressions need not agree on one symmetric joint parameterization. The node conditionals
    usually have two sufficient statistics and differ from the original univariate
    base family. A base-family name is not a claim about every conditional or marginal
    distribution, and an edge parameter is not a universal marginal-correlation or
    causal-effect statement. The printed radial formulas omit the Jacobian needed
    to interpret x=z*v as a change of continuous coordinates. In p dimensions the
    L1-radius transformation contributes z^(p-1); a bare ray kernel is not generally
    the radius distribution. Discrete directions require a counting-measure treatment.
    The normalization arguments stated here use direct joint domination instead. The
    paper proposes nodewise l1-penalized fitting, numerical conditional partitions
    and annealed importance sampling. Model existence does not establish finite-data
    graph recovery, sampler mixing, numerical accuracy or optimizer convergence; no
    author code, empirical fitting or benchmark was reproduced. Reported synthetic
    and airport-delay experiments are contextual. The paper’s synthetic description
    prints a positive diagonal while calling the matrix negative definite, an inconsistent
    sign convention that must be resolved before reproducing that generator. Airport
    associations and fitted likelihoods do not establish causal effects or held-out
    predictive performance.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: A general finite-graph square-root construction and its distinct integer/factorial
      and continuous/exponential specializations, with explicit parameter-validity
      conditions.
    evidence_ids:
    - squarerootgraphicalmodel-source-0
    - squarerootgraphicalmodel-source-1
  - name: aio-assessment
    value: broad_match,related_match
    definition: The general SQR construction, Poisson specialization and exponential
      specialization each map broad to Model and related to the task-scoped ProbabilisticGraphicalModel.
      This is a curator assessment, not an upstream AIO assertion. The general construction
      is broader than either specialization; integer support with factorial weights
      and continuous support without those weights distinguish the two named cases.
      The classical auto-Poisson and auto-exponential families use different raw-variable
      interactions, while TPGM, QPGM and SPGM respectively change support, quadratic
      penalties or a bounded statistic. The signed-Gaussian special case is covered
      by an existing proper auto-normal family rather than asserted as another new
      record. RadialBasisNetwork uses radial neural activations; a radial normalization
      argument does not identify SQR with that architecture. GeneralizedLinearModel,
      LinearRegression, LogisticRegression, SpatialRegression and RegressionAnalysis
      are regression contexts, while LassoRegression and RidgeRegression do not identify
      a model merely because its parameters can be fitted with a penalty. BinaryClassification,
      MulticlassClassification and ProbabilisticTopicModel impose tasks or latent-topic
      semantics absent from the generic joint law. Boltzmann, restricted Boltzmann
      and Hopfield classes add particular architectures or dynamics; equality in selected
      binary cases is not equality of the whole SQR construction. Gaussian neural
      noise/dropout layers, sigmoid/exponential/ELU/SELU activation functions, preprocessing,
      normalization and tensor-maximum layers do not define these joint families.
      Temporal smoothing, autoregressive classes and MarkovChain impose ordering not
      inherent in an arbitrary undirected graph. BayesianNetwork and CausalGraphicalModel
      do not preserve the same graph or causal semantics under arbitrary factorization.
      Language-model, autoencoder, hidden-layer and sparse-representation classes
      are not justified mappings from a count or continuous base measure. Eighteen
      native neighbors distinguish general and latent graphical models, classical/modified
      site laws, Gaussian process regression, estimation, state optimization and sampling.
      Gibbs and slice algorithms can fit or sample a model without being its identity.
      Contextual inspection does not renew scientific approval of previous records.
    evidence_ids:
    - mapping
- assessment_id: poissonsquarerootgraphicalmodel
  area: evidence
  topic: Identity, definition, mechanism, limitations, evidence version and AIO direction
  outcome: supported
  target_ids:
  - AIMech:PoissonSquareRootGraphicalModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - poissonsquarerootgraphicalmodel-source-0
  - poissonsquarerootgraphicalmodel-source-1
  summary: 'Poisson SQR is the Poisson-base specialization of the SQR construction.
    It preserves the factorial count base measure and changes the interaction statistic
    to square roots. It is distinct from the classical auto-Poisson field, finite
    TPGM, factorial-free QPGM and bounded-statistic SPGM. Taking square roots of observed
    counts and fitting a Gaussian is a different model: the sample space, base measure
    and conditional law must be retained. No normalized identity match was found across
    all 442 pinned AIO labels and all scoped synonyms and 409 preceding native IDs,
    names and aliases. Fixed-string full-checkout searches included ignored and hidden
    files in worktree and main, yielding 15 and 12 matched lines; all nine unique
    contents were read. They describe prior square-root/temporal-square-root leads
    and publication links, not existing records of these identities. Search preparation
    included the three preceding modified-count records before their merge; their
    bytes are retained unchanged. All 186 semantic label/synonym hits were read. Forty-six
    fully annotated exact CLASS nodes and outgoing edges were inspected: 45 byte-equivalent
    to prior inspected nodes and one freshly read. Sixty-four contextual YAMLs comprise
    46 generated and 18 native records: 59 byte-verified after prior reading and five
    fully read during this preparation. The three-character SQR acronym was checked
    in normalized identities and omitted from broad text searches. Absence is bounded
    to the pinned snapshot, maintained corpus and inspected semantic neighborhood.'
  details: 'For X_i in {0,1,...}, a finite symmetric matrix Phi and finite theta,
    define p(x)=Z^(-1)*exp[sum_i theta_i*sqrt(x_i)+sum_i Phi_ii*x_i+2*sum_(i<j) Phi_ij*sqrt(x_i*x_j)-sum_i
    log(x_i!)]. The full conditional at i is proportional to exp[Phi_ii*k+eta_i*sqrt(k)]/k!,
    k>=0, where eta_i=theta_i+2*sum_(j!=i) Phi_ij*sqrt(x_j). All finite parameters
    are admissible on a finite graph. To see this directly, use 2*sqrt(x_i*x_j)<=x_i+x_j
    and sqrt(x_i)<=1+x_i to bound the parameter-dependent exponent by C+sum_i d_i*x_i
    for finite C,d_i. The joint kernel is then bounded by exp(C)*product_i exp(d_i*x_i)/x_i!,
    whose sum is exp(C+sum_i exp(d_i)). For theta=0 and diagonal Phi, the independent
    Poisson means are exp(Phi_ii). For nonzero eta_i the conditional is generally
    not an ordinary Poisson law. Limitations: The factorial base measure is essential
    to the unrestricted finite-parameter normalization result. Removing it or changing
    support requires a new validity analysis. No statement about infinite graphs or
    unbounded parameter limits follows. The conditional normalizer is generally an
    infinite sum, and existence alone does not certify any cutoff or numerical approximation.
    exp(eta_i) is not its general conditional mean. The direct factorial-domination
    argument avoids treating the paper’s directional summations as a complete change-of-measure
    proof. It is a curator derivation consistent with the stated finite-parameter
    model, not an empirical reproduction. The graph is finite and Phi is symmetric;
    an off-diagonal matrix entry contributes twice in the quadratic form. Separately
    estimated node regressions need not agree on one symmetric joint parameterization.
    The node conditionals usually have two sufficient statistics and differ from the
    original univariate base family. A base-family name is not a claim about every
    conditional or marginal distribution, and an edge parameter is not a universal
    marginal-correlation or causal-effect statement. The printed radial formulas omit
    the Jacobian needed to interpret x=z*v as a change of continuous coordinates.
    In p dimensions the L1-radius transformation contributes z^(p-1); a bare ray kernel
    is not generally the radius distribution. Discrete directions require a counting-measure
    treatment. The normalization arguments stated here use direct joint domination
    instead. The paper proposes nodewise l1-penalized fitting, numerical conditional
    partitions and annealed importance sampling. Model existence does not establish
    finite-data graph recovery, sampler mixing, numerical accuracy or optimizer convergence;
    no author code, empirical fitting or benchmark was reproduced. Reported synthetic
    and airport-delay experiments are contextual. The paper’s synthetic description
    prints a positive diagonal while calling the matrix negative definite, an inconsistent
    sign convention that must be resolved before reproducing that generator. Airport
    associations and fitted likelihoods do not establish causal effects or held-out
    predictive performance.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: A general finite-graph square-root construction and its distinct integer/factorial
      and continuous/exponential specializations, with explicit parameter-validity
      conditions.
    evidence_ids:
    - poissonsquarerootgraphicalmodel-source-0
    - poissonsquarerootgraphicalmodel-source-1
  - name: aio-assessment
    value: broad_match,related_match
    definition: The general SQR construction, Poisson specialization and exponential
      specialization each map broad to Model and related to the task-scoped ProbabilisticGraphicalModel.
      This is a curator assessment, not an upstream AIO assertion. The general construction
      is broader than either specialization; integer support with factorial weights
      and continuous support without those weights distinguish the two named cases.
      The classical auto-Poisson and auto-exponential families use different raw-variable
      interactions, while TPGM, QPGM and SPGM respectively change support, quadratic
      penalties or a bounded statistic. The signed-Gaussian special case is covered
      by an existing proper auto-normal family rather than asserted as another new
      record. RadialBasisNetwork uses radial neural activations; a radial normalization
      argument does not identify SQR with that architecture. GeneralizedLinearModel,
      LinearRegression, LogisticRegression, SpatialRegression and RegressionAnalysis
      are regression contexts, while LassoRegression and RidgeRegression do not identify
      a model merely because its parameters can be fitted with a penalty. BinaryClassification,
      MulticlassClassification and ProbabilisticTopicModel impose tasks or latent-topic
      semantics absent from the generic joint law. Boltzmann, restricted Boltzmann
      and Hopfield classes add particular architectures or dynamics; equality in selected
      binary cases is not equality of the whole SQR construction. Gaussian neural
      noise/dropout layers, sigmoid/exponential/ELU/SELU activation functions, preprocessing,
      normalization and tensor-maximum layers do not define these joint families.
      Temporal smoothing, autoregressive classes and MarkovChain impose ordering not
      inherent in an arbitrary undirected graph. BayesianNetwork and CausalGraphicalModel
      do not preserve the same graph or causal semantics under arbitrary factorization.
      Language-model, autoencoder, hidden-layer and sparse-representation classes
      are not justified mappings from a count or continuous base measure. Eighteen
      native neighbors distinguish general and latent graphical models, classical/modified
      site laws, Gaussian process regression, estimation, state optimization and sampling.
      Gibbs and slice algorithms can fit or sample a model without being its identity.
      Contextual inspection does not renew scientific approval of previous records.
    evidence_ids:
    - mapping
- assessment_id: exponentialsquarerootgraphicalmodel
  area: evidence
  topic: Identity, definition, mechanism, limitations, evidence version and AIO direction
  outcome: supported
  target_ids:
  - AIMech:ExponentialSquareRootGraphicalModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - exponentialsquarerootgraphicalmodel-source-0
  - exponentialsquarerootgraphicalmodel-source-1
  summary: 'Exponential SQR is the continuous exponential-base specialization of SQR,
    not the classical auto-exponential model with bilinear raw-variable interactions
    and exponential full conditionals. It is also distinct from Poisson SQR because
    it uses Lebesgue measure without factorial weights. The change of variables y_i=sqrt(x_i)
    introduces a product Jacobian, so the resulting law is not simply a truncated
    Gaussian on y. No normalized identity match was found across all 442 pinned AIO
    labels and all scoped synonyms and 409 preceding native IDs, names and aliases.
    Fixed-string full-checkout searches included ignored and hidden files in worktree
    and main, yielding 15 and 12 matched lines; all nine unique contents were read.
    They describe prior square-root/temporal-square-root leads and publication links,
    not existing records of these identities. Search preparation included the three
    preceding modified-count records before their merge; their bytes are retained
    unchanged. All 186 semantic label/synonym hits were read. Forty-six fully annotated
    exact CLASS nodes and outgoing edges were inspected: 45 byte-equivalent to prior
    inspected nodes and one freshly read. Sixty-four contextual YAMLs comprise 46
    generated and 18 native records: 59 byte-verified after prior reading and five
    fully read during this preparation. The three-character SQR acronym was checked
    in normalized identities and omitted from broad text searches. Absence is bounded
    to the pinned snapshot, maintained corpus and inspected semantic neighborhood.'
  details: 'On X_i>=0 relative to product Lebesgue measure, define p(x)=Z^(-1)*exp[sum_i
    theta_i*sqrt(x_i)+sum_i Phi_ii*x_i+2*sum_(i<j) Phi_ij*sqrt(x_i*x_j)], with symmetric
    Phi and finite positive Z. The site conditional has kernel exp[Phi_ii*t+eta_i*sqrt(t)],
    t>=0, with eta_i=theta_i+2*sum_(j!=i) Phi_ij*sqrt(x_j). A sufficient regime for
    every finite theta is u^T Phi u<0 for every nonzero u>=0. Continuity on the compact
    nonnegative unit sphere then gives u^T Phi u<=-c*||u||^2 for some c>0. With u_i=sqrt(x_i),
    Young’s inequality bounds theta_i*u_i by epsilon*x_i+theta_i^2/(4*epsilon), where
    0<epsilon<c; the joint kernel is dominated by an integrable constant times exp[-(c-epsilon)*sum_i
    x_i]. Whole-space negative definiteness is sufficient, not necessary. With theta=0
    and diagonal negative Phi, the variables are independent exponentials of rates
    -Phi_ii. Flat quadratic boundary cases require separate linear-in-root tail analysis.
    Limitations: Strict negativity on nonnegative directions is sufficient, not an
    exhaustive characterization of boundary parameters. For example, in one dimension
    Phi=0 and theta<0 still gives a finite integral 2/theta^2. This example does not
    classify all multivariate boundary cases. An indefinite matrix can satisfy the
    restricted negative-quadratic condition. A positive-definite matrix cannot; the
    paper’s speculation to that effect is not adopted. Its condition includes coordinate
    axes and therefore requires negative diagonals in the strict regime. The displayed
    conditional-partition formula on PDF p. 7 fails its independent exponential special
    case: at eta1=-1 and eta2=0 it gives a partition of 1+sqrt(pi)/2, whereas the
    integral of exp(-t) on t>=0 is 1. The record retains the defining integral and
    the explicit valid tail argument rather than that printed closed form. Outside
    the independent special case, node conditionals need not be ordinary exponential
    distributions and their means are not generally reciprocals of simple linear rates.
    This model does not by itself define a temporal waiting-time process. The graph
    is finite and Phi is symmetric; an off-diagonal matrix entry contributes twice
    in the quadratic form. Separately estimated node regressions need not agree on
    one symmetric joint parameterization. The node conditionals usually have two sufficient
    statistics and differ from the original univariate base family. A base-family
    name is not a claim about every conditional or marginal distribution, and an edge
    parameter is not a universal marginal-correlation or causal-effect statement.
    The printed radial formulas omit the Jacobian needed to interpret x=z*v as a change
    of continuous coordinates. In p dimensions the L1-radius transformation contributes
    z^(p-1); a bare ray kernel is not generally the radius distribution. Discrete
    directions require a counting-measure treatment. The normalization arguments stated
    here use direct joint domination instead. The paper proposes nodewise l1-penalized
    fitting, numerical conditional partitions and annealed importance sampling. Model
    existence does not establish finite-data graph recovery, sampler mixing, numerical
    accuracy or optimizer convergence; no author code, empirical fitting or benchmark
    was reproduced. Reported synthetic and airport-delay experiments are contextual.
    The paper’s synthetic description prints a positive diagonal while calling the
    matrix negative definite, an inconsistent sign convention that must be resolved
    before reproducing that generator. Airport associations and fitted likelihoods
    do not establish causal effects or held-out predictive performance.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: A general finite-graph square-root construction and its distinct integer/factorial
      and continuous/exponential specializations, with explicit parameter-validity
      conditions.
    evidence_ids:
    - exponentialsquarerootgraphicalmodel-source-0
    - exponentialsquarerootgraphicalmodel-source-1
  - name: aio-assessment
    value: broad_match,related_match
    definition: The general SQR construction, Poisson specialization and exponential
      specialization each map broad to Model and related to the task-scoped ProbabilisticGraphicalModel.
      This is a curator assessment, not an upstream AIO assertion. The general construction
      is broader than either specialization; integer support with factorial weights
      and continuous support without those weights distinguish the two named cases.
      The classical auto-Poisson and auto-exponential families use different raw-variable
      interactions, while TPGM, QPGM and SPGM respectively change support, quadratic
      penalties or a bounded statistic. The signed-Gaussian special case is covered
      by an existing proper auto-normal family rather than asserted as another new
      record. RadialBasisNetwork uses radial neural activations; a radial normalization
      argument does not identify SQR with that architecture. GeneralizedLinearModel,
      LinearRegression, LogisticRegression, SpatialRegression and RegressionAnalysis
      are regression contexts, while LassoRegression and RidgeRegression do not identify
      a model merely because its parameters can be fitted with a penalty. BinaryClassification,
      MulticlassClassification and ProbabilisticTopicModel impose tasks or latent-topic
      semantics absent from the generic joint law. Boltzmann, restricted Boltzmann
      and Hopfield classes add particular architectures or dynamics; equality in selected
      binary cases is not equality of the whole SQR construction. Gaussian neural
      noise/dropout layers, sigmoid/exponential/ELU/SELU activation functions, preprocessing,
      normalization and tensor-maximum layers do not define these joint families.
      Temporal smoothing, autoregressive classes and MarkovChain impose ordering not
      inherent in an arbitrary undirected graph. BayesianNetwork and CausalGraphicalModel
      do not preserve the same graph or causal semantics under arbitrary factorization.
      Language-model, autoencoder, hidden-layer and sparse-representation classes
      are not justified mappings from a count or continuous base measure. Eighteen
      native neighbors distinguish general and latent graphical models, classical/modified
      site laws, Gaussian process regression, estimation, state optimization and sampling.
      Gibbs and slice algorithms can fit or sample a model without being its identity.
      Contextual inspection does not renew scientific approval of previous records.
    evidence_ids:
    - mapping
- assessment_id: general-construction
  area: consistency
  topic: Root conventions, base measures and construction scope
  outcome: supported
  target_ids:
  - AIMech:SquareRootGraphicalModel
  evidence_ids:
  - squarerootgraphicalmodel-source-0
  - squarerootgraphicalmodel-source-1
  - finite-boundaries
  - neighbors
  summary: Retain the general SQR model construction.
  details: The joint kernel uses unary roots and a symmetric quadratic form of roots
    while preserving the univariate log base measure. The diagonal supplies the original
    sufficient statistic. The record uses the ordinary nonnegative root and makes
    the paper's signed Gaussian exception explicit, rather than silently treating
    sqrt(x^2) as x on the real line. Indicator statistics are unchanged, and the Gaussian
    special case overlaps the existing proper auto-normal family; neither warrants
    a duplicate subtype record here. Z is the normalizing integral or sum and A=log
    Z. The finite-partition requirement is explicit, so unrestricted Poisson parameters
    are not generalized to every base family. Supplementary tail cases are contextual
    evidence for this general construction.
- assessment_id: poisson-specialization
  area: consistency
  topic: Unbounded counts, factorial domination and conditional laws
  outcome: supported
  target_ids:
  - AIMech:PoissonSquareRootGraphicalModel
  evidence_ids:
  - poissonsquarerootgraphicalmodel-source-0
  - poissonsquarerootgraphicalmodel-source-1
  - finite-boundaries
  - neighbors
  summary: Retain Poisson SQR as a distinct specialization.
  details: The record retains unbounded integer support, factorial weights, unary
    square-root terms, diagonal linear count terms and the factor of two for off-diagonal
    matrix entries. Direct inequalities bound the parameter exponent by C+sum d_i*x_i,
    after which independent factorial sums prove finiteness for all finite parameters
    on a finite graph. This proof avoids the source radial measure and uniformity
    gaps. Conditional mass ratios generally differ from Poisson ratios when the square-root
    coefficient is nonzero. The theta=0 diagonal case gives independent Poisson means
    exp(Phi_ii). Truncated, quadratic, bounded-statistic and raw-count auto-Poisson
    models have different supports or potentials and are not aliases.
- assessment_id: exponential-specialization
  area: consistency
  topic: Continuous measure, strict orthant decay and source-formula qualifications
  outcome: supported
  target_ids:
  - AIMech:ExponentialSquareRootGraphicalModel
  evidence_ids:
  - exponentialsquarerootgraphicalmodel-source-0
  - exponentialsquarerootgraphicalmodel-source-1
  - finite-boundaries
  - neighbors
  summary: Retain exponential SQR as a distinct specialization.
  details: The continuous kernel has no factorial weights. Strict negativity on nonnegative
    directions gives a uniform quadratic bound by compactness; Young's inequality
    then yields an integrable product-exponential envelope for any finite theta. Whole-space
    negative definiteness is sufficient, but an indefinite example also works. Positive
    definiteness cannot satisfy negative values on these directions. The record preserves
    one-dimensional flat-quadratic boundary examples without claiming a complete multivariate
    classification. The printed conditional partition formula fails at eta1=-1,eta2=0,
    producing approximately 1.886 instead of 1; the defining integral is retained.
    The synthetic positive-diagonal description is inconsistent with its negative-definite
    claim and is not reproduced as valid.
- assessment_id: radial-measure
  area: consistency
  topic: Ray kernels versus distributions under a coordinate change
  outcome: supported
  target_ids:
  - AIMech:SquareRootGraphicalModel
  - AIMech:PoissonSquareRootGraphicalModel
  - AIMech:ExponentialSquareRootGraphicalModel
  evidence_ids:
  - finite-boundaries
  - squarerootgraphicalmodel-source-0
  - exponentialsquarerootgraphicalmodel-source-0
  summary: Keep radial-measure limitations explicit.
  details: For the continuous L1 transformation x=z*v, the Jacobian contributes z^(p-1).
    An exact two-dimensional rate-2 independent exponential example has joint partition
    1/4 with the factor and 1/2 without it. Thus the bare ray kernel is not the conditional
    distribution of radius under the transformed joint law. Discrete count directions
    require separate counting-measure treatment. The records use direct joint domination
    and do not elevate the bounded-direction-set argument to a universal normalizability
    theorem.
- assessment_id: mapping-boundary
  area: grounding
  topic: Directional AIO mappings and neighboring identities
  outcome: supported
  target_ids:
  - AIMech:SquareRootGraphicalModel
  - AIMech:PoissonSquareRootGraphicalModel
  - AIMech:ExponentialSquareRootGraphicalModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain all three native identities with scoped AIO mappings.
  details: The general SQR construction, Poisson specialization and exponential specialization
    each map broad to Model and related to the task-scoped ProbabilisticGraphicalModel.
    This is a curator assessment, not an upstream AIO assertion. The general construction
    is broader than either specialization; integer support with factorial weights
    and continuous support without those weights distinguish the two named cases.
    The classical auto-Poisson and auto-exponential families use different raw-variable
    interactions, while TPGM, QPGM and SPGM respectively change support, quadratic
    penalties or a bounded statistic. The signed-Gaussian special case is covered
    by an existing proper auto-normal family rather than asserted as another new record.
    RadialBasisNetwork uses radial neural activations; a radial normalization argument
    does not identify SQR with that architecture. GeneralizedLinearModel, LinearRegression,
    LogisticRegression, SpatialRegression and RegressionAnalysis are regression contexts,
    while LassoRegression and RidgeRegression do not identify a model merely because
    its parameters can be fitted with a penalty. BinaryClassification, MulticlassClassification
    and ProbabilisticTopicModel impose tasks or latent-topic semantics absent from
    the generic joint law. Boltzmann, restricted Boltzmann and Hopfield classes add
    particular architectures or dynamics; equality in selected binary cases is not
    equality of the whole SQR construction. Gaussian neural noise/dropout layers,
    sigmoid/exponential/ELU/SELU activation functions, preprocessing, normalization
    and tensor-maximum layers do not define these joint families. Temporal smoothing,
    autoregressive classes and MarkovChain impose ordering not inherent in an arbitrary
    undirected graph. BayesianNetwork and CausalGraphicalModel do not preserve the
    same graph or causal semantics under arbitrary factorization. Language-model,
    autoencoder, hidden-layer and sparse-representation classes are not justified
    mappings from a count or continuous base measure. Eighteen native neighbors distinguish
    general and latent graphical models, classical/modified site laws, Gaussian process
    regression, estimation, state optimization and sampling. Gibbs and slice algorithms
    can fit or sample a model without being its identity. Contextual inspection does
    not renew scientific approval of previous records.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:SquareRootGraphicalModel
  - AIMech:PoissonSquareRootGraphicalModel
  - AIMech:ExponentialSquareRootGraphicalModel
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - squarerootgraphicalmodel-source-0
  - squarerootgraphicalmodel-source-1
  - poissonsquarerootgraphicalmodel-source-0
  - poissonsquarerootgraphicalmodel-source-1
  - exponentialsquarerootgraphicalmodel-source-0
  - exponentialsquarerootgraphicalmodel-source-1
  rationale: The generic SQR construction is broader than either specialization. Poisson
    SQR has integer support and factorial weights permitting all finite parameters;
    exponential SQR has continuous measure and requires a joint-integrability regime.
    Shared root interactions do not make the general family and its distinct specializations
    equivalent. Preserve all three identities and their directional mappings; do not
    duplicate the signed-Gaussian or indicator special cases.
limitations:
- Adversarial author self-review only; all records remain DRAFT.
- All nine proceedings PDF pages and both official supplemental pages were visually
  read. Main extracted text pages 6 and 7 were also read to resolve symbols; no complete
  extracted-text reading is claimed.
- 'Both official PDFs downloaded and rendered successfully. The author-hosted 11-page
  file differs in bytes, but its main pages 1–7 have identical extracted text. All
  extracted-text differences on later main/appendix pages were read: they adjust citation
  labels, bibliography and equation numbering/cross-references. No full visual inspection
  of that alternate file is asserted.'
- The displayed exponential conditional normalizer fails an independent special case.
  The synthetic positive-diagonal description conflicts with negative definiteness.
  The source radial coordinates omit a required continuous Jacobian and cannot be
  used as a literal radius law. These limitations are retained; direct finite-graph
  domination supports the narrower definitions.
- 'Two initial visual suspicions were corrected after complete extracted-text reading
  of pages 6 and 7: the Gaussian mean parameter does include mu, and Equation 14 does
  contain an exponential. Neither mistaken suspicion becomes a record claim.'
- Original finite calculations and stated analytic bounds are not author-code reproduction,
  fitting, benchmark evaluation or a complete classification of boundary parameters.
  The public author-code landing page was located, but no implementation was read
  or run.
- The GRM abstract and bibliography/author links provide provisional frontier context.
  Their full methods have not been read in this round. A bounded erratum search did
  not establish an author correction; mathematical qualifications are identified as
  curator calculations.
- All additions remain DRAFT and require saved adversarial author self-review. The
  discovery frontier remains nonempty.
- The ordinary-root convention and the Poisson unary terms were clarified before this
  formal review; the review assesses the final inspected bytes.
- The author-file comparison establishes matching extracted method text and read citation/numbering
  differences, not complete visual equivalence or an independently published erratum.
- 243 pending leads plus other unresolved dispositions remain; discovery continues.
links: []
tags:
- native-concepts
- square-root-graphical-models
- self-review
- discovery-ongoing
```
