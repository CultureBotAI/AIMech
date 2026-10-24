# Scientific author self-review of Loss-Specific Optimal Eigenvalue Shrinkage for Spiked Covariance Matrices

- Review: 20261019T005300Z-optimal-eigenvalue-shrinkage-spiked-covariance
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T00:52:00Z
- Finished UTC: 2026-10-19T00:53:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Loss-Specific Optimal Eigenvalue Shrinkage for Spiked Covariance Matrices as a distinct DRAFT mathematical_method with related_match PrincipalComponentAnalysis mapping. All three claims and locators across Donoho, Gavish, &amp; Johnstone (2018, Ann. Stat. 46(4):1742-1778, arXiv:1311.0851v3) are supported with explicit precision-operator Tracy-Widom discontinuity and isotropic-bulk limitations and primary-source typographical notes.

## Scope And Provenance

All fields of the exact maintained LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices record and its primary evidence.

Selection: Exact maintained ID: AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 49fa2c71ac3cf05e84292ead176e7593856479b1.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices | data/curated/LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices.yaml | maintained | Loss-Specific Optimal Eigenvalue Shrinkage for Spiked Covariance Matrices |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices | Validated 646 curated concept record(s). |
| aimech seed --check | passed | True | AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices | Checked 442 record(s); 0 drift. |
| aimech validate-history | passed | True | AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices | Validated 299 history file(s). |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices | Vendored record_review files match. |
| aimech check-source | passed | True | AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices | Exited 0 without output. |
| Constructed Donoho, Gavish, &amp; Johnstone 2018 2x2 pivot-loss optimal shrinkage and Wishart Monte Carlo checks | passed | True | AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices | Donoho, Gavish, &amp; Johnstone (2018) loss-specific optimal eigenvalue shrinkage verified: Frobenius loss 38.67 -&gt; 7.18 (asymp=6.18); Stein loss 9.69 -&gt; 0.33 (asymp=0.30); MP median sigma^2_hat=2.578 vs 2.500. |

## Scientific And Domain Assessments

### Distinctness of Loss-Specific Optimal Eigenvalue Shrinkage for Spiked Covariance Matrices

identity: supported. Targets: AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices.

Distinct mathematical_method for loss-specific optimal eigenvalue shrinkage in the spiked covariance model.

Resolved against all 442 pinned AIO concepts and 645 maintained AIMech records. Distinct from AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation (Baik &amp; Silverstein 2006), which establishes the first-order almost-sure forward eigenvalue limit lambda(ell) = ell + gamma ell / (ell - 1) via companion inverse Stieltjes transforms without eigenvector cosine decoupling, 2 x 2 pivot-loss block reduction, or loss-specific eigenvalue shrinkage estimators; distinct from AIMech:BaikBenArousPecheLargestEigenvaluePhaseTransition (Baik, Ben Arous, &amp; Peche 2005), which characterizes the M^{-2/3} F_k and M^{-1/2} G_k fluctuation distributions of the largest sample eigenvalue; distinct from AIMech:RotationallyInvariantNonlinearShrinkageCovarianceEstimation (Ledoit &amp; Wolf 2012) and AIMech:QuESTNonlinearShrinkageCovarianceEstimation (Ledoit &amp; Wolf 2015, 2017), which target bulk-regime general population spectra with O(p) non-trivial eigenvalues under Frobenius or minimum-variance loss via sample Stieltjes transforms rather than finite-rank spiked 2 x 2 pivot-loss reductions across 26 matrix losses; and distinct from AIMech:LedoitWolfLinearShrinkageCovariance (Ledoit &amp; Wolf 2004), which restricts shrinkage to affine combinations of S and I_p.

### AIO mappings for AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices

grounding: supported. Targets: AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices.

related_match to AIO:PrincipalComponentAnalysis is accurate.

Verified exact target existence in data/aio/ and documented why AIO:LassoRegression is rejected.

### Definition and scope

evidence: supported. Targets: AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices.

Definition accurately captures Lemma 1, Theorem 1, Table 2, Propositions 1-3, Theorem 2, and Lemma 9.

All equations and claims verified against arXiv:1311.0851v3 (pp. 1-36).

### Lemma 1 and Lemmas 5-7 simultaneous 2x2 QR Gram-Schmidt block diagonalization and pivot-loss decoupling

evidence: supported. Targets: AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices.

Claim 1 (Lemma 1 and Lemma 7 simultaneous 2x2 block diagonalization and loss decoupling) is verified.

Verified 2x2 matrices A(ell) and B(eta, c(ell)) and exact component loss formulas.

### Theorem 1, Lemma 4, and Table 2 closed-form loss-specific optimal shrinkers across 18 losses

evidence: supported. Targets: AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices.

Claim 2 (Table 2 closed-form shrinkers for Frobenius, Stein, Operator, Nuclear, and Frechet losses) is verified.

Confirmed 2x2 grid-optimality, strict shrinker ordering, and nuclear-norm neighborhood bulk collapse where c^2(ell) &lt;= 1/2.

### Propositions 1-3 rank-agnostic bulk tail control, Theorem 2 equivariant oracle optimality, and Lemma 9 MP median variance plug-in

evidence: supported. Targets: AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices.

Claim 3 (Propositions 1-3, Theorem 2, and Lemma 9 MP median plug-in) is verified.

Verified Frobenius and Stein Monte Carlo risk reductions and Marcenko-Pastur median noise variance estimation.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices.

The full record is consistent; retain DRAFT.

Read every field of LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices.yaml and verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T005200Z-optimal-eigenvalue-shrinkage-spiked-covariance.json | supports | No normalized identity match for Loss-Specific Optimal Eigenvalue Shrinkage for Spiked Covariance Matrices across 442 pinned AIO records and 645 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected PrincipalComponentAnalysis in the pinned AIO snapshot (2026-07-22). Provides accurate related_match context. |
| calculation | research/discovery/optimal-eigenvalue-shrinkage-spiked-covariance-boundaries.py | supports | Verified analytically and via Monte Carlo: (1) exact forward/inverse Baik-Silverstein bijection lambda(ell) = ell + gamma ell / (ell - 1) and ell(lambda) above lambda_+(gamma); (2) nuclear-norm neighborhood bulk shrinkage eta_*^N(ell) = 1 on (ell_+(gamma), 1 + 0.5*(gamma + sqrt(gamma^2 + 8*gamma))] where c^2(ell) &lt;= 1/2; (3) strict ordering 1 &lt; eta_*^{St}(ell) &lt; eta_*^{fre}(ell) &lt; eta_*^F(ell) &lt; eta_*^O(ell) = ell and 2x2 grid-optimality across Frobenius, Stein, Operator, and Nuclear losses; and (4) high-dimensional Wishart simulation (n=120, p=60, gamma=0.5, spikes 5.0 and 3.0) reducing Frobenius squared loss from 38.67 to 7.18 (asymptotic 6.18) and Stein loss from 9.69 to 0.33 (asymptotic 0.30) with Marcenko-Pastur median variance plug-in hat_sigma^2 = 2.578 vs 2.500. |
| dgj2018-spiked-shrinkage-pdf | https://export.arxiv.org/pdf/1311.0851.pdf; Pages 1-36 (Ann. Stat. pp. 1742-1778), Sections 1-9 and Supplement (Lemma 1, Definitions 1-6, Theorem 1, Tables 1-2, Propositions 1-3, Theorem 2, Lemma 9) | supports | All 36 pages of Donoho, Gavish, &amp; Johnstone (2018, Ann. Stat. 46(4):1742-1778, arXiv:1311.0851v3) read and verified. |
| dgj2018-spiked-shrinkage-abs | https://arxiv.org/abs/1311.0851; arXiv:1311.0851 abstract | supports | arXiv abstract and submission metadata read and verified. |
| dgj2018-spiked-shrinkage-cr | https://api.crossref.org/works/10.1214/17-AOS1601; DOI:10.1214/17-AOS1601 Crossref metadata | supports | The Annals of Statistics 2018 Crossref metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Loss-Specific Optimal Eigenvalue Shrinkage for Spiked Covariance Matrices record, yielding 646 native and 442 unchanged generated records.
- All 36 PDF pages of arXiv:1311.0851v3 were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T005300Z-optimal-eigenvalue-shrinkage-spiked-covariance
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Loss-Specific Optimal Eigenvalue Shrinkage
  for Spiked Covariance Matrices
started_at: '2026-10-19T00:52:00Z'
finished_at: '2026-10-19T00:53:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation,
    BaikBenArousPecheLargestEigenvaluePhaseTransition, and RotationallyInvariantNonlinearShrinkageCovarianceEstimation,
    verified Lemma 1, Theorem 1, Table 2, Propositions 1-3, Theorem 2, and Lemma 9,
    and documented primary-source typographical notes in Donoho, Gavish, & Johnstone
    (2018, arXiv:1311.0851v3). This is adversarial author self-review, not independent
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Loss-Specific Optimal Eigenvalue Shrinkage for Spiked Covariance Matrices
  as a distinct DRAFT mathematical_method with related_match PrincipalComponentAnalysis
  mapping. All three claims and locators across Donoho, Gavish, & Johnstone (2018,
  Ann. Stat. 46(4):1742-1778, arXiv:1311.0851v3) are supported with explicit precision-operator
  Tracy-Widom discontinuity and isotropic-bulk limitations and primary-source typographical
  notes.
source:
  git_revision: 49fa2c71ac3cf05e84292ead176e7593856479b1
  state: working_tree
  inputs:
  - path: data/aio/PrincipalComponentAnalysis.yaml
    sha256: 7b45b5c558b7e984abb44e1610fb8d829409ae391a151ed0dc0e5cd95023e8d4
    role: context
  - path: data/curated/BaikBenArousPecheLargestEigenvaluePhaseTransition.yaml
    sha256: c298917167b99c6a12d1b98c4dcf229e563be721314de5619bea5dfb3a6bc7e6
    role: context
  - path: data/curated/BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation.yaml
    sha256: 756d3dfde9d7e9d06e296c5c89e6846d91ab5ed98955ad1324f3d51ada58e92b
    role: context
  - path: data/curated/LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices.yaml
    sha256: f6c45ac7b8a8f8f5f8c5a105acc0fba83a445f80424cdc0053376c8f85cc49f5
    role: target
  - path: research/discovery/20261019T005200Z-optimal-eigenvalue-shrinkage-spiked-covariance.json
    sha256: 03d64787eec942a32c64e28f94f4ad298438b7f9e27865dbfde9c038a9d0fb5e
    role: context
  - path: research/discovery/optimal-eigenvalue-shrinkage-spiked-covariance-boundaries.py
    sha256: 4fb7bd559cebafca09783b110d8aca4b291ec95feb75f9bc0d07157872d29c00
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
- target_id: AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
  path: data/curated/LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices.yaml
  label: Loss-Specific Optimal Eigenvalue Shrinkage for Spiked Covariance Matrices
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices.yaml
    role: maintained
scope:
  description: All fields of the exact maintained LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
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
  - AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 646 curated concept record(s).
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 record(s); 0 drift.
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 299 history file(s).
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored record_review files match.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed Donoho, Gavish, & Johnstone 2018 2x2 pivot-loss optimal shrinkage
    and Wishart Monte Carlo checks
  command: python3 research/discovery/optimal-eigenvalue-shrinkage-spiked-covariance-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
  exit_code: 0
  expected_exit_code: 0
  summary: 'Donoho, Gavish, & Johnstone (2018) loss-specific optimal eigenvalue shrinkage
    verified: Frobenius loss 38.67 -> 7.18 (asymp=6.18); Stein loss 9.69 -> 0.33 (asymp=0.30);
    MP median sigma^2_hat=2.578 vs 2.500.'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T005200Z-optimal-eigenvalue-shrinkage-spiked-covariance.json
  accessed_at: '2026-10-19T00:52:00Z'
  support: supports
  summary: No normalized identity match for Loss-Specific Optimal Eigenvalue Shrinkage
    for Spiked Covariance Matrices across 442 pinned AIO records and 645 maintained
    IDs, names, aliases and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T00:52:00Z'
  support: supports
  summary: Inspected PrincipalComponentAnalysis in the pinned AIO snapshot (2026-07-22).
    Provides accurate related_match context.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/optimal-eigenvalue-shrinkage-spiked-covariance-boundaries.py
  accessed_at: '2026-10-19T00:52:00Z'
  snapshot_sha256: 4fb7bd559cebafca09783b110d8aca4b291ec95feb75f9bc0d07157872d29c00
  support: supports
  summary: 'Verified analytically and via Monte Carlo: (1) exact forward/inverse Baik-Silverstein
    bijection lambda(ell) = ell + gamma ell / (ell - 1) and ell(lambda) above lambda_+(gamma);
    (2) nuclear-norm neighborhood bulk shrinkage eta_*^N(ell) = 1 on (ell_+(gamma),
    1 + 0.5*(gamma + sqrt(gamma^2 + 8*gamma))] where c^2(ell) <= 1/2; (3) strict ordering
    1 < eta_*^{St}(ell) < eta_*^{fre}(ell) < eta_*^F(ell) < eta_*^O(ell) = ell and
    2x2 grid-optimality across Frobenius, Stein, Operator, and Nuclear losses; and
    (4) high-dimensional Wishart simulation (n=120, p=60, gamma=0.5, spikes 5.0 and
    3.0) reducing Frobenius squared loss from 38.67 to 7.18 (asymptotic 6.18) and
    Stein loss from 9.69 to 0.33 (asymptotic 0.30) with Marcenko-Pastur median variance
    plug-in hat_sigma^2 = 2.578 vs 2.500.'
- evidence_id: dgj2018-spiked-shrinkage-pdf
  kind: primary_source
  reference: https://export.arxiv.org/pdf/1311.0851.pdf
  locator: Pages 1-36 (Ann. Stat. pp. 1742-1778), Sections 1-9 and Supplement (Lemma
    1, Definitions 1-6, Theorem 1, Tables 1-2, Propositions 1-3, Theorem 2, Lemma
    9)
  accessed_at: '2026-10-18T17:41:00Z'
  snapshot_sha256: 72c9e3fda5844df2e515446e82c2ed61d758e4a098ef1601fe3603e3d7b501dd
  support: supports
  summary: All 36 pages of Donoho, Gavish, & Johnstone (2018, Ann. Stat. 46(4):1742-1778,
    arXiv:1311.0851v3) read and verified.
- evidence_id: dgj2018-spiked-shrinkage-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1311.0851
  locator: arXiv:1311.0851 abstract
  accessed_at: '2026-10-18T17:41:00Z'
  snapshot_sha256: 7629c38bd03b036cf26709ed7fb58527b3a6a60081ce642c47e1d3a3147db46f
  support: supports
  summary: arXiv abstract and submission metadata read and verified.
- evidence_id: dgj2018-spiked-shrinkage-cr
  kind: primary_source
  reference: https://api.crossref.org/works/10.1214/17-AOS1601
  locator: DOI:10.1214/17-AOS1601 Crossref metadata
  accessed_at: '2026-10-18T17:41:00Z'
  snapshot_sha256: de54e58fa73d6974d13a107c849e3247207bbcfc186d8f8d1d5fb929b3df3e2c
  support: supports
  summary: The Annals of Statistics 2018 Crossref metadata read and verified.
assessments:
- assessment_id: identity-boundary
  area: identity
  topic: Distinctness of Loss-Specific Optimal Eigenvalue Shrinkage for Spiked Covariance
    Matrices
  outcome: supported
  target_ids:
  - AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
  evidence_ids:
  - identity
  - dgj2018-spiked-shrinkage-pdf
  - dgj2018-spiked-shrinkage-abs
  - dgj2018-spiked-shrinkage-cr
  summary: Distinct mathematical_method for loss-specific optimal eigenvalue shrinkage
    in the spiked covariance model.
  details: Resolved against all 442 pinned AIO concepts and 645 maintained AIMech
    records. Distinct from AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation
    (Baik & Silverstein 2006), which establishes the first-order almost-sure forward
    eigenvalue limit lambda(ell) = ell + gamma ell / (ell - 1) via companion inverse
    Stieltjes transforms without eigenvector cosine decoupling, 2 x 2 pivot-loss block
    reduction, or loss-specific eigenvalue shrinkage estimators; distinct from AIMech:BaikBenArousPecheLargestEigenvaluePhaseTransition
    (Baik, Ben Arous, & Peche 2005), which characterizes the M^{-2/3} F_k and M^{-1/2}
    G_k fluctuation distributions of the largest sample eigenvalue; distinct from
    AIMech:RotationallyInvariantNonlinearShrinkageCovarianceEstimation (Ledoit & Wolf
    2012) and AIMech:QuESTNonlinearShrinkageCovarianceEstimation (Ledoit & Wolf 2015,
    2017), which target bulk-regime general population spectra with O(p) non-trivial
    eigenvalues under Frobenius or minimum-variance loss via sample Stieltjes transforms
    rather than finite-rank spiked 2 x 2 pivot-loss reductions across 26 matrix losses;
    and distinct from AIMech:LedoitWolfLinearShrinkageCovariance (Ledoit & Wolf 2004),
    which restricts shrinkage to affine combinations of S and I_p.
- assessment_id: aio-mappings
  area: grounding
  topic: AIO mappings for AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
  outcome: supported
  target_ids:
  - AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
  evidence_ids:
  - mapping
  - dgj2018-spiked-shrinkage-pdf
  summary: related_match to AIO:PrincipalComponentAnalysis is accurate.
  details: Verified exact target existence in data/aio/ and documented why AIO:LassoRegression
    is rejected.
- assessment_id: definition
  area: evidence
  topic: Definition and scope
  outcome: supported
  target_ids:
  - AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
  evidence_ids:
  - dgj2018-spiked-shrinkage-pdf
  - dgj2018-spiked-shrinkage-abs
  - dgj2018-spiked-shrinkage-cr
  summary: Definition accurately captures Lemma 1, Theorem 1, Table 2, Propositions
    1-3, Theorem 2, and Lemma 9.
  details: All equations and claims verified against arXiv:1311.0851v3 (pp. 1-36).
- assessment_id: claim-1-2x2-gram-schmidt-block-decomposition
  area: evidence
  topic: Lemma 1 and Lemmas 5-7 simultaneous 2x2 QR Gram-Schmidt block diagonalization
    and pivot-loss decoupling
  outcome: supported
  target_ids:
  - AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
  evidence_ids:
  - dgj2018-spiked-shrinkage-pdf
  - calculation
  summary: Claim 1 (Lemma 1 and Lemma 7 simultaneous 2x2 block diagonalization and
    loss decoupling) is verified.
  details: Verified 2x2 matrices A(ell) and B(eta, c(ell)) and exact component loss
    formulas.
- assessment_id: claim-2-closed-form-loss-specific-shrinkers
  area: evidence
  topic: Theorem 1, Lemma 4, and Table 2 closed-form loss-specific optimal shrinkers
    across 18 losses
  outcome: supported
  target_ids:
  - AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
  evidence_ids:
  - dgj2018-spiked-shrinkage-pdf
  - calculation
  summary: Claim 2 (Table 2 closed-form shrinkers for Frobenius, Stein, Operator,
    Nuclear, and Frechet losses) is verified.
  details: Confirmed 2x2 grid-optimality, strict shrinker ordering, and nuclear-norm
    neighborhood bulk collapse where c^2(ell) <= 1/2.
- assessment_id: claim-3-rank-agnostic-oracle-and-unknown-sigma2
  area: evidence
  topic: Propositions 1-3 rank-agnostic bulk tail control, Theorem 2 equivariant oracle
    optimality, and Lemma 9 MP median variance plug-in
  outcome: supported
  target_ids:
  - AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
  evidence_ids:
  - dgj2018-spiked-shrinkage-pdf
  - calculation
  summary: Claim 3 (Propositions 1-3, Theorem 2, and Lemma 9 MP median plug-in) is
    verified.
  details: Verified Frobenius and Stein Monte Carlo risk reductions and Marcenko-Pastur
    median noise variance estimation.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
  evidence_ids:
  - identity
  - mapping
  - dgj2018-spiked-shrinkage-pdf
  - dgj2018-spiked-shrinkage-abs
  - dgj2018-spiked-shrinkage-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Read every field of LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices.yaml
    and verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Loss-Specific Optimal Eigenvalue Shrinkage for Spiked Covariance
  Matrices record, yielding 646 native and 442 unchanged generated records.
- All 36 PDF pages of arXiv:1311.0851v3 were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- random-matrix-theory
- spiked-covariance
- eigenvalue-shrinkage
- stein-loss
- self-review
- discovery-ongoing
```
