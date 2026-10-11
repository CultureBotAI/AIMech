# Scientific self-review of local search and racing

- Review: 20261011T120853Z-local-search-and-racing-initial
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T12:05:41Z
- Finished UTC: 2026-10-11T12:08:53Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Retain five distinct algorithm-configuration concepts. One minor ROAR wrapper/early-exit wording defect requires correction.

## Scope And Provenance

All fields of five newly maintained local-search/racing records.

Selection: Exact five IDs in the discovery ledger; no sampling.
Coverage: full; 5 reviewed / 5 in the declared population.
Source: working_tree at Git base 10ec02664b207cd857c320a50927226c483e6e93.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ParamILS | data/curated/ParamILS.yaml | maintained | ParamILS |
| AIMech:BasicILS | data/curated/BasicILS.yaml | maintained | BasicILS |
| AIMech:FocusedILS | data/curated/FocusedILS.yaml | maintained | FocusedILS |
| AIMech:RandomOnlineAggressiveRacing | data/curated/RandomOnlineAggressiveRacing.yaml | maintained | Random Online Aggressive Racing |
| AIMech:FRace | data/curated/FRace.yaml | maintained | F-Race |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:ParamILS, AIMech:BasicILS, AIMech:FocusedILS, AIMech:RandomOnlineAggressiveRacing, AIMech:FRace | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 87.19s (0:01:27)<br>Checked 442 record(s); 0 failed.<br>Checked 270 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 64 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 62,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:ParamILS, AIMech:BasicILS, AIMech:FocusedILS, AIMech:RandomOnlineAggressiveRacing, AIMech:FRace | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| Finite configuration/racing boundary calculations | passed | True | AIMech:ParamILS, AIMech:BasicILS, AIMech:FocusedILS, AIMech:RandomOnlineAggressiveRacing, AIMech:FRace | {"nonnegative_cost_lower_bound": {"partial_sum": 11, "N": 100, "lower_bound": 0.11, "comparison_bound": 0.1}, "printed_capping_max_vs_shortening": {"cutoff": 100, "remaining_allowance": 6.0, "printed_max": 100, "shortening_min": 6.0}, "non_strict_plateau_trace": ["a", "b", "a", "b", "a"], "blocked_comparison": {"longer_all_mean": 5.5, "longer_common_prefix_mean": 10, "shorter_mean": 6}, "ranks_vs_means": {"a_rank_sum": 4, "b_rank_sum": 5, "a_mean": 33.333333333333336, "b_mean": 1.3333333333333333}, "scope": "Finite arithmetic and control-flow counterexamples only; no statistical significance test, author code, model or benchmark was executed."} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, limitations and AIO no-match assessment

evidence: supported. Targets: AIMech:ParamILS.

This record denotes the algorithmic framework in the 2009 paper, not its Ruby software package or a configured SAT/MIP solver. BasicILS and FocusedILS are distinct concrete instantiations of its comparison procedure and are not aliases. The framework optimizes one configuration over a supplied instance distribution, rather than selecting a different solver per instance or adapting a target solver during its own run. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 265 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main checkout, returning 20 lines in the worktree and 25 in main. These were prior candidate leads, source references, neighboring-method mentions and five unrelated ROAR namespace entries in ignored dependencies, not existing records for these identities. Seven exact AIO CLASS nodes with synonyms and outgoing edges and six neighboring native mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Compare a supplied initial configuration with a fixed number of random configurations, then perform randomized first-acceptable one-exchange local search. Exclude moves that change only a currently inactive conditional parameter. Repeatedly perturb the current search configuration by a fixed number of random neighborhood moves, apply the local-search routine, and accept the resulting configuration when the chosen comparison procedure judges it at least as good. Independently restart the search configuration at random with a specified probability. Maintain an overall incumbent and return it at termination. The framework deliberately leaves comparison and objective estimation to an instantiation such as BasicILS or FocusedILS. Limits: The 2009 formulation has a finite configuration domain; numerical parameters require discretization. Objective, run cutoff and training-instance distribution affect the selected configuration. Independent held-out evaluation is needed to assess generalization; no universal solver speedup is asserted. The printed first-improvement loop accepts the supplied non-strict comparison. Equal-cost neighboring configurations can therefore cycle under a literal reading; this record does not assert unconditional termination of that loop or executable equivalence to a software release. Adaptive capping is a separable acceleration, not the defining identity of this search/comparison method. Section4 describes trajectory-preserving and more aggressive alternatives. Procedure4 prints a max operation inconsistent with shortening the run cutoff described in the prose, and uses inconsistent cutoff symbols; the printed routine is not treated as verified executable code.

### Identity, definition, mechanism, limitations and AIO no-match assessment

evidence: supported. Targets: AIMech:BasicILS.

BasicILS(N) specializes the ParamILS framework by fixing the comparison sample size N. N counts instance/seed evaluations, not necessarily distinct instances. It differs from FocusedILS, which grows evaluation prefixes adaptively, and from random search, which does not use ParamILS neighborhood perturbation and local search. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 265 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main checkout, returning 20 lines in the worktree and 25 in main. These were prior candidate leads, source references, neighboring-method mentions and five unrelated ROAR namespace entries in ignored dependencies, not existing records for these identities. Seven exact AIO CLASS nodes with synonyms and outgoing edges and six neighboring native mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Use ParamILS initialization, randomized one-exchange local search, perturbation, nonworsening acceptance and random restart. Implement each comparison by obtaining the chosen cost statistic for both configurations on the first N pairs in the shared instance/seed sequence, reusing cached compatible target-algorithm runs. The uncapped comparison returns true when the first configuration’s estimate is no greater than the second’s. Track the best encountered configuration under that empirical objective. The fixed comparison budget is independent of the overall time or iteration budget used to stop the configurator. Limits: The 2009 formulation has a finite configuration domain; numerical parameters require discretization. Objective, run cutoff and training-instance distribution affect the selected configuration. Independent held-out evaluation is needed to assess generalization; no universal solver speedup is asserted. The printed first-improvement loop accepts the supplied non-strict comparison. Equal-cost neighboring configurations can therefore cycle under a literal reading; this record does not assert unconditional termination of that loop or executable equivalence to a software release. Adaptive capping is a separable acceleration, not the defining identity of this search/comparison method. Section4 describes trajectory-preserving and more aggressive alternatives. Procedure4 prints a max operation inconsistent with shortening the run cutoff described in the prose, and uses inconsistent cutoff symbols; the printed routine is not treated as verified executable code. A small fixed N can give unreliable rankings and overfitting; a large N increases evaluation cost and reduces search progress at a fixed time budget. These are experimental-design tradeoffs, not a guarantee that one N is optimal.

### Identity, definition, mechanism, limitations and AIO no-match assessment

evidence: supported. Targets: AIMech:FocusedILS.

FocusedILS is the adaptive comparison instantiation of ParamILS. Its domination relation compares common instance/seed prefixes and requires the dominating configuration to have at least as many cached runs. It is not a fixed-sample BasicILS comparison, a Friedman significance test, or ROAR’s uniform proposal method with a different intensification routine. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 265 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main checkout, returning 20 lines in the worktree and 25 in main. These were prior candidate leads, source references, neighboring-method mentions and five unrelated ROAR namespace entries in ignored dependencies, not existing records for these identities. Seven exact AIO CLASS nodes with synonyms and outgoing edges and six neighboring native mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Within the ParamILS search framework, compare configurations using cached target-algorithm runs on a common ordered instance/seed sequence. A configuration dominates another when it has at least as many runs and its estimated cost over the other’s full prefix is no greater. Begin a comparison by extending the shorter prefix by one run, or both when their lengths are equal; continue extending until either configuration dominates. Procedure3 increments its global bonus counter once per comparison and again when the initial run counts tie. When the first configuration dominates, add the accumulated number of bonus evaluations to it and reset the counter; otherwise return the unsuccessful comparison without that reset. Keep an incumbent while the search continues. Limits: The 2009 formulation has a finite configuration domain; numerical parameters require discretization. Objective, run cutoff and training-instance distribution affect the selected configuration. Independent held-out evaluation is needed to assess generalization; no universal solver speedup is asserted. The printed first-improvement loop accepts the supplied non-strict comparison. Equal-cost neighboring configurations can therefore cycle under a literal reading; this record does not assert unconditional termination of that loop or executable equivalence to a software release. Adaptive capping is a separable acceleration, not the defining identity of this search/comparison method. Section4 describes trajectory-preserving and more aggressive alternatives. Procedure4 prints a max operation inconsistent with shortening the run cutoff described in the prose, and uses inconsistent cutoff symbols; the printed routine is not treated as verified executable code. The paper’s asymptotic statements require a finite space, positive-probability random restarts, consistent cost estimates and indefinitely continuing iterations/evaluations. They are not a finite-budget optimality certificate. Repeated sampling from a finite training set does not by itself establish consistency for a different population of instances.

### Identity, definition, mechanism, limitations and AIO no-match assessment

evidence: supported. Targets: AIMech:RandomOnlineAggressiveRacing.

The 2011 source expands ROAR as Random Online Adaptive Racing in its introduction and Random Online Aggressive Racing in Section3. Both wordings here refer to that source’s same method. It shares SMAC’s intensification procedure but omits SMAC’s random-forest surrogate and acquisition-guided proposals. It differs from fixed-evaluation random search and significance-based elimination in F-Race. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 265 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main checkout, returning 20 lines in the worktree and 25 in main. These were prior candidate leads, source references, neighboring-method mentions and five unrelated ROAR namespace entries in ignored dependencies, not existing records for these identities. Seven exact AIO CLASS nodes with synonyms and outgoing edges and six neighboring native mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Initialize by evaluating the default configuration or a random setting when a default is unavailable. Supply uniformly random configurations to the intensification routine; the nominal model is constant and unused for proposing them. Add an incumbent evaluation, subject to the maximum-run cap, on an instance with the fewest incumbent runs and a random seed. Evaluate a challenger on a subset of the incumbent’s instance/seed pairs and compare their empirical costs on exactly those pairs. Reject a worse challenger; otherwise enlarge its tested subset in doubling batches until it has covered the incumbent’s available runs, then replace the incumbent when the challenger remains at least as good. Continue proposing random challengers within the configuration budget. Limits: Aggressive racing in this source makes empirical decisions without waiting for a statistical significance threshold. An early rejection can discard a configuration with better expected performance; no family-wise error control or finite-budget optimum is claimed. The displayed intensification routine caps incumbent runs at maxR=2000 and uses an intensification-time budget after processing at least two challengers. The paper’s asymptotic discussion assumes consistent estimation and unbounded evaluation growth in a finite configuration space, which are not automatic properties of the capped practical routine. The original procedure lacks adaptive capping of individual poor runs. Uniform configuration proposals do not mean equal allocation of evaluations to every configuration. No implementation or benchmark outcome was reproduced.

### Identity, definition, mechanism, limitations and AIO no-match assessment

evidence: supported. Targets: AIMech:FRace.

This record covers the original 2002 F-Race method. It uses a fixed starting candidate pool and nested survivor sets, not iterative resampling of configurations as in later iterated racing methods. It differs from ROAR’s challenger-incumbent heuristic comparisons, fixed-fraction successive halving and a standalone Friedman test without sequential resource allocation. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 265 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main checkout, returning 20 lines in the worktree and 25 in main. These were prior candidate leads, source references, neighboring-method mentions and five unrelated ROAR namespace entries in ignored dependencies, not existing records for these identities. Seven exact AIO CLASS nodes with synonyms and outgoing edges and six neighboring native mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Start with a finite set of candidate configurations and draw a sequence of training instances independently from the selected instance distribution. At each racing step, evaluate every surviving candidate on the same new instance and append its observed solution cost. Rank surviving candidates by cost within each accumulated instance block, using average ranks for ties. Apply the paper’s Friedman aggregate rank statistic to the accumulated blocks. If its null is not rejected, retain all survivors; if rejected, compare each candidate with the best-ranked one using the stated post-hoc rank-difference test and discard candidates found worse. Repeat with the reduced candidate set until one remains or the prescribed total computation budget stops further evaluation. Limits: The method assumes independent instance blocks and appropriate within-block comparability. The aggregate test uses an approximate chi-square reference distribution, followed by the paper’s Student-t-based pairwise rule. No implementation-level small-sample correction or sequential family-wise error guarantee was verified. Rank comparisons discard cost magnitudes. Better rank sums need not identify the lowest arithmetic mean cost, so the method is not asserted to certify the minimizer of the expected-cost objective stated in Section2. Repeated significance decisions and early elimination do not ensure that the best configuration survives. A finite initial candidate pool limits what can be selected, and the time budget can expire with multiple survivors. The inspected method does not establish a unique returned configuration in every such case. No general superiority over parametric racing methods or replicated TSP result is claimed.

### Framework versus concrete comparison algorithms

consistency: supported. Targets: AIMech:ParamILS, AIMech:BasicILS, AIMech:FocusedILS.

Retain ParamILS as the shared framework and BasicILS/FocusedILS as distinct instantiations.

BasicILS fixes N paired evaluations; FocusedILS extends cached common prefixes until domination and uses a comparison-dependent bonus counter. The methods share neighborhood perturbation and restarts but are not synonyms. Numerical discretization, training-set generalization, non-strict plateau behavior and printed capping ambiguities remain explicit.

### Heuristic challenger racing versus fixed-pool statistical elimination

consistency: supported. Targets: AIMech:RandomOnlineAggressiveRacing, AIMech:FRace.

Retain ROAR and F-Race as separate methods.

ROAR samples new configurations uniformly and compares a challenger against an incumbent on shared randomized evaluations, without a significance threshold. F-Race retains a fixed initial pool, ranks candidates within instance blocks and performs aggregate/post-hoc significance tests. Rank sums are not raw expected-cost certificates. ROAR’s single-proposal wrapper must be distinguished from the shared intensification routine’s i&gt;=2 early-exit condition.

### General configuration versus AIO learning/training concepts

grounding: supported. Targets: AIMech:ParamILS, AIMech:BasicILS, AIMech:FocusedILS, AIMech:RandomOnlineAggressiveRacing, AIMech:FRace.

Retain explicit no-match assessments for all five records.

All five records carry explicit aio_no_match assessments. The inspected AIO TrainingStrategy definition concerns model preprocessing/training, whereas these methods configure general target algorithms. MachineLearningTask and MetaLearning do not automatically cover arbitrary solver configuration; ActiveLearning concerns label queries, RandomForest a tree ensemble, ReinforcementLearning a learning task, and EvaluationBias a bias. Incidental applications or common optimization vocabulary do not establish a mapping. SMAC’s separate RandomForest component mapping is therefore not inherited by ROAR or ParamILS.

## Findings

### roar-single-proposal: ROAR limitation conflates the shared routine’s early-exit condition with its single-proposal wrapper.

minor / open / confirmed; issue key: CultureBotAI-AIMech-ROAR-single-proposal-intensification.

The draft says the intensification budget applies after at least two challengers. Procedure2 has an i&gt;=2 early-exit guard, but Section3.2 explicitly gives ROAR one proposal per call. The loop therefore ends after that one proposal; the guard does not require two challengers. Clarify this distinction without changing the main identity or attributing SMAC’s interleaving to ROAR.

## Recommended Actions And Acceptance Checks

### clarify-roar-wrapper

Clarify single-proposal ROAR versus the shared routine guard, update ledger/history and save a successor disposition.

- State that ROAR supplies one challenger per call and that i&gt;=2 is a conditional early exit, not a mandatory minimum.
- Pass required record/repository checks and retain the initial review.
- Save a successor disposition linked to this exact finding and issue72.

## Category Boundaries

- retain: AIMech:ParamILS, AIMech:BasicILS, AIMech:FocusedILS, AIMech:RandomOnlineAggressiveRacing, AIMech:FRace. The shared ParamILS framework and its fixed/adaptive comparison instantiations are explicitly distinct concepts. ROAR’s random-proposal heuristic racing and F-Race’s fixed-pool rank-test elimination have different proposal, comparison and stopping mechanisms.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T120527Z-local-search-and-racing.json | supports | All 442 pinned AIO labels/scoped synonyms and 265 preceding maintained IDs/names/aliases were compared, including candidate-internal normalized uniqueness. No identity match was found. Full-checkout fixed-string searches included ignored and hidden files: 20 worktree lines and 25 main-checkout lines. Matches were prior leads, SMAC source/neighbor context and five unrelated ROAR namespace entries in ignored dependencies. Seven exact AIO CLASS nodes with synonyms/outgoing edges and six native neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood. |
| mapping | sources/aio/aio.json; Seven exact CLASS nodes and their scoped synonyms/outgoing edges in source_analysis.aio_mapping_inspection | supports | All five records carry explicit aio_no_match assessments. The inspected AIO TrainingStrategy definition concerns model preprocessing/training, whereas these methods configure general target algorithms. MachineLearningTask and MetaLearning do not automatically cover arbitrary solver configuration; ActiveLearning concerns label queries, RandomForest a tree ensemble, ReinforcementLearning a learning task, and EvaluationBias a bias. Incidental applications or common optimization vocabulary do not establish a mapping. SMAC’s separate RandomForest component mapping is therefore not inherited by ROAR or ParamILS. |
| neighbors | research/discovery/20261011T120527Z-local-search-and-racing.json; source_analysis.aio_mapping_inspection.native_neighbors | supports | Inspected SMAC, random hyperparameter search, Hyperband, successive halving, ASHA and genetic-algorithm mechanisms. Framework specialization, proposal choice, evaluation allocation and statistical elimination establish different boundaries. |
| finite-conventions | research/discovery/configuration-racing-boundaries.py; calculate(): capping, plateau, common-prefix and rank/mean examples | supports | Original finite examples examine nonnegative-cost capping bounds, the printed max cutoff, non-strict plateau cycling, blocked comparisons and rank-versus-mean objectives. They do not reproduce any author algorithm or significance test. |
| paramils-source-0 | https://www.cs.ubc.ca/labs/algorithms/Projects/MIP-Config/papers/09-JAIR-ParamILS.pdf; Sections2–3.1, PDF pp.3–8 (printed269–274), especially Algorithm Framework1; Sections4 and5.1, PDF pp.11–15; Section10, PDF pp.34–36 | supports | ParamILS: An Automatic Algorithm Configuration Framework. JAIR 36:267–306, 2009; author-hosted 40-page article. Actual text and visual scopes are declared in the ledger; no author implementation was executed. |
| basicils-source-0 | https://www.cs.ubc.ca/labs/algorithms/Projects/MIP-Config/papers/09-JAIR-ParamILS.pdf; Sections3.1–3.2 and Algorithm Framework1/Procedure2, PDF pp.7–9 (printed273–275); Section5.1, PDF pp.14–15; capping qualifications in Section4, PDF pp.11–14; Section10, PDF pp.34–36 | supports | ParamILS: An Automatic Algorithm Configuration Framework. JAIR 36:267–306, 2009; author-hosted 40-page article. Actual text and visual scopes are declared in the ledger; no author implementation was executed. |
| focusedils-source-0 | https://www.cs.ubc.ca/labs/algorithms/Projects/MIP-Config/papers/09-JAIR-ParamILS.pdf; Sections3.1 and3.3, PDF pp.7–11 (printed273–277), especially Definition5 and Procedure3; Section4.2, PDF pp.13–14; Section5.1, PDF pp.14–15; Section10, PDF pp.34–36 | supports | ParamILS: An Automatic Algorithm Configuration Framework. JAIR 36:267–306, 2009; author-hosted 40-page article. Actual text and visual scopes are declared in the ledger; no author implementation was executed. |
| randomonlineaggressiveracing-source-0 | https://www.cs.ubc.ca/labs/algorithms/Projects/SMAC/papers/11-LION5-SMAC.pdf; Section3 and Framework1/Procedure2, PDF pp.4–6; acronym wording in Section1, PDFp.2; comparison and limitations in Sections4.3 and6, PDF pp.9 and14 | supports | Sequential Model-Based Optimization for General Algorithm Configuration. LION 5, 2011; author-hosted 15-page manuscript. Actual text and visual scopes are declared in the ledger; no author implementation was executed. |
| frace-source-0 | https://iridia.ulb.ac.be/~stuetzle/publications/GECCO02.pdf; Sections2–3.3, PDF pp.2–5, especially Section3.1 racing and Section3.2 Friedman/post-hoc comparisons; Section6, PDFp.8 | supports | A Racing Algorithm for Configuring Metaheuristics. GECCO 2002, pp.11–18; author-hosted eight-page paper. Actual text and visual scopes are declared in the ledger; no author implementation was executed. |

## Limits And Additional Notes

- Adversarial author self-review only; all five records remain DRAFT.
- Only declared PDF pages were inspected. No training, benchmark, complete proof audit, significance-test implementation or author-code execution was performed.
- Published capping and tie-handling ambiguities remain qualified; no author-issued erratum or executable equivalence is claimed.
- Five additions and a nonempty inherited/new frontier leave discovery active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T120853Z-local-search-and-racing-initial
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of local search and racing
started_at: '2026-10-11T12:05:41Z'
finished_at: '2026-10-11T12:08:53Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed all five records
    against declared primary methods, rendered pages, seven exact AIO nodes, six native
    neighbors and original finite examples. This is not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Retain five distinct algorithm-configuration concepts. One minor ROAR wrapper/early-exit
  wording defect requires correction.
source:
  git_revision: 10ec02664b207cd857c320a50927226c483e6e93
  state: working_tree
  inputs:
  - path: data/aio/ActiveLearning.yaml
    sha256: a4d5b2c82df6f586fedc7290261bc978e7c8d17f1d844c5ee9efc8243e46bbaf
    role: context
  - path: data/aio/EvaluationBias.yaml
    sha256: 6523f8c43f7b140c6dd593069e30b7fc1bdd60b89d01bdf5441d2bc83a12e749
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MetaLearning.yaml
    sha256: 4a1835675f779c8f924cfe085f1b5def3b5c6a2c111596385c61063056f3b8a6
    role: context
  - path: data/aio/RandomForest.yaml
    sha256: cfdce4625131a8da239adf1b3957fadbc5433ddc8fc4ac8a3be5fe9018ce66ab
    role: context
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/curated/AsynchronousSuccessiveHalving.yaml
    sha256: 16e68a69439a4ad7d06ad34483d4db288163810967516776edac5a6082d8a725
    role: context
  - path: data/curated/BasicILS.yaml
    sha256: e0bb96e7fa5c20e3bd4d41480db07b51eed44627787828d48f87e60a5d7f255b
    role: target
  - path: data/curated/FRace.yaml
    sha256: 2bfaad9c6d4b7c24452e7ccb63fe47e2c8515f3b1856566f8ae22dc14e16d0e7
    role: target
  - path: data/curated/FocusedILS.yaml
    sha256: 644fe2c07abcf0df3fb5b269044d45aef196556b9d14febc7d7e3cc01eca27f9
    role: target
  - path: data/curated/GeneticAlgorithm.yaml
    sha256: d40bf1a03e29a3ca6bf88f6553f18c6b1559baf56da6a21d63b54163f4752ceb
    role: context
  - path: data/curated/Hyperband.yaml
    sha256: ed8dae09ccd45becb03f2e0ad41aa4c2898ecafc999e6b2ba9637c7d8b311e56
    role: context
  - path: data/curated/ParamILS.yaml
    sha256: 8cb2244b7c067b3379e607b3df01a571623c1700c89ff951469d762a72539fa3
    role: target
  - path: data/curated/RandomOnlineAggressiveRacing.yaml
    sha256: b2fc81401622bfcedfecc0b325542573f2f5c56c8bbd9282b9d013af76bdc6dd
    role: target
  - path: data/curated/RandomSearchHyperparameterOptimization.yaml
    sha256: 24dde2b9d19169c383b403742ea355727c2f167ae8aa21970fbda34e832c89fd
    role: context
  - path: data/curated/SequentialModelBasedAlgorithmConfiguration.yaml
    sha256: 578ea6762a48bc56063d3e5907bb038b728112560a3baee7811d4f9b50354357
    role: context
  - path: data/curated/SuccessiveHalving.yaml
    sha256: 2d7bc826d5618a7cc0d751ed80a1a67bc61eb123cbb4abc845b7f87ba520331c
    role: context
  - path: research/discovery/20261011T120527Z-local-search-and-racing.json
    sha256: 6a08c1b911e4e16ea372ec5d891975b8573f0078c31cba94de957fb9aefff4c8
    role: context
  - path: research/discovery/configuration-racing-boundaries.py
    sha256: 17d4f37e5e8a0cb0808e97c262452f340b040f456e9ba4c9375c5280b82785c8
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
- target_id: AIMech:ParamILS
  path: data/curated/ParamILS.yaml
  label: ParamILS
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ParamILS.yaml
    role: maintained
- target_id: AIMech:BasicILS
  path: data/curated/BasicILS.yaml
  label: BasicILS
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/BasicILS.yaml
    role: maintained
- target_id: AIMech:FocusedILS
  path: data/curated/FocusedILS.yaml
  label: FocusedILS
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FocusedILS.yaml
    role: maintained
- target_id: AIMech:RandomOnlineAggressiveRacing
  path: data/curated/RandomOnlineAggressiveRacing.yaml
  label: Random Online Aggressive Racing
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RandomOnlineAggressiveRacing.yaml
    role: maintained
- target_id: AIMech:FRace
  path: data/curated/FRace.yaml
  label: F-Race
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FRace.yaml
    role: maintained
scope:
  description: All fields of five newly maintained local-search/racing records.
  selection: Exact five IDs in the discovery ledger; no sampling.
  coverage: full
  population_size: 5
  reviewed_target_ids:
  - AIMech:ParamILS
  - AIMech:BasicILS
  - AIMech:FocusedILS
  - AIMech:RandomOnlineAggressiveRacing
  - AIMech:FRace
  exclusions:
  - target: Older records and unselected candidates
    reason: Neighbors were inspected for identity boundaries, not a fresh review of
      the whole corpus.
  - target: Unread pages, proofs, outcomes and implementations
    reason: Only declared primary-source pages were inspected. No author code or model
      was executed.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:ParamILS
  - AIMech:BasicILS
  - AIMech:FocusedILS
  - AIMech:RandomOnlineAggressiveRacing
  - AIMech:FRace
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 87.19s (0:01:27)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 270 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 64 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 62,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:ParamILS
  - AIMech:BasicILS
  - AIMech:FocusedILS
  - AIMech:RandomOnlineAggressiveRacing
  - AIMech:FRace
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
- check_id: finite-arithmetic
  name: Finite configuration/racing boundary calculations
  command: python3 research/discovery/configuration-racing-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:ParamILS
  - AIMech:BasicILS
  - AIMech:FocusedILS
  - AIMech:RandomOnlineAggressiveRacing
  - AIMech:FRace
  exit_code: 0
  expected_exit_code: 0
  summary: '{"nonnegative_cost_lower_bound": {"partial_sum": 11, "N": 100, "lower_bound":
    0.11, "comparison_bound": 0.1}, "printed_capping_max_vs_shortening": {"cutoff":
    100, "remaining_allowance": 6.0, "printed_max": 100, "shortening_min": 6.0}, "non_strict_plateau_trace":
    ["a", "b", "a", "b", "a"], "blocked_comparison": {"longer_all_mean": 5.5, "longer_common_prefix_mean":
    10, "shorter_mean": 6}, "ranks_vs_means": {"a_rank_sum": 4, "b_rank_sum": 5, "a_mean":
    33.333333333333336, "b_mean": 1.3333333333333333}, "scope": "Finite arithmetic
    and control-flow counterexamples only; no statistical significance test, author
    code, model or benchmark was executed."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T120527Z-local-search-and-racing.json
  accessed_at: '2026-10-11T12:05:41Z'
  support: supports
  summary: 'All 442 pinned AIO labels/scoped synonyms and 265 preceding maintained
    IDs/names/aliases were compared, including candidate-internal normalized uniqueness.
    No identity match was found. Full-checkout fixed-string searches included ignored
    and hidden files: 20 worktree lines and 25 main-checkout lines. Matches were prior
    leads, SMAC source/neighbor context and five unrelated ROAR namespace entries
    in ignored dependencies. Seven exact AIO CLASS nodes with synonyms/outgoing edges
    and six native neighboring mechanisms were inspected. Absence is bounded to this
    snapshot and semantic neighborhood.'
  search_scope: All 442 pinned AIO labels/scoped synonyms and 265 preceding maintained
    IDs/names/aliases; full checkouts including ignored/hidden files; candidate-internal
    normalized uniqueness.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Seven exact CLASS nodes and their scoped synonyms/outgoing edges in source_analysis.aio_mapping_inspection
  accessed_at: '2026-10-11T12:05:41Z'
  support: supports
  summary: All five records carry explicit aio_no_match assessments. The inspected
    AIO TrainingStrategy definition concerns model preprocessing/training, whereas
    these methods configure general target algorithms. MachineLearningTask and MetaLearning
    do not automatically cover arbitrary solver configuration; ActiveLearning concerns
    label queries, RandomForest a tree ensemble, ReinforcementLearning a learning
    task, and EvaluationBias a bias. Incidental applications or common optimization
    vocabulary do not establish a mapping. SMAC’s separate RandomForest component
    mapping is therefore not inherited by ROAR or ParamILS.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T120527Z-local-search-and-racing.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors
  accessed_at: '2026-10-11T12:05:41Z'
  support: supports
  summary: Inspected SMAC, random hyperparameter search, Hyperband, successive halving,
    ASHA and genetic-algorithm mechanisms. Framework specialization, proposal choice,
    evaluation allocation and statistical elimination establish different boundaries.
- evidence_id: finite-conventions
  kind: record_content
  reference: research/discovery/configuration-racing-boundaries.py
  locator: 'calculate(): capping, plateau, common-prefix and rank/mean examples'
  accessed_at: '2026-10-11T12:05:41Z'
  snapshot_sha256: 17d4f37e5e8a0cb0808e97c262452f340b040f456e9ba4c9375c5280b82785c8
  support: supports
  summary: Original finite examples examine nonnegative-cost capping bounds, the printed
    max cutoff, non-strict plateau cycling, blocked comparisons and rank-versus-mean
    objectives. They do not reproduce any author algorithm or significance test.
- evidence_id: paramils-source-0
  kind: primary_source
  reference: https://www.cs.ubc.ca/labs/algorithms/Projects/MIP-Config/papers/09-JAIR-ParamILS.pdf
  locator: Sections2–3.1, PDF pp.3–8 (printed269–274), especially Algorithm Framework1;
    Sections4 and5.1, PDF pp.11–15; Section10, PDF pp.34–36
  accessed_at: '2026-10-11T11:56:17Z'
  snapshot_sha256: 3a1223d28e13b289771ff59c3bf7967c883137346b23d1d69887359f797e4bd4
  support: supports
  summary: 'ParamILS: An Automatic Algorithm Configuration Framework. JAIR 36:267–306,
    2009; author-hosted 40-page article. Actual text and visual scopes are declared
    in the ledger; no author implementation was executed.'
- evidence_id: basicils-source-0
  kind: primary_source
  reference: https://www.cs.ubc.ca/labs/algorithms/Projects/MIP-Config/papers/09-JAIR-ParamILS.pdf
  locator: Sections3.1–3.2 and Algorithm Framework1/Procedure2, PDF pp.7–9 (printed273–275);
    Section5.1, PDF pp.14–15; capping qualifications in Section4, PDF pp.11–14; Section10,
    PDF pp.34–36
  accessed_at: '2026-10-11T11:56:17Z'
  snapshot_sha256: 3a1223d28e13b289771ff59c3bf7967c883137346b23d1d69887359f797e4bd4
  support: supports
  summary: 'ParamILS: An Automatic Algorithm Configuration Framework. JAIR 36:267–306,
    2009; author-hosted 40-page article. Actual text and visual scopes are declared
    in the ledger; no author implementation was executed.'
- evidence_id: focusedils-source-0
  kind: primary_source
  reference: https://www.cs.ubc.ca/labs/algorithms/Projects/MIP-Config/papers/09-JAIR-ParamILS.pdf
  locator: Sections3.1 and3.3, PDF pp.7–11 (printed273–277), especially Definition5
    and Procedure3; Section4.2, PDF pp.13–14; Section5.1, PDF pp.14–15; Section10,
    PDF pp.34–36
  accessed_at: '2026-10-11T11:56:17Z'
  snapshot_sha256: 3a1223d28e13b289771ff59c3bf7967c883137346b23d1d69887359f797e4bd4
  support: supports
  summary: 'ParamILS: An Automatic Algorithm Configuration Framework. JAIR 36:267–306,
    2009; author-hosted 40-page article. Actual text and visual scopes are declared
    in the ledger; no author implementation was executed.'
- evidence_id: randomonlineaggressiveracing-source-0
  kind: primary_source
  reference: https://www.cs.ubc.ca/labs/algorithms/Projects/SMAC/papers/11-LION5-SMAC.pdf
  locator: Section3 and Framework1/Procedure2, PDF pp.4–6; acronym wording in Section1,
    PDFp.2; comparison and limitations in Sections4.3 and6, PDF pp.9 and14
  accessed_at: '2026-10-11T11:45:03Z'
  snapshot_sha256: aecf80aba31329965bbfcb75c6d8ad2f19da51b2124a920b9f4af3574a9fcdcb
  support: supports
  summary: Sequential Model-Based Optimization for General Algorithm Configuration.
    LION 5, 2011; author-hosted 15-page manuscript. Actual text and visual scopes
    are declared in the ledger; no author implementation was executed.
- evidence_id: frace-source-0
  kind: primary_source
  reference: https://iridia.ulb.ac.be/~stuetzle/publications/GECCO02.pdf
  locator: Sections2–3.3, PDF pp.2–5, especially Section3.1 racing and Section3.2
    Friedman/post-hoc comparisons; Section6, PDFp.8
  accessed_at: '2026-10-11T11:57:05Z'
  snapshot_sha256: 4e67ab87a580dce69be5a2f484712f8173dfac1096e2343c3e89bfce16c162ad
  support: supports
  summary: A Racing Algorithm for Configuring Metaheuristics. GECCO 2002, pp.11–18;
    author-hosted eight-page paper. Actual text and visual scopes are declared in
    the ledger; no author implementation was executed.
assessments:
- assessment_id: paramils
  area: evidence
  topic: Identity, definition, mechanism, limitations and AIO no-match assessment
  outcome: supported
  target_ids:
  - AIMech:ParamILS
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - paramils-source-0
  summary: This record denotes the algorithmic framework in the 2009 paper, not its
    Ruby software package or a configured SAT/MIP solver. BasicILS and FocusedILS
    are distinct concrete instantiations of its comparison procedure and are not aliases.
    The framework optimizes one configuration over a supplied instance distribution,
    rather than selecting a different solver per instance or adapting a target solver
    during its own run. No normalized identity match was found across all 442 pinned
    AIO labels/scoped synonyms and 265 preceding native IDs/names/aliases. Full-checkout
    fixed-string searches included ignored and hidden files in both worktree and main
    checkout, returning 20 lines in the worktree and 25 in main. These were prior
    candidate leads, source references, neighboring-method mentions and five unrelated
    ROAR namespace entries in ignored dependencies, not existing records for these
    identities. Seven exact AIO CLASS nodes with synonyms and outgoing edges and six
    neighboring native mechanisms were inspected. Absence is bounded to this snapshot
    and semantic neighborhood.
  details: 'Compare a supplied initial configuration with a fixed number of random
    configurations, then perform randomized first-acceptable one-exchange local search.
    Exclude moves that change only a currently inactive conditional parameter. Repeatedly
    perturb the current search configuration by a fixed number of random neighborhood
    moves, apply the local-search routine, and accept the resulting configuration
    when the chosen comparison procedure judges it at least as good. Independently
    restart the search configuration at random with a specified probability. Maintain
    an overall incumbent and return it at termination. The framework deliberately
    leaves comparison and objective estimation to an instantiation such as BasicILS
    or FocusedILS. Limits: The 2009 formulation has a finite configuration domain;
    numerical parameters require discretization. Objective, run cutoff and training-instance
    distribution affect the selected configuration. Independent held-out evaluation
    is needed to assess generalization; no universal solver speedup is asserted. The
    printed first-improvement loop accepts the supplied non-strict comparison. Equal-cost
    neighboring configurations can therefore cycle under a literal reading; this record
    does not assert unconditional termination of that loop or executable equivalence
    to a software release. Adaptive capping is a separable acceleration, not the defining
    identity of this search/comparison method. Section4 describes trajectory-preserving
    and more aggressive alternatives. Procedure4 prints a max operation inconsistent
    with shortening the run cutoff described in the prose, and uses inconsistent cutoff
    symbols; the printed routine is not treated as verified executable code.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: An algorithmic framework or defined algorithm-configuration procedure;
      not a software package, target solver or trained model.
    evidence_ids:
    - paramils-source-0
  - name: aio-assessment
    value: aio_no_match
    definition: No inspected AIO target captures this general algorithm-configuration
      procedure or a defining component. The local algorithm remains supported by
      its primary source; this is a bounded mapping assessment, not absence from all
      ontologies.
    evidence_ids:
    - mapping
- assessment_id: basicils
  area: evidence
  topic: Identity, definition, mechanism, limitations and AIO no-match assessment
  outcome: supported
  target_ids:
  - AIMech:BasicILS
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - basicils-source-0
  summary: BasicILS(N) specializes the ParamILS framework by fixing the comparison
    sample size N. N counts instance/seed evaluations, not necessarily distinct instances.
    It differs from FocusedILS, which grows evaluation prefixes adaptively, and from
    random search, which does not use ParamILS neighborhood perturbation and local
    search. No normalized identity match was found across all 442 pinned AIO labels/scoped
    synonyms and 265 preceding native IDs/names/aliases. Full-checkout fixed-string
    searches included ignored and hidden files in both worktree and main checkout,
    returning 20 lines in the worktree and 25 in main. These were prior candidate
    leads, source references, neighboring-method mentions and five unrelated ROAR
    namespace entries in ignored dependencies, not existing records for these identities.
    Seven exact AIO CLASS nodes with synonyms and outgoing edges and six neighboring
    native mechanisms were inspected. Absence is bounded to this snapshot and semantic
    neighborhood.
  details: 'Use ParamILS initialization, randomized one-exchange local search, perturbation,
    nonworsening acceptance and random restart. Implement each comparison by obtaining
    the chosen cost statistic for both configurations on the first N pairs in the
    shared instance/seed sequence, reusing cached compatible target-algorithm runs.
    The uncapped comparison returns true when the first configuration’s estimate is
    no greater than the second’s. Track the best encountered configuration under that
    empirical objective. The fixed comparison budget is independent of the overall
    time or iteration budget used to stop the configurator. Limits: The 2009 formulation
    has a finite configuration domain; numerical parameters require discretization.
    Objective, run cutoff and training-instance distribution affect the selected configuration.
    Independent held-out evaluation is needed to assess generalization; no universal
    solver speedup is asserted. The printed first-improvement loop accepts the supplied
    non-strict comparison. Equal-cost neighboring configurations can therefore cycle
    under a literal reading; this record does not assert unconditional termination
    of that loop or executable equivalence to a software release. Adaptive capping
    is a separable acceleration, not the defining identity of this search/comparison
    method. Section4 describes trajectory-preserving and more aggressive alternatives.
    Procedure4 prints a max operation inconsistent with shortening the run cutoff
    described in the prose, and uses inconsistent cutoff symbols; the printed routine
    is not treated as verified executable code. A small fixed N can give unreliable
    rankings and overfitting; a large N increases evaluation cost and reduces search
    progress at a fixed time budget. These are experimental-design tradeoffs, not
    a guarantee that one N is optimal.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: An algorithmic framework or defined algorithm-configuration procedure;
      not a software package, target solver or trained model.
    evidence_ids:
    - basicils-source-0
  - name: aio-assessment
    value: aio_no_match
    definition: No inspected AIO target captures this general algorithm-configuration
      procedure or a defining component. The local algorithm remains supported by
      its primary source; this is a bounded mapping assessment, not absence from all
      ontologies.
    evidence_ids:
    - mapping
- assessment_id: focusedils
  area: evidence
  topic: Identity, definition, mechanism, limitations and AIO no-match assessment
  outcome: supported
  target_ids:
  - AIMech:FocusedILS
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - focusedils-source-0
  summary: FocusedILS is the adaptive comparison instantiation of ParamILS. Its domination
    relation compares common instance/seed prefixes and requires the dominating configuration
    to have at least as many cached runs. It is not a fixed-sample BasicILS comparison,
    a Friedman significance test, or ROAR’s uniform proposal method with a different
    intensification routine. No normalized identity match was found across all 442
    pinned AIO labels/scoped synonyms and 265 preceding native IDs/names/aliases.
    Full-checkout fixed-string searches included ignored and hidden files in both
    worktree and main checkout, returning 20 lines in the worktree and 25 in main.
    These were prior candidate leads, source references, neighboring-method mentions
    and five unrelated ROAR namespace entries in ignored dependencies, not existing
    records for these identities. Seven exact AIO CLASS nodes with synonyms and outgoing
    edges and six neighboring native mechanisms were inspected. Absence is bounded
    to this snapshot and semantic neighborhood.
  details: 'Within the ParamILS search framework, compare configurations using cached
    target-algorithm runs on a common ordered instance/seed sequence. A configuration
    dominates another when it has at least as many runs and its estimated cost over
    the other’s full prefix is no greater. Begin a comparison by extending the shorter
    prefix by one run, or both when their lengths are equal; continue extending until
    either configuration dominates. Procedure3 increments its global bonus counter
    once per comparison and again when the initial run counts tie. When the first
    configuration dominates, add the accumulated number of bonus evaluations to it
    and reset the counter; otherwise return the unsuccessful comparison without that
    reset. Keep an incumbent while the search continues. Limits: The 2009 formulation
    has a finite configuration domain; numerical parameters require discretization.
    Objective, run cutoff and training-instance distribution affect the selected configuration.
    Independent held-out evaluation is needed to assess generalization; no universal
    solver speedup is asserted. The printed first-improvement loop accepts the supplied
    non-strict comparison. Equal-cost neighboring configurations can therefore cycle
    under a literal reading; this record does not assert unconditional termination
    of that loop or executable equivalence to a software release. Adaptive capping
    is a separable acceleration, not the defining identity of this search/comparison
    method. Section4 describes trajectory-preserving and more aggressive alternatives.
    Procedure4 prints a max operation inconsistent with shortening the run cutoff
    described in the prose, and uses inconsistent cutoff symbols; the printed routine
    is not treated as verified executable code. The paper’s asymptotic statements
    require a finite space, positive-probability random restarts, consistent cost
    estimates and indefinitely continuing iterations/evaluations. They are not a finite-budget
    optimality certificate. Repeated sampling from a finite training set does not
    by itself establish consistency for a different population of instances.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: An algorithmic framework or defined algorithm-configuration procedure;
      not a software package, target solver or trained model.
    evidence_ids:
    - focusedils-source-0
  - name: aio-assessment
    value: aio_no_match
    definition: No inspected AIO target captures this general algorithm-configuration
      procedure or a defining component. The local algorithm remains supported by
      its primary source; this is a bounded mapping assessment, not absence from all
      ontologies.
    evidence_ids:
    - mapping
- assessment_id: randomonlineaggressiveracing
  area: evidence
  topic: Identity, definition, mechanism, limitations and AIO no-match assessment
  outcome: supported
  target_ids:
  - AIMech:RandomOnlineAggressiveRacing
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - randomonlineaggressiveracing-source-0
  summary: The 2011 source expands ROAR as Random Online Adaptive Racing in its introduction
    and Random Online Aggressive Racing in Section3. Both wordings here refer to that
    source’s same method. It shares SMAC’s intensification procedure but omits SMAC’s
    random-forest surrogate and acquisition-guided proposals. It differs from fixed-evaluation
    random search and significance-based elimination in F-Race. No normalized identity
    match was found across all 442 pinned AIO labels/scoped synonyms and 265 preceding
    native IDs/names/aliases. Full-checkout fixed-string searches included ignored
    and hidden files in both worktree and main checkout, returning 20 lines in the
    worktree and 25 in main. These were prior candidate leads, source references,
    neighboring-method mentions and five unrelated ROAR namespace entries in ignored
    dependencies, not existing records for these identities. Seven exact AIO CLASS
    nodes with synonyms and outgoing edges and six neighboring native mechanisms were
    inspected. Absence is bounded to this snapshot and semantic neighborhood.
  details: 'Initialize by evaluating the default configuration or a random setting
    when a default is unavailable. Supply uniformly random configurations to the intensification
    routine; the nominal model is constant and unused for proposing them. Add an incumbent
    evaluation, subject to the maximum-run cap, on an instance with the fewest incumbent
    runs and a random seed. Evaluate a challenger on a subset of the incumbent’s instance/seed
    pairs and compare their empirical costs on exactly those pairs. Reject a worse
    challenger; otherwise enlarge its tested subset in doubling batches until it has
    covered the incumbent’s available runs, then replace the incumbent when the challenger
    remains at least as good. Continue proposing random challengers within the configuration
    budget. Limits: Aggressive racing in this source makes empirical decisions without
    waiting for a statistical significance threshold. An early rejection can discard
    a configuration with better expected performance; no family-wise error control
    or finite-budget optimum is claimed. The displayed intensification routine caps
    incumbent runs at maxR=2000 and uses an intensification-time budget after processing
    at least two challengers. The paper’s asymptotic discussion assumes consistent
    estimation and unbounded evaluation growth in a finite configuration space, which
    are not automatic properties of the capped practical routine. The original procedure
    lacks adaptive capping of individual poor runs. Uniform configuration proposals
    do not mean equal allocation of evaluations to every configuration. No implementation
    or benchmark outcome was reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: An algorithmic framework or defined algorithm-configuration procedure;
      not a software package, target solver or trained model.
    evidence_ids:
    - randomonlineaggressiveracing-source-0
  - name: aio-assessment
    value: aio_no_match
    definition: No inspected AIO target captures this general algorithm-configuration
      procedure or a defining component. The local algorithm remains supported by
      its primary source; this is a bounded mapping assessment, not absence from all
      ontologies.
    evidence_ids:
    - mapping
- assessment_id: frace
  area: evidence
  topic: Identity, definition, mechanism, limitations and AIO no-match assessment
  outcome: supported
  target_ids:
  - AIMech:FRace
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - frace-source-0
  summary: This record covers the original 2002 F-Race method. It uses a fixed starting
    candidate pool and nested survivor sets, not iterative resampling of configurations
    as in later iterated racing methods. It differs from ROAR’s challenger-incumbent
    heuristic comparisons, fixed-fraction successive halving and a standalone Friedman
    test without sequential resource allocation. No normalized identity match was
    found across all 442 pinned AIO labels/scoped synonyms and 265 preceding native
    IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden
    files in both worktree and main checkout, returning 20 lines in the worktree and
    25 in main. These were prior candidate leads, source references, neighboring-method
    mentions and five unrelated ROAR namespace entries in ignored dependencies, not
    existing records for these identities. Seven exact AIO CLASS nodes with synonyms
    and outgoing edges and six neighboring native mechanisms were inspected. Absence
    is bounded to this snapshot and semantic neighborhood.
  details: 'Start with a finite set of candidate configurations and draw a sequence
    of training instances independently from the selected instance distribution. At
    each racing step, evaluate every surviving candidate on the same new instance
    and append its observed solution cost. Rank surviving candidates by cost within
    each accumulated instance block, using average ranks for ties. Apply the paper’s
    Friedman aggregate rank statistic to the accumulated blocks. If its null is not
    rejected, retain all survivors; if rejected, compare each candidate with the best-ranked
    one using the stated post-hoc rank-difference test and discard candidates found
    worse. Repeat with the reduced candidate set until one remains or the prescribed
    total computation budget stops further evaluation. Limits: The method assumes
    independent instance blocks and appropriate within-block comparability. The aggregate
    test uses an approximate chi-square reference distribution, followed by the paper’s
    Student-t-based pairwise rule. No implementation-level small-sample correction
    or sequential family-wise error guarantee was verified. Rank comparisons discard
    cost magnitudes. Better rank sums need not identify the lowest arithmetic mean
    cost, so the method is not asserted to certify the minimizer of the expected-cost
    objective stated in Section2. Repeated significance decisions and early elimination
    do not ensure that the best configuration survives. A finite initial candidate
    pool limits what can be selected, and the time budget can expire with multiple
    survivors. The inspected method does not establish a unique returned configuration
    in every such case. No general superiority over parametric racing methods or replicated
    TSP result is claimed.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: An algorithmic framework or defined algorithm-configuration procedure;
      not a software package, target solver or trained model.
    evidence_ids:
    - frace-source-0
  - name: aio-assessment
    value: aio_no_match
    definition: No inspected AIO target captures this general algorithm-configuration
      procedure or a defining component. The local algorithm remains supported by
      its primary source; this is a bounded mapping assessment, not absence from all
      ontologies.
    evidence_ids:
    - mapping
- assessment_id: framework-specializations
  area: consistency
  topic: Framework versus concrete comparison algorithms
  outcome: supported
  target_ids:
  - AIMech:ParamILS
  - AIMech:BasicILS
  - AIMech:FocusedILS
  evidence_ids:
  - paramils-source-0
  - basicils-source-0
  - focusedils-source-0
  - finite-conventions
  summary: Retain ParamILS as the shared framework and BasicILS/FocusedILS as distinct
    instantiations.
  details: BasicILS fixes N paired evaluations; FocusedILS extends cached common prefixes
    until domination and uses a comparison-dependent bonus counter. The methods share
    neighborhood perturbation and restarts but are not synonyms. Numerical discretization,
    training-set generalization, non-strict plateau behavior and printed capping ambiguities
    remain explicit.
- assessment_id: racing-boundaries
  area: consistency
  topic: Heuristic challenger racing versus fixed-pool statistical elimination
  outcome: supported
  target_ids:
  - AIMech:RandomOnlineAggressiveRacing
  - AIMech:FRace
  evidence_ids:
  - randomonlineaggressiveracing-source-0
  - frace-source-0
  - finite-conventions
  - neighbors
  summary: Retain ROAR and F-Race as separate methods.
  details: ROAR samples new configurations uniformly and compares a challenger against
    an incumbent on shared randomized evaluations, without a significance threshold.
    F-Race retains a fixed initial pool, ranks candidates within instance blocks and
    performs aggregate/post-hoc significance tests. Rank sums are not raw expected-cost
    certificates. ROAR’s single-proposal wrapper must be distinguished from the shared
    intensification routine’s i>=2 early-exit condition.
- assessment_id: mapping-boundaries
  area: grounding
  topic: General configuration versus AIO learning/training concepts
  outcome: supported
  target_ids:
  - AIMech:ParamILS
  - AIMech:BasicILS
  - AIMech:FocusedILS
  - AIMech:RandomOnlineAggressiveRacing
  - AIMech:FRace
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain explicit no-match assessments for all five records.
  details: All five records carry explicit aio_no_match assessments. The inspected
    AIO TrainingStrategy definition concerns model preprocessing/training, whereas
    these methods configure general target algorithms. MachineLearningTask and MetaLearning
    do not automatically cover arbitrary solver configuration; ActiveLearning concerns
    label queries, RandomForest a tree ensemble, ReinforcementLearning a learning
    task, and EvaluationBias a bias. Incidental applications or common optimization
    vocabulary do not establish a mapping. SMAC’s separate RandomForest component
    mapping is therefore not inherited by ROAR or ParamILS.
findings:
- finding_id: roar-single-proposal
  issue_key: CultureBotAI-AIMech-ROAR-single-proposal-intensification
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  target_ids:
  - AIMech:RandomOnlineAggressiveRacing
  field_paths:
  - limitations[1]
  evidence_ids:
  - randomonlineaggressiveracing-source-0
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RandomOnlineAggressiveRacing.yaml
    role: maintained
  title: ROAR limitation conflates the shared routine’s early-exit condition with
    its single-proposal wrapper.
  description: The draft says the intensification budget applies after at least two
    challengers. Procedure2 has an i>=2 early-exit guard, but Section3.2 explicitly
    gives ROAR one proposal per call. The loop therefore ends after that one proposal;
    the guard does not require two challengers. Clarify this distinction without changing
    the main identity or attributing SMAC’s interleaving to ROAR.
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/72
actions:
- action_id: clarify-roar-wrapper
  finding_ids:
  - roar-single-proposal
  target_ids:
  - AIMech:RandomOnlineAggressiveRacing
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/RandomOnlineAggressiveRacing.yaml
    role: maintained
  description: Clarify single-proposal ROAR versus the shared routine guard, update
    ledger/history and save a successor disposition.
  acceptance_checks:
  - State that ROAR supplies one challenger per call and that i>=2 is a conditional
    early exit, not a mandatory minimum.
  - Pass required record/repository checks and retain the initial review.
  - Save a successor disposition linked to this exact finding and issue72.
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:ParamILS
  - AIMech:BasicILS
  - AIMech:FocusedILS
  - AIMech:RandomOnlineAggressiveRacing
  - AIMech:FRace
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - paramils-source-0
  - basicils-source-0
  - focusedils-source-0
  - randomonlineaggressiveracing-source-0
  - frace-source-0
  rationale: The shared ParamILS framework and its fixed/adaptive comparison instantiations
    are explicitly distinct concepts. ROAR’s random-proposal heuristic racing and
    F-Race’s fixed-pool rank-test elimination have different proposal, comparison
    and stopping mechanisms.
limitations:
- Adversarial author self-review only; all five records remain DRAFT.
- Only declared PDF pages were inspected. No training, benchmark, complete proof audit,
  significance-test implementation or author-code execution was performed.
- Published capping and tie-handling ambiguities remain qualified; no author-issued
  erratum or executable equivalence is claimed.
- Five additions and a nonempty inherited/new frontier leave discovery active.
tags:
- native-concepts
- algorithm-configuration
- local-search
- racing
- self-review
- discovery-ongoing
```
