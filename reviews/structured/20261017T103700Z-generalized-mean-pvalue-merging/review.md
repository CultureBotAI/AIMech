# Scientific author self-review of generalized mean p-value merging

- Review: 20261017T103700Z-generalized-mean-pvalue-merging
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T10:35:00Z
- Finished UTC: 2026-10-17T10:37:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain generalized mean p-value merging as a distinct DRAFT mathematical_method with related DataDredgingBias mapping. All four claims and locators across Vovk &amp; Wang (2020), Fang et al. (2023), and Gui, Jiang, &amp; Wang (2023) are supported with explicit worst-case dependence conservativeness, finite-sample precision boundary, and post-hoc exponent selection limitations.

## Scope And Provenance

All fields of the exact maintained GeneralizedMeanPValueMerging record and its primary evidence.

Selection: Exact maintained ID: AIMech:GeneralizedMeanPValueMerging
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base fc78821398ca6093aad2ad8d0614398c5127af80.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:GeneralizedMeanPValueMerging | data/curated/GeneralizedMeanPValueMerging.yaml | maintained | Generalized mean p-value merging |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validation suite | passed | True | AIMech:GeneralizedMeanPValueMerging | All AIMech schema, curated, seed, and history validations passed. |
| just vendored-check | passed | True | AIMech:GeneralizedMeanPValueMerging | Vendored CLAW review files match canonical checksums. |
| aimech check-source | passed | True | AIMech:GeneralizedMeanPValueMerging | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:GeneralizedMeanPValueMerging | Exited 0 without output. |
| Constructed generalized mean p-value merging boundaries | passed | True | AIMech:GeneralizedMeanPValueMerging | {"concept_id": "AIMech:GeneralizedMeanPValueMerging", "prop8_prop9_harmonic_multipliers": {"3": {"y_K": 1.8169605355365102, "a_K_H": 2.745643576732724, "a_K_H_over_ln_K": 2.499192485878138, "r_star_minimizer": -11.140723975747152, "e_ln_K": 2.9863378208083255}, "5": {"y_K": 6.76088975619874, "a_K_H": 3.5645018084938873, "a_K_H_over_ln_K": 2.2147494979181674, "r_star_minimizer": -2.640856237522197, "e_ln_K": 4.374905831402675}, "10": {"y_K": 23.258789671962646, "a_K_H": 4.559778560272899, "a_K_H_over_ln_K": 1.9802866674272739, "r_star_minimizer": -1.7677041641106597, "e_ln_K": 6.259075216766395}, "50": {"y_K": 221.45694655270665, "a_K_H": 6.625000924775344, "a_K_H_over_ln_K": 1.6934974348521963, "r_star_minimizer": -1.3434038804418624, "e_ln_K": 10.633981048169069}, "1000": {"y_K": 7986.795110324581, "a_K_H": 10.110735846311918, "a_K_H_over_ln_K": 1.4636789286782237, "r_star_minimizer": -1.1692690290604408, "e_ln_K": 18.777225650299183}}, "prop4_prop5_prop5w_precision_checks": {"eps": 0.1, "prob_2_M12_le_eps_under_joint_mixability": 0.1, "prob_unscaled_M12_le_eps_under_joint_mixability": 0.2, "prop5_k2_r2_precise_multiplier": 1.4142135623730951, "prop3_k2_r2_asymptotic_multiplier": 1.7320508075688772, "prop5w_dominant_weight_multiplier_w07": 1.4285714285714286, "prop5w_merged_p_value": 0.041428571428571426}, "prop12_eq17_simulation_K50_mu3": {"rho_0.1": {"mean_bonferroni": 2.6857250696607493e-05, "mean_geometric": 0.0027689647881950046, "mean_arithmetic": 0.03438829586782956, "mean_compound_BG": 5.3714501393214986e-05, "mean_compound_BA": 5.3714501393214986e-05}, "rho_0.9": {"mean_bonferroni": 0.13459898203203058, "mean_geometric": 0.03596571591761933, "mean_arithmetic": 0.03601379134003679, "mean_compound_BG": 0.06841813529520667, "mean_compound_BA": 0.06517145269925724}}} |

## Scientific And Domain Assessments

### Generalized Mean P-Value Merging versus ExactHarmonicMeanPValueTest and LogarithmicOpinionPool

identity: supported. Targets: AIMech:GeneralizedMeanPValueMerging.

Retain generalized mean p-value merging as a distinct DRAFT mathematical_method.

Vovk &amp; Wang (2020) define a complete family of worst-case dependence-valid p-merging functions based on generalized r-means across r in [-infinity, +infinity], distinct from Landau-calibrated ExactHarmonicMeanPValueTest and probability-density LogarithmicOpinionPool.

### Mapping to AIO:DataDredgingBias

grounding: supported. Targets: AIMech:GeneralizedMeanPValueMerging.

Related mapping to DataDredgingBias is supported.

Generalized mean p-value merging guarantees valid Type I error control when combining multiple arbitrarily dependent hypothesis tests, mitigating multiple-testing false-positive inflation (AIO:DataDredgingBias).

### integrable-exponent-merging-and-finite-sample-precision-interval

evidence: supported. Targets: AIMech:GeneralizedMeanPValueMerging.

Supported by Theorem 2 and Propositions 3-5 in Vovk &amp; Wang (2020) and verified numerically.

Verified exact joint-mixability tightness P(2 M_{1,2} &lt;= eps) = eps and Proposition 5 sharpened multiplier min(r+1, K)^(1/r).

### non-integrable-negative-exponent-and-harmonic-worst-case-multipliers

evidence: supported. Targets: AIMech:GeneralizedMeanPValueMerging.

Supported by Theorem 7 and Propositions 8-9 in Vovk &amp; Wang (2020) and verified via root solving.

Solved y(y+K)/((y+1)K) = ln(y+1) for K in {3, 5, 10, 50, 1000}, confirming strict monotonicity of a_K^H / ln K -&gt; 1 and a_K^H &lt; e * ln K.

### simplex-weighted-generalized-mean-precision-conditions

evidence: supported. Targets: AIMech:GeneralizedMeanPValueMerging.

Supported by Theorem 2w and Propositions 4w-5w in Vovk &amp; Wang (2020) and verified numerically.

Verified Proposition 4w precision interval [w_max/(1-w_max), (1-w_max)/w_max] for w_max &lt;= 1/2 and Proposition 5w dominant-weight formula p_1 + sum_{k&gt;=2} (w_k/w_1) p_k.

### power-index-phase-transition-and-compound-bonferroni-averaging

evidence: supported. Targets: AIMech:GeneralizedMeanPValueMerging.

Supported by Propositions 11-12 and Lemma 15 in Vovk &amp; Wang (2020) and verified on Eq. 17.

Confirmed that compound Bonferroni-Geometric and Bonferroni-Arithmetic merging adapt across weak (rho = 0.1) and strong (rho = 0.9) equicorrelated Gaussian z-tests.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:GeneralizedMeanPValueMerging.

The full record is consistent; retain DRAFT.

Read every field of GeneralizedMeanPValueMerging.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, three full-text primary sources with exact SHA-256 digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T103500Z-generalized-mean-pvalue-merging.json | supports | No normalized identity match for generalized mean p-value merging across 442 pinned AIO records and 568 maintained IDs, names, aliases and scoped synonyms. Distinct from AIMech:ExactHarmonicMeanPValueTest and AIMech:LogarithmicOpinionPool. |
| mapping | sources/aio/aio.json | supports | Inspected DataDredgingBias and EnsembleLearning in the pinned AIO snapshot (2026-07-22). DataDredgingBias provides multiple-testing bias context via related_match. |
| calculation | research/discovery/generalized-mean-pvalue-merging-boundaries.py | supports | Constructed analytical and simulation checks for (1) Proposition 8/9 exact harmonic multipliers a_K^H and root equation y(y+K)/((y+1)K) = ln(y+1), (2) Proposition 4/5/5w joint-mixability precision intervals and simplex-weighted multipliers, and (3) Section 6 Equation 17 compound Bonferroni-Geometric and Bonferroni-Arithmetic merging. |
| vovk-wang2020 | https://ar5iv.labs.arxiv.org/html/1212.4966; Sections 2-6 (Lemma 1, Theorems 2, 2w, 7, Propositions 3-12, 4w-5w) and Appendix A (lines 846-1024) | supports | All 1,046 lines of the full-text ar5iv HTML conversion of arXiv:1212.4966 read. Checked Theorems 2, 2w, 7, Propositions 3-12, 4w-5w, and Appendix A proofs. |
| fang-chang-park-tseng2023 | https://ar5iv.labs.arxiv.org/html/2103.12967; Section 1 (lines 17-21), Section 3.2 Remark (lines 86-92) | supports | All 546 lines of arXiv:2103.12967 read. Checked comparison between Vovk &amp; Wang (2020) worst-case dependence multipliers and bivariate-normal tail robustness. |
| gui-jiang-wang2023 | https://arxiv.org/html/2310.20460v1; Section 1 (lines 50-78) | supports | All 1,071 lines of arXiv:2310.20460v1 read. Checked discussion of Vovk &amp; Wang (2020) generalized mean p-value averaging. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT generalized mean p-value merging record, yielding 569 native and 442 unchanged generated records.
- All 1,046 lines of Vovk &amp; Wang (2020, arXiv:1212.4966) were read. Display equations in Proposition 6 were omitted by the ar5iv HTML-to-markdown converter while all inline formulas in Propositions 3-5, 8-10, 4w-5w, 11-12, and Appendix A proofs were preserved verbatim.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T103700Z-generalized-mean-pvalue-merging
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of generalized mean p-value merging
started_at: '2026-10-17T10:35:00Z'
finished_at: '2026-10-17T10:37:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from ExactHarmonicMeanPValueTest
    (Wilson 2019; Fang et al. 2023) and LogarithmicOpinionPool, worst-case copula
    conservativeness under weak dependence, finite-sample precision interval boundaries
    r in [1/(K-1), K-1], and post-hoc exponent selection invalidity. This is adversarial
    author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain generalized mean p-value merging as a distinct DRAFT mathematical_method
  with related DataDredgingBias mapping. All four claims and locators across Vovk
  & Wang (2020), Fang et al. (2023), and Gui, Jiang, & Wang (2023) are supported with
  explicit worst-case dependence conservativeness, finite-sample precision boundary,
  and post-hoc exponent selection limitations.
source:
  git_revision: fc78821398ca6093aad2ad8d0614398c5127af80
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/DataDredgingBias.yaml
    sha256: 335067e88f1462e141ac5f35e697cd42f7d250ec4dde9250531babe0d96cc1d0
    role: context
  - path: data/aio/EnsembleLearning.yaml
    sha256: cf9435e5a799d84072222190c2d681c53b22bf9e7094891405008ebe398a39ed
    role: context
  - path: data/aio/EvaluationBias.yaml
    sha256: 6523f8c43f7b140c6dd593069e30b7fc1bdd60b89d01bdf5441d2bc83a12e749
    role: context
  - path: data/curated/ExactHarmonicMeanPValueTest.yaml
    sha256: e37fe73ff6637f2951762fe4cceca81cd277e7f3d8dafaad63ca150e314a9793
    role: context
  - path: data/curated/GeneralizedMeanPValueMerging.yaml
    sha256: 099a7959a7d93ae42c966e7ca9e54c90581ba3c54218810baead7bd017e58396
    role: target
  - path: data/curated/HalfCauchyCombinationTest.yaml
    sha256: 16580963357781445af56264dcff8c16033282879c5e99819ce15a9445d5e95e
    role: context
  - path: data/curated/LeftTruncatedCauchyCombinationTest.yaml
    sha256: 6f330e91bd1f1994411c626759aee135f6dc781c2b3107e2c9db78e26c5685f6
    role: context
  - path: data/curated/LogarithmicOpinionPool.yaml
    sha256: bdff4b82fa80ae38dd1a1295afdf9f5c0d877632818ea25841ca7a4adce2f430
    role: context
  - path: data/curated/MultipleTestingNodeConflictDiagnostic.yaml
    sha256: 1a21330e57dec49c7dd243afce713439382955663f979a1ec9df393d79798a0c
    role: context
  - path: research/discovery/20261017T103500Z-generalized-mean-pvalue-merging.json
    sha256: 39b2bae95af9ebfe2a95b08512f128cd2bc96c2194fe361e97a6b277debe8344
    role: context
  - path: research/discovery/generalized-mean-pvalue-merging-boundaries.py
    sha256: 44f1931563deeed6236f5c62da4a02520f051ee356d5391c7817918d69090c38
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
- target_id: AIMech:GeneralizedMeanPValueMerging
  path: data/curated/GeneralizedMeanPValueMerging.yaml
  label: Generalized mean p-value merging
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/GeneralizedMeanPValueMerging.yaml
    role: maintained
scope:
  description: All fields of the exact maintained GeneralizedMeanPValueMerging record
    and its primary evidence.
  selection: 'Exact maintained ID: AIMech:GeneralizedMeanPValueMerging'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:GeneralizedMeanPValueMerging
  exclusions:
  - target: Existing native and AIO neighbors
    reason: Identity and mapping context, not full scientific rereview.
checks:
- check_id: required-0
  name: aimech validation suite
  command: aimech validate && aimech validate-curated && aimech seed --check && aimech
    validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:GeneralizedMeanPValueMerging
  exit_code: 0
  expected_exit_code: 0
  summary: All AIMech schema, curated, seed, and history validations passed.
- check_id: required-1
  name: just vendored-check
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:GeneralizedMeanPValueMerging
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW review files match canonical checksums.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:GeneralizedMeanPValueMerging
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:GeneralizedMeanPValueMerging
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed generalized mean p-value merging boundaries
  command: python3 research/discovery/generalized-mean-pvalue-merging-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:GeneralizedMeanPValueMerging
  exit_code: 0
  expected_exit_code: 0
  summary: '{"concept_id": "AIMech:GeneralizedMeanPValueMerging", "prop8_prop9_harmonic_multipliers":
    {"3": {"y_K": 1.8169605355365102, "a_K_H": 2.745643576732724, "a_K_H_over_ln_K":
    2.499192485878138, "r_star_minimizer": -11.140723975747152, "e_ln_K": 2.9863378208083255},
    "5": {"y_K": 6.76088975619874, "a_K_H": 3.5645018084938873, "a_K_H_over_ln_K":
    2.2147494979181674, "r_star_minimizer": -2.640856237522197, "e_ln_K": 4.374905831402675},
    "10": {"y_K": 23.258789671962646, "a_K_H": 4.559778560272899, "a_K_H_over_ln_K":
    1.9802866674272739, "r_star_minimizer": -1.7677041641106597, "e_ln_K": 6.259075216766395},
    "50": {"y_K": 221.45694655270665, "a_K_H": 6.625000924775344, "a_K_H_over_ln_K":
    1.6934974348521963, "r_star_minimizer": -1.3434038804418624, "e_ln_K": 10.633981048169069},
    "1000": {"y_K": 7986.795110324581, "a_K_H": 10.110735846311918, "a_K_H_over_ln_K":
    1.4636789286782237, "r_star_minimizer": -1.1692690290604408, "e_ln_K": 18.777225650299183}},
    "prop4_prop5_prop5w_precision_checks": {"eps": 0.1, "prob_2_M12_le_eps_under_joint_mixability":
    0.1, "prob_unscaled_M12_le_eps_under_joint_mixability": 0.2, "prop5_k2_r2_precise_multiplier":
    1.4142135623730951, "prop3_k2_r2_asymptotic_multiplier": 1.7320508075688772, "prop5w_dominant_weight_multiplier_w07":
    1.4285714285714286, "prop5w_merged_p_value": 0.041428571428571426}, "prop12_eq17_simulation_K50_mu3":
    {"rho_0.1": {"mean_bonferroni": 2.6857250696607493e-05, "mean_geometric": 0.0027689647881950046,
    "mean_arithmetic": 0.03438829586782956, "mean_compound_BG": 5.3714501393214986e-05,
    "mean_compound_BA": 5.3714501393214986e-05}, "rho_0.9": {"mean_bonferroni": 0.13459898203203058,
    "mean_geometric": 0.03596571591761933, "mean_arithmetic": 0.03601379134003679,
    "mean_compound_BG": 0.06841813529520667, "mean_compound_BA": 0.06517145269925724}}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T103500Z-generalized-mean-pvalue-merging.json
  accessed_at: '2026-10-17T10:35:00Z'
  support: supports
  summary: No normalized identity match for generalized mean p-value merging across
    442 pinned AIO records and 568 maintained IDs, names, aliases and scoped synonyms.
    Distinct from AIMech:ExactHarmonicMeanPValueTest and AIMech:LogarithmicOpinionPool.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T10:35:00Z'
  support: supports
  summary: Inspected DataDredgingBias and EnsembleLearning in the pinned AIO snapshot
    (2026-07-22). DataDredgingBias provides multiple-testing bias context via related_match.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/generalized-mean-pvalue-merging-boundaries.py
  accessed_at: '2026-10-17T10:35:00Z'
  snapshot_sha256: 44f1931563deeed6236f5c62da4a02520f051ee356d5391c7817918d69090c38
  support: supports
  summary: Constructed analytical and simulation checks for (1) Proposition 8/9 exact
    harmonic multipliers a_K^H and root equation y(y+K)/((y+1)K) = ln(y+1), (2) Proposition
    4/5/5w joint-mixability precision intervals and simplex-weighted multipliers,
    and (3) Section 6 Equation 17 compound Bonferroni-Geometric and Bonferroni-Arithmetic
    merging.
- evidence_id: vovk-wang2020
  kind: primary_source
  reference: https://ar5iv.labs.arxiv.org/html/1212.4966
  locator: Sections 2-6 (Lemma 1, Theorems 2, 2w, 7, Propositions 3-12, 4w-5w) and
    Appendix A (lines 846-1024)
  accessed_at: '2026-10-17T10:35:00Z'
  snapshot_sha256: 795de89f2d3ab8ce1a5c07046cce1fb85a097610b08ba7ffd661ddeae22a16a3
  support: supports
  summary: All 1,046 lines of the full-text ar5iv HTML conversion of arXiv:1212.4966
    read. Checked Theorems 2, 2w, 7, Propositions 3-12, 4w-5w, and Appendix A proofs.
- evidence_id: fang-chang-park-tseng2023
  kind: primary_source
  reference: https://ar5iv.labs.arxiv.org/html/2103.12967
  locator: Section 1 (lines 17-21), Section 3.2 Remark (lines 86-92)
  accessed_at: '2026-10-17T09:10:00Z'
  snapshot_sha256: 432b18ec119b33e5b3cd66b32bb71015a243bb7dd28362cf7c9557f0e78a8402
  support: supports
  summary: All 546 lines of arXiv:2103.12967 read. Checked comparison between Vovk
    & Wang (2020) worst-case dependence multipliers and bivariate-normal tail robustness.
- evidence_id: gui-jiang-wang2023
  kind: primary_source
  reference: https://arxiv.org/html/2310.20460v1
  locator: Section 1 (lines 50-78)
  accessed_at: '2026-10-17T09:10:00Z'
  snapshot_sha256: 3f487fc6bca4b5db326053b80a172ec71bee5387faa78dc2605e6bf91c795f71
  support: supports
  summary: All 1,071 lines of arXiv:2310.20460v1 read. Checked discussion of Vovk
    & Wang (2020) generalized mean p-value averaging.
assessments:
- assessment_id: identity
  area: identity
  topic: Generalized Mean P-Value Merging versus ExactHarmonicMeanPValueTest and LogarithmicOpinionPool
  outcome: supported
  target_ids:
  - AIMech:GeneralizedMeanPValueMerging
  evidence_ids:
  - identity
  - vovk-wang2020
  - fang-chang-park-tseng2023
  summary: Retain generalized mean p-value merging as a distinct DRAFT mathematical_method.
  details: Vovk & Wang (2020) define a complete family of worst-case dependence-valid
    p-merging functions based on generalized r-means across r in [-infinity, +infinity],
    distinct from Landau-calibrated ExactHarmonicMeanPValueTest and probability-density
    LogarithmicOpinionPool.
- assessment_id: mapping
  area: grounding
  topic: Mapping to AIO:DataDredgingBias
  outcome: supported
  target_ids:
  - AIMech:GeneralizedMeanPValueMerging
  evidence_ids:
  - mapping
  - vovk-wang2020
  summary: Related mapping to DataDredgingBias is supported.
  details: Generalized mean p-value merging guarantees valid Type I error control
    when combining multiple arbitrarily dependent hypothesis tests, mitigating multiple-testing
    false-positive inflation (AIO:DataDredgingBias).
- assessment_id: integrable-exponent-merging-and-finite-sample-precision-interval
  area: evidence
  topic: integrable-exponent-merging-and-finite-sample-precision-interval
  outcome: supported
  target_ids:
  - AIMech:GeneralizedMeanPValueMerging
  evidence_ids:
  - vovk-wang2020
  - calculation
  summary: Supported by Theorem 2 and Propositions 3-5 in Vovk & Wang (2020) and verified
    numerically.
  details: Verified exact joint-mixability tightness P(2 M_{1,2} <= eps) = eps and
    Proposition 5 sharpened multiplier min(r+1, K)^(1/r).
- assessment_id: non-integrable-negative-exponent-and-harmonic-worst-case-multipliers
  area: evidence
  topic: non-integrable-negative-exponent-and-harmonic-worst-case-multipliers
  outcome: supported
  target_ids:
  - AIMech:GeneralizedMeanPValueMerging
  evidence_ids:
  - vovk-wang2020
  - fang-chang-park-tseng2023
  - calculation
  summary: Supported by Theorem 7 and Propositions 8-9 in Vovk & Wang (2020) and verified
    via root solving.
  details: Solved y(y+K)/((y+1)K) = ln(y+1) for K in {3, 5, 10, 50, 1000}, confirming
    strict monotonicity of a_K^H / ln K -> 1 and a_K^H < e * ln K.
- assessment_id: simplex-weighted-generalized-mean-precision-conditions
  area: evidence
  topic: simplex-weighted-generalized-mean-precision-conditions
  outcome: supported
  target_ids:
  - AIMech:GeneralizedMeanPValueMerging
  evidence_ids:
  - vovk-wang2020
  - calculation
  summary: Supported by Theorem 2w and Propositions 4w-5w in Vovk & Wang (2020) and
    verified numerically.
  details: Verified Proposition 4w precision interval [w_max/(1-w_max), (1-w_max)/w_max]
    for w_max <= 1/2 and Proposition 5w dominant-weight formula p_1 + sum_{k>=2} (w_k/w_1)
    p_k.
- assessment_id: power-index-phase-transition-and-compound-bonferroni-averaging
  area: evidence
  topic: power-index-phase-transition-and-compound-bonferroni-averaging
  outcome: supported
  target_ids:
  - AIMech:GeneralizedMeanPValueMerging
  evidence_ids:
  - vovk-wang2020
  - gui-jiang-wang2023
  - calculation
  summary: Supported by Propositions 11-12 and Lemma 15 in Vovk & Wang (2020) and
    verified on Eq. 17.
  details: Confirmed that compound Bonferroni-Geometric and Bonferroni-Arithmetic
    merging adapt across weak (rho = 0.1) and strong (rho = 0.9) equicorrelated Gaussian
    z-tests.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:GeneralizedMeanPValueMerging
  evidence_ids:
  - identity
  - mapping
  - vovk-wang2020
  - fang-chang-park-tseng2023
  - gui-jiang-wang2023
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of GeneralizedMeanPValueMerging.yaml: stable ID, name,
    aliases, mathematical_method kind, definition, definition_evidence, identity_notes,
    four claims and locators, three full-text primary sources with exact SHA-256 digests,
    pinned AIO mapping and rationale, four scoped limitations, and UTC curation metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT generalized mean p-value merging record, yielding 569 native and
  442 unchanged generated records.
- All 1,046 lines of Vovk & Wang (2020, arXiv:1212.4966) were read. Display equations
  in Proposition 6 were omitted by the ar5iv HTML-to-markdown converter while all
  inline formulas in Propositions 3-5, 8-10, 4w-5w, 11-12, and Appendix A proofs were
  preserved verbatim.
related_reviews: []
links: []
tags:
- native-concepts
- hypothesis-testing
- multiple-testing
- self-review
- discovery-ongoing
```
