# Scientific author self-review of randomized sketches of convex programs with tangent-cone Gaussian-width cost-approximation and privacy mutual-information guarantees

- Review: 20261018T204600Z-randomized-sketches-convex-programs-sharp-guarantees
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-18T20:45:00Z
- Finished UTC: 2026-10-18T20:46:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Randomized Sketches of Convex Programs with Tangent-Cone Gaussian-Width Cost-Approximation and Privacy Mutual-Information Guarantees as a distinct DRAFT mathematical_method with related LinearRegression, LassoRegression, and SupportVectorMachine mappings. All three claims and locators across Pilanci &amp; Wainwright (2015, IEEE Trans. Inf. Theory 61(9):5096-5115, arXiv:1404.7203v1) are supported with explicit cost-ratio vs. noisy statistical estimation and matrix-variable dimensionality limitations.

## Scope And Provenance

All fields of the exact maintained RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees record and its primary evidence.

Selection: Exact maintained ID: AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base be35f27caf0b7a3caa811f50a0e894a48a13a4d3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees | data/curated/RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees.yaml | maintained | Randomized Sketches of Convex Programs with Tangent-Cone Gaussian-Width Cost-Approximation and Privacy Mutual-Information Guarantees |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees | All 442 AIO concept records are valid. |
| aimech validate-curated | passed | True | AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees | All 622 curated concept records are valid. |
| aimech seed --check | passed | True | AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees | All 442 AIO records match the pinned source. |
| aimech validate-history | passed | True | AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees | All history sidecars are valid. |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees | Vendored CLAW files are in sync. |
| aimech check-source | passed | True | AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees | Exited 0 without output. |
| Constructed Pilanci &amp; Wainwright 2015 sketched convex program, privacy mutual information, and convex-hull inclusion checks | passed | True | AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees | {<br>  "concept_id": "AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees",<br>  "all_passed": true,<br>  "lemma1_and_corollary1_privacy": {<br>    "passed": true,<br>    "f_star": 49.067043781522855,<br>    "f_hat": 52.74937743533492,<br>    "approx_ratio": 1.0750469840858585,<br>    "lhs_error_ratio": 0.27394704613457416,<br>    "rhs_2z2_over_z1": 0.9339985897644327,<br>    "lemma1_cost_upper_bound": 183.5279439601019,<br>    "mi_rate_n200": 0.4256815599614018,<br>    "mi_rate_n4000": 0.02128407799807009<br>  },<br>  "corollary4_denoising_and_corollary5_svm": {<br>    "passed": true,<br>    "noiseless_cs_recovery_err": 1.6691059580047844e-15,<br>    "noisy_denoise_ratio": 1.7371440177078805,<br>    "dual_svm_approx_ratio": 1.4376573178420367<br>  },<br>  "lemma8_and_lemma13_convex_hull": {<br>    "passed": true,<br>    "all_lemma13_passed": true,<br>    "max_support_ratio_observed": 1.973747104582024,<br>    "lemma8_eq84_passed": true<br>  }<br>} |

## Scientific And Domain Assessments

### Distinctness of randomized sketches of convex programs with tangent-cone Gaussian-width cost-approximation and privacy mutual-information guarantees

identity: supported. Targets: AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees.

Distinct from multi-round Iterative Hessian Sketch for noisy statistical estimation and Newton Sketch for general second-order and self-concordant barrier optimization.

Confirmed via normalized identity check and full-text reading of Pilanci &amp; Wainwright (2015, arXiv:1404.7203v1).

### AIO mappings for AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees

grounding: supported. Targets: AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees.

related_match to AIO:LinearRegression, AIO:LassoRegression, and AIO:SupportVectorMachine are accurate.

Pinned AIO (2026-07-22) contains LinearRegression, LassoRegression, and SupportVectorMachine broadly without tangent-cone Gaussian-width cost-approximation bounds or privacy mutual-information guarantees.

### Definition and scope

evidence: supported. Targets: AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees.

Definition accurately captures Lemma 1 tangent-cone cost approximation, Theorem 1 sub-Gaussian bounds, Corollary 1 privacy mutual-information rates, Theorem 2 ROS S-Gaussian/Rademacher width bounds, and Corollaries 2-7.

All equations and claims verified against Sections 1-6 and Appendices A-D of arXiv:1404.7203v1.

### tangent-cone-cost-approximation-lemma-and-privacy-mutual-information-rate

evidence: supported. Targets: AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees.

Supported by Sections 2.1-2.2 (Theorem 1, Corollary 1), Sections 4.1-4.2 (Lemmas 1-3, Proposition 1), and boundary script.

Verified Lemma 1 error and cost bounds (0.273947 &lt;= 0.933999, f(x_hat) = 52.749 &lt;= 183.528) and Corollary 1 vanishing mutual-information rate.

### ros-s-gaussian-rademacher-width-bounds-and-set-difference-covering-sharpening

evidence: supported. Targets: AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees.

Supported by Section 2.3 (Theorem 2), Section 4.3 (Lemmas 4-7, Proposition 2), Section 5 (Lemmas 8-12), Appendices B-D (Lemma 13), and boundary script.

Verified Lemma 13 support-function bound across 90 random matrices (max ratio 1.9737 &lt;= 3) and Lemma 8 Equation (84) across 50 random convex combinations.

### concrete-sketch-dimension-instantiations-across-convex-programs

evidence: supported. Targets: AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees.

Supported by Sections 3.1-3.6 (Corollaries 2-7, Equations 12-40) and boundary script.

Verified Corollary 4 noiseless compressed sensing exact recovery (error 1.669e-15), folded-noise denoising ratio (1.7371), and Corollary 5 dual SVM simplex sketching ratio (1.4377).

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees.

The full record is consistent; retain DRAFT.

Read every field of RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, three claims and locators, three primary sources with exact SHA-256 digests, three pinned AIO mappings and rationales, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261018T204500Z-randomized-sketches-convex-programs-sharp-guarantees.json | supports | No normalized identity match for Randomized Sketches of Convex Programs with Sharp Guarantees across 442 pinned AIO records and 621 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected LinearRegression, LassoRegression, and SupportVectorMachine in the pinned AIO snapshot (2026-07-22). Provide accurate related_match context. |
| calculation | research/discovery/randomized-sketches-convex-programs-sharp-guarantees-boundaries.py | supports | Executed pure-Python verification in research/discovery/randomized-sketches-convex-programs-sharp-guarantees-boundaries.py (SHA-256 c9fd8f5cd7b66fd03ff1122bfa039b9e705515f20a95ad956e462b443a891a03): verified (1) Lemma 1 deterministic tangent-cone cost approximation inequality (relative error ratio 0.273947 &lt;= 2 Z_2(AK)/Z_1(AK) = 0.933999, f(x_hat) = 52.749377 &lt;= 183.527944, approximation ratio 1.075047) and Corollary 1 vanishing mutual information rate per matrix symbol (0.425682 at n = 200 vs. 0.021284 at n = 4000); (2) Corollary 4 noiseless compressed sensing exact recovery via sketched l_1 denoising (recovery error 1.669e-15), folded-noise denoising cost ratio (1.737144), and Corollary 5 dual squared-hinge SVM simplex sketching cost ratio (1.437657); and (3) Lemma 13 support-function inequality phi_1(X) &lt;= 3 phi_0(X) across 90 random test matrices (maximum ratio 1.973747 &lt;= 2 &lt;= 3) and Lemma 8 Equation (84) convex-hull difference quadratic-form bound across 50 random convex combinations. |
| pilanci2015-convex-sketches-pdf | https://arxiv.org/pdf/1404.7203; Pages 1-37, Sections 1-6 and Appendices A-D (Theorems 1-2, Corollaries 1-7, Propositions 1-2, Lemmas 1-13, Equations 1-86) | supports | All 37 pages of the full-text PDF of Pilanci &amp; Wainwright (2014/2015, arXiv:1404.7203v1) read. Checked all definitions, lemmas, propositions, theorems, corollaries, and proofs. |
| pilanci2015-convex-sketches-abs | https://arxiv.org/abs/1404.7203; arXiv:1404.7203v1 abstract | supports | arXiv abstract and submission metadata read and verified. |
| pilanci2015-convex-sketches-crossref | https://api.crossref.org/works/10.1109/TIT.2015.2450722; IEEE Trans. Inf. Theory 61(9):5096-5115 (2015) Crossref record | supports | IEEE Transactions on Information Theory 2015 Crossref metadata record read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Randomized Sketches of Convex Programs record, yielding 622 native and 442 unchanged generated records.
- All 37 PDF pages of arXiv:1404.7203v1 were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261018T204600Z-randomized-sketches-convex-programs-sharp-guarantees
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of randomized sketches of convex programs with
  tangent-cone Gaussian-width cost-approximation and privacy mutual-information guarantees
started_at: '2026-10-18T20:45:00Z'
finished_at: '2026-10-18T20:46:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from IterativeHessianSketchForConstrainedLeastSquares
    and NewtonSketchRandomizedHessianProjectedOptimization, verified Lemma 1 deterministic
    tangent-cone cost approximation, Corollary 1 vanishing mutual information per
    symbol, Corollary 4 noiseless compressed sensing exact recovery and folded-noise
    denoising, Corollary 5 dual SVM simplex sketching, and Lemmas 8 and 13 set-difference
    covering and rank-to-nuclear convex-hull inclusion, and documented five primary-source
    typographical notes in Pilanci & Wainwright (2015, arXiv:1404.7203v1, pp. 4, 17-20,
    25). This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Randomized Sketches of Convex Programs with Tangent-Cone Gaussian-Width
  Cost-Approximation and Privacy Mutual-Information Guarantees as a distinct DRAFT
  mathematical_method with related LinearRegression, LassoRegression, and SupportVectorMachine
  mappings. All three claims and locators across Pilanci & Wainwright (2015, IEEE
  Trans. Inf. Theory 61(9):5096-5115, arXiv:1404.7203v1) are supported with explicit
  cost-ratio vs. noisy statistical estimation and matrix-variable dimensionality limitations.
source:
  git_revision: be35f27caf0b7a3caa811f50a0e894a48a13a4d3
  state: working_tree
  inputs:
  - path: data/aio/LassoRegression.yaml
    sha256: c62e7ffd00a16f5a82d514687b094aee5f6796d19a7d16200bdb10498c024949
    role: context
  - path: data/aio/LinearRegression.yaml
    sha256: 9b6f1b2ea06d9a47e5f7cf94c66afeaa6d40c3e7d0fdb5037d2c25fabc6d8167
    role: context
  - path: data/aio/SupportVectorMachine.yaml
    sha256: 0cc2faa913fdafdc539a7d04d08d26c0963f77ad3ca26b833b29ed3ed313e4e0
    role: context
  - path: data/curated/IterativeHessianSketchForConstrainedLeastSquares.yaml
    sha256: 7624f3072ac2ec20f35299908dc147a50cc8ae497303a3d4813fb05fa281558c
    role: context
  - path: data/curated/NewtonSketchRandomizedHessianProjectedOptimization.yaml
    sha256: 7e4b3c72c5a4729fde85b448ad4a4d10c22bf40ebdb309f7abaf509fc0ed010c
    role: context
  - path: data/curated/RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees.yaml
    sha256: d387d7abf16c903bdbeb9de17b977194e1a68c5f654ceb46c434c6cb42c0488e
    role: target
  - path: research/discovery/20261018T204500Z-randomized-sketches-convex-programs-sharp-guarantees.json
    sha256: c3d98b9e2f4d279fb9f4279244e3c1bbd17af9f26846e5520b0c05421b05804b
    role: context
  - path: research/discovery/randomized-sketches-convex-programs-sharp-guarantees-boundaries.py
    sha256: c9fd8f5cd7b66fd03ff1122bfa039b9e705515f20a95ad956e462b443a891a03
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
- target_id: AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees
  path: data/curated/RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees.yaml
  label: Randomized Sketches of Convex Programs with Tangent-Cone Gaussian-Width Cost-Approximation
    and Privacy Mutual-Information Guarantees
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees.yaml
    role: maintained
scope:
  description: All fields of the exact maintained RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees
  exclusions:
  - target: Existing native and AIO neighbors
    reason: Identity and mapping context, not full scientific rereview.
checks:
- check_id: maintain-1
  name: aimech validate
  command: aimech validate
  status: passed
  required: true
  target_ids:
  - AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO concept records are valid.
- check_id: maintain-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees
  exit_code: 0
  expected_exit_code: 0
  summary: All 622 curated concept records are valid.
- check_id: maintain-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO records match the pinned source.
- check_id: maintain-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees
  exit_code: 0
  expected_exit_code: 0
  summary: All history sidecars are valid.
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW files are in sync.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed Pilanci & Wainwright 2015 sketched convex program, privacy mutual
    information, and convex-hull inclusion checks
  command: python3 research/discovery/randomized-sketches-convex-programs-sharp-guarantees-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"concept_id\": \"AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees\"\
    ,\n  \"all_passed\": true,\n  \"lemma1_and_corollary1_privacy\": {\n    \"passed\"\
    : true,\n    \"f_star\": 49.067043781522855,\n    \"f_hat\": 52.74937743533492,\n\
    \    \"approx_ratio\": 1.0750469840858585,\n    \"lhs_error_ratio\": 0.27394704613457416,\n\
    \    \"rhs_2z2_over_z1\": 0.9339985897644327,\n    \"lemma1_cost_upper_bound\"\
    : 183.5279439601019,\n    \"mi_rate_n200\": 0.4256815599614018,\n    \"mi_rate_n4000\"\
    : 0.02128407799807009\n  },\n  \"corollary4_denoising_and_corollary5_svm\": {\n\
    \    \"passed\": true,\n    \"noiseless_cs_recovery_err\": 1.6691059580047844e-15,\n\
    \    \"noisy_denoise_ratio\": 1.7371440177078805,\n    \"dual_svm_approx_ratio\"\
    : 1.4376573178420367\n  },\n  \"lemma8_and_lemma13_convex_hull\": {\n    \"passed\"\
    : true,\n    \"all_lemma13_passed\": true,\n    \"max_support_ratio_observed\"\
    : 1.973747104582024,\n    \"lemma8_eq84_passed\": true\n  }\n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261018T204500Z-randomized-sketches-convex-programs-sharp-guarantees.json
  accessed_at: '2026-10-18T20:45:00Z'
  support: supports
  summary: No normalized identity match for Randomized Sketches of Convex Programs
    with Sharp Guarantees across 442 pinned AIO records and 621 maintained IDs, names,
    aliases and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-18T20:45:00Z'
  support: supports
  summary: Inspected LinearRegression, LassoRegression, and SupportVectorMachine in
    the pinned AIO snapshot (2026-07-22). Provide accurate related_match context.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/randomized-sketches-convex-programs-sharp-guarantees-boundaries.py
  accessed_at: '2026-10-18T20:45:00Z'
  snapshot_sha256: c9fd8f5cd7b66fd03ff1122bfa039b9e705515f20a95ad956e462b443a891a03
  support: supports
  summary: 'Executed pure-Python verification in research/discovery/randomized-sketches-convex-programs-sharp-guarantees-boundaries.py
    (SHA-256 c9fd8f5cd7b66fd03ff1122bfa039b9e705515f20a95ad956e462b443a891a03): verified
    (1) Lemma 1 deterministic tangent-cone cost approximation inequality (relative
    error ratio 0.273947 <= 2 Z_2(AK)/Z_1(AK) = 0.933999, f(x_hat) = 52.749377 <=
    183.527944, approximation ratio 1.075047) and Corollary 1 vanishing mutual information
    rate per matrix symbol (0.425682 at n = 200 vs. 0.021284 at n = 4000); (2) Corollary
    4 noiseless compressed sensing exact recovery via sketched l_1 denoising (recovery
    error 1.669e-15), folded-noise denoising cost ratio (1.737144), and Corollary
    5 dual squared-hinge SVM simplex sketching cost ratio (1.437657); and (3) Lemma
    13 support-function inequality phi_1(X) <= 3 phi_0(X) across 90 random test matrices
    (maximum ratio 1.973747 <= 2 <= 3) and Lemma 8 Equation (84) convex-hull difference
    quadratic-form bound across 50 random convex combinations.'
- evidence_id: pilanci2015-convex-sketches-pdf
  kind: primary_source
  reference: https://arxiv.org/pdf/1404.7203
  locator: Pages 1-37, Sections 1-6 and Appendices A-D (Theorems 1-2, Corollaries
    1-7, Propositions 1-2, Lemmas 1-13, Equations 1-86)
  accessed_at: '2026-10-18T13:41:00Z'
  snapshot_sha256: 899110b22c4ad05f9d27efd82d3d77cc3071bfd638e50d3b6907e42335dd860f
  support: supports
  summary: All 37 pages of the full-text PDF of Pilanci & Wainwright (2014/2015, arXiv:1404.7203v1)
    read. Checked all definitions, lemmas, propositions, theorems, corollaries, and
    proofs.
- evidence_id: pilanci2015-convex-sketches-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1404.7203
  locator: arXiv:1404.7203v1 abstract
  accessed_at: '2026-10-18T13:41:00Z'
  snapshot_sha256: 456699d94d7316fb287e723936a65211ee170cd6c3c00a64954d1458c2c26c16
  support: supports
  summary: arXiv abstract and submission metadata read and verified.
- evidence_id: pilanci2015-convex-sketches-crossref
  kind: primary_source
  reference: https://api.crossref.org/works/10.1109/TIT.2015.2450722
  locator: IEEE Trans. Inf. Theory 61(9):5096-5115 (2015) Crossref record
  accessed_at: '2026-10-18T13:41:00Z'
  snapshot_sha256: 27b3fe6046311afa141ca9a1db13a28454e2dec09179ae37b99e555546e5c26e
  support: supports
  summary: IEEE Transactions on Information Theory 2015 Crossref metadata record read
    and verified.
assessments:
- assessment_id: identity-boundary
  area: identity
  topic: Distinctness of randomized sketches of convex programs with tangent-cone
    Gaussian-width cost-approximation and privacy mutual-information guarantees
  outcome: supported
  target_ids:
  - AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees
  evidence_ids:
  - identity
  - pilanci2015-convex-sketches-pdf
  - pilanci2015-convex-sketches-abs
  - pilanci2015-convex-sketches-crossref
  summary: Distinct from multi-round Iterative Hessian Sketch for noisy statistical
    estimation and Newton Sketch for general second-order and self-concordant barrier
    optimization.
  details: Confirmed via normalized identity check and full-text reading of Pilanci
    & Wainwright (2015, arXiv:1404.7203v1).
- assessment_id: aio-mappings
  area: grounding
  topic: AIO mappings for AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees
  outcome: supported
  target_ids:
  - AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees
  evidence_ids:
  - mapping
  - pilanci2015-convex-sketches-pdf
  summary: related_match to AIO:LinearRegression, AIO:LassoRegression, and AIO:SupportVectorMachine
    are accurate.
  details: Pinned AIO (2026-07-22) contains LinearRegression, LassoRegression, and
    SupportVectorMachine broadly without tangent-cone Gaussian-width cost-approximation
    bounds or privacy mutual-information guarantees.
- assessment_id: definition
  area: evidence
  topic: Definition and scope
  outcome: supported
  target_ids:
  - AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees
  evidence_ids:
  - pilanci2015-convex-sketches-pdf
  - pilanci2015-convex-sketches-abs
  - pilanci2015-convex-sketches-crossref
  summary: Definition accurately captures Lemma 1 tangent-cone cost approximation,
    Theorem 1 sub-Gaussian bounds, Corollary 1 privacy mutual-information rates, Theorem
    2 ROS S-Gaussian/Rademacher width bounds, and Corollaries 2-7.
  details: All equations and claims verified against Sections 1-6 and Appendices A-D
    of arXiv:1404.7203v1.
- assessment_id: tangent-cone-cost-approximation-lemma-and-privacy-mutual-information-rate
  area: evidence
  topic: tangent-cone-cost-approximation-lemma-and-privacy-mutual-information-rate
  outcome: supported
  target_ids:
  - AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees
  evidence_ids:
  - pilanci2015-convex-sketches-pdf
  - calculation
  summary: Supported by Sections 2.1-2.2 (Theorem 1, Corollary 1), Sections 4.1-4.2
    (Lemmas 1-3, Proposition 1), and boundary script.
  details: Verified Lemma 1 error and cost bounds (0.273947 <= 0.933999, f(x_hat)
    = 52.749 <= 183.528) and Corollary 1 vanishing mutual-information rate.
- assessment_id: ros-s-gaussian-rademacher-width-bounds-and-set-difference-covering-sharpening
  area: evidence
  topic: ros-s-gaussian-rademacher-width-bounds-and-set-difference-covering-sharpening
  outcome: supported
  target_ids:
  - AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees
  evidence_ids:
  - pilanci2015-convex-sketches-pdf
  - calculation
  summary: Supported by Section 2.3 (Theorem 2), Section 4.3 (Lemmas 4-7, Proposition
    2), Section 5 (Lemmas 8-12), Appendices B-D (Lemma 13), and boundary script.
  details: Verified Lemma 13 support-function bound across 90 random matrices (max
    ratio 1.9737 <= 3) and Lemma 8 Equation (84) across 50 random convex combinations.
- assessment_id: concrete-sketch-dimension-instantiations-across-convex-programs
  area: evidence
  topic: concrete-sketch-dimension-instantiations-across-convex-programs
  outcome: supported
  target_ids:
  - AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees
  evidence_ids:
  - pilanci2015-convex-sketches-pdf
  - calculation
  summary: Supported by Sections 3.1-3.6 (Corollaries 2-7, Equations 12-40) and boundary
    script.
  details: Verified Corollary 4 noiseless compressed sensing exact recovery (error
    1.669e-15), folded-noise denoising ratio (1.7371), and Corollary 5 dual SVM simplex
    sketching ratio (1.4377).
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees
  evidence_ids:
  - identity
  - mapping
  - pilanci2015-convex-sketches-pdf
  - pilanci2015-convex-sketches-abs
  - pilanci2015-convex-sketches-crossref
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of RandomizedSketchesOfConvexProgramsWithTangentConeGaussianWidthGuarantees.yaml:
    stable ID, name, aliases, mathematical_method kind, definition, definition_evidence,
    identity_notes, three claims and locators, three primary sources with exact SHA-256
    digests, three pinned AIO mappings and rationales, four scoped limitations, and
    UTC curation metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Randomized Sketches of Convex Programs record, yielding 622 native
  and 442 unchanged generated records.
- All 37 PDF pages of arXiv:1404.7203v1 were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- randomized-sketching
- convex-programming
- gaussian-width
- privacy-preserving-optimization
- self-review
- discovery-ongoing
```
