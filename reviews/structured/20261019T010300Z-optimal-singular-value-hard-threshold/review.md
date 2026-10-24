# Scientific author self-review of Optimal Singular Value Hard Thresholding at 4/sqrt(3) for Low-Rank Matrix Denoising

- Review: 20261019T010300Z-optimal-singular-value-hard-threshold
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T01:02:00Z
- Finished UTC: 2026-10-19T01:03:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Optimal Singular Value Hard Thresholding at 4/sqrt(3) for Low-Rank Matrix Denoising as a distinct DRAFT mathematical_method with related_match PrincipalComponentAnalysis mapping. All three claims and locators across Gavish &amp; Donoho (2014, IEEE Trans. Inf. Theory 60(8):5040-5053, arXiv:1305.5870v3) are supported with explicit continuous-shrinkage comparison, fixed-rank, and bulk-edge Tracy-Widom limitations and primary-source typographical notes.

## Scope And Provenance

All fields of the exact maintained OptimalSingularValueHardThresholdingAtFourOverSqrtThree record and its primary evidence.

Selection: Exact maintained ID: AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9d5bad6e59d8ff8808ad96b96d4d646d921e4aa2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree | data/curated/OptimalSingularValueHardThresholdingAtFourOverSqrtThree.yaml | maintained | Optimal Singular Value Hard Thresholding at 4/sqrt(3) for Low-Rank Matrix Denoising |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree | Validated 647 curated concept record(s). |
| aimech seed --check | passed | True | AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree | Checked 442 record(s); 0 drift. |
| aimech validate-history | passed | True | AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree | Validated 300 history file(s). |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree | Vendored record_review files match. |
| aimech check-source | passed | True | AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree | Exited 0 without output. |
| Constructed Gavish &amp; Donoho 2014 SVHT 4/sqrt(3), Table I-IV, and Monte Carlo checks | passed | True | AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree | Gavish &amp; Donoho (2014) optimal singular value hard threshold 4/sqrt(3) verified: tau*=2.3094 (adaptive tau^*=2.2969), MSE SVHT=2.885 (adaptive=2.885) vs TSVD=7.788 and USVT=5.022. |

## Scientific And Domain Assessments

### Distinctness of Optimal Singular Value Hard Thresholding at 4/sqrt(3) for Low-Rank Matrix Denoising

identity: supported. Targets: AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree.

Distinct mathematical_method for optimal singular value hard thresholding at lambda_*(beta) sqrt(n) sigma and omega(beta) y_{med}.

Resolved against all 442 pinned AIO concepts and 646 maintained AIMech records. Distinct from AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices (Donoho, Gavish, &amp; Johnstone 2018), which shrinks eigenvalues eta(lambda_i) of symmetric sample covariance matrices S = (1/n) X'X toward a unit noise bulk floor 1 across 26 covariance pivot-losses rather than hard-thresholding rectangular data singular values y_i to 0 at tau_* = lambda_*(beta) sqrt(n) sigma under Frobenius MSE; distinct from AIMech:SingularValueThresholdingForMatrixCompletion (Cai, Candes, &amp; Shen 2010), which applies iterative soft thresholding (y_i - tau)_+ within Uzawa subgradient iterations for incomplete matrix nuclear-norm minimization; and distinct from AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation (Baik &amp; Silverstein 2006) and AIMech:BaikBenArousPecheLargestEigenvaluePhaseTransition (Baik, Ben Arous, &amp; Peche 2005), which analyze sample covariance eigenvalue limits and fluctuations without singular-vector rotation AMSE trade-offs or matrix denoising estimators.

### AIO mappings for AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree

grounding: supported. Targets: AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree.

related_match to AIO:PrincipalComponentAnalysis is accurate.

Verified exact target existence in data/aio/ and documented why AIO:LassoRegression is rejected.

### Definition and scope

evidence: supported. Targets: AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree.

Definition accurately captures Theorems 1-5, Lemmas 1-5, Corollaries 1-3, and Tables I-IV.

All equations and claims verified against arXiv:1305.5870v3 (pp. 1-14).

### Lemmas 2-4 singular-vector rotation AMSE decomposition and indifference quartic root lambda_*(beta)

evidence: supported. Targets: AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree.

Claim 1 (Lemma 4 AMSE formula and quartic indifference root x_*^4 - (beta+1)x_*^2 - 3*beta = 0) is verified.

Verified Table I values and exact root x_*(4/sqrt(3)) = sqrt(3) for beta = 1.

### Theorems 1-5 uniform admissibility over TSVD and minimax AMSE over bounded-rank and nuclear-norm classes

evidence: supported. Targets: AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree.

Claim 2 (Theorems 1-5 and Tables II-III worst-case AMSE constants 3r vs 4.26r, 5r, 6r, 2r and sqrt(3)*xi) is verified.

Confirmed analytically and via low-SNR Monte Carlo where SVHT reduces MSE from 7.788 (TSVD) and 5.022 (USVT) to 2.885.

### Lemma 1, Corollaries 1-3, Table IV Marcenko-Pastur median unknown-sigma adaptation omega(beta) y_{med}, and Section VI general white noise

evidence: supported. Targets: AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree.

Claim 3 (Table IV omega(beta) = lambda_*(beta)/sqrt(mu_beta) and cubic polynomial approximation) is verified.

Verified Table IV via quarter-circle substitution integration t = u^2 (omega(1) = 2.8582) and adaptive Monte Carlo threshold.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree.

The full record is consistent; retain DRAFT.

Read every field of OptimalSingularValueHardThresholdingAtFourOverSqrtThree.yaml and verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T010200Z-optimal-singular-value-hard-threshold.json | supports | No normalized identity match for Optimal Singular Value Hard Thresholding at 4/sqrt(3) for Low-Rank Matrix Denoising across 442 pinned AIO records and 646 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected PrincipalComponentAnalysis in the pinned AIO snapshot (2026-07-22). Provides accurate related_match context. |
| calculation | research/discovery/optimal-singular-value-hard-threshold-boundaries.py | supports | Verified analytically and via Monte Carlo: (1) exact reproduction of Table I aspect-ratio optimal thresholds lambda_*(beta) for beta in {0.05, 0.25, 0.50, 0.75, 1.00} with lambda_*(1) = 4/sqrt(3) ~= 2.3094; (2) exact verification of the indifference quartic x_*^4 - (beta + 1) x_*^2 - 3 beta = 0, Table II square-matrix worst-case AMSE constants (SVHT 3r, USVT 4.26r, TSVD 5r), and Theorem 5 nuclear-norm minimax constant sqrt(3); (3) exact reproduction of Table IV unknown-noise coefficients omega(beta) = lambda_*(beta) / sqrt(mu_beta) (omega(1) = 2.8582) via quarter-circle substitution t = u^2 and cubic approximation within 0.02; and (4) finite-sample Monte Carlo (n=60, r=2, low-SNR singular values 1.25 and 1.15) confirming SVHT (MSE=2.885, adaptive=2.885) substantially outperforms oracle-rank TSVD (MSE=7.788) and USVT 2.02 (MSE=5.022). |
| gd2014-svht-pdf | https://export.arxiv.org/pdf/1305.5870.pdf; Pages 1-14 (IEEE Trans. Inf. Theory pp. 5040-5053), Sections I-VIII (Theorems 1-5, Lemmas 1-5, Corollaries 1-3, Tables I-IV) | supports | All 14 pages of Gavish &amp; Donoho (2014, IEEE Trans. Inf. Theory 60(8):5040-5053, arXiv:1305.5870v3) read and verified. |
| gd2014-svht-abs | https://arxiv.org/abs/1305.5870; arXiv:1305.5870 abstract | supports | arXiv abstract and submission metadata read and verified. |
| gd2014-svht-cr | https://api.crossref.org/works/10.1109/TIT.2014.2323359; DOI:10.1109/TIT.2014.2323359 Crossref metadata | supports | IEEE Transactions on Information Theory 2014 Crossref metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Optimal Singular Value Hard Thresholding at 4/sqrt(3) for Low-Rank Matrix Denoising record, yielding 647 native and 442 unchanged generated records.
- All 14 PDF pages of arXiv:1305.5870v3 were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T010300Z-optimal-singular-value-hard-threshold
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Optimal Singular Value Hard Thresholding at
  4/sqrt(3) for Low-Rank Matrix Denoising
started_at: '2026-10-19T01:02:00Z'
finished_at: '2026-10-19T01:03:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
    and SingularValueThresholdingForMatrixCompletion, verified Theorems 1-5, Lemmas
    1-5, Corollaries 1-3, and Tables I-IV, and documented primary-source typographical
    notes in Gavish & Donoho (2014, arXiv:1305.5870v3). This is adversarial author
    self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Optimal Singular Value Hard Thresholding at 4/sqrt(3) for Low-Rank
  Matrix Denoising as a distinct DRAFT mathematical_method with related_match PrincipalComponentAnalysis
  mapping. All three claims and locators across Gavish & Donoho (2014, IEEE Trans.
  Inf. Theory 60(8):5040-5053, arXiv:1305.5870v3) are supported with explicit continuous-shrinkage
  comparison, fixed-rank, and bulk-edge Tracy-Widom limitations and primary-source
  typographical notes.
source:
  git_revision: 9d5bad6e59d8ff8808ad96b96d4d646d921e4aa2
  state: working_tree
  inputs:
  - path: data/aio/PrincipalComponentAnalysis.yaml
    sha256: 7b45b5c558b7e984abb44e1610fb8d829409ae391a151ed0dc0e5cd95023e8d4
    role: context
  - path: data/curated/LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices.yaml
    sha256: f6c45ac7b8a8f8f5f8c5a105acc0fba83a445f80424cdc0053376c8f85cc49f5
    role: context
  - path: data/curated/OptimalSingularValueHardThresholdingAtFourOverSqrtThree.yaml
    sha256: 5b589c274241ca2a72f36559f894c1519725673723f200d0afbd4a90c89166f6
    role: target
  - path: research/discovery/20261019T010200Z-optimal-singular-value-hard-threshold.json
    sha256: 7f0909c7397322a11d500de3d245ba1914df1dd3595a06bde7f927cd2aae69b0
    role: context
  - path: research/discovery/optimal-singular-value-hard-threshold-boundaries.py
    sha256: 5d1646b5b1a2b7e1c4bbc222ec6d65eebe43c1ee6b8b1d394c1bc3a607f23f61
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
- target_id: AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree
  path: data/curated/OptimalSingularValueHardThresholdingAtFourOverSqrtThree.yaml
  label: Optimal Singular Value Hard Thresholding at 4/sqrt(3) for Low-Rank Matrix
    Denoising
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/OptimalSingularValueHardThresholdingAtFourOverSqrtThree.yaml
    role: maintained
scope:
  description: All fields of the exact maintained OptimalSingularValueHardThresholdingAtFourOverSqrtThree
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree
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
  - AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 647 curated concept record(s).
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 record(s); 0 drift.
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 300 history file(s).
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored record_review files match.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed Gavish & Donoho 2014 SVHT 4/sqrt(3), Table I-IV, and Monte Carlo
    checks
  command: python3 research/discovery/optimal-singular-value-hard-threshold-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree
  exit_code: 0
  expected_exit_code: 0
  summary: 'Gavish & Donoho (2014) optimal singular value hard threshold 4/sqrt(3)
    verified: tau*=2.3094 (adaptive tau^*=2.2969), MSE SVHT=2.885 (adaptive=2.885)
    vs TSVD=7.788 and USVT=5.022.'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T010200Z-optimal-singular-value-hard-threshold.json
  accessed_at: '2026-10-19T01:02:00Z'
  support: supports
  summary: No normalized identity match for Optimal Singular Value Hard Thresholding
    at 4/sqrt(3) for Low-Rank Matrix Denoising across 442 pinned AIO records and 646
    maintained IDs, names, aliases and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T01:02:00Z'
  support: supports
  summary: Inspected PrincipalComponentAnalysis in the pinned AIO snapshot (2026-07-22).
    Provides accurate related_match context.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/optimal-singular-value-hard-threshold-boundaries.py
  accessed_at: '2026-10-19T01:02:00Z'
  snapshot_sha256: 5d1646b5b1a2b7e1c4bbc222ec6d65eebe43c1ee6b8b1d394c1bc3a607f23f61
  support: supports
  summary: 'Verified analytically and via Monte Carlo: (1) exact reproduction of Table
    I aspect-ratio optimal thresholds lambda_*(beta) for beta in {0.05, 0.25, 0.50,
    0.75, 1.00} with lambda_*(1) = 4/sqrt(3) ~= 2.3094; (2) exact verification of
    the indifference quartic x_*^4 - (beta + 1) x_*^2 - 3 beta = 0, Table II square-matrix
    worst-case AMSE constants (SVHT 3r, USVT 4.26r, TSVD 5r), and Theorem 5 nuclear-norm
    minimax constant sqrt(3); (3) exact reproduction of Table IV unknown-noise coefficients
    omega(beta) = lambda_*(beta) / sqrt(mu_beta) (omega(1) = 2.8582) via quarter-circle
    substitution t = u^2 and cubic approximation within 0.02; and (4) finite-sample
    Monte Carlo (n=60, r=2, low-SNR singular values 1.25 and 1.15) confirming SVHT
    (MSE=2.885, adaptive=2.885) substantially outperforms oracle-rank TSVD (MSE=7.788)
    and USVT 2.02 (MSE=5.022).'
- evidence_id: gd2014-svht-pdf
  kind: primary_source
  reference: https://export.arxiv.org/pdf/1305.5870.pdf
  locator: Pages 1-14 (IEEE Trans. Inf. Theory pp. 5040-5053), Sections I-VIII (Theorems
    1-5, Lemmas 1-5, Corollaries 1-3, Tables I-IV)
  accessed_at: '2026-10-18T17:46:40Z'
  snapshot_sha256: efdf529e9df7c910ae7e3a02dcaa420a8cf0463ae5559ef1d432a0fa43d32f4f
  support: supports
  summary: All 14 pages of Gavish & Donoho (2014, IEEE Trans. Inf. Theory 60(8):5040-5053,
    arXiv:1305.5870v3) read and verified.
- evidence_id: gd2014-svht-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1305.5870
  locator: arXiv:1305.5870 abstract
  accessed_at: '2026-10-18T17:46:39Z'
  snapshot_sha256: cd92e0db3b8af880a25eaa0956542d2a82f323a5cad216a60660404947ec0afb
  support: supports
  summary: arXiv abstract and submission metadata read and verified.
- evidence_id: gd2014-svht-cr
  kind: primary_source
  reference: https://api.crossref.org/works/10.1109/TIT.2014.2323359
  locator: DOI:10.1109/TIT.2014.2323359 Crossref metadata
  accessed_at: '2026-10-18T17:46:39Z'
  snapshot_sha256: 5e82266f48ecde691aeac4310aedc0a38a1d29d9ca145a064821123737144e8f
  support: supports
  summary: IEEE Transactions on Information Theory 2014 Crossref metadata read and
    verified.
assessments:
- assessment_id: identity-boundary
  area: identity
  topic: Distinctness of Optimal Singular Value Hard Thresholding at 4/sqrt(3) for
    Low-Rank Matrix Denoising
  outcome: supported
  target_ids:
  - AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree
  evidence_ids:
  - identity
  - gd2014-svht-pdf
  - gd2014-svht-abs
  - gd2014-svht-cr
  summary: Distinct mathematical_method for optimal singular value hard thresholding
    at lambda_*(beta) sqrt(n) sigma and omega(beta) y_{med}.
  details: Resolved against all 442 pinned AIO concepts and 646 maintained AIMech
    records. Distinct from AIMech:LossSpecificOptimalEigenvalueShrinkageForSpikedCovarianceMatrices
    (Donoho, Gavish, & Johnstone 2018), which shrinks eigenvalues eta(lambda_i) of
    symmetric sample covariance matrices S = (1/n) X'X toward a unit noise bulk floor
    1 across 26 covariance pivot-losses rather than hard-thresholding rectangular
    data singular values y_i to 0 at tau_* = lambda_*(beta) sqrt(n) sigma under Frobenius
    MSE; distinct from AIMech:SingularValueThresholdingForMatrixCompletion (Cai, Candes,
    & Shen 2010), which applies iterative soft thresholding (y_i - tau)_+ within Uzawa
    subgradient iterations for incomplete matrix nuclear-norm minimization; and distinct
    from AIMech:BaikSilversteinSpikedPopulationCovarianceEigenvalueSeparation (Baik
    & Silverstein 2006) and AIMech:BaikBenArousPecheLargestEigenvaluePhaseTransition
    (Baik, Ben Arous, & Peche 2005), which analyze sample covariance eigenvalue limits
    and fluctuations without singular-vector rotation AMSE trade-offs or matrix denoising
    estimators.
- assessment_id: aio-mappings
  area: grounding
  topic: AIO mappings for AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree
  outcome: supported
  target_ids:
  - AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree
  evidence_ids:
  - mapping
  - gd2014-svht-pdf
  summary: related_match to AIO:PrincipalComponentAnalysis is accurate.
  details: Verified exact target existence in data/aio/ and documented why AIO:LassoRegression
    is rejected.
- assessment_id: definition
  area: evidence
  topic: Definition and scope
  outcome: supported
  target_ids:
  - AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree
  evidence_ids:
  - gd2014-svht-pdf
  - gd2014-svht-abs
  - gd2014-svht-cr
  summary: Definition accurately captures Theorems 1-5, Lemmas 1-5, Corollaries 1-3,
    and Tables I-IV.
  details: All equations and claims verified against arXiv:1305.5870v3 (pp. 1-14).
- assessment_id: claim-1-amse-decomposition-and-indifference-quartic
  area: evidence
  topic: Lemmas 2-4 singular-vector rotation AMSE decomposition and indifference quartic
    root lambda_*(beta)
  outcome: supported
  target_ids:
  - AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree
  evidence_ids:
  - gd2014-svht-pdf
  - calculation
  summary: Claim 1 (Lemma 4 AMSE formula and quartic indifference root x_*^4 - (beta+1)x_*^2
    - 3*beta = 0) is verified.
  details: Verified Table I values and exact root x_*(4/sqrt(3)) = sqrt(3) for beta
    = 1.
- assessment_id: claim-2-uniform-admissibility-and-minimax-guarantees
  area: evidence
  topic: Theorems 1-5 uniform admissibility over TSVD and minimax AMSE over bounded-rank
    and nuclear-norm classes
  outcome: supported
  target_ids:
  - AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree
  evidence_ids:
  - gd2014-svht-pdf
  - calculation
  summary: Claim 2 (Theorems 1-5 and Tables II-III worst-case AMSE constants 3r vs
    4.26r, 5r, 6r, 2r and sqrt(3)*xi) is verified.
  details: Confirmed analytically and via low-SNR Monte Carlo where SVHT reduces MSE
    from 7.788 (TSVD) and 5.022 (USVT) to 2.885.
- assessment_id: claim-3-unknown-noise-mp-median-and-haar-general-noise
  area: evidence
  topic: Lemma 1, Corollaries 1-3, Table IV Marcenko-Pastur median unknown-sigma adaptation
    omega(beta) y_{med}, and Section VI general white noise
  outcome: supported
  target_ids:
  - AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree
  evidence_ids:
  - gd2014-svht-pdf
  - calculation
  summary: Claim 3 (Table IV omega(beta) = lambda_*(beta)/sqrt(mu_beta) and cubic
    polynomial approximation) is verified.
  details: Verified Table IV via quarter-circle substitution integration t = u^2 (omega(1)
    = 2.8582) and adaptive Monte Carlo threshold.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:OptimalSingularValueHardThresholdingAtFourOverSqrtThree
  evidence_ids:
  - identity
  - mapping
  - gd2014-svht-pdf
  - gd2014-svht-abs
  - gd2014-svht-cr
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Read every field of OptimalSingularValueHardThresholdingAtFourOverSqrtThree.yaml
    and verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Optimal Singular Value Hard Thresholding at 4/sqrt(3) for Low-Rank
  Matrix Denoising record, yielding 647 native and 442 unchanged generated records.
- All 14 PDF pages of arXiv:1305.5870v3 were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- random-matrix-theory
- singular-value-thresholding
- matrix-denoising
- marcenko-pastur
- self-review
- discovery-ongoing
```
