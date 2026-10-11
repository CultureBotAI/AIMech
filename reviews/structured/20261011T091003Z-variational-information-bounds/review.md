# Scientific self-review of variational information bounds and IM

- Review: 20261011T091003Z-variational-information-bounds
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T09:05:30Z
- Finished UTC: 2026-10-11T09:10:03Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain six named formulas/procedures with explicit mathematical relationships, sampling assumptions and AIO assessments. The interpolation ceiling is qualified by a reproducible calculation and conflicting sources. Issue46 corrected source traceability; no actionable finding remains in the current records. All remain DRAFT.

## Scope And Provenance

Six explicitly selected variational-information concepts, including five mathematical methods and the named IM algorithm.

Selection: Exactly the six maintained IDs from the discovery ledger; no sampling.
Coverage: full; 6 reviewed / 6 in the declared population.
Source: working_tree at Git base a7eee4dfe9ddb2a5933c9d434a60816b0eea0105.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:BarberAgakovBound | data/curated/BarberAgakovBound.yaml | maintained | Barber–Agakov mutual information bound |
| AIMech:VariationalInformationMaximizationIMAlgorithm | data/curated/VariationalInformationMaximizationIMAlgorithm.yaml | maintained | Variational information maximization IM algorithm |
| AIMech:NguyenWainwrightJordanBound | data/curated/NguyenWainwrightJordanBound.yaml | maintained | Nguyen–Wainwright–Jordan variational bound |
| AIMech:TUBABound | data/curated/TUBABound.yaml | maintained | Tractable unnormalized Barber–Agakov bound |
| AIMech:InterpolatedVariationalInformationBound | data/curated/InterpolatedVariationalInformationBound.yaml | maintained | Interpolated variational information bound |
| AIMech:LeaveOneOutMutualInformationUpperBound | data/curated/LeaveOneOutMutualInformationUpperBound.yaml | maintained | Leave-one-out mutual information upper bound |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:BarberAgakovBound, AIMech:VariationalInformationMaximizationIMAlgorithm, AIMech:NguyenWainwrightJordanBound, AIMech:TUBABound, AIMech:InterpolatedVariationalInformationBound, AIMech:LeaveOneOutMutualInformationUpperBound | All checks passed!<br>........................................................................ [ 30%]<br>........................................................................ [ 61%]<br>........................................................................ [ 91%]<br>................sss                                                      [100%]<br>232 passed, 3 skipped in 80.72s (0:01:20)<br>Checked 442 record(s); 0 failed.<br>Checked 214 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 44 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 43,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:BarberAgakovBound, AIMech:VariationalInformationMaximizationIMAlgorithm, AIMech:NguyenWainwrightJordanBound, AIMech:TUBABound, AIMech:InterpolatedVariationalInformationBound, AIMech:LeaveOneOutMutualInformationUpperBound | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| Finite-domain interpolation check | passed | True | AIMech:InterpolatedVariationalInformationBound | {"M": 20, "K": 2, "alpha": 0.5, "exp_f_equal": 1.0, "exp_f_unequal": 1e-06, "q_y": 0.05, "joint_log_ratio": 1.258651959433342, "product_ratio": 0.17752529246965698, "I_alpha": 2.081126666963685, "stated_ceiling": 1.3862943611198906, "conservative_ceiling": 2.386294361119891, "true_MI": 2.995732273553991} Deterministic complete enumeration of the finite expectation, without training, Monte Carlo or TensorFlow execution. |

## Scientific And Domain Assessments

### Identity, formula or procedure, limitations and AIO assessment

evidence: supported. Targets: AIMech:BarberAgakovBound.

The Barber–Agakov bound is the mathematical objective, distinct from Barber and Agakov’s alternating IM optimization procedure. It requires a normalized decoder; TUBA and NWJ provide different parameterizations using unnormalized critics. Reconstruction terminology alone does not identify a VAE, a particular autoencoder architecture or the complete IM algorithm. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 208 preceding native IDs/names/aliases. Word-delimited fixed-string searches of both full checkouts, including ignored and hidden files, returned 57 lines each: existing MINE-f component discussion, shared primary-source references, and discovery/review context. Four native neighbors and seven exact AIO nodes with scoped synonyms and outgoing relations were inspected.

For a joint distribution p(x,y) and normalized conditional decoder q(x&#124;y), define L_BA=H(X)+E_p(x,y)[log q(X&#124;Y)], using differential entropy for continuous variables when the required quantities are finite. The identity I(X;Y)−L_BA=E_p(y)[KL(p(X&#124;Y)&#124;&#124;q(X&#124;Y))] gives L_BA&lt;=I(X;Y). Equality holds when the decoder matches the true conditional almost everywhere. For representation learning with fixed p(x), an encoder p_theta(y&#124;x) and decoder q_phi(x&#124;y) can be trained to increase the expected decoder log probability; H(X) is constant with respect to their parameters. Dropping that constant for optimization does not supply a numerical information estimate when the entropy is unknown. Limitations: The decoder must be normalized and assign compatible support. An arbitrary real score substituted for log q is not this bound; zeros or divergent entropies require extended-value care. Increasing a loose lower bound does not by itself prove that true mutual information increased. Decoder expressiveness and optimization quality determine the gap. A sample average is an estimate of the expected objective and is not a certified lower bound for every realized sample. Unknown H(X) prevents reporting its numerical value without additional information. Only declared theoretical passages and example context were inspected; no decoder implementation, training or benchmark was reproduced.

### Identity, formula or procedure, limitations and AIO assessment

evidence: supported. Targets: AIMech:VariationalInformationMaximizationIMAlgorithm.

This is the named IM algorithm in Barber and Agakov’s 2003 paper, not every algorithm that maximizes information. It is separate from its lower-bound objective and from RIM’s regularized discrete clustering, MINE’s dependence estimation and DIM’s feature-matching framework. The analogy to expectation maximization does not make the optimized target an observed-data likelihood. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 208 preceding native IDs/names/aliases. Word-delimited fixed-string searches of both full checkouts, including ignored and hidden files, returned 57 lines each: existing MINE-f component discussion, shared primary-source references, and discovery/review context. Four native neighbors and seven exact AIO nodes with scoped synonyms and outgoing relations were inspected.

Choose a fixed input distribution p(x), a parameterized encoder p_theta(y&#124;x), and a class Q of normalized decoders q(x&#124;y) for which the expected decoder log probability is tractable or can be approximated. Starting from an encoder and decoder, hold q fixed and maximize H(X)+E_p(x)p_theta(y&#124;x)[log q(X&#124;Y)] over theta. Then hold theta fixed and fit q within Q by maximizing the same expectation. Repeat the two updates. H(X) is constant in these updates. Exact coordinate maximizations cannot decrease the chosen lower bound; approximate updates require their own improvement check. The paper develops a noisy linear projection with Gaussian decoding as one feature-extraction configuration and also describes richer encoder/decoder choices. Limitations: Restricted decoders can leave a positive variational gap. Monotonic improvement of the bound does not generally imply monotonic true mutual information or a global optimum. The coordinate subproblems may be nonconvex or expensive, and exact maximization is an idealization. The paper’s instruction to iterate to convergence is not a general finite-iteration convergence guarantee. Encoder noise, capacity and constraints matter. In the linear noisy example, unconstrained encoder scaling can diverge; the procedure does not prescribe one universal norm or power constraint for every application. The normalized decoder and fixed source distribution distinguish this method from generic contrastive loss minimization. No IM implementation or empirical performance claim was reproduced.

### Identity, formula or procedure, limitations and AIO assessment

evidence: supported. Targets: AIMech:NguyenWainwrightJordanBound.

NWJ denotes the variational objective, also called the f-GAN KL bound or MINE-f objective in the inspected follow-up. The neural MINE-f estimator is an optimization configuration using this bound, not a separate formula here. The original paper also develops density-ratio estimation algorithms; this record does not equate the mathematical bound with those kernel estimators or with MINE’s Donsker–Varadhan objective. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 208 preceding native IDs/names/aliases. Word-delimited fixed-string searches of both full checkouts, including ignored and hidden files, returned 57 lines each: existing MINE-f component discussion, shared primary-source references, and discovery/review context. Four native neighbors and seven exact AIO nodes with scoped synonyms and outgoing relations were inspected.

For P absolutely continuous with respect to Q and a real critic T with well-defined expectations, set L_NWJ=E_P[T]−E_Q[exp(T−1)]&lt;=KL(P&#124;&#124;Q). The original representation is sup_(g&gt;0){E_P[log g]−E_Q[g]+1}; substituting g=exp(T−1) gives the displayed objective. With P=p(x,y) and Q=p(x)p(y), it lower-bounds I(X;Y). Under positive density ratios and sufficient critic capacity, T*=1+log(dP/dQ) attains equality; boundary cases may require limiting critics. For a fixed critic with integrable moments, correctly sampled empirical means estimate this expected bound without a log-of-sample-mean bias. Optimizing a neural critic changes the statistical estimation and optimization problem and does not inherit convexity merely from the original function-space formulation. Limitations: The exponential product term can have large or infinite variance. Unbiased estimation of a fixed critic’s objective is not unbiased estimation of true mutual information unless the variational gap vanishes. A realized finite-sample value need not stay below the true divergence. Critic fitting and evaluation on the same data introduce selection effects; finite optimization and restricted function classes add approximation error. The optimal critic includes a fixed normalization offset. Arbitrarily shifting a nonoptimal critic changes this objective, unlike the shift invariance of the population Donsker–Varadhan expression. The original constrained and penalized density-ratio programs have their own assumptions. Their consistency or convexity results are not claimed for every neural parameterization. No estimator benchmark was reproduced.

### Identity, formula or procedure, limitations and AIO assessment

evidence: supported. Targets: AIMech:TUBABound.

TUBA is the named parameterization with separate critic f(x,y) and normalizer a(y)&gt;0. It is algebraically NWJ evaluated at T=f−log(a)+1; retaining it separately records its explicit normalizer and optimization interpretation, not a claim of inequivalent unrestricted variational families. Fixing a=e gives NWJ with the same f, while a held-fixed scalar moving average explains the modified MINE gradient. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 208 preceding native IDs/names/aliases. Word-delimited fixed-string searches of both full checkouts, including ignored and hidden files, returned 57 lines each: existing MINE-f component discussion, shared primary-source references, and discovery/review context. Four native neighbors and seven exact AIO nodes with scoped synonyms and outgoing relations were inspected.

Let Z(y)=E_p(x)[exp(f(X,y))]. For normalized q(x&#124;y)=p(x)exp(f(x,y))/Z(y), the unnormalized Barber–Agakov expression is E_joint[f]−E_p(y)[log Z(y)]. Apply log Z&lt;=Z/a+log a−1 for a(y)&gt;0 to obtain L_TUBA=1+E_joint[f(X,Y)−log a(Y)]−E_product[exp(f(X,Y))/a(Y)]&lt;=I(X;Y). The inequality replacing log Z is tight at a(y)=Z(y); full information tightness additionally requires a critic that represents the conditional-to-marginal relationship. Critic and positive normalizer parameters can be optimized toward the same objective. Reparameterizing T=f−log a+1 recovers exactly the NWJ expression. With fixed functions and appropriate independent joint/product sampling and integrability, the linear expectations admit unbiased Monte Carlo estimates of this bound. The pinned notebook subtracts a row-wise log baseline in its TUBA function. Its separable critic returns Y-indexed rows and X-indexed columns, while the concatenation critic transposes a matrix initially tiled with Y-indexed rows. These paths therefore do not share one score orientation. This is a source-level observation supporting caution about a blanket implementation-equivalence claim; it does not change the stated population formula or claim an executed runtime defect. Limitations: The normalizer must remain positive and must match the variable/sampling convention of the formula. A batch-dependent normalizer cannot be inserted without checking the extended sampling argument. TUBA and NWJ have the same unrestricted family under the stated critic transformation. Different parameterizations, restrictions or optimizers can behave differently; no universal superiority is claimed. Replacing the normalizer by a running statistic has a fixed-denominator gradient interpretation. It does not automatically yield unbiased population Donsker–Varadhan gradients, especially when the statistic depends on the current batch. Finite samples can exceed true information, and exponential moments can be unstable. The inspected notebook has inconsistent matrix-orientation documentation/implementations; no blanket equivalence of all code paths or runtime correctness is asserted.

### Identity, formula or procedure, limitations and AIO assessment

evidence: supported. Targets: AIMech:InterpolatedVariationalInformationBound.

This is Poole et al.’s I_alpha family, not Rényi alpha-information, a convex average of final scalar bounds, or an ordinary temperature parameter. Its endpoints connect existing parameterizations; the interior normalizer and residual product expectation define the distinct construction. The paper’s proposed optimal critic is explicitly a conjecture. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 208 preceding native IDs/names/aliases. Word-delimited fixed-string searches of both full checkouts, including ignored and hidden files, returned 57 lines each: existing MINE-f component discussion, shared primary-source references, and discovery/review context. Four native neighbors and seven exact AIO nodes with scoped synonyms and outgoing relations were inspected.

Draw X_1:K independently from p(x), with Y conditional on X_1 for the joint term. Let m(y;X_1:K)=K^−1 sum_i exp(f(X_i,y)), b_alpha=alpha*m+(1−alpha)*q(y), and r=exp(f(X_1,y))/b_alpha, for q(y)&gt;0 and alpha in [0,1]. Define I_alpha=1+E_p(x_1:K)p(y&#124;x_1)[log r]−E_p(x_1:K)p(y)[r]. The second expectation uses Y independent of all K inputs. Applying NWJ to the augmented variables gives I_alpha&lt;=I(X_1;Y). At alpha=0 this is NWJ after the critic transformation T=1+f−log q; at alpha=1 exchangeability makes the product expectation equal one and yields InfoNCE. For interior alpha the product term must be retained. A leave-one-out minibatch implementation can hold out an additional paired sample’s Y to estimate that independent product term, leaving K other inputs in the normalizer. A curator derivation from Equation (11) gives the conservative ceiling 1+log(K/alpha) for alpha&gt;0: r&lt;=K/alpha and the product expectation is nonnegative. At alpha=1 the cancellation gives the sharper InfoNCE ceiling log K. The paper’s page-5 prose states log(K/alpha) for the general family, whereas the pinned notebook’s plotting code includes the additive one. A deterministic finite-domain calculation saved in the discovery ledger yields I_alpha approximately 2.08113 for K=2 and alpha=0.5, exceeding log(4) approximately 1.38629 while remaining below the true information. Therefore the stronger printed ceiling is not adopted. This is explicit curator analysis of the displayed formula, not an author-issued erratum. The main Equation (11) uses a ratio without a logarithm in the product expectation, but supplementary Table 2 prints a logarithm in that term. The pinned notebook implements the ratio term; its interpolation docstring reverses endpoint labels even though log_interpolate weights the batch normalizer by alpha. The notebook also uses different score orientations in its two critic classes. The record follows the explicit main formula and keeps these source inconsistencies visible rather than asserting that every displayed expression or code path is equivalent. Limitations: The lower bound is an expectation with specified independence; a finite minibatch is not a guaranteed lower bound. The held-out product sample must be independent of every input used in its normalizer. The positive q is a variational normalizer; choosing it as an estimated marginal is one configuration. The paper conjectures f=log p(y&#124;x), q=p(y) as an optimum rather than proving it generally. The main formula, supplemental table and notebook are not textually consistent: the supplemental I_alpha row places a log in the product term, and a notebook docstring reverses the alpha-logit endpoint labels. This record follows main Equation (11), the explicit mixture definition and the independently checked ceiling qualification. The notebook mixes score-matrix orientations across critic implementations. Only declared cells were read; no TensorFlow code, training or benchmark was executed. The finite-domain arithmetic check evaluates the population formula by enumeration and is not a trained-estimator experiment.

### Identity, formula or procedure, limitations and AIO assessment

evidence: supported. Targets: AIMech:LeaveOneOutMutualInformationUpperBound.

This is the leave-one-out upper bound in Poole et al., distinct from InfoNCE’s lower bound and from generic leave-one-out cross-validation. It requires evaluable normalized p(y&#124;x), which may be the encoder defining the modeled joint distribution; an arbitrary learned critic does not supply that requirement. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 208 preceding native IDs/names/aliases. Word-delimited fixed-string searches of both full checkouts, including ignored and hidden files, returned 57 lines each: existing MINE-f component discussion, shared primary-source references, and discovery/review context. Four native neighbors and seven exact AIO nodes with scoped synonyms and outgoing relations were inspected.

Draw K&gt;=2 independent pairs (X_i,Y_i) from p(x)p(y&#124;x), with evaluable normalized conditional density p(y&#124;x). For each i form q_-i(y)=(K−1)^−1 sum_(j!=i) p(y&#124;X_j). Then I(X;Y)&lt;=E[K^−1 sum_i log(p(Y_i&#124;X_i)/q_-i(Y_i))], assuming the expectations are well-defined. The mixture q_-i is independent of the held-out pair because it uses only the other inputs. Conditional on those inputs, the gap of the corresponding variational upper bound is KL(p(Y)&#124;&#124;q_-i(Y)), a nonnegative quantity. Including the paired input in this denominator instead gives the known-conditional InfoNCE lower-bound construction, so the exclusion is essential. A finite batch computes an estimator of the upper-bound expectation rather than a guaranteed upper bound on its own. Limitations: The conditional must be normalized and evaluable for cross-sample inputs. Treating an uncalibrated score as p(y&#124;x) invalidates the stated derivation. For small batches or sharply separated conditional supports, the leave-one-out mixture can be tiny or zero where the held-out conditional is positive, producing a loose or infinite upper bound. Independence of batch examples is part of the proof. Correlated samples or using the held-out input to construct its own denominator require a different argument. The expected bound does not certify a realized finite-sample number. Optimization of a noisy estimate does not guarantee monotonic true information reduction or convergence. No encoder implementation or benchmark was reproduced.

### BA bound and named IM optimization procedure

scope: supported. Targets: AIMech:BarberAgakovBound, AIMech:VariationalInformationMaximizationIMAlgorithm.

Retain the normalized-decoder inequality separately from the alternating encoder/decoder algorithm.

The BA objective has an expected conditional-KL gap. Fixed source entropy can be dropped for optimization but is still needed for a numeric information value. IM alternates constrained decoder fitting and encoder optimization; exact coordinate ascent improves the bound, while restricted decoders and approximate updates do not certify increasing true MI, global optimality or finite convergence. The Gaussian projection example supports a scoped FeatureExtraction association.

### Named parameterizations with explicit algebraic equivalence

representation: supported. Targets: AIMech:NguyenWainwrightJordanBound, AIMech:TUBABound.

Retain NWJ and TUBA with their exact reparameterization relation explicit.

NWJ uses E_P T−E_Q exp(T−1). TUBA separates f and a&gt;0 and is exactly NWJ at T=f−log a+1; a=e recovers the same-f NWJ form. The records do not claim inequivalent unrestricted bound families. Their named parameterization and optimizer/normalizer interpretation justify retaining distinct curated identities with this limitation. No universal accuracy advantage or neural convexity is inferred.

### Interpolation formula, independence and contradictory source ceiling

consistency: supported. Targets: AIMech:InterpolatedVariationalInformationBound.

Retain the main Eq11 construction and qualify the printed ceiling with a reproducible finite case.

The interpolated normalizer is inside the critic ratio, not a convex mixture of final scalar bounds. Independent product samples must exclude every input in their normalizer. Endpoint identities require the stated reparameterization/cancellation. The paper’s log(K/alpha) statement conflicts with its displayed formula on the saved finite case; the conservative1+log(K/alpha) follows directly, and alpha1 retains the sharper InfoNCE ceiling. The supplement’s extra log, notebook endpoint docstring and score-orientation differences are cited rather than silently treated as equivalent.

### Known conditionals and expected upper bounds

scope: supported. Targets: AIMech:LeaveOneOutMutualInformationUpperBound.

Retain the normalized-conditional leave-one-out upper bound as distinct from InfoNCE.

The omitted paired input makes the mixture independent of the held-out pair, yielding an expected marginal-KL gap. Including the positive conditional gives the corresponding lower-bound construction. A generic score or one realized batch is not certified by this argument, and disjoint support may make the upper bound infinite.

### Task association and no-match assessments

grounding: supported. Targets: AIMech:BarberAgakovBound, AIMech:VariationalInformationMaximizationIMAlgorithm, AIMech:NguyenWainwrightJordanBound, AIMech:TUBABound, AIMech:InterpolatedVariationalInformationBound, AIMech:LeaveOneOutMutualInformationUpperBound.

Retain the scoped IM task relation and explicit no-match assessments for all five bounds.

Seven exact AIO nodes with definitions, scoped synonyms and outgoing relations were inspected. IM has a qualified related match to FeatureExtraction for the explicitly developed encoder/linear-compression configuration. Each of the five mathematical bounds has a snapshot-bounded no-match assessment with seven rejected targets. Network architectures, a possible neural parameterization, or an incidental downstream task are not forced mappings for an information inequality.

### Traceable implementation and supplemental limitations

provenance: supported. Targets: AIMech:TUBABound, AIMech:InterpolatedVariationalInformationBound.

Current records include the missing versioned sources and precise limitation citations.

The draft limitations were based on inspected sources but omitted complete structured evidence metadata. Issue46 corrected that gap. Added notebook/supplement sources, cell/table locators and limitation claims were reread and hashed. This is a current-state review; no earlier structured finding or independent approval is invented.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:BarberAgakovBound, AIMech:VariationalInformationMaximizationIMAlgorithm, AIMech:NguyenWainwrightJordanBound, AIMech:TUBABound, AIMech:InterpolatedVariationalInformationBound, AIMech:LeaveOneOutMutualInformationUpperBound. Keep a normalized-decoder inequality separate from its alternating optimizer; preserve the named NWJ/TUBA parameterizations while explicitly stating their algebraic relationship; distinguish an interpolated multi-sample lower bound and a known-conditional leave-one-out upper bound. Shared mathematics or applications do not justify erasing those declared scopes. This is a curator boundary judgment, not an upstream ontology mutation.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T090514Z-variational-information-bounds.json | supports | No normalized identity match among all 442 AIO labels/scoped synonyms and 208 preceding native IDs/names/aliases. Fixed-string word-delimited searches of both full checkouts included hidden/ignored files and returned 57 lines each: existing MINE-f discussion, shared Poole citations and earlier discovery/review references. MINE, InfoNCE, DIM and RIM mechanisms were inspected. Bound formulas, estimator procedures and representation-learning frameworks are not equated. |
| mapping | sources/aio/aio.json; Seven exact CLASS nodes with definitions, scoped synonyms and outgoing relations in source_analysis.aio_mapping_inspection | supports | Seven exact AIO nodes with definitions, scoped synonyms and outgoing relations were inspected. IM has a qualified related match to FeatureExtraction for the explicitly developed encoder/linear-compression configuration. Each of the five mathematical bounds has a snapshot-bounded no-match assessment with seven rejected targets. Network architectures, a possible neural parameterization, or an incidental downstream task are not forced mappings for an information inequality. |
| neighbors | data/curated/MutualInformationNeuralEstimation.yaml; Definitions and mechanisms in MINE, InfoNCE, DeepInfoMax and RIM | supports | Existing records denote neural DV estimation, a finite-candidate contrastive objective, feature-dependence representation learning and regularized categorical clustering. None is the same identity as all six newly selected formulas/procedures. |
| barberagakovbound-source | https://papers.nips.cc/paper_files/paper/2003/file/a6ea8471c120fe8cc35a2954c9b9c595-Paper.pdf; Section 2, PDF p. 2, Equation (3) and equality condition; relation to conditional likelihood, p. 3 | supports | A variational lower bound on mutual information formed by adding input entropy to the expected log probability assigned by a normalized conditional decoder to the input given the output. Version: NIPS 2003, eight-page proceedings PDF; landing-page title is Information Maximization in Noisy Channels: A Variational Approach. Complete local text pages read: 1. Actual image pages viewed: 2, 3, 4. Partial/web reads are separately declared. No model or benchmark execution. |
| barberagakovbound-source-1 | https://proceedings.mlr.press/v97/poole19a/poole19a.pdf; Section 2.1, PDF pp. 2–3, Equation (2): normalized-decoder bound and entropy/tractability limitations | supports | Inspected source: On Variational Bounds of Mutual Information. ICML 2019, PMLR 97:5171–5180; ten-page proceedings PDF. Exact paper/supplement page scope is in source_analysis; expression inconsistencies are explicitly qualified. |
| variationalinformationmaximizationimalgorithm-source | https://papers.nips.cc/paper_files/paper/2003/file/a6ea8471c120fe8cc35a2954c9b9c595-Paper.pdf; Section 2, PDF pp. 2–3, Equation (3) and The IM algorithm numbered updates; Section 3, pp. 3–4, linear Gaussian channel and constrained projection context | supports | An alternating optimization procedure that adjusts a noisy encoder and a variational decoder to increase the Barber–Agakov lower bound on transmitted information for a fixed input distribution. Version: NIPS 2003, eight-page proceedings PDF; landing-page title is Information Maximization in Noisy Channels: A Variational Approach. Complete local text pages read: 1. Actual image pages viewed: 2, 3, 4. Partial/web reads are separately declared. No model or benchmark execution. |
| nguyenwainwrightjordanbound-source | https://dept.stat.lsa.umich.edu/~xuanlong/Papers/Nguyen-Wainwright-Jordan-10.pdf; Section II-A/B, journal pp. 5848–5849 (PDF pp. 2–3), Lemma 1 and Equations (5)–(9): variational characterization and positive density-ratio form | supports | A variational lower bound on Kullback–Leibler divergence that subtracts a product-distribution exponential critic moment from a joint-distribution critic expectation when specialized to mutual information. Version: IEEE Transactions on Information Theory 56(11):5847–5861, November 2010; author-hosted journal PDF, 15 pages. Complete local text pages read: . Actual image pages viewed: 2, 3. Partial/web reads are separately declared. No model or benchmark execution. |
| nguyenwainwrightjordanbound-source-1 | https://proceedings.mlr.press/v97/poole19a/poole19a.pdf; Section 2.2, PDF p. 3, Equation (7), optimal critic and MINE-f/f-GAN naming; footnote 1 for TUBA reparameterization | supports | Inspected source: On Variational Bounds of Mutual Information. ICML 2019, PMLR 97:5171–5180; ten-page proceedings PDF. Exact paper/supplement page scope is in source_analysis; expression inconsistencies are explicitly qualified. |
| tubabound-source | https://proceedings.mlr.press/v97/poole19a/poole19a.pdf; Section 2.2, PDF p. 3, Equations (3), (4), (6), (7), log-partition inequality and footnote 1; moving-average interpretation continues on p. 4 | supports | A tractable unnormalized Barber–Agakov lower-bound parameterization that uses a real critic and a positive output-dependent normalizer to replace an intractable log partition term by a linear upper bound. Version: ICML 2019, PMLR 97:5171–5180; ten-page proceedings PDF. Complete local text pages read: . Actual image pages viewed: 2, 3, 4, 5. Partial/web reads are separately declared. No model or benchmark execution. |
| tubabound-source-1 | https://raw.githubusercontent.com/google-research/google-research/5b381db4139c3cbf25cc9a698c5fe9754215fae2/vbmi/vbmi_demo.ipynb; Zero-based notebook cells 7, 16 and 19: row normalizer subtraction, baseline(y), and differing score-matrix orientations in SeparableCritic and ConcatCritic | supports | Inspected source: On Variational Bounds of Mutual Information: author demonstration notebook. google-research/google-research commit 5b381db4139c3cbf25cc9a698c5fe9754215fae2. Pinned notebook source was read at declared zero-based cells; it was not executed. |
| interpolatedvariationalinformationbound-source | https://proceedings.mlr.press/v97/poole19a/poole19a.pdf; Sections 2.3–2.4, PDF pp. 4–5, Equations (8)–(11), independence construction, endpoint discussion and conjecture | supports | A family of multi-sample mutual-information lower bounds that interpolates the critic’s empirical partition estimate with a positive variational normalizer inside a ratio, connecting NWJ and InfoNCE parameterizations. Version: ICML 2019, PMLR 97:5171–5180; ten-page proceedings PDF. Complete local text pages read: . Actual image pages viewed: 2, 3, 4, 5. Partial/web reads are separately declared. No model or benchmark execution. |
| interpolatedvariationalinformationbound-source-1 | https://raw.githubusercontent.com/google-research/google-research/5b381db4139c3cbf25cc9a698c5fe9754215fae2/vbmi/vbmi_demo.ipynb; Zero-based cells 10–11: leave-one-out construction and log-normalizer interpolation; cell 35 line 35: plotted ceiling includes 1+log(batch_size/alpha) | supports | Inspected source: On Variational Bounds of Mutual Information: author demonstration notebook. google-research/google-research commit 5b381db4139c3cbf25cc9a698c5fe9754215fae2. Pinned notebook source was read at declared zero-based cells; it was not executed. |
| interpolatedvariationalinformationbound-source-2 | https://proceedings.mlr.press/v97/poole19a/poole19a-supp.pdf; Supplementary PDF p. 1, Table 2, I_alpha row: logarithm shown in the second expectation, unlike main Equation (11) | supports | Inspected source: On Variational Bounds of Mutual Information — Supplementary Material. ICML 2019 supplementary PDF; four pages. Exact paper/supplement page scope is in source_analysis; expression inconsistencies are explicitly qualified. |
| leaveoneoutmutualinformationupperbound-source | https://proceedings.mlr.press/v97/poole19a/poole19a.pdf; Section 2.5, PDF p. 5, Equations (12)–(13), Leave one out upper bound; Section 2.1 p. 2, Equation (1), variational upper-bound identity | supports | An expectation-level upper bound on mutual information that compares a known conditional density for each paired sample with a mixture of conditional densities from the other independent inputs in its batch. Version: ICML 2019, PMLR 97:5171–5180; ten-page proceedings PDF. Complete local text pages read: . Actual image pages viewed: 2, 3, 4, 5. Partial/web reads are separately declared. No model or benchmark execution. |
| ceiling-calculation | research/discovery/poole-interpolation-ceiling.py; Finite-domain ratio and complete joint/product enumeration; report calculation object contains parameters, output and execution time | supports | For uniform X on20 values, Y=X, K=2, alpha=.5, positive diagonal/off-diagonal scores and normalized q, the population Eq11 evaluates to2.081126666963685, exceeding log4=1.3862943611198906. It remains below1+log4 and true MI=log20. This is curator mathematical analysis, not an author erratum, random simulation or model run. |
| corrections | research/discovery/20261011T090514Z-variational-information-bounds.json; review_refinements | supports | Issue46 added missing notebook/supplement source metadata and claim-specific limitation citations. The ledger preserves prior/final record hashes, added fields and actual correction time. |

## Limits And Additional Notes

- Adversarial author self-review only; all six records remain DRAFT.
- The selected NWJ/TUBA identities are distinct named parameterizations, not claims of mathematically inequivalent unrestricted variational families.
- Expected inequalities and unbiased fixed-function objectives are not finite-sample certificates or optimizer guarantees.
- The paper, supplement and notebook contain discrepancies; the record states the main formula, source differences and curator calculation explicitly.
- The finite-domain enumeration is reproducible arithmetic, not a learned-estimator experiment or an author-issued correction.
- Only declared source pages and notebook cells were read; no TensorFlow environment, training or benchmark was reproduced.
- Positive discoveries and the remaining frontier keep the goal active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T091003Z-variational-information-bounds
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of variational information bounds and IM
started_at: '2026-10-11T09:05:30Z'
finished_at: '2026-10-11T09:10:03Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed all six current records
    against inspected primary derivations, rendered equations, supplementary discrepancies,
    pinned notebook cells, a deterministic finite-domain calculation, four native
    neighbors and seven exact AIO nodes. Issue46 evidence additions were reread and
    inspected. No independent approval is claimed.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain six named formulas/procedures with explicit mathematical relationships,
  sampling assumptions and AIO assessments. The interpolation ceiling is qualified
  by a reproducible calculation and conflicting sources. Issue46 corrected source
  traceability; no actionable finding remains in the current records. All remain DRAFT.
source:
  git_revision: a7eee4dfe9ddb2a5933c9d434a60816b0eea0105
  state: working_tree
  inputs:
  - path: data/aio/AutoEncoderNetwork.yaml
    sha256: 7a5eb5c54dab03959ca7a19c03a4c4ece161b05618255294e61df174bcaa4521
    role: context
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/DeepNeuralNetwork.yaml
    sha256: f5c4c7764ea05631bb6396200141eb8ba124725d2dc27919c7efe89e5e30b19e
    role: context
  - path: data/aio/FeatureExtraction.yaml
    sha256: d153b8bbe04e9abb7f1ec13e6219dbcd329235ac58bb9229d4a1f416216c07ef
    role: context
  - path: data/aio/RepresentationLearning.yaml
    sha256: bc7af756440437f60210019e17ad1e2dd15cd1c7cbfbc96312520934b7a5c7ca
    role: context
  - path: data/aio/SelfsupervisedLearning.yaml
    sha256: ad9a98dfee5629f6433f13470f56e333316f8f03847df2c5678faf023d979c0e
    role: context
  - path: data/aio/VariationalAutoEncoder.yaml
    sha256: f8f523c5f2cecf91f1510c5ab74bfd36d717f3e683a9a8384e44a3f855e4c45e
    role: context
  - path: data/curated/BarberAgakovBound.yaml
    sha256: ac947a28b3c48611fdbf557cc0bca656e2e93db0d8e158785c579fbc8868076c
    role: target
  - path: data/curated/DeepInfoMax.yaml
    sha256: ebda53a216420e7455b5435a380e383d78569acf9b3e0031ae036f8c25b23fb1
    role: context
  - path: data/curated/InfoNCE.yaml
    sha256: b202ebcafc444df533d78ae82c3618d821ce4c5081a99ffe744deb644a6957da
    role: context
  - path: data/curated/InterpolatedVariationalInformationBound.yaml
    sha256: 7d28eb8cf13222d08a2889e00e2e889a6716306a5827646cae3583a14c2cc520
    role: target
  - path: data/curated/LeaveOneOutMutualInformationUpperBound.yaml
    sha256: 5e79219187336c54036101dab32127ab77fb7c41854dcf3b716b77e81eea1162
    role: target
  - path: data/curated/MutualInformationNeuralEstimation.yaml
    sha256: bc60c4ec4f58081b8875f0f585cb6a27a85bda74853668e5830949d8bfb9708a
    role: context
  - path: data/curated/NguyenWainwrightJordanBound.yaml
    sha256: f91d9a0fb9c061adae4817d7dd6412d5577017b0b2c7abc6276ee9f140ae1987
    role: target
  - path: data/curated/RegularizedInformationMaximization.yaml
    sha256: d46bd458678d2a6cd3ae56c41bb14356ee8316c2c4110494e95a42ec60021c34
    role: context
  - path: data/curated/TUBABound.yaml
    sha256: cd1d4cf3c4f5a072148154fdbccda9092dbb15d495d0300b6f22b18f8a2691d5
    role: target
  - path: data/curated/VariationalInformationMaximizationIMAlgorithm.yaml
    sha256: 61783c7e57a0ce7b6b9201e1f29e7e3d603b7027b7ad541f9d26591f70222e6b
    role: target
  - path: research/discovery/20261011T090514Z-variational-information-bounds.json
    sha256: a85b4cfee59046c4c1c21f23a2e89d94dfaa0ebee17c34dfa19541409b8ce67e
    role: context
  - path: research/discovery/poole-interpolation-ceiling.py
    sha256: d186d80be3fe85bf8e6ce3d2bad73b13357e774028068720ed46ad51ed41d76a
    role: context
  - path: sources/aio/aio.json
    sha256: 8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6
    role: context
  - path: sources/aio/source.yaml
    sha256: a12f1e974c25fab2ebff5e44150fb86f64399471accdf0baeafd986f00e6f345
    role: context
  - path: src/aimech/curated.py
    sha256: 0600ec8ca628d2dac611f2a068074ebcd4b83b6b5f31832a32dbc4f4bfa35b06
    role: context
  - path: src/aimech/schema/curated_concept.yaml
    sha256: a4b7e2f0327eb784d2c5b98c713534f644adf3a7848d4e3c2995e772425725c4
    role: context
targets:
- target_id: AIMech:BarberAgakovBound
  path: data/curated/BarberAgakovBound.yaml
  label: Barber–Agakov mutual information bound
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BarberAgakovBound.yaml
    role: maintained
- target_id: AIMech:VariationalInformationMaximizationIMAlgorithm
  path: data/curated/VariationalInformationMaximizationIMAlgorithm.yaml
  label: Variational information maximization IM algorithm
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/VariationalInformationMaximizationIMAlgorithm.yaml
    role: maintained
- target_id: AIMech:NguyenWainwrightJordanBound
  path: data/curated/NguyenWainwrightJordanBound.yaml
  label: Nguyen–Wainwright–Jordan variational bound
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NguyenWainwrightJordanBound.yaml
    role: maintained
- target_id: AIMech:TUBABound
  path: data/curated/TUBABound.yaml
  label: Tractable unnormalized Barber–Agakov bound
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TUBABound.yaml
    role: maintained
- target_id: AIMech:InterpolatedVariationalInformationBound
  path: data/curated/InterpolatedVariationalInformationBound.yaml
  label: Interpolated variational information bound
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/InterpolatedVariationalInformationBound.yaml
    role: maintained
- target_id: AIMech:LeaveOneOutMutualInformationUpperBound
  path: data/curated/LeaveOneOutMutualInformationUpperBound.yaml
  label: Leave-one-out mutual information upper bound
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LeaveOneOutMutualInformationUpperBound.yaml
    role: maintained
scope:
  description: Six explicitly selected variational-information concepts, including
    five mathematical methods and the named IM algorithm.
  selection: Exactly the six maintained IDs from the discovery ledger; no sampling.
  coverage: full
  population_size: 6
  reviewed_target_ids:
  - AIMech:BarberAgakovBound
  - AIMech:VariationalInformationMaximizationIMAlgorithm
  - AIMech:NguyenWainwrightJordanBound
  - AIMech:TUBABound
  - AIMech:InterpolatedVariationalInformationBound
  - AIMech:LeaveOneOutMutualInformationUpperBound
  exclusions:
  - target: Original NWJ kernel estimators, JS-trained estimator, standalone DV/variational-upper-bound
      identities and older frontier
    reason: Complete identity/method inspection remains future discovery work.
  - target: Uninspected paper passages, full 2007 precursor methods and notebook runtime
      behavior
    reason: Only declared pages/cells support this review; no training or benchmark
      was executed.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:BarberAgakovBound
  - AIMech:VariationalInformationMaximizationIMAlgorithm
  - AIMech:NguyenWainwrightJordanBound
  - AIMech:TUBABound
  - AIMech:InterpolatedVariationalInformationBound
  - AIMech:LeaveOneOutMutualInformationUpperBound
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 30%]\n........................................................................\
    \ [ 61%]\n........................................................................\
    \ [ 91%]\n................sss                                                \
    \      [100%]\n232 passed, 3 skipped in 80.72s (0:01:20)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 214 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 44 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 43,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:BarberAgakovBound
  - AIMech:VariationalInformationMaximizationIMAlgorithm
  - AIMech:NguyenWainwrightJordanBound
  - AIMech:TUBABound
  - AIMech:InterpolatedVariationalInformationBound
  - AIMech:LeaveOneOutMutualInformationUpperBound
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
- check_id: ceiling-enumeration
  name: Finite-domain interpolation check
  command: python3 research/discovery/poole-interpolation-ceiling.py
  status: passed
  required: true
  target_ids:
  - AIMech:InterpolatedVariationalInformationBound
  exit_code: 0
  expected_exit_code: 0
  summary: '{"M": 20, "K": 2, "alpha": 0.5, "exp_f_equal": 1.0, "exp_f_unequal": 1e-06,
    "q_y": 0.05, "joint_log_ratio": 1.258651959433342, "product_ratio": 0.17752529246965698,
    "I_alpha": 2.081126666963685, "stated_ceiling": 1.3862943611198906, "conservative_ceiling":
    2.386294361119891, "true_MI": 2.995732273553991} Deterministic complete enumeration
    of the finite expectation, without training, Monte Carlo or TensorFlow execution.'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T090514Z-variational-information-bounds.json
  accessed_at: '2026-10-11T09:05:30Z'
  support: supports
  summary: 'No normalized identity match among all 442 AIO labels/scoped synonyms
    and 208 preceding native IDs/names/aliases. Fixed-string word-delimited searches
    of both full checkouts included hidden/ignored files and returned 57 lines each:
    existing MINE-f discussion, shared Poole citations and earlier discovery/review
    references. MINE, InfoNCE, DIM and RIM mechanisms were inspected. Bound formulas,
    estimator procedures and representation-learning frameworks are not equated.'
  search_scope: All 442 AIO labels/scoped synonyms and 208 preceding native IDs/names/aliases;
    both full checkouts including hidden and ignored files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-11T09:05:30Z'
  support: supports
  locator: Seven exact CLASS nodes with definitions, scoped synonyms and outgoing
    relations in source_analysis.aio_mapping_inspection
  summary: Seven exact AIO nodes with definitions, scoped synonyms and outgoing relations
    were inspected. IM has a qualified related match to FeatureExtraction for the
    explicitly developed encoder/linear-compression configuration. Each of the five
    mathematical bounds has a snapshot-bounded no-match assessment with seven rejected
    targets. Network architectures, a possible neural parameterization, or an incidental
    downstream task are not forced mappings for an information inequality.
- evidence_id: neighbors
  kind: record_content
  reference: data/curated/MutualInformationNeuralEstimation.yaml
  accessed_at: '2026-10-11T09:05:30Z'
  support: supports
  locator: Definitions and mechanisms in MINE, InfoNCE, DeepInfoMax and RIM
  summary: Existing records denote neural DV estimation, a finite-candidate contrastive
    objective, feature-dependence representation learning and regularized categorical
    clustering. None is the same identity as all six newly selected formulas/procedures.
- evidence_id: barberagakovbound-source
  kind: primary_source
  reference: https://papers.nips.cc/paper_files/paper/2003/file/a6ea8471c120fe8cc35a2954c9b9c595-Paper.pdf
  locator: Section 2, PDF p. 2, Equation (3) and equality condition; relation to conditional
    likelihood, p. 3
  accessed_at: '2026-10-11T08:49:16Z'
  snapshot_sha256: 50da364cfa25ff60cb787cf023239024157e7c45a679d1038427228f443790c2
  support: supports
  summary: 'A variational lower bound on mutual information formed by adding input
    entropy to the expected log probability assigned by a normalized conditional decoder
    to the input given the output. Version: NIPS 2003, eight-page proceedings PDF;
    landing-page title is Information Maximization in Noisy Channels: A Variational
    Approach. Complete local text pages read: 1. Actual image pages viewed: 2, 3,
    4. Partial/web reads are separately declared. No model or benchmark execution.'
- evidence_id: barberagakovbound-source-1
  kind: primary_source
  reference: https://proceedings.mlr.press/v97/poole19a/poole19a.pdf
  locator: 'Section 2.1, PDF pp. 2–3, Equation (2): normalized-decoder bound and entropy/tractability
    limitations'
  accessed_at: '2026-10-11T08:36:10Z'
  snapshot_sha256: 38da74b0bae67ce3e565808b7bf81ce3efbcb2e2477f436d9afe7d114d1198cc
  support: supports
  summary: 'Inspected source: On Variational Bounds of Mutual Information. ICML 2019,
    PMLR 97:5171–5180; ten-page proceedings PDF. Exact paper/supplement page scope
    is in source_analysis; expression inconsistencies are explicitly qualified.'
- evidence_id: variationalinformationmaximizationimalgorithm-source
  kind: primary_source
  reference: https://papers.nips.cc/paper_files/paper/2003/file/a6ea8471c120fe8cc35a2954c9b9c595-Paper.pdf
  locator: Section 2, PDF pp. 2–3, Equation (3) and The IM algorithm numbered updates;
    Section 3, pp. 3–4, linear Gaussian channel and constrained projection context
  accessed_at: '2026-10-11T08:49:16Z'
  snapshot_sha256: 50da364cfa25ff60cb787cf023239024157e7c45a679d1038427228f443790c2
  support: supports
  summary: 'An alternating optimization procedure that adjusts a noisy encoder and
    a variational decoder to increase the Barber–Agakov lower bound on transmitted
    information for a fixed input distribution. Version: NIPS 2003, eight-page proceedings
    PDF; landing-page title is Information Maximization in Noisy Channels: A Variational
    Approach. Complete local text pages read: 1. Actual image pages viewed: 2, 3,
    4. Partial/web reads are separately declared. No model or benchmark execution.'
- evidence_id: nguyenwainwrightjordanbound-source
  kind: primary_source
  reference: https://dept.stat.lsa.umich.edu/~xuanlong/Papers/Nguyen-Wainwright-Jordan-10.pdf
  locator: 'Section II-A/B, journal pp. 5848–5849 (PDF pp. 2–3), Lemma 1 and Equations
    (5)–(9): variational characterization and positive density-ratio form'
  accessed_at: '2026-10-11T08:49:16Z'
  snapshot_sha256: 7f8582371c96bb5c8f7c7d230044dde3c32bbd056c4dc3a84f851eb1a2672072
  support: supports
  summary: 'A variational lower bound on Kullback–Leibler divergence that subtracts
    a product-distribution exponential critic moment from a joint-distribution critic
    expectation when specialized to mutual information. Version: IEEE Transactions
    on Information Theory 56(11):5847–5861, November 2010; author-hosted journal PDF,
    15 pages. Complete local text pages read: . Actual image pages viewed: 2, 3. Partial/web
    reads are separately declared. No model or benchmark execution.'
- evidence_id: nguyenwainwrightjordanbound-source-1
  kind: primary_source
  reference: https://proceedings.mlr.press/v97/poole19a/poole19a.pdf
  locator: Section 2.2, PDF p. 3, Equation (7), optimal critic and MINE-f/f-GAN naming;
    footnote 1 for TUBA reparameterization
  accessed_at: '2026-10-11T08:36:10Z'
  snapshot_sha256: 38da74b0bae67ce3e565808b7bf81ce3efbcb2e2477f436d9afe7d114d1198cc
  support: supports
  summary: 'Inspected source: On Variational Bounds of Mutual Information. ICML 2019,
    PMLR 97:5171–5180; ten-page proceedings PDF. Exact paper/supplement page scope
    is in source_analysis; expression inconsistencies are explicitly qualified.'
- evidence_id: tubabound-source
  kind: primary_source
  reference: https://proceedings.mlr.press/v97/poole19a/poole19a.pdf
  locator: Section 2.2, PDF p. 3, Equations (3), (4), (6), (7), log-partition inequality
    and footnote 1; moving-average interpretation continues on p. 4
  accessed_at: '2026-10-11T08:36:10Z'
  snapshot_sha256: 38da74b0bae67ce3e565808b7bf81ce3efbcb2e2477f436d9afe7d114d1198cc
  support: supports
  summary: 'A tractable unnormalized Barber–Agakov lower-bound parameterization that
    uses a real critic and a positive output-dependent normalizer to replace an intractable
    log partition term by a linear upper bound. Version: ICML 2019, PMLR 97:5171–5180;
    ten-page proceedings PDF. Complete local text pages read: . Actual image pages
    viewed: 2, 3, 4, 5. Partial/web reads are separately declared. No model or benchmark
    execution.'
- evidence_id: tubabound-source-1
  kind: primary_source
  reference: https://raw.githubusercontent.com/google-research/google-research/5b381db4139c3cbf25cc9a698c5fe9754215fae2/vbmi/vbmi_demo.ipynb
  locator: 'Zero-based notebook cells 7, 16 and 19: row normalizer subtraction, baseline(y),
    and differing score-matrix orientations in SeparableCritic and ConcatCritic'
  accessed_at: '2026-10-11T08:55:05Z'
  snapshot_sha256: 8b90ab53effb980d681daf458b124a000b92eb2ca85d95815942040d62d24bd8
  support: supports
  summary: 'Inspected source: On Variational Bounds of Mutual Information: author
    demonstration notebook. google-research/google-research commit 5b381db4139c3cbf25cc9a698c5fe9754215fae2.
    Pinned notebook source was read at declared zero-based cells; it was not executed.'
- evidence_id: interpolatedvariationalinformationbound-source
  kind: primary_source
  reference: https://proceedings.mlr.press/v97/poole19a/poole19a.pdf
  locator: Sections 2.3–2.4, PDF pp. 4–5, Equations (8)–(11), independence construction,
    endpoint discussion and conjecture
  accessed_at: '2026-10-11T08:36:10Z'
  snapshot_sha256: 38da74b0bae67ce3e565808b7bf81ce3efbcb2e2477f436d9afe7d114d1198cc
  support: supports
  summary: 'A family of multi-sample mutual-information lower bounds that interpolates
    the critic’s empirical partition estimate with a positive variational normalizer
    inside a ratio, connecting NWJ and InfoNCE parameterizations. Version: ICML 2019,
    PMLR 97:5171–5180; ten-page proceedings PDF. Complete local text pages read: .
    Actual image pages viewed: 2, 3, 4, 5. Partial/web reads are separately declared.
    No model or benchmark execution.'
- evidence_id: interpolatedvariationalinformationbound-source-1
  kind: primary_source
  reference: https://raw.githubusercontent.com/google-research/google-research/5b381db4139c3cbf25cc9a698c5fe9754215fae2/vbmi/vbmi_demo.ipynb
  locator: 'Zero-based cells 10–11: leave-one-out construction and log-normalizer
    interpolation; cell 35 line 35: plotted ceiling includes 1+log(batch_size/alpha)'
  accessed_at: '2026-10-11T08:55:05Z'
  snapshot_sha256: 8b90ab53effb980d681daf458b124a000b92eb2ca85d95815942040d62d24bd8
  support: supports
  summary: 'Inspected source: On Variational Bounds of Mutual Information: author
    demonstration notebook. google-research/google-research commit 5b381db4139c3cbf25cc9a698c5fe9754215fae2.
    Pinned notebook source was read at declared zero-based cells; it was not executed.'
- evidence_id: interpolatedvariationalinformationbound-source-2
  kind: primary_source
  reference: https://proceedings.mlr.press/v97/poole19a/poole19a-supp.pdf
  locator: 'Supplementary PDF p. 1, Table 2, I_alpha row: logarithm shown in the second
    expectation, unlike main Equation (11)'
  accessed_at: '2026-10-11T08:36:12Z'
  snapshot_sha256: 4d9c5a5f008850c05c5033de81891fbd9050dcc275c857594856c8d1d8a1d90d
  support: supports
  summary: 'Inspected source: On Variational Bounds of Mutual Information — Supplementary
    Material. ICML 2019 supplementary PDF; four pages. Exact paper/supplement page
    scope is in source_analysis; expression inconsistencies are explicitly qualified.'
- evidence_id: leaveoneoutmutualinformationupperbound-source
  kind: primary_source
  reference: https://proceedings.mlr.press/v97/poole19a/poole19a.pdf
  locator: Section 2.5, PDF p. 5, Equations (12)–(13), Leave one out upper bound;
    Section 2.1 p. 2, Equation (1), variational upper-bound identity
  accessed_at: '2026-10-11T08:36:10Z'
  snapshot_sha256: 38da74b0bae67ce3e565808b7bf81ce3efbcb2e2477f436d9afe7d114d1198cc
  support: supports
  summary: 'An expectation-level upper bound on mutual information that compares a
    known conditional density for each paired sample with a mixture of conditional
    densities from the other independent inputs in its batch. Version: ICML 2019,
    PMLR 97:5171–5180; ten-page proceedings PDF. Complete local text pages read: .
    Actual image pages viewed: 2, 3, 4, 5. Partial/web reads are separately declared.
    No model or benchmark execution.'
- evidence_id: ceiling-calculation
  kind: validation
  reference: research/discovery/poole-interpolation-ceiling.py
  locator: Finite-domain ratio and complete joint/product enumeration; report calculation
    object contains parameters, output and execution time
  accessed_at: '2026-10-11T09:05:15Z'
  snapshot_sha256: d186d80be3fe85bf8e6ce3d2bad73b13357e774028068720ed46ad51ed41d76a
  support: supports
  summary: For uniform X on20 values, Y=X, K=2, alpha=.5, positive diagonal/off-diagonal
    scores and normalized q, the population Eq11 evaluates to2.081126666963685, exceeding
    log4=1.3862943611198906. It remains below1+log4 and true MI=log20. This is curator
    mathematical analysis, not an author erratum, random simulation or model run.
- evidence_id: corrections
  kind: record_content
  reference: research/discovery/20261011T090514Z-variational-information-bounds.json
  locator: review_refinements
  accessed_at: '2026-10-11T09:05:30Z'
  support: supports
  summary: Issue46 added missing notebook/supplement source metadata and claim-specific
    limitation citations. The ledger preserves prior/final record hashes, added fields
    and actual correction time.
assessments:
- assessment_id: barberagakovbound
  area: evidence
  topic: Identity, formula or procedure, limitations and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:BarberAgakovBound
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - barberagakovbound-source
  - barberagakovbound-source-1
  summary: 'The Barber–Agakov bound is the mathematical objective, distinct from Barber
    and Agakov’s alternating IM optimization procedure. It requires a normalized decoder;
    TUBA and NWJ provide different parameterizations using unnormalized critics. Reconstruction
    terminology alone does not identify a VAE, a particular autoencoder architecture
    or the complete IM algorithm. No normalized identity match was found across all
    442 pinned AIO labels/scoped synonyms and 208 preceding native IDs/names/aliases.
    Word-delimited fixed-string searches of both full checkouts, including ignored
    and hidden files, returned 57 lines each: existing MINE-f component discussion,
    shared primary-source references, and discovery/review context. Four native neighbors
    and seven exact AIO nodes with scoped synonyms and outgoing relations were inspected.'
  details: 'For a joint distribution p(x,y) and normalized conditional decoder q(x|y),
    define L_BA=H(X)+E_p(x,y)[log q(X|Y)], using differential entropy for continuous
    variables when the required quantities are finite. The identity I(X;Y)−L_BA=E_p(y)[KL(p(X|Y)||q(X|Y))]
    gives L_BA<=I(X;Y). Equality holds when the decoder matches the true conditional
    almost everywhere. For representation learning with fixed p(x), an encoder p_theta(y|x)
    and decoder q_phi(x|y) can be trained to increase the expected decoder log probability;
    H(X) is constant with respect to their parameters. Dropping that constant for
    optimization does not supply a numerical information estimate when the entropy
    is unknown. Limitations: The decoder must be normalized and assign compatible
    support. An arbitrary real score substituted for log q is not this bound; zeros
    or divergent entropies require extended-value care. Increasing a loose lower bound
    does not by itself prove that true mutual information increased. Decoder expressiveness
    and optimization quality determine the gap. A sample average is an estimate of
    the expected objective and is not a certified lower bound for every realized sample.
    Unknown H(X) prevents reporting its numerical value without additional information.
    Only declared theoretical passages and example context were inspected; no decoder
    implementation, training or benchmark was reproduced.'
  dimensions:
  - name: concept-kind
    value: mathematical_method
    definition: A mathematical objective/inequality, or for IM a specified alternating
      optimization algorithm; not a trained instance or benchmark outcome.
    evidence_ids:
    - barberagakovbound-source
  - name: aio-assessment
    value: snapshot-bounded no match
    definition: 'The inspected candidates describe networks, feature-extraction tasks
      or self-supervised tasks, not the mathematical information bound. Shared variational
      terminology, an optional neural parameterization or downstream use does not
      establish a suitable mapping. AIO:VariationalAutoEncoder: A probabilistic latent
      autoencoder architecture is not a variational information inequality; neither
      implies the other. AIO:AutoEncoderNetwork: Reconstruction networks can use information
      objectives but do not identify this mathematical bound. AIO:RepresentationLearning:
      The target is a deep-network representation-learning class; it is a possible
      use of a bound, not the bound itself. AIO:DeepNeuralNetwork: A neural critic
      or decoder is one possible parameterization, not the information formula. AIO:FeatureExtraction:
      This preprocessing task does not specify an information estimator or bound.
      AIO:BayesianNetwork: Conditional distributions do not make this bound a directed
      graphical-model architecture. AIO:SelfsupervisedLearning: A self-generated prediction
      task does not specify this population information inequality.'
    evidence_ids:
    - identity
    - mapping
- assessment_id: variationalinformationmaximizationimalgorithm
  area: evidence
  topic: Identity, formula or procedure, limitations and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:VariationalInformationMaximizationIMAlgorithm
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - variationalinformationmaximizationimalgorithm-source
  summary: 'This is the named IM algorithm in Barber and Agakov’s 2003 paper, not
    every algorithm that maximizes information. It is separate from its lower-bound
    objective and from RIM’s regularized discrete clustering, MINE’s dependence estimation
    and DIM’s feature-matching framework. The analogy to expectation maximization
    does not make the optimized target an observed-data likelihood. No normalized
    identity match was found across all 442 pinned AIO labels/scoped synonyms and
    208 preceding native IDs/names/aliases. Word-delimited fixed-string searches of
    both full checkouts, including ignored and hidden files, returned 57 lines each:
    existing MINE-f component discussion, shared primary-source references, and discovery/review
    context. Four native neighbors and seven exact AIO nodes with scoped synonyms
    and outgoing relations were inspected.'
  details: 'Choose a fixed input distribution p(x), a parameterized encoder p_theta(y|x),
    and a class Q of normalized decoders q(x|y) for which the expected decoder log
    probability is tractable or can be approximated. Starting from an encoder and
    decoder, hold q fixed and maximize H(X)+E_p(x)p_theta(y|x)[log q(X|Y)] over theta.
    Then hold theta fixed and fit q within Q by maximizing the same expectation. Repeat
    the two updates. H(X) is constant in these updates. Exact coordinate maximizations
    cannot decrease the chosen lower bound; approximate updates require their own
    improvement check. The paper develops a noisy linear projection with Gaussian
    decoding as one feature-extraction configuration and also describes richer encoder/decoder
    choices. Limitations: Restricted decoders can leave a positive variational gap.
    Monotonic improvement of the bound does not generally imply monotonic true mutual
    information or a global optimum. The coordinate subproblems may be nonconvex or
    expensive, and exact maximization is an idealization. The paper’s instruction
    to iterate to convergence is not a general finite-iteration convergence guarantee.
    Encoder noise, capacity and constraints matter. In the linear noisy example, unconstrained
    encoder scaling can diverge; the procedure does not prescribe one universal norm
    or power constraint for every application. The normalized decoder and fixed source
    distribution distinguish this method from generic contrastive loss minimization.
    No IM implementation or empirical performance claim was reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A mathematical objective/inequality, or for IM a specified alternating
      optimization algorithm; not a trained instance or benchmark outcome.
    evidence_ids:
    - variationalinformationmaximizationimalgorithm-source
  - name: aio-assessment
    value: 'related_match: AIO:FeatureExtraction'
    definition: The paper explicitly develops encoder optimization for linear compression
      and feature extraction. This associates the algorithm’s feature-extraction configuration
      with the AIO preprocessing task; it does not assert equivalence, an is-a relation,
      or that every communication-channel use is preprocessing.
    evidence_ids:
    - identity
    - mapping
- assessment_id: nguyenwainwrightjordanbound
  area: evidence
  topic: Identity, formula or procedure, limitations and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:NguyenWainwrightJordanBound
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - nguyenwainwrightjordanbound-source
  - nguyenwainwrightjordanbound-source-1
  summary: 'NWJ denotes the variational objective, also called the f-GAN KL bound
    or MINE-f objective in the inspected follow-up. The neural MINE-f estimator is
    an optimization configuration using this bound, not a separate formula here. The
    original paper also develops density-ratio estimation algorithms; this record
    does not equate the mathematical bound with those kernel estimators or with MINE’s
    Donsker–Varadhan objective. No normalized identity match was found across all
    442 pinned AIO labels/scoped synonyms and 208 preceding native IDs/names/aliases.
    Word-delimited fixed-string searches of both full checkouts, including ignored
    and hidden files, returned 57 lines each: existing MINE-f component discussion,
    shared primary-source references, and discovery/review context. Four native neighbors
    and seven exact AIO nodes with scoped synonyms and outgoing relations were inspected.'
  details: 'For P absolutely continuous with respect to Q and a real critic T with
    well-defined expectations, set L_NWJ=E_P[T]−E_Q[exp(T−1)]<=KL(P||Q). The original
    representation is sup_(g>0){E_P[log g]−E_Q[g]+1}; substituting g=exp(T−1) gives
    the displayed objective. With P=p(x,y) and Q=p(x)p(y), it lower-bounds I(X;Y).
    Under positive density ratios and sufficient critic capacity, T*=1+log(dP/dQ)
    attains equality; boundary cases may require limiting critics. For a fixed critic
    with integrable moments, correctly sampled empirical means estimate this expected
    bound without a log-of-sample-mean bias. Optimizing a neural critic changes the
    statistical estimation and optimization problem and does not inherit convexity
    merely from the original function-space formulation. Limitations: The exponential
    product term can have large or infinite variance. Unbiased estimation of a fixed
    critic’s objective is not unbiased estimation of true mutual information unless
    the variational gap vanishes. A realized finite-sample value need not stay below
    the true divergence. Critic fitting and evaluation on the same data introduce
    selection effects; finite optimization and restricted function classes add approximation
    error. The optimal critic includes a fixed normalization offset. Arbitrarily shifting
    a nonoptimal critic changes this objective, unlike the shift invariance of the
    population Donsker–Varadhan expression. The original constrained and penalized
    density-ratio programs have their own assumptions. Their consistency or convexity
    results are not claimed for every neural parameterization. No estimator benchmark
    was reproduced.'
  dimensions:
  - name: concept-kind
    value: mathematical_method
    definition: A mathematical objective/inequality, or for IM a specified alternating
      optimization algorithm; not a trained instance or benchmark outcome.
    evidence_ids:
    - nguyenwainwrightjordanbound-source
  - name: aio-assessment
    value: snapshot-bounded no match
    definition: 'The inspected candidates describe networks, feature-extraction tasks
      or self-supervised tasks, not the mathematical information bound. Shared variational
      terminology, an optional neural parameterization or downstream use does not
      establish a suitable mapping. AIO:VariationalAutoEncoder: A probabilistic latent
      autoencoder architecture is not a variational information inequality; neither
      implies the other. AIO:AutoEncoderNetwork: Reconstruction networks can use information
      objectives but do not identify this mathematical bound. AIO:RepresentationLearning:
      The target is a deep-network representation-learning class; it is a possible
      use of a bound, not the bound itself. AIO:DeepNeuralNetwork: A neural critic
      or decoder is one possible parameterization, not the information formula. AIO:FeatureExtraction:
      This preprocessing task does not specify an information estimator or bound.
      AIO:BayesianNetwork: Conditional distributions do not make this bound a directed
      graphical-model architecture. AIO:SelfsupervisedLearning: A self-generated prediction
      task does not specify this population information inequality.'
    evidence_ids:
    - identity
    - mapping
- assessment_id: tubabound
  area: evidence
  topic: Identity, formula or procedure, limitations and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:TUBABound
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - tubabound-source
  - tubabound-source-1
  summary: 'TUBA is the named parameterization with separate critic f(x,y) and normalizer
    a(y)>0. It is algebraically NWJ evaluated at T=f−log(a)+1; retaining it separately
    records its explicit normalizer and optimization interpretation, not a claim of
    inequivalent unrestricted variational families. Fixing a=e gives NWJ with the
    same f, while a held-fixed scalar moving average explains the modified MINE gradient.
    No normalized identity match was found across all 442 pinned AIO labels/scoped
    synonyms and 208 preceding native IDs/names/aliases. Word-delimited fixed-string
    searches of both full checkouts, including ignored and hidden files, returned
    57 lines each: existing MINE-f component discussion, shared primary-source references,
    and discovery/review context. Four native neighbors and seven exact AIO nodes
    with scoped synonyms and outgoing relations were inspected.'
  details: 'Let Z(y)=E_p(x)[exp(f(X,y))]. For normalized q(x|y)=p(x)exp(f(x,y))/Z(y),
    the unnormalized Barber–Agakov expression is E_joint[f]−E_p(y)[log Z(y)]. Apply
    log Z<=Z/a+log a−1 for a(y)>0 to obtain L_TUBA=1+E_joint[f(X,Y)−log a(Y)]−E_product[exp(f(X,Y))/a(Y)]<=I(X;Y).
    The inequality replacing log Z is tight at a(y)=Z(y); full information tightness
    additionally requires a critic that represents the conditional-to-marginal relationship.
    Critic and positive normalizer parameters can be optimized toward the same objective.
    Reparameterizing T=f−log a+1 recovers exactly the NWJ expression. With fixed functions
    and appropriate independent joint/product sampling and integrability, the linear
    expectations admit unbiased Monte Carlo estimates of this bound. The pinned notebook
    subtracts a row-wise log baseline in its TUBA function. Its separable critic returns
    Y-indexed rows and X-indexed columns, while the concatenation critic transposes
    a matrix initially tiled with Y-indexed rows. These paths therefore do not share
    one score orientation. This is a source-level observation supporting caution about
    a blanket implementation-equivalence claim; it does not change the stated population
    formula or claim an executed runtime defect. Limitations: The normalizer must
    remain positive and must match the variable/sampling convention of the formula.
    A batch-dependent normalizer cannot be inserted without checking the extended
    sampling argument. TUBA and NWJ have the same unrestricted family under the stated
    critic transformation. Different parameterizations, restrictions or optimizers
    can behave differently; no universal superiority is claimed. Replacing the normalizer
    by a running statistic has a fixed-denominator gradient interpretation. It does
    not automatically yield unbiased population Donsker–Varadhan gradients, especially
    when the statistic depends on the current batch. Finite samples can exceed true
    information, and exponential moments can be unstable. The inspected notebook has
    inconsistent matrix-orientation documentation/implementations; no blanket equivalence
    of all code paths or runtime correctness is asserted.'
  dimensions:
  - name: concept-kind
    value: mathematical_method
    definition: A mathematical objective/inequality, or for IM a specified alternating
      optimization algorithm; not a trained instance or benchmark outcome.
    evidence_ids:
    - tubabound-source
  - name: aio-assessment
    value: snapshot-bounded no match
    definition: 'The inspected candidates describe networks, feature-extraction tasks
      or self-supervised tasks, not the mathematical information bound. Shared variational
      terminology, an optional neural parameterization or downstream use does not
      establish a suitable mapping. AIO:VariationalAutoEncoder: A probabilistic latent
      autoencoder architecture is not a variational information inequality; neither
      implies the other. AIO:AutoEncoderNetwork: Reconstruction networks can use information
      objectives but do not identify this mathematical bound. AIO:RepresentationLearning:
      The target is a deep-network representation-learning class; it is a possible
      use of a bound, not the bound itself. AIO:DeepNeuralNetwork: A neural critic
      or decoder is one possible parameterization, not the information formula. AIO:FeatureExtraction:
      This preprocessing task does not specify an information estimator or bound.
      AIO:BayesianNetwork: Conditional distributions do not make this bound a directed
      graphical-model architecture. AIO:SelfsupervisedLearning: A self-generated prediction
      task does not specify this population information inequality.'
    evidence_ids:
    - identity
    - mapping
- assessment_id: interpolatedvariationalinformationbound
  area: evidence
  topic: Identity, formula or procedure, limitations and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:InterpolatedVariationalInformationBound
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - interpolatedvariationalinformationbound-source
  - interpolatedvariationalinformationbound-source-1
  - interpolatedvariationalinformationbound-source-2
  - ceiling-calculation
  summary: 'This is Poole et al.’s I_alpha family, not Rényi alpha-information, a
    convex average of final scalar bounds, or an ordinary temperature parameter. Its
    endpoints connect existing parameterizations; the interior normalizer and residual
    product expectation define the distinct construction. The paper’s proposed optimal
    critic is explicitly a conjecture. No normalized identity match was found across
    all 442 pinned AIO labels/scoped synonyms and 208 preceding native IDs/names/aliases.
    Word-delimited fixed-string searches of both full checkouts, including ignored
    and hidden files, returned 57 lines each: existing MINE-f component discussion,
    shared primary-source references, and discovery/review context. Four native neighbors
    and seven exact AIO nodes with scoped synonyms and outgoing relations were inspected.'
  details: 'Draw X_1:K independently from p(x), with Y conditional on X_1 for the
    joint term. Let m(y;X_1:K)=K^−1 sum_i exp(f(X_i,y)), b_alpha=alpha*m+(1−alpha)*q(y),
    and r=exp(f(X_1,y))/b_alpha, for q(y)>0 and alpha in [0,1]. Define I_alpha=1+E_p(x_1:K)p(y|x_1)[log
    r]−E_p(x_1:K)p(y)[r]. The second expectation uses Y independent of all K inputs.
    Applying NWJ to the augmented variables gives I_alpha<=I(X_1;Y). At alpha=0 this
    is NWJ after the critic transformation T=1+f−log q; at alpha=1 exchangeability
    makes the product expectation equal one and yields InfoNCE. For interior alpha
    the product term must be retained. A leave-one-out minibatch implementation can
    hold out an additional paired sample’s Y to estimate that independent product
    term, leaving K other inputs in the normalizer. A curator derivation from Equation
    (11) gives the conservative ceiling 1+log(K/alpha) for alpha>0: r<=K/alpha and
    the product expectation is nonnegative. At alpha=1 the cancellation gives the
    sharper InfoNCE ceiling log K. The paper’s page-5 prose states log(K/alpha) for
    the general family, whereas the pinned notebook’s plotting code includes the additive
    one. A deterministic finite-domain calculation saved in the discovery ledger yields
    I_alpha approximately 2.08113 for K=2 and alpha=0.5, exceeding log(4) approximately
    1.38629 while remaining below the true information. Therefore the stronger printed
    ceiling is not adopted. This is explicit curator analysis of the displayed formula,
    not an author-issued erratum. The main Equation (11) uses a ratio without a logarithm
    in the product expectation, but supplementary Table 2 prints a logarithm in that
    term. The pinned notebook implements the ratio term; its interpolation docstring
    reverses endpoint labels even though log_interpolate weights the batch normalizer
    by alpha. The notebook also uses different score orientations in its two critic
    classes. The record follows the explicit main formula and keeps these source inconsistencies
    visible rather than asserting that every displayed expression or code path is
    equivalent. Limitations: The lower bound is an expectation with specified independence;
    a finite minibatch is not a guaranteed lower bound. The held-out product sample
    must be independent of every input used in its normalizer. The positive q is a
    variational normalizer; choosing it as an estimated marginal is one configuration.
    The paper conjectures f=log p(y|x), q=p(y) as an optimum rather than proving it
    generally. The main formula, supplemental table and notebook are not textually
    consistent: the supplemental I_alpha row places a log in the product term, and
    a notebook docstring reverses the alpha-logit endpoint labels. This record follows
    main Equation (11), the explicit mixture definition and the independently checked
    ceiling qualification. The notebook mixes score-matrix orientations across critic
    implementations. Only declared cells were read; no TensorFlow code, training or
    benchmark was executed. The finite-domain arithmetic check evaluates the population
    formula by enumeration and is not a trained-estimator experiment.'
  dimensions:
  - name: concept-kind
    value: mathematical_method
    definition: A mathematical objective/inequality, or for IM a specified alternating
      optimization algorithm; not a trained instance or benchmark outcome.
    evidence_ids:
    - interpolatedvariationalinformationbound-source
  - name: aio-assessment
    value: snapshot-bounded no match
    definition: 'The inspected candidates describe networks, feature-extraction tasks
      or self-supervised tasks, not the mathematical information bound. Shared variational
      terminology, an optional neural parameterization or downstream use does not
      establish a suitable mapping. AIO:VariationalAutoEncoder: A probabilistic latent
      autoencoder architecture is not a variational information inequality; neither
      implies the other. AIO:AutoEncoderNetwork: Reconstruction networks can use information
      objectives but do not identify this mathematical bound. AIO:RepresentationLearning:
      The target is a deep-network representation-learning class; it is a possible
      use of a bound, not the bound itself. AIO:DeepNeuralNetwork: A neural critic
      or decoder is one possible parameterization, not the information formula. AIO:FeatureExtraction:
      This preprocessing task does not specify an information estimator or bound.
      AIO:BayesianNetwork: Conditional distributions do not make this bound a directed
      graphical-model architecture. AIO:SelfsupervisedLearning: A self-generated prediction
      task does not specify this population information inequality.'
    evidence_ids:
    - identity
    - mapping
- assessment_id: leaveoneoutmutualinformationupperbound
  area: evidence
  topic: Identity, formula or procedure, limitations and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:LeaveOneOutMutualInformationUpperBound
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - leaveoneoutmutualinformationupperbound-source
  summary: 'This is the leave-one-out upper bound in Poole et al., distinct from InfoNCE’s
    lower bound and from generic leave-one-out cross-validation. It requires evaluable
    normalized p(y|x), which may be the encoder defining the modeled joint distribution;
    an arbitrary learned critic does not supply that requirement. No normalized identity
    match was found across all 442 pinned AIO labels/scoped synonyms and 208 preceding
    native IDs/names/aliases. Word-delimited fixed-string searches of both full checkouts,
    including ignored and hidden files, returned 57 lines each: existing MINE-f component
    discussion, shared primary-source references, and discovery/review context. Four
    native neighbors and seven exact AIO nodes with scoped synonyms and outgoing relations
    were inspected.'
  details: 'Draw K>=2 independent pairs (X_i,Y_i) from p(x)p(y|x), with evaluable
    normalized conditional density p(y|x). For each i form q_-i(y)=(K−1)^−1 sum_(j!=i)
    p(y|X_j). Then I(X;Y)<=E[K^−1 sum_i log(p(Y_i|X_i)/q_-i(Y_i))], assuming the expectations
    are well-defined. The mixture q_-i is independent of the held-out pair because
    it uses only the other inputs. Conditional on those inputs, the gap of the corresponding
    variational upper bound is KL(p(Y)||q_-i(Y)), a nonnegative quantity. Including
    the paired input in this denominator instead gives the known-conditional InfoNCE
    lower-bound construction, so the exclusion is essential. A finite batch computes
    an estimator of the upper-bound expectation rather than a guaranteed upper bound
    on its own. Limitations: The conditional must be normalized and evaluable for
    cross-sample inputs. Treating an uncalibrated score as p(y|x) invalidates the
    stated derivation. For small batches or sharply separated conditional supports,
    the leave-one-out mixture can be tiny or zero where the held-out conditional is
    positive, producing a loose or infinite upper bound. Independence of batch examples
    is part of the proof. Correlated samples or using the held-out input to construct
    its own denominator require a different argument. The expected bound does not
    certify a realized finite-sample number. Optimization of a noisy estimate does
    not guarantee monotonic true information reduction or convergence. No encoder
    implementation or benchmark was reproduced.'
  dimensions:
  - name: concept-kind
    value: mathematical_method
    definition: A mathematical objective/inequality, or for IM a specified alternating
      optimization algorithm; not a trained instance or benchmark outcome.
    evidence_ids:
    - leaveoneoutmutualinformationupperbound-source
  - name: aio-assessment
    value: snapshot-bounded no match
    definition: 'The inspected candidates describe networks, feature-extraction tasks
      or self-supervised tasks, not the mathematical information bound. Shared variational
      terminology, an optional neural parameterization or downstream use does not
      establish a suitable mapping. AIO:VariationalAutoEncoder: A probabilistic latent
      autoencoder architecture is not a variational information inequality; neither
      implies the other. AIO:AutoEncoderNetwork: Reconstruction networks can use information
      objectives but do not identify this mathematical bound. AIO:RepresentationLearning:
      The target is a deep-network representation-learning class; it is a possible
      use of a bound, not the bound itself. AIO:DeepNeuralNetwork: A neural critic
      or decoder is one possible parameterization, not the information formula. AIO:FeatureExtraction:
      This preprocessing task does not specify an information estimator or bound.
      AIO:BayesianNetwork: Conditional distributions do not make this bound a directed
      graphical-model architecture. AIO:SelfsupervisedLearning: A self-generated prediction
      task does not specify this population information inequality.'
    evidence_ids:
    - identity
    - mapping
- assessment_id: bound-versus-procedure
  area: scope
  topic: BA bound and named IM optimization procedure
  outcome: supported
  target_ids:
  - AIMech:BarberAgakovBound
  - AIMech:VariationalInformationMaximizationIMAlgorithm
  evidence_ids:
  - barberagakovbound-source
  - barberagakovbound-source-1
  - variationalinformationmaximizationimalgorithm-source
  - neighbors
  summary: Retain the normalized-decoder inequality separately from the alternating
    encoder/decoder algorithm.
  details: The BA objective has an expected conditional-KL gap. Fixed source entropy
    can be dropped for optimization but is still needed for a numeric information
    value. IM alternates constrained decoder fitting and encoder optimization; exact
    coordinate ascent improves the bound, while restricted decoders and approximate
    updates do not certify increasing true MI, global optimality or finite convergence.
    The Gaussian projection example supports a scoped FeatureExtraction association.
- assessment_id: nwj-tuba-parameterization
  area: representation
  topic: Named parameterizations with explicit algebraic equivalence
  outcome: supported
  target_ids:
  - AIMech:NguyenWainwrightJordanBound
  - AIMech:TUBABound
  evidence_ids:
  - nguyenwainwrightjordanbound-source
  - nguyenwainwrightjordanbound-source-1
  - tubabound-source
  summary: Retain NWJ and TUBA with their exact reparameterization relation explicit.
  details: NWJ uses E_P T−E_Q exp(T−1). TUBA separates f and a>0 and is exactly NWJ
    at T=f−log a+1; a=e recovers the same-f NWJ form. The records do not claim inequivalent
    unrestricted bound families. Their named parameterization and optimizer/normalizer
    interpretation justify retaining distinct curated identities with this limitation.
    No universal accuracy advantage or neural convexity is inferred.
- assessment_id: interpolation-audit
  area: consistency
  topic: Interpolation formula, independence and contradictory source ceiling
  outcome: supported
  target_ids:
  - AIMech:InterpolatedVariationalInformationBound
  evidence_ids:
  - interpolatedvariationalinformationbound-source
  - interpolatedvariationalinformationbound-source-1
  - interpolatedvariationalinformationbound-source-2
  - ceiling-calculation
  summary: Retain the main Eq11 construction and qualify the printed ceiling with
    a reproducible finite case.
  details: The interpolated normalizer is inside the critic ratio, not a convex mixture
    of final scalar bounds. Independent product samples must exclude every input in
    their normalizer. Endpoint identities require the stated reparameterization/cancellation.
    The paper’s log(K/alpha) statement conflicts with its displayed formula on the
    saved finite case; the conservative1+log(K/alpha) follows directly, and alpha1
    retains the sharper InfoNCE ceiling. The supplement’s extra log, notebook endpoint
    docstring and score-orientation differences are cited rather than silently treated
    as equivalent.
- assessment_id: leave-one-out-scope
  area: scope
  topic: Known conditionals and expected upper bounds
  outcome: supported
  target_ids:
  - AIMech:LeaveOneOutMutualInformationUpperBound
  evidence_ids:
  - leaveoneoutmutualinformationupperbound-source
  - neighbors
  summary: Retain the normalized-conditional leave-one-out upper bound as distinct
    from InfoNCE.
  details: The omitted paired input makes the mixture independent of the held-out
    pair, yielding an expected marginal-KL gap. Including the positive conditional
    gives the corresponding lower-bound construction. A generic score or one realized
    batch is not certified by this argument, and disjoint support may make the upper
    bound infinite.
- assessment_id: mapping-boundaries
  area: grounding
  topic: Task association and no-match assessments
  outcome: supported
  target_ids:
  - AIMech:BarberAgakovBound
  - AIMech:VariationalInformationMaximizationIMAlgorithm
  - AIMech:NguyenWainwrightJordanBound
  - AIMech:TUBABound
  - AIMech:InterpolatedVariationalInformationBound
  - AIMech:LeaveOneOutMutualInformationUpperBound
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain the scoped IM task relation and explicit no-match assessments for
    all five bounds.
  details: Seven exact AIO nodes with definitions, scoped synonyms and outgoing relations
    were inspected. IM has a qualified related match to FeatureExtraction for the
    explicitly developed encoder/linear-compression configuration. Each of the five
    mathematical bounds has a snapshot-bounded no-match assessment with seven rejected
    targets. Network architectures, a possible neural parameterization, or an incidental
    downstream task are not forced mappings for an information inequality.
- assessment_id: issue46-current-evidence
  area: provenance
  topic: Traceable implementation and supplemental limitations
  outcome: supported
  target_ids:
  - AIMech:TUBABound
  - AIMech:InterpolatedVariationalInformationBound
  evidence_ids:
  - tubabound-source-1
  - interpolatedvariationalinformationbound-source-1
  - interpolatedvariationalinformationbound-source-2
  - corrections
  summary: Current records include the missing versioned sources and precise limitation
    citations.
  details: The draft limitations were based on inspected sources but omitted complete
    structured evidence metadata. Issue46 corrected that gap. Added notebook/supplement
    sources, cell/table locators and limitation claims were reread and hashed. This
    is a current-state review; no earlier structured finding or independent approval
    is invented.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:BarberAgakovBound
  - AIMech:VariationalInformationMaximizationIMAlgorithm
  - AIMech:NguyenWainwrightJordanBound
  - AIMech:TUBABound
  - AIMech:InterpolatedVariationalInformationBound
  - AIMech:LeaveOneOutMutualInformationUpperBound
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - barberagakovbound-source
  - barberagakovbound-source-1
  - variationalinformationmaximizationimalgorithm-source
  - nguyenwainwrightjordanbound-source
  - nguyenwainwrightjordanbound-source-1
  - tubabound-source
  - tubabound-source-1
  - interpolatedvariationalinformationbound-source
  - interpolatedvariationalinformationbound-source-1
  - interpolatedvariationalinformationbound-source-2
  - leaveoneoutmutualinformationupperbound-source
  - ceiling-calculation
  - corrections
  rationale: Keep a normalized-decoder inequality separate from its alternating optimizer;
    preserve the named NWJ/TUBA parameterizations while explicitly stating their algebraic
    relationship; distinguish an interpolated multi-sample lower bound and a known-conditional
    leave-one-out upper bound. Shared mathematics or applications do not justify erasing
    those declared scopes. This is a curator boundary judgment, not an upstream ontology
    mutation.
limitations:
- Adversarial author self-review only; all six records remain DRAFT.
- The selected NWJ/TUBA identities are distinct named parameterizations, not claims
  of mathematically inequivalent unrestricted variational families.
- Expected inequalities and unbiased fixed-function objectives are not finite-sample
  certificates or optimizer guarantees.
- The paper, supplement and notebook contain discrepancies; the record states the
  main formula, source differences and curator calculation explicitly.
- The finite-domain enumeration is reproducible arithmetic, not a learned-estimator
  experiment or an author-issued correction.
- Only declared source pages and notebook cells were read; no TensorFlow environment,
  training or benchmark was reproduced.
- Positive discoveries and the remaining frontier keep the goal active.
tags:
- native-concepts
- mutual-information
- variational-bounds
- self-review
- discovery-ongoing
```
