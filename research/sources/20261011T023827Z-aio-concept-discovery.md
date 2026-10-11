# AIO concept discovery and addition assessment

Started 2026-10-11T02:34:04Z; assessed 2026-10-11T02:46:50Z. AIMech base `945bd67d190e867ac379f8d4ebbc6d4ddec152a9`.

**Result: 442 of 442 accepted AIO classes are present; zero new native records can currently be added.** The review of 36 classical-ML requests produced 32 local upstream-term proposals, three deferrals and one existing alias. No proposal has been assigned an AIO ID or submitted upstream.

The add-record workflow requires accepted AIO identities. The scan reached that boundary: every current accepted class already reproduces in AIMech. This does not mean that AIO contains every AI concept; the proposal ledger and additional source leads show remaining vocabulary work.

## Scope and stopping criterion

The user requested iterative discovery, review and addition with the add-record skill. This assessment searches the pinned AIO release, current upstream main/latest release, committed source template, live source sheet, and the full open-issue/open-PR queues. It reviews primary method evidence for the finite 36-candidate roster in issue 167. All 56 open issue bodies are triaged; comments, closed history and every external source catalog are not exhaustively reviewed.

Stop adding records when those authoritative AIO identifier sets yield zero unimported classes. Route unsupported candidates into upstream proposals, retain duplicates and deferrals, and do not fabricate identifiers or rewrite generated YAML. Global AI-concept exhaustion is neither claimed nor established.

## Discovery rounds

| Round | Surface checked | Result |
| --- | --- | --- |
| 1 | Pinned JSON and generated corpus | 442 classes; 0 missing, changed or unexpected records |
| 2 | Upstream main/latest release and committed ROBOT template | Same 442 IDs; current release JSON byte-identical to the pin |
| 3 | Live maintained Google Sheet | 442 AIO IDs; 0 additional or missing IDs; other cells not compared |
| 4 | 56 open issues, 0 open PRs; 36 named classical-ML requests | 32 draft proposals; 3 deferred; 1 existing alias; 0 accepted additions |

## Source comparison and reuse

| Source | Version, access and ownership | Disposition |
| --- | --- | --- |
| [AIO release](https://github.com/berkeleybop/artificial-intelligence-ontology/releases/tag/v2026-07-22) and [JSON](https://github.com/berkeleybop/artificial-intelligence-ontology/blob/397851c547d1c4d8f06ef184f63c1d40bc86937a/aio.json) | Release 2026-07-22; commit `397851c547d1c4d8f06ef184f63c1d40bc86937a`; CC-BY-4.0; stable AIO IRIs | Already fully represented; no source refresh |
| [ROBOT template](https://github.com/berkeleybop/artificial-intelligence-ontology/blob/397851c547d1c4d8f06ef184f63c1d40bc86937a/src/ontology/aio-src.csv) | Same commit; 442 AIO rows plus template metadata | No additional accepted ID |
| [Live source sheet](https://docs.google.com/spreadsheets/d/1LVubUGg56YDGJ0VUdJDMNBPY8iFfissRfy4eM56bUFg/export?exportFormat=csv) | Retrieved 2026-10-11T02:40:25.609969+00:00; hash `635f00309bbf94f4b53a9a09f9c54157672e8c16f782bd9229712380b72ffec1`; maintained input established by [aio.Makefile](https://github.com/berkeleybop/artificial-intelligence-ontology/blob/397851c547d1c4d8f06ef184f63c1d40bc86937a/src/ontology/aio.Makefile) | Same identifier set; no claim of whole-sheet semantic equality |
| [Upstream requests](https://github.com/berkeleybop/artificial-intelligence-ontology/issues) | Public open-issue list, limit 200 returned 56; open-PR query returned 0 | Research leads and upstream review, not accepted source nodes |
| [scikit-learn User Guide](https://scikit-learn.org/1.8/user_guide.html) | Version 1.8; 11 method documents inspected and hashed; cite for method descriptions, no bulk documentation reuse | Suitable research evidence for algorithm proposals; implementation names are not automatically ontology identities |
| Primary author papers, tutorials and implementation descriptions | Candidate-specific locators in the proposal ledger; public text accessed, no model execution | Narrow method evidence; license for wholesale redistribution not inferred |
| BioPortal AIO and the AIO paper already retained by AIMech | Discovery/reference context; neither replaces the pinned source authority | No duplicate acquisition or import from a similarly named ontology |

AIO release SHA-256: `8f741d71408c93f15c62607106aa46f6edbc4e070c5546ed3ae111ada6e65cf6`. The JSON assessment preserves checksums for the other inspected upstream artifacts and query outputs. Versioned implementation-document hashes are in the candidate JSON. Original downloaded HTML and API responses were temporary working files; their availability in `/private/tmp` is not part of the repository contract.

## Candidate outcomes

See the [36-candidate proposal ledger](../../docs/proposals/aio/classical-ml-candidates.md) and [machine-readable companion](../../docs/proposals/aio/classical-ml-candidates.json). The 32 proposed terms include k-means, DBSCAN, HDBSCAN, AdaBoost, naive Bayes, hidden Markov models, elastic net and GloVe. Their AIO IDs remain unassigned.

- XGBoost and LightGBM are deferred pending a method-versus-software decision.
- Ordinary least squares is deferred because existing `LeastsquaresAnalysis` and `LinearRegression` overlap its scope.
- MLP is an exact synonym of `DeepFeedForwardNetwork`; its expanded synonym has a typo, and depth scope needs review before any new identity.
- EM, genetic algorithms, SGD, GloVe, Apriori and Eclat have unresolved parent abstractions. A convenient nearest class is not asserted as a correct parent.

The [complete open-request inventory](20261011T023827Z-aio-upstream-request-triage.json) retains every issue and rationale. Priorities for further research are few-shot/learning-paradigm boundaries (#150/#152), framework layer equivalence (#54/#35), and dated AI-risk/security or reproducibility vocabularies (#119/#31/#26). These leads may yield additional proposals; no claim is made that the 36-candidate roster exhausts them.

Issue 12 is a useful duplicate check: its 13 activation functions already have AIO records; [serialization](https://www.tensorflow.org/api_docs/python/tf/keras/activations/serialize) and [deserialization](https://www.tensorflow.org/api_docs/python/tf/keras/activations/deserialize) are API utilities, not additional activation functions. Issue 72 concerns synonyms of existing `RetrievalAugmentedLLM`. Issue 45 must account for existing `ConceptDriftBias` with exact synonym `Concept Drift`. These requests do not justify duplicate native records.

## Review and validation

The persisted [category review](../../reviews/structured/20261011T024345Z-aio-accepted-concept-coverage/review.md) ([YAML](../../reviews/structured/20261011T024345Z-aio-accepted-concept-coverage/review.yaml)) covers all 442 selected targets for identity, source provenance and exact import coverage. Verdict: `pass_with_limitations`; zero findings within that scope; semantic lump/split decisions deferred. Literature support of the full corpus was not reassessed, and every native record remains `NOT_REVIEWED`.

Actual required checks all exited 0: `aimech check-source`, `aimech validate` (442 valid), `aimech seed --check` (0 missing/changed/unexpected), and the structured-review checker. The new review was validated and saved through the canonical helper, and the post-save checker confirmed one valid review. `aimech validate-history --base 945bd67d190e867ac379f8d4ebbc6d4ddec152a9` passed with three history records and zero errors; proposal references, versioned evidence anchors and all local Markdown links were also checked. Duplicate searches included hidden and ignored text files in both AIMech checkouts, as well as normalized labels and scoped synonyms in all source class nodes.

## Concrete integration handoff

Review the candidate ledger with upstream AIO maintainers through existing issue 167. Resolve definitions, identity, synonyms, parent abstraction and scope in the maintained sheet/template. Only after accepted identifiers appear in a reviewed source revision should AIMech perform a complete source-diff assessment and reproducible import. Local proposals do not authorize identifier minting, generated-file edits, or automatic source refresh.

Broader source leads need their own dated inventories, identifier and reuse checks, primary evidence, and boundary decisions. The current stopping condition is exhaustion of accepted additions in the checked AIO surfaces, not exhaustion of possible AI research. No paid providers, model training or model evaluations were run.

The actual write session is recorded in [append-only history](../../history/reports/aio-concept-discovery/2026-10-11T024716Z-codex-9febb0.yaml). All eight new artifacts are local to the isolated `goal/discover-ai-concepts` worktree; they have not been committed or published.
