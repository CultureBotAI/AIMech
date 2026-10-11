# Scientific self-review of evolutionary search distributions

- Review: 20261011T122130Z-evolutionary-search-distributions
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T12:18:32Z
- Finished UTC: 2026-10-11T12:21:30Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain differential evolution, the 2001 CMA-ES account and the canonical NES framework with explicit source conventions, objective/distribution distinctions and bounded AIO no-match assessments. No actionable record defect was found in this scope.

## Scope And Provenance

All fields of the three newly maintained evolutionary-optimization records.

Selection: Exact three IDs in the discovery ledger; no sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 8e8214c37c04e38fcf57446c3972b67c21906d60.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:DifferentialEvolution | data/curated/DifferentialEvolution.yaml | maintained | Differential Evolution |
| AIMech:CovarianceMatrixAdaptationEvolutionStrategy | data/curated/CovarianceMatrixAdaptationEvolutionStrategy.yaml | maintained | Covariance Matrix Adaptation Evolution Strategy |
| AIMech:NaturalEvolutionStrategies | data/curated/NaturalEvolutionStrategies.yaml | maintained | Natural Evolution Strategies |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:DifferentialEvolution, AIMech:CovarianceMatrixAdaptationEvolutionStrategy, AIMech:NaturalEvolutionStrategies | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 69.27s (0:01:09)<br>Checked 442 record(s); 0 failed.<br>Checked 273 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 66 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 64,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:DifferentialEvolution, AIMech:CovarianceMatrixAdaptationEvolutionStrategy, AIMech:NaturalEvolutionStrategies | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| Finite evolutionary-search calculations | passed | True | AIMech:DifferentialEvolution, AIMech:CovarianceMatrixAdaptationEvolutionStrategy, AIMech:NaturalEvolutionStrategies | {"de_equal_cost": {"prose_strict_accepts": false, "figure3_nonstrict_accepts": true}, "de_initial_range_escape": 1.4, "de_collapsed_population_mutant": 0.7, "cma_rank_one_covariance": [[1.75, 0.0], [0.0, 0.75]], "cma_sampling_covariance_with_sigma2": [[7.0, 0.0], [0.0, 3.0]], "nes_gaussian_score": [1.0, 0.0], "nes_single_sample_fisher": [[1.0, 0.0], [0.0, 0.0]], "nes_exact_fisher_at_mu0_sigma1": [[1.0, 0.0], [0.0, 2.0]], "fitness_weighting": {"raw": 0.5, "cubed_fitness": 3.5, "same_rank_utility": 1.0}, "scope": "Finite arithmetic only; no optimizer, author implementation, training or benchmark was executed."} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, source conventions and AIO relations

evidence: supported. Targets: AIMech:DifferentialEvolution.

This record denotes differential evolution, with the 1997 DE/rand/1/bin procedure as its explicitly inspected core. Mutation/crossover variants are distinguished by the source’s DE/x/y/z notation rather than treated as identical executable rules. It differs from generic genetic algorithms, a fitted Gaussian search distribution, objective-gradient descent, and DEHB’s additional budget-specific populations and Hyperband scheduling. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 270 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 19 and 19 lines respectively. These were prior candidate leads, source discussions and neighboring DEHB/FABOLAS method mentions. Eight exact AIO CLASS nodes with scoped synonyms and outgoing edges and seven native neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Maintain a fixed-size population of real-valued vectors. In the inspected DE/rand/1/bin scheme, for each target select three mutually distinct current-generation population indices that also differ from the target index. Add a scaled difference of two selected vectors to the third to form a mutant. Build a trial by independently choosing mutant or target coordinates according to the crossover probability, forcing one randomly selected coordinate to come from the mutant. Evaluate the trial and use a greedy comparison against its target to choose the next-generation member. Complete all target comparisons using the old population before replacing it with the next population. Repeat until the configured stopping criterion is met. Population size, mutation scale, crossover probability and initialization are configuration choices. Limits: The prose specifies replacement for a strictly smaller objective, whereas the displayed C-style Figure3 uses &lt;=. The tie policy must therefore be identified when implementing or comparing versions; these source statements are not treated as identical code. A forced mutant coordinate need not change its numerical value. DE/rand/1/bin needs at least four population members for its distinct-index rule. Difference-vector proposals can leave the initialization range; that range is not a hard feasible-domain boundary. Bound repair, general constraint handling, noise treatment and categorical encodings are additional choices. The method uses function evaluations, not derivatives of the objective. Population collapse can eliminate difference-vector variation, and finite-budget greedy selection does not certify a global optimum. The source’s control-variable suggestions and comparative results are empirical, not universal guarantees or reproduced experiments.

### Identity, definition, mechanism, source conventions and AIO relations

evidence: supported. Targets: AIMech:CovarianceMatrixAdaptationEvolutionStrategy.

This record describes CMA-ES through the 2001 weighted-recombination algorithm and its author-supplied errata. That algorithm’s covariance update is based on a rank-one evolution-path outer product; later rank-mu, active covariance, restart and limited-memory variants are not silently imported. The search distribution is not a predictive model of objective values. Derandomized adaptation does not make offspring sampling deterministic. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 270 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 19 and 19 lines respectively. These were prior candidate leads, source discussions and neighboring DEHB/FABOLAS method mentions. Eight exact AIO CLASS nodes with scoped synonyms and outgoing edges and seven native neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Initialize a search mean, positive global step size, identity covariance and zero evolution paths. Sample a generation of Gaussian offspring with covariance equal to the global step size squared times the covariance matrix. Rank offspring by the minimization objective and recombine the selected best offspring with positive normalized weights to set the next mean. Accumulate a normalized selected mean displacement into a covariance evolution path. In the inspected 2001 procedure, blend the old covariance with the outer product of that path. Accumulate a separate path with covariance scaling removed and adjust the global step size exponentially according to its length relative to the expected length of a standard normal vector. Obtain the covariance axes and scales by eigendecomposition for subsequent sampling and repeat under the chosen stopping criterion. No derivatives of the objective are required. Limits: This is a source-specific account of the 2001 algorithm, not an exact implementation contract for all contemporary CMA-ES software. Its positive recombination weights, rank-one covariance update and cumulative step-size rule are distinguished from later extensions. The author errata qualify the default weight formula when the selected-parent count exceeds half the offspring population and revise a suggested ordering of cumulation parameters. Initial mean and step size matter. Weak, noisy or selection-irrelevant feedback and numerical conditioning can impair covariance adaptation or collapse short search directions. Full covariance storage grows quadratically with dimension; eigendecomposition and expensive function evaluations add computational costs. Constraint handling and termination require explicit choices. The paper discusses resampling feasible offspring but cautions about boundary optima. Ranking and distribution adaptation do not guarantee a global optimum, monotonic improvement of every generation, or a calibrated inverse-Hessian estimate. No benchmark speedup or author-code execution is asserted.

### Identity, definition, mechanism, source conventions and AIO relations

evidence: supported. Targets: AIMech:NaturalEvolutionStrategies.

NES is the shared natural-gradient search-distribution framework, not a single Gaussian implementation, a trained neural network or ordinary stochastic gradient descent on model weights. Its canonical method differentiates the search distribution’s log density, not the black-box objective itself. Exponential NES and separable NES are concrete variants with additional parameterization and computational choices; the framework record does not equate them. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 270 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 19 and 19 lines respectively. These were prior candidate leads, source discussions and neighboring DEHB/FABOLAS method mentions. Eight exact AIO CLASS nodes with scoped synonyms and outgoing edges and seven native neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Draw candidate points from a parameterized search distribution and evaluate their fitness. Compute the log-density derivative, or score, of each sample with respect to distribution parameters. In the canonical raw-fitness formulation, estimate the expected-fitness gradient by averaging score vectors weighted by fitness. Obtain the Fisher information of the distribution, analytically when available or through score outer products, and use its inverse action to transform the search gradient into a natural-gradient direction. Update the distribution parameters with a chosen learning rate and repeat. The paper additionally describes rank-based fitness shaping, which replaces raw fitness by ordered utility weights, and specialized distribution parameterizations that avoid a literal general Fisher-matrix inversion. Limits: The score identity and Fisher construction require suitable regularity, integrability and a usable parameterization. The empirical Fisher matrix can be singular or numerically unstable even when the population Fisher is invertible; a small batch does not automatically support the displayed inverse. Natural-gradient invariance describes the local direction under the appropriate exact metric. It is not an assertion that every finite, sampled parameter update is invariant under arbitrary reparameterization, stays in a valid distribution domain or improves expected fitness. Variant-specific parameterizations and learning rates matter. Rank-based shaping changes the weighting criterion; its update should not be described as an unbiased estimate of the raw expected-fitness gradient in general. A Gaussian search distribution, exponential covariance update and adaptation sampling are not mandatory features of every NES family member. Only the declared method and discussion pages were inspected. The record does not certify every displayed variant formula, an executable xNES/SNES implementation, universal benchmark superiority or a finite-budget global optimum.

### Difference-vector mutation, crossover, replacement and degeneracy

consistency: supported. Targets: AIMech:DifferentialEvolution.

Retain DE with the inspected DE/rand/1/bin core.

The selected donor indices differ from each other and the target; old-generation vectors feed every trial. Forced coordinate selection need not change its value. Source prose uses strict improvement, while Figure3 permits equal-cost replacement. Initial bounds do not constrain later proposals, and a collapsed population loses difference-vector variation. These qualifications avoid claiming a universal executable DE rule or global-optimum guarantee.

### Distribution adaptation, path covariance and author errata

consistency: supported. Targets: AIMech:CovarianceMatrixAdaptationEvolutionStrategy.

Retain the 2001 weighted-recombination CMA-ES account with source-version boundaries.

Gaussian offspring are ranked; weighted selected displacements drive a rank-one path outer product and a separate covariance-scaled step-size path. The 2001 positive-weight convention and author errata are explicit. Modern rank-mu, active and restart variants are not imported. Derandomized adaptation does not eliminate stochastic offspring, and full covariance is not a learned objective-value surrogate.

### Score-gradient objective, Fisher geometry and rank shaping

consistency: supported. Targets: AIMech:NaturalEvolutionStrategies.

Retain NES as a family rather than an executable xNES or SNES rule.

The canonical expected-fitness gradient uses fitness-weighted log-density derivatives, with natural-gradient preconditioning. Empirical Fisher inversion requires a usable estimate; a small batch can be singular even when the population matrix is nonsingular. Rank shaping changes the objective weighting. Local exact-metric invariance does not guarantee every finite estimated update is invariant or improves fitness. Unresolved variant transpose conventions are not asserted in this framework record.

### General optimizers versus evolutionary language models and learning tasks

grounding: supported. Targets: AIMech:DifferentialEvolution, AIMech:CovarianceMatrixAdaptationEvolutionStrategy, AIMech:NaturalEvolutionStrategies.

Retain three distinct native concepts with bounded no-match assessments.

No suitable AIO mapping identified among eight exact nodes. EvolutionaryLLM is specifically a language model despite its broad related synonym evolutionary algorithms. The general continuous optimizers are not language models, label acquisition, ensembles, ML experiment metadata learners or necessarily model training. Retain qualified no-match assessments rather than infer parenthood from an optional use. Native genericGA lacks DE-specific differences, CMA path/covariance adaptation and NES Fisher-preconditioned score estimates. DEHB is a composite HPO/resource-allocation method; SGD/gradient boosting differentiate different objectives/representations, and CGMC is a target-invariant sampler rather than an optimizer.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:DifferentialEvolution, AIMech:CovarianceMatrixAdaptationEvolutionStrategy, AIMech:NaturalEvolutionStrategies. Difference-vector proposals, rank-selected path covariance adaptation and Fisher-preconditioned search-distribution updates have distinct mechanisms. Shared population sampling or optimization applications do not establish equivalence.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T121829Z-evolutionary-search-distributions.json | supports | Compared all 442 pinned AIO labels/scoped synonyms and 270 preceding native IDs/names/aliases, including candidate-internal normalized uniqueness. No identity match was found. Full-checkout fixed-string searches included ignored/hidden files and returned 19 worktree and 19 main lines: prior leads, neighboring DEHB/FABOLAS mechanisms and source discussions. Eight exact AIO CLASS nodes with scoped synonyms/outgoing edges and seven native neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood. |
| mapping | sources/aio/aio.json; Eight exact CLASS nodes and their scoped synonyms/outgoing edges in source_analysis.aio_mapping_inspection | supports | No suitable AIO mapping identified among eight exact nodes. EvolutionaryLLM is specifically a language model despite its broad related synonym evolutionary algorithms. The general continuous optimizers are not language models, label acquisition, ensembles, ML experiment metadata learners or necessarily model training. Retain qualified no-match assessments rather than infer parenthood from an optional use. Native genericGA lacks DE-specific differences, CMA path/covariance adaptation and NES Fisher-preconditioned score estimates. DEHB is a composite HPO/resource-allocation method; SGD/gradient boosting differentiate different objectives/representations, and CGMC is a target-invariant sampler rather than an optimizer. |
| neighbors | research/discovery/20261011T121829Z-evolutionary-search-distributions.json; source_analysis.aio_mapping_inspection.native_neighbors | supports | Inspect seven native neighbors: DEHB, genetic algorithm, stochastic gradient descent, gradient boosting, conjugate-gradient Monte Carlo, FABOLAS and SMAC. Shared evolutionary components, adaptation or application as an acquisition optimizer do not identify the complete procedures. |
| finite-conventions | research/discovery/evolutionary-search-boundaries.py; calculate(): DE tie/range/degenerate-population boundaries, CMA covariance blend and sampling scale, NES empirical Fisher singularity and raw versus ranked fitness | supports | Original finite examples examine DE ties/range/degenerate variation, the CMA rank-one covariance blend and sampling scale, and NES empirical-Fisher singularity and raw-versus-rank fitness weighting. No author algorithm or model was executed. |
| differentialevolution-source-0 | https://groups.csail.mit.edu/EVO-DesignOpt/pb/uploads/Site/differentialEv.pdf; Section2, PDF pp.3–7 (printed343–347), especially Equations2–4 and Figure3; Section4, PDF pp.16–17; Section5, PDF pp.17–18 | supports | Differential Evolution – A Simple and Efficient Heuristic for Global Optimization over Continuous Spaces. Journal of Global Optimization 11:341–359, 1997; 19-page article hosted by MIT CSAIL. Actual PDF reading scopes are declared in the ledger. Source rendering alone does not attest inspection. |
| covariancematrixadaptationevolutionstrategy-source-0 | https://www.cmap.polytechnique.fr/~nikolaus.hansen/cmaartic.pdf; Section4 cumulation, PDF pp.15–18; Section5 and Equations13–17, PDF pp.18–23 (article pp.16–21); prefixed errata PDFp.1; conclusion PDF pp.34–35 | supports | Completely Derandomized Self-Adaptation in Evolution Strategies. Evolutionary Computation 9(2):159–195, 2001; 39-page author copy with prefixed errata and blank page; article begins at PDFp.3. Actual PDF reading scopes are declared in the ledger. Source rendering alone does not attest inspection. |
| naturalevolutionstrategies-source-0 | https://www.jmlr.org/papers/volume15/wierstra14a/wierstra14a.pdf; Sections1.2 and2–2.3, PDF pp.3–10 (printed951–958), especially Equations1–5 and Algorithm3; fitness shaping in Section3.1, pp.10–11; variants and scope in Sections3.3–3.4, pp.13–16; discussion pp.27–28 | supports | Natural Evolution Strategies. JMLR 15(27):949–980, 2014; 32-page journal PDF. Actual PDF reading scopes are declared in the ledger. Source rendering alone does not attest inspection. |

## Limits And Additional Notes

- Adversarial author self-review only; every record remains DRAFT.
- Only declared PDF pages were inspected. No training, benchmark, complete proof audit or author-code execution was performed.
- Source-version discrepancies and source-pseudocode ambiguities remain explicit. CMA author errata were inspected; unresolved executable-variant details are outside the NES family record.
- Three additions and a nonempty inherited/new frontier leave discovery active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T122130Z-evolutionary-search-distributions
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of evolutionary search distributions
started_at: '2026-10-11T12:18:32Z'
finished_at: '2026-10-11T12:21:30Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed all three records
    against the declared primary methods, rendered pages, CMA author errata, eight
    exact AIO nodes, seven native neighbors and original finite arithmetic. This is
    not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain differential evolution, the 2001 CMA-ES account and the canonical
  NES framework with explicit source conventions, objective/distribution distinctions
  and bounded AIO no-match assessments. No actionable record defect was found in this
  scope.
source:
  git_revision: 8e8214c37c04e38fcf57446c3972b67c21906d60
  state: working_tree
  inputs:
  - path: data/aio/ActiveLearning.yaml
    sha256: a4d5b2c82df6f586fedc7290261bc978e7c8d17f1d844c5ee9efc8243e46bbaf
    role: context
  - path: data/aio/EvaluationBias.yaml
    sha256: 6523f8c43f7b140c6dd593069e30b7fc1bdd60b89d01bdf5441d2bc83a12e749
    role: context
  - path: data/aio/EvolutionaryLLM.yaml
    sha256: d3db6adea3d8d58096c9fb5abef67273489ee719ab900b2d4adbb129e4f7362f
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
  - path: data/curated/ConjugateGradientMonteCarlo.yaml
    sha256: 59c29605048365b38ef298fdd3401bf00a8beb522fc9d4b3c8fe868d6946fa4f
    role: context
  - path: data/curated/CovarianceMatrixAdaptationEvolutionStrategy.yaml
    sha256: 7018c9916e78f34ba32a3a9d46e694d2a78c17a6e7222d9050d305eedf96ed06
    role: target
  - path: data/curated/DEHB.yaml
    sha256: c0c18d5afdd9aa26db73d0c84e4e0d2a623e242a0fb18bd42ee5c4588473d412
    role: context
  - path: data/curated/DifferentialEvolution.yaml
    sha256: 8c937f585818445a809f6aa26c51c4195e1fe2e3a634d349762322f89e97ff68
    role: target
  - path: data/curated/FABOLAS.yaml
    sha256: 800fb7787896a6cd3f0c2ced22fd70543a79d3a59502ff2c52cf4ae4f8ba0cb9
    role: context
  - path: data/curated/GeneticAlgorithm.yaml
    sha256: d40bf1a03e29a3ca6bf88f6553f18c6b1559baf56da6a21d63b54163f4752ceb
    role: context
  - path: data/curated/GradientBoosting.yaml
    sha256: 2e89ee7d292a071d6d4b8aecf81cd57cae84a50a2d167cc69ffee2cebf4dffe5
    role: context
  - path: data/curated/NaturalEvolutionStrategies.yaml
    sha256: b11c8d02da55175afcf5d5c11cf91a864418d7396b726f423f865d95cfe76a4c
    role: target
  - path: data/curated/SequentialModelBasedAlgorithmConfiguration.yaml
    sha256: 578ea6762a48bc56063d3e5907bb038b728112560a3baee7811d4f9b50354357
    role: context
  - path: data/curated/StochasticGradientDescent.yaml
    sha256: 5c57fc809ae8667d5be8cda421cc9f0bd1f0c668f64ba3d7b23d788528b46e97
    role: context
  - path: research/discovery/20261011T121829Z-evolutionary-search-distributions.json
    sha256: 45877683e793babd51cf335e05aef3f52224e48e500b4b296716071dc60acd4d
    role: context
  - path: research/discovery/evolutionary-search-boundaries.py
    sha256: c5969386ed608f8374507df52f21e7c7dd3087104c544ef7920d83bed467f891
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
- target_id: AIMech:DifferentialEvolution
  path: data/curated/DifferentialEvolution.yaml
  label: Differential Evolution
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/DifferentialEvolution.yaml
    role: maintained
- target_id: AIMech:CovarianceMatrixAdaptationEvolutionStrategy
  path: data/curated/CovarianceMatrixAdaptationEvolutionStrategy.yaml
  label: Covariance Matrix Adaptation Evolution Strategy
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CovarianceMatrixAdaptationEvolutionStrategy.yaml
    role: maintained
- target_id: AIMech:NaturalEvolutionStrategies
  path: data/curated/NaturalEvolutionStrategies.yaml
  label: Natural Evolution Strategies
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/NaturalEvolutionStrategies.yaml
    role: maintained
scope:
  description: All fields of the three newly maintained evolutionary-optimization
    records.
  selection: Exact three IDs in the discovery ledger; no sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:DifferentialEvolution
  - AIMech:CovarianceMatrixAdaptationEvolutionStrategy
  - AIMech:NaturalEvolutionStrategies
  exclusions:
  - target: Older records and unselected candidates
    reason: Neighbors were inspected for boundaries, not a complete new review of
      the earlier corpus.
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
  - AIMech:DifferentialEvolution
  - AIMech:CovarianceMatrixAdaptationEvolutionStrategy
  - AIMech:NaturalEvolutionStrategies
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 69.27s (0:01:09)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 273 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 66 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 64,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:DifferentialEvolution
  - AIMech:CovarianceMatrixAdaptationEvolutionStrategy
  - AIMech:NaturalEvolutionStrategies
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
- check_id: finite-arithmetic
  name: Finite evolutionary-search calculations
  command: python3 research/discovery/evolutionary-search-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:DifferentialEvolution
  - AIMech:CovarianceMatrixAdaptationEvolutionStrategy
  - AIMech:NaturalEvolutionStrategies
  exit_code: 0
  expected_exit_code: 0
  summary: '{"de_equal_cost": {"prose_strict_accepts": false, "figure3_nonstrict_accepts":
    true}, "de_initial_range_escape": 1.4, "de_collapsed_population_mutant": 0.7,
    "cma_rank_one_covariance": [[1.75, 0.0], [0.0, 0.75]], "cma_sampling_covariance_with_sigma2":
    [[7.0, 0.0], [0.0, 3.0]], "nes_gaussian_score": [1.0, 0.0], "nes_single_sample_fisher":
    [[1.0, 0.0], [0.0, 0.0]], "nes_exact_fisher_at_mu0_sigma1": [[1.0, 0.0], [0.0,
    2.0]], "fitness_weighting": {"raw": 0.5, "cubed_fitness": 3.5, "same_rank_utility":
    1.0}, "scope": "Finite arithmetic only; no optimizer, author implementation, training
    or benchmark was executed."}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T121829Z-evolutionary-search-distributions.json
  accessed_at: '2026-10-11T12:18:32Z'
  support: supports
  summary: 'Compared all 442 pinned AIO labels/scoped synonyms and 270 preceding native
    IDs/names/aliases, including candidate-internal normalized uniqueness. No identity
    match was found. Full-checkout fixed-string searches included ignored/hidden files
    and returned 19 worktree and 19 main lines: prior leads, neighboring DEHB/FABOLAS
    mechanisms and source discussions. Eight exact AIO CLASS nodes with scoped synonyms/outgoing
    edges and seven native neighboring mechanisms were inspected. Absence is bounded
    to this snapshot and semantic neighborhood.'
  search_scope: All 442 pinned AIO labels/scoped synonyms and 270 preceding maintained
    IDs/names/aliases; full checkouts including ignored/hidden files; candidate-internal
    normalized uniqueness.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Eight exact CLASS nodes and their scoped synonyms/outgoing edges in source_analysis.aio_mapping_inspection
  accessed_at: '2026-10-11T12:18:32Z'
  support: supports
  summary: No suitable AIO mapping identified among eight exact nodes. EvolutionaryLLM
    is specifically a language model despite its broad related synonym evolutionary
    algorithms. The general continuous optimizers are not language models, label acquisition,
    ensembles, ML experiment metadata learners or necessarily model training. Retain
    qualified no-match assessments rather than infer parenthood from an optional use.
    Native genericGA lacks DE-specific differences, CMA path/covariance adaptation
    and NES Fisher-preconditioned score estimates. DEHB is a composite HPO/resource-allocation
    method; SGD/gradient boosting differentiate different objectives/representations,
    and CGMC is a target-invariant sampler rather than an optimizer.
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T121829Z-evolutionary-search-distributions.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors
  accessed_at: '2026-10-11T12:18:32Z'
  support: supports
  summary: 'Inspect seven native neighbors: DEHB, genetic algorithm, stochastic gradient
    descent, gradient boosting, conjugate-gradient Monte Carlo, FABOLAS and SMAC.
    Shared evolutionary components, adaptation or application as an acquisition optimizer
    do not identify the complete procedures.'
- evidence_id: finite-conventions
  kind: record_content
  reference: research/discovery/evolutionary-search-boundaries.py
  locator: 'calculate(): DE tie/range/degenerate-population boundaries, CMA covariance
    blend and sampling scale, NES empirical Fisher singularity and raw versus ranked
    fitness'
  accessed_at: '2026-10-11T12:18:32Z'
  snapshot_sha256: c5969386ed608f8374507df52f21e7c7dd3087104c544ef7920d83bed467f891
  support: supports
  summary: Original finite examples examine DE ties/range/degenerate variation, the
    CMA rank-one covariance blend and sampling scale, and NES empirical-Fisher singularity
    and raw-versus-rank fitness weighting. No author algorithm or model was executed.
- evidence_id: differentialevolution-source-0
  kind: primary_source
  reference: https://groups.csail.mit.edu/EVO-DesignOpt/pb/uploads/Site/differentialEv.pdf
  locator: Section2, PDF pp.3–7 (printed343–347), especially Equations2–4 and Figure3;
    Section4, PDF pp.16–17; Section5, PDF pp.17–18
  accessed_at: '2026-10-11T12:07:35Z'
  snapshot_sha256: d8bd6c0f8030790d9d172076b57119bc94fd861bbca79c94ae6b680363239f12
  support: supports
  summary: Differential Evolution – A Simple and Efficient Heuristic for Global Optimization
    over Continuous Spaces. Journal of Global Optimization 11:341–359, 1997; 19-page
    article hosted by MIT CSAIL. Actual PDF reading scopes are declared in the ledger.
    Source rendering alone does not attest inspection.
- evidence_id: covariancematrixadaptationevolutionstrategy-source-0
  kind: primary_source
  reference: https://www.cmap.polytechnique.fr/~nikolaus.hansen/cmaartic.pdf
  locator: Section4 cumulation, PDF pp.15–18; Section5 and Equations13–17, PDF pp.18–23
    (article pp.16–21); prefixed errata PDFp.1; conclusion PDF pp.34–35
  accessed_at: '2026-10-11T12:07:35Z'
  snapshot_sha256: 423664eab4f67c106ccd0fed616bbcaf9bf7faf23c13c917f5af578b1dddba6f
  support: supports
  summary: Completely Derandomized Self-Adaptation in Evolution Strategies. Evolutionary
    Computation 9(2):159–195, 2001; 39-page author copy with prefixed errata and blank
    page; article begins at PDFp.3. Actual PDF reading scopes are declared in the
    ledger. Source rendering alone does not attest inspection.
- evidence_id: naturalevolutionstrategies-source-0
  kind: primary_source
  reference: https://www.jmlr.org/papers/volume15/wierstra14a/wierstra14a.pdf
  locator: Sections1.2 and2–2.3, PDF pp.3–10 (printed951–958), especially Equations1–5
    and Algorithm3; fitness shaping in Section3.1, pp.10–11; variants and scope in
    Sections3.3–3.4, pp.13–16; discussion pp.27–28
  accessed_at: '2026-10-11T12:07:35Z'
  snapshot_sha256: 80ec84951836e76f3db0ce5d245d73ceecf8b233069cca387ed97f157bae08d6
  support: supports
  summary: Natural Evolution Strategies. JMLR 15(27):949–980, 2014; 32-page journal
    PDF. Actual PDF reading scopes are declared in the ledger. Source rendering alone
    does not attest inspection.
assessments:
- assessment_id: differentialevolution
  area: evidence
  topic: Identity, definition, mechanism, source conventions and AIO relations
  outcome: supported
  target_ids:
  - AIMech:DifferentialEvolution
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - differentialevolution-source-0
  summary: This record denotes differential evolution, with the 1997 DE/rand/1/bin
    procedure as its explicitly inspected core. Mutation/crossover variants are distinguished
    by the source’s DE/x/y/z notation rather than treated as identical executable
    rules. It differs from generic genetic algorithms, a fitted Gaussian search distribution,
    objective-gradient descent, and DEHB’s additional budget-specific populations
    and Hyperband scheduling. No normalized identity match was found across all 442
    pinned AIO labels/scoped synonyms and 270 preceding native IDs/names/aliases.
    Full-checkout fixed-string searches included ignored and hidden files in worktree
    and main, returning 19 and 19 lines respectively. These were prior candidate leads,
    source discussions and neighboring DEHB/FABOLAS method mentions. Eight exact AIO
    CLASS nodes with scoped synonyms and outgoing edges and seven native neighboring
    mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.
  details: 'Maintain a fixed-size population of real-valued vectors. In the inspected
    DE/rand/1/bin scheme, for each target select three mutually distinct current-generation
    population indices that also differ from the target index. Add a scaled difference
    of two selected vectors to the third to form a mutant. Build a trial by independently
    choosing mutant or target coordinates according to the crossover probability,
    forcing one randomly selected coordinate to come from the mutant. Evaluate the
    trial and use a greedy comparison against its target to choose the next-generation
    member. Complete all target comparisons using the old population before replacing
    it with the next population. Repeat until the configured stopping criterion is
    met. Population size, mutation scale, crossover probability and initialization
    are configuration choices. Limits: The prose specifies replacement for a strictly
    smaller objective, whereas the displayed C-style Figure3 uses <=. The tie policy
    must therefore be identified when implementing or comparing versions; these source
    statements are not treated as identical code. A forced mutant coordinate need
    not change its numerical value. DE/rand/1/bin needs at least four population members
    for its distinct-index rule. Difference-vector proposals can leave the initialization
    range; that range is not a hard feasible-domain boundary. Bound repair, general
    constraint handling, noise treatment and categorical encodings are additional
    choices. The method uses function evaluations, not derivatives of the objective.
    Population collapse can eliminate difference-vector variation, and finite-budget
    greedy selection does not certify a global optimum. The source’s control-variable
    suggestions and comparative results are empirical, not universal guarantees or
    reproduced experiments.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A continuous black-box optimization procedure or framework with explicit
      proposal-distribution and update scope.
    evidence_ids:
    - differentialevolution-source-0
  - name: aio-relations
    value: aio_no_match
    definition: No inspected AIO target captures this general optimization procedure
      or a defining component. The assessment distinguishes evolutionary language
      models, learning/training tasks and predictive models from the native algorithm;
      it is bounded to this pinned vocabulary. The CLASS definition is a large language
      model with evolutionary optimization. Its broad related synonym evolutionary
      algorithms does not make a general continuous optimizer a language model or
      an exact vocabulary match. The pinned definition concerns preprocessing/training
      of machine-learning models. General black-box continuous optimization is not
      inherently model training; an optional application does not establish a necessary
      mapping. The target denotes building methods that learn from data. These algorithms
      can optimize arbitrary evaluated functions without a learning task, so shared
      optimization vocabulary alone is insufficient. Adapting a search distribution
      or optimizer state does not require learning from metadata about machine-learning
      experiments as in the pinned definition. Candidate evaluation is not the defined
      task of querying labels for data points. A possible policy-search application
      does not turn the general optimizer into the pinned learning task; no environment/reward-policy
      interface is inherent to the full identity. Population members and search distributions
      are not a predictive decision-tree ensemble; no random-forest surrogate is required.
      This is a bias concept, not the optimizer. Possible evaluation or sampling problems
      are limitations rather than identity mappings.
    evidence_ids:
    - mapping
- assessment_id: covariancematrixadaptationevolutionstrategy
  area: evidence
  topic: Identity, definition, mechanism, source conventions and AIO relations
  outcome: supported
  target_ids:
  - AIMech:CovarianceMatrixAdaptationEvolutionStrategy
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - covariancematrixadaptationevolutionstrategy-source-0
  summary: This record describes CMA-ES through the 2001 weighted-recombination algorithm
    and its author-supplied errata. That algorithm’s covariance update is based on
    a rank-one evolution-path outer product; later rank-mu, active covariance, restart
    and limited-memory variants are not silently imported. The search distribution
    is not a predictive model of objective values. Derandomized adaptation does not
    make offspring sampling deterministic. No normalized identity match was found
    across all 442 pinned AIO labels/scoped synonyms and 270 preceding native IDs/names/aliases.
    Full-checkout fixed-string searches included ignored and hidden files in worktree
    and main, returning 19 and 19 lines respectively. These were prior candidate leads,
    source discussions and neighboring DEHB/FABOLAS method mentions. Eight exact AIO
    CLASS nodes with scoped synonyms and outgoing edges and seven native neighboring
    mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.
  details: 'Initialize a search mean, positive global step size, identity covariance
    and zero evolution paths. Sample a generation of Gaussian offspring with covariance
    equal to the global step size squared times the covariance matrix. Rank offspring
    by the minimization objective and recombine the selected best offspring with positive
    normalized weights to set the next mean. Accumulate a normalized selected mean
    displacement into a covariance evolution path. In the inspected 2001 procedure,
    blend the old covariance with the outer product of that path. Accumulate a separate
    path with covariance scaling removed and adjust the global step size exponentially
    according to its length relative to the expected length of a standard normal vector.
    Obtain the covariance axes and scales by eigendecomposition for subsequent sampling
    and repeat under the chosen stopping criterion. No derivatives of the objective
    are required. Limits: This is a source-specific account of the 2001 algorithm,
    not an exact implementation contract for all contemporary CMA-ES software. Its
    positive recombination weights, rank-one covariance update and cumulative step-size
    rule are distinguished from later extensions. The author errata qualify the default
    weight formula when the selected-parent count exceeds half the offspring population
    and revise a suggested ordering of cumulation parameters. Initial mean and step
    size matter. Weak, noisy or selection-irrelevant feedback and numerical conditioning
    can impair covariance adaptation or collapse short search directions. Full covariance
    storage grows quadratically with dimension; eigendecomposition and expensive function
    evaluations add computational costs. Constraint handling and termination require
    explicit choices. The paper discusses resampling feasible offspring but cautions
    about boundary optima. Ranking and distribution adaptation do not guarantee a
    global optimum, monotonic improvement of every generation, or a calibrated inverse-Hessian
    estimate. No benchmark speedup or author-code execution is asserted.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A continuous black-box optimization procedure or framework with explicit
      proposal-distribution and update scope.
    evidence_ids:
    - covariancematrixadaptationevolutionstrategy-source-0
  - name: aio-relations
    value: aio_no_match
    definition: No inspected AIO target captures this general optimization procedure
      or a defining component. The assessment distinguishes evolutionary language
      models, learning/training tasks and predictive models from the native algorithm;
      it is bounded to this pinned vocabulary. The CLASS definition is a large language
      model with evolutionary optimization. Its broad related synonym evolutionary
      algorithms does not make a general continuous optimizer a language model or
      an exact vocabulary match. The pinned definition concerns preprocessing/training
      of machine-learning models. General black-box continuous optimization is not
      inherently model training; an optional application does not establish a necessary
      mapping. The target denotes building methods that learn from data. These algorithms
      can optimize arbitrary evaluated functions without a learning task, so shared
      optimization vocabulary alone is insufficient. Adapting a search distribution
      or optimizer state does not require learning from metadata about machine-learning
      experiments as in the pinned definition. Candidate evaluation is not the defined
      task of querying labels for data points. A possible policy-search application
      does not turn the general optimizer into the pinned learning task; no environment/reward-policy
      interface is inherent to the full identity. Population members and search distributions
      are not a predictive decision-tree ensemble; no random-forest surrogate is required.
      This is a bias concept, not the optimizer. Possible evaluation or sampling problems
      are limitations rather than identity mappings.
    evidence_ids:
    - mapping
- assessment_id: naturalevolutionstrategies
  area: evidence
  topic: Identity, definition, mechanism, source conventions and AIO relations
  outcome: supported
  target_ids:
  - AIMech:NaturalEvolutionStrategies
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - naturalevolutionstrategies-source-0
  summary: NES is the shared natural-gradient search-distribution framework, not a
    single Gaussian implementation, a trained neural network or ordinary stochastic
    gradient descent on model weights. Its canonical method differentiates the search
    distribution’s log density, not the black-box objective itself. Exponential NES
    and separable NES are concrete variants with additional parameterization and computational
    choices; the framework record does not equate them. No normalized identity match
    was found across all 442 pinned AIO labels/scoped synonyms and 270 preceding native
    IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden
    files in worktree and main, returning 19 and 19 lines respectively. These were
    prior candidate leads, source discussions and neighboring DEHB/FABOLAS method
    mentions. Eight exact AIO CLASS nodes with scoped synonyms and outgoing edges
    and seven native neighboring mechanisms were inspected. Absence is bounded to
    this snapshot and semantic neighborhood.
  details: 'Draw candidate points from a parameterized search distribution and evaluate
    their fitness. Compute the log-density derivative, or score, of each sample with
    respect to distribution parameters. In the canonical raw-fitness formulation,
    estimate the expected-fitness gradient by averaging score vectors weighted by
    fitness. Obtain the Fisher information of the distribution, analytically when
    available or through score outer products, and use its inverse action to transform
    the search gradient into a natural-gradient direction. Update the distribution
    parameters with a chosen learning rate and repeat. The paper additionally describes
    rank-based fitness shaping, which replaces raw fitness by ordered utility weights,
    and specialized distribution parameterizations that avoid a literal general Fisher-matrix
    inversion. Limits: The score identity and Fisher construction require suitable
    regularity, integrability and a usable parameterization. The empirical Fisher
    matrix can be singular or numerically unstable even when the population Fisher
    is invertible; a small batch does not automatically support the displayed inverse.
    Natural-gradient invariance describes the local direction under the appropriate
    exact metric. It is not an assertion that every finite, sampled parameter update
    is invariant under arbitrary reparameterization, stays in a valid distribution
    domain or improves expected fitness. Variant-specific parameterizations and learning
    rates matter. Rank-based shaping changes the weighting criterion; its update should
    not be described as an unbiased estimate of the raw expected-fitness gradient
    in general. A Gaussian search distribution, exponential covariance update and
    adaptation sampling are not mandatory features of every NES family member. Only
    the declared method and discussion pages were inspected. The record does not certify
    every displayed variant formula, an executable xNES/SNES implementation, universal
    benchmark superiority or a finite-budget global optimum.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: A continuous black-box optimization procedure or framework with explicit
      proposal-distribution and update scope.
    evidence_ids:
    - naturalevolutionstrategies-source-0
  - name: aio-relations
    value: aio_no_match
    definition: No inspected AIO target captures this general optimization procedure
      or a defining component. The assessment distinguishes evolutionary language
      models, learning/training tasks and predictive models from the native algorithm;
      it is bounded to this pinned vocabulary. The CLASS definition is a large language
      model with evolutionary optimization. Its broad related synonym evolutionary
      algorithms does not make a general continuous optimizer a language model or
      an exact vocabulary match. The pinned definition concerns preprocessing/training
      of machine-learning models. General black-box continuous optimization is not
      inherently model training; an optional application does not establish a necessary
      mapping. The target denotes building methods that learn from data. These algorithms
      can optimize arbitrary evaluated functions without a learning task, so shared
      optimization vocabulary alone is insufficient. Adapting a search distribution
      or optimizer state does not require learning from metadata about machine-learning
      experiments as in the pinned definition. Candidate evaluation is not the defined
      task of querying labels for data points. A possible policy-search application
      does not turn the general optimizer into the pinned learning task; no environment/reward-policy
      interface is inherent to the full identity. Population members and search distributions
      are not a predictive decision-tree ensemble; no random-forest surrogate is required.
      This is a bias concept, not the optimizer. Possible evaluation or sampling problems
      are limitations rather than identity mappings.
    evidence_ids:
    - mapping
- assessment_id: de-boundaries
  area: consistency
  topic: Difference-vector mutation, crossover, replacement and degeneracy
  outcome: supported
  target_ids:
  - AIMech:DifferentialEvolution
  evidence_ids:
  - differentialevolution-source-0
  - finite-conventions
  - neighbors
  summary: Retain DE with the inspected DE/rand/1/bin core.
  details: The selected donor indices differ from each other and the target; old-generation
    vectors feed every trial. Forced coordinate selection need not change its value.
    Source prose uses strict improvement, while Figure3 permits equal-cost replacement.
    Initial bounds do not constrain later proposals, and a collapsed population loses
    difference-vector variation. These qualifications avoid claiming a universal executable
    DE rule or global-optimum guarantee.
- assessment_id: cma-boundaries
  area: consistency
  topic: Distribution adaptation, path covariance and author errata
  outcome: supported
  target_ids:
  - AIMech:CovarianceMatrixAdaptationEvolutionStrategy
  evidence_ids:
  - covariancematrixadaptationevolutionstrategy-source-0
  - finite-conventions
  - neighbors
  summary: Retain the 2001 weighted-recombination CMA-ES account with source-version
    boundaries.
  details: Gaussian offspring are ranked; weighted selected displacements drive a
    rank-one path outer product and a separate covariance-scaled step-size path. The
    2001 positive-weight convention and author errata are explicit. Modern rank-mu,
    active and restart variants are not imported. Derandomized adaptation does not
    eliminate stochastic offspring, and full covariance is not a learned objective-value
    surrogate.
- assessment_id: nes-boundaries
  area: consistency
  topic: Score-gradient objective, Fisher geometry and rank shaping
  outcome: supported
  target_ids:
  - AIMech:NaturalEvolutionStrategies
  evidence_ids:
  - naturalevolutionstrategies-source-0
  - finite-conventions
  - neighbors
  summary: Retain NES as a family rather than an executable xNES or SNES rule.
  details: The canonical expected-fitness gradient uses fitness-weighted log-density
    derivatives, with natural-gradient preconditioning. Empirical Fisher inversion
    requires a usable estimate; a small batch can be singular even when the population
    matrix is nonsingular. Rank shaping changes the objective weighting. Local exact-metric
    invariance does not guarantee every finite estimated update is invariant or improves
    fitness. Unresolved variant transpose conventions are not asserted in this framework
    record.
- assessment_id: mapping-boundaries
  area: grounding
  topic: General optimizers versus evolutionary language models and learning tasks
  outcome: supported
  target_ids:
  - AIMech:DifferentialEvolution
  - AIMech:CovarianceMatrixAdaptationEvolutionStrategy
  - AIMech:NaturalEvolutionStrategies
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain three distinct native concepts with bounded no-match assessments.
  details: No suitable AIO mapping identified among eight exact nodes. EvolutionaryLLM
    is specifically a language model despite its broad related synonym evolutionary
    algorithms. The general continuous optimizers are not language models, label acquisition,
    ensembles, ML experiment metadata learners or necessarily model training. Retain
    qualified no-match assessments rather than infer parenthood from an optional use.
    Native genericGA lacks DE-specific differences, CMA path/covariance adaptation
    and NES Fisher-preconditioned score estimates. DEHB is a composite HPO/resource-allocation
    method; SGD/gradient boosting differentiate different objectives/representations,
    and CGMC is a target-invariant sampler rather than an optimizer.
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:DifferentialEvolution
  - AIMech:CovarianceMatrixAdaptationEvolutionStrategy
  - AIMech:NaturalEvolutionStrategies
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - differentialevolution-source-0
  - covariancematrixadaptationevolutionstrategy-source-0
  - naturalevolutionstrategies-source-0
  rationale: Difference-vector proposals, rank-selected path covariance adaptation
    and Fisher-preconditioned search-distribution updates have distinct mechanisms.
    Shared population sampling or optimization applications do not establish equivalence.
limitations:
- Adversarial author self-review only; every record remains DRAFT.
- Only declared PDF pages were inspected. No training, benchmark, complete proof audit
  or author-code execution was performed.
- Source-version discrepancies and source-pseudocode ambiguities remain explicit.
  CMA author errata were inspected; unresolved executable-variant details are outside
  the NES family record.
- Three additions and a nonempty inherited/new frontier leave discovery active.
tags:
- native-concepts
- black-box-optimization
- search-distributions
- evolution
- source-conventions
- self-review
- discovery-ongoing
```
