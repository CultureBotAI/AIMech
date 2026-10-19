# Scientific author self-review of Baik-Silverstein Eigenvalue Separation for High-Dimensional Spiked Population Covariance Matrices

- Review: 20261019T003300Z-baik-silverstein-spiked-eigenvalue-separation
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T00:32:00Z
- Finished UTC: 2026-10-19T00:33:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Baik-Silverstein Eigenvalue Separation for High-Dimensional Spiked Population Covariance Matrices as a distinct DRAFT mathematical_method with related_match PrincipalComponentAnalysis and broad_match LinearDimensionalityReduction mappings. Both claims and all locators across Baik &amp; Silverstein (2006, J. Multivariate Anal. 97(6):1382-1408, arXiv:math/0408165v1) are supported with explicit fourth-moment and c &gt; 1 small-spike absorption limitations and primary-source typographical notes.

## Scope And Provenance

All fields of the exact maintained BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation record and its primary evidence.

Selection: Exact maintained ID: AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 58903c47eb74e45b732b3a595398846d29505472.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation | data/curated/BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation.yaml | maintained | Baik-Silverstein Eigenvalue Separation for High-Dimensional Spiked Population Covariance Matrices |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation | Validated 644 curated concept record(s). |
| aimech seed --check | passed | True | AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation | Checked 442 record(s); 0 drift. |
| aimech validate-history | passed | True | AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation | Validated 297 history file(s). |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation | Vendored record_review files match. |
| aimech check-source | passed | True | AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation | Exited 0 without output. |
| Constructed Baik &amp; Silverstein 2006 Silverstein-Choi companion inverse Stieltjes transform and Theorems 1.1-1.2 checks | passed | True | AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation | Baik &amp; Silverstein (2006) spiked covariance eigenvalue separation verified: c=0.5 (s_1=4.154~4.200, s_2=2.693~2.914, s_{p-1}=0.1107~0.0858, s_p=0.0369~0.0365); c=2.0 (s_1=7.166~7.071, s_2=5.123~5.828, s_n=0.2193~0.1716). |

## Scientific And Domain Assessments

### Distinctness of Baik-Silverstein Eigenvalue Separation for High-Dimensional Spiked Population Covariance Matrices

identity: supported. Targets: AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation.

Distinct mathematical_method for high-dimensional non-Gaussian spiked sample covariance eigenvalue separation.

Resolved as a distinct AIMech-native mathematical_method concept from Baik &amp; Silverstein (2006, Journal of Multivariate Analysis 97(6):1382-1408; arXiv:math/0408165v1, DOI:10.1016/j.jmva.2005.08.003). Distinct from AIMech:MarcenkoPasturConvexOptimizationSpectrumEstimation (El Karoui 2008, Ann. Statist. 36(6):2757-2790), which estimates the global limiting spectral distribution H via convex optimization of the unperturbed Silverstein-Choi equation without isolating finite-rank outlier spikes, from AIMech:SparsePrincipalComponentsAnalysisViaCoordinateVarianceSelectionAndThresholding (Johnstone &amp; Lu 2009, JASA 104(486):682-693), which proves l2 eigenvector consistency of coordinate-variance selection and wavelet thresholding under sparsity, and from AIMech:DiagonalThresholdingAndSemidefiniteRelaxationSupportRecoveryForSparsePCA (Amini &amp; Wainwright 2009, Ann. Statist. 37(5B):2877-2921), which analyzes signed support recovery via diagonal thresholding and semidefinite relaxation.

### AIO mappings for AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation

grounding: supported. Targets: AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation.

related_match to AIO:PrincipalComponentAnalysis and broad_match to AIO:LinearDimensionalityReduction are accurate.

Verified exact target existence in data/aio/ and documented why AIO:LassoRegression is rejected.

### Definition and scope

evidence: supported. Targets: AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation.

Definition accurately captures Theorems 1.1-1.3, Proposition 2.1, and Lemmas 3.1-3.4.

All equations and claims verified against arXiv:math/0408165v1 (pp. 1-24).

### Section 2 Proposition 2.1 and Section 3 Lemmas 3.1-3.4 companion inverse Stieltjes transform critical point splitting

evidence: supported. Targets: AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation.

Claim 1 (Silverstein-Choi companion inverse Stieltjes transform factorization and Lemma 3.4 sign condition) is verified.

Checked G_j(-1/alpha_j) = k_j (alpha_j - 1)^2 / [(alpha_j - 1)^2 - c_p] &gt; 0 iff &#124;alpha_j - 1&#124; &gt; sqrt(c_p) and O(1/n) midpoint cancellation.

### Theorems 1.1-1.3 and Propositions 3.5-3.6 almost-sure outlier eigenvalue limits and subcritical collapse

evidence: supported. Targets: AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation.

Claim 2 (Theorems 1.1-1.3 almost-sure outlier limits for 0 &lt; c &lt; 1, c &gt; 1, and c = 1) is verified.

Confirmed numerically for c = 0.5 (upper and lower supercritical outliers + subcritical collapse) and c = 2.0 (upper outlier + small-spike absorption).

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation.

The full record is consistent; retain DRAFT.

Read every field of BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation.yaml and verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T003200Z-baik-silverstein-spiked-eigenvalue-separation.json | supports | No normalized identity match for Baik-Silverstein Eigenvalue Separation for High-Dimensional Spiked Population Covariance Matrices across 442 pinned AIO records and 643 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected PrincipalComponentAnalysis and LinearDimensionalityReduction in the pinned AIO snapshot (2026-07-22). Provides accurate related_match and broad_match context. |
| calculation | research/discovery/baik-silverstein-spiked-eigenvalue-separation-boundaries.py | supports | Executed pure-Python verification in research/discovery/baik-silverstein-spiked-eigenvalue-separation-boundaries.py (SHA-256 1f18c5f2c14f7b713bae518da9c6867f0d9c3b8c01934e8c14d527cecdb3f5a8): verified (1) Theorems 1.1-1.2 critical points and bulk-edge continuity of psi(alpha) = alpha + c alpha / (alpha - 1) at alpha = 1 +- sqrt(c); (2) exact algebraic equivalence between the direct derivative of the Silverstein-Choi companion inverse Stieltjes transform z_p(m) (eq. 3.2) and the rational factorization [f(m) + (1/n) g(m)] / D(m) (eqs. 3.3-3.5), plus the Lemma 3.4 sign condition G_j(-1/alpha_j) = k_j (alpha_j - 1)^2 / [(alpha_j - 1)^2 - c_p] &gt; 0 iff &#124;alpha_j - 1&#124; &gt; sqrt(c_p) and O(1/n) midpoint cancellation of z_p(m_{j,+/-}^{(n)}); and (3) Monte Carlo non-Gaussian Rademacher sample covariance simulations confirming Theorem 1.1 for c = 0.5 (supercritical upper outlier s_1 = 4.154 ~ 4.200, subcritical collapse s_2 = 2.693 ~ 2.914, lower bulk edge s_{p-1} = 0.1107 ~ 0.0858, supercritical lower outlier s_p = 0.0369 ~ 0.0365) and Theorem 1.2 for c = 2.0 (supercritical upper outlier s_1 = 7.166 ~ 7.071, bulk edge s_2 = 5.123 ~ 5.828, and absorption of small spike alpha_p = 0.05 &lt; 1 with smallest nonzero eigenvalue s_n = 0.2193 ~ (1 - sqrt(2))^2 = 0.1716). |
| bs2006-spiked-pdf | https://export.arxiv.org/pdf/math/0408165.pdf; Pages 1-24 (J. Multivariate Anal. pp. 1382-1408), Sections 1-4 (Theorems 1.1-1.3, Proposition 2.1, Lemmas 3.1-3.4, Propositions 3.5-3.6) | supports | All 24 pages of Baik &amp; Silverstein (2006, J. Multivariate Anal. 97(6):1382-1408, arXiv:math/0408165v1) read and verified. |
| bs2006-spiked-abs | https://export.arxiv.org/abs/math/0408165; arXiv:math/0408165 abstract | supports | arXiv abstract and submission metadata read and verified. |
| bs2006-spiked-cr | https://api.crossref.org/works/10.1016/j.jmva.2005.08.003; DOI:10.1016/j.jmva.2005.08.003 Crossref metadata | supports | Journal of Multivariate Analysis 2006 Crossref metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Baik-Silverstein Eigenvalue Separation for High-Dimensional Spiked Population Covariance Matrices record, yielding 644 native and 442 unchanged generated records.
- All 24 PDF pages of arXiv:math/0408165v1 were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T003300Z-baik-silverstein-spiked-eigenvalue-separation
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Baik-Silverstein Eigenvalue Separation for
  High-Dimensional Spiked Population Covariance Matrices
started_at: '2026-10-19T00:32:00Z'
finished_at: '2026-10-19T00:33:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from MarcenkoPasturConvexOptimizationSpectrumEstimation,
    SparsePrincipalComponentsAnalysisViaCoordinateVarianceSelectionAndThresholding,
    and DiagonalThresholdingAndSemidefiniteRelaxationSupportRecoveryForSparsePCA,
    verified Theorems 1.1-1.3, Proposition 2.1, Lemmas 3.1-3.4, and Propositions 3.5-3.6,
    and documented primary-source typographical notes in Baik & Silverstein (2006,
    arXiv:math/0408165v1). This is adversarial author self-review, not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Baik-Silverstein Eigenvalue Separation for High-Dimensional Spiked
  Population Covariance Matrices as a distinct DRAFT mathematical_method with related_match
  PrincipalComponentAnalysis and broad_match LinearDimensionalityReduction mappings.
  Both claims and all locators across Baik & Silverstein (2006, J. Multivariate Anal.
  97(6):1382-1408, arXiv:math/0408165v1) are supported with explicit fourth-moment
  and c > 1 small-spike absorption limitations and primary-source typographical notes.
source:
  git_revision: 58903c47eb74e45b732b3a595398846d29505472
  state: working_tree
  inputs:
  - path: data/aio/PrincipalComponentAnalysis.yaml
    sha256: 7b45b5c558b7e984abb44e1610fb8d829409ae391a151ed0dc0e5cd95023e8d4
    role: context
  - path: data/curated/BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation.yaml
    sha256: 756d3dfde9d7e9d06e296c5c89e6846d91ab5ed98955ad1324f3d51ada58e92b
    role: target
  - path: data/curated/DiagonalThresholdingAndSemidefiniteRelaxationSupportRecoveryForSparsePCA.yaml
    sha256: bc93cbf86451897504cebd87dd3a8b3f51d5808be029487a537685b11c81d388
    role: context
  - path: data/curated/MarcenkoPasturConvexOptimizationSpectrumEstimation.yaml
    sha256: bf726e223ecf6df73f879f5a48ecb5c36f661e9a07d9f46273a48471ab31256a
    role: context
  - path: data/curated/SparsePrincipalComponentsAnalysisViaCoordinateVarianceSelectionAndThresholding.yaml
    sha256: 73d0e1b34afeb34f40b3e3fa2b3389ce0294b9468c284481d5b860945362b74f
    role: context
  - path: research/discovery/20261019T003200Z-baik-silverstein-spiked-eigenvalue-separation.json
    sha256: 475bf9cd4bde2e05cd1cd3703087b26cf65ce6a904b2443d54ccf3df9dba5146
    role: context
  - path: research/discovery/baik-silverstein-spiked-eigenvalue-separation-boundaries.py
    sha256: 1f18c5f2c14f7b713bae518da9c6867f0d9c3b8c01934e8c14d527cecdb3f5a8
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
- target_id: AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation
  path: data/curated/BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation.yaml
  label: Baik-Silverstein Eigenvalue Separation for High-Dimensional Spiked Population
    Covariance Matrices
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation.yaml
    role: maintained
scope:
  description: All fields of the exact maintained BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation
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
  - AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 644 curated concept record(s).
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 record(s); 0 drift.
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 297 history file(s).
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored record_review files match.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed Baik & Silverstein 2006 Silverstein-Choi companion inverse Stieltjes
    transform and Theorems 1.1-1.2 checks
  command: python3 research/discovery/baik-silverstein-spiked-eigenvalue-separation-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation
  exit_code: 0
  expected_exit_code: 0
  summary: 'Baik & Silverstein (2006) spiked covariance eigenvalue separation verified:
    c=0.5 (s_1=4.154~4.200, s_2=2.693~2.914, s_{p-1}=0.1107~0.0858, s_p=0.0369~0.0365);
    c=2.0 (s_1=7.166~7.071, s_2=5.123~5.828, s_n=0.2193~0.1716).'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T003200Z-baik-silverstein-spiked-eigenvalue-separation.json
  accessed_at: '2026-10-19T00:32:00Z'
  support: supports
  summary: No normalized identity match for Baik-Silverstein Eigenvalue Separation
    for High-Dimensional Spiked Population Covariance Matrices across 442 pinned AIO
    records and 643 maintained IDs, names, aliases and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T00:32:00Z'
  support: supports
  summary: Inspected PrincipalComponentAnalysis and LinearDimensionalityReduction
    in the pinned AIO snapshot (2026-07-22). Provides accurate related_match and broad_match
    context.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/baik-silverstein-spiked-eigenvalue-separation-boundaries.py
  accessed_at: '2026-10-19T00:32:00Z'
  snapshot_sha256: 1f18c5f2c14f7b713bae518da9c6867f0d9c3b8c01934e8c14d527cecdb3f5a8
  support: supports
  summary: 'Executed pure-Python verification in research/discovery/baik-silverstein-spiked-eigenvalue-separation-boundaries.py
    (SHA-256 1f18c5f2c14f7b713bae518da9c6867f0d9c3b8c01934e8c14d527cecdb3f5a8): verified
    (1) Theorems 1.1-1.2 critical points and bulk-edge continuity of psi(alpha) =
    alpha + c alpha / (alpha - 1) at alpha = 1 +- sqrt(c); (2) exact algebraic equivalence
    between the direct derivative of the Silverstein-Choi companion inverse Stieltjes
    transform z_p(m) (eq. 3.2) and the rational factorization [f(m) + (1/n) g(m)]
    / D(m) (eqs. 3.3-3.5), plus the Lemma 3.4 sign condition G_j(-1/alpha_j) = k_j
    (alpha_j - 1)^2 / [(alpha_j - 1)^2 - c_p] > 0 iff |alpha_j - 1| > sqrt(c_p) and
    O(1/n) midpoint cancellation of z_p(m_{j,+/-}^{(n)}); and (3) Monte Carlo non-Gaussian
    Rademacher sample covariance simulations confirming Theorem 1.1 for c = 0.5 (supercritical
    upper outlier s_1 = 4.154 ~ 4.200, subcritical collapse s_2 = 2.693 ~ 2.914, lower
    bulk edge s_{p-1} = 0.1107 ~ 0.0858, supercritical lower outlier s_p = 0.0369
    ~ 0.0365) and Theorem 1.2 for c = 2.0 (supercritical upper outlier s_1 = 7.166
    ~ 7.071, bulk edge s_2 = 5.123 ~ 5.828, and absorption of small spike alpha_p
    = 0.05 < 1 with smallest nonzero eigenvalue s_n = 0.2193 ~ (1 - sqrt(2))^2 = 0.1716).'
- evidence_id: bs2006-spiked-pdf
  kind: primary_source
  reference: https://export.arxiv.org/pdf/math/0408165.pdf
  locator: Pages 1-24 (J. Multivariate Anal. pp. 1382-1408), Sections 1-4 (Theorems
    1.1-1.3, Proposition 2.1, Lemmas 3.1-3.4, Propositions 3.5-3.6)
  accessed_at: '2026-10-18T17:22:00Z'
  snapshot_sha256: 1eb7d0eb27408acdc9178873a9c47c6a446ffe341f69477ea51c0474d9e2c960
  support: supports
  summary: All 24 pages of Baik & Silverstein (2006, J. Multivariate Anal. 97(6):1382-1408,
    arXiv:math/0408165v1) read and verified.
- evidence_id: bs2006-spiked-abs
  kind: primary_source
  reference: https://export.arxiv.org/abs/math/0408165
  locator: arXiv:math/0408165 abstract
  accessed_at: '2026-10-18T17:22:00Z'
  snapshot_sha256: 6a6cc776bed2cf882834344652cb4c4be7724b309380488a6e93e90d3d0f08d7
  support: supports
  summary: arXiv abstract and submission metadata read and verified.
- evidence_id: bs2006-spiked-cr
  kind: primary_source
  reference: https://api.crossref.org/works/10.1016/j.jmva.2005.08.003
  locator: DOI:10.1016/j.jmva.2005.08.003 Crossref metadata
  accessed_at: '2026-10-18T17:22:00Z'
  snapshot_sha256: 090b2257aed03868d9a574fc0040e5ac7b5c00f8b48603b2409f72de2c5af628
  support: supports
  summary: Journal of Multivariate Analysis 2006 Crossref metadata read and verified.
assessments:
- assessment_id: identity-boundary
  area: identity
  topic: Distinctness of Baik-Silverstein Eigenvalue Separation for High-Dimensional
    Spiked Population Covariance Matrices
  outcome: supported
  target_ids:
  - AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation
  evidence_ids:
  - identity
  - bs2006-spiked-pdf
  - bs2006-spiked-abs
  - bs2006-spiked-cr
  summary: Distinct mathematical_method for high-dimensional non-Gaussian spiked sample
    covariance eigenvalue separation.
  details: Resolved as a distinct AIMech-native mathematical_method concept from Baik
    & Silverstein (2006, Journal of Multivariate Analysis 97(6):1382-1408; arXiv:math/0408165v1,
    DOI:10.1016/j.jmva.2005.08.003). Distinct from AIMech:MarcenkoPasturConvexOptimizationSpectrumEstimation
    (El Karoui 2008, Ann. Statist. 36(6):2757-2790), which estimates the global limiting
    spectral distribution H via convex optimization of the unperturbed Silverstein-Choi
    equation without isolating finite-rank outlier spikes, from AIMech:SparsePrincipalComponentsAnalysisViaCoordinateVarianceSelectionAndThresholding
    (Johnstone & Lu 2009, JASA 104(486):682-693), which proves l2 eigenvector consistency
    of coordinate-variance selection and wavelet thresholding under sparsity, and
    from AIMech:DiagonalThresholdingAndSemidefiniteRelaxationSupportRecoveryForSparsePCA
    (Amini & Wainwright 2009, Ann. Statist. 37(5B):2877-2921), which analyzes signed
    support recovery via diagonal thresholding and semidefinite relaxation.
- assessment_id: aio-mappings
  area: grounding
  topic: AIO mappings for AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation
  outcome: supported
  target_ids:
  - AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation
  evidence_ids:
  - mapping
  - bs2006-spiked-pdf
  summary: related_match to AIO:PrincipalComponentAnalysis and broad_match to AIO:LinearDimensionalityReduction
    are accurate.
  details: Verified exact target existence in data/aio/ and documented why AIO:LassoRegression
    is rejected.
- assessment_id: definition
  area: evidence
  topic: Definition and scope
  outcome: supported
  target_ids:
  - AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation
  evidence_ids:
  - bs2006-spiked-pdf
  - bs2006-spiked-abs
  - bs2006-spiked-cr
  summary: Definition accurately captures Theorems 1.1-1.3, Proposition 2.1, and Lemmas
    3.1-3.4.
  details: All equations and claims verified against arXiv:math/0408165v1 (pp. 1-24).
- assessment_id: claim-1-companion-stieltjes-rouche-perturbation
  area: evidence
  topic: Section 2 Proposition 2.1 and Section 3 Lemmas 3.1-3.4 companion inverse
    Stieltjes transform critical point splitting
  outcome: supported
  target_ids:
  - AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation
  evidence_ids:
  - bs2006-spiked-pdf
  - calculation
  summary: Claim 1 (Silverstein-Choi companion inverse Stieltjes transform factorization
    and Lemma 3.4 sign condition) is verified.
  details: Checked G_j(-1/alpha_j) = k_j (alpha_j - 1)^2 / [(alpha_j - 1)^2 - c_p]
    > 0 iff |alpha_j - 1| > sqrt(c_p) and O(1/n) midpoint cancellation.
- assessment_id: claim-2-almost-sure-outlier-limits
  area: evidence
  topic: Theorems 1.1-1.3 and Propositions 3.5-3.6 almost-sure outlier eigenvalue
    limits and subcritical collapse
  outcome: supported
  target_ids:
  - AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation
  evidence_ids:
  - bs2006-spiked-pdf
  - calculation
  summary: Claim 2 (Theorems 1.1-1.3 almost-sure outlier limits for 0 < c < 1, c >
    1, and c = 1) is verified.
  details: Confirmed numerically for c = 0.5 (upper and lower supercritical outliers
    + subcritical collapse) and c = 2.0 (upper outlier + small-spike absorption).
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation
  evidence_ids:
  - identity
  - mapping
  - bs2006-spiked-pdf
  - bs2006-spiked-abs
  - bs2006-spiked-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Read every field of BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation.yaml
    and verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Baik-Silverstein Eigenvalue Separation for High-Dimensional Spiked
  Population Covariance Matrices record, yielding 644 native and 442 unchanged generated
  records.
- All 24 PDF pages of arXiv:math/0408165v1 were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- random-matrix-theory
- spiked-covariance
- stieltjes-transform
- eigenvalue-separation
- self-review
- discovery-ongoing
```
