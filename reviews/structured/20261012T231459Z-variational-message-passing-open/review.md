# Scientific author self-review of conjugate variational message passing

- Review: 20261012T231459Z-variational-message-passing-open
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T23:10:25Z
- Finished UTC: 2026-10-12T23:14:59Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Retain the original conjugate VMP algorithm with graph-local moments, valid sequential coordinate scope and explicit extension limits. Clarify one minor log-evidence wording omission; the equation is already correct and DRAFT remains.

## Scope And Provenance

All fields and primary evidence of the maintained original-core VMP record.

Selection: Exact maintained ID: AIMech:VariationalMessagePassing
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 56b70740815983072f2b6d1cea8594850c279b3c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:VariationalMessagePassing | data/curated/VariationalMessagePassing.yaml | maintained | Variational message passing |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:VariationalMessagePassing | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 109.63s (0:01:49)<br>Checked 442 record(s); 0 failed.<br>Checked 552 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 200 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 198,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:VariationalMessagePassing | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:VariationalMessagePassing | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:VariationalMessagePassing | Exited 0 without output. |
| Conjugate message and stationary-saddle calculations | passed | True | AIMech:VariationalMessagePassing | {"gaussian_natural_parameters": ["35/2", "-17/4"], "gaussian_coordinate_mean": "35/17", "gaussian_coordinate_variance": "2/17", "gamma_shape": "7/2", "gamma_rate": "1625/289", "omitted_variance_rate_error": "3/17", "gaussian_coordinate_elbo_improvement": 11.348099210324834, "saddle_hessian": [["-1", "2"], ["2", "-1"]], "saddle_eigenvalues": [1, -3], "saddle_equal_mean_elbo_change": 9.999998335488129e-07, "saddle_opposite_mean_elbo_change": -3.000000166451187e-06, "interpretation": "Exact Fraction message/expectation identities and analytic Hessian, with floating-point KL and finite perturbation illustrations. No fitted source model or empirical reproduction."} |

## Scientific And Domain Assessments

### Graph-local conjugate variational update algorithm

identity: supported. Targets: AIMech:VariationalMessagePassing.

Retain VMP as a distinct algorithm.

The maintained mean-field records specify variational families and objective constructions. VMP organizes expected sufficient-statistic and natural-parameter messages through parent/child/coparent neighborhoods for analytic coordinate updates. NCVMP instead matches expected-log-factor gradients when conjugacy fails, BBVI estimates gradients from samples, VEM alternates model parameters, and ICM optimizes point states. VIBES is implementation context rather than an alias. Extensions are not promoted to distinct concepts without primary assessment.

### Direct inference-to-Bayesian-network relationship

grounding: supported. Targets: AIMech:VariationalMessagePassing.

A related mapping preserves the algorithm/model distinction.

The paper’s DAG conditionals directly determine the message neighborhoods. The pinned BayesianNetwork definition denotes this model architecture, not the inference algorithm. ProbabilisticGraphicalModel is broader task context; the more direct network relation is selected. VAE and probabilistic layer are unrelated architecture types, and regression/topic modeling are optional applications. No is-a or exact-match claim is asserted.

### variational-coordinate-objective

evidence: supported. Targets: AIMech:VariationalMessagePassing.

Supported within the explicitly scoped conjugate core.

For fixed observed variables v and a proper Bayesian-network joint p(h,v)=product_i p(x_i&#124;pa_i) with positive finite evidence p(v), choose normalized variational factors q(h)=product_j q_j(h_j) over disjoint hidden blocks. Maximize L(q)=E_q[log p(h,v)]+H(q), so log p(v)-L(q)=KL(q&#124;&#124;p(h&#124;v)) where expectations are finite and supports compatible. Holding all other factors fixed, the normalized update q_j_new(h_j) proportional to exp(E_q_-j[log p(h,v)]) is the exact coordinate optimum when this distribution exists in the permitted family. Vector-valued node blocks can retain within-block dependence.

### local-markov-blanket

evidence: supported. Targets: AIMech:VariationalMessagePassing.

Supported within the explicitly scoped conjugate core.

The coordinate log update depends only on the updated node’s own conditional and its children’s conditionals: its parents, children and the children’s other parents supply the required local information. Nonadjacent log terms are constant in the updated block. The graph’s conditional-independence structure is used to compute the variational update; it does not assert that the true posterior factors like q.

### conjugate-message-routing

evidence: supported. Targets: AIMech:VariationalMessagePassing.

Supported within the explicitly scoped conjugate core.

In the conjugate-exponential core, write the updated node’s conditional log density as phi(pa)^T*u(x)+f(x)-kappa(phi(pa)). Parent-to-child messages provide current expected sufficient statistics. Each child-to-parent message supplies the expected natural-parameter coefficient of u(x) from that child’s log conditional, using the child’s moments and its other parents’ current moments. The node’s new natural parameter is E[phi(pa)] plus the sum of its child contributions; retain the carrier f(x) once and normalize the resulting factor. Recompute its sufficient-statistic moments from the log-partition derivative or equivalent exact formulas. Observed nodes send their actual sufficient statistics. The needed expectations must be closed under the selected conjugate families.

### schedule-and-guarantee

evidence: supported. Targets: AIMech:VariationalMessagePassing.

Supported within the explicitly scoped conjugate core.

Initialize proper factors with consistent moments and update one block at a time using current incoming information, recomputing its outgoing moments before later affected updates. In exact arithmetic, each valid conjugate coordinate optimum cannot decrease the fixed-model variational lower bound. A bound threshold or iteration cap is a stopping rule, not a posterior-accuracy certificate. Bound monotonicity does not imply global optimality, convergence of all parameter iterates or even that every fixed point is a local optimum; synchronous updates using stale interacting neighbors do not inherit the sequential guarantee.

### gaussian-mean-precision

evidence: supported. Targets: AIMech:VariationalMessagePassing.

Supported within the explicitly scoped conjugate core.

For observations y_n conditionally N(mu,tau^-1), independent priors mu~N(m0,lambda0^-1) and tau~Gamma(a0,b0) in shape-rate form, and q(mu)q(tau), the conjugate updates are v_mu=(lambda0+N*E[tau])^-1, m_mu=v_mu*(lambda0*m0+E[tau]*sum_n y_n), a_tau=a0+N/2 and b_tau=b0+0.5*sum_n((y_n-E[mu])^2+Var(mu)), with each update using current moments. E[tau]=a_tau/b_tau. The variance term in the precision-rate update is required; replacing E[(y_n-mu)^2] by its squared-mean residual alone changes the method. These are coordinate updates of an approximate product posterior.

### bound-accounting

evidence: supported. Targets: AIMech:VariationalMessagePassing.

Supported within the explicitly scoped conjugate core; the bound-accounting wording is qualified below.

The variational bound sums the expected log conditional of every model node, including observed nodes, plus the entropy of each hidden variational factor. Node normalizers and carrier terms must be retained for the bound even when constants cancel from parameter updates. The resulting quantity is a lower bound on model evidence; comparing such bounds does not in general reproduce exact Bayes-factor rankings, because different models can have different approximation gaps.

### extension-boundaries

evidence: supported. Targets: AIMech:VariationalMessagePassing.

Supported within the explicitly scoped conjugate core.

Deterministic transformations require appropriate moment closure and consistent substitution; they are not arbitrary independent variational point masses. Mixture indicators weight natural-parameter contributions by responsibilities rather than replacing the update by an arithmetic mixture of child densities. Multivariate node blocks can retain internal correlation while separate factors remain independent. Nonconjugate auxiliary bounds, point-estimate heuristics and sampling of message expectations are extensions whose objectives, normalization and progress guarantees require separate analysis.

### Message equivalence and moment propagation

consistency: supported. Targets: AIMech:VariationalMessagePassing.

The Gaussian natural parameters and variance term agree with direct expectations.

For supplied observations [1,2,4], prior mean0/precision1 and expected precision5/2, routed natural coefficients [35/2,-17/4] equal the direct expected log joint, yielding mean35/17 and variance2/17. The Gamma update has shape7/2 and rate1625/289; omitting the mean-factor variance lowers the rate by3/17. The positive fixed-q(tau) Gaussian coordinate bound improvement equals the Gaussian KL. This is finite curator arithmetic, not a reproduced model fit.

### Exact coordinate ascent is weaker than local optimality

scope: supported. Targets: AIMech:VariationalMessagePassing.

The source local-optimum guarantee is appropriately qualified.

For the proper finite target proportional to exp(2*x*y), the uniform product is unchanged by each exact coordinate update. Its mean-coordinate ELBO Hessian is [[-1,2],[2,-1]], with eigenvalues1,-3. Perturbing the two means together increases the bound, and opposing them decreases it. This disproves an unconditional claim that every converged fixed point is a local optimum without contradicting coordinate monotonicity. The approximation need not recover exact posterior dependence.

### Normalizer and carrier accounting

consistency: supported. Targets: AIMech:VariationalMessagePassing.

The absolute-bound and local-update roles are distinguished.

The node carrier is retained once; child contributions are expected natural coefficients and depend on current coparents. Observed nodes send actual statistics and contribute their conditional log density once. Hidden entropies and normalizers enter the ELBO. The Gaussian Equation22 constant typo cancels from updates but not evidence, and Gamma uses a rate despite a scale label. Comparing approximate evidence bounds does not guarantee exact Bayes-factor ranking.

### Deterministic, mixture and nonconjugate boundaries

scope: supported. Targets: AIMech:VariationalMessagePassing.

The record avoids unsupported extension guarantees.

Deterministic moments need closure and substitution; arbitrary independent delta factors are not justified. Responsibilities scale natural contributions. Full node blocks may retain correlations. Auxiliary logistic bounds, continuous point estimates and sampled expectations are distinct treatments. The source notes retain a transformed gamma-shape density counterexample to unconditional log-concavity; no ARS implementation is certified. No VIBES runtime, posterior accuracy, pruning implementation or benchmark result is asserted.

### Complete record and source/version audit

provenance: supported. Targets: AIMech:VariationalMessagePassing.

All maintained fields are assessed; DRAFT retained.

Read ID/name/VMP alias, algorithm kind, definition, identity notes, all seven claims and precise locators, primary source author/version/hash/access, pin and related mapping, six limitations and actual curation timestamps. The report mirrors the exact YAML. The JMLR primary page establishes 2005; a later bibliography’s 2006 label is not propagated. All34pages were read; the downloaded Castiglione v5 paper remains abstract-only evidence and is not support for this record. Original source-reading notes preserve historical access states.

### State the logarithmic evidence scale explicitly

consistency: concern. Targets: AIMech:VariationalMessagePassing.

Clarify log model evidence in the bound-accounting claim.

The mathematical definition and KL identity are already correct. Make the later accounting statement self-contained by naming log model evidence, log p(v), so its scale agrees explicitly with the earlier equation and primary source. Retain the approximation-gap qualification and all updates.

## Findings

### F1: Clarify the logarithmic evidence scale in VMP bound accounting

minor / open / confirmed; issue key: aimech-vmp-log-evidence-wording.

The bound-accounting claim omits log when naming the quantity bounded by the ELBO. The earlier log p(v)-L=KL equation is correct, so this is a minor self-contained wording clarification. Name log model evidence, log p(v), without changing the coordinate equations or model-comparison limitation.

## Recommended Actions And Acceptance Checks

### A1

Clarify log model evidence in the maintained claim, synchronize report and page, append actual history and save a linked successor review.

- The bound-accounting statement explicitly names log model evidence, log p(v).
- The coordinate equations, identity, AIO mapping and approximation-gap qualification remain unchanged.
- Required checks pass and a successor review resolves F1 for the maintained target.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T231014Z-variational-message-passing.json | supports | No normalized identity match across 442 pinned AIO IDs, labels and all scoped synonyms and 551 native IDs, names and aliases, including VMP and conjugate spelling variants. Full-checkout fixed-string searches included ignored and hidden files in the recovery, old discovery and original Documents checkouts, with 58, 0 and 1 matched lines. All 42 distinct contents were read, including the complete generated NCVMP search string: matches are the newer nonconjugate algorithm, pending source leads and an unrelated word. Assessed all 15 semantic AIO rows and 122 native names/definitions, six full annotated AIO CLASS nodes with incident edges/generated YAML and six full native context records. VMP supplies graph-local sufficient-statistic message routing and closed conjugate coordinate updates, beyond a mean-field family and objective alone. It differs from BBVI stochastic gradients, NCVMP expected-log-gradient fixed-point proposals, VEM model-parameter alternation and ICM point-state maximization. This record covers the original conjugate-exponential core; auxiliary-bound, sampling and structured extensions need their own assumptions. Absence is bounded to the inspected pin and corpus. |
| mapping | sources/aio/aio.json | supports | Assessed 15 semantic AIO rows and 122 native names/definitions, six complete annotated AIO nodes with all incident edges/generated YAML and six full native context records. The direct Bayesian-network related mapping is bounded to the original core algorithm. |
| winn2005 | https://www.jmlr.org/papers/volume6/winn05a/winn05a.pdf; Sections 2–3, Algorithm 1, Equations 6–23, PDF pp. 3–15; Sections 4 and 6, PDF pp. 15–26; Appendix A, PDF pp. 27–32. | supports | JMLR 6(23):661–694, April 2005; official 34-page journal PDF. All pages visually read, including 16 figures, Table 1, Algorithm 1, Appendix A and 19 references. Printed page = PDF page + 660. The primary page resolves the 2006 citation year in a later bibliography to 2005. All pages read during preparation. After freezing the record, the complete YAML and core message/update/bound pages were reread. |
| calculation | research/discovery/vmp-boundaries.py | supports | Exact Fraction checks compare routed Gaussian messages with direct expected log-joint coefficients and retain the variance contribution to the Gamma rate. An analytic finite-state Hessian and finite perturbations demonstrate a coordinate fixed point that is a saddle. No model fitting or source benchmark. |
| bound-wording | data/curated/VariationalMessagePassing.yaml | supports | The bound-accounting statement calls the expected-log-joint plus entropy a lower bound on model evidence without specifying log evidence. The earlier coordinate-objective equation correctly identifies log p(v). Winn Equations 2–3 on PDF page 3 and Section 3.6 on PDF page 13 explicitly use log evidence. This is a bounded terminology ambiguity, not an incorrect coordinate update. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. One bounded terminology clarification is recorded; this is not an incorrect-update finding.
- Added one DRAFT algorithm, yielding 552 native and 442 unchanged generated records. The 737-entry main frontier retains 485 pending and 56 partly addressed cohorts; discovery is incomplete.
- The full 34-page primary paper was read, including all figures, Table 1, Algorithm 1, Appendix A and references. The saved rational and analytic examples check message equivalence, uncertainty propagation and stationary-point boundaries; no source experiment, fitted posterior or benchmark was reproduced. The record remains DRAFT; author self-review is not independent approval.
- Historical query/download notes describe the access state at capture. Winn2005 was subsequently fully read; Castiglione2025 v5 remains entirely unread beyond its abstract. No author implementation was inspected.
- Nested leads remain incompletely deduplicated and are not counted as fully assessed main-frontier candidates.
- Original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection; isolated recovery work only.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T231459Z-variational-message-passing-open
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of conjugate variational message passing
started_at: '2026-10-12T23:10:25Z'
finished_at: '2026-10-12T23:14:59Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent challenged identity, graph routing, moment/normalizer
    accounting, coordinate guarantees, source formula errors and extension boundaries.
    This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Retain the original conjugate VMP algorithm with graph-local moments, valid
  sequential coordinate scope and explicit extension limits. Clarify one minor log-evidence
  wording omission; the equation is already correct and DRAFT remains.
source:
  git_revision: 56b70740815983072f2b6d1cea8594850c279b3c
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
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
  - path: data/aio/VariationalAutoEncoder.yaml
    sha256: f8f523c5f2cecf91f1510c5ab74bfd36d717f3e683a9a8384e44a3f855e4c45e
    role: context
  - path: data/curated/BlackBoxVariationalInference.yaml
    sha256: 8237d3233ae06163b8fab5b4fa047ffc938e275bc1e3ede883348e06c2b266a8
    role: context
  - path: data/curated/FullyFactorizedMeanFieldInference.yaml
    sha256: 102be6f77143b26acb0d482f91e2dfa58ea113f2188b14b92067484cc4f9408d
    role: context
  - path: data/curated/IteratedConditionalModes.yaml
    sha256: e3cab6676e99fc64d8afca411250e28eec5126524709c6e67988180fa54ffc78
    role: context
  - path: data/curated/NonconjugateVariationalMessagePassing.yaml
    sha256: 0d303d220e92ad009eb802ddee59c6ab74cfd1d7872f3a50ad939deed002ad23
    role: context
  - path: data/curated/StructuredMeanFieldInference.yaml
    sha256: 3cd31e539123908291c2a9a394792c52dacf415ce3c19c4d6a42e9be6173c86b
    role: context
  - path: data/curated/VariationalExpectationMaximization.yaml
    sha256: 5ec118dcfd17dd552866d1f4b883ed273c812c04aca5c3eefc628a5f8035ad5d
    role: context
  - path: data/curated/VariationalMessagePassing.yaml
    sha256: 2fca0db1579eb029f12fdf1f0fc7fbe9974e11b6c8c80e73b27aabb6c16b2880
    role: target
  - path: research/discovery/20261012T231014Z-variational-message-passing.json
    sha256: 7e4902c7925db5f65be2e6c7a13aaaa85ea92caff6b21ffd6c60e9b8593cc494
    role: context
  - path: research/discovery/vmp-boundaries.py
    sha256: 55cf90d622989102d600e78e03f0a3d751ac4b005d72f681b7c57a99603cae3a
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
- target_id: AIMech:VariationalMessagePassing
  path: data/curated/VariationalMessagePassing.yaml
  label: Variational message passing
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/VariationalMessagePassing.yaml
    role: maintained
scope:
  description: All fields and primary evidence of the maintained original-core VMP
    record.
  selection: 'Exact maintained ID: AIMech:VariationalMessagePassing'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:VariationalMessagePassing
  exclusions:
  - target: VIBES code and empirical reproduction
    reason: Historical implementation described by source but not inspected or run.
  - target: Structured, auxiliary-bound and sampling extensions
    reason: Source caveats recorded; distinct identity and full-primary assessments
      remain pending.
  - target: Existing AIO/native context records
    reason: Identity/mapping context rather than complete scientific rereview.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:VariationalMessagePassing
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 109.63s (0:01:49)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 552 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 200 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 198,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:VariationalMessagePassing
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
  - AIMech:VariationalMessagePassing
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
  - AIMech:VariationalMessagePassing
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Conjugate message and stationary-saddle calculations
  command: python3 research/discovery/vmp-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:VariationalMessagePassing
  exit_code: 0
  expected_exit_code: 0
  summary: '{"gaussian_natural_parameters": ["35/2", "-17/4"], "gaussian_coordinate_mean":
    "35/17", "gaussian_coordinate_variance": "2/17", "gamma_shape": "7/2", "gamma_rate":
    "1625/289", "omitted_variance_rate_error": "3/17", "gaussian_coordinate_elbo_improvement":
    11.348099210324834, "saddle_hessian": [["-1", "2"], ["2", "-1"]], "saddle_eigenvalues":
    [1, -3], "saddle_equal_mean_elbo_change": 9.999998335488129e-07, "saddle_opposite_mean_elbo_change":
    -3.000000166451187e-06, "interpretation": "Exact Fraction message/expectation
    identities and analytic Hessian, with floating-point KL and finite perturbation
    illustrations. No fitted source model or empirical reproduction."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T231014Z-variational-message-passing.json
  accessed_at: '2026-10-12T23:10:25Z'
  support: supports
  summary: 'No normalized identity match across 442 pinned AIO IDs, labels and all
    scoped synonyms and 551 native IDs, names and aliases, including VMP and conjugate
    spelling variants. Full-checkout fixed-string searches included ignored and hidden
    files in the recovery, old discovery and original Documents checkouts, with 58,
    0 and 1 matched lines. All 42 distinct contents were read, including the complete
    generated NCVMP search string: matches are the newer nonconjugate algorithm, pending
    source leads and an unrelated word. Assessed all 15 semantic AIO rows and 122
    native names/definitions, six full annotated AIO CLASS nodes with incident edges/generated
    YAML and six full native context records. VMP supplies graph-local sufficient-statistic
    message routing and closed conjugate coordinate updates, beyond a mean-field family
    and objective alone. It differs from BBVI stochastic gradients, NCVMP expected-log-gradient
    fixed-point proposals, VEM model-parameter alternation and ICM point-state maximization.
    This record covers the original conjugate-exponential core; auxiliary-bound, sampling
    and structured extensions need their own assumptions. Absence is bounded to the
    inspected pin and corpus.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-12T23:10:25Z'
  support: supports
  summary: Assessed 15 semantic AIO rows and 122 native names/definitions, six complete
    annotated AIO nodes with all incident edges/generated YAML and six full native
    context records. The direct Bayesian-network related mapping is bounded to the
    original core algorithm.
- evidence_id: winn2005
  kind: primary_source
  reference: https://www.jmlr.org/papers/volume6/winn05a/winn05a.pdf
  locator: Sections 2–3, Algorithm 1, Equations 6–23, PDF pp. 3–15; Sections 4 and
    6, PDF pp. 15–26; Appendix A, PDF pp. 27–32.
  accessed_at: '2026-10-12T22:48:01Z'
  snapshot_sha256: 54b3d6c6fdb702763198795b998b4079476358f5b0d170f9154c48f8aeaa4f2e
  support: supports
  summary: JMLR 6(23):661–694, April 2005; official 34-page journal PDF. All pages
    visually read, including 16 figures, Table 1, Algorithm 1, Appendix A and 19 references.
    Printed page = PDF page + 660. The primary page resolves the 2006 citation year
    in a later bibliography to 2005. All pages read during preparation. After freezing
    the record, the complete YAML and core message/update/bound pages were reread.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/vmp-boundaries.py
  accessed_at: '2026-10-12T23:10:25Z'
  snapshot_sha256: 55cf90d622989102d600e78e03f0a3d751ac4b005d72f681b7c57a99603cae3a
  support: supports
  summary: Exact Fraction checks compare routed Gaussian messages with direct expected
    log-joint coefficients and retain the variance contribution to the Gamma rate.
    An analytic finite-state Hessian and finite perturbations demonstrate a coordinate
    fixed point that is a saddle. No model fitting or source benchmark.
- evidence_id: bound-wording
  kind: record_content
  reference: data/curated/VariationalMessagePassing.yaml
  accessed_at: '2026-10-12T23:10:25Z'
  snapshot_sha256: 2fca0db1579eb029f12fdf1f0fc7fbe9974e11b6c8c80e73b27aabb6c16b2880
  support: supports
  summary: The bound-accounting statement calls the expected-log-joint plus entropy
    a lower bound on model evidence without specifying log evidence. The earlier coordinate-objective
    equation correctly identifies log p(v). Winn Equations 2–3 on PDF page 3 and Section
    3.6 on PDF page 13 explicitly use log evidence. This is a bounded terminology
    ambiguity, not an incorrect coordinate update.
assessments:
- assessment_id: identity
  area: identity
  topic: Graph-local conjugate variational update algorithm
  outcome: supported
  target_ids:
  - AIMech:VariationalMessagePassing
  evidence_ids:
  - identity
  - winn2005
  summary: Retain VMP as a distinct algorithm.
  details: The maintained mean-field records specify variational families and objective
    constructions. VMP organizes expected sufficient-statistic and natural-parameter
    messages through parent/child/coparent neighborhoods for analytic coordinate updates.
    NCVMP instead matches expected-log-factor gradients when conjugacy fails, BBVI
    estimates gradients from samples, VEM alternates model parameters, and ICM optimizes
    point states. VIBES is implementation context rather than an alias. Extensions
    are not promoted to distinct concepts without primary assessment.
- assessment_id: mapping
  area: grounding
  topic: Direct inference-to-Bayesian-network relationship
  outcome: supported
  target_ids:
  - AIMech:VariationalMessagePassing
  evidence_ids:
  - mapping
  - winn2005
  summary: A related mapping preserves the algorithm/model distinction.
  details: The paper’s DAG conditionals directly determine the message neighborhoods.
    The pinned BayesianNetwork definition denotes this model architecture, not the
    inference algorithm. ProbabilisticGraphicalModel is broader task context; the
    more direct network relation is selected. VAE and probabilistic layer are unrelated
    architecture types, and regression/topic modeling are optional applications. No
    is-a or exact-match claim is asserted.
- assessment_id: variational-coordinate-objective
  area: evidence
  topic: variational-coordinate-objective
  outcome: supported
  target_ids:
  - AIMech:VariationalMessagePassing
  evidence_ids:
  - winn2005
  summary: Supported within the explicitly scoped conjugate core.
  details: For fixed observed variables v and a proper Bayesian-network joint p(h,v)=product_i
    p(x_i|pa_i) with positive finite evidence p(v), choose normalized variational
    factors q(h)=product_j q_j(h_j) over disjoint hidden blocks. Maximize L(q)=E_q[log
    p(h,v)]+H(q), so log p(v)-L(q)=KL(q||p(h|v)) where expectations are finite and
    supports compatible. Holding all other factors fixed, the normalized update q_j_new(h_j)
    proportional to exp(E_q_-j[log p(h,v)]) is the exact coordinate optimum when this
    distribution exists in the permitted family. Vector-valued node blocks can retain
    within-block dependence.
- assessment_id: local-markov-blanket
  area: evidence
  topic: local-markov-blanket
  outcome: supported
  target_ids:
  - AIMech:VariationalMessagePassing
  evidence_ids:
  - winn2005
  summary: Supported within the explicitly scoped conjugate core.
  details: 'The coordinate log update depends only on the updated node’s own conditional
    and its children’s conditionals: its parents, children and the children’s other
    parents supply the required local information. Nonadjacent log terms are constant
    in the updated block. The graph’s conditional-independence structure is used to
    compute the variational update; it does not assert that the true posterior factors
    like q.'
- assessment_id: conjugate-message-routing
  area: evidence
  topic: conjugate-message-routing
  outcome: supported
  target_ids:
  - AIMech:VariationalMessagePassing
  evidence_ids:
  - winn2005
  - calculation
  summary: Supported within the explicitly scoped conjugate core.
  details: In the conjugate-exponential core, write the updated node’s conditional
    log density as phi(pa)^T*u(x)+f(x)-kappa(phi(pa)). Parent-to-child messages provide
    current expected sufficient statistics. Each child-to-parent message supplies
    the expected natural-parameter coefficient of u(x) from that child’s log conditional,
    using the child’s moments and its other parents’ current moments. The node’s new
    natural parameter is E[phi(pa)] plus the sum of its child contributions; retain
    the carrier f(x) once and normalize the resulting factor. Recompute its sufficient-statistic
    moments from the log-partition derivative or equivalent exact formulas. Observed
    nodes send their actual sufficient statistics. The needed expectations must be
    closed under the selected conjugate families.
- assessment_id: schedule-and-guarantee
  area: evidence
  topic: schedule-and-guarantee
  outcome: supported
  target_ids:
  - AIMech:VariationalMessagePassing
  evidence_ids:
  - winn2005
  - calculation
  summary: Supported within the explicitly scoped conjugate core.
  details: Initialize proper factors with consistent moments and update one block
    at a time using current incoming information, recomputing its outgoing moments
    before later affected updates. In exact arithmetic, each valid conjugate coordinate
    optimum cannot decrease the fixed-model variational lower bound. A bound threshold
    or iteration cap is a stopping rule, not a posterior-accuracy certificate. Bound
    monotonicity does not imply global optimality, convergence of all parameter iterates
    or even that every fixed point is a local optimum; synchronous updates using stale
    interacting neighbors do not inherit the sequential guarantee.
- assessment_id: gaussian-mean-precision
  area: evidence
  topic: gaussian-mean-precision
  outcome: supported
  target_ids:
  - AIMech:VariationalMessagePassing
  evidence_ids:
  - winn2005
  - calculation
  summary: Supported within the explicitly scoped conjugate core.
  details: For observations y_n conditionally N(mu,tau^-1), independent priors mu~N(m0,lambda0^-1)
    and tau~Gamma(a0,b0) in shape-rate form, and q(mu)q(tau), the conjugate updates
    are v_mu=(lambda0+N*E[tau])^-1, m_mu=v_mu*(lambda0*m0+E[tau]*sum_n y_n), a_tau=a0+N/2
    and b_tau=b0+0.5*sum_n((y_n-E[mu])^2+Var(mu)), with each update using current
    moments. E[tau]=a_tau/b_tau. The variance term in the precision-rate update is
    required; replacing E[(y_n-mu)^2] by its squared-mean residual alone changes the
    method. These are coordinate updates of an approximate product posterior.
- assessment_id: bound-accounting
  area: evidence
  topic: bound-accounting
  outcome: supported
  target_ids:
  - AIMech:VariationalMessagePassing
  evidence_ids:
  - winn2005
  summary: Supported within the explicitly scoped conjugate core; the bound-accounting
    wording is qualified below.
  details: The variational bound sums the expected log conditional of every model
    node, including observed nodes, plus the entropy of each hidden variational factor.
    Node normalizers and carrier terms must be retained for the bound even when constants
    cancel from parameter updates. The resulting quantity is a lower bound on model
    evidence; comparing such bounds does not in general reproduce exact Bayes-factor
    rankings, because different models can have different approximation gaps.
- assessment_id: extension-boundaries
  area: evidence
  topic: extension-boundaries
  outcome: supported
  target_ids:
  - AIMech:VariationalMessagePassing
  evidence_ids:
  - winn2005
  summary: Supported within the explicitly scoped conjugate core.
  details: Deterministic transformations require appropriate moment closure and consistent
    substitution; they are not arbitrary independent variational point masses. Mixture
    indicators weight natural-parameter contributions by responsibilities rather than
    replacing the update by an arithmetic mixture of child densities. Multivariate
    node blocks can retain internal correlation while separate factors remain independent.
    Nonconjugate auxiliary bounds, point-estimate heuristics and sampling of message
    expectations are extensions whose objectives, normalization and progress guarantees
    require separate analysis.
- assessment_id: finite-checks
  area: consistency
  topic: Message equivalence and moment propagation
  outcome: supported
  target_ids:
  - AIMech:VariationalMessagePassing
  evidence_ids:
  - winn2005
  - calculation
  summary: The Gaussian natural parameters and variance term agree with direct expectations.
  details: For supplied observations [1,2,4], prior mean0/precision1 and expected
    precision5/2, routed natural coefficients [35/2,-17/4] equal the direct expected
    log joint, yielding mean35/17 and variance2/17. The Gamma update has shape7/2
    and rate1625/289; omitting the mean-factor variance lowers the rate by3/17. The
    positive fixed-q(tau) Gaussian coordinate bound improvement equals the Gaussian
    KL. This is finite curator arithmetic, not a reproduced model fit.
- assessment_id: stationary-saddle
  area: scope
  topic: Exact coordinate ascent is weaker than local optimality
  outcome: supported
  target_ids:
  - AIMech:VariationalMessagePassing
  evidence_ids:
  - winn2005
  - calculation
  summary: The source local-optimum guarantee is appropriately qualified.
  details: For the proper finite target proportional to exp(2*x*y), the uniform product
    is unchanged by each exact coordinate update. Its mean-coordinate ELBO Hessian
    is [[-1,2],[2,-1]], with eigenvalues1,-3. Perturbing the two means together increases
    the bound, and opposing them decreases it. This disproves an unconditional claim
    that every converged fixed point is a local optimum without contradicting coordinate
    monotonicity. The approximation need not recover exact posterior dependence.
- assessment_id: carrier-and-bound
  area: consistency
  topic: Normalizer and carrier accounting
  outcome: supported
  target_ids:
  - AIMech:VariationalMessagePassing
  evidence_ids:
  - winn2005
  summary: The absolute-bound and local-update roles are distinguished.
  details: The node carrier is retained once; child contributions are expected natural
    coefficients and depend on current coparents. Observed nodes send actual statistics
    and contribute their conditional log density once. Hidden entropies and normalizers
    enter the ELBO. The Gaussian Equation22 constant typo cancels from updates but
    not evidence, and Gamma uses a rate despite a scale label. Comparing approximate
    evidence bounds does not guarantee exact Bayes-factor ranking.
- assessment_id: extensions
  area: scope
  topic: Deterministic, mixture and nonconjugate boundaries
  outcome: supported
  target_ids:
  - AIMech:VariationalMessagePassing
  evidence_ids:
  - winn2005
  summary: The record avoids unsupported extension guarantees.
  details: Deterministic moments need closure and substitution; arbitrary independent
    delta factors are not justified. Responsibilities scale natural contributions.
    Full node blocks may retain correlations. Auxiliary logistic bounds, continuous
    point estimates and sampled expectations are distinct treatments. The source notes
    retain a transformed gamma-shape density counterexample to unconditional log-concavity;
    no ARS implementation is certified. No VIBES runtime, posterior accuracy, pruning
    implementation or benchmark result is asserted.
- assessment_id: complete-fields
  area: provenance
  topic: Complete record and source/version audit
  outcome: supported
  target_ids:
  - AIMech:VariationalMessagePassing
  evidence_ids:
  - identity
  - mapping
  - winn2005
  - calculation
  summary: All maintained fields are assessed; DRAFT retained.
  details: Read ID/name/VMP alias, algorithm kind, definition, identity notes, all
    seven claims and precise locators, primary source author/version/hash/access,
    pin and related mapping, six limitations and actual curation timestamps. The report
    mirrors the exact YAML. The JMLR primary page establishes 2005; a later bibliography’s
    2006 label is not propagated. All34pages were read; the downloaded Castiglione
    v5 paper remains abstract-only evidence and is not support for this record. Original
    source-reading notes preserve historical access states.
- assessment_id: bound-wording
  area: consistency
  topic: State the logarithmic evidence scale explicitly
  outcome: concern
  target_ids:
  - AIMech:VariationalMessagePassing
  evidence_ids:
  - bound-wording
  - winn2005
  summary: Clarify log model evidence in the bound-accounting claim.
  details: The mathematical definition and KL identity are already correct. Make the
    later accounting statement self-contained by naming log model evidence, log p(v),
    so its scale agrees explicitly with the earlier equation and primary source. Retain
    the approximation-gap qualification and all updates.
findings:
- finding_id: F1
  issue_key: aimech-vmp-log-evidence-wording
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Clarify the logarithmic evidence scale in VMP bound accounting
  description: The bound-accounting claim omits log when naming the quantity bounded
    by the ELBO. The earlier log p(v)-L=KL equation is correct, so this is a minor
    self-contained wording clarification. Name log model evidence, log p(v), without
    changing the coordinate equations or model-comparison limitation.
  target_ids:
  - AIMech:VariationalMessagePassing
  field_paths:
  - claims[5].statement
  evidence_ids:
  - bound-wording
  - winn2005
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/VariationalMessagePassing.yaml
    role: maintained
actions:
- action_id: A1
  description: Clarify log model evidence in the maintained claim, synchronize report
    and page, append actual history and save a linked successor review.
  finding_ids:
  - F1
  target_ids:
  - AIMech:VariationalMessagePassing
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/VariationalMessagePassing.yaml
    role: maintained
  acceptance_checks:
  - The bound-accounting statement explicitly names log model evidence, log p(v).
  - The coordinate equations, identity, AIO mapping and approximation-gap qualification
    remain unchanged.
  - Required checks pass and a successor review resolves F1 for the maintained target.
limitations:
- Author self-review only; no independent approval or status promotion. One bounded
  terminology clarification is recorded; this is not an incorrect-update finding.
- Added one DRAFT algorithm, yielding 552 native and 442 unchanged generated records.
  The 737-entry main frontier retains 485 pending and 56 partly addressed cohorts;
  discovery is incomplete.
- The full 34-page primary paper was read, including all figures, Table 1, Algorithm
  1, Appendix A and references. The saved rational and analytic examples check message
  equivalence, uncertainty propagation and stationary-point boundaries; no source
  experiment, fitted posterior or benchmark was reproduced. The record remains DRAFT;
  author self-review is not independent approval.
- Historical query/download notes describe the access state at capture. Winn2005 was
  subsequently fully read; Castiglione2025 v5 remains entirely unread beyond its abstract.
  No author implementation was inspected.
- Nested leads remain incompletely deduplicated and are not counted as fully assessed
  main-frontier candidates.
- Original-checkout synchronization and old round141 cleanup remain pending explicit
  approval after automatic review rejection; isolated recovery work only.
related_reviews: []
links: []
tags:
- native-concepts
- variational-inference
- message-passing
- self-review
- discovery-ongoing
```
