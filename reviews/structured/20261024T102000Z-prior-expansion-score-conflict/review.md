# Successor scientific author self-review of prior-expansion score conflict diagnostic after Issue

- Review: 20261024T102000Z-prior-expansion-score-conflict
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-24T10:15:00Z
- Finished UTC: 2026-10-24T10:20:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the prior-expansion score conflict diagnostic as a distinct DRAFT algorithm with related Bayesian-network context. All seven claims and locators are supported after resolving AIM-PR428-E0EC-F1 (dimensionless multiplicative normal variance-expansion score verified across unit and non-unit baseline prior variances) and AIM-PR428-E0EC-F2 (scalar one-at-a-time directional calibration attributed to Nott et al. 2020 Section 1 and Yang et al. 2026 Section 2.3 rather than an unsupported covariance-normalized vector quadratic form). Author MCMC/variational code and empirical repeated-data calibration remain unverified.

## Scope And Provenance

All fields of the corrected maintained prior-expansion score diagnostic and its primary evidence after resolving Issue

Selection: Exact maintained ID: AIMech:PriorExpansionScoreConflictDiagnostic
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e0ec3050952cf97f111dbf5307873595fe08eed9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:PriorExpansionScoreConflictDiagnostic | data/curated/PriorExpansionScoreConflictDiagnostic.yaml | maintained | Prior-expansion score conflict diagnostic |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validation suite | passed | True | AIMech:PriorExpansionScoreConflictDiagnostic | Checked 442 record(s); 0 failed.<br>Checked 564 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 223 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 218,<br>  "coverage": "declared_scopes_only"<br>}<br> |
| just vendored-check | passed | True | AIMech:PriorExpansionScoreConflictDiagnostic | OK: 22 governed artifacts match the pinned claw revision<br> |
| aimech check-source | passed | True | AIMech:PriorExpansionScoreConflictDiagnostic | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:PriorExpansionScoreConflictDiagnostic | Exited 0 without output. |
| Constructed prior-expansion score boundaries including non-unit baseline variances | passed | True | AIMech:PriorExpansionScoreConflictDiagnostic | {<br>  "coordinate_wise_directional_expansions": {<br>    "location_two_sided_matches_scale_upper_tail": true,<br>    "one_at_a_time_identities_agree": true,<br>    "rows": [<br>      {<br>        "p_location_two_sided": 0.00040695,<br>        "p_scale_upper_tail": 0.00040695,<br>        "s_location": 5.0,<br>        "s_scale": 2.875,<br>        "tau0_sq": 0.25<br>      },<br>      {<br>        "p_location_two_sided": 0.02534732,<br>        "p_scale_upper_tail": 0.02534732,<br>        "s_location": 2.0,<br>        "s_scale": 1.6,<br>        "tau0_sq": 1.0<br>      },<br>      {<br>        "p_location_two_sided": 0.22525291,<br>        "p_scale_upper_tail": 0.22525291,<br>        "s_location": 0.58823529,<br>        "s_scale": 0.22145329,<br>        "tau0_sq": 4.0<br>      }<br>    ]<br>  },<br>  "evans_moshonov_equivalence": {<br>    "exact_equivalence": true,<br>    "p_evans_moshonov": 0.02534732,<br>    "p_score_upper_tail": 0.02534732,<br>    "tested_tau0_sq_values": [<br>      0.25,<br>      1.0,<br>      2.0,<br>      4.0<br>    ],<br>    "z_obs": 2.23606798<br>  },<br>  "fisher_and_renyi": {<br>    "identities_agree": true,<br>    "neg_d_fixed_posterior_kl": 1.6,<br>    "neg_d_varying_posterior_kl": 0.88,<br>    "non_unit_tau0_sq_4_v_025_score": 0.22145329,<br>    "non_unit_tau0_sq_4_v_025_tau2_derivative": 0.05536332,<br>    "s_claim_expanded": 1.6,<br>    "s_direct": 1.6,<br>    "s_fisher": 1.6,<br>    "s_tau2_example_4_1": 1.6,<br>    "tested_grid_size": 20,<br>    "varying_posterior_differs_by_cov_term": true<br>  },<br>  "hierarchical_normal_random_effects": {<br>    "s1_lower_mixed": 0.22687596,<br>    "s2_upper_marginal": 0.99722992,<br>    "ss_between": 2.48,<br>    "upper_score_positive_for_grand_mean_shift": true,<br>    "y_grand": 2.0<br>  },<br>  "support_dependent_boundary": {<br>    "boundary_posterior_density": 0.31303529,<br>    "naive_fails_by_boundary_term": true,<br>    "reparameterized_matches_exact": true,<br>    "s_exact_fd": -0.68696471,<br>    "s_naive_eq_1_3": -1.0,<br>    "s_reparameterized": -0.68696471<br>  }<br>} |

## Scientific And Domain Assessments

### Prior-expansion score diagnostic versus node-splitting and sequential DAG checks

identity: supported. Targets: AIMech:PriorExpansionScoreConflictDiagnostic.

Retain the prior-expansion score conflict diagnostic as a distinct DRAFT algorithm.

The diagnostic is defined by embedding a baseline prior in a smooth expansion family g(theta &#124; gamma) and evaluating the posterior expectation of the prior score at gamma_0 via Fisher's identity. Unlike cross-validated prior-likelihood or separator/INLA node-splitting diagnostics, it does not partition data or duplicate graphical nodes into split posteriors. The sequential parent-to-child DAG conflict procedure of Yang et al. (2026) uses this score discrepancy as its second-stage building block and remains a separate concept.

### Diagnostic-to-BayesianNetwork, ProbabilisticGraphicalModel, and RandomEffectsModel relations

grounding: supported. Targets: AIMech:PriorExpansionScoreConflictDiagnostic.

Related BayesianNetwork, ProbabilisticGraphicalModel, and RandomEffectsModel mappings are supported.

The diagnostic checks prior-data and hierarchical stagewise conflict in Bayesian models, probabilistic graphical models, and random-effects models. Those three AIO classes supply representation and model context via related_match without asserting subclass or equivalence semantics.

### prior-expansion-fisher-score

evidence: supported. Targets: AIMech:PriorExpansionScoreConflictDiagnostic.

Supported with explicit support-independence and regularity boundaries.

Embedding g(theta)=g(theta&#124;gamma_0) in a smooth expansion family g(theta&#124;gamma) defines S(y) = d/dgamma log p(y&#124;gamma)&#124;_{gamma_0}. Under regularity conditions allowing interchange of differentiation and integration on a gamma-independent parameter support, Fisher's identity expresses S(y) as the posterior expectation int [d/dgamma log g(theta&#124;gamma)&#124;_{gamma_0}] g(theta&#124;y) dtheta. Constructed boundary checks confirm that when support depends on gamma (e.g. Uniform(0,gamma)), naive differentiation under the integral sign misses the boundary posterior density term unless reparameterized to a fixed domain.

### relative-belief-renyi-sensitivity

evidence: supported. Targets: AIMech:PriorExpansionScoreConflictDiagnostic.

Supported with the fixed-posterior weighting distinction made explicit.

Because the relative belief ratio RB(theta&#124;y,gamma) = p(y&#124;theta)/p(y&#124;gamma) depends on gamma solely through p(y&#124;gamma)^(-1), differentiating log RB(theta&#124;y,gamma), the baseline-posterior-weighted Renyi functional (Equation 2.3, where g(theta&#124;y) in the integral weight is held fixed at gamma_0), or the fixed-posterior KL divergence KL(g(theta&#124;y) &#124;&#124; g(theta&#124;gamma)) with respect to gamma at gamma_0 yields -S(y) identically for every alpha &gt; 0. Varying the posterior weighting density g(theta&#124;y,gamma) inside R_alpha(g(theta&#124;y,gamma) &#124;&#124; g(theta&#124;gamma)) adds a posterior covariance term.

### coordinate-wise-directional-calibration

evidence: supported. Targets: AIMech:PriorExpansionScoreConflictDiagnostic.

Supported after resolving AIM-PR428-E0EC-F2 to reflect scalar one-at-a-time expansions and directional tail calibration.

Nott et al. (2020) Section 1 (PDF p. 2) restricts gamma to a scalar parameter or one-at-a-time coordinate-wise perturbations when multiple baseline hyperparameters exist, calibrating each scalar score S_j(y) against the prior predictive distribution p(y) using upper-tail probabilities for variance-broadening expansions and two-sided tail probabilities for location-shift expansions (Section 1, pp. 3-4; Yang et al. 2026 Section 2.3, pp. 11-12).

### evans-moshonov-normal-location-equivalence

evidence: supported. Targets: AIMech:PriorExpansionScoreConflictDiagnostic.

Supported and verified analytically across unit and non-unit baseline prior variances after resolving AIM-PR428-E0EC-F1.

Under multiplicative variance expansion theta &#124; gamma ~ N(mu_0, gamma*tau_0^2) at gamma_0 = 1, the dimensionless score is S(y) = (1/(2*tau_0^2)) E[theta^2 - 2*theta*mu_0 + mu_0^2 - tau_0^2 &#124; y] = (tau_0^2/2) * [(x_bar - mu_0)^2 / (tau_0^2 + sigma^2/n)^2 - 1 / (tau_0^2 + sigma^2/n)], which equals tau_0^2 times the direct variance derivative S_{tau^2}(y) of Nott et al. (2020) Example 4.1 (PDF p. 8). Because S(y) is a strictly increasing affine function of (x_bar - mu_0)^2 for every tau_0^2 &gt; 0, its upper-tail prior-predictive p-value equals the Evans-Moshonov (2006) prior-predictive p-value identically.

### exponential-family-conjugate-score-expectation

evidence: supported. Targets: AIMech:PriorExpansionScoreConflictDiagnostic.

Supported for exponential-family priors via posterior expectations of sufficient statistics.

When the expanded prior family g(theta&#124;gamma) = h(theta) exp(eta(gamma)^T T(theta) - A(eta(gamma))) belongs to an exponential family, the prior score d/dgamma log g(theta&#124;gamma)&#124;_{gamma_0} is linear in the sufficient statistics T(theta), reducing S(y) to a linear combination of posterior expectations E[T(theta)&#124;y] minus prior expectations E[T(theta)&#124;gamma_0] as shown in Nott et al. (2020) Section 4.1-4.3 (PDF pp. 8-13).

### hierarchical-stagewise-mixed-predictive-scores

evidence: supported. Targets: AIMech:PriorExpansionScoreConflictDiagnostic.

Supported with explicit stagewise reference distributions.

In a two-stage hierarchical model p(y&#124;theta_1)g_1(theta_1&#124;theta_2)g_2(theta_2), expanding the first-stage prior g_1(theta_1&#124;theta_2,zeta) checks lower-level conflict against a mixed predictive reference p_M(y) that draws theta_2' ~ g(theta_2&#124;y_obs), theta_1' ~ g_1(theta_1&#124;theta_2'), and y ~ p(y&#124;theta_1'), whereas expanding the hyperprior g_2(theta_2&#124;eta) checks upper-level conflict against the marginal prior predictive p(y).

### variational-posterior-score-approximation

evidence: supported. Targets: AIMech:PriorExpansionScoreConflictDiagnostic.

Supported with explicit variational-error caveat.

Evaluating S(y) requires only posterior expectations of the prior score under the baseline model and can be approximated by substituting a Gaussian variational posterior q(theta) for g(theta&#124;y) in both observed and simulated reference datasets, subject to variational approximation bias.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:PriorExpansionScoreConflictDiagnostic.

The full record is consistent after resolving Issue

Read every field of PriorExpansionScoreConflictDiagnostic.yaml: stable ID, name, aliases, algorithm kind, definition, definition_evidence, identity_notes, seven claims and locators, two full-text primary sources with exact SHA-256 digests, three pinned AIO mappings and rationales, five scoped limitations, and UTC curation metadata. All repository validation checks and constructed boundary assertions across unit and non-unit baseline variances passed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T082300Z-prior-expansion-score-conflict.json | supports | No normalized identity match for the prior-expansion score conflict diagnostic across 442 pinned AIO records and 563 other maintained IDs, names, aliases and scoped synonyms. This concept denotes score-type prior-data conflict diagnostics formed by differentiating log marginal likelihood along a smooth scalar or coordinate-wise prior expansion family at the baseline prior via Fisher's identity; it is distinct from cross-validated held-out prior-likelihood splitting, separator node splitting, INLA group node splitting, and sequential DAG parent-child score checks. |
| mapping | sources/aio/aio.json | supports | Inspected BayesianNetwork, ProbabilisticGraphicalModel, RandomEffectsModel, and EvaluationBias in the pinned AIO snapshot (2026-07-22). BayesianNetwork and ProbabilisticGraphicalModel supply directed acyclic graph and hierarchical conditional factorization context as related_match mappings, while RandomEffectsModel supplies random-effects stage context. |
| calculation | research/discovery/prior-expansion-score-conflict-boundaries.py | supports | Constructed exact analytic and numerical checks across unit and non-unit baseline prior variances (tau_0^2 in {0.25, 1.0, 2.0, 4.0} and sigma^2/n in {0.1, 0.25, 0.5, 1.0, 2.0}) for (1) Fisher's identity, the dimensionless multiplicative normal variance-expansion score S(y) = tau_0^2 S_{tau^2}(y), and fixed-posterior versus varying-posterior Renyi divergence derivatives, (2) exact normal-location equivalence with the Evans-Moshonov prior-predictive p-value, (3) one-at-a-time scalar directional location and scale prior expansions and tail calibration, (4) two-stage hierarchical normal mixed-predictive and prior-predictive scores, and (5) support-dependent boundary failure of naive integral-derivative interchange. |
| nott2020 | https://arxiv.org/pdf/1902.10393v2; Section 1, PDF pp. 2-4; Section 2.1-2.2, pp. 4-6; Section 3, pp. 6-8; Section 4.1-4.3, pp. 8-13; Section 5, pp. 13-16 | supports | Re-verified all cited sections of Nott et al. (2020), specifically confirming that Section 1 (PDF p. 2) restricts gamma to a scalar or one-at-a-time coordinate-wise expansion parameter and that Example 4.1 (PDF p. 8) differentiates directly with respect to gamma = tau^2 at tau_0^2 so that multiplicative variance scaling theta &#124; gamma ~ N(mu_0, gamma tau_0^2) at gamma_0 = 1 scales the score by tau_0^2. |
| yang2026 | https://arxiv.org/pdf/2511.02977v2; Section 2.3, PDF pp. 11-12; Section 3.1, pp. 13-16; Appendix D.2, p. 43 | supports | Re-verified Section 2.3 (PDF pp. 11-12), Section 3.1 (pp. 13-16), and Appendix D.2 (p. 43) of Yang et al. (2026), confirming directional one-sided and two-sided prior-predictive tail calibration of the score statistic and its child-stage use in sequential DAG conflict checks. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Successor scientific review after resolving independent review findings AIM-PR428-E0EC-F1 and AIM-PR428-E0EC-F2 tracked in Issue
- All 31 pages of Nott et al. (2020) and all 52 pages of Yang et al. (2026) were read. No author MCMC or variational implementation, real-data model fit, or empirical repeated-data calibration benchmark was run; constructed analytic examples verify mathematical identities and boundary conditions across unit and non-unit baseline prior variances.
- Resolved AIM-PR428-E0EC-F1 (Issue
- Resolved AIM-PR428-E0EC-F2 (Issue

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261024T102000Z-prior-expansion-score-conflict
kind: record
repository: CultureBotAI/AIMech
title: Successor scientific author self-review of prior-expansion score conflict diagnostic
  after Issue
started_at: '2026-10-24T10:15:00Z'
finished_at: '2026-10-24T10:20:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: Successor adversarial author self-review after resolving independent
    review findings AIM-PR428-E0EC-F1 and AIM-PR428-E0EC-F2 (Issue
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the prior-expansion score conflict diagnostic as a distinct DRAFT
  algorithm with related Bayesian-network context. All seven claims and locators are
  supported after resolving AIM-PR428-E0EC-F1 (dimensionless multiplicative normal
  variance-expansion score verified across unit and non-unit baseline prior variances)
  and AIM-PR428-E0EC-F2 (scalar one-at-a-time directional calibration attributed to
  Nott et al. 2020 Section 1 and Yang et al. 2026 Section 2.3 rather than an unsupported
  covariance-normalized vector quadratic form). Author MCMC/variational code and empirical
  repeated-data calibration remain unverified.
source:
  git_revision: e0ec3050952cf97f111dbf5307873595fe08eed9
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/EvaluationBias.yaml
    sha256: 6523f8c43f7b140c6dd593069e30b7fc1bdd60b89d01bdf5441d2bc83a12e749
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/RandomEffectsModel.yaml
    sha256: 4e3f50ef012b217822c2b731cce1b07dff14e66826f26d7717a6dab42d482d4c
    role: context
  - path: data/curated/CrossValidatedPriorLikelihoodConflictDiagnostic.yaml
    sha256: 92c4daf84d56e0ea6528ee512063fcf8d7fc8c69795bff9fe19fe5de8c65d119
    role: context
  - path: data/curated/GaussianMessageConflictDiagnostic.yaml
    sha256: adc6c4f1c16288b59515f77401ff4d1c2a02f673a00a91963de6e3fa588c4cff
    role: context
  - path: data/curated/INLAGroupNodeConflictDiagnostic.yaml
    sha256: c97bf3553a26f7bb84a4539bf0cfed7d6bbe5170c7df411deb77ca1cf868f0b1
    role: context
  - path: data/curated/MultipleTestingNodeConflictDiagnostic.yaml
    sha256: 1a21330e57dec49c7dd243afce713439382955663f979a1ec9df393d79798a0c
    role: context
  - path: data/curated/PriorExpansionScoreConflictDiagnostic.yaml
    sha256: 39bc0d584ab3947f97aef617baf9742f73d469d3d69b15a68beb84fe7608b401
    role: target
  - path: data/curated/SeparatorNodeConflictDiagnostic.yaml
    sha256: 302a2e72e9e2a174ee433925f4e2e0bcf02f3a2dbc860bcd71e92c97b948e429
    role: context
  - path: history/records/PriorExpansionScoreConflictDiagnostic/2026-10-24T101758Z-antigravity-79cf3e.yaml
    sha256: 745aa6900f85e12cb80ffed008ba4bcfeeaf59a9c65749653e1537affbe3fe07
    role: context
  - path: history/reports/prior-expansion-score-conflict/2026-10-24T101759Z-antigravity-29b549.yaml
    sha256: 4b85263a56e669c3b727b2eea4b74f98a4d1f93710f30ec7e8a078ee6de3feb0
    role: context
  - path: research/discovery/20261017T082300Z-prior-expansion-score-conflict.json
    sha256: 804e5327bf7dda1488a35664cd03d4f47347b27d3ed4e64bbf2673f191d93622
    role: context
  - path: research/discovery/prior-expansion-score-conflict-boundaries.py
    sha256: 5a81d47ff4d439bf8f659861817c0c39357d6e8e0ccfcbe15824e7959bbbbb1f
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
    sha256: 3826f6a7643d6a0140cf60bb52a1d3ac2fbab4811b4fd8d1d178a13c3341fa3f
    role: context
targets:
- target_id: AIMech:PriorExpansionScoreConflictDiagnostic
  path: data/curated/PriorExpansionScoreConflictDiagnostic.yaml
  label: Prior-expansion score conflict diagnostic
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/PriorExpansionScoreConflictDiagnostic.yaml
    role: maintained
scope:
  description: All fields of the corrected maintained prior-expansion score diagnostic
    and its primary evidence after resolving Issue
  selection: 'Exact maintained ID: AIMech:PriorExpansionScoreConflictDiagnostic'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:PriorExpansionScoreConflictDiagnostic
  exclusions:
  - target: Sequential DAG parent-child score conflict diagnostic
    reason: Separate pending concept in Yang et al. (2026) Section 3.1; kept distinct
      from the general Nott et al. (2020) prior-expansion score diagnostic.
  - target: Existing native and AIO neighbors
    reason: Identity and mapping context, not full scientific rereview.
  - target: Source software and empirical calibration
    reason: No author MCMC/variational code, real-data fitting, or repeated-data calibration
      simulation run.
checks:
- check_id: required-0
  name: aimech validation suite
  command: aimech validate && aimech validate-curated && aimech seed --check && aimech
    validate-history --base origin/main && python scripts/record_review.py --repo-root
    . --schema schema/record_review.yaml check --base origin/main
  status: passed
  required: true
  target_ids:
  - AIMech:PriorExpansionScoreConflictDiagnostic
  exit_code: 0
  expected_exit_code: 0
  summary: "Checked 442 record(s); 0 failed.\nChecked 564 curated concept record(s);\
    \ 0 error(s).\nAIO: 442 records; 0 missing, 0 changed, 0 unexpected.\nChecked\
    \ 223 history record(s); 0 error(s).\n{\n  \"repository\": \"CultureBotAI/AIMech\"\
    ,\n  \"valid_reviews\": 218,\n  \"coverage\": \"declared_scopes_only\"\n}\n"
- check_id: required-1
  name: just vendored-check
  command: python scripts/check_vendored_sync.py
  status: passed
  required: true
  target_ids:
  - AIMech:PriorExpansionScoreConflictDiagnostic
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    '
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:PriorExpansionScoreConflictDiagnostic
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
  - AIMech:PriorExpansionScoreConflictDiagnostic
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed prior-expansion score boundaries including non-unit baseline variances
  command: python3 research/discovery/prior-expansion-score-conflict-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:PriorExpansionScoreConflictDiagnostic
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"coordinate_wise_directional_expansions\": {\n    \"location_two_sided_matches_scale_upper_tail\"\
    : true,\n    \"one_at_a_time_identities_agree\": true,\n    \"rows\": [\n    \
    \  {\n        \"p_location_two_sided\": 0.00040695,\n        \"p_scale_upper_tail\"\
    : 0.00040695,\n        \"s_location\": 5.0,\n        \"s_scale\": 2.875,\n   \
    \     \"tau0_sq\": 0.25\n      },\n      {\n        \"p_location_two_sided\":\
    \ 0.02534732,\n        \"p_scale_upper_tail\": 0.02534732,\n        \"s_location\"\
    : 2.0,\n        \"s_scale\": 1.6,\n        \"tau0_sq\": 1.0\n      },\n      {\n\
    \        \"p_location_two_sided\": 0.22525291,\n        \"p_scale_upper_tail\"\
    : 0.22525291,\n        \"s_location\": 0.58823529,\n        \"s_scale\": 0.22145329,\n\
    \        \"tau0_sq\": 4.0\n      }\n    ]\n  },\n  \"evans_moshonov_equivalence\"\
    : {\n    \"exact_equivalence\": true,\n    \"p_evans_moshonov\": 0.02534732,\n\
    \    \"p_score_upper_tail\": 0.02534732,\n    \"tested_tau0_sq_values\": [\n \
    \     0.25,\n      1.0,\n      2.0,\n      4.0\n    ],\n    \"z_obs\": 2.23606798\n\
    \  },\n  \"fisher_and_renyi\": {\n    \"identities_agree\": true,\n    \"neg_d_fixed_posterior_kl\"\
    : 1.6,\n    \"neg_d_varying_posterior_kl\": 0.88,\n    \"non_unit_tau0_sq_4_v_025_score\"\
    : 0.22145329,\n    \"non_unit_tau0_sq_4_v_025_tau2_derivative\": 0.05536332,\n\
    \    \"s_claim_expanded\": 1.6,\n    \"s_direct\": 1.6,\n    \"s_fisher\": 1.6,\n\
    \    \"s_tau2_example_4_1\": 1.6,\n    \"tested_grid_size\": 20,\n    \"varying_posterior_differs_by_cov_term\"\
    : true\n  },\n  \"hierarchical_normal_random_effects\": {\n    \"s1_lower_mixed\"\
    : 0.22687596,\n    \"s2_upper_marginal\": 0.99722992,\n    \"ss_between\": 2.48,\n\
    \    \"upper_score_positive_for_grand_mean_shift\": true,\n    \"y_grand\": 2.0\n\
    \  },\n  \"support_dependent_boundary\": {\n    \"boundary_posterior_density\"\
    : 0.31303529,\n    \"naive_fails_by_boundary_term\": true,\n    \"reparameterized_matches_exact\"\
    : true,\n    \"s_exact_fd\": -0.68696471,\n    \"s_naive_eq_1_3\": -1.0,\n   \
    \ \"s_reparameterized\": -0.68696471\n  }\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T082300Z-prior-expansion-score-conflict.json
  accessed_at: '2026-10-24T10:17:00Z'
  support: supports
  summary: No normalized identity match for the prior-expansion score conflict diagnostic
    across 442 pinned AIO records and 563 other maintained IDs, names, aliases and
    scoped synonyms. This concept denotes score-type prior-data conflict diagnostics
    formed by differentiating log marginal likelihood along a smooth scalar or coordinate-wise
    prior expansion family at the baseline prior via Fisher's identity; it is distinct
    from cross-validated held-out prior-likelihood splitting, separator node splitting,
    INLA group node splitting, and sequential DAG parent-child score checks.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-24T10:17:00Z'
  support: supports
  summary: Inspected BayesianNetwork, ProbabilisticGraphicalModel, RandomEffectsModel,
    and EvaluationBias in the pinned AIO snapshot (2026-07-22). BayesianNetwork and
    ProbabilisticGraphicalModel supply directed acyclic graph and hierarchical conditional
    factorization context as related_match mappings, while RandomEffectsModel supplies
    random-effects stage context.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/prior-expansion-score-conflict-boundaries.py
  accessed_at: '2026-10-24T10:17:00Z'
  snapshot_sha256: 5a81d47ff4d439bf8f659861817c0c39357d6e8e0ccfcbe15824e7959bbbbb1f
  support: supports
  summary: Constructed exact analytic and numerical checks across unit and non-unit
    baseline prior variances (tau_0^2 in {0.25, 1.0, 2.0, 4.0} and sigma^2/n in {0.1,
    0.25, 0.5, 1.0, 2.0}) for (1) Fisher's identity, the dimensionless multiplicative
    normal variance-expansion score S(y) = tau_0^2 S_{tau^2}(y), and fixed-posterior
    versus varying-posterior Renyi divergence derivatives, (2) exact normal-location
    equivalence with the Evans-Moshonov prior-predictive p-value, (3) one-at-a-time
    scalar directional location and scale prior expansions and tail calibration, (4)
    two-stage hierarchical normal mixed-predictive and prior-predictive scores, and
    (5) support-dependent boundary failure of naive integral-derivative interchange.
- evidence_id: nott2020
  kind: primary_source
  reference: https://arxiv.org/pdf/1902.10393v2
  locator: Section 1, PDF pp. 2-4; Section 2.1-2.2, pp. 4-6; Section 3, pp. 6-8; Section
    4.1-4.3, pp. 8-13; Section 5, pp. 13-16
  accessed_at: '2026-10-24T10:15:00Z'
  snapshot_sha256: 2d36e3af352ac38b3811af3540aed3d115be5f4b4f6ecdadb4ec8fec74d07a99
  support: supports
  summary: Re-verified all cited sections of Nott et al. (2020), specifically confirming
    that Section 1 (PDF p. 2) restricts gamma to a scalar or one-at-a-time coordinate-wise
    expansion parameter and that Example 4.1 (PDF p. 8) differentiates directly with
    respect to gamma = tau^2 at tau_0^2 so that multiplicative variance scaling theta
    | gamma ~ N(mu_0, gamma tau_0^2) at gamma_0 = 1 scales the score by tau_0^2.
- evidence_id: yang2026
  kind: primary_source
  reference: https://arxiv.org/pdf/2511.02977v2
  locator: Section 2.3, PDF pp. 11-12; Section 3.1, pp. 13-16; Appendix D.2, p. 43
  accessed_at: '2026-10-24T10:15:00Z'
  snapshot_sha256: 4829e0d63d562483aa6aab88a418c62e6d336cd63e9205ee175bf9e9c1bade2d
  support: supports
  summary: Re-verified Section 2.3 (PDF pp. 11-12), Section 3.1 (pp. 13-16), and Appendix
    D.2 (p. 43) of Yang et al. (2026), confirming directional one-sided and two-sided
    prior-predictive tail calibration of the score statistic and its child-stage use
    in sequential DAG conflict checks.
assessments:
- assessment_id: identity
  area: identity
  topic: Prior-expansion score diagnostic versus node-splitting and sequential DAG
    checks
  outcome: supported
  target_ids:
  - AIMech:PriorExpansionScoreConflictDiagnostic
  evidence_ids:
  - identity
  - nott2020
  - yang2026
  summary: Retain the prior-expansion score conflict diagnostic as a distinct DRAFT
    algorithm.
  details: The diagnostic is defined by embedding a baseline prior in a smooth expansion
    family g(theta | gamma) and evaluating the posterior expectation of the prior
    score at gamma_0 via Fisher's identity. Unlike cross-validated prior-likelihood
    or separator/INLA node-splitting diagnostics, it does not partition data or duplicate
    graphical nodes into split posteriors. The sequential parent-to-child DAG conflict
    procedure of Yang et al. (2026) uses this score discrepancy as its second-stage
    building block and remains a separate concept.
- assessment_id: mapping
  area: grounding
  topic: Diagnostic-to-BayesianNetwork, ProbabilisticGraphicalModel, and RandomEffectsModel
    relations
  outcome: supported
  target_ids:
  - AIMech:PriorExpansionScoreConflictDiagnostic
  evidence_ids:
  - mapping
  - nott2020
  - yang2026
  summary: Related BayesianNetwork, ProbabilisticGraphicalModel, and RandomEffectsModel
    mappings are supported.
  details: The diagnostic checks prior-data and hierarchical stagewise conflict in
    Bayesian models, probabilistic graphical models, and random-effects models. Those
    three AIO classes supply representation and model context via related_match without
    asserting subclass or equivalence semantics.
- assessment_id: prior-expansion-fisher-score
  area: evidence
  topic: prior-expansion-fisher-score
  outcome: supported
  target_ids:
  - AIMech:PriorExpansionScoreConflictDiagnostic
  evidence_ids:
  - nott2020
  - yang2026
  - calculation
  summary: Supported with explicit support-independence and regularity boundaries.
  details: Embedding g(theta)=g(theta|gamma_0) in a smooth expansion family g(theta|gamma)
    defines S(y) = d/dgamma log p(y|gamma)|_{gamma_0}. Under regularity conditions
    allowing interchange of differentiation and integration on a gamma-independent
    parameter support, Fisher's identity expresses S(y) as the posterior expectation
    int [d/dgamma log g(theta|gamma)|_{gamma_0}] g(theta|y) dtheta. Constructed boundary
    checks confirm that when support depends on gamma (e.g. Uniform(0,gamma)), naive
    differentiation under the integral sign misses the boundary posterior density
    term unless reparameterized to a fixed domain.
- assessment_id: relative-belief-renyi-sensitivity
  area: evidence
  topic: relative-belief-renyi-sensitivity
  outcome: supported
  target_ids:
  - AIMech:PriorExpansionScoreConflictDiagnostic
  evidence_ids:
  - nott2020
  - calculation
  summary: Supported with the fixed-posterior weighting distinction made explicit.
  details: Because the relative belief ratio RB(theta|y,gamma) = p(y|theta)/p(y|gamma)
    depends on gamma solely through p(y|gamma)^(-1), differentiating log RB(theta|y,gamma),
    the baseline-posterior-weighted Renyi functional (Equation 2.3, where g(theta|y)
    in the integral weight is held fixed at gamma_0), or the fixed-posterior KL divergence
    KL(g(theta|y) || g(theta|gamma)) with respect to gamma at gamma_0 yields -S(y)
    identically for every alpha > 0. Varying the posterior weighting density g(theta|y,gamma)
    inside R_alpha(g(theta|y,gamma) || g(theta|gamma)) adds a posterior covariance
    term.
- assessment_id: coordinate-wise-directional-calibration
  area: evidence
  topic: coordinate-wise-directional-calibration
  outcome: supported
  target_ids:
  - AIMech:PriorExpansionScoreConflictDiagnostic
  evidence_ids:
  - nott2020
  - yang2026
  - calculation
  summary: Supported after resolving AIM-PR428-E0EC-F2 to reflect scalar one-at-a-time
    expansions and directional tail calibration.
  details: Nott et al. (2020) Section 1 (PDF p. 2) restricts gamma to a scalar parameter
    or one-at-a-time coordinate-wise perturbations when multiple baseline hyperparameters
    exist, calibrating each scalar score S_j(y) against the prior predictive distribution
    p(y) using upper-tail probabilities for variance-broadening expansions and two-sided
    tail probabilities for location-shift expansions (Section 1, pp. 3-4; Yang et
    al. 2026 Section 2.3, pp. 11-12).
- assessment_id: evans-moshonov-normal-location-equivalence
  area: evidence
  topic: evans-moshonov-normal-location-equivalence
  outcome: supported
  target_ids:
  - AIMech:PriorExpansionScoreConflictDiagnostic
  evidence_ids:
  - nott2020
  - calculation
  summary: Supported and verified analytically across unit and non-unit baseline prior
    variances after resolving AIM-PR428-E0EC-F1.
  details: Under multiplicative variance expansion theta | gamma ~ N(mu_0, gamma*tau_0^2)
    at gamma_0 = 1, the dimensionless score is S(y) = (1/(2*tau_0^2)) E[theta^2 -
    2*theta*mu_0 + mu_0^2 - tau_0^2 | y] = (tau_0^2/2) * [(x_bar - mu_0)^2 / (tau_0^2
    + sigma^2/n)^2 - 1 / (tau_0^2 + sigma^2/n)], which equals tau_0^2 times the direct
    variance derivative S_{tau^2}(y) of Nott et al. (2020) Example 4.1 (PDF p. 8).
    Because S(y) is a strictly increasing affine function of (x_bar - mu_0)^2 for
    every tau_0^2 > 0, its upper-tail prior-predictive p-value equals the Evans-Moshonov
    (2006) prior-predictive p-value identically.
- assessment_id: exponential-family-conjugate-score-expectation
  area: evidence
  topic: exponential-family-conjugate-score-expectation
  outcome: supported
  target_ids:
  - AIMech:PriorExpansionScoreConflictDiagnostic
  evidence_ids:
  - nott2020
  - calculation
  summary: Supported for exponential-family priors via posterior expectations of sufficient
    statistics.
  details: When the expanded prior family g(theta|gamma) = h(theta) exp(eta(gamma)^T
    T(theta) - A(eta(gamma))) belongs to an exponential family, the prior score d/dgamma
    log g(theta|gamma)|_{gamma_0} is linear in the sufficient statistics T(theta),
    reducing S(y) to a linear combination of posterior expectations E[T(theta)|y]
    minus prior expectations E[T(theta)|gamma_0] as shown in Nott et al. (2020) Section
    4.1-4.3 (PDF pp. 8-13).
- assessment_id: hierarchical-stagewise-mixed-predictive-scores
  area: evidence
  topic: hierarchical-stagewise-mixed-predictive-scores
  outcome: supported
  target_ids:
  - AIMech:PriorExpansionScoreConflictDiagnostic
  evidence_ids:
  - nott2020
  - calculation
  summary: Supported with explicit stagewise reference distributions.
  details: In a two-stage hierarchical model p(y|theta_1)g_1(theta_1|theta_2)g_2(theta_2),
    expanding the first-stage prior g_1(theta_1|theta_2,zeta) checks lower-level conflict
    against a mixed predictive reference p_M(y) that draws theta_2' ~ g(theta_2|y_obs),
    theta_1' ~ g_1(theta_1|theta_2'), and y ~ p(y|theta_1'), whereas expanding the
    hyperprior g_2(theta_2|eta) checks upper-level conflict against the marginal prior
    predictive p(y).
- assessment_id: variational-posterior-score-approximation
  area: evidence
  topic: variational-posterior-score-approximation
  outcome: supported
  target_ids:
  - AIMech:PriorExpansionScoreConflictDiagnostic
  evidence_ids:
  - nott2020
  summary: Supported with explicit variational-error caveat.
  details: Evaluating S(y) requires only posterior expectations of the prior score
    under the baseline model and can be approximated by substituting a Gaussian variational
    posterior q(theta) for g(theta|y) in both observed and simulated reference datasets,
    subject to variational approximation bias.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:PriorExpansionScoreConflictDiagnostic
  evidence_ids:
  - identity
  - mapping
  - nott2020
  - yang2026
  - calculation
  summary: The full record is consistent after resolving Issue
  details: 'Read every field of PriorExpansionScoreConflictDiagnostic.yaml: stable
    ID, name, aliases, algorithm kind, definition, definition_evidence, identity_notes,
    seven claims and locators, two full-text primary sources with exact SHA-256 digests,
    three pinned AIO mappings and rationales, five scoped limitations, and UTC curation
    metadata. All repository validation checks and constructed boundary assertions
    across unit and non-unit baseline variances passed.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Successor scientific review after resolving independent review findings AIM-PR428-E0EC-F1
  and AIM-PR428-E0EC-F2 tracked in Issue
- All 31 pages of Nott et al. (2020) and all 52 pages of Yang et al. (2026) were read.
  No author MCMC or variational implementation, real-data model fit, or empirical
  repeated-data calibration benchmark was run; constructed analytic examples verify
  mathematical identities and boundary conditions across unit and non-unit baseline
  prior variances.
notes:
- Resolved AIM-PR428-E0EC-F1 (Issue
- Resolved AIM-PR428-E0EC-F2 (Issue
related_reviews:
- repository: CultureBotAI/AIMech
  review_id: 20261017T083500Z-prior-expansion-score-conflict
  relationship: Predecessor scientific self-review before resolving AIM-PR428-E0EC-F1
    and AIM-PR428-E0EC-F2 (Issue
links:
- https://github.com/CultureBotAI/AIMech/issues/432
tags:
- native-concepts
- model-diagnostics
- prior-data-conflict
- self-review
- issue-432
```
