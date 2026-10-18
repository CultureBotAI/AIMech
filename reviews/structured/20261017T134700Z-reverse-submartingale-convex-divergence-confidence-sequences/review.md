# Scientific author self-review of Reverse-submartingale confidence sequences for convex divergences and functionals

- Review: 20261017T134700Z-reverse-submartingale-convex-divergence-confidence-sequences
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-17T13:45:00Z
- Finished UTC: 2026-10-17T13:47:00Z
- Reviewer: Antigravity (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Reverse-submartingale confidence sequences for convex divergences and functionals as a distinct DRAFT mathematical_method with related DataDredgingBias and TimeSeriesAnalysis mappings. All four claims and locators across Manole &amp; Ramdas (2023 IEEE TIT 69(7):4641-4658) are supported with explicit finite-sample plug-in bias, dimension-dependent smoothing prefactor, and attained variational-supremum limitations.

## Scope And Provenance

All fields of the exact maintained ReverseSubmartingaleConvexDivergenceConfidenceSequences record and its primary evidence.

Selection: Exact maintained ID: AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 393a120638155fc277c601a762624118a02ce418.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences | data/curated/ReverseSubmartingaleConvexDivergenceConfidenceSequences.yaml | maintained | Reverse-submartingale confidence sequences for convex divergences and functionals |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| aimech validate | passed | True | AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences | All 442 AIO concept records are valid. |
| aimech validate-curated | passed | True | AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences | All 582 curated concept records are valid. |
| aimech seed --check | passed | True | AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences | All 442 AIO records match the pinned source. |
| aimech validate-history | passed | True | AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences | All history sidecars are valid. |
| bash scripts/check_vendored_sync.sh | passed | True | AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences | Vendored CLAW files are in sync. |
| aimech check-source | passed | True | AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences | Pinned AIO source metadata matches. |
| git diff --check | passed | True | AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences | Exited 0 without output. |
| Constructed reverse-submartingale convex divergence confidence sequences checks | passed | True | AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences | {"claim1_reverse_submartingale_loo_and_ville_inequality": {"max_emp_measure_reverse_martingale_diff": 0.0, "max_ustat_neg_kernel_loo_diff": 0.0, "min_kl_loo_excess": 0.0, "min_tv_loo_excess": 0.0, "min_vstat_neg_kernel_loo_excess": -0.04, "min_vstat_psd_loo_excess": 0.0, "ville_empirical_exceed_prob": 0.042, "ville_theoretical_upper_bound": 0.2786}, "claim2_two_sample_ks_cs_and_stopping_time_upward_bias": {"mean_stopped_plugin_ks": 0.6034, "true_ks_distance": 0.25, "two_sample_ks_cs_simultaneous_coverage": 1.0, "upward_bias_at_stopping_time": 0.3534}, "claim3_discrete_divergences_and_gaussian_smoothing": {"discrete_tv_cs_violation_rate": 0.0, "smoothed_tv_cs_violation_rate": 0.0, "smoothed_tv_mean_at_t10": 0.1016, "smoothed_tv_mean_at_t200": 0.0192, "unsmoothed_continuous_tv": 1.0}, "claim4_rademacher_loo_and_forward_supermartingale_failure": {"forward_supermartingale_asymptotic_width_limit": 1.029653, "min_rademacher_loo_excess": 1e-16, "reverse_submartingale_kl_bound_at_t500": 0.066883}} |

## Scientific And Domain Assessments

### ReverseSubmartingaleConvexDivergenceConfidenceSequences versus SubPsiUniformBoundaryConfidenceSequences and NonparametricTwoSampleTestingByBetting

identity: supported. Targets: AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences.

Retain Reverse-submartingale confidence sequences for convex divergences and functionals as a distinct DRAFT mathematical_method.

ReverseSubmartingaleConvexDivergenceConfidenceSequences operates on reverse exchangeable filtrations E_t^X and partially ordered filtrations E_{ts} = E_t^X vee E_s^Y to construct two-sided time-uniform confidence sequences for nonlinear convex functionals and two-sample divergences, whereas forward canonical-filtration supermartingales fail to yield vanishing width for convex divergences (Appendix E Lemma 32) and betting tests target point-null rejection.

### Mappings to AIO:DataDredgingBias and AIO:TimeSeriesAnalysis

grounding: supported. Targets: AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences.

Related mappings to DataDredgingBias and TimeSeriesAnalysis are supported.

Reverse-submartingale confidence sequences bound and correct stopping-time upward plug-in bias under arbitrary optional stopping in N^2 (Corollary 10, Proposition 12; AIO:DataDredgingBias) and track divergences across sequential observation streams (AIO:TimeSeriesAnalysis).

### exchangeable-filtration-reverse-submartingale-loo-and-partially-ordered-ville-inequality

evidence: supported. Targets: AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences.

Supported by Section 2.1 Lemma 1, Section 2.3-2.4 Definition 1, Theorem 2, Proposition 3, Section 3.1 Theorem 4, Proposition 5, and Section 4.2 Proposition 16.

Verified exact reverse-martingale identity for empirical measures (max diff 0.0), leave-one-out reverse-submartingale nonnegativity for KL (0.0), TV (0.0), and PSD V-statistics (0.0) vs. negative excess (-0.04) for non-PSD hollow-kernel V-statistics and exact equality (0.0) for U-statistics, and Ville's reverse maximal inequality (0.042 &lt;= 0.2786).

### reverse-cramer-chernoff-geometric-epoch-stitching-variational-minorant-and-stopping-time-bias

evidence: supported. Targets: AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences.

Supported by Section 3.1 Proposition 6, Theorem 7, Corollary 8, Section 3.2 Proposition 9, Corollaries 10-11, Section 3.3 Proposition 12, and Section 4.1-4.2 Corollaries 13-15.

Verified positive stopping-time upward bias of plug-in two-sample KS distance (mean stopped KS 0.6034 vs. true KS 0.25, bias +0.3534) and 1.0 &gt;= 0.90 simultaneous coverage of the two-sample reverse-stitched KS confidence sequence.

### finite-support-phi-divergences-optimal-transport-and-gaussian-smoothed-parametric-rates

evidence: supported. Targets: AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences.

Supported by Section 4.3 Corollary 17, Section 4.4 Proposition 18, Corollary 19, and Section 4.5 Proposition 20, Corollary 21.

Verified 0.0 violation rate for discrete TV confidence sequences (Corollary 19), degeneracy of unsmoothed continuous empirical TV (1.0), and O(t^{-1/2}) decay of Gaussian-smoothed empirical TV from 0.1016 (t=10) to 0.0192 (t=200) with 0.0 violation rate against Proposition 20(i).

### rademacher-generalization-norm-estimation-upper-lil-and-forward-supermartingale-failure

evidence: supported. Targets: AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences.

Supported by Section 4.6-4.8 Corollaries 22-24 and Appendix E Lemmas 32-33, Theorem 34.

Verified exact leave-one-out reverse-submartingale inequality for empirical Rademacher complexity (min excess 1e-16 &gt;= 0) and non-vanishing asymptotic width limit H(P) = 1.029653 for forward canonical-filtration supermartingales vs. 0.066883 at t=500 for the reverse-submartingale KL bound.

### Complete maintained record, source locators and mirrored report

provenance: supported. Targets: AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences.

The full record is consistent; retain DRAFT.

Read every field of ReverseSubmartingaleConvexDivergenceConfidenceSequences.yaml: stable ID, name, aliases, mathematical_method kind, definition, definition_evidence, identity_notes, four claims and locators, three primary sources with exact SHA-256 digests, two pinned AIO mappings and rationales, four scoped limitations, and UTC curation metadata.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261017T134500Z-reverse-submartingale-convex-divergence-confidence-sequences.json | supports | No normalized identity match for reverse-submartingale confidence sequences for convex divergences and functionals across 442 pinned AIO records and 581 maintained IDs, names, aliases and scoped synonyms. |
| mapping | sources/aio/aio.json | supports | Inspected DataDredgingBias, TimeSeriesAnalysis, and SupportVectorMachine in the pinned AIO snapshot (2026-07-22). DataDredgingBias and TimeSeriesAnalysis provide optional-stopping and sequential-stream context via related_match. |
| calculation | research/discovery/reverse-submartingale-convex-divergence-confidence-sequences-boundaries.py | supports | Constructed analytical and numerical checks for the exchangeable-filtration reverse-submartingale leave-one-out inequality, Ville's reverse maximal inequality, two-sample KS confidence sequence coverage and stopping-time upward bias, discrete and Gaussian-smoothed TV confidence sequences, empirical Rademacher complexity LOO submartingale property, and Appendix E forward-supermartingale failure. |
| manole2023-reverse-submartingale-ar5iv | https://ar5iv.labs.arxiv.org/html/2103.09267; Sections 1-5 and Appendices A-E (lines 1-2502, Lemma 1, Definition 1, Theorems 2, 4, 7, 28, 34, Propositions 3, 5, 6, 9, 12, 16, 18, 20, 29, Corollaries 8, 10, 11, 13-15, 17, 19, 21-24, Lemmas 27, 31-33) | supports | All 2,502 lines of the full-text ar5iv HTML conversion of arXiv:2103.09267v4 read. Checked all theorems, propositions, corollaries, and proofs across Sections 1-5 and Appendices A-E. |
| manole2023-reverse-submartingale-crossref | https://api.crossref.org/works/10.1109/TIT.2023.3250099; IEEE Transactions on Information Theory Vol. 69, Issue 7, pp. 4641-4658 publication record | supports | Official IEEE Transactions on Information Theory 69(7):4641-4658 Crossref record read and verified. |
| manole2023-reverse-submartingale-abs | https://arxiv.org/abs/2103.09267; arXiv:2103.09267v4 abstract and IEEE TIT 2023 metadata | supports | arXiv:2103.09267v4 abstract and IEEE TIT 2023 metadata read and verified. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion. No issue was manufactured for a clean review.
- Added one DRAFT Reverse-submartingale confidence sequences for convex divergences and functionals record, yielding 582 native and 442 unchanged generated records.
- All 2,502 lines of Manole &amp; Ramdas (2023, arXiv:2103.09267v4) were read in full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T134700Z-reverse-submartingale-convex-divergence-confidence-sequences
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Reverse-submartingale confidence sequences
  for convex divergences and functionals
started_at: '2026-10-17T13:45:00Z'
finished_at: '2026-10-17T13:47:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: Gemini
  independence: self_review
  independence_basis: The author challenged definition distinctness from SubPsiUniformBoundaryConfidenceSequences
    and NonparametricTwoSampleTestingByBetting, the necessity of known finite-sample
    expected plug-in bias upper bounds E[Phi(P_{ceil(t/2)}) - Phi(P)] in Theorem 7
    and Corollary 8, the exponential-in-dimension prefactors c_d and C_d in Gaussian-smoothed
    divergence bounds (Proposition 20), and the requirement of attained variational
    suprema for upper confidence sequences (Proposition 9, Corollary 11, Corollary
    22). This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Reverse-submartingale confidence sequences for convex divergences
  and functionals as a distinct DRAFT mathematical_method with related DataDredgingBias
  and TimeSeriesAnalysis mappings. All four claims and locators across Manole & Ramdas
  (2023 IEEE TIT 69(7):4641-4658) are supported with explicit finite-sample plug-in
  bias, dimension-dependent smoothing prefactor, and attained variational-supremum
  limitations.
source:
  git_revision: 393a120638155fc277c601a762624118a02ce418
  state: working_tree
  inputs:
  - path: data/aio/DataDredgingBias.yaml
    sha256: 335067e88f1462e141ac5f35e697cd42f7d250ec4dde9250531babe0d96cc1d0
    role: context
  - path: data/aio/SupportVectorMachine.yaml
    sha256: 0cc2faa913fdafdc539a7d04d08d26c0963f77ad3ca26b833b29ed3ed313e4e0
    role: context
  - path: data/aio/TimeSeriesAnalysis.yaml
    sha256: c26b267d0f5fb895e9cb0eb587fe86a115d461dae4d70e0ac6baf1eefb1d4eff
    role: context
  - path: data/curated/BettingConfidenceSequencesForBoundedMeans.yaml
    sha256: b7a7f4290f77d5f8152269f60afdaa354defb0251adccd88be92f055839249c7
    role: context
  - path: data/curated/CatoniStyleHeavyTailedConfidenceSequences.yaml
    sha256: 5b4dc96917166cb9c70ab7d896501c5f167f5495329e712584ff212feff5b126
    role: context
  - path: data/curated/HuberRobustHeavyTailedConfidenceSequences.yaml
    sha256: bbc3017a6bdb3fc69cc076792b14903903a71dda687e467e3961e187340da36a
    role: context
  - path: data/curated/NonparametricTwoSampleTestingByBetting.yaml
    sha256: 5c119acd76a48be2ae886b4ebcbcc952d5f4269de14ce3dece35766648d417ac
    role: context
  - path: data/curated/ReverseSubmartingaleConvexDivergenceConfidenceSequences.yaml
    sha256: 7ab66808e86837214be02e6ca9183a7ebd19df51f6c6dbd9ddadfd84a1d81afe
    role: target
  - path: data/curated/SequentialKernelizedIndependenceTestingByBetting.yaml
    sha256: 13d50b1f150eec5c72de7b682597b072d55c89440d57ca0e2585bdf2b2d561d9
    role: context
  - path: data/curated/SequentialNonparametricQuantileConfidenceSequences.yaml
    sha256: a3d72fae22daf9b8ad6d2049df0f3e79ce5b8ff72bb829ed14b162853030dc11
    role: context
  - path: data/curated/SubPsiUniformBoundaryConfidenceSequences.yaml
    sha256: 8ad6737fae460a74a9f3c534284689f281dee04b225a5674ce91eb8488d3976a
    role: context
  - path: research/discovery/20261017T134500Z-reverse-submartingale-convex-divergence-confidence-sequences.json
    sha256: 2fff505a34b1d21a367768a6dbcb5915e04c7c270217b8ad36f7b3da4e1301f8
    role: context
  - path: research/discovery/reverse-submartingale-convex-divergence-confidence-sequences-boundaries.py
    sha256: 3be3507b60779fcaa44006e746083168f4f2f2c7cfa45571f31f54ea702bcb2b
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
- target_id: AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences
  path: data/curated/ReverseSubmartingaleConvexDivergenceConfidenceSequences.yaml
  label: Reverse-submartingale confidence sequences for convex divergences and functionals
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ReverseSubmartingaleConvexDivergenceConfidenceSequences.yaml
    role: maintained
scope:
  description: All fields of the exact maintained ReverseSubmartingaleConvexDivergenceConfidenceSequences
    record and its primary evidence.
  selection: 'Exact maintained ID: AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences
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
  - AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO concept records are valid.
- check_id: maintain-2
  name: aimech validate-curated
  command: aimech validate-curated
  status: passed
  required: true
  target_ids:
  - AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: All 582 curated concept records are valid.
- check_id: maintain-3
  name: aimech seed --check
  command: aimech seed --check
  status: passed
  required: true
  target_ids:
  - AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: All 442 AIO records match the pinned source.
- check_id: maintain-4
  name: aimech validate-history
  command: aimech validate-history
  status: passed
  required: true
  target_ids:
  - AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: All history sidecars are valid.
- check_id: required-1
  name: bash scripts/check_vendored_sync.sh
  command: bash scripts/check_vendored_sync.sh
  status: passed
  required: true
  target_ids:
  - AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: Vendored CLAW files are in sync.
- check_id: required-2
  name: aimech check-source
  command: aimech check-source
  status: passed
  required: true
  target_ids:
  - AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: Pinned AIO source metadata matches.
- check_id: required-3
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  target_ids:
  - AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: Exited 0 without output.
- check_id: calculation
  name: Constructed reverse-submartingale convex divergence confidence sequences checks
  command: python3 research/discovery/reverse-submartingale-convex-divergence-confidence-sequences-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences
  exit_code: 0
  expected_exit_code: 0
  summary: '{"claim1_reverse_submartingale_loo_and_ville_inequality": {"max_emp_measure_reverse_martingale_diff":
    0.0, "max_ustat_neg_kernel_loo_diff": 0.0, "min_kl_loo_excess": 0.0, "min_tv_loo_excess":
    0.0, "min_vstat_neg_kernel_loo_excess": -0.04, "min_vstat_psd_loo_excess": 0.0,
    "ville_empirical_exceed_prob": 0.042, "ville_theoretical_upper_bound": 0.2786},
    "claim2_two_sample_ks_cs_and_stopping_time_upward_bias": {"mean_stopped_plugin_ks":
    0.6034, "true_ks_distance": 0.25, "two_sample_ks_cs_simultaneous_coverage": 1.0,
    "upward_bias_at_stopping_time": 0.3534}, "claim3_discrete_divergences_and_gaussian_smoothing":
    {"discrete_tv_cs_violation_rate": 0.0, "smoothed_tv_cs_violation_rate": 0.0, "smoothed_tv_mean_at_t10":
    0.1016, "smoothed_tv_mean_at_t200": 0.0192, "unsmoothed_continuous_tv": 1.0},
    "claim4_rademacher_loo_and_forward_supermartingale_failure": {"forward_supermartingale_asymptotic_width_limit":
    1.029653, "min_rademacher_loo_excess": 1e-16, "reverse_submartingale_kl_bound_at_t500":
    0.066883}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261017T134500Z-reverse-submartingale-convex-divergence-confidence-sequences.json
  accessed_at: '2026-10-17T13:45:00Z'
  support: supports
  summary: No normalized identity match for reverse-submartingale confidence sequences
    for convex divergences and functionals across 442 pinned AIO records and 581 maintained
    IDs, names, aliases and scoped synonyms.
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text fixed-string searches across data, sources, research, history,
    and reviews including ignored and hidden files.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-17T13:45:00Z'
  support: supports
  summary: Inspected DataDredgingBias, TimeSeriesAnalysis, and SupportVectorMachine
    in the pinned AIO snapshot (2026-07-22). DataDredgingBias and TimeSeriesAnalysis
    provide optional-stopping and sequential-stream context via related_match.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/reverse-submartingale-convex-divergence-confidence-sequences-boundaries.py
  accessed_at: '2026-10-17T13:45:00Z'
  snapshot_sha256: 3be3507b60779fcaa44006e746083168f4f2f2c7cfa45571f31f54ea702bcb2b
  support: supports
  summary: Constructed analytical and numerical checks for the exchangeable-filtration
    reverse-submartingale leave-one-out inequality, Ville's reverse maximal inequality,
    two-sample KS confidence sequence coverage and stopping-time upward bias, discrete
    and Gaussian-smoothed TV confidence sequences, empirical Rademacher complexity
    LOO submartingale property, and Appendix E forward-supermartingale failure.
- evidence_id: manole2023-reverse-submartingale-ar5iv
  kind: primary_source
  reference: https://ar5iv.labs.arxiv.org/html/2103.09267
  locator: Sections 1-5 and Appendices A-E (lines 1-2502, Lemma 1, Definition 1, Theorems
    2, 4, 7, 28, 34, Propositions 3, 5, 6, 9, 12, 16, 18, 20, 29, Corollaries 8, 10,
    11, 13-15, 17, 19, 21-24, Lemmas 27, 31-33)
  accessed_at: '2026-10-17T13:45:00Z'
  snapshot_sha256: 473bd824958b260761bdac2383a11e13f12e0f864dad5a097da3de03b9c331fe
  support: supports
  summary: All 2,502 lines of the full-text ar5iv HTML conversion of arXiv:2103.09267v4
    read. Checked all theorems, propositions, corollaries, and proofs across Sections
    1-5 and Appendices A-E.
- evidence_id: manole2023-reverse-submartingale-crossref
  kind: primary_source
  reference: https://api.crossref.org/works/10.1109/TIT.2023.3250099
  locator: IEEE Transactions on Information Theory Vol. 69, Issue 7, pp. 4641-4658
    publication record
  accessed_at: '2026-10-17T13:45:00Z'
  snapshot_sha256: 2f4bded756bd8507874158acca0883f29751d3f8a6d6a51d45246a916410bc21
  support: supports
  summary: Official IEEE Transactions on Information Theory 69(7):4641-4658 Crossref
    record read and verified.
- evidence_id: manole2023-reverse-submartingale-abs
  kind: primary_source
  reference: https://arxiv.org/abs/2103.09267
  locator: arXiv:2103.09267v4 abstract and IEEE TIT 2023 metadata
  accessed_at: '2026-10-17T13:45:00Z'
  snapshot_sha256: 8fb54fe7ac0e37f396fa80bd29283642c1b46b70567b3dac986fb3aea0b53050
  support: supports
  summary: arXiv:2103.09267v4 abstract and IEEE TIT 2023 metadata read and verified.
assessments:
- assessment_id: identity
  area: identity
  topic: ReverseSubmartingaleConvexDivergenceConfidenceSequences versus SubPsiUniformBoundaryConfidenceSequences
    and NonparametricTwoSampleTestingByBetting
  outcome: supported
  target_ids:
  - AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences
  evidence_ids:
  - identity
  - manole2023-reverse-submartingale-ar5iv
  - manole2023-reverse-submartingale-crossref
  summary: Retain Reverse-submartingale confidence sequences for convex divergences
    and functionals as a distinct DRAFT mathematical_method.
  details: ReverseSubmartingaleConvexDivergenceConfidenceSequences operates on reverse
    exchangeable filtrations E_t^X and partially ordered filtrations E_{ts} = E_t^X
    vee E_s^Y to construct two-sided time-uniform confidence sequences for nonlinear
    convex functionals and two-sample divergences, whereas forward canonical-filtration
    supermartingales fail to yield vanishing width for convex divergences (Appendix
    E Lemma 32) and betting tests target point-null rejection.
- assessment_id: mapping
  area: grounding
  topic: Mappings to AIO:DataDredgingBias and AIO:TimeSeriesAnalysis
  outcome: supported
  target_ids:
  - AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences
  evidence_ids:
  - mapping
  - manole2023-reverse-submartingale-ar5iv
  summary: Related mappings to DataDredgingBias and TimeSeriesAnalysis are supported.
  details: Reverse-submartingale confidence sequences bound and correct stopping-time
    upward plug-in bias under arbitrary optional stopping in N^2 (Corollary 10, Proposition
    12; AIO:DataDredgingBias) and track divergences across sequential observation
    streams (AIO:TimeSeriesAnalysis).
- assessment_id: exchangeable-filtration-reverse-submartingale-loo-and-partially-ordered-ville-inequality
  area: evidence
  topic: exchangeable-filtration-reverse-submartingale-loo-and-partially-ordered-ville-inequality
  outcome: supported
  target_ids:
  - AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences
  evidence_ids:
  - manole2023-reverse-submartingale-ar5iv
  - manole2023-reverse-submartingale-abs
  - calculation
  summary: Supported by Section 2.1 Lemma 1, Section 2.3-2.4 Definition 1, Theorem
    2, Proposition 3, Section 3.1 Theorem 4, Proposition 5, and Section 4.2 Proposition
    16.
  details: Verified exact reverse-martingale identity for empirical measures (max
    diff 0.0), leave-one-out reverse-submartingale nonnegativity for KL (0.0), TV
    (0.0), and PSD V-statistics (0.0) vs. negative excess (-0.04) for non-PSD hollow-kernel
    V-statistics and exact equality (0.0) for U-statistics, and Ville's reverse maximal
    inequality (0.042 <= 0.2786).
- assessment_id: reverse-cramer-chernoff-geometric-epoch-stitching-variational-minorant-and-stopping-time-bias
  area: evidence
  topic: reverse-cramer-chernoff-geometric-epoch-stitching-variational-minorant-and-stopping-time-bias
  outcome: supported
  target_ids:
  - AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences
  evidence_ids:
  - manole2023-reverse-submartingale-ar5iv
  - manole2023-reverse-submartingale-crossref
  - calculation
  summary: Supported by Section 3.1 Proposition 6, Theorem 7, Corollary 8, Section
    3.2 Proposition 9, Corollaries 10-11, Section 3.3 Proposition 12, and Section
    4.1-4.2 Corollaries 13-15.
  details: Verified positive stopping-time upward bias of plug-in two-sample KS distance
    (mean stopped KS 0.6034 vs. true KS 0.25, bias +0.3534) and 1.0 >= 0.90 simultaneous
    coverage of the two-sample reverse-stitched KS confidence sequence.
- assessment_id: finite-support-phi-divergences-optimal-transport-and-gaussian-smoothed-parametric-rates
  area: evidence
  topic: finite-support-phi-divergences-optimal-transport-and-gaussian-smoothed-parametric-rates
  outcome: supported
  target_ids:
  - AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences
  evidence_ids:
  - manole2023-reverse-submartingale-ar5iv
  - calculation
  summary: Supported by Section 4.3 Corollary 17, Section 4.4 Proposition 18, Corollary
    19, and Section 4.5 Proposition 20, Corollary 21.
  details: Verified 0.0 violation rate for discrete TV confidence sequences (Corollary
    19), degeneracy of unsmoothed continuous empirical TV (1.0), and O(t^{-1/2}) decay
    of Gaussian-smoothed empirical TV from 0.1016 (t=10) to 0.0192 (t=200) with 0.0
    violation rate against Proposition 20(i).
- assessment_id: rademacher-generalization-norm-estimation-upper-lil-and-forward-supermartingale-failure
  area: evidence
  topic: rademacher-generalization-norm-estimation-upper-lil-and-forward-supermartingale-failure
  outcome: supported
  target_ids:
  - AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences
  evidence_ids:
  - manole2023-reverse-submartingale-ar5iv
  - calculation
  summary: Supported by Section 4.6-4.8 Corollaries 22-24 and Appendix E Lemmas 32-33,
    Theorem 34.
  details: Verified exact leave-one-out reverse-submartingale inequality for empirical
    Rademacher complexity (min excess 1e-16 >= 0) and non-vanishing asymptotic width
    limit H(P) = 1.029653 for forward canonical-filtration supermartingales vs. 0.066883
    at t=500 for the reverse-submartingale KL bound.
- assessment_id: complete-fields
  area: provenance
  topic: Complete maintained record, source locators and mirrored report
  outcome: supported
  target_ids:
  - AIMech:ReverseSubmartingaleConvexDivergenceConfidenceSequences
  evidence_ids:
  - identity
  - mapping
  - manole2023-reverse-submartingale-ar5iv
  - manole2023-reverse-submartingale-crossref
  - manole2023-reverse-submartingale-abs
  - calculation
  summary: The full record is consistent; retain DRAFT.
  details: 'Read every field of ReverseSubmartingaleConvexDivergenceConfidenceSequences.yaml:
    stable ID, name, aliases, mathematical_method kind, definition, definition_evidence,
    identity_notes, four claims and locators, three primary sources with exact SHA-256
    digests, two pinned AIO mappings and rationales, four scoped limitations, and
    UTC curation metadata.'
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion. No issue was
  manufactured for a clean review.
- Added one DRAFT Reverse-submartingale confidence sequences for convex divergences
  and functionals record, yielding 582 native and 442 unchanged generated records.
- All 2,502 lines of Manole & Ramdas (2023, arXiv:2103.09267v4) were read in full
  text.
related_reviews: []
links: []
tags:
- native-concepts
- confidence-sequences
- reverse-submartingales
- convex-divergences
- optimal-transport
- anytime-valid-inference
- self-review
- discovery-ongoing
```
