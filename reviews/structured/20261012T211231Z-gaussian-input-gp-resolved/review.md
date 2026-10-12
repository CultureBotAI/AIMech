# Scientific author self-review of Gaussian-input GP moments: resolved

- Review: 20261012T211231Z-gaussian-input-gp-resolved
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T21:08:42Z
- Finished UTC: 2026-10-12T21:12:31Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The Gaussian-input moment algorithm remains supported within its stated limits; the six citation locators are corrected and the sole review finding is resolved.

## Scope And Provenance

All fields of GaussianProcessGaussianInputMomentMatching and its claim evidence.

Selection: Exact maintained ID: AIMech:GaussianProcessGaussianInputMomentMatching
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 33b285829394f923f9e72bf9e6a62e39935710ac.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:GaussianProcessGaussianInputMomentMatching | data/curated/GaussianProcessGaussianInputMomentMatching.yaml | maintained | Gaussian-process moment matching for Gaussian inputs |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:GaussianProcessGaussianInputMomentMatching | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 111.05s (0:01:51)<br>Checked 442 record(s); 0 failed.<br>Checked 541 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 189 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 187,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:GaussianProcessGaussianInputMomentMatching | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:GaussianProcessGaussianInputMomentMatching | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:GaussianProcessGaussianInputMomentMatching | Exited0 without output. |
| Gaussian-input boundary calculations | passed | True | AIMech:GaussianProcessGaussianInputMomentMatching | {"scope": "Analytic and quadrature curator illustrations, not fitted source models or benchmark replication.", "rbf_kernel_moments": {"input_mean": 0.4, "input_variance": 0.7, "training_locations": [-1.0, 1.0], "q": [0.43094073084886136, 0.6899083760976416], "Q": [[0.2852466497288544, 0.22215031417732647], [0.22215031417732647, 0.5555846097736892]], "maximum_quadrature_error": 5.88418203051333e-15}, "zero_input_variance": {"q": [0.37531109885139957, 0.835270211411272], "Q": [[0.14085842092104503, 0.31348618088260527], [0.31348618088260527, 0.697676326071031]]}, "non_gaussian_mixture": {"variance": 0.42264973081037416, "fourth_moment": 0.8775391713621188, "matched_gaussian_fourth_moment": 0.5358983848622452}, "variance_need_not_increase": {"value_only_at_mean": 0.9816843611112658, "integrated_input": 0.8478121213512702}, "taylor_invalid_variance": {"input_mean": 1, "input_variance": 2, "taylor_variance": -0.103638323514327, "exact_mixture_variance": 0.6338524761696075}, "shared_function_dependence": {"shared_coefficient_second_step": {"mean": 1, "variance": 2}, "independent_redraw_second_step": {"mean": 0, "variance": 1}}, "limits": ["The q/Q check uses the one-dimensional unit squared-exponential kernel and fixed Gaussian input parameters.", "The linear-kernel shared-function example illustrates an additional dependence assumption, not a numerical reproduction of the squared-exponential benchmark.", "Gaussian matching preserves the first two moments under its stated mixture law, not the entire distribution or arbitrary multistep dependence.", "Taylor negativity is a deliberately nonlocal example and does not refute the small-uncertainty approximation within its regime."]} |

## Scientific And Domain Assessments

### Exact input integration versus generic priors and local approximations

identity: supported. Targets: AIMech:GaussianProcessGaussianInputMomentMatching.

Retain the scoped Gaussian-input moment-matching algorithm.

The definition specifies a squared-exponential GP posterior, prescribed Gaussian test inputs and exact first-two-moment Gaussian matching. Generic GPR, EP site approximation, random-mask DropConnect, derivative observations and a local Taylor method do not denote that procedure. Names and alias do not claim all uncertain-input GP methods are equivalent; the body distinguishes the iterative application and its further dependence assumptions.

### Regression and forecasting task relations

grounding: supported. Targets: AIMech:GaussianProcessGaussianInputMomentMatching.

Both related mappings fit the stated application scope.

RegressionAnalysis provides response-prediction context. TimeSeriesForecasting is the primary source’s explicitly developed multi-step application. Neither related_match asserts equivalence or upstream is-a. Processing/demographic bias nodes are not methods for integration, GLM imposes a different model structure, and the generic time-series task is redundant with the more specific mapping.

### mixture-moments

evidence: supported. Targets: AIMech:GaussianProcessGaussianInputMomentMatching.

The scientific statement is supported under its explicit assumptions.

Let X have a prescribed Gaussian distribution independent of the latent GP posterior, conditional on the training data and fixed hyperparameters. Integrating p(f(x)&#124;x,data) over this input law gives a generally non-Gaussian mixture. Its mean is E_X[m(X)] and its variance is E_X[v(X)]+Var_X[m(X)], where m and v are the fixed-input latent posterior mean and variance. Replacing this mixture by a Gaussian with those moments is a distributional approximation, even when both moments are evaluated exactly. Corrected section/equation/page locators were reread against the source.

### squared-exponential-integrals

evidence: supported. Targets: AIMech:GaussianProcessGaussianInputMomentMatching.

The scientific statement is supported under its explicit assumptions.

For the paper’s zero-mean, unit-amplitude squared-exponential GP with Gaussian observation noise, write beta=K_y^{-1}y, k_X for covariances between the training inputs and X, q=E[k_X], and Q=E[k_X k_X^T]. Then the latent predictive mean is q^T beta and variance is 1-tr(K_y^{-1}Q)+beta^T Q beta-(q^T beta)^2. Gaussian integration supplies closed forms for q and Q. For the one-dimensional unit-lengthscale kernel and X~N(mu,s), q_i=exp(-(mu-x_i)^2/(2(1+s)))/sqrt(1+s) and Q_ij=exp(-(x_i-x_j)^2/4-(mu-(x_i+x_j)/2)^2/(1+2s))/sqrt(1+2s), with s denoting input variance. The zero-input-variance limit recovers ordinary fixed-input prediction. These exact moment statements condition on the specified kernel, data and hyperparameters. Corrected section/equation/page locators were reread against the source.

### forecasting-extension

evidence: supported. Targets: AIMech:GaussianProcessGaussianInputMomentMatching.

The scientific statement is supported under its explicit assumptions.

For iterative autoregressive forecasting, the source carries a joint Gaussian approximation to the lagged outputs, computes the next scalar output moments and its cross-covariances with the existing lags, and shifts the resulting covariance block. Full lag covariance is part of that construction; independently propagating only marginal variances is a different approximation. When the predicted quantity is a future noisy observation, add its independent observation-noise variance once to the new output diagonal. Gaussian moment closure and treating the current input distribution as independent of the uncertain GP function are additional assumptions; retained lag covariance alone does not make the complete shared-function trajectory posterior exact. Corrected section/equation/page locators were reread against the source.

### taylor-boundary

evidence: supported. Targets: AIMech:GaussianProcessGaussianInputMomentMatching.

The scientific statement is supported under its explicit assumptions.

The earlier first-order posterior-mean and second-order posterior-variance Taylor construction approximates the same total-moment integrals locally; it is not the closed-form squared-exponential Gaussian integral. The technical report explicitly leaves exact evaluation of those moments to future work. Curator boundary calculations show why the distinction matters: with the unit kernel, an exact observation f(0)=0, input mean 1 and input variance 2, the local Taylor variance is 1-3/e&lt;0, whereas the exact mixture variance is 1-exp(-1/5)/sqrt(5)&gt;0. This deliberately nonlocal example is not a reproduction of the paper’s benchmark or a rejection of the approximation within its small-uncertainty regime. Corrected section/equation/page locators were reread against the source.

### shared-function-limit

evidence: supported. Targets: AIMech:GaussianProcessGaussianInputMomentMatching.

The scientific statement is supported under its explicit assumptions.

In a trajectory generated by a single uncertain GP dynamics function, later inputs generally depend on that same function. Repeated independent-input moment calculations do not preserve this dependence. Hewing and colleagues explicitly identify this issue in established GP trajectory prediction, including the Girard construction. A curator linear-kernel illustration uses f(x)=A*x with A~N(0,1) and x_0=1: reusing A gives x_2=A^2 with mean 1 and variance 2, while independently redrawing A at each step gives a product with mean 0 and variance 1. This illustrates a change in the modeled law, not a squared-exponential benchmark replication or a universal direction of variance error. Corrected section/equation/page locators were reread against the source.

### Kernel expectations and distributional approximation

consistency: supported. Targets: AIMech:GaussianProcessGaussianInputMomentMatching.

Exact moments and Gaussian distributional approximation remain separate.

Total variance gives1-tr(K_y^-1 Q)+beta^T Q beta-(q^T beta)^2. Direct one-dimensional Gaussian integration agrees with independent Simpson quadrature to approximately5.9e-15 and the degenerate input limit reproduces the fixed-input kernel. Under f0=0 and X~N0,1 the mixture’s fourth moment differs from3v², proving the matched Gaussian need not equal that law. The latent/future-noisy-output distinction and fixed hyperparameters are explicit.

### Taylor variance and temporal dependence

scope: supported. Targets: AIMech:GaussianProcessGaussianInputMomentMatching.

The counterexamples are qualified curator calculations.

The large input-variance Taylor example gives1-3/e&lt;0 while exact integrated variance ispositive. This is not evidence against a justified local approximation. The persistent coefficient example givesA² rather thanA1*A2; it demonstrates missing state/function dependence, not a squared-exponential experimental reproduction. Full lag covariance alone does not retain that dependence. Input integration need not increase variance versus evaluating only at the input mean.

### Illustrative source results and unresolved metadata

scope: supported. Targets: AIMech:GaussianProcessGaussianInputMomentMatching.

The record avoids unsupported universal performance and calibration claims.

The pH proceedings test-count placeholder is not filled from an earlier report with different preprocessing/results. No code, fitted model or stochastic trajectory simulation was run. The exact-kernel method, local Taylor approximation and correlation-aware proposals are separately scoped. Singular initial input covariance and width-parameter notation remain explicit implementation limits.

### Complete record fields and report consistency

provenance: supported. Targets: AIMech:GaussianProcessGaussianInputMomentMatching.

All maintained fields and corrected evidence locations are consistent.

Read stableID,name,one descriptive alias,algorithm kind,definition,identity search,five claims,three exact source versions/access times/hashes,pinned AIO snapshot,two related mappings,six limitations,DRAFT status and actual curation timestamps. The discovery report entry equals the YAML. The two2002publications have distinct authorship and methods; PMLR2020 metadata page range differs from its printedPDFindices and the record usesPDFindices.

### Section and equation label audit

evidence: supported. Targets: AIMech:GaussianProcessGaussianInputMomentMatching.

All six corrected citation locator strings now match the papers.

Definition and random-input moments citeSections3–3.1; fixed prediction citesSections2.1–2.2; forecasting citesSection4 and the unnumbered lag covariance paragraph; Taylor citesNIPS3.1 and report3.2–3.4. PDF indices and actual equations were checked visually.

## Findings

### source-locators: Correct Gaussian-input GP section and equation locators

minor / resolved / confirmed; issue key: aimech-gaussian-input-gp-source-locators.

The NIPS paper places random-input prediction in Section3 and Gaussian moments in3.1, not2/2.2. Fixed-input GP formulas are in2.1–2.2, not1. Iterative forecasting is Section4 onPDF4–5; Equation14 belongs to the Monte-Carlo alternative onPDF4, not lag-covariance propagation. The Taylor report has Sections3.2–3.4 onPDF8–9, notSection4. Correct the definition and five claim-evidence locator strings across both papers; retain the supported statements and synchronized report mirror.

Disposition: Corrected all six source locators in the maintained record and discovery mirror, appended actual correction history, regenerated pages, reread the changed input bytes against rendered source labels and reran required checks. Scientific claims and method identity are unchanged.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T210207Z-gaussian-input-gp-moments.json | supports | Compared all 442 pinned AIO IDs, labels and scoped synonyms and 540 native IDs, names and aliases against the proposed ID/name, descriptive alias, uncertain-input and GP-moment terminology: no normalized identity match. Ignored- and hidden-inclusive full-text searches in the recovery, older discovery and original Documents checkouts returned 60, 47 and 46 lines. All ten distinct matched text strings were read in full; they concern pending GP source leads, EP or DropConnect moment approximations, and neighboring derivative GP records. Read all 37 semantic AIO rows, 76 native name/definition neighbors, six full annotated AIO CLASS nodes with incident edges and generated records, and four complete contextual native records. The procedure integrates a prescribed Gaussian test-input law against a fixed squared-exponential GP posterior and matches the resulting first two moments. It is narrower than generic GP regression and is not EP site matching, DropConnect prediction, a derivative-observation method, or the earlier local Taylor approximation. Iterative forecasting uses the procedure with additional Gaussian and temporal-independence approximations. Absence is bounded to the inspected pin and record corpus; no universal uncertain-input-GP alias is asserted. |
| mapping | sources/aio/aio.json | supports | Read37semantic AIO rows,76native neighbors,six complete annotated CLASS nodes and incident edges/generated records,four complete native contextual records. Regression and forecasting are explicit task/application relationships; bias and GLM matches are rejected. |
| calculation | research/discovery/uncertain-gp-boundaries.py | supports | Closed-form scalar q/Q match independent Simpson quadrature; zero-input-variance limits, non-Gaussian fourth moments, variance decrease, nonlocal Taylor negativity and shared-function dependence are explicit scoped calculations, not empirical source replication. |
| girard2002 | https://papers.nips.cc/paper_files/paper/2002/file/f3ac63c91272f19ce97c7397825cc15f-Paper.pdf; Sections2.1–2.2,Equations1–4,PDF2–3; Sections3–3.1,Equations5–13,PDF3–4; Section4 unnumbered lag-covariance construction,PDF4–5. Equation14 is the Monte-Carlo alternative in Section3.2 on PDF4. | supports | NIPS 2002, Advances in Neural Information Processing Systems 15; official eight-page unpaginated PDF, also cited as the 2003 volume. All eight pages, figures, table and references visually read; locators use PDF indices. The cited method passages and section/equation labels were visually reread after input capture. |
| girard-tr2002 | https://www.dcs.gla.ac.uk/~rod/publications/GirRasMur02-TR-2002-119.pdf; Sections3.2–3.4,Equations12–22,PDF8–9; conclusions PDF17. | supports | University of Glasgow Technical Report TR-2002-119, October 2002; all 18 PDF pages visually read, with matching printed page indices. Earlier Taylor method, distinct authorship and experiments from the four-author proceedings paper. The cited method passages and section/equation labels were visually reread after input capture. |
| hewing2020 | https://proceedings.mlr.press/v120/hewing20a/hewing20a.pdf; Introduction and Sections2–3,PDF1–4; all11pages including proposals,examples,references read. | supports | L4DC 2020, PMLR 120:424–434. All 11 official PDF pages visually read; PDF and printed indices are 1–11, which are used for locators. The cited method passages and section/equation labels were visually reread after input capture. |
| prior | reviews/structured/20261012T210627Z-gaussian-input-gp-open/review.yaml | context_only | Immutable predecessor scientific review with the confirmed citation-locator finding. |

## Limits And Additional Notes

- Author self-review only; the record remains DRAFT.
- The first restricted-network vendored check failed to resolve the public host; a permitted read-only retry verified all22pinned artifacts.
- Added one native DRAFT algorithm, bringing the total to541 with442 unchanged generated records. Discovery remains active:484 pending and54 partly addressed cohorts plus other unresolved scopes; no saturation claim.
- Read all8NIPS2002 pages, all18earlier-report pages, and all11Hewing2020 pages, including figures, tables and references. The36-page local-linear GP report is downloaded but only partially accessed; it is not primary support for the curated record.
- Analytic examples and independent scalar numerical quadrature were executed. No source implementation, fitted model, stochastic simulation, paid provider or benchmark was executed. Exact moments are separated from a Gaussian law and shared-function trajectory independence.
- Original Documents checkout was read in ignored-inclusive identity searches. Original synchronization and old round141 cleanup still await explicit approval after automatic review rejected the combined action.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T211231Z-gaussian-input-gp-resolved
kind: record
repository: CultureBotAI/AIMech
title: 'Scientific author self-review of Gaussian-input GP moments: resolved'
started_at: '2026-10-12T21:08:42Z'
finished_at: '2026-10-12T21:12:31Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent challenged identity,mappings,moment formulas,distributional
    assumptions,source locators and temporal-dependence claims. This is author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The Gaussian-input moment algorithm remains supported within its stated limits;
  the six citation locators are corrected and the sole review finding is resolved.
source:
  git_revision: 33b285829394f923f9e72bf9e6a62e39935710ac
  state: working_tree
  inputs:
  - path: data/aio/ErrorPropagationBias.yaml
    sha256: 98a57881fa8f2a8f47efdf37f12f8dbcc66df495112e46c454d26cf4d934c5e4
    role: context
  - path: data/aio/GeneralizedLinearModel.yaml
    sha256: 202002ec50c6e6207bc2fefba5baeab233514fd8f9118a623d1917b599ce2c7d
    role: context
  - path: data/aio/RegressionAnalysis.yaml
    sha256: 6f5d48096556a2ec31770aab306219e9020919940b4e80554639cc97aaa94bc6
    role: context
  - path: data/aio/TimeSeriesAnalysis.yaml
    sha256: c26b267d0f5fb895e9cb0eb587fe86a115d461dae4d70e0ac6baf1eefb1d4eff
    role: context
  - path: data/aio/TimeSeriesForecasting.yaml
    sha256: 88bbef37663508cc885b40d258cdb6b720c627c0f73af1935c01a372c18b3863
    role: context
  - path: data/aio/UncertaintyBias.yaml
    sha256: b013064a48a14beef5040486a8d1cbd11d9c503739d6fc89f73460b08f38e8f3
    role: context
  - path: data/curated/DerivativeObservationGaussianProcessRegression.yaml
    sha256: 888850faa100e14b96057c516e7d65d01ed2932a142577d101660c73dbf90905
    role: context
  - path: data/curated/DropConnect.yaml
    sha256: 4785777508a6f24792c7533279a08eb66977144b62a260eb26f1d0fbdad1b356
    role: context
  - path: data/curated/GaussianProcessGaussianInputMomentMatching.yaml
    sha256: 1ee8ce71dc9dd12e404033168e575cb0628cc2f377e9c3efe4189962ae9378d3
    role: target
  - path: data/curated/GaussianProcessRegression.yaml
    sha256: d83d0de4a152e7db689636928f41eb5d3663281285585d835f2a5535403d6a0d
    role: context
  - path: data/curated/MonotonicGaussianProcessWithVirtualDerivatives.yaml
    sha256: 9b72af4401c813c1fb3d51aa894a080ca96b86b37a051d8e7bb86a73b54e9cfd
    role: context
  - path: research/discovery/20261012T210207Z-gaussian-input-gp-moments.json
    sha256: 6091e73607c9710bb0f741f801f6ada60abd231d5a89061757fd0ee27969b46c
    role: context
  - path: research/discovery/uncertain-gp-boundaries.py
    sha256: 98951f1b89fbac7092cef4c2524d294ee466be7eb7616f303e111db6cee189ab
    role: context
  - path: reviews/structured/20261012T210627Z-gaussian-input-gp-open/review.yaml
    sha256: 1cd9af343f04911e8cfdc402530675349de327c7dadb25da7accd0c96d89205d
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
- target_id: AIMech:GaussianProcessGaussianInputMomentMatching
  path: data/curated/GaussianProcessGaussianInputMomentMatching.yaml
  label: Gaussian-process moment matching for Gaussian inputs
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GaussianProcessGaussianInputMomentMatching.yaml
    role: maintained
scope:
  description: All fields of GaussianProcessGaussianInputMomentMatching and its claim
    evidence.
  selection: 'Exact maintained ID: AIMech:GaussianProcessGaussianInputMomentMatching'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:GaussianProcessGaussianInputMomentMatching
  exclusions:
  - target: Taylor,correlation-aware trajectory,filtering and sparse-spectrum concept
      additions
    reason: Their own identity and mapping audits are pending.
  - target: Implementation and empirical replication
    reason: Paper reading and curator mathematical/quadrature checks only.
  - target: Contextual generated/native neighbors
    reason: Identity and mapping context,not full scientific rereview.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:GaussianProcessGaussianInputMomentMatching
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 111.05s (0:01:51)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 541 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 189 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 187,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:GaussianProcessGaussianInputMomentMatching
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
  - AIMech:GaussianProcessGaussianInputMomentMatching
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
  - AIMech:GaussianProcessGaussianInputMomentMatching
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculations
  name: Gaussian-input boundary calculations
  command: python3 research/discovery/uncertain-gp-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:GaussianProcessGaussianInputMomentMatching
  exit_code: 0
  expected_exit_code: 0
  summary: '{"scope": "Analytic and quadrature curator illustrations, not fitted source
    models or benchmark replication.", "rbf_kernel_moments": {"input_mean": 0.4, "input_variance":
    0.7, "training_locations": [-1.0, 1.0], "q": [0.43094073084886136, 0.6899083760976416],
    "Q": [[0.2852466497288544, 0.22215031417732647], [0.22215031417732647, 0.5555846097736892]],
    "maximum_quadrature_error": 5.88418203051333e-15}, "zero_input_variance": {"q":
    [0.37531109885139957, 0.835270211411272], "Q": [[0.14085842092104503, 0.31348618088260527],
    [0.31348618088260527, 0.697676326071031]]}, "non_gaussian_mixture": {"variance":
    0.42264973081037416, "fourth_moment": 0.8775391713621188, "matched_gaussian_fourth_moment":
    0.5358983848622452}, "variance_need_not_increase": {"value_only_at_mean": 0.9816843611112658,
    "integrated_input": 0.8478121213512702}, "taylor_invalid_variance": {"input_mean":
    1, "input_variance": 2, "taylor_variance": -0.103638323514327, "exact_mixture_variance":
    0.6338524761696075}, "shared_function_dependence": {"shared_coefficient_second_step":
    {"mean": 1, "variance": 2}, "independent_redraw_second_step": {"mean": 0, "variance":
    1}}, "limits": ["The q/Q check uses the one-dimensional unit squared-exponential
    kernel and fixed Gaussian input parameters.", "The linear-kernel shared-function
    example illustrates an additional dependence assumption, not a numerical reproduction
    of the squared-exponential benchmark.", "Gaussian matching preserves the first
    two moments under its stated mixture law, not the entire distribution or arbitrary
    multistep dependence.", "Taylor negativity is a deliberately nonlocal example
    and does not refute the small-uncertainty approximation within its regime."]}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T210207Z-gaussian-input-gp-moments.json
  accessed_at: '2026-10-12T21:08:42Z'
  support: supports
  summary: 'Compared all 442 pinned AIO IDs, labels and scoped synonyms and 540 native
    IDs, names and aliases against the proposed ID/name, descriptive alias, uncertain-input
    and GP-moment terminology: no normalized identity match. Ignored- and hidden-inclusive
    full-text searches in the recovery, older discovery and original Documents checkouts
    returned 60, 47 and 46 lines. All ten distinct matched text strings were read
    in full; they concern pending GP source leads, EP or DropConnect moment approximations,
    and neighboring derivative GP records. Read all 37 semantic AIO rows, 76 native
    name/definition neighbors, six full annotated AIO CLASS nodes with incident edges
    and generated records, and four complete contextual native records. The procedure
    integrates a prescribed Gaussian test-input law against a fixed squared-exponential
    GP posterior and matches the resulting first two moments. It is narrower than
    generic GP regression and is not EP site matching, DropConnect prediction, a derivative-observation
    method, or the earlier local Taylor approximation. Iterative forecasting uses
    the procedure with additional Gaussian and temporal-independence approximations.
    Absence is bounded to the inspected pin and record corpus; no universal uncertain-input-GP
    alias is asserted.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-12T21:08:42Z'
  support: supports
  summary: Read37semantic AIO rows,76native neighbors,six complete annotated CLASS
    nodes and incident edges/generated records,four complete native contextual records.
    Regression and forecasting are explicit task/application relationships; bias and
    GLM matches are rejected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/uncertain-gp-boundaries.py
  accessed_at: '2026-10-12T21:08:42Z'
  snapshot_sha256: 98951f1b89fbac7092cef4c2524d294ee466be7eb7616f303e111db6cee189ab
  support: supports
  summary: Closed-form scalar q/Q match independent Simpson quadrature; zero-input-variance
    limits, non-Gaussian fourth moments, variance decrease, nonlocal Taylor negativity
    and shared-function dependence are explicit scoped calculations, not empirical
    source replication.
- evidence_id: girard2002
  kind: primary_source
  reference: https://papers.nips.cc/paper_files/paper/2002/file/f3ac63c91272f19ce97c7397825cc15f-Paper.pdf
  locator: Sections2.1–2.2,Equations1–4,PDF2–3; Sections3–3.1,Equations5–13,PDF3–4;
    Section4 unnumbered lag-covariance construction,PDF4–5. Equation14 is the Monte-Carlo
    alternative in Section3.2 on PDF4.
  accessed_at: '2026-10-12T20:50:31Z'
  snapshot_sha256: b8b19f828d8d796566549d0ddbda746b04868af65c5af9d9a2a8fc978c9da7aa
  support: supports
  summary: NIPS 2002, Advances in Neural Information Processing Systems 15; official
    eight-page unpaginated PDF, also cited as the 2003 volume. All eight pages, figures,
    table and references visually read; locators use PDF indices. The cited method
    passages and section/equation labels were visually reread after input capture.
- evidence_id: girard-tr2002
  kind: primary_source
  reference: https://www.dcs.gla.ac.uk/~rod/publications/GirRasMur02-TR-2002-119.pdf
  locator: Sections3.2–3.4,Equations12–22,PDF8–9; conclusions PDF17.
  accessed_at: '2026-10-12T20:50:34Z'
  snapshot_sha256: f2e78afd674d4a4224933b3b4c0e4656a93553491a65ffcd4f118b7d740d006b
  support: supports
  summary: University of Glasgow Technical Report TR-2002-119, October 2002; all 18
    PDF pages visually read, with matching printed page indices. Earlier Taylor method,
    distinct authorship and experiments from the four-author proceedings paper. The
    cited method passages and section/equation labels were visually reread after input
    capture.
- evidence_id: hewing2020
  kind: primary_source
  reference: https://proceedings.mlr.press/v120/hewing20a/hewing20a.pdf
  locator: Introduction and Sections2–3,PDF1–4; all11pages including proposals,examples,references
    read.
  accessed_at: '2026-10-12T20:55:19Z'
  snapshot_sha256: e03bc1f123643b8ae5607d096b0ac94aacb5fa0bb1ea425aa50f7ea5c7e412ce
  support: supports
  summary: L4DC 2020, PMLR 120:424–434. All 11 official PDF pages visually read; PDF
    and printed indices are 1–11, which are used for locators. The cited method passages
    and section/equation labels were visually reread after input capture.
- evidence_id: prior
  kind: record_content
  reference: reviews/structured/20261012T210627Z-gaussian-input-gp-open/review.yaml
  accessed_at: '2026-10-12T21:08:42Z'
  support: context_only
  summary: Immutable predecessor scientific review with the confirmed citation-locator
    finding.
assessments:
- assessment_id: identity
  area: identity
  topic: Exact input integration versus generic priors and local approximations
  outcome: supported
  target_ids:
  - AIMech:GaussianProcessGaussianInputMomentMatching
  evidence_ids:
  - identity
  - girard2002
  - girard-tr2002
  summary: Retain the scoped Gaussian-input moment-matching algorithm.
  details: The definition specifies a squared-exponential GP posterior, prescribed
    Gaussian test inputs and exact first-two-moment Gaussian matching. Generic GPR,
    EP site approximation, random-mask DropConnect, derivative observations and a
    local Taylor method do not denote that procedure. Names and alias do not claim
    all uncertain-input GP methods are equivalent; the body distinguishes the iterative
    application and its further dependence assumptions.
- assessment_id: grounding
  area: grounding
  topic: Regression and forecasting task relations
  outcome: supported
  target_ids:
  - AIMech:GaussianProcessGaussianInputMomentMatching
  evidence_ids:
  - mapping
  - girard2002
  summary: Both related mappings fit the stated application scope.
  details: RegressionAnalysis provides response-prediction context. TimeSeriesForecasting
    is the primary source’s explicitly developed multi-step application. Neither related_match
    asserts equivalence or upstream is-a. Processing/demographic bias nodes are not
    methods for integration, GLM imposes a different model structure, and the generic
    time-series task is redundant with the more specific mapping.
- assessment_id: mixture-moments
  area: evidence
  topic: mixture-moments
  outcome: supported
  target_ids:
  - AIMech:GaussianProcessGaussianInputMomentMatching
  evidence_ids:
  - girard2002
  - hewing2020
  - calculation
  summary: The scientific statement is supported under its explicit assumptions.
  details: Let X have a prescribed Gaussian distribution independent of the latent
    GP posterior, conditional on the training data and fixed hyperparameters. Integrating
    p(f(x)|x,data) over this input law gives a generally non-Gaussian mixture. Its
    mean is E_X[m(X)] and its variance is E_X[v(X)]+Var_X[m(X)], where m and v are
    the fixed-input latent posterior mean and variance. Replacing this mixture by
    a Gaussian with those moments is a distributional approximation, even when both
    moments are evaluated exactly. Corrected section/equation/page locators were reread
    against the source.
- assessment_id: squared-exponential-integrals
  area: evidence
  topic: squared-exponential-integrals
  outcome: supported
  target_ids:
  - AIMech:GaussianProcessGaussianInputMomentMatching
  evidence_ids:
  - girard2002
  - calculation
  summary: The scientific statement is supported under its explicit assumptions.
  details: For the paper’s zero-mean, unit-amplitude squared-exponential GP with Gaussian
    observation noise, write beta=K_y^{-1}y, k_X for covariances between the training
    inputs and X, q=E[k_X], and Q=E[k_X k_X^T]. Then the latent predictive mean is
    q^T beta and variance is 1-tr(K_y^{-1}Q)+beta^T Q beta-(q^T beta)^2. Gaussian
    integration supplies closed forms for q and Q. For the one-dimensional unit-lengthscale
    kernel and X~N(mu,s), q_i=exp(-(mu-x_i)^2/(2(1+s)))/sqrt(1+s) and Q_ij=exp(-(x_i-x_j)^2/4-(mu-(x_i+x_j)/2)^2/(1+2s))/sqrt(1+2s),
    with s denoting input variance. The zero-input-variance limit recovers ordinary
    fixed-input prediction. These exact moment statements condition on the specified
    kernel, data and hyperparameters. Corrected section/equation/page locators were
    reread against the source.
- assessment_id: forecasting-extension
  area: evidence
  topic: forecasting-extension
  outcome: supported
  target_ids:
  - AIMech:GaussianProcessGaussianInputMomentMatching
  evidence_ids:
  - girard2002
  - hewing2020
  - calculation
  summary: The scientific statement is supported under its explicit assumptions.
  details: For iterative autoregressive forecasting, the source carries a joint Gaussian
    approximation to the lagged outputs, computes the next scalar output moments and
    its cross-covariances with the existing lags, and shifts the resulting covariance
    block. Full lag covariance is part of that construction; independently propagating
    only marginal variances is a different approximation. When the predicted quantity
    is a future noisy observation, add its independent observation-noise variance
    once to the new output diagonal. Gaussian moment closure and treating the current
    input distribution as independent of the uncertain GP function are additional
    assumptions; retained lag covariance alone does not make the complete shared-function
    trajectory posterior exact. Corrected section/equation/page locators were reread
    against the source.
- assessment_id: taylor-boundary
  area: evidence
  topic: taylor-boundary
  outcome: supported
  target_ids:
  - AIMech:GaussianProcessGaussianInputMomentMatching
  evidence_ids:
  - girard2002
  - girard-tr2002
  - calculation
  summary: The scientific statement is supported under its explicit assumptions.
  details: 'The earlier first-order posterior-mean and second-order posterior-variance
    Taylor construction approximates the same total-moment integrals locally; it is
    not the closed-form squared-exponential Gaussian integral. The technical report
    explicitly leaves exact evaluation of those moments to future work. Curator boundary
    calculations show why the distinction matters: with the unit kernel, an exact
    observation f(0)=0, input mean 1 and input variance 2, the local Taylor variance
    is 1-3/e<0, whereas the exact mixture variance is 1-exp(-1/5)/sqrt(5)>0. This
    deliberately nonlocal example is not a reproduction of the paper’s benchmark or
    a rejection of the approximation within its small-uncertainty regime. Corrected
    section/equation/page locators were reread against the source.'
- assessment_id: shared-function-limit
  area: evidence
  topic: shared-function-limit
  outcome: supported
  target_ids:
  - AIMech:GaussianProcessGaussianInputMomentMatching
  evidence_ids:
  - hewing2020
  - calculation
  summary: The scientific statement is supported under its explicit assumptions.
  details: 'In a trajectory generated by a single uncertain GP dynamics function,
    later inputs generally depend on that same function. Repeated independent-input
    moment calculations do not preserve this dependence. Hewing and colleagues explicitly
    identify this issue in established GP trajectory prediction, including the Girard
    construction. A curator linear-kernel illustration uses f(x)=A*x with A~N(0,1)
    and x_0=1: reusing A gives x_2=A^2 with mean 1 and variance 2, while independently
    redrawing A at each step gives a product with mean 0 and variance 1. This illustrates
    a change in the modeled law, not a squared-exponential benchmark replication or
    a universal direction of variance error. Corrected section/equation/page locators
    were reread against the source.'
- assessment_id: moment-law
  area: consistency
  topic: Kernel expectations and distributional approximation
  outcome: supported
  target_ids:
  - AIMech:GaussianProcessGaussianInputMomentMatching
  evidence_ids:
  - girard2002
  - calculation
  summary: Exact moments and Gaussian distributional approximation remain separate.
  details: Total variance gives1-tr(K_y^-1 Q)+beta^T Q beta-(q^T beta)^2. Direct one-dimensional
    Gaussian integration agrees with independent Simpson quadrature to approximately5.9e-15
    and the degenerate input limit reproduces the fixed-input kernel. Under f0=0 and
    X~N0,1 the mixture’s fourth moment differs from3v², proving the matched Gaussian
    need not equal that law. The latent/future-noisy-output distinction and fixed
    hyperparameters are explicit.
- assessment_id: boundaries
  area: scope
  topic: Taylor variance and temporal dependence
  outcome: supported
  target_ids:
  - AIMech:GaussianProcessGaussianInputMomentMatching
  evidence_ids:
  - girard-tr2002
  - hewing2020
  - calculation
  summary: The counterexamples are qualified curator calculations.
  details: The large input-variance Taylor example gives1-3/e<0 while exact integrated
    variance ispositive. This is not evidence against a justified local approximation.
    The persistent coefficient example givesA² rather thanA1*A2; it demonstrates missing
    state/function dependence, not a squared-exponential experimental reproduction.
    Full lag covariance alone does not retain that dependence. Input integration need
    not increase variance versus evaluating only at the input mean.
- assessment_id: empirical
  area: scope
  topic: Illustrative source results and unresolved metadata
  outcome: supported
  target_ids:
  - AIMech:GaussianProcessGaussianInputMomentMatching
  evidence_ids:
  - girard2002
  - girard-tr2002
  - hewing2020
  summary: The record avoids unsupported universal performance and calibration claims.
  details: The pH proceedings test-count placeholder is not filled from an earlier
    report with different preprocessing/results. No code, fitted model or stochastic
    trajectory simulation was run. The exact-kernel method, local Taylor approximation
    and correlation-aware proposals are separately scoped. Singular initial input
    covariance and width-parameter notation remain explicit implementation limits.
- assessment_id: all-fields
  area: provenance
  topic: Complete record fields and report consistency
  outcome: supported
  target_ids:
  - AIMech:GaussianProcessGaussianInputMomentMatching
  evidence_ids:
  - identity
  - mapping
  - girard2002
  - girard-tr2002
  - hewing2020
  - calculation
  summary: All maintained fields and corrected evidence locations are consistent.
  details: Read stableID,name,one descriptive alias,algorithm kind,definition,identity
    search,five claims,three exact source versions/access times/hashes,pinned AIO
    snapshot,two related mappings,six limitations,DRAFT status and actual curation
    timestamps. The discovery report entry equals the YAML. The two2002publications
    have distinct authorship and methods; PMLR2020 metadata page range differs from
    its printedPDFindices and the record usesPDFindices.
- assessment_id: citation-locators
  area: evidence
  topic: Section and equation label audit
  outcome: supported
  target_ids:
  - AIMech:GaussianProcessGaussianInputMomentMatching
  evidence_ids:
  - girard2002
  - girard-tr2002
  summary: All six corrected citation locator strings now match the papers.
  details: Definition and random-input moments citeSections3–3.1; fixed prediction
    citesSections2.1–2.2; forecasting citesSection4 and the unnumbered lag covariance
    paragraph; Taylor citesNIPS3.1 and report3.2–3.4. PDF indices and actual equations
    were checked visually.
findings:
- finding_id: source-locators
  issue_key: aimech-gaussian-input-gp-source-locators
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Correct Gaussian-input GP section and equation locators
  description: The NIPS paper places random-input prediction in Section3 and Gaussian
    moments in3.1, not2/2.2. Fixed-input GP formulas are in2.1–2.2, not1. Iterative
    forecasting is Section4 onPDF4–5; Equation14 belongs to the Monte-Carlo alternative
    onPDF4, not lag-covariance propagation. The Taylor report has Sections3.2–3.4
    onPDF8–9, notSection4. Correct the definition and five claim-evidence locator
    strings across both papers; retain the supported statements and synchronized report
    mirror.
  target_ids:
  - AIMech:GaussianProcessGaussianInputMomentMatching
  field_paths:
  - definition_evidence[0].locator
  - claims[claim_id=mixture-moments].evidence[0].locator
  - claims[claim_id=squared-exponential-integrals].evidence[0].locator
  - claims[claim_id=forecasting-extension].evidence[0].locator
  - claims[claim_id=taylor-boundary].evidence[0].locator
  - claims[claim_id=taylor-boundary].evidence[1].locator
  evidence_ids:
  - girard2002
  - girard-tr2002
  - prior
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GaussianProcessGaussianInputMomentMatching.yaml
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261012T210207Z-gaussian-input-gp-moments.json
    role: discovery_report
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261012T210627Z-gaussian-input-gp-open
    finding_id: source-locators
  disposition_reason: Corrected all six source locators in the maintained record and
    discovery mirror, appended actual correction history, regenerated pages, reread
    the changed input bytes against rendered source labels and reran required checks.
    Scientific claims and method identity are unchanged.
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/199
actions: []
limitations:
- Author self-review only; the record remains DRAFT.
- The first restricted-network vendored check failed to resolve the public host; a
  permitted read-only retry verified all22pinned artifacts.
- Added one native DRAFT algorithm, bringing the total to541 with442 unchanged generated
  records. Discovery remains active:484 pending and54 partly addressed cohorts plus
  other unresolved scopes; no saturation claim.
- Read all8NIPS2002 pages, all18earlier-report pages, and all11Hewing2020 pages, including
  figures, tables and references. The36-page local-linear GP report is downloaded
  but only partially accessed; it is not primary support for the curated record.
- Analytic examples and independent scalar numerical quadrature were executed. No
  source implementation, fitted model, stochastic simulation, paid provider or benchmark
  was executed. Exact moments are separated from a Gaussian law and shared-function
  trajectory independence.
- Original Documents checkout was read in ignored-inclusive identity searches. Original
  synchronization and old round141 cleanup still await explicit approval after automatic
  review rejected the combined action.
related_reviews:
- repository: CultureBotAI/AIMech
  review_id: 20261012T210627Z-gaussian-input-gp-open
  relationship: Successor resolves the six citation-location defects without changing
    scientific statements.
links: []
tags:
- native-concepts
- gaussian-processes
- self-review
- discovery-ongoing
```
