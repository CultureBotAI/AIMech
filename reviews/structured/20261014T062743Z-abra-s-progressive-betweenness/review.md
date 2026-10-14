# Scientific author self-review of ABRA-s progressive betweenness approximation

- Review: 20261014T062743Z-abra-s-progressive-betweenness
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-14T06:13:46Z
- Finished UTC: 2026-10-14T06:27:43Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain revised ABRA-s progressive betweenness approximation as DRAFT with bounded AIO no-match assessment. Fixed scheduling, stage confidence allocation, estimator normalization and termination limits are explicit.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:ABRASProgressiveBetweenness
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9106d7f9c5da17e6cda025ac576834bd74cffde0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ABRASProgressiveBetweenness | data/curated/ABRASProgressiveBetweenness.yaml | maintained | ABRA-s progressive betweenness approximation |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:ABRASProgressiveBetweenness | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 330.73s (0:05:30)<br>Checked 442 record(s); 0 failed.<br>Checked 693 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 381 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 381,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:ABRASProgressiveBetweenness | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:ABRASProgressiveBetweenness | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:ABRASProgressiveBetweenness | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:ABRASProgressiveBetweenness | {"cases": {"path3": {"ordered_pairs": 6, "reachable_pairs": 6, "exact_ordered_pair_mean": ["0", "1/3", "0"], "one_and_two_draw_expectations_equal": true, "selected_sample_rademacher": "1/8"}, "diamond4": {"ordered_pairs": 12, "reachable_pairs": 12, "exact_ordered_pair_mean": ["1/12", "1/12", "1/12", "1/12"], "one_and_two_draw_expectations_equal": true, "selected_sample_rademacher": "1/16"}, "directed_chain3": {"ordered_pairs": 6, "reachable_pairs": 3, "exact_ordered_pair_mean": ["0", "1/6", "0"], "one_and_two_draw_expectations_equal": true, "selected_sample_rademacher": "1/8"}, "weighted_triangle": {"ordered_pairs": 6, "reachable_pairs": 6, "exact_ordered_pair_mean": ["0", "1/6", "0"], "one_and_two_draw_expectations_equal": true, "selected_sample_rademacher": "1/16"}}, "unreachable_pair_conditioning": {"full_mean": "1/6", "conditioned_mean": "1/3"}, "multiple_shortest_paths": {"paths": [[0, 1, 3, 4], [0, 2, 3, 4]], "fractions": ["0", "1/2", "1/2", "1", "0"], "shared_internal_raw_count": 2, "shared_internal_fraction": "1"}, "vector_identity": {"full_rademacher": "3/8", "after_invalid_equal_norm_merge": "1/4", "note": "Equal norms do not identify sample vectors. This is not a claim that author software merges them."}, "hypothetical_stopping": {"fixed_mean": "1/3", "stop_on_first_one_else_take_two_mean": "4/9", "note": "Illustrates why unbiasedness at fixed size is not inherited by arbitrary stopping; not an ABRA failure example."}, "stage_budget": {"delta": "1/20", "first_ten_stages": "1023/20480"}, "zero_score_complete_graph": {"geometric_schedule": [{"stage": 1, "count": 16, "xi": 0.9852298454564461}, {"stage": 2, "count": 32, "xi": 0.6351744883874864}, {"stage": 3, "count": 64, "xi": 0.4125502682932295}], "linear_schedule_lower_bound_limit": 0.5887050112577373, "note": "For S_i=i, the square-root term alone stays above sqrt(ln2/2), so epsilon=.5 cannot be met. Geometric example terminates."}, "scope": "Finite exact paths, pair expectations and Rademacher signs, with floating evaluation of explicit bounds; no author code, benchmark or empirical guarantee."} |

## Scientific And Domain Assessments

### ABRA-s progressive betweenness approximation

identity: supported. Targets: AIMech:ABRASProgressiveBetweenness.

Retain this distinct DRAFT algorithm.

Retain the revised static progressive algorithm separately from fixed-sample ABRA-s-fix, forced-stop pseudodimension, top-k, target-set, alternative-estimator and dynamic variants. It averages pair fractions rather than source-pivot dependencies, electrical throughputs or indicators for one sampled path.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:ABRASProgressiveBetweenness.

The explicit AIO mapping assessment is supported within its stated scope.

Retain the bounded no-match over ten complete AIO contexts. Statistical-learning concentration results do not identify this progressive graph algorithm with data-dredging or sampling bias, clustering, a language model or data preparation.

### graph-domain-and-estimand

evidence: supported. Targets: AIMech:ABRASProgressiveBetweenness.

Supported within the stated primary-source and mathematical scope.

The complete ordered distinct-pair population has n(n-1) elements. Endpoint and unreachable contributions are zero. Positive-weight scope gives acyclic shortest-path predecessor ordering; the broader source nonnegative wording is not imported without conventions. Epsilon and delta are in(0,1).

### fraction-estimator-and-vector-state

evidence: supported. Targets: AIMech:ABRASProgressiveBetweenness.

Supported within the stated primary-source and mathematical scope.

Algorithms1–2 use sigma_uw sigma_wv/sigma_uv for internal vertices and map nodes to distinct sample vectors. Equal norms can describe different vectors; the finite sign-sum example demonstrates the consequence without claiming author software incorrectly merges them.

### rademacher-stopping-bound

evidence: supported. Targets: AIMech:ABRASProgressiveBetweenness.

Supported within the stated primary-source and mathematical scope.

Theorems3.3–3.4 supply the Euclidean-norm exponential bound and the displayed simultaneous deviation expression. Conservative upper values are permissible; uncertified underestimates are not. Finite Rademacher sign enumeration checks selected bounds, not the general theorem.

### progressive-validity-and-schedule

evidence: supported. Targets: AIMech:ABRASProgressiveBetweenness.

Supported within the stated primary-source and mathematical scope.

Lemmas4.2–4.3 apply a union bound to fixed-stage sample collections with delta/2^i. The earlier adaptive schedule is explicitly excluded. For S_i=i, ln(3/delta)+i ln2 in the square-root term yields a lower bound above sqrt(ln2/2); epsilon=.5 cannot be attained. No universal termination is asserted.

### finite-estimator-boundaries

evidence: supported. Targets: AIMech:ABRASProgressiveBetweenness.

Supported within the stated primary-source and mathematical scope.

Exact small graph enumeration yields path3 middle1/3 and directed-chain middle1/6; reachable conditioning changes the latter to1/3. The branching graph needs a denominator2 for a shared-node raw count2. One/two fixed draw expectations agree with targets, while the separate hypothetical stopped example is labeled accordingly.

### version-and-evaluation-boundaries

evidence: supported. Targets: AIMech:ABRASProgressiveBetweenness.

Supported within the stated primary-source and mathematical scope.

The author manuscript explicitly corrects the earlier stopping argument. Historical C++11/NetworKit/NLopt experiments with four SNAP graphs, geometric schedules and delta.1 remain descriptive; email-Enron slower cases and single-selected-run table reporting are retained. No quantitative universal advantage is imported.

### revised versus early stopping proof, fractions versus counts, vector identity versus norms, pair normalization, schedule termination, numerical bounds and historical evaluation

consistency: supported. Targets: AIMech:ABRASProgressiveBetweenness.

Constructed calculations support the stated distinctions.

Exhaustive small-graph pair and one/two-draw averages check the endpoint-normalized target, disconnected-pair treatment and raw-count versus fraction distinction. Finite Rademacher sign sums distinguish vector identity from equal norms. A hypothetical stopping example separates fixed-size unbiasedness from arbitrary stopped means. Stage allocations and zero-score geometric/linear schedules expose the stopping-rule boundary. These are curator arithmetic, not author code, a universal concentration proof or replicated performance.

### All maintained fields

provenance: supported. Targets: AIMech:ABRASProgressiveBetweenness.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Complete maintained fields, all six claims, source identity and locators assessed. The revised algorithm uses normalized shortest-path fractions and a schedule fixed independently of samples, with delta/2^i stage allocations. Finite examples distinguish unreachable-pair conditioning, raw path counts, vector identity and stopped expectations. The linear-schedule counterexample prevents a universal termination claim.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261014T061302Z-abra-s-progressive-betweenness.json | supports | Compared all 442 pinned AIO and 691 native identities; no normalized match. Ignored- and hidden-inclusive searches of three full checkouts returned 56,0,1 lines, all read as existing ABRA/Bavarian leads, source-reading notes, query strings or an unrelated Portuguese translation. Semantic assessment covered 154 AIO and 535 native definitions: all 147 AIO and 524 prior native rows verified unchanged, with seven additional AIO and eleven additional native rows read. Ten complete AIO contexts and six full native neighbors were assessed. The identity is the revised static progressive ABRA-s algorithm: independently sampled ordered pairs contribute shortest-path fractions and a fixed stage schedule with allocated failure budgets determines when to stop. It differs from exact source dependency accumulation, source-pivot estimation, electrical-flow pair sampling, shortest-path closeness sampling and the separate fixed-sample ABRA-s-fix variant. |
| mapping | sources/aio/aio.json | supports | Retain the bounded no-match over ten complete AIO contexts. Statistical-learning concentration results do not identify this progressive graph algorithm with data-dredging or sampling bias, clustering, a language model or data preparation. |
| riondatoupfal2018 | https://www.rionda.to/papers/RiondatoUpfal-BetweennessRademacherAverages-TKDD.pdf; Sections 4.1–4.1.2, Algorithms 1–2 and Theorem 4.1, PDF pp. 10–16; Definitions 3.1–3.2, PDF pp. 5–6; Equation 11 and Algorithms 1–2, pp. 10–13. The positive-weight restriction avoids unresolved zero-weight predecessor and cycle conventions.; Section 4.1, Algorithms 1–2 and Figure 2, PDF pp. 11–14; curator vector distinction in research/discovery/abra-pair-boundaries.py; Theorems 3.3–3.4, Equations 4–6, PDF p. 7; Section 4.1 and Algorithm 1, pp. 11–12; Section 1 correction notice, PDF p. 2; Section 4.1.1, Lemmas 4.2–4.3, pp. 13–16; Section 4.1.2, p. 16; curator schedule check in research/discovery/abra-pair-boundaries.py; Definition 3.1 and Equation 11, PDF pp. 5 and 10–11; Algorithms 1–2, pp. 12–13; explicit curator examples in research/discovery/abra-pair-boundaries.py; Section 1, PDF pp. 2–3; Sections 4.1.3–5, pp. 16–28; Sections 6–6.4 and Tables 3–10, pp. 28–34 | supports | Thirty-seven-page author-hosted ACM-style manuscript labeled April 2018, retaining placeholder journal header and DOI fields. Author catalog and BibTeX identify ACM Transactions on Knowledge Discovery from Data 12(5), article 61 (2018). All text and 53 references read; four figures, Tables 3–10 and selected equations/algorithms visually inspected. Tables 1–2 were read as text; not every proof equation was visually checked. The 27-page arXiv v1 was read for the earlier-version comparison, without publisher-byte equivalence. No author software or raw benchmark data inspected. |
| calculation | research/discovery/abra-pair-boundaries.py | supports | Exhaustive small-graph pair and one/two-draw averages check the endpoint-normalized target, disconnected-pair treatment and raw-count versus fraction distinction. Finite Rademacher sign sums distinguish vector identity from equal norms. A hypothetical stopping example separates fixed-size unbiasedness from arbitrary stopped means. Stage allocations and zero-score geometric/linear schedules expose the stopping-rule boundary. These are curator arithmetic, not author code, a universal concentration proof or replicated performance. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- This round adds one DRAFT concept, reaching 692 native and 442 unchanged AIO records. The main frontier has 877 entries, including 472 pending and 58 partly addressed cohorts; nested leads remain.
- All37 PDF pages and53references read in extracted text. Rendered pages5,7,12,14,15,16,22,24,25,28,29,31,32,33,34 inspected: all four figures and Tables3–10, plus relevant equations and algorithms. Tables1–2 text only. Not all theorem proofs visually checked.
- Primary author manuscript only; earlier arXiv is version-comparison context. The record uses fixed scheduling and exact-path/positive-weight conventions. No author software, publisher-layout equivalence, replicated benchmark or universal termination result asserted.
- The revised static progressive ABRA-s procedure is added. Other ABRA variants and KADABRA remain explicit leads; original information/flow centrality and Noh–Rieger scope assessment also remain pending.
- Original Documents synchronization and old round141 cleanup remain unapproved after automatic-review rejection; only the isolated recovery worktree is modified.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T062743Z-abra-s-progressive-betweenness
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of ABRA-s progressive betweenness approximation
started_at: '2026-10-14T06:13:46Z'
finished_at: '2026-10-14T06:27:43Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged revised versus early stopping proof, fractions
    versus counts, vector identity versus norms, pair normalization, schedule termination,
    numerical bounds and historical evaluation. This is adversarial author self-review,
    not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain revised ABRA-s progressive betweenness approximation as DRAFT with
  bounded AIO no-match assessment. Fixed scheduling, stage confidence allocation,
  estimator normalization and termination limits are explicit.
source:
  git_revision: 9106d7f9c5da17e6cda025ac576834bd74cffde0
  state: working_tree
  inputs:
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
    role: context
  - path: data/aio/DataDredgingBias.yaml
    sha256: 335067e88f1462e141ac5f35e697cd42f7d250ec4dde9250531babe0d96cc1d0
    role: context
  - path: data/aio/DataPreparation.yaml
    sha256: 99aebfc324b628969407ddc7591312e992db1469e7ef8fb3ad28e4b62d3bb359
    role: context
  - path: data/aio/DeepActiveLearning.yaml
    sha256: b04c9aa74728adbe1bd907cb3f0e15b263bda18ed29660babce092daeed2b4f9
    role: context
  - path: data/aio/GraphLanguageModel.yaml
    sha256: 1cdda6f7d19946e0672835185e179e2336832225c180e2b70d7860b0c96fc2a8
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/RankingBias.yaml
    sha256: 3e931657e0ee2a47e36a7858dbb8f26f00b565040f4fedd138f55353551160b0
    role: context
  - path: data/aio/RepresentationBias.yaml
    sha256: 5ac7d1455814eb8305b1ab9d0934e61fc50c09fe3dfd7724da5fdb4a21f360b2
    role: context
  - path: data/aio/SelectionAndSamplingBias.yaml
    sha256: 72d8ef34949942ddee1fe60d645806a2117b95207f681de923297b64f78cc477
    role: context
  - path: data/aio/UnsupervisedClustering.yaml
    sha256: 78d3917b751b29e83802dfd2ceff6b5ee131cd64a5a3a7d40de02f5d2b9bdb1e
    role: context
  - path: data/curated/ABRASProgressiveBetweenness.yaml
    sha256: 9b1d85ceb3a3305970c23930e67cda59be68985f8fd5da6b4ae3ec94c655a113
    role: target
  - path: data/curated/BrandesBetweennessCentrality.yaml
    sha256: 2ff7051fa27a4e1150545d634b90599a335b909b1fe6956441260c5284830e21
    role: context
  - path: data/curated/BrandesFleischerGroundedCurrentFlowCloseness.yaml
    sha256: 1419f42eda073f6fc8ca83dc1e65d1f8cb03573ab07240aef71d253323d1dffd
    role: context
  - path: data/curated/BrandesFleischerSampledCurrentFlowBetweenness.yaml
    sha256: 32b66dbd161efc40fa7162b43f16436146accd5aa8ea90c10874d91be21948ad
    role: context
  - path: data/curated/BrandesPichPivotCentralityEstimation.yaml
    sha256: 7f8492fc3a881da6c35439412b535572f687215410b85b05439d2ca8d799b9c1
    role: context
  - path: data/curated/EppsteinWangRANDClosenessApproximation.yaml
    sha256: 33d58cab5cddbe19e25fa1f1efa66982a6ca9c461b8cee211df186c570688d19
    role: context
  - path: data/curated/NewmanRandomWalkBetweennessMatrix.yaml
    sha256: 9ed2e0ea7ac76abbf3de52341f78f4944e73b6215af2008fff08888d9fb59bd8
    role: context
  - path: research/discovery/20261014T061302Z-abra-s-progressive-betweenness.json
    sha256: 6d9f26c95a0879fbf85cfdfd477e2e5be62e4a37401639aae10e471ba1e76684
    role: context
  - path: research/discovery/abra-pair-boundaries.py
    sha256: a38b589db131fe6b916646e68e0845fc897d3bb6a9494049297f7d390804e4d8
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
- target_id: AIMech:ABRASProgressiveBetweenness
  path: data/curated/ABRASProgressiveBetweenness.yaml
  label: ABRA-s progressive betweenness approximation
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ABRASProgressiveBetweenness.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:ABRASProgressiveBetweenness'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:ABRASProgressiveBetweenness
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Uninspected source versions and implementation components
    reason: The37-page author manuscript and53 references were read, with all four
      figures, Tables3–10 and selected equations visually inspected; not every proof
      equation was visually checked. Earlier27-page arXiv is version-comparison context.
      No publisher-byte identity, author code or benchmark replication is asserted.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:ABRASProgressiveBetweenness
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 330.73s (0:05:30)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 693 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 381 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 381,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:ABRASProgressiveBetweenness
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
  - AIMech:ABRASProgressiveBetweenness
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
  - AIMech:ABRASProgressiveBetweenness
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/abra-pair-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:ABRASProgressiveBetweenness
  exit_code: 0
  expected_exit_code: 0
  summary: '{"cases": {"path3": {"ordered_pairs": 6, "reachable_pairs": 6, "exact_ordered_pair_mean":
    ["0", "1/3", "0"], "one_and_two_draw_expectations_equal": true, "selected_sample_rademacher":
    "1/8"}, "diamond4": {"ordered_pairs": 12, "reachable_pairs": 12, "exact_ordered_pair_mean":
    ["1/12", "1/12", "1/12", "1/12"], "one_and_two_draw_expectations_equal": true,
    "selected_sample_rademacher": "1/16"}, "directed_chain3": {"ordered_pairs": 6,
    "reachable_pairs": 3, "exact_ordered_pair_mean": ["0", "1/6", "0"], "one_and_two_draw_expectations_equal":
    true, "selected_sample_rademacher": "1/8"}, "weighted_triangle": {"ordered_pairs":
    6, "reachable_pairs": 6, "exact_ordered_pair_mean": ["0", "1/6", "0"], "one_and_two_draw_expectations_equal":
    true, "selected_sample_rademacher": "1/16"}}, "unreachable_pair_conditioning":
    {"full_mean": "1/6", "conditioned_mean": "1/3"}, "multiple_shortest_paths": {"paths":
    [[0, 1, 3, 4], [0, 2, 3, 4]], "fractions": ["0", "1/2", "1/2", "1", "0"], "shared_internal_raw_count":
    2, "shared_internal_fraction": "1"}, "vector_identity": {"full_rademacher": "3/8",
    "after_invalid_equal_norm_merge": "1/4", "note": "Equal norms do not identify
    sample vectors. This is not a claim that author software merges them."}, "hypothetical_stopping":
    {"fixed_mean": "1/3", "stop_on_first_one_else_take_two_mean": "4/9", "note": "Illustrates
    why unbiasedness at fixed size is not inherited by arbitrary stopping; not an
    ABRA failure example."}, "stage_budget": {"delta": "1/20", "first_ten_stages":
    "1023/20480"}, "zero_score_complete_graph": {"geometric_schedule": [{"stage":
    1, "count": 16, "xi": 0.9852298454564461}, {"stage": 2, "count": 32, "xi": 0.6351744883874864},
    {"stage": 3, "count": 64, "xi": 0.4125502682932295}], "linear_schedule_lower_bound_limit":
    0.5887050112577373, "note": "For S_i=i, the square-root term alone stays above
    sqrt(ln2/2), so epsilon=.5 cannot be met. Geometric example terminates."}, "scope":
    "Finite exact paths, pair expectations and Rademacher signs, with floating evaluation
    of explicit bounds; no author code, benchmark or empirical guarantee."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261014T061302Z-abra-s-progressive-betweenness.json
  accessed_at: '2026-10-14T06:13:46Z'
  support: supports
  summary: 'Compared all 442 pinned AIO and 691 native identities; no normalized match.
    Ignored- and hidden-inclusive searches of three full checkouts returned 56,0,1
    lines, all read as existing ABRA/Bavarian leads, source-reading notes, query strings
    or an unrelated Portuguese translation. Semantic assessment covered 154 AIO and
    535 native definitions: all 147 AIO and 524 prior native rows verified unchanged,
    with seven additional AIO and eleven additional native rows read. Ten complete
    AIO contexts and six full native neighbors were assessed. The identity is the
    revised static progressive ABRA-s algorithm: independently sampled ordered pairs
    contribute shortest-path fractions and a fixed stage schedule with allocated failure
    budgets determines when to stop. It differs from exact source dependency accumulation,
    source-pivot estimation, electrical-flow pair sampling, shortest-path closeness
    sampling and the separate fixed-sample ABRA-s-fix variant.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-14T06:13:46Z'
  support: supports
  summary: Retain the bounded no-match over ten complete AIO contexts. Statistical-learning
    concentration results do not identify this progressive graph algorithm with data-dredging
    or sampling bias, clustering, a language model or data preparation.
- evidence_id: riondatoupfal2018
  kind: primary_source
  reference: https://www.rionda.to/papers/RiondatoUpfal-BetweennessRademacherAverages-TKDD.pdf
  locator: Sections 4.1–4.1.2, Algorithms 1–2 and Theorem 4.1, PDF pp. 10–16; Definitions
    3.1–3.2, PDF pp. 5–6; Equation 11 and Algorithms 1–2, pp. 10–13. The positive-weight
    restriction avoids unresolved zero-weight predecessor and cycle conventions.;
    Section 4.1, Algorithms 1–2 and Figure 2, PDF pp. 11–14; curator vector distinction
    in research/discovery/abra-pair-boundaries.py; Theorems 3.3–3.4, Equations 4–6,
    PDF p. 7; Section 4.1 and Algorithm 1, pp. 11–12; Section 1 correction notice,
    PDF p. 2; Section 4.1.1, Lemmas 4.2–4.3, pp. 13–16; Section 4.1.2, p. 16; curator
    schedule check in research/discovery/abra-pair-boundaries.py; Definition 3.1 and
    Equation 11, PDF pp. 5 and 10–11; Algorithms 1–2, pp. 12–13; explicit curator
    examples in research/discovery/abra-pair-boundaries.py; Section 1, PDF pp. 2–3;
    Sections 4.1.3–5, pp. 16–28; Sections 6–6.4 and Tables 3–10, pp. 28–34
  accessed_at: '2026-10-14T05:26:24Z'
  snapshot_sha256: d703b83aff52e25b8018e49ebd5f0778242bad441db0430d35af8f332a409d8b
  support: supports
  summary: Thirty-seven-page author-hosted ACM-style manuscript labeled April 2018,
    retaining placeholder journal header and DOI fields. Author catalog and BibTeX
    identify ACM Transactions on Knowledge Discovery from Data 12(5), article 61 (2018).
    All text and 53 references read; four figures, Tables 3–10 and selected equations/algorithms
    visually inspected. Tables 1–2 were read as text; not every proof equation was
    visually checked. The 27-page arXiv v1 was read for the earlier-version comparison,
    without publisher-byte equivalence. No author software or raw benchmark data inspected.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/abra-pair-boundaries.py
  accessed_at: '2026-10-14T06:17:00Z'
  snapshot_sha256: a38b589db131fe6b916646e68e0845fc897d3bb6a9494049297f7d390804e4d8
  support: supports
  summary: Exhaustive small-graph pair and one/two-draw averages check the endpoint-normalized
    target, disconnected-pair treatment and raw-count versus fraction distinction.
    Finite Rademacher sign sums distinguish vector identity from equal norms. A hypothetical
    stopping example separates fixed-size unbiasedness from arbitrary stopped means.
    Stage allocations and zero-score geometric/linear schedules expose the stopping-rule
    boundary. These are curator arithmetic, not author code, a universal concentration
    proof or replicated performance.
assessments:
- assessment_id: identity
  area: identity
  topic: ABRA-s progressive betweenness approximation
  outcome: supported
  target_ids:
  - AIMech:ABRASProgressiveBetweenness
  evidence_ids:
  - identity
  - riondatoupfal2018
  summary: Retain this distinct DRAFT algorithm.
  details: Retain the revised static progressive algorithm separately from fixed-sample
    ABRA-s-fix, forced-stop pseudodimension, top-k, target-set, alternative-estimator
    and dynamic variants. It averages pair fractions rather than source-pivot dependencies,
    electrical throughputs or indicators for one sampled path.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:ABRASProgressiveBetweenness
  evidence_ids:
  - mapping
  - riondatoupfal2018
  summary: The explicit AIO mapping assessment is supported within its stated scope.
  details: Retain the bounded no-match over ten complete AIO contexts. Statistical-learning
    concentration results do not identify this progressive graph algorithm with data-dredging
    or sampling bias, clustering, a language model or data preparation.
- assessment_id: graph-domain-and-estimand
  area: evidence
  topic: graph-domain-and-estimand
  outcome: supported
  target_ids:
  - AIMech:ABRASProgressiveBetweenness
  evidence_ids:
  - riondatoupfal2018
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: The complete ordered distinct-pair population has n(n-1) elements. Endpoint
    and unreachable contributions are zero. Positive-weight scope gives acyclic shortest-path
    predecessor ordering; the broader source nonnegative wording is not imported without
    conventions. Epsilon and delta are in(0,1).
- assessment_id: fraction-estimator-and-vector-state
  area: evidence
  topic: fraction-estimator-and-vector-state
  outcome: supported
  target_ids:
  - AIMech:ABRASProgressiveBetweenness
  evidence_ids:
  - riondatoupfal2018
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Algorithms1–2 use sigma_uw sigma_wv/sigma_uv for internal vertices and
    map nodes to distinct sample vectors. Equal norms can describe different vectors;
    the finite sign-sum example demonstrates the consequence without claiming author
    software incorrectly merges them.
- assessment_id: rademacher-stopping-bound
  area: evidence
  topic: rademacher-stopping-bound
  outcome: supported
  target_ids:
  - AIMech:ABRASProgressiveBetweenness
  evidence_ids:
  - riondatoupfal2018
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Theorems3.3–3.4 supply the Euclidean-norm exponential bound and the displayed
    simultaneous deviation expression. Conservative upper values are permissible;
    uncertified underestimates are not. Finite Rademacher sign enumeration checks
    selected bounds, not the general theorem.
- assessment_id: progressive-validity-and-schedule
  area: evidence
  topic: progressive-validity-and-schedule
  outcome: supported
  target_ids:
  - AIMech:ABRASProgressiveBetweenness
  evidence_ids:
  - riondatoupfal2018
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Lemmas4.2–4.3 apply a union bound to fixed-stage sample collections with
    delta/2^i. The earlier adaptive schedule is explicitly excluded. For S_i=i, ln(3/delta)+i
    ln2 in the square-root term yields a lower bound above sqrt(ln2/2); epsilon=.5
    cannot be attained. No universal termination is asserted.
- assessment_id: finite-estimator-boundaries
  area: evidence
  topic: finite-estimator-boundaries
  outcome: supported
  target_ids:
  - AIMech:ABRASProgressiveBetweenness
  evidence_ids:
  - riondatoupfal2018
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Exact small graph enumeration yields path3 middle1/3 and directed-chain
    middle1/6; reachable conditioning changes the latter to1/3. The branching graph
    needs a denominator2 for a shared-node raw count2. One/two fixed draw expectations
    agree with targets, while the separate hypothetical stopped example is labeled
    accordingly.
- assessment_id: version-and-evaluation-boundaries
  area: evidence
  topic: version-and-evaluation-boundaries
  outcome: supported
  target_ids:
  - AIMech:ABRASProgressiveBetweenness
  evidence_ids:
  - riondatoupfal2018
  summary: Supported within the stated primary-source and mathematical scope.
  details: The author manuscript explicitly corrects the earlier stopping argument.
    Historical C++11/NetworKit/NLopt experiments with four SNAP graphs, geometric
    schedules and delta.1 remain descriptive; email-Enron slower cases and single-selected-run
    table reporting are retained. No quantitative universal advantage is imported.
- assessment_id: constructed-boundaries
  area: consistency
  topic: revised versus early stopping proof, fractions versus counts, vector identity
    versus norms, pair normalization, schedule termination, numerical bounds and historical
    evaluation
  outcome: supported
  target_ids:
  - AIMech:ABRASProgressiveBetweenness
  evidence_ids:
  - riondatoupfal2018
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Exhaustive small-graph pair and one/two-draw averages check the endpoint-normalized
    target, disconnected-pair treatment and raw-count versus fraction distinction.
    Finite Rademacher sign sums distinguish vector identity from equal norms. A hypothetical
    stopping example separates fixed-size unbiasedness from arbitrary stopped means.
    Stage allocations and zero-score geometric/linear schedules expose the stopping-rule
    boundary. These are curator arithmetic, not author code, a universal concentration
    proof or replicated performance.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:ABRASProgressiveBetweenness
  evidence_ids:
  - identity
  - mapping
  - riondatoupfal2018
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. Complete maintained fields, all six claims, source
    identity and locators assessed. The revised algorithm uses normalized shortest-path
    fractions and a schedule fixed independently of samples, with delta/2^i stage
    allocations. Finite examples distinguish unreachable-pair conditioning, raw path
    counts, vector identity and stopped expectations. The linear-schedule counterexample
    prevents a universal termination claim.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- This round adds one DRAFT concept, reaching 692 native and 442 unchanged AIO records.
  The main frontier has 877 entries, including 472 pending and 58 partly addressed
  cohorts; nested leads remain.
- 'All37 PDF pages and53references read in extracted text. Rendered pages5,7,12,14,15,16,22,24,25,28,29,31,32,33,34
  inspected: all four figures and Tables3–10, plus relevant equations and algorithms.
  Tables1–2 text only. Not all theorem proofs visually checked.'
- Primary author manuscript only; earlier arXiv is version-comparison context. The
  record uses fixed scheduling and exact-path/positive-weight conventions. No author
  software, publisher-layout equivalence, replicated benchmark or universal termination
  result asserted.
- The revised static progressive ABRA-s procedure is added. Other ABRA variants and
  KADABRA remain explicit leads; original information/flow centrality and Noh–Rieger
  scope assessment also remain pending.
- Original Documents synchronization and old round141 cleanup remain unapproved after
  automatic-review rejection; only the isolated recovery worktree is modified.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
