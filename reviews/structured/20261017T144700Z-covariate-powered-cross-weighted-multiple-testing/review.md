# Scientific author self-review of Covariate-powered cross-weighted multiple testing

- Review: 20261017T144700Z-covariate-powered-cross-weighted-multiple-testing
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T14:45:00Z
- Finished UTC: 2026-10-17T14:47:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Covariate-powered cross-weighted multiple testing as a distinct DRAFT mathematical_method with a related DataDredgingBias mapping. All four claims and locators across Ignatiadis &amp; Huber (2021 JRSS-B 83(4):720-751) are supported with explicit tau-censoring, independent-block fold partitioning, and covariate-discretization limitations.

## Scope And Provenance

All fields of the exact maintained CovariatePoweredCrossWeightedMultipleTesting record and its primary evidence.

Selection: Exact maintained ID: AIMech:CovariatePoweredCrossWeightedMultipleTesting
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ab2f7f866cc1a668c8cd5a8fadd7f381737dbd11.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:CovariatePoweredCrossWeightedMultipleTesting | data/curated/CovariatePoweredCrossWeightedMultipleTesting.yaml | maintained | Covariate-powered cross-weighted multiple testing |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:CovariatePoweredCrossWeightedMultipleTesting | All 442 AIO concept records are valid. |
| aimech validate-curated | passed | True | AIMech:CovariatePoweredCrossWeightedMultipleTesting | All 588 curated concept records are valid. |
| aimech seed --check | passed | True | AIMech:CovariatePoweredCrossWeightedMultipleTesting | All 442 AIO records match the pinned source. |
| aimech validate-history | passed | True | AIMech:CovariatePoweredCrossWeightedMultipleTesting | All history sidecars are valid. |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:CovariatePoweredCrossWeightedMultipleTesting | Vendored CLAW files are in sync. |
| aimech check-source | passed | True | AIMech:CovariatePoweredCrossWeightedMultipleTesting | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:CovariatePoweredCrossWeightedMultipleTesting | Exited 0 without output. |
| Constructed covariate-powered cross-weighted multiple testing checks | passed | True | AIMech:CovariatePoweredCrossWeightedMultipleTesting | {"claim1_honest_tau_censored_fdr_and_counterexamples": {"fdr_ihw_bh_alt": 0.0385, "fdr_ihw_gbh_global_null_G25": 0.065, "fdr_ihw_storey_alt": 0.0859, "fdr_naive_gbh_global_null_G25": 0.2533, "power_ihw_bh_no_storey": 0.8148, "power_ihw_storey": 0.8891, "power_unweighted_bh": 0.7487, "s13_exact_uncensored_honest_fdr": 0.216, "s13_mc_tau_censored_honest_fdr": 0.2023, "s13_mc_uncensored_honest_fdr": 0.212}, "claim2_asymptotic_proposition1_and_corollary2": {"prop1a_naive_spec7_fdr": 0.7674, "prop1b_ihw_spec7_uncensored_fdr": 0.1331, "prop1c_gbh_power": 0.3978, "prop1c_ihw_gbh_uncensored_fdr": 0.0789, "prop1c_ihw_gbh_uncensored_power": 0.3954, "prop1c_ihw_vs_oracle_power_gap": 0.00522, "prop1c_oracle_power": 0.4006}, "claim3_block_dependence_theorems3_4_and_examples1_2": {"example1_dishonest_wby_fdr": 1.0, "example1_honest_ihw_by_fdr": 0.012, "example2_adapt_by_exact_fdr_lower_bound": 0.2925, "example2_adapt_by_mc_fdr": 0.2938, "thm3_ihw_kbonf_kfwer": 0.016, "thm3_ihw_kbonf_power": 0.8829, "thm3_unweighted_kbonf_power": 0.7881, "thm4_ihw_by_fdr": 0.0083, "thm4_ihw_by_power": 0.8709, "thm4_unweighted_by_power": 0.7551}, "claim4_grenander_kkt_and_breaking_adapt_regimes": {"adapt_min_rejections_at_alpha_0_05": 20, "fdr_ihw_grenander_sparse_superuniform": 0.0454, "grenander_max_concavity_slope_violation": 0.0, "power_adapt_sparse_superuniform": 0.0, "power_ihw_grenander_sparse_superuniform": 0.8375, "power_unweighted_bh_sparse_superuniform": 0.7672, "sparse_m1_true_signals": 12}} |

## Scientific And Domain Assessments

### CovariatePoweredCrossWeightedMultipleTesting versus AdaptivePValueThresholding, SelectivelyTraversedAccumulationRulesForStructuredFDRControl, and ConditionalCalibrationForFalseDiscoveryRateControl

identity: supported. Targets: AIMech:CovariatePoweredCrossWeightedMultipleTesting.

Retain Covariate-powered cross-weighted multiple testing as a distinct DRAFT mathematical_method.

CovariatePoweredCrossWeightedMultipleTesting partitions hypotheses into K folds and learns out-of-fold covariate weights W_i = W_hat^{-ell}(X_i) via Grenander least-concave-majorant linear programming for weighted BH, weighted Storey, weighted k-Bonferroni, and weighted BY procedures (Theorems 1-4), whereas AdaptivePValueThresholding iteratively shrinks mirror-masked rejection thresholds on the full dataset, SelectivelyTraversedAccumulationRulesForStructuredFDRControl interactively peels structured candidate sets under accumulation-function masking, and ConditionalCalibrationForFalseDiscoveryRateControl calibrates thresholds by conditioning on exact null sufficiency statistics.

### Mapping to AIO:DataDredgingBias

grounding: supported. Targets: AIMech:CovariatePoweredCrossWeightedMultipleTesting.

Related mapping to DataDredgingBias is supported.

IHW prevents in-sample weight overfitting and false-discovery inflation (AIO:DataDredgingBias) when learning data-driven hypothesis weights from covariates by enforcing out-of-fold honesty across K disjoint hypothesis folds.

### honest-tau-censored-cross-weighting-finite-sample-fdr-control-and-uncensored-counterexample

evidence: supported. Targets: AIMech:CovariatePoweredCrossWeightedMultipleTesting.

Supported by Section 2.2-2.3 Algorithms 1-2, Section 3.1 Theorems 1-2, Corollary 1, and Supplement S1.1-S1.4.

Verified Supplement S1.3 exact uncensored honest counterexample FDR (0.216 vs. MC 0.212 &gt; 0.20, restored to 0.2023 &lt;= 0.20 under tau-censoring), Section 2.2 naive GBH global-null overfitting (0.2533 vs. IHW-GBH 0.065 &lt;= 0.10), and Theorem 1/2 power gains (IHW-Storey 0.8891 &gt; IHW-BH 0.8148 &gt; unweighted BH 0.7487).

### asymptotic-consistency-without-tau-censoring-and-zero-power-loss-from-fold-splitting

evidence: supported. Targets: AIMech:CovariatePoweredCrossWeightedMultipleTesting.

Supported by Section 3.2 Proposition 1, Corollary 2, and Supplement S2.1-S2.4.

Verified Proposition 1(a) full-sample Specification-7 overfitting (FDR = 0.7674 &gt; 0.15) vs. Proposition 1(b) uncensored cross-weighted FDR control (0.1331 &lt;= 0.15) and Proposition 1(c)/Corollary 2 convergence to oracle W* power (0.3954 vs. oracle 0.4006, gap 0.00522).

### block-dependent-fold-partitioning-for-finite-sample-kfwer-and-ihw-by-fdr-control

evidence: supported. Targets: AIMech:CovariatePoweredCrossWeightedMultipleTesting.

Supported by Section 3.3 Assumption 2, Lemma 1(a), Theorems 3-4, Examples 1-2, and Supplement S1.5-S1.6.

Verified Example 1 dishonest wBY failure (FDR = 1.0) and Example 2 AdaPT-BY failure (exact bound 0.2925, MC 0.2938 &gt; 0.10) vs. Theorem 3 IHW-k-Bonferroni k-FWER control (0.016 &lt;= 0.10, power 0.8829 &gt; 0.7881) and Theorem 4 IHW-BY FDR control (0.0083 &lt;= 0.10, power 0.8709 &gt; 0.7551).

### grenander-least-concave-majorant-convex-weight-optimization-and-sparse-superuniform-robustness

evidence: supported. Targets: AIMech:CovariatePoweredCrossWeightedMultipleTesting.

Supported by Section 4 Equations 8-12, Section 5.2 ('Breaking AdaPT'), and Supplement S4.1-S4.2 Algorithm 5.

Verified Grenander KKT concavity (violation 0.0) and sparse/super-uniform robustness where IHW-Grenander achieves power 0.8375 (FDR 0.0454 &lt;= 0.05) while AdaPT has power 0.0 due to its ceil(1/alpha) = 20 minimum-rejection floor.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:CovariatePoweredCrossWeightedMultipleTesting.

The full record is consistent; retain DRAFT.

Read every field of CovariatePoweredCrossWeightedMultipleTesting.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, three primary sources with exact SHA-256 digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T144500Z-covariate-powered-cross-weighted-multiple-testing.json | supports | No normalized identity match for covariate-powered cross-weighted multiple testing across 442 pinned AIO records and 587 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). DataDredgingBias provides out-of-fold cross-weighted false-discovery rate control context via related_match. |
| calculation | research/discovery/covariate-powered-cross-weighted-multiple-testing-boundaries.py | supports | Constructed analytical and numerical checks for honest + tau-censored finite-sample FDR control (Theorems 1-2) and the m=4 uncensored counterexample (Supplement S1.3), asymptotic consistency without tau-censoring and oracle power convergence (Proposition 1, Corollary 2), block-dependent k-FWER and IHW-BY FDR control (Theorems 3-4, Examples 1-2), and Grenander least-concave-majorant KKT weight optimization and sparse/super-uniform robustness (Sections 4 and 5.2). |
| ignatiadis2021-ihw-cross-weighting-ar5iv | https://ar5iv.labs.arxiv.org/html/1701.05179; Sections 1-8 and Supplement Sections S1-S6 (lines 1-2154, Algorithms 1-5, Theorems 1-4, Proposition 1, Corollaries 1-2) | supports | All 2,154 lines of the full-text ar5iv HTML conversion of arXiv:1701.05179v7 read. Checked all theorems, propositions, lemmas, examples, algorithms, and proofs across Sections 1-8 and Supplement S1-S6. |
| ignatiadis2021-ihw-cross-weighting-crossref | https://api.crossref.org/works/10.1111/rssb.12411; JRSS-B Vol. 83, Issue 4, pp. 720-751 publication record | supports | Official JRSS-B 83(4):720-751 Crossref record read and verified. |
| ignatiadis2021-ihw-cross-weighting-abs | https://arxiv.org/abs/1701.05179; arXiv:1701.05179v7 abstract and JRSS-B 2021 metadata | supports | arXiv:1701.05179v7 abstract and JRSS-B 2021 metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Covariate-powered cross-weighted multiple testing record, yielding 588 native and 442 unchanged generated records.
- All 2,154 lines of Ignatiadis &amp; Huber (2021, arXiv:1701.05179v7) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T144700Z-covariate-powered-cross-weighted-multiple-testing
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Covariate-powered cross-weighted multiple
  testing
started_at: '2026-10-17T14:45:00Z'
finished_at: '2026-10-17T14:47:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from AdaptivePValueThresholding,
    SelectivelyTraversedAccumulationRulesForStructuredFDRControl, and ConditionalCalibrationForFalseDiscoveryRateControl,
    the necessity of tau-censoring for finite-sample FDR control in Theorems 1-2 (Supplement
    S1.3), the domain-specific independent block-partitioning requirement under dependence
    in Theorems 3-4, and the covariate discretization requirements of Grenander LCM
    weight estimation. This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Covariate-powered cross-weighted multiple testing as a distinct DRAFT
  mathematical_method with a related DataDredgingBias mapping. All four claims and
  locators across Ignatiadis & Huber (2021 JRSS-B 83(4):720-751) are supported with
  explicit tau-censoring, independent-block fold partitioning, and covariate-discretization
  limitations.
source:
  git_revision: ab2f7f866cc1a668c8cd5a8fadd7f381737dbd11
  state: working_tree
  inputs:
  - path: data/aio/DataDredgingBias.yaml
    sha256: 335067e88f1462e141ac5f35e697cd42f7d250ec4dde9250531babe0d96cc1d0
    role: context
  - path: data/curated/ConditionalCalibrationForFalseDiscoveryRateControl.yaml
    sha256: 6167290e8178827ea950c80549426c871ba5e2b6d727b42b4a536d860e097946
    role: context
  - path: data/curated/CovariatePoweredCrossWeightedMultipleTesting.yaml
    sha256: 84d7094933c475533243366de9802790a89da87fb149ceffcb6ff304eacd3cf9
    role: target
  - path: data/curated/SelectivelyTraversedAccumulationRulesForStructuredFDRControl.yaml
    sha256: d701f5a7c2cc640bfc6cfa0d3fd87253f9f6a5f231a80bcaa14901dbf52486a9
    role: context
  - path: data/curated/SimultaneousPathwiseFalseDiscoveryProportionBounds.yaml
    sha256: 4eb73d4bf06e30006a686d5ead362dae952311a5d2e2ee7f62f43762849485de
    role: context
  - path: research/discovery/20261017T144500Z-covariate-powered-cross-weighted-multiple-testing.json
    sha256: f3eda8a99b4041a6aec8f16915638fc243e11d4806f571a419ec43139f42fcb3
    role: context
  - path: research/discovery/covariate-powered-cross-weighted-multiple-testing-boundaries.py
    sha256: 1d1be938e747200cda54c07cec039d6bd6c38c3881c99aca95c7fe396bcc035e
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
- target_id: AIMech:CovariatePoweredCrossWeightedMultipleTesting
  path: data/curated/CovariatePoweredCrossWeightedMultipleTesting.yaml
  label: Covariate-powered cross-weighted multiple testing
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CovariatePoweredCrossWeightedMultipleTesting.yaml
    role: maintained
scope:
  description: All fields of the exact maintained CovariatePoweredCrossWeightedMultipleTesting
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:CovariatePoweredCrossWeightedMultipleTesting'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:CovariatePoweredCrossWeightedMultipleTesting
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
  - AIMech:CovariatePoweredCrossWeightedMultipleTesting
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO concept records are valid.
- check_id: maintain-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:CovariatePoweredCrossWeightedMultipleTesting
  exit_code: 0
  expected_exit_code: 0
  summary: All 588 curated concept records are valid.
- check_id: maintain-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:CovariatePoweredCrossWeightedMultipleTesting
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO records match the pinned source.
- check_id: maintain-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:CovariatePoweredCrossWeightedMultipleTesting
  exit_code: 0
  expected_exit_code: 0
  summary: All history sidecars are valid.
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:CovariatePoweredCrossWeightedMultipleTesting
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW files are in sync.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:CovariatePoweredCrossWeightedMultipleTesting
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:CovariatePoweredCrossWeightedMultipleTesting
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed covariate-powered cross-weighted multiple testing checks
  command: python3 research/discovery/covariate-powered-cross-weighted-multiple-testing-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:CovariatePoweredCrossWeightedMultipleTesting
  exit_code: 0
  expected_exit_code: 0
  summary: '{"claim1_honest_tau_censored_fdr_and_counterexamples": {"fdr_ihw_bh_alt":
    0.0385, "fdr_ihw_gbh_global_null_G25": 0.065, "fdr_ihw_storey_alt": 0.0859, "fdr_naive_gbh_global_null_G25":
    0.2533, "power_ihw_bh_no_storey": 0.8148, "power_ihw_storey": 0.8891, "power_unweighted_bh":
    0.7487, "s13_exact_uncensored_honest_fdr": 0.216, "s13_mc_tau_censored_honest_fdr":
    0.2023, "s13_mc_uncensored_honest_fdr": 0.212}, "claim2_asymptotic_proposition1_and_corollary2":
    {"prop1a_naive_spec7_fdr": 0.7674, "prop1b_ihw_spec7_uncensored_fdr": 0.1331,
    "prop1c_gbh_power": 0.3978, "prop1c_ihw_gbh_uncensored_fdr": 0.0789, "prop1c_ihw_gbh_uncensored_power":
    0.3954, "prop1c_ihw_vs_oracle_power_gap": 0.00522, "prop1c_oracle_power": 0.4006},
    "claim3_block_dependence_theorems3_4_and_examples1_2": {"example1_dishonest_wby_fdr":
    1.0, "example1_honest_ihw_by_fdr": 0.012, "example2_adapt_by_exact_fdr_lower_bound":
    0.2925, "example2_adapt_by_mc_fdr": 0.2938, "thm3_ihw_kbonf_kfwer": 0.016, "thm3_ihw_kbonf_power":
    0.8829, "thm3_unweighted_kbonf_power": 0.7881, "thm4_ihw_by_fdr": 0.0083, "thm4_ihw_by_power":
    0.8709, "thm4_unweighted_by_power": 0.7551}, "claim4_grenander_kkt_and_breaking_adapt_regimes":
    {"adapt_min_rejections_at_alpha_0_05": 20, "fdr_ihw_grenander_sparse_superuniform":
    0.0454, "grenander_max_concavity_slope_violation": 0.0, "power_adapt_sparse_superuniform":
    0.0, "power_ihw_grenander_sparse_superuniform": 0.8375, "power_unweighted_bh_sparse_superuniform":
    0.7672, "sparse_m1_true_signals": 12}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T144500Z-covariate-powered-cross-weighted-multiple-testing.json
  accessed_at: '2026-10-17T14:45:00Z'
  support: supports
  summary: No normalized identity match for covariate-powered cross-weighted multiple
    testing across 442 pinned AIO records and 587 maintained IDs, names, aliases and
    scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T14:45:00Z'
  support: supports
  summary: Inspected DataDredgingBias in the pinned AIO snapshot (2026-07-22). DataDredgingBias
    provides out-of-fold cross-weighted false-discovery rate control context via related_match.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/covariate-powered-cross-weighted-multiple-testing-boundaries.py
  accessed_at: '2026-10-17T14:45:00Z'
  snapshot_sha256: 1d1be938e747200cda54c07cec039d6bd6c38c3881c99aca95c7fe396bcc035e
  support: supports
  summary: Constructed analytical and numerical checks for honest + tau-censored finite-sample
    FDR control (Theorems 1-2) and the m=4 uncensored counterexample (Supplement S1.3),
    asymptotic consistency without tau-censoring and oracle power convergence (Proposition
    1, Corollary 2), block-dependent k-FWER and IHW-BY FDR control (Theorems 3-4,
    Examples 1-2), and Grenander least-concave-majorant KKT weight optimization and
    sparse/super-uniform robustness (Sections 4 and 5.2).
- evidence_id: ignatiadis2021-ihw-cross-weighting-ar5iv
  kind: primary_source
  reference: https://ar5iv.labs.arxiv.org/html/1701.05179
  locator: Sections 1-8 and Supplement Sections S1-S6 (lines 1-2154, Algorithms 1-5,
    Theorems 1-4, Proposition 1, Corollaries 1-2)
  accessed_at: '2026-10-17T14:45:00Z'
  snapshot_sha256: 601c70dd0ebaa83c002b3882400ac8da8514ae8a54bf8a1c3a205c87d3080271
  support: supports
  summary: All 2,154 lines of the full-text ar5iv HTML conversion of arXiv:1701.05179v7
    read. Checked all theorems, propositions, lemmas, examples, algorithms, and proofs
    across Sections 1-8 and Supplement S1-S6.
- evidence_id: ignatiadis2021-ihw-cross-weighting-crossref
  kind: primary_source
  reference: https://api.crossref.org/works/10.1111/rssb.12411
  locator: JRSS-B Vol. 83, Issue 4, pp. 720-751 publication record
  accessed_at: '2026-10-17T14:45:00Z'
  snapshot_sha256: 3375754909898a3e6a4661ebd98b49507e8a988a4680c4d4d101299b749b4b45
  support: supports
  summary: Official JRSS-B 83(4):720-751 Crossref record read and verified.
- evidence_id: ignatiadis2021-ihw-cross-weighting-abs
  kind: primary_source
  reference: https://arxiv.org/abs/1701.05179
  locator: arXiv:1701.05179v7 abstract and JRSS-B 2021 metadata
  accessed_at: '2026-10-17T14:45:00Z'
  snapshot_sha256: 2c863b983bbb6aed7033dcf5b5bb109495f4ca455cf91458933f3ce93ed816fd
  support: supports
  summary: arXiv:1701.05179v7 abstract and JRSS-B 2021 metadata read and verified.
assessments:
- assessment_id: identity
  area: identity
  topic: CovariatePoweredCrossWeightedMultipleTesting versus AdaptivePValueThresholding,
    SelectivelyTraversedAccumulationRulesForStructuredFDRControl, and ConditionalCalibrationForFalseDiscoveryRateControl
  outcome: supported
  target_ids:
  - AIMech:CovariatePoweredCrossWeightedMultipleTesting
  evidence_ids:
  - identity
  - ignatiadis2021-ihw-cross-weighting-ar5iv
  - ignatiadis2021-ihw-cross-weighting-crossref
  summary: Retain Covariate-powered cross-weighted multiple testing as a distinct
    DRAFT mathematical_method.
  details: CovariatePoweredCrossWeightedMultipleTesting partitions hypotheses into
    K folds and learns out-of-fold covariate weights W_i = W_hat^{-ell}(X_i) via Grenander
    least-concave-majorant linear programming for weighted BH, weighted Storey, weighted
    k-Bonferroni, and weighted BY procedures (Theorems 1-4), whereas AdaptivePValueThresholding
    iteratively shrinks mirror-masked rejection thresholds on the full dataset, SelectivelyTraversedAccumulationRulesForStructuredFDRControl
    interactively peels structured candidate sets under accumulation-function masking,
    and ConditionalCalibrationForFalseDiscoveryRateControl calibrates thresholds by
    conditioning on exact null sufficiency statistics.
- assessment_id: mapping
  area: grounding
  topic: Mapping to AIO:DataDredgingBias
  outcome: supported
  target_ids:
  - AIMech:CovariatePoweredCrossWeightedMultipleTesting
  evidence_ids:
  - mapping
  - ignatiadis2021-ihw-cross-weighting-ar5iv
  summary: Related mapping to DataDredgingBias is supported.
  details: IHW prevents in-sample weight overfitting and false-discovery inflation
    (AIO:DataDredgingBias) when learning data-driven hypothesis weights from covariates
    by enforcing out-of-fold honesty across K disjoint hypothesis folds.
- assessment_id: honest-tau-censored-cross-weighting-finite-sample-fdr-control-and-uncensored-counterexample
  area: evidence
  topic: honest-tau-censored-cross-weighting-finite-sample-fdr-control-and-uncensored-counterexample
  outcome: supported
  target_ids:
  - AIMech:CovariatePoweredCrossWeightedMultipleTesting
  evidence_ids:
  - ignatiadis2021-ihw-cross-weighting-ar5iv
  - ignatiadis2021-ihw-cross-weighting-abs
  - calculation
  summary: Supported by Section 2.2-2.3 Algorithms 1-2, Section 3.1 Theorems 1-2,
    Corollary 1, and Supplement S1.1-S1.4.
  details: Verified Supplement S1.3 exact uncensored honest counterexample FDR (0.216
    vs. MC 0.212 > 0.20, restored to 0.2023 <= 0.20 under tau-censoring), Section
    2.2 naive GBH global-null overfitting (0.2533 vs. IHW-GBH 0.065 <= 0.10), and
    Theorem 1/2 power gains (IHW-Storey 0.8891 > IHW-BH 0.8148 > unweighted BH 0.7487).
- assessment_id: asymptotic-consistency-without-tau-censoring-and-zero-power-loss-from-fold-splitting
  area: evidence
  topic: asymptotic-consistency-without-tau-censoring-and-zero-power-loss-from-fold-splitting
  outcome: supported
  target_ids:
  - AIMech:CovariatePoweredCrossWeightedMultipleTesting
  evidence_ids:
  - ignatiadis2021-ihw-cross-weighting-ar5iv
  - ignatiadis2021-ihw-cross-weighting-crossref
  - calculation
  summary: Supported by Section 3.2 Proposition 1, Corollary 2, and Supplement S2.1-S2.4.
  details: Verified Proposition 1(a) full-sample Specification-7 overfitting (FDR
    = 0.7674 > 0.15) vs. Proposition 1(b) uncensored cross-weighted FDR control (0.1331
    <= 0.15) and Proposition 1(c)/Corollary 2 convergence to oracle W* power (0.3954
    vs. oracle 0.4006, gap 0.00522).
- assessment_id: block-dependent-fold-partitioning-for-finite-sample-kfwer-and-ihw-by-fdr-control
  area: evidence
  topic: block-dependent-fold-partitioning-for-finite-sample-kfwer-and-ihw-by-fdr-control
  outcome: supported
  target_ids:
  - AIMech:CovariatePoweredCrossWeightedMultipleTesting
  evidence_ids:
  - ignatiadis2021-ihw-cross-weighting-ar5iv
  - calculation
  summary: Supported by Section 3.3 Assumption 2, Lemma 1(a), Theorems 3-4, Examples
    1-2, and Supplement S1.5-S1.6.
  details: Verified Example 1 dishonest wBY failure (FDR = 1.0) and Example 2 AdaPT-BY
    failure (exact bound 0.2925, MC 0.2938 > 0.10) vs. Theorem 3 IHW-k-Bonferroni
    k-FWER control (0.016 <= 0.10, power 0.8829 > 0.7881) and Theorem 4 IHW-BY FDR
    control (0.0083 <= 0.10, power 0.8709 > 0.7551).
- assessment_id: grenander-least-concave-majorant-convex-weight-optimization-and-sparse-superuniform-robustness
  area: evidence
  topic: grenander-least-concave-majorant-convex-weight-optimization-and-sparse-superuniform-robustness
  outcome: supported
  target_ids:
  - AIMech:CovariatePoweredCrossWeightedMultipleTesting
  evidence_ids:
  - ignatiadis2021-ihw-cross-weighting-ar5iv
  - calculation
  summary: Supported by Section 4 Equations 8-12, Section 5.2 ('Breaking AdaPT'),
    and Supplement S4.1-S4.2 Algorithm 5.
  details: Verified Grenander KKT concavity (violation 0.0) and sparse/super-uniform
    robustness where IHW-Grenander achieves power 0.8375 (FDR 0.0454 <= 0.05) while
    AdaPT has power 0.0 due to its ceil(1/alpha) = 20 minimum-rejection floor.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:CovariatePoweredCrossWeightedMultipleTesting
  evidence_ids:
  - identity
  - mapping
  - ignatiadis2021-ihw-cross-weighting-ar5iv
  - ignatiadis2021-ihw-cross-weighting-crossref
  - ignatiadis2021-ihw-cross-weighting-abs
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of CovariatePoweredCrossWeightedMultipleTesting.yaml:
    stable ID, name, aliases, mathematical_method kind, definition, definition_evidence,
    identity_notes, four claims and locators, three primary sources with exact SHA-256
    digests, pinned AIO mapping and rationale, four scoped limitations, and UTC curation
    metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Covariate-powered cross-weighted multiple testing record, yielding
  588 native and 442 unchanged generated records.
- All 2,154 lines of Ignatiadis & Huber (2021, arXiv:1701.05179v7) were read in full
  text.
related_reviews: []
links: []
tags:
- native-concepts
- multiple-testing
- false-discovery-rate
- cross-weighting
- covariate-assisted-testing
- grenander-estimator
- self-review
- discovery-ongoing
```
