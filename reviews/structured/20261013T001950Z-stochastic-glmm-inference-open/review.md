# Scientific author self-review of stochastic nonconjugate GLMM inference

- Review: 20261013T001950Z-stochastic-glmm-inference-open
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T00:11:24Z
- Finished UTC: 2026-10-13T00:19:50Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Retain the qualified stochastic GLMM algorithm and related random-effects mapping. Correct one minor source-attribution defect distinguishing a repeated malformed display from the supporting normalized appendix; mathematical expectations are already correct and DRAFT remains.

## Scope And Provenance

All fields and primary support of the exact maintained stochastic GLMM inference record.

Selection: Exact maintained ID: AIMech:StochasticNonconjugateGLMMVariationalInference
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 1a431889423527d2df0178890fcd986722860aae.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:StochasticNonconjugateGLMMVariationalInference | data/curated/StochasticNonconjugateGLMMVariationalInference.yaml | maintained | Stochastic nonconjugate GLMM variational inference |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:StochasticNonconjugateGLMMVariationalInference | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 130.31s (0:02:10)<br>Checked 442 record(s); 0 failed.<br>Checked 556 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 206 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 204,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:StochasticNonconjugateGLMMVariationalInference | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:StochasticNonconjugateGLMMVariationalInference | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:StochasticNonconjugateGLMMVariationalInference | Exited0 without output. |
| Independent frozen-state sampling and natural-coordinate arithmetic | passed | True | AIMech:StochasticNonconjugateGLMMVariationalInference | {"limits": "Supplied local Gaussian factors are not optimized. These calculations check finite frozen-state sums and one simultaneous global step, not the profiled-gradient envelope condition, convergence, source implementation or benchmark.", "natural_step": {"IW_degrees": 6.0, "IW_scale": [[1.7342602999999999, 0.21385069999999998], [0.21385069999999998, 1.5386080999999998]], "beta_mean": [0.18017540453118402, -0.24359335881717006], "beta_precision": [[4.228559016630407, -0.46070141106253004], [-0.4607014110625301, 5.045709465902732]], "mean_form_error": 2.7755575615628914e-17, "omitted_local_covariance_error": [[0.243, -0.018], [-0.018, 0.31499999999999995]], "rho": 0.3, "selected_clusters": [0, 2]}, "printed_gaussian_weight_integral": 0.7071067811865475, "sampling": {"conditional_remaining_mean_after_first_index_zero": 13.5, "fixed_score_sum": 10.0, "fresh_singleton_mean": 10.0, "uniform_subset_and_iid_multiset_target_error": 8.881784197001252e-16}} |

## Scientific And Domain Assessments

### Cluster-local solves and global stochastic natural coordinates

identity: supported. Targets: AIMech:StochasticNonconjugateGLMMVariationalInference.

Retain the distinct model-specific algorithm.

The finite-N GLMM factorization is shared with the prior full-data method, but repeated selected-local solves and scaled cluster-minibatch global natural targets define a different schedule. Generic NCVMP, score-sampling BBVI, generic SGD and spectral GP updates do not identify this procedure. The source message-conflict diagnostic remains a separate candidate. No alias or upstream acceptance is invented.

### Method-to-random-effects context

grounding: supported. Targets: AIMech:StochasticNonconjugateGLMMVariationalInference.

Related RandomEffectsModel mapping is justified.

The shared random-effect covariance and clustered local/global hierarchy define the model context. GLM/logistic/regression are less specific or subcase/task context. FixedEffectsModel omits the defining latent covariance, PGM/BayesianNetwork describe broader graph structure, and VAE is a different architecture. No class equivalence or is-a relation is asserted.

### model-and-family

evidence: supported. Targets: AIMech:StochasticNonconjugateGLMMVariationalInference.

Mechanism or qualification is supported; one source-attribution defect is recorded separately.

For a fixed finite set of N clusters, use the partially noncentered Bernoulli-logit or Poisson-log mixed model: beta~N(0,Sigma0), u_i&#124;D~N(0,D), D~IW(nu,S), with positive-definite Sigma0,S and nu&gt;r-1. At fixed cluster maps B_i define a_i=u_i+B_i*beta and eta_i=V_i*beta+Z_i*a_i with V_i=X_i-Z_i*B_i; the source uses B_i=[(I-W_i)*C_i,0] for its shared/cluster-constant design. Approximate the posterior by q(beta)q(D)product_i q(a_i), using full Gaussian blocks q(beta)=N(m,Q), q(a_i)=N(m_i,Q_i) and q(D)=IW(nuq,Sq). Set nuq=nu+N. The ELBO is expected log joint plus entropy for this proper model; the algorithm infers global beta,D factors from cluster minibatches, not individual observation minibatches or an unspecified unbounded stream.

### local-iterations

evidence: supported. Targets: AIMech:StochasticNonconjugateGLMMVariationalInference.

Mechanism or qualification is supported; one source-attribution defect is recorded separately.

At the current global Gaussian and inverse-Wishart factors, draw a nonempty cluster minibatch and hold the globals and W_i fixed while iterating each selected local Gaussian. Let A=nuq*Sq^-1 and let G_i and F_i be expected first and second observation-cumulant derivatives under the current predictor distribution. With P_i=A+Z_i^T*diag(F_i)*Z_i and g_i=-A*(m_i-B_i*m)+Z_i^T*(y_i-G_i), propose Q_i_new=P_i^-1 and m_i_new=m_i+Q_i_new*g_i, evaluating both derivatives at the same old local state and recomputing moments for another local iteration. The source uses a loose relative local-mean stopping criterion; this is not a certificate of an exact stationary local solution or maximizer. Proper globals and exact nonnegative Bernoulli/Poisson curvature yield positive local precision.

### expected-observation-curvature

evidence: supported. Targets: AIMech:StochasticNonconjugateGLMMVariationalInference.

Mechanism or qualification is supported; one source-attribution defect is recorded separately.

For a selected cluster the scalar predictor means and variances are t_i=V_i*m+Z_i*m_i and v_i=diag(V_i*Q*V_i^T+Z_i*Q_i*Z_i^T). With positive Poisson exposures E_i, G_i=F_i=E_i*exp(t_i+v_i/2), elementwise. For Bernoulli-logit, G_ij=E[sigmoid(t_ij+sqrt(v_ij)*Z0)] and F_ij=E[sigmoid(T)*(1-sigmoid(T))] for the same T and Z0~N(0,1). These are one-dimensional normal expectations, approximated by quadrature for logistic observations. The standard-normal density uses exp(-z^2/2)/sqrt(2*pi); the missing half in the 2014 appendix display is qualified against the normalized construction and the 2013 source.

### frozen-global-targets

evidence: supported. Targets: AIMech:StochasticNonconjugateGLMMVariationalInference.

Mechanism or qualification is supported; one source-attribution defect is recorded separately.

After selected local iterations, freeze the old global m,Q,Sq and the selected local factors for both global proposals. For minibatch B of size b, define P_hat=Sigma0^-1+(N/b)*sum_{i in B}[B_i^T*A*B_i+V_i^T*diag(F_i)*V_i], g_hat=-Sigma0^-1*m+(N/b)*sum_{i in B}[B_i^T*A*(m_i-B_i*m)+V_i^T*(y_i-G_i)], and h_hat=P_hat*m+g_hat. The covariance-factor target is S_hat=S+(N/b)*sum_{i in B}[(m_i-B_i*m)*(m_i-B_i*m)^T+Q_i+B_i*Q*B_i^T], with degrees nu+N. Global priors enter once; only cluster contributions are expanded. S_hat includes the local covariance Q_i, present in Appendix B Equation 21 but omitted in printed Algorithm 2. Frozen global targets implement the simultaneous natural-gradient construction rather than silently reusing newly changed beta moments inside the other target.

### natural-parameter-mixing

evidence: supported. Targets: AIMech:StochasticNonconjugateGLMMVariationalInference.

Mechanism or qualification is supported; one source-attribution defect is recorded separately.

Choose 0&lt;rho&lt;=1 and write P_old=Q^-1 and h_old=P_old*m. Mix the Gaussian natural coordinates as P_new=(1-rho)*P_old+rho*P_hat and h_new=(1-rho)*h_old+rho*h_hat; then Q_new=P_new^-1 and m_new=Q_new*h_new=m+rho*Q_new*g_hat. Mix the inverse-Wishart scale as Sq_new=(1-rho)*Sq+rho*S_hat, keeping nuq=nu+N. This is not ordinary arithmetic averaging of Gaussian covariance matrices or means. Positive-definite old/target precisions and scales make this convex natural step proper. The source derives it from stochastic natural-gradient ascent; proper factors alone do not guarantee ELBO ascent or convergence.

### sampling-and-profile-boundary

evidence: supported. Targets: AIMech:StochasticNonconjugateGLMMVariationalInference.

Mechanism or qualification is supported; one source-attribution defect is recorded separately.

At a frozen global state, assume each cluster contribution is evaluated by the same specified local-solution rule. A fresh uniform subset of b clusters gives an unbiased N/b-scaled sum for the corresponding full sum; independent uniform draws with replacement also do so when repeated draws are counted with multiplicity. To identify that sum as the gradient of an optimized-local ELBO additionally requires the envelope argument’s differentiable stationary local solution and regularity. Approximate local solves, history-dependent warm starts or biased quadrature need separate error assessment. The source implementation description instead shuffles clusters into a sweep and samples from those remaining: its next-batch estimate is not generally conditionally unbiased at the changing current state under the fresh-subset argument. This does not by itself prove reshuffling fails; it limits the unbiased-gradient/convergence claim.

### schedule-and-hybrid-scope

evidence: supported. Targets: AIMech:StochasticNonconjugateGLMMVariationalInference.

Mechanism or qualification is supported; one source-attribution defect is recorded separately.

The source discusses diminishing gains rho_t=a/(t+A)^alpha with 1/2&lt;alpha&lt;=1 and later uses a sweep-count clock, and optionally switches to the full-data procedure when an attained-bound progress criterion is small. The schedule must be defined at the initial index and respect the factor-domain requirement; Robbins–Monro summability is only part of the regularity conditions needed for convergence. A finite hybrid switching/stopping rule does not establish stationary or globally optimal inference, and its reported runtime belongs to that hybrid experiment. This record does not certify a streaming population-size rule, constant-memory implementation, author software or the separate prior-likelihood conflict diagnostic.

### Simultaneous old-global evaluation and complete covariance moments

consistency: supported. Targets: AIMech:StochasticNonconjugateGLMMVariationalInference.

The target and damping equations agree with the source derivation.

Equation11 explicitly evaluates both global targets at current globals. Gaussian natural coordinates give hhat=Phat*m+ghat and newm=m+rho*newQ*ghat; independent finite arithmetic agrees within2.8e-17. AppendixB Equation21 includes Qi, unlike Algorithm2. Its omission changes the supplied one-step scale by [[.243,-.018],[-.018,.315]]. Proper prior scale plus nonnegative covariance contributions gives a proper IW target; nuq=nu+N satisfies normalization. This does not prove convergence or certify the pseudocode.

### Frozen finite-population sums versus profiled optimization and reshuffling

consistency: supported. Targets: AIMech:StochasticNonconjugateGLMMVariationalInference.

Unbiasedness is qualified to the appropriate sampling and local-rule assumptions.

Enumerating all uniform N=3,b=2 subsets and iid multisets gives target means agreeing with full sums within8.9e-16 at fixed supplied factors. Repeated draws count with multiplicity. Those factors were not optimized, so this is not an envelope-theorem or gradient-profile test. With fixed scores[1,2,7], fresh singleton rescaling averages10, while conditional resampling from the two remaining after index0 averages13.5. This refutes a general conditional-unbiased claim for source reshuffling, without proving algorithmic failure. Approximate local solves and quadrature are explicitly unverified error sources.

### Expected cumulants, finite gain and schedule limits

consistency: supported. Targets: AIMech:StochasticNonconjugateGLMMVariationalInference.

The stated equations use normalized Gaussian moments and preserve proper natural-coordinate domains.

Poisson G/F include exp(t+v/2); logistic expectations use normalized standard-normal weights and F&gt;=0. The printed malformed Gaussian weight integrates to1/sqrt(2), not1. Convex precision/scale mixing with0&lt;rho&lt;=1 remains proper, without ELBO-ascent guarantees. The source uses a fractional sweep clock and hybrid switching; undefined initial gain or finite stopping thresholds supply no convergence theorem. Record scope is finiteN, without a streaming or constant-memory claim.

### All fields, source versions and DRAFT scope

provenance: supported. Targets: AIMech:StochasticNonconjugateGLMMVariationalInference.

All fields were inspected; one bounded source-attribution clarification is required.

Read identity/name/empty aliases, kind, definition/citation, identity context, all seven claim statements/locators, both source metadata/access/hash, AIO snapshot/mapping, six limitations and real timestamps. The discovery report mirrors the exact YAML and captured context hashes agree. Full primary access does not imply implementation access. No fitting or clinical/general performance result is asserted. The normalization formula is correct, but the cited supporting2013 display is itself malformed and must be distinguished from its correct appendix.

### Distinguish repeated display error from normalized appendix

evidence: concern. Targets: AIMech:StochasticNonconjugateGLMMVariationalInference.

Qualify the2013 display as well as the2014 display.

The mathematical expectation is supported by the normalized2013 AppendixB, so no mechanism rewrite is needed. Explicitly identify the shared missing-half error in2013 Section4.3/PDF8 and2014 AppendixB/PDF37; narrow the supporting normalized locator to2013 AppendixB/PDF19–20.

## Findings

### F1: Distinguish the 2013 malformed normal-weight display from its normalized appendix

minor / open / confirmed; issue key: aimech-stochastic-glmm-normalization-source-attribution.

The logistic-curvature claim cites2013 Section4.3/PDF8 and AppendixB/PDF19–20 jointly as normalized Gaussian expectations, while explicitly flagging only the2014 display. The2013 p.8 display repeats exp(-x^2)/sqrt(2pi); its AppendixB uses the correct standard-normal density. State both display discrepancies and identify AppendixB as the normalized source. The curated expectation itself is already correct. Synchronize the discovery report and rendered page.

## Recommended Actions And Acceptance Checks

### A1

Clarify both malformed displays and the supporting normalized appendix; synchronize derived content, append actual history and save a linked successor.

- 2013PDF8 and2014PDF37 are explicitly distinguished from normalized2013AppendixB19–20.
- Correct mathematical expectations, identity and mapping remain unchanged.
- Validation and a linked successor review pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T001117Z-stochastic-nonconjugate-glmm-inference.json | supports | No normalized identity match across all 442 pinned AIO IDs, names and scoped synonyms and 555 maintained IDs, names and aliases for the stochastic GLMM or proposed message-conflict diagnostic identities. Fixed-string searches included ignored and hidden files in the recovery, older discovery and original Documents checkouts, returning 4, 0 and 0 lines; all four are previously saved source links. Assessed 31 semantic AIO rows and 130 native names/definitions: 28 and 99, respectively, were verified identical to the preceding complete readings, with all 3 and 31 new rows read. Eight full AIO nodes with incident edges/generated records were verified unchanged, and six full native context records were read or verified against prior readings. This descriptive local name denotes the Tan–Nott stochastic GLMM procedure derived in Equations 11, 13 and 20–21, with Algorithm 2 qualified by its appendix. Local Gaussian iterations and cluster-minibatch natural updates of global Gaussian/inverse-Wishart factors distinguish it from the existing full-data partially noncentered procedure, generic NCVMP, score-sampling BBVI, generic SGD and stochastic spectral regression. The source mixed-message conflict diagnostic is a separate pending identity. Absence is bounded to the inspected pin and corpus. |
| mapping | sources/aio/aio.json | supports | 31 semantic AIO rows and130 native definitions assessed, including verified reuse of28 and99 unchanged rows; all new rows read. Eight complete AIO nodes/edges/generated records and six complete native context records read or hash-verified against prior readings. Related RandomEffectsModel mapping preserves algorithm/model distinction. |
| calculation | research/discovery/stochastic-glmm-boundaries.py | supports | Independent enumeration of fresh uniform subsets and iid multisets at fixed supplied factors, simultaneous Gaussian/IW natural mixing, missing-local-covariance difference and a simple conditional reshuffling counterexample. No optimized local solution, convergence, source software or empirical fitting is certified. |
| tan2014 | https://arxiv.org/pdf/1208.4949v4; Sections 3–4, PDF pp.4–16; Appendix B, PDF pp.37–39 | supports | arXiv:1208.4949v4, 2014-03-28; all 42 preprint pages visually read, including Algorithms 1–2, Figures 1–13, Tables 1–9 and Appendices A–D. Journal reference: Bayesian Analysis 9:963–1004 (2014); locators use this preprint. All42pages read during preparation; after capture reread PDF pp.5,7,10–16,37–39. |
| tan2013 | https://arxiv.org/pdf/1205.3906v3; Section4.3 display PDF p.8 and normalized AppendixB construction PDF pp.19–20 | supports | arXiv:1205.3906v3, 2013-06-11; complete 21-page electronic reprint of Statistical Science 28(2):168–188 read. PDF pagination 1–21 differs from journal pagination. All21pages read during preparation; after capture reread PDF pp.8,19–20. The p.8 display repeats the missing-half error, while AppendixB explicitly uses the standard-normal density. |
| normalization-attribution | data/curated/StochasticNonconjugateGLMMVariationalInference.yaml | supports | expected-observation-curvature cites2013 Section4.3/PDF8 together with AppendixB/PDF19–20 as normalized Gaussian expectations. PDF8 also prints exp(-x^2)/sqrt(2pi), whereas AppendixB19 explicitly integrates against phi(x;0,1). The record flags only the2014 display and leaves this source distinction unclear. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. The one minor finding concerns source attribution, not the mathematical normal expectation. The initial sandboxed vendor fetch failed DNS; authorized network retry passed22 artifacts. An initial check before rendering failed two stale-page tests; pages were regenerated and the full gate rerun.
- Added one DRAFT algorithm, yielding 556 native and 442 unchanged generated records. The 741-entry main frontier retains 484 pending and 57 partly addressed cohorts; additional nested leads remain pending.
- All 42 primary 2014 preprint pages and the supporting 21-page 2013 reprint were read. The reported clinical-data comparisons and simulated hybrid-fit timings are not curated as clinical conclusions or general accuracy/speed guarantees. Source minibatch percentages contain decimal errors; finite-population weights here use actual N and b. No fitting, author implementation, diagnostic calibration study or benchmark was run.
- Independent arithmetic checks fixed supplied local Gaussian factors, all uniform subsets/iid draw multisets in a tiny example and one simultaneous global step. Those local factors were not optimized, so this is not a numerical test of the envelope theorem, a profiled-gradient reproduction or convergence. DRAFT remains.
- Original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection; isolated recovery work only.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T001950Z-stochastic-glmm-inference-open
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of stochastic nonconjugate GLMM inference
started_at: '2026-10-13T00:11:24Z'
finished_at: '2026-10-13T00:19:50Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged global evaluation points, complete covariance
    moments, natural mixing, sampling/envelope assumptions, proper factor domains
    and source locators. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Retain the qualified stochastic GLMM algorithm and related random-effects
  mapping. Correct one minor source-attribution defect distinguishing a repeated malformed
  display from the supporting normalized appendix; mathematical expectations are already
  correct and DRAFT remains.
source:
  git_revision: 1a431889423527d2df0178890fcd986722860aae
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
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
  - path: data/aio/VariationalAutoEncoder.yaml
    sha256: f8f523c5f2cecf91f1510c5ab74bfd36d717f3e683a9a8384e44a3f855e4c45e
    role: context
  - path: data/curated/BlackBoxVariationalInference.yaml
    sha256: 8237d3233ae06163b8fab5b4fa047ffc938e275bc1e3ede883348e06c2b266a8
    role: context
  - path: data/curated/GaussianLossSmoothedMixedModelVariationalInference.yaml
    sha256: c02f90d76cda5b494bcd213b746478d573905c29a87e6edf24bf6dce32a554b0
    role: context
  - path: data/curated/NonconjugateVariationalMessagePassing.yaml
    sha256: 0d303d220e92ad009eb802ddee59c6ab74cfd1d7872f3a50ad939deed002ad23
    role: context
  - path: data/curated/PartiallyNoncenteredGLMMVariationalInference.yaml
    sha256: 9c5bfdf2ad7cee069ecf1559d3df296ac7c7c0c807a49eee5644f984e7abc361
    role: context
  - path: data/curated/StochasticFactorizedVariationalSparseSpectrumGaussianProcessInference.yaml
    sha256: 58cad0537cfd416ecb4620b74e341ac69dd459fe0c80331cdb99ab0512b793a4
    role: context
  - path: data/curated/StochasticGradientDescent.yaml
    sha256: 5c57fc809ae8667d5be8cda421cc9f0bd1f0c668f64ba3d7b23d788528b46e97
    role: context
  - path: data/curated/StochasticNonconjugateGLMMVariationalInference.yaml
    sha256: 19ed20596f0cb31138a15b2855ed27652e981acd7ccf90d3f0b38f4b7387d888
    role: target
  - path: research/discovery/20261013T001117Z-stochastic-nonconjugate-glmm-inference.json
    sha256: b9a691d83cd551f6c1fb89623235fd896e5787899b0bf7babe7de272329b5660
    role: context
  - path: research/discovery/stochastic-glmm-boundaries.py
    sha256: a6f186de60597dc12cb5eb25f4f51a92e508b45e028c1bda8ac7edad912a392f
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
- target_id: AIMech:StochasticNonconjugateGLMMVariationalInference
  path: data/curated/StochasticNonconjugateGLMMVariationalInference.yaml
  label: Stochastic nonconjugate GLMM variational inference
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/StochasticNonconjugateGLMMVariationalInference.yaml
    role: maintained
scope:
  description: All fields and primary support of the exact maintained stochastic GLMM
    inference record.
  selection: 'Exact maintained ID: AIMech:StochasticNonconjugateGLMMVariationalInference'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:StochasticNonconjugateGLMMVariationalInference
  exclusions:
  - target: Message-conflict diagnostic and original diagnostic primary sources
    reason: Separate pending identity and evidence assessment.
  - target: Author implementation, model fitting and diagnostic calibration
    reason: Not executed or certified.
  - target: Existing native/AIO context records
    reason: Identity/mapping context, not full scientific rereview.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:StochasticNonconjugateGLMMVariationalInference
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 130.31s (0:02:10)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 556 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 206 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 204,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:StochasticNonconjugateGLMMVariationalInference
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
  - AIMech:StochasticNonconjugateGLMMVariationalInference
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
  - AIMech:StochasticNonconjugateGLMMVariationalInference
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Independent frozen-state sampling and natural-coordinate arithmetic
  command: python3 research/discovery/stochastic-glmm-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:StochasticNonconjugateGLMMVariationalInference
  exit_code: 0
  expected_exit_code: 0
  summary: '{"limits": "Supplied local Gaussian factors are not optimized. These calculations
    check finite frozen-state sums and one simultaneous global step, not the profiled-gradient
    envelope condition, convergence, source implementation or benchmark.", "natural_step":
    {"IW_degrees": 6.0, "IW_scale": [[1.7342602999999999, 0.21385069999999998], [0.21385069999999998,
    1.5386080999999998]], "beta_mean": [0.18017540453118402, -0.24359335881717006],
    "beta_precision": [[4.228559016630407, -0.46070141106253004], [-0.4607014110625301,
    5.045709465902732]], "mean_form_error": 2.7755575615628914e-17, "omitted_local_covariance_error":
    [[0.243, -0.018], [-0.018, 0.31499999999999995]], "rho": 0.3, "selected_clusters":
    [0, 2]}, "printed_gaussian_weight_integral": 0.7071067811865475, "sampling": {"conditional_remaining_mean_after_first_index_zero":
    13.5, "fixed_score_sum": 10.0, "fresh_singleton_mean": 10.0, "uniform_subset_and_iid_multiset_target_error":
    8.881784197001252e-16}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T001117Z-stochastic-nonconjugate-glmm-inference.json
  accessed_at: '2026-10-13T00:11:24Z'
  support: supports
  summary: 'No normalized identity match across all 442 pinned AIO IDs, names and
    scoped synonyms and 555 maintained IDs, names and aliases for the stochastic GLMM
    or proposed message-conflict diagnostic identities. Fixed-string searches included
    ignored and hidden files in the recovery, older discovery and original Documents
    checkouts, returning 4, 0 and 0 lines; all four are previously saved source links.
    Assessed 31 semantic AIO rows and 130 native names/definitions: 28 and 99, respectively,
    were verified identical to the preceding complete readings, with all 3 and 31
    new rows read. Eight full AIO nodes with incident edges/generated records were
    verified unchanged, and six full native context records were read or verified
    against prior readings. This descriptive local name denotes the Tan–Nott stochastic
    GLMM procedure derived in Equations 11, 13 and 20–21, with Algorithm 2 qualified
    by its appendix. Local Gaussian iterations and cluster-minibatch natural updates
    of global Gaussian/inverse-Wishart factors distinguish it from the existing full-data
    partially noncentered procedure, generic NCVMP, score-sampling BBVI, generic SGD
    and stochastic spectral regression. The source mixed-message conflict diagnostic
    is a separate pending identity. Absence is bounded to the inspected pin and corpus.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T00:11:24Z'
  support: supports
  summary: 31 semantic AIO rows and130 native definitions assessed, including verified
    reuse of28 and99 unchanged rows; all new rows read. Eight complete AIO nodes/edges/generated
    records and six complete native context records read or hash-verified against
    prior readings. Related RandomEffectsModel mapping preserves algorithm/model distinction.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/stochastic-glmm-boundaries.py
  accessed_at: '2026-10-13T00:11:24Z'
  snapshot_sha256: a6f186de60597dc12cb5eb25f4f51a92e508b45e028c1bda8ac7edad912a392f
  support: supports
  summary: Independent enumeration of fresh uniform subsets and iid multisets at fixed
    supplied factors, simultaneous Gaussian/IW natural mixing, missing-local-covariance
    difference and a simple conditional reshuffling counterexample. No optimized local
    solution, convergence, source software or empirical fitting is certified.
- evidence_id: tan2014
  kind: primary_source
  reference: https://arxiv.org/pdf/1208.4949v4
  locator: Sections 3–4, PDF pp.4–16; Appendix B, PDF pp.37–39
  accessed_at: '2026-10-12T23:58:40Z'
  snapshot_sha256: 276ebdc67a5f3d0a3453b1859bbc40458d77f83bd58b604c063972df6cf6de15
  support: supports
  summary: 'arXiv:1208.4949v4, 2014-03-28; all 42 preprint pages visually read, including
    Algorithms 1–2, Figures 1–13, Tables 1–9 and Appendices A–D. Journal reference:
    Bayesian Analysis 9:963–1004 (2014); locators use this preprint. All42pages read
    during preparation; after capture reread PDF pp.5,7,10–16,37–39.'
- evidence_id: tan2013
  kind: primary_source
  reference: https://arxiv.org/pdf/1205.3906v3
  locator: Section4.3 display PDF p.8 and normalized AppendixB construction PDF pp.19–20
  accessed_at: '2026-10-12T23:41:04Z'
  snapshot_sha256: 32f56daf18e03d20a6d50785d2370248b22599d2db67dca0cec0c9f5723e74f0
  support: supports
  summary: arXiv:1205.3906v3, 2013-06-11; complete 21-page electronic reprint of Statistical
    Science 28(2):168–188 read. PDF pagination 1–21 differs from journal pagination.
    All21pages read during preparation; after capture reread PDF pp.8,19–20. The p.8
    display repeats the missing-half error, while AppendixB explicitly uses the standard-normal
    density.
- evidence_id: normalization-attribution
  kind: record_content
  reference: data/curated/StochasticNonconjugateGLMMVariationalInference.yaml
  accessed_at: '2026-10-13T00:11:24Z'
  snapshot_sha256: 19ed20596f0cb31138a15b2855ed27652e981acd7ccf90d3f0b38f4b7387d888
  support: supports
  summary: expected-observation-curvature cites2013 Section4.3/PDF8 together with
    AppendixB/PDF19–20 as normalized Gaussian expectations. PDF8 also prints exp(-x^2)/sqrt(2pi),
    whereas AppendixB19 explicitly integrates against phi(x;0,1). The record flags
    only the2014 display and leaves this source distinction unclear.
assessments:
- assessment_id: identity
  area: identity
  topic: Cluster-local solves and global stochastic natural coordinates
  outcome: supported
  target_ids:
  - AIMech:StochasticNonconjugateGLMMVariationalInference
  evidence_ids:
  - identity
  - tan2014
  summary: Retain the distinct model-specific algorithm.
  details: The finite-N GLMM factorization is shared with the prior full-data method,
    but repeated selected-local solves and scaled cluster-minibatch global natural
    targets define a different schedule. Generic NCVMP, score-sampling BBVI, generic
    SGD and spectral GP updates do not identify this procedure. The source message-conflict
    diagnostic remains a separate candidate. No alias or upstream acceptance is invented.
- assessment_id: mapping
  area: grounding
  topic: Method-to-random-effects context
  outcome: supported
  target_ids:
  - AIMech:StochasticNonconjugateGLMMVariationalInference
  evidence_ids:
  - mapping
  - tan2014
  summary: Related RandomEffectsModel mapping is justified.
  details: The shared random-effect covariance and clustered local/global hierarchy
    define the model context. GLM/logistic/regression are less specific or subcase/task
    context. FixedEffectsModel omits the defining latent covariance, PGM/BayesianNetwork
    describe broader graph structure, and VAE is a different architecture. No class
    equivalence or is-a relation is asserted.
- assessment_id: model-and-family
  area: evidence
  topic: model-and-family
  outcome: supported
  target_ids:
  - AIMech:StochasticNonconjugateGLMMVariationalInference
  evidence_ids:
  - tan2014
  summary: Mechanism or qualification is supported; one source-attribution defect
    is recorded separately.
  details: 'For a fixed finite set of N clusters, use the partially noncentered Bernoulli-logit
    or Poisson-log mixed model: beta~N(0,Sigma0), u_i|D~N(0,D), D~IW(nu,S), with positive-definite
    Sigma0,S and nu>r-1. At fixed cluster maps B_i define a_i=u_i+B_i*beta and eta_i=V_i*beta+Z_i*a_i
    with V_i=X_i-Z_i*B_i; the source uses B_i=[(I-W_i)*C_i,0] for its shared/cluster-constant
    design. Approximate the posterior by q(beta)q(D)product_i q(a_i), using full Gaussian
    blocks q(beta)=N(m,Q), q(a_i)=N(m_i,Q_i) and q(D)=IW(nuq,Sq). Set nuq=nu+N. The
    ELBO is expected log joint plus entropy for this proper model; the algorithm infers
    global beta,D factors from cluster minibatches, not individual observation minibatches
    or an unspecified unbounded stream.'
- assessment_id: local-iterations
  area: evidence
  topic: local-iterations
  outcome: supported
  target_ids:
  - AIMech:StochasticNonconjugateGLMMVariationalInference
  evidence_ids:
  - tan2014
  summary: Mechanism or qualification is supported; one source-attribution defect
    is recorded separately.
  details: At the current global Gaussian and inverse-Wishart factors, draw a nonempty
    cluster minibatch and hold the globals and W_i fixed while iterating each selected
    local Gaussian. Let A=nuq*Sq^-1 and let G_i and F_i be expected first and second
    observation-cumulant derivatives under the current predictor distribution. With
    P_i=A+Z_i^T*diag(F_i)*Z_i and g_i=-A*(m_i-B_i*m)+Z_i^T*(y_i-G_i), propose Q_i_new=P_i^-1
    and m_i_new=m_i+Q_i_new*g_i, evaluating both derivatives at the same old local
    state and recomputing moments for another local iteration. The source uses a loose
    relative local-mean stopping criterion; this is not a certificate of an exact
    stationary local solution or maximizer. Proper globals and exact nonnegative Bernoulli/Poisson
    curvature yield positive local precision.
- assessment_id: expected-observation-curvature
  area: evidence
  topic: expected-observation-curvature
  outcome: supported
  target_ids:
  - AIMech:StochasticNonconjugateGLMMVariationalInference
  evidence_ids:
  - tan2014
  - tan2013
  - calculation
  summary: Mechanism or qualification is supported; one source-attribution defect
    is recorded separately.
  details: For a selected cluster the scalar predictor means and variances are t_i=V_i*m+Z_i*m_i
    and v_i=diag(V_i*Q*V_i^T+Z_i*Q_i*Z_i^T). With positive Poisson exposures E_i,
    G_i=F_i=E_i*exp(t_i+v_i/2), elementwise. For Bernoulli-logit, G_ij=E[sigmoid(t_ij+sqrt(v_ij)*Z0)]
    and F_ij=E[sigmoid(T)*(1-sigmoid(T))] for the same T and Z0~N(0,1). These are
    one-dimensional normal expectations, approximated by quadrature for logistic observations.
    The standard-normal density uses exp(-z^2/2)/sqrt(2*pi); the missing half in the
    2014 appendix display is qualified against the normalized construction and the
    2013 source.
- assessment_id: frozen-global-targets
  area: evidence
  topic: frozen-global-targets
  outcome: supported
  target_ids:
  - AIMech:StochasticNonconjugateGLMMVariationalInference
  evidence_ids:
  - tan2014
  - calculation
  summary: Mechanism or qualification is supported; one source-attribution defect
    is recorded separately.
  details: After selected local iterations, freeze the old global m,Q,Sq and the selected
    local factors for both global proposals. For minibatch B of size b, define P_hat=Sigma0^-1+(N/b)*sum_{i
    in B}[B_i^T*A*B_i+V_i^T*diag(F_i)*V_i], g_hat=-Sigma0^-1*m+(N/b)*sum_{i in B}[B_i^T*A*(m_i-B_i*m)+V_i^T*(y_i-G_i)],
    and h_hat=P_hat*m+g_hat. The covariance-factor target is S_hat=S+(N/b)*sum_{i
    in B}[(m_i-B_i*m)*(m_i-B_i*m)^T+Q_i+B_i*Q*B_i^T], with degrees nu+N. Global priors
    enter once; only cluster contributions are expanded. S_hat includes the local
    covariance Q_i, present in Appendix B Equation 21 but omitted in printed Algorithm
    2. Frozen global targets implement the simultaneous natural-gradient construction
    rather than silently reusing newly changed beta moments inside the other target.
- assessment_id: natural-parameter-mixing
  area: evidence
  topic: natural-parameter-mixing
  outcome: supported
  target_ids:
  - AIMech:StochasticNonconjugateGLMMVariationalInference
  evidence_ids:
  - tan2014
  - calculation
  summary: Mechanism or qualification is supported; one source-attribution defect
    is recorded separately.
  details: Choose 0<rho<=1 and write P_old=Q^-1 and h_old=P_old*m. Mix the Gaussian
    natural coordinates as P_new=(1-rho)*P_old+rho*P_hat and h_new=(1-rho)*h_old+rho*h_hat;
    then Q_new=P_new^-1 and m_new=Q_new*h_new=m+rho*Q_new*g_hat. Mix the inverse-Wishart
    scale as Sq_new=(1-rho)*Sq+rho*S_hat, keeping nuq=nu+N. This is not ordinary arithmetic
    averaging of Gaussian covariance matrices or means. Positive-definite old/target
    precisions and scales make this convex natural step proper. The source derives
    it from stochastic natural-gradient ascent; proper factors alone do not guarantee
    ELBO ascent or convergence.
- assessment_id: sampling-and-profile-boundary
  area: evidence
  topic: sampling-and-profile-boundary
  outcome: supported
  target_ids:
  - AIMech:StochasticNonconjugateGLMMVariationalInference
  evidence_ids:
  - tan2014
  - calculation
  summary: Mechanism or qualification is supported; one source-attribution defect
    is recorded separately.
  details: 'At a frozen global state, assume each cluster contribution is evaluated
    by the same specified local-solution rule. A fresh uniform subset of b clusters
    gives an unbiased N/b-scaled sum for the corresponding full sum; independent uniform
    draws with replacement also do so when repeated draws are counted with multiplicity.
    To identify that sum as the gradient of an optimized-local ELBO additionally requires
    the envelope argument’s differentiable stationary local solution and regularity.
    Approximate local solves, history-dependent warm starts or biased quadrature need
    separate error assessment. The source implementation description instead shuffles
    clusters into a sweep and samples from those remaining: its next-batch estimate
    is not generally conditionally unbiased at the changing current state under the
    fresh-subset argument. This does not by itself prove reshuffling fails; it limits
    the unbiased-gradient/convergence claim.'
- assessment_id: schedule-and-hybrid-scope
  area: evidence
  topic: schedule-and-hybrid-scope
  outcome: supported
  target_ids:
  - AIMech:StochasticNonconjugateGLMMVariationalInference
  evidence_ids:
  - tan2014
  summary: Mechanism or qualification is supported; one source-attribution defect
    is recorded separately.
  details: The source discusses diminishing gains rho_t=a/(t+A)^alpha with 1/2<alpha<=1
    and later uses a sweep-count clock, and optionally switches to the full-data procedure
    when an attained-bound progress criterion is small. The schedule must be defined
    at the initial index and respect the factor-domain requirement; Robbins–Monro
    summability is only part of the regularity conditions needed for convergence.
    A finite hybrid switching/stopping rule does not establish stationary or globally
    optimal inference, and its reported runtime belongs to that hybrid experiment.
    This record does not certify a streaming population-size rule, constant-memory
    implementation, author software or the separate prior-likelihood conflict diagnostic.
- assessment_id: global-state
  area: consistency
  topic: Simultaneous old-global evaluation and complete covariance moments
  outcome: supported
  target_ids:
  - AIMech:StochasticNonconjugateGLMMVariationalInference
  evidence_ids:
  - tan2014
  - calculation
  summary: The target and damping equations agree with the source derivation.
  details: Equation11 explicitly evaluates both global targets at current globals.
    Gaussian natural coordinates give hhat=Phat*m+ghat and newm=m+rho*newQ*ghat; independent
    finite arithmetic agrees within2.8e-17. AppendixB Equation21 includes Qi, unlike
    Algorithm2. Its omission changes the supplied one-step scale by [[.243,-.018],[-.018,.315]].
    Proper prior scale plus nonnegative covariance contributions gives a proper IW
    target; nuq=nu+N satisfies normalization. This does not prove convergence or certify
    the pseudocode.
- assessment_id: sampling
  area: consistency
  topic: Frozen finite-population sums versus profiled optimization and reshuffling
  outcome: supported
  target_ids:
  - AIMech:StochasticNonconjugateGLMMVariationalInference
  evidence_ids:
  - tan2014
  - calculation
  summary: Unbiasedness is qualified to the appropriate sampling and local-rule assumptions.
  details: Enumerating all uniform N=3,b=2 subsets and iid multisets gives target
    means agreeing with full sums within8.9e-16 at fixed supplied factors. Repeated
    draws count with multiplicity. Those factors were not optimized, so this is not
    an envelope-theorem or gradient-profile test. With fixed scores[1,2,7], fresh
    singleton rescaling averages10, while conditional resampling from the two remaining
    after index0 averages13.5. This refutes a general conditional-unbiased claim for
    source reshuffling, without proving algorithmic failure. Approximate local solves
    and quadrature are explicitly unverified error sources.
- assessment_id: factor-domain
  area: consistency
  topic: Expected cumulants, finite gain and schedule limits
  outcome: supported
  target_ids:
  - AIMech:StochasticNonconjugateGLMMVariationalInference
  evidence_ids:
  - tan2014
  - tan2013
  - calculation
  summary: The stated equations use normalized Gaussian moments and preserve proper
    natural-coordinate domains.
  details: Poisson G/F include exp(t+v/2); logistic expectations use normalized standard-normal
    weights and F>=0. The printed malformed Gaussian weight integrates to1/sqrt(2),
    not1. Convex precision/scale mixing with0<rho<=1 remains proper, without ELBO-ascent
    guarantees. The source uses a fractional sweep clock and hybrid switching; undefined
    initial gain or finite stopping thresholds supply no convergence theorem. Record
    scope is finiteN, without a streaming or constant-memory claim.
- assessment_id: complete-fields
  area: provenance
  topic: All fields, source versions and DRAFT scope
  outcome: supported
  target_ids:
  - AIMech:StochasticNonconjugateGLMMVariationalInference
  evidence_ids:
  - identity
  - mapping
  - tan2014
  - tan2013
  - calculation
  summary: All fields were inspected; one bounded source-attribution clarification
    is required.
  details: Read identity/name/empty aliases, kind, definition/citation, identity context,
    all seven claim statements/locators, both source metadata/access/hash, AIO snapshot/mapping,
    six limitations and real timestamps. The discovery report mirrors the exact YAML
    and captured context hashes agree. Full primary access does not imply implementation
    access. No fitting or clinical/general performance result is asserted. The normalization
    formula is correct, but the cited supporting2013 display is itself malformed and
    must be distinguished from its correct appendix.
- assessment_id: normalization-attribution
  area: evidence
  topic: Distinguish repeated display error from normalized appendix
  outcome: concern
  target_ids:
  - AIMech:StochasticNonconjugateGLMMVariationalInference
  evidence_ids:
  - normalization-attribution
  - tan2013
  - tan2014
  summary: Qualify the2013 display as well as the2014 display.
  details: The mathematical expectation is supported by the normalized2013 AppendixB,
    so no mechanism rewrite is needed. Explicitly identify the shared missing-half
    error in2013 Section4.3/PDF8 and2014 AppendixB/PDF37; narrow the supporting normalized
    locator to2013 AppendixB/PDF19–20.
findings:
- finding_id: F1
  issue_key: aimech-stochastic-glmm-normalization-source-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Distinguish the 2013 malformed normal-weight display from its normalized
    appendix
  description: The logistic-curvature claim cites2013 Section4.3/PDF8 and AppendixB/PDF19–20
    jointly as normalized Gaussian expectations, while explicitly flagging only the2014
    display. The2013 p.8 display repeats exp(-x^2)/sqrt(2pi); its AppendixB uses the
    correct standard-normal density. State both display discrepancies and identify
    AppendixB as the normalized source. The curated expectation itself is already
    correct. Synchronize the discovery report and rendered page.
  target_ids:
  - AIMech:StochasticNonconjugateGLMMVariationalInference
  field_paths:
  - claims[2].statement
  - claims[2].evidence[1].locator
  - limitations[1]
  evidence_ids:
  - normalization-attribution
  - tan2013
  - tan2014
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/StochasticNonconjugateGLMMVariationalInference.yaml
    role: maintained
actions:
- action_id: A1
  description: Clarify both malformed displays and the supporting normalized appendix;
    synchronize derived content, append actual history and save a linked successor.
  finding_ids:
  - F1
  target_ids:
  - AIMech:StochasticNonconjugateGLMMVariationalInference
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/StochasticNonconjugateGLMMVariationalInference.yaml
    role: maintained
  acceptance_checks:
  - 2013PDF8 and2014PDF37 are explicitly distinguished from normalized2013AppendixB19–20.
  - Correct mathematical expectations, identity and mapping remain unchanged.
  - Validation and a linked successor review pass.
limitations:
- Author self-review only; no independent approval or status promotion. The one minor
  finding concerns source attribution, not the mathematical normal expectation. The
  initial sandboxed vendor fetch failed DNS; authorized network retry passed22 artifacts.
  An initial check before rendering failed two stale-page tests; pages were regenerated
  and the full gate rerun.
- Added one DRAFT algorithm, yielding 556 native and 442 unchanged generated records.
  The 741-entry main frontier retains 484 pending and 57 partly addressed cohorts;
  additional nested leads remain pending.
- All 42 primary 2014 preprint pages and the supporting 21-page 2013 reprint were
  read. The reported clinical-data comparisons and simulated hybrid-fit timings are
  not curated as clinical conclusions or general accuracy/speed guarantees. Source
  minibatch percentages contain decimal errors; finite-population weights here use
  actual N and b. No fitting, author implementation, diagnostic calibration study
  or benchmark was run.
- Independent arithmetic checks fixed supplied local Gaussian factors, all uniform
  subsets/iid draw multisets in a tiny example and one simultaneous global step. Those
  local factors were not optimized, so this is not a numerical test of the envelope
  theorem, a profiled-gradient reproduction or convergence. DRAFT remains.
- Original-checkout synchronization and old round141 cleanup remain pending explicit
  approval after automatic review rejection; isolated recovery work only.
related_reviews: []
links: []
tags:
- native-concepts
- mixed-models
- variational-inference
- self-review
- discovery-ongoing
```
