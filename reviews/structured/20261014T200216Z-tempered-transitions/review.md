# Scientific author self-review of Tempered transitions

- Review: 20261014T200216Z-tempered-transitions
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-14T19:57:45Z
- Finished UTC: 2026-10-14T20:02:16Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain tempered transitions as DRAFT with a related Markov-process mapping. Primary equations and exact finite calculations support the scoped transition, while mixing, implementation and source-version limitations remain explicit.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:TemperedTransitions
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c924f97a3db72c41c068391adbbd8fd3690d5740.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:TemperedTransitions | data/curated/TemperedTransitions.yaml | maintained | Tempered transitions |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:TemperedTransitions | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 437.22s (0:07:17)<br>Checked 442 record(s); 0 failed.<br>Checked 701 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 392 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 393,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:TemperedTransitions | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:TemperedTransitions | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:TemperedTransitions | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:TemperedTransitions | {"target": ["1/10", "1/5", "7/10"], "correct_path_kernel": [["7/27", "7/27", "13/27"], ["7/54", "7/18", "13/27"], ["13/189", "26/189", "50/63"]], "independent_density_scales_cancel": true, "endpoint_only_acceptance": {"kernel": [["1/6", "1/3", "1/2"], ["1/12", "5/12", "1/2"], ["1/42", "2/21", "37/42"]], "target_after_one_step": ["1/20", "11/60", "23/30"]}, "wrong_same_nonreversible_directions": {"kernel": [["0", "0", "1"], ["1/2", "1/2", "0"], ["0", "2/7", "5/7"]], "target_after_one_step": ["1/10", "3/10", "3/5"]}, "correct_cycle_reverse_is_identity": true, "finite_invariant_family_cases": 72, "scope": "Exact finite path enumeration, including rejection self-loops. No author-code or benchmark replication, universal efficiency bound, guarantee of ergodicity or numerical implementation audit."} |

## Scientific And Domain Assessments

### Tempered transitions

identity: supported. Targets: AIMech:TemperedTransitions.

Retain this distinct DRAFT algorithm.

Retain the full outward/return accept/reject kernel as one algorithm. It differs from AIS weighted estimation, simultaneous replicas, random temperature-index evolution and tempered Hamiltonian trajectory modifications. The later backward normalizer estimator is an explicitly scoped extension rather than a duplicate transition record.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:TemperedTransitions.

The explicit AIO mapping assessment is supported within its stated scope.

Related MarkovChain connects the constructed target-preserving transition algorithm to the process/model. It is not equivalence or a Network/hidden-layer subclass assertion. Ten complete contexts reject incidental model applications, data normalization and bias labels. Five full native neighbors distinguish AIS, Metropolis–Hastings, parallel tempering, annealing optimization and ordinary HMC.

### auxiliary-kernel-pairs

evidence: supported. Targets: AIMech:TemperedTransitions.

Supported within the stated primary-source and mathematical scope.

Equation5 requires mutual reversal, not merely separate invariance. Reusing one kernel is valid when reversible; compositions need reversed update order. The nonreversible-cycle counterexample isolates this condition.

### path-and-acceptance

evidence: supported. Targets: AIMech:TemperedTransitions.

Supported within the stated primary-source and mathematical scope.

Both outermost kernels occur, totaling2n applications. Equation6 uses the full outward and return intermediate states, retains rejection self-loops and cancels each density normalizer. Endpoint-only correction is insufficient in the explicit refresh-kernel example.

### invariance-and-exploration

evidence: supported. Targets: AIMech:TemperedTransitions.

Supported within the stated primary-source and mathematical scope.

Pairing reversed complete paths establishes detailed balance, without implying ergodicity or rapid convergence. A fully accepted cycle/reverse pair returns the identity transition. The maintained regular case does not claim exact target sampling from arbitrary initialization.

### finite-path-balance-checks

evidence: supported. Targets: AIMech:TemperedTransitions.

Supported within the stated primary-source and mathematical scope.

Exact path enumeration reproduces the reported kernel, density-scale invariance and72 finite cases. Both incorrect alternatives move the target to the stated wrong distributions; these finite failures and identities are not universal performance results.

### temperature-and-method-boundaries

evidence: supported. Targets: AIMech:TemperedTransitions.

Supported within the stated primary-source and mathematical scope.

The source permits auxiliary families beyond canonical temperatures. Its Gaussian comparison and synthetic examples remain conditional. Existing HMC-variant and nonreversible-method leads retain separate scope instead of being declared resolved by this record.

### later-normalizer-extension

evidence: supported. Targets: AIMech:TemperedTransitions.

Supported within the stated primary-source and mathematical scope.

The unnumbered1994 comparison table records the then-unavailable estimate. AIS Equations28–29 subsequently provide backward weights over accepted and rejected attempts, with target-chain convergence/stationarity and variance/autocorrelation qualifications. The two sources are cited separately and the estimator is not confused with acceptance.

### mutual reversal, full-path acceptance, normalizer cancellation, identity transitions and version-specific normalizer-estimation claims

consistency: supported. Targets: AIMech:TemperedTransitions.

Constructed calculations support the stated distinctions.

Exact three-state full-path enumeration checks detailed balance, independent density rescaling and72 finite kernel cases. Counterexamples show why endpoint-only acceptance and using the same nonreversible cycle in both directions can fail; a fully accepted identity transition illustrates absence of an ergodicity guarantee.

### All maintained fields

provenance: supported. Targets: AIMech:TemperedTransitions.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. All six claims, aliases, definition, two source versions and precise locators, ten AIO contexts, five native neighbors, limitations and actual provenance assessed. The draft table label was corrected to unnumbered before maintained creation, with separate evidence for the1994 comparison and1998 extension. Full-path acceptance and kernel reversal were checked against exact finite path enumeration.

### Draft correction before maintained creation

provenance: supported. Targets: AIMech:TemperedTransitions.

The draft table locator was corrected before this maintained record was created.

The1994 table is unnumbered and is cited separately from the1998 estimator extension. No fictitious maintained-record issue or independent-review approval is claimed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261014T194707Z-tempered-transitions.json | supports | Compared tempered transitions against all442 pinned AIO and700 native identities; no normalized match. Ignored- and hidden-inclusive searches of three full checkouts returned312,116,115 lines in24 unique content groups, all classified as the pending cohort or newly written AIS record/report, primary-source notes and queries. The23 new groups were read in full; the shared cohort line was retained from the earlier assessment. Semantic assessment covered103 AIO and307 native definitions: all103 and306 preceding rows verified unchanged, plus the new AIS row and maintained record read and its three corrections reassessed. Ten complete AIO contexts and five full native neighbors assessed. This identity is the full up/down Metropolis transition on one target state. It differs from weighted one-way AIS estimates, replica exchanges in parallel tempering, a temperature-index random walk in simulated tempering, annealing optimization, and tempered Hamiltonian trajectory modifications. |
| mapping | sources/aio/aio.json | supports | Related MarkovChain connects the constructed target-preserving transition algorithm to the process/model. It is not equivalence or a Network/hidden-layer subclass assertion. Ten complete contexts reject incidental model applications, data normalization and bias labels. Five full native neighbors distinguish AIS, Metropolis–Hastings, parallel tempering, annealing optimization and ordinary HMC. |
| neal1994tempered | https://glizen.com/radfordneal/ftp/ttrans.pdf; Section 3.1, PDF pp. 5–6, Equation 5, up/down construction and Equation 6; detailed-balance proof, Section 3.2, pp. 6–7; Section 3.1, PDF p. 5, Equation 5 and composition-order paragraph; Section 3.1, PDF pp. 5–6, explicit path construction and Equation 6; Section 3.2, PDF pp. 6–7, Equations 7–12; efficiency discussion, Sections 4–5; curator identity-transition example in research/discovery/tempered-boundaries.py; Equation 5, PDF p. 5; Equation 6, p. 6; full-path proof, pp. 6–7; exact independent enumeration in research/discovery/tempered-boundaries.py; General interpolating distributions, PDF pp. 3–4; Section 3.3, pp. 7–10; Sections 4–6, pp. 10–21; Unnumbered comparison table and accompanying discussion, PDF p. 20 | supports | Technical Report 9421, October 29,1994,22pages. All pages and9 references read via OCR; method/proof pages5–7 and figures/table on9,15,17,20 visually checked. Author metadata links a revised Statistics and Computing6:353–366(1996) paper; those journal bytes were not inspected. |
| neal1998ais | https://arxiv.org/pdf/physics/9803008v2; Section 7, PDF pp. 19–20, Equations 28–29 and variance warning | supports | arXiv physics/9803008v2, submitted September 4, 1998; printed report first version February 18, revised September 1, 1998. All 25 pages and 18 references inspected, with figure pages 14–15 and core method pages 4–6 visually checked. Author metadata lists Statistics and Computing 11:125–139 (2001); journal-byte equivalence was not established. |
| calculation | research/discovery/tempered-boundaries.py | supports | Exact three-state full-path enumeration checks detailed balance, independent density rescaling and72 finite kernel cases. Counterexamples show why endpoint-only acceptance and using the same nonreversible cycle in both directions can fail; a fully accepted identity transition illustrates absence of an ergodicity guarantee. |
| supporting-fix-audit | research/discovery/20261014T194929Z-ais-tempered-fix-verification.json | supports | Separate bounded agent verification confirms four original audit dispositions in exact current bytes; it is not independent approval or a complete formal review. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- A bounded supporting agent audit confirmed the mathematics; its draft table-locator finding was corrected before this maintained record was written. The formal saved review remains author self-review, not independent approval.
- This round adds one DRAFT concept, reaching 701 native and 442 unchanged AIO records. The main frontier has 886 entries, including 471 pending and 59 partly addressed cohorts; nested leads remain.
- All22PDF pages read using Tesseract OCR after garbled native text extraction. Equations5–12 and the complete up/down algorithm on pages5–7 visually checked; all3figures on9,15,17 and comparison table20 visually inspected. Other equations remain OCR-only. The full25-page AIS report is separately read for the later normalizer-estimation qualification.
- The inspected source is the October29,1994 Technical Report9421,22pages. Author metadata lists a revised1996journalpaper; those journal bytes were not inspected. Invariance of the full transition does not guarantee irreducibility, fast mixing, independent samples or an exact target draw from arbitrary initialization. Identity-like paths can have high acceptance with no movement. Geometric spacing and dimension-scaling comparisons assume Gaussian targets and immediately equilibrating base kernels; they are not universal performance guarantees. The4292component synthetic-mixture comparison is historical and source-specific, not a present benchmark or universal advantage over simulated tempering. The1994comparison table lacks normalizer estimates for tempered transitions, but the inspected1998AIS paper Section7 derives such estimates. Do not preserve the older absence statement as timeless. Overrelaxed-energy variants, nonrandom simulated-temperature movement, combined replica methods and tempered Hamiltonian trajectories are separate proposals/identities; no full implementation or benchmark is claimed.
- AIS and tempered transitions are added. The nonreversible, overrelaxation, HMC-extension and broader discovery frontiers remain unresolved; no saturation claim is made.
- Original Documents synchronization and old round141 cleanup remain unapproved after automatic-review rejection; only the isolated recovery worktree is modified.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T200216Z-tempered-transitions
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Tempered transitions
started_at: '2026-10-14T19:57:45Z'
finished_at: '2026-10-14T20:02:16Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged mutual reversal, full-path acceptance,
    normalizer cancellation, identity transitions and version-specific normalizer-estimation
    claims. A separate bounded supporting agent math audit was also assessed. This
    is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain tempered transitions as DRAFT with a related Markov-process mapping.
  Primary equations and exact finite calculations support the scoped transition, while
  mixing, implementation and source-version limitations remain explicit.
source:
  git_revision: c924f97a3db72c41c068391adbbd8fd3690d5740
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/BoltzmannMachineNetwork.yaml
    sha256: 1152d2d85c5c1c408a0420e13f211ed109b12fb289c706ee7449864e91aece03
    role: context
  - path: data/aio/DataPreparation.yaml
    sha256: 99aebfc324b628969407ddc7591312e992db1469e7ef8fb3ad28e4b62d3bb359
    role: context
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/Model.yaml
    sha256: 56b85d1c6d559d9ce4172dcf9c776126e91a03649c8f4d1fa8e3f5130f0ca73b
    role: context
  - path: data/aio/Normalization.yaml
    sha256: ecdbd41476b6125c670855f1f00090047acd61f5ee16d71384f6b9ed86bea2bb
    role: context
  - path: data/aio/ProbabilisticGraphicalModel.yaml
    sha256: 288c6df0138836e2fcf554982ffa00dc5b09e497a9a14c27dba64f2320b9eda4
    role: context
  - path: data/aio/ProbabilisticHiddenLayer.yaml
    sha256: 610c29db815f7348c5bdcdc7e7460dd2dea9ea338f3727ebb1596c51b4af41da
    role: context
  - path: data/aio/SelectionAndSamplingBias.yaml
    sha256: 72d8ef34949942ddee1fe60d645806a2117b95207f681de923297b64f78cc477
    role: context
  - path: data/curated/AnnealedImportanceSampling.yaml
    sha256: 94c7b8e597f3551b2b804778e11385d6ec9137515bc44a9c9d429268869f7e68
    role: context
  - path: data/curated/HamiltonianMonteCarlo.yaml
    sha256: 28367594dbc36a8357c33a4e639aeb0fefdd47adc8c46e2b3d5feb96b67e84ca
    role: context
  - path: data/curated/MetropolisHastings.yaml
    sha256: 01cb22a25242e8564e2a7bb839ecb46da1bc49eb09b3c85200f9a596e05b99b4
    role: context
  - path: data/curated/ParallelTempering.yaml
    sha256: e2976bcbbe756cf1b943520c6c9d739b862213c2df4ab4f2806957b67db8d0eb
    role: context
  - path: data/curated/SimulatedAnnealing.yaml
    sha256: 7e77f553c8b2afc4563dc7ef6cba2b53719f22b1fd02ed37d22de9821079d42c
    role: context
  - path: data/curated/TemperedTransitions.yaml
    sha256: d0f1d74d46bcd92995467e13b3552cdf5637cd0a81c8e88fd8a3c52b8bd1af79
    role: target
  - path: research/discovery/20261014T194311Z-ais-tempered-supporting-math-audit.json
    sha256: 4fd496660b8f67fdff5d93ebea24f245e8b4cfc293dec87a283ae9224a4f4c24
    role: context
  - path: research/discovery/20261014T194609Z-ais-review-corrections.json
    sha256: 62628b695dd8dc99c78486538c1b639241d51bbceb7a1a4e11708a45c81518b8
    role: context
  - path: research/discovery/20261014T194707Z-tempered-transitions.json
    sha256: b8ba8deb77b341dd245e17565b6db8e9a5b862f8cf52a8c404b639ecb2141d40
    role: context
  - path: research/discovery/20261014T194929Z-ais-tempered-fix-verification.json
    sha256: 29654c16fae36802d32f135267eaf80664c2d3c4c276a1a7734ca3113c6b7757
    role: context
  - path: research/discovery/tempered-boundaries.py
    sha256: d407c71035e4f3c97ef72203cf1ea575466abf24ffd7080aa2933dc18f1725b4
    role: context
  - path: reviews/structured/20261014T194501Z-ais-path-and-locators/review.yaml
    sha256: cdaec32a376e922eab9cca5614d42c1523e4b0b0fd67cc4329d9798c86cd304c
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
- target_id: AIMech:TemperedTransitions
  path: data/curated/TemperedTransitions.yaml
  label: Tempered transitions
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/TemperedTransitions.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:TemperedTransitions'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:TemperedTransitions
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Uninspected source versions and implementation components
    reason: Positive proper common-state densities define the maintained regular case.
      Other zero-support/constrained formulations, numerical implementations, journal
      bytes and benchmarks were not audited.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:TemperedTransitions
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 437.22s (0:07:17)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 701 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 392 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 393,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:TemperedTransitions
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
  - AIMech:TemperedTransitions
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
  - AIMech:TemperedTransitions
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/tempered-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:TemperedTransitions
  exit_code: 0
  expected_exit_code: 0
  summary: '{"target": ["1/10", "1/5", "7/10"], "correct_path_kernel": [["7/27", "7/27",
    "13/27"], ["7/54", "7/18", "13/27"], ["13/189", "26/189", "50/63"]], "independent_density_scales_cancel":
    true, "endpoint_only_acceptance": {"kernel": [["1/6", "1/3", "1/2"], ["1/12",
    "5/12", "1/2"], ["1/42", "2/21", "37/42"]], "target_after_one_step": ["1/20",
    "11/60", "23/30"]}, "wrong_same_nonreversible_directions": {"kernel": [["0", "0",
    "1"], ["1/2", "1/2", "0"], ["0", "2/7", "5/7"]], "target_after_one_step": ["1/10",
    "3/10", "3/5"]}, "correct_cycle_reverse_is_identity": true, "finite_invariant_family_cases":
    72, "scope": "Exact finite path enumeration, including rejection self-loops. No
    author-code or benchmark replication, universal efficiency bound, guarantee of
    ergodicity or numerical implementation audit."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261014T194707Z-tempered-transitions.json
  accessed_at: '2026-10-14T19:57:45Z'
  support: supports
  summary: 'Compared tempered transitions against all442 pinned AIO and700 native
    identities; no normalized match. Ignored- and hidden-inclusive searches of three
    full checkouts returned312,116,115 lines in24 unique content groups, all classified
    as the pending cohort or newly written AIS record/report, primary-source notes
    and queries. The23 new groups were read in full; the shared cohort line was retained
    from the earlier assessment. Semantic assessment covered103 AIO and307 native
    definitions: all103 and306 preceding rows verified unchanged, plus the new AIS
    row and maintained record read and its three corrections reassessed. Ten complete
    AIO contexts and five full native neighbors assessed. This identity is the full
    up/down Metropolis transition on one target state. It differs from weighted one-way
    AIS estimates, replica exchanges in parallel tempering, a temperature-index random
    walk in simulated tempering, annealing optimization, and tempered Hamiltonian
    trajectory modifications.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-14T19:57:45Z'
  support: supports
  summary: Related MarkovChain connects the constructed target-preserving transition
    algorithm to the process/model. It is not equivalence or a Network/hidden-layer
    subclass assertion. Ten complete contexts reject incidental model applications,
    data normalization and bias labels. Five full native neighbors distinguish AIS,
    Metropolis–Hastings, parallel tempering, annealing optimization and ordinary HMC.
- evidence_id: neal1994tempered
  kind: primary_source
  reference: https://glizen.com/radfordneal/ftp/ttrans.pdf
  locator: Section 3.1, PDF pp. 5–6, Equation 5, up/down construction and Equation
    6; detailed-balance proof, Section 3.2, pp. 6–7; Section 3.1, PDF p. 5, Equation
    5 and composition-order paragraph; Section 3.1, PDF pp. 5–6, explicit path construction
    and Equation 6; Section 3.2, PDF pp. 6–7, Equations 7–12; efficiency discussion,
    Sections 4–5; curator identity-transition example in research/discovery/tempered-boundaries.py;
    Equation 5, PDF p. 5; Equation 6, p. 6; full-path proof, pp. 6–7; exact independent
    enumeration in research/discovery/tempered-boundaries.py; General interpolating
    distributions, PDF pp. 3–4; Section 3.3, pp. 7–10; Sections 4–6, pp. 10–21; Unnumbered
    comparison table and accompanying discussion, PDF p. 20
  accessed_at: '2026-10-14T07:51:05Z'
  snapshot_sha256: b91a045d73ddbe45ab6f75b3877cbd66fc43127ebb0c55989388894afc35a596
  support: supports
  summary: Technical Report 9421, October 29,1994,22pages. All pages and9 references
    read via OCR; method/proof pages5–7 and figures/table on9,15,17,20 visually checked.
    Author metadata links a revised Statistics and Computing6:353–366(1996) paper;
    those journal bytes were not inspected.
- evidence_id: neal1998ais
  kind: primary_source
  reference: https://arxiv.org/pdf/physics/9803008v2
  locator: Section 7, PDF pp. 19–20, Equations 28–29 and variance warning
  accessed_at: '2026-10-14T07:51:05Z'
  snapshot_sha256: 6ae14b83d623438355c2de17a5e830d67a07fd5331b2eb997b82ed40174745cc
  support: supports
  summary: arXiv physics/9803008v2, submitted September 4, 1998; printed report first
    version February 18, revised September 1, 1998. All 25 pages and 18 references
    inspected, with figure pages 14–15 and core method pages 4–6 visually checked.
    Author metadata lists Statistics and Computing 11:125–139 (2001); journal-byte
    equivalence was not established.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/tempered-boundaries.py
  accessed_at: '2026-10-14T19:59:05Z'
  snapshot_sha256: d407c71035e4f3c97ef72203cf1ea575466abf24ffd7080aa2933dc18f1725b4
  support: supports
  summary: Exact three-state full-path enumeration checks detailed balance, independent
    density rescaling and72 finite kernel cases. Counterexamples show why endpoint-only
    acceptance and using the same nonreversible cycle in both directions can fail;
    a fully accepted identity transition illustrates absence of an ergodicity guarantee.
- evidence_id: supporting-fix-audit
  kind: record_content
  reference: research/discovery/20261014T194929Z-ais-tempered-fix-verification.json
  accessed_at: '2026-10-14T19:49:29Z'
  snapshot_sha256: 29654c16fae36802d32f135267eaf80664c2d3c4c276a1a7734ca3113c6b7757
  support: supports
  summary: Separate bounded agent verification confirms four original audit dispositions
    in exact current bytes; it is not independent approval or a complete formal review.
assessments:
- assessment_id: identity
  area: identity
  topic: Tempered transitions
  outcome: supported
  target_ids:
  - AIMech:TemperedTransitions
  evidence_ids:
  - identity
  - neal1994tempered
  - neal1998ais
  summary: Retain this distinct DRAFT algorithm.
  details: Retain the full outward/return accept/reject kernel as one algorithm. It
    differs from AIS weighted estimation, simultaneous replicas, random temperature-index
    evolution and tempered Hamiltonian trajectory modifications. The later backward
    normalizer estimator is an explicitly scoped extension rather than a duplicate
    transition record.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:TemperedTransitions
  evidence_ids:
  - mapping
  - neal1994tempered
  - neal1998ais
  summary: The explicit AIO mapping assessment is supported within its stated scope.
  details: Related MarkovChain connects the constructed target-preserving transition
    algorithm to the process/model. It is not equivalence or a Network/hidden-layer
    subclass assertion. Ten complete contexts reject incidental model applications,
    data normalization and bias labels. Five full native neighbors distinguish AIS,
    Metropolis–Hastings, parallel tempering, annealing optimization and ordinary HMC.
- assessment_id: auxiliary-kernel-pairs
  area: evidence
  topic: auxiliary-kernel-pairs
  outcome: supported
  target_ids:
  - AIMech:TemperedTransitions
  evidence_ids:
  - neal1994tempered
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equation5 requires mutual reversal, not merely separate invariance. Reusing
    one kernel is valid when reversible; compositions need reversed update order.
    The nonreversible-cycle counterexample isolates this condition.
- assessment_id: path-and-acceptance
  area: evidence
  topic: path-and-acceptance
  outcome: supported
  target_ids:
  - AIMech:TemperedTransitions
  evidence_ids:
  - neal1994tempered
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Both outermost kernels occur, totaling2n applications. Equation6 uses the
    full outward and return intermediate states, retains rejection self-loops and
    cancels each density normalizer. Endpoint-only correction is insufficient in the
    explicit refresh-kernel example.
- assessment_id: invariance-and-exploration
  area: evidence
  topic: invariance-and-exploration
  outcome: supported
  target_ids:
  - AIMech:TemperedTransitions
  evidence_ids:
  - neal1994tempered
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Pairing reversed complete paths establishes detailed balance, without implying
    ergodicity or rapid convergence. A fully accepted cycle/reverse pair returns the
    identity transition. The maintained regular case does not claim exact target sampling
    from arbitrary initialization.
- assessment_id: finite-path-balance-checks
  area: evidence
  topic: finite-path-balance-checks
  outcome: supported
  target_ids:
  - AIMech:TemperedTransitions
  evidence_ids:
  - neal1994tempered
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Exact path enumeration reproduces the reported kernel, density-scale invariance
    and72 finite cases. Both incorrect alternatives move the target to the stated
    wrong distributions; these finite failures and identities are not universal performance
    results.
- assessment_id: temperature-and-method-boundaries
  area: evidence
  topic: temperature-and-method-boundaries
  outcome: supported
  target_ids:
  - AIMech:TemperedTransitions
  evidence_ids:
  - neal1994tempered
  summary: Supported within the stated primary-source and mathematical scope.
  details: The source permits auxiliary families beyond canonical temperatures. Its
    Gaussian comparison and synthetic examples remain conditional. Existing HMC-variant
    and nonreversible-method leads retain separate scope instead of being declared
    resolved by this record.
- assessment_id: later-normalizer-extension
  area: evidence
  topic: later-normalizer-extension
  outcome: supported
  target_ids:
  - AIMech:TemperedTransitions
  evidence_ids:
  - neal1998ais
  - neal1994tempered
  summary: Supported within the stated primary-source and mathematical scope.
  details: The unnumbered1994 comparison table records the then-unavailable estimate.
    AIS Equations28–29 subsequently provide backward weights over accepted and rejected
    attempts, with target-chain convergence/stationarity and variance/autocorrelation
    qualifications. The two sources are cited separately and the estimator is not
    confused with acceptance.
- assessment_id: constructed-boundaries
  area: consistency
  topic: mutual reversal, full-path acceptance, normalizer cancellation, identity
    transitions and version-specific normalizer-estimation claims
  outcome: supported
  target_ids:
  - AIMech:TemperedTransitions
  evidence_ids:
  - neal1994tempered
  - neal1998ais
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Exact three-state full-path enumeration checks detailed balance, independent
    density rescaling and72 finite kernel cases. Counterexamples show why endpoint-only
    acceptance and using the same nonreversible cycle in both directions can fail;
    a fully accepted identity transition illustrates absence of an ergodicity guarantee.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:TemperedTransitions
  evidence_ids:
  - identity
  - mapping
  - neal1994tempered
  - neal1998ais
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. All six claims, aliases, definition, two source versions
    and precise locators, ten AIO contexts, five native neighbors, limitations and
    actual provenance assessed. The draft table label was corrected to unnumbered
    before maintained creation, with separate evidence for the1994 comparison and1998
    extension. Full-path acceptance and kernel reversal were checked against exact
    finite path enumeration.
- assessment_id: supporting-audit-boundary
  area: provenance
  topic: Draft correction before maintained creation
  outcome: supported
  target_ids:
  - AIMech:TemperedTransitions
  evidence_ids:
  - supporting-fix-audit
  - neal1994tempered
  - neal1998ais
  summary: The draft table locator was corrected before this maintained record was
    created.
  details: The1994 table is unnumbered and is cited separately from the1998 estimator
    extension. No fictitious maintained-record issue or independent-review approval
    is claimed.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- A bounded supporting agent audit confirmed the mathematics; its draft table-locator
  finding was corrected before this maintained record was written. The formal saved
  review remains author self-review, not independent approval.
- This round adds one DRAFT concept, reaching 701 native and 442 unchanged AIO records.
  The main frontier has 886 entries, including 471 pending and 59 partly addressed
  cohorts; nested leads remain.
- All22PDF pages read using Tesseract OCR after garbled native text extraction. Equations5–12
  and the complete up/down algorithm on pages5–7 visually checked; all3figures on9,15,17
  and comparison table20 visually inspected. Other equations remain OCR-only. The
  full25-page AIS report is separately read for the later normalizer-estimation qualification.
- The inspected source is the October29,1994 Technical Report9421,22pages. Author
  metadata lists a revised1996journalpaper; those journal bytes were not inspected.
  Invariance of the full transition does not guarantee irreducibility, fast mixing,
  independent samples or an exact target draw from arbitrary initialization. Identity-like
  paths can have high acceptance with no movement. Geometric spacing and dimension-scaling
  comparisons assume Gaussian targets and immediately equilibrating base kernels;
  they are not universal performance guarantees. The4292component synthetic-mixture
  comparison is historical and source-specific, not a present benchmark or universal
  advantage over simulated tempering. The1994comparison table lacks normalizer estimates
  for tempered transitions, but the inspected1998AIS paper Section7 derives such estimates.
  Do not preserve the older absence statement as timeless. Overrelaxed-energy variants,
  nonrandom simulated-temperature movement, combined replica methods and tempered
  Hamiltonian trajectories are separate proposals/identities; no full implementation
  or benchmark is claimed.
- AIS and tempered transitions are added. The nonreversible, overrelaxation, HMC-extension
  and broader discovery frontiers remain unresolved; no saturation claim is made.
- Original Documents synchronization and old round141 cleanup remain unapproved after
  automatic-review rejection; only the isolated recovery worktree is modified.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
