# Scientific author self-review of Gamma filter

- Review: 20261013T072202Z-gamma-filter
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-13T07:13:55Z
- Finished UTC: 2026-10-13T07:22:02Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Gamma filter as a distinct DRAFT linear adaptive model family with related LinearRegression mapping. Resolve the saved source-location finding after correcting three locators and one section attribution; recurrence, mathematical boundaries and limited experiments remain supported.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:GammaFilter
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 979c918cbf59603232be85a07bcec0fd0db95110.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:GammaFilter | data/curated/GammaFilter.yaml | maintained | Gamma filter |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:GammaFilter | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 226.75s (0:03:46)<br>Checked 442 record(s); 0 failed.<br>Checked 585 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 244 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 243,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:GammaFilter | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:GammaFilter | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:GammaFilter | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:GammaFilter | {"weight_gradient": ["4769/5000", "-2131599/2500000", "532629/1250000"], "memory_parameter_gradient": "6173769/5000000", "maximum_finite_difference_error": 7.29350000001023e-13, "two_stage_impulse": ["0", "0", "1/4", "1/4", "3/16", "1/8", "5/64", "3/64"], "second_moment_derivative_quadratic": "841269/2500000", "one_sided_crossmoment_quadratic": "841269/5000000", "parameter_count_for_K2": 4, "scope": "Fixed-parameter rational recurrence with independent zero initialization; direct input tap retained. Correct derivative of a second moment includes both transpose terms. No fitting, adaptive convergence test, author implementation or empirical performance claim."} |

## Scientific And Domain Assessments

### Gamma filter

identity: supported. Targets: AIMech:GammaFilter.

Retain this distinct DRAFT model_family.

The source independently names an adaptive linear Gamma filter and ADALINE(mu), with direct tap and linear trace combination. The broader Gamma neural architecture permits nonlinear mapping/coupling; generic ADALINE is only the mu1 configuration. Other inspected estimation and layer records are not exact synonyms.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:GammaFilter.

Mapping direction and scope are supported.

Fixed-mu fitting is linear least squares in trace features, supporting related_match to LinearRegression. The pinned regression-analysis task is not an exact filter-family identity or a supported broad is-a relation for joint adaptation.

### linear-filter-recurrence

evidence: supported. Targets: AIMech:GammaFilter.

Supported within the stated primary-source and mathematical scope.

Source Equations1–6 include the k0 direct tap. K+1 weights plus shared mu give K+2 scalars. Simultaneous old-state updates yield the stated transfer; fixed coefficient input linearity is separated from joint parameter nonlinearity.

### fixed-memory-stability

evidence: supported. Targets: AIMech:GammaFilter.

Supported within the stated primary-source and mathematical scope.

Pole1-mu gives strict0&lt;mu&lt;2 for the memory stages. Frozen initial states at0, possible alternating resonance at2, output cancellations and unconstrained adaptation all prevent overgeneralization. Corrected locator now names III.B.

### dispersive-memory

evidence: supported. Targets: AIMech:GammaFilter.

Supported within the stated primary-source and mathematical scope.

The negative-binomial-shaped impulse response has mean k/mu only as a positive normalized kernel in the stated interval. An alternative gamma-coordinate polynomial is not general ordinary-time FIR. Corrected locator includes III.A where Equation8 appears.

### block-and-online-adaptation

evidence: supported. Targets: AIMech:GammaFilter.

Supported within the stated primary-source and mathematical scope.

Half-squared-error sign and all K+1 tap derivatives agree with direct differentiation. Fixed-parameter alpha recurrence matches finite differences; source calls samplewise adaptation a local approximation. No arbitrary drifting-parameter exactness is claimed.

### normal-equations-and-nonconvexity

evidence: supported. Targets: AIMech:GammaFilter.

Supported within the stated primary-source and mathematical scope.

Fixed-mu normal equations need rank for unique weights. Direct dR includes the transpose cross-moment omitted in the printed equality; the constructed quadratic confirms the factor2. The record avoids asserting an author-code failure or a globally convex mu objective.

### system-identification-evidence

evidence: supported. Targets: AIMech:GammaFilter.

Supported within the stated primary-source and mathematical scope.

The source evaluates two third-order elliptic systems with selected mu and order settings. Corrected Figures4–5 provide experiments; Figure6 concerns the transform. The deferred applications are now accurately placed at the end of IV. No automatic mu-convergence benchmark is inferred.

### direct-tap indexing, strict fixed-stage stability, parameter drift and source-location accuracy

consistency: supported. Targets: AIMech:GammaFilter.

Constructed calculations support the stated distinctions.

A rational two-stage fixed-parameter filter checks all three tap derivatives and the shared memory-coefficient derivative against finite differences, verifies a short impulse-response sequence and demonstrates the missing-transpose factor in a one-sided second-moment derivative. No parameters are fitted and no empirical study is replicated.

### All maintained fields

provenance: supported. Targets: AIMech:GammaFilter.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all six claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Read the complete corrected maintained YAML and LinearRegression mapping after fresh capture. Visually reread primary pages2,6 after that capture to verify stability III.B, impulse-response III.A and experimental Figures4–5 with deferred applications in SectionIV. All8 pages were read before curation; pages2,4,6,7 were also reread during the initial review. Fixed direct-tap indexing, sensitivities and second-moment derivative were checked algebraically.

## Findings

### F1: Correct Gamma filter section and figure references

minor / resolved / confirmed; issue key: gamma-filter-principe1993-locators.

The stability locator names SectionIII.A, but stability is SectionIII.B. The impulse-response Equation8 is in SectionIII.A, outside the stated III.B–C span. The experimental locator names Figures4–6, but only Figures4–5 show the two identification studies; Figure6 is a transform illustration on printed p.655. The statement places deferred signal applications in Discussion, while that sentence is in SectionIV on printed p.654. Correct these source-location descriptions; the mathematical and experimental scope remains supported.

Disposition: Corrected stability to III.B, included III.A for impulse response, restricted experimental figures to4–5 and moved deferred-application attribution to SectionIV. Report mirror and EDIT history agree; fresh capture, corrected-record and source-page rereading and required gates pass.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261013T071125Z-gamma-filter.json | supports | Compared all 442 pinned AIO and 584 native IDs, names, aliases and scoped synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string searches of the recovery, older discovery and original Documents checkouts returned 5, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered 110 AIO and 251 native definitions, with unchanged preceding rows verified and new matches read. 4 full annotated AIO node/edge/generated contexts and 4 full native records were inspected. Matches point to the pending Gamma-filter lead and Gamma neural-model context. This source-defined linear adaptive filter has a direct input tap and a weighted sum of cascaded gamma-memory traces; the broader Gamma neural architecture allows nonlinear spatial maps and neural couplings. The independently named ADALINE(mu) filter is a narrower model family, not a renamed generic ADALINE or the entire Gamma neural family. LinearStateSpaceLayer concerns a layer based on discretized continuous state-space systems; PseudoLinearRegressionEstimation is an estimation method and IteratedWienerFilter is a particular iterative denoising procedure. None supplies this exact identity. Fixed-memory-coefficient fitting is linear in tap weights, while joint memory-coefficient adaptation is not linear in all parameters, motivating only a related LinearRegression mapping. |
| mapping | sources/aio/aio.json | supports | Fixed-mu fitting is linear least squares in trace features, supporting related_match to LinearRegression. The pinned regression-analysis task is not an exact filter-family identity or a supported broad is-a relation for joint adaptation. |
| principe1993 | https://www.cnel.ufl.edu/wp-content/uploads/courses/EEL6504/principe_gamma_1993.pdf; All8 primary journal pages read. After the correction and fresh capture, pages2,6 were reread; other primary pages were inspected earlier. No author code, empirical reproduction or adaptation-convergence experiment. | supports | IEEE Transactions on Signal Processing41(2):649–656, February1993, as printed in the complete eight-page primary PDF. Author institutional metadata lists1992; the primary printed issue determines the cited year. All pages, equations, figures, TableI and references read. |
| calculation | research/discovery/gamma-filter-boundaries.py | supports | A rational two-stage fixed-parameter filter checks all three tap derivatives and the shared memory-coefficient derivative against finite differences, verifies a short impulse-response sequence and demonstrates the missing-transpose factor in a one-sided second-moment derivative. No parameters are fitted and no empirical study is replicated. |
| predecessor | reviews/structured/20261013T071314Z-gamma-filter-locators-open/review.yaml | supports | Initial partial review preserves three incorrect locators and one section attribution; corrected against the primary PDF. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these are not independent gate runs.
- One new DRAFT concept, yielding 585 native and 442 unchanged generated records. The 769-entry main frontier retains 481 pending and 57 partly addressed cohorts, plus nested leads; discovery is incomplete.
- All eight journal pages649–656 visually read, including Equations1–35, Figures1–7, TableI, experiments, Discussion, references and author biographies. Printed issue is February1993; the inspected institutional metadata page lists1992, so use the primary printed1993 date. DOI10.1109/78.193206 was found in author institutional metadata; an earlier provisional search-key typo was corrected before curation. No author implementation or training.
- No author code, training, paid service, hardware measurement or empirical replication. Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization and old round141 cleanup remain pending explicit approval after automatic review rejection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T072202Z-gamma-filter
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Gamma filter
started_at: '2026-10-13T07:13:55Z'
finished_at: '2026-10-13T07:22:02Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged direct-tap indexing, strict fixed-stage
    stability, parameter drift and source-location accuracy. This is adversarial author
    self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Gamma filter as a distinct DRAFT linear adaptive model family with
  related LinearRegression mapping. Resolve the saved source-location finding after
  correcting three locators and one section attribution; recurrence, mathematical
  boundaries and limited experiments remain supported.
source:
  git_revision: 979c918cbf59603232be85a07bcec0fd0db95110
  state: working_tree
  inputs:
  - path: data/aio/Convolution1DLayer.yaml
    sha256: 4d7c7bef628e3b308ad22eb41f2959bb65e34edebfd9336c9d7c05dc9feb645c
    role: context
  - path: data/aio/LinearRegression.yaml
    sha256: 9b6f1b2ea06d9a47e5f7cf94c66afeaa6d40c3e7d0fdb5037d2c25fabc6d8167
    role: context
  - path: data/aio/Perceptron.yaml
    sha256: 6b1cc7cb96bfe03ed8720cca04490657976eea656fab6674d7ef685c34216915
    role: context
  - path: data/aio/RecurrentNeuralNetwork.yaml
    sha256: 1ebef94d2014e9a19d4bb3ed0fed6c5d77098a5a44e00e2cbd1cfe682dfcd892
    role: context
  - path: data/curated/GammaFilter.yaml
    sha256: 144855292b39113aa7d9bde1fc0939b4d9a51ef6b0799070c9cf0cfa29d163bd
    role: target
  - path: data/curated/GammaNeuralModel.yaml
    sha256: 496ce0a31262d619eac9d487ca2ed3e5971abbd28c9dce1688a5be50430a6fb5
    role: context
  - path: data/curated/IteratedWienerFilter.yaml
    sha256: 803905a00467ecfc963cbd5a24f5616013484c0d0ce57d205c386868346addac
    role: context
  - path: data/curated/LinearStateSpaceLayer.yaml
    sha256: 05d7d834a8c0db4c33613384cde4a250838290cce6960fda10e7209da318c151
    role: context
  - path: data/curated/PseudoLinearRegressionEstimation.yaml
    sha256: 70f7a23a68a1248b2aaf11252bdaffb5e72c61d805eed6e7099ec2d4ddeaaffc
    role: context
  - path: research/discovery/20261013T071125Z-gamma-filter.json
    sha256: bf4f3ad246e778a0d4c489df5a4f99f4a89d7f089fb727d22e6dd891dcd090e6
    role: context
  - path: research/discovery/gamma-filter-boundaries.py
    sha256: 3d655b6cc5590e0210cdb5b5c164306c1a1ab988430fdfd1276ff2ab4d93df74
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
- target_id: AIMech:GammaFilter
  path: data/curated/GammaFilter.yaml
  label: Gamma filter
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GammaFilter.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:GammaFilter'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:GammaFilter
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Other source versions and author implementation
    reason: All8 primary journal pages read. After the correction and fresh capture,
      pages2,6 were reread; other primary pages were inspected earlier. No author
      code, empirical reproduction or adaptation-convergence experiment.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:GammaFilter
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 226.75s (0:03:46)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 585 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 244 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 243,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:GammaFilter
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
  - AIMech:GammaFilter
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
  - AIMech:GammaFilter
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/gamma-filter-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:GammaFilter
  exit_code: 0
  expected_exit_code: 0
  summary: '{"weight_gradient": ["4769/5000", "-2131599/2500000", "532629/1250000"],
    "memory_parameter_gradient": "6173769/5000000", "maximum_finite_difference_error":
    7.29350000001023e-13, "two_stage_impulse": ["0", "0", "1/4", "1/4", "3/16", "1/8",
    "5/64", "3/64"], "second_moment_derivative_quadratic": "841269/2500000", "one_sided_crossmoment_quadratic":
    "841269/5000000", "parameter_count_for_K2": 4, "scope": "Fixed-parameter rational
    recurrence with independent zero initialization; direct input tap retained. Correct
    derivative of a second moment includes both transpose terms. No fitting, adaptive
    convergence test, author implementation or empirical performance claim."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261013T071125Z-gamma-filter.json
  accessed_at: '2026-10-13T07:13:55Z'
  support: supports
  summary: Compared all 442 pinned AIO and 584 native IDs, names, aliases and scoped
    synonyms; no normalized identity match. Ignored- and hidden-inclusive fixed-string
    searches of the recovery, older discovery and original Documents checkouts returned
    5, 0, 0 lines. All distinct match contents were inspected. Semantic matching covered
    110 AIO and 251 native definitions, with unchanged preceding rows verified and
    new matches read. 4 full annotated AIO node/edge/generated contexts and 4 full
    native records were inspected. Matches point to the pending Gamma-filter lead
    and Gamma neural-model context. This source-defined linear adaptive filter has
    a direct input tap and a weighted sum of cascaded gamma-memory traces; the broader
    Gamma neural architecture allows nonlinear spatial maps and neural couplings.
    The independently named ADALINE(mu) filter is a narrower model family, not a renamed
    generic ADALINE or the entire Gamma neural family. LinearStateSpaceLayer concerns
    a layer based on discretized continuous state-space systems; PseudoLinearRegressionEstimation
    is an estimation method and IteratedWienerFilter is a particular iterative denoising
    procedure. None supplies this exact identity. Fixed-memory-coefficient fitting
    is linear in tap weights, while joint memory-coefficient adaptation is not linear
    in all parameters, motivating only a related LinearRegression mapping.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-13T07:13:55Z'
  support: supports
  summary: Fixed-mu fitting is linear least squares in trace features, supporting
    related_match to LinearRegression. The pinned regression-analysis task is not
    an exact filter-family identity or a supported broad is-a relation for joint adaptation.
- evidence_id: principe1993
  kind: primary_source
  reference: https://www.cnel.ufl.edu/wp-content/uploads/courses/EEL6504/principe_gamma_1993.pdf
  locator: All8 primary journal pages read. After the correction and fresh capture,
    pages2,6 were reread; other primary pages were inspected earlier. No author code,
    empirical reproduction or adaptation-convergence experiment.
  accessed_at: '2026-10-13T06:52:29Z'
  snapshot_sha256: 0c4cf590b91e07237a9975c08a4e4f35a8c153fcc7acec965c7e9019f61d584a
  support: supports
  summary: IEEE Transactions on Signal Processing41(2):649–656, February1993, as printed
    in the complete eight-page primary PDF. Author institutional metadata lists1992;
    the primary printed issue determines the cited year. All pages, equations, figures,
    TableI and references read.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/gamma-filter-boundaries.py
  accessed_at: '2026-10-13T07:15:24Z'
  snapshot_sha256: 3d655b6cc5590e0210cdb5b5c164306c1a1ab988430fdfd1276ff2ab4d93df74
  support: supports
  summary: A rational two-stage fixed-parameter filter checks all three tap derivatives
    and the shared memory-coefficient derivative against finite differences, verifies
    a short impulse-response sequence and demonstrates the missing-transpose factor
    in a one-sided second-moment derivative. No parameters are fitted and no empirical
    study is replicated.
- evidence_id: predecessor
  kind: record_content
  reference: reviews/structured/20261013T071314Z-gamma-filter-locators-open/review.yaml
  accessed_at: '2026-10-13T07:15:24Z'
  snapshot_sha256: b10b6e87e1286b3a7b6c96082c40eb2a86ea0298f8b8bdf998f8f7ad80de15d6
  support: supports
  summary: Initial partial review preserves three incorrect locators and one section
    attribution; corrected against the primary PDF.
assessments:
- assessment_id: identity
  area: identity
  topic: Gamma filter
  outcome: supported
  target_ids:
  - AIMech:GammaFilter
  evidence_ids:
  - identity
  - principe1993
  summary: Retain this distinct DRAFT model_family.
  details: The source independently names an adaptive linear Gamma filter and ADALINE(mu),
    with direct tap and linear trace combination. The broader Gamma neural architecture
    permits nonlinear mapping/coupling; generic ADALINE is only the mu1 configuration.
    Other inspected estimation and layer records are not exact synonyms.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:GammaFilter
  evidence_ids:
  - mapping
  - principe1993
  summary: Mapping direction and scope are supported.
  details: Fixed-mu fitting is linear least squares in trace features, supporting
    related_match to LinearRegression. The pinned regression-analysis task is not
    an exact filter-family identity or a supported broad is-a relation for joint adaptation.
- assessment_id: linear-filter-recurrence
  area: evidence
  topic: linear-filter-recurrence
  outcome: supported
  target_ids:
  - AIMech:GammaFilter
  evidence_ids:
  - principe1993
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Source Equations1–6 include the k0 direct tap. K+1 weights plus shared
    mu give K+2 scalars. Simultaneous old-state updates yield the stated transfer;
    fixed coefficient input linearity is separated from joint parameter nonlinearity.
- assessment_id: fixed-memory-stability
  area: evidence
  topic: fixed-memory-stability
  outcome: supported
  target_ids:
  - AIMech:GammaFilter
  evidence_ids:
  - principe1993
  summary: Supported within the stated primary-source and mathematical scope.
  details: Pole1-mu gives strict0<mu<2 for the memory stages. Frozen initial states
    at0, possible alternating resonance at2, output cancellations and unconstrained
    adaptation all prevent overgeneralization. Corrected locator now names III.B.
- assessment_id: dispersive-memory
  area: evidence
  topic: dispersive-memory
  outcome: supported
  target_ids:
  - AIMech:GammaFilter
  evidence_ids:
  - principe1993
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The negative-binomial-shaped impulse response has mean k/mu only as a positive
    normalized kernel in the stated interval. An alternative gamma-coordinate polynomial
    is not general ordinary-time FIR. Corrected locator includes III.A where Equation8
    appears.
- assessment_id: block-and-online-adaptation
  area: evidence
  topic: block-and-online-adaptation
  outcome: supported
  target_ids:
  - AIMech:GammaFilter
  evidence_ids:
  - principe1993
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Half-squared-error sign and all K+1 tap derivatives agree with direct differentiation.
    Fixed-parameter alpha recurrence matches finite differences; source calls samplewise
    adaptation a local approximation. No arbitrary drifting-parameter exactness is
    claimed.
- assessment_id: normal-equations-and-nonconvexity
  area: evidence
  topic: normal-equations-and-nonconvexity
  outcome: supported
  target_ids:
  - AIMech:GammaFilter
  evidence_ids:
  - principe1993
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Fixed-mu normal equations need rank for unique weights. Direct dR includes
    the transpose cross-moment omitted in the printed equality; the constructed quadratic
    confirms the factor2. The record avoids asserting an author-code failure or a
    globally convex mu objective.
- assessment_id: system-identification-evidence
  area: evidence
  topic: system-identification-evidence
  outcome: supported
  target_ids:
  - AIMech:GammaFilter
  evidence_ids:
  - principe1993
  summary: Supported within the stated primary-source and mathematical scope.
  details: The source evaluates two third-order elliptic systems with selected mu
    and order settings. Corrected Figures4–5 provide experiments; Figure6 concerns
    the transform. The deferred applications are now accurately placed at the end
    of IV. No automatic mu-convergence benchmark is inferred.
- assessment_id: constructed-boundaries
  area: consistency
  topic: direct-tap indexing, strict fixed-stage stability, parameter drift and source-location
    accuracy
  outcome: supported
  target_ids:
  - AIMech:GammaFilter
  evidence_ids:
  - principe1993
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: A rational two-stage fixed-parameter filter checks all three tap derivatives
    and the shared memory-coefficient derivative against finite differences, verifies
    a short impulse-response sequence and demonstrates the missing-transpose factor
    in a one-sided second-moment derivative. No parameters are fitted and no empirical
    study is replicated.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:GammaFilter
  evidence_ids:
  - identity
  - mapping
  - principe1993
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all six claims/locators, source identities/versions/access/hashes, AIO pin and
    mapping, limitations and actual curation timestamps. Capture/source/context hashes
    and exact report mirror agree. Read the complete corrected maintained YAML and
    LinearRegression mapping after fresh capture. Visually reread primary pages2,6
    after that capture to verify stability III.B, impulse-response III.A and experimental
    Figures4–5 with deferred applications in SectionIV. All8 pages were read before
    curation; pages2,4,6,7 were also reread during the initial review. Fixed direct-tap
    indexing, sensitivities and second-moment derivative were checked algebraically.
findings:
- finding_id: F1
  issue_key: gamma-filter-principe1993-locators
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Correct Gamma filter section and figure references
  description: The stability locator names SectionIII.A, but stability is SectionIII.B.
    The impulse-response Equation8 is in SectionIII.A, outside the stated III.B–C
    span. The experimental locator names Figures4–6, but only Figures4–5 show the
    two identification studies; Figure6 is a transform illustration on printed p.655.
    The statement places deferred signal applications in Discussion, while that sentence
    is in SectionIV on printed p.654. Correct these source-location descriptions;
    the mathematical and experimental scope remains supported.
  target_ids:
  - AIMech:GammaFilter
  field_paths:
  - claims[claim_id=fixed-memory-stability].evidence
  - claims[claim_id=dispersive-memory].evidence
  - claims[claim_id=system-identification-evidence]
  evidence_ids:
  - predecessor
  - principe1993
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GammaFilter.yaml
    role: maintained
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261013T071314Z-gamma-filter-locators-open
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/250
  disposition_reason: Corrected stability to III.B, included III.A for impulse response,
    restricted experimental figures to4–5 and moved deferred-application attribution
    to SectionIV. Report mirror and EDIT history agree; fresh capture, corrected-record
    and source-page rereading and required gates pass.
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Both records cite the same combined current-input repository gate execution; these
  are not independent gate runs.
- One new DRAFT concept, yielding 585 native and 442 unchanged generated records.
  The 769-entry main frontier retains 481 pending and 57 partly addressed cohorts,
  plus nested leads; discovery is incomplete.
- All eight journal pages649–656 visually read, including Equations1–35, Figures1–7,
  TableI, experiments, Discussion, references and author biographies. Printed issue
  is February1993; the inspected institutional metadata page lists1992, so use the
  primary printed1993 date. DOI10.1109/78.193206 was found in author institutional
  metadata; an earlier provisional search-key typo was corrected before curation.
  No author implementation or training.
- No author code, training, paid service, hardware measurement or empirical replication.
  Constructed checks test stated boundaries only.
- Only the isolated recovery checkout is changed; original-checkout synchronization
  and old round141 cleanup remain pending explicit approval after automatic review
  rejection.
related_reviews:
- repository: CultureBotAI/AIMech
  review_id: 20261013T071314Z-gamma-filter-locators-open
  relationship: Resolves F1 after source-location corrections and corrected-input
    review.
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
