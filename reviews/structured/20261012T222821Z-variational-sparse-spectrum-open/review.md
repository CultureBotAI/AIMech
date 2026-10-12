# Scientific author self-review of variational sparse-spectrum inference

- Review: 20261012T222821Z-variational-sparse-spectrum-open
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T22:21:51Z
- Finished UTC: 2026-10-12T22:28:21Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Retain the three supported inference variants. One minor sfVSSGP notation omission needs correction: define its per-observation expected-log-likelihood summand. All records remain DRAFT.

## Scope And Provenance

All fields of the three newly added Gal–Turner inference algorithms.

Selection: Exact maintained IDs: AIMech:VariationalSparseSpectrumGaussianProcessInference, AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference, AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 078961fc07b8f7b8e27bc83b6eadb319243d329c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:VariationalSparseSpectrumGaussianProcessInference | data/curated/VariationalSparseSpectrumGaussianProcessInference.yaml | maintained | Variational sparse-spectrum Gaussian-process inference |
| AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference | data/curated/FactorizedVariationalSparseSpectrumGaussianProcessInference.yaml | maintained | Factorized variational sparse-spectrum Gaussian-process inference |
| AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference | data/curated/StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.yaml | maintained | Stochastic factorized variational sparse-spectrum Gaussian-process inference |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:VariationalSparseSpectrumGaussianProcessInference, AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference, AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 147.10s (0:02:27)<br>Checked 442 record(s); 0 failed.<br>Checked 549 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 195 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 193,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:VariationalSparseSpectrumGaussianProcessInference, AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference, AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:VariationalSparseSpectrumGaussianProcessInference, AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference, AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:VariationalSparseSpectrumGaussianProcessInference, AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference, AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference | Exited 0 without output. |
| Finite variational moment, bound and minibatch calculations | passed | True | AIMech:VariationalSparseSpectrumGaussianProcessInference, AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference, AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference | {"scope": "Finite analytic variational arithmetic for two independent Gaussian angular frequencies and fixed phases; no optimization run, training pipeline, author-code execution or benchmark.", "parameters": {"inputs": [-0.5, 0.3, 1.2], "responses": [0.5, -0.4, 1.1], "precision": 2.5, "frequency_means": [0.4, 1.1], "frequency_variances": [0.2, 0.3], "phases": [0.1, 0.4], "feature_amplitude": 1}, "coefficient_variational_optimum": {"mean": [0.48177885990972563, -0.32175955071506274], "full_covariance": [[0.22434521854578196, -0.16067821017791495], [-0.16067821017791495, 0.3000855926963357]], "diagonal_restriction_covariance": [[0.13831147399309499, 0.0], [0.0, 0.1850063082198107]]}, "bounds_without_common_frequency_kl": {"explicit_full": -4.479572834285149, "collapsed": -4.479572834285147, "diagonal_restricted": -4.721411744269482, "full_minus_diagonal": 0.2418389099843347}, "prediction": {"input": 0.8, "mean": 0.32882606194399255, "noisy_variance": 0.5841232122619725, "first_feature_mean": 0.856481991029161, "first_feature_second_moment": 0.758355493046214, "first_feature_squared_mean": 0.7335614009572758, "quadrature_max_abs_error": 9.769962616701378e-15}, "minibatch_identity": {"full_diagonal_bound": -4.721411744269482, "uniform_two_of_three_estimates": [-4.502211292065503, -4.629821323365673, -5.032202617377271], "mean": -4.721411744269482, "incorrect_scaled_kl_mean": -5.302554318213935}, "phase_comparison": {"interval": [0.2, 1.1], "uniform_mean": 0.5125380476498214, "uniform_second_moment": 0.37842468615012925, "fixed_at_lower_endpoint_mean": 0.814018729226292}, "far_field": {"input": 100.0, "noisy_variance": 0.8300354447871958, "derived_limit": 0.8300354447871958, "unit_coefficient_prior_noisy_variance": 1.4}, "caveats": ["The full coefficient optimum is within a factorization between coefficients and frequencies, not exact frequency inference.", "The same fixed frequency KL is omitted in both displayed bound values; do not compare them directly to complete evidence.", "The diagonal coefficient restriction is strictly looser in this nonorthogonal finite example.", "Uniform phase integration differs from fixing the phase at one endpoint; zero width is not a finite-density variational distribution.", "The far-field variance depends on fitted variational coefficient moments and need not equal the original prior variance."]} |

## Scientific And Domain Assessments

### Retain the three explicitly named inference variants

identity: supported. Targets: AIMech:VariationalSparseSpectrumGaussianProcessInference, AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference, AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.

The coefficient family and optimization estimator distinguish the records.

The Section 7 labels identify VSSGP with the analytic generally full coefficient optimum, fVSSGP with explicit diagonal factors, and sfVSSGP with its data-minibatch estimator. The collapsed variant remains mean-field between spectra and coefficients. None is identical to the paired-feature SSGP prior, generic mean-field inference, generic SGD, or Gaussian test-input prediction. Tan uses a shared uncertain inverse-lengthscale vector; Hoang permits a joint affine variational distribution. Their methods remain separate unresolved leads, not synonyms.

### Algorithm-to-regression relationship

grounding: supported. Targets: AIMech:VariationalSparseSpectrumGaussianProcessInference, AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference, AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.

The related regression mappings are supported.

RegressionAnalysis is a task class in this AIO snapshot despite the exact synonym Regression model. These procedures infer a covariate/response model; they are not that general task or a neural layer/autoencoder. BayesianNetwork and ProbabilisticGraphicalModel describe broader model contexts and do not identify this specific spectral fitting algorithm. The two bias terms differ from epistemic frequency uncertainty. No AIO subclass or equivalence axiom is implied.

### finite-feature-model

evidence: supported. Targets: AIMech:VariationalSparseSpectrumGaussianProcessInference.

The substantive mechanism is supported within its stated family and scope.

For one squared-exponential component, use K features phi_k(x)=sqrt(2*sigma^2/K)*cos(2*pi*w_k^T*L^{-1}*(x-z_k)+b_k), where L=diag(2*pi*l_j), l_j&gt;0, and z_k are feature locations. Independent standardized frequencies have prior N(0,I); phases have uniform priors on [0,2*pi]. For N inputs, Phi has shape N by K. Each output column y_d has likelihood N(Phi*a_d,tau^{-1}*I), tau&gt;0, with independent unit-Gaussian coefficient priors a_d. The variational family separates q(A) from q(omega), omega collecting frequencies and phases, and factors q(omega) across k with diagonal-Gaussian frequency factors and uniform phase intervals [alpha_k,beta_k] with 0&lt;=alpha_k&lt;beta_k&lt;=2*pi. This is a finite-feature hierarchical regression model; integrating its random features does not generally yield the original full-kernel GP.

### variational-objective

evidence: supported. Targets: AIMech:VariationalSparseSpectrumGaussianProcessInference.

The substantive mechanism is supported within its stated family and scope.

The evidence lower bound is the expected Gaussian log likelihood minus KL(q(A)&#124;&#124;p(A)) and KL(q(omega)&#124;&#124;p(omega)). For F=E_q[Phi], H=E_q[Phi^T*Phi], q(a_d)=N(m_d,S_d) and response column y_d, its output-d likelihood contribution is -N/2*log(2*pi/tau)-tau/2*[y_d^T*y_d-2*y_d^T*F*m_d+tr(H*(S_d+m_d*m_d^T))]. Gaussian trigonometric moments and uniform-phase integrals give F and H analytically. Distinct feature moments factor under the declared independent spectral factors; a feature’s second moment must be computed as E[phi_k^2], not (E[phi_k])^2.

### optimal-coefficient-factor

evidence: supported. Targets: AIMech:VariationalSparseSpectrumGaussianProcessInference.

The substantive mechanism is supported within its stated family and scope.

At fixed spectral distribution, tau and feature hyperparameters, define H=E_q[Phi^T*Phi], F=E_q[Phi], B=I+tau*H and g_d=F^T*y_d. Functional optimization over the coefficient factor gives S=B^{-1} and m_d=tau*S*g_d. S is generally full, shared across output columns. Substitution into the ELBO removes explicit coefficient variational parameters and yields the source’s Equation 7. This is optimal within the coefficient-versus-spectrum factorization; it does not integrate the true coupled frequency/coefficient posterior exactly or preserve the earlier diagonal coefficient restriction.

### predictive-moments

evidence: supported. Targets: AIMech:VariationalSparseSpectrumGaussianProcessInference.

The substantive mechanism is supported within its stated family and scope.

For a fixed query, let phi be its K-dimensional column feature vector, f=E_q[phi], R=E_q[phi*phi^T], and M=[m_1,...,m_D]. Under q(A)q(omega), the response mean is M^T*f and its covariance is tau^{-1}*I+diag_d[tr(R*S_d)]+M^T*(R-f*f^T)*M. Shared spectral uncertainty can therefore correlate different outputs even though their coefficient factors are independent. These are moments of the variational predictive mixture, which is not generally Gaussian; the latent-output covariance omits only the future-observation-noise term.

### implementation-boundary

evidence: supported. Targets: AIMech:VariationalSparseSpectrumGaussianProcessInference.

The substantive mechanism is supported within its stated family and scope.

The inspected author model source computes Gaussian-frequency moments with the phase alpha fixed inside each cosine; its beta argument does not enter those moments and its objective contains frequency KL without a phase KL. Thus that revision implements a fixed-phase conditional variant, not integration over the paper’s positive-width uniform phase factors. Its second-moment diagonal uses the cosine-square expectation. The optimal-coefficient routine retains a full covariance and adds numerical diagonal regularization; source-code reading does not establish an executed result or exact correspondence to every published experiment.

### finite-feature-model

evidence: supported. Targets: AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference.

The substantive mechanism is supported within its stated family and scope.

For one squared-exponential component, use K features phi_k(x)=sqrt(2*sigma^2/K)*cos(2*pi*w_k^T*L^{-1}*(x-z_k)+b_k), where L=diag(2*pi*l_j), l_j&gt;0, and z_k are feature locations. Independent standardized frequencies have prior N(0,I); phases have uniform priors on [0,2*pi]. For N inputs, Phi has shape N by K. Each output column y_d has likelihood N(Phi*a_d,tau^{-1}*I), tau&gt;0, with independent unit-Gaussian coefficient priors a_d. The variational family separates q(A) from q(omega), omega collecting frequencies and phases, and factors q(omega) across k with diagonal-Gaussian frequency factors and uniform phase intervals [alpha_k,beta_k] with 0&lt;=alpha_k&lt;beta_k&lt;=2*pi. This is a finite-feature hierarchical regression model; integrating its random features does not generally yield the original full-kernel GP.

### variational-objective

evidence: supported. Targets: AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference.

The substantive mechanism is supported within its stated family and scope.

The evidence lower bound is the expected Gaussian log likelihood minus KL(q(A)&#124;&#124;p(A)) and KL(q(omega)&#124;&#124;p(omega)). For F=E_q[Phi], H=E_q[Phi^T*Phi], q(a_d)=N(m_d,S_d) and response column y_d, its output-d likelihood contribution is -N/2*log(2*pi/tau)-tau/2*[y_d^T*y_d-2*y_d^T*F*m_d+tr(H*(S_d+m_d*m_d^T))]. Gaussian trigonometric moments and uniform-phase integrals give F and H analytically. Distinct feature moments factor under the declared independent spectral factors; a feature’s second moment must be computed as E[phi_k^2], not (E[phi_k])^2.

### explicit-diagonal-factors

evidence: supported. Targets: AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference.

The substantive mechanism is supported within its stated family and scope.

The fVSSGP variant retains explicit means m_d and positive diagonal covariances S_d for each coefficient vector, jointly optimizing them with spectral variational parameters. The data term in Equation 6 decomposes into individual observation/output contributions L_nd, giving Equation 8 with two global KL penalties subtracted once. The diagonal coefficient family is restricted relative to the generally full analytic coefficient optimum of VSSGP; the factorized expression and the optimized full-covariance bound are not interchangeable. Distributing the sum of likelihood contributions does not itself change the variational family.

### predictive-moments

evidence: supported. Targets: AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference.

The substantive mechanism is supported within its stated family and scope.

For a fixed query, let phi be its K-dimensional column feature vector, f=E_q[phi], R=E_q[phi*phi^T], and M=[m_1,...,m_D]. Under q(A)q(omega), the response mean is M^T*f and its covariance is tau^{-1}*I+diag_d[tr(R*S_d)]+M^T*(R-f*f^T)*M. Shared spectral uncertainty can therefore correlate different outputs even though their coefficient factors are independent. These are moments of the variational predictive mixture, which is not generally Gaussian; the latent-output covariance omits only the future-observation-noise term.

### implementation-boundary

evidence: supported. Targets: AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference.

The substantive mechanism is supported within its stated family and scope.

The inspected author model source computes Gaussian-frequency moments with the phase alpha fixed inside each cosine; its beta argument does not enter those moments and its objective contains frequency KL without a phase KL. Thus that revision implements a fixed-phase conditional variant, not integration over the paper’s positive-width uniform phase factors. Its second-moment diagonal uses the cosine-square expectation. The optimal-coefficient routine retains a full covariance and adds numerical diagonal regularization; source-code reading does not establish an executed result or exact correspondence to every published experiment.

### finite-feature-model

evidence: supported. Targets: AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.

The substantive mechanism is supported within its stated family and scope.

For one squared-exponential component, use K features phi_k(x)=sqrt(2*sigma^2/K)*cos(2*pi*w_k^T*L^{-1}*(x-z_k)+b_k), where L=diag(2*pi*l_j), l_j&gt;0, and z_k are feature locations. Independent standardized frequencies have prior N(0,I); phases have uniform priors on [0,2*pi]. For N inputs, Phi has shape N by K. Each output column y_d has likelihood N(Phi*a_d,tau^{-1}*I), tau&gt;0, with independent unit-Gaussian coefficient priors a_d. The variational family separates q(A) from q(omega), omega collecting frequencies and phases, and factors q(omega) across k with diagonal-Gaussian frequency factors and uniform phase intervals [alpha_k,beta_k] with 0&lt;=alpha_k&lt;beta_k&lt;=2*pi. This is a finite-feature hierarchical regression model; integrating its random features does not generally yield the original full-kernel GP.

### variational-objective

evidence: supported. Targets: AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.

The substantive mechanism is supported within its stated family and scope.

The evidence lower bound is the expected Gaussian log likelihood minus KL(q(A)&#124;&#124;p(A)) and KL(q(omega)&#124;&#124;p(omega)). For F=E_q[Phi], H=E_q[Phi^T*Phi], q(a_d)=N(m_d,S_d) and response column y_d, its output-d likelihood contribution is -N/2*log(2*pi/tau)-tau/2*[y_d^T*y_d-2*y_d^T*F*m_d+tr(H*(S_d+m_d*m_d^T))]. Gaussian trigonometric moments and uniform-phase integrals give F and H analytically. Distinct feature moments factor under the declared independent spectral factors; a feature’s second moment must be computed as E[phi_k^2], not (E[phi_k])^2.

### minibatch-estimator

evidence: supported. Targets: AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.

The substantive mechanism is supported within its stated family and scope.

For a nonempty batch S of uniformly sampled observations, Equation 9 uses (N/&#124;S&#124;)*sum_{n in S,d} L_nd-KL(q(A)&#124;&#124;p(A))-KL(q(omega)&#124;&#124;p(omega)), retaining the explicit diagonal coefficient family of fVSSGP. With fixed current variational parameters and the stated uniform sampling, its expectation is the full fVSSGP objective; gradient unbiasedness additionally requires valid differentiation under expectation. Stochastic optimization updates spectral and coefficient variational parameters using this noisy objective or its gradients. A sampled value need not be a lower bound pointwise. Subsampling the already collapsed VSSGP log determinant and matrix inverse would be a different estimator.

### predictive-moments

evidence: supported. Targets: AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.

The substantive mechanism is supported within its stated family and scope.

For a fixed query, let phi be its K-dimensional column feature vector, f=E_q[phi], R=E_q[phi*phi^T], and M=[m_1,...,m_D]. Under q(A)q(omega), the response mean is M^T*f and its covariance is tau^{-1}*I+diag_d[tr(R*S_d)]+M^T*(R-f*f^T)*M. Shared spectral uncertainty can therefore correlate different outputs even though their coefficient factors are independent. These are moments of the variational predictive mixture, which is not generally Gaussian; the latent-output covariance omits only the future-observation-noise term.

### implementation-boundary

evidence: supported. Targets: AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.

The substantive mechanism is supported within its stated family and scope.

The inspected author model source computes Gaussian-frequency moments with the phase alpha fixed inside each cosine; its beta argument does not enter those moments and its objective contains frequency KL without a phase KL. Thus that revision implements a fixed-phase conditional variant, not integration over the paper’s positive-width uniform phase factors. Its second-moment diagonal uses the cosine-square expectation. The optimal-coefficient routine retains a full covariance and adds numerical diagonal regularization; source-code reading does not establish an executed result or exact correspondence to every published experiment.

### Optimal coefficient covariance versus explicit diagonal restriction

consistency: supported. Targets: AIMech:VariationalSparseSpectrumGaussianProcessInference, AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference.

The full and diagonal objectives are distinguished correctly.

With B=I+tau H, the optimal full covariance is B inverse; its mean is tau B inverse F transpose y. At a fixed spectral factor, the diagonal optimum instead has covariance entries 1/B_ii. The two-dimensional nonorthogonal example yields a positive bound gap of 0.2418389099843347, equal to half the log determinant ratio. The same frequency KL is explicitly omitted from both displayed numerical values; their difference is the checked quantity. Functional optimization within q(A)q(omega) is not exact coupled-posterior inference.

### First moments, second moments and output covariance

consistency: supported. Targets: AIMech:VariationalSparseSpectrumGaussianProcessInference, AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference, AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.

The predictive formula retains coefficient and frequency uncertainty.

For a K-column feature, R is K by K and M is K by D, so the response covariance is D by D. Total covariance produces the stated diagonal coefficient-variance term and the shared-frequency cross-output term. Future observation noise enters once. Simpson integration at fixed Gaussian frequency parameters agrees with the first and second moment identities within 1e-10. This does not establish exact Gaussian shape of the mixture. The supplement final-page diagonal is inconsistent with its own cosine-square identity; the record correctly retains the second moment instead.

### Likelihood-only expansion factor

consistency: supported. Targets: AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.

The uniform-minibatch estimator has the correct weighting.

Exhaustively averaging all two-of-three batches at fixed variational parameters returns the full diagonal-family objective. Expanding the global coefficient KL along with the likelihood fails this check. Unbiased gradients also need interchange conditions, and a noisy objective sample need not lie below evidence. The nonlinear already-collapsed objective is not the same estimator. The mechanism needs a local definition of its likelihood summand, recorded separately below.

### Uniform phase factors versus fixed-phase code

provenance: supported. Targets: AIMech:VariationalSparseSpectrumGaussianProcessInference, AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference, AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.

The implementation is accurately bounded to static, pinned evidence.

The model source uses alpha in cosine and ignores beta in get_EPhi; the KL consists of Gaussian frequency and, in the explicit branch, Gaussian coefficient terms. The example fixes the phase parameters. The record therefore does not claim that this code integrates the paper’s interval-valued phase distribution. get_opt_A returns a full coefficient covariance with added regularization. Uniform-phase and fixed-endpoint means differ in the curator example; a zero-width density is not silently treated as a finite-KL endpoint. The source revision predates proceedings and is not certified as the exact experiment code.

### Finite prior and empirical limits

scope: supported. Targets: AIMech:VariationalSparseSpectrumGaussianProcessInference, AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference, AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.

Overbroad full-GP and overfitting guarantees are excluded.

One random-phase cosine per sampled frequency does not give the earlier stationary paired-feature kernel for each realization. Marginalizing random covariance is a mixture, not automatically the original GP. Feature-mean decay is distinct from random-feature decay; the example far-field noisy variance is 0.8300354447871958 rather than prior 1.4. Local optima, factorization and implementation sampling constraints remain explicit. No runtime, benchmark improvement or universal calibration claim is curated.

### Complete field and source audit

provenance: supported. Targets: AIMech:VariationalSparseSpectrumGaussianProcessInference, AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference, AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.

All maintained fields were read, including the common and variant-specific contents.

Read the first complete record and all fields differing in the other two, verifying the remaining fields equal. Assessed IDs, names/acronyms, algorithm kind, definitions, identity notes, all fifteen claim occurrences and citations, three source versions/access/hash entries per record, AIO snapshot and mapping, limitations and actual curation timestamps. YAMLs equal report entries. Tan and Hoang are fully read follow-up evidence with unresolved curation, not additional asserted records. DRAFT statuses are retained.

### Define the per-observation likelihood summand

consistency: concern. Targets: AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.

The sfVSSGP estimator requires a local definition of L_nd.

Define L_nd as E_q[log N(y_nd;phi_n^T a_d,tau^-1)], with y_nd the observed response and phi_n the feature column for observation n. This makes clear that the expanded sum contains likelihood terms only, separate from both global KL penalties. The existing weighting and algorithm identity are supported; the finding is a bounded notation omission.

## Findings

### F1: Define the likelihood summand in the sfVSSGP minibatch estimator

minor / open / confirmed; issue key: aimech-sfvssgp-likelihood-notation.

The standalone minibatch formula uses L_nd without defining its local expected-log-likelihood meaning. The preceding claim defines only an entire output-column contribution. Add the per-observation summand and its response/feature symbols so the likelihood expansion and unscaled global KL penalties can be read without consulting another record or the paper.

## Recommended Actions And Acceptance Checks

### A1

Define L_nd, y_nd and the observation feature column in the sfVSSGP claim; synchronize its report/page, record actual history and save a linked successor review.

- The record states L_nd=E_q[log N(y_nd;phi_n^T a_d,tau^-1)] and defines the observation/response symbols.
- The likelihood N/&#124;S&#124; factor and unscaled KL penalties, record identity and mappings remain unchanged.
- Required checks pass and a successor review explicitly resolves this occurrence for the affected maintained target.

## Category Boundaries

- retain: AIMech:VariationalSparseSpectrumGaussianProcessInference, AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference, AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference. Analytically optimized full coefficient factors, explicit diagonal factors and the minibatch estimator of the latter define distinct named inference variants. A shared model and source do not make their objectives or updates identical.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T222135Z-variational-sparse-spectrum.json | supports | Compared all 442 pinned AIO IDs, names and scoped synonyms and 546 maintained IDs, names and aliases; none matches the three proposed identities after normalization. Full-text searches of the recovery, older discovery and original Documents checkouts included hidden and ignored files, with 22, 0 and 0 matched lines. All 21 distinct matched contents were read: pending source leads and source-reading context, not existing records. Assessed 50 semantic AIO rows and 172 maintained names/definitions, ten full annotated AIO CLASS nodes with incident edges and generated YAML, and five complete native context records. Generic mean-field methods and stochastic gradient descent do not identify this finite spectral regression procedure. The paired-feature SSGP model and its uncertain-test-input transforms also differ: these methods infer uncertain spectral parameters from training data. The three source labels distinguish optimal unrestricted coefficient factors, explicit diagonal factors, and data-minibatch optimization. Absence is bounded to the searched pin and corpus. |
| mapping | sources/aio/aio.json | supports | Assessed 50 semantic AIO rows, 172 native names/definitions, ten full annotated AIO nodes with incident edges/generated YAML, and five full native context records. The related regression mapping preserves the method/task distinction. |
| calculation | research/discovery/vssgp-boundaries.py | supports | Fixed analytic and one-dimensional quadrature checks distinguish full versus diagonal coefficient optima, first versus second moments, phase integration and far-field limits. Exhaustive two-of-three minibatches check unbiased objective weighting with global KL retained once; no optimization or benchmark. |
| gal2015 | https://proceedings.mlr.press/v37/galb15.pdf; Sections 2–7, Equations 2 and 5–11, PDF pp. 2–5; fixed-phase experimental setup PDF p. 6. | supports | ICML 2015, PMLR 37:655–664; all ten official main-paper PDF pages, figures, tables and references visually read. Locators use PDF page indices. Main/supplement were fully read during preparation, with moment and variant pages reread against the captured records. Implementation evidence is static source inspection, not execution. |
| gal2015-supp | https://proceedings.mlr.press/v37/galb15-supp.pdf; Identities 1–3 and Propositions 1–5, PDF pp. 1–3; covariance and diagonal-factor discussion PDF pp. 3–4. | supports | Official four-page supplement linked from the Gal–Turner ICML 2015 proceedings page; all pages visually read. Its title differs from the main paper and some equation references are stale. Main/supplement were fully read during preparation, with moment and variant pages reread against the captured records. Implementation evidence is static source inspection, not execution. |
| author-implementation | https://raw.githubusercontent.com/yaringal/VSSGP/f0331a963c0779828a178f0c86f597f0c451dcaf/VSSGP_model.py; Complete VSSGP_model.py at the pinned commit, especially get_EPhi, get_opt_A, get_model and get_model_exact_A. | supports | Author repository commit f0331a963c0779828a178f0c86f597f0c451dcaf (2015-04-07), complete 131-line model source read statically, with README, optimizer and example as context. This revision predates the proceedings; exact experimental-version correspondence is not established. No code imported or executed. Main/supplement were fully read during preparation, with moment and variant pages reread against the captured records. Implementation evidence is static source inspection, not execution. |
| summand-notation | data/curated/StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.yaml | supports | Complete record inspection shows the minibatch-estimator claim uses L_nd without defining it. The earlier objective claim defines only the complete output-column likelihood contribution. The source defines the per-observation summand directly above Equation 8. |

## Limits And Additional Notes

- Author self-review only, with one minor maintained-record notation finding. Source-paper inconsistencies and implementation limitations are distinguished from this actionable local omission.
- Added three DRAFT native algorithms: 549 maintained and 442 unchanged generated records. The 734-entry main frontier retains 486 pending and 56 partly addressed cohorts; other nested source leads remain preserved through predecessor reports. Discovery has not reached saturation.
- Gal main10 and supplement4, Tan21 and Hoang11 rendered pages all read. Only Gal methods are curated in this round; unresolved Tan and Hoang details remain explicitly pending.
- All four pinned Gal implementation files were statically read. No author code, fitting pipeline or benchmark executed. Curator calculations test fixed moments, coefficient-bound differences and exhaustive finite minibatch arithmetic only.
- Original-checkout synchronization and old round141 cleanup await explicit approval following automatic review rejection; this work uses only the isolated public recovery checkout.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T222821Z-variational-sparse-spectrum-open
kind: category
repository: CultureBotAI/AIMech
title: Scientific author self-review of variational sparse-spectrum inference
started_at: '2026-10-12T22:21:51Z'
finished_at: '2026-10-12T22:28:21Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent challenged variant identity, coefficient
    restrictions, sampling weights, predictive covariance, source inconsistencies
    and pinned implementation scope. This is adversarial author self-review, not independent
    approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Retain the three supported inference variants. One minor sfVSSGP notation
  omission needs correction: define its per-observation expected-log-likelihood summand.
  All records remain DRAFT.'
source:
  git_revision: 078961fc07b8f7b8e27bc83b6eadb319243d329c
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/ErrorPropagationBias.yaml
    sha256: 98a57881fa8f2a8f47efdf37f12f8dbcc66df495112e46c454d26cf4d934c5e4
    role: context
  - path: data/aio/KernelLayer.yaml
    sha256: 0723e7f15d57807a1f922cd87b878593fb167757c7429dd06e99bde723290d43
    role: context
  - path: data/aio/LinearRegression.yaml
    sha256: 9b6f1b2ea06d9a47e5f7cf94c66afeaa6d40c3e7d0fdb5037d2c25fabc6d8167
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/RandomEffectsModel.yaml
    sha256: 4e3f50ef012b217822c2b731cce1b07dff14e66826f26d7717a6dab42d482d4c
    role: context
  - path: data/aio/RegressionAnalysis.yaml
    sha256: 6f5d48096556a2ec31770aab306219e9020919940b4e80554639cc97aaa94bc6
    role: context
  - path: data/aio/TimeSeriesForecasting.yaml
    sha256: 88bbef37663508cc885b40d258cdb6b720c627c0f73af1935c01a372c18b3863
    role: context
  - path: data/aio/UncertaintyBias.yaml
    sha256: b013064a48a14beef5040486a8d1cbd11d9c503739d6fc89f73460b08f38e8f3
    role: context
  - path: data/aio/VariationalAutoEncoder.yaml
    sha256: f8f523c5f2cecf91f1510c5ab74bfd36d717f3e683a9a8384e44a3f855e4c45e
    role: context
  - path: data/curated/BlackBoxVariationalInference.yaml
    sha256: 8237d3233ae06163b8fab5b4fa047ffc938e275bc1e3ede883348e06c2b266a8
    role: context
  - path: data/curated/FactorizedVariationalSparseSpectrumGaussianProcessInference.yaml
    sha256: 8b8ff1fc769a4df4b039bd65c36d484b3829afb9eae18f91e659a93dc78f9ef3
    role: target
  - path: data/curated/FullyFactorizedMeanFieldInference.yaml
    sha256: 102be6f77143b26acb0d482f91e2dfa58ea113f2188b14b92067484cc4f9408d
    role: context
  - path: data/curated/SparseSpectrumGaussianProcessRegression.yaml
    sha256: d1680103fd8df79740d12629429a4009709f0b2e136140fc95c565852f63db44
    role: context
  - path: data/curated/StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.yaml
    sha256: 022c17b1a0d4815ecbda9e3953a4101800b1e3234970988f31c63c287c1233f6
    role: target
  - path: data/curated/StochasticGradientDescent.yaml
    sha256: 5c57fc809ae8667d5be8cda421cc9f0bd1f0c668f64ba3d7b23d788528b46e97
    role: context
  - path: data/curated/StructuredMeanFieldInference.yaml
    sha256: 3cd31e539123908291c2a9a394792c52dacf415ce3c19c4d6a42e9be6173c86b
    role: context
  - path: data/curated/VariationalSparseSpectrumGaussianProcessInference.yaml
    sha256: e508cdaea10654cf24a1b219887c88e4d3236cd440a2db4c2f9a8eee7742bba2
    role: target
  - path: research/discovery/20261012T222135Z-variational-sparse-spectrum.json
    sha256: 0248e07b50d0396542206e09a4f59662bef6b8cec201fbef223279f8d2536904
    role: context
  - path: research/discovery/vssgp-boundaries.py
    sha256: d589c26ec5c4a2de8e74e4bf3dc66402f8bc39a79c9c155bfc187b0072b74f08
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
- target_id: AIMech:VariationalSparseSpectrumGaussianProcessInference
  path: data/curated/VariationalSparseSpectrumGaussianProcessInference.yaml
  label: Variational sparse-spectrum Gaussian-process inference
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/VariationalSparseSpectrumGaussianProcessInference.yaml
    role: maintained
- target_id: AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference
  path: data/curated/FactorizedVariationalSparseSpectrumGaussianProcessInference.yaml
  label: Factorized variational sparse-spectrum Gaussian-process inference
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FactorizedVariationalSparseSpectrumGaussianProcessInference.yaml
    role: maintained
- target_id: AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
  path: data/curated/StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.yaml
  label: Stochastic factorized variational sparse-spectrum Gaussian-process inference
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.yaml
    role: maintained
scope:
  description: All fields of the three newly added Gal–Turner inference algorithms.
  selection: 'Exact maintained IDs: AIMech:VariationalSparseSpectrumGaussianProcessInference,
    AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference, AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference'
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:VariationalSparseSpectrumGaussianProcessInference
  - AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
  exclusions:
  - target: Tan and Hoang follow-up algorithms
    reason: Full sources read; curation and source concerns remain pending.
  - target: Author-code execution and empirical reproduction
    reason: Static code reading and finite curator arithmetic only.
  - target: Other generated/native records
    reason: Identity/mapping context, not complete scientific rereview.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:VariationalSparseSpectrumGaussianProcessInference
  - AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 147.10s (0:02:27)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 549 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 195 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 193,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:VariationalSparseSpectrumGaussianProcessInference
  - AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
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
  - AIMech:VariationalSparseSpectrumGaussianProcessInference
  - AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
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
  - AIMech:VariationalSparseSpectrumGaussianProcessInference
  - AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Finite variational moment, bound and minibatch calculations
  command: python3 research/discovery/vssgp-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:VariationalSparseSpectrumGaussianProcessInference
  - AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
  exit_code: 0
  expected_exit_code: 0
  summary: '{"scope": "Finite analytic variational arithmetic for two independent
    Gaussian angular frequencies and fixed phases; no optimization run, training pipeline,
    author-code execution or benchmark.", "parameters": {"inputs": [-0.5, 0.3, 1.2],
    "responses": [0.5, -0.4, 1.1], "precision": 2.5, "frequency_means": [0.4, 1.1],
    "frequency_variances": [0.2, 0.3], "phases": [0.1, 0.4], "feature_amplitude":
    1}, "coefficient_variational_optimum": {"mean": [0.48177885990972563, -0.32175955071506274],
    "full_covariance": [[0.22434521854578196, -0.16067821017791495], [-0.16067821017791495,
    0.3000855926963357]], "diagonal_restriction_covariance": [[0.13831147399309499,
    0.0], [0.0, 0.1850063082198107]]}, "bounds_without_common_frequency_kl": {"explicit_full":
    -4.479572834285149, "collapsed": -4.479572834285147, "diagonal_restricted": -4.721411744269482,
    "full_minus_diagonal": 0.2418389099843347}, "prediction": {"input": 0.8, "mean":
    0.32882606194399255, "noisy_variance": 0.5841232122619725, "first_feature_mean":
    0.856481991029161, "first_feature_second_moment": 0.758355493046214, "first_feature_squared_mean":
    0.7335614009572758, "quadrature_max_abs_error": 9.769962616701378e-15}, "minibatch_identity":
    {"full_diagonal_bound": -4.721411744269482, "uniform_two_of_three_estimates":
    [-4.502211292065503, -4.629821323365673, -5.032202617377271], "mean": -4.721411744269482,
    "incorrect_scaled_kl_mean": -5.302554318213935}, "phase_comparison": {"interval":
    [0.2, 1.1], "uniform_mean": 0.5125380476498214, "uniform_second_moment": 0.37842468615012925,
    "fixed_at_lower_endpoint_mean": 0.814018729226292}, "far_field": {"input": 100.0,
    "noisy_variance": 0.8300354447871958, "derived_limit": 0.8300354447871958, "unit_coefficient_prior_noisy_variance":
    1.4}, "caveats": ["The full coefficient optimum is within a factorization between
    coefficients and frequencies, not exact frequency inference.", "The same fixed
    frequency KL is omitted in both displayed bound values; do not compare them directly
    to complete evidence.", "The diagonal coefficient restriction is strictly looser
    in this nonorthogonal finite example.", "Uniform phase integration differs from
    fixing the phase at one endpoint; zero width is not a finite-density variational
    distribution.", "The far-field variance depends on fitted variational coefficient
    moments and need not equal the original prior variance."]}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T222135Z-variational-sparse-spectrum.json
  accessed_at: '2026-10-12T22:21:51Z'
  support: supports
  summary: 'Compared all 442 pinned AIO IDs, names and scoped synonyms and 546 maintained
    IDs, names and aliases; none matches the three proposed identities after normalization.
    Full-text searches of the recovery, older discovery and original Documents checkouts
    included hidden and ignored files, with 22, 0 and 0 matched lines. All 21 distinct
    matched contents were read: pending source leads and source-reading context, not
    existing records. Assessed 50 semantic AIO rows and 172 maintained names/definitions,
    ten full annotated AIO CLASS nodes with incident edges and generated YAML, and
    five complete native context records. Generic mean-field methods and stochastic
    gradient descent do not identify this finite spectral regression procedure. The
    paired-feature SSGP model and its uncertain-test-input transforms also differ:
    these methods infer uncertain spectral parameters from training data. The three
    source labels distinguish optimal unrestricted coefficient factors, explicit diagonal
    factors, and data-minibatch optimization. Absence is bounded to the searched pin
    and corpus.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-12T22:21:51Z'
  support: supports
  summary: Assessed 50 semantic AIO rows, 172 native names/definitions, ten full annotated
    AIO nodes with incident edges/generated YAML, and five full native context records.
    The related regression mapping preserves the method/task distinction.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/vssgp-boundaries.py
  accessed_at: '2026-10-12T22:21:51Z'
  snapshot_sha256: d589c26ec5c4a2de8e74e4bf3dc66402f8bc39a79c9c155bfc187b0072b74f08
  support: supports
  summary: Fixed analytic and one-dimensional quadrature checks distinguish full versus
    diagonal coefficient optima, first versus second moments, phase integration and
    far-field limits. Exhaustive two-of-three minibatches check unbiased objective
    weighting with global KL retained once; no optimization or benchmark.
- evidence_id: gal2015
  kind: primary_source
  reference: https://proceedings.mlr.press/v37/galb15.pdf
  locator: Sections 2–7, Equations 2 and 5–11, PDF pp. 2–5; fixed-phase experimental
    setup PDF p. 6.
  accessed_at: '2026-10-12T22:01:48Z'
  snapshot_sha256: 158bdd0ef09cc1926957e34b45c98327e437745f88a658453eda98fdc4798177
  support: supports
  summary: ICML 2015, PMLR 37:655–664; all ten official main-paper PDF pages, figures,
    tables and references visually read. Locators use PDF page indices. Main/supplement
    were fully read during preparation, with moment and variant pages reread against
    the captured records. Implementation evidence is static source inspection, not
    execution.
- evidence_id: gal2015-supp
  kind: primary_source
  reference: https://proceedings.mlr.press/v37/galb15-supp.pdf
  locator: Identities 1–3 and Propositions 1–5, PDF pp. 1–3; covariance and diagonal-factor
    discussion PDF pp. 3–4.
  accessed_at: '2026-10-12T22:01:48Z'
  snapshot_sha256: 19b4948bcf25f2e6aa6306bab66586c501e3ad2ffca185fb5dbd074b83e7c235
  support: supports
  summary: Official four-page supplement linked from the Gal–Turner ICML 2015 proceedings
    page; all pages visually read. Its title differs from the main paper and some
    equation references are stale. Main/supplement were fully read during preparation,
    with moment and variant pages reread against the captured records. Implementation
    evidence is static source inspection, not execution.
- evidence_id: author-implementation
  kind: primary_source
  reference: https://raw.githubusercontent.com/yaringal/VSSGP/f0331a963c0779828a178f0c86f597f0c451dcaf/VSSGP_model.py
  locator: Complete VSSGP_model.py at the pinned commit, especially get_EPhi, get_opt_A,
    get_model and get_model_exact_A.
  accessed_at: '2026-10-12T22:08:51Z'
  snapshot_sha256: 1227bfd02ccd6a6577b9eea0db2135e7483954fd0ff35a1d77ec14458900ebfa
  support: supports
  summary: Author repository commit f0331a963c0779828a178f0c86f597f0c451dcaf (2015-04-07),
    complete 131-line model source read statically, with README, optimizer and example
    as context. This revision predates the proceedings; exact experimental-version
    correspondence is not established. No code imported or executed. Main/supplement
    were fully read during preparation, with moment and variant pages reread against
    the captured records. Implementation evidence is static source inspection, not
    execution.
- evidence_id: summand-notation
  kind: record_content
  reference: data/curated/StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.yaml
  accessed_at: '2026-10-12T22:21:51Z'
  snapshot_sha256: 022c17b1a0d4815ecbda9e3953a4101800b1e3234970988f31c63c287c1233f6
  support: supports
  summary: Complete record inspection shows the minibatch-estimator claim uses L_nd
    without defining it. The earlier objective claim defines only the complete output-column
    likelihood contribution. The source defines the per-observation summand directly
    above Equation 8.
assessments:
- assessment_id: identity
  area: identity
  topic: Retain the three explicitly named inference variants
  outcome: supported
  target_ids:
  - AIMech:VariationalSparseSpectrumGaussianProcessInference
  - AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - identity
  - gal2015
  - gal2015-supp
  summary: The coefficient family and optimization estimator distinguish the records.
  details: The Section 7 labels identify VSSGP with the analytic generally full coefficient
    optimum, fVSSGP with explicit diagonal factors, and sfVSSGP with its data-minibatch
    estimator. The collapsed variant remains mean-field between spectra and coefficients.
    None is identical to the paired-feature SSGP prior, generic mean-field inference,
    generic SGD, or Gaussian test-input prediction. Tan uses a shared uncertain inverse-lengthscale
    vector; Hoang permits a joint affine variational distribution. Their methods remain
    separate unresolved leads, not synonyms.
- assessment_id: grounding
  area: grounding
  topic: Algorithm-to-regression relationship
  outcome: supported
  target_ids:
  - AIMech:VariationalSparseSpectrumGaussianProcessInference
  - AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - mapping
  - gal2015
  summary: The related regression mappings are supported.
  details: RegressionAnalysis is a task class in this AIO snapshot despite the exact
    synonym Regression model. These procedures infer a covariate/response model; they
    are not that general task or a neural layer/autoencoder. BayesianNetwork and ProbabilisticGraphicalModel
    describe broader model contexts and do not identify this specific spectral fitting
    algorithm. The two bias terms differ from epistemic frequency uncertainty. No
    AIO subclass or equivalence axiom is implied.
- assessment_id: 0-finite-feature-model
  area: evidence
  topic: finite-feature-model
  outcome: supported
  target_ids:
  - AIMech:VariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - gal2015
  - gal2015-supp
  summary: The substantive mechanism is supported within its stated family and scope.
  details: For one squared-exponential component, use K features phi_k(x)=sqrt(2*sigma^2/K)*cos(2*pi*w_k^T*L^{-1}*(x-z_k)+b_k),
    where L=diag(2*pi*l_j), l_j>0, and z_k are feature locations. Independent standardized
    frequencies have prior N(0,I); phases have uniform priors on [0,2*pi]. For N inputs,
    Phi has shape N by K. Each output column y_d has likelihood N(Phi*a_d,tau^{-1}*I),
    tau>0, with independent unit-Gaussian coefficient priors a_d. The variational
    family separates q(A) from q(omega), omega collecting frequencies and phases,
    and factors q(omega) across k with diagonal-Gaussian frequency factors and uniform
    phase intervals [alpha_k,beta_k] with 0<=alpha_k<beta_k<=2*pi. This is a finite-feature
    hierarchical regression model; integrating its random features does not generally
    yield the original full-kernel GP.
- assessment_id: 0-variational-objective
  area: evidence
  topic: variational-objective
  outcome: supported
  target_ids:
  - AIMech:VariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - gal2015
  - gal2015-supp
  - calculation
  summary: The substantive mechanism is supported within its stated family and scope.
  details: The evidence lower bound is the expected Gaussian log likelihood minus
    KL(q(A)||p(A)) and KL(q(omega)||p(omega)). For F=E_q[Phi], H=E_q[Phi^T*Phi], q(a_d)=N(m_d,S_d)
    and response column y_d, its output-d likelihood contribution is -N/2*log(2*pi/tau)-tau/2*[y_d^T*y_d-2*y_d^T*F*m_d+tr(H*(S_d+m_d*m_d^T))].
    Gaussian trigonometric moments and uniform-phase integrals give F and H analytically.
    Distinct feature moments factor under the declared independent spectral factors;
    a feature’s second moment must be computed as E[phi_k^2], not (E[phi_k])^2.
- assessment_id: 0-optimal-coefficient-factor
  area: evidence
  topic: optimal-coefficient-factor
  outcome: supported
  target_ids:
  - AIMech:VariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - gal2015
  - gal2015-supp
  - calculation
  summary: The substantive mechanism is supported within its stated family and scope.
  details: At fixed spectral distribution, tau and feature hyperparameters, define
    H=E_q[Phi^T*Phi], F=E_q[Phi], B=I+tau*H and g_d=F^T*y_d. Functional optimization
    over the coefficient factor gives S=B^{-1} and m_d=tau*S*g_d. S is generally full,
    shared across output columns. Substitution into the ELBO removes explicit coefficient
    variational parameters and yields the source’s Equation 7. This is optimal within
    the coefficient-versus-spectrum factorization; it does not integrate the true
    coupled frequency/coefficient posterior exactly or preserve the earlier diagonal
    coefficient restriction.
- assessment_id: 0-predictive-moments
  area: evidence
  topic: predictive-moments
  outcome: supported
  target_ids:
  - AIMech:VariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - gal2015
  - gal2015-supp
  - calculation
  summary: The substantive mechanism is supported within its stated family and scope.
  details: For a fixed query, let phi be its K-dimensional column feature vector,
    f=E_q[phi], R=E_q[phi*phi^T], and M=[m_1,...,m_D]. Under q(A)q(omega), the response
    mean is M^T*f and its covariance is tau^{-1}*I+diag_d[tr(R*S_d)]+M^T*(R-f*f^T)*M.
    Shared spectral uncertainty can therefore correlate different outputs even though
    their coefficient factors are independent. These are moments of the variational
    predictive mixture, which is not generally Gaussian; the latent-output covariance
    omits only the future-observation-noise term.
- assessment_id: 0-implementation-boundary
  area: evidence
  topic: implementation-boundary
  outcome: supported
  target_ids:
  - AIMech:VariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - author-implementation
  - gal2015
  summary: The substantive mechanism is supported within its stated family and scope.
  details: The inspected author model source computes Gaussian-frequency moments with
    the phase alpha fixed inside each cosine; its beta argument does not enter those
    moments and its objective contains frequency KL without a phase KL. Thus that
    revision implements a fixed-phase conditional variant, not integration over the
    paper’s positive-width uniform phase factors. Its second-moment diagonal uses
    the cosine-square expectation. The optimal-coefficient routine retains a full
    covariance and adds numerical diagonal regularization; source-code reading does
    not establish an executed result or exact correspondence to every published experiment.
- assessment_id: 1-finite-feature-model
  area: evidence
  topic: finite-feature-model
  outcome: supported
  target_ids:
  - AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - gal2015
  - gal2015-supp
  summary: The substantive mechanism is supported within its stated family and scope.
  details: For one squared-exponential component, use K features phi_k(x)=sqrt(2*sigma^2/K)*cos(2*pi*w_k^T*L^{-1}*(x-z_k)+b_k),
    where L=diag(2*pi*l_j), l_j>0, and z_k are feature locations. Independent standardized
    frequencies have prior N(0,I); phases have uniform priors on [0,2*pi]. For N inputs,
    Phi has shape N by K. Each output column y_d has likelihood N(Phi*a_d,tau^{-1}*I),
    tau>0, with independent unit-Gaussian coefficient priors a_d. The variational
    family separates q(A) from q(omega), omega collecting frequencies and phases,
    and factors q(omega) across k with diagonal-Gaussian frequency factors and uniform
    phase intervals [alpha_k,beta_k] with 0<=alpha_k<beta_k<=2*pi. This is a finite-feature
    hierarchical regression model; integrating its random features does not generally
    yield the original full-kernel GP.
- assessment_id: 1-variational-objective
  area: evidence
  topic: variational-objective
  outcome: supported
  target_ids:
  - AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - gal2015
  - gal2015-supp
  - calculation
  summary: The substantive mechanism is supported within its stated family and scope.
  details: The evidence lower bound is the expected Gaussian log likelihood minus
    KL(q(A)||p(A)) and KL(q(omega)||p(omega)). For F=E_q[Phi], H=E_q[Phi^T*Phi], q(a_d)=N(m_d,S_d)
    and response column y_d, its output-d likelihood contribution is -N/2*log(2*pi/tau)-tau/2*[y_d^T*y_d-2*y_d^T*F*m_d+tr(H*(S_d+m_d*m_d^T))].
    Gaussian trigonometric moments and uniform-phase integrals give F and H analytically.
    Distinct feature moments factor under the declared independent spectral factors;
    a feature’s second moment must be computed as E[phi_k^2], not (E[phi_k])^2.
- assessment_id: 1-explicit-diagonal-factors
  area: evidence
  topic: explicit-diagonal-factors
  outcome: supported
  target_ids:
  - AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - gal2015
  - gal2015-supp
  - calculation
  summary: The substantive mechanism is supported within its stated family and scope.
  details: The fVSSGP variant retains explicit means m_d and positive diagonal covariances
    S_d for each coefficient vector, jointly optimizing them with spectral variational
    parameters. The data term in Equation 6 decomposes into individual observation/output
    contributions L_nd, giving Equation 8 with two global KL penalties subtracted
    once. The diagonal coefficient family is restricted relative to the generally
    full analytic coefficient optimum of VSSGP; the factorized expression and the
    optimized full-covariance bound are not interchangeable. Distributing the sum
    of likelihood contributions does not itself change the variational family.
- assessment_id: 1-predictive-moments
  area: evidence
  topic: predictive-moments
  outcome: supported
  target_ids:
  - AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - gal2015
  - gal2015-supp
  - calculation
  summary: The substantive mechanism is supported within its stated family and scope.
  details: For a fixed query, let phi be its K-dimensional column feature vector,
    f=E_q[phi], R=E_q[phi*phi^T], and M=[m_1,...,m_D]. Under q(A)q(omega), the response
    mean is M^T*f and its covariance is tau^{-1}*I+diag_d[tr(R*S_d)]+M^T*(R-f*f^T)*M.
    Shared spectral uncertainty can therefore correlate different outputs even though
    their coefficient factors are independent. These are moments of the variational
    predictive mixture, which is not generally Gaussian; the latent-output covariance
    omits only the future-observation-noise term.
- assessment_id: 1-implementation-boundary
  area: evidence
  topic: implementation-boundary
  outcome: supported
  target_ids:
  - AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - author-implementation
  - gal2015
  summary: The substantive mechanism is supported within its stated family and scope.
  details: The inspected author model source computes Gaussian-frequency moments with
    the phase alpha fixed inside each cosine; its beta argument does not enter those
    moments and its objective contains frequency KL without a phase KL. Thus that
    revision implements a fixed-phase conditional variant, not integration over the
    paper’s positive-width uniform phase factors. Its second-moment diagonal uses
    the cosine-square expectation. The optimal-coefficient routine retains a full
    covariance and adds numerical diagonal regularization; source-code reading does
    not establish an executed result or exact correspondence to every published experiment.
- assessment_id: 2-finite-feature-model
  area: evidence
  topic: finite-feature-model
  outcome: supported
  target_ids:
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - gal2015
  - gal2015-supp
  summary: The substantive mechanism is supported within its stated family and scope.
  details: For one squared-exponential component, use K features phi_k(x)=sqrt(2*sigma^2/K)*cos(2*pi*w_k^T*L^{-1}*(x-z_k)+b_k),
    where L=diag(2*pi*l_j), l_j>0, and z_k are feature locations. Independent standardized
    frequencies have prior N(0,I); phases have uniform priors on [0,2*pi]. For N inputs,
    Phi has shape N by K. Each output column y_d has likelihood N(Phi*a_d,tau^{-1}*I),
    tau>0, with independent unit-Gaussian coefficient priors a_d. The variational
    family separates q(A) from q(omega), omega collecting frequencies and phases,
    and factors q(omega) across k with diagonal-Gaussian frequency factors and uniform
    phase intervals [alpha_k,beta_k] with 0<=alpha_k<beta_k<=2*pi. This is a finite-feature
    hierarchical regression model; integrating its random features does not generally
    yield the original full-kernel GP.
- assessment_id: 2-variational-objective
  area: evidence
  topic: variational-objective
  outcome: supported
  target_ids:
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - gal2015
  - gal2015-supp
  - calculation
  summary: The substantive mechanism is supported within its stated family and scope.
  details: The evidence lower bound is the expected Gaussian log likelihood minus
    KL(q(A)||p(A)) and KL(q(omega)||p(omega)). For F=E_q[Phi], H=E_q[Phi^T*Phi], q(a_d)=N(m_d,S_d)
    and response column y_d, its output-d likelihood contribution is -N/2*log(2*pi/tau)-tau/2*[y_d^T*y_d-2*y_d^T*F*m_d+tr(H*(S_d+m_d*m_d^T))].
    Gaussian trigonometric moments and uniform-phase integrals give F and H analytically.
    Distinct feature moments factor under the declared independent spectral factors;
    a feature’s second moment must be computed as E[phi_k^2], not (E[phi_k])^2.
- assessment_id: 2-minibatch-estimator
  area: evidence
  topic: minibatch-estimator
  outcome: supported
  target_ids:
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - gal2015
  - calculation
  summary: The substantive mechanism is supported within its stated family and scope.
  details: For a nonempty batch S of uniformly sampled observations, Equation 9 uses
    (N/|S|)*sum_{n in S,d} L_nd-KL(q(A)||p(A))-KL(q(omega)||p(omega)), retaining the
    explicit diagonal coefficient family of fVSSGP. With fixed current variational
    parameters and the stated uniform sampling, its expectation is the full fVSSGP
    objective; gradient unbiasedness additionally requires valid differentiation under
    expectation. Stochastic optimization updates spectral and coefficient variational
    parameters using this noisy objective or its gradients. A sampled value need not
    be a lower bound pointwise. Subsampling the already collapsed VSSGP log determinant
    and matrix inverse would be a different estimator.
- assessment_id: 2-predictive-moments
  area: evidence
  topic: predictive-moments
  outcome: supported
  target_ids:
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - gal2015
  - gal2015-supp
  - calculation
  summary: The substantive mechanism is supported within its stated family and scope.
  details: For a fixed query, let phi be its K-dimensional column feature vector,
    f=E_q[phi], R=E_q[phi*phi^T], and M=[m_1,...,m_D]. Under q(A)q(omega), the response
    mean is M^T*f and its covariance is tau^{-1}*I+diag_d[tr(R*S_d)]+M^T*(R-f*f^T)*M.
    Shared spectral uncertainty can therefore correlate different outputs even though
    their coefficient factors are independent. These are moments of the variational
    predictive mixture, which is not generally Gaussian; the latent-output covariance
    omits only the future-observation-noise term.
- assessment_id: 2-implementation-boundary
  area: evidence
  topic: implementation-boundary
  outcome: supported
  target_ids:
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - author-implementation
  - gal2015
  summary: The substantive mechanism is supported within its stated family and scope.
  details: The inspected author model source computes Gaussian-frequency moments with
    the phase alpha fixed inside each cosine; its beta argument does not enter those
    moments and its objective contains frequency KL without a phase KL. Thus that
    revision implements a fixed-phase conditional variant, not integration over the
    paper’s positive-width uniform phase factors. Its second-moment diagonal uses
    the cosine-square expectation. The optimal-coefficient routine retains a full
    covariance and adds numerical diagonal regularization; source-code reading does
    not establish an executed result or exact correspondence to every published experiment.
- assessment_id: bound-families
  area: consistency
  topic: Optimal coefficient covariance versus explicit diagonal restriction
  outcome: supported
  target_ids:
  - AIMech:VariationalSparseSpectrumGaussianProcessInference
  - AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - gal2015
  - gal2015-supp
  - calculation
  summary: The full and diagonal objectives are distinguished correctly.
  details: With B=I+tau H, the optimal full covariance is B inverse; its mean is tau
    B inverse F transpose y. At a fixed spectral factor, the diagonal optimum instead
    has covariance entries 1/B_ii. The two-dimensional nonorthogonal example yields
    a positive bound gap of 0.2418389099843347, equal to half the log determinant
    ratio. The same frequency KL is explicitly omitted from both displayed numerical
    values; their difference is the checked quantity. Functional optimization within
    q(A)q(omega) is not exact coupled-posterior inference.
- assessment_id: moments
  area: consistency
  topic: First moments, second moments and output covariance
  outcome: supported
  target_ids:
  - AIMech:VariationalSparseSpectrumGaussianProcessInference
  - AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - gal2015
  - gal2015-supp
  - author-implementation
  - calculation
  summary: The predictive formula retains coefficient and frequency uncertainty.
  details: For a K-column feature, R is K by K and M is K by D, so the response covariance
    is D by D. Total covariance produces the stated diagonal coefficient-variance
    term and the shared-frequency cross-output term. Future observation noise enters
    once. Simpson integration at fixed Gaussian frequency parameters agrees with the
    first and second moment identities within 1e-10. This does not establish exact
    Gaussian shape of the mixture. The supplement final-page diagonal is inconsistent
    with its own cosine-square identity; the record correctly retains the second moment
    instead.
- assessment_id: minibatch-weight
  area: consistency
  topic: Likelihood-only expansion factor
  outcome: supported
  target_ids:
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - gal2015
  - calculation
  summary: The uniform-minibatch estimator has the correct weighting.
  details: Exhaustively averaging all two-of-three batches at fixed variational parameters
    returns the full diagonal-family objective. Expanding the global coefficient KL
    along with the likelihood fails this check. Unbiased gradients also need interchange
    conditions, and a noisy objective sample need not lie below evidence. The nonlinear
    already-collapsed objective is not the same estimator. The mechanism needs a local
    definition of its likelihood summand, recorded separately below.
- assessment_id: phase-code
  area: provenance
  topic: Uniform phase factors versus fixed-phase code
  outcome: supported
  target_ids:
  - AIMech:VariationalSparseSpectrumGaussianProcessInference
  - AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - gal2015
  - author-implementation
  - calculation
  summary: The implementation is accurately bounded to static, pinned evidence.
  details: The model source uses alpha in cosine and ignores beta in get_EPhi; the
    KL consists of Gaussian frequency and, in the explicit branch, Gaussian coefficient
    terms. The example fixes the phase parameters. The record therefore does not claim
    that this code integrates the paper’s interval-valued phase distribution. get_opt_A
    returns a full coefficient covariance with added regularization. Uniform-phase
    and fixed-endpoint means differ in the curator example; a zero-width density is
    not silently treated as a finite-KL endpoint. The source revision predates proceedings
    and is not certified as the exact experiment code.
- assessment_id: limits
  area: scope
  topic: Finite prior and empirical limits
  outcome: supported
  target_ids:
  - AIMech:VariationalSparseSpectrumGaussianProcessInference
  - AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - gal2015
  - gal2015-supp
  - calculation
  summary: Overbroad full-GP and overfitting guarantees are excluded.
  details: One random-phase cosine per sampled frequency does not give the earlier
    stationary paired-feature kernel for each realization. Marginalizing random covariance
    is a mixture, not automatically the original GP. Feature-mean decay is distinct
    from random-feature decay; the example far-field noisy variance is 0.8300354447871958
    rather than prior 1.4. Local optima, factorization and implementation sampling
    constraints remain explicit. No runtime, benchmark improvement or universal calibration
    claim is curated.
- assessment_id: all-fields
  area: provenance
  topic: Complete field and source audit
  outcome: supported
  target_ids:
  - AIMech:VariationalSparseSpectrumGaussianProcessInference
  - AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - identity
  - mapping
  - gal2015
  - gal2015-supp
  - author-implementation
  summary: All maintained fields were read, including the common and variant-specific
    contents.
  details: Read the first complete record and all fields differing in the other two,
    verifying the remaining fields equal. Assessed IDs, names/acronyms, algorithm
    kind, definitions, identity notes, all fifteen claim occurrences and citations,
    three source versions/access/hash entries per record, AIO snapshot and mapping,
    limitations and actual curation timestamps. YAMLs equal report entries. Tan and
    Hoang are fully read follow-up evidence with unresolved curation, not additional
    asserted records. DRAFT statuses are retained.
- assessment_id: summand-notation
  area: consistency
  topic: Define the per-observation likelihood summand
  outcome: concern
  target_ids:
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - summand-notation
  - gal2015
  summary: The sfVSSGP estimator requires a local definition of L_nd.
  details: Define L_nd as E_q[log N(y_nd;phi_n^T a_d,tau^-1)], with y_nd the observed
    response and phi_n the feature column for observation n. This makes clear that
    the expanded sum contains likelihood terms only, separate from both global KL
    penalties. The existing weighting and algorithm identity are supported; the finding
    is a bounded notation omission.
findings:
- finding_id: F1
  issue_key: aimech-sfvssgp-likelihood-notation
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Define the likelihood summand in the sfVSSGP minibatch estimator
  description: The standalone minibatch formula uses L_nd without defining its local
    expected-log-likelihood meaning. The preceding claim defines only an entire output-column
    contribution. Add the per-observation summand and its response/feature symbols
    so the likelihood expansion and unscaled global KL penalties can be read without
    consulting another record or the paper.
  target_ids:
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
  field_paths:
  - claims[2].statement
  evidence_ids:
  - summand-notation
  - gal2015
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.yaml
    role: maintained
actions:
- action_id: A1
  description: Define L_nd, y_nd and the observation feature column in the sfVSSGP
    claim; synchronize its report/page, record actual history and save a linked successor
    review.
  finding_ids:
  - F1
  target_ids:
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.yaml
    role: maintained
  acceptance_checks:
  - The record states L_nd=E_q[log N(y_nd;phi_n^T a_d,tau^-1)] and defines the observation/response
    symbols.
  - The likelihood N/|S| factor and unscaled KL penalties, record identity and mappings
    remain unchanged.
  - Required checks pass and a successor review explicitly resolves this occurrence
    for the affected maintained target.
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:VariationalSparseSpectrumGaussianProcessInference
  - AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference
  - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
  evidence_ids:
  - identity
  - gal2015
  - gal2015-supp
  - calculation
  rationale: Analytically optimized full coefficient factors, explicit diagonal factors
    and the minibatch estimator of the latter define distinct named inference variants.
    A shared model and source do not make their objectives or updates identical.
  proposed_groups:
  - label: Variational sparse-spectrum Gaussian-process inference
    target_ids:
    - AIMech:VariationalSparseSpectrumGaussianProcessInference
  - label: Factorized variational sparse-spectrum Gaussian-process inference
    target_ids:
    - AIMech:FactorizedVariationalSparseSpectrumGaussianProcessInference
  - label: Stochastic factorized variational sparse-spectrum Gaussian-process inference
    target_ids:
    - AIMech:StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference
limitations:
- Author self-review only, with one minor maintained-record notation finding. Source-paper
  inconsistencies and implementation limitations are distinguished from this actionable
  local omission.
- 'Added three DRAFT native algorithms: 549 maintained and 442 unchanged generated
  records. The 734-entry main frontier retains 486 pending and 56 partly addressed
  cohorts; other nested source leads remain preserved through predecessor reports.
  Discovery has not reached saturation.'
- Gal main10 and supplement4, Tan21 and Hoang11 rendered pages all read. Only Gal
  methods are curated in this round; unresolved Tan and Hoang details remain explicitly
  pending.
- All four pinned Gal implementation files were statically read. No author code, fitting
  pipeline or benchmark executed. Curator calculations test fixed moments, coefficient-bound
  differences and exhaustive finite minibatch arithmetic only.
- Original-checkout synchronization and old round141 cleanup await explicit approval
  following automatic review rejection; this work uses only the isolated public recovery
  checkout.
related_reviews: []
links: []
tags:
- native-concepts
- gaussian-processes
- variational-inference
- category-boundaries
- self-review
- discovery-ongoing
```
