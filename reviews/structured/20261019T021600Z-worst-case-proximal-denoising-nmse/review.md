# Scientific author self-review of Worst-Case Proximal Denoising Normalized Mean-Squared Error and Subdifferential Mean-Squared Distance

- Review: 20261019T021600Z-worst-case-proximal-denoising-nmse
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-19T02:15:00Z
- Finished UTC: 2026-10-19T02:16:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Worst-Case Proximal Denoising Normalized Mean-Squared Error and Subdifferential Mean-Squared Distance as a distinct DRAFT mathematical_method with LassoRegression and MathematicalOptimization mappings. All three claims across Oymak &amp; Hassibi (2016, Foundations of Computational Mathematics 16(4):965-1029, arXiv:1305.2714v5) are supported with explicit high-noise conservatism, non-minimality, and primary-source typographical limitations.

## Scope And Provenance

All fields of the exact maintained WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance record and its primary evidence.

Selection: Exact maintained ID: AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base fe1861cdbbd522deccb8670f43492dd26ed040f5.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance | data/curated/WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance.yaml | maintained | Worst-Case Proximal Denoising Normalized Mean-Squared Error and Subdifferential Mean-Squared Distance |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance | Validated 442 AIO concept record(s). |
| aimech validate-curated | passed | True | AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance | Validated 654 curated concept record(s). |
| aimech seed --check | passed | True | AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance | Checked 442 AIO concept record(s). |
| aimech validate-history | passed | True | AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance | Validated history sidecar files. |
| python3 worst-case-proximal-denoising-nmse-boundaries.py | passed | True | AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance | Oymak &amp; Hassibi (2016) verified: D(lam*partial f)=32.9944, NMSE(sigma=10)=10.0260, sigma-&gt;0 err=0.00e+00, Prop6.1 ratios=(l1:1.5060, nuc:1.004472), LASSO(m=60,D=40) eta=2.00, F=58.00. |

## Scientific And Domain Assessments

### Concept distinctness and boundary verification

identity: supported. Targets: AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance.

Worst-Case Proximal Denoising Normalized Mean-Squared Error and Subdifferential Mean-Squared Distance is a distinct mathematical_method unifying finite-noise and vanishing-noise proximal denoising risk with subdifferential geometry and projected LASSO risk.

Checked against all 442 pinned AIO concepts and 653 maintained AIMech concepts. Distinct from &#96;AIMech:ConicStatisticalDimensionIntrinsicVolumeConcentrationAndPhaseTransitions&#96; (Amelunxen, Lotz, McCoy, &amp; Tropp 2014, Information and Inference 3(3):224-294), which defines conic intrinsic volumes $v_k(C)$, statistical dimension $\delta(C) = \mathbb{E}[\&#124;\Pi_C(g)\&#124;_2^2]$, and kinematic conic intersection phase transitions, whereas Oymak &amp; Hassibi (2016) analyze finite-noise and vanishing-noise regularized proximal denoisers $x^*(\sigma\lambda, \sigma v)$ and constrained denoisers $x^c(\sigma v)$, proving point-wise domination $\&#124;x^*(\sigma\lambda, \sigma v) - x_0\&#124;_2 \le \operatorname{dist}(\sigma v, \sigma\lambda\partial f(x_0))$ (Lemma 5.1) and the exact identity $\sup_{\sigma &gt; 0} \operatorname{NMSE}(\sigma) = \lim_{\sigma \to 0^+} \operatorname{NMSE}(\sigma) = \mathbf{D}(\lambda\partial f(x_0))$ (Theorem 1.1), establishing tight multiplicative sandwiching ratios $1 + 2/\sqrt{k^3/n}$ and $1 + 2/\sqrt{r^3 d}$ between $\inf_{\lambda \ge 0}\mathbf{D}(\lambda\partial f(x_0))$ and the squared Gaussian complexity $\mathbf{S}(T_f(x_0) \cap \mathcal{B}^n)$ (Proposition 6.1), and deriving the high-SNR projected LASSO risk $\mathbf{D}/(m - \mathbf{D})$ and optimal cost $m - \mathbf{D}/(m - \mathbf{D})$ (Theorem 3.3 and Proposition 7.1). Also distinct from &#96;AIMech:AtomicNormConvexGeometryAndTangentConeGaussianWidthForLinearInverseProblems&#96; (Chandrasekaran et al. 2012) and &#96;AIMech:MinimaxRiskOfMatrixDenoisingBySingularValueSoftThresholding&#96; (Donoho &amp; Gavish 2014).

### AIO mapping accuracy

grounding: supported. Targets: AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance.

Related_match to AIO:LassoRegression and broad_match to AIO:MathematicalOptimization accurately situate proximal denoising subdifferential distance bounds within the pinned AIO hierarchy.

Verified exact target existence in data/aio/.

### Claim 1: Point-wise subdifferential domination and exact vanishing-noise proximal and constrained denoising NMSE

evidence: supported. Targets: AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance.

Claim 1 is directly supported by Sections 2.2, 3.1, 5, and Appendix B (Theorem 1.1, Theorem 3.1, Lemmas 5.1-5.3, Proposition 5.2, and Lemma B.1) of arXiv:1305.2714v5.

Verified finite-sigma l_1 soft-thresholding NMSE monotonicity and convergence to D(lambda partial &#124;&#124;x_0&#124;&#124;_1) = 32.9944 with 0.00e+00 error in pure Python.

### Claim 2: Gaussian squared complexity sandwiching and decomposable subdifferential cone gap bounds

evidence: supported. Targets: AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance.

Claim 2 is supported by Section 6 Propositions 6.1-6.2 and Appendix C Lemmas C.1-C.4 (pp. 16-17, 29-31) of arXiv:1305.2714v5.

Verified Proposition 6.1 multiplicative sandwiching ratios (l_1: 1.5060, nuclear: 1.004472) in pure Python.

### Claim 3: Compressed sensing phase transition and projected LASSO asymptotic risk and cost laws

evidence: supported. Targets: AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance.

Claim 3 is supported by Section 3.3 Theorem 3.3 and Section 7.2 Proposition 7.1 (pp. 7-8, 18-19) of arXiv:1305.2714v5.

Verified projected LASSO risk eta = D/(m-D) = 2.00 and residual cost F = m - D/(m-D) = 58.00 at m=60, D=40 in pure Python.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance.

The full record is consistent; retain DRAFT.

Read every field of WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance.yaml and verified all schema, history, and review gates.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261019T021500Z-worst-case-proximal-denoising-nmse.json | supports | No normalized identity match for Worst-Case Proximal Denoising Normalized Mean-Squared Error and Subdifferential Mean-Squared Distance across 442 pinned AIO records and 653 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected LassoRegression and MathematicalOptimization in the pinned AIO snapshot (2026-07-22). Provides accurate related_match and broad_match context. |
| calculation | research/discovery/worst-case-proximal-denoising-nmse-boundaries.py | supports | Verified in pure Python: (1) for l_1 soft-thresholding at n=100, k=10, lambda=1.2, and non-zero amplitude x_{0,i}=2.5, the exact analytic finite-sigma NMSE increases monotonically from NMSE(sigma=10)=10.0260 as sigma decreases and converges to D(lambda partial &#124;&#124;x_0&#124;&#124;_1) = 32.9944 with error 0.00e+00 at sigma=1e-6, confirming Theorem 1.1 and Lemma 5.1; (2) Proposition 6.1 multiplicative sandwiching ratios evaluate to 1.5060 for l_1 (n=1000, k=25) and 1.004472 for the nuclear norm (d=200, r=10); and (3) Theorem 3.3 / Proposition 7.1 projected LASSO risk eta = D/(m-D) = 2.00 and residual cost F = m - D/(m-D) = 58.00 at m=60, D=40 satisfy exact complementarity and diverge at the phase transition m -&gt; D+. |
| oh2016-prox-denoising-pdf | https://export.arxiv.org/pdf/1305.2714.pdf; Pages 1-37 (Foundations of Computational Mathematics 16(4):965-1029), Sections 1-11 and Appendices A-F | supports | All 37 pages of Oymak &amp; Hassibi (2016, Foundations of Computational Mathematics 16(4):965-1029, arXiv:1305.2714v5) read and verified. |
| oh2016-prox-denoising-abs | https://arxiv.org/abs/1305.2714; arXiv:1305.2714 abstract | supports | arXiv abstract and submission metadata read and verified. |
| oh2016-prox-denoising-crossref | https://api.crossref.org/works/10.1007/s10208-015-9278-4; Foundations of Computational Mathematics 16(4):965-1029 Crossref metadata | supports | Foundations of Computational Mathematics (2016) Crossref metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Worst-Case Proximal Denoising Normalized Mean-Squared Error and Subdifferential Mean-Squared Distance record, yielding 654 native and 442 unchanged generated records.
- All 37 PDF pages of arXiv:1305.2714v5 were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T021600Z-worst-case-proximal-denoising-nmse
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Worst-Case Proximal Denoising Normalized Mean-Squared
  Error and Subdifferential Mean-Squared Distance
started_at: '2026-10-19T02:15:00Z'
finished_at: '2026-10-19T02:16:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from ConicStatisticalDimensionIntrinsicVolumeConcentrationAndPhaseTransitions,
    AtomicNormConvexGeometryAndTangentConeGaussianWidthForLinearInverseProblems, and
    MinimaxRiskOfMatrixDenoisingBySingularValueSoftThresholding, verified Theorems
    1.1, 3.1, 3.3 and Proposition 6.1 in pure Python, and identified four primary-source
    typographical errors in Oymak & Hassibi (2016, arXiv:1305.2714v5). This is adversarial
    author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Worst-Case Proximal Denoising Normalized Mean-Squared Error and Subdifferential
  Mean-Squared Distance as a distinct DRAFT mathematical_method with LassoRegression
  and MathematicalOptimization mappings. All three claims across Oymak & Hassibi (2016,
  Foundations of Computational Mathematics 16(4):965-1029, arXiv:1305.2714v5) are
  supported with explicit high-noise conservatism, non-minimality, and primary-source
  typographical limitations.
source:
  git_revision: fe1861cdbbd522deccb8670f43492dd26ed040f5
  state: working_tree
  inputs:
  - path: data/aio/LassoRegression.yaml
    sha256: c62e7ffd00a16f5a82d514687b094aee5f6796d19a7d16200bdb10498c024949
    role: context
  - path: data/curated/AtomicNormConvexGeometryAndTangentConeGaussianWidthForLinearInverseProblems.yaml
    sha256: 08d5b4f4bd301541c007103136cc533333a570d95cbe293b38ed739313cdfe8e
    role: context
  - path: data/curated/ConicStatisticalDimensionIntrinsicVolumeConcentrationAndPhaseTransitions.yaml
    sha256: f30902cac7658717e5cd219a904f8e5e890f77e899893c9d3845f7fe2d590cd1
    role: context
  - path: data/curated/MinimaxRiskOfMatrixDenoisingBySingularValueSoftThresholding.yaml
    sha256: 85d72d8d72d7537327d96cce6944f55cc20fe7b458d42b34967098fa8d1fe856
    role: context
  - path: data/curated/WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance.yaml
    sha256: 7143c4561a89996de5d338fc6377d5317b771c08828a1fa5fa60d2b785eb46bf
    role: target
  - path: research/discovery/20261019T021500Z-worst-case-proximal-denoising-nmse.json
    sha256: 407a2f81b7232e52e29587db6c0b4cd155bb492c7405c04c88097f553dd38899
    role: context
  - path: research/discovery/worst-case-proximal-denoising-nmse-boundaries.py
    sha256: 1d43005f67499d12912747a721af4ba9fbd6bcd1795dd0e2169f308fddb45c7b
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
- target_id: AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance
  path: data/curated/WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance.yaml
  label: Worst-Case Proximal Denoising Normalized Mean-Squared Error and Subdifferential
    Mean-Squared Distance
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance.yaml
    role: maintained
scope:
  description: All fields of the exact maintained WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance
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
  - AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 442 AIO concept record(s).
- check_id: validation-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance
  exit_code: 0
  expected_exit_code: 0
  summary: Validated 654 curated concept record(s).
- check_id: validation-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance
  exit_code: 0
  expected_exit_code: 0
  summary: Checked 442 AIO concept record(s).
- check_id: validation-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance
  exit_code: 0
  expected_exit_code: 0
  summary: Validated history sidecar files.
- check_id: validation-5
  name: python3 worst-case-proximal-denoising-nmse-boundaries.py
  command: python3 research/discovery/worst-case-proximal-denoising-nmse-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance
  exit_code: 0
  expected_exit_code: 0
  summary: 'Oymak & Hassibi (2016) verified: D(lam*partial f)=32.9944, NMSE(sigma=10)=10.0260,
    sigma->0 err=0.00e+00, Prop6.1 ratios=(l1:1.5060, nuc:1.004472), LASSO(m=60,D=40)
    eta=2.00, F=58.00.'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261019T021500Z-worst-case-proximal-denoising-nmse.json
  accessed_at: '2026-10-19T02:15:00Z'
  support: supports
  summary: No normalized identity match for Worst-Case Proximal Denoising Normalized
    Mean-Squared Error and Subdifferential Mean-Squared Distance across 442 pinned
    AIO records and 653 maintained IDs, names, aliases and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-19T02:15:00Z'
  support: supports
  summary: Inspected LassoRegression and MathematicalOptimization in the pinned AIO
    snapshot (2026-07-22). Provides accurate related_match and broad_match context.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/worst-case-proximal-denoising-nmse-boundaries.py
  accessed_at: '2026-10-19T02:15:00Z'
  snapshot_sha256: 1d43005f67499d12912747a721af4ba9fbd6bcd1795dd0e2169f308fddb45c7b
  support: supports
  summary: 'Verified in pure Python: (1) for l_1 soft-thresholding at n=100, k=10,
    lambda=1.2, and non-zero amplitude x_{0,i}=2.5, the exact analytic finite-sigma
    NMSE increases monotonically from NMSE(sigma=10)=10.0260 as sigma decreases and
    converges to D(lambda partial ||x_0||_1) = 32.9944 with error 0.00e+00 at sigma=1e-6,
    confirming Theorem 1.1 and Lemma 5.1; (2) Proposition 6.1 multiplicative sandwiching
    ratios evaluate to 1.5060 for l_1 (n=1000, k=25) and 1.004472 for the nuclear
    norm (d=200, r=10); and (3) Theorem 3.3 / Proposition 7.1 projected LASSO risk
    eta = D/(m-D) = 2.00 and residual cost F = m - D/(m-D) = 58.00 at m=60, D=40 satisfy
    exact complementarity and diverge at the phase transition m -> D+.'
- evidence_id: oh2016-prox-denoising-pdf
  kind: primary_source
  reference: https://export.arxiv.org/pdf/1305.2714.pdf
  locator: Pages 1-37 (Foundations of Computational Mathematics 16(4):965-1029), Sections
    1-11 and Appendices A-F
  accessed_at: '2026-10-19T02:15:00Z'
  snapshot_sha256: 316e368e253f464daf136a24930baca3a6266b2f6a0a17668483775761e30a62
  support: supports
  summary: All 37 pages of Oymak & Hassibi (2016, Foundations of Computational Mathematics
    16(4):965-1029, arXiv:1305.2714v5) read and verified.
- evidence_id: oh2016-prox-denoising-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1305.2714
  locator: arXiv:1305.2714 abstract
  accessed_at: '2026-10-19T02:15:00Z'
  snapshot_sha256: 0994d0cef57d50115111a499f53cd46d4c10d7e97adfc7d4d6dcc60ae93547f6
  support: supports
  summary: arXiv abstract and submission metadata read and verified.
- evidence_id: oh2016-prox-denoising-crossref
  kind: primary_source
  reference: https://api.crossref.org/works/10.1007/s10208-015-9278-4
  locator: Foundations of Computational Mathematics 16(4):965-1029 Crossref metadata
  accessed_at: '2026-10-19T02:15:00Z'
  snapshot_sha256: 1b39f0c7f4dcfa1a8d9a65d68d915ac119762107416e733976dfa350a0436085
  support: supports
  summary: Foundations of Computational Mathematics (2016) Crossref metadata read
    and verified.
assessments:
- assessment_id: identity-and-boundary
  area: identity
  topic: Concept distinctness and boundary verification
  outcome: supported
  target_ids:
  - AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance
  evidence_ids:
  - identity
  - oh2016-prox-denoising-pdf
  - oh2016-prox-denoising-abs
  - oh2016-prox-denoising-crossref
  summary: Worst-Case Proximal Denoising Normalized Mean-Squared Error and Subdifferential
    Mean-Squared Distance is a distinct mathematical_method unifying finite-noise
    and vanishing-noise proximal denoising risk with subdifferential geometry and
    projected LASSO risk.
  details: Checked against all 442 pinned AIO concepts and 653 maintained AIMech concepts.
    Distinct from `AIMech:ConicStatisticalDimensionIntrinsicVolumeConcentrationAndPhaseTransitions`
    (Amelunxen, Lotz, McCoy, & Tropp 2014, Information and Inference 3(3):224-294),
    which defines conic intrinsic volumes $v_k(C)$, statistical dimension $\delta(C)
    = \mathbb{E}[\|\Pi_C(g)\|_2^2]$, and kinematic conic intersection phase transitions,
    whereas Oymak & Hassibi (2016) analyze finite-noise and vanishing-noise regularized
    proximal denoisers $x^*(\sigma\lambda, \sigma v)$ and constrained denoisers $x^c(\sigma
    v)$, proving point-wise domination $\|x^*(\sigma\lambda, \sigma v) - x_0\|_2 \le
    \operatorname{dist}(\sigma v, \sigma\lambda\partial f(x_0))$ (Lemma 5.1) and the
    exact identity $\sup_{\sigma > 0} \operatorname{NMSE}(\sigma) = \lim_{\sigma \to
    0^+} \operatorname{NMSE}(\sigma) = \mathbf{D}(\lambda\partial f(x_0))$ (Theorem
    1.1), establishing tight multiplicative sandwiching ratios $1 + 2/\sqrt{k^3/n}$
    and $1 + 2/\sqrt{r^3 d}$ between $\inf_{\lambda \ge 0}\mathbf{D}(\lambda\partial
    f(x_0))$ and the squared Gaussian complexity $\mathbf{S}(T_f(x_0) \cap \mathcal{B}^n)$
    (Proposition 6.1), and deriving the high-SNR projected LASSO risk $\mathbf{D}/(m
    - \mathbf{D})$ and optimal cost $m - \mathbf{D}/(m - \mathbf{D})$ (Theorem 3.3
    and Proposition 7.1). Also distinct from `AIMech:AtomicNormConvexGeometryAndTangentConeGaussianWidthForLinearInverseProblems`
    (Chandrasekaran et al. 2012) and `AIMech:MinimaxRiskOfMatrixDenoisingBySingularValueSoftThresholding`
    (Donoho & Gavish 2014).
- assessment_id: aio-mapping-sufficiency
  area: grounding
  topic: AIO mapping accuracy
  outcome: supported
  target_ids:
  - AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance
  evidence_ids:
  - mapping
  - oh2016-prox-denoising-pdf
  summary: Related_match to AIO:LassoRegression and broad_match to AIO:MathematicalOptimization
    accurately situate proximal denoising subdifferential distance bounds within the
    pinned AIO hierarchy.
  details: Verified exact target existence in data/aio/.
- assessment_id: claim-1-verification
  area: evidence
  topic: 'Claim 1: Point-wise subdifferential domination and exact vanishing-noise
    proximal and constrained denoising NMSE'
  outcome: supported
  target_ids:
  - AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance
  evidence_ids:
  - oh2016-prox-denoising-pdf
  - calculation
  summary: Claim 1 is directly supported by Sections 2.2, 3.1, 5, and Appendix B (Theorem
    1.1, Theorem 3.1, Lemmas 5.1-5.3, Proposition 5.2, and Lemma B.1) of arXiv:1305.2714v5.
  details: Verified finite-sigma l_1 soft-thresholding NMSE monotonicity and convergence
    to D(lambda partial ||x_0||_1) = 32.9944 with 0.00e+00 error in pure Python.
- assessment_id: claim-2-verification
  area: evidence
  topic: 'Claim 2: Gaussian squared complexity sandwiching and decomposable subdifferential
    cone gap bounds'
  outcome: supported
  target_ids:
  - AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance
  evidence_ids:
  - oh2016-prox-denoising-pdf
  - calculation
  summary: Claim 2 is supported by Section 6 Propositions 6.1-6.2 and Appendix C Lemmas
    C.1-C.4 (pp. 16-17, 29-31) of arXiv:1305.2714v5.
  details: 'Verified Proposition 6.1 multiplicative sandwiching ratios (l_1: 1.5060,
    nuclear: 1.004472) in pure Python.'
- assessment_id: claim-3-verification
  area: evidence
  topic: 'Claim 3: Compressed sensing phase transition and projected LASSO asymptotic
    risk and cost laws'
  outcome: supported
  target_ids:
  - AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance
  evidence_ids:
  - oh2016-prox-denoising-pdf
  - calculation
  summary: Claim 3 is supported by Section 3.3 Theorem 3.3 and Section 7.2 Proposition
    7.1 (pp. 7-8, 18-19) of arXiv:1305.2714v5.
  details: Verified projected LASSO risk eta = D/(m-D) = 2.00 and residual cost F
    = m - D/(m-D) = 58.00 at m=60, D=40 in pure Python.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance
  evidence_ids:
  - identity
  - mapping
  - oh2016-prox-denoising-pdf
  - oh2016-prox-denoising-abs
  - oh2016-prox-denoising-crossref
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: Read every field of WorstCaseProximalDenoisingNMSEAndSubdifferentialMeanSquaredDistance.yaml
    and verified all schema, history, and review gates.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Worst-Case Proximal Denoising Normalized Mean-Squared Error and
  Subdifferential Mean-Squared Distance record, yielding 654 native and 442 unchanged
  generated records.
- All 37 PDF pages of arXiv:1305.2714v5 were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- proximal-denoising
- subdifferential-geometry
- lasso-risk
- phase-transitions
- self-review
- discovery-ongoing
```
