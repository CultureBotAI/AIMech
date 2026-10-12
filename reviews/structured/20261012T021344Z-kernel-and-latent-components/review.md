# Scientific self-review of kernel PCA, GTM and FastICA

- Review: 20261012T021344Z-kernel-and-latent-components
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T02:08:10Z
- Finished UTC: 2026-10-12T02:13:44Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain kernel PCA, the original generative topographic mapping model and the FastICA algorithm family. Explicitly preserve feature-space kernel validity and preimage limits, exact mixture/EM semantics, smoothness versus invertibility, and conditional FastICA convergence and robustness. No actionable curation finding remains in the three additions.

## Scope And Provenance

All fields of three source-defined kernel and latent-component concepts.

Selection: Exact maintained IDs KernelPCA, GenerativeTopographicMapping and FastICA; full selected cohort without sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base de8760275471de9fc4e9a36b67fb52ef9d13a499.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:KernelPCA | data/curated/KernelPCA.yaml | maintained | Kernel Principal Component Analysis |
| AIMech:GenerativeTopographicMapping | data/curated/GenerativeTopographicMapping.yaml | maintained | Generative Topographic Mapping |
| AIMech:FastICA | data/curated/FastICA.yaml | maintained | FastICA |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:KernelPCA, AIMech:GenerativeTopographicMapping, AIMech:FastICA | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 119.48s (0:01:59)<br>Checked 442 record(s); 0 failed.<br>Checked 457 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 133 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 130,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:KernelPCA, AIMech:GenerativeTopographicMapping, AIMech:FastICA | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:KernelPCA, AIMech:GenerativeTopographicMapping, AIMech:FastICA | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:KernelPCA, AIMech:GenerativeTopographicMapping, AIMech:FastICA | Command exited 0 with no output. |
| Kernel and latent-component boundaries | passed | True | AIMech:KernelPCA, AIMech:GenerativeTopographicMapping, AIMech:FastICA | {"kernel_pca": {"gram_eigenvalue": 1.0, "covariance_eigenvalue": 0.4999999999999999, "test_projection_kernel": 2.1213203435596424, "test_projection_explicit": 2.121320343559642, "input_mean": 0.0, "quadratic_feature_mean": 1.0, "feature_mean_required_cross_squared": 0.5, "tanh_gram_determinant": -0.16826582059019524, "tanh_centered_nonzero_eigenvalue": -0.08356585222840096}, "gtm": {"log_likelihood_before": -7.140362161327257, "log_likelihood_after_one_exact_update": -4.440645606528282, "new_precision": 6.109470221563882, "normal_equation_max_error": 6.938893903907228e-18, "folded_map_responsibilities": [0.49999999948471163, 1.0305768101571904e-09, 0.49999999948471163], "posterior_mean": 0.0}, "fastica": {"zero_kurtosis_source_second_moment": 0.9999999999999998, "fourth_moment": 2.999999999999999, "two_source_cubic_update": [-4.440892098500626e-16, 0.0], "tied_mixed_start_next": [-0.7071067811865476, -0.7071067811865476], "untied_ratio_after_update": 0.4218749999999999, "zero_decorrelation_eigenvalue_after_update": 0.0}, "scope": "Finite synthetic arithmetic only; no author software, training or empirical benchmark reproduced."} |

## Scientific And Domain Assessments

### Definition, identity, claim support, limitations and AIO mapping direction

evidence: supported. Targets: AIMech:KernelPCA.

The Schölkopf-Smola-Müller kernel eigenvalue construction generalizes ordinary PCA to a kernel-defined feature space. It includes linear PCA as a special case but is not the identity of ordinary input-space PCA, an SVM classifier, a dot-product KernelLayer, Isomap, LLE or Diffusion Maps. A trained embedding, chosen kernel and preimage approximation are not separate aliases for the algorithm. Three candidate identities were compared against all 442 pinned AIO IDs, labels and scoped synonyms and 454 preceding native IDs, names and aliases, with no normalized match. Searches of both complete checkouts included ignored and hidden files and returned the same 176 matched-line set across 81 paths. All matching excerpts were read and distinguished from existing concept records; historical ledgers were not reread in full solely because they contained a match. All 213 semantic-search rows were read, including 212 unchanged prior rows and the additional KernelLayer row. Twenty-one annotated AIO nodes with outgoing edges were inspected: 19 unchanged prior readings and two new readings. Thirty-one contextual YAMLs, including ten native neighbors, comprise 23 unchanged prior readings and eight complete readings in this round. This identity assessment is bounded to the pinned snapshot and maintained corpus.

For M training points and a positive-semidefinite kernel k, form K_ij=k(x_i,x_j) and Kc=H K H with H=I-11^T/M. If Kc v=kappa v, &#124;&#124;v&#124;&#124;=1 and kappa&gt;0, coefficients alpha=v/sqrt(kappa) define a unit feature-space principal axis. The corresponding empirical covariance eigenvalue is kappa/M. Centered rank is at most M-1. Zero Gram eigenvalues do not define additional nonzero covariance directions. For a new x, center its similarity to each training point using the same training feature mean: kc_i(x)=k(x_i,x)-M^(-1)sum_j k(x_j,x)-M^(-1)sum_j K_ij+M^(-2)sum_jl K_jl. Its component coordinate is sum_i alpha_i kc_i(x). Centering input coordinates before a nonlinear kernel does not generally center the feature vectors; centering each test batch independently changes the learned projection. With a fixed valid kernel, leading components maximize retained empirical variance and minimize rank-constrained squared reconstruction error in the centered feature space. Their sample coordinates are uncorrelated, not necessarily statistically independent. They can outnumber input dimensions. A linear kernel recovers ordinary PCA with consistent centering. Truncated feature reconstructions or principal directions need not have an exact input-space preimage, so reconstructing original inputs is a separate problem. The feature-space covariance interpretation requires a positive-semidefinite kernel. The paper lists sigmoid similarities, but arbitrary tanh parameters do not meet that requirement: a curator two-point example k(x,y)=tanh(x*y), x in {1,2}, gives a negative Gram determinant and a negative eigenvalue even after centering. Keeping selected positive eigenpairs of an indefinite similarity does not establish that the original similarity is a Hilbert-space inner product. Limitations: Kernel and hyperparameter selection remain modeling decisions. An eigensolution for a fixed kernel does not solve all kernel-selection or preimage optimization problems. The exact Gram construction requires storage quadratic in training sample count; partial eigensolvers, subsets and reduced-set projections are additional approximation choices. Implicit features avoid explicit feature-dimension costs, not all sample-size costs. Eigenvector signs and bases within degenerate eigenspaces are nonunique. Variance and reconstruction guarantees concern the chosen feature space, not causal factors, independence, universal input reconstruction or classification accuracy. All 21 source pages were inspected. Finite calculations verify centering, eigenvalue scaling, projection and PSD boundaries; the historical USPS classifier experiments and author implementation were not reproduced.

### Definition, identity, claim support, limitations and AIO mapping direction

evidence: supported. Targets: AIMech:GenerativeTopographicMapping.

Scoped to the original fixed-basis GTM construction and its batch EM fitting. The shared latent-to-data map ties Gaussian centers and distinguishes the model from an unconstrained mixture, a conditional mixture-density network, a Kohonen map and topographic ICA energy dependence. Gaussian radial basis functions are a usual map choice, not an identity with every radial-basis network. Learned mixture weights, heteroscedastic extensions and mixtures of GTMs require separate scope. Three candidate identities were compared against all 442 pinned AIO IDs, labels and scoped synonyms and 454 preceding native IDs, names and aliases, with no normalized match. Searches of both complete checkouts included ignored and hidden files and returned the same 176 matched-line set across 81 paths. All matching excerpts were read and distinguished from existing concept records; historical ledgers were not reread in full solely because they contained a match. All 213 semantic-search rows were read, including 212 unchanged prior rows and the additional KernelLayer row. Twenty-one annotated AIO nodes with outgoing edges were inspected: 19 unchanged prior readings and two new readings. Thirty-one contextual YAMLs, including ten native neighbors, comprise 23 unchanged prior readings and eight complete readings in this round. This identity assessment is bounded to the pinned snapshot and maintained corpus.

Choose K fixed nodes x_i in a latent space of dimension L&lt;D, fixed smooth basis vectors phi(x_i), a weight matrix W and shared precision beta&gt;0. Set y_i=W phi(x_i) and p(t)=K^(-1)sum_i Normal(t;y_i,beta^(-1)I_D). This finite mixture is normalized exactly for finite parameters; the equal node weights do not imply a uniform density over the mapped surface. Mixture centers move together through W rather than being independent free parameters. For N observations, the E-step gives R_in proportional to exp(-beta*&#124;&#124;t_n-W phi(x_i)&#124;&#124;^2/2), normalized over nodes i. With Phi_ij=phi_j(x_i), T containing data rows and G_ii=sum_n R_in, the unregularized M-step solves Phi^T G Phi W_new^T=Phi^T R T. Then beta_new^(-1)=(ND)^(-1)sum_ni R_in&#124;&#124;t_n-W_new phi(x_i)&#124;&#124;^2, using the old responsibilities. Exact well-defined EM updates make the observed-data log likelihood nondecreasing. Rank deficiency can require a pseudoinverse or another weighted least-squares minimizer; zero residual variance lies outside the finite-positive-precision model. Bayes responsibilities define a posterior distribution over latent nodes for each observation. A posterior-mean display uses sum_i R_in x_i; a modal display selects a node with maximum responsibility. Multimodal posteriors can make the mean misleading. Smooth forward mapping supports local continuity, but does not ensure global injectivity, distance preservation or a unique inverse. A curator circular-map example has identical images for separated latent nodes and a posterior mean at a nearly unsupported middle node. EM objective nondecrease is narrower than an unconditional guarantee of convergence to a local maximum or globally optimal density. Gaussian weight regularization changes the objective to MAP and changes the normal equations. The original comparisons with SOM concern explicit mixture probability, soft responsibilities and tied-center regression; they do not establish universal superiority, monotonic posterior concentration or biologically correct topology. Limitations: Latent dimension, nodes, basis functions and smoothness parameters are modeling choices. The source does not establish automatic recovery of the true manifold or globally preserved topology. Likelihood fitting is nonconvex and sensitive to initialization and model choice. Responsibilities require numerically stable evaluation; exact finite-parameter EM statements do not guarantee arbitrary approximate or floating-point implementations. The source’s effective regression smoother can have negative entries; it is not the posterior responsibility matrix. Its row-sum property relies on the stated constant-basis and unregularized algebra. The 16-page author reprint, including simulated oil-flow and toy-curve experiments, was read completely. Finite calculations check a tiny exact update and a topology boundary; no author software, empirical training or benchmark comparison was reproduced.

### Definition, identity, claim support, limitations and AIO mapping direction

evidence: supported. Targets: AIMech:FastICA.

Scoped to Hyvarinen-Oja 1997 kurtosis FastICA and Hyvarinen 1999 generalized contrasts. This is an estimation algorithm, not the general ICA model, a trained source separator, ordinary-gradient Infomax ICA, topographic ICA or every fixed-point optimizer. Deflation and symmetric variants share the core update but have distinct ordering and decorrelation behavior; optional stabilization is not a claim that every variant is step-size-free. Three candidate identities were compared against all 442 pinned AIO IDs, labels and scoped synonyms and 454 preceding native IDs, names and aliases, with no normalized match. Searches of both complete checkouts included ignored and hidden files and returned the same 176 matched-line set across 81 paths. All matching excerpts were read and distinguished from existing concept records; historical ledgers were not reread in full solely because they contained a match. All 213 semantic-search rows were read, including 212 unchanged prior rows and the additional KernelLayer row. Twenty-one annotated AIO nodes with outgoing edges were inspected: 19 unchanged prior readings and two new readings. Thirty-one contextual YAMLs, including ten native neighbors, comprise 23 unchanged prior readings and eight complete readings in this round. This identity assessment is bounded to the pinned snapshot and maintained corpus.

For centered whitened observations x with E[xx^T]=I and unit w, choose a differentiable nonlinearity g=Gprime and compute w_plus=E[x*g(w^T x)]-E[gprime(w^T x)]*w, then normalize its nonzero norm. The source derives this from an approximate Newton step for a constrained projection contrast; sample means replace expectations in practice. Cubic g(u)=u^3 gives the original kurtosis step E[x(w^T x)^3]-3w under the whitening and unit-norm conditions. Tanh and Gaussian-weighted-linear nonlinearities are other source choices. Deflation subtracts projections on previously estimated orthonormal directions after each update and renormalizes. Symmetric FastICA updates rows together and applies W &lt;- (W W^T)^(-1/2)W for whitened data, requiring full row rank. For nonsphered data, the source uses covariance-metric normalization and decorrelation with nonsingular covariance. Orthogonality prevents exact duplicate directions but does not by itself prove statistical independence. Signs and component ordering are not identified by the ICA objective. The generalized proof assumes the linear independent-source model, exact expectations, suitable moments and E[s_i*g(s_i)-gprime(s_i)] nonzero. It establishes local convergence near a source direction, generally quadratic and cubic with the stated symmetry condition. For the original kurtosis rule, source-coordinate updates are proportional to kurt(s_i)*z_i^3. A unique dominant scaled initial coordinate yields the cubic ratio contraction; tied starts can remain mixed up to sign. A source can be non-Gaussian with zero kurtosis, so the kurtosis rule cannot resolve multiple such sources merely from their non-Gaussianity. The squared contrast [E G(w^T x)-E G(v)]^2, with standard Gaussian v, approximates negentropy rather than giving exact entropy for arbitrary distributions. Contrast choice affects consistency conditions, estimation variance and sensitivity to outliers. The robustness theorem assumes robust whitening and explicitly does not give a globally bounded influence function. The reported outlier experiment estimates covariance from uncontaminated data to emulate robust whitening; it does not certify robustness of an arbitrary complete FastICA pipeline. Limitations: Standard source identification assumes an appropriate full-rank instantaneous linear mixture, independent sources and at most one Gaussian source; the usable contrasts additionally require their own moments and nondegeneracy. Whitening needs finite covariance and a retained full-rank subspace. A zero fixed-point update cannot be normalized. Singular intermediate matrices cannot be repaired to full rank by the displayed symmetric inverse square root or iterative decorrelation formula. Finite-sample errors and model mismatch are outside the exact-expectation convergence proof. The original sign-insensitive stopping criterion can declare a mixed tied-start direction unchanged. Finite counterexamples qualify blanket recovery claims; they do not establish typical failure rates for randomized practical implementations. Optional stabilized, nonsphered, noisy and overcomplete variants need their stated assumptions. The core algorithm is not universally globally convergent, noise-consistent, step-size-free in all variants, or superior to other estimators. Both primary PDFs were read completely, totaling 19 pages. Finite arithmetic verifies zero-kurtosis and tied-start boundaries; no source-separation training, author implementation or historical benchmark was reproduced.

### Feature centering, spectral normalization and preimages

consistency: supported. Targets: AIMech:KernelPCA.

Retain the kernel feature-space interpretation with its conditions.

The explicit quadratic feature and centered-kernel computations agree. Gram eigenvalue kappa and covariance eigenvalue kappa/M are kept distinct. Training feature means are reused for unseen points; input centering is insufficient for nonlinear features. The finite tanh Gram matrix is indefinite even after centering, and a quadratic feature mean need not have an input preimage. Variance and reconstruction guarantees do not imply independent factors, input reconstruction or classifier superiority.

### Normalized latent mixture and exact EM

consistency: supported. Targets: AIMech:GenerativeTopographicMapping.

Retain the original equal-weight, shared-variance, tied-center model.

The finite normalized mixture uses a discrete latent prior, not an unnormalized product or generic conditional MDN. Exact responsibilities and weighted normal equations yield the stated variance update. Finite arithmetic increases log likelihood and satisfies normal equations; it does not prove arbitrary numerical implementations, global optimality or unconditional local-maximum convergence. Rank deficiency and zero residual variance require explicit treatment, and MAP regularization changes the objective.

### Forward smoothness versus latent inversion

consistency: supported. Targets: AIMech:GenerativeTopographicMapping.

Preserve multimodal posterior and noninjective-map limitations.

A circle-valued smooth map with nonzero derivative identifies separated latent nodes. At the shared image, the posterior mean lies at a nearly unsupported middle node. Thus continuity and local rank do not establish a globally invertible embedding. GTM posterior responsibilities differ from the signed effective regression smoother, the Kohonen hard winner and topographic ICA component-energy neighborhoods.

### Exact-expectation contraction, zero kurtosis and rank

consistency: supported. Targets: AIMech:FastICA.

Keep convergence claims conditional and source-version specific.

The generalized rule is an approximate-Newton constrained-contrast iteration. Its local proof requires the independent linear model, exact expectations, suitable moments and nonzero source contrast factors. The original cubic update has zero output for two independent non-Gaussian zero-kurtosis sources; a tied Rademacher initialization stays mixed up to sign. An untied ratio follows cubic contraction. These exceptional finite examples do not establish practical failure frequencies. Symmetric inverse square roots and iterative decorrelation cannot restore missing row rank.

### Approximate negentropy and preprocessing assumptions

consistency: supported. Targets: AIMech:FastICA.

Retain restricted contrast and robustness claims.

The contrast is an approximation to negentropy. The primary robustness theorem assumes robust whitening and does not give a globally bounded influence function; the outlier experiment estimates covariance from the uncontaminated observations. Batch FastICA, adaptive Hebbian rules, stabilized variants and noise/overcomplete extensions are not interchangeable. No unqualified robustness, speed or empirical source-recovery claim is asserted.

### Primary versions and mapping abstraction

grounding: supported. Targets: AIMech:KernelPCA, AIMech:GenerativeTopographicMapping, AIMech:FastICA.

Preserve distinct concepts and bounded historical evidence.

Kernel PCA maps related to PrincipalComponentAnalysis, preserving its kernel feature-space generalization and the pinned task/algorithm distinction. KernelLayer denotes a neural layer, not a spectral algorithm, and the source SVM is a downstream classifier rather than kernel-PCA identity. GTM maps broadly to Model and related to ManifoldLearning: a normalized tied-center latent density with posterior visualization is not the Kohonen prototype algorithm, every RBF network, or topographic ICA amplitude dependence. FastICA maps related to UnsupervisedLearning, not a neural architecture or a preprocessing TrainingStrategy. RepresentationLearning is network-scoped in the pin. Native Infomax, topographic ICA, NMF, GCA, EM, MDN, GPR, LLE, Isomap and Diffusion Maps contextualize different objectives, model laws and geometry; their prior scientific reviews are not renewed by this comparison. All 56 primary pages were visually read, with source-specific pagination. Author-paper PDFs, preprints and journal versions are named accurately; access and publication dates are distinct. Historical USPS, oil-flow and source-separation examples are not new benchmark results.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:KernelPCA, AIMech:GenerativeTopographicMapping, AIMech:FastICA. Kernel spectral feature extraction, a tied-center latent probability model and fixed-point independent-component estimation have distinct defining objects and operations. Source versions within FastICA form one supported algorithm family with explicit variants. Model/task and algorithm/task mappings preserve abstraction.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T020743Z-kernel-and-latent-components.json | supports | Three candidate identities were compared against all 442 pinned AIO IDs, labels and scoped synonyms and 454 preceding native IDs, names and aliases, with no normalized match. Searches of both complete checkouts included ignored and hidden files and returned the same 176 matched-line set across 81 paths. All matching excerpts were read and distinguished from existing concept records; historical ledgers were not reread in full solely because they contained a match. All 213 semantic-search rows were read, including 212 unchanged prior rows and the additional KernelLayer row. Twenty-one annotated AIO nodes with outgoing edges were inspected: 19 unchanged prior readings and two new readings. Thirty-one contextual YAMLs, including ten native neighbors, comprise 23 unchanged prior readings and eight complete readings in this round. This identity assessment is bounded to the pinned snapshot and maintained corpus. |
| mapping | sources/aio/aio.json; 21 annotated CLASS nodes and outgoing edges; all 213 semantic label/synonym rows | supports | Kernel PCA maps related to PrincipalComponentAnalysis, preserving its kernel feature-space generalization and the pinned task/algorithm distinction. KernelLayer denotes a neural layer, not a spectral algorithm, and the source SVM is a downstream classifier rather than kernel-PCA identity. GTM maps broadly to Model and related to ManifoldLearning: a normalized tied-center latent density with posterior visualization is not the Kohonen prototype algorithm, every RBF network, or topographic ICA amplitude dependence. FastICA maps related to UnsupervisedLearning, not a neural architecture or a preprocessing TrainingStrategy. RepresentationLearning is network-scoped in the pin. Native Infomax, topographic ICA, NMF, GCA, EM, MDN, GPR, LLE, Isomap and Diffusion Maps contextualize different objectives, model laws and geometry; their prior scientific reviews are not renewed by this comparison. |
| neighbors | research/discovery/20261012T020743Z-kernel-and-latent-components.json; Ten native neighbors and 21 generated contextual YAMLs in source_analysis.context_reading | supports | Thirty-one contextual YAMLs comprise 23 unchanged prior readings and eight complete current readings. Infomax, topographic ICA, NMF, GCA, EM, MDN, GPR, LLE, Isomap and Diffusion Maps distinguish estimators, model laws, conditional distributions and geometric objectives. Contextual records receive no renewed scientific approval. |
| finite-boundaries | research/discovery/kernel-and-latent-component-boundaries.py; Kernel centering, eigenvalue scaling, projections and PSD; exact GTM update and folded posterior; FastICA zero kurtosis, tied starts and rank | supports | Kernel and explicit-feature projections agree, with Gram eigenvalue 1 and covariance eigenvalue 1/2. Centered inputs need not have centered quadratic features, a feature mean need not have a preimage, and the tested tanh similarity has negative uncentered determinant and centered eigenvalue. A finite exact GTM update raises log likelihood from about -7.1404 to -4.4406 and solves the normal equations to floating-point precision. A smooth circular map yields a multimodal latent posterior whose mean is nearly unsupported. Two independent finite-support non-Gaussian zero-kurtosis sources give a zero original FastICA update, while a tied Rademacher start remains mixed up to sign. An untied component ratio obeys the cubic recurrence. A zero decorrelation eigenvalue remains zero. These are bounded curator arithmetic checks, not author-software or empirical reproduction. |
| kernelpca-source-0 | https://alex.smola.org/papers/1998/SchSmoMul98.pdf; Equation 4.1, printed p. 1305 / PDF p. 7; Appendix B, Equations B.1-B.4 and test-kernel formula, pp. 1316-1317 / PDF pp. 18-19; Section 2, Equations 2.7-2.15, printed pp. 1301-1302 / PDF pp. 3-4; Appendices A-B, pp. 1315-1317 / PDF pp. 17-19; curator explicit distinction of Gram and covariance eigenvalues; Section 3, Equation 3.7, printed p. 1304 / PDF p. 6; Appendix C, Equations C.1-C.3, p. 1317 / PDF p. 19; curator finite PSD counterexample; Sections 2-4.1, Equations 2.7-2.15 and 4.1, printed pp. 1301-1305 / PDF pp. 3-7; Appendix B, pp. 1316-1317 / PDF pp. 18-19; Sections 4.2-4.5, Figures 1-2 and Equation 4.2, printed pp. 1305-1309 / PDF pp. 7-11; Section 6.3.5, pp. 1314-1315 / PDF pp. 16-17 | supports | Nonlinear Component Analysis as a Kernel Eigenvalue Problem. Author-hosted final Neural Computation 10(5):1299-1319 (1998) PDF. All 21 pages visually read; printed page equals PDF page plus 1298. The 1996 technical report and 1997 acceptance date are predecessor metadata, not the publication year. Curator algebraic deductions are distinguished from historical empirical results or uninspected software. |
| generativetopographicmapping-source-0 | https://www.microsoft.com/en-us/research/wp-content/uploads/1998/01/bishop-gtm-ncomp-98.pdf; Section 2.1, Equations 15-16, reprint/PDF p. 6; Sections 4.1-4.2, Equations 21-27 and Figures 6-7, pp. 9-13; curator qualification of the paper’s convergence language; Section 2.1, Equations 8-14, reprint/PDF pp. 5-6; Section 2.4, p. 8; curator rank, boundary and EM qualifications; Section 2.2, Equations 17-19, reprint/PDF p. 6; Sections 2 and 4.2, pp. 4 and 12; curator smooth-map counterexample; Sections 2-2.1, Equations 1-14, reprint/PDF pp. 3-5; Section 2.4, p. 8; Sections 2-2.1, Equations 1-7, reprint/PDF pp. 3-5 | supports | GTM: The Generative Topographic Mapping. Microsoft Research author reprint of the 1998 Neural Computation 10(1):215-234 article. All 16 PDF pages visually read. Locators use the reprint internal pages, which coincide with PDF pages, not the journal pagination. Curator algebraic deductions are distinguished from historical empirical results or uninspected software. |
| fastica-source-0 | https://www.cs.helsinki.fi/u/ahyvarin/papers/NC97.pdf; Section 3.1, internal/PDF pp. 5-6; Section 3.1.2, Equation 10, internal/PDF p. 6; Section 3.2, Equations 11-15, internal/PDF pp. 6-7; Section 5, p. 9 | supports | A Fast Fixed-Point Algorithm for Independent Component Analysis. Author-hosted ten-page preprint marked for Neural Computation 9:1483-1492 (1997). All pages visually read. Locators use internal/PDF pages 1-10 rather than assuming the final journal layout. Curator algebraic deductions are distinguished from historical empirical results or uninspected software. |
| fastica-source-1 | https://www.cs.helsinki.fi/u/ahyvarin/papers/TNN99_reprint.pdf; Appendix A.A, Equations 27-34, printed p. 633 / PDF p. 8; curator finite zero-kurtosis and tied-start examples; Section II.B, Equations 6-8, printed p. 627 / PDF p. 2; Section III.A, Theorems 1-3, p. 628 / PDF p. 3; Section V, pp. 631-632 / PDF pp. 6-7; Section III.B, Equations 14-16, printed p. 629 / PDF p. 4; Section IV.B, Equations 17-20, p. 630 / PDF p. 5; Sections IV.B-IV.C, Equations 20-25, printed pp. 630-631 / PDF pp. 5-6; Sections IV.B-IV.C, Equations 22-26, printed pp. 630-631 / PDF pp. 5-6 | supports | Fast and Robust Fixed-Point Algorithms for Independent Component Analysis. Author-hosted final IEEE Transactions on Neural Networks 10(3):626-634, May 1999, reprint. All nine PDF pages visually read; printed page equals PDF page plus 625. The licensed-download watermark date is not the publication date. Curator algebraic deductions are distinguished from historical empirical results or uninspected software. |

## Limits And Additional Notes

- Adversarial author self-review only; all three records remain DRAFT.
- All 56 PDF pages were visually read: kernel PCA21, GTM16, original FastICA10 and generalized FastICA9. Preprint/reprint pagination is recorded separately from final journal pagination. Earlier truncated page displays and context reads were reopened.
- Source URLs, versions, actual UTC access times and byte hashes are retained. Search/open captures describe discovery provenance, not inspection of every returned link. No full PDFs are redistributed in this change.
- Kernel validity, feature-space centering, Gram/covariance scaling and preimage limitations are explicit. The sigmoid example does not establish a PSD kernel for arbitrary parameters.
- GTM is an exactly normalized finite mixture with a fixed latent prior and tied centers. Smoothness is not global invertibility, and exact EM nondecrease is not an unconditional convergence-to-local-maximum theorem.
- FastICA preserves the distinction between the original cumulant rule, generalized approximate-negentropy contrasts and their practical variants. Exact-expectation, moment, nondegeneracy, rank and robust-whitening assumptions remain explicit.
- No author implementation, empirical training or benchmark was run. Finite synthetic calculations do not establish performance or typical failure rates.
- Three DRAFT additions and sixteen provisional new cohorts leave 363 pending leads plus other unresolved dispositions. No global saturation is claimed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T021344Z-kernel-and-latent-components
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of kernel PCA, GTM and FastICA
started_at: '2026-10-12T02:08:10Z'
finished_at: '2026-10-12T02:13:44Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially read all fields of three final
    maintained records against 56 complete primary PDF pages, 21 annotated AIO nodes
    and ten native neighbors. Finite arithmetic checks centering, normalization, fitting
    and recovery boundaries. This is author self-review; no independent approval is
    claimed.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain kernel PCA, the original generative topographic mapping model and
  the FastICA algorithm family. Explicitly preserve feature-space kernel validity
  and preimage limits, exact mixture/EM semantics, smoothness versus invertibility,
  and conditional FastICA convergence and robustness. No actionable curation finding
  remains in the three additions.
source:
  git_revision: de8760275471de9fc4e9a36b67fb52ef9d13a499
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
  - path: data/aio/FeatureExtraction.yaml
    sha256: d153b8bbe04e9abb7f1ec13e6219dbcd329235ac58bb9229d4a1f416216c07ef
    role: context
  - path: data/aio/GeneralizedLinearModel.yaml
    sha256: 202002ec50c6e6207bc2fefba5baeab233514fd8f9118a623d1917b599ce2c7d
    role: context
  - path: data/aio/KernelLayer.yaml
    sha256: 0723e7f15d57807a1f922cd87b878593fb167757c7429dd06e99bde723290d43
    role: context
  - path: data/aio/KohonenNetwork.yaml
    sha256: 88932d6b90c0faf268d66f33a580130ec1bcc637650bd05b03c0e24e6714067b
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
  - path: data/aio/MultidimensionalScaling.yaml
    sha256: b8e28ac7a39e438cd6fc6ac93d90f62628d209c84193a72fe88a5cf50d4ef3ff
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
  - path: data/aio/RadialBasisNetwork.yaml
    sha256: 67023f07d0faf5c76e4ef59d1be8b78edf40775223592ab94324607e5403a489
    role: context
  - path: data/aio/RepresentationLearning.yaml
    sha256: bc7af756440437f60210019e17ad1e2dd15cd1c7cbfbc96312520934b7a5c7ca
    role: context
  - path: data/aio/SupportVectorMachine.yaml
    sha256: 0cc2faa913fdafdc539a7d04d08d26c0963f77ad3ca26b833b29ed3ed313e4e0
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/aio/tDistributedStochasticNeighborembedding.yaml
    sha256: 3ffae8e4f79f2959698d8569bf599bca13b08b0e602230e5f1ebb11ef5212822
    role: context
  - path: data/curated/DiffusionMaps.yaml
    sha256: 07a56c43776672a6267a25ba103786e668b36a8ba2d9924d3bac632b36045e44
    role: context
  - path: data/curated/ExpectationMaximization.yaml
    sha256: eab2880f9e6db51aa49135ada0c3f6d1504e947e6f920d0a5913fd7ddbd069c4
    role: context
  - path: data/curated/FastICA.yaml
    sha256: 33f9d6ae1f77a527f66cee5fc6d02ec733660ef7066a186fcdde6f6838f32806
    role: target
  - path: data/curated/GaussianProcessRegression.yaml
    sha256: d83d0de4a152e7db689636928f41eb5d3663281285585d835f2a5535403d6a0d
    role: context
  - path: data/curated/GeneralizedComponentAnalysis.yaml
    sha256: 79ab7923284423c0f542c77deff5f0ce3de898c795d16e930340380b9046a8ff
    role: context
  - path: data/curated/GenerativeTopographicMapping.yaml
    sha256: e91185614eb30867e91a235bbfb97cec1caf03aead662ecee161d2e2780207be
    role: target
  - path: data/curated/InfomaxICA.yaml
    sha256: 9cd4b9da2ef26e210f67fd0daf2f567a32cea4ff26433210008e513711a07a36
    role: context
  - path: data/curated/Isomap.yaml
    sha256: 34e60f41e9f1c8d94cc1b8c869e216e35b409e791291552a4477061c16de46b7
    role: context
  - path: data/curated/KernelPCA.yaml
    sha256: a93227a6b2d6b2b89b679b8f7f9ddd5054741d1c11f9510490d82a3e691a1cab
    role: target
  - path: data/curated/LocallyLinearEmbedding.yaml
    sha256: 621f5e3eb78c5d7ae59dbdc639ed778e52e1845e63e9dbff1922d02220e8e55d
    role: context
  - path: data/curated/MixtureDensityNetwork.yaml
    sha256: 1c6eab5597faff5398e917351cea1b0ab6feca98d690219dc69d44ffe7abba52
    role: context
  - path: data/curated/NonnegativeMatrixFactorization.yaml
    sha256: 3b79c0f7568f3cdc86f5779be7e9c3e2341c547682223e214a6b94031016df7b
    role: context
  - path: data/curated/TopographicICA.yaml
    sha256: 2ade4a230d625874ff765bbb1d44f81fe5e27b4c08f9a9f687b1163b678dc9f1
    role: context
  - path: research/discovery/20261012T020743Z-kernel-and-latent-components.json
    sha256: 3064e8f894b6aaf438cc677d967a6a04f66121ad5aab9536aea7a518d405c084
    role: context
  - path: research/discovery/kernel-and-latent-component-boundaries.py
    sha256: b51d733aa2f4c1f200ec91a29aeae2dc2633d61fcf28ef9a53d586fd146fc4b6
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
- target_id: AIMech:KernelPCA
  path: data/curated/KernelPCA.yaml
  label: Kernel Principal Component Analysis
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/KernelPCA.yaml
    role: maintained
- target_id: AIMech:GenerativeTopographicMapping
  path: data/curated/GenerativeTopographicMapping.yaml
  label: Generative Topographic Mapping
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GenerativeTopographicMapping.yaml
    role: maintained
- target_id: AIMech:FastICA
  path: data/curated/FastICA.yaml
  label: FastICA
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FastICA.yaml
    role: maintained
scope:
  description: All fields of three source-defined kernel and latent-component concepts.
  selection: Exact maintained IDs KernelPCA, GenerativeTopographicMapping and FastICA;
    full selected cohort without sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:KernelPCA
  - AIMech:GenerativeTopographicMapping
  - AIMech:FastICA
  exclusions:
  - target: Contextual AIO and maintained records
    reason: Context informs identity and abstraction boundaries without renewed scientific
      approval or mutation.
  - target: Historical implementations and empirical reproduction
    reason: No source software, classifier fitting, empirical source separation or
      benchmark ran. Curator arithmetic checks bounded mathematical claims only.
  - target: Remaining discovery frontier
    reason: Sixteen new provisional cohorts and 363 pending leads remain, alongside
      other unresolved dispositions. The three named core identities are represented,
      not the whole literature.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:KernelPCA
  - AIMech:GenerativeTopographicMapping
  - AIMech:FastICA
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 119.48s (0:01:59)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 457 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 133 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 130,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:KernelPCA
  - AIMech:GenerativeTopographicMapping
  - AIMech:FastICA
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
  - AIMech:KernelPCA
  - AIMech:GenerativeTopographicMapping
  - AIMech:FastICA
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
  - AIMech:KernelPCA
  - AIMech:GenerativeTopographicMapping
  - AIMech:FastICA
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited 0 with no output.
- check_id: finite-arithmetic
  name: Kernel and latent-component boundaries
  command: python3 research/discovery/kernel-and-latent-component-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:KernelPCA
  - AIMech:GenerativeTopographicMapping
  - AIMech:FastICA
  exit_code: 0
  expected_exit_code: 0
  summary: '{"kernel_pca": {"gram_eigenvalue": 1.0, "covariance_eigenvalue": 0.4999999999999999,
    "test_projection_kernel": 2.1213203435596424, "test_projection_explicit": 2.121320343559642,
    "input_mean": 0.0, "quadratic_feature_mean": 1.0, "feature_mean_required_cross_squared":
    0.5, "tanh_gram_determinant": -0.16826582059019524, "tanh_centered_nonzero_eigenvalue":
    -0.08356585222840096}, "gtm": {"log_likelihood_before": -7.140362161327257, "log_likelihood_after_one_exact_update":
    -4.440645606528282, "new_precision": 6.109470221563882, "normal_equation_max_error":
    6.938893903907228e-18, "folded_map_responsibilities": [0.49999999948471163, 1.0305768101571904e-09,
    0.49999999948471163], "posterior_mean": 0.0}, "fastica": {"zero_kurtosis_source_second_moment":
    0.9999999999999998, "fourth_moment": 2.999999999999999, "two_source_cubic_update":
    [-4.440892098500626e-16, 0.0], "tied_mixed_start_next": [-0.7071067811865476,
    -0.7071067811865476], "untied_ratio_after_update": 0.4218749999999999, "zero_decorrelation_eigenvalue_after_update":
    0.0}, "scope": "Finite synthetic arithmetic only; no author software, training
    or empirical benchmark reproduced."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T020743Z-kernel-and-latent-components.json
  accessed_at: '2026-10-12T02:08:10Z'
  support: supports
  summary: 'Three candidate identities were compared against all 442 pinned AIO IDs,
    labels and scoped synonyms and 454 preceding native IDs, names and aliases, with
    no normalized match. Searches of both complete checkouts included ignored and
    hidden files and returned the same 176 matched-line set across 81 paths. All matching
    excerpts were read and distinguished from existing concept records; historical
    ledgers were not reread in full solely because they contained a match. All 213
    semantic-search rows were read, including 212 unchanged prior rows and the additional
    KernelLayer row. Twenty-one annotated AIO nodes with outgoing edges were inspected:
    19 unchanged prior readings and two new readings. Thirty-one contextual YAMLs,
    including ten native neighbors, comprise 23 unchanged prior readings and eight
    complete readings in this round. This identity assessment is bounded to the pinned
    snapshot and maintained corpus.'
  search_scope: All labels, all scoped synonyms, aliases and IDs normalized for record
    identity; full-text searches of both checkouts include ignored/hidden files. Acronyms
    were checked in the normalized identity comparison; short acronyms were omitted
    from broad substring searches to avoid irrelevant matches.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: 21 annotated CLASS nodes and outgoing edges; all 213 semantic label/synonym
    rows
  accessed_at: '2026-10-12T02:08:10Z'
  support: supports
  summary: 'Kernel PCA maps related to PrincipalComponentAnalysis, preserving its
    kernel feature-space generalization and the pinned task/algorithm distinction.
    KernelLayer denotes a neural layer, not a spectral algorithm, and the source SVM
    is a downstream classifier rather than kernel-PCA identity. GTM maps broadly to
    Model and related to ManifoldLearning: a normalized tied-center latent density
    with posterior visualization is not the Kohonen prototype algorithm, every RBF
    network, or topographic ICA amplitude dependence. FastICA maps related to UnsupervisedLearning,
    not a neural architecture or a preprocessing TrainingStrategy. RepresentationLearning
    is network-scoped in the pin. Native Infomax, topographic ICA, NMF, GCA, EM, MDN,
    GPR, LLE, Isomap and Diffusion Maps contextualize different objectives, model
    laws and geometry; their prior scientific reviews are not renewed by this comparison.'
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261012T020743Z-kernel-and-latent-components.json
  locator: Ten native neighbors and 21 generated contextual YAMLs in source_analysis.context_reading
  accessed_at: '2026-10-12T02:08:10Z'
  support: supports
  summary: Thirty-one contextual YAMLs comprise 23 unchanged prior readings and eight
    complete current readings. Infomax, topographic ICA, NMF, GCA, EM, MDN, GPR, LLE,
    Isomap and Diffusion Maps distinguish estimators, model laws, conditional distributions
    and geometric objectives. Contextual records receive no renewed scientific approval.
- evidence_id: finite-boundaries
  kind: record_content
  reference: research/discovery/kernel-and-latent-component-boundaries.py
  locator: Kernel centering, eigenvalue scaling, projections and PSD; exact GTM update
    and folded posterior; FastICA zero kurtosis, tied starts and rank
  accessed_at: '2026-10-12T02:08:10Z'
  snapshot_sha256: b51d733aa2f4c1f200ec91a29aeae2dc2633d61fcf28ef9a53d586fd146fc4b6
  support: supports
  summary: Kernel and explicit-feature projections agree, with Gram eigenvalue 1 and
    covariance eigenvalue 1/2. Centered inputs need not have centered quadratic features,
    a feature mean need not have a preimage, and the tested tanh similarity has negative
    uncentered determinant and centered eigenvalue. A finite exact GTM update raises
    log likelihood from about -7.1404 to -4.4406 and solves the normal equations to
    floating-point precision. A smooth circular map yields a multimodal latent posterior
    whose mean is nearly unsupported. Two independent finite-support non-Gaussian
    zero-kurtosis sources give a zero original FastICA update, while a tied Rademacher
    start remains mixed up to sign. An untied component ratio obeys the cubic recurrence.
    A zero decorrelation eigenvalue remains zero. These are bounded curator arithmetic
    checks, not author-software or empirical reproduction.
- evidence_id: kernelpca-source-0
  kind: primary_source
  reference: https://alex.smola.org/papers/1998/SchSmoMul98.pdf
  locator: Equation 4.1, printed p. 1305 / PDF p. 7; Appendix B, Equations B.1-B.4
    and test-kernel formula, pp. 1316-1317 / PDF pp. 18-19; Section 2, Equations 2.7-2.15,
    printed pp. 1301-1302 / PDF pp. 3-4; Appendices A-B, pp. 1315-1317 / PDF pp. 17-19;
    curator explicit distinction of Gram and covariance eigenvalues; Section 3, Equation
    3.7, printed p. 1304 / PDF p. 6; Appendix C, Equations C.1-C.3, p. 1317 / PDF
    p. 19; curator finite PSD counterexample; Sections 2-4.1, Equations 2.7-2.15 and
    4.1, printed pp. 1301-1305 / PDF pp. 3-7; Appendix B, pp. 1316-1317 / PDF pp.
    18-19; Sections 4.2-4.5, Figures 1-2 and Equation 4.2, printed pp. 1305-1309 /
    PDF pp. 7-11; Section 6.3.5, pp. 1314-1315 / PDF pp. 16-17
  accessed_at: '2026-10-12T01:53:46Z'
  snapshot_sha256: ac778f1c3740ca0fc9b197b52766d0d99a21435aa718b9d9837c5f39abc511d8
  support: supports
  summary: Nonlinear Component Analysis as a Kernel Eigenvalue Problem. Author-hosted
    final Neural Computation 10(5):1299-1319 (1998) PDF. All 21 pages visually read;
    printed page equals PDF page plus 1298. The 1996 technical report and 1997 acceptance
    date are predecessor metadata, not the publication year. Curator algebraic deductions
    are distinguished from historical empirical results or uninspected software.
- evidence_id: generativetopographicmapping-source-0
  kind: primary_source
  reference: https://www.microsoft.com/en-us/research/wp-content/uploads/1998/01/bishop-gtm-ncomp-98.pdf
  locator: Section 2.1, Equations 15-16, reprint/PDF p. 6; Sections 4.1-4.2, Equations
    21-27 and Figures 6-7, pp. 9-13; curator qualification of the paper’s convergence
    language; Section 2.1, Equations 8-14, reprint/PDF pp. 5-6; Section 2.4, p. 8;
    curator rank, boundary and EM qualifications; Section 2.2, Equations 17-19, reprint/PDF
    p. 6; Sections 2 and 4.2, pp. 4 and 12; curator smooth-map counterexample; Sections
    2-2.1, Equations 1-14, reprint/PDF pp. 3-5; Section 2.4, p. 8; Sections 2-2.1,
    Equations 1-7, reprint/PDF pp. 3-5
  accessed_at: '2026-10-12T01:53:49Z'
  snapshot_sha256: 296ee07618735e368901d1a46d5ad1a78b2fd13fcfa1efc2ea544caba9975af1
  support: supports
  summary: 'GTM: The Generative Topographic Mapping. Microsoft Research author reprint
    of the 1998 Neural Computation 10(1):215-234 article. All 16 PDF pages visually
    read. Locators use the reprint internal pages, which coincide with PDF pages,
    not the journal pagination. Curator algebraic deductions are distinguished from
    historical empirical results or uninspected software.'
- evidence_id: fastica-source-0
  kind: primary_source
  reference: https://www.cs.helsinki.fi/u/ahyvarin/papers/NC97.pdf
  locator: Section 3.1, internal/PDF pp. 5-6; Section 3.1.2, Equation 10, internal/PDF
    p. 6; Section 3.2, Equations 11-15, internal/PDF pp. 6-7; Section 5, p. 9
  accessed_at: '2026-10-12T01:53:54Z'
  snapshot_sha256: 7ab4ef35cb535e952dfc8f5201b5c7796abacdfb3d1cae58212db808de18b149
  support: supports
  summary: A Fast Fixed-Point Algorithm for Independent Component Analysis. Author-hosted
    ten-page preprint marked for Neural Computation 9:1483-1492 (1997). All pages
    visually read. Locators use internal/PDF pages 1-10 rather than assuming the final
    journal layout. Curator algebraic deductions are distinguished from historical
    empirical results or uninspected software.
- evidence_id: fastica-source-1
  kind: primary_source
  reference: https://www.cs.helsinki.fi/u/ahyvarin/papers/TNN99_reprint.pdf
  locator: Appendix A.A, Equations 27-34, printed p. 633 / PDF p. 8; curator finite
    zero-kurtosis and tied-start examples; Section II.B, Equations 6-8, printed p.
    627 / PDF p. 2; Section III.A, Theorems 1-3, p. 628 / PDF p. 3; Section V, pp.
    631-632 / PDF pp. 6-7; Section III.B, Equations 14-16, printed p. 629 / PDF p.
    4; Section IV.B, Equations 17-20, p. 630 / PDF p. 5; Sections IV.B-IV.C, Equations
    20-25, printed pp. 630-631 / PDF pp. 5-6; Sections IV.B-IV.C, Equations 22-26,
    printed pp. 630-631 / PDF pp. 5-6
  accessed_at: '2026-10-12T01:53:56Z'
  snapshot_sha256: a58d27223e2b13dac1feaec6a49b6f439582ecf5105c6a1e9cec81d5b07200c8
  support: supports
  summary: Fast and Robust Fixed-Point Algorithms for Independent Component Analysis.
    Author-hosted final IEEE Transactions on Neural Networks 10(3):626-634, May 1999,
    reprint. All nine PDF pages visually read; printed page equals PDF page plus 625.
    The licensed-download watermark date is not the publication date. Curator algebraic
    deductions are distinguished from historical empirical results or uninspected
    software.
assessments:
- assessment_id: kernelpca
  area: evidence
  topic: Definition, identity, claim support, limitations and AIO mapping direction
  outcome: supported
  target_ids:
  - AIMech:KernelPCA
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - kernelpca-source-0
  summary: 'The Schölkopf-Smola-Müller kernel eigenvalue construction generalizes
    ordinary PCA to a kernel-defined feature space. It includes linear PCA as a special
    case but is not the identity of ordinary input-space PCA, an SVM classifier, a
    dot-product KernelLayer, Isomap, LLE or Diffusion Maps. A trained embedding, chosen
    kernel and preimage approximation are not separate aliases for the algorithm.
    Three candidate identities were compared against all 442 pinned AIO IDs, labels
    and scoped synonyms and 454 preceding native IDs, names and aliases, with no normalized
    match. Searches of both complete checkouts included ignored and hidden files and
    returned the same 176 matched-line set across 81 paths. All matching excerpts
    were read and distinguished from existing concept records; historical ledgers
    were not reread in full solely because they contained a match. All 213 semantic-search
    rows were read, including 212 unchanged prior rows and the additional KernelLayer
    row. Twenty-one annotated AIO nodes with outgoing edges were inspected: 19 unchanged
    prior readings and two new readings. Thirty-one contextual YAMLs, including ten
    native neighbors, comprise 23 unchanged prior readings and eight complete readings
    in this round. This identity assessment is bounded to the pinned snapshot and
    maintained corpus.'
  details: 'For M training points and a positive-semidefinite kernel k, form K_ij=k(x_i,x_j)
    and Kc=H K H with H=I-11^T/M. If Kc v=kappa v, ||v||=1 and kappa>0, coefficients
    alpha=v/sqrt(kappa) define a unit feature-space principal axis. The corresponding
    empirical covariance eigenvalue is kappa/M. Centered rank is at most M-1. Zero
    Gram eigenvalues do not define additional nonzero covariance directions. For a
    new x, center its similarity to each training point using the same training feature
    mean: kc_i(x)=k(x_i,x)-M^(-1)sum_j k(x_j,x)-M^(-1)sum_j K_ij+M^(-2)sum_jl K_jl.
    Its component coordinate is sum_i alpha_i kc_i(x). Centering input coordinates
    before a nonlinear kernel does not generally center the feature vectors; centering
    each test batch independently changes the learned projection. With a fixed valid
    kernel, leading components maximize retained empirical variance and minimize rank-constrained
    squared reconstruction error in the centered feature space. Their sample coordinates
    are uncorrelated, not necessarily statistically independent. They can outnumber
    input dimensions. A linear kernel recovers ordinary PCA with consistent centering.
    Truncated feature reconstructions or principal directions need not have an exact
    input-space preimage, so reconstructing original inputs is a separate problem.
    The feature-space covariance interpretation requires a positive-semidefinite kernel.
    The paper lists sigmoid similarities, but arbitrary tanh parameters do not meet
    that requirement: a curator two-point example k(x,y)=tanh(x*y), x in {1,2}, gives
    a negative Gram determinant and a negative eigenvalue even after centering. Keeping
    selected positive eigenpairs of an indefinite similarity does not establish that
    the original similarity is a Hilbert-space inner product. Limitations: Kernel
    and hyperparameter selection remain modeling decisions. An eigensolution for a
    fixed kernel does not solve all kernel-selection or preimage optimization problems.
    The exact Gram construction requires storage quadratic in training sample count;
    partial eigensolvers, subsets and reduced-set projections are additional approximation
    choices. Implicit features avoid explicit feature-dimension costs, not all sample-size
    costs. Eigenvector signs and bases within degenerate eigenspaces are nonunique.
    Variance and reconstruction guarantees concern the chosen feature space, not causal
    factors, independence, universal input reconstruction or classification accuracy.
    All 21 source pages were inspected. Finite calculations verify centering, eigenvalue
    scaling, projection and PSD boundaries; the historical USPS classifier experiments
    and author implementation were not reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A source-defined feature/source estimator or latent density model;
      not a trained instance.
    evidence_ids:
    - kernelpca-source-0
  - name: aio-assessment
    value: related_match
    definition: 'Kernel PCA maps related to PrincipalComponentAnalysis, preserving
      its kernel feature-space generalization and the pinned task/algorithm distinction.
      KernelLayer denotes a neural layer, not a spectral algorithm, and the source
      SVM is a downstream classifier rather than kernel-PCA identity. GTM maps broadly
      to Model and related to ManifoldLearning: a normalized tied-center latent density
      with posterior visualization is not the Kohonen prototype algorithm, every RBF
      network, or topographic ICA amplitude dependence. FastICA maps related to UnsupervisedLearning,
      not a neural architecture or a preprocessing TrainingStrategy. RepresentationLearning
      is network-scoped in the pin. Native Infomax, topographic ICA, NMF, GCA, EM,
      MDN, GPR, LLE, Isomap and Diffusion Maps contextualize different objectives,
      model laws and geometry; their prior scientific reviews are not renewed by this
      comparison.'
    evidence_ids:
    - mapping
- assessment_id: generativetopographicmapping
  area: evidence
  topic: Definition, identity, claim support, limitations and AIO mapping direction
  outcome: supported
  target_ids:
  - AIMech:GenerativeTopographicMapping
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - generativetopographicmapping-source-0
  summary: 'Scoped to the original fixed-basis GTM construction and its batch EM fitting.
    The shared latent-to-data map ties Gaussian centers and distinguishes the model
    from an unconstrained mixture, a conditional mixture-density network, a Kohonen
    map and topographic ICA energy dependence. Gaussian radial basis functions are
    a usual map choice, not an identity with every radial-basis network. Learned mixture
    weights, heteroscedastic extensions and mixtures of GTMs require separate scope.
    Three candidate identities were compared against all 442 pinned AIO IDs, labels
    and scoped synonyms and 454 preceding native IDs, names and aliases, with no normalized
    match. Searches of both complete checkouts included ignored and hidden files and
    returned the same 176 matched-line set across 81 paths. All matching excerpts
    were read and distinguished from existing concept records; historical ledgers
    were not reread in full solely because they contained a match. All 213 semantic-search
    rows were read, including 212 unchanged prior rows and the additional KernelLayer
    row. Twenty-one annotated AIO nodes with outgoing edges were inspected: 19 unchanged
    prior readings and two new readings. Thirty-one contextual YAMLs, including ten
    native neighbors, comprise 23 unchanged prior readings and eight complete readings
    in this round. This identity assessment is bounded to the pinned snapshot and
    maintained corpus.'
  details: 'Choose K fixed nodes x_i in a latent space of dimension L<D, fixed smooth
    basis vectors phi(x_i), a weight matrix W and shared precision beta>0. Set y_i=W
    phi(x_i) and p(t)=K^(-1)sum_i Normal(t;y_i,beta^(-1)I_D). This finite mixture
    is normalized exactly for finite parameters; the equal node weights do not imply
    a uniform density over the mapped surface. Mixture centers move together through
    W rather than being independent free parameters. For N observations, the E-step
    gives R_in proportional to exp(-beta*||t_n-W phi(x_i)||^2/2), normalized over
    nodes i. With Phi_ij=phi_j(x_i), T containing data rows and G_ii=sum_n R_in, the
    unregularized M-step solves Phi^T G Phi W_new^T=Phi^T R T. Then beta_new^(-1)=(ND)^(-1)sum_ni
    R_in||t_n-W_new phi(x_i)||^2, using the old responsibilities. Exact well-defined
    EM updates make the observed-data log likelihood nondecreasing. Rank deficiency
    can require a pseudoinverse or another weighted least-squares minimizer; zero
    residual variance lies outside the finite-positive-precision model. Bayes responsibilities
    define a posterior distribution over latent nodes for each observation. A posterior-mean
    display uses sum_i R_in x_i; a modal display selects a node with maximum responsibility.
    Multimodal posteriors can make the mean misleading. Smooth forward mapping supports
    local continuity, but does not ensure global injectivity, distance preservation
    or a unique inverse. A curator circular-map example has identical images for separated
    latent nodes and a posterior mean at a nearly unsupported middle node. EM objective
    nondecrease is narrower than an unconditional guarantee of convergence to a local
    maximum or globally optimal density. Gaussian weight regularization changes the
    objective to MAP and changes the normal equations. The original comparisons with
    SOM concern explicit mixture probability, soft responsibilities and tied-center
    regression; they do not establish universal superiority, monotonic posterior concentration
    or biologically correct topology. Limitations: Latent dimension, nodes, basis
    functions and smoothness parameters are modeling choices. The source does not
    establish automatic recovery of the true manifold or globally preserved topology.
    Likelihood fitting is nonconvex and sensitive to initialization and model choice.
    Responsibilities require numerically stable evaluation; exact finite-parameter
    EM statements do not guarantee arbitrary approximate or floating-point implementations.
    The source’s effective regression smoother can have negative entries; it is not
    the posterior responsibility matrix. Its row-sum property relies on the stated
    constant-basis and unregularized algebra. The 16-page author reprint, including
    simulated oil-flow and toy-curve experiments, was read completely. Finite calculations
    check a tiny exact update and a topology boundary; no author software, empirical
    training or benchmark comparison was reproduced.'
  dimensions:
  - name: concept-kind
    value: model_family
    definition: A source-defined feature/source estimator or latent density model;
      not a trained instance.
    evidence_ids:
    - generativetopographicmapping-source-0
  - name: aio-assessment
    value: broad_match,related_match
    definition: 'Kernel PCA maps related to PrincipalComponentAnalysis, preserving
      its kernel feature-space generalization and the pinned task/algorithm distinction.
      KernelLayer denotes a neural layer, not a spectral algorithm, and the source
      SVM is a downstream classifier rather than kernel-PCA identity. GTM maps broadly
      to Model and related to ManifoldLearning: a normalized tied-center latent density
      with posterior visualization is not the Kohonen prototype algorithm, every RBF
      network, or topographic ICA amplitude dependence. FastICA maps related to UnsupervisedLearning,
      not a neural architecture or a preprocessing TrainingStrategy. RepresentationLearning
      is network-scoped in the pin. Native Infomax, topographic ICA, NMF, GCA, EM,
      MDN, GPR, LLE, Isomap and Diffusion Maps contextualize different objectives,
      model laws and geometry; their prior scientific reviews are not renewed by this
      comparison.'
    evidence_ids:
    - mapping
- assessment_id: fastica
  area: evidence
  topic: Definition, identity, claim support, limitations and AIO mapping direction
  outcome: supported
  target_ids:
  - AIMech:FastICA
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - fastica-source-0
  - fastica-source-1
  summary: 'Scoped to Hyvarinen-Oja 1997 kurtosis FastICA and Hyvarinen 1999 generalized
    contrasts. This is an estimation algorithm, not the general ICA model, a trained
    source separator, ordinary-gradient Infomax ICA, topographic ICA or every fixed-point
    optimizer. Deflation and symmetric variants share the core update but have distinct
    ordering and decorrelation behavior; optional stabilization is not a claim that
    every variant is step-size-free. Three candidate identities were compared against
    all 442 pinned AIO IDs, labels and scoped synonyms and 454 preceding native IDs,
    names and aliases, with no normalized match. Searches of both complete checkouts
    included ignored and hidden files and returned the same 176 matched-line set across
    81 paths. All matching excerpts were read and distinguished from existing concept
    records; historical ledgers were not reread in full solely because they contained
    a match. All 213 semantic-search rows were read, including 212 unchanged prior
    rows and the additional KernelLayer row. Twenty-one annotated AIO nodes with outgoing
    edges were inspected: 19 unchanged prior readings and two new readings. Thirty-one
    contextual YAMLs, including ten native neighbors, comprise 23 unchanged prior
    readings and eight complete readings in this round. This identity assessment is
    bounded to the pinned snapshot and maintained corpus.'
  details: 'For centered whitened observations x with E[xx^T]=I and unit w, choose
    a differentiable nonlinearity g=Gprime and compute w_plus=E[x*g(w^T x)]-E[gprime(w^T
    x)]*w, then normalize its nonzero norm. The source derives this from an approximate
    Newton step for a constrained projection contrast; sample means replace expectations
    in practice. Cubic g(u)=u^3 gives the original kurtosis step E[x(w^T x)^3]-3w
    under the whitening and unit-norm conditions. Tanh and Gaussian-weighted-linear
    nonlinearities are other source choices. Deflation subtracts projections on previously
    estimated orthonormal directions after each update and renormalizes. Symmetric
    FastICA updates rows together and applies W <- (W W^T)^(-1/2)W for whitened data,
    requiring full row rank. For nonsphered data, the source uses covariance-metric
    normalization and decorrelation with nonsingular covariance. Orthogonality prevents
    exact duplicate directions but does not by itself prove statistical independence.
    Signs and component ordering are not identified by the ICA objective. The generalized
    proof assumes the linear independent-source model, exact expectations, suitable
    moments and E[s_i*g(s_i)-gprime(s_i)] nonzero. It establishes local convergence
    near a source direction, generally quadratic and cubic with the stated symmetry
    condition. For the original kurtosis rule, source-coordinate updates are proportional
    to kurt(s_i)*z_i^3. A unique dominant scaled initial coordinate yields the cubic
    ratio contraction; tied starts can remain mixed up to sign. A source can be non-Gaussian
    with zero kurtosis, so the kurtosis rule cannot resolve multiple such sources
    merely from their non-Gaussianity. The squared contrast [E G(w^T x)-E G(v)]^2,
    with standard Gaussian v, approximates negentropy rather than giving exact entropy
    for arbitrary distributions. Contrast choice affects consistency conditions, estimation
    variance and sensitivity to outliers. The robustness theorem assumes robust whitening
    and explicitly does not give a globally bounded influence function. The reported
    outlier experiment estimates covariance from uncontaminated data to emulate robust
    whitening; it does not certify robustness of an arbitrary complete FastICA pipeline.
    Limitations: Standard source identification assumes an appropriate full-rank instantaneous
    linear mixture, independent sources and at most one Gaussian source; the usable
    contrasts additionally require their own moments and nondegeneracy. Whitening
    needs finite covariance and a retained full-rank subspace. A zero fixed-point
    update cannot be normalized. Singular intermediate matrices cannot be repaired
    to full rank by the displayed symmetric inverse square root or iterative decorrelation
    formula. Finite-sample errors and model mismatch are outside the exact-expectation
    convergence proof. The original sign-insensitive stopping criterion can declare
    a mixed tied-start direction unchanged. Finite counterexamples qualify blanket
    recovery claims; they do not establish typical failure rates for randomized practical
    implementations. Optional stabilized, nonsphered, noisy and overcomplete variants
    need their stated assumptions. The core algorithm is not universally globally
    convergent, noise-consistent, step-size-free in all variants, or superior to other
    estimators. Both primary PDFs were read completely, totaling 19 pages. Finite
    arithmetic verifies zero-kurtosis and tied-start boundaries; no source-separation
    training, author implementation or historical benchmark was reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A source-defined feature/source estimator or latent density model;
      not a trained instance.
    evidence_ids:
    - fastica-source-0
    - fastica-source-1
  - name: aio-assessment
    value: related_match
    definition: 'Kernel PCA maps related to PrincipalComponentAnalysis, preserving
      its kernel feature-space generalization and the pinned task/algorithm distinction.
      KernelLayer denotes a neural layer, not a spectral algorithm, and the source
      SVM is a downstream classifier rather than kernel-PCA identity. GTM maps broadly
      to Model and related to ManifoldLearning: a normalized tied-center latent density
      with posterior visualization is not the Kohonen prototype algorithm, every RBF
      network, or topographic ICA amplitude dependence. FastICA maps related to UnsupervisedLearning,
      not a neural architecture or a preprocessing TrainingStrategy. RepresentationLearning
      is network-scoped in the pin. Native Infomax, topographic ICA, NMF, GCA, EM,
      MDN, GPR, LLE, Isomap and Diffusion Maps contextualize different objectives,
      model laws and geometry; their prior scientific reviews are not renewed by this
      comparison.'
    evidence_ids:
    - mapping
- assessment_id: kernel-geometry
  area: consistency
  topic: Feature centering, spectral normalization and preimages
  outcome: supported
  target_ids:
  - AIMech:KernelPCA
  evidence_ids:
  - kernelpca-source-0
  - finite-boundaries
  - neighbors
  summary: Retain the kernel feature-space interpretation with its conditions.
  details: The explicit quadratic feature and centered-kernel computations agree.
    Gram eigenvalue kappa and covariance eigenvalue kappa/M are kept distinct. Training
    feature means are reused for unseen points; input centering is insufficient for
    nonlinear features. The finite tanh Gram matrix is indefinite even after centering,
    and a quadratic feature mean need not have an input preimage. Variance and reconstruction
    guarantees do not imply independent factors, input reconstruction or classifier
    superiority.
- assessment_id: gtm-density-and-fitting
  area: consistency
  topic: Normalized latent mixture and exact EM
  outcome: supported
  target_ids:
  - AIMech:GenerativeTopographicMapping
  evidence_ids:
  - generativetopographicmapping-source-0
  - finite-boundaries
  - neighbors
  summary: Retain the original equal-weight, shared-variance, tied-center model.
  details: The finite normalized mixture uses a discrete latent prior, not an unnormalized
    product or generic conditional MDN. Exact responsibilities and weighted normal
    equations yield the stated variance update. Finite arithmetic increases log likelihood
    and satisfies normal equations; it does not prove arbitrary numerical implementations,
    global optimality or unconditional local-maximum convergence. Rank deficiency
    and zero residual variance require explicit treatment, and MAP regularization
    changes the objective.
- assessment_id: gtm-posterior-and-topology
  area: consistency
  topic: Forward smoothness versus latent inversion
  outcome: supported
  target_ids:
  - AIMech:GenerativeTopographicMapping
  evidence_ids:
  - generativetopographicmapping-source-0
  - finite-boundaries
  - mapping
  summary: Preserve multimodal posterior and noninjective-map limitations.
  details: A circle-valued smooth map with nonzero derivative identifies separated
    latent nodes. At the shared image, the posterior mean lies at a nearly unsupported
    middle node. Thus continuity and local rank do not establish a globally invertible
    embedding. GTM posterior responsibilities differ from the signed effective regression
    smoother, the Kohonen hard winner and topographic ICA component-energy neighborhoods.
- assessment_id: fastica-convergence
  area: consistency
  topic: Exact-expectation contraction, zero kurtosis and rank
  outcome: supported
  target_ids:
  - AIMech:FastICA
  evidence_ids:
  - fastica-source-0
  - fastica-source-1
  - finite-boundaries
  summary: Keep convergence claims conditional and source-version specific.
  details: The generalized rule is an approximate-Newton constrained-contrast iteration.
    Its local proof requires the independent linear model, exact expectations, suitable
    moments and nonzero source contrast factors. The original cubic update has zero
    output for two independent non-Gaussian zero-kurtosis sources; a tied Rademacher
    initialization stays mixed up to sign. An untied ratio follows cubic contraction.
    These exceptional finite examples do not establish practical failure frequencies.
    Symmetric inverse square roots and iterative decorrelation cannot restore missing
    row rank.
- assessment_id: fastica-robustness
  area: consistency
  topic: Approximate negentropy and preprocessing assumptions
  outcome: supported
  target_ids:
  - AIMech:FastICA
  evidence_ids:
  - fastica-source-1
  - finite-boundaries
  summary: Retain restricted contrast and robustness claims.
  details: The contrast is an approximation to negentropy. The primary robustness
    theorem assumes robust whitening and does not give a globally bounded influence
    function; the outlier experiment estimates covariance from the uncontaminated
    observations. Batch FastICA, adaptive Hebbian rules, stabilized variants and noise/overcomplete
    extensions are not interchangeable. No unqualified robustness, speed or empirical
    source-recovery claim is asserted.
- assessment_id: evidence-and-mapping-scope
  area: grounding
  topic: Primary versions and mapping abstraction
  outcome: supported
  target_ids:
  - AIMech:KernelPCA
  - AIMech:GenerativeTopographicMapping
  - AIMech:FastICA
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - kernelpca-source-0
  - generativetopographicmapping-source-0
  - fastica-source-0
  - fastica-source-1
  summary: Preserve distinct concepts and bounded historical evidence.
  details: 'Kernel PCA maps related to PrincipalComponentAnalysis, preserving its
    kernel feature-space generalization and the pinned task/algorithm distinction.
    KernelLayer denotes a neural layer, not a spectral algorithm, and the source SVM
    is a downstream classifier rather than kernel-PCA identity. GTM maps broadly to
    Model and related to ManifoldLearning: a normalized tied-center latent density
    with posterior visualization is not the Kohonen prototype algorithm, every RBF
    network, or topographic ICA amplitude dependence. FastICA maps related to UnsupervisedLearning,
    not a neural architecture or a preprocessing TrainingStrategy. RepresentationLearning
    is network-scoped in the pin. Native Infomax, topographic ICA, NMF, GCA, EM, MDN,
    GPR, LLE, Isomap and Diffusion Maps contextualize different objectives, model
    laws and geometry; their prior scientific reviews are not renewed by this comparison.
    All 56 primary pages were visually read, with source-specific pagination. Author-paper
    PDFs, preprints and journal versions are named accurately; access and publication
    dates are distinct. Historical USPS, oil-flow and source-separation examples are
    not new benchmark results.'
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:KernelPCA
  - AIMech:GenerativeTopographicMapping
  - AIMech:FastICA
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-boundaries
  - kernelpca-source-0
  - generativetopographicmapping-source-0
  - fastica-source-0
  - fastica-source-1
  rationale: Kernel spectral feature extraction, a tied-center latent probability
    model and fixed-point independent-component estimation have distinct defining
    objects and operations. Source versions within FastICA form one supported algorithm
    family with explicit variants. Model/task and algorithm/task mappings preserve
    abstraction.
limitations:
- Adversarial author self-review only; all three records remain DRAFT.
- 'All 56 PDF pages were visually read: kernel PCA21, GTM16, original FastICA10 and
  generalized FastICA9. Preprint/reprint pagination is recorded separately from final
  journal pagination. Earlier truncated page displays and context reads were reopened.'
- Source URLs, versions, actual UTC access times and byte hashes are retained. Search/open
  captures describe discovery provenance, not inspection of every returned link. No
  full PDFs are redistributed in this change.
- Kernel validity, feature-space centering, Gram/covariance scaling and preimage limitations
  are explicit. The sigmoid example does not establish a PSD kernel for arbitrary
  parameters.
- GTM is an exactly normalized finite mixture with a fixed latent prior and tied centers.
  Smoothness is not global invertibility, and exact EM nondecrease is not an unconditional
  convergence-to-local-maximum theorem.
- FastICA preserves the distinction between the original cumulant rule, generalized
  approximate-negentropy contrasts and their practical variants. Exact-expectation,
  moment, nondegeneracy, rank and robust-whitening assumptions remain explicit.
- No author implementation, empirical training or benchmark was run. Finite synthetic
  calculations do not establish performance or typical failure rates.
- Three DRAFT additions and sixteen provisional new cohorts leave 363 pending leads
  plus other unresolved dispositions. No global saturation is claimed.
links: []
tags:
- native-concepts
- kernel-and-latent-components
- self-review
- discovery-ongoing
```
