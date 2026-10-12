# Scientific author self-review of correlation-based cascade identification

- Review: 20261012T142331Z-correlation-cascade-resolved
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-12T14:17:29Z
- Finished UTC: 2026-10-12T14:23:31Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain both algorithms and related mappings; comparative citation finding is resolved.

## Scope And Provenance

All fields of the exact two-record correlation-based Wiener/Hammerstein identification cohort.

Selection: Exact IDs: AIMech:CorrelationBasedWienerIdentification, AIMech:CorrelationBasedHammersteinIdentification
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base 587cfc9f78766b2c1b49ee00175b3bcf7f763ade.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:CorrelationBasedWienerIdentification | data/curated/CorrelationBasedWienerIdentification.yaml | maintained | Correlation-based Wiener identification |
| AIMech:CorrelationBasedHammersteinIdentification | data/curated/CorrelationBasedHammersteinIdentification.yaml | maintained | Correlation-based Hammerstein identification |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:CorrelationBasedWienerIdentification, AIMech:CorrelationBasedHammersteinIdentification | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 98.54s (0:01:38)<br>Checked 442 record(s); 0 failed.<br>Checked 536 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 183 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 181,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:CorrelationBasedWienerIdentification, AIMech:CorrelationBasedHammersteinIdentification | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:CorrelationBasedWienerIdentification, AIMech:CorrelationBasedHammersteinIdentification | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:CorrelationBasedWienerIdentification, AIMech:CorrelationBasedHammersteinIdentification | Exited 0 without output. |
| Exact Gaussian and finite-design boundary examples | passed | True | AIMech:CorrelationBasedWienerIdentification, AIMech:CorrelationBasedHammersteinIdentification | {"wiener_square_cross": ["6", "12"], "hammerstein_square_cross": ["2", "4"], "wiener_nonzero_mean_cancellation": ["0", "0"], "hammerstein_nonzero_mean_cancellation": ["0", "0"], "wiener_zero_dc_cross": ["0", "0"], "wiener_scaled_design": [["7", "49"], ["28", "784"], ["21", "441"]], "hammerstein_scaled_design": [["3", "3"], ["12", "18"], ["9", "27"]], "wiener_scaled_coefficients": ["1/7", "1/49"], "hammerstein_scaled_coefficients": ["1/3", "1/3"], "wiener_reconstructed_output": ["2", "20", "12"], "hammerstein_reconstructed_output": ["2", "10", "12"], "independent_uncentered_noise_second_moment": "2", "uncentered_noise_through_origin_slope": "2"} |

## Scientific And Domain Assessments

### Distinct observed-input two-stage cascade estimators

identity: supported. Targets: AIMech:CorrelationBasedWienerIdentification, AIMech:CorrelationBasedHammersteinIdentification.

Retain the two algorithm identities.

The first stages use related Gaussian correlation separation, but the second stages do not commute: Wiener takes powers after linear filtering, whereas Hammerstein filters each input power. Internal gain consequently rescales degree j by beta^j versus a common alpha. These are not the existing cascade model families, recursive prediction-error or pseudo-linear updates, structure selection, image Wiener filtering, or unknown-input blind deconvolution. The local names do not claim priority or original terminology.

### Claim-level support for the opposite estimator design

evidence: supported. Targets: AIMech:CorrelationBasedWienerIdentification, AIMech:CorrelationBasedHammersteinIdentification.

Both comparative claims now cite the two supporting primary passages.

Both design-matrix claims explicitly contrast Wiener and Hammerstein ordering. Their own report supports the local procedure, but the opposite ordering is supported by the other fully inspected report. Include both evidence-source identities and both precise claim citations so each maintained record is independently traceable. The mechanism itself is supported by the combined inspected evidence.

### Algorithm, component fitting and analysis task

grounding: supported. Targets: AIMech:CorrelationBasedWienerIdentification, AIMech:CorrelationBasedHammersteinIdentification.

Related mappings are supported curator assessments.

Both stages use residual-squared parameter fitting after the source’s correlation-based separation. The pinned target describes a general fitting analysis, whereas this record specifies an ordered identification procedure with excitation and block-structure assumptions. A related mapping reflects its component mechanism without claiming exact identity or an asserted subclass. The procedure estimates nonlinear dynamical structure from temporal input/output observations and lagged correlations. The pinned target is the analysis task; related mapping preserves the algorithm/task distinction. Both stages use residual-squared parameter fitting after the source’s correlation-based separation. The pinned target describes a general fitting analysis, whereas this record specifies an ordered identification procedure with excitation and block-structure assumptions. A related mapping reflects its component mechanism without claiming exact identity or an asserted subclass. The procedure estimates nonlinear dynamical structure from temporal input/output observations and lagged correlations. The pinned target is the analysis task; related mapping preserves the algorithm/task distinction.

### correlation-separation

evidence: supported. Targets: AIMech:CorrelationBasedWienerIdentification.

Mechanism or boundary is supported within its stated scope.

The first stage correlates measured output with the centered Gaussian input fluctuation, while the actual excitation can include a constant mean. Under the source’s white-Gaussian and independent-output-noise assumptions, the population correlation has form beta*h at unit input spectral normalization, where h is the LTI impulse response and beta depends on the polynomial and excitation moments. A sampled rational transfer function is fitted to that scaled response. Recovering its shape requires beta != 0 and a meaningful finite-moment linear response; BIBO stability alone is not a substitute for finite filtered variance in an ideal continuous-white formulation. Locators: Equations 2–12, PDF pp. 5–7 / printed pp. 2–4; finite-moment and nonzero-gain conditions are curator qualifications of the displayed factorization

### powers-of-filtered-input

evidence: supported. Targets: AIMech:CorrelationBasedWienerIdentification.

Mechanism or boundary is supported within its stated scope.

Apply the estimated scaled linear dynamics to the measured input, including its mean, to reconstruct qhat. For a chosen degree k, form columns qhat^j, j=1,...,k, and least-squares fit measured output. The displayed Gram inverse requires full column rank; practical solves need numerical conditioning. This uses powers of a filtered input, whereas Hammerstein identification filters the individual input powers. Polynomial degree, linear order and transient handling remain supplied choices. Locators: Equations 12–17, PDF pp. 7–8 / printed pp. 4–5; Figure 1, PDF p. 12; Section 2, Equations 15–17, PDF pp. 8–9 / printed pp. 6–7: Hammerstein filtered-input-power design

### scale-reparameterization

evidence: supported. Targets: AIMech:CorrelationBasedWienerIdentification.

Mechanism or boundary is supported within its stated scope.

If the first stage recovers beta*L, the reconstructed internal variable is beta*q, so the polynomial coefficient of degree j becomes gamma_j/beta^j. The composite response can be recovered without determining the original block gains. In a separate exact zero-state example with h=(1,2), u=(1,2,-1), g(v)=v+v² and scale 7, the reconstructed signal is (7,28,21), and coefficients (1/7,1/49) give outputs (2,20,12). This verifies the reparameterization, not a stochastic estimator’s accuracy. Locators: Equations 13–17 and coefficient relation following Equation 15, PDF pp. 7–8 / printed pp. 4–5; curator exact calculations in research/discovery/correlation-identification-boundaries.py

### nonzero-mean-cancellation

evidence: supported. Targets: AIMech:CorrelationBasedWienerIdentification.

Mechanism or boundary is supported within its stated scope.

A nonzero input mean does not guarantee an informative first correlation. In the discrete iid unit-variance Gaussian example u_t=1+x_t, h=(1,2), q has mean 3 and variance 5. For g(q)=q³-42q, Gaussian moments give E[g(q_t)*x_t]=E[g(q_t)*x_(t-1)]=0 although g is nonconstant. An even nonlinearity with a zero-DC-gain linear block can also defeat an input mean shift. These curator examples qualify the source conclusion; they do not prove that all identification methods fail. Locators: Equations 6–11, PDF pp. 6–7 / printed pp. 3–4; Conclusions, PDF p. 9 / printed p. 6; curator exact Gaussian-moment calculations in research/discovery/correlation-identification-boundaries.py

### correlation-separation

evidence: supported. Targets: AIMech:CorrelationBasedHammersteinIdentification.

Mechanism or boundary is supported within its stated scope.

The first stage correlates centered output with the centered Gaussian input fluctuation of excitation u=b+x. Under the source’s independent-output-noise and sufficiently white practical-excitation assumptions, the result approximates alpha*h, with alpha=mu*[gamma1+2*b*gamma2+3*gamma3*(variance(x)+b²)+...] and mu the input autocorrelation area. The report explicitly distinguishes finite practical variance from ideal continuous-white variance. For discrete iid unit-variance Gaussian inputs the corresponding factorization is exact at the population level. A nonzero alpha and appropriate moment/linear-response conditions are needed for recovery. Locators: Section 2, Equations 3–14, PDF pp. 5–8 / printed pp. 3–6; the discrete iid statement is a direct curator Gaussian-moment consequence of these equations

### filtered-input-powers

evidence: supported. Targets: AIMech:CorrelationBasedHammersteinIdentification.

Mechanism or boundary is supported within its stated scope.

After estimating the scaled linear response, build a design column for each degree j by filtering u^j through that response. Least-squares fit measured output on these columns. The input u includes the applied mean; x denotes the centered fluctuation only in the correlation stage. The displayed inverse requires full column rank. This differs from raising a filtered input to successive powers as in Wiener identification, and it does not select the polynomial degree or linear order automatically. Locators: Section 2, Equations 14–17, PDF pp. 8–9 / printed pp. 6–7; Figure 2, PDF p. 22; Equations 13–17, PDF pp. 7–8 / printed pp. 4–5: Wiener powers-of-filtered-input design

### scale-reparameterization

evidence: supported. Targets: AIMech:CorrelationBasedHammersteinIdentification.

Mechanism or boundary is supported within its stated scope.

If the first stage recovers alpha*L, divide every polynomial coefficient by alpha, independent of its degree, to preserve L(g(u)). For h=(1,2), u=(1,2,-1), g(v)=v+v² and scale 3, the two filtered-power columns are (3,12,9) and (3,18,27); coefficients (1/3,1/3) reproduce outputs (2,10,12). These are exact deterministic curator calculations and do not uniquely determine the physical block gains or establish finite-sample estimation performance. Locators: Section 2, coefficient relation following Equation 15 and Equations 16–17, PDF pp. 8–9 / printed pp. 6–7; curator exact calculations in research/discovery/correlation-identification-boundaries.py

### gain-and-variant-boundaries

evidence: supported. Targets: AIMech:CorrelationBasedHammersteinIdentification.

Mechanism or boundary is supported within its stated scope.

Even with u_t=1+x_t for iid standard Gaussian x, g(u)=u³-6u has zero centered input/output cross-correlation through a nonzero LTI block: the polynomial contributions cancel. The source’s nonzero-mean recommendation therefore needs a nonzero-gain check. Its separate parallel-feedforward extension uses squared-input correlation, whose gain can also vanish, and generally identifies the combined linear branch h1+omega1*h2 rather than both original paths. Those extra steps are not part of this two-stage Hammerstein algorithm. Locators: Section 2, Equations 12–13, PDF p. 7 / printed p. 5; Section 3, Equations 20–32, PDF pp. 11–15 / printed pp. 9–13; Conclusions, PDF p. 17 / printed p. 15; curator exact calculations in research/discovery/correlation-identification-boundaries.py

### Nonzero mean is not a nonzero-gain guarantee

consistency: supported. Targets: AIMech:CorrelationBasedWienerIdentification, AIMech:CorrelationBasedHammersteinIdentification.

Exact counterexamples are preserved as curator qualifications.

For iid N(1,1) input and h=(1,2), Wiener q has mean 3 and variance 5; g(q)=q³−42q has zero first cross-moments. Hammerstein g(u)=u³−6u likewise has zero first cross-moments. A zero-DC-gain Wiener block with an even output nonlinearity gives another cancellation. These are exact population statements in a finite discrete model, not empirical estimates or an impossibility theorem for all estimators.

### Centered correlation versus raw-output regression

consistency: supported. Targets: AIMech:CorrelationBasedWienerIdentification, AIMech:CorrelationBasedHammersteinIdentification.

Noise-offset qualifications prevent an unsupported unbiasedness claim.

Independent noise has zero correlation with centered input even at nonzero noise mean. It need not have zero moment with squared centered input before noise centering. With u~N(1,1), z=u+n and independent E[n]=2, the population through-origin least-squares slope is 2 instead of the true 1, while centered first correlation remains 1. Records require zero-mean noise or separately justified offset treatment for coefficient interpretation and do not claim finite-sample unbiasedness with estimated regressors.

### Finite moments and practical white excitation

scope: supported. Targets: AIMech:CorrelationBasedWienerIdentification, AIMech:CorrelationBasedHammersteinIdentification.

Ideal continuous-white formulas are qualified.

The Hammerstein report explicitly distinguishes finite practical input variance from ideal infinite pointwise variance. Its impulse approximation requires bandwidth conditions, not arbitrary colored excitation. For Wiener, finite filtered Gaussian variance requires more than an unqualified BIBO statement in the ideal continuous-white setting. Both records distinguish these approximations from exact discrete iid curator examples and retain chosen-order, transient and conditioning limits.

### Parallel feedforward method is separate

scope: supported. Targets: AIMech:CorrelationBasedWienerIdentification, AIMech:CorrelationBasedHammersteinIdentification.

Do not infer unique original branch decomposition.

The fully read extension uses squared-input correlation and a second possibly vanishing gain, then recovers the combined linear path h1+omega1*h2. The source example sets omega1=0. Those additional steps are not silently included in the two-stage Hammerstein record; a separate frontier candidate retains the original-source and identity work.

### Complete fields, evidence versions and report mirrors

provenance: supported. Targets: AIMech:CorrelationBasedWienerIdentification, AIMech:CorrelationBasedHammersteinIdentification.

All maintained fields and mirrors inspected.

Read both stable IDs and descriptive names, absent aliases, algorithm kinds, definitions and locators, eight claims, all source metadata and hashes, four related mappings and pin, six limitations per record, DRAFT status and actual curation times. Technical-report full text is distinguished from later final journal metadata. No empirical replication, independent approval, priority or upstream acceptance is asserted.

## Findings

### comparative-citations: Cite both primary reports for cascade design comparisons

minor / resolved / confirmed; issue key: aimech-correlation-cascade-comparative-design-citations.

The Wiener powers-of-filtered-input claim and Hammerstein filtered-input-powers claim each contrast the two estimator designs, but each record lists and cites only its own primary report. The opposite design is supported by the other fully read report, which is presently traceable only through the discovery context. Add that report as an evidence source and a precise second citation to each comparative claim. This is a bounded claim-traceability defect; the combined inspected evidence supports the mechanisms.

Disposition: Both records now list both inspected primary reports and cite the counterpart report’s exact design equations on the comparative claim. Source hashes/access metadata are preserved, report mirrors and actual edit history are updated, and pages are regenerated. Definitions, eight claim statements and mappings are unchanged; both targets were reassessed.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:CorrelationBasedWienerIdentification, AIMech:CorrelationBasedHammersteinIdentification. Both are observed-input two-stage estimators, but their second-stage operations and degree-dependent versus common gain reparameterizations differ. Shared least-squares fitting and linear special cases do not establish algorithm equivalence.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261012T141214Z-correlation-cascade-identification.json | supports | Compared all 442 pinned AIO IDs, names and scoped synonyms and 534 native IDs, names and aliases with both proposed estimator names, expanded two-stage/correlation names and related Bussgang/linear-approximation terms: no normalized identity match. Ignored- and hidden-inclusive full-text searches of the accessible recovery worktree and readable earlier worktree returned 81 and 68 lines. All distinct matched text was read; it concerns pending Bussgang blind-deconvolution leads and prior cascade-model source context. Blind deconvolution with unknown input is not these observed-input estimators. Original Documents untracked files remain inaccessible and are not claimed re-audited. Read all 36 semantic AIO rows, 58 native name/definition neighbors, eight complete annotated AIO CLASS nodes with incident edges, eight contextual generated YAMLs and six complete native neighbors. Wiener/Hammerstein records denote models, RPE/PLR denote recursive updates, forward OLS selects candidate structure, and the iterated Wiener filter estimates an image under a fixed prior. These are distinct mechanisms. AIO linear/least-squares regression supplies component fitting context, not the ordered two-stage estimator identity. DCC models changing covariances, GLM specifies a statistical link, ARDL specifies lagged model structure, and a convolutional layer is a neural component. No exact mapping is justified. These local descriptive method names do not claim original nomenclature or priority. |
| mapping | sources/aio/aio.json | supports | Read all 36 semantic AIO rows, 58 native name/definition neighbors, eight complete annotated CLASS nodes with incident edges, eight generated YAMLs and six complete native neighbors. Four related mappings to LeastsquaresAnalysis and TimeSeriesAnalysis preserve algorithm/component and algorithm/task distinctions. |
| calculations | research/discovery/correlation-identification-boundaries.py | supports | Exact Gaussian moments verify distinct nonzero gains and nonzero-mean cancellation examples for both orders. Separate finite zero-state calculations verify powers of a filtered input versus filtered input powers, different coefficient rescaling and full two-column rank. Independent nonzero-mean noise examples show why centered correlation and raw-output no-intercept regression need different offset treatment. These are curator derivations, not empirical estimation results. |
| wiener | https://eprints.whiterose.ac.uk/id/eprint/75410/1/report%2060%20%282%29.pdf; Billings, S. A. and Fakhouri, S. Y. (1977), Identification of Non-Linear Systems Using the Wiener Model, ACSE Report 60, July 1977 | supports | All 13 PDF pages read. After initial category capture, reread PDF 6–9, printed 3–6: Gaussian correlations, scaled pulse-response fit, powers of the reconstructed signal, degree-dependent coefficient scale, rank and conclusion limits. After successor capture, reread Wiener PDF 7–8 and Hammerstein PDF 8–9 to verify both added comparative citations; the remaining primary evidence is unchanged. |
| hammerstein | https://eprints.whiterose.ac.uk/id/eprint/75422/2/report%2068.pdf; Billings, S. A. and Fakhouri, S. Y. (1978), Nonlinear System Identification using the Hammerstein Model, ACSE Report 68, February 1978 | supports | All 26 PDF pages read. After initial category capture, reread PDF 6–9 and 11–15, printed 4–7 and 9–13: practical white excitation, filtered input powers, common coefficient scale, parallel extension and aggregate-path ambiguity. After successor capture, reread Wiener PDF 7–8 and Hammerstein PDF 8–9 to verify both added comparative citations; the remaining primary evidence is unchanged. |
| prior | reviews/structured/20261012T141620Z-correlation-cascade-open/review.yaml | supports | Initial immutable review retained both algorithms and requested complete claim-level citations for their comparison. |

## Limits And Additional Notes

- Author self-review only; both records remain DRAFT.
- Two native DRAFT algorithm records added: 536 curated and 442 unchanged generated records. Discovery remains active with 471 pending and 50 partly addressed cohorts plus other unresolved scopes.
- All 39 pages of ACSE60 and ACSE68 visually read. The 42-page ACSE131 report was unread at discovery-report creation; subsequent partial reading belongs to the next discovery cohort, not this review. Later final journal versions are metadata/abstract context only.
- Observed-input, real SISO polynomial cascades with independent additive output noise. Continuous practical-white approximations and exact discrete iid Gaussian curator examples are distinguished. Nonzero correlation gain, finite moments, full design rank and noise-offset treatment are explicit; no general identifiability or convergence guarantee.
- No empirical replication, model training or paid provider. Original Documents checkout synchronization and old local branch cleanup still require restored OS access.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T142331Z-correlation-cascade-resolved
kind: category
repository: CultureBotAI/AIMech
title: Scientific author self-review of correlation-based cascade identification
started_at: '2026-10-12T14:17:29Z'
finished_at: '2026-10-12T14:23:31Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent read both primary reports, inspected every
    field and challenged gain cancellation, design order, scaling, noise offsets and
    continuous-white assumptions. This is adversarial author self-review, not independent
    approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain both algorithms and related mappings; comparative citation finding
  is resolved.
source:
  git_revision: 587cfc9f78766b2c1b49ee00175b3bcf7f763ade
  state: working_tree
  inputs:
  - path: data/aio/AutoregressiveDistributedLag.yaml
    sha256: ec96eff60d187277db7e53193e2a91671c047127c75a493ff764bb362521458e
    role: context
  - path: data/aio/ConvolutionalLayer.yaml
    sha256: 3b87e9fe798141deee846b353fa6d8530c637135eeb7e9eb4fa9f6597d7a25fd
    role: context
  - path: data/aio/DynamicConditionalCorrelation.yaml
    sha256: 5cf6959d2e27d395fdc956473bf305fcaf9f5d99ad0a855477b49c609a7ed43b
    role: context
  - path: data/aio/GeneralizedLinearModel.yaml
    sha256: 202002ec50c6e6207bc2fefba5baeab233514fd8f9118a623d1917b599ce2c7d
    role: context
  - path: data/aio/LeastsquaresAnalysis.yaml
    sha256: 666926bd17035ea825f0f521620b9c5538ff2a8695e7d37f96ab3b0cc8aa1d3c
    role: context
  - path: data/aio/LinearRegression.yaml
    sha256: 9b6f1b2ea06d9a47e5f7cf94c66afeaa6d40c3e7d0fdb5037d2c25fabc6d8167
    role: context
  - path: data/aio/RegressionAnalysis.yaml
    sha256: 6f5d48096556a2ec31770aab306219e9020919940b4e80554639cc97aaa94bc6
    role: context
  - path: data/aio/TimeSeriesAnalysis.yaml
    sha256: c26b267d0f5fb895e9cb0eb587fe86a115d461dae4d70e0ac6baf1eefb1d4eff
    role: context
  - path: data/curated/CorrelationBasedHammersteinIdentification.yaml
    sha256: 2d0a8d5cfb94238255a86d8f96ff3a40853c8fa92c39b3fd131ad276f41cd5e3
    role: target
  - path: data/curated/CorrelationBasedWienerIdentification.yaml
    sha256: 42cb617ee6ecaae592441a4811cc31857ce6d6ea5d47d6327e9fbced01b5483d
    role: target
  - path: data/curated/HammersteinModel.yaml
    sha256: 03e25ac3b355174c7011e2aec536286009102d3dac75be07ac041025861db56b
    role: context
  - path: data/curated/IteratedWienerFilter.yaml
    sha256: 803905a00467ecfc963cbd5a24f5616013484c0d0ce57d205c386868346addac
    role: context
  - path: data/curated/OrthogonalLeastSquaresForwardSelection.yaml
    sha256: 909a5791745c4970ecf2897f8000df528a5d20275e64765b61165d2e73a63931
    role: context
  - path: data/curated/PseudoLinearRegressionEstimation.yaml
    sha256: 70f7a23a68a1248b2aaf11252bdaffb5e72c61d805eed6e7099ec2d4ddeaaffc
    role: context
  - path: data/curated/RecursivePredictionErrorEstimation.yaml
    sha256: fc2d56ffe0222a82d32752e278ea48db32b67c9e818377a37eff2c383d26be47
    role: context
  - path: data/curated/WienerModel.yaml
    sha256: 3e327ccc2366267909e7c0bf3e31156a1b1461ffa5a2d8f79fc9a764555c5b01
    role: context
  - path: research/discovery/20261012T141214Z-correlation-cascade-identification.json
    sha256: 155ad7b4cd774895c0162fddeb8c095f88946fee6b4b3559640c0c8c140d4ff2
    role: context
  - path: research/discovery/correlation-identification-boundaries.py
    sha256: 136ff694b1c291108e8b9df293a73c2ec386ed631072fda6352f23d0bc1de6f6
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
- target_id: AIMech:CorrelationBasedWienerIdentification
  path: data/curated/CorrelationBasedWienerIdentification.yaml
  label: Correlation-based Wiener identification
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CorrelationBasedWienerIdentification.yaml
    role: maintained
- target_id: AIMech:CorrelationBasedHammersteinIdentification
  path: data/curated/CorrelationBasedHammersteinIdentification.yaml
  label: Correlation-based Hammerstein identification
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CorrelationBasedHammersteinIdentification.yaml
    role: maintained
scope:
  description: All fields of the exact two-record correlation-based Wiener/Hammerstein
    identification cohort.
  selection: 'Exact IDs: AIMech:CorrelationBasedWienerIdentification, AIMech:CorrelationBasedHammersteinIdentification'
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - AIMech:CorrelationBasedWienerIdentification
  - AIMech:CorrelationBasedHammersteinIdentification
  exclusions:
  - target: Parallel, feedback, colored-input, multivariable and newer estimator variants
    reason: Separate pending identity and primary-source audits.
  - target: Contextual ontology and neighboring records
    reason: Identity/mapping context, not full scientific review.
  - target: Empirical reproduction or implementation audit
    reason: Only exact finite curator calculations were executed.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:CorrelationBasedWienerIdentification
  - AIMech:CorrelationBasedHammersteinIdentification
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 98.54s (0:01:38)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 536 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 183 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 181,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:CorrelationBasedWienerIdentification
  - AIMech:CorrelationBasedHammersteinIdentification
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
  - AIMech:CorrelationBasedWienerIdentification
  - AIMech:CorrelationBasedHammersteinIdentification
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
  - AIMech:CorrelationBasedWienerIdentification
  - AIMech:CorrelationBasedHammersteinIdentification
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculations
  name: Exact Gaussian and finite-design boundary examples
  command: python3 research/discovery/correlation-identification-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:CorrelationBasedWienerIdentification
  - AIMech:CorrelationBasedHammersteinIdentification
  exit_code: 0
  expected_exit_code: 0
  summary: '{"wiener_square_cross": ["6", "12"], "hammerstein_square_cross": ["2",
    "4"], "wiener_nonzero_mean_cancellation": ["0", "0"], "hammerstein_nonzero_mean_cancellation":
    ["0", "0"], "wiener_zero_dc_cross": ["0", "0"], "wiener_scaled_design": [["7",
    "49"], ["28", "784"], ["21", "441"]], "hammerstein_scaled_design": [["3", "3"],
    ["12", "18"], ["9", "27"]], "wiener_scaled_coefficients": ["1/7", "1/49"], "hammerstein_scaled_coefficients":
    ["1/3", "1/3"], "wiener_reconstructed_output": ["2", "20", "12"], "hammerstein_reconstructed_output":
    ["2", "10", "12"], "independent_uncentered_noise_second_moment": "2", "uncentered_noise_through_origin_slope":
    "2"}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261012T141214Z-correlation-cascade-identification.json
  accessed_at: '2026-10-12T14:17:29Z'
  support: supports
  summary: 'Compared all 442 pinned AIO IDs, names and scoped synonyms and 534 native
    IDs, names and aliases with both proposed estimator names, expanded two-stage/correlation
    names and related Bussgang/linear-approximation terms: no normalized identity
    match. Ignored- and hidden-inclusive full-text searches of the accessible recovery
    worktree and readable earlier worktree returned 81 and 68 lines. All distinct
    matched text was read; it concerns pending Bussgang blind-deconvolution leads
    and prior cascade-model source context. Blind deconvolution with unknown input
    is not these observed-input estimators. Original Documents untracked files remain
    inaccessible and are not claimed re-audited. Read all 36 semantic AIO rows, 58
    native name/definition neighbors, eight complete annotated AIO CLASS nodes with
    incident edges, eight contextual generated YAMLs and six complete native neighbors.
    Wiener/Hammerstein records denote models, RPE/PLR denote recursive updates, forward
    OLS selects candidate structure, and the iterated Wiener filter estimates an image
    under a fixed prior. These are distinct mechanisms. AIO linear/least-squares regression
    supplies component fitting context, not the ordered two-stage estimator identity.
    DCC models changing covariances, GLM specifies a statistical link, ARDL specifies
    lagged model structure, and a convolutional layer is a neural component. No exact
    mapping is justified. These local descriptive method names do not claim original
    nomenclature or priority.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. The original Documents checkout cannot be read because
    of OS permissions, so its untracked files are not claimed re-audited in this round.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-12T14:17:29Z'
  support: supports
  summary: Read all 36 semantic AIO rows, 58 native name/definition neighbors, eight
    complete annotated CLASS nodes with incident edges, eight generated YAMLs and
    six complete native neighbors. Four related mappings to LeastsquaresAnalysis and
    TimeSeriesAnalysis preserve algorithm/component and algorithm/task distinctions.
- evidence_id: calculations
  kind: record_content
  reference: research/discovery/correlation-identification-boundaries.py
  accessed_at: '2026-10-12T14:17:29Z'
  snapshot_sha256: 136ff694b1c291108e8b9df293a73c2ec386ed631072fda6352f23d0bc1de6f6
  support: supports
  summary: Exact Gaussian moments verify distinct nonzero gains and nonzero-mean cancellation
    examples for both orders. Separate finite zero-state calculations verify powers
    of a filtered input versus filtered input powers, different coefficient rescaling
    and full two-column rank. Independent nonzero-mean noise examples show why centered
    correlation and raw-output no-intercept regression need different offset treatment.
    These are curator derivations, not empirical estimation results.
- evidence_id: wiener
  kind: primary_source
  reference: https://eprints.whiterose.ac.uk/id/eprint/75410/1/report%2060%20%282%29.pdf
  locator: Billings, S. A. and Fakhouri, S. Y. (1977), Identification of Non-Linear
    Systems Using the Wiener Model, ACSE Report 60, July 1977
  accessed_at: '2026-10-12T13:47:28Z'
  snapshot_sha256: 4520676002d287a1b2da5a1af6023d1ba8071797280b12835b2a1f782ad0b441
  support: supports
  summary: 'All 13 PDF pages read. After initial category capture, reread PDF 6–9,
    printed 3–6: Gaussian correlations, scaled pulse-response fit, powers of the reconstructed
    signal, degree-dependent coefficient scale, rank and conclusion limits. After
    successor capture, reread Wiener PDF 7–8 and Hammerstein PDF 8–9 to verify both
    added comparative citations; the remaining primary evidence is unchanged.'
- evidence_id: hammerstein
  kind: primary_source
  reference: https://eprints.whiterose.ac.uk/id/eprint/75422/2/report%2068.pdf
  locator: Billings, S. A. and Fakhouri, S. Y. (1978), Nonlinear System Identification
    using the Hammerstein Model, ACSE Report 68, February 1978
  accessed_at: '2026-10-12T13:47:24Z'
  snapshot_sha256: 6d50fec13e5904cd417d198d05a787ed55d80f3652f790d90ab4fd545d527590
  support: supports
  summary: 'All 26 PDF pages read. After initial category capture, reread PDF 6–9
    and 11–15, printed 4–7 and 9–13: practical white excitation, filtered input powers,
    common coefficient scale, parallel extension and aggregate-path ambiguity. After
    successor capture, reread Wiener PDF 7–8 and Hammerstein PDF 8–9 to verify both
    added comparative citations; the remaining primary evidence is unchanged.'
- evidence_id: prior
  kind: prior_review
  reference: reviews/structured/20261012T141620Z-correlation-cascade-open/review.yaml
  accessed_at: '2026-10-12T14:17:29Z'
  support: supports
  summary: Initial immutable review retained both algorithms and requested complete
    claim-level citations for their comparison.
assessments:
- assessment_id: identity
  area: identity
  topic: Distinct observed-input two-stage cascade estimators
  outcome: supported
  target_ids:
  - AIMech:CorrelationBasedWienerIdentification
  - AIMech:CorrelationBasedHammersteinIdentification
  evidence_ids:
  - identity
  - wiener
  - hammerstein
  - calculations
  summary: Retain the two algorithm identities.
  details: 'The first stages use related Gaussian correlation separation, but the
    second stages do not commute: Wiener takes powers after linear filtering, whereas
    Hammerstein filters each input power. Internal gain consequently rescales degree
    j by beta^j versus a common alpha. These are not the existing cascade model families,
    recursive prediction-error or pseudo-linear updates, structure selection, image
    Wiener filtering, or unknown-input blind deconvolution. The local names do not
    claim priority or original terminology.'
- assessment_id: comparative-citations
  area: evidence
  topic: Claim-level support for the opposite estimator design
  outcome: supported
  target_ids:
  - AIMech:CorrelationBasedWienerIdentification
  - AIMech:CorrelationBasedHammersteinIdentification
  evidence_ids:
  - wiener
  - hammerstein
  summary: Both comparative claims now cite the two supporting primary passages.
  details: Both design-matrix claims explicitly contrast Wiener and Hammerstein ordering.
    Their own report supports the local procedure, but the opposite ordering is supported
    by the other fully inspected report. Include both evidence-source identities and
    both precise claim citations so each maintained record is independently traceable.
    The mechanism itself is supported by the combined inspected evidence.
- assessment_id: mapping
  area: grounding
  topic: Algorithm, component fitting and analysis task
  outcome: supported
  target_ids:
  - AIMech:CorrelationBasedWienerIdentification
  - AIMech:CorrelationBasedHammersteinIdentification
  evidence_ids:
  - mapping
  - identity
  summary: Related mappings are supported curator assessments.
  details: Both stages use residual-squared parameter fitting after the source’s correlation-based
    separation. The pinned target describes a general fitting analysis, whereas this
    record specifies an ordered identification procedure with excitation and block-structure
    assumptions. A related mapping reflects its component mechanism without claiming
    exact identity or an asserted subclass. The procedure estimates nonlinear dynamical
    structure from temporal input/output observations and lagged correlations. The
    pinned target is the analysis task; related mapping preserves the algorithm/task
    distinction. Both stages use residual-squared parameter fitting after the source’s
    correlation-based separation. The pinned target describes a general fitting analysis,
    whereas this record specifies an ordered identification procedure with excitation
    and block-structure assumptions. A related mapping reflects its component mechanism
    without claiming exact identity or an asserted subclass. The procedure estimates
    nonlinear dynamical structure from temporal input/output observations and lagged
    correlations. The pinned target is the analysis task; related mapping preserves
    the algorithm/task distinction.
- assessment_id: r0-correlation-separation
  area: evidence
  topic: correlation-separation
  outcome: supported
  target_ids:
  - AIMech:CorrelationBasedWienerIdentification
  evidence_ids:
  - wiener
  - hammerstein
  - calculations
  summary: Mechanism or boundary is supported within its stated scope.
  details: 'The first stage correlates measured output with the centered Gaussian
    input fluctuation, while the actual excitation can include a constant mean. Under
    the source’s white-Gaussian and independent-output-noise assumptions, the population
    correlation has form beta*h at unit input spectral normalization, where h is the
    LTI impulse response and beta depends on the polynomial and excitation moments.
    A sampled rational transfer function is fitted to that scaled response. Recovering
    its shape requires beta != 0 and a meaningful finite-moment linear response; BIBO
    stability alone is not a substitute for finite filtered variance in an ideal continuous-white
    formulation. Locators: Equations 2–12, PDF pp. 5–7 / printed pp. 2–4; finite-moment
    and nonzero-gain conditions are curator qualifications of the displayed factorization'
- assessment_id: r0-powers-of-filtered-input
  area: evidence
  topic: powers-of-filtered-input
  outcome: supported
  target_ids:
  - AIMech:CorrelationBasedWienerIdentification
  evidence_ids:
  - wiener
  - hammerstein
  - calculations
  summary: Mechanism or boundary is supported within its stated scope.
  details: 'Apply the estimated scaled linear dynamics to the measured input, including
    its mean, to reconstruct qhat. For a chosen degree k, form columns qhat^j, j=1,...,k,
    and least-squares fit measured output. The displayed Gram inverse requires full
    column rank; practical solves need numerical conditioning. This uses powers of
    a filtered input, whereas Hammerstein identification filters the individual input
    powers. Polynomial degree, linear order and transient handling remain supplied
    choices. Locators: Equations 12–17, PDF pp. 7–8 / printed pp. 4–5; Figure 1, PDF
    p. 12; Section 2, Equations 15–17, PDF pp. 8–9 / printed pp. 6–7: Hammerstein
    filtered-input-power design'
- assessment_id: r0-scale-reparameterization
  area: evidence
  topic: scale-reparameterization
  outcome: supported
  target_ids:
  - AIMech:CorrelationBasedWienerIdentification
  evidence_ids:
  - wiener
  - hammerstein
  - calculations
  summary: Mechanism or boundary is supported within its stated scope.
  details: 'If the first stage recovers beta*L, the reconstructed internal variable
    is beta*q, so the polynomial coefficient of degree j becomes gamma_j/beta^j. The
    composite response can be recovered without determining the original block gains.
    In a separate exact zero-state example with h=(1,2), u=(1,2,-1), g(v)=v+v² and
    scale 7, the reconstructed signal is (7,28,21), and coefficients (1/7,1/49) give
    outputs (2,20,12). This verifies the reparameterization, not a stochastic estimator’s
    accuracy. Locators: Equations 13–17 and coefficient relation following Equation
    15, PDF pp. 7–8 / printed pp. 4–5; curator exact calculations in research/discovery/correlation-identification-boundaries.py'
- assessment_id: r0-nonzero-mean-cancellation
  area: evidence
  topic: nonzero-mean-cancellation
  outcome: supported
  target_ids:
  - AIMech:CorrelationBasedWienerIdentification
  evidence_ids:
  - wiener
  - hammerstein
  - calculations
  summary: Mechanism or boundary is supported within its stated scope.
  details: 'A nonzero input mean does not guarantee an informative first correlation.
    In the discrete iid unit-variance Gaussian example u_t=1+x_t, h=(1,2), q has mean
    3 and variance 5. For g(q)=q³-42q, Gaussian moments give E[g(q_t)*x_t]=E[g(q_t)*x_(t-1)]=0
    although g is nonconstant. An even nonlinearity with a zero-DC-gain linear block
    can also defeat an input mean shift. These curator examples qualify the source
    conclusion; they do not prove that all identification methods fail. Locators:
    Equations 6–11, PDF pp. 6–7 / printed pp. 3–4; Conclusions, PDF p. 9 / printed
    p. 6; curator exact Gaussian-moment calculations in research/discovery/correlation-identification-boundaries.py'
- assessment_id: r1-correlation-separation
  area: evidence
  topic: correlation-separation
  outcome: supported
  target_ids:
  - AIMech:CorrelationBasedHammersteinIdentification
  evidence_ids:
  - wiener
  - hammerstein
  - calculations
  summary: Mechanism or boundary is supported within its stated scope.
  details: 'The first stage correlates centered output with the centered Gaussian
    input fluctuation of excitation u=b+x. Under the source’s independent-output-noise
    and sufficiently white practical-excitation assumptions, the result approximates
    alpha*h, with alpha=mu*[gamma1+2*b*gamma2+3*gamma3*(variance(x)+b²)+...] and mu
    the input autocorrelation area. The report explicitly distinguishes finite practical
    variance from ideal continuous-white variance. For discrete iid unit-variance
    Gaussian inputs the corresponding factorization is exact at the population level.
    A nonzero alpha and appropriate moment/linear-response conditions are needed for
    recovery. Locators: Section 2, Equations 3–14, PDF pp. 5–8 / printed pp. 3–6;
    the discrete iid statement is a direct curator Gaussian-moment consequence of
    these equations'
- assessment_id: r1-filtered-input-powers
  area: evidence
  topic: filtered-input-powers
  outcome: supported
  target_ids:
  - AIMech:CorrelationBasedHammersteinIdentification
  evidence_ids:
  - wiener
  - hammerstein
  - calculations
  summary: Mechanism or boundary is supported within its stated scope.
  details: 'After estimating the scaled linear response, build a design column for
    each degree j by filtering u^j through that response. Least-squares fit measured
    output on these columns. The input u includes the applied mean; x denotes the
    centered fluctuation only in the correlation stage. The displayed inverse requires
    full column rank. This differs from raising a filtered input to successive powers
    as in Wiener identification, and it does not select the polynomial degree or linear
    order automatically. Locators: Section 2, Equations 14–17, PDF pp. 8–9 / printed
    pp. 6–7; Figure 2, PDF p. 22; Equations 13–17, PDF pp. 7–8 / printed pp. 4–5:
    Wiener powers-of-filtered-input design'
- assessment_id: r1-scale-reparameterization
  area: evidence
  topic: scale-reparameterization
  outcome: supported
  target_ids:
  - AIMech:CorrelationBasedHammersteinIdentification
  evidence_ids:
  - wiener
  - hammerstein
  - calculations
  summary: Mechanism or boundary is supported within its stated scope.
  details: 'If the first stage recovers alpha*L, divide every polynomial coefficient
    by alpha, independent of its degree, to preserve L(g(u)). For h=(1,2), u=(1,2,-1),
    g(v)=v+v² and scale 3, the two filtered-power columns are (3,12,9) and (3,18,27);
    coefficients (1/3,1/3) reproduce outputs (2,10,12). These are exact deterministic
    curator calculations and do not uniquely determine the physical block gains or
    establish finite-sample estimation performance. Locators: Section 2, coefficient
    relation following Equation 15 and Equations 16–17, PDF pp. 8–9 / printed pp.
    6–7; curator exact calculations in research/discovery/correlation-identification-boundaries.py'
- assessment_id: r1-gain-and-variant-boundaries
  area: evidence
  topic: gain-and-variant-boundaries
  outcome: supported
  target_ids:
  - AIMech:CorrelationBasedHammersteinIdentification
  evidence_ids:
  - wiener
  - hammerstein
  - calculations
  summary: Mechanism or boundary is supported within its stated scope.
  details: 'Even with u_t=1+x_t for iid standard Gaussian x, g(u)=u³-6u has zero centered
    input/output cross-correlation through a nonzero LTI block: the polynomial contributions
    cancel. The source’s nonzero-mean recommendation therefore needs a nonzero-gain
    check. Its separate parallel-feedforward extension uses squared-input correlation,
    whose gain can also vanish, and generally identifies the combined linear branch
    h1+omega1*h2 rather than both original paths. Those extra steps are not part of
    this two-stage Hammerstein algorithm. Locators: Section 2, Equations 12–13, PDF
    p. 7 / printed p. 5; Section 3, Equations 20–32, PDF pp. 11–15 / printed pp. 9–13;
    Conclusions, PDF p. 17 / printed p. 15; curator exact calculations in research/discovery/correlation-identification-boundaries.py'
- assessment_id: adversarial-gain
  area: consistency
  topic: Nonzero mean is not a nonzero-gain guarantee
  outcome: supported
  target_ids:
  - AIMech:CorrelationBasedWienerIdentification
  - AIMech:CorrelationBasedHammersteinIdentification
  evidence_ids:
  - wiener
  - hammerstein
  - calculations
  summary: Exact counterexamples are preserved as curator qualifications.
  details: For iid N(1,1) input and h=(1,2), Wiener q has mean 3 and variance 5; g(q)=q³−42q
    has zero first cross-moments. Hammerstein g(u)=u³−6u likewise has zero first cross-moments.
    A zero-DC-gain Wiener block with an even output nonlinearity gives another cancellation.
    These are exact population statements in a finite discrete model, not empirical
    estimates or an impossibility theorem for all estimators.
- assessment_id: adversarial-noise
  area: consistency
  topic: Centered correlation versus raw-output regression
  outcome: supported
  target_ids:
  - AIMech:CorrelationBasedWienerIdentification
  - AIMech:CorrelationBasedHammersteinIdentification
  evidence_ids:
  - hammerstein
  - wiener
  - calculations
  summary: Noise-offset qualifications prevent an unsupported unbiasedness claim.
  details: Independent noise has zero correlation with centered input even at nonzero
    noise mean. It need not have zero moment with squared centered input before noise
    centering. With u~N(1,1), z=u+n and independent E[n]=2, the population through-origin
    least-squares slope is 2 instead of the true 1, while centered first correlation
    remains 1. Records require zero-mean noise or separately justified offset treatment
    for coefficient interpretation and do not claim finite-sample unbiasedness with
    estimated regressors.
- assessment_id: adversarial-continuous
  area: scope
  topic: Finite moments and practical white excitation
  outcome: supported
  target_ids:
  - AIMech:CorrelationBasedWienerIdentification
  - AIMech:CorrelationBasedHammersteinIdentification
  evidence_ids:
  - wiener
  - hammerstein
  summary: Ideal continuous-white formulas are qualified.
  details: The Hammerstein report explicitly distinguishes finite practical input
    variance from ideal infinite pointwise variance. Its impulse approximation requires
    bandwidth conditions, not arbitrary colored excitation. For Wiener, finite filtered
    Gaussian variance requires more than an unqualified BIBO statement in the ideal
    continuous-white setting. Both records distinguish these approximations from exact
    discrete iid curator examples and retain chosen-order, transient and conditioning
    limits.
- assessment_id: adversarial-parallel
  area: scope
  topic: Parallel feedforward method is separate
  outcome: supported
  target_ids:
  - AIMech:CorrelationBasedWienerIdentification
  - AIMech:CorrelationBasedHammersteinIdentification
  evidence_ids:
  - hammerstein
  summary: Do not infer unique original branch decomposition.
  details: The fully read extension uses squared-input correlation and a second possibly
    vanishing gain, then recovers the combined linear path h1+omega1*h2. The source
    example sets omega1=0. Those additional steps are not silently included in the
    two-stage Hammerstein record; a separate frontier candidate retains the original-source
    and identity work.
- assessment_id: all-fields
  area: provenance
  topic: Complete fields, evidence versions and report mirrors
  outcome: supported
  target_ids:
  - AIMech:CorrelationBasedWienerIdentification
  - AIMech:CorrelationBasedHammersteinIdentification
  evidence_ids:
  - identity
  - mapping
  - wiener
  - hammerstein
  summary: All maintained fields and mirrors inspected.
  details: Read both stable IDs and descriptive names, absent aliases, algorithm kinds,
    definitions and locators, eight claims, all source metadata and hashes, four related
    mappings and pin, six limitations per record, DRAFT status and actual curation
    times. Technical-report full text is distinguished from later final journal metadata.
    No empirical replication, independent approval, priority or upstream acceptance
    is asserted.
findings:
- finding_id: comparative-citations
  issue_key: aimech-correlation-cascade-comparative-design-citations
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Cite both primary reports for cascade design comparisons
  description: The Wiener powers-of-filtered-input claim and Hammerstein filtered-input-powers
    claim each contrast the two estimator designs, but each record lists and cites
    only its own primary report. The opposite design is supported by the other fully
    read report, which is presently traceable only through the discovery context.
    Add that report as an evidence source and a precise second citation to each comparative
    claim. This is a bounded claim-traceability defect; the combined inspected evidence
    supports the mechanisms.
  target_ids:
  - AIMech:CorrelationBasedWienerIdentification
  - AIMech:CorrelationBasedHammersteinIdentification
  field_paths:
  - claims[1].evidence
  - evidence_sources
  evidence_ids:
  - prior
  - wiener
  - hammerstein
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CorrelationBasedWienerIdentification.yaml
    role: maintained
  - repository: CultureBotAI/AIMech
    path: data/curated/CorrelationBasedHammersteinIdentification.yaml
    role: maintained
  - repository: CultureBotAI/AIMech
    path: research/discovery/20261012T141214Z-correlation-cascade-identification.json
    role: discovery_report
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261012T141620Z-correlation-cascade-open
    finding_id: comparative-citations
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/192
  disposition_reason: Both records now list both inspected primary reports and cite
    the counterpart report’s exact design equations on the comparative claim. Source
    hashes/access metadata are preserved, report mirrors and actual edit history are
    updated, and pages are regenerated. Definitions, eight claim statements and mappings
    are unchanged; both targets were reassessed.
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:CorrelationBasedWienerIdentification
  - AIMech:CorrelationBasedHammersteinIdentification
  evidence_ids:
  - identity
  - wiener
  - hammerstein
  - calculations
  rationale: Both are observed-input two-stage estimators, but their second-stage
    operations and degree-dependent versus common gain reparameterizations differ.
    Shared least-squares fitting and linear special cases do not establish algorithm
    equivalence.
limitations:
- Author self-review only; both records remain DRAFT.
- 'Two native DRAFT algorithm records added: 536 curated and 442 unchanged generated
  records. Discovery remains active with 471 pending and 50 partly addressed cohorts
  plus other unresolved scopes.'
- All 39 pages of ACSE60 and ACSE68 visually read. The 42-page ACSE131 report was
  unread at discovery-report creation; subsequent partial reading belongs to the next
  discovery cohort, not this review. Later final journal versions are metadata/abstract
  context only.
- Observed-input, real SISO polynomial cascades with independent additive output noise.
  Continuous practical-white approximations and exact discrete iid Gaussian curator
  examples are distinguished. Nonzero correlation gain, finite moments, full design
  rank and noise-offset treatment are explicit; no general identifiability or convergence
  guarantee.
- No empirical replication, model training or paid provider. Original Documents checkout
  synchronization and old local branch cleanup still require restored OS access.
related_reviews:
- repository: CultureBotAI/AIMech
  review_id: 20261012T141620Z-correlation-cascade-open
  relationship: Successor resolves comparative claim traceability while retaining
    both targets.
links: []
tags:
- native-concepts
- system-identification
- self-review
- discovery-ongoing
```
