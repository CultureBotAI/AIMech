# Scientific author self-review of prior-expansion score conflict diagnostic

- Review: 20261017T083500Z-prior-expansion-score-conflict
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T08:31:00Z
- Finished UTC: 2026-10-17T08:35:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain the prior-expansion score conflict diagnostic as a distinct DRAFT algorithm with related Bayesian-network context. All seven claims and locators are supported with explicit family choice, fixed-posterior Renyi weighting, support-independent integral interchange, covariance-invertibility, and calibration boundaries. No actionable defect was found; author MCMC/variational code and empirical calibration remain unverified.

## Scope And Provenance

All fields of the exact maintained prior-expansion score diagnostic and its primary evidence.

Selection: Exact maintained ID: AIMech:PriorExpansionScoreConflictDiagnostic
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base b325dd440bc5d8e2fc33a58a1807559859723fb0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:PriorExpansionScoreConflictDiagnostic | data/curated/PriorExpansionScoreConflictDiagnostic.yaml | maintained | Prior-expansion score conflict diagnostic |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validation suite | passed | True | AIMech:PriorExpansionScoreConflictDiagnostic | Checked 442 record(s); 0 failed.<br>Checked 562 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 215 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 214,<br>  "coverage": "declared_scopes_only"<br>}<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:PriorExpansionScoreConflictDiagnostic | OK: 22 governed artifacts match the pinned claw revision<br> |
| aimech check-source | passed | True | AIMech:PriorExpansionScoreConflictDiagnostic | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:PriorExpansionScoreConflictDiagnostic | Exited 0 without output. |
| Constructed prior-expansion score boundaries | passed | True | AIMech:PriorExpansionScoreConflictDiagnostic | {<br>  "evans_moshonov_equivalence": {<br>    "exact_equivalence": true,<br>    "p_evans_moshonov": 0.02534732,<br>    "p_score_upper_tail": 0.02534732,<br>    "z_obs": 2.23606798<br>  },<br>  "fisher_and_renyi": {<br>    "identities_agree": true,<br>    "neg_d_fixed_posterior_kl": 1.6,<br>    "neg_d_varying_posterior_kl": 0.88,<br>    "s_direct": 1.6,<br>    "s_example_4_1": 1.6,<br>    "s_fisher": 1.6,<br>    "varying_posterior_differs_by_cov_term": true<br>  },<br>  "hierarchical_normal_random_effects": {<br>    "s1_lower_mixed": 0.22687596,<br>    "s2_upper_marginal": 0.99722992,<br>    "ss_between": 2.48,<br>    "upper_score_positive_for_grand_mean_shift": true,<br>    "y_grand": 2.0<br>  },<br>  "multivariate_quadratic_score": {<br>    "d_closed": 13.0,<br>    "d_obs": 13.0,<br>    "quadratic_form_matches": true,<br>    "s1": 2.0,<br>    "s2": 1.6,<br>    "var_s1": 0.8,<br>    "var_s2": 0.32<br>  },<br>  "support_dependent_boundary": {<br>    "boundary_posterior_density": 0.31303529,<br>    "naive_fails_by_boundary_term": true,<br>    "reparameterized_matches_exact": true,<br>    "s_exact_fd": -0.68696471,<br>    "s_naive_eq_1_3": -1.0,<br>    "s_reparameterized": -0.68696471<br>  }<br>} |

## Scientific And Domain Assessments

### Prior-expansion score diagnostic versus node-splitting and sequential DAG checks

identity: supported. Targets: AIMech:PriorExpansionScoreConflictDiagnostic.

Retain the prior-expansion score conflict diagnostic as a distinct DRAFT algorithm.

The diagnostic is defined by embedding a baseline prior in a smooth expansion family g(theta &#124; gamma) and evaluating the posterior expectation of the prior score vector at gamma_0 via Fisher's identity. Unlike cross-validated prior-likelihood or separator/INLA node-splitting diagnostics, it does not partition data or duplicate graphical nodes into split posteriors. The sequential parent-to-child DAG conflict procedure of Yang et al. (2026) uses this score discrepancy as its second-stage building block and remains a separate concept.

### Diagnostic-to-BayesianNetwork representation relation

grounding: supported. Targets: AIMech:PriorExpansionScoreConflictDiagnostic.

Related BayesianNetwork mapping is supported.

The diagnostic checks prior-data and hierarchical stagewise conflict in Bayesian models and Bayesian DAG factorizations. BayesianNetwork supplies the graphical representation context via related_match without asserting subclass or equivalence semantics.

### prior-expansion-fisher-score

evidence: supported. Targets: AIMech:PriorExpansionScoreConflictDiagnostic.

Supported with explicit support-independence and regularity boundaries.

Embedding g(theta)=g(theta&#124;gamma_0) in a smooth expansion family g(theta&#124;gamma) defines S(y) = d/dgamma log p(y&#124;gamma)&#124;_{gamma_0}. Under regularity conditions allowing interchange of differentiation and integration on a gamma-independent parameter support, Fisher's identity expresses S(y) as the posterior expectation int [d/dgamma log g(theta&#124;gamma)&#124;_{gamma_0}] g(theta&#124;y) dtheta. Our constructed boundary script confirms that when support depends on gamma (e.g. Uniform(0,gamma)), naive differentiation under the integral sign misses the boundary posterior density term unless reparameterized to a fixed domain.

### relative-belief-renyi-sensitivity

evidence: supported. Targets: AIMech:PriorExpansionScoreConflictDiagnostic.

Supported with the fixed-posterior weighting distinction made explicit.

Because the relative belief ratio RB(theta&#124;y,gamma) = p(y&#124;theta)/p(y&#124;gamma) depends on gamma solely through p(y&#124;gamma)^(-1), differentiating log RB(theta&#124;y,gamma), the baseline-posterior-weighted Renyi functional (Equation 2.3, where g(theta&#124;y) in the integral weight is held fixed at gamma_0), or the fixed-posterior KL divergence KL(g(theta&#124;y) &#124;&#124; g(theta&#124;gamma)) with respect to gamma at gamma_0 yields -S(y) identically for every alpha &gt; 0. Varying the posterior weighting density g(theta&#124;y,gamma) inside R_alpha(g(theta&#124;y,gamma) &#124;&#124; g(theta&#124;gamma)) adds a posterior covariance term.

### multivariate-quadratic-score-form

evidence: supported. Targets: AIMech:PriorExpansionScoreConflictDiagnostic.

Supported with positive-definite covariance requirements.

For a multi-parameter expansion vector gamma, the vector score S(y) is combined into the quadratic form D(y) = S(y)^T V_S^(-1) S(y) using the prior-predictive covariance V_S = Cov_{Y~p(y)}(S(Y)), with p-value P_{Y~p(y)}(D(Y) &gt;= D(y_obs)). This requires V_S to be finite and positive definite.

### evans-moshonov-normal-location-equivalence

evidence: supported. Targets: AIMech:PriorExpansionScoreConflictDiagnostic.

Supported and verified analytically.

In the conjugate normal location model with variance expansion N(mu_0, gamma*tau^2) around gamma_0=1, S(y) is a strictly increasing affine function of (x_bar - mu_0)^2, making the upper-tail score p-value identical to the Evans-Moshonov (2006) prior-predictive p-value.

### hierarchical-stagewise-mixed-predictive-scores

evidence: supported. Targets: AIMech:PriorExpansionScoreConflictDiagnostic.

Supported with explicit stagewise reference distributions.

In a two-stage hierarchical model p(y&#124;theta_1)g_1(theta_1&#124;theta_2)g_2(theta_2), expanding the first-stage prior g_1(theta_1&#124;theta_2,zeta) checks lower-level conflict against a mixed predictive reference p_M(y) that draws theta_2' ~ g(theta_2&#124;y_obs), theta_1' ~ g_1(theta_1&#124;theta_2'), and y ~ p(y&#124;theta_1'), whereas expanding the hyperprior g_2(theta_2&#124;eta) checks upper-level conflict against the marginal prior predictive p(y).

### variational-posterior-score-approximation

evidence: supported. Targets: AIMech:PriorExpansionScoreConflictDiagnostic.

Supported with explicit variational-error caveat.

Evaluating S(y) requires only posterior expectations of the prior score vector under the baseline model and can be approximated by substituting a Gaussian variational posterior q(theta) for g(theta&#124;y) in both observed and simulated reference datasets, subject to variational approximation bias.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:PriorExpansionScoreConflictDiagnostic.

The full record is consistent; retain DRAFT.

Read every field of PriorExpansionScoreConflictDiagnostic.yaml: stable ID, name, aliases, algorithm kind, definition, definition_evidence, identity_notes, six claims and locators, two full-text primary sources with exact SHA-256 digests, pinned AIO mapping and rationale, five scoped limitations, and UTC curation metadata. All repository validation checks and constructed boundary assertions passed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T082300Z-prior-expansion-score-conflict.json | supports | No normalized identity match for the prior-expansion score conflict diagnostic across 442 pinned AIO records and 561 maintained IDs, names, aliases and scoped synonyms. Ignored- and hidden-inclusive fixed-string searches across data, sources, research, history, and reviews returned 5 lines (1 pending frontier entry for Nott et al. 2020/2021 in 20261013T013528Z-inla-group-node-conflict.json and 4 unrelated Fisher references). This concept denotes score-type prior-data conflict diagnostics formed by differentiating log marginal likelihood along a smooth prior expansion family at the baseline prior via Fisher's identity; it is distinct from cross-validated held-out prior-likelihood splitting, separator node splitting, INLA group node splitting, and sequential DAG parent-child score checks. |
| mapping | sources/aio/aio.json | supports | Inspected BayesianNetwork, ProbabilisticGraphicalModel, and EvaluationBias in the pinned AIO snapshot (2026-07-22). BayesianNetwork supplies directed acyclic graph and hierarchical conditional factorization context as a related_match rather than an algorithm superclass. |
| calculation | research/discovery/prior-expansion-score-conflict-boundaries.py | supports | Constructed exact analytic and numerical checks for (1) Fisher's identity and fixed-posterior versus varying-posterior Renyi divergence derivatives, (2) exact normal-location equivalence with the Evans-Moshonov prior-predictive p-value, (3) 2D location-scale multivariate quadratic score, (4) two-stage hierarchical normal mixed-predictive and prior-predictive scores, and (5) support-dependent boundary failure of naive integral-derivative interchange. No MCMC, variational fitting, or author software. |
| nott2020 | https://arxiv.org/pdf/1902.10393v2; Section 1, PDF pp. 2-4; Section 2.1-2.2, pp. 4-6; Section 3, pp. 6-8; Section 4.1-4.3, pp. 8-13; Section 5, pp. 13-16 | supports | All 31 pages of the primary manuscript read, including equations (1.1)-(5.3), Examples 4.1-4.3, Sections 5.1-5.2, and references. Checked prior-expansion score definition, Fisher's identity, relative belief and fixed-posterior Renyi divergence derivative, multivariate quadratic discrepancy, hierarchical stagewise mixed/prior-predictive calibration, and variational substitution. |
| yang2026 | https://arxiv.org/pdf/2511.02977v2; Section 2.3, PDF pp. 11-12; Section 3.1, pp. 13-16; Appendix D.2, p. 43 | supports | All 52 pages of the follow-up DAG conflict-checking manuscript read, including Section 2.3 reviewing the Nott et al. (2020/2021) score-based check and Section 3.1 showing its use as the child-stage score discrepancy within sequential DAG conflict checks. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT prior-expansion score conflict diagnostic, yielding 562 native and 442 unchanged generated records.
- All 31 pages of Nott et al. (2020) and all 52 pages of Yang et al. (2026) were read. No author MCMC or variational implementation, real-data model fit, or empirical repeated-data calibration benchmark was run; constructed analytic examples verify mathematical identities and boundary conditions only.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083500Z-prior-expansion-score-conflict
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of prior-expansion score conflict diagnostic
started_at: '2026-10-17T08:31:00Z'
finished_at: '2026-10-17T08:35:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness, Fisher/Renyi
    score identities, fixed-posterior versus varying-posterior Renyi differentiation,
    support-independent differentiation under the integral sign, covariance singularity,
    hierarchical stage replication laws, mapping and source support. This is adversarial
    author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain the prior-expansion score conflict diagnostic as a distinct DRAFT
  algorithm with related Bayesian-network context. All seven claims and locators are
  supported with explicit family choice, fixed-posterior Renyi weighting, support-independent
  integral interchange, covariance-invertibility, and calibration boundaries. No actionable
  defect was found; author MCMC/variational code and empirical calibration remain
  unverified.
source:
  git_revision: b325dd440bc5d8e2fc33a58a1807559859723fb0
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
    sha256: a52b0ed1f942269c6a9fe0f48683b4d69a0706f522633b70e85bc05f48d8f792
    role: target
  - path: data/curated/SeparatorNodeConflictDiagnostic.yaml
    sha256: 302a2e72e9e2a174ee433925f4e2e0bcf02f3a2dbc860bcd71e92c97b948e429
    role: context
  - path: research/discovery/20261017T082300Z-prior-expansion-score-conflict.json
    sha256: 8fa15c57f7ef020f304d60b6766aca9a6ec29a70f87d13b1102ff8efe4187de2
    role: context
  - path: research/discovery/prior-expansion-score-conflict-boundaries.py
    sha256: 294b67b3699f2d4b28701378ab546bc19af2a7e573612939967202dd717d7f91
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
  description: All fields of the exact maintained prior-expansion score diagnostic
    and its primary evidence.
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
    validate-history && python scripts/record_review.py --repo-root . check
  status: passed
  required: true
  target_ids:
  - AIMech:PriorExpansionScoreConflictDiagnostic
  exit_code: 0
  expected_exit_code: 0
  summary: "Checked 442 record(s); 0 failed.\nChecked 562 curated concept record(s);\
    \ 0 error(s).\nAIO: 442 records; 0 missing, 0 changed, 0 unexpected.\nChecked\
    \ 215 history record(s); 0 error(s).\n{\n  \"repository\": \"CultureBotAI/AIMech\"\
    ,\n  \"valid_reviews\": 214,\n  \"coverage\": \"declared_scopes_only\"\n}\ntopClass\
    \ is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: bash scripts/check_vendored_sync.sh
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
  name: Constructed prior-expansion score boundaries
  command: python3 research/discovery/prior-expansion-score-conflict-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:PriorExpansionScoreConflictDiagnostic
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"evans_moshonov_equivalence\": {\n    \"exact_equivalence\": true,\n\
    \    \"p_evans_moshonov\": 0.02534732,\n    \"p_score_upper_tail\": 0.02534732,\n\
    \    \"z_obs\": 2.23606798\n  },\n  \"fisher_and_renyi\": {\n    \"identities_agree\"\
    : true,\n    \"neg_d_fixed_posterior_kl\": 1.6,\n    \"neg_d_varying_posterior_kl\"\
    : 0.88,\n    \"s_direct\": 1.6,\n    \"s_example_4_1\": 1.6,\n    \"s_fisher\"\
    : 1.6,\n    \"varying_posterior_differs_by_cov_term\": true\n  },\n  \"hierarchical_normal_random_effects\"\
    : {\n    \"s1_lower_mixed\": 0.22687596,\n    \"s2_upper_marginal\": 0.99722992,\n\
    \    \"ss_between\": 2.48,\n    \"upper_score_positive_for_grand_mean_shift\"\
    : true,\n    \"y_grand\": 2.0\n  },\n  \"multivariate_quadratic_score\": {\n \
    \   \"d_closed\": 13.0,\n    \"d_obs\": 13.0,\n    \"quadratic_form_matches\"\
    : true,\n    \"s1\": 2.0,\n    \"s2\": 1.6,\n    \"var_s1\": 0.8,\n    \"var_s2\"\
    : 0.32\n  },\n  \"support_dependent_boundary\": {\n    \"boundary_posterior_density\"\
    : 0.31303529,\n    \"naive_fails_by_boundary_term\": true,\n    \"reparameterized_matches_exact\"\
    : true,\n    \"s_exact_fd\": -0.68696471,\n    \"s_naive_eq_1_3\": -1.0,\n   \
    \ \"s_reparameterized\": -0.68696471\n  }\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T082300Z-prior-expansion-score-conflict.json
  accessed_at: '2026-10-17T08:23:00Z'
  support: supports
  summary: No normalized identity match for the prior-expansion score conflict diagnostic
    across 442 pinned AIO records and 561 maintained IDs, names, aliases and scoped
    synonyms. Ignored- and hidden-inclusive fixed-string searches across data, sources,
    research, history, and reviews returned 5 lines (1 pending frontier entry for
    Nott et al. 2020/2021 in 20261013T013528Z-inla-group-node-conflict.json and 4
    unrelated Fisher references). This concept denotes score-type prior-data conflict
    diagnostics formed by differentiating log marginal likelihood along a smooth prior
    expansion family at the baseline prior via Fisher's identity; it is distinct from
    cross-validated held-out prior-likelihood splitting, separator node splitting,
    INLA group node splitting, and sequential DAG parent-child score checks.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T08:23:00Z'
  support: supports
  summary: Inspected BayesianNetwork, ProbabilisticGraphicalModel, and EvaluationBias
    in the pinned AIO snapshot (2026-07-22). BayesianNetwork supplies directed acyclic
    graph and hierarchical conditional factorization context as a related_match rather
    than an algorithm superclass.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/prior-expansion-score-conflict-boundaries.py
  accessed_at: '2026-10-17T08:23:00Z'
  snapshot_sha256: 294b67b3699f2d4b28701378ab546bc19af2a7e573612939967202dd717d7f91
  support: supports
  summary: Constructed exact analytic and numerical checks for (1) Fisher's identity
    and fixed-posterior versus varying-posterior Renyi divergence derivatives, (2)
    exact normal-location equivalence with the Evans-Moshonov prior-predictive p-value,
    (3) 2D location-scale multivariate quadratic score, (4) two-stage hierarchical
    normal mixed-predictive and prior-predictive scores, and (5) support-dependent
    boundary failure of naive integral-derivative interchange. No MCMC, variational
    fitting, or author software.
- evidence_id: nott2020
  kind: primary_source
  reference: https://arxiv.org/pdf/1902.10393v2
  locator: Section 1, PDF pp. 2-4; Section 2.1-2.2, pp. 4-6; Section 3, pp. 6-8; Section
    4.1-4.3, pp. 8-13; Section 5, pp. 13-16
  accessed_at: '2026-10-17T08:20:00Z'
  snapshot_sha256: 2d36e3af352ac38b3811af3540aed3d115be5f4b4f6ecdadb4ec8fec74d07a99
  support: supports
  summary: All 31 pages of the primary manuscript read, including equations (1.1)-(5.3),
    Examples 4.1-4.3, Sections 5.1-5.2, and references. Checked prior-expansion score
    definition, Fisher's identity, relative belief and fixed-posterior Renyi divergence
    derivative, multivariate quadratic discrepancy, hierarchical stagewise mixed/prior-predictive
    calibration, and variational substitution.
- evidence_id: yang2026
  kind: primary_source
  reference: https://arxiv.org/pdf/2511.02977v2
  locator: Section 2.3, PDF pp. 11-12; Section 3.1, pp. 13-16; Appendix D.2, p. 43
  accessed_at: '2026-10-17T08:20:00Z'
  snapshot_sha256: 4829e0d63d562483aa6aab88a418c62e6d336cd63e9205ee175bf9e9c1bade2d
  support: supports
  summary: All 52 pages of the follow-up DAG conflict-checking manuscript read, including
    Section 2.3 reviewing the Nott et al. (2020/2021) score-based check and Section
    3.1 showing its use as the child-stage score discrepancy within sequential DAG
    conflict checks.
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
    score vector at gamma_0 via Fisher's identity. Unlike cross-validated prior-likelihood
    or separator/INLA node-splitting diagnostics, it does not partition data or duplicate
    graphical nodes into split posteriors. The sequential parent-to-child DAG conflict
    procedure of Yang et al. (2026) uses this score discrepancy as its second-stage
    building block and remains a separate concept.
- assessment_id: mapping
  area: grounding
  topic: Diagnostic-to-BayesianNetwork representation relation
  outcome: supported
  target_ids:
  - AIMech:PriorExpansionScoreConflictDiagnostic
  evidence_ids:
  - mapping
  - nott2020
  - yang2026
  summary: Related BayesianNetwork mapping is supported.
  details: The diagnostic checks prior-data and hierarchical stagewise conflict in
    Bayesian models and Bayesian DAG factorizations. BayesianNetwork supplies the
    graphical representation context via related_match without asserting subclass
    or equivalence semantics.
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
    int [d/dgamma log g(theta|gamma)|_{gamma_0}] g(theta|y) dtheta. Our constructed
    boundary script confirms that when support depends on gamma (e.g. Uniform(0,gamma)),
    naive differentiation under the integral sign misses the boundary posterior density
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
- assessment_id: multivariate-quadratic-score-form
  area: evidence
  topic: multivariate-quadratic-score-form
  outcome: supported
  target_ids:
  - AIMech:PriorExpansionScoreConflictDiagnostic
  evidence_ids:
  - nott2020
  - yang2026
  - calculation
  summary: Supported with positive-definite covariance requirements.
  details: For a multi-parameter expansion vector gamma, the vector score S(y) is
    combined into the quadratic form D(y) = S(y)^T V_S^(-1) S(y) using the prior-predictive
    covariance V_S = Cov_{Y~p(y)}(S(Y)), with p-value P_{Y~p(y)}(D(Y) >= D(y_obs)).
    This requires V_S to be finite and positive definite.
- assessment_id: evans-moshonov-normal-location-equivalence
  area: evidence
  topic: evans-moshonov-normal-location-equivalence
  outcome: supported
  target_ids:
  - AIMech:PriorExpansionScoreConflictDiagnostic
  evidence_ids:
  - nott2020
  - calculation
  summary: Supported and verified analytically.
  details: In the conjugate normal location model with variance expansion N(mu_0,
    gamma*tau^2) around gamma_0=1, S(y) is a strictly increasing affine function of
    (x_bar - mu_0)^2, making the upper-tail score p-value identical to the Evans-Moshonov
    (2006) prior-predictive p-value.
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
    vector under the baseline model and can be approximated by substituting a Gaussian
    variational posterior q(theta) for g(theta|y) in both observed and simulated reference
    datasets, subject to variational approximation bias.
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
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of PriorExpansionScoreConflictDiagnostic.yaml: stable
    ID, name, aliases, algorithm kind, definition, definition_evidence, identity_notes,
    six claims and locators, two full-text primary sources with exact SHA-256 digests,
    pinned AIO mapping and rationale, five scoped limitations, and UTC curation metadata.
    All repository validation checks and constructed boundary assertions passed.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT prior-expansion score conflict diagnostic, yielding 562 native and
  442 unchanged generated records.
- All 31 pages of Nott et al. (2020) and all 52 pages of Yang et al. (2026) were read.
  No author MCMC or variational implementation, real-data model fit, or empirical
  repeated-data calibration benchmark was run; constructed analytic examples verify
  mathematical identities and boundary conditions only.
related_reviews: []
links: []
tags:
- native-concepts
- model-diagnostics
- prior-data-conflict
- self-review
- discovery-ongoing
```
