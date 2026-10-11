# Scientific self-review of configuration surrogates and evolution

- Review: 20261011T115739Z-configuration-surrogates-and-evolution
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T11:54:41Z
- Finished UTC: 2026-10-11T11:57:39Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain original SMAC, FABOLAS and DEHB with explicit surrogate, fidelity, resource-allocation, version and mapping boundaries. No actionable record defect was found in this scope.

## Scope And Provenance

All fields of the three newly maintained configuration-search records.

Selection: Exact three IDs in the discovery ledger; no sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 6777cf063e21cd2bdb6cd172a847d7b323d6e148.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:SequentialModelBasedAlgorithmConfiguration | data/curated/SequentialModelBasedAlgorithmConfiguration.yaml | maintained | Sequential Model-based Algorithm Configuration |
| AIMech:FABOLAS | data/curated/FABOLAS.yaml | maintained | FABOLAS |
| AIMech:DEHB | data/curated/DEHB.yaml | maintained | DEHB |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:SequentialModelBasedAlgorithmConfiguration, AIMech:FABOLAS, AIMech:DEHB | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 94.57s (0:01:34)<br>Checked 442 record(s); 0 failed.<br>Checked 265 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 63 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 61,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:SequentialModelBasedAlgorithmConfiguration, AIMech:FABOLAS, AIMech:DEHB | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| Finite configuration-search calculations | passed | True | AIMech:SequentialModelBasedAlgorithmConfiguration, AIMech:FABOLAS, AIMech:DEHB | {"smac_cost_aggregation": {"arithmetic": 5.0, "geometric": 3.0000000000000004}, "blocked_comparison": {"incumbent_all": 5.5, "incumbent_common": 10, "challenger_common": 6}, "fabolas_cost_weighting": {"no_overhead": [1.0, 0.3], "overhead10": [0.09090909090909091, 0.15]}, "fidelity_coordinate": {"counts": [4, 16, 64], "normalized_log2": [0.0, 0.5, 1.0]}, "unsigned_loss_basis": {"coefficient": -1, "values": [0, 0.75, 1]}, "dehb_budget_units": {"printed_start": 1.0, "physical_start": 3.0, "printed_terminal": 27, "physical_terminal": 81}, "same_budget_selection": {"target_loss": 1, "trial_loss": 2, "retained": "target"}} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, source conventions and AIO relations

evidence: supported. Targets: AIMech:SequentialModelBasedAlgorithmConfiguration.

The primary scope is the original 2011 SMAC procedure, not every sequential model-based optimizer or every later SMAC software release. It configures a target algorithm over a set or distribution of instances and returns one incumbent configuration; it is not per-instance algorithm selection, a prediction forest by itself, or population-based transfer of trained model weights. Its model-guided proposals distinguish it from ROAR, which shares the intensification procedure but samples configurations at random. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 262 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main checkout, returning 9 lines in each checkout. These were prior candidate leads, source references and neighboring-method mentions, not existing records for these identities. Ten exact AIO CLASS nodes with synonyms and outgoing edges and eight neighboring native mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Initialize with an evaluation of the default configuration, or a random setting when no default is available. Fit a random-forest surrogate using configuration values and, when available, training-instance features. Aggregate each tree’s predictions over instances according to the chosen cost metric, then derive predictive moments across trees. For runtime optimization the paper uses log-transformed responses while preserving the original aggregation objective through inverse transformation at leaves. Rank proposals by expected improvement, using its log-cost formulation, and search for promising settings with multistart one-coordinate local changes plus randomly sampled acquisition candidates. Interleave guided proposals with uniformly sampled configurations. The intensification routine compares a challenger and incumbent on shared instance/seed evaluations, enlarges the challenger’s evaluated subset in doubling batches, rejects it when its empirical cost is worse, and replaces the incumbent when the challenger has matched the available evaluation set and is at least as good. Repeat model fitting and configuration comparisons within the overall configuration budget. Limits: The original method explicitly lacks adaptive capping of individual poor runs. Its adaptive allocation of additional evaluations must not be equated with the censored-runtime handling or other features of later SMAC releases. Surrogate uncertainty and early empirical comparisons do not certify an optimal configuration or generalization to unseen instance distributions. The paper’s asymptotic argument assumes a finite configuration space, consistent cost estimates and unbounded evaluation growth; the displayed experimental procedure caps incumbent evaluations with maxR=2000. These conditions are not an unconditional guarantee for the capped implementation or continuous spaces. Instance features are optional; the result is a single configuration and does not require test-instance feature computation. The reviewed source is an author-hosted manuscript, not a claim that its 15 PDF pages match the publisher’s page layout. No benchmark result or executable implementation was reproduced.

### Identity, definition, mechanism, source conventions and AIO relations

evidence: supported. Targets: AIMech:FABOLAS.

FABOLAS treats dataset size as an environmental evaluation variable while retaining the full dataset as the optimization target. It differs from Gaussian-process regression alone, fixed-fidelity Bayesian optimization, a discrete multi-task optimizer with manually selected task sizes, and Hyperband’s predetermined resource brackets. The paper method and the separately pinned RoBO implementation are recorded as distinct source versions. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 262 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main checkout, returning 9 lines in each checkout. These were prior candidate leads, source references and neighboring-method mentions, not existing records for these identities. Ten exact AIO CLASS nodes with synonyms and outgoing edges and eight neighboring native mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Model loss and computational cost as functions of configuration and dataset fraction, using Gaussian-process surrogates with a kernel over configuration coordinates and a finite-rank basis over size. Begin with evaluations of configurations on small subsets. Select the next configuration/size pair using an entropy-search acquisition focused on the minimizer at full dataset size; the paper divides its information criterion by predicted evaluation cost plus optimization overhead. Evaluate the selected pair, observe loss and cost, and update the models. Select the incumbent among configurations already evaluated by projecting their predicted loss to the full dataset, rather than requiring each candidate to have been evaluated there. The paper integrates surrogate hyperparameters using MCMC and describes DIRECT/CMA-ES acquisition optimization; the inspected code has separate implementation choices. In the inspected RoBO revision, dataset counts are mapped to a normalized log2 coordinate between the selected minimum and maximum; proposed coordinates are transformed back and rounded to integer counts. Quadratic loss and linear cost basis functions operate on that transformed coordinate, while both observed objective values and costs are logged. The outer function uses a Latin-hypercube initial design and RandomSampling acquisition maximizer. Its marginalized acquisition update passes no overhead keyword, so the per-unit-cost estimator sets overhead to zero and divides by the exponentiated predicted log-cost mean. These are static observations of this revision, not claims of equality with the original experiments or executable compatibility. Limits: Extrapolation depends on the adequacy of the loss-versus-size and cost models. Small subsets need not preserve the ranking at full size, and the returned projected incumbent need not have a confirming full-data evaluation or optimal test performance. The paper’s loss basis (1,(1-s)^2) allows a monotonic latent trend at fixed configuration but does not by itself force that trend to decrease when coefficient signs are unconstrained. Its polynomial-cost interpretation also depends on the size coordinate: log-cost affine in raw relative size is exponential in that coordinate; the pinned code instead uses normalized log dataset counts. The pinned code logs both objective and cost, applies Latin-hypercube initialization and a RandomSampling acquisition optimizer, and leaves the acquisition overhead at zero through the inspected call chain. Those choices are not silently attributed to the paper’s algorithm. Positive objective/cost values and compatible parameter settings are required by that source; static inspection is not a runtime result. No universal speedup, exact information-gain computation or independent calibration result is asserted. The full entropy-search implementation and the paper’s supplementary experiments were not audited.

### Identity, definition, mechanism, source conventions and AIO relations

evidence: supported. Targets: AIMech:DEHB.

DEHB is the combined resource-allocation and differential-evolution method, distinct from generic genetic algorithms, differential evolution alone, random-proposal Hyperband, KDE-guided BOHB and ASHA’s asynchronous within-stage promotions. Budget-specific populations contain configuration vectors, not a population of trained checkpoints whose weights are copied between configurations. The proceedings paper and the versioned appendix are distinguished explicitly. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 262 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in both worktree and main checkout, returning 9 lines in each checkout. These were prior candidate leads, source references and neighboring-method mentions, not existing records for these identities. Ten exact AIO CLASS nodes with synonyms and outgoing edges and eight neighboring native mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Maintain a differential-evolution subpopulation for each Hyperband resource level, sized according to the maximum number of evaluations assigned to that level. Iterate through the prescribed halving brackets. For a bracket’s starting level use evolution within its own population; for higher levels form a parent pool from promising lower-level configurations and use it for difference-vector mutation, followed by crossover with a target in the current level’s population. Evaluate the proposed configuration at the current level and retain it only according to a same-level fitness comparison with the target. Supplement an undersized mutation pool from a global pool of configurations. The initialization cycle includes direct lower-to-higher promotions before the general evolutionary transfer pattern. For mixed search spaces, the appendix keeps continuous population coordinates in a unit hypercube and maps copies to numerical or binned ordinal/categorical settings for evaluation. Its parallel design keeps each halving stage synchronized while allowing brackets to overlap and applying completed differential-evolution updates immediately. Limits: The source’s initialization prose and pseudocode use bracket and iteration terminology inconsistently. Algorithm3’s bracket_counter==0 condition spans an outer cycle and applies direct promotion only for i&gt;0. The record describes the common mechanism without treating every printed initialization statement as byte-equivalent executable steps. Appendix Algorithm2 prints b0=(bmax/bmin)*eta^(-s), which gives normalized rather than absolute budgets when bmin differs from1. Its return order for counts and budgets is reversed at the Algorithm3 call site. These discrepancies are retained as source qualifications; no author-issued erratum or exact executable schedule is claimed. The appendix updates its incumbent after evaluations without an explicit full-budget restriction. The record therefore does not promise that the returned best observed configuration has been verified at maximum resource. Greedy same-budget replacement limits harmful transfers but is not a proof of global optimality or universal robustness. Continuous encodings impose numerical neighborhoods on categorical choices, and low-fidelity information can be misleading. Parallel completion order can affect shared populations. No benchmark speedup, constant total runtime or author-code execution is claimed.

### Original configuration algorithm, component model and evaluation comparison

consistency: supported. Targets: AIMech:SequentialModelBasedAlgorithmConfiguration.

Retain original SMAC with source-specific scope and a component relation to RandomForest.

A random-forest surrogate and log-cost expected improvement guide proposals, interleaved with uniform configurations. Blocked instance/seed comparisons and expanding evaluation subsets differ from independent random search. Original SMAC explicitly lacks adaptive capping; finite maxR and empirical comparisons do not inherit unconditional asymptotic guarantees. A single configured target algorithm is distinct from per-instance selection or its surrogate forest.

### Dataset-size extrapolation, cost weighting and implementation versions

consistency: supported. Targets: AIMech:FABOLAS.

Retain FABOLAS with full-dataset target and explicit paper/code distinctions.

The paper selects informative configuration/size evaluations and returns a projected incumbent among observed configurations. The pinned code uses normalized log dataset counts, logs objective and cost, and applies Latin-hypercube initialization and a RandomSampling acquisition maximizer. Its update chain omits overhead and therefore uses zero, unlike the paper objective. A fixed-direction basis is not a guaranteed decreasing trend. These are static source observations, not evidence of executable compatibility or original-experiment identity.

### Evolutionary transfer, resource units and parallel stage boundaries

consistency: supported. Targets: AIMech:DEHB.

Retain DEHB with budget-specific populations and synchronous halving stages.

Parent pools transfer low-budget configuration information into higher-budget mutation, while same-budget selection evaluates proposed changes. Brackets may overlap and population updates are immediate, but the versioned appendix explicitly waits for a lower stage before advancing. Printed budget units, return-order and initialization terminology require qualifications; the record does not claim literal pseudocode execution or a full-budget incumbent guarantee.

### Component relations versus algorithm identity

grounding: supported. Targets: AIMech:SequentialModelBasedAlgorithmConfiguration, AIMech:FABOLAS, AIMech:DEHB.

Retain three distinct native concepts with related AIO mappings.

SMAC relates to AIO RandomForest through its surrogate component, not as an equivalent model or subclass. FABOLAS and DEHB relate to TrainingStrategy through explicit hyperparameter search and resource allocation; its preprocessing-oriented pinned definition does not justify an is-a link. BayesianNetwork, EvolutionaryLLM, broad learning tasks and prediction ensembles do not identify these full search algorithms. GPR is a surrogate component, and generic genetic algorithms do not identify DEHB’s budget-specific transfer and scheduling.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:SequentialModelBasedAlgorithmConfiguration, AIMech:FABOLAS, AIMech:DEHB. Random-forest guided algorithm configuration, dataset-size extrapolating Bayesian optimization and evolutionary multi-fidelity search have distinct proposal and evaluation mechanisms. Shared surrogate or Hyperband components do not identify the complete algorithms.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T115419Z-configuration-surrogates-and-evolution.json | supports | Compared all 442 pinned AIO labels/scoped synonyms and 262 preceding maintained IDs/names/aliases, including candidate-internal normalized uniqueness. No matching identity was found. Full-checkout fixed-string searches included ignored and hidden files and returned nine lines in each checkout, all prior leads and source-context mentions. Ten exact AIO CLASS nodes with synonyms/outgoing edges and eight native neighboring mechanisms were assessed; unchanged nodes and neighbors already inspected in preceding rounds were reused, with RandomForest, Gaussian-process regression and genetic-algorithm context inspected additionally. Absence is bounded to this snapshot and semantic neighborhood. |
| mapping | sources/aio/aio.json; Ten exact CLASS nodes and their scoped synonyms/outgoing edges in source_analysis.aio_mapping_inspection | supports | SMAC relates to AIO RandomForest through its surrogate component, not as an equivalent model or subclass. FABOLAS and DEHB relate to TrainingStrategy through explicit hyperparameter search and resource allocation; its preprocessing-oriented pinned definition does not justify an is-a link. BayesianNetwork, EvolutionaryLLM, broad learning tasks and prediction ensembles do not identify these full search algorithms. GPR is a surrogate component, and generic genetic algorithms do not identify DEHB’s budget-specific transfer and scheduling. |
| neighbors | research/discovery/20261011T115419Z-configuration-surrogates-and-evolution.json; source_analysis.aio_mapping_inspection.native_neighbors | supports | Read or reuse unchanged inspected Hyperband, BOHB, random search, TPE, PBT, ASHA, Gaussian-process regression and genetic-algorithm mechanisms. Shared surrogate or evolutionary components do not identify the complete configuration procedures. |
| finite-conventions | research/discovery/configuration-surrogate-boundaries.py; calculate(): cost aggregation, blocked comparisons, acquisition overhead, log-size coordinates, trend direction, budget units and same-level selection | supports | Original arithmetic illustrates cost aggregation, blocked comparisons, acquisition overhead, log-size coordinates, unconstrained trend direction, DEHB budget units and same-budget selection. No author code or model was executed. |
| sequentialmodelbasedalgorithmconfiguration-source-0 | https://www.cs.ubc.ca/labs/algorithms/Projects/SMAC/papers/11-LION5-SMAC.pdf; Sections2–4.3, PDF pp.3–9, especially Framework1, Procedure2 and Equation1; original scope and limitations in Sections1 and6, PDF pp.1–3 and14 | supports | Sequential Model-Based Optimization for General Algorithm Configuration. LION 5, 2011; author-hosted 15-page manuscript. Actual PDF and static-code reading scopes are declared in the ledger. Source rendering alone does not attest inspection. |
| fabolas-source-0 | https://proceedings.mlr.press/v54/klein17a/klein17a.pdf; Sections2–3.4, PDF pp.2–5, especially Section3.1 kernels, Equation7 and Algorithm1 on PDFp.4, and incumbent/initialization details on PDFp.5 | supports | Fast Bayesian Optimization of Machine Learning Hyperparameters on Large Datasets. AISTATS 2017, PMLR 54:528–536; nine-page proceedings PDF. Actual PDF and static-code reading scopes are declared in the ledger. Source rendering alone does not attest inspection. |
| fabolas-source-1 | https://raw.githubusercontent.com/automl/RoBO/91366b12a1a3deb8e80dd08599e0eaf4df28adc1/robo/fmin/fabolas.py; fabolas(): transformations lines21–28, kernels/bases lines105–173, initialization and acquisition lines180–215, model update and proposal lines234–284 | supports | RoBO author implementation: robo/fmin/fabolas.py. automl/RoBO commit 91366b12a1a3deb8e80dd08599e0eaf4df28adc1. Actual PDF and static-code reading scopes are declared in the ledger. Source rendering alone does not attest inspection. |
| fabolas-source-2 | https://raw.githubusercontent.com/automl/RoBO/91366b12a1a3deb8e80dd08599e0eaf4df28adc1/robo/models/fabolas_gp.py; FabolasGPMCMC.train and FabolasGP.normalize/train/predict, lines32–99 and122–139 | supports | RoBO author implementation: robo/models/fabolas_gp.py. automl/RoBO commit 91366b12a1a3deb8e80dd08599e0eaf4df28adc1. Actual PDF and static-code reading scopes are declared in the ledger. Source rendering alone does not attest inspection. |
| fabolas-source-3 | https://raw.githubusercontent.com/automl/RoBO/91366b12a1a3deb8e80dd08599e0eaf4df28adc1/robo/acquisition_functions/information_gain_per_unit_cost.py; InformationGainPerUnitCost.update and compute, lines59–107 | supports | RoBO author implementation: robo/acquisition_functions/information_gain_per_unit_cost.py. automl/RoBO commit 91366b12a1a3deb8e80dd08599e0eaf4df28adc1. Actual PDF and static-code reading scopes are declared in the ledger. Source rendering alone does not attest inspection. |
| fabolas-source-4 | https://raw.githubusercontent.com/automl/RoBO/91366b12a1a3deb8e80dd08599e0eaf4df28adc1/robo/acquisition_functions/marginalization.py; MarginalizationGPMCMC.update, lines49–90 | supports | RoBO author implementation: robo/acquisition_functions/marginalization.py. automl/RoBO commit 91366b12a1a3deb8e80dd08599e0eaf4df28adc1. Actual PDF and static-code reading scopes are declared in the ledger. Source rendering alone does not attest inspection. |
| dehb-source-0 | https://www.ijcai.org/proceedings/2021/0296.pdf; Sections3–4.3, PDF pp.2–4 (printed2148–2150), especially Figures1–3 and the modified halving procedure | supports | DEHB: Evolutionary Hyberband for Scalable, Robust and Efficient Hyperparameter Optimization. IJCAI 2021, pp.2147–2153; seven-page proceedings PDF; title retains published Hyberband spelling. Actual PDF and static-code reading scopes are declared in the ledger. Source rendering alone does not attest inspection. |
| dehb-source-1 | https://arxiv.org/pdf/2105.09821v2; AppendicesA–C, PDF pp.9–12, especially Algorithm2 on p.10, Algorithm3 and SectionsC.2–C.3 on pp.11–12; title/version on p.1 | supports | DEHB: Evolutionary Hyperband for Scalable, Robust and Efficient Hyperparameter Optimization. arXiv:2105.09821v2, 21 October 2021; 19-page manuscript including appendices. Actual PDF and static-code reading scopes are declared in the ledger. Source rendering alone does not attest inspection. |

## Limits And Additional Notes

- Adversarial author self-review only; every record remains DRAFT.
- Only declared PDF pages and four static RoBO files were inspected. No training, benchmark, complete proof audit or author-code execution was performed.
- Source-version discrepancies and source-pseudocode ambiguities remain explicit. The failed DEHB supplementary link was replaced by an identified arXiv version; no author-issued erratum is claimed.
- Three additions and a nonempty inherited/new frontier leave discovery active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T115739Z-configuration-surrogates-and-evolution
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of configuration surrogates and evolution
started_at: '2026-10-11T11:54:41Z'
finished_at: '2026-10-11T11:57:39Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed all three records
    against the declared primary methods, rendered pages, four pinned RoBO source
    files, ten exact AIO nodes, eight native neighbors and original finite arithmetic.
    This is not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain original SMAC, FABOLAS and DEHB with explicit surrogate, fidelity,
  resource-allocation, version and mapping boundaries. No actionable record defect
  was found in this scope.
source:
  git_revision: 6777cf063e21cd2bdb6cd172a847d7b323d6e148
  state: working_tree
  inputs:
  - path: data/aio/BayesianNetwork.yaml
    sha256: f195dcc9b03c06b65c8c95c246fc4a7f34d41de74afc226dfbbc3b223e7f8769
    role: context
  - path: data/aio/EnsembleLearning.yaml
    sha256: cf9435e5a799d84072222190c2d681c53b22bf9e7094891405008ebe398a39ed
    role: context
  - path: data/aio/EvolutionaryLLM.yaml
    sha256: d3db6adea3d8d58096c9fb5abef67273489ee719ab900b2d4adbb129e4f7362f
    role: context
  - path: data/aio/MachineLearningTask.yaml
    sha256: 508870ec8844fc3b4cb76e7c074d655694e07c98bf741e7bba195f27dcf8df52
    role: context
  - path: data/aio/Preprocessing.yaml
    sha256: 2c4a30f4f829a757be1feabf78d15780eedf93681a62eede3e76b2304f21bb7a
    role: context
  - path: data/aio/RandomForest.yaml
    sha256: cfdce4625131a8da239adf1b3957fadbc5433ddc8fc4ac8a3be5fe9018ce66ab
    role: context
  - path: data/aio/ReinforcementLearning.yaml
    sha256: dc8ad2a5e092e6ea34023f73574b3d436d895635690d9ef92202c2afa893bb9e
    role: context
  - path: data/aio/ReinforcementLearningLLM.yaml
    sha256: e386376b9b1a9c78349d66e8609a655e273620d8bc607978c728ac3b7ce3808a
    role: context
  - path: data/aio/SupervisedLearning.yaml
    sha256: 472f033f91a14c8727e525ddd30f82fcaf16a2514fa8f062667fb94fc9c9b718
    role: context
  - path: data/aio/TrainingStrategy.yaml
    sha256: 5b67f81f3735b07709b76437ee8f4438150886c34582e4f47c76cfd33a958daa
    role: context
  - path: data/curated/AsynchronousSuccessiveHalving.yaml
    sha256: 16e68a69439a4ad7d06ad34483d4db288163810967516776edac5a6082d8a725
    role: context
  - path: data/curated/BOHB.yaml
    sha256: bb965b104107d30a9d74f4ac4eaa0aa72023cdf676afb53528d3a1b41bebf291
    role: context
  - path: data/curated/DEHB.yaml
    sha256: c0c18d5afdd9aa26db73d0c84e4e0d2a623e242a0fb18bd42ee5c4588473d412
    role: target
  - path: data/curated/FABOLAS.yaml
    sha256: 800fb7787896a6cd3f0c2ced22fd70543a79d3a59502ff2c52cf4ae4f8ba0cb9
    role: target
  - path: data/curated/GaussianProcessRegression.yaml
    sha256: d83d0de4a152e7db689636928f41eb5d3663281285585d835f2a5535403d6a0d
    role: context
  - path: data/curated/GeneticAlgorithm.yaml
    sha256: d40bf1a03e29a3ca6bf88f6553f18c6b1559baf56da6a21d63b54163f4752ceb
    role: context
  - path: data/curated/Hyperband.yaml
    sha256: ed8dae09ccd45becb03f2e0ad41aa4c2898ecafc999e6b2ba9637c7d8b311e56
    role: context
  - path: data/curated/PopulationBasedTraining.yaml
    sha256: 4a0fff56bd5ccb2d2b21cea0c533bd0fa83e1601a035b1c0b5dbf796e7e81261
    role: context
  - path: data/curated/RandomSearchHyperparameterOptimization.yaml
    sha256: 24dde2b9d19169c383b403742ea355727c2f167ae8aa21970fbda34e832c89fd
    role: context
  - path: data/curated/SequentialModelBasedAlgorithmConfiguration.yaml
    sha256: 578ea6762a48bc56063d3e5907bb038b728112560a3baee7811d4f9b50354357
    role: target
  - path: data/curated/TreeStructuredParzenEstimator.yaml
    sha256: bdd8130958b93502ecd3bf0cd73f411dfb4aecb5d6d2ab2e01454dee9bae2737
    role: context
  - path: research/discovery/20261011T115419Z-configuration-surrogates-and-evolution.json
    sha256: 6ef6b8e4fe4543b8ad94f7836172ca96499b35668c9fd5bb8bbcd6197aa93f90
    role: context
  - path: research/discovery/configuration-surrogate-boundaries.py
    sha256: 68cb0f501a9753076b44394ec267fa123d48d2a1b7e1b7bce462aa1865a294ba
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
- target_id: AIMech:SequentialModelBasedAlgorithmConfiguration
  path: data/curated/SequentialModelBasedAlgorithmConfiguration.yaml
  label: Sequential Model-based Algorithm Configuration
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SequentialModelBasedAlgorithmConfiguration.yaml
    role: maintained
- target_id: AIMech:FABOLAS
  path: data/curated/FABOLAS.yaml
  label: FABOLAS
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/FABOLAS.yaml
    role: maintained
- target_id: AIMech:DEHB
  path: data/curated/DEHB.yaml
  label: DEHB
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DEHB.yaml
    role: maintained
scope:
  description: All fields of the three newly maintained configuration-search records.
  selection: Exact three IDs in the discovery ledger; no sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:SequentialModelBasedAlgorithmConfiguration
  - AIMech:FABOLAS
  - AIMech:DEHB
  exclusions:
  - target: Older records and unselected candidates
    reason: Neighbors were inspected for boundaries, not a complete new review of
      the earlier corpus.
  - target: Unread pages, proofs, outcomes and implementations
    reason: Only declared primary-source pages and four pinned source files were inspected.
      No author code or model was executed.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:SequentialModelBasedAlgorithmConfiguration
  - AIMech:FABOLAS
  - AIMech:DEHB
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 94.57s (0:01:34)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 265 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 63 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 61,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:SequentialModelBasedAlgorithmConfiguration
  - AIMech:FABOLAS
  - AIMech:DEHB
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
- check_id: finite-arithmetic
  name: Finite configuration-search calculations
  command: python3 research/discovery/configuration-surrogate-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:SequentialModelBasedAlgorithmConfiguration
  - AIMech:FABOLAS
  - AIMech:DEHB
  exit_code: 0
  expected_exit_code: 0
  summary: '{"smac_cost_aggregation": {"arithmetic": 5.0, "geometric": 3.0000000000000004},
    "blocked_comparison": {"incumbent_all": 5.5, "incumbent_common": 10, "challenger_common":
    6}, "fabolas_cost_weighting": {"no_overhead": [1.0, 0.3], "overhead10": [0.09090909090909091,
    0.15]}, "fidelity_coordinate": {"counts": [4, 16, 64], "normalized_log2": [0.0,
    0.5, 1.0]}, "unsigned_loss_basis": {"coefficient": -1, "values": [0, 0.75, 1]},
    "dehb_budget_units": {"printed_start": 1.0, "physical_start": 3.0, "printed_terminal":
    27, "physical_terminal": 81}, "same_budget_selection": {"target_loss": 1, "trial_loss":
    2, "retained": "target"}}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T115419Z-configuration-surrogates-and-evolution.json
  accessed_at: '2026-10-11T11:54:41Z'
  support: supports
  summary: Compared all 442 pinned AIO labels/scoped synonyms and 262 preceding maintained
    IDs/names/aliases, including candidate-internal normalized uniqueness. No matching
    identity was found. Full-checkout fixed-string searches included ignored and hidden
    files and returned nine lines in each checkout, all prior leads and source-context
    mentions. Ten exact AIO CLASS nodes with synonyms/outgoing edges and eight native
    neighboring mechanisms were assessed; unchanged nodes and neighbors already inspected
    in preceding rounds were reused, with RandomForest, Gaussian-process regression
    and genetic-algorithm context inspected additionally. Absence is bounded to this
    snapshot and semantic neighborhood.
  search_scope: All 442 pinned AIO labels/scoped synonyms and 262 preceding maintained
    IDs/names/aliases; full checkouts including ignored/hidden files; candidate-internal
    normalized uniqueness.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Ten exact CLASS nodes and their scoped synonyms/outgoing edges in source_analysis.aio_mapping_inspection
  accessed_at: '2026-10-11T11:54:41Z'
  support: supports
  summary: SMAC relates to AIO RandomForest through its surrogate component, not as
    an equivalent model or subclass. FABOLAS and DEHB relate to TrainingStrategy through
    explicit hyperparameter search and resource allocation; its preprocessing-oriented
    pinned definition does not justify an is-a link. BayesianNetwork, EvolutionaryLLM,
    broad learning tasks and prediction ensembles do not identify these full search
    algorithms. GPR is a surrogate component, and generic genetic algorithms do not
    identify DEHB’s budget-specific transfer and scheduling.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T115419Z-configuration-surrogates-and-evolution.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors
  accessed_at: '2026-10-11T11:54:41Z'
  support: supports
  summary: Read or reuse unchanged inspected Hyperband, BOHB, random search, TPE,
    PBT, ASHA, Gaussian-process regression and genetic-algorithm mechanisms. Shared
    surrogate or evolutionary components do not identify the complete configuration
    procedures.
- evidence_id: finite-conventions
  kind: record_content
  reference: research/discovery/configuration-surrogate-boundaries.py
  locator: 'calculate(): cost aggregation, blocked comparisons, acquisition overhead,
    log-size coordinates, trend direction, budget units and same-level selection'
  accessed_at: '2026-10-11T11:54:41Z'
  snapshot_sha256: 68cb0f501a9753076b44394ec267fa123d48d2a1b7e1b7bce462aa1865a294ba
  support: supports
  summary: Original arithmetic illustrates cost aggregation, blocked comparisons,
    acquisition overhead, log-size coordinates, unconstrained trend direction, DEHB
    budget units and same-budget selection. No author code or model was executed.
- evidence_id: sequentialmodelbasedalgorithmconfiguration-source-0
  kind: primary_source
  reference: https://www.cs.ubc.ca/labs/algorithms/Projects/SMAC/papers/11-LION5-SMAC.pdf
  locator: Sections2–4.3, PDF pp.3–9, especially Framework1, Procedure2 and Equation1;
    original scope and limitations in Sections1 and6, PDF pp.1–3 and14
  accessed_at: '2026-10-11T11:45:03Z'
  snapshot_sha256: aecf80aba31329965bbfcb75c6d8ad2f19da51b2124a920b9f4af3574a9fcdcb
  support: supports
  summary: Sequential Model-Based Optimization for General Algorithm Configuration.
    LION 5, 2011; author-hosted 15-page manuscript. Actual PDF and static-code reading
    scopes are declared in the ledger. Source rendering alone does not attest inspection.
- evidence_id: fabolas-source-0
  kind: primary_source
  reference: https://proceedings.mlr.press/v54/klein17a/klein17a.pdf
  locator: Sections2–3.4, PDF pp.2–5, especially Section3.1 kernels, Equation7 and
    Algorithm1 on PDFp.4, and incumbent/initialization details on PDFp.5
  accessed_at: '2026-10-11T11:45:03Z'
  snapshot_sha256: c1369156837a4e64ae81285d3fc9a4b9c8f237678e88493cf8fae0210498f08c
  support: supports
  summary: Fast Bayesian Optimization of Machine Learning Hyperparameters on Large
    Datasets. AISTATS 2017, PMLR 54:528–536; nine-page proceedings PDF. Actual PDF
    and static-code reading scopes are declared in the ledger. Source rendering alone
    does not attest inspection.
- evidence_id: fabolas-source-1
  kind: primary_source
  reference: https://raw.githubusercontent.com/automl/RoBO/91366b12a1a3deb8e80dd08599e0eaf4df28adc1/robo/fmin/fabolas.py
  locator: 'fabolas(): transformations lines21–28, kernels/bases lines105–173, initialization
    and acquisition lines180–215, model update and proposal lines234–284'
  accessed_at: '2026-10-11T11:48:27Z'
  snapshot_sha256: 2f6d006f53c27f03329c3e8fa1cca66e3013687e9f8f6a460dfa5eaf6f00783f
  support: supports
  summary: 'RoBO author implementation: robo/fmin/fabolas.py. automl/RoBO commit 91366b12a1a3deb8e80dd08599e0eaf4df28adc1.
    Actual PDF and static-code reading scopes are declared in the ledger. Source rendering
    alone does not attest inspection.'
- evidence_id: fabolas-source-2
  kind: primary_source
  reference: https://raw.githubusercontent.com/automl/RoBO/91366b12a1a3deb8e80dd08599e0eaf4df28adc1/robo/models/fabolas_gp.py
  locator: FabolasGPMCMC.train and FabolasGP.normalize/train/predict, lines32–99 and122–139
  accessed_at: '2026-10-11T11:48:27Z'
  snapshot_sha256: 6c5f0dde17f527bbe2676e14740bd8990b6763f8c8f259e52448cfdb6d057d1a
  support: supports
  summary: 'RoBO author implementation: robo/models/fabolas_gp.py. automl/RoBO commit
    91366b12a1a3deb8e80dd08599e0eaf4df28adc1. Actual PDF and static-code reading scopes
    are declared in the ledger. Source rendering alone does not attest inspection.'
- evidence_id: fabolas-source-3
  kind: primary_source
  reference: https://raw.githubusercontent.com/automl/RoBO/91366b12a1a3deb8e80dd08599e0eaf4df28adc1/robo/acquisition_functions/information_gain_per_unit_cost.py
  locator: InformationGainPerUnitCost.update and compute, lines59–107
  accessed_at: '2026-10-11T11:48:27Z'
  snapshot_sha256: fb05bd07ffb480d2d82bf695097d815c6768bbd7fe2181281e4159d9fb16aeb9
  support: supports
  summary: 'RoBO author implementation: robo/acquisition_functions/information_gain_per_unit_cost.py.
    automl/RoBO commit 91366b12a1a3deb8e80dd08599e0eaf4df28adc1. Actual PDF and static-code
    reading scopes are declared in the ledger. Source rendering alone does not attest
    inspection.'
- evidence_id: fabolas-source-4
  kind: primary_source
  reference: https://raw.githubusercontent.com/automl/RoBO/91366b12a1a3deb8e80dd08599e0eaf4df28adc1/robo/acquisition_functions/marginalization.py
  locator: MarginalizationGPMCMC.update, lines49–90
  accessed_at: '2026-10-11T11:49:31Z'
  snapshot_sha256: 4d7ce68913dbfe867cdf4a6edfa0262e96114e244688ffa71e54c6d898f70b4f
  support: supports
  summary: 'RoBO author implementation: robo/acquisition_functions/marginalization.py.
    automl/RoBO commit 91366b12a1a3deb8e80dd08599e0eaf4df28adc1. Actual PDF and static-code
    reading scopes are declared in the ledger. Source rendering alone does not attest
    inspection.'
- evidence_id: dehb-source-0
  kind: primary_source
  reference: https://www.ijcai.org/proceedings/2021/0296.pdf
  locator: Sections3–4.3, PDF pp.2–4 (printed2148–2150), especially Figures1–3 and
    the modified halving procedure
  accessed_at: '2026-10-11T11:45:03Z'
  snapshot_sha256: 48ff58a4bdc3d3ba1613472f0b984fa1f24c572e1da960366f63967c77f42234
  support: supports
  summary: 'DEHB: Evolutionary Hyberband for Scalable, Robust and Efficient Hyperparameter
    Optimization. IJCAI 2021, pp.2147–2153; seven-page proceedings PDF; title retains
    published Hyberband spelling. Actual PDF and static-code reading scopes are declared
    in the ledger. Source rendering alone does not attest inspection.'
- evidence_id: dehb-source-1
  kind: primary_source
  reference: https://arxiv.org/pdf/2105.09821v2
  locator: AppendicesA–C, PDF pp.9–12, especially Algorithm2 on p.10, Algorithm3 and
    SectionsC.2–C.3 on pp.11–12; title/version on p.1
  accessed_at: '2026-10-11T11:47:53Z'
  snapshot_sha256: 90b2d08b7234c591b1e74a7b91a5d8c9ce695669e2b4f5fd3b5482b3c7f30fbd
  support: supports
  summary: 'DEHB: Evolutionary Hyperband for Scalable, Robust and Efficient Hyperparameter
    Optimization. arXiv:2105.09821v2, 21 October 2021; 19-page manuscript including
    appendices. Actual PDF and static-code reading scopes are declared in the ledger.
    Source rendering alone does not attest inspection.'
assessments:
- assessment_id: sequentialmodelbasedalgorithmconfiguration
  area: evidence
  topic: Identity, definition, mechanism, source conventions and AIO relations
  outcome: supported
  target_ids:
  - AIMech:SequentialModelBasedAlgorithmConfiguration
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - sequentialmodelbasedalgorithmconfiguration-source-0
  summary: The primary scope is the original 2011 SMAC procedure, not every sequential
    model-based optimizer or every later SMAC software release. It configures a target
    algorithm over a set or distribution of instances and returns one incumbent configuration;
    it is not per-instance algorithm selection, a prediction forest by itself, or
    population-based transfer of trained model weights. Its model-guided proposals
    distinguish it from ROAR, which shares the intensification procedure but samples
    configurations at random. No normalized identity match was found across all 442
    pinned AIO labels/scoped synonyms and 262 preceding native IDs/names/aliases.
    Full-checkout fixed-string searches included ignored and hidden files in both
    worktree and main checkout, returning 9 lines in each checkout. These were prior
    candidate leads, source references and neighboring-method mentions, not existing
    records for these identities. Ten exact AIO CLASS nodes with synonyms and outgoing
    edges and eight neighboring native mechanisms were inspected. Absence is bounded
    to this snapshot and semantic neighborhood.
  details: 'Initialize with an evaluation of the default configuration, or a random
    setting when no default is available. Fit a random-forest surrogate using configuration
    values and, when available, training-instance features. Aggregate each tree’s
    predictions over instances according to the chosen cost metric, then derive predictive
    moments across trees. For runtime optimization the paper uses log-transformed
    responses while preserving the original aggregation objective through inverse
    transformation at leaves. Rank proposals by expected improvement, using its log-cost
    formulation, and search for promising settings with multistart one-coordinate
    local changes plus randomly sampled acquisition candidates. Interleave guided
    proposals with uniformly sampled configurations. The intensification routine compares
    a challenger and incumbent on shared instance/seed evaluations, enlarges the challenger’s
    evaluated subset in doubling batches, rejects it when its empirical cost is worse,
    and replaces the incumbent when the challenger has matched the available evaluation
    set and is at least as good. Repeat model fitting and configuration comparisons
    within the overall configuration budget. Limits: The original method explicitly
    lacks adaptive capping of individual poor runs. Its adaptive allocation of additional
    evaluations must not be equated with the censored-runtime handling or other features
    of later SMAC releases. Surrogate uncertainty and early empirical comparisons
    do not certify an optimal configuration or generalization to unseen instance distributions.
    The paper’s asymptotic argument assumes a finite configuration space, consistent
    cost estimates and unbounded evaluation growth; the displayed experimental procedure
    caps incumbent evaluations with maxR=2000. These conditions are not an unconditional
    guarantee for the capped implementation or continuous spaces. Instance features
    are optional; the result is a single configuration and does not require test-instance
    feature computation. The reviewed source is an author-hosted manuscript, not a
    claim that its 15 PDF pages match the publisher’s page layout. No benchmark result
    or executable implementation was reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A defined algorithm-configuration or hyperparameter-search procedure
      with explicit surrogate, allocation and population scope.
    evidence_ids:
    - sequentialmodelbasedalgorithmconfiguration-source-0
  - name: aio-relations
    value: 'related_match: AIO:RandomForest'
    definition: The original SMAC algorithm uses a random-forest regression surrogate
      as a component. The full proposal-and-comparison procedure is neither identical
      to that ensemble model nor a subclass of it; this is a component-based conceptual
      relation.
    evidence_ids:
    - mapping
- assessment_id: fabolas
  area: evidence
  topic: Identity, definition, mechanism, source conventions and AIO relations
  outcome: supported
  target_ids:
  - AIMech:FABOLAS
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - fabolas-source-0
  - fabolas-source-1
  - fabolas-source-2
  - fabolas-source-3
  - fabolas-source-4
  summary: FABOLAS treats dataset size as an environmental evaluation variable while
    retaining the full dataset as the optimization target. It differs from Gaussian-process
    regression alone, fixed-fidelity Bayesian optimization, a discrete multi-task
    optimizer with manually selected task sizes, and Hyperband’s predetermined resource
    brackets. The paper method and the separately pinned RoBO implementation are recorded
    as distinct source versions. No normalized identity match was found across all
    442 pinned AIO labels/scoped synonyms and 262 preceding native IDs/names/aliases.
    Full-checkout fixed-string searches included ignored and hidden files in both
    worktree and main checkout, returning 9 lines in each checkout. These were prior
    candidate leads, source references and neighboring-method mentions, not existing
    records for these identities. Ten exact AIO CLASS nodes with synonyms and outgoing
    edges and eight neighboring native mechanisms were inspected. Absence is bounded
    to this snapshot and semantic neighborhood.
  details: 'Model loss and computational cost as functions of configuration and dataset
    fraction, using Gaussian-process surrogates with a kernel over configuration coordinates
    and a finite-rank basis over size. Begin with evaluations of configurations on
    small subsets. Select the next configuration/size pair using an entropy-search
    acquisition focused on the minimizer at full dataset size; the paper divides its
    information criterion by predicted evaluation cost plus optimization overhead.
    Evaluate the selected pair, observe loss and cost, and update the models. Select
    the incumbent among configurations already evaluated by projecting their predicted
    loss to the full dataset, rather than requiring each candidate to have been evaluated
    there. The paper integrates surrogate hyperparameters using MCMC and describes
    DIRECT/CMA-ES acquisition optimization; the inspected code has separate implementation
    choices. In the inspected RoBO revision, dataset counts are mapped to a normalized
    log2 coordinate between the selected minimum and maximum; proposed coordinates
    are transformed back and rounded to integer counts. Quadratic loss and linear
    cost basis functions operate on that transformed coordinate, while both observed
    objective values and costs are logged. The outer function uses a Latin-hypercube
    initial design and RandomSampling acquisition maximizer. Its marginalized acquisition
    update passes no overhead keyword, so the per-unit-cost estimator sets overhead
    to zero and divides by the exponentiated predicted log-cost mean. These are static
    observations of this revision, not claims of equality with the original experiments
    or executable compatibility. Limits: Extrapolation depends on the adequacy of
    the loss-versus-size and cost models. Small subsets need not preserve the ranking
    at full size, and the returned projected incumbent need not have a confirming
    full-data evaluation or optimal test performance. The paper’s loss basis (1,(1-s)^2)
    allows a monotonic latent trend at fixed configuration but does not by itself
    force that trend to decrease when coefficient signs are unconstrained. Its polynomial-cost
    interpretation also depends on the size coordinate: log-cost affine in raw relative
    size is exponential in that coordinate; the pinned code instead uses normalized
    log dataset counts. The pinned code logs both objective and cost, applies Latin-hypercube
    initialization and a RandomSampling acquisition optimizer, and leaves the acquisition
    overhead at zero through the inspected call chain. Those choices are not silently
    attributed to the paper’s algorithm. Positive objective/cost values and compatible
    parameter settings are required by that source; static inspection is not a runtime
    result. No universal speedup, exact information-gain computation or independent
    calibration result is asserted. The full entropy-search implementation and the
    paper’s supplementary experiments were not audited.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A defined algorithm-configuration or hyperparameter-search procedure
      with explicit surrogate, allocation and population scope.
    evidence_ids:
    - fabolas-source-0
    - fabolas-source-1
    - fabolas-source-2
    - fabolas-source-3
    - fabolas-source-4
  - name: aio-relations
    value: 'related_match: AIO:TrainingStrategy'
    definition: This hyperparameter procedure selects model configurations and allocates
      training resources. The relation links that scope to the pinned training-strategy
      concept without treating the optimizer as preprocessing, an identical concept
      or a subclass.
    evidence_ids:
    - mapping
- assessment_id: dehb
  area: evidence
  topic: Identity, definition, mechanism, source conventions and AIO relations
  outcome: supported
  target_ids:
  - AIMech:DEHB
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - dehb-source-0
  - dehb-source-1
  summary: DEHB is the combined resource-allocation and differential-evolution method,
    distinct from generic genetic algorithms, differential evolution alone, random-proposal
    Hyperband, KDE-guided BOHB and ASHA’s asynchronous within-stage promotions. Budget-specific
    populations contain configuration vectors, not a population of trained checkpoints
    whose weights are copied between configurations. The proceedings paper and the
    versioned appendix are distinguished explicitly. No normalized identity match
    was found across all 442 pinned AIO labels/scoped synonyms and 262 preceding native
    IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden
    files in both worktree and main checkout, returning 9 lines in each checkout.
    These were prior candidate leads, source references and neighboring-method mentions,
    not existing records for these identities. Ten exact AIO CLASS nodes with synonyms
    and outgoing edges and eight neighboring native mechanisms were inspected. Absence
    is bounded to this snapshot and semantic neighborhood.
  details: 'Maintain a differential-evolution subpopulation for each Hyperband resource
    level, sized according to the maximum number of evaluations assigned to that level.
    Iterate through the prescribed halving brackets. For a bracket’s starting level
    use evolution within its own population; for higher levels form a parent pool
    from promising lower-level configurations and use it for difference-vector mutation,
    followed by crossover with a target in the current level’s population. Evaluate
    the proposed configuration at the current level and retain it only according to
    a same-level fitness comparison with the target. Supplement an undersized mutation
    pool from a global pool of configurations. The initialization cycle includes direct
    lower-to-higher promotions before the general evolutionary transfer pattern. For
    mixed search spaces, the appendix keeps continuous population coordinates in a
    unit hypercube and maps copies to numerical or binned ordinal/categorical settings
    for evaluation. Its parallel design keeps each halving stage synchronized while
    allowing brackets to overlap and applying completed differential-evolution updates
    immediately. Limits: The source’s initialization prose and pseudocode use bracket
    and iteration terminology inconsistently. Algorithm3’s bracket_counter==0 condition
    spans an outer cycle and applies direct promotion only for i>0. The record describes
    the common mechanism without treating every printed initialization statement as
    byte-equivalent executable steps. Appendix Algorithm2 prints b0=(bmax/bmin)*eta^(-s),
    which gives normalized rather than absolute budgets when bmin differs from1. Its
    return order for counts and budgets is reversed at the Algorithm3 call site. These
    discrepancies are retained as source qualifications; no author-issued erratum
    or exact executable schedule is claimed. The appendix updates its incumbent after
    evaluations without an explicit full-budget restriction. The record therefore
    does not promise that the returned best observed configuration has been verified
    at maximum resource. Greedy same-budget replacement limits harmful transfers but
    is not a proof of global optimality or universal robustness. Continuous encodings
    impose numerical neighborhoods on categorical choices, and low-fidelity information
    can be misleading. Parallel completion order can affect shared populations. No
    benchmark speedup, constant total runtime or author-code execution is claimed.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A defined algorithm-configuration or hyperparameter-search procedure
      with explicit surrogate, allocation and population scope.
    evidence_ids:
    - dehb-source-0
    - dehb-source-1
  - name: aio-relations
    value: 'related_match: AIO:TrainingStrategy'
    definition: This hyperparameter procedure selects model configurations and allocates
      training resources. The relation links that scope to the pinned training-strategy
      concept without treating the optimizer as preprocessing, an identical concept
      or a subclass.
    evidence_ids:
    - mapping
- assessment_id: smac-boundaries
  area: consistency
  topic: Original configuration algorithm, component model and evaluation comparison
  outcome: supported
  target_ids:
  - AIMech:SequentialModelBasedAlgorithmConfiguration
  evidence_ids:
  - sequentialmodelbasedalgorithmconfiguration-source-0
  - finite-conventions
  - neighbors
  summary: Retain original SMAC with source-specific scope and a component relation
    to RandomForest.
  details: A random-forest surrogate and log-cost expected improvement guide proposals,
    interleaved with uniform configurations. Blocked instance/seed comparisons and
    expanding evaluation subsets differ from independent random search. Original SMAC
    explicitly lacks adaptive capping; finite maxR and empirical comparisons do not
    inherit unconditional asymptotic guarantees. A single configured target algorithm
    is distinct from per-instance selection or its surrogate forest.
- assessment_id: fabolas-boundaries
  area: consistency
  topic: Dataset-size extrapolation, cost weighting and implementation versions
  outcome: supported
  target_ids:
  - AIMech:FABOLAS
  evidence_ids:
  - fabolas-source-0
  - fabolas-source-1
  - fabolas-source-2
  - fabolas-source-3
  - fabolas-source-4
  - finite-conventions
  - neighbors
  summary: Retain FABOLAS with full-dataset target and explicit paper/code distinctions.
  details: The paper selects informative configuration/size evaluations and returns
    a projected incumbent among observed configurations. The pinned code uses normalized
    log dataset counts, logs objective and cost, and applies Latin-hypercube initialization
    and a RandomSampling acquisition maximizer. Its update chain omits overhead and
    therefore uses zero, unlike the paper objective. A fixed-direction basis is not
    a guaranteed decreasing trend. These are static source observations, not evidence
    of executable compatibility or original-experiment identity.
- assessment_id: dehb-boundaries
  area: consistency
  topic: Evolutionary transfer, resource units and parallel stage boundaries
  outcome: supported
  target_ids:
  - AIMech:DEHB
  evidence_ids:
  - dehb-source-0
  - dehb-source-1
  - finite-conventions
  - neighbors
  summary: Retain DEHB with budget-specific populations and synchronous halving stages.
  details: Parent pools transfer low-budget configuration information into higher-budget
    mutation, while same-budget selection evaluates proposed changes. Brackets may
    overlap and population updates are immediate, but the versioned appendix explicitly
    waits for a lower stage before advancing. Printed budget units, return-order and
    initialization terminology require qualifications; the record does not claim literal
    pseudocode execution or a full-budget incumbent guarantee.
- assessment_id: mapping-boundaries
  area: grounding
  topic: Component relations versus algorithm identity
  outcome: supported
  target_ids:
  - AIMech:SequentialModelBasedAlgorithmConfiguration
  - AIMech:FABOLAS
  - AIMech:DEHB
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain three distinct native concepts with related AIO mappings.
  details: SMAC relates to AIO RandomForest through its surrogate component, not as
    an equivalent model or subclass. FABOLAS and DEHB relate to TrainingStrategy through
    explicit hyperparameter search and resource allocation; its preprocessing-oriented
    pinned definition does not justify an is-a link. BayesianNetwork, EvolutionaryLLM,
    broad learning tasks and prediction ensembles do not identify these full search
    algorithms. GPR is a surrogate component, and generic genetic algorithms do not
    identify DEHB’s budget-specific transfer and scheduling.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:SequentialModelBasedAlgorithmConfiguration
  - AIMech:FABOLAS
  - AIMech:DEHB
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - sequentialmodelbasedalgorithmconfiguration-source-0
  - fabolas-source-0
  - fabolas-source-1
  - fabolas-source-2
  - fabolas-source-3
  - fabolas-source-4
  - dehb-source-0
  - dehb-source-1
  rationale: Random-forest guided algorithm configuration, dataset-size extrapolating
    Bayesian optimization and evolutionary multi-fidelity search have distinct proposal
    and evaluation mechanisms. Shared surrogate or Hyperband components do not identify
    the complete algorithms.
limitations:
- Adversarial author self-review only; every record remains DRAFT.
- Only declared PDF pages and four static RoBO files were inspected. No training,
  benchmark, complete proof audit or author-code execution was performed.
- Source-version discrepancies and source-pseudocode ambiguities remain explicit.
  The failed DEHB supplementary link was replaced by an identified arXiv version;
  no author-issued erratum is claimed.
- Three additions and a nonempty inherited/new frontier leave discovery active.
tags:
- native-concepts
- hyperparameter-search
- surrogates
- evolution
- source-conventions
- self-review
- discovery-ongoing
```
