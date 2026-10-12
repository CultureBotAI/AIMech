# Successor author review of corrected mixed-model primary locators

- Review: 20261012T235356Z-loss-smoothed-mixed-model-resolved
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T23:50:25Z
- Finished UTC: 2026-10-12T23:53:56Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The minor finding affecting three primary-source locators is resolved. Model, family and variance-coordinate citations now identify the inspected supporting passages. All mechanism statements, identity, mapping and source qualifications remain unchanged; DRAFT remains.

## Scope And Provenance

All maintained fields and primary support of the exact base loss-smoothed mixed-model inference record.

Selection: Exact maintained ID: AIMech:GaussianLossSmoothedMixedModelVariationalInference
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 998c081823d41d0ac90369903c57dffd21b14452.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:GaussianLossSmoothedMixedModelVariationalInference | data/curated/GaussianLossSmoothedMixedModelVariationalInference.yaml | maintained | Gaussian loss-smoothed mixed-model variational inference |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:GaussianLossSmoothedMixedModelVariationalInference | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 105.03s (0:01:45)<br>Checked 442 record(s); 0 failed.<br>Checked 554 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 204 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 202,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:GaussianLossSmoothedMixedModelVariationalInference | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:GaussianLossSmoothedMixedModelVariationalInference | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:GaussianLossSmoothedMixedModelVariationalInference | Exited 0 without output. |
| Unchanged independent loss-convolution and fixed-state arithmetic | passed | True | AIMech:GaussianLossSmoothedMixedModelVariationalInference | {"quantile": {"analytic": [0.626652376470149, -0.5413447460685429, 0.3024634056489292], "hermite_quadrature": [0.6266523764701492, -0.5413447460681581, 0.3024634056494104], "max_error": 4.811706588725428e-13}, "mixed_model_state": {"predictor_means": [0.4, 0.25, 0.09999999999999998], "predictor_variances": [1.1600000000000001, 1.07, 3.6799999999999997], "variance_factor_shape": 2.5, "variance_factor_rate": 1.3965, "expected_inverse_variance": 1.790189760114572, "proposal_precision": [[1.13034988866348, 0.23673567405060184], [0.23673567405060184, 3.4659958774257165]], "proposal_covariance": [[0.8975208172260317, -0.06130278371775282], [-0.06130278371775282, 0.2927044900521073]], "proposal_mean": [0.7400915336851399, 0.20769274720273945], "natural_and_newton_form_max_difference": 1.1102230246251565e-16}, "source_precision_sign": {"correct": 1.25, "printed": -0.75}, "uniform_convergence_counterexample": {"nu": 0.1, "values": [{"xi": 0, "difference": 0.0050125208594010645}, {"xi": 5, "difference": 0.7439240558112742}, {"xi": 10, "difference": 110.40811925535272}], "argument": "Difference exp(xi)*(exp(nu\u00b2/2)-1) has infinite supremum over real xi for each nu&gt;0."}, "package_hinge_derivative": {"finite_difference_of_psi0": -0.8734510455188359, "correct": -0.8734510455264423, "statically_transcribed_psi1": -1.7469020910528845}, "scope": "One supplied Gaussian/IG state and finite quadratures; not an iterative fit, author-code execution, convergence test or empirical benchmark."} |

## Scientific And Domain Assessments

### Loss-smoothed full-Gaussian mixed-model procedure

identity: supported. Targets: AIMech:GaussianLossSmoothedMixedModelVariationalInference.

Retain the distinct base procedure with a descriptive local name.

The generalized mixed-model target, full fixed/random-coefficient factor, independent inverse-gamma variance factors, Gaussian loss convolution and specified natural-proposal schedule are more specific than generic NCVMP or mean-field families. BBVI uses sampling-based gradients; the preceding shared-spectral method has uncertain nonlinear spectral parameters and different scale factors. NCVB-UF is the source-specific Algorithm 1 designation. Revised arXiv titles are one version history, not multiple concepts. Projected/stochastic extensions remain outside scope.

### Inference-to-random-effects context

grounding: supported. Targets: AIMech:GaussianLossSmoothedMixedModelVariationalInference.

A related mapping preserves abstraction level.

Random-effect blocks and inferred variance parameters define this procedure’s modeling context. The pinned RandomEffectsModel class does not identify its variational schedule and is not asserted equivalent or superclass. Conventional GLMs need not include arbitrary generalized losses; regression is only one application; SVM does not follow from sharing a loss; PGM/BayesianNetwork are broader structural context, and VAE is a different neural architecture.

### generalized-target

evidence: supported. Targets: AIMech:GaussianLossSmoothedMixedModelVariationalInference.

The statement and corrected citation are supported under the explicit domain.

For observations y_i and design rows c_i^T, let theta=(beta,u_1,...,u_H) and eta_i=c_i^T*theta. The unit-loss generalized posterior is proportional to exp(-sum_i psi(y_i,eta_i)) times the prior: beta~N(0,sigma_beta^2*R_beta^-1), u_h&#124;s_h~N(0,s_h*R_h^-1) and independent s_h~IG(A_h,B_h). Here sigma_beta^2,A_h,B_h are positive, each R is positive definite, and IG(A,B) has density proportional to s^(-A-1)*exp(-B/s), s&gt;0. These proper-prior and positive-definite assumptions delimit this record; an intrinsic singular Gaussian requires separate constraints. An arbitrary loss defines a generalized target, not automatically a normalized sampling likelihood. Assume its normalizing constant Z is finite and positive; a finite nonnegative loss with these proper priors suffices.

### factor-family-objective

evidence: supported. Targets: AIMech:GaussianLossSmoothedMixedModelVariationalInference.

The statement and corrected citation are supported under the explicit domain.

Use q(theta)=N(mu,Sigma) with a full positive-definite covariance, independently of q(s_h)=IG(alpha_h,b_h) for each random-effect variance. Dependence among fixed and random coefficients is retained; dependence between theta and the variances, and between the variance factors, is omitted. The variational objective is L=E_q[log unnormalized_target]-E_q[log q], a lower bound on log Z under the proper-target and finite-expectation conditions. It does not assert a normalized-data-likelihood evidence for arbitrary losses. This is the unconstrained Gaussian factorization called NCVB-UF in the source, not its further block-factorized Gaussian projections.

### gaussian-loss-smoothing

evidence: supported. Targets: AIMech:GaussianLossSmoothedMixedModelVariationalInference.

The statement and corrected citation are supported under the explicit domain.

At current Gaussian moments, xi_i=c_i^T*mu and nu_i^2=c_i^T*Sigma*c_i. For nu_i&gt;0 define Psi0_i=E[psi(y_i,xi_i+nu_i*Z0)] with Z0~N(0,1), and Psi1_i and Psi2_i as its first and second xi derivatives. Under dominated differentiation, for example a measurable loss of at most polynomial growth, these equal E[Z0*psi]/nu_i and E[(Z0^2-1)*psi]/nu_i^2. Thus nondifferentiable losses can give smooth Gaussian expected losses through one-dimensional expectations, with analytic forms for some losses and quadrature for others. These identities concern positive nu and the stated integrability conditions; they are not a blanket global uniform-convergence theorem or a rule for substituting nu=0.

### variance-coordinates

evidence: supported. Targets: AIMech:GaussianLossSmoothedMixedModelVariationalInference.

The statement and corrected citation are supported under the explicit domain.

Holding current q(theta) fixed, each exact inverse-gamma coordinate has alpha_h=A_h+d_h/2 and b_h=B_h+(mu_h^T*R_h*mu_h+tr(R_h*Sigma_hh))/2, where d_h is the random-effect block size. Therefore E_q[1/s_h]=alpha_h/b_h. The expected prior precision Rbar is block diagonal, with beta block R_beta/sigma_beta^2 and random block (alpha_h/b_h)*R_h. Positive prior parameters and positive-definite R make these factors proper and Rbar positive definite. These exact variance-factor coordinates do not make the coupled full posterior exact.

### gaussian-natural-proposal

evidence: supported. Targets: AIMech:GaussianLossSmoothedMixedModelVariationalInference.

The statement and corrected citation are supported under the explicit domain.

In the base full-data cycle, compute xi,nu and Psi1,Psi2 from the old mu,Sigma; update the variance factors from those old Gaussian moments; then use their new Rbar. Set W=diag(Psi2), P=Rbar+C^T*W*C and h=C^T*(W*xi-Psi1). If P is positive definite, propose Sigma_new=P^-1 and mu_new=Sigma_new*h, equivalently mu_new=mu+Sigma_new*g with g=-C^T*Psi1-Rbar*mu. This uses the plus curvature sign from Proposition 2 and Appendix A2, correcting the inconsistent minus sign in printed Algorithm 1. For convex losses with nonnegative smoothed curvature, positive-definite Rbar makes P positive definite. The h form avoids dividing by individual zero curvature entries. It is a Gaussian NCVMP fixed-point/natural proposal, not an exact Gaussian-family maximizer or a general bound-ascent guarantee; recompute moments after changing q(theta).

### pinball-loss-example

evidence: supported. Targets: AIMech:GaussianLossSmoothedMixedModelVariationalInference.

The statement and corrected citation are supported under the explicit domain.

For the unscaled pinball loss psi(y,eta)=(y-eta)*(tau-1[y&lt;eta]), 0&lt;tau&lt;1, set z=(y-xi)/nu with nu&gt;0. With phi and Phi the standard normal density and cumulative distribution, Psi0=nu*(phi(z)+z*(Phi(z)-1+tau)), Psi1=1-tau-Phi(z), and Psi2=phi(z)/nu. This concrete Gaussian convolution supplies the gradient and nonnegative curvature used by the base mixed-model update without differentiating the loss at its kink. The scaling is part of the generalized target; multiplying a loss by a constant generally changes that target relative to its prior.

### implementation-boundary

evidence: supported. Targets: AIMech:GaussianLossSmoothedMixedModelVariationalInference.

The statement and corrected citation are supported under the explicit domain.

In the inspected package psifun SVC method, the expected hinge loss psi0 has the unscaled Gaussian-convolution form, while psi1 and psi2 use twice its corresponding derivatives (apart from numeric clipping). They therefore do not consistently describe derivatives of that same psi0. This is a static source inconsistency, not a measured runtime or benchmark result, and does not alter the unscaled pinball formulas curated here.

### Generalized normalization and proper priors

consistency: supported. Targets: AIMech:GaussianLossSmoothedMixedModelVariationalInference.

The target and Gaussian domains are appropriately delimited.

The record conditions on a finite positive generalized normalizer and well-defined expectations. For finite nonnegative loss, exp(-sum loss) is positive and at most one under a proper prior, so its expectation is in (0,1]. The ELBO bounds log Z, without inventing a normalized observation likelihood. SPD prior matrices delimit ordinary proper Gaussians despite the source PSD wording. Shape/rate and expected inverse variance use the variance variable s_h, not the standard deviation. Source bound-display inconsistencies do not enter the defining objective.

### Frozen loss moments and new variance precision

consistency: supported. Targets: AIMech:GaussianLossSmoothedMixedModelVariationalInference.

The qualified plus-curvature proposal follows the expected-log-target Hessian.

Source Algorithm 1 computes old predictor moments, updates IG factors from old coefficient moments, then applies the Gaussian proposal using new expected prior precision. P=Rbar+C^T diag(Psi2) C, and P*mu+g=C^T(W*xi-Psi1), so the natural and Newton forms agree. With convex losses and SPD prior precision, P is SPD. The calculator verifies one 2-coefficient state and exposes the printed minus-sign failure for a quadratic loss. This does not establish iterative ascent or convergence, nor certify a differently scheduled package.

### Nonsmooth losses and explicit regularity

consistency: supported. Targets: AIMech:GaussianLossSmoothedMixedModelVariationalInference.

The derivative identities and pinball normalization are internally consistent.

Differentiating the Gaussian kernel gives the first two Hermite moments for positive nu under domination. Polynomial growth is a sufficient condition, not a copied blanket theorem. Split quadrature around the pinball kink agrees within 4.9e-13 for the supplied case. The exponential-loss counterexample shows that Gaussian integrability/convexity alone do not imply global uniform convergence. Zero variance is excluded from the divided Hermite expressions; h avoids a separate division by zero Psi2. No doubled hinge/SVR formula is imported.

### Static implementation evidence does not certify paper fidelity

provenance: supported. Targets: AIMech:GaussianLossSmoothedMixedModelVariationalInference.

The selected package inconsistency is accurately and narrowly stated.

The complete _psi SVC method has unscaled psi_0 but doubled psi_1 and psi_2 for ordinary +/-1 labels, apart from clipping. A finite derivative of its statically transcribed unscaled expression distinguishes the factor of two; no Julia call was executed. The record distinguishes post-v5 package changes, observation-scale factors and controls from the base unit-loss procedure. Its source URL/hash identify the exact file; the broader downloaded/read scopes are preserved in the report.

### Complete maintained record, report mirror and source provenance

provenance: supported. Targets: AIMech:GaussianLossSmoothedMixedModelVariationalInference.

All maintained fields were read; DRAFT remains.

Assessed stable ID/name/source alias, algorithm kind, definition, identity context, all seven statements/citations, both source identities/authors/versions/access/hash, unchanged AIO snapshot and related mapping, six limitations and real timestamps. All source bytes, context hashes and the exact report mirror agree. Primary PDF and ten selected package files were read; journal PDF/supplement and package runtime remain unassessed. The formula, projection and empirical-context caveats prevent unsupported performance claims. The three citation locators are now corrected; full-field comparison confirms all statements, identity, mapping and limitations unchanged apart from the real updated timestamp.

### Claim-specific primary locators

evidence: supported. Targets: AIMech:GaussianLossSmoothedMixedModelVariationalInference.

All three primary locators now point to the supporting model, family and variance passages.

The generalized target is Equation1/PDF3, Gaussian/IG factorization Equation3/PDF5, alternative factorization Section3.1/PDF9, and IG coordinate Proposition2/PDF6/AppendixA2/PDF17. Corrected citations preserve the supported statements, qualified Gaussian natural step and source limitations. Full-field comparison with the published initial record confirms the bounded change.

## Findings

### F1: Correct three primary-source locators in the loss-smoothed inference record

minor / resolved / confirmed; issue key: aimech-loss-smoothed-primary-locators.

The generalized-target, factor-family-objective and variance-coordinates claims contain incorrect equation/section references. The model is Equation1/PDF3, the family Equation3/PDF5 with Section3.1/PDF9 for alternative factorizations, and IG coordinates Proposition2/PDF6 and AppendixA2/PDF17. Correct the locators and mirror the record in the discovery report; the statements and mathematical qualifications are supported and need no change.

Disposition: The generalized-target locator now identifies Equation1/Section2/PDF3–4; factor-family-objective identifies the objective on PDF4, family Equation3/PDF5 and Section3.1/PDF9; variance-coordinates identifies Proposition2/PDF5–6, AppendixA2/PDF17 and Algorithm1/PDF26. The relevant source pages were visually verified, and full-field comparison shows only these three locators and the actual updated timestamp changed. Report/page synchronization and required checks pass.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T234243Z-loss-smoothed-mixed-model-inference.json | supports | No normalized identity match across all 442 pinned AIO IDs, labels and scoped synonyms and 553 maintained IDs, names and aliases. Ignored- and hidden-inclusive fixed-string searches of the recovery, old discovery and original Documents checkouts returned 30, 0 and 0 lines, all 30 read: prior source leads and contextual references, without a matching record. Assessed all 33 semantic AIO rows and 113 native names/definitions, seven complete annotated AIO nodes with incident edges/generated YAML and five complete native context records. Gaussian loss-smoothed mixed-model variational inference is a descriptive local name for the base unconstrained-Gaussian NCVB-UF procedure in Castiglione and Bernardi Algorithm 1, with the precision sign qualified against Proposition 2 and Appendix A2. Its unit-loss generalized target, one-dimensional Gaussian loss smoothing, full fixed/random-effect covariance and inverse-gamma variance coordinates distinguish it from generic NCVMP, BBVI, generic mean-field families and the shared-spectral regression procedure. NCVB-UF is a source-specific algorithm designation, not a claim that all nonconjugate variational Bayes is this method. Older titles of arXiv:2206.09444 are the same source version history. Projected and stochastic extensions are separate pending scope. Absence is bounded to this pin and inspected corpus. |
| mapping | sources/aio/aio.json | supports | All 33 semantic AIO rows, 113 native definitions, seven complete AIO nodes/incident edges/generated YAML and five complete native context records were assessed in preparation. The related random-effects mapping distinguishes algorithm from model context; all captured bytes remain unchanged. |
| calculation | research/discovery/loss-smoothed-mixed-model-boundaries.py | supports | Independent finite pinball/Hermite quadrature, one supplied full Gaussian and inverse-gamma state, and equivalent natural/Newton Gaussian forms. Explicit counterexamples expose a source precision sign and global uniform-convergence overstatement; static hinge expressions expose a package derivative mismatch. No fitting loop, author implementation execution, or benchmark. |
| castiglione2025 | https://arxiv.org/pdf/2206.09444v5; Section 2, Equation 1, PDF p. 3; Sections 2.1–2.3, Equations 2–6 and Propositions 2–3, PDF pp. 4–6; Section 3.1, PDF p. 9; Appendix A1–A3, PDF pp. 16–20; B3, PDF p. 24; Algorithm 1, PDF p. 26 | supports | arXiv:2206.09444v5, revised 2025-10-13; all 41 PDF pages inspected. DOI 10.1080/10618600.2025.2527925 identifies the journal article; its full text and reproduction supplement were not inspected. All 41 pages visually read during preparation; after capture reread PDF pp. 3–6,9,16–18,24,26 against the exact full YAML. |
| bayesglmm-psifun | https://raw.githubusercontent.com/CristianCastiglione/BayesGLMM.jl/15ce3551f62b0dfb5a54a6bc455deb1cb6966b34/src/psifun.jl; _psi(...,f::SVC,...) and _psi(...,f::Quantile,...) in the complete src/psifun.jl file | supports | Commit 15ce3551f62b0dfb5a54a6bc455deb1cb6966b34, dated 2025-11-04; complete selected source file statically inspected, not executed. Package as a whole not certified. Complete selected source file statically reread after capture; no Julia execution. Ten package files read during preparation, not the whole package. |
| locator-defect | data/curated/GaussianLossSmoothedMixedModelVariationalInference.yaml | supports | Three corrected locators now identify model Equation1, family Equation3/Section3.1, and variance coordinates Proposition2/AppendixA2. After successor capture, visually reread PDF3,5,9,17; PDF4,6,26 were verified in the initial full review. All statements remain unchanged and the report/page agree. |
| predecessor | reviews/structured/20261012T234720Z-loss-smoothed-mixed-model-open/review.yaml | context_only | Immutable initial full scientific review records minor locator finding F1 and the maintained owner. Its captured source base predates the unrelated two-file Pages deployment change; all scientific inputs survived integration unchanged. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- The sole minor citation finding is resolved with explicit predecessor linkage. Source-level formula, convergence and implementation caveats remain explicit.
- The initial publication guard detected the independently merged Pages workflow and .nojekyll changes at8390491ea3f6cd3950482ef71350c2715efdbc7c. They were inspected and integrated by rebase; all scientific review inputs remained unchanged. Post-correction gates ran on the integrated branch.
- Added one DRAFT algorithm, yielding 554 native and 442 unchanged generated records. The 739-entry main frontier retains 484 pending and 57 partly addressed cohorts; nested source inventories also remain incomplete.
- All 41 arXiv v5 pages were visually read. The full journal article and reproduction supplement were not accessed; journal landing-page access returned HTTP 403. Independent finite quadrature and a single supplied Gaussian/IG state check derivative and update algebra, not iterative fitting, convergence or accuracy. No empirical performance claim is made; inconsistencies in the source experiment descriptions and table contexts are retained in the discovery report. DRAFT remains.
- The author-linked BayesGLMM.jl snapshot 15ce3551f62b0dfb5a54a6bc455deb1cb6966b34 postdates arXiv v5. Ten selected files were statically read, with no Julia execution. Its added observation-scale factors, update order and step controls differ from the base target; its SVC expected-loss derivatives are inconsistent with its own unscaled expected loss. This package was not used to certify Algorithm 1 fidelity. The remaining package and journal reproduction supplement were not fully inspected.
- Source pseudocode, normalization, convergence, projection and empirical-context discrepancies are explicitly retained rather than treated as implementation fidelity or general superiority. No upstream paper/package correction was requested or performed.
- Original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection; isolated recovery work only.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T235356Z-loss-smoothed-mixed-model-resolved
kind: record
repository: CultureBotAI/AIMech
title: Successor author review of corrected mixed-model primary locators
started_at: '2026-10-12T23:50:25Z'
finished_at: '2026-10-12T23:53:56Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author reread the corrected locators and supporting primary
    pages after capture, compared every field with the initial commit, verified report/page
    synchronization and reran required checks. This is author self-review, not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The minor finding affecting three primary-source locators is resolved. Model,
  family and variance-coordinate citations now identify the inspected supporting passages.
  All mechanism statements, identity, mapping and source qualifications remain unchanged;
  DRAFT remains.
source:
  git_revision: 998c081823d41d0ac90369903c57dffd21b14452
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/GeneralizedLinearModel.yaml
    sha256: 202002ec50c6e6207bc2fefba5baeab233514fd8f9118a623d1917b599ce2c7d
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
  - path: data/aio/SupportVectorMachine.yaml
    sha256: 0cc2faa913fdafdc539a7d04d08d26c0963f77ad3ca26b833b29ed3ed313e4e0
    role: context
  - path: data/aio/VariationalAutoEncoder.yaml
    sha256: f8f523c5f2cecf91f1510c5ab74bfd36d717f3e683a9a8384e44a3f855e4c45e
    role: context
  - path: data/curated/BlackBoxVariationalInference.yaml
    sha256: 8237d3233ae06163b8fab5b4fa047ffc938e275bc1e3ede883348e06c2b266a8
    role: context
  - path: data/curated/FullyFactorizedMeanFieldInference.yaml
    sha256: 102be6f77143b26acb0d482f91e2dfa58ea113f2188b14b92067484cc4f9408d
    role: context
  - path: data/curated/GaussianLossSmoothedMixedModelVariationalInference.yaml
    sha256: c02f90d76cda5b494bcd213b746478d573905c29a87e6edf24bf6dce32a554b0
    role: target
  - path: data/curated/NonconjugateVariationalMessagePassing.yaml
    sha256: 0d303d220e92ad009eb802ddee59c6ab74cfd1d7872f3a50ad939deed002ad23
    role: context
  - path: data/curated/SharedInverseLengthscaleVariationalSparseSpectrumInference.yaml
    sha256: e770d9f4bc09fd642cda3e77c07223b517e97285d8ebf655a55a0cddd0711427
    role: context
  - path: data/curated/StructuredMeanFieldInference.yaml
    sha256: 3cd31e539123908291c2a9a394792c52dacf415ce3c19c4d6a42e9be6173c86b
    role: context
  - path: research/discovery/20261012T234243Z-loss-smoothed-mixed-model-inference.json
    sha256: e9d9418116ffd391ce5001c96a68d90d943f096f4758a14278aa2e2e8aafa034
    role: context
  - path: research/discovery/loss-smoothed-mixed-model-boundaries.py
    sha256: dc22a0a65d72cbacaeb97eacd84b9a1c51ce1b190367a36bb29ccd33a2a6b1ef
    role: context
  - path: reviews/structured/20261012T234720Z-loss-smoothed-mixed-model-open/review.yaml
    sha256: 03b96ccca362159471b8097a1fba68c1cdec8b3c2827dde149b5941a2fb1430e
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
- target_id: AIMech:GaussianLossSmoothedMixedModelVariationalInference
  path: data/curated/GaussianLossSmoothedMixedModelVariationalInference.yaml
  label: Gaussian loss-smoothed mixed-model variational inference
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GaussianLossSmoothedMixedModelVariationalInference.yaml
    role: maintained
scope:
  description: All maintained fields and primary support of the exact base loss-smoothed
    mixed-model inference record.
  selection: 'Exact maintained ID: AIMech:GaussianLossSmoothedMixedModelVariationalInference'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
  exclusions:
  - target: Projected and stochastic algorithms
    reason: Separate unresolved source formula/schedule questions; excluded from this
      base procedure.
  - target: Complete package, journal article and reproduction supplement
    reason: Only the primary preprint and selected versioned source files were inspected;
      no Julia execution or fitting.
  - target: Existing native and AIO context records
    reason: Identity/mapping context, not full scientific rereview.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 105.03s (0:01:45)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 554 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 204 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 202,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
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
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
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
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Unchanged independent loss-convolution and fixed-state arithmetic
  command: python3 research/discovery/loss-smoothed-mixed-model-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
  exit_code: 0
  expected_exit_code: 0
  summary: '{"quantile": {"analytic": [0.626652376470149, -0.5413447460685429, 0.3024634056489292],
    "hermite_quadrature": [0.6266523764701492, -0.5413447460681581, 0.3024634056494104],
    "max_error": 4.811706588725428e-13}, "mixed_model_state": {"predictor_means":
    [0.4, 0.25, 0.09999999999999998], "predictor_variances": [1.1600000000000001,
    1.07, 3.6799999999999997], "variance_factor_shape": 2.5, "variance_factor_rate":
    1.3965, "expected_inverse_variance": 1.790189760114572, "proposal_precision":
    [[1.13034988866348, 0.23673567405060184], [0.23673567405060184, 3.4659958774257165]],
    "proposal_covariance": [[0.8975208172260317, -0.06130278371775282], [-0.06130278371775282,
    0.2927044900521073]], "proposal_mean": [0.7400915336851399, 0.20769274720273945],
    "natural_and_newton_form_max_difference": 1.1102230246251565e-16}, "source_precision_sign":
    {"correct": 1.25, "printed": -0.75}, "uniform_convergence_counterexample": {"nu":
    0.1, "values": [{"xi": 0, "difference": 0.0050125208594010645}, {"xi": 5, "difference":
    0.7439240558112742}, {"xi": 10, "difference": 110.40811925535272}], "argument":
    "Difference exp(xi)*(exp(nu\u00b2/2)-1) has infinite supremum over real xi for
    each nu>0."}, "package_hinge_derivative": {"finite_difference_of_psi0": -0.8734510455188359,
    "correct": -0.8734510455264423, "statically_transcribed_psi1": -1.7469020910528845},
    "scope": "One supplied Gaussian/IG state and finite quadratures; not an iterative
    fit, author-code execution, convergence test or empirical benchmark."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T234243Z-loss-smoothed-mixed-model-inference.json
  accessed_at: '2026-10-12T23:50:25Z'
  support: supports
  summary: 'No normalized identity match across all 442 pinned AIO IDs, labels and
    scoped synonyms and 553 maintained IDs, names and aliases. Ignored- and hidden-inclusive
    fixed-string searches of the recovery, old discovery and original Documents checkouts
    returned 30, 0 and 0 lines, all 30 read: prior source leads and contextual references,
    without a matching record. Assessed all 33 semantic AIO rows and 113 native names/definitions,
    seven complete annotated AIO nodes with incident edges/generated YAML and five
    complete native context records. Gaussian loss-smoothed mixed-model variational
    inference is a descriptive local name for the base unconstrained-Gaussian NCVB-UF
    procedure in Castiglione and Bernardi Algorithm 1, with the precision sign qualified
    against Proposition 2 and Appendix A2. Its unit-loss generalized target, one-dimensional
    Gaussian loss smoothing, full fixed/random-effect covariance and inverse-gamma
    variance coordinates distinguish it from generic NCVMP, BBVI, generic mean-field
    families and the shared-spectral regression procedure. NCVB-UF is a source-specific
    algorithm designation, not a claim that all nonconjugate variational Bayes is
    this method. Older titles of arXiv:2206.09444 are the same source version history.
    Projected and stochastic extensions are separate pending scope. Absence is bounded
    to this pin and inspected corpus.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-12T23:50:25Z'
  support: supports
  summary: All 33 semantic AIO rows, 113 native definitions, seven complete AIO nodes/incident
    edges/generated YAML and five complete native context records were assessed in
    preparation. The related random-effects mapping distinguishes algorithm from model
    context; all captured bytes remain unchanged.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/loss-smoothed-mixed-model-boundaries.py
  accessed_at: '2026-10-12T23:50:25Z'
  snapshot_sha256: dc22a0a65d72cbacaeb97eacd84b9a1c51ce1b190367a36bb29ccd33a2a6b1ef
  support: supports
  summary: Independent finite pinball/Hermite quadrature, one supplied full Gaussian
    and inverse-gamma state, and equivalent natural/Newton Gaussian forms. Explicit
    counterexamples expose a source precision sign and global uniform-convergence
    overstatement; static hinge expressions expose a package derivative mismatch.
    No fitting loop, author implementation execution, or benchmark.
- evidence_id: castiglione2025
  kind: primary_source
  reference: https://arxiv.org/pdf/2206.09444v5
  locator: Section 2, Equation 1, PDF p. 3; Sections 2.1–2.3, Equations 2–6 and Propositions
    2–3, PDF pp. 4–6; Section 3.1, PDF p. 9; Appendix A1–A3, PDF pp. 16–20; B3, PDF
    p. 24; Algorithm 1, PDF p. 26
  accessed_at: '2026-10-12T22:48:02Z'
  snapshot_sha256: 5213ddc037e51a1165214416577ae2708cfc06f5753bc0718ca3c121c223ea9a
  support: supports
  summary: arXiv:2206.09444v5, revised 2025-10-13; all 41 PDF pages inspected. DOI
    10.1080/10618600.2025.2527925 identifies the journal article; its full text and
    reproduction supplement were not inspected. All 41 pages visually read during
    preparation; after capture reread PDF pp. 3–6,9,16–18,24,26 against the exact
    full YAML.
- evidence_id: bayesglmm-psifun
  kind: primary_source
  reference: https://raw.githubusercontent.com/CristianCastiglione/BayesGLMM.jl/15ce3551f62b0dfb5a54a6bc455deb1cb6966b34/src/psifun.jl
  locator: _psi(...,f::SVC,...) and _psi(...,f::Quantile,...) in the complete src/psifun.jl
    file
  accessed_at: '2026-10-12T23:28:08Z'
  snapshot_sha256: 708ec333ac71bb42f49bdf45d02242999831a9f4f1bdf92a50645ca6c21a2895
  support: supports
  summary: Commit 15ce3551f62b0dfb5a54a6bc455deb1cb6966b34, dated 2025-11-04; complete
    selected source file statically inspected, not executed. Package as a whole not
    certified. Complete selected source file statically reread after capture; no Julia
    execution. Ten package files read during preparation, not the whole package.
- evidence_id: locator-defect
  kind: record_content
  reference: data/curated/GaussianLossSmoothedMixedModelVariationalInference.yaml
  accessed_at: '2026-10-12T23:50:25Z'
  snapshot_sha256: c02f90d76cda5b494bcd213b746478d573905c29a87e6edf24bf6dce32a554b0
  support: supports
  summary: Three corrected locators now identify model Equation1, family Equation3/Section3.1,
    and variance coordinates Proposition2/AppendixA2. After successor capture, visually
    reread PDF3,5,9,17; PDF4,6,26 were verified in the initial full review. All statements
    remain unchanged and the report/page agree.
- evidence_id: predecessor
  kind: record_content
  reference: reviews/structured/20261012T234720Z-loss-smoothed-mixed-model-open/review.yaml
  accessed_at: '2026-10-12T23:50:25Z'
  snapshot_sha256: 03b96ccca362159471b8097a1fba68c1cdec8b3c2827dde149b5941a2fb1430e
  support: context_only
  summary: Immutable initial full scientific review records minor locator finding
    F1 and the maintained owner. Its captured source base predates the unrelated two-file
    Pages deployment change; all scientific inputs survived integration unchanged.
assessments:
- assessment_id: identity
  area: identity
  topic: Loss-smoothed full-Gaussian mixed-model procedure
  outcome: supported
  target_ids:
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
  evidence_ids:
  - identity
  - castiglione2025
  summary: Retain the distinct base procedure with a descriptive local name.
  details: The generalized mixed-model target, full fixed/random-coefficient factor,
    independent inverse-gamma variance factors, Gaussian loss convolution and specified
    natural-proposal schedule are more specific than generic NCVMP or mean-field families.
    BBVI uses sampling-based gradients; the preceding shared-spectral method has uncertain
    nonlinear spectral parameters and different scale factors. NCVB-UF is the source-specific
    Algorithm 1 designation. Revised arXiv titles are one version history, not multiple
    concepts. Projected/stochastic extensions remain outside scope.
- assessment_id: mapping
  area: grounding
  topic: Inference-to-random-effects context
  outcome: supported
  target_ids:
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
  evidence_ids:
  - mapping
  - castiglione2025
  summary: A related mapping preserves abstraction level.
  details: Random-effect blocks and inferred variance parameters define this procedure’s
    modeling context. The pinned RandomEffectsModel class does not identify its variational
    schedule and is not asserted equivalent or superclass. Conventional GLMs need
    not include arbitrary generalized losses; regression is only one application;
    SVM does not follow from sharing a loss; PGM/BayesianNetwork are broader structural
    context, and VAE is a different neural architecture.
- assessment_id: generalized-target
  area: evidence
  topic: generalized-target
  outcome: supported
  target_ids:
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
  evidence_ids:
  - castiglione2025
  summary: The statement and corrected citation are supported under the explicit domain.
  details: 'For observations y_i and design rows c_i^T, let theta=(beta,u_1,...,u_H)
    and eta_i=c_i^T*theta. The unit-loss generalized posterior is proportional to
    exp(-sum_i psi(y_i,eta_i)) times the prior: beta~N(0,sigma_beta^2*R_beta^-1),
    u_h|s_h~N(0,s_h*R_h^-1) and independent s_h~IG(A_h,B_h). Here sigma_beta^2,A_h,B_h
    are positive, each R is positive definite, and IG(A,B) has density proportional
    to s^(-A-1)*exp(-B/s), s>0. These proper-prior and positive-definite assumptions
    delimit this record; an intrinsic singular Gaussian requires separate constraints.
    An arbitrary loss defines a generalized target, not automatically a normalized
    sampling likelihood. Assume its normalizing constant Z is finite and positive;
    a finite nonnegative loss with these proper priors suffices.'
- assessment_id: factor-family-objective
  area: evidence
  topic: factor-family-objective
  outcome: supported
  target_ids:
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
  evidence_ids:
  - castiglione2025
  summary: The statement and corrected citation are supported under the explicit domain.
  details: Use q(theta)=N(mu,Sigma) with a full positive-definite covariance, independently
    of q(s_h)=IG(alpha_h,b_h) for each random-effect variance. Dependence among fixed
    and random coefficients is retained; dependence between theta and the variances,
    and between the variance factors, is omitted. The variational objective is L=E_q[log
    unnormalized_target]-E_q[log q], a lower bound on log Z under the proper-target
    and finite-expectation conditions. It does not assert a normalized-data-likelihood
    evidence for arbitrary losses. This is the unconstrained Gaussian factorization
    called NCVB-UF in the source, not its further block-factorized Gaussian projections.
- assessment_id: gaussian-loss-smoothing
  area: evidence
  topic: gaussian-loss-smoothing
  outcome: supported
  target_ids:
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
  evidence_ids:
  - castiglione2025
  - calculation
  summary: The statement and corrected citation are supported under the explicit domain.
  details: At current Gaussian moments, xi_i=c_i^T*mu and nu_i^2=c_i^T*Sigma*c_i.
    For nu_i>0 define Psi0_i=E[psi(y_i,xi_i+nu_i*Z0)] with Z0~N(0,1), and Psi1_i and
    Psi2_i as its first and second xi derivatives. Under dominated differentiation,
    for example a measurable loss of at most polynomial growth, these equal E[Z0*psi]/nu_i
    and E[(Z0^2-1)*psi]/nu_i^2. Thus nondifferentiable losses can give smooth Gaussian
    expected losses through one-dimensional expectations, with analytic forms for
    some losses and quadrature for others. These identities concern positive nu and
    the stated integrability conditions; they are not a blanket global uniform-convergence
    theorem or a rule for substituting nu=0.
- assessment_id: variance-coordinates
  area: evidence
  topic: variance-coordinates
  outcome: supported
  target_ids:
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
  evidence_ids:
  - castiglione2025
  - calculation
  summary: The statement and corrected citation are supported under the explicit domain.
  details: Holding current q(theta) fixed, each exact inverse-gamma coordinate has
    alpha_h=A_h+d_h/2 and b_h=B_h+(mu_h^T*R_h*mu_h+tr(R_h*Sigma_hh))/2, where d_h
    is the random-effect block size. Therefore E_q[1/s_h]=alpha_h/b_h. The expected
    prior precision Rbar is block diagonal, with beta block R_beta/sigma_beta^2 and
    random block (alpha_h/b_h)*R_h. Positive prior parameters and positive-definite
    R make these factors proper and Rbar positive definite. These exact variance-factor
    coordinates do not make the coupled full posterior exact.
- assessment_id: gaussian-natural-proposal
  area: evidence
  topic: gaussian-natural-proposal
  outcome: supported
  target_ids:
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
  evidence_ids:
  - castiglione2025
  - calculation
  summary: The statement and corrected citation are supported under the explicit domain.
  details: In the base full-data cycle, compute xi,nu and Psi1,Psi2 from the old mu,Sigma;
    update the variance factors from those old Gaussian moments; then use their new
    Rbar. Set W=diag(Psi2), P=Rbar+C^T*W*C and h=C^T*(W*xi-Psi1). If P is positive
    definite, propose Sigma_new=P^-1 and mu_new=Sigma_new*h, equivalently mu_new=mu+Sigma_new*g
    with g=-C^T*Psi1-Rbar*mu. This uses the plus curvature sign from Proposition 2
    and Appendix A2, correcting the inconsistent minus sign in printed Algorithm 1.
    For convex losses with nonnegative smoothed curvature, positive-definite Rbar
    makes P positive definite. The h form avoids dividing by individual zero curvature
    entries. It is a Gaussian NCVMP fixed-point/natural proposal, not an exact Gaussian-family
    maximizer or a general bound-ascent guarantee; recompute moments after changing
    q(theta).
- assessment_id: pinball-loss-example
  area: evidence
  topic: pinball-loss-example
  outcome: supported
  target_ids:
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
  evidence_ids:
  - castiglione2025
  - calculation
  summary: The statement and corrected citation are supported under the explicit domain.
  details: For the unscaled pinball loss psi(y,eta)=(y-eta)*(tau-1[y<eta]), 0<tau<1,
    set z=(y-xi)/nu with nu>0. With phi and Phi the standard normal density and cumulative
    distribution, Psi0=nu*(phi(z)+z*(Phi(z)-1+tau)), Psi1=1-tau-Phi(z), and Psi2=phi(z)/nu.
    This concrete Gaussian convolution supplies the gradient and nonnegative curvature
    used by the base mixed-model update without differentiating the loss at its kink.
    The scaling is part of the generalized target; multiplying a loss by a constant
    generally changes that target relative to its prior.
- assessment_id: implementation-boundary
  area: evidence
  topic: implementation-boundary
  outcome: supported
  target_ids:
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
  evidence_ids:
  - bayesglmm-psifun
  - calculation
  summary: The statement and corrected citation are supported under the explicit domain.
  details: In the inspected package psifun SVC method, the expected hinge loss psi0
    has the unscaled Gaussian-convolution form, while psi1 and psi2 use twice its
    corresponding derivatives (apart from numeric clipping). They therefore do not
    consistently describe derivatives of that same psi0. This is a static source inconsistency,
    not a measured runtime or benchmark result, and does not alter the unscaled pinball
    formulas curated here.
- assessment_id: target-and-domain
  area: consistency
  topic: Generalized normalization and proper priors
  outcome: supported
  target_ids:
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
  evidence_ids:
  - castiglione2025
  summary: The target and Gaussian domains are appropriately delimited.
  details: The record conditions on a finite positive generalized normalizer and well-defined
    expectations. For finite nonnegative loss, exp(-sum loss) is positive and at most
    one under a proper prior, so its expectation is in (0,1]. The ELBO bounds log
    Z, without inventing a normalized observation likelihood. SPD prior matrices delimit
    ordinary proper Gaussians despite the source PSD wording. Shape/rate and expected
    inverse variance use the variance variable s_h, not the standard deviation. Source
    bound-display inconsistencies do not enter the defining objective.
- assessment_id: curvature-and-schedule
  area: consistency
  topic: Frozen loss moments and new variance precision
  outcome: supported
  target_ids:
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
  evidence_ids:
  - castiglione2025
  - calculation
  summary: The qualified plus-curvature proposal follows the expected-log-target Hessian.
  details: Source Algorithm 1 computes old predictor moments, updates IG factors from
    old coefficient moments, then applies the Gaussian proposal using new expected
    prior precision. P=Rbar+C^T diag(Psi2) C, and P*mu+g=C^T(W*xi-Psi1), so the natural
    and Newton forms agree. With convex losses and SPD prior precision, P is SPD.
    The calculator verifies one 2-coefficient state and exposes the printed minus-sign
    failure for a quadratic loss. This does not establish iterative ascent or convergence,
    nor certify a differently scheduled package.
- assessment_id: loss-convolution
  area: consistency
  topic: Nonsmooth losses and explicit regularity
  outcome: supported
  target_ids:
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
  evidence_ids:
  - castiglione2025
  - calculation
  summary: The derivative identities and pinball normalization are internally consistent.
  details: Differentiating the Gaussian kernel gives the first two Hermite moments
    for positive nu under domination. Polynomial growth is a sufficient condition,
    not a copied blanket theorem. Split quadrature around the pinball kink agrees
    within 4.9e-13 for the supplied case. The exponential-loss counterexample shows
    that Gaussian integrability/convexity alone do not imply global uniform convergence.
    Zero variance is excluded from the divided Hermite expressions; h avoids a separate
    division by zero Psi2. No doubled hinge/SVR formula is imported.
- assessment_id: package-boundary
  area: provenance
  topic: Static implementation evidence does not certify paper fidelity
  outcome: supported
  target_ids:
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
  evidence_ids:
  - castiglione2025
  - bayesglmm-psifun
  - calculation
  summary: The selected package inconsistency is accurately and narrowly stated.
  details: The complete _psi SVC method has unscaled psi_0 but doubled psi_1 and psi_2
    for ordinary +/-1 labels, apart from clipping. A finite derivative of its statically
    transcribed unscaled expression distinguishes the factor of two; no Julia call
    was executed. The record distinguishes post-v5 package changes, observation-scale
    factors and controls from the base unit-loss procedure. Its source URL/hash identify
    the exact file; the broader downloaded/read scopes are preserved in the report.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, report mirror and source provenance
  outcome: supported
  target_ids:
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
  evidence_ids:
  - identity
  - mapping
  - castiglione2025
  - bayesglmm-psifun
  - calculation
  summary: All maintained fields were read; DRAFT remains.
  details: Assessed stable ID/name/source alias, algorithm kind, definition, identity
    context, all seven statements/citations, both source identities/authors/versions/access/hash,
    unchanged AIO snapshot and related mapping, six limitations and real timestamps.
    All source bytes, context hashes and the exact report mirror agree. Primary PDF
    and ten selected package files were read; journal PDF/supplement and package runtime
    remain unassessed. The formula, projection and empirical-context caveats prevent
    unsupported performance claims. The three citation locators are now corrected;
    full-field comparison confirms all statements, identity, mapping and limitations
    unchanged apart from the real updated timestamp.
- assessment_id: locator-defect
  area: evidence
  topic: Claim-specific primary locators
  outcome: supported
  target_ids:
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
  evidence_ids:
  - locator-defect
  - castiglione2025
  summary: All three primary locators now point to the supporting model, family and
    variance passages.
  details: The generalized target is Equation1/PDF3, Gaussian/IG factorization Equation3/PDF5,
    alternative factorization Section3.1/PDF9, and IG coordinate Proposition2/PDF6/AppendixA2/PDF17.
    Corrected citations preserve the supported statements, qualified Gaussian natural
    step and source limitations. Full-field comparison with the published initial
    record confirms the bounded change.
findings:
- finding_id: F1
  issue_key: aimech-loss-smoothed-primary-locators
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Correct three primary-source locators in the loss-smoothed inference record
  description: The generalized-target, factor-family-objective and variance-coordinates
    claims contain incorrect equation/section references. The model is Equation1/PDF3,
    the family Equation3/PDF5 with Section3.1/PDF9 for alternative factorizations,
    and IG coordinates Proposition2/PDF6 and AppendixA2/PDF17. Correct the locators
    and mirror the record in the discovery report; the statements and mathematical
    qualifications are supported and need no change.
  target_ids:
  - AIMech:GaussianLossSmoothedMixedModelVariationalInference
  field_paths:
  - claims[0].evidence[0].locator
  - claims[1].evidence[0].locator
  - claims[3].evidence[0].locator
  evidence_ids:
  - locator-defect
  - castiglione2025
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GaussianLossSmoothedMixedModelVariationalInference.yaml
    role: maintained
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261012T234720Z-loss-smoothed-mixed-model-open
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/215
  disposition_reason: The generalized-target locator now identifies Equation1/Section2/PDF3–4;
    factor-family-objective identifies the objective on PDF4, family Equation3/PDF5
    and Section3.1/PDF9; variance-coordinates identifies Proposition2/PDF5–6, AppendixA2/PDF17
    and Algorithm1/PDF26. The relevant source pages were visually verified, and full-field
    comparison shows only these three locators and the actual updated timestamp changed.
    Report/page synchronization and required checks pass.
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- The sole minor citation finding is resolved with explicit predecessor linkage. Source-level
  formula, convergence and implementation caveats remain explicit.
- The initial publication guard detected the independently merged Pages workflow and
  .nojekyll changes at8390491ea3f6cd3950482ef71350c2715efdbc7c. They were inspected
  and integrated by rebase; all scientific review inputs remained unchanged. Post-correction
  gates ran on the integrated branch.
- Added one DRAFT algorithm, yielding 554 native and 442 unchanged generated records.
  The 739-entry main frontier retains 484 pending and 57 partly addressed cohorts;
  nested source inventories also remain incomplete.
- All 41 arXiv v5 pages were visually read. The full journal article and reproduction
  supplement were not accessed; journal landing-page access returned HTTP 403. Independent
  finite quadrature and a single supplied Gaussian/IG state check derivative and update
  algebra, not iterative fitting, convergence or accuracy. No empirical performance
  claim is made; inconsistencies in the source experiment descriptions and table contexts
  are retained in the discovery report. DRAFT remains.
- The author-linked BayesGLMM.jl snapshot 15ce3551f62b0dfb5a54a6bc455deb1cb6966b34
  postdates arXiv v5. Ten selected files were statically read, with no Julia execution.
  Its added observation-scale factors, update order and step controls differ from
  the base target; its SVC expected-loss derivatives are inconsistent with its own
  unscaled expected loss. This package was not used to certify Algorithm 1 fidelity.
  The remaining package and journal reproduction supplement were not fully inspected.
- Source pseudocode, normalization, convergence, projection and empirical-context
  discrepancies are explicitly retained rather than treated as implementation fidelity
  or general superiority. No upstream paper/package correction was requested or performed.
- Original-checkout synchronization and old round141 cleanup remain pending explicit
  approval after automatic review rejection; isolated recovery work only.
related_reviews:
- repository: CultureBotAI/AIMech
  review_id: 20261012T234720Z-loss-smoothed-mixed-model-open
  relationship: Resolves F1 for the maintained loss-smoothed mixed-model record.
links: []
tags:
- native-concepts
- variational-inference
- mixed-models
- self-review
- discovery-ongoing
```
