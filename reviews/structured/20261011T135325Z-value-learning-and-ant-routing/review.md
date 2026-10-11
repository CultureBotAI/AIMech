# Scientific self-review of value learning and ant routing

- Review: 20261011T135325Z-value-learning-and-ant-routing
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T13:50:13Z
- Finished UTC: 2026-10-11T13:53:25Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain Q-learning, AntNet and ACO with explicit source conventions and AIO assessments. One minor AntNet eligibility finding is resolved; no actionable finding remains in the declared scope.

## Scope And Provenance

All fields of three newly maintained optimization concepts.

Selection: Exact three IDs in the discovery ledger; no sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 8d6f2185ea286454f2f5577e4e0686af6d0aaf32.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:QLearning | data/curated/QLearning.yaml | maintained | Q-learning |
| AIMech:AntNet | data/curated/AntNet.yaml | maintained | AntNet |
| AIMech:AntColonyOptimization | data/curated/AntColonyOptimization.yaml | maintained | Ant colony optimization |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:QLearning, AIMech:AntNet, AIMech:AntColonyOptimization | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 71.41s (0:01:11)<br>Checked 442 record(s); 0 failed.<br>Checked 298 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 76 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 74,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:QLearning, AIMech:AntNet, AIMech:AntColonyOptimization | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python -m aimech.cli check-source | passed | True | AIMech:QLearning, AIMech:AntNet, AIMech:AntColonyOptimization | Verified AIO https://w3id.org/aio/releases/2026-07-22/aio.json at 397851c547d1c4d8f06ef184f63c1d40bc86937a<br> |
| git diff --check | passed | True | AIMech:QLearning, AIMech:AntNet, AIMech:AntColonyOptimization | Command exited 0 with no output. |
| Finite value-learning and ant-routing calculations | passed | True | AIMech:QLearning, AIMech:AntNet, AIMech:AntColonyOptimization | {"q_learning": {"max_target": 9.2, "updated_observed_entry": 3.05, "next_behavior_action_substitution": 1.7, "other_entries_unchanged": true, "constant_stepsize_squared_sums_at_100_and_200": [6.25, 12.5], "qualification": "The exact constant-rate squared-sum grows linearly, violating the theorem condition; these finite values are not a convergence proof or a universal failure claim."}, "antnet": {"full_neighbor_probabilities": [0.28125, 0.3125, 0.40625], "mass_after_excluding_third_without_renormalizing": 0.59375, "conditional_eligible_probabilities": [0.47368421052631576, 0.5263157894736842], "reinforced_probabilities": [0.36000000000000004, 0.24, 0.4], "weakly_rewarded_selected_probability": 0.20800000000000002, "r_equals_one": [1.0, 0.0, 0.0], "power_reweighted_data_policy": [0.1776350778590918, 0.2889603412690355, 0.5334045808718727], "two_update_orders": [[0.252, 0.46799999999999997, 0.27999999999999997], [0.312, 0.40800000000000003, 0.27999999999999997]], "measured_forward_time": 9.0, "different_backward_time_not_substituted": 2.0}, "aco_schedule": {"evaporate_then_deposit": 2.0, "deposit_then_evaporate": 1.5, "qualification": "A simple noncommuting pair illustrates why a framework must declare update scheduling; it does not assert one universal ACO update."}, "limits": "Illustrative finite arithmetic only; no stochastic algorithm execution, simulator, author code, benchmark or theorem-proof audit."} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, limitations, provenance and AIO assessment

evidence: supported. Targets: AIMech:QLearning.

The record captures one-step Q-learning through the original finite tabular formulation and its explicitly conditional convergence statement. It is distinct from a learned Q table, a generic reinforcement-learning task, the complete deep Q-network procedure with replay and target networks, and Ant-Q’s edge-based constructive search. Maximizing the next-state estimate distinguishes its target from simply evaluating the next action chosen by the behavior policy. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 295 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 57 and 57 lines respectively. Text hits were prior candidate leads and neighboring-method mentions in maintained records, saved reviews and discovery reports; they did not identify an existing record for these candidates. Six exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and six native neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Maintain a finite table Q(x,a). On a sampled transition with current state x, action a, reward r and next state y, change only that entry to (1−alpha)*Q(x,a)+alpha*(r+gamma*max_b Q(y,b)), using the pre-update table for the target; leave other entries unchanged. Repeated samples supply rewards and next states without requiring an explicit estimated transition model. The maximum defines a greedy target even when behavior chooses an exploratory action; the update itself does not prescribe an exploration policy. In the paper’s discounted finite Markov setting, 0&lt;gamma&lt;1. Its theorem reports almost-sure convergence to optimal action values under bounded rewards, table representation, infinitely many samples of each state-action pair, and per-pair learning-rate sequences whose sum diverges while their squared sum converges, with 0&lt;=alpha&lt;1. This is an asymptotic, assumption-dependent statement, not a finite-sample stopping certificate. Limits: The state representation and sampling process must support the controlled Markov assumptions. Partial observability, changing dynamics, biased sample reuse or unvisited actions prevent importing the stated theorem unchanged. Infinite visits alone are insufficient without the learning-rate conditions. A fixed positive learning rate violates the finite squared-sum condition; neural or other function approximation is not covered by the tabular theorem. The record does not claim all such variants fail, only that this particular guarantee does not establish their convergence. The action-replay process in the proof is an analytical construction, not a required replay-buffer implementation. Section 4 separately discusses reusing empirical samples and warns that repeated reuse can favor the observed empirical environment. DQN’s additional machinery is not silently included. The paper sketches undiscounted absorbing and multiple-entry extensions but does not establish every multi-step variant under the displayed theorem. Discounting, available actions, ties, terminal representation and initialization need a declared application. The proof’s full appendix was not independently audited; no benchmark claim is curated.

### Identity, definition, mechanism, limitations, provenance and AIO assessment

evidence: supported. Targets: AIMech:AntNet.

This record denotes the 1998 datagram-network AntNet formulation. Forward ants experience ordinary data queues and backward ants return with priority; the proposed later scheme using fast forward ants and estimated virtual delays is a separate extension. It is an instantiated routing method within the ant-colony approach, not all ACO algorithms, a static TSP optimizer, Q-routing, or a generic multi-agent system. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 295 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 57 and 57 lines respectively. Text hits were prior candidate leads and neighboring-method mentions in maintained records, saved reviews and discovery reports; they did not identify an existing record for these candidates. Six exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and six native neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

At each node maintain destination-specific next-hop probabilities summing to one and local statistics of experienced trip times, including mean, variance and a recent best time. Periodically launch forward ants with destinations biased by local data traffic. They share data queues, record visited nodes and elapsed times, and choose among unvisited neighbors whenever any are available, falling back to all neighbors only when all have already been visited. Within that eligible set, choices use routing probabilities plus an instantaneous queue-length heuristic. On revisiting a node, remove the cycle from memory; discard an ant if the cycle consumed more than half its current age. At the destination, create a backward ant carrying the recorded path; it returns along that path through higher-priority queues. At each visited node, use forward-trip elapsed times to update the destination’s local statistics and reinforce the neighbor leading forward toward that destination. Statistically good subpaths can also update their corresponding destinations. For a chosen forward neighbor f and reinforcement r in (0,1], set P_f_new=P_f+r*(1−P_f) and each other P_n_new=(1−r)*P_n. The inspected scoring scheme combines a recent-best-time ratio with a dispersion-based correction and a normalized nonlinear squash; it rewards a path relative to local traffic conditions. Data packets sample from a power-reweighted routing table, whereas forward ants also use queue heuristics. Updates are concurrent and local; measured forward times, not recursively bootstrapped estimates from downstream nodes, supply the feedback. Limits: Backward traversal requires bidirectional links; forward and reverse costs need not be equal. The simulation omits full transport-layer error, flow and congestion control, so its comparisons are not deployment guarantees or universal superiority claims. The full-neighbor queue formula uses l_n=1−q_n/sum(q) and weights P_n+alpha*l_n. Zero queue sums and sampling from the restricted unvisited set require a declared normalization/fallback convention. The record does not silently treat the full-neighbor denominator as normalized after exclusions. Zero local traffic also needs a destination-selection convention. Every selected completed route receives positive reinforcement in the baseline, including poorly scored routes; alternatives decrease by normalization. This is not a negative reward on the selected bad route. At r=1 other probabilities become zero, so the algebra alone supplies no permanent full-support guarantee. Positive probabilities remain positive under a finite power reweighting in exact arithmetic; that transformation suppresses rather than categorically forbids rare data routes. The score’s interval is a deliberately rough asymmetric estimate built from adaptive statistics, not a calibrated confidence guarantee. Score parameters, window reset, zero dispersion, denominators, queue behavior and finite precision require declared conventions. Returned information can already be stale under changing traffic. The explicit method and Figure 3 allow good-subpath updates; Section 8.3’s one-destination summary is a simplification. Relations to actor–critic, Monte Carlo and temporal-difference learning are qualified analogies in the paper; the method does not inherit tabular Q-learning convergence or require TD bootstrapping. No author simulator or empirical benchmark was run.

### Identity, definition, mechanism, limitations, provenance and AIO assessment

evidence: supported. Targets: AIMech:AntColonyOptimization.

The record denotes the ACO framework defined in the 1999 source, not a single fixed update equation. Ant System, ACS, MAX–MIN and AntNet are individual procedures with additional choices. The source distinguishes strict ACO instantiations from the broader class of ant-inspired algorithms, so all ant algorithms are not treated as synonyms. PBIL’s probability-vector update and other population heuristics share some ideas without becoming identical to ACO. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 295 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 57 and 57 lines respectively. Text hits were prior candidate leads and neighboring-method mentions in maintained records, saved reviews and discovery reports; they did not identify an existing record for these candidates. Six exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and six native neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Represent the problem through states or solution components, feasible local moves and an objective. Artificial ants incrementally construct a solution or a component of one, maintaining private history as needed for feasibility. Their stochastic decisions use locally available pheromone information and, where configured, problem-specific heuristic information. Search experience changes the shared pheromone representation so later constructions can exploit prior discoveries. The framework schedules ant generation/activity, pheromone evaporation or forgetting, and optional globally informed daemon actions such as extra pheromone updates or local optimization. Deposits can occur during construction, after a solution is evaluated, or through the daemon; the ant’s stepwise and delayed deposit routines can both be absent when the daemon supplies deposits. A concrete algorithm must specify the representation, decision policy, update rule, scheduling and stopping criterion. Sequential or concurrent schedules are permitted by the prose; the framework does not prescribe a universal tau-power formula, inverse-cost deposit, elite rule or trail bound. Limits: A biological analogy is not a guarantee of optimality, exploration or prevention of stagnation. Positive feedback can concentrate search, and stochastic transitions or evaporation alone do not ensure that every feasible solution remains reachable. Constraints, candidate restrictions, zero weights and finite precision matter. Heuristic information and daemon actions are optional or instance dependent. Source prose permits local optimization, lookahead and other extensions; these are not obligatory baseline operations. Its Figure 3 caption refers to an in_parallel statement while the displayed code uses schedule_activities, so the scheduling prose and explicit instantiation must govern an executable implementation. The framework was synthesized from algorithms with varied representations and update schedules. Membership does not transfer one member’s convergence result or benchmark performance to another. The static/dynamic application examples do not define a universal network-routing or machine-learning algorithm. The paper’s broad PBIL/evolutionary/learning-automata comparisons are conceptual parallels, not evidence of exact algorithm equivalence. No experimental outcomes, fixed best parameterization or full field-wide coverage claim is curated.

### Maximum target and conditional tabular theorem

consistency: supported. Targets: AIMech:QLearning.

Retain one-step Q-learning with its conditional finite-table convergence statement.

The update uses the pre-update maximum at the next state and changes only the sampled pair. It does not require the behavior action to attain that maximum or prescribe exploration. The displayed theorem requires finite Markov spaces, bounded rewards, discounting, infinite pair visits and both stepsize sums. Constant positive alpha fails the squared-sum condition, without proving every constant-rate application fails. The proof action-replay construction is not a required replay buffer; the appendix was not independently audited.

### Eligibility, measured forward trips and normalized local policy updates

consistency: supported. Targets: AIMech:AntNet.

Retain original AntNet with the corrected hard neighbor-eligibility rule.

Issue 83’s soft preference was replaced with the source’s two cases: choose among unvisited neighbors when possible; otherwise all neighbors. The restricted-set normalization and zero-queue qualifications remain. Forward ants use ordinary data queues, backward ants use priority queues and reinforce forward-direction choices from measured forward times. Good-subpath updates follow the explicit method despite the later simplified summary. The update preserves the simplex for valid reinforcement but r=1 removes alternatives; positive power reweighting does not categorically exclude positive-probability routes. The rough score interval is not calibrated coverage, and the simplified simulator establishes no deployment guarantee.

### Metaheuristic scope and optional components

consistency: supported. Targets: AIMech:AntColonyOptimization.

Retain ACO as a framework distinct from its individual algorithms and broader ant-inspired computation.

Source footnote 3 defines framework/instance/broader-ant boundaries. Deposits can be stepwise, delayed or daemon-driven; heuristics, daemon actions and local optimization are not universal requirements. The scheduling prose allows sequential or concurrent implementations despite the figure-caption mismatch. Noncommuting finite updates show why schedule choice matters. No single trail exponent, elite deposit, bound, convergence theorem or benchmark ranking is assigned to the framework.

### Qualified learning relations and framework no-match

grounding: supported. Targets: AIMech:QLearning, AIMech:AntNet, AIMech:AntColonyOptimization.

Retain three native concepts with two related matches and one bounded no-match assessment.

Six exact AIO CLASS nodes with scoped synonyms/comments/outgoing edges and six native neighbors were inspected. Q-learning and AntNet receive related_match relations to the AIO Reinforcement Learning task, supported by their primary definitions and explicit discussion; no task/algorithm identity or shared convergence theorem is asserted. ACO retains a bounded no-match assessment because instance-specific learning relations, generic search language and language-model targets do not ground the framework itself. The original ACO source distinguishes strict ACO from the broader ant-inspired category.

## Findings

### antnet-neighbor-eligibility: AntNet eligibility is phrased as a soft preference.

minor / resolved / confirmed; issue key: CultureBotAI-AIMech-AntNet-neighbor-eligibility.

The initial draft phrased the eligibility constraint as a soft preference. The corrected claim preserves the primary two-case rule; the original review remains immutable.

Disposition: The maintained mechanism now explicitly restricts selection to unvisited neighbors whenever any exist, using all neighbors only when all were visited. The restricted-set normalization and zero-queue qualifications remain intact. The ledger and append-only history were updated, the final inputs inspected, and post-fix required checks passed.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:QLearning, AIMech:AntNet, AIMech:AntColonyOptimization. Tabular action-value learning, measured-trip adaptive routing and the constructive ant-search framework have distinct supported scopes. Shared learning vocabulary and ACO membership do not imply method equivalence or transferable guarantees.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T134751Z-value-learning-and-ant-routing.json | supports | Compared all 442 pinned AIO labels/scoped synonyms and 295 preceding native IDs/names/aliases, including candidate-internal normalized uniqueness. No identity match was found. Full-checkout fixed-string searches included ignored/hidden files and returned 57 worktree and 57 main lines. All 34 unique hit contents were inspected: prior candidate leads and neighboring-method distinctions in maintained records, saved reviews and discovery reports. No existing candidate identity was found. Six exact AIO CLASS nodes with scoped synonyms/comments/outgoing edges and six native neighboring records were inspected. Absence is bounded to this snapshot and semantic neighborhood. |
| mapping | sources/aio/aio.json; Six exact CLASS nodes and scoped synonyms/comments/outgoing edges in source_analysis.aio_mapping_inspection | supports | Six exact AIO CLASS nodes with scoped synonyms/comments/outgoing edges and six native neighbors were inspected. Q-learning and AntNet receive related_match relations to the AIO Reinforcement Learning task, supported by their primary definitions and explicit discussion; no task/algorithm identity or shared convergence theorem is asserted. ACO retains a bounded no-match assessment because instance-specific learning relations, generic search language and language-model targets do not ground the framework itself. The original ACO source distinguishes strict ACO from the broader ant-inspired category. |
| neighbors | research/discovery/20261011T134751Z-value-learning-and-ant-routing.json; source_analysis.aio_mapping_inspection.native_neighbors | supports | Deep Q-network learning, Ant-Q, Ant System, ACS, MAX–MIN and PBIL were read for identity and mechanism boundaries. The new records separate the tabular value-learning update, the original measured-trip routing method and the ACO framework. Instance-specific guarantees and update choices are not transferred to the framework. |
| finite-conventions | research/discovery/value-learning-and-ant-routing-boundaries.py; calculate(): Q-learning target, stepsize condition, routing eligibility, simplex reinforcement, power reweighting, forward-time feedback and update scheduling | supports | Original finite arithmetic distinguishes the Q-learning maximum target from the next behavior action, shows why a constant stepsize violates the squared-sum theorem condition, checks AntNet subset normalization, simplex updates, positive-route reinforcement, power reweighting and forward/reverse-time distinction, and demonstrates schedule-dependent noncommuting updates. These examples are not full algorithms, benchmarks or convergence proofs. |
| qlearning-source-0 | https://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf; Section 2, PDF pp.2–4 / journal pp.280–282, Equations 1–3 and convergence theorem; Section 4, PDF pp.7–8 / journal pp.285–286 | supports | Q-learning. Machine Learning 8:279–292 (1992), 14-page journal article hosted on Peter Dayan’s UCL publication site. Actual reading scopes are declared in the ledger. Critical equations and the ACO pseudocode were visually checked; AntNet required declared OCR reading after corrupted native glyph extraction. No author code was run. |
| antnet-source-0 | https://arxiv.org/pdf/1105.5449; Sections 4.1–4.2, PDF pp.9–18 / journal pp.325–334, Equations 1–9 and Figures 2–3; model limits, PDF p.7; Sections 8–10, PDF pp.35–42 | supports | AntNet: Distributed Stigmergetic Control for Communications Networks. JAIR 9:317–365 (1998), 49-page article archived as arXiv:1105.5449v1 on 27 May 2011; archive upload date is not the publication year. Actual reading scopes are declared in the ledger. Critical equations and the ACO pseudocode were visually checked; AntNet required declared OCR reading after corrupted native glyph extraction. No author code was run. |
| antcolonyoptimization-source-0 | https://iridia.ulb.ac.be/~mdorigo/Published_papers/All_Dorigo_papers/DorDicGam1999al.pdf; Section 2 and footnote 3, PDF pp.5–9 / journal pp.141–145, especially Figure 3; Section 3 opening, PDF p.10; discussion and conclusions, PDF pp.28–30 | supports | Ant Algorithms for Discrete Optimization. Artificial Life 5(2):137–172 (1999), 36-page journal-formatted author-hosted PDF; author URL redirects to a public ULB cloud file. Actual reading scopes are declared in the ledger. Critical equations and the ACO pseudocode were visually checked; AntNet required declared OCR reading after corrupted native glyph extraction. No author code was run. |

## Limits And Additional Notes

- Adversarial author self-review only; every record remains DRAFT.
- Only declared text/OCR and visual pages were inspected. No benchmark, author-code execution or convergence-proof audit was performed.
- Source presentation and numerical-boundary ambiguities remain explicit. The AntNet archive upload year is distinguished from its 1998 publication, and the Q-learning guarantee is reported with assumptions rather than independently proved.
- Three additions and 171 pending inspection leads plus other unresolved dispositions leave discovery active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T135325Z-value-learning-and-ant-routing
kind: category
repository: CultureBotAI/AIMech
title: Scientific self-review of value learning and ant routing
started_at: '2026-10-11T13:50:13Z'
finished_at: '2026-10-11T13:53:25Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed all three records
    against declared primary methods, PDF images and AntNet OCR text, six exact AIO
    nodes, six native neighbors and original finite arithmetic. Issue 83 was recorded
    and corrected with a linked successor disposition. This is not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain Q-learning, AntNet and ACO with explicit source conventions and AIO
  assessments. One minor AntNet eligibility finding is resolved; no actionable finding
  remains in the declared scope.
source:
  git_revision: 8d6f2185ea286454f2f5577e4e0686af6d0aaf32
  state: working_tree
  inputs:
  - path: data/aio/EvolutionaryLLM.yaml
    sha256: d3db6adea3d8d58096c9fb5abef67273489ee719ab900b2d4adbb129e4f7362f
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
    role: context
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
    role: context
  - path: data/aio/ReinforcementLearningLLM.yaml
    sha256: e386376b9b1a9c78349d66e8609a655e273620d8bc607978c728ac3b7ce3808a
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/curated/AntColonyOptimization.yaml
    sha256: d65642ea5cac777843fa0285d27a8b8bc129c2544528ba122c7144c0eb794f9d
    role: target
  - path: data/curated/AntColonySystem.yaml
    sha256: 9069dd63cc6c1710594246d2817d162b6cd42f2ee383ad84e9cb7a17f94dfc2f
    role: context
  - path: data/curated/AntNet.yaml
    sha256: e7d511a9923dd43bea25f50c09619789c9fbeaa7f4677344007cc0a9c1836c50
    role: target
  - path: data/curated/AntQ.yaml
    sha256: a01fc6b6c6529db01836d0bf7b63a02948ea5dd640af3a9c6c5044f411c7acfe
    role: context
  - path: data/curated/AntSystem.yaml
    sha256: 89aa5c8e5a5d8ae3717bcd5c3be94d32543402900872533c1c4a6bbdf41f506c
    role: context
  - path: data/curated/DeepQNetwork.yaml
    sha256: ea346f5f8650c02e1d8d825c896797e3c022f20525d07b64b96f97ae96a1df2a
    role: context
  - path: data/curated/MaxMinAntSystem.yaml
    sha256: 6f50bb6ce0399ffeeeab89c1ebc7ab94e2360da5708618f7ac2ff2d3dad37837
    role: context
  - path: data/curated/PopulationBasedIncrementalLearning.yaml
    sha256: fb2500f70c8a0cf57639b33f7f89acf9f141adf75a238aa248e784afc09866d2
    role: context
  - path: data/curated/QLearning.yaml
    sha256: bcbd0f51f46e91ba6d88c9dc84baa9656aef82282c5c56d887ca81ff5182eb95
    role: target
  - path: research/discovery/20261011T134751Z-value-learning-and-ant-routing.json
    sha256: 3afe06627bac0b4bb80c67fa54a74d8e78f626c1c8e03005d81802e504768d51
    role: context
  - path: research/discovery/value-learning-and-ant-routing-boundaries.py
    sha256: 4165542caeda9461f00b0f3974c0d13a03ac1f0bc4c255325fdb0cd708624b9b
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
- target_id: AIMech:QLearning
  path: data/curated/QLearning.yaml
  label: Q-learning
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/QLearning.yaml
    role: maintained
- target_id: AIMech:AntNet
  path: data/curated/AntNet.yaml
  label: AntNet
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AntNet.yaml
    role: maintained
- target_id: AIMech:AntColonyOptimization
  path: data/curated/AntColonyOptimization.yaml
  label: Ant colony optimization
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AntColonyOptimization.yaml
    role: maintained
scope:
  description: All fields of three newly maintained optimization concepts.
  selection: Exact three IDs in the discovery ledger; no sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:QLearning
  - AIMech:AntNet
  - AIMech:AntColonyOptimization
  exclusions:
  - target: Older records and unselected candidates
    reason: Neighbors were inspected for boundaries, not a complete new review of
      the earlier corpus.
  - target: Unread pages, outcomes and implementations
    reason: Only declared primary text/OCR and visual pages and finite curator calculations
      were inspected; no author code or benchmark was run.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:QLearning
  - AIMech:AntNet
  - AIMech:AntColonyOptimization
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 71.41s (0:01:11)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 298 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 76 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 74,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:QLearning
  - AIMech:AntNet
  - AIMech:AntColonyOptimization
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
- check_id: required-2
  name: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/AIMech/.venv/bin/python
    -m aimech.cli check-source
  status: passed
  required: true
  target_ids:
  - AIMech:QLearning
  - AIMech:AntNet
  - AIMech:AntColonyOptimization
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
  - AIMech:QLearning
  - AIMech:AntNet
  - AIMech:AntColonyOptimization
  exit_code: 0
  expected_exit_code: 0
  summary: Command exited 0 with no output.
- check_id: finite-arithmetic
  name: Finite value-learning and ant-routing calculations
  command: python3 research/discovery/value-learning-and-ant-routing-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:QLearning
  - AIMech:AntNet
  - AIMech:AntColonyOptimization
  exit_code: 0
  expected_exit_code: 0
  summary: '{"q_learning": {"max_target": 9.2, "updated_observed_entry": 3.05, "next_behavior_action_substitution":
    1.7, "other_entries_unchanged": true, "constant_stepsize_squared_sums_at_100_and_200":
    [6.25, 12.5], "qualification": "The exact constant-rate squared-sum grows linearly,
    violating the theorem condition; these finite values are not a convergence proof
    or a universal failure claim."}, "antnet": {"full_neighbor_probabilities": [0.28125,
    0.3125, 0.40625], "mass_after_excluding_third_without_renormalizing": 0.59375,
    "conditional_eligible_probabilities": [0.47368421052631576, 0.5263157894736842],
    "reinforced_probabilities": [0.36000000000000004, 0.24, 0.4], "weakly_rewarded_selected_probability":
    0.20800000000000002, "r_equals_one": [1.0, 0.0, 0.0], "power_reweighted_data_policy":
    [0.1776350778590918, 0.2889603412690355, 0.5334045808718727], "two_update_orders":
    [[0.252, 0.46799999999999997, 0.27999999999999997], [0.312, 0.40800000000000003,
    0.27999999999999997]], "measured_forward_time": 9.0, "different_backward_time_not_substituted":
    2.0}, "aco_schedule": {"evaporate_then_deposit": 2.0, "deposit_then_evaporate":
    1.5, "qualification": "A simple noncommuting pair illustrates why a framework
    must declare update scheduling; it does not assert one universal ACO update."},
    "limits": "Illustrative finite arithmetic only; no stochastic algorithm execution,
    simulator, author code, benchmark or theorem-proof audit."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T134751Z-value-learning-and-ant-routing.json
  accessed_at: '2026-10-11T13:50:13Z'
  support: supports
  summary: 'Compared all 442 pinned AIO labels/scoped synonyms and 295 preceding native
    IDs/names/aliases, including candidate-internal normalized uniqueness. No identity
    match was found. Full-checkout fixed-string searches included ignored/hidden files
    and returned 57 worktree and 57 main lines. All 34 unique hit contents were inspected:
    prior candidate leads and neighboring-method distinctions in maintained records,
    saved reviews and discovery reports. No existing candidate identity was found.
    Six exact AIO CLASS nodes with scoped synonyms/comments/outgoing edges and six
    native neighboring records were inspected. Absence is bounded to this snapshot
    and semantic neighborhood.'
  search_scope: All 442 pinned AIO labels/scoped synonyms and 295 preceding maintained
    IDs/names/aliases; both full checkouts including ignored/hidden files; candidate-internal
    normalized uniqueness.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Six exact CLASS nodes and scoped synonyms/comments/outgoing edges in source_analysis.aio_mapping_inspection
  accessed_at: '2026-10-11T13:50:13Z'
  support: supports
  summary: Six exact AIO CLASS nodes with scoped synonyms/comments/outgoing edges
    and six native neighbors were inspected. Q-learning and AntNet receive related_match
    relations to the AIO Reinforcement Learning task, supported by their primary definitions
    and explicit discussion; no task/algorithm identity or shared convergence theorem
    is asserted. ACO retains a bounded no-match assessment because instance-specific
    learning relations, generic search language and language-model targets do not
    ground the framework itself. The original ACO source distinguishes strict ACO
    from the broader ant-inspired category.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T134751Z-value-learning-and-ant-routing.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors
  accessed_at: '2026-10-11T13:50:13Z'
  support: supports
  summary: Deep Q-network learning, Ant-Q, Ant System, ACS, MAX–MIN and PBIL were
    read for identity and mechanism boundaries. The new records separate the tabular
    value-learning update, the original measured-trip routing method and the ACO framework.
    Instance-specific guarantees and update choices are not transferred to the framework.
- evidence_id: finite-conventions
  kind: record_content
  reference: research/discovery/value-learning-and-ant-routing-boundaries.py
  locator: 'calculate(): Q-learning target, stepsize condition, routing eligibility,
    simplex reinforcement, power reweighting, forward-time feedback and update scheduling'
  accessed_at: '2026-10-11T13:50:13Z'
  snapshot_sha256: 4165542caeda9461f00b0f3974c0d13a03ac1f0bc4c255325fdb0cd708624b9b
  support: supports
  summary: Original finite arithmetic distinguishes the Q-learning maximum target
    from the next behavior action, shows why a constant stepsize violates the squared-sum
    theorem condition, checks AntNet subset normalization, simplex updates, positive-route
    reinforcement, power reweighting and forward/reverse-time distinction, and demonstrates
    schedule-dependent noncommuting updates. These examples are not full algorithms,
    benchmarks or convergence proofs.
- evidence_id: qlearning-source-0
  kind: primary_source
  reference: https://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf
  locator: Section 2, PDF pp.2–4 / journal pp.280–282, Equations 1–3 and convergence
    theorem; Section 4, PDF pp.7–8 / journal pp.285–286
  accessed_at: '2026-10-11T13:40:26Z'
  support: supports
  summary: Q-learning. Machine Learning 8:279–292 (1992), 14-page journal article
    hosted on Peter Dayan’s UCL publication site. Actual reading scopes are declared
    in the ledger. Critical equations and the ACO pseudocode were visually checked;
    AntNet required declared OCR reading after corrupted native glyph extraction.
    No author code was run.
  snapshot_sha256: 3f1938a6001991f3171e13a93196fc8fc27978f18c87445321bb25058f35776f
- evidence_id: antnet-source-0
  kind: primary_source
  reference: https://arxiv.org/pdf/1105.5449
  locator: Sections 4.1–4.2, PDF pp.9–18 / journal pp.325–334, Equations 1–9 and Figures
    2–3; model limits, PDF p.7; Sections 8–10, PDF pp.35–42
  accessed_at: '2026-10-11T13:41:42Z'
  support: supports
  summary: 'AntNet: Distributed Stigmergetic Control for Communications Networks.
    JAIR 9:317–365 (1998), 49-page article archived as arXiv:1105.5449v1 on 27 May
    2011; archive upload date is not the publication year. Actual reading scopes are
    declared in the ledger. Critical equations and the ACO pseudocode were visually
    checked; AntNet required declared OCR reading after corrupted native glyph extraction.
    No author code was run.'
  snapshot_sha256: bee45446fa421191bd2e9396261532b5a0a6c339c369792b37506a0242cd867d
- evidence_id: antcolonyoptimization-source-0
  kind: primary_source
  reference: https://iridia.ulb.ac.be/~mdorigo/Published_papers/All_Dorigo_papers/DorDicGam1999al.pdf
  locator: Section 2 and footnote 3, PDF pp.5–9 / journal pp.141–145, especially Figure
    3; Section 3 opening, PDF p.10; discussion and conclusions, PDF pp.28–30
  accessed_at: '2026-10-11T13:40:26Z'
  support: supports
  summary: Ant Algorithms for Discrete Optimization. Artificial Life 5(2):137–172
    (1999), 36-page journal-formatted author-hosted PDF; author URL redirects to a
    public ULB cloud file. Actual reading scopes are declared in the ledger. Critical
    equations and the ACO pseudocode were visually checked; AntNet required declared
    OCR reading after corrupted native glyph extraction. No author code was run.
  snapshot_sha256: 7c6a5a0df5dd5ba71abe1da99763edee038003df3335827dc5d862270ae9f51e
assessments:
- assessment_id: qlearning
  area: evidence
  topic: Identity, definition, mechanism, limitations, provenance and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:QLearning
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - qlearning-source-0
  summary: The record captures one-step Q-learning through the original finite tabular
    formulation and its explicitly conditional convergence statement. It is distinct
    from a learned Q table, a generic reinforcement-learning task, the complete deep
    Q-network procedure with replay and target networks, and Ant-Q’s edge-based constructive
    search. Maximizing the next-state estimate distinguishes its target from simply
    evaluating the next action chosen by the behavior policy. No normalized identity
    match was found across all 442 pinned AIO labels/scoped synonyms and 295 preceding
    native IDs/names/aliases. Full-checkout fixed-string searches included ignored
    and hidden files in worktree and main, returning 57 and 57 lines respectively.
    Text hits were prior candidate leads and neighboring-method mentions in maintained
    records, saved reviews and discovery reports; they did not identify an existing
    record for these candidates. Six exact AIO CLASS nodes with scoped synonyms/comments
    and outgoing edges and six native neighboring mechanisms were inspected. Absence
    is bounded to this snapshot and semantic neighborhood.
  details: 'Maintain a finite table Q(x,a). On a sampled transition with current state
    x, action a, reward r and next state y, change only that entry to (1−alpha)*Q(x,a)+alpha*(r+gamma*max_b
    Q(y,b)), using the pre-update table for the target; leave other entries unchanged.
    Repeated samples supply rewards and next states without requiring an explicit
    estimated transition model. The maximum defines a greedy target even when behavior
    chooses an exploratory action; the update itself does not prescribe an exploration
    policy. In the paper’s discounted finite Markov setting, 0<gamma<1. Its theorem
    reports almost-sure convergence to optimal action values under bounded rewards,
    table representation, infinitely many samples of each state-action pair, and per-pair
    learning-rate sequences whose sum diverges while their squared sum converges,
    with 0<=alpha<1. This is an asymptotic, assumption-dependent statement, not a
    finite-sample stopping certificate. Limits: The state representation and sampling
    process must support the controlled Markov assumptions. Partial observability,
    changing dynamics, biased sample reuse or unvisited actions prevent importing
    the stated theorem unchanged. Infinite visits alone are insufficient without the
    learning-rate conditions. A fixed positive learning rate violates the finite squared-sum
    condition; neural or other function approximation is not covered by the tabular
    theorem. The record does not claim all such variants fail, only that this particular
    guarantee does not establish their convergence. The action-replay process in the
    proof is an analytical construction, not a required replay-buffer implementation.
    Section 4 separately discusses reusing empirical samples and warns that repeated
    reuse can favor the observed empirical environment. DQN’s additional machinery
    is not silently included. The paper sketches undiscounted absorbing and multiple-entry
    extensions but does not establish every multi-step variant under the displayed
    theorem. Discounting, available actions, ties, terminal representation and initialization
    need a declared application. The proof’s full appendix was not independently audited;
    no benchmark claim is curated.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A named optimization algorithm or algorithm family with specified
      search state and update rules, not a trained instance or benchmark outcome.
    evidence_ids:
    - qlearning-source-0
  - name: aio-relations
    value: related_match
    definition: 'related_match to AIO:ReinforcementLearning: The source explicitly
      defines Q-learning as a model-free reinforcement-learning algorithm. The pinned
      AIO target is a learning task; the relation records this direct connection without
      equating the algorithm to the task or asserting an algorithm-class hierarchy.'
    evidence_ids:
    - mapping
- assessment_id: antnet
  area: evidence
  topic: Identity, definition, mechanism, limitations, provenance and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:AntNet
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - antnet-source-0
  summary: This record denotes the 1998 datagram-network AntNet formulation. Forward
    ants experience ordinary data queues and backward ants return with priority; the
    proposed later scheme using fast forward ants and estimated virtual delays is
    a separate extension. It is an instantiated routing method within the ant-colony
    approach, not all ACO algorithms, a static TSP optimizer, Q-routing, or a generic
    multi-agent system. No normalized identity match was found across all 442 pinned
    AIO labels/scoped synonyms and 295 preceding native IDs/names/aliases. Full-checkout
    fixed-string searches included ignored and hidden files in worktree and main,
    returning 57 and 57 lines respectively. Text hits were prior candidate leads and
    neighboring-method mentions in maintained records, saved reviews and discovery
    reports; they did not identify an existing record for these candidates. Six exact
    AIO CLASS nodes with scoped synonyms/comments and outgoing edges and six native
    neighboring mechanisms were inspected. Absence is bounded to this snapshot and
    semantic neighborhood.
  details: 'At each node maintain destination-specific next-hop probabilities summing
    to one and local statistics of experienced trip times, including mean, variance
    and a recent best time. Periodically launch forward ants with destinations biased
    by local data traffic. They share data queues, record visited nodes and elapsed
    times, and choose among unvisited neighbors whenever any are available, falling
    back to all neighbors only when all have already been visited. Within that eligible
    set, choices use routing probabilities plus an instantaneous queue-length heuristic.
    On revisiting a node, remove the cycle from memory; discard an ant if the cycle
    consumed more than half its current age. At the destination, create a backward
    ant carrying the recorded path; it returns along that path through higher-priority
    queues. At each visited node, use forward-trip elapsed times to update the destination’s
    local statistics and reinforce the neighbor leading forward toward that destination.
    Statistically good subpaths can also update their corresponding destinations.
    For a chosen forward neighbor f and reinforcement r in (0,1], set P_f_new=P_f+r*(1−P_f)
    and each other P_n_new=(1−r)*P_n. The inspected scoring scheme combines a recent-best-time
    ratio with a dispersion-based correction and a normalized nonlinear squash; it
    rewards a path relative to local traffic conditions. Data packets sample from
    a power-reweighted routing table, whereas forward ants also use queue heuristics.
    Updates are concurrent and local; measured forward times, not recursively bootstrapped
    estimates from downstream nodes, supply the feedback. Limits: Backward traversal
    requires bidirectional links; forward and reverse costs need not be equal. The
    simulation omits full transport-layer error, flow and congestion control, so its
    comparisons are not deployment guarantees or universal superiority claims. The
    full-neighbor queue formula uses l_n=1−q_n/sum(q) and weights P_n+alpha*l_n. Zero
    queue sums and sampling from the restricted unvisited set require a declared normalization/fallback
    convention. The record does not silently treat the full-neighbor denominator as
    normalized after exclusions. Zero local traffic also needs a destination-selection
    convention. Every selected completed route receives positive reinforcement in
    the baseline, including poorly scored routes; alternatives decrease by normalization.
    This is not a negative reward on the selected bad route. At r=1 other probabilities
    become zero, so the algebra alone supplies no permanent full-support guarantee.
    Positive probabilities remain positive under a finite power reweighting in exact
    arithmetic; that transformation suppresses rather than categorically forbids rare
    data routes. The score’s interval is a deliberately rough asymmetric estimate
    built from adaptive statistics, not a calibrated confidence guarantee. Score parameters,
    window reset, zero dispersion, denominators, queue behavior and finite precision
    require declared conventions. Returned information can already be stale under
    changing traffic. The explicit method and Figure 3 allow good-subpath updates;
    Section 8.3’s one-destination summary is a simplification. Relations to actor–critic,
    Monte Carlo and temporal-difference learning are qualified analogies in the paper;
    the method does not inherit tabular Q-learning convergence or require TD bootstrapping.
    No author simulator or empirical benchmark was run.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A named optimization algorithm or algorithm family with specified
      search state and update rules, not a trained instance or benchmark outcome.
    evidence_ids:
    - antnet-source-0
  - name: aio-relations
    value: related_match
    definition: 'related_match to AIO:ReinforcementLearning: The source explicitly
      analyzes AntNet as adaptive stochastic routing with reinforcement-based policy
      updates and discusses its connection to reinforcement learning. The AIO target
      is a learning task; this related match does not equate AntNet to that task,
      to Q-learning, or to a stationary Markov controller.'
    evidence_ids:
    - mapping
- assessment_id: antcolonyoptimization
  area: evidence
  topic: Identity, definition, mechanism, limitations, provenance and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:AntColonyOptimization
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - antcolonyoptimization-source-0
  summary: The record denotes the ACO framework defined in the 1999 source, not a
    single fixed update equation. Ant System, ACS, MAX–MIN and AntNet are individual
    procedures with additional choices. The source distinguishes strict ACO instantiations
    from the broader class of ant-inspired algorithms, so all ant algorithms are not
    treated as synonyms. PBIL’s probability-vector update and other population heuristics
    share some ideas without becoming identical to ACO. No normalized identity match
    was found across all 442 pinned AIO labels/scoped synonyms and 295 preceding native
    IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden
    files in worktree and main, returning 57 and 57 lines respectively. Text hits
    were prior candidate leads and neighboring-method mentions in maintained records,
    saved reviews and discovery reports; they did not identify an existing record
    for these candidates. Six exact AIO CLASS nodes with scoped synonyms/comments
    and outgoing edges and six native neighboring mechanisms were inspected. Absence
    is bounded to this snapshot and semantic neighborhood.
  details: 'Represent the problem through states or solution components, feasible
    local moves and an objective. Artificial ants incrementally construct a solution
    or a component of one, maintaining private history as needed for feasibility.
    Their stochastic decisions use locally available pheromone information and, where
    configured, problem-specific heuristic information. Search experience changes
    the shared pheromone representation so later constructions can exploit prior discoveries.
    The framework schedules ant generation/activity, pheromone evaporation or forgetting,
    and optional globally informed daemon actions such as extra pheromone updates
    or local optimization. Deposits can occur during construction, after a solution
    is evaluated, or through the daemon; the ant’s stepwise and delayed deposit routines
    can both be absent when the daemon supplies deposits. A concrete algorithm must
    specify the representation, decision policy, update rule, scheduling and stopping
    criterion. Sequential or concurrent schedules are permitted by the prose; the
    framework does not prescribe a universal tau-power formula, inverse-cost deposit,
    elite rule or trail bound. Limits: A biological analogy is not a guarantee of
    optimality, exploration or prevention of stagnation. Positive feedback can concentrate
    search, and stochastic transitions or evaporation alone do not ensure that every
    feasible solution remains reachable. Constraints, candidate restrictions, zero
    weights and finite precision matter. Heuristic information and daemon actions
    are optional or instance dependent. Source prose permits local optimization, lookahead
    and other extensions; these are not obligatory baseline operations. Its Figure
    3 caption refers to an in_parallel statement while the displayed code uses schedule_activities,
    so the scheduling prose and explicit instantiation must govern an executable implementation.
    The framework was synthesized from algorithms with varied representations and
    update schedules. Membership does not transfer one member’s convergence result
    or benchmark performance to another. The static/dynamic application examples do
    not define a universal network-routing or machine-learning algorithm. The paper’s
    broad PBIL/evolutionary/learning-automata comparisons are conceptual parallels,
    not evidence of exact algorithm equivalence. No experimental outcomes, fixed best
    parameterization or full field-wide coverage claim is curated.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A named optimization algorithm or algorithm family with specified
      search state and update rules, not a trained instance or benchmark outcome.
    evidence_ids:
    - antcolonyoptimization-source-0
  - name: aio-relations
    value: aio_no_match
    definition: No suitable AIO target was found for the ACO framework in the inspected
      snapshot and semantic neighborhood. Instance-specific learning relations and
      model labels are not generalized into a framework identity. The framework is
      general constructive optimization, not specifically preprocessing or training
      a machine-learning model. The target is a learning task, whereas this record
      defines a general search framework; optimization terminology alone does not
      identify that task. Some ACO members have explicit reinforcement-learning formulations,
      but the framework does not require their action-value or policy-learning semantics.
      Their individual related matches do not establish an appropriate relation for
      every ACO instantiation. Artificial ants and shared search memory do not establish
      a reward-fine-tuned language-model identity. The target is a large language
      model; population-search analogies and its related evolutionary-algorithms synonym
      do not identify this framework. A stochastic augmented-state representation
      does not make this constructive search framework the pinned network/model class.
      Its representation and transition laws remain instance dependent.
    evidence_ids:
    - mapping
- assessment_id: qlearning-boundaries
  area: consistency
  topic: Maximum target and conditional tabular theorem
  outcome: supported
  target_ids:
  - AIMech:QLearning
  evidence_ids:
  - qlearning-source-0
  - finite-conventions
  - neighbors
  summary: Retain one-step Q-learning with its conditional finite-table convergence
    statement.
  details: The update uses the pre-update maximum at the next state and changes only
    the sampled pair. It does not require the behavior action to attain that maximum
    or prescribe exploration. The displayed theorem requires finite Markov spaces,
    bounded rewards, discounting, infinite pair visits and both stepsize sums. Constant
    positive alpha fails the squared-sum condition, without proving every constant-rate
    application fails. The proof action-replay construction is not a required replay
    buffer; the appendix was not independently audited.
- assessment_id: antnet-boundaries
  area: consistency
  topic: Eligibility, measured forward trips and normalized local policy updates
  outcome: supported
  target_ids:
  - AIMech:AntNet
  evidence_ids:
  - antnet-source-0
  - finite-conventions
  - neighbors
  summary: Retain original AntNet with the corrected hard neighbor-eligibility rule.
  details: 'Issue 83’s soft preference was replaced with the source’s two cases: choose
    among unvisited neighbors when possible; otherwise all neighbors. The restricted-set
    normalization and zero-queue qualifications remain. Forward ants use ordinary
    data queues, backward ants use priority queues and reinforce forward-direction
    choices from measured forward times. Good-subpath updates follow the explicit
    method despite the later simplified summary. The update preserves the simplex
    for valid reinforcement but r=1 removes alternatives; positive power reweighting
    does not categorically exclude positive-probability routes. The rough score interval
    is not calibrated coverage, and the simplified simulator establishes no deployment
    guarantee.'
- assessment_id: aco-boundaries
  area: consistency
  topic: Metaheuristic scope and optional components
  outcome: supported
  target_ids:
  - AIMech:AntColonyOptimization
  evidence_ids:
  - antcolonyoptimization-source-0
  - finite-conventions
  - neighbors
  summary: Retain ACO as a framework distinct from its individual algorithms and broader
    ant-inspired computation.
  details: Source footnote 3 defines framework/instance/broader-ant boundaries. Deposits
    can be stepwise, delayed or daemon-driven; heuristics, daemon actions and local
    optimization are not universal requirements. The scheduling prose allows sequential
    or concurrent implementations despite the figure-caption mismatch. Noncommuting
    finite updates show why schedule choice matters. No single trail exponent, elite
    deposit, bound, convergence theorem or benchmark ranking is assigned to the framework.
- assessment_id: mapping-boundaries
  area: grounding
  topic: Qualified learning relations and framework no-match
  outcome: supported
  target_ids:
  - AIMech:QLearning
  - AIMech:AntNet
  - AIMech:AntColonyOptimization
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain three native concepts with two related matches and one bounded no-match
    assessment.
  details: Six exact AIO CLASS nodes with scoped synonyms/comments/outgoing edges
    and six native neighbors were inspected. Q-learning and AntNet receive related_match
    relations to the AIO Reinforcement Learning task, supported by their primary definitions
    and explicit discussion; no task/algorithm identity or shared convergence theorem
    is asserted. ACO retains a bounded no-match assessment because instance-specific
    learning relations, generic search language and language-model targets do not
    ground the framework itself. The original ACO source distinguishes strict ACO
    from the broader ant-inspired category.
findings:
- finding_id: antnet-neighbor-eligibility
  issue_key: CultureBotAI-AIMech-AntNet-neighbor-eligibility
  category: consistency
  severity: minor
  status: resolved
  certainty: confirmed
  target_ids:
  - AIMech:AntNet
  field_paths:
  - claims[claim_id=method].statement
  evidence_ids:
  - antnet-source-0
  - finite-conventions
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/AntNet.yaml
    role: maintained
  title: AntNet eligibility is phrased as a soft preference.
  description: The initial draft phrased the eligibility constraint as a soft preference.
    The corrected claim preserves the primary two-case rule; the original review remains
    immutable.
  external_issues:
  - https://github.com/CultureBotAI/AIMech/issues/83
  previous_occurrences:
  - repository: CultureBotAI/AIMech
    review_id: 20261011T134916Z-antnet-neighbor-eligibility
    finding_id: antnet-neighbor-eligibility
  disposition_reason: The maintained mechanism now explicitly restricts selection
    to unvisited neighbors whenever any exist, using all neighbors only when all were
    visited. The restricted-set normalization and zero-queue qualifications remain
    intact. The ledger and append-only history were updated, the final inputs inspected,
    and post-fix required checks passed.
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:QLearning
  - AIMech:AntNet
  - AIMech:AntColonyOptimization
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - qlearning-source-0
  - antnet-source-0
  - antcolonyoptimization-source-0
  rationale: Tabular action-value learning, measured-trip adaptive routing and the
    constructive ant-search framework have distinct supported scopes. Shared learning
    vocabulary and ACO membership do not imply method equivalence or transferable
    guarantees.
limitations:
- Adversarial author self-review only; every record remains DRAFT.
- Only declared text/OCR and visual pages were inspected. No benchmark, author-code
  execution or convergence-proof audit was performed.
- Source presentation and numerical-boundary ambiguities remain explicit. The AntNet
  archive upload year is distinguished from its 1998 publication, and the Q-learning
  guarantee is reported with assumptions rather than independently proved.
- Three additions and 171 pending inspection leads plus other unresolved dispositions
  leave discovery active.
links:
- https://github.com/CultureBotAI/AIMech/issues/83
tags:
- native-concepts
- value-learning
- ant-colony-optimization
- self-review
- discovery-ongoing
```
