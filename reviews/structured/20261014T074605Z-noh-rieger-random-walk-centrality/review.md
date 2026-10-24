# Scientific author self-review of Noh–Rieger random-walk centrality

- Review: 20261014T074605Z-noh-rieger-random-walk-centrality
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-14T07:30:46Z
- Finished UTC: 2026-10-14T07:46:05Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Noh–Rieger random-walk centrality as DRAFT with a broader mathematical-function match and a related Markov-process match. Its aperiodic undirected domain and limited mean-passage interpretation are explicit.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:NohRiegerRandomWalkCentrality
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 2593b07b341480f709596150ed3ed4ea993e17ce.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:NohRiegerRandomWalkCentrality | data/curated/NohRiegerRandomWalkCentrality.yaml | maintained | Noh–Rieger random-walk centrality |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:NohRiegerRandomWalkCentrality | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 308.83s (0:05:08)<br>Checked 442 record(s); 0 failed.<br>Checked 697 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 387 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 388,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:NohRiegerRandomWalkCentrality | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:NohRiegerRandomWalkCentrality | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:NohRiegerRandomWalkCentrality | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:NohRiegerRandomWalkCentrality | {"triangle": {"degrees": [2, 2, 2], "stationary": ["1/3", "1/3", "1/3"], "tau": ["4/9", "4/9", "4/9"], "centrality": ["3/4", "3/4", "3/4"], "mean_hitting_or_positive_return": [["3", "2", "2"], ["2", "3", "2"], ["2", "2", "3"]]}, "triangle_with_two_edge_tail": {"degrees": [3, 2, 2, 2, 1], "stationary": ["3/10", "1/5", "1/5", "1/5", "1/10"], "tau": ["27/50", "67/75", "67/75", "29/25", "69/50"], "centrality": ["5/9", "15/67", "15/67", "5/29", "5/69"], "mean_hitting_or_positive_return": [["10/3", "14/3", "14/3", "7", "16"], ["2", "5", "10/3", "9", "18"], ["2", "10/3", "5", "9", "18"], ["3", "23/3", "23/3", "5", "9"], ["4", "26/3", "26/3", "1", "10"]]}, "bipartite_four_cycle": {"deviation_terms": ["3/4", "-1/4", "1/4", "-1/4", "1/4", "-1/4", "1/4", "-1/4"], "partial_sums": ["3/4", "1/2", "3/4", "1/2", "3/4", "1/2", "3/4", "1/2"], "ordinary_series_converges": false}, "scope": "Exact rational finite checks. Inverse representation is curator mathematics equivalent to the convergent deviation series on the two connected non-bipartite examples. No source code, simulation replication, directed extension or universal early-arrival probability claim."} |

## Scientific And Domain Assessments

### Noh–Rieger random-walk centrality

identity: supported. Targets: AIMech:NohRiegerRandomWalkCentrality.

Retain this distinct DRAFT mathematical_method.

Retain the Noh–Rieger return-dynamics functional separately from degree/stationary visitation, PageRank, Newman current-flow betweenness, resistance-sum closeness, sampled geodesic centralities and a Markov transition-construction algorithm. Network transport/search supplies bounded relevance; no learned predictor is asserted.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:NohRiegerRandomWalkCentrality.

The explicit AIO mapping assessment is supported within its stated scope.

A broad MathematicalFunction match is supported by the defined graph/node-to-value functional and the target rule/value definition. The related MarkovChain match connects the score to its generating process, preserving the distinct abstraction levels. The full target node, incident edges, Network parent and hidden-layer context were inspected without importing those assertions into the scalar score. Ten other targets were rejected for explicit scope reasons.

### walk-domain

evidence: supported. Targets: AIMech:NohRiegerRandomWalkCentrality.

Supported within the stated primary-source and mathematical scope.

The actual core is a finite connected unweighted simple undirected graph with an odd cycle. The row-stochastic neighbor walk has stationary degree/total-degree probabilities. No disconnected cross-component, directed or interacting-walker extension is adopted.

### integrated-return-score

evidence: supported. Targets: AIMech:NohRiegerRandomWalkCentrality.

Supported within the stated primary-source and mathematical scope.

Equations7,10,11 support R, tau and pi/tau with the t=0 term. The source spectral single-mode estimate remains an approximation. Triangle scores sum to9/4, directly excluding a probability-distribution interpretation; equal-degree tail nodes have different scores.

### mean-first-passage-asymmetry

evidence: supported. Targets: AIMech:NohRiegerRandomWalkCentrality.

Supported within the stated primary-source and mathematical scope.

Equation8 distinguishes positive return1/pi from off-diagonal passage. Detailed balance cancels cross terms and yields H_ij-H_ji=1/C_j-1/C_i. The sign interpretation in the record is correct and restricted to means, without claiming realization-wise or arrival-race ordering.

### periodic-walk-boundary

evidence: supported. Targets: AIMech:NohRiegerRandomWalkCentrality.

Supported within the stated primary-source and mathematical scope.

Note21 explicitly states the odd-cycle restriction and self-loop modification. On C4 the t=0 term is3/4 and subsequent terms alternate; partial sums alternate3/4 and1/2. A matrix generalized inverse must not be substituted silently for an ordinary convergent series.

### finite-algebraic-checks

evidence: supported. Targets: AIMech:NohRiegerRandomWalkCentrality.

Supported within the stated primary-source and mathematical scope.

Exact rational inversion on two connected non-bipartite graphs is checked against independently solved absorbing-target equations and the positive-return first-step relation. Triangle C=3/4 and tail comparison15/67 versus5/29 agree with H13=9,H31=23/3 and reciprocal difference4/3. These are mathematical examples, not source-simulation replication.

### interpretation-and-evaluation-limits

evidence: supported. Targets: AIMech:NohRiegerRandomWalkCentrality.

Supported within the stated primary-source and mathematical scope.

The paper labels its early-visit argument inexact. Figure1 BA10000 and Figure2 BA512/hierarchical625 scope is retained, with initially one noninteracting walker per node. The record adds no universal degree monotonicity, causal influence, learned prediction, congestion or directed validity.

### convergent deviation series versus periodic walks, positive returns versus zero-time hitting, expectation versus arrival-race ordering, degree versus return dynamics, and functional-versus-process mappings

consistency: supported. Targets: AIMech:NohRiegerRandomWalkCentrality.

Constructed calculations support the stated distinctions.

Exact rational finite graphs compare the deviation-matrix representation with independent absorbing-target first-step equations, verify reciprocal-centrality passage asymmetry and positive returns, separate degree from the full score, and expose the nonconvergent ordinary series on a bipartite four-cycle. The matrix expression is curator mathematics and no paper simulation or author code is replicated.

### All maintained fields

provenance: supported. Targets: AIMech:NohRiegerRandomWalkCentrality.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. All maintained fields, six claims, definition evidence and source metadata read after capture. The maintained functional uses the complete convergent deviation sum, including t=0. Positive returns, undirected reversibility, odd-cycle convergence and the explicitly inexact early-visit interpretation remain separated. The source printed-date/page-count mismatch is preserved.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261014T073004Z-noh-rieger-random-walk-centrality.json | supports | Compared all 442 pinned AIO and 696 native identities; no normalized match. Ignored- and hidden-inclusive searches of three full checkouts returned 67,0,0 lines, all read as existing Noh source references, leads, query strings or review limitations. Semantic assessment covered 155 AIO and 541 native definitions: 155 AIO and540 prior native rows verified unchanged, plus the newly added RK row and full record read. Twelve complete AIO contexts and six full native neighbors assessed. The identity is the centrality functional pi_i divided by the complete integrated excess return probability, with its pairwise mean-passage asymmetry interpretation. It differs from stationary visitation/PageRank, Newman net-flow betweenness, resistance-sum closeness, sampled shortest-path betweenness and Markov-chain transition construction. Network transport/search analysis is the scoped relevance; no learned predictor or universal information advantage is asserted. |
| mapping | sources/aio/aio.json | supports | A broad MathematicalFunction match is supported by the defined graph/node-to-value functional and the target rule/value definition. The related MarkovChain match connects the score to its generating process, preserving the distinct abstraction levels. The full target node, incident edges, Network parent and hidden-layer context were inspected without importing those assertions into the scalar score. Ten other targets were rejected for explicit scope reasons. |
| nohrieger2004v2 | https://arxiv.org/pdf/cond-mat/0307719v2; Equations 8–11, PDF p. 2; convergence condition in note 21, pp. 4–5; Model description, PDF pp. 1–2; Equations 1–4, p. 2; note 21, pp. 4–5; Equations 7 and 10–11, PDF p. 2; spectral approximation and Figure 1 discussion, p. 3; Equations 3 and 5–11 with the pairwise interpretation, PDF p. 2; Note 21, PDF pp. 4–5; explicit four-cycle calculation in research/discovery/noh-rieger-boundaries.py; Equations 8–11, PDF p. 2; explicit finite matrix interpretation and calculations in research/discovery/noh-rieger-boundaries.py; Figure 1 and the explicitly inexact argument, PDF p. 3; Figure 2 and simulation/extension discussion, pp. 3–4 | supports | arXiv identifier cond-mat/0307719v2 and watermark 19March2004, with printed Dated November26,2024. Actual copy has five PDF pages although abstract metadata says four pages. Cause of mismatch unresolved; no journal-byte equivalence asserted. All five actual PDF pages and24numbered references/notes read; all rendered pages, equations and both figures inspected. ArXiv metadata links PRL92:118701(2004), DOI10.1103/PhysRevLett.92.118701. The source date/page-count mismatch is retained. |
| calculation | research/discovery/noh-rieger-boundaries.py | supports | Exact rational finite graphs compare the deviation-matrix representation with independent absorbing-target first-step equations, verify reciprocal-centrality passage asymmetry and positive returns, separate degree from the full score, and expose the nonconvergent ordinary series on a bipartite four-cycle. The matrix expression is curator mathematics and no paper simulation or author code is replicated. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- This round adds one DRAFT concept, reaching 697 native and 442 unchanged AIO records. The main frontier has 882 entries, including 472 pending and 58 partly addressed cohorts; nested leads remain.
- All five actual PDF pages and24 references/notes read; all rendered pages, equations and both figures inspected. Core pages2–4 visually reread in this continuation.
- Printed PDF date/page-count discrepancies remain unresolved. No publisher-byte equivalence, directed extension, raw experiment replication, author code or early-arrival probability guarantee.
- The original Noh–Rieger centrality is added. Weighted/self-loop extensions, local search and congestion methods, Zhou community algorithms and PDRW-GCN retain separate pending evidence/identity assessments.
- Original Documents synchronization and old round141 cleanup remain unapproved after automatic-review rejection; only the isolated recovery worktree is modified.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T074605Z-noh-rieger-random-walk-centrality
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Noh–Rieger random-walk centrality
started_at: '2026-10-14T07:30:46Z'
finished_at: '2026-10-14T07:46:05Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged convergent deviation series versus periodic
    walks, positive returns versus zero-time hitting, expectation versus arrival-race
    ordering, degree versus return dynamics, and functional-versus-process mappings.
    This is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Noh–Rieger random-walk centrality as DRAFT with a broader mathematical-function
  match and a related Markov-process match. Its aperiodic undirected domain and limited
  mean-passage interpretation are explicit.
source:
  git_revision: 2593b07b341480f709596150ed3ed4ea993e17ce
  state: working_tree
  inputs:
  - path: data/aio/BidirectionalLayer.yaml
    sha256: e5a9046594e0cc0b0ddf152c6d84745d25b3a3246273babbd7a859f01d7270c8
    role: context
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
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
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
  - path: data/curated/BarkerAcceptanceRule.yaml
    sha256: e81a763ba4f2eb2c7e51f3e520311bd111d269f45cdf2417055d72a4ddd4d08c
    role: context
  - path: data/curated/BrandesFleischerGroundedCurrentFlowCloseness.yaml
    sha256: 1419f42eda073f6fc8ca83dc1e65d1f8cb03573ab07240aef71d253323d1dffd
    role: context
  - path: data/curated/EppsteinWangRANDClosenessApproximation.yaml
    sha256: 33d58cab5cddbe19e25fa1f1efa66982a6ca9c461b8cee211df186c570688d19
    role: context
  - path: data/curated/NewmanRandomWalkBetweennessMatrix.yaml
    sha256: 9ed2e0ea7ac76abbf3de52341f78f4944e73b6215af2008fff08888d9fb59bd8
    role: context
  - path: data/curated/NohRiegerRandomWalkCentrality.yaml
    sha256: e96329ed333e5a3658b3ebfa688c5e9b6a8eb2009607adecce3cd6df2d338843
    role: target
  - path: data/curated/PageRank.yaml
    sha256: 8561bc6973069e960effb6f14cd8eaa377e7d5e52ab6c15e2ea4a96f7eeb52e6
    role: context
  - path: data/curated/RiondatoKornaropoulosBetweennessSampling.yaml
    sha256: ea24a1a5cf5019380c36640508cc8a7458203f4491276551898d5477da07f6b8
    role: context
  - path: research/discovery/20261014T073004Z-noh-rieger-random-walk-centrality.json
    sha256: e0de2a41567d9f4d568464bb32eac6c624a11dafa5eff7e03d8ee102257c80af
    role: context
  - path: research/discovery/noh-rieger-boundaries.py
    sha256: 953fe71278d885df2f0070fc0000e2725754a7a02752a6be48b37483ef5b7d94
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
- target_id: AIMech:NohRiegerRandomWalkCentrality
  path: data/curated/NohRiegerRandomWalkCentrality.yaml
  label: Noh–Rieger random-walk centrality
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NohRiegerRandomWalkCentrality.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:NohRiegerRandomWalkCentrality'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:NohRiegerRandomWalkCentrality
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Uninspected source versions and implementation components
    reason: All five downloaded pages and figures read visually and as text. No journal-byte
      equivalence, source-date resolution, raw experiment replication, author-code
      execution, directed extension or probability-of-winning guarantee.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:NohRiegerRandomWalkCentrality
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 308.83s (0:05:08)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 697 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 387 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 388,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:NohRiegerRandomWalkCentrality
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
  - AIMech:NohRiegerRandomWalkCentrality
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
  - AIMech:NohRiegerRandomWalkCentrality
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/noh-rieger-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:NohRiegerRandomWalkCentrality
  exit_code: 0
  expected_exit_code: 0
  summary: '{"triangle": {"degrees": [2, 2, 2], "stationary": ["1/3", "1/3", "1/3"],
    "tau": ["4/9", "4/9", "4/9"], "centrality": ["3/4", "3/4", "3/4"], "mean_hitting_or_positive_return":
    [["3", "2", "2"], ["2", "3", "2"], ["2", "2", "3"]]}, "triangle_with_two_edge_tail":
    {"degrees": [3, 2, 2, 2, 1], "stationary": ["3/10", "1/5", "1/5", "1/5", "1/10"],
    "tau": ["27/50", "67/75", "67/75", "29/25", "69/50"], "centrality": ["5/9", "15/67",
    "15/67", "5/29", "5/69"], "mean_hitting_or_positive_return": [["10/3", "14/3",
    "14/3", "7", "16"], ["2", "5", "10/3", "9", "18"], ["2", "10/3", "5", "9", "18"],
    ["3", "23/3", "23/3", "5", "9"], ["4", "26/3", "26/3", "1", "10"]]}, "bipartite_four_cycle":
    {"deviation_terms": ["3/4", "-1/4", "1/4", "-1/4", "1/4", "-1/4", "1/4", "-1/4"],
    "partial_sums": ["3/4", "1/2", "3/4", "1/2", "3/4", "1/2", "3/4", "1/2"], "ordinary_series_converges":
    false}, "scope": "Exact rational finite checks. Inverse representation is curator
    mathematics equivalent to the convergent deviation series on the two connected
    non-bipartite examples. No source code, simulation replication, directed extension
    or universal early-arrival probability claim."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261014T073004Z-noh-rieger-random-walk-centrality.json
  accessed_at: '2026-10-14T07:30:46Z'
  support: supports
  summary: 'Compared all 442 pinned AIO and 696 native identities; no normalized match.
    Ignored- and hidden-inclusive searches of three full checkouts returned 67,0,0
    lines, all read as existing Noh source references, leads, query strings or review
    limitations. Semantic assessment covered 155 AIO and 541 native definitions: 155
    AIO and540 prior native rows verified unchanged, plus the newly added RK row and
    full record read. Twelve complete AIO contexts and six full native neighbors assessed.
    The identity is the centrality functional pi_i divided by the complete integrated
    excess return probability, with its pairwise mean-passage asymmetry interpretation.
    It differs from stationary visitation/PageRank, Newman net-flow betweenness, resistance-sum
    closeness, sampled shortest-path betweenness and Markov-chain transition construction.
    Network transport/search analysis is the scoped relevance; no learned predictor
    or universal information advantage is asserted.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-14T07:30:46Z'
  support: supports
  summary: A broad MathematicalFunction match is supported by the defined graph/node-to-value
    functional and the target rule/value definition. The related MarkovChain match
    connects the score to its generating process, preserving the distinct abstraction
    levels. The full target node, incident edges, Network parent and hidden-layer
    context were inspected without importing those assertions into the scalar score.
    Ten other targets were rejected for explicit scope reasons.
- evidence_id: nohrieger2004v2
  kind: primary_source
  reference: https://arxiv.org/pdf/cond-mat/0307719v2
  locator: Equations 8–11, PDF p. 2; convergence condition in note 21, pp. 4–5; Model
    description, PDF pp. 1–2; Equations 1–4, p. 2; note 21, pp. 4–5; Equations 7 and
    10–11, PDF p. 2; spectral approximation and Figure 1 discussion, p. 3; Equations
    3 and 5–11 with the pairwise interpretation, PDF p. 2; Note 21, PDF pp. 4–5; explicit
    four-cycle calculation in research/discovery/noh-rieger-boundaries.py; Equations
    8–11, PDF p. 2; explicit finite matrix interpretation and calculations in research/discovery/noh-rieger-boundaries.py;
    Figure 1 and the explicitly inexact argument, PDF p. 3; Figure 2 and simulation/extension
    discussion, pp. 3–4
  accessed_at: '2026-10-14T05:18:31Z'
  snapshot_sha256: 30125860cee7e6da4a0213c2a995b67e69366c9d8f95e02b389bd7aa0a877456
  support: supports
  summary: arXiv identifier cond-mat/0307719v2 and watermark 19March2004, with printed
    Dated November26,2024. Actual copy has five PDF pages although abstract metadata
    says four pages. Cause of mismatch unresolved; no journal-byte equivalence asserted.
    All five actual PDF pages and24numbered references/notes read; all rendered pages,
    equations and both figures inspected. ArXiv metadata links PRL92:118701(2004),
    DOI10.1103/PhysRevLett.92.118701. The source date/page-count mismatch is retained.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/noh-rieger-boundaries.py
  accessed_at: '2026-10-14T07:33:17Z'
  snapshot_sha256: 953fe71278d885df2f0070fc0000e2725754a7a02752a6be48b37483ef5b7d94
  support: supports
  summary: Exact rational finite graphs compare the deviation-matrix representation
    with independent absorbing-target first-step equations, verify reciprocal-centrality
    passage asymmetry and positive returns, separate degree from the full score, and
    expose the nonconvergent ordinary series on a bipartite four-cycle. The matrix
    expression is curator mathematics and no paper simulation or author code is replicated.
assessments:
- assessment_id: identity
  area: identity
  topic: Noh–Rieger random-walk centrality
  outcome: supported
  target_ids:
  - AIMech:NohRiegerRandomWalkCentrality
  evidence_ids:
  - identity
  - nohrieger2004v2
  summary: Retain this distinct DRAFT mathematical_method.
  details: Retain the Noh–Rieger return-dynamics functional separately from degree/stationary
    visitation, PageRank, Newman current-flow betweenness, resistance-sum closeness,
    sampled geodesic centralities and a Markov transition-construction algorithm.
    Network transport/search supplies bounded relevance; no learned predictor is asserted.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:NohRiegerRandomWalkCentrality
  evidence_ids:
  - mapping
  - nohrieger2004v2
  summary: The explicit AIO mapping assessment is supported within its stated scope.
  details: A broad MathematicalFunction match is supported by the defined graph/node-to-value
    functional and the target rule/value definition. The related MarkovChain match
    connects the score to its generating process, preserving the distinct abstraction
    levels. The full target node, incident edges, Network parent and hidden-layer
    context were inspected without importing those assertions into the scalar score.
    Ten other targets were rejected for explicit scope reasons.
- assessment_id: walk-domain
  area: evidence
  topic: walk-domain
  outcome: supported
  target_ids:
  - AIMech:NohRiegerRandomWalkCentrality
  evidence_ids:
  - nohrieger2004v2
  summary: Supported within the stated primary-source and mathematical scope.
  details: The actual core is a finite connected unweighted simple undirected graph
    with an odd cycle. The row-stochastic neighbor walk has stationary degree/total-degree
    probabilities. No disconnected cross-component, directed or interacting-walker
    extension is adopted.
- assessment_id: integrated-return-score
  area: evidence
  topic: integrated-return-score
  outcome: supported
  target_ids:
  - AIMech:NohRiegerRandomWalkCentrality
  evidence_ids:
  - nohrieger2004v2
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equations7,10,11 support R, tau and pi/tau with the t=0 term. The source
    spectral single-mode estimate remains an approximation. Triangle scores sum to9/4,
    directly excluding a probability-distribution interpretation; equal-degree tail
    nodes have different scores.
- assessment_id: mean-first-passage-asymmetry
  area: evidence
  topic: mean-first-passage-asymmetry
  outcome: supported
  target_ids:
  - AIMech:NohRiegerRandomWalkCentrality
  evidence_ids:
  - nohrieger2004v2
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Equation8 distinguishes positive return1/pi from off-diagonal passage.
    Detailed balance cancels cross terms and yields H_ij-H_ji=1/C_j-1/C_i. The sign
    interpretation in the record is correct and restricted to means, without claiming
    realization-wise or arrival-race ordering.
- assessment_id: periodic-walk-boundary
  area: evidence
  topic: periodic-walk-boundary
  outcome: supported
  target_ids:
  - AIMech:NohRiegerRandomWalkCentrality
  evidence_ids:
  - nohrieger2004v2
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Note21 explicitly states the odd-cycle restriction and self-loop modification.
    On C4 the t=0 term is3/4 and subsequent terms alternate; partial sums alternate3/4
    and1/2. A matrix generalized inverse must not be substituted silently for an ordinary
    convergent series.
- assessment_id: finite-algebraic-checks
  area: evidence
  topic: finite-algebraic-checks
  outcome: supported
  target_ids:
  - AIMech:NohRiegerRandomWalkCentrality
  evidence_ids:
  - nohrieger2004v2
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Exact rational inversion on two connected non-bipartite graphs is checked
    against independently solved absorbing-target equations and the positive-return
    first-step relation. Triangle C=3/4 and tail comparison15/67 versus5/29 agree
    with H13=9,H31=23/3 and reciprocal difference4/3. These are mathematical examples,
    not source-simulation replication.
- assessment_id: interpretation-and-evaluation-limits
  area: evidence
  topic: interpretation-and-evaluation-limits
  outcome: supported
  target_ids:
  - AIMech:NohRiegerRandomWalkCentrality
  evidence_ids:
  - nohrieger2004v2
  summary: Supported within the stated primary-source and mathematical scope.
  details: The paper labels its early-visit argument inexact. Figure1 BA10000 and
    Figure2 BA512/hierarchical625 scope is retained, with initially one noninteracting
    walker per node. The record adds no universal degree monotonicity, causal influence,
    learned prediction, congestion or directed validity.
- assessment_id: constructed-boundaries
  area: consistency
  topic: convergent deviation series versus periodic walks, positive returns versus
    zero-time hitting, expectation versus arrival-race ordering, degree versus return
    dynamics, and functional-versus-process mappings
  outcome: supported
  target_ids:
  - AIMech:NohRiegerRandomWalkCentrality
  evidence_ids:
  - nohrieger2004v2
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Exact rational finite graphs compare the deviation-matrix representation
    with independent absorbing-target first-step equations, verify reciprocal-centrality
    passage asymmetry and positive returns, separate degree from the full score, and
    expose the nonconvergent ordinary series on a bipartite four-cycle. The matrix
    expression is curator mathematics and no paper simulation or author code is replicated.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:NohRiegerRandomWalkCentrality
  evidence_ids:
  - identity
  - mapping
  - nohrieger2004v2
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. All maintained fields, six claims, definition evidence
    and source metadata read after capture. The maintained functional uses the complete
    convergent deviation sum, including t=0. Positive returns, undirected reversibility,
    odd-cycle convergence and the explicitly inexact early-visit interpretation remain
    separated. The source printed-date/page-count mismatch is preserved.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- This round adds one DRAFT concept, reaching 697 native and 442 unchanged AIO records.
  The main frontier has 882 entries, including 472 pending and 58 partly addressed
  cohorts; nested leads remain.
- All five actual PDF pages and24 references/notes read; all rendered pages, equations
  and both figures inspected. Core pages2–4 visually reread in this continuation.
- Printed PDF date/page-count discrepancies remain unresolved. No publisher-byte equivalence,
  directed extension, raw experiment replication, author code or early-arrival probability
  guarantee.
- The original Noh–Rieger centrality is added. Weighted/self-loop extensions, local
  search and congestion methods, Zhou community algorithms and PDRW-GCN retain separate
  pending evidence/identity assessments.
- Original Documents synchronization and old round141 cleanup remain unapproved after
  automatic-review rejection; only the isolated recovery worktree is modified.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
