# Scientific author self-review of Catoni-style heavy-tailed confidence sequences

- Review: 20261017T125200Z-catoni-style-heavy-tailed-confidence-sequences
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T12:50:00Z
- Finished UTC: 2026-10-17T12:52:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Catoni-style heavy-tailed confidence sequences as a distinct DRAFT mathematical_method with related DataDredgingBias and TimeSeriesAnalysis mappings. All four claims and locators across Wang &amp; Ramdas (2023), Catoni (2012), and Howard, Ramdas, McAuliffe, &amp; Sekhon (2021) are supported with explicit known-variance-bound, small-sample root-finding, and adversarial contamination limitations.

## Scope And Provenance

All fields of the exact maintained CatoniStyleHeavyTailedConfidenceSequences record and its primary evidence.

Selection: Exact maintained ID: AIMech:CatoniStyleHeavyTailedConfidenceSequences
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9a3de36008866e3d41a7a0c5681cde0402261d82.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:CatoniStyleHeavyTailedConfidenceSequences | data/curated/CatoniStyleHeavyTailedConfidenceSequences.yaml | maintained | Catoni-style heavy-tailed confidence sequences |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:CatoniStyleHeavyTailedConfidenceSequences | All 442 AIO concept records are valid. |
| aimech validate-curated | passed | True | AIMech:CatoniStyleHeavyTailedConfidenceSequences | All 578 curated concept records are valid. |
| aimech seed --check | passed | True | AIMech:CatoniStyleHeavyTailedConfidenceSequences | All 442 AIO records match the pinned source. |
| aimech validate-history | passed | True | AIMech:CatoniStyleHeavyTailedConfidenceSequences | All history sidecars are valid. |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:CatoniStyleHeavyTailedConfidenceSequences | Vendored CLAW files are in sync. |
| aimech check-source | passed | True | AIMech:CatoniStyleHeavyTailedConfidenceSequences | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:CatoniStyleHeavyTailedConfidenceSequences | Exited 0 without output. |
| Constructed Catoni-style heavy-tailed confidence sequence checks | passed | True | AIMech:CatoniStyleHeavyTailedConfidenceSequences | {<br>  "all_assertions_passed": true,<br>  "check_1_influence_and_supermartingale": {<br>    "max_influence_bound_violation": 0.0,<br>    "mc_supermartingale_factor_neg_t3": 0.947503,<br>    "mc_supermartingale_factor_pos_t3": 0.962479,<br>    "prop16_underestimated_variance_factor": 1.013879<br>  },<br>  "check_2_three_cs_comparison_and_topology": {<br>    "catoni_widths_by_alpha": {<br>      "0.0001": 1.10578,<br>      "0.01": 0.67182,<br>      "0.1": 0.45491,<br>      "1e-06": 1.54006<br>    },<br>    "dubins_savage_widths_by_alpha": {<br>      "0.0001": 1821.73855,<br>      "0.01": 18.458,<br>      "0.1": 2.06454,<br>      "1e-06": 182149.79306<br>    },<br>    "max_delyon_violation": 0.0,<br>    "sn_outlier_discriminant_pos": 62.9567<br>  },<br>  "check_3_anytime_coverage_and_theorem10": {<br>    "alpha": 0.1,<br>    "peeking_clt_miscoverage_rate": 0.564,<br>    "sequential_catoni_miscoverage_rate": 0.0,<br>    "thm10_quadratic_root_bound_holds": true<br>  },<br>  "check_4_infinite_variance_p_catoni": {<br>    "max_lemma21_violation": 0.0,<br>    "max_phi_p_violation": 0.0,<br>    "p_catoni_miscoverage_rate": 0.0,<br>    "p_exponent": 1.5,<br>    "p_moment_bound_v": 5.999999999999999,<br>    "pareto_tail_index": 1.8,<br>    "width_t150": 4.7246,<br>    "width_t20": 8.3089<br>  },<br>  "concept_id": "AIMech:CatoniStyleHeavyTailedConfidenceSequences"<br>} |

## Scientific And Domain Assessments

### CatoniStyleHeavyTailedConfidenceSequences versus SubPsiUniformBoundaryConfidenceSequences, BettingConfidenceSequencesForBoundedMeans, and SequentialNonparametricQuantileConfidenceSequences

identity: supported. Targets: AIMech:CatoniStyleHeavyTailedConfidenceSequences.

Retain Catoni-style heavy-tailed confidence sequences as a distinct DRAFT mathematical_method.

CatoniStyleHeavyTailedConfidenceSequences constructs anytime-valid confidence sequences for unbounded heavy-tailed and infinite-variance conditional means by applying Catoni and p-Catoni M-estimator influence functions inside exponential supermartingales using only a 2nd or p-th central moment bound, distinct from light-tailed sub-psi boundaries, bounded-mean betting martingales, and order-statistic quantile confidence sequences.

### Mappings to AIO:DataDredgingBias and AIO:TimeSeriesAnalysis

grounding: supported. Targets: AIMech:CatoniStyleHeavyTailedConfidenceSequences.

Related mappings to DataDredgingBias and TimeSeriesAnalysis are supported.

Catoni-style and p-Catoni confidence sequences guarantee valid sequential coverage across arbitrary stopping times under heavy tails (AIO:DataDredgingBias) while tracking conditional means across dependent sequential filtrations (AIO:TimeSeriesAnalysis).

### catoni-influence-supermartingale-and-tightness-necessity

evidence: supported. Targets: AIMech:CatoniStyleHeavyTailedConfidenceSequences.

Supported by Section 6 Equations 26-33, Lemma 8, Theorem 9, and Appendix B.3 Proposition 16.

Verified 0 violations of Catoni influence bounds, Monte Carlo supermartingale factors 0.962479 &lt;= 1 and 0.947503 &lt;= 1 on Student-t_3, and Proposition 16 violation (1.013879 &gt; 1) when true variance exceeds (1 + 2*kappa)*sigma^2.

### comparison-with-dubins-savage-and-delyon-self-normalized-confidence-sequences

evidence: supported. Targets: AIMech:CatoniStyleHeavyTailedConfidenceSequences.

Supported by Section 1 Table 1, Section 3 Theorem 2, Section 5 Lemmas 4-6 and Theorem 7, and Section 6 Theorem 9.

Verified 0 violations of Delyon's inequality, positive discriminant D^+ = 62.9567 &gt; 0 inducing a disconnected 3-component Self-Normalized confidence region under an outlier, and O(log(2/alpha)) Catoni width scaling (1.54006 at alpha=1e-6) vs. O(1/alpha) Dubins-Savage width explosion (182149.79 at alpha=1e-6).

### nonasymptotic-quadratic-width-bound-and-stitched-iterated-logarithm-rate

evidence: supported. Targets: AIMech:CatoniStyleHeavyTailedConfidenceSequences.

Supported by Section 6.1-6.2 Theorem 10, Corollaries 10.1-10.2, Section 8 Figures 4-5, and Appendix B.4-B.5 Lemma 17.

Verified 0.0% &lt;= 10% cumulative miscoverage of Catoni CS on heavy-tailed Student-t_3 (sigma^2 = 25) vs. 56.4% miscoverage for naive CLT peeking, and 100% satisfaction of Theorem 10's quadratic root half-width bound rho_t.

### infinite-variance-p-catoni-supermartingale-confidence-sequences

evidence: supported. Targets: AIMech:CatoniStyleHeavyTailedConfidenceSequences.

Supported by Section 9 Lemma 13, Theorems 14-15, Corollary 15.1, and Appendix C Lemmas 19-21.

Verified 0 violations of exp(phi_p(x)) &lt;= 1 + x + &#124;x&#124;^p/p and Lemma 21's inequality for p = 1.5, and 0.0% &lt;= 10% anytime miscoverage with shrinking width (8.3089 at t=20 to 4.7246 at t=150) on infinite-variance symmetric Pareto(alpha_tail=1.8) streams.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:CatoniStyleHeavyTailedConfidenceSequences.

The full record is consistent; retain DRAFT.

Read every field of CatoniStyleHeavyTailedConfidenceSequences.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, three primary sources with exact SHA-256 digests, two pinned AIO mappings and rationales, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T125000Z-catoni-style-heavy-tailed-confidence-sequences.json | supports | No normalized identity match for Catoni-style heavy-tailed confidence sequences across 442 pinned AIO records and 577 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected DataDredgingBias, TimeSeriesAnalysis, and SamplingBias in the pinned AIO snapshot (2026-07-22). DataDredgingBias and TimeSeriesAnalysis provide optional-stopping and sequential filtration context via related_match. |
| calculation | research/discovery/catoni-style-heavy-tailed-confidence-sequences-boundaries.py | supports | Constructed analytical and numerical checks for Catoni influence bounds, Lemma 8 supermartingale expectations on Student-t_3 and Proposition 16 tightness failure, Delyon's inequality and 3-component Self-Normalized topology vs. Catoni O(log(1/alpha)) and Dubins-Savage O(1/alpha) scaling, Student-t_3 anytime coverage and Theorem 10 quadratic root bounds, and Section 9 p-Catoni infinite-variance bounds on Pareto(1.8). |
| wang-ramdas2023-catoni-cs | https://ar5iv.labs.arxiv.org/html/2202.01250; Sections 1-10 and Appendices A-C (lines 15-804, Lemmas 1, 4-6, 8, 13, 17, 19-21, Theorems 2, 7, 9-10, 14-15, Proposition 16) | supports | All 804 lines of the full-text ar5iv HTML conversion of arXiv:2202.01250 read. Checked Lemmas 1, 4-6, 8, 13, 17, 19-21, Theorems 2, 7, 9-10, 14-15, and Proposition 16. |
| catoni2012-deviation-study | https://api.crossref.org/works/10.1214/11-AIHP454; Abstract and bibliographic record (Ann. Inst. H. Poincare Probab. Statist. 48(4):1148-1185) | supports | Publisher Crossref bibliographic and abstract record read for Catoni (2012). |
| howard-ramdas-mcauliffe-sekhon2021-subpsi | https://ar5iv.labs.arxiv.org/html/1810.08240; Section 2-3 (lines 142-277, Lemma 1 and Theorem 1) | supports | All 1,696 lines of arXiv:1810.08240 read. Checked nonnegative supermartingale and geometric epoch-stitching building blocks. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Catoni-style heavy-tailed confidence sequences record, yielding 578 native and 442 unchanged generated records.
- All 804 lines of Wang &amp; Ramdas (2023, arXiv:2202.01250) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T125200Z-catoni-style-heavy-tailed-confidence-sequences
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Catoni-style heavy-tailed confidence sequences
started_at: '2026-10-17T12:50:00Z'
finished_at: '2026-10-17T12:52:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from SubPsiUniformBoundaryConfidenceSequences,
    BettingConfidenceSequencesForBoundedMeans, and SequentialNonparametricQuantileConfidenceSequences,
    a priori conditional variance / p-th moment upper bound requirements (Proposition
    16), small-sample numerical root-finding and discriminant conditions (Theorem
    10), and sensitivity to adversarial contamination with unbounded moments. This
    is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Catoni-style heavy-tailed confidence sequences as a distinct DRAFT
  mathematical_method with related DataDredgingBias and TimeSeriesAnalysis mappings.
  All four claims and locators across Wang & Ramdas (2023), Catoni (2012), and Howard,
  Ramdas, McAuliffe, & Sekhon (2021) are supported with explicit known-variance-bound,
  small-sample root-finding, and adversarial contamination limitations.
source:
  git_revision: 9a3de36008866e3d41a7a0c5681cde0402261d82
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
  - path: data/curated/CatoniStyleHeavyTailedConfidenceSequences.yaml
    sha256: 5b4dc96917166cb9c70ab7d896501c5f167f5495329e712584ff212feff5b126
    role: target
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
    role: context
  - path: data/curated/SubPsiUniformBoundaryConfidenceSequences.yaml
    sha256: 8ad6737fae460a74a9f3c534284689f281dee04b225a5674ce91eb8488d3976a
    role: context
  - path: data/curated/UniversalInferenceSplitLikelihoodRatioTest.yaml
    sha256: f5e33b1cf0e7733ebbd66e466e65044fa2b6d418a03440714eb82cc7fbff5ebb
    role: context
  - path: research/discovery/20261017T125000Z-catoni-style-heavy-tailed-confidence-sequences.json
    sha256: 0e520152f9974d20cbdcaa3f8d401da5da38f717fa97712a88093188c4146221
    role: context
  - path: research/discovery/catoni-style-heavy-tailed-confidence-sequences-boundaries.py
    sha256: 3eed62c6d9bf2f8041ce323b4dfb4700ac8e98e23f811bb84bfb00de7e68f0f7
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
- target_id: AIMech:CatoniStyleHeavyTailedConfidenceSequences
  path: data/curated/CatoniStyleHeavyTailedConfidenceSequences.yaml
  label: Catoni-style heavy-tailed confidence sequences
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CatoniStyleHeavyTailedConfidenceSequences.yaml
    role: maintained
scope:
  description: All fields of the exact maintained CatoniStyleHeavyTailedConfidenceSequences
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:CatoniStyleHeavyTailedConfidenceSequences'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:CatoniStyleHeavyTailedConfidenceSequences
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
  - AIMech:CatoniStyleHeavyTailedConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO concept records are valid.
- check_id: maintain-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:CatoniStyleHeavyTailedConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: All 578 curated concept records are valid.
- check_id: maintain-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:CatoniStyleHeavyTailedConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO records match the pinned source.
- check_id: maintain-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:CatoniStyleHeavyTailedConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: All history sidecars are valid.
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:CatoniStyleHeavyTailedConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW files are in sync.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:CatoniStyleHeavyTailedConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:CatoniStyleHeavyTailedConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed Catoni-style heavy-tailed confidence sequence checks
  command: python3 research/discovery/catoni-style-heavy-tailed-confidence-sequences-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:CatoniStyleHeavyTailedConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: "{\n  \"all_assertions_passed\": true,\n  \"check_1_influence_and_supermartingale\"\
    : {\n    \"max_influence_bound_violation\": 0.0,\n    \"mc_supermartingale_factor_neg_t3\"\
    : 0.947503,\n    \"mc_supermartingale_factor_pos_t3\": 0.962479,\n    \"prop16_underestimated_variance_factor\"\
    : 1.013879\n  },\n  \"check_2_three_cs_comparison_and_topology\": {\n    \"catoni_widths_by_alpha\"\
    : {\n      \"0.0001\": 1.10578,\n      \"0.01\": 0.67182,\n      \"0.1\": 0.45491,\n\
    \      \"1e-06\": 1.54006\n    },\n    \"dubins_savage_widths_by_alpha\": {\n\
    \      \"0.0001\": 1821.73855,\n      \"0.01\": 18.458,\n      \"0.1\": 2.06454,\n\
    \      \"1e-06\": 182149.79306\n    },\n    \"max_delyon_violation\": 0.0,\n \
    \   \"sn_outlier_discriminant_pos\": 62.9567\n  },\n  \"check_3_anytime_coverage_and_theorem10\"\
    : {\n    \"alpha\": 0.1,\n    \"peeking_clt_miscoverage_rate\": 0.564,\n    \"\
    sequential_catoni_miscoverage_rate\": 0.0,\n    \"thm10_quadratic_root_bound_holds\"\
    : true\n  },\n  \"check_4_infinite_variance_p_catoni\": {\n    \"max_lemma21_violation\"\
    : 0.0,\n    \"max_phi_p_violation\": 0.0,\n    \"p_catoni_miscoverage_rate\":\
    \ 0.0,\n    \"p_exponent\": 1.5,\n    \"p_moment_bound_v\": 5.999999999999999,\n\
    \    \"pareto_tail_index\": 1.8,\n    \"width_t150\": 4.7246,\n    \"width_t20\"\
    : 8.3089\n  },\n  \"concept_id\": \"AIMech:CatoniStyleHeavyTailedConfidenceSequences\"\
    \n}"
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T125000Z-catoni-style-heavy-tailed-confidence-sequences.json
  accessed_at: '2026-10-17T12:50:00Z'
  support: supports
  summary: No normalized identity match for Catoni-style heavy-tailed confidence sequences
    across 442 pinned AIO records and 577 maintained IDs, names, aliases and scoped
    synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T12:50:00Z'
  support: supports
  summary: Inspected DataDredgingBias, TimeSeriesAnalysis, and SamplingBias in the
    pinned AIO snapshot (2026-07-22). DataDredgingBias and TimeSeriesAnalysis provide
    optional-stopping and sequential filtration context via related_match.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/catoni-style-heavy-tailed-confidence-sequences-boundaries.py
  accessed_at: '2026-10-17T12:50:00Z'
  snapshot_sha256: 3eed62c6d9bf2f8041ce323b4dfb4700ac8e98e23f811bb84bfb00de7e68f0f7
  support: supports
  summary: Constructed analytical and numerical checks for Catoni influence bounds,
    Lemma 8 supermartingale expectations on Student-t_3 and Proposition 16 tightness
    failure, Delyon's inequality and 3-component Self-Normalized topology vs. Catoni
    O(log(1/alpha)) and Dubins-Savage O(1/alpha) scaling, Student-t_3 anytime coverage
    and Theorem 10 quadratic root bounds, and Section 9 p-Catoni infinite-variance
    bounds on Pareto(1.8).
- evidence_id: wang-ramdas2023-catoni-cs
  kind: primary_source
  reference: https://ar5iv.labs.arxiv.org/html/2202.01250
  locator: Sections 1-10 and Appendices A-C (lines 15-804, Lemmas 1, 4-6, 8, 13, 17,
    19-21, Theorems 2, 7, 9-10, 14-15, Proposition 16)
  accessed_at: '2026-10-17T12:50:00Z'
  snapshot_sha256: e80a2fc7a2a49108bd3c276657ed1864c0ad1da6f784198574b0b0a92c444fd2
  support: supports
  summary: All 804 lines of the full-text ar5iv HTML conversion of arXiv:2202.01250
    read. Checked Lemmas 1, 4-6, 8, 13, 17, 19-21, Theorems 2, 7, 9-10, 14-15, and
    Proposition 16.
- evidence_id: catoni2012-deviation-study
  kind: primary_source
  reference: https://api.crossref.org/works/10.1214/11-AIHP454
  locator: Abstract and bibliographic record (Ann. Inst. H. Poincare Probab. Statist.
    48(4):1148-1185)
  accessed_at: '2026-10-17T12:50:00Z'
  snapshot_sha256: af6e53dac76c890dc1f787d9fea25c0b34bc47f8a7dedf80a9e6570ac9e83334
  support: supports
  summary: Publisher Crossref bibliographic and abstract record read for Catoni (2012).
- evidence_id: howard-ramdas-mcauliffe-sekhon2021-subpsi
  kind: primary_source
  reference: https://ar5iv.labs.arxiv.org/html/1810.08240
  locator: Section 2-3 (lines 142-277, Lemma 1 and Theorem 1)
  accessed_at: '2026-10-17T12:20:00Z'
  snapshot_sha256: aef352a6e271a2317826f200bf481b2aaf956b978323ee8a2b25b589c2ec1732
  support: supports
  summary: All 1,696 lines of arXiv:1810.08240 read. Checked nonnegative supermartingale
    and geometric epoch-stitching building blocks.
assessments:
- assessment_id: identity
  area: identity
  topic: CatoniStyleHeavyTailedConfidenceSequences versus SubPsiUniformBoundaryConfidenceSequences,
    BettingConfidenceSequencesForBoundedMeans, and SequentialNonparametricQuantileConfidenceSequences
  outcome: supported
  target_ids:
  - AIMech:CatoniStyleHeavyTailedConfidenceSequences
  evidence_ids:
  - identity
  - wang-ramdas2023-catoni-cs
  - howard-ramdas-mcauliffe-sekhon2021-subpsi
  summary: Retain Catoni-style heavy-tailed confidence sequences as a distinct DRAFT
    mathematical_method.
  details: CatoniStyleHeavyTailedConfidenceSequences constructs anytime-valid confidence
    sequences for unbounded heavy-tailed and infinite-variance conditional means by
    applying Catoni and p-Catoni M-estimator influence functions inside exponential
    supermartingales using only a 2nd or p-th central moment bound, distinct from
    light-tailed sub-psi boundaries, bounded-mean betting martingales, and order-statistic
    quantile confidence sequences.
- assessment_id: mapping
  area: grounding
  topic: Mappings to AIO:DataDredgingBias and AIO:TimeSeriesAnalysis
  outcome: supported
  target_ids:
  - AIMech:CatoniStyleHeavyTailedConfidenceSequences
  evidence_ids:
  - mapping
  - wang-ramdas2023-catoni-cs
  summary: Related mappings to DataDredgingBias and TimeSeriesAnalysis are supported.
  details: Catoni-style and p-Catoni confidence sequences guarantee valid sequential
    coverage across arbitrary stopping times under heavy tails (AIO:DataDredgingBias)
    while tracking conditional means across dependent sequential filtrations (AIO:TimeSeriesAnalysis).
- assessment_id: catoni-influence-supermartingale-and-tightness-necessity
  area: evidence
  topic: catoni-influence-supermartingale-and-tightness-necessity
  outcome: supported
  target_ids:
  - AIMech:CatoniStyleHeavyTailedConfidenceSequences
  evidence_ids:
  - wang-ramdas2023-catoni-cs
  - catoni2012-deviation-study
  - calculation
  summary: Supported by Section 6 Equations 26-33, Lemma 8, Theorem 9, and Appendix
    B.3 Proposition 16.
  details: Verified 0 violations of Catoni influence bounds, Monte Carlo supermartingale
    factors 0.962479 <= 1 and 0.947503 <= 1 on Student-t_3, and Proposition 16 violation
    (1.013879 > 1) when true variance exceeds (1 + 2*kappa)*sigma^2.
- assessment_id: comparison-with-dubins-savage-and-delyon-self-normalized-confidence-sequences
  area: evidence
  topic: comparison-with-dubins-savage-and-delyon-self-normalized-confidence-sequences
  outcome: supported
  target_ids:
  - AIMech:CatoniStyleHeavyTailedConfidenceSequences
  evidence_ids:
  - wang-ramdas2023-catoni-cs
  - calculation
  summary: Supported by Section 1 Table 1, Section 3 Theorem 2, Section 5 Lemmas 4-6
    and Theorem 7, and Section 6 Theorem 9.
  details: Verified 0 violations of Delyon's inequality, positive discriminant D^+
    = 62.9567 > 0 inducing a disconnected 3-component Self-Normalized confidence region
    under an outlier, and O(log(2/alpha)) Catoni width scaling (1.54006 at alpha=1e-6)
    vs. O(1/alpha) Dubins-Savage width explosion (182149.79 at alpha=1e-6).
- assessment_id: nonasymptotic-quadratic-width-bound-and-stitched-iterated-logarithm-rate
  area: evidence
  topic: nonasymptotic-quadratic-width-bound-and-stitched-iterated-logarithm-rate
  outcome: supported
  target_ids:
  - AIMech:CatoniStyleHeavyTailedConfidenceSequences
  evidence_ids:
  - wang-ramdas2023-catoni-cs
  - howard-ramdas-mcauliffe-sekhon2021-subpsi
  - calculation
  summary: Supported by Section 6.1-6.2 Theorem 10, Corollaries 10.1-10.2, Section
    8 Figures 4-5, and Appendix B.4-B.5 Lemma 17.
  details: Verified 0.0% <= 10% cumulative miscoverage of Catoni CS on heavy-tailed
    Student-t_3 (sigma^2 = 25) vs. 56.4% miscoverage for naive CLT peeking, and 100%
    satisfaction of Theorem 10's quadratic root half-width bound rho_t.
- assessment_id: infinite-variance-p-catoni-supermartingale-confidence-sequences
  area: evidence
  topic: infinite-variance-p-catoni-supermartingale-confidence-sequences
  outcome: supported
  target_ids:
  - AIMech:CatoniStyleHeavyTailedConfidenceSequences
  evidence_ids:
  - wang-ramdas2023-catoni-cs
  - calculation
  summary: Supported by Section 9 Lemma 13, Theorems 14-15, Corollary 15.1, and Appendix
    C Lemmas 19-21.
  details: Verified 0 violations of exp(phi_p(x)) <= 1 + x + |x|^p/p and Lemma 21's
    inequality for p = 1.5, and 0.0% <= 10% anytime miscoverage with shrinking width
    (8.3089 at t=20 to 4.7246 at t=150) on infinite-variance symmetric Pareto(alpha_tail=1.8)
    streams.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:CatoniStyleHeavyTailedConfidenceSequences
  evidence_ids:
  - identity
  - mapping
  - wang-ramdas2023-catoni-cs
  - catoni2012-deviation-study
  - howard-ramdas-mcauliffe-sekhon2021-subpsi
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of CatoniStyleHeavyTailedConfidenceSequences.yaml: stable
    ID, name, aliases, mathematical_method kind, definition, definition_evidence,
    identity_notes, four claims and locators, three primary sources with exact SHA-256
    digests, two pinned AIO mappings and rationales, four scoped limitations, and
    UTC curation metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Catoni-style heavy-tailed confidence sequences record, yielding
  578 native and 442 unchanged generated records.
- All 804 lines of Wang & Ramdas (2023, arXiv:2202.01250) were read in full text.
related_reviews: []
links: []
tags:
- native-concepts
- confidence-sequences
- heavy-tailed-estimation
- catoni-estimator
- anytime-valid-inference
- self-review
- discovery-ongoing
```
