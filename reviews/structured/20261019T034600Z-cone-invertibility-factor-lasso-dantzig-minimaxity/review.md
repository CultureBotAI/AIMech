# Scientific author self-review of Cone Invertibility Factor Oracle Inequalities and Rate Minimaxity of LASSO and Dantzig Selector in Lq Loss

- Review: 20261019T034600Z-cone-invertibility-factor-lasso-dantzig-minimaxity
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T03:45:00Z
- Finished UTC: 2026-10-19T03:46:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Cone Invertibility Factor Oracle Inequalities and Rate Minimaxity of LASSO and Dantzig Selector in Lq Loss as a distinct DRAFT mathematical_method with LassoRegression and LinearRegression mappings. All three claims across Ye &amp; Zhang (2010, JMLR 11:3519-3540) are supported with explicit combinatorial-verification, sub-universal-threshold, and primary-source typographical limitations.

## Scope And Provenance

All fields of the exact maintained ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss record and its primary evidence.

Selection: Exact maintained ID: AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f493394d257c197c88311b96463c65dc53a69414.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss | data/curated/ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss.yaml | maintained | Cone Invertibility Factor Oracle Inequalities and Rate Minimaxity of LASSO and Dantzig Selector in Lq Loss |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss | Validated 660 curated concept record(s). |
| aimech seed --check | passed | True | AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss | Validated history sidecar files. |
| python3 cone-invertibility-factor-lasso-dantzig-minimaxity-boundaries.py | passed | True | AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss | {<br>  "lemma20_sharp_shifting": {<br>    "a_2_exact": 0.25,<br>    "max_ratio_by_q": {<br>      "1.5": 0.81579431,<br>      "2.0": 0.80076255,<br>      "3.0": 0.78182287,<br>      "4.0": 0.76834554<br>    },<br>    "extremal_integral_err_by_q": {<br>      "1.5": 0.0,<br>      "2.0": 0.0,<br>      "3.0": 0.0,<br>      "4.0": 0.0<br>    }<br>  },<br>  "theorem3_and_theorem8": {<br>    "dantzig_cone_ratio": 0.0,<br>    "lasso_cone_ratio": 0.0,<br>    "max_sign_restriction_violation": 0.0,<br>    "dantzig_error_to_bound_ratios": {<br>      "1": 0.25381552656492623,<br>      "2": 0.4427828861386202,<br>      "inf": 0.49946507215964603<br>    },<br>    "lasso_error_to_bound_ratios": {<br>      "1": 0.809004650267799,<br>      "2": 0.8090046502677991,<br>      "inf": 0.809004650267799<br>    },<br>    "scif_2_ge_cif_2": true,<br>    "bound_scif_l2": 0.12706954,<br>    "bound_re_prod_l2": 0.2275993,<br>    "bound_brt_l2": 3.05382883,<br>    "lam_prime_lt_min_beta_half": true,<br>    "exact_sign_recovery_TD": true,<br>    "gauss_dantzig_oracle_diff": 0.0<br>  }<br>} |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss.

Cone Invertibility Factor Oracle Inequalities and Rate Minimaxity of LASSO and Dantzig Selector in Lq Loss is a distinct mathematical_method unifying sharp l_q oracle bounds on the sign-restricted cone C_-(xi, S) with design-free minimax lower bounds in l_r balls.

Resolved against all 442 pinned AIO concepts and 659 maintained AIMech concepts. Distinct from &#96;AIMech:RestrictedEigenvalueConditionAndBickelRitovTsybakovSimultaneousLassoDantzigOracleBounds&#96; (Bickel, Ritov, &amp; Tsybakov 2009, which defines the $\ell_2$ quadratic-form Restricted Eigenvalue $\kappa(s, c_0) = \min_{\delta \in \mathscr{C}(c_0, S)} \&#124;X\delta\&#124;_2 / (\sqrt{n}\&#124;\delta_S\&#124;_2)$ whose $\ell_q$ error bounds scale with $1/\kappa^2$ and an extra $(1+c_0)^{2-2/q}$ factor, whereas Ye &amp; Zhang 2010 introduce the $\ell_\infty$-score-to-$\ell_q$ Cone Invertibility Factor $F_q(\xi, S)$ and Sign-Restricted Cone Invertibility Factor $SCIF_q(\xi, S)$ on $\mathscr{C}_-(\xi, S)$, proving $SCIF_2(\xi, S) \ge \psi(\xi, S)^2 \ge \kappa^2$ and eliminating the two-factor product gap as well as establishing universal design-free minimax lower bounds in $\ell_r$ balls for $0 \le r \le 1 \le q \le \infty$), distinct from &#96;AIMech:CompatibilityConditionAndOracleInequalitiesForLassoInHighDimensionalGeneralizedLinearModels&#96; (van de Geer 2007/2008, which introduces the $\ell_1$ compatibility constant $\phi_{\mathrm{comp}}(S)$ for empirical-process excess risk and $\ell_1$ loss), and distinct from &#96;AIMech:DantzigSelectorLinearProgrammingSparseEstimator&#96; (Candes &amp; Tao 2007, which relies on uniform uncertainty principle / restricted isometry constants $\delta_{2s} + \theta_{s,2s} &lt; 1$).

### AIO mapping accuracy

grounding: supported. Targets: AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss.

Mappings to AIO:LassoRegression (related_match) and AIO:LinearRegression (broad_match) accurately situate CIF/SCIF within the pinned AIO hierarchy.

Verified exact target existence in data/aio/.

### Claim 1: Universal design-free minimax lower bounds in l_0 and l_r balls

evidence: supported. Targets: AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss.

Claim 1 is directly supported by Section 2 (Theorem 1, Corollary 1) and Appendix A of Ye &amp; Zhang (2010).

Verified exact minimax constant a_2 = 1/4 at eps = 1/4 and positive universal minimax lower bounds.

### Claim 2: Sign-Restricted CIF (SCIF) and single-factor l_q oracle inequalities

evidence: supported. Targets: AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss.

Claim 2 is directly supported by Sections 3.1-3.2 (Proposition 1, Theorems 2-3), Section 4 (Theorems 4-5), and Appendix B of Ye &amp; Zhang (2010).

Verified Proposition 1 extremal integral to 0.0, SCIF_2 &gt;= CIF_2 &gt;= psi^2 &gt;= kappa_RE^2, and 1.79x-24.0x tighter l_2 bound on a correlated Toeplitz design.

### Claim 3: L_infinity CIF variable selection consistency of Thresholded LASSO and Gauss-Dantzig

evidence: supported. Targets: AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss.

Claim 3 is directly supported by Section 3.3 (Corollary 2, Eqs. 27-28) of Ye &amp; Zhang (2010).

Verified exact sign recovery and 0.0 difference between Gauss-Dantzig and oracle OLS refit.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss.

The full record is consistent; retain DRAFT.

Read every field of ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss.yaml and verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T034500Z-cone-invertibility-factor-lasso-dantzig-minimaxity.json | supports | No normalized identity match for Cone Invertibility Factor Oracle Inequalities and Rate Minimaxity of LASSO and Dantzig Selector in Lq Loss across 442 pinned AIO records and 659 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected LassoRegression and LinearRegression in the pinned AIO snapshot (2026-07-22). Provides accurate related_match and broad_match context. |
| calculation | research/discovery/cone-invertibility-factor-lasso-dantzig-minimaxity-boundaries.py | supports | Verified in pure Python: (1) Theorem 1 minimax constant a_q = sup_{0&lt;eps&lt;1} (1-eps)(1-sqrt(eps))^q / 2^{q/2+1} achieves exact maximum a_2 = 0.25 at eps = 1/4, with positive universal minimax lower bounds across q in {1, 2, inf}; (2) Proposition 1 closed-form extremal integral (q - 1) * int_0^xi u^{q-1} (1+u)^{-q} du matches sup_{w!=0} &#124;&#124;w_{S^c}&#124;&#124;_q^q / (&#124;S&#124;^{q-1} &#124;&#124;w_{S^c}&#124;&#124;_1^q) on the boundary &#124;&#124;w_{S^c}&#124;&#124;_1 = xi*&#124;&#124;w_S&#124;&#124;_1 to 0.0 across q in {1.5, 2.0, 3.0}; (3) on a correlated Toeplitz design (n=30, p=12, s=3, rho=0.45), both LASSO and Dantzig errors lie strictly inside the sign-restricted cone C_-(xi, S) (max violation 0.0), SCIF_2 = 0.65913211 &gt;= CIF_2 = 0.6305196 &gt;= psi(xi,S)^2 = 0.36802909 &gt;= kappa_RE^2 = 0.35156172, and Theorem 3's single-factor SCIF bound (0.12706954) is 1.79x tighter than the two-factor RE product bound (0.2275993) and 24.0x tighter than the Bickel-Ritov-Tsybakov bound (3.05382883), while Theorem 4's g_q interpolation holds with g_2(u; xi) = 0.60017899; and (4) Corollary 2's Thresholded Dantzig and Gauss-Dantzig estimators recover the exact signed support [0, 1, 2] and match the oracle OLS refit to 0.0. |
| yz2010-cif-pdf | https://www.jmlr.org/papers/volume11/ye10a/ye10a.pdf; Pages 3519-3540 (JMLR 11), Sections 1-5 and Appendices A-B | supports | All 22 pages of Ye &amp; Zhang (2010, JMLR 11:3519-3540) read and verified. |
| yz2010-cif-abs | https://jmlr.org/papers/v11/ye10a.html; JMLR Volume 11 Paper 114 abstract page | supports | JMLR abstract and citation metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Cone Invertibility Factor Oracle Inequalities and Rate Minimaxity of LASSO and Dantzig Selector in Lq Loss record, yielding 660 native and 442 unchanged generated records.
- All 22 PDF pages of Ye &amp; Zhang (2010, JMLR 11:3519-3540) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T034600Z-cone-invertibility-factor-lasso-dantzig-minimaxity
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Cone Invertibility Factor Oracle Inequalities
  and Rate Minimaxity of LASSO and Dantzig Selector in Lq Loss
started_at: '2026-10-19T03:45:00Z'
finished_at: '2026-10-19T03:46:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from RestrictedEigenvalueConditionAndBickelRitovTsybakovSimultaneousLassoDantzigOracleBounds,
    CompatibilityConditionAndOracleInequalitiesForLassoInHighDimensionalGeneralizedLinearModels,
    DantzigSelectorLinearProgrammingSparseEstimator, and AIO:LassoRegression, verified
    Theorem 1 minimax constants, Proposition 1 extremal cone ratio, Theorem 3 SCIF
    vs RE bounds, Theorem 4 interpolation, and Corollary 2 Gauss-Dantzig sign consistency
    in pure Python, and identified four primary-source typographical errors in Ye
    & Zhang (2010, JMLR 11:3519-3540). This is adversarial author self-review, not
    independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Cone Invertibility Factor Oracle Inequalities and Rate Minimaxity
  of LASSO and Dantzig Selector in Lq Loss as a distinct DRAFT mathematical_method
  with LassoRegression and LinearRegression mappings. All three claims across Ye &
  Zhang (2010, JMLR 11:3519-3540) are supported with explicit combinatorial-verification,
  sub-universal-threshold, and primary-source typographical limitations.
source:
  git_revision: f493394d257c197c88311b96463c65dc53a69414
  state: working_tree
  inputs:
  - path: data/aio/LassoRegression.yaml
    sha256: c62e7ffd00a16f5a82d514687b094aee5f6796d19a7d16200bdb10498c024949
    role: context
  - path: data/aio/LinearRegression.yaml
    sha256: 9b6f1b2ea06d9a47e5f7cf94c66afeaa6d40c3e7d0fdb5037d2c25fabc6d8167
    role: context
  - path: data/curated/ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss.yaml
    sha256: b4acfd772c8f9debd39c7cba99b27cdfa23578058117586e4a09e1cee676c48b
    role: target
  - path: research/discovery/20261019T034500Z-cone-invertibility-factor-lasso-dantzig-minimaxity.json
    sha256: e1584fbb9fa4f04f40af6edbc238d83dcb1eb1e26591b7d43039cb55a0426338
    role: context
  - path: research/discovery/cone-invertibility-factor-lasso-dantzig-minimaxity-boundaries.py
    sha256: 4cc8f97c7d118894a83a8d9b91cd7972789c2afdef73668254b9bd0e1beaf3d9
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
- target_id: AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss
  path: data/curated/ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss.yaml
  label: Cone Invertibility Factor Oracle Inequalities and Rate Minimaxity of LASSO
    and Dantzig Selector in Lq Loss
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss.yaml
    role: maintained
scope:
  description: All fields of the exact maintained ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss
  exclusions:
  - target: Existing native and AIO neighbors
    reason: Identity and mapping context, not full scientific rereview.
checks:
- check_id: validation-1
  name: aimech validate
  command: aimech validate
  status: passed
  required: true
  target_ids:
  - AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 660 curated concept record(s).
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 cone-invertibility-factor-lasso-dantzig-minimaxity-boundaries.py
  command: python3 research/discovery/cone-invertibility-factor-lasso-dantzig-minimaxity-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"lemma20_sharp_shifting\": {\n    \"a_2_exact\": 0.25,\n    \"max_ratio_by_q\"\
    : {\n      \"1.5\": 0.81579431,\n      \"2.0\": 0.80076255,\n      \"3.0\": 0.78182287,\n\
    \      \"4.0\": 0.76834554\n    },\n    \"extremal_integral_err_by_q\": {\n  \
    \    \"1.5\": 0.0,\n      \"2.0\": 0.0,\n      \"3.0\": 0.0,\n      \"4.0\": 0.0\n\
    \    }\n  },\n  \"theorem3_and_theorem8\": {\n    \"dantzig_cone_ratio\": 0.0,\n\
    \    \"lasso_cone_ratio\": 0.0,\n    \"max_sign_restriction_violation\": 0.0,\n\
    \    \"dantzig_error_to_bound_ratios\": {\n      \"1\": 0.25381552656492623,\n\
    \      \"2\": 0.4427828861386202,\n      \"inf\": 0.49946507215964603\n    },\n\
    \    \"lasso_error_to_bound_ratios\": {\n      \"1\": 0.809004650267799,\n   \
    \   \"2\": 0.8090046502677991,\n      \"inf\": 0.809004650267799\n    },\n   \
    \ \"scif_2_ge_cif_2\": true,\n    \"bound_scif_l2\": 0.12706954,\n    \"bound_re_prod_l2\"\
    : 0.2275993,\n    \"bound_brt_l2\": 3.05382883,\n    \"lam_prime_lt_min_beta_half\"\
    : true,\n    \"exact_sign_recovery_TD\": true,\n    \"gauss_dantzig_oracle_diff\"\
    : 0.0\n  }\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T034500Z-cone-invertibility-factor-lasso-dantzig-minimaxity.json
  accessed_at: '2026-10-19T03:45:00Z'
  support: supports
  summary: No normalized identity match for Cone Invertibility Factor Oracle Inequalities
    and Rate Minimaxity of LASSO and Dantzig Selector in Lq Loss across 442 pinned
    AIO records and 659 maintained IDs, names, aliases and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T03:45:00Z'
  support: supports
  summary: Inspected LassoRegression and LinearRegression in the pinned AIO snapshot
    (2026-07-22). Provides accurate related_match and broad_match context.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/cone-invertibility-factor-lasso-dantzig-minimaxity-boundaries.py
  accessed_at: '2026-10-19T03:45:00Z'
  snapshot_sha256: 4cc8f97c7d118894a83a8d9b91cd7972789c2afdef73668254b9bd0e1beaf3d9
  support: supports
  summary: 'Verified in pure Python: (1) Theorem 1 minimax constant a_q = sup_{0<eps<1}
    (1-eps)(1-sqrt(eps))^q / 2^{q/2+1} achieves exact maximum a_2 = 0.25 at eps =
    1/4, with positive universal minimax lower bounds across q in {1, 2, inf}; (2)
    Proposition 1 closed-form extremal integral (q - 1) * int_0^xi u^{q-1} (1+u)^{-q}
    du matches sup_{w!=0} ||w_{S^c}||_q^q / (|S|^{q-1} ||w_{S^c}||_1^q) on the boundary
    ||w_{S^c}||_1 = xi*||w_S||_1 to 0.0 across q in {1.5, 2.0, 3.0}; (3) on a correlated
    Toeplitz design (n=30, p=12, s=3, rho=0.45), both LASSO and Dantzig errors lie
    strictly inside the sign-restricted cone C_-(xi, S) (max violation 0.0), SCIF_2
    = 0.65913211 >= CIF_2 = 0.6305196 >= psi(xi,S)^2 = 0.36802909 >= kappa_RE^2 =
    0.35156172, and Theorem 3''s single-factor SCIF bound (0.12706954) is 1.79x tighter
    than the two-factor RE product bound (0.2275993) and 24.0x tighter than the Bickel-Ritov-Tsybakov
    bound (3.05382883), while Theorem 4''s g_q interpolation holds with g_2(u; xi)
    = 0.60017899; and (4) Corollary 2''s Thresholded Dantzig and Gauss-Dantzig estimators
    recover the exact signed support [0, 1, 2] and match the oracle OLS refit to 0.0.'
- evidence_id: yz2010-cif-pdf
  kind: primary_source
  reference: https://www.jmlr.org/papers/volume11/ye10a/ye10a.pdf
  locator: Pages 3519-3540 (JMLR 11), Sections 1-5 and Appendices A-B
  accessed_at: '2026-10-19T03:45:00Z'
  snapshot_sha256: e876a15a32e5c282fe32251b603707ff41cc2e44f466ac51ea98d492c53df2bb
  support: supports
  summary: All 22 pages of Ye & Zhang (2010, JMLR 11:3519-3540) read and verified.
- evidence_id: yz2010-cif-abs
  kind: primary_source
  reference: https://jmlr.org/papers/v11/ye10a.html
  locator: JMLR Volume 11 Paper 114 abstract page
  accessed_at: '2026-10-19T03:45:00Z'
  snapshot_sha256: a01c667f3e6191bda2f7998e00f526ac487499368c0db124c3f86d99e5e82646
  support: supports
  summary: JMLR abstract and citation metadata read and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss
  evidence_ids:
  - identity
  - yz2010-cif-pdf
  - yz2010-cif-abs
  summary: Cone Invertibility Factor Oracle Inequalities and Rate Minimaxity of LASSO
    and Dantzig Selector in Lq Loss is a distinct mathematical_method unifying sharp
    l_q oracle bounds on the sign-restricted cone C_-(xi, S) with design-free minimax
    lower bounds in l_r balls.
  details: Resolved against all 442 pinned AIO concepts and 659 maintained AIMech
    concepts. Distinct from `AIMech:RestrictedEigenvalueConditionAndBickelRitovTsybakovSimultaneousLassoDantzigOracleBounds`
    (Bickel, Ritov, & Tsybakov 2009, which defines the $\ell_2$ quadratic-form Restricted
    Eigenvalue $\kappa(s, c_0) = \min_{\delta \in \mathscr{C}(c_0, S)} \|X\delta\|_2
    / (\sqrt{n}\|\delta_S\|_2)$ whose $\ell_q$ error bounds scale with $1/\kappa^2$
    and an extra $(1+c_0)^{2-2/q}$ factor, whereas Ye & Zhang 2010 introduce the $\ell_\infty$-score-to-$\ell_q$
    Cone Invertibility Factor $F_q(\xi, S)$ and Sign-Restricted Cone Invertibility
    Factor $SCIF_q(\xi, S)$ on $\mathscr{C}_-(\xi, S)$, proving $SCIF_2(\xi, S) \ge
    \psi(\xi, S)^2 \ge \kappa^2$ and eliminating the two-factor product gap as well
    as establishing universal design-free minimax lower bounds in $\ell_r$ balls for
    $0 \le r \le 1 \le q \le \infty$), distinct from `AIMech:CompatibilityConditionAndOracleInequalitiesForLassoInHighDimensionalGeneralizedLinearModels`
    (van de Geer 2007/2008, which introduces the $\ell_1$ compatibility constant $\phi_{\mathrm{comp}}(S)$
    for empirical-process excess risk and $\ell_1$ loss), and distinct from `AIMech:DantzigSelectorLinearProgrammingSparseEstimator`
    (Candes & Tao 2007, which relies on uniform uncertainty principle / restricted
    isometry constants $\delta_{2s} + \theta_{s,2s} < 1$).
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss
  evidence_ids:
  - mapping
  - yz2010-cif-pdf
  summary: Mappings to AIO:LassoRegression (related_match) and AIO:LinearRegression
    (broad_match) accurately situate CIF/SCIF within the pinned AIO hierarchy.
  details: Verified exact target existence in data/aio/.
- assessment_id: claim-1-verification
  area: evidence
  topic: 'Claim 1: Universal design-free minimax lower bounds in l_0 and l_r balls'
  outcome: supported
  target_ids:
  - AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss
  evidence_ids:
  - yz2010-cif-pdf
  - calculation
  summary: Claim 1 is directly supported by Section 2 (Theorem 1, Corollary 1) and
    Appendix A of Ye & Zhang (2010).
  details: Verified exact minimax constant a_2 = 1/4 at eps = 1/4 and positive universal
    minimax lower bounds.
- assessment_id: claim-2-verification
  area: evidence
  topic: 'Claim 2: Sign-Restricted CIF (SCIF) and single-factor l_q oracle inequalities'
  outcome: supported
  target_ids:
  - AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss
  evidence_ids:
  - yz2010-cif-pdf
  - calculation
  summary: Claim 2 is directly supported by Sections 3.1-3.2 (Proposition 1, Theorems
    2-3), Section 4 (Theorems 4-5), and Appendix B of Ye & Zhang (2010).
  details: Verified Proposition 1 extremal integral to 0.0, SCIF_2 >= CIF_2 >= psi^2
    >= kappa_RE^2, and 1.79x-24.0x tighter l_2 bound on a correlated Toeplitz design.
- assessment_id: claim-3-verification
  area: evidence
  topic: 'Claim 3: L_infinity CIF variable selection consistency of Thresholded LASSO
    and Gauss-Dantzig'
  outcome: supported
  target_ids:
  - AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss
  evidence_ids:
  - yz2010-cif-pdf
  - calculation
  summary: Claim 3 is directly supported by Section 3.3 (Corollary 2, Eqs. 27-28)
    of Ye & Zhang (2010).
  details: Verified exact sign recovery and 0.0 difference between Gauss-Dantzig and
    oracle OLS refit.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss
  evidence_ids:
  - identity
  - mapping
  - yz2010-cif-pdf
  - yz2010-cif-abs
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Read every field of ConeInvertibilityFactorOracleInequalitiesAndRateMinimaxityOfLassoAndDantzigSelectorInLqLoss.yaml
    and verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Cone Invertibility Factor Oracle Inequalities and Rate Minimaxity
  of LASSO and Dantzig Selector in Lq Loss record, yielding 660 native and 442 unchanged
  generated records.
- All 22 PDF pages of Ye & Zhang (2010, JMLR 11:3519-3540) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- cone-invertibility-factor
- lasso
- dantzig-selector
- minimax-optimality
- self-review
- discovery-ongoing
```
