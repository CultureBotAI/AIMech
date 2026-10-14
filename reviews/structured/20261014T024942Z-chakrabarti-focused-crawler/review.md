# Scientific author self-review of Chakrabarti classifier-guided focused crawling

- Review: 20261014T024942Z-chakrabarti-focused-crawler
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-14T02:43:32Z
- Finished UTC: 2026-10-14T02:49:42Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Chakrabarti classifier-guided focused crawling as DRAFT with a related AIO Classification mapping. Author self-review supports the acquisition policies and interface while preserving the printed probability discrepancy and historical evaluation limits.

## Scope And Provenance

All maintained fields and the complete inspected primary sources.

Selection: Exact maintained ID: AIMech:ChakrabartiFocusedCrawler
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base deb57eebe330c3976c6dd440e2ce9379613147d6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ChakrabartiFocusedCrawler | data/curated/ChakrabartiFocusedCrawler.yaml | maintained | Chakrabarti classifier-guided focused crawling |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:ChakrabartiFocusedCrawler | All checks passed!<br>........................................................................ [ 28%]<br>........................................................................ [ 57%]<br>........................................................................ [ 86%]<br>...............................sss                                       [100%]<br>247 passed, 3 skipped in 168.07s (0:02:48)<br>Checked 442 record(s); 0 failed.<br>Checked 681 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 368 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 366,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:ChakrabartiFocusedCrawler | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| uv run --locked aimech check-source | passed | True | AIMech:ChakrabartiFocusedCrawler | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:ChakrabartiFocusedCrawler | Exited0 without output. |
| Constructed mechanism boundaries | passed | True | AIMech:ChakrabartiFocusedCrawler | {"probability_equation": {"literal": ["1/8", "3/8"], "literal_sum": "1/2", "normalized_bayes": ["1/4", "3/4"]}, "hard_versus_soft": {"hard_expands": false, "soft_relevance": "3/5"}, "frontier_order": ["new-low", "tried-high"], "parent_priority_max": "3/4", "weighted_link_step": {"allowed_edges": [["low-hub", "good-authority"], ["high-hub", "good-authority"]], "raw_authorities": {"good-authority": "9/5", "bad-authority": "0"}, "raw_hubs": {"low-hub": "9/25", "high-hub": "36/25", "same-site": "0"}, "hub_ratio": "4"}, "limits": "Exact finite arithmetic on constructed inputs. Common positive norm scaling preserves the displayed ratios; this is not a convergence proof, classifier training, author-code conformance test or historical benchmark."} |

## Scientific And Domain Assessments

### Chakrabarti classifier-guided focused crawling

identity: supported. Targets: AIMech:ChakrabartiFocusedCrawler.

Retain this distinct DRAFT algorithm.

Retain the hard/soft 1999 acquisition family separately from its classifier, general best-first search, Flake maximum-flow crawling and the distinct relevance-weighted distiller. The actual paper presents the two focus policies together with a shared topic-tree and system interface.

### Explicit AIO mapping

grounding: supported. Targets: AIMech:ChakrabartiFocusedCrawler.

The explicit AIO mapping assessment is supported within its stated scope.

Retain the related Classification task mapping because trained topic assignment directly controls traversal and priorities. This is neither classifier identity nor an AIO subclass assertion. The supplied hierarchy is not inferred; eleven complete AIO node/edge/record contexts were inspected and all generated YAMLs reread after capture.

### taxonomy-and-classifier

evidence: supported. Targets: AIMech:ChakrabartiFocusedCrawler.

Supported within the stated primary-source and mathematical scope.

Sections 3/3.1 require an antichain of selected good topics and assume a hierarchical partition of documents. The bag-of-words generator uses class priors; the record calls this the intended model and explicitly retains the nonnormalizing printed Equation 1 elsewhere.

### focus-policies

evidence: supported. Targets: AIMech:ChakrabartiFocusedCrawler.

Supported within the stated primary-source and mathematical scope.

Rendered pages 7–8 specify the maximum-leaf ancestor test versus summed good-topic mass, maximum over multiple referring parents and post-fetch updates. The finite example has good-topic mass 3/5 but an outside maximum leaf of 2/5; it explains why these are distinct rules without asserting observed performance.

### frontier-and-distiller

evidence: supported. Targets: AIMech:ChakrabartiFocusedCrawler.

Supported within the stated primary-source and mathematical scope.

Rendered page 9 prioritizes numtries before relevance, states arbitrary hard-focus ties and describes stopping for distiller execution and promoting hub neighbors. The finite ordering example confirms that a new low-score URL outranks an already-tried high-score URL. Later relational/concurrent work remains outside this version.

### probability-equation-boundary

evidence: supported. Targets: AIMech:ChakrabartiFocusedCrawler.

Supported within the stated primary-source and mathematical scope.

Rendered Equation 1 includes a prior in the numerator only. Exact rational arithmetic gives a total of 1/2 for the supplied two-class example, versus one under a properly prior-weighted denominator. This is a presentation-boundary check, not an author-code bug or corrected implementation claim.

### evaluation-boundary

evidence: supported. Targets: AIMech:ChakrabartiFocusedCrawler.

Supported within the stated primary-source and mathematical scope.

Rendered page 10 explicitly says automatic classifier scores replace impractical human inspection and defends this as evaluation of the neighborhood crawl heuristic. Figures use URL counts, and Sections 4.3–4.4 provide indirect overlap evidence. These are correctly separated from calibrated relevance, exhaustive recall and universal seed invariance.

### failure-and-scope

evidence: supported. Targets: AIMech:ChakrabartiFocusedCrawler.

Supported within the stated primary-source and mathematical scope.

Sections 4.1/4.2/4.7 identify topic mixing, hard-pruning loss, soft diffusion and image-map/text-poor misclassification. The average-relevance objective is aspirational rather than a proved global optimum. The record makes no medical or social-causal assertion from historical topic names.

### classifier-guided acquisition versus link-ranking scope, intended probabilities versus a printed normalization discrepancy, directional edge weights, authority-only eligibility and classifier-defined evaluation

consistency: supported. Targets: AIMech:ChakrabartiFocusedCrawler.

Constructed calculations support the stated distinctions.

Exact finite arithmetic checks the printed probability normalization, hard versus soft focus distinction, lexicographic attempt ordering and asymmetric hub/authority weights under an explicit inter-site eligibility mask. No author code, live crawl, training or historical benchmark is executed.

### All maintained fields

provenance: supported. Targets: AIMech:ChakrabartiFocusedCrawler.

Complete maintained record inspected; DRAFT remains.

Read ID/name/aliases, kind, definition and evidence, identity context, all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping, limitations and actual curation timestamps. Capture/source/context hashes and exact report mirror agree. Every maintained field and all six claims were read, with exact locators and source-byte identity checked. The record preserves the supplied taxonomy, lexicographic attempt-first ordering, printed denominator ambiguity, same-classifier evaluation and historical implementation boundaries.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261014T024328Z-chakrabarti-focused-crawler.json | supports | Compared all 442 pinned AIO and 679 native IDs, names, aliases and scoped synonyms before either cohort write; no normalized identity match. Ignored- and hidden-inclusive searches of three checkouts returned 26,0,0 lines, all read: prior deduplication logs and the source lead, not these maintained identities. Semantic search covered 127 AIO and 439 native definitions: 70 AIO and 318 native rows match previously inspected unchanged context; all 57 newly selected AIO and 121 new native definitions were read. Eleven complete AIO nodes, incident edges and generated records were assessed, with full native NaiveBayes, BestFirstSearch, DINOSelfDistillation and FlakeFocusedCrawl context. The classifier-guided acquisition family and relevance-weighted ranking component were compared directly. The concept is the 1999 classifier-guided acquisition family with hard and soft focus modes and periodic distiller integration. A human taxonomy is an input, not a learned hierarchy. It differs from Flake flow grouping, general best-first search and the naive Bayes component alone. |
| mapping | sources/aio/aio.json | supports | Retain the related Classification task mapping because trained topic assignment directly controls traversal and priorities. This is neither classifier identity nor an AIO subclass assertion. The supplied hierarchy is not inferred; eleven complete AIO node/edge/record contexts were inspected and all generated YAMLs reread after capture. |
| chakrabarti1999 | https://www.cse.iitb.ac.in/~soumen/doc/www1999f/pdf/www1999f.pdf; Sections 3.1–3.3 and Figure 2, printed pp. 551–553 / PDF pp. 7–9; Sections 2.3, 3 and 3.1, printed pp. 549–551 / PDF pp. 5–7; Section 3.1, printed pp. 551–552 / PDF pp. 7–8; curator finite example in research/discovery/focused-crawling-boundaries.py; Sections 3.2–3.3, printed pp. 552–553 / PDF pp. 8–9; Section 3.1, Equation 1, printed p. 551 / PDF p. 7; exact curator arithmetic in research/discovery/focused-crawling-boundaries.py; Sections 4.1–4.4 and Figures 3–8, printed pp. 553–558 / PDF pp. 9–14; Sections 3, 4.1–4.3, 4.7 and 6, printed pp. 550,553–556,559–561 / PDF pp. 6,9–12,15–17 | supports | 1999 author-hosted Elsevier-layout PDF, eighteen pages, displayed pagination 546–562 after its unnumbered first page. All text and 31 references read; rendered pages 4,6–8,10–15 inspected, covering all ten figures and central formulas. Publisher metadata lists Computer Networks 31(11–16):1623–1640; locators here use the inspected PDF pagination, without claiming identical bytes to the unavailable publisher full text. |
| calculation | research/discovery/focused-crawling-boundaries.py | supports | Exact finite arithmetic checks the printed probability normalization, hard versus soft focus distinction, lexicographic attempt ordering and asymmetric hub/authority weights under an explicit inter-site eligibility mask. No author code, live crawl, training or historical benchmark is executed. |

## Limits And Additional Notes

- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark replication.
- This cohort step adds one DRAFT record, reaching 680 native and 442 unchanged AIO records. The main frontier now has 865 entries, including 473 pending and 58 partly addressed cohorts; nested leads remain.
- Complete eighteen-page primary text and 31 references read. Rendered pages 4,6–8,10–15 cover all ten figures and displayed formulas; relevant tables/URL lists and captions read. Historical URLs not visited.
- Primary methods were read; no author-code execution, model fitting, paid service, data upload, hardware benchmark or formal theorem certification. Constructed arithmetic examples are not experiment replication.
- Original Documents checkout synchronization and old round141 cleanup remain unapproved after automatic-review rejection; only the isolated recovery checkout is changed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T024942Z-chakrabarti-focused-crawler
kind: record
repository: CultureBotAI/AIMech
title: Scientific author self-review of Chakrabarti classifier-guided focused crawling
started_at: '2026-10-14T02:43:32Z'
finished_at: '2026-10-14T02:49:42Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The author challenged classifier-guided acquisition versus link-ranking
    scope, intended probabilities versus a printed normalization discrepancy, directional
    edge weights, authority-only eligibility and classifier-defined evaluation. This
    is adversarial author self-review, not independent approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Chakrabarti classifier-guided focused crawling as DRAFT with a related
  AIO Classification mapping. Author self-review supports the acquisition policies
  and interface while preserving the printed probability discrepancy and historical
  evaluation limits.
source:
  git_revision: deb57eebe330c3976c6dd440e2ce9379613147d6
  state: working_tree
  inputs:
  - path: data/aio/Classification.yaml
    sha256: d97da621c5052c7ab913cda95184ea2cca274f803298fd5f2c1273a22a211219
    role: context
  - path: data/aio/Clustering.yaml
    sha256: 3727f99787bb5748c57338221c984e2575abc538ae51ebf3c6e69ef0da9405d5
    role: context
  - path: data/aio/DataPreparation.yaml
    sha256: 99aebfc324b628969407ddc7591312e992db1469e7ef8fb3ad28e4b62d3bb359
    role: context
  - path: data/aio/Distillation.yaml
    sha256: 02faf8db468fca6adfe257a141c98c7b13f85dc301e856a1f9622dfdb68ae5c9
    role: context
  - path: data/aio/GraphLanguageModel.yaml
    sha256: 1cdda6f7d19946e0672835185e179e2336832225c180e2b70d7860b0c96fc2a8
    role: context
  - path: data/aio/HierarchicalClassification.yaml
    sha256: 5e1f65090a3a9e7842b57c12410a7279d02c60baef05844fa1dd73545f1cbfc7
    role: context
  - path: data/aio/MathematicalFunction.yaml
    sha256: a94d32b253e2a11dd3485b77f282486b775ffe577c8ef824d45875721317fca0
    role: context
  - path: data/aio/OrdinalLLM.yaml
    sha256: 2bbb482a7007dd95f6e644863e264f646f7cc40e3debc05273bdb7ac96160d4b
    role: context
  - path: data/aio/ProbabilisticTopicModel.yaml
    sha256: a3ddfd23b511de967f562e99542d8a89109852359d286a4d707d784359ddfe32
    role: context
  - path: data/aio/RankingBias.yaml
    sha256: 3e931657e0ee2a47e36a7858dbb8f26f00b565040f4fedd138f55353551160b0
    role: context
  - path: data/aio/RetrievalAugmentedLLM.yaml
    sha256: 05511e7f4671c2940df670a17ac14f579560dba5b45794d4c9f40e300ba17a8f
    role: context
  - path: data/curated/BestFirstSearch.yaml
    sha256: d43811f831e3a4d2c08e861f5a973c03ec481c1b406d724c042847b7dbb426bf
    role: context
  - path: data/curated/ChakrabartiFocusedCrawler.yaml
    sha256: b8ef804f124949e9d98895169e9d41693ae10931ddd8b21ffd6ae8e94fd7cd30
    role: target
  - path: data/curated/DINOSelfDistillation.yaml
    sha256: 66ac3400efd5deda6468cb7e8ae53f3c7f6f0cf942557b634ef3a7bdafc93516
    role: context
  - path: data/curated/FlakeFocusedCrawl.yaml
    sha256: 09eeae7222206c9076299b965786077221c4f5b3167c2a560d84edd47021ed1f
    role: context
  - path: data/curated/NaiveBayes.yaml
    sha256: 99caf757d49a76920b59c60591beeaf1f019ec0d1acb7ae5944ea0f5f7339b61
    role: context
  - path: research/discovery/20261014T024328Z-chakrabarti-focused-crawler.json
    sha256: f46c21799af3e2a69a1e96ec57d231e766d80bc0e74c3ce0fd1afd1c2facbacf
    role: context
  - path: research/discovery/focused-crawling-boundaries.py
    sha256: 8b0173f5e9b85a0d09f1fcf8459b1e2d341a3c31d2fa400c493178ee839cbb7f
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
- target_id: AIMech:ChakrabartiFocusedCrawler
  path: data/curated/ChakrabartiFocusedCrawler.yaml
  label: Chakrabarti classifier-guided focused crawling
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ChakrabartiFocusedCrawler.yaml
    role: maintained
scope:
  description: All maintained fields and the complete inspected primary sources.
  selection: 'Exact maintained ID: AIMech:ChakrabartiFocusedCrawler'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - AIMech:ChakrabartiFocusedCrawler
  exclusions:
  - target: Neighboring AIO and native records
    reason: Identity and mapping context, not complete scientific rereview.
  - target: Uninspected source versions and implementation components
    reason: No author implementation, classifier training details beyond this paper,
      historical data or current-web crawl were inspected. Printed probability and
      ranking-count ambiguities remain unresolved at implementation level. Constructed
      arithmetic is not benchmark replication.
  - target: Training, benchmark replication and universal guarantees
    reason: No model fitting, hardware experiment or general convergence certification.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:ChakrabartiFocusedCrawler
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 28%]\n........................................................................\
    \ [ 57%]\n........................................................................\
    \ [ 86%]\n...............................sss                                 \
    \      [100%]\n247 passed, 3 skipped in 168.07s (0:02:48)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 681 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 368 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 366,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:ChakrabartiFocusedCrawler
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
  - AIMech:ChakrabartiFocusedCrawler
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
  - AIMech:ChakrabartiFocusedCrawler
  exit_code: 0
  expected_exit_code: 0
  summary: Exited0 without output.
- check_id: calculation
  name: Constructed mechanism boundaries
  command: python3 research/discovery/focused-crawling-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:ChakrabartiFocusedCrawler
  exit_code: 0
  expected_exit_code: 0
  summary: '{"probability_equation": {"literal": ["1/8", "3/8"], "literal_sum": "1/2",
    "normalized_bayes": ["1/4", "3/4"]}, "hard_versus_soft": {"hard_expands": false,
    "soft_relevance": "3/5"}, "frontier_order": ["new-low", "tried-high"], "parent_priority_max":
    "3/4", "weighted_link_step": {"allowed_edges": [["low-hub", "good-authority"],
    ["high-hub", "good-authority"]], "raw_authorities": {"good-authority": "9/5",
    "bad-authority": "0"}, "raw_hubs": {"low-hub": "9/25", "high-hub": "36/25", "same-site":
    "0"}, "hub_ratio": "4"}, "limits": "Exact finite arithmetic on constructed inputs.
    Common positive norm scaling preserves the displayed ratios; this is not a convergence
    proof, classifier training, author-code conformance test or historical benchmark."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261014T024328Z-chakrabarti-focused-crawler.json
  accessed_at: '2026-10-14T02:43:32Z'
  support: supports
  summary: 'Compared all 442 pinned AIO and 679 native IDs, names, aliases and scoped
    synonyms before either cohort write; no normalized identity match. Ignored- and
    hidden-inclusive searches of three checkouts returned 26,0,0 lines, all read:
    prior deduplication logs and the source lead, not these maintained identities.
    Semantic search covered 127 AIO and 439 native definitions: 70 AIO and 318 native
    rows match previously inspected unchanged context; all 57 newly selected AIO and
    121 new native definitions were read. Eleven complete AIO nodes, incident edges
    and generated records were assessed, with full native NaiveBayes, BestFirstSearch,
    DINOSelfDistillation and FlakeFocusedCrawl context. The classifier-guided acquisition
    family and relevance-weighted ranking component were compared directly. The concept
    is the 1999 classifier-guided acquisition family with hard and soft focus modes
    and periodic distiller integration. A human taxonomy is an input, not a learned
    hierarchy. It differs from Flake flow grouping, general best-first search and
    the naive Bayes component alone.'
  search_scope: All maintained/generated IDs, labels, aliases and scoped synonyms
    normalized; full-text searches of the public clone and readable previous worktree
    include ignored/hidden files. Original Documents access is restored; its full
    readable checkout is included, with no mutation.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  accessed_at: '2026-10-14T02:43:32Z'
  support: supports
  summary: Retain the related Classification task mapping because trained topic assignment
    directly controls traversal and priorities. This is neither classifier identity
    nor an AIO subclass assertion. The supplied hierarchy is not inferred; eleven
    complete AIO node/edge/record contexts were inspected and all generated YAMLs
    reread after capture.
- evidence_id: chakrabarti1999
  kind: primary_source
  reference: https://www.cse.iitb.ac.in/~soumen/doc/www1999f/pdf/www1999f.pdf
  locator: Sections 3.1–3.3 and Figure 2, printed pp. 551–553 / PDF pp. 7–9; Sections
    2.3, 3 and 3.1, printed pp. 549–551 / PDF pp. 5–7; Section 3.1, printed pp. 551–552
    / PDF pp. 7–8; curator finite example in research/discovery/focused-crawling-boundaries.py;
    Sections 3.2–3.3, printed pp. 552–553 / PDF pp. 8–9; Section 3.1, Equation 1,
    printed p. 551 / PDF p. 7; exact curator arithmetic in research/discovery/focused-crawling-boundaries.py;
    Sections 4.1–4.4 and Figures 3–8, printed pp. 553–558 / PDF pp. 9–14; Sections
    3, 4.1–4.3, 4.7 and 6, printed pp. 550,553–556,559–561 / PDF pp. 6,9–12,15–17
  accessed_at: '2026-10-14T02:28:13Z'
  snapshot_sha256: bd6570f7155839c2bf83552c2acfc65a37cdb017da2f030f4f266414b1c23ac0
  support: supports
  summary: 1999 author-hosted Elsevier-layout PDF, eighteen pages, displayed pagination
    546–562 after its unnumbered first page. All text and 31 references read; rendered
    pages 4,6–8,10–15 inspected, covering all ten figures and central formulas. Publisher
    metadata lists Computer Networks 31(11–16):1623–1640; locators here use the inspected
    PDF pagination, without claiming identical bytes to the unavailable publisher
    full text.
- evidence_id: calculation
  kind: record_content
  reference: research/discovery/focused-crawling-boundaries.py
  accessed_at: '2026-10-14T02:45:10Z'
  snapshot_sha256: 8b0173f5e9b85a0d09f1fcf8459b1e2d341a3c31d2fa400c493178ee839cbb7f
  support: supports
  summary: Exact finite arithmetic checks the printed probability normalization, hard
    versus soft focus distinction, lexicographic attempt ordering and asymmetric hub/authority
    weights under an explicit inter-site eligibility mask. No author code, live crawl,
    training or historical benchmark is executed.
assessments:
- assessment_id: identity
  area: identity
  topic: Chakrabarti classifier-guided focused crawling
  outcome: supported
  target_ids:
  - AIMech:ChakrabartiFocusedCrawler
  evidence_ids:
  - identity
  - chakrabarti1999
  summary: Retain this distinct DRAFT algorithm.
  details: Retain the hard/soft 1999 acquisition family separately from its classifier,
    general best-first search, Flake maximum-flow crawling and the distinct relevance-weighted
    distiller. The actual paper presents the two focus policies together with a shared
    topic-tree and system interface.
- assessment_id: mapping
  area: grounding
  topic: Explicit AIO mapping
  outcome: supported
  target_ids:
  - AIMech:ChakrabartiFocusedCrawler
  evidence_ids:
  - mapping
  - chakrabarti1999
  summary: The explicit AIO mapping assessment is supported within its stated scope.
  details: Retain the related Classification task mapping because trained topic assignment
    directly controls traversal and priorities. This is neither classifier identity
    nor an AIO subclass assertion. The supplied hierarchy is not inferred; eleven
    complete AIO node/edge/record contexts were inspected and all generated YAMLs
    reread after capture.
- assessment_id: taxonomy-and-classifier
  area: evidence
  topic: taxonomy-and-classifier
  outcome: supported
  target_ids:
  - AIMech:ChakrabartiFocusedCrawler
  evidence_ids:
  - chakrabarti1999
  summary: Supported within the stated primary-source and mathematical scope.
  details: Sections 3/3.1 require an antichain of selected good topics and assume
    a hierarchical partition of documents. The bag-of-words generator uses class priors;
    the record calls this the intended model and explicitly retains the nonnormalizing
    printed Equation 1 elsewhere.
- assessment_id: focus-policies
  area: evidence
  topic: focus-policies
  outcome: supported
  target_ids:
  - AIMech:ChakrabartiFocusedCrawler
  evidence_ids:
  - chakrabarti1999
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Rendered pages 7–8 specify the maximum-leaf ancestor test versus summed
    good-topic mass, maximum over multiple referring parents and post-fetch updates.
    The finite example has good-topic mass 3/5 but an outside maximum leaf of 2/5;
    it explains why these are distinct rules without asserting observed performance.
- assessment_id: frontier-and-distiller
  area: evidence
  topic: frontier-and-distiller
  outcome: supported
  target_ids:
  - AIMech:ChakrabartiFocusedCrawler
  evidence_ids:
  - chakrabarti1999
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Rendered page 9 prioritizes numtries before relevance, states arbitrary
    hard-focus ties and describes stopping for distiller execution and promoting hub
    neighbors. The finite ordering example confirms that a new low-score URL outranks
    an already-tried high-score URL. Later relational/concurrent work remains outside
    this version.
- assessment_id: probability-equation-boundary
  area: evidence
  topic: probability-equation-boundary
  outcome: supported
  target_ids:
  - AIMech:ChakrabartiFocusedCrawler
  evidence_ids:
  - chakrabarti1999
  - calculation
  summary: Supported within the stated primary-source and mathematical scope.
  details: Rendered Equation 1 includes a prior in the numerator only. Exact rational
    arithmetic gives a total of 1/2 for the supplied two-class example, versus one
    under a properly prior-weighted denominator. This is a presentation-boundary check,
    not an author-code bug or corrected implementation claim.
- assessment_id: evaluation-boundary
  area: evidence
  topic: evaluation-boundary
  outcome: supported
  target_ids:
  - AIMech:ChakrabartiFocusedCrawler
  evidence_ids:
  - chakrabarti1999
  summary: Supported within the stated primary-source and mathematical scope.
  details: Rendered page 10 explicitly says automatic classifier scores replace impractical
    human inspection and defends this as evaluation of the neighborhood crawl heuristic.
    Figures use URL counts, and Sections 4.3–4.4 provide indirect overlap evidence.
    These are correctly separated from calibrated relevance, exhaustive recall and
    universal seed invariance.
- assessment_id: failure-and-scope
  area: evidence
  topic: failure-and-scope
  outcome: supported
  target_ids:
  - AIMech:ChakrabartiFocusedCrawler
  evidence_ids:
  - chakrabarti1999
  summary: Supported within the stated primary-source and mathematical scope.
  details: Sections 4.1/4.2/4.7 identify topic mixing, hard-pruning loss, soft diffusion
    and image-map/text-poor misclassification. The average-relevance objective is
    aspirational rather than a proved global optimum. The record makes no medical
    or social-causal assertion from historical topic names.
- assessment_id: constructed-boundaries
  area: consistency
  topic: classifier-guided acquisition versus link-ranking scope, intended probabilities
    versus a printed normalization discrepancy, directional edge weights, authority-only
    eligibility and classifier-defined evaluation
  outcome: supported
  target_ids:
  - AIMech:ChakrabartiFocusedCrawler
  evidence_ids:
  - chakrabarti1999
  - calculation
  summary: Constructed calculations support the stated distinctions.
  details: Exact finite arithmetic checks the printed probability normalization, hard
    versus soft focus distinction, lexicographic attempt ordering and asymmetric hub/authority
    weights under an explicit inter-site eligibility mask. No author code, live crawl,
    training or historical benchmark is executed.
- assessment_id: complete-fields
  area: provenance
  topic: All maintained fields
  outcome: supported
  target_ids:
  - AIMech:ChakrabartiFocusedCrawler
  evidence_ids:
  - identity
  - mapping
  - chakrabarti1999
  summary: Complete maintained record inspected; DRAFT remains.
  details: Read ID/name/aliases, kind, definition and evidence, identity context,
    all 6 claims/locators, source identities/versions/access/hashes, AIO pin and mapping,
    limitations and actual curation timestamps. Capture/source/context hashes and
    exact report mirror agree. Every maintained field and all six claims were read,
    with exact locators and source-byte identity checked. The record preserves the
    supplied taxonomy, lexicographic attempt-first ordering, printed denominator ambiguity,
    same-classifier evaluation and historical implementation boundaries.
findings: []
actions: []
limitations:
- Author self-review only; no independent approval or status promotion.
- Constructed calculations assess mathematical boundaries; they are not benchmark
  replication.
- This cohort step adds one DRAFT record, reaching 680 native and 442 unchanged AIO
  records. The main frontier now has 865 entries, including 473 pending and 58 partly
  addressed cohorts; nested leads remain.
- Complete eighteen-page primary text and 31 references read. Rendered pages 4,6–8,10–15
  cover all ten figures and displayed formulas; relevant tables/URL lists and captions
  read. Historical URLs not visited.
- Primary methods were read; no author-code execution, model fitting, paid service,
  data upload, hardware benchmark or formal theorem certification. Constructed arithmetic
  examples are not experiment replication.
- Original Documents checkout synchronization and old round141 cleanup remain unapproved
  after automatic-review rejection; only the isolated recovery checkout is changed.
related_reviews: []
links: []
tags:
- native-concepts
- self-review
- discovery-ongoing
```
