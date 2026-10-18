# Scientific author self-review of Regularized Covariance Estimation by Banding

- Review: 20261018T231600Z-regularized-estimation-of-large-covariance-matrices-by-banding
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-18T23:15:00Z
- Finished UTC: 2026-10-18T23:16:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Regularized Covariance Estimation by Banding as a distinct DRAFT mathematical_method with related_match PrincipalComponentAnalysis and LinearRegression mappings. All three claims and locators across Bickel &amp; Levina (2008a, Ann. Statist. 36(1):199-227, arXiv:0803.1909v1) are supported with explicit index-ordering dependence, lack of finite-sample positive definiteness under hard banding, k &lt; n Cholesky regression constraint, long-range dependence boundary, and primary-source typographical limitations.

## Scope And Provenance

All fields of the exact maintained RegularizedCovarianceEstimationByBanding record and its primary evidence.

Selection: Exact maintained ID: AIMech:RegularizedCovarianceEstimationByBanding
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 003a4670e5ecb2ebff8f5e33c8954a3d8289f990.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:RegularizedCovarianceEstimationByBanding | data/curated/RegularizedCovarianceEstimationByBanding.yaml | maintained | Regularized Covariance Estimation by Banding |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:RegularizedCovarianceEstimationByBanding | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:RegularizedCovarianceEstimationByBanding | Validated 637 curated concept record(s). |
| aimech seed --check | passed | True | AIMech:RegularizedCovarianceEstimationByBanding | Checked 442 record(s); 0 drift. |
| aimech validate-history | passed | True | AIMech:RegularizedCovarianceEstimationByBanding | Validated 290 history file(s). |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:RegularizedCovarianceEstimationByBanding | Vendored record_review files match. |
| aimech check-source | passed | True | AIMech:RegularizedCovarianceEstimationByBanding | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:RegularizedCovarianceEstimationByBanding | Exited 0 without output. |
| Constructed Bickel &amp; Levina 2008a sample covariance banding, modified Cholesky k-predecessor inverse banding, Schur tapering positive definiteness, and random-split resampling bandwidth selection checks | passed | True | AIMech:RegularizedCovarianceEstimationByBanding | All Bickel &amp; Levina (2008a) boundary and mechanism assertions passed. |

## Scientific And Domain Assessments

### Distinctness of Regularized Covariance Estimation by Banding

identity: supported. Targets: AIMech:RegularizedCovarianceEstimationByBanding.

Distinct mathematical_method for sample covariance banding, Schur tapering, and modified Cholesky inverse banding.

Resolved as a distinct AIMech-native mathematical_method concept from Bickel and Levina (2008a, The Annals of Statistics 36(1):199-227; arXiv:0803.1909v1, DOI:10.1214/009053607000000758). Distinct from AIMech:MinimaxOptimalTaperingForHighDimensionalCovarianceMatrixEstimation (Cai, Zhang, &amp; Zhou 2010, The Annals of Statistics 38(4):2118-2144), which proves that Bickel and Levina's (2008a) rate O_P(((log p)/n)^{alpha/(2(alpha+1))}) over row-sum/entry-decay classes is sub-optimal because of the l1-to-l2 norm bound &#124;&#124;B_k(Sigma_hat) - B_k(Sigma)&#124;&#124;_2 &lt;= k &#124;&#124;B_k(Sigma_hat) - B_k(Sigma)&#124;&#124;_infty (Eq. A3) and introduces the two-parameter piecewise-linear trapezoid taper w_{ij} to establish the sharp minimax rate n^{-2 alpha /(2 alpha+1)} + (log p)/n via delta-net quadratic-form discretization and Assouad's lemma. Also distinct from AIMech:HighDimensionalCovarianceRegularizationByHardThresholding (Bickel &amp; Levina 2008b, The Annals of Statistics 36(6):2577-2604), which applies permutation-invariant entrywise hard thresholding T_s(M) = [m_{ij} 1(&#124;m_{ij}&#124; &gt;= s)] over weak l_q row-sparsity balls without requiring a natural index ordering, and from AIMech:SparsePermutationInvariantCovarianceEstimation (Rothman, Bickel, Levina, &amp; Zhu 2008), which minimizes an off-diagonal l1-penalized Gaussian log-likelihood.

### AIO mappings for AIMech:RegularizedCovarianceEstimationByBanding

grounding: supported. Targets: AIMech:RegularizedCovarianceEstimationByBanding.

related_match to AIO:PrincipalComponentAnalysis and AIO:LinearRegression is accurate.

Verified exact target existence in data/aio/ and documented why AIO:LassoRegression is rejected.

### Definition and scope

evidence: supported. Targets: AIMech:RegularizedCovarianceEstimationByBanding.

Definition accurately captures Theorems 1-5, Corollaries 1-2, and Section 5 resampling selection.

All equations and claims verified against arXiv:0803.1909v1 (pp. 199-227).

### Theorems 1-2 uniform operator-norm convergence for sample covariance banding and Schur-product tapering

evidence: supported. Targets: AIMech:RegularizedCovarianceEstimationByBanding.

Claim 1 (Theorems 1-2 uniform operator-norm convergence for sample covariance banding and Schur-product tapering) is verified.

Checked Eq. (A2) operator norm inequality, monotone banding bias decay, and Schur-product positive definiteness preservation when B_1(M) is indefinite.

### Theorem 3 and Corollary 2 modified Cholesky k-predecessor regression banding of the inverse covariance

evidence: supported. Targets: AIMech:RegularizedCovarianceEstimationByBanding.

Claim 2 (Theorem 3 and Corollary 2 modified Cholesky k-predecessor regression banding of the inverse covariance) is verified.

Checked k-banded positive-definite Sigma_tilde_{k,p}^{-1} construction in the p &gt; n regime and operator-norm accuracy.

### Theorems 4-5 spectral-measure/eigenspace consistency and Section 5 random-split resampling bandwidth selection

evidence: supported. Targets: AIMech:RegularizedCovarianceEstimationByBanding.

Claim 3 (Theorems 4-5 spectral-measure/eigenspace consistency and Section 5 random-split resampling bandwidth selection) is verified.

Checked exact recovery of oracle bandwidth k_hat = k_0 = 1 via random-split resampling on an MA(1) model.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:RegularizedCovarianceEstimationByBanding.

The full record is consistent; retain DRAFT.

Read every field of RegularizedCovarianceEstimationByBanding.yaml and verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261018T231500Z-regularized-estimation-of-large-covariance-matrices-by-banding.json | supports | No normalized identity match for Regularized Covariance Estimation by Banding across 442 pinned AIO records and 636 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected PrincipalComponentAnalysis and LinearRegression in the pinned AIO snapshot (2026-07-22). Provide accurate related_match context. |
| calculation | research/discovery/regularized-estimation-of-large-covariance-matrices-by-banding-boundaries.py | supports | Executed pure-Python verification in research/discovery/regularized-estimation-of-large-covariance-matrices-by-banding-boundaries.py (SHA-256 f48943debe4b3af9381a201f427ef3367d52b0d92926d4ab063f03b3674900d0): verified (1) in the p &gt; n regime (p=18, n=12) where the sample covariance S is singular, modified Cholesky k-predecessor regression banding (k=2 &lt; n) produces a strictly lower-triangular 2-banded factor A_tilde_2, positive residual variances D_tilde_2, and a symmetric positive-definite 2-banded precision estimator Sigma_tilde_{2,18}^{-1} = (I - A_tilde_2)^T D_tilde_2^{-1} (I - A_tilde_2) whose inverse Sigma_tilde_{2,18} is unbanded and distinct from B_2(S) (Section 2.2, Eqs. 2-4); (2) symmetric operator-norm inequality &#124;&#124;M&#124;&#124;_2 &lt;= &#124;&#124;M&#124;&#124;_{(1,1)} (Eq. A2), monotone banding bias decay, and operator/l1 norm reductions of B_2(S) and Sigma_tilde_{1,24} relative to unregularized S (Theorems 1 &amp; 3); (3) construction of a positive-definite 4x4 covariance matrix M whose 1-banded version B_1(M) is indefinite (min eigenvalue &lt; -0.2) whereas Schur-product tapering R_sigma(M) = M * R_sigma with triangular and exponential positive-definite tapers preserves strict positive definiteness (Section 3.3, Theorem 2); and (4) random-split resampling risk minimization (Section 5, Eqs. 24-25) recovering the exact oracle bandwidth k_hat = k_0 = 1 on an MA(1) process (Section 6.1, Example 1). |
| bl2008a-banding-pdf | https://export.arxiv.org/pdf/0803.1909.pdf; Pages 199-227 (PDF pp. 1-30), Sections 1-7 and Appendix (Theorems 1-5, Corollaries 1-2, Lemmas A.1-A.4, Equations 1-26 and A1-A32) | supports | All 30 pages of Bickel &amp; Levina (2008a, Ann. Statist. 36(1):199-227, arXiv:0803.1909v1) read and verified. |
| bl2008a-banding-abs | https://export.arxiv.org/abs/0803.1909; arXiv:0803.1909 abstract | supports | arXiv abstract and submission metadata read and verified. |
| bl2008a-banding-cr | https://api.crossref.org/works/10.1214/009053607000000758; DOI:10.1214/009053607000000758 Crossref metadata | supports | The Annals of Statistics 2008 Crossref metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Regularized Covariance Estimation by Banding record, yielding 637 native and 442 unchanged generated records.
- All 30 PDF pages of arXiv:0803.1909v1 were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261018T231600Z-regularized-estimation-of-large-covariance-matrices-by-banding
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Regularized Covariance Estimation by Banding
started_at: '2026-10-18T23:15:00Z'
finished_at: '2026-10-18T23:16:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from MinimaxOptimalTaperingForHighDimensionalCovarianceMatrixEstimation,
    HighDimensionalCovarianceRegularizationByHardThresholding, and SparsePermutationInvariantCovarianceEstimation,
    verified Theorems 1-5, Corollaries 1-2, Lemmas A.1-A.4, and Equations (1)-(26)
    and (A1)-(A32), and documented primary-source typographical notes in Bickel &
    Levina (2008a, arXiv:0803.1909v1). This is adversarial author self-review, not
    independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Regularized Covariance Estimation by Banding as a distinct DRAFT mathematical_method
  with related_match PrincipalComponentAnalysis and LinearRegression mappings. All
  three claims and locators across Bickel & Levina (2008a, Ann. Statist. 36(1):199-227,
  arXiv:0803.1909v1) are supported with explicit index-ordering dependence, lack of
  finite-sample positive definiteness under hard banding, k < n Cholesky regression
  constraint, long-range dependence boundary, and primary-source typographical limitations.
source:
  git_revision: 003a4670e5ecb2ebff8f5e33c8954a3d8289f990
  state: working_tree
  inputs:
  - path: data/aio/LinearRegression.yaml
    sha256: 9b6f1b2ea06d9a47e5f7cf94c66afeaa6d40c3e7d0fdb5037d2c25fabc6d8167
    role: context
  - path: data/aio/PrincipalComponentAnalysis.yaml
    sha256: 7b45b5c558b7e984abb44e1610fb8d829409ae391a151ed0dc0e5cd95023e8d4
    role: context
  - path: data/curated/HighDimensionalCovarianceRegularizationByHardThresholding.yaml
    sha256: 88744208883977cc24688f1be111758e3de60b77d3c994617e5bb1d2400857fd
    role: context
  - path: data/curated/MinimaxOptimalTaperingForHighDimensionalCovarianceMatrixEstimation.yaml
    sha256: d900858d9986a103b787df4717adab9baa4e874dfc114f3afacc969fd3960144
    role: context
  - path: data/curated/RegularizedCovarianceEstimationByBanding.yaml
    sha256: 7f8da1a283988b3eaf377198957c8f8492fa3fa15f9edc51c71a11acfa3b3b4e
    role: target
  - path: data/curated/SparsePermutationInvariantCovarianceEstimation.yaml
    sha256: 4f4677a1a45fc47752842dd18ea9e1994735ba3ef7869aecd1e5fd43293d7e05
    role: context
  - path: research/discovery/20261018T231500Z-regularized-estimation-of-large-covariance-matrices-by-banding.json
    sha256: 6d610f1b409dbcf477de1f593c5cc68c4d2ee4fdc651affb29a3637e5d8d0915
    role: context
  - path: research/discovery/regularized-estimation-of-large-covariance-matrices-by-banding-boundaries.py
    sha256: f48943debe4b3af9381a201f427ef3367d52b0d92926d4ab063f03b3674900d0
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
- target_id: AIMech:RegularizedCovarianceEstimationByBanding
  path: data/curated/RegularizedCovarianceEstimationByBanding.yaml
  label: Regularized Covariance Estimation by Banding
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RegularizedCovarianceEstimationByBanding.yaml
    role: maintained
scope:
  description: All fields of the exact maintained RegularizedCovarianceEstimationByBanding
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:RegularizedCovarianceEstimationByBanding'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:RegularizedCovarianceEstimationByBanding
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
  - AIMech:RegularizedCovarianceEstimationByBanding
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:RegularizedCovarianceEstimationByBanding
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 637 curated concept record(s).
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:RegularizedCovarianceEstimationByBanding
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 record(s); 0 drift.
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:RegularizedCovarianceEstimationByBanding
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 290 history file(s).
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:RegularizedCovarianceEstimationByBanding
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored record_review files match.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:RegularizedCovarianceEstimationByBanding
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:RegularizedCovarianceEstimationByBanding
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed Bickel & Levina 2008a sample covariance banding, modified Cholesky
    k-predecessor inverse banding, Schur tapering positive definiteness, and random-split
    resampling bandwidth selection checks
  command: python3 research/discovery/regularized-estimation-of-large-covariance-matrices-by-banding-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:RegularizedCovarianceEstimationByBanding
  exit_code: 0
  expected_exit_code: 0
  summary: All Bickel & Levina (2008a) boundary and mechanism assertions passed.
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261018T231500Z-regularized-estimation-of-large-covariance-matrices-by-banding.json
  accessed_at: '2026-10-18T23:15:00Z'
  support: supports
  summary: No normalized identity match for Regularized Covariance Estimation by Banding
    across 442 pinned AIO records and 636 maintained IDs, names, aliases and scoped
    synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-18T23:15:00Z'
  support: supports
  summary: Inspected PrincipalComponentAnalysis and LinearRegression in the pinned
    AIO snapshot (2026-07-22). Provide accurate related_match context.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/regularized-estimation-of-large-covariance-matrices-by-banding-boundaries.py
  accessed_at: '2026-10-18T23:15:00Z'
  snapshot_sha256: f48943debe4b3af9381a201f427ef3367d52b0d92926d4ab063f03b3674900d0
  support: supports
  summary: 'Executed pure-Python verification in research/discovery/regularized-estimation-of-large-covariance-matrices-by-banding-boundaries.py
    (SHA-256 f48943debe4b3af9381a201f427ef3367d52b0d92926d4ab063f03b3674900d0): verified
    (1) in the p > n regime (p=18, n=12) where the sample covariance S is singular,
    modified Cholesky k-predecessor regression banding (k=2 < n) produces a strictly
    lower-triangular 2-banded factor A_tilde_2, positive residual variances D_tilde_2,
    and a symmetric positive-definite 2-banded precision estimator Sigma_tilde_{2,18}^{-1}
    = (I - A_tilde_2)^T D_tilde_2^{-1} (I - A_tilde_2) whose inverse Sigma_tilde_{2,18}
    is unbanded and distinct from B_2(S) (Section 2.2, Eqs. 2-4); (2) symmetric operator-norm
    inequality ||M||_2 <= ||M||_{(1,1)} (Eq. A2), monotone banding bias decay, and
    operator/l1 norm reductions of B_2(S) and Sigma_tilde_{1,24} relative to unregularized
    S (Theorems 1 & 3); (3) construction of a positive-definite 4x4 covariance matrix
    M whose 1-banded version B_1(M) is indefinite (min eigenvalue < -0.2) whereas
    Schur-product tapering R_sigma(M) = M * R_sigma with triangular and exponential
    positive-definite tapers preserves strict positive definiteness (Section 3.3,
    Theorem 2); and (4) random-split resampling risk minimization (Section 5, Eqs.
    24-25) recovering the exact oracle bandwidth k_hat = k_0 = 1 on an MA(1) process
    (Section 6.1, Example 1).'
- evidence_id: bl2008a-banding-pdf
  kind: primary_source
  reference: https://export.arxiv.org/pdf/0803.1909.pdf
  locator: Pages 199-227 (PDF pp. 1-30), Sections 1-7 and Appendix (Theorems 1-5,
    Corollaries 1-2, Lemmas A.1-A.4, Equations 1-26 and A1-A32)
  accessed_at: '2026-10-18T16:36:47Z'
  snapshot_sha256: 2ca5cccd7bbd0845e95ce36c89cb3e9746b32a7335fc06935fd417ecbcb5aba3
  support: supports
  summary: All 30 pages of Bickel & Levina (2008a, Ann. Statist. 36(1):199-227, arXiv:0803.1909v1)
    read and verified.
- evidence_id: bl2008a-banding-abs
  kind: primary_source
  reference: https://export.arxiv.org/abs/0803.1909
  locator: arXiv:0803.1909 abstract
  accessed_at: '2026-10-18T16:36:46Z'
  snapshot_sha256: bd09cffdd7a97113786cdb1f083d9fdb43515981b978ccfe7df1786feebf9d3e
  support: supports
  summary: arXiv abstract and submission metadata read and verified.
- evidence_id: bl2008a-banding-cr
  kind: primary_source
  reference: https://api.crossref.org/works/10.1214/009053607000000758
  locator: DOI:10.1214/009053607000000758 Crossref metadata
  accessed_at: '2026-10-18T16:34:00Z'
  snapshot_sha256: 6dfcedbb21fb25632d304f11a39a5fc222f9e3a7dd7080e82711804635dda3d5
  support: supports
  summary: The Annals of Statistics 2008 Crossref metadata read and verified.
assessments:
- assessment_id: identity-boundary
  area: identity
  topic: Distinctness of Regularized Covariance Estimation by Banding
  outcome: supported
  target_ids:
  - AIMech:RegularizedCovarianceEstimationByBanding
  evidence_ids:
  - identity
  - bl2008a-banding-pdf
  - bl2008a-banding-abs
  - bl2008a-banding-cr
  summary: Distinct mathematical_method for sample covariance banding, Schur tapering,
    and modified Cholesky inverse banding.
  details: Resolved as a distinct AIMech-native mathematical_method concept from Bickel
    and Levina (2008a, The Annals of Statistics 36(1):199-227; arXiv:0803.1909v1,
    DOI:10.1214/009053607000000758). Distinct from AIMech:MinimaxOptimalTaperingForHighDimensionalCovarianceMatrixEstimation
    (Cai, Zhang, & Zhou 2010, The Annals of Statistics 38(4):2118-2144), which proves
    that Bickel and Levina's (2008a) rate O_P(((log p)/n)^{alpha/(2(alpha+1))}) over
    row-sum/entry-decay classes is sub-optimal because of the l1-to-l2 norm bound
    ||B_k(Sigma_hat) - B_k(Sigma)||_2 <= k ||B_k(Sigma_hat) - B_k(Sigma)||_infty (Eq.
    A3) and introduces the two-parameter piecewise-linear trapezoid taper w_{ij} to
    establish the sharp minimax rate n^{-2 alpha /(2 alpha+1)} + (log p)/n via delta-net
    quadratic-form discretization and Assouad's lemma. Also distinct from AIMech:HighDimensionalCovarianceRegularizationByHardThresholding
    (Bickel & Levina 2008b, The Annals of Statistics 36(6):2577-2604), which applies
    permutation-invariant entrywise hard thresholding T_s(M) = [m_{ij} 1(|m_{ij}|
    >= s)] over weak l_q row-sparsity balls without requiring a natural index ordering,
    and from AIMech:SparsePermutationInvariantCovarianceEstimation (Rothman, Bickel,
    Levina, & Zhu 2008), which minimizes an off-diagonal l1-penalized Gaussian log-likelihood.
- assessment_id: aio-mappings
  area: grounding
  topic: AIO mappings for AIMech:RegularizedCovarianceEstimationByBanding
  outcome: supported
  target_ids:
  - AIMech:RegularizedCovarianceEstimationByBanding
  evidence_ids:
  - mapping
  - bl2008a-banding-pdf
  summary: related_match to AIO:PrincipalComponentAnalysis and AIO:LinearRegression
    is accurate.
  details: Verified exact target existence in data/aio/ and documented why AIO:LassoRegression
    is rejected.
- assessment_id: definition
  area: evidence
  topic: Definition and scope
  outcome: supported
  target_ids:
  - AIMech:RegularizedCovarianceEstimationByBanding
  evidence_ids:
  - bl2008a-banding-pdf
  - bl2008a-banding-abs
  - bl2008a-banding-cr
  summary: Definition accurately captures Theorems 1-5, Corollaries 1-2, and Section
    5 resampling selection.
  details: All equations and claims verified against arXiv:0803.1909v1 (pp. 199-227).
- assessment_id: claim-1-banding-and-schur-tapering-rates
  area: evidence
  topic: Theorems 1-2 uniform operator-norm convergence for sample covariance banding
    and Schur-product tapering
  outcome: supported
  target_ids:
  - AIMech:RegularizedCovarianceEstimationByBanding
  evidence_ids:
  - bl2008a-banding-pdf
  - calculation
  summary: Claim 1 (Theorems 1-2 uniform operator-norm convergence for sample covariance
    banding and Schur-product tapering) is verified.
  details: Checked Eq. (A2) operator norm inequality, monotone banding bias decay,
    and Schur-product positive definiteness preservation when B_1(M) is indefinite.
- assessment_id: claim-2-cholesky-inverse-banding
  area: evidence
  topic: Theorem 3 and Corollary 2 modified Cholesky k-predecessor regression banding
    of the inverse covariance
  outcome: supported
  target_ids:
  - AIMech:RegularizedCovarianceEstimationByBanding
  evidence_ids:
  - bl2008a-banding-pdf
  - calculation
  summary: Claim 2 (Theorem 3 and Corollary 2 modified Cholesky k-predecessor regression
    banding of the inverse covariance) is verified.
  details: Checked k-banded positive-definite Sigma_tilde_{k,p}^{-1} construction
    in the p > n regime and operator-norm accuracy.
- assessment_id: claim-3-eigenstructure-and-resampling-tuning
  area: evidence
  topic: Theorems 4-5 spectral-measure/eigenspace consistency and Section 5 random-split
    resampling bandwidth selection
  outcome: supported
  target_ids:
  - AIMech:RegularizedCovarianceEstimationByBanding
  evidence_ids:
  - bl2008a-banding-pdf
  - calculation
  summary: Claim 3 (Theorems 4-5 spectral-measure/eigenspace consistency and Section
    5 random-split resampling bandwidth selection) is verified.
  details: Checked exact recovery of oracle bandwidth k_hat = k_0 = 1 via random-split
    resampling on an MA(1) model.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:RegularizedCovarianceEstimationByBanding
  evidence_ids:
  - identity
  - mapping
  - bl2008a-banding-pdf
  - bl2008a-banding-abs
  - bl2008a-banding-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Read every field of RegularizedCovarianceEstimationByBanding.yaml and verified
    all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Regularized Covariance Estimation by Banding record, yielding 637
  native and 442 unchanged generated records.
- All 30 PDF pages of arXiv:0803.1909v1 were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- covariance-estimation
- banding
- cholesky-decomposition
- self-review
- discovery-ongoing
```
