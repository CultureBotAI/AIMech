# Scientific author self-review of Sequential nonparametric quantile confidence sequences

- Review: 20261017T123700Z-sequential-nonparametric-quantile-confidence-sequences
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T12:35:00Z
- Finished UTC: 2026-10-17T12:37:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Sequential nonparametric quantile confidence sequences as a distinct DRAFT mathematical_method with related DataDredgingBias and TimeSeriesAnalysis mappings. All four claims and locators across Howard &amp; Ramdas (2022) and Howard, Ramdas, McAuliffe, &amp; Sekhon (2021) are supported with explicit i.i.d. quantile, flat-CDF plateau, and two-sample non-zero-shift limitations.

## Scope And Provenance

All fields of the exact maintained SequentialNonparametricQuantileConfidenceSequences record and its primary evidence.

Selection: Exact maintained ID: AIMech:SequentialNonparametricQuantileConfidenceSequences
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 2abd448cf3d0ceb229989695ada3886b13606b8c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SequentialNonparametricQuantileConfidenceSequences | data/curated/SequentialNonparametricQuantileConfidenceSequences.yaml | maintained | Sequential nonparametric quantile confidence sequences |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:SequentialNonparametricQuantileConfidenceSequences | All 442 AIO concept records are valid. |
| aimech validate-curated | passed | True | AIMech:SequentialNonparametricQuantileConfidenceSequences | All 577 curated concept records are valid. |
| aimech seed --check | passed | True | AIMech:SequentialNonparametricQuantileConfidenceSequences | All 442 AIO records match the pinned source. |
| aimech validate-history | passed | True | AIMech:SequentialNonparametricQuantileConfidenceSequences | All history sidecars are valid. |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:SequentialNonparametricQuantileConfidenceSequences | Vendored CLAW files are in sync. |
| aimech check-source | passed | True | AIMech:SequentialNonparametricQuantileConfidenceSequences | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:SequentialNonparametricQuantileConfidenceSequences | Exited 0 without output. |
| Constructed sequential nonparametric quantile confidence sequence checks | passed | True | AIMech:SequentialNonparametricQuantileConfidenceSequences | {"empirical_process_lil_and_lemma10": {"cor2_radius_t1000": 0.083344, "cor2_to_fixed_dkw_ratio_t1000": 1.940623, "dr68_radius_t1000": 0.120129, "gamma_sq_A085_C7_eta101": 1.256413, "max_lemma10_violation": -2.6e-06, "prefactor_at_gamma_sq_125": 1611.9867, "szorenyi_radius_t1000": 0.094706}, "fixed_quantile_bounds_and_cauchy_coverage": {"cauchy_cs_miscover_rate": 0.0, "cauchy_naive_clt_miscover_rate": 0.358, "f_bb_p05_t200": 0.061055, "f_stitch_p05_t200": 0.070183, "f_subg_p05_t200": 0.122514, "r_tuned_p05_m32": 0.145, "r_tuned_p50_m32": 0.758, "tail_tightness_ratio_subg_to_bb": 2.006621}, "galois_inversion_and_martingale": {"atom_martingale_mean_abs_err": 1e-16, "inversion_mismatches": 0.0, "max_cgf_minus_psi_b": -5.63308e-05, "max_psi_b_minus_psi_g": -4.2e-09}, "two_sample_and_qlucb": {"min_profile_g_minus_true_log_l": -0.142992, "qlucb_accuracy": 1.0, "qlucb_mean_samples": 121.6, "sample_reduction_ratio": 1.3263, "uniform_rr_mean_samples": 161.28}} |

## Scientific And Domain Assessments

### SequentialNonparametricQuantileConfidenceSequences versus SubPsiUniformBoundaryConfidenceSequences and BettingConfidenceSequencesForBoundedMeans

identity: supported. Targets: AIMech:SequentialNonparametricQuantileConfidenceSequences.

Retain Sequential nonparametric quantile confidence sequences as a distinct DRAFT mathematical_method.

SequentialNonparametricQuantileConfidenceSequences formalizes distribution-free order-statistic confidence sequences for fixed quantiles and simultaneous quantile/CDF bands via exact Galois inversions, point-mass randomization martingales, stratified dyadic empirical-process finite-LIL chaining, double-stitched log-odds quantile grids, two-sample sequential quantile tests, and QLUCB best-arm identification, distinct from mean/martingale sub-psi boundaries and bounded-mean betting martingales.

### Mappings to AIO:DataDredgingBias and AIO:TimeSeriesAnalysis

grounding: supported. Targets: AIMech:SequentialNonparametricQuantileConfidenceSequences.

Related mappings to DataDredgingBias and TimeSeriesAnalysis are supported.

Sequential nonparametric quantile confidence sequences guarantee time-uniform coverage across all stopping times (AIO:DataDredgingBias) while tracking order statistics and quantile differences across sequential observation streams and bandit pulls (AIO:TimeSeriesAnalysis).

### galois-order-statistic-inversion-and-point-mass-quantile-martingale

evidence: supported. Targets: AIMech:SequentialNonparametricQuantileConfidenceSequences.

Supported by Section 2 Equations 1-5, Section 7.1 Equations 35-40, and Appendix C.1.

Verified 0 mismatches across all (x, p) grid points on a sample with ties for the exact Galois equivalences in Equation 35, exact zero mean (1e-16) of the point-mass quantile increment, and strict CGF dominance &lt;= psi_B(lam) &lt;= psi_{G,c_p}(lam).

### fixed-quantile-stitched-and-beta-binomial-mixture-confidence-sequences

evidence: supported. Targets: AIMech:SequentialNonparametricQuantileConfidenceSequences.

Supported by Section 3.1 Theorem 1, Section 4.1 Figure 1, Section 7.2-7.3 Equations 41-46, and Appendix D.

Verified 2.0066x tightness improvement of beta-binomial f_tilde_t(0.05) = 0.061055 over the variance-agnostic sub-Gaussian normal mixture (0.122514) at t = 200, and 0.0% &lt;= 5% miscoverage on Cauchy(0, 1) streams vs. 35.8% miscoverage for naive asymptotic CLT peeking.

### time-and-quantile-uniform-empirical-process-lil-and-double-stitching

evidence: supported. Targets: AIMech:SequentialNonparametricQuantileConfidenceSequences.

Supported by Section 3.2 Theorem 2 and Corollaries 1-2, Section 7.4-7.5 Theorems 4-5, and Appendix C.2-C.3 Lemmas 4-10.

Verified finite-LIL exponent gamma^2 = 1.256413 &gt;= 1.25 and prefactor 1611.9867 &lt;= 1612, Corollary 2 radius 0.083344 &lt; Szorenyi et al. (0.094706) &lt; Darling-Robbins (0.120129) at t = 1000, and 0 violations of Lemma 10's hyperbolic-tangent log-odds spacing bound.

### two-sample-sequential-quantile-testing-and-qlucb-best-arm-identification

evidence: supported. Targets: AIMech:SequentialNonparametricQuantileConfidenceSequences.

Supported by Section 5 Corollary 3, Section 6 Theorem 3, and Appendix C.4-C.5 Theorem 6.

Verified Theorem 6's joint product supermartingale lower bound min_x(G_1(x) + G_2(x)) &lt;= log L_1 + log L_2 (diff -0.142992 &lt;= 0) and 100% accuracy of QLUCB with 1.3263x sample reduction over uniform round-robin sampling.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:SequentialNonparametricQuantileConfidenceSequences.

The full record is consistent; retain DRAFT.

Read every field of SequentialNonparametricQuantileConfidenceSequences.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, three full-text primary sources with exact SHA-256 digests, two pinned AIO mappings and rationales, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T123500Z-sequential-nonparametric-quantile-confidence-sequences.json | supports | No normalized identity match for Sequential nonparametric quantile confidence sequences across 442 pinned AIO records and 576 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected DataDredgingBias, TimeSeriesAnalysis, and SamplingBias in the pinned AIO snapshot (2026-07-22). DataDredgingBias and TimeSeriesAnalysis provide optional-stopping and sequential quantile monitoring context via related_match. |
| calculation | research/discovery/sequential-nonparametric-quantile-confidence-sequences-boundaries.py | supports | Constructed analytical and numerical checks for Equation 35 Galois order-statistic inversions and point-mass quantile martingales, Theorem 1a/1b stitched and beta-binomial tail tightness and Cauchy(0, 1) coverage, Theorem 2/4/5 and Corollary 2/Lemma 10 empirical-process finite-LIL and log-odds spacing bounds, and Theorem 6/3 two-sample sequential quantile tests and QLUCB best-arm identification. |
| howard-ramdas2022-quantile-cs | https://ar5iv.labs.arxiv.org/html/1906.09712; Sections 1-8 and Appendices A-D (lines 28-1139, Theorems 1-6, Corollaries 1-3, Lemmas 1-10) | supports | All 1,139 lines of the full-text ar5iv HTML conversion of arXiv:1906.09712 read. Checked Theorems 1-6, Corollaries 1-3, and Lemmas 1-10. |
| howard-ramdas-mcauliffe-sekhon2021-subpsi | https://ar5iv.labs.arxiv.org/html/1810.08240; Section 1.5 (lines 118-134) and Section 3.1-3.2 (lines 221-277) | supports | All 1,696 lines of arXiv:1810.08240 read. Checked stitched sub-gamma and beta-binomial conjugate mixture boundary building blocks. |
| waudby-smith-ramdas2024-betting | https://ar5iv.labs.arxiv.org/html/2010.09686; Section 1.2 (lines 102-115) and References [36] | supports | All 1,971 lines of arXiv:2010.09686 read. Checked anytime-valid confidence sequence context. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Sequential nonparametric quantile confidence sequences record, yielding 577 native and 442 unchanged generated records.
- All 1,139 lines of Howard &amp; Ramdas (2022, arXiv:1906.09712) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T123700Z-sequential-nonparametric-quantile-confidence-sequences
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Sequential nonparametric quantile confidence
  sequences
started_at: '2026-10-17T12:35:00Z'
finished_at: '2026-10-17T12:37:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from SubPsiUniformBoundaryConfidenceSequences
    and BettingConfidenceSequencesForBoundedMeans, i.i.d./shared-marginal-quantile
    assumptions versus general martingale means, flat-CDF interval plateaus [Q(p),
    Q^+(p)], and two-sample testing scope for delta != 0 without a location-shift
    assumption. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Sequential nonparametric quantile confidence sequences as a distinct
  DRAFT mathematical_method with related DataDredgingBias and TimeSeriesAnalysis mappings.
  All four claims and locators across Howard & Ramdas (2022) and Howard, Ramdas, McAuliffe,
  & Sekhon (2021) are supported with explicit i.i.d. quantile, flat-CDF plateau, and
  two-sample non-zero-shift limitations.
source:
  git_revision: 2abd448cf3d0ceb229989695ada3886b13606b8c
  state: working_tree
  inputs:
  - path: data/aio/DataDredgingBias.yaml
    sha256: 335067e88f1462e141ac5f35e697cd42f7d250ec4dde9250531babe0d96cc1d0
    role: context
  - path: data/aio/TimeSeriesAnalysis.yaml
    sha256: c26b267d0f5fb895e9cb0eb587fe86a115d461dae4d70e0ac6baf1eefb1d4eff
    role: context
  - path: data/curated/BettingConfidenceSequencesForBoundedMeans.yaml
    sha256: b7a7f4290f77d5f8152269f60afdaa354defb0251adccd88be92f055839249c7
    role: context
  - path: data/curated/EDetectorSequentialChangeDetection.yaml
    sha256: fb34abf117f642f21e36f7f68a8f3ea10faf4ace751965b8188ef139e36f1956
    role: context
  - path: data/curated/EValueBenjaminiHochbergProcedure.yaml
    sha256: a9553e05b33722aab92042bef82fe67208d2ddb565f7133125bdb2cb79b27057
    role: context
  - path: data/curated/EValueCalibrationAndMerging.yaml
    sha256: f5246f4bae50e562eaa72b28da34d9ab2100831ad5a4e148447754f4debd2107
    role: context
  - path: data/curated/ExactHarmonicMeanPValueTest.yaml
    sha256: e37fe73ff6637f2951762fe4cceca81cd277e7f3d8dafaad63ca150e314a9793
    role: context
  - path: data/curated/GeneralizedMeanPValueMerging.yaml
    sha256: 099a7959a7d93ae42c966e7ca9e54c90581ba3c54218810baead7bd017e58396
    role: context
  - path: data/curated/ProjectedHotellingT2DivideAndCombineConfidenceRegion.yaml
    sha256: e90c5c9448b52371dbe720d48eebd14211970a06202b343e255f35248e7101f0
    role: context
  - path: data/curated/SequentialNonparametricQuantileConfidenceSequences.yaml
    sha256: a3d72fae22daf9b8ad6d2049df0f3e79ce5b8ff72bb829ed14b162853030dc11
    role: target
  - path: data/curated/SubPsiUniformBoundaryConfidenceSequences.yaml
    sha256: 8ad6737fae460a74a9f3c534284689f281dee04b225a5674ce91eb8488d3976a
    role: context
  - path: data/curated/UniversalInferenceSplitLikelihoodRatioTest.yaml
    sha256: f5e33b1cf0e7733ebbd66e466e65044fa2b6d418a03440714eb82cc7fbff5ebb
    role: context
  - path: research/discovery/20261017T123500Z-sequential-nonparametric-quantile-confidence-sequences.json
    sha256: f48e0b27e9ec92ca18df7003e310550ab4200791f8d8a402653e4dd7bf362b9b
    role: context
  - path: research/discovery/sequential-nonparametric-quantile-confidence-sequences-boundaries.py
    sha256: 2d2bedcb5fe830f3c5444ccbad91b96e034af2ff89e0d42a740066d17ac7b8aa
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
- target_id: AIMech:SequentialNonparametricQuantileConfidenceSequences
  path: data/curated/SequentialNonparametricQuantileConfidenceSequences.yaml
  label: Sequential nonparametric quantile confidence sequences
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SequentialNonparametricQuantileConfidenceSequences.yaml
    role: maintained
scope:
  description: All fields of the exact maintained SequentialNonparametricQuantileConfidenceSequences
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:SequentialNonparametricQuantileConfidenceSequences'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:SequentialNonparametricQuantileConfidenceSequences
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
  - AIMech:SequentialNonparametricQuantileConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO concept records are valid.
- check_id: maintain-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:SequentialNonparametricQuantileConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: All 577 curated concept records are valid.
- check_id: maintain-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:SequentialNonparametricQuantileConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO records match the pinned source.
- check_id: maintain-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:SequentialNonparametricQuantileConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: All history sidecars are valid.
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:SequentialNonparametricQuantileConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW files are in sync.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:SequentialNonparametricQuantileConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:SequentialNonparametricQuantileConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed sequential nonparametric quantile confidence sequence checks
  command: python3 research/discovery/sequential-nonparametric-quantile-confidence-sequences-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SequentialNonparametricQuantileConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: '{"empirical_process_lil_and_lemma10": {"cor2_radius_t1000": 0.083344,
    "cor2_to_fixed_dkw_ratio_t1000": 1.940623, "dr68_radius_t1000": 0.120129, "gamma_sq_A085_C7_eta101":
    1.256413, "max_lemma10_violation": -2.6e-06, "prefactor_at_gamma_sq_125": 1611.9867,
    "szorenyi_radius_t1000": 0.094706}, "fixed_quantile_bounds_and_cauchy_coverage":
    {"cauchy_cs_miscover_rate": 0.0, "cauchy_naive_clt_miscover_rate": 0.358, "f_bb_p05_t200":
    0.061055, "f_stitch_p05_t200": 0.070183, "f_subg_p05_t200": 0.122514, "r_tuned_p05_m32":
    0.145, "r_tuned_p50_m32": 0.758, "tail_tightness_ratio_subg_to_bb": 2.006621},
    "galois_inversion_and_martingale": {"atom_martingale_mean_abs_err": 1e-16, "inversion_mismatches":
    0.0, "max_cgf_minus_psi_b": -5.63308e-05, "max_psi_b_minus_psi_g": -4.2e-09},
    "two_sample_and_qlucb": {"min_profile_g_minus_true_log_l": -0.142992, "qlucb_accuracy":
    1.0, "qlucb_mean_samples": 121.6, "sample_reduction_ratio": 1.3263, "uniform_rr_mean_samples":
    161.28}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T123500Z-sequential-nonparametric-quantile-confidence-sequences.json
  accessed_at: '2026-10-17T12:35:00Z'
  support: supports
  summary: No normalized identity match for Sequential nonparametric quantile confidence
    sequences across 442 pinned AIO records and 576 maintained IDs, names, aliases
    and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T12:35:00Z'
  support: supports
  summary: Inspected DataDredgingBias, TimeSeriesAnalysis, and SamplingBias in the
    pinned AIO snapshot (2026-07-22). DataDredgingBias and TimeSeriesAnalysis provide
    optional-stopping and sequential quantile monitoring context via related_match.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/sequential-nonparametric-quantile-confidence-sequences-boundaries.py
  accessed_at: '2026-10-17T12:35:00Z'
  snapshot_sha256: 2d2bedcb5fe830f3c5444ccbad91b96e034af2ff89e0d42a740066d17ac7b8aa
  support: supports
  summary: Constructed analytical and numerical checks for Equation 35 Galois order-statistic
    inversions and point-mass quantile martingales, Theorem 1a/1b stitched and beta-binomial
    tail tightness and Cauchy(0, 1) coverage, Theorem 2/4/5 and Corollary 2/Lemma
    10 empirical-process finite-LIL and log-odds spacing bounds, and Theorem 6/3 two-sample
    sequential quantile tests and QLUCB best-arm identification.
- evidence_id: howard-ramdas2022-quantile-cs
  kind: primary_source
  reference: https://ar5iv.labs.arxiv.org/html/1906.09712
  locator: Sections 1-8 and Appendices A-D (lines 28-1139, Theorems 1-6, Corollaries
    1-3, Lemmas 1-10)
  accessed_at: '2026-10-17T12:35:00Z'
  snapshot_sha256: 09a883cff34d29a90f41d1fb175392703bd82f68c23248d45aa1b1a9e79d18b7
  support: supports
  summary: All 1,139 lines of the full-text ar5iv HTML conversion of arXiv:1906.09712
    read. Checked Theorems 1-6, Corollaries 1-3, and Lemmas 1-10.
- evidence_id: howard-ramdas-mcauliffe-sekhon2021-subpsi
  kind: primary_source
  reference: https://ar5iv.labs.arxiv.org/html/1810.08240
  locator: Section 1.5 (lines 118-134) and Section 3.1-3.2 (lines 221-277)
  accessed_at: '2026-10-17T12:20:00Z'
  snapshot_sha256: aef352a6e271a2317826f200bf481b2aaf956b978323ee8a2b25b589c2ec1732
  support: supports
  summary: All 1,696 lines of arXiv:1810.08240 read. Checked stitched sub-gamma and
    beta-binomial conjugate mixture boundary building blocks.
- evidence_id: waudby-smith-ramdas2024-betting
  kind: primary_source
  reference: https://ar5iv.labs.arxiv.org/html/2010.09686
  locator: Section 1.2 (lines 102-115) and References [36]
  accessed_at: '2026-10-17T12:05:00Z'
  snapshot_sha256: c41bcb5ff7e35853316a0709b17b18506ef1e4be8252a3a474ed38a4811f2495
  support: supports
  summary: All 1,971 lines of arXiv:2010.09686 read. Checked anytime-valid confidence
    sequence context.
assessments:
- assessment_id: identity
  area: identity
  topic: SequentialNonparametricQuantileConfidenceSequences versus SubPsiUniformBoundaryConfidenceSequences
    and BettingConfidenceSequencesForBoundedMeans
  outcome: supported
  target_ids:
  - AIMech:SequentialNonparametricQuantileConfidenceSequences
  evidence_ids:
  - identity
  - howard-ramdas2022-quantile-cs
  - howard-ramdas-mcauliffe-sekhon2021-subpsi
  summary: Retain Sequential nonparametric quantile confidence sequences as a distinct
    DRAFT mathematical_method.
  details: SequentialNonparametricQuantileConfidenceSequences formalizes distribution-free
    order-statistic confidence sequences for fixed quantiles and simultaneous quantile/CDF
    bands via exact Galois inversions, point-mass randomization martingales, stratified
    dyadic empirical-process finite-LIL chaining, double-stitched log-odds quantile
    grids, two-sample sequential quantile tests, and QLUCB best-arm identification,
    distinct from mean/martingale sub-psi boundaries and bounded-mean betting martingales.
- assessment_id: mapping
  area: grounding
  topic: Mappings to AIO:DataDredgingBias and AIO:TimeSeriesAnalysis
  outcome: supported
  target_ids:
  - AIMech:SequentialNonparametricQuantileConfidenceSequences
  evidence_ids:
  - mapping
  - howard-ramdas2022-quantile-cs
  summary: Related mappings to DataDredgingBias and TimeSeriesAnalysis are supported.
  details: Sequential nonparametric quantile confidence sequences guarantee time-uniform
    coverage across all stopping times (AIO:DataDredgingBias) while tracking order
    statistics and quantile differences across sequential observation streams and
    bandit pulls (AIO:TimeSeriesAnalysis).
- assessment_id: galois-order-statistic-inversion-and-point-mass-quantile-martingale
  area: evidence
  topic: galois-order-statistic-inversion-and-point-mass-quantile-martingale
  outcome: supported
  target_ids:
  - AIMech:SequentialNonparametricQuantileConfidenceSequences
  evidence_ids:
  - howard-ramdas2022-quantile-cs
  - calculation
  summary: Supported by Section 2 Equations 1-5, Section 7.1 Equations 35-40, and
    Appendix C.1.
  details: Verified 0 mismatches across all (x, p) grid points on a sample with ties
    for the exact Galois equivalences in Equation 35, exact zero mean (1e-16) of the
    point-mass quantile increment, and strict CGF dominance <= psi_B(lam) <= psi_{G,c_p}(lam).
- assessment_id: fixed-quantile-stitched-and-beta-binomial-mixture-confidence-sequences
  area: evidence
  topic: fixed-quantile-stitched-and-beta-binomial-mixture-confidence-sequences
  outcome: supported
  target_ids:
  - AIMech:SequentialNonparametricQuantileConfidenceSequences
  evidence_ids:
  - howard-ramdas2022-quantile-cs
  - howard-ramdas-mcauliffe-sekhon2021-subpsi
  - calculation
  summary: Supported by Section 3.1 Theorem 1, Section 4.1 Figure 1, Section 7.2-7.3
    Equations 41-46, and Appendix D.
  details: Verified 2.0066x tightness improvement of beta-binomial f_tilde_t(0.05)
    = 0.061055 over the variance-agnostic sub-Gaussian normal mixture (0.122514) at
    t = 200, and 0.0% <= 5% miscoverage on Cauchy(0, 1) streams vs. 35.8% miscoverage
    for naive asymptotic CLT peeking.
- assessment_id: time-and-quantile-uniform-empirical-process-lil-and-double-stitching
  area: evidence
  topic: time-and-quantile-uniform-empirical-process-lil-and-double-stitching
  outcome: supported
  target_ids:
  - AIMech:SequentialNonparametricQuantileConfidenceSequences
  evidence_ids:
  - howard-ramdas2022-quantile-cs
  - calculation
  summary: Supported by Section 3.2 Theorem 2 and Corollaries 1-2, Section 7.4-7.5
    Theorems 4-5, and Appendix C.2-C.3 Lemmas 4-10.
  details: Verified finite-LIL exponent gamma^2 = 1.256413 >= 1.25 and prefactor 1611.9867
    <= 1612, Corollary 2 radius 0.083344 < Szorenyi et al. (0.094706) < Darling-Robbins
    (0.120129) at t = 1000, and 0 violations of Lemma 10's hyperbolic-tangent log-odds
    spacing bound.
- assessment_id: two-sample-sequential-quantile-testing-and-qlucb-best-arm-identification
  area: evidence
  topic: two-sample-sequential-quantile-testing-and-qlucb-best-arm-identification
  outcome: supported
  target_ids:
  - AIMech:SequentialNonparametricQuantileConfidenceSequences
  evidence_ids:
  - howard-ramdas2022-quantile-cs
  - calculation
  summary: Supported by Section 5 Corollary 3, Section 6 Theorem 3, and Appendix C.4-C.5
    Theorem 6.
  details: Verified Theorem 6's joint product supermartingale lower bound min_x(G_1(x)
    + G_2(x)) <= log L_1 + log L_2 (diff -0.142992 <= 0) and 100% accuracy of QLUCB
    with 1.3263x sample reduction over uniform round-robin sampling.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:SequentialNonparametricQuantileConfidenceSequences
  evidence_ids:
  - identity
  - mapping
  - howard-ramdas2022-quantile-cs
  - howard-ramdas-mcauliffe-sekhon2021-subpsi
  - waudby-smith-ramdas2024-betting
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of SequentialNonparametricQuantileConfidenceSequences.yaml:
    stable ID, name, aliases, mathematical_method kind, definition, definition_evidence,
    identity_notes, four claims and locators, three full-text primary sources with
    exact SHA-256 digests, two pinned AIO mappings and rationales, four scoped limitations,
    and UTC curation metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Sequential nonparametric quantile confidence sequences record, yielding
  577 native and 442 unchanged generated records.
- All 1,139 lines of Howard & Ramdas (2022, arXiv:1906.09712) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- confidence-sequences
- quantile-estimation
- empirical-processes
- anytime-valid-inference
- self-review
- discovery-ongoing
```
