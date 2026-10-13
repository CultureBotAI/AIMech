# Scientific author self-review of Gaussian message conflict diagnostic

- Review: 20261013T003933Z-gaussian-message-conflict-diagnostic
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T00:34:45Z
- Finished UTC: 2026-10-13T00:39:33Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the Gaussian-message diagnostic as a distinct DRAFT algorithm with related random-effects context. All seven claims and their locators are supported within the explicit approximation limits. No actionable defect was found; empirical calibration and source implementation remain unverified.

## Scope And Provenance

All fields of the exact maintained Gaussian message conflict diagnostic and their primary support.

Selection: Exact maintained ID: AIMech:GaussianMessageConflictDiagnostic
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9443501f4f1b9ba298ed11ef7a0b91dac0c0c318.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:GaussianMessageConflictDiagnostic | data/curated/GaussianMessageConflictDiagnostic.yaml | maintained | Gaussian message conflict diagnostic |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:GaussianMessageConflictDiagnostic | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 134.11s (0:02:14)<br>Checked 442 record(s); 0 failed.<br>Checked 557 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 208 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 206,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:GaussianMessageConflictDiagnostic | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:GaussianMessageConflictDiagnostic | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:GaussianMessageConflictDiagnostic | Exited 0 without output. |
| Finite Gaussian-message boundary arithmetic | passed | True | AIMech:GaussianMessageConflictDiagnostic | {"approximation_boundaries": {"exact_flat_prior_likelihood_mass": 1.0000000000000002, "exact_flat_prior_likelihood_mean": 0.3546371545385245, "exact_flat_prior_likelihood_variance": 0.39493406684819216, "full_q_predictive_prior_variance": 0.95, "message_prior_variance": 0.5}, "balanced_gaussian": {"expected_ratio": 0.6, "full_data_statistic": 2.7, "loo_statistic": 4.5, "ratio": 0.6000000000000001}, "limits": "Finite supplied-state arithmetic only. The Poisson local block is stationary under supplied globals, which are not optimized. No global fit, source software or calibration simulation was run.", "local_poisson": {"difference_mean": -1.0, "difference_variance": 1.0, "exposure": 1.764993805169191, "finite_gradient_mean": -4.4408920985006255e-11, "finite_gradient_variance": 1.021405182655144e-09, "likelihood_message_mean": 0.5, "likelihood_message_variance": 0.5, "lower_tail": 0.8413447460685429, "mean": 0.0, "prior_message_mean": -0.5, "prior_message_variance": 0.5, "recombined_mean": 0.0, "recombined_variance": 0.25, "two_sided": 0.31731050786291415, "upper_tail": 0.15865525393145707, "variance": 0.25, "y": 3.0}, "multivariate": {"chi2_two_degrees_upper": 0.49260582073598913, "combined_precision_determinant": 3, "mahalanobis": 1.4160919540229886, "singular_likelihood_determinant": 0, "transformed_mahalanobis": 1.4160919540229884}} |

## Scientific And Domain Assessments

### Gaussian-message screening versus fitting and cross-validation

identity: supported. Targets: AIMech:GaussianMessageConflictDiagnostic.

Retain the bounded diagnostic algorithm identity.

The procedure consumes fitted GLMM variational factors, separates prior and likelihood messages and evaluates their approximate independent Gaussian difference. It does not denote NCVMP fitting itself, stochastic optimization, local-neighbor density scoring or the exact simulation-based leave-one-unit-out comparator. The descriptive native name avoids asserting an upstream AIO class or a source acronym.

### Method-to-model context

grounding: supported. Targets: AIMech:GaussianMessageConflictDiagnostic.

The related random-effects mapping is justified.

The hierarchical unit effects and shared prior covariance supply the defining context. GLM and logistic regression are less specific or subcases; fixed-effects-only modeling omits the tested hierarchy. RegressionAnalysis is task context, PGM/BayesianNetwork broader representation context, VAE a different architecture, and EvaluationBias a bias type. Unlabeled screening alone does not make the procedure an UnsupervisedLearning identity. No equivalence or is-a relation is asserted.

### fitted-glmm-context

evidence: supported. Targets: AIMech:GaussianMessageConflictDiagnostic.

Supported within the declared approximation and domain.

The inspected diagnostic applies to the partially noncentered Poisson-log or Bernoulli-logit GLMM with a_i=u_i+B_i*beta and predictor eta_i=V_i*beta+Z_i*a_i, where a_i&#124;beta,D~N(B_i*beta,D). Its input is a fitted block-factorized approximation q(beta)q(D)product_i q(a_i), with q(beta)=N(m,Q), q(D)=IW(nuq,Sq) and q(a_i)=N(m_i,Q_i). Require proper factors, finite Gaussian moments and a local Gaussian NCVMP fixed point for every assessed unit at the final fixed global factors. Stochastic global fitting alone can leave local factors stale; the source calls for a final local refresh. The diagnostic compares prior and likelihood messages about unit random effects; it does not itself fit the model or prove that a flagged unit is erroneous.

### prior-message

evidence: supported. Targets: AIMech:GaussianMessageConflictDiagnostic.

Supported within the declared approximation and domain.

Write A=E_q[D^-1]=nuq*Sq^-1. The Gaussian prior message has precision A, mean m_prior=B_i*m and covariance C_prior=A^-1=Sq/nuq. These natural parameters follow from the a_i-dependent part of E_q(beta,D)[log p(a_i&#124;beta,D)]. After normalization it is a Gaussian function of a_i. It is not the arithmetic predictive mixture integral p(a_i&#124;beta,D)q(beta)q(D) d beta dD: when nuq&gt;r+1 that mixture has covariance Sq/(nuq-r-1)+B_i*Q*B_i^T, generally different. A pointwise Jensen bound on an unnormalized expected-log kernel does not establish a density lower bound after separate normalization. The mixture-moment comparison is curator reasoning under the stated independent factors.

### likelihood-message

evidence: supported. Targets: AIMech:GaussianMessageConflictDiagnostic.

Supported within the declared approximation and domain.

At the same local state, let G_i and F_i be expected first and second cumulant derivatives under the Gaussian predictor. For positive-exposure Poisson observations, both equal E_i*exp(t_i+v_i/2), elementwise, where t_i=V_i*m+Z_i*m_i and v_i=diag(V_i*Q*V_i^T+Z_i*Q_i*Z_i^T). For Bernoulli-logit they are standard-normal expectations of sigmoid(T) and sigmoid(T)*(1-sigmoid(T)), with T=t_ij+sqrt(v_ij)*Z0 and Z0~N(0,1). Define R_i=Z_i^T*diag(F_i)*Z_i and s_i=Z_i^T*(y_i-G_i). If R_i is positive definite, the standalone likelihood message is N(m_lik,C_lik), with C_lik=R_i^-1 and m_lik=m_i+C_lik*s_i. Positive semidefinite curvature alone does not suffice: rank-deficient Z_i gives a singular R_i and no proper Gaussian density on the full r-dimensional space, even when the combined posterior factor is proper. The normalized expectations here follow the 2013 Appendix B; the 2014 Appendix B display on PDF p. 37 and the 2013 Section 4.3 display on PDF p. 8 both omit a half in the Gaussian exponent.

### fixed-point-combination

evidence: supported. Targets: AIMech:GaussianMessageConflictDiagnostic.

Supported within the declared approximation and domain.

At a local fixed point, Q_i^-1=A+R_i and A*(m_i-B_i*m)=s_i. Thus the prior and likelihood natural parameters add to those of q(a_i): Q_i^-1*m_i=A*m_prior+R_i*m_lik. Equivalently, the ratio q(a_i)/N(a_i;m_prior,C_prior) is proportional to the likelihood Gaussian when its precision is positive definite. Away from the fixed point, summing the current messages produces the local Gaussian proposal, not necessarily the stored q(a_i); the ratio interpretation and diagnostic must not silently assume that stale local parameters satisfy these equations.

### gaussian-conflict-score

evidence: supported. Targets: AIMech:GaussianMessageConflictDiagnostic.

Supported within the declared approximation and domain.

Under the additional approximation that the two message-based replicates are independent, their difference delta=a_prior-a_lik is Gaussian with mean d=m_prior-m_lik and covariance C=C_prior+C_lik. In one dimension define the lower tail P(delta&lt;=0)=Phi(-d/sqrt(C)), the upper tail as one minus that value, and the two-sided score as twice their minimum. State the selected tail explicitly. For r-dimensional positive-definite C, the source uses d^T*C^-1*d and the upper chi-square tail with r degrees of freedom under a Gaussian-difference approximation. These are probabilities or reference-tail scores from the constructed approximation; this algebra alone does not establish uniform frequentist p-values or false-positive control under repeated data.

### leave-one-out-boundary

evidence: supported. Targets: AIMech:GaussianMessageConflictDiagnostic.

Supported within the declared approximation and domain.

The simulation-based comparator draws a predictive-prior replicate using hyperparameters fitted without the assessed unit and a likelihood replicate from that unit with a reference prior. The variational messages instead use the full-data fitted factors, replace hyperparameter mixtures by expected-log Gaussian messages, and neglect replicate dependence. The likelihood-message interpretation invokes a uniform reference prior, whereas the source comparison uses Jeffreys priors for its likelihood replications. Nuisance fixed effects learned from other units can still couple the two replications. Full-data fitting, factorization, reference-prior choice and approximate Gaussian likelihood messages therefore prevent treating this diagnostic as exact leave-one-unit-out conflict analysis. The source describes its approximation argument as nonrigorous.

### screening-and-evaluation

evidence: supported. Targets: AIMech:GaussianMessageConflictDiagnostic.

Supported within the declared approximation and domain.

The source proposes the message diagnostic as an initial screen, with selected units eligible for closer Monte Carlo assessment. Its comparisons use small GLMM datasets and transformed tail-probability agreement with simulation-based comparators; those comparisons do not establish universal calibration, multiple-testing control or a clinical decision rule. Changing the centered/partially noncentered factorization can change the approximate messages and scores. A common invertible linear transformation of an already constructed Gaussian difference preserves its Mahalanobis statistic, but this algebraic invariance does not imply invariance across separately fitted variational parametrizations. No diagnostic threshold is made intrinsic to this concept.

### Expected precision, moment mixtures and stationary recombination

consistency: supported. Targets: AIMech:GaussianMessageConflictDiagnostic.

Message precision and local fixed-point restrictions are correct.

The inverse expected precision is Sq/nuq; it differs from the predictive mixture covariance E[D]+B Q B^T. The finite scalar case gives 0.5 versus 0.95. At the constructed Poisson stationary block, prior (-0.5,0.5) and likelihood (0.5,0.5) recombine to local mean 0 and variance 0.25, with finite local derivatives below 1.1e-9. The exact flat-prior likelihood posterior instead has mean about0.35464 and variance0.39493, independently checked by quadrature and Gamma log-moments. A singular separated likelihood precision remains improper even when adding a proper prior yields a proper combined factor. These are supplied-state calculations, not a global fit.

### Signed difference and qualified reference probabilities

consistency: supported. Targets: AIMech:GaussianMessageConflictDiagnostic.

The tail direction is internally consistent and calibration is not overclaimed.

For delta=prior-likelihood with mean -1 and variance1, the lower tail is0.8413447, upper0.1586553 and two-sided0.3173105. This avoids copying the 2007 displayed mean and Figure4 caption inconsistencies. A two-dimensional Gaussian difference gives Mahalanobis1.41609195 and chi-square2 upper0.49260582; a common invertible linear transformation preserves the statistic. This does not establish invariance between distinct variational fits. The balanced Gaussian full-data/leave-one-out ratio0.6 is a finite example only. Conditional, preposterior and parameterwise calibration require their separate assumptions; no FDR or clinical threshold follows.

### All maintained fields and evidence provenance

provenance: supported. Targets: AIMech:GaussianMessageConflictDiagnostic.

The full record and report mirror are consistent; retain DRAFT.

Read ID, name, empty aliases, algorithm kind, definition and citations, identity notes, all seven claims and locators, source titles/authors/versions/URLs/access/hash, AIO pin and mapping, all five limitations and actual UTC provenance. Checked source acquisition hashes and exact report mirror. The Presanis2013 follow-up reading is separate pending discovery, not silently added as evidence for this record. No author code, global model fitting, clinical inference or benchmark/calibration reproduction is asserted. No actionable defect was found in this one-record review.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T003442Z-gaussian-message-conflict-diagnostic.json | supports | No normalized identity match across 442 pinned AIO and 556 maintained IDs, names, aliases and scoped synonyms for the proposed Gaussian-message and general cross-validated conflict diagnostics. Fixed-string searches of the recovery, older discovery and original Documents checkouts included ignored and hidden files and returned 59, 0 and 0 lines. All 59 were assessed: prior source links, the stochastic fitting record and its generated/review mirrors, and explicit pending diagnostic leads. Assessed 50 semantic AIO rows and 177 native names/definitions, reusing 31 and 130 verified unchanged rows and reading all 19 and 47 additional rows. Ten complete AIO nodes, annotations, incident edges and generated records were read or verified unchanged; four full native context records were read or verified against prior readings. The source phrase mixed messages diagnostics denotes this Gaussian approximation to prior-likelihood conflict scoring, not the separate GLMM fitting algorithm. It is distinct from generic NCVMP, the full-data and stochastic GLMM fitting procedures, distance-based local outlier factors and the simulation-based cross-validated comparator. This is a descriptive AIMech algorithm identity bounded to the inspected source and corpus. |
| mapping | sources/aio/aio.json | supports | Assessed 50 semantic AIO rows and 177 native definitions, with verified prior-reading reuse and all additional rows read. Ten full AIO nodes/annotations/incident edges/generated records and four full native context records were read or verified unchanged. Context hashes match. RandomEffectsModel is a related model-context mapping, not an algorithm superclass. |
| calculation | research/discovery/gaussian-message-conflict-boundaries.py | supports | Independent scalar Poisson local stationarity and message recombination under supplied globals, scalar exact-likelihood integration, predictive/message variance distinction, two-dimensional Gaussian coordinate invariance, singular likelihood precision, and balanced known-variance full-data/leave-one-out comparison. No global fit, source software or empirical calibration. |
| tan2014 | https://arxiv.org/pdf/1208.4949v4; Sections 5–5.2, PDF pp. 17–21; Appendix B, pp. 37–38; Appendix C, p. 39; diagnostic examples, pp. 21–28 and 40–42 | supports | All 42 primary pages were read during preparation. After capture, visually reread pp. 17–21 and 37–39 against the complete record. Checked Gaussian messages, fixed-point sum, refresh, reference priors, normalization error and limits of the source approximation argument. |
| marshall2007 | https://projecteuclid.org/journals/bayesian-analysis/volume-2/issue-2/Identifying-outliers-in-Bayesian-hierarchical-models--a-simulation-based/10.1214/07-BA218.pdf; Sections 3–4, PDF pp. 7–12 / journal pp. 415–420; Section 6, PDF pp. 14–16; Appendix A1, PDF pp. 21–22; Figure 4, PDF p. 31 | supports | All 36 primary pages were read during preparation. After capture, visually reread pp. 10–12, 21–22 and 31. Verified prior-minus-likelihood tail algebra, source sign/caption inconsistencies, nuisance coupling and the distinction between preposterior and parameterwise repeated-data calibration. |
| tan2013 | https://arxiv.org/pdf/1205.3906v3; Section 4.3, PDF p. 8; Appendix B, PDF pp. 19–20 | supports | All 21 primary pages were read during preparation. After capture, visually reread pp. 8 and 19–20. The malformed Gaussian exponent is explicit, while Appendix B supplies the normalized standard-normal construction used in the record. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT diagnostic algorithm, yielding 557 native and 442 unchanged generated records. The 742-entry main frontier retains 484 pending and 57 partly addressed cohorts, plus nested source leads.
- All 42 pages of the 2014 preprint, 36 pages of the 2007 journal PDF and 21 pages of the supporting 2013 reprint were read. No author software, model fitting or empirical calibration simulation was run. The independent calculation constructs one local Poisson stationary block under supplied globals, compares its message with an exact scalar likelihood posterior, and checks Gaussian and singular-message boundaries; it does not optimize the global factors or reproduce reported experiments.
- Original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection; isolated recovery work only.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T003933Z-gaussian-message-conflict-diagnostic
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Gaussian message conflict diagnostic
started_at: '2026-10-13T00:34:45Z'
finished_at: '2026-10-13T00:39:33Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged message propriety, normalization, local
    stationarity, exact-likelihood and predictive-mixture distinctions, tail orientation,
    calibration and mapping. This is adversarial author self-review, not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the Gaussian-message diagnostic as a distinct DRAFT algorithm with
  related random-effects context. All seven claims and their locators are supported
  within the explicit approximation limits. No actionable defect was found; empirical
  calibration and source implementation remain unverified.
source:
  git_revision: 9443501f4f1b9ba298ed11ef7a0b91dac0c0c318
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/EvaluationBias.yaml
    sha256: 6523f8c43f7b140c6dd593069e30b7fc1bdd60b89d01bdf5441d2bc83a12e749
    role: context
  - path: data/aio/FixedEffectsModel.yaml
    sha256: ce9b21b60e99bf7abfd19b9b480d5c73777ba59f38af53c3fa2d6bfc50f71a86
    role: context
  - path: data/aio/GeneralizedLinearModel.yaml
    sha256: 202002ec50c6e6207bc2fefba5baeab233514fd8f9118a623d1917b599ce2c7d
    role: context
  - path: data/aio/LogisticRegression.yaml
    sha256: 67dd6e8ae1bb6bfc48598b41adccbf7d48d925db8b0ee3a71f59569913b8c968
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
  - path: data/aio/UnsupervisedLearning.yaml
    sha256: c75c631eb034257c75645995539dcc614fd5ab5e521dbede69457a318e86615e
    role: context
  - path: data/aio/VariationalAutoEncoder.yaml
    sha256: f8f523c5f2cecf91f1510c5ab74bfd36d717f3e683a9a8384e44a3f855e4c45e
    role: context
  - path: data/curated/GaussianMessageConflictDiagnostic.yaml
    sha256: adc6c4f1c16288b59515f77401ff4d1c2a02f673a00a91963de6e3fa588c4cff
    role: target
  - path: data/curated/LocalOutlierFactor.yaml
    sha256: b9293fde56804e7df6d3056e00b08240ca9dc8711a715bda54d064cfd9bc8812
    role: context
  - path: data/curated/NonconjugateVariationalMessagePassing.yaml
    sha256: 0d303d220e92ad009eb802ddee59c6ab74cfd1d7872f3a50ad939deed002ad23
    role: context
  - path: data/curated/PartiallyNoncenteredGLMMVariationalInference.yaml
    sha256: 9c5bfdf2ad7cee069ecf1559d3df296ac7c7c0c807a49eee5644f984e7abc361
    role: context
  - path: data/curated/StochasticNonconjugateGLMMVariationalInference.yaml
    sha256: 27235b4323710bcd53fb73d6dbe06f0eb115a3d6cbf52600345f9c7c68c45c99
    role: context
  - path: research/discovery/20261013T003442Z-gaussian-message-conflict-diagnostic.json
    sha256: a1e56e685e922bec4373079eeb4df46f891d14d818a7c85c035f6c36286cd9ca
    role: context
  - path: research/discovery/gaussian-message-conflict-boundaries.py
    sha256: 875140ac830921142f8590a0f2af2f659f607fc7676fa487593bdd3f96b98973
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
- target_id: AIMech:GaussianMessageConflictDiagnostic
  path: data/curated/GaussianMessageConflictDiagnostic.yaml
  label: Gaussian message conflict diagnostic
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GaussianMessageConflictDiagnostic.yaml
    role: maintained
scope:
  description: All fields of the exact maintained Gaussian message conflict diagnostic
    and their primary support.
  selection: 'Exact maintained ID: AIMech:GaussianMessageConflictDiagnostic'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:GaussianMessageConflictDiagnostic
  exclusions:
  - target: General cross-validated and separator-node conflict procedures
    reason: Separate pending concepts; not certified by this Gaussian-message approximation.
  - target: Existing native and AIO neighbors
    reason: Identity and mapping context, not full scientific rereview.
  - target: Source software and empirical calibration
    reason: No author implementation, global fitting or repeated-data simulation run.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:GaussianMessageConflictDiagnostic
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 134.11s (0:02:14)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 557 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 208 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 206,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:GaussianMessageConflictDiagnostic
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
  - AIMech:GaussianMessageConflictDiagnostic
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
  - AIMech:GaussianMessageConflictDiagnostic
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Finite Gaussian-message boundary arithmetic
  command: python3 research/discovery/gaussian-message-conflict-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:GaussianMessageConflictDiagnostic
  exit_code: 0
  expected_exit_code: 0
  summary: '{"approximation_boundaries": {"exact_flat_prior_likelihood_mass": 1.0000000000000002,
    "exact_flat_prior_likelihood_mean": 0.3546371545385245, "exact_flat_prior_likelihood_variance":
    0.39493406684819216, "full_q_predictive_prior_variance": 0.95, "message_prior_variance":
    0.5}, "balanced_gaussian": {"expected_ratio": 0.6, "full_data_statistic": 2.7,
    "loo_statistic": 4.5, "ratio": 0.6000000000000001}, "limits": "Finite supplied-state
    arithmetic only. The Poisson local block is stationary under supplied globals,
    which are not optimized. No global fit, source software or calibration simulation
    was run.", "local_poisson": {"difference_mean": -1.0, "difference_variance": 1.0,
    "exposure": 1.764993805169191, "finite_gradient_mean": -4.4408920985006255e-11,
    "finite_gradient_variance": 1.021405182655144e-09, "likelihood_message_mean":
    0.5, "likelihood_message_variance": 0.5, "lower_tail": 0.8413447460685429, "mean":
    0.0, "prior_message_mean": -0.5, "prior_message_variance": 0.5, "recombined_mean":
    0.0, "recombined_variance": 0.25, "two_sided": 0.31731050786291415, "upper_tail":
    0.15865525393145707, "variance": 0.25, "y": 3.0}, "multivariate": {"chi2_two_degrees_upper":
    0.49260582073598913, "combined_precision_determinant": 3, "mahalanobis": 1.4160919540229886,
    "singular_likelihood_determinant": 0, "transformed_mahalanobis": 1.4160919540229884}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T003442Z-gaussian-message-conflict-diagnostic.json
  accessed_at: '2026-10-13T00:34:45Z'
  support: supports
  summary: 'No normalized identity match across 442 pinned AIO and 556 maintained
    IDs, names, aliases and scoped synonyms for the proposed Gaussian-message and
    general cross-validated conflict diagnostics. Fixed-string searches of the recovery,
    older discovery and original Documents checkouts included ignored and hidden files
    and returned 59, 0 and 0 lines. All 59 were assessed: prior source links, the
    stochastic fitting record and its generated/review mirrors, and explicit pending
    diagnostic leads. Assessed 50 semantic AIO rows and 177 native names/definitions,
    reusing 31 and 130 verified unchanged rows and reading all 19 and 47 additional
    rows. Ten complete AIO nodes, annotations, incident edges and generated records
    were read or verified unchanged; four full native context records were read or
    verified against prior readings. The source phrase mixed messages diagnostics
    denotes this Gaussian approximation to prior-likelihood conflict scoring, not
    the separate GLMM fitting algorithm. It is distinct from generic NCVMP, the full-data
    and stochastic GLMM fitting procedures, distance-based local outlier factors and
    the simulation-based cross-validated comparator. This is a descriptive AIMech
    algorithm identity bounded to the inspected source and corpus.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T00:34:45Z'
  support: supports
  summary: Assessed 50 semantic AIO rows and 177 native definitions, with verified
    prior-reading reuse and all additional rows read. Ten full AIO nodes/annotations/incident
    edges/generated records and four full native context records were read or verified
    unchanged. Context hashes match. RandomEffectsModel is a related model-context
    mapping, not an algorithm superclass.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/gaussian-message-conflict-boundaries.py
  accessed_at: '2026-10-13T00:34:45Z'
  snapshot_sha256: 875140ac830921142f8590a0f2af2f659f607fc7676fa487593bdd3f96b98973
  support: supports
  summary: Independent scalar Poisson local stationarity and message recombination
    under supplied globals, scalar exact-likelihood integration, predictive/message
    variance distinction, two-dimensional Gaussian coordinate invariance, singular
    likelihood precision, and balanced known-variance full-data/leave-one-out comparison.
    No global fit, source software or empirical calibration.
- evidence_id: tan2014
  kind: primary_source
  reference: https://arxiv.org/pdf/1208.4949v4
  locator: Sections 5–5.2, PDF pp. 17–21; Appendix B, pp. 37–38; Appendix C, p. 39;
    diagnostic examples, pp. 21–28 and 40–42
  accessed_at: '2026-10-12T23:58:40Z'
  snapshot_sha256: 276ebdc67a5f3d0a3453b1859bbc40458d77f83bd58b604c063972df6cf6de15
  support: supports
  summary: All 42 primary pages were read during preparation. After capture, visually
    reread pp. 17–21 and 37–39 against the complete record. Checked Gaussian messages,
    fixed-point sum, refresh, reference priors, normalization error and limits of
    the source approximation argument.
- evidence_id: marshall2007
  kind: primary_source
  reference: https://projecteuclid.org/journals/bayesian-analysis/volume-2/issue-2/Identifying-outliers-in-Bayesian-hierarchical-models--a-simulation-based/10.1214/07-BA218.pdf
  locator: Sections 3–4, PDF pp. 7–12 / journal pp. 415–420; Section 6, PDF pp. 14–16;
    Appendix A1, PDF pp. 21–22; Figure 4, PDF p. 31
  accessed_at: '2026-10-13T00:08:57Z'
  snapshot_sha256: 289815a344a25cce48f822228e8ed9d25a4e08daf22f241ca77526dc991374b1
  support: supports
  summary: All 36 primary pages were read during preparation. After capture, visually
    reread pp. 10–12, 21–22 and 31. Verified prior-minus-likelihood tail algebra,
    source sign/caption inconsistencies, nuisance coupling and the distinction between
    preposterior and parameterwise repeated-data calibration.
- evidence_id: tan2013
  kind: primary_source
  reference: https://arxiv.org/pdf/1205.3906v3
  locator: Section 4.3, PDF p. 8; Appendix B, PDF pp. 19–20
  accessed_at: '2026-10-12T23:41:04Z'
  snapshot_sha256: 32f56daf18e03d20a6d50785d2370248b22599d2db67dca0cec0c9f5723e74f0
  support: supports
  summary: All 21 primary pages were read during preparation. After capture, visually
    reread pp. 8 and 19–20. The malformed Gaussian exponent is explicit, while Appendix
    B supplies the normalized standard-normal construction used in the record.
assessments:
- assessment_id: identity
  area: identity
  topic: Gaussian-message screening versus fitting and cross-validation
  outcome: supported
  target_ids:
  - AIMech:GaussianMessageConflictDiagnostic
  evidence_ids:
  - identity
  - tan2014
  - marshall2007
  summary: Retain the bounded diagnostic algorithm identity.
  details: The procedure consumes fitted GLMM variational factors, separates prior
    and likelihood messages and evaluates their approximate independent Gaussian difference.
    It does not denote NCVMP fitting itself, stochastic optimization, local-neighbor
    density scoring or the exact simulation-based leave-one-unit-out comparator. The
    descriptive native name avoids asserting an upstream AIO class or a source acronym.
- assessment_id: mapping
  area: grounding
  topic: Method-to-model context
  outcome: supported
  target_ids:
  - AIMech:GaussianMessageConflictDiagnostic
  evidence_ids:
  - mapping
  - tan2014
  summary: The related random-effects mapping is justified.
  details: The hierarchical unit effects and shared prior covariance supply the defining
    context. GLM and logistic regression are less specific or subcases; fixed-effects-only
    modeling omits the tested hierarchy. RegressionAnalysis is task context, PGM/BayesianNetwork
    broader representation context, VAE a different architecture, and EvaluationBias
    a bias type. Unlabeled screening alone does not make the procedure an UnsupervisedLearning
    identity. No equivalence or is-a relation is asserted.
- assessment_id: fitted-glmm-context
  area: evidence
  topic: fitted-glmm-context
  outcome: supported
  target_ids:
  - AIMech:GaussianMessageConflictDiagnostic
  evidence_ids:
  - tan2014
  summary: Supported within the declared approximation and domain.
  details: The inspected diagnostic applies to the partially noncentered Poisson-log
    or Bernoulli-logit GLMM with a_i=u_i+B_i*beta and predictor eta_i=V_i*beta+Z_i*a_i,
    where a_i|beta,D~N(B_i*beta,D). Its input is a fitted block-factorized approximation
    q(beta)q(D)product_i q(a_i), with q(beta)=N(m,Q), q(D)=IW(nuq,Sq) and q(a_i)=N(m_i,Q_i).
    Require proper factors, finite Gaussian moments and a local Gaussian NCVMP fixed
    point for every assessed unit at the final fixed global factors. Stochastic global
    fitting alone can leave local factors stale; the source calls for a final local
    refresh. The diagnostic compares prior and likelihood messages about unit random
    effects; it does not itself fit the model or prove that a flagged unit is erroneous.
- assessment_id: prior-message
  area: evidence
  topic: prior-message
  outcome: supported
  target_ids:
  - AIMech:GaussianMessageConflictDiagnostic
  evidence_ids:
  - tan2014
  - calculation
  summary: Supported within the declared approximation and domain.
  details: 'Write A=E_q[D^-1]=nuq*Sq^-1. The Gaussian prior message has precision
    A, mean m_prior=B_i*m and covariance C_prior=A^-1=Sq/nuq. These natural parameters
    follow from the a_i-dependent part of E_q(beta,D)[log p(a_i|beta,D)]. After normalization
    it is a Gaussian function of a_i. It is not the arithmetic predictive mixture
    integral p(a_i|beta,D)q(beta)q(D) d beta dD: when nuq>r+1 that mixture has covariance
    Sq/(nuq-r-1)+B_i*Q*B_i^T, generally different. A pointwise Jensen bound on an
    unnormalized expected-log kernel does not establish a density lower bound after
    separate normalization. The mixture-moment comparison is curator reasoning under
    the stated independent factors.'
- assessment_id: likelihood-message
  area: evidence
  topic: likelihood-message
  outcome: supported
  target_ids:
  - AIMech:GaussianMessageConflictDiagnostic
  evidence_ids:
  - tan2014
  - tan2013
  - calculation
  summary: Supported within the declared approximation and domain.
  details: 'At the same local state, let G_i and F_i be expected first and second
    cumulant derivatives under the Gaussian predictor. For positive-exposure Poisson
    observations, both equal E_i*exp(t_i+v_i/2), elementwise, where t_i=V_i*m+Z_i*m_i
    and v_i=diag(V_i*Q*V_i^T+Z_i*Q_i*Z_i^T). For Bernoulli-logit they are standard-normal
    expectations of sigmoid(T) and sigmoid(T)*(1-sigmoid(T)), with T=t_ij+sqrt(v_ij)*Z0
    and Z0~N(0,1). Define R_i=Z_i^T*diag(F_i)*Z_i and s_i=Z_i^T*(y_i-G_i). If R_i
    is positive definite, the standalone likelihood message is N(m_lik,C_lik), with
    C_lik=R_i^-1 and m_lik=m_i+C_lik*s_i. Positive semidefinite curvature alone does
    not suffice: rank-deficient Z_i gives a singular R_i and no proper Gaussian density
    on the full r-dimensional space, even when the combined posterior factor is proper.
    The normalized expectations here follow the 2013 Appendix B; the 2014 Appendix
    B display on PDF p. 37 and the 2013 Section 4.3 display on PDF p. 8 both omit
    a half in the Gaussian exponent.'
- assessment_id: fixed-point-combination
  area: evidence
  topic: fixed-point-combination
  outcome: supported
  target_ids:
  - AIMech:GaussianMessageConflictDiagnostic
  evidence_ids:
  - tan2014
  - calculation
  summary: Supported within the declared approximation and domain.
  details: 'At a local fixed point, Q_i^-1=A+R_i and A*(m_i-B_i*m)=s_i. Thus the prior
    and likelihood natural parameters add to those of q(a_i): Q_i^-1*m_i=A*m_prior+R_i*m_lik.
    Equivalently, the ratio q(a_i)/N(a_i;m_prior,C_prior) is proportional to the likelihood
    Gaussian when its precision is positive definite. Away from the fixed point, summing
    the current messages produces the local Gaussian proposal, not necessarily the
    stored q(a_i); the ratio interpretation and diagnostic must not silently assume
    that stale local parameters satisfy these equations.'
- assessment_id: gaussian-conflict-score
  area: evidence
  topic: gaussian-conflict-score
  outcome: supported
  target_ids:
  - AIMech:GaussianMessageConflictDiagnostic
  evidence_ids:
  - tan2014
  - marshall2007
  - calculation
  summary: Supported within the declared approximation and domain.
  details: Under the additional approximation that the two message-based replicates
    are independent, their difference delta=a_prior-a_lik is Gaussian with mean d=m_prior-m_lik
    and covariance C=C_prior+C_lik. In one dimension define the lower tail P(delta<=0)=Phi(-d/sqrt(C)),
    the upper tail as one minus that value, and the two-sided score as twice their
    minimum. State the selected tail explicitly. For r-dimensional positive-definite
    C, the source uses d^T*C^-1*d and the upper chi-square tail with r degrees of
    freedom under a Gaussian-difference approximation. These are probabilities or
    reference-tail scores from the constructed approximation; this algebra alone does
    not establish uniform frequentist p-values or false-positive control under repeated
    data.
- assessment_id: leave-one-out-boundary
  area: evidence
  topic: leave-one-out-boundary
  outcome: supported
  target_ids:
  - AIMech:GaussianMessageConflictDiagnostic
  evidence_ids:
  - tan2014
  - marshall2007
  summary: Supported within the declared approximation and domain.
  details: The simulation-based comparator draws a predictive-prior replicate using
    hyperparameters fitted without the assessed unit and a likelihood replicate from
    that unit with a reference prior. The variational messages instead use the full-data
    fitted factors, replace hyperparameter mixtures by expected-log Gaussian messages,
    and neglect replicate dependence. The likelihood-message interpretation invokes
    a uniform reference prior, whereas the source comparison uses Jeffreys priors
    for its likelihood replications. Nuisance fixed effects learned from other units
    can still couple the two replications. Full-data fitting, factorization, reference-prior
    choice and approximate Gaussian likelihood messages therefore prevent treating
    this diagnostic as exact leave-one-unit-out conflict analysis. The source describes
    its approximation argument as nonrigorous.
- assessment_id: screening-and-evaluation
  area: evidence
  topic: screening-and-evaluation
  outcome: supported
  target_ids:
  - AIMech:GaussianMessageConflictDiagnostic
  evidence_ids:
  - tan2014
  - calculation
  summary: Supported within the declared approximation and domain.
  details: The source proposes the message diagnostic as an initial screen, with selected
    units eligible for closer Monte Carlo assessment. Its comparisons use small GLMM
    datasets and transformed tail-probability agreement with simulation-based comparators;
    those comparisons do not establish universal calibration, multiple-testing control
    or a clinical decision rule. Changing the centered/partially noncentered factorization
    can change the approximate messages and scores. A common invertible linear transformation
    of an already constructed Gaussian difference preserves its Mahalanobis statistic,
    but this algebraic invariance does not imply invariance across separately fitted
    variational parametrizations. No diagnostic threshold is made intrinsic to this
    concept.
- assessment_id: message-propriety
  area: consistency
  topic: Expected precision, moment mixtures and stationary recombination
  outcome: supported
  target_ids:
  - AIMech:GaussianMessageConflictDiagnostic
  evidence_ids:
  - tan2014
  - tan2013
  - calculation
  summary: Message precision and local fixed-point restrictions are correct.
  details: The inverse expected precision is Sq/nuq; it differs from the predictive
    mixture covariance E[D]+B Q B^T. The finite scalar case gives 0.5 versus 0.95.
    At the constructed Poisson stationary block, prior (-0.5,0.5) and likelihood (0.5,0.5)
    recombine to local mean 0 and variance 0.25, with finite local derivatives below
    1.1e-9. The exact flat-prior likelihood posterior instead has mean about0.35464
    and variance0.39493, independently checked by quadrature and Gamma log-moments.
    A singular separated likelihood precision remains improper even when adding a
    proper prior yields a proper combined factor. These are supplied-state calculations,
    not a global fit.
- assessment_id: tails-and-calibration
  area: consistency
  topic: Signed difference and qualified reference probabilities
  outcome: supported
  target_ids:
  - AIMech:GaussianMessageConflictDiagnostic
  evidence_ids:
  - tan2014
  - marshall2007
  - calculation
  summary: The tail direction is internally consistent and calibration is not overclaimed.
  details: For delta=prior-likelihood with mean -1 and variance1, the lower tail is0.8413447,
    upper0.1586553 and two-sided0.3173105. This avoids copying the 2007 displayed
    mean and Figure4 caption inconsistencies. A two-dimensional Gaussian difference
    gives Mahalanobis1.41609195 and chi-square2 upper0.49260582; a common invertible
    linear transformation preserves the statistic. This does not establish invariance
    between distinct variational fits. The balanced Gaussian full-data/leave-one-out
    ratio0.6 is a finite example only. Conditional, preposterior and parameterwise
    calibration require their separate assumptions; no FDR or clinical threshold follows.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields and evidence provenance
  outcome: supported
  target_ids:
  - AIMech:GaussianMessageConflictDiagnostic
  evidence_ids:
  - identity
  - mapping
  - tan2014
  - marshall2007
  - tan2013
  - calculation
  summary: The full record and report mirror are consistent; retain DRAFT.
  details: Read ID, name, empty aliases, algorithm kind, definition and citations,
    identity notes, all seven claims and locators, source titles/authors/versions/URLs/access/hash,
    AIO pin and mapping, all five limitations and actual UTC provenance. Checked source
    acquisition hashes and exact report mirror. The Presanis2013 follow-up reading
    is separate pending discovery, not silently added as evidence for this record.
    No author code, global model fitting, clinical inference or benchmark/calibration
    reproduction is asserted. No actionable defect was found in this one-record review.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT diagnostic algorithm, yielding 557 native and 442 unchanged generated
  records. The 742-entry main frontier retains 484 pending and 57 partly addressed
  cohorts, plus nested source leads.
- All 42 pages of the 2014 preprint, 36 pages of the 2007 journal PDF and 21 pages
  of the supporting 2013 reprint were read. No author software, model fitting or empirical
  calibration simulation was run. The independent calculation constructs one local
  Poisson stationary block under supplied globals, compares its message with an exact
  scalar likelihood posterior, and checks Gaussian and singular-message boundaries;
  it does not optimize the global factors or reproduce reported experiments.
- Original-checkout synchronization and old round141 cleanup remain pending explicit
  approval after automatic review rejection; isolated recovery work only.
related_reviews: []
links: []
tags:
- native-concepts
- model-diagnostics
- variational-inference
- self-review
- discovery-ongoing
```
