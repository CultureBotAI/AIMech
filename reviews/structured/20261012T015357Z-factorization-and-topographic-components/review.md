# Scientific self-review of nonnegative factorization and independent-component methods

- Review: 20261012T015357Z-factorization-and-topographic-components
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T01:50:57Z
- Finished UTC: 2026-10-12T01:53:57Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain NMF, Lee-Seung multiplicative updates, standard logistic Infomax ICA and topographic ICA with distinct representation, optimization and model scopes. Explicitly preserve zero-locking, differential-entropy, distribution mismatch, likelihood-surrogate and moment boundaries. No actionable curation finding remains in the four additions.

## Scope And Provenance

All fields of four source-defined factorization and latent-component concepts.

Selection: Exact maintained IDs NonnegativeMatrixFactorization, LeeSeungMultiplicativeUpdates, InfomaxICA and TopographicICA; full selected cohort without sampling.
Coverage: full; 4 reviewed / 4 in the declared population.
Source: working_tree at Git base a7523fc2877d2d46b5e5050d40b3cc50e611867e.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:NonnegativeMatrixFactorization | data/curated/NonnegativeMatrixFactorization.yaml | maintained | Nonnegative Matrix Factorization |
| AIMech:LeeSeungMultiplicativeUpdates | data/curated/LeeSeungMultiplicativeUpdates.yaml | maintained | Lee-Seung Multiplicative Updates |
| AIMech:InfomaxICA | data/curated/InfomaxICA.yaml | maintained | Infomax Independent Component Analysis |
| AIMech:TopographicICA | data/curated/TopographicICA.yaml | maintained | Topographic Independent Component Analysis |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:NonnegativeMatrixFactorization, AIMech:LeeSeungMultiplicativeUpdates, AIMech:InfomaxICA, AIMech:TopographicICA | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 86.07s (0:01:26)<br>Checked 442 record(s); 0 failed.<br>Checked 454 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 132 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 129,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:NonnegativeMatrixFactorization, AIMech:LeeSeungMultiplicativeUpdates, AIMech:InfomaxICA, AIMech:TopographicICA | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> Initial sandbox execution failed to resolve raw.githubusercontent.com (exit 1); the read-only check was rerun with network access and passed. No governed bytes changed. |
| uv run --locked aimech check-source | passed | True | AIMech:NonnegativeMatrixFactorization, AIMech:LeeSeungMultiplicativeUpdates, AIMech:InfomaxICA, AIMech:TopographicICA | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:NonnegativeMatrixFactorization, AIMech:LeeSeungMultiplicativeUpdates, AIMech:InfomaxICA, AIMech:TopographicICA | Command exited 0 with no output. |
| Factorization and topographic-component boundaries | passed | True | AIMech:NonnegativeMatrixFactorization, AIMech:LeeSeungMultiplicativeUpdates, AIMech:InfomaxICA, AIMech:TopographicICA | {"nmf_block_objectives": {"squared_error": [20.345, 4.643645222757498, 0.5121403961160389], "generalized_kl": [9.004858394930977, 1.9726972204360944, 0.5333623412979441]}, "nmf_simultaneous_scalar_errors": [0.5625, 9], "zero_locked_half_squared_gradient": [[0.0], [-0.5]], "infomax_gradient_max_error": 2.905420903864808e-10, "generalized_sigmoid_scores": [0.0735, 0.5], "tica_lower_bound_mass": 0.6054988603092419, "normalized_surrogate_max_ratio": 1.10089843785717, "tica_energy_covariance": 0.03452932098765432, "tica_gradient_max_error": 2.3984542130151e-10, "cauchy_truncated_second_moments": [5.4296487585369215, 62.66834322228795, 635.6204089871416]} |

## Scientific And Domain Assessments

### Definition, identity, claim support, limitations and AIO mapping direction

evidence: supported. Targets: AIMech:NonnegativeMatrixFactorization.

The mathematical factorization is distinct from a particular fitting algorithm, trained dictionary or application. The separately represented Lee-Seung multiplicative updates optimize two specified objectives. Nonnegative factors need not be sparse, orthogonal or uniquely determined; this is not the exact sparse-coding identity in AIO or ordinary PCA. Non-negative and British factorisation spellings name the same method. Four candidate identities were compared against all 442 pinned AIO IDs, labels and scoped synonyms and 450 preceding native IDs, names and aliases, with no normalized match. Ignored/hidden full-checkout searches returned the same 106 matched-line set in each checkout after the prior merge. All matched excerpts from 76 files were read; they are discovery context, not existing concept records. The semantic search covered all pinned labels and scoped synonyms and returned 212 rows: 205 byte-equivalent prior readings and seven additional rows, all inspected. Twenty-three annotated AIO nodes with outgoing edges comprise 21 unchanged prior readings and two new inspections. Thirty contextual YAMLs, including seven native neighbors, comprise 25 unchanged prior readings and five complete new readings. This absence assessment is bounded to the pinned snapshot and inspected maintained corpus.

For V in the nonnegative n-by-m matrices, seek W of size n-by-r and H of size r-by-m with nonnegative entries and V approximately W H. Columns of W supply basis elements and columns of H their nonnegative coefficients. Choosing r below the data dimensions yields a compressed representation with product rank at most r, but small r is a modeling choice rather than a consequence of nonnegativity. Factors can be dense. The inspected source fits either squared Frobenius error &#124;&#124;V-WH&#124;&#124;_F^2 or generalized KL divergence sum_ij[V_ij log(V_ij/(WH)_ij)-V_ij+(WH)_ij]. The latter is a divergence between nonnegative arrays, not necessarily normalized probability distributions and not a symmetric distance. By continuity a zero V entry contributes the corresponding reconstruction, while a positive V entry with zero reconstruction gives infinite divergence. An observed zero contributes to these objectives; it is not automatically a missing value. Nonnegativity supports additive representations but does not guarantee recovery of unique physical parts or causes. For any positive diagonal D, W D and D^(-1) H give the same reconstruction, and a common factor permutation also preserves it. The nonconvex joint fitting problem and chosen objective further affect the result. These algebraic ambiguities remain even when a factorization has small reconstruction error. Limitations: No universal sparsity, uniqueness, causal interpretation or global optimization guarantee follows from the nonnegative constraint. Additional constraints or probabilistic models define narrower methods. The two inspected objectives are representative source formulations, not an exhaustive definition of every NMF loss or algorithm. Missing-data masks, regularization, sparse constraints and probabilistic count models require their own specification. The inspected paper is an algorithm and proof contribution; no new benchmark ranking, author implementation, empirical fitting or parts-recognition result was reproduced.

### Definition, identity, claim support, limitations and AIO mapping direction

evidence: supported. Targets: AIMech:LeeSeungMultiplicativeUpdates.

Scoped to Equations 4-5 and their auxiliary-function derivations in Lee and Seung, NIPS 2000. This is a particular family of fitting rules, distinct from the general NMF factorization, every multiplicative optimizer, generic EM and the fixed-prior Iterated Wiener Filter. An update of one entire factor block is different from simultaneously changing both factors from stale values. Four candidate identities were compared against all 442 pinned AIO IDs, labels and scoped synonyms and 450 preceding native IDs, names and aliases, with no normalized match. Ignored/hidden full-checkout searches returned the same 106 matched-line set in each checkout after the prior merge. All matched excerpts from 76 files were read; they are discovery context, not existing concept records. The semantic search covered all pinned labels and scoped synonyms and returned 212 rows: 205 byte-equivalent prior readings and seven additional rows, all inspected. Twenty-three annotated AIO nodes with outgoing edges comprise 21 unchanged prior readings and two new inspections. Thirty contextual YAMLs, including seven native neighbors, comprise 25 unchanged prior readings and five complete new readings. This absence assessment is bounded to the pinned snapshot and inspected maintained corpus.

For squared error and well-defined positive denominators, update H elementwise as H &lt;- H*(W^T V)/(W^T W H) with W fixed. Update W analogously as W &lt;- W*(V H^T)/(W H H^T) with H fixed, evaluating each block rule against its current other factor. Multiplication and division of corresponding entries are elementwise. The proof uses a quadratic auxiliary function whose diagonal curvature majorizes W^T W, with current positive coordinates required in its displayed derivation. For generalized KL divergence, H_aμ is multiplied by [sum_i W_ia V_iμ/(WH)_iμ]/[sum_i W_ia], and W_ia by [sum_μ H_aμ V_iμ/(WH)_iμ]/[sum_μ H_aμ], with the other block fixed. Jensen majorization of the negative logarithm gives the source auxiliary function. With valid ratios and the stated domain, exact minimization of each auxiliary does not increase the corresponding objective. These are two objective-specific rules, not a universal multiplicative update for arbitrary losses. Monotone objective values do not alone prove convergence of factor matrices to a local minimum. In a curator scalar example V=1 and W=H=0.5, updating both factors simultaneously from their old values sets both to 2 and raises squared error from 0.5625 to 9. A separate fixed-W example W=[[1,0],[1,1]], V=[1,2]^T and H=[1.5,0]^T is unchanged by the H rule, although the zero coordinate has half-squared-error derivative -0.5 and increasing it lowers the loss. This is a zero-locked nonoptimal block state with positive denominators, not a claim about an inspected author implementation. Limitations: The rules require defined denominators and an explicit zero policy. The proof for positive current coordinates does not automatically cover arbitrary boundary initializations; multiplicative zeros may remain locked. Sequential block descent is not a license to update both blocks from stale factors. Arbitrary epsilon denominators, clipping, approximate updates or added penalties change the algorithm and require separate analysis. The objective is generally nonconvex jointly in W and H. Descent, bounded objective values and an auxiliary-function proof do not establish unique factors, a global optimum or the source discussion’s unrestricted local-optimum guarantee. Finite arithmetic verifies selected update and boundary claims; no author software, empirical model fitting or benchmark was executed.

### Definition, identity, claim support, limitations and AIO mapping direction

evidence: supported. Targets: AIMech:InfomaxICA.

Scoped to the standard logistic instantaneous algorithm of Bell and Sejnowski 1995. The unsquashed linear outputs estimate sources; the sigmoid outputs define its entropy contrast. This is distinct from the broader Infomax principle, Deep InfoMax’s learned dependence critics, later natural-gradient ICA, FastICA, and the paper’s separately developed temporal deconvolution and generalized-sigmoid variants. Four candidate identities were compared against all 442 pinned AIO IDs, labels and scoped synonyms and 450 preceding native IDs, names and aliases, with no normalized match. Ignored/hidden full-checkout searches returned the same 106 matched-line set in each checkout after the prior merge. All matched excerpts from 76 files were read; they are discovery context, not existing concept records. The semantic search covered all pinned labels and scoped synonyms and returned 212 rows: 205 byte-equivalent prior readings and seven additional rows, all inspected. Twenty-three annotated AIO nodes with outgoing edges comprise 21 unchanged prior readings and two new inspections. Thirty contextual YAMLs, including seven native neighbors, comprise 25 unchanged prior readings and five complete new readings. This absence assessment is bounded to the pinned snapshot and inspected maintained corpus.

Let u=Wx+b with square invertible W and y_i=1/(1+exp(-u_i)). The output differential entropy differs from H(X) by log&#124;det W&#124;+sum_i E[log(y_i(1-y_i))]. Its ordinary gradient updates are proportional to W^(-T)+(1-2y)x^T for W and 1-2y for b, averaged or sampled over observations. This is the ordinary parameter gradient, not a natural-gradient replacement. The inverse term is undefined at singular W, and finite steps need not preserve invertibility automatically. The curated objective is output differential entropy. For noiseless invertible transformations of continuous variables, mutual information between input and output is infinite, so the finite change-of-variables contrast is not a finite noiseless mutual-information value. A finite added output-noise model has a different noisy-output entropy unless the appropriate limiting approximation is justified. Maximizing the sigmoid-output entropy also trades off marginal entropy and dependence: a fixed nonlinearity mismatched to source distributions can prefer mixed outputs. The source illustrates this for uniform sources; arbitrary stationary points do not certify independent components. The instantaneous application assumes a linear mixture x=A s and seeks unsquashed outputs u that recover sources up to scale, sign and permutation under suitable distributional and identifiability conditions. The historical demonstrations mix recorded audio and discuss failures with multiple Gaussian white-noise sources and ill-conditioned mixing. The paper separately derives FIR blind deconvolution, which can whiten a nonwhite source instead of recovering the exact original. Neither arbitrary acoustic propagation delays nor unmodeled input noise is handled by the standard instantaneous rule. Limitations: Square nonsingular mixing, suitable source distributions and an appropriate contrast are substantive assumptions. The standard fixed logistic rule is not a universal source-separation or independence guarantee. The generalized sigmoid ODE in Equation 2.32 gives a chain-rule factor y^(p-1)(1-y)^(r-1) multiplying p(1-y)-r*y; Equations 2.33-2.34 omit it outside the standard p=r=1 case. Curator arithmetic verifies this discrepancy. Those generalized variants are excluded here; no uninspected author-code defect is asserted. Gradient ascent with a chosen finite learning rate need not converge globally or monotonically. The inverse-weight term is nonlocal; the source does not establish a biological learning mechanism. Audio demonstrations, annealing schedules and comparative timings are historical source-specific evidence. No author implementation, audio separation experiment or benchmark was run.

### Definition, identity, claim support, limitations and AIO mapping direction

evidence: supported. Targets: AIMech:TopographicICA.

Scoped to Hyvarinen, Hoyer and Inki’s 2001 generative construction and its approximate estimation. Topography describes higher-order statistical dependence of component amplitudes, not Euclidean proximity of prototypes, causal structure or arbitrary spatial data. This differs from ordinary mutually independent ICA, Kohonen maps and the undirected Product of Student-t analysis density. Overlapping neighborhoods distinguish it from disjoint independent subspaces; the source likelihood surrogate is not silently substituted for the exact directed model. Four candidate identities were compared against all 442 pinned AIO IDs, labels and scoped synonyms and 450 preceding native IDs, names and aliases, with no normalized match. Ignored/hidden full-checkout searches returned the same 106 matched-line set in each checkout after the prior merge. All matched excerpts from 76 files were read; they are discovery context, not existing concept records. The semantic search covered all pinned labels and scoped synonyms and returned 212 rows: 205 byte-equivalent prior readings and seven additional rows, all inspected. Twenty-three annotated AIO nodes with outgoing edges comprise 21 unchanged prior readings and two new inspections. Thirty contextual YAMLs, including seven native neighbors, comprise 25 unchanged prior readings and five complete new readings. This absence assessment is bounded to the pinned snapshot and inspected maintained corpus.

Generate independent higher-order variables u_k and independent zero-mean unit-variance z_i, all mutually independent. For a fixed nonnegative neighborhood h, set sigma_i=phi(sum_k h(i,k)u_k), s_i=sigma_i*z_i and x=A s with square invertible mixing A, proper latent distributions and finite positive scales. Distinct s_i are uncorrelated when the needed moments exist, but their squared-value covariance equals Cov(sigma_i^2,sigma_j^2). Disjoint scale neighborhoods imply independent components under the model. Shared neighborhoods can yield energy dependence; constant scales need not. Gaussian z gives Gaussian scale mixtures, with excess fourth cumulant 3 Var(sigma_i^2) when finite. Delta neighborhoods recover independent source components. The exact marginal integrates the latent scales. For Gaussian z and phi(v)=v^(-1/2), the paper replaces sqrt(sum_k h(i,k)u_k) by sqrt(h(i,i)u_i) in the integrand. With nonnegative u,h and positive diagonal h this produces a pointwise lower bound, factoring as exp(sum_k G(sum_i h(i,k)s_i^2)), where G is the one-dimensional log integral in Equation 3.9. This is generally an unnormalized surrogate rather than the original marginal. Normalizing the surrogate does not preserve its pointwise lower-bound property. The later smoothed-square-root and polynomial contrast choices are not automatically exact lower bounds for a specified latent prior. After centering and whitening, optionally in a PCA-reduced subspace, constrain the square separating matrix W to be orthogonal. Write a_i=w_i^T z, local energies e_k=sum_j h(k,j)a_j^2 and r_i=sum_k h(i,k)Gprime(e_k) for symmetric h. The source contrast gradient is proportional to E[z*a_i*r_i], with a common factor two absorbed into step size. Reorthogonalize using W &lt;- (W W^T)^(-1/2) W when full rank. On this orthogonal domain log&#124;det W&#124; is constant, explaining its omission. The rule differentiates the approximate contrast, not the generally intractable exact likelihood. The image experiment finds energy covariance that remains above zero at long distances, indicating mismatch to the model’s distant-independence ideal. Synthetic recovery with matched topology does not prove consistency for arbitrary contrasts; the quadratic/kurtosis contrast gives unsatisfactory image results. Proper scale mixtures need not have finite variance: with delta neighborhoods and squared-standard-Gaussian u, the inverse-square-root construction gives a Cauchy component. Thus moment and whitening arguments need conditions beyond a proper probability distribution. A positive quadratic G also defines an optimization contrast, not an integrable exp(G) source density over all real coordinates. Limitations: Neighborhoods and latent hyperparameters are specified by the model; the paper does not infer an arbitrary topology. Neighborhood overlap, sufficient moments and actual data fit govern statistical interpretations. A proper generative marginal, its lower-bound surrogate and heuristic contrasts are different objects. For fixed complete invertible transforms a surrogate normalizer can be independent of W without making the surrogate the original likelihood. Whitening and moment claims require finite moments and suitable covariance rank. Orthogonalization requires a full-rank intermediate matrix. PCA reduction retains a subspace; it does not reconstruct discarded dimensions. Finite-step projected gradient updates do not establish monotone ascent, unique estimates or global optimization. The finite calculations check local derivatives, mixture normalization and energy covariance, not statistical consistency. Natural-image features and a two-minute MEG artifact illustration provide bounded applications. Complex-cell and wiring interpretations are hypotheses, not causal biological validation; adjacency is not automatically meaningful for every recovered signal. No author implementation, image-model training, MEG processing or benchmark was executed.

### Mathematical representation versus a specific optimization algorithm

consistency: supported. Targets: AIMech:NonnegativeMatrixFactorization, AIMech:LeeSeungMultiplicativeUpdates.

Retain NMF and Lee-Seung updates as distinct concepts.

Nonnegative factors define additive reconstruction, not guaranteed sparsity or identifiable physical causes. The two multiplicative rules fit different objectives and are not the definition of NMF. Positive diagonal rescaling and factor permutation preserve the product. Generalized KL is not necessarily a distributional KL and observed zeros are not missing values.

### Block-update proofs, zero locking and convergence scope

consistency: supported. Targets: AIMech:LeeSeungMultiplicativeUpdates.

Preserve the exact update domain and limited guarantee.

The source auxiliary proof supports valid sequential blocks. A scalar simultaneous old-state update increases error from 0.5625 to 9. A separate fixed-W zero-locked block violates nonnegative first-order optimality despite positive denominators. These examples do not claim the complete joint algorithm was run or that an uninspected implementation has a defect. Objective descent is not proof of local/global factor convergence.

### Output differential entropy and ordinary gradient

consistency: supported. Targets: AIMech:InfomaxICA.

Retain standard logistic instantaneous Infomax with explicit information and distribution qualifications.

Finite differences verify the ordinary W inverse-transpose and logistic score gradient. Deterministic invertible continuous input/output mutual information is infinite; the finite contrast is output differential entropy, with a separate low-noise interpretation. The paper itself illustrates nonlinearity mismatch and failure of general independence claims. Deep InfoMax dependence critics, natural-gradient ICA, FastICA and FIR deconvolution are distinct scopes.

### Generalized-sigmoid derivative boundary

consistency: supported. Targets: AIMech:InfomaxICA.

Exclude unsupported transfer of the displayed generalized formula.

The standard p=r=1 logistic rule is valid. The ODE gprime=y^p(1-y)^r gives d log(gprime)/du=[p(1-y)-r*y]*y^(p-1)(1-y)^(r-1). Source Equations 2.33-2.34 omit the last factor in general. Curator arithmetic gives 0.0735 versus 0.5 for p=2,r=3,y=0.3. No code defect or universal generalized-sigmoid failure is asserted.

### Generative dependence, lower-bound normalization and moments

consistency: supported. Targets: AIMech:TopographicICA.

Retain the shared-scale model without replacing its likelihood by a heuristic contrast.

A finite discrete-scale analogue has uncorrelated components and positive energy covariance. Its pointwise lower-bound surrogate has total mass about 0.6055; renormalization can exceed the true density. The exact model, its approximation and later contrast choices remain distinct. A proper Cauchy specialization lacks finite variance, and a positive quadratic contrast is not a normalized source density. These are algebraic qualifications, not claims about all historical fitted parameters.

### Whitened orthogonal estimation and neighborhood scope

consistency: supported. Targets: AIMech:TopographicICA.

Keep the source constrained-gradient approximation explicit.

The finite contrast derivative matches the source modulation rule, including the absorbed common factor two. Log determinant is constant only on the stated orthogonal domain. Whitening and reorthogonalization need moment/rank conditions; finite steps do not guarantee ascent or global optimization. Fixed neighborhoods and component-energy relationships differ from prototype geometry, spatial causes and unique anatomical localization.

### Primary versions, contextual comparisons and mapping abstraction

grounding: supported. Targets: AIMech:NonnegativeMatrixFactorization, AIMech:LeeSeungMultiplicativeUpdates, AIMech:InfomaxICA, AIMech:TopographicICA.

Preserve local concept boundaries and bounded historical evidence.

NMF maps related to task-scoped DimensionalityReduction, preserving the mathematical-method/task distinction and allowing factor sizes that do not reduce dimension. Lee-Seung fitting and Infomax ICA map related to UnsupervisedLearning, reflecting their defining unlabeled parameter estimation without an is-a assertion. Topographic ICA maps broadly to Model and related to UnsupervisedLearning. TrainingStrategy has a preprocessing genus; RepresentationLearning and SparseLearning are network-scoped, while nonnegative factors need not be sparse. PCA orthogonality and Kohonen prototype topology are not equivalent identities. Deep InfoMax, ordinary SGD, EM, GCA, PoE, PoT and fixed-prior IWF contextualize distinct contrasts, model laws and optimization roles; contextual records receive no renewed scientific approval. All 70 primary pages were visually read. NMF is not a new benchmark paper; audio, image and MEG examples do not establish general superiority or a biological mechanism. No author implementation, empirical fitting or benchmark ran.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:NonnegativeMatrixFactorization, AIMech:LeeSeungMultiplicativeUpdates, AIMech:InfomaxICA, AIMech:TopographicICA. The factorization problem, objective-specific block optimizer, ordinary-gradient source-separation algorithm and topographic shared-scale probability model denote different supported concepts. Related task mappings preserve abstraction; the specific model maps broadly to Model. Similar basis representations or names do not justify lumping.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T015038Z-factorization-and-topographic-components.json | supports | Four candidate identities were compared against all 442 pinned AIO IDs, labels and scoped synonyms and 450 preceding native IDs, names and aliases, with no normalized match. Ignored/hidden full-checkout searches returned the same 106 matched-line set in each checkout after the prior merge. All matched excerpts from 76 files were read; they are discovery context, not existing concept records. The semantic search covered all pinned labels and scoped synonyms and returned 212 rows: 205 byte-equivalent prior readings and seven additional rows, all inspected. Twenty-three annotated AIO nodes with outgoing edges comprise 21 unchanged prior readings and two new inspections. Thirty contextual YAMLs, including seven native neighbors, comprise 25 unchanged prior readings and five complete new readings. This absence assessment is bounded to the pinned snapshot and inspected maintained corpus. |
| mapping | sources/aio/aio.json; 23 annotated CLASS nodes and outgoing edges; all 212 semantic label/synonym rows | supports | NMF maps related to task-scoped DimensionalityReduction, preserving the mathematical-method/task distinction and allowing factor sizes that do not reduce dimension. Lee-Seung fitting and Infomax ICA map related to UnsupervisedLearning, reflecting their defining unlabeled parameter estimation without an is-a assertion. Topographic ICA maps broadly to Model and related to UnsupervisedLearning. TrainingStrategy has a preprocessing genus; RepresentationLearning and SparseLearning are network-scoped, while nonnegative factors need not be sparse. PCA orthogonality and Kohonen prototype topology are not equivalent identities. Deep InfoMax, ordinary SGD, EM, GCA, PoE, PoT and fixed-prior IWF contextualize distinct contrasts, model laws and optimization roles; contextual records receive no renewed scientific approval. |
| neighbors | research/discovery/20261012T015038Z-factorization-and-topographic-components.json; Seven native neighbors and 23 generated contextual YAMLs in source_analysis.context_reading | supports | Thirty contextual YAMLs comprise 25 unchanged prior readings and five fully read current records. General PoE, PoT, GCA, Deep InfoMax, EM, SGD and IWF distinguish model laws, learning contrasts and fixed-model inference. Contextual records receive no renewed scientific approval. |
| finite-boundaries | research/discovery/factorization-and-topographic-components.py; Sequential versus simultaneous NMF updates, zero-locking; Infomax gradients; topographic mixture normalization, moments and contrast gradient | supports | Finite arithmetic shows descent for the two NMF block objectives, a simultaneous-update increase from 0.5625 to 9 and a zero-locked nonoptimal H block with derivative -0.5. Infomax ordinary gradients agree with finite differences within 3e-10, while generalized-sigmoid chain-rule and printed scores differ (0.0735 versus 0.5). A two-scale topographic-mixture analogue has a lower-bound surrogate of total mass about 0.6055; normalization can make it exceed the exact density. Its component covariance is zero while energy covariance is positive. The topographic contrast gradient agrees within 2.4e-10. Diverging Cauchy truncated second moments illustrate why properness does not ensure finite variance. These are curator checks, not historical software or empirical reproduction. |
| nonnegativematrixfactorization-source-0 | https://proceedings.neurips.cc/paper_files/paper/2000/file/f9d1152547c0bde01830b7e8bd60024c-Paper.pdf; Section 3, Equations 2-3, PDF p. 2; curator boundary conventions of the displayed divergence; Sections 1-2, Equation 1, PDF pp. 1-2; Sections 1-3, Equations 1-3, PDF pp. 1-2; Sections 1-3, PDF pp. 1-2; curator invariances of Equation 1 | supports | Algorithms for Non-negative Matrix Factorization. Official seven-page NIPS 2000 paper in Advances in Neural Information Processing Systems 13. All pages visually read, including both auxiliary-function proofs; locators use PDF pages. The conference year is 2000, although later references may cite the proceedings as 2001. Curator algebraic deductions are marked separately from historical empirical results or uninspected software. |
| leeseungmultiplicativeupdates-source-0 | https://proceedings.neurips.cc/paper_files/paper/2000/file/f9d1152547c0bde01830b7e8bd60024c-Paper.pdf; Section 4, Equation 4, PDF p. 3; Section 6, Lemma 2 and Equations 12-19, PDF pp. 4-5; Section 4, Equation 5, PDF p. 3; Section 6, Lemma 3 and Equations 20-33, PDF pp. 5-6; Sections 4 and 6-7, PDF pp. 3-7; curator finite counterexamples to unrestricted update and local-optimum interpretations; Sections 4-6, Equations 4-5 and auxiliary-function proofs, PDF pp. 3-6 | supports | Algorithms for Non-negative Matrix Factorization. Official seven-page NIPS 2000 paper in Advances in Neural Information Processing Systems 13. All pages visually read, including both auxiliary-function proofs; locators use PDF pages. The conference year is 2000, although later references may cite the proceedings as 2001. Curator algebraic deductions are marked separately from historical empirical results or uninspected software. |
| infomaxica-source-0 | https://papers.cnl.salk.edu/PDFs/An%20Information-Maximization%20Approach%20to%20Blind%20Separation%20and%20Blind%20Deconvolution%201995-3631.pdf; Section 2.1, printed p. 1131 / PDF p. 3; Section 4 and Figure 4, pp. 1141-1143 / PDF pp. 13-15; curator continuous-information qualification; Sections 2.1-2.2, Equations 2.1-2.16, printed pp. 1131-1134 / PDF pp. 3-6; Appendix A.1-A.8, pp. 1154-1155 / PDF pp. 26-27; Sections 2.1-2.2, Equations 2.2-2.16, printed pp. 1131-1134 / PDF pp. 3-6; Appendix A.1-A.8, pp. 1154-1155 / PDF pp. 26-27; Sections 3-5.3, printed pp. 1138-1149 / PDF pp. 10-21; Section 6.4, pp. 1153-1154 / PDF pp. 25-26 | supports | An Information-Maximization Approach to Blind Separation and Blind Deconvolution. Salk-hosted final Neural Computation 7(6):1129-1159 (1995) scan, 31 PDF pages, all visually read. Printed page equals PDF page plus 1128. This is not the earlier institutional technical report. Curator algebraic deductions are marked separately from historical empirical results or uninspected software. |
| topographicica-source-0 | https://redwood.berkeley.edu/wp-content/uploads/2020/08/hyvarinen-hoyer01.pdf; Section 2, Equations 2.1-2.10 and Figure 2, printed pp. 1529-1534 / PDF pp. 3-8; Section 2.3-2.4, Equations 2.5-2.10, printed pp. 1532-1534 / PDF pp. 6-8; curator moment and degeneracy qualifications; Section 3, Equations 3.1-3.14, printed pp. 1534-1537 / PDF pp. 8-11; curator normalization consequences; Section 4, Equations 4.1-4.5, printed pp. 1538-1539 / PDF pp. 12-13; Appendix A.1-A.5, pp. 1554-1555 / PDF pp. 28-29; Sections 3 and 6.1-6.2, printed pp. 1537 and 1543-1548 / PDF pp. 11 and 17-22; curator tail and moment deductions | supports | Topographic Independent Component Analysis. Institution-hosted final Neural Computation 13:1527-1558 (2001) PDF, 32 pages, all visually read. Printed page equals PDF page plus 1526. Acceptance and PDF producer dates do not replace the publication year. Curator algebraic deductions are marked separately from historical empirical results or uninspected software. |

## Limits And Additional Notes

- Adversarial author self-review only; all four records remain DRAFT.
- The initial vendored network lookup failed inside the sandbox; the authorized network retry passed.
- All 70 pages of three primary PDFs were visually read, including the NMF proofs, the scanned Infomax appendix and topographic ICA experiments and appendix. NMF uses PDF-page locators; printed Infomax page=PDF page+1128 and topographic ICA page=PDF page+1526.
- Exact source URLs, versions, UTC access times and downloaded-byte SHA-256 values are retained. Search/open times are captured immediately before the actual requests; output captures are discovery provenance, not a claim to have read every returned link.
- NMF and Lee-Seung fitting are distinct concepts. Descent requires valid sequential block updates; zero-locking and factor indeterminacy preclude blanket local-optimum or unique-parts claims.
- The standard logistic Infomax gradient is retained. No finite noiseless continuous mutual-information value, arbitrary-source independence guarantee or silently corrected generalized-sigmoid implementation is asserted.
- Topographic ICA preserves the directed latent-scale model, unnormalized lower-bound surrogate and heuristic contrast distinctions. Moment existence, whitening rank and neighborhood overlap are substantive conditions.
- Historical image, audio and MEG demonstrations do not establish universal gains or biological mechanisms. No author implementation, training or empirical benchmark was executed.
- Fifteen new provisional cohorts leave 349 pending leads, plus partially addressed and deferred entries. Four new records remain DRAFT; no global saturation is claimed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T015357Z-factorization-and-topographic-components
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of nonnegative factorization and independent-component
  methods
started_at: '2026-10-12T01:50:57Z'
finished_at: '2026-10-12T01:53:57Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially read all fields of four final
    maintained records against 70 complete primary PDF pages, 23 annotated AIO nodes
    and seven native neighbors. Finite arithmetic verifies selected gradients and
    demonstrates descent, boundary and normalization limits. This is author self-review,
    not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain NMF, Lee-Seung multiplicative updates, standard logistic Infomax ICA
  and topographic ICA with distinct representation, optimization and model scopes.
  Explicitly preserve zero-locking, differential-entropy, distribution mismatch, likelihood-surrogate
  and moment boundaries. No actionable curation finding remains in the four additions.
source:
  git_revision: a7523fc2877d2d46b5e5050d40b3cc50e611867e
  state: working_tree
  inputs:
  - path: data/aio/ArtificialNeuralNetwork.yaml
    sha256: 718528c2d43f98b200c7656e9844890e9b445bbff53d3286cb22af39f34c69ce
    role: context
  - path: data/aio/DeepFeedForwardNetwork.yaml
    sha256: d66c246318687598cf762fae4b54586a312b70d143735aba5c12b2606c45c8c9
    role: context
  - path: data/aio/DimensionalityReduction.yaml
    sha256: 99eb0714b362a98a9e704e5ef2ac370cb7a900fbe97da43de790c3ec67ed812e
    role: context
  - path: data/aio/EnergyBasedLLM.yaml
    sha256: e9e29aa4f8400ad463dfe058fade876ef36c4a2637e1ebc4b42688116896310b
    role: context
  - path: data/aio/FactorizedLLM.yaml
    sha256: f73a5e4d591e4d832f94bfa044d77c5645f585b042f07485f99920527d67b6d5
    role: context
  - path: data/aio/FeatureExtraction.yaml
    sha256: d153b8bbe04e9abb7f1ec13e6219dbcd329235ac58bb9229d4a1f416216c07ef
    role: context
  - path: data/aio/ImplicitLanguageModel.yaml
    sha256: 818c396b19757360dcdff6291a85d589c50638e0dc6d6bfcd96fdcb7bdf46ce9
    role: context
  - path: data/aio/KohonenNetwork.yaml
    sha256: 88932d6b90c0faf268d66f33a580130ec1bcc637650bd05b03c0e24e6714067b
    role: context
  - path: data/aio/LinearRegression.yaml
    sha256: 9b6f1b2ea06d9a47e5f7cf94c66afeaa6d40c3e7d0fdb5037d2c25fabc6d8167
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/ManifoldLearning.yaml
    sha256: eb8e1a854af3e8f920c76d1ea4618406edd1693b4e5d99511ab057a2bf56ddea
    role: context
  - path: data/aio/Model.yaml
    sha256: 56b85d1c6d559d9ce4172dcf9c776126e91a03649c8f4d1fa8e3f5130f0ca73b
    role: context
  - path: data/aio/Normalization.yaml
    sha256: ecdbd41476b6125c670855f1f00090047acd61f5ee16d71384f6b9ed86bea2bb
    role: context
  - path: data/aio/Preprocessing.yaml
    sha256: 2c4a30f4f829a757be1feabf78d15780eedf93681a62eede3e76b2304f21bb7a
    role: context
  - path: data/aio/PrincipalComponentAnalysis.yaml
    sha256: 7b45b5c558b7e984abb44e1610fb8d829409ae391a151ed0dc0e5cd95023e8d4
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/RegressionAnalysis.yaml
    sha256: 6f5d48096556a2ec31770aab306219e9020919940b4e80554639cc97aaa94bc6
    role: context
  - path: data/aio/RepresentationLearning.yaml
    sha256: bc7af756440437f60210019e17ad1e2dd15cd1c7cbfbc96312520934b7a5c7ca
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
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/curated/DeepInfoMax.yaml
    sha256: ebda53a216420e7455b5435a380e383d78569acf9b3e0031ae036f8c25b23fb1
    role: context
  - path: data/curated/ExpectationMaximization.yaml
    sha256: eab2880f9e6db51aa49135ada0c3f6d1504e947e6f920d0a5913fd7ddbd069c4
    role: context
  - path: data/curated/GeneralizedComponentAnalysis.yaml
    sha256: 79ab7923284423c0f542c77deff5f0ce3de898c795d16e930340380b9046a8ff
    role: context
  - path: data/curated/InfomaxICA.yaml
    sha256: 9cd4b9da2ef26e210f67fd0daf2f567a32cea4ff26433210008e513711a07a36
    role: target
  - path: data/curated/IteratedWienerFilter.yaml
    sha256: 803905a00467ecfc963cbd5a24f5616013484c0d0ce57d205c386868346addac
    role: context
  - path: data/curated/LeeSeungMultiplicativeUpdates.yaml
    sha256: c94eb2299a6f71dea98ac6e47548358f1eea4905aa2708b5efa12f2874b15fb1
    role: target
  - path: data/curated/NonnegativeMatrixFactorization.yaml
    sha256: 3b79c0f7568f3cdc86f5779be7e9c3e2341c547682223e214a6b94031016df7b
    role: target
  - path: data/curated/ProductOfExperts.yaml
    sha256: f08d34564c86a3531094451fb045ee5d1bd20b89d3111bb68d0c19de0cf373a8
    role: context
  - path: data/curated/ProductOfStudentT.yaml
    sha256: 980d2e40631704548ae01a61510d29dffc1a97c66c9cd770c366cdfcfd945602
    role: context
  - path: data/curated/StochasticGradientDescent.yaml
    sha256: 5c57fc809ae8667d5be8cda421cc9f0bd1f0c668f64ba3d7b23d788528b46e97
    role: context
  - path: data/curated/TopographicICA.yaml
    sha256: 2ade4a230d625874ff765bbb1d44f81fe5e27b4c08f9a9f687b1163b678dc9f1
    role: target
  - path: research/discovery/20261012T015038Z-factorization-and-topographic-components.json
    sha256: 4f96dbf9c3a1eb7578d56447e3a77a31d612715e50a7a89be6defc4284186d4d
    role: context
  - path: research/discovery/factorization-and-topographic-components.py
    sha256: dbd5dfebd275e02dc7c156ec314cf1810c717ba3f769bc7ad7c2fd0058ecc211
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
- target_id: AIMech:NonnegativeMatrixFactorization
  path: data/curated/NonnegativeMatrixFactorization.yaml
  label: Nonnegative Matrix Factorization
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NonnegativeMatrixFactorization.yaml
    role: maintained
- target_id: AIMech:LeeSeungMultiplicativeUpdates
  path: data/curated/LeeSeungMultiplicativeUpdates.yaml
  label: Lee-Seung Multiplicative Updates
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LeeSeungMultiplicativeUpdates.yaml
    role: maintained
- target_id: AIMech:InfomaxICA
  path: data/curated/InfomaxICA.yaml
  label: Infomax Independent Component Analysis
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/InfomaxICA.yaml
    role: maintained
- target_id: AIMech:TopographicICA
  path: data/curated/TopographicICA.yaml
  label: Topographic Independent Component Analysis
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TopographicICA.yaml
    role: maintained
scope:
  description: All fields of four source-defined factorization and latent-component
    concepts.
  selection: Exact maintained IDs NonnegativeMatrixFactorization, LeeSeungMultiplicativeUpdates,
    InfomaxICA and TopographicICA; full selected cohort without sampling.
  coverage: full
  population_size: 4
  reviewed_target_ids:
  - AIMech:NonnegativeMatrixFactorization
  - AIMech:LeeSeungMultiplicativeUpdates
  - AIMech:InfomaxICA
  - AIMech:TopographicICA
  exclusions:
  - target: Contextual AIO and maintained records
    reason: Context informs identity and abstraction boundaries without renewed scientific
      approval or mutation.
  - target: Historical implementations and empirical reproduction
    reason: No source software, audio processing, image training, MEG analysis or
      benchmark ran. Curator arithmetic checks bounded mathematical claims only.
  - target: Remaining discovery frontier
    reason: Fifteen new provisional cohorts and 349 pending leads remain, alongside
      other unresolved dispositions. Kernel PCA remains open in its partially addressed
      cohort.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:NonnegativeMatrixFactorization
  - AIMech:LeeSeungMultiplicativeUpdates
  - AIMech:InfomaxICA
  - AIMech:TopographicICA
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 86.07s (0:01:26)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 454 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 132 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 129,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:NonnegativeMatrixFactorization
  - AIMech:LeeSeungMultiplicativeUpdates
  - AIMech:InfomaxICA
  - AIMech:TopographicICA
  exit_code: 0
  expected_exit_code: 0
  summary: "OK: 22 governed artifacts match the pinned claw revision\nbash scripts/check_vendored_sync.sh\n\
    \ Initial sandbox execution failed to resolve raw.githubusercontent.com (exit\
    \ 1); the read-only check was rerun with network access and passed. No governed\
    \ bytes changed."
- check_id: required-2
  name: uv run --locked aimech check-source
  command: uv run --locked aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:NonnegativeMatrixFactorization
  - AIMech:LeeSeungMultiplicativeUpdates
  - AIMech:InfomaxICA
  - AIMech:TopographicICA
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
  - AIMech:NonnegativeMatrixFactorization
  - AIMech:LeeSeungMultiplicativeUpdates
  - AIMech:InfomaxICA
  - AIMech:TopographicICA
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited 0 with no output.
- check_id: finite-arithmetic
  name: Factorization and topographic-component boundaries
  command: python3 research/discovery/factorization-and-topographic-components.py
  status: passed
  required: true
  target_ids:
  - AIMech:NonnegativeMatrixFactorization
  - AIMech:LeeSeungMultiplicativeUpdates
  - AIMech:InfomaxICA
  - AIMech:TopographicICA
  exit_code: 0
  expected_exit_code: 0
  summary: '{"nmf_block_objectives": {"squared_error": [20.345, 4.643645222757498,
    0.5121403961160389], "generalized_kl": [9.004858394930977, 1.9726972204360944,
    0.5333623412979441]}, "nmf_simultaneous_scalar_errors": [0.5625, 9], "zero_locked_half_squared_gradient":
    [[0.0], [-0.5]], "infomax_gradient_max_error": 2.905420903864808e-10, "generalized_sigmoid_scores":
    [0.0735, 0.5], "tica_lower_bound_mass": 0.6054988603092419, "normalized_surrogate_max_ratio":
    1.10089843785717, "tica_energy_covariance": 0.03452932098765432, "tica_gradient_max_error":
    2.3984542130151e-10, "cauchy_truncated_second_moments": [5.4296487585369215, 62.66834322228795,
    635.6204089871416]}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T015038Z-factorization-and-topographic-components.json
  accessed_at: '2026-10-12T01:50:57Z'
  support: supports
  summary: 'Four candidate identities were compared against all 442 pinned AIO IDs,
    labels and scoped synonyms and 450 preceding native IDs, names and aliases, with
    no normalized match. Ignored/hidden full-checkout searches returned the same 106
    matched-line set in each checkout after the prior merge. All matched excerpts
    from 76 files were read; they are discovery context, not existing concept records.
    The semantic search covered all pinned labels and scoped synonyms and returned
    212 rows: 205 byte-equivalent prior readings and seven additional rows, all inspected.
    Twenty-three annotated AIO nodes with outgoing edges comprise 21 unchanged prior
    readings and two new inspections. Thirty contextual YAMLs, including seven native
    neighbors, comprise 25 unchanged prior readings and five complete new readings.
    This absence assessment is bounded to the pinned snapshot and inspected maintained
    corpus.'
  search_scope: All labels, all scoped synonyms, aliases and IDs normalized for record
    identity; full-text searches of both checkouts include ignored/hidden files. Acronyms
    were checked in the normalized identity comparison; short acronyms were omitted
    from broad substring searches to avoid irrelevant matches.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: 23 annotated CLASS nodes and outgoing edges; all 212 semantic label/synonym
    rows
  accessed_at: '2026-10-12T01:50:57Z'
  support: supports
  summary: NMF maps related to task-scoped DimensionalityReduction, preserving the
    mathematical-method/task distinction and allowing factor sizes that do not reduce
    dimension. Lee-Seung fitting and Infomax ICA map related to UnsupervisedLearning,
    reflecting their defining unlabeled parameter estimation without an is-a assertion.
    Topographic ICA maps broadly to Model and related to UnsupervisedLearning. TrainingStrategy
    has a preprocessing genus; RepresentationLearning and SparseLearning are network-scoped,
    while nonnegative factors need not be sparse. PCA orthogonality and Kohonen prototype
    topology are not equivalent identities. Deep InfoMax, ordinary SGD, EM, GCA, PoE,
    PoT and fixed-prior IWF contextualize distinct contrasts, model laws and optimization
    roles; contextual records receive no renewed scientific approval.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261012T015038Z-factorization-and-topographic-components.json
  locator: Seven native neighbors and 23 generated contextual YAMLs in source_analysis.context_reading
  accessed_at: '2026-10-12T01:50:57Z'
  support: supports
  summary: Thirty contextual YAMLs comprise 25 unchanged prior readings and five fully
    read current records. General PoE, PoT, GCA, Deep InfoMax, EM, SGD and IWF distinguish
    model laws, learning contrasts and fixed-model inference. Contextual records receive
    no renewed scientific approval.
- evidence_id: finite-boundaries
  kind: record_content
  reference: research/discovery/factorization-and-topographic-components.py
  locator: Sequential versus simultaneous NMF updates, zero-locking; Infomax gradients;
    topographic mixture normalization, moments and contrast gradient
  accessed_at: '2026-10-12T01:50:57Z'
  snapshot_sha256: dbd5dfebd275e02dc7c156ec314cf1810c717ba3f769bc7ad7c2fd0058ecc211
  support: supports
  summary: Finite arithmetic shows descent for the two NMF block objectives, a simultaneous-update
    increase from 0.5625 to 9 and a zero-locked nonoptimal H block with derivative
    -0.5. Infomax ordinary gradients agree with finite differences within 3e-10, while
    generalized-sigmoid chain-rule and printed scores differ (0.0735 versus 0.5).
    A two-scale topographic-mixture analogue has a lower-bound surrogate of total
    mass about 0.6055; normalization can make it exceed the exact density. Its component
    covariance is zero while energy covariance is positive. The topographic contrast
    gradient agrees within 2.4e-10. Diverging Cauchy truncated second moments illustrate
    why properness does not ensure finite variance. These are curator checks, not
    historical software or empirical reproduction.
- evidence_id: nonnegativematrixfactorization-source-0
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper_files/paper/2000/file/f9d1152547c0bde01830b7e8bd60024c-Paper.pdf
  locator: Section 3, Equations 2-3, PDF p. 2; curator boundary conventions of the
    displayed divergence; Sections 1-2, Equation 1, PDF pp. 1-2; Sections 1-3, Equations
    1-3, PDF pp. 1-2; Sections 1-3, PDF pp. 1-2; curator invariances of Equation 1
  accessed_at: '2026-10-12T01:33:53Z'
  snapshot_sha256: d943865213cbb4c678d783ab20944147d9eaef1756513e9f9388e26471f31305
  support: supports
  summary: Algorithms for Non-negative Matrix Factorization. Official seven-page NIPS
    2000 paper in Advances in Neural Information Processing Systems 13. All pages
    visually read, including both auxiliary-function proofs; locators use PDF pages.
    The conference year is 2000, although later references may cite the proceedings
    as 2001. Curator algebraic deductions are marked separately from historical empirical
    results or uninspected software.
- evidence_id: leeseungmultiplicativeupdates-source-0
  kind: primary_source
  reference: https://proceedings.neurips.cc/paper_files/paper/2000/file/f9d1152547c0bde01830b7e8bd60024c-Paper.pdf
  locator: Section 4, Equation 4, PDF p. 3; Section 6, Lemma 2 and Equations 12-19,
    PDF pp. 4-5; Section 4, Equation 5, PDF p. 3; Section 6, Lemma 3 and Equations
    20-33, PDF pp. 5-6; Sections 4 and 6-7, PDF pp. 3-7; curator finite counterexamples
    to unrestricted update and local-optimum interpretations; Sections 4-6, Equations
    4-5 and auxiliary-function proofs, PDF pp. 3-6
  accessed_at: '2026-10-12T01:33:53Z'
  snapshot_sha256: d943865213cbb4c678d783ab20944147d9eaef1756513e9f9388e26471f31305
  support: supports
  summary: Algorithms for Non-negative Matrix Factorization. Official seven-page NIPS
    2000 paper in Advances in Neural Information Processing Systems 13. All pages
    visually read, including both auxiliary-function proofs; locators use PDF pages.
    The conference year is 2000, although later references may cite the proceedings
    as 2001. Curator algebraic deductions are marked separately from historical empirical
    results or uninspected software.
- evidence_id: infomaxica-source-0
  kind: primary_source
  reference: https://papers.cnl.salk.edu/PDFs/An%20Information-Maximization%20Approach%20to%20Blind%20Separation%20and%20Blind%20Deconvolution%201995-3631.pdf
  locator: Section 2.1, printed p. 1131 / PDF p. 3; Section 4 and Figure 4, pp. 1141-1143
    / PDF pp. 13-15; curator continuous-information qualification; Sections 2.1-2.2,
    Equations 2.1-2.16, printed pp. 1131-1134 / PDF pp. 3-6; Appendix A.1-A.8, pp.
    1154-1155 / PDF pp. 26-27; Sections 2.1-2.2, Equations 2.2-2.16, printed pp. 1131-1134
    / PDF pp. 3-6; Appendix A.1-A.8, pp. 1154-1155 / PDF pp. 26-27; Sections 3-5.3,
    printed pp. 1138-1149 / PDF pp. 10-21; Section 6.4, pp. 1153-1154 / PDF pp. 25-26
  accessed_at: '2026-10-12T01:33:57Z'
  snapshot_sha256: abcb3468dc3c1c0cdf08b2fd508371f5b2a73acd1101ba603a3a2205a94bcc9b
  support: supports
  summary: An Information-Maximization Approach to Blind Separation and Blind Deconvolution.
    Salk-hosted final Neural Computation 7(6):1129-1159 (1995) scan, 31 PDF pages,
    all visually read. Printed page equals PDF page plus 1128. This is not the earlier
    institutional technical report. Curator algebraic deductions are marked separately
    from historical empirical results or uninspected software.
- evidence_id: topographicica-source-0
  kind: primary_source
  reference: https://redwood.berkeley.edu/wp-content/uploads/2020/08/hyvarinen-hoyer01.pdf
  locator: Section 2, Equations 2.1-2.10 and Figure 2, printed pp. 1529-1534 / PDF
    pp. 3-8; Section 2.3-2.4, Equations 2.5-2.10, printed pp. 1532-1534 / PDF pp.
    6-8; curator moment and degeneracy qualifications; Section 3, Equations 3.1-3.14,
    printed pp. 1534-1537 / PDF pp. 8-11; curator normalization consequences; Section
    4, Equations 4.1-4.5, printed pp. 1538-1539 / PDF pp. 12-13; Appendix A.1-A.5,
    pp. 1554-1555 / PDF pp. 28-29; Sections 3 and 6.1-6.2, printed pp. 1537 and 1543-1548
    / PDF pp. 11 and 17-22; curator tail and moment deductions
  accessed_at: '2026-10-12T01:34:07Z'
  snapshot_sha256: 662379f40bc4104c6bdb2ca04027a385c5c22efbd5aaa8f661848bf4eb1dfe85
  support: supports
  summary: Topographic Independent Component Analysis. Institution-hosted final Neural
    Computation 13:1527-1558 (2001) PDF, 32 pages, all visually read. Printed page
    equals PDF page plus 1526. Acceptance and PDF producer dates do not replace the
    publication year. Curator algebraic deductions are marked separately from historical
    empirical results or uninspected software.
assessments:
- assessment_id: nonnegativematrixfactorization
  area: evidence
  topic: Definition, identity, claim support, limitations and AIO mapping direction
  outcome: supported
  target_ids:
  - AIMech:NonnegativeMatrixFactorization
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - nonnegativematrixfactorization-source-0
  summary: 'The mathematical factorization is distinct from a particular fitting algorithm,
    trained dictionary or application. The separately represented Lee-Seung multiplicative
    updates optimize two specified objectives. Nonnegative factors need not be sparse,
    orthogonal or uniquely determined; this is not the exact sparse-coding identity
    in AIO or ordinary PCA. Non-negative and British factorisation spellings name
    the same method. Four candidate identities were compared against all 442 pinned
    AIO IDs, labels and scoped synonyms and 450 preceding native IDs, names and aliases,
    with no normalized match. Ignored/hidden full-checkout searches returned the same
    106 matched-line set in each checkout after the prior merge. All matched excerpts
    from 76 files were read; they are discovery context, not existing concept records.
    The semantic search covered all pinned labels and scoped synonyms and returned
    212 rows: 205 byte-equivalent prior readings and seven additional rows, all inspected.
    Twenty-three annotated AIO nodes with outgoing edges comprise 21 unchanged prior
    readings and two new inspections. Thirty contextual YAMLs, including seven native
    neighbors, comprise 25 unchanged prior readings and five complete new readings.
    This absence assessment is bounded to the pinned snapshot and inspected maintained
    corpus.'
  details: 'For V in the nonnegative n-by-m matrices, seek W of size n-by-r and H
    of size r-by-m with nonnegative entries and V approximately W H. Columns of W
    supply basis elements and columns of H their nonnegative coefficients. Choosing
    r below the data dimensions yields a compressed representation with product rank
    at most r, but small r is a modeling choice rather than a consequence of nonnegativity.
    Factors can be dense. The inspected source fits either squared Frobenius error
    ||V-WH||_F^2 or generalized KL divergence sum_ij[V_ij log(V_ij/(WH)_ij)-V_ij+(WH)_ij].
    The latter is a divergence between nonnegative arrays, not necessarily normalized
    probability distributions and not a symmetric distance. By continuity a zero V
    entry contributes the corresponding reconstruction, while a positive V entry with
    zero reconstruction gives infinite divergence. An observed zero contributes to
    these objectives; it is not automatically a missing value. Nonnegativity supports
    additive representations but does not guarantee recovery of unique physical parts
    or causes. For any positive diagonal D, W D and D^(-1) H give the same reconstruction,
    and a common factor permutation also preserves it. The nonconvex joint fitting
    problem and chosen objective further affect the result. These algebraic ambiguities
    remain even when a factorization has small reconstruction error. Limitations:
    No universal sparsity, uniqueness, causal interpretation or global optimization
    guarantee follows from the nonnegative constraint. Additional constraints or probabilistic
    models define narrower methods. The two inspected objectives are representative
    source formulations, not an exhaustive definition of every NMF loss or algorithm.
    Missing-data masks, regularization, sparse constraints and probabilistic count
    models require their own specification. The inspected paper is an algorithm and
    proof contribution; no new benchmark ranking, author implementation, empirical
    fitting or parts-recognition result was reproduced.'
  dimensions:
  - name: concept-kind
    value: mathematical_method
    definition: A mathematical method, specific learning algorithm or latent-variable
      model family; not a trained instance.
    evidence_ids:
    - nonnegativematrixfactorization-source-0
  - name: aio-assessment
    value: related_match
    definition: NMF maps related to task-scoped DimensionalityReduction, preserving
      the mathematical-method/task distinction and allowing factor sizes that do not
      reduce dimension. Lee-Seung fitting and Infomax ICA map related to UnsupervisedLearning,
      reflecting their defining unlabeled parameter estimation without an is-a assertion.
      Topographic ICA maps broadly to Model and related to UnsupervisedLearning. TrainingStrategy
      has a preprocessing genus; RepresentationLearning and SparseLearning are network-scoped,
      while nonnegative factors need not be sparse. PCA orthogonality and Kohonen
      prototype topology are not equivalent identities. Deep InfoMax, ordinary SGD,
      EM, GCA, PoE, PoT and fixed-prior IWF contextualize distinct contrasts, model
      laws and optimization roles; contextual records receive no renewed scientific
      approval.
    evidence_ids:
    - mapping
- assessment_id: leeseungmultiplicativeupdates
  area: evidence
  topic: Definition, identity, claim support, limitations and AIO mapping direction
  outcome: supported
  target_ids:
  - AIMech:LeeSeungMultiplicativeUpdates
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - leeseungmultiplicativeupdates-source-0
  summary: 'Scoped to Equations 4-5 and their auxiliary-function derivations in Lee
    and Seung, NIPS 2000. This is a particular family of fitting rules, distinct from
    the general NMF factorization, every multiplicative optimizer, generic EM and
    the fixed-prior Iterated Wiener Filter. An update of one entire factor block is
    different from simultaneously changing both factors from stale values. Four candidate
    identities were compared against all 442 pinned AIO IDs, labels and scoped synonyms
    and 450 preceding native IDs, names and aliases, with no normalized match. Ignored/hidden
    full-checkout searches returned the same 106 matched-line set in each checkout
    after the prior merge. All matched excerpts from 76 files were read; they are
    discovery context, not existing concept records. The semantic search covered all
    pinned labels and scoped synonyms and returned 212 rows: 205 byte-equivalent prior
    readings and seven additional rows, all inspected. Twenty-three annotated AIO
    nodes with outgoing edges comprise 21 unchanged prior readings and two new inspections.
    Thirty contextual YAMLs, including seven native neighbors, comprise 25 unchanged
    prior readings and five complete new readings. This absence assessment is bounded
    to the pinned snapshot and inspected maintained corpus.'
  details: 'For squared error and well-defined positive denominators, update H elementwise
    as H <- H*(W^T V)/(W^T W H) with W fixed. Update W analogously as W <- W*(V H^T)/(W
    H H^T) with H fixed, evaluating each block rule against its current other factor.
    Multiplication and division of corresponding entries are elementwise. The proof
    uses a quadratic auxiliary function whose diagonal curvature majorizes W^T W,
    with current positive coordinates required in its displayed derivation. For generalized
    KL divergence, H_aμ is multiplied by [sum_i W_ia V_iμ/(WH)_iμ]/[sum_i W_ia], and
    W_ia by [sum_μ H_aμ V_iμ/(WH)_iμ]/[sum_μ H_aμ], with the other block fixed. Jensen
    majorization of the negative logarithm gives the source auxiliary function. With
    valid ratios and the stated domain, exact minimization of each auxiliary does
    not increase the corresponding objective. These are two objective-specific rules,
    not a universal multiplicative update for arbitrary losses. Monotone objective
    values do not alone prove convergence of factor matrices to a local minimum. In
    a curator scalar example V=1 and W=H=0.5, updating both factors simultaneously
    from their old values sets both to 2 and raises squared error from 0.5625 to 9.
    A separate fixed-W example W=[[1,0],[1,1]], V=[1,2]^T and H=[1.5,0]^T is unchanged
    by the H rule, although the zero coordinate has half-squared-error derivative
    -0.5 and increasing it lowers the loss. This is a zero-locked nonoptimal block
    state with positive denominators, not a claim about an inspected author implementation.
    Limitations: The rules require defined denominators and an explicit zero policy.
    The proof for positive current coordinates does not automatically cover arbitrary
    boundary initializations; multiplicative zeros may remain locked. Sequential block
    descent is not a license to update both blocks from stale factors. Arbitrary epsilon
    denominators, clipping, approximate updates or added penalties change the algorithm
    and require separate analysis. The objective is generally nonconvex jointly in
    W and H. Descent, bounded objective values and an auxiliary-function proof do
    not establish unique factors, a global optimum or the source discussion’s unrestricted
    local-optimum guarantee. Finite arithmetic verifies selected update and boundary
    claims; no author software, empirical model fitting or benchmark was executed.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A mathematical method, specific learning algorithm or latent-variable
      model family; not a trained instance.
    evidence_ids:
    - leeseungmultiplicativeupdates-source-0
  - name: aio-assessment
    value: related_match
    definition: NMF maps related to task-scoped DimensionalityReduction, preserving
      the mathematical-method/task distinction and allowing factor sizes that do not
      reduce dimension. Lee-Seung fitting and Infomax ICA map related to UnsupervisedLearning,
      reflecting their defining unlabeled parameter estimation without an is-a assertion.
      Topographic ICA maps broadly to Model and related to UnsupervisedLearning. TrainingStrategy
      has a preprocessing genus; RepresentationLearning and SparseLearning are network-scoped,
      while nonnegative factors need not be sparse. PCA orthogonality and Kohonen
      prototype topology are not equivalent identities. Deep InfoMax, ordinary SGD,
      EM, GCA, PoE, PoT and fixed-prior IWF contextualize distinct contrasts, model
      laws and optimization roles; contextual records receive no renewed scientific
      approval.
    evidence_ids:
    - mapping
- assessment_id: infomaxica
  area: evidence
  topic: Definition, identity, claim support, limitations and AIO mapping direction
  outcome: supported
  target_ids:
  - AIMech:InfomaxICA
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - infomaxica-source-0
  summary: 'Scoped to the standard logistic instantaneous algorithm of Bell and Sejnowski
    1995. The unsquashed linear outputs estimate sources; the sigmoid outputs define
    its entropy contrast. This is distinct from the broader Infomax principle, Deep
    InfoMax’s learned dependence critics, later natural-gradient ICA, FastICA, and
    the paper’s separately developed temporal deconvolution and generalized-sigmoid
    variants. Four candidate identities were compared against all 442 pinned AIO IDs,
    labels and scoped synonyms and 450 preceding native IDs, names and aliases, with
    no normalized match. Ignored/hidden full-checkout searches returned the same 106
    matched-line set in each checkout after the prior merge. All matched excerpts
    from 76 files were read; they are discovery context, not existing concept records.
    The semantic search covered all pinned labels and scoped synonyms and returned
    212 rows: 205 byte-equivalent prior readings and seven additional rows, all inspected.
    Twenty-three annotated AIO nodes with outgoing edges comprise 21 unchanged prior
    readings and two new inspections. Thirty contextual YAMLs, including seven native
    neighbors, comprise 25 unchanged prior readings and five complete new readings.
    This absence assessment is bounded to the pinned snapshot and inspected maintained
    corpus.'
  details: 'Let u=Wx+b with square invertible W and y_i=1/(1+exp(-u_i)). The output
    differential entropy differs from H(X) by log|det W|+sum_i E[log(y_i(1-y_i))].
    Its ordinary gradient updates are proportional to W^(-T)+(1-2y)x^T for W and 1-2y
    for b, averaged or sampled over observations. This is the ordinary parameter gradient,
    not a natural-gradient replacement. The inverse term is undefined at singular
    W, and finite steps need not preserve invertibility automatically. The curated
    objective is output differential entropy. For noiseless invertible transformations
    of continuous variables, mutual information between input and output is infinite,
    so the finite change-of-variables contrast is not a finite noiseless mutual-information
    value. A finite added output-noise model has a different noisy-output entropy
    unless the appropriate limiting approximation is justified. Maximizing the sigmoid-output
    entropy also trades off marginal entropy and dependence: a fixed nonlinearity
    mismatched to source distributions can prefer mixed outputs. The source illustrates
    this for uniform sources; arbitrary stationary points do not certify independent
    components. The instantaneous application assumes a linear mixture x=A s and seeks
    unsquashed outputs u that recover sources up to scale, sign and permutation under
    suitable distributional and identifiability conditions. The historical demonstrations
    mix recorded audio and discuss failures with multiple Gaussian white-noise sources
    and ill-conditioned mixing. The paper separately derives FIR blind deconvolution,
    which can whiten a nonwhite source instead of recovering the exact original. Neither
    arbitrary acoustic propagation delays nor unmodeled input noise is handled by
    the standard instantaneous rule. Limitations: Square nonsingular mixing, suitable
    source distributions and an appropriate contrast are substantive assumptions.
    The standard fixed logistic rule is not a universal source-separation or independence
    guarantee. The generalized sigmoid ODE in Equation 2.32 gives a chain-rule factor
    y^(p-1)(1-y)^(r-1) multiplying p(1-y)-r*y; Equations 2.33-2.34 omit it outside
    the standard p=r=1 case. Curator arithmetic verifies this discrepancy. Those generalized
    variants are excluded here; no uninspected author-code defect is asserted. Gradient
    ascent with a chosen finite learning rate need not converge globally or monotonically.
    The inverse-weight term is nonlocal; the source does not establish a biological
    learning mechanism. Audio demonstrations, annealing schedules and comparative
    timings are historical source-specific evidence. No author implementation, audio
    separation experiment or benchmark was run.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A mathematical method, specific learning algorithm or latent-variable
      model family; not a trained instance.
    evidence_ids:
    - infomaxica-source-0
  - name: aio-assessment
    value: related_match
    definition: NMF maps related to task-scoped DimensionalityReduction, preserving
      the mathematical-method/task distinction and allowing factor sizes that do not
      reduce dimension. Lee-Seung fitting and Infomax ICA map related to UnsupervisedLearning,
      reflecting their defining unlabeled parameter estimation without an is-a assertion.
      Topographic ICA maps broadly to Model and related to UnsupervisedLearning. TrainingStrategy
      has a preprocessing genus; RepresentationLearning and SparseLearning are network-scoped,
      while nonnegative factors need not be sparse. PCA orthogonality and Kohonen
      prototype topology are not equivalent identities. Deep InfoMax, ordinary SGD,
      EM, GCA, PoE, PoT and fixed-prior IWF contextualize distinct contrasts, model
      laws and optimization roles; contextual records receive no renewed scientific
      approval.
    evidence_ids:
    - mapping
- assessment_id: topographicica
  area: evidence
  topic: Definition, identity, claim support, limitations and AIO mapping direction
  outcome: supported
  target_ids:
  - AIMech:TopographicICA
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - topographicica-source-0
  summary: 'Scoped to Hyvarinen, Hoyer and Inki’s 2001 generative construction and
    its approximate estimation. Topography describes higher-order statistical dependence
    of component amplitudes, not Euclidean proximity of prototypes, causal structure
    or arbitrary spatial data. This differs from ordinary mutually independent ICA,
    Kohonen maps and the undirected Product of Student-t analysis density. Overlapping
    neighborhoods distinguish it from disjoint independent subspaces; the source likelihood
    surrogate is not silently substituted for the exact directed model. Four candidate
    identities were compared against all 442 pinned AIO IDs, labels and scoped synonyms
    and 450 preceding native IDs, names and aliases, with no normalized match. Ignored/hidden
    full-checkout searches returned the same 106 matched-line set in each checkout
    after the prior merge. All matched excerpts from 76 files were read; they are
    discovery context, not existing concept records. The semantic search covered all
    pinned labels and scoped synonyms and returned 212 rows: 205 byte-equivalent prior
    readings and seven additional rows, all inspected. Twenty-three annotated AIO
    nodes with outgoing edges comprise 21 unchanged prior readings and two new inspections.
    Thirty contextual YAMLs, including seven native neighbors, comprise 25 unchanged
    prior readings and five complete new readings. This absence assessment is bounded
    to the pinned snapshot and inspected maintained corpus.'
  details: 'Generate independent higher-order variables u_k and independent zero-mean
    unit-variance z_i, all mutually independent. For a fixed nonnegative neighborhood
    h, set sigma_i=phi(sum_k h(i,k)u_k), s_i=sigma_i*z_i and x=A s with square invertible
    mixing A, proper latent distributions and finite positive scales. Distinct s_i
    are uncorrelated when the needed moments exist, but their squared-value covariance
    equals Cov(sigma_i^2,sigma_j^2). Disjoint scale neighborhoods imply independent
    components under the model. Shared neighborhoods can yield energy dependence;
    constant scales need not. Gaussian z gives Gaussian scale mixtures, with excess
    fourth cumulant 3 Var(sigma_i^2) when finite. Delta neighborhoods recover independent
    source components. The exact marginal integrates the latent scales. For Gaussian
    z and phi(v)=v^(-1/2), the paper replaces sqrt(sum_k h(i,k)u_k) by sqrt(h(i,i)u_i)
    in the integrand. With nonnegative u,h and positive diagonal h this produces a
    pointwise lower bound, factoring as exp(sum_k G(sum_i h(i,k)s_i^2)), where G is
    the one-dimensional log integral in Equation 3.9. This is generally an unnormalized
    surrogate rather than the original marginal. Normalizing the surrogate does not
    preserve its pointwise lower-bound property. The later smoothed-square-root and
    polynomial contrast choices are not automatically exact lower bounds for a specified
    latent prior. After centering and whitening, optionally in a PCA-reduced subspace,
    constrain the square separating matrix W to be orthogonal. Write a_i=w_i^T z,
    local energies e_k=sum_j h(k,j)a_j^2 and r_i=sum_k h(i,k)Gprime(e_k) for symmetric
    h. The source contrast gradient is proportional to E[z*a_i*r_i], with a common
    factor two absorbed into step size. Reorthogonalize using W <- (W W^T)^(-1/2)
    W when full rank. On this orthogonal domain log|det W| is constant, explaining
    its omission. The rule differentiates the approximate contrast, not the generally
    intractable exact likelihood. The image experiment finds energy covariance that
    remains above zero at long distances, indicating mismatch to the model’s distant-independence
    ideal. Synthetic recovery with matched topology does not prove consistency for
    arbitrary contrasts; the quadratic/kurtosis contrast gives unsatisfactory image
    results. Proper scale mixtures need not have finite variance: with delta neighborhoods
    and squared-standard-Gaussian u, the inverse-square-root construction gives a
    Cauchy component. Thus moment and whitening arguments need conditions beyond a
    proper probability distribution. A positive quadratic G also defines an optimization
    contrast, not an integrable exp(G) source density over all real coordinates. Limitations:
    Neighborhoods and latent hyperparameters are specified by the model; the paper
    does not infer an arbitrary topology. Neighborhood overlap, sufficient moments
    and actual data fit govern statistical interpretations. A proper generative marginal,
    its lower-bound surrogate and heuristic contrasts are different objects. For fixed
    complete invertible transforms a surrogate normalizer can be independent of W
    without making the surrogate the original likelihood. Whitening and moment claims
    require finite moments and suitable covariance rank. Orthogonalization requires
    a full-rank intermediate matrix. PCA reduction retains a subspace; it does not
    reconstruct discarded dimensions. Finite-step projected gradient updates do not
    establish monotone ascent, unique estimates or global optimization. The finite
    calculations check local derivatives, mixture normalization and energy covariance,
    not statistical consistency. Natural-image features and a two-minute MEG artifact
    illustration provide bounded applications. Complex-cell and wiring interpretations
    are hypotheses, not causal biological validation; adjacency is not automatically
    meaningful for every recovered signal. No author implementation, image-model training,
    MEG processing or benchmark was executed.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: A mathematical method, specific learning algorithm or latent-variable
      model family; not a trained instance.
    evidence_ids:
    - topographicica-source-0
  - name: aio-assessment
    value: broad_match,related_match
    definition: NMF maps related to task-scoped DimensionalityReduction, preserving
      the mathematical-method/task distinction and allowing factor sizes that do not
      reduce dimension. Lee-Seung fitting and Infomax ICA map related to UnsupervisedLearning,
      reflecting their defining unlabeled parameter estimation without an is-a assertion.
      Topographic ICA maps broadly to Model and related to UnsupervisedLearning. TrainingStrategy
      has a preprocessing genus; RepresentationLearning and SparseLearning are network-scoped,
      while nonnegative factors need not be sparse. PCA orthogonality and Kohonen
      prototype topology are not equivalent identities. Deep InfoMax, ordinary SGD,
      EM, GCA, PoE, PoT and fixed-prior IWF contextualize distinct contrasts, model
      laws and optimization roles; contextual records receive no renewed scientific
      approval.
    evidence_ids:
    - mapping
- assessment_id: factorization-versus-fitting
  area: consistency
  topic: Mathematical representation versus a specific optimization algorithm
  outcome: supported
  target_ids:
  - AIMech:NonnegativeMatrixFactorization
  - AIMech:LeeSeungMultiplicativeUpdates
  evidence_ids:
  - nonnegativematrixfactorization-source-0
  - leeseungmultiplicativeupdates-source-0
  - finite-boundaries
  - neighbors
  summary: Retain NMF and Lee-Seung updates as distinct concepts.
  details: Nonnegative factors define additive reconstruction, not guaranteed sparsity
    or identifiable physical causes. The two multiplicative rules fit different objectives
    and are not the definition of NMF. Positive diagonal rescaling and factor permutation
    preserve the product. Generalized KL is not necessarily a distributional KL and
    observed zeros are not missing values.
- assessment_id: nmf-descent-domain
  area: consistency
  topic: Block-update proofs, zero locking and convergence scope
  outcome: supported
  target_ids:
  - AIMech:LeeSeungMultiplicativeUpdates
  evidence_ids:
  - leeseungmultiplicativeupdates-source-0
  - finite-boundaries
  summary: Preserve the exact update domain and limited guarantee.
  details: The source auxiliary proof supports valid sequential blocks. A scalar simultaneous
    old-state update increases error from 0.5625 to 9. A separate fixed-W zero-locked
    block violates nonnegative first-order optimality despite positive denominators.
    These examples do not claim the complete joint algorithm was run or that an uninspected
    implementation has a defect. Objective descent is not proof of local/global factor
    convergence.
- assessment_id: infomax-objective
  area: consistency
  topic: Output differential entropy and ordinary gradient
  outcome: supported
  target_ids:
  - AIMech:InfomaxICA
  evidence_ids:
  - infomaxica-source-0
  - finite-boundaries
  - neighbors
  summary: Retain standard logistic instantaneous Infomax with explicit information
    and distribution qualifications.
  details: Finite differences verify the ordinary W inverse-transpose and logistic
    score gradient. Deterministic invertible continuous input/output mutual information
    is infinite; the finite contrast is output differential entropy, with a separate
    low-noise interpretation. The paper itself illustrates nonlinearity mismatch and
    failure of general independence claims. Deep InfoMax dependence critics, natural-gradient
    ICA, FastICA and FIR deconvolution are distinct scopes.
- assessment_id: infomax-generalization
  area: consistency
  topic: Generalized-sigmoid derivative boundary
  outcome: supported
  target_ids:
  - AIMech:InfomaxICA
  evidence_ids:
  - infomaxica-source-0
  - finite-boundaries
  summary: Exclude unsupported transfer of the displayed generalized formula.
  details: The standard p=r=1 logistic rule is valid. The ODE gprime=y^p(1-y)^r gives
    d log(gprime)/du=[p(1-y)-r*y]*y^(p-1)(1-y)^(r-1). Source Equations 2.33-2.34 omit
    the last factor in general. Curator arithmetic gives 0.0735 versus 0.5 for p=2,r=3,y=0.3.
    No code defect or universal generalized-sigmoid failure is asserted.
- assessment_id: topographic-model-and-surrogate
  area: consistency
  topic: Generative dependence, lower-bound normalization and moments
  outcome: supported
  target_ids:
  - AIMech:TopographicICA
  evidence_ids:
  - topographicica-source-0
  - finite-boundaries
  - neighbors
  summary: Retain the shared-scale model without replacing its likelihood by a heuristic
    contrast.
  details: A finite discrete-scale analogue has uncorrelated components and positive
    energy covariance. Its pointwise lower-bound surrogate has total mass about 0.6055;
    renormalization can exceed the true density. The exact model, its approximation
    and later contrast choices remain distinct. A proper Cauchy specialization lacks
    finite variance, and a positive quadratic contrast is not a normalized source
    density. These are algebraic qualifications, not claims about all historical fitted
    parameters.
- assessment_id: topographic-estimation
  area: consistency
  topic: Whitened orthogonal estimation and neighborhood scope
  outcome: supported
  target_ids:
  - AIMech:TopographicICA
  evidence_ids:
  - topographicica-source-0
  - finite-boundaries
  summary: Keep the source constrained-gradient approximation explicit.
  details: The finite contrast derivative matches the source modulation rule, including
    the absorbed common factor two. Log determinant is constant only on the stated
    orthogonal domain. Whitening and reorthogonalization need moment/rank conditions;
    finite steps do not guarantee ascent or global optimization. Fixed neighborhoods
    and component-energy relationships differ from prototype geometry, spatial causes
    and unique anatomical localization.
- assessment_id: evidence-and-mapping-scope
  area: grounding
  topic: Primary versions, contextual comparisons and mapping abstraction
  outcome: supported
  target_ids:
  - AIMech:NonnegativeMatrixFactorization
  - AIMech:LeeSeungMultiplicativeUpdates
  - AIMech:InfomaxICA
  - AIMech:TopographicICA
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - nonnegativematrixfactorization-source-0
  - infomaxica-source-0
  - topographicica-source-0
  summary: Preserve local concept boundaries and bounded historical evidence.
  details: NMF maps related to task-scoped DimensionalityReduction, preserving the
    mathematical-method/task distinction and allowing factor sizes that do not reduce
    dimension. Lee-Seung fitting and Infomax ICA map related to UnsupervisedLearning,
    reflecting their defining unlabeled parameter estimation without an is-a assertion.
    Topographic ICA maps broadly to Model and related to UnsupervisedLearning. TrainingStrategy
    has a preprocessing genus; RepresentationLearning and SparseLearning are network-scoped,
    while nonnegative factors need not be sparse. PCA orthogonality and Kohonen prototype
    topology are not equivalent identities. Deep InfoMax, ordinary SGD, EM, GCA, PoE,
    PoT and fixed-prior IWF contextualize distinct contrasts, model laws and optimization
    roles; contextual records receive no renewed scientific approval. All 70 primary
    pages were visually read. NMF is not a new benchmark paper; audio, image and MEG
    examples do not establish general superiority or a biological mechanism. No author
    implementation, empirical fitting or benchmark ran.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:NonnegativeMatrixFactorization
  - AIMech:LeeSeungMultiplicativeUpdates
  - AIMech:InfomaxICA
  - AIMech:TopographicICA
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - nonnegativematrixfactorization-source-0
  - leeseungmultiplicativeupdates-source-0
  - infomaxica-source-0
  - topographicica-source-0
  rationale: The factorization problem, objective-specific block optimizer, ordinary-gradient
    source-separation algorithm and topographic shared-scale probability model denote
    different supported concepts. Related task mappings preserve abstraction; the
    specific model maps broadly to Model. Similar basis representations or names do
    not justify lumping.
limitations:
- Adversarial author self-review only; all four records remain DRAFT.
- The initial vendored network lookup failed inside the sandbox; the authorized network
  retry passed.
- All 70 pages of three primary PDFs were visually read, including the NMF proofs,
  the scanned Infomax appendix and topographic ICA experiments and appendix. NMF uses
  PDF-page locators; printed Infomax page=PDF page+1128 and topographic ICA page=PDF
  page+1526.
- Exact source URLs, versions, UTC access times and downloaded-byte SHA-256 values
  are retained. Search/open times are captured immediately before the actual requests;
  output captures are discovery provenance, not a claim to have read every returned
  link.
- NMF and Lee-Seung fitting are distinct concepts. Descent requires valid sequential
  block updates; zero-locking and factor indeterminacy preclude blanket local-optimum
  or unique-parts claims.
- The standard logistic Infomax gradient is retained. No finite noiseless continuous
  mutual-information value, arbitrary-source independence guarantee or silently corrected
  generalized-sigmoid implementation is asserted.
- Topographic ICA preserves the directed latent-scale model, unnormalized lower-bound
  surrogate and heuristic contrast distinctions. Moment existence, whitening rank
  and neighborhood overlap are substantive conditions.
- Historical image, audio and MEG demonstrations do not establish universal gains
  or biological mechanisms. No author implementation, training or empirical benchmark
  was executed.
- Fifteen new provisional cohorts leave 349 pending leads, plus partially addressed
  and deferred entries. Four new records remain DRAFT; no global saturation is claimed.
links: []
tags:
- native-concepts
- factorization-and-topographic-components
- self-review
- discovery-ongoing
```
