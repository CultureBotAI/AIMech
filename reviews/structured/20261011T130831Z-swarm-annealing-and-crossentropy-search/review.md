# Scientific self-review of swarm, annealing and cross-entropy search

- Review: 20261011T130831Z-swarm-annealing-and-crossentropy-search
- Repository: CultureBotAI/AIMech
- Started UTC: 2026-10-11T13:07:35Z
- Finished UTC: 2026-10-11T13:08:31Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Retain PSO, simulated annealing and cross-entropy optimization with explicit source conventions, optimization/sampling distinctions and bounded AIO assessments. No actionable record defect was found in this scope.

## Scope And Provenance

All fields of the three newly maintained stochastic optimization records.

Selection: Exact three IDs in the discovery ledger; no sampling.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 886d146bca59db1de4a786c056fba5fd34fb818f.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| AIMech:ParticleSwarmOptimization | data/curated/ParticleSwarmOptimization.yaml | maintained | Particle swarm optimization |
| AIMech:SimulatedAnnealing | data/curated/SimulatedAnnealing.yaml | maintained | Simulated annealing |
| AIMech:CrossEntropyOptimization | data/curated/CrossEntropyOptimization.yaml | maintained | Cross-entropy optimization |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just check | passed | True | AIMech:ParticleSwarmOptimization, AIMech:SimulatedAnnealing, AIMech:CrossEntropyOptimization | All checks passed!<br>........................................................................ [ 29%]<br>........................................................................ [ 59%]<br>........................................................................ [ 89%]<br>.......................sss                                               [100%]<br>239 passed, 3 skipped in 83.12s (0:01:23)<br>Checked 442 record(s); 0 failed.<br>Checked 288 curated concept record(s); 0 error(s).<br>AIO: 442 records; 0 missing, 0 changed, 0 unexpected.<br>Checked 71 history record(s); 0 error(s).<br>{<br>  "repository": "CultureBotAI/AIMech",<br>  "valid_reviews": 69,<br>  "coverage": "declared_scopes_only"<br>}<br>uv run --locked --extra dev python scripts/check.py<br>topClass is deprecated - use top_class<br> |
| just vendored-check | passed | True | AIMech:ParticleSwarmOptimization, AIMech:SimulatedAnnealing, AIMech:CrossEntropyOptimization | OK: 22 governed artifacts match the pinned claw revision<br>bash scripts/check_vendored_sync.sh<br> |
| Finite stochastic-optimization boundary calculations | passed | True | AIMech:ParticleSwarmOptimization, AIMech:SimulatedAnnealing, AIMech:CrossEntropyOptimization | {"pso_two_pull_velocity": 1.0, "pso_midpoint_displacement": 0.0, "pso_fixed_nonoptimal_position": 2.0, "pso_overshoot_position": 2.5, "annealing_uphill_probability_T2": 0.36787944117144233, "annealing_uphill_probability_T1": 0.1353352832366127, "equal_energy_uncorrected_stationary": [0.1, 0.9], "corrected_offdiagonal_probabilities": [0.1, 0.1], "ce_threshold": 2, "ce_elite_indices": [2, 3], "ce_bernoulli_fit": [1.0, 0.5], "ce_smoothed_fit": [0.75, 0.5], "ce_collapsed_probability_one": 0.0} |

## Scientific And Domain Assessments

### Identity, definition, mechanism, primary conventions and AIO assessment

evidence: supported. Targets: AIMech:ParticleSwarmOptimization.

The record describes continuous particle swarm optimization through the inspected global-best formulation. The 1995 simplified update retains the old velocity with coefficient 1 and uses two attraction coefficients equal to 2; the later inertia-weighted formulation is an explicit variant. It is not differential evolution, an objective-gradient method, a biological flock simulation, a trained neural network or an exact description of every discrete, neighborhood or constricted PSO variant. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 285 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 15 and 15 lines respectively. Every text hit was a prior candidate lead. Nine exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and seven native neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Initialize a population of real-valued positions and velocities and evaluate the objective. Retain each particle’s best evaluated position and the best position shared across the population. For each coordinate in the inspected global-best rule, add two randomly scaled displacements to the retained velocity: one from the current position toward the personal best and one toward the global best. The baseline is v_new=v+c1*r1*(p−x)+c2*r2*(g−x), followed by x_new=x+v_new; the source gives random factors in [0,1]. Evaluate the resulting positions and refresh the remembered bests when improved. Particles remain population members rather than undergoing target-trial survival selection. In the 1995 simplified version c1=c2=2. The 1999 inertia variant replaces the retained term v by w*v and studies a decreasing w schedule. Initialization, population size, coefficients, velocity limits, boundary treatment, update ordering and stopping rules must be specified for an executable configuration. Limits: Current positions can overshoot remembered bests and have worse objective values. Attraction to a best-so-far position is not attraction to a known global optimum. If every particle has zero velocity and its current position equals both remembered attractors, this displayed rule has no motion; the fixed state need not be optimal. The original coefficient 1 on old velocity and the later inertia weight must not be conflated. The 1999 experiment’s decreasing weight and Vmax/Xmax settings are particular choices, not universal optimal settings or a complete bound-repair specification. Clipping a velocity alone does not ensure a feasible position. The full random-stream coupling, synchronous versus asynchronous best updates, ties, constraints and noisy evaluations require declared implementation choices. The social analogy is not a convergence proof. The 1999 discussion explicitly allows failure to find the required optimum; no universal speed, accuracy or finite-budget global-optimum guarantee is asserted.

### Identity, definition, mechanism, primary conventions and AIO assessment

evidence: supported. Targets: AIMech:SimulatedAnnealing.

This record denotes the temperature-scheduled optimization procedure exemplified by Kirkpatrick, Gelatt and Vecchi. Its basic symmetric-proposal Metropolis step is distinguished from fixed-temperature target sampling, generic annealing metaphors, training signal annealing and a proof that a particular finite schedule reaches a global minimum. The 1983 article is a primary formulation, not a claim of exclusive invention. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 285 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 15 and 15 lines respectively. Every text hit was a prior candidate lead. Nine exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and seven native neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Choose a representation of feasible configurations, an objective E to minimize, a random rearrangement proposal and an annealing schedule specifying temperatures and work at each temperature. At current configuration x, propose y and compute delta=E(y)−E(x). For the basic symmetric-proposal Metropolis rule at effective temperature T&gt;0 measured in cost units, accept delta&lt;=0 moves and accept delta&gt;0 with probability exp(−delta/T); otherwise retain x. Repeat transitions at the current temperature, then lower temperature according to the schedule. High temperatures permit larger cost-increasing moves more frequently; cooling reduces that probability. The source motivates sufficient equilibration at each stage. Candidate representation, move set and schedule depend on the optimization problem; the returned low-cost configuration is a search result rather than a certified global minimizer. Curator qualification by substituting pi_T(x) proportional to exp(−E(x)/T) into Hastings’s Metropolis choice: when the target is proper and the ratio is defined, an asymmetric proposal requires acceptance min(1,exp(−delta/T)*q(x&#124;y)/q(y&#124;x)). The uncorrected exponential rule follows when the proposal ratio cancels. This fixed-temperature construction does not establish finite-schedule equilibration or annealing convergence. Limits: The exp(−delta/T) expression is for positive effective temperature with the physical Boltzmann constant absorbed into its cost units. Zero temperature is a limiting or separately defined greedy rule, not evaluation of that quotient at T=0. Equal-cost moves are accepted in the displayed symmetric-proposal rule. At fixed T the Boltzmann interpretation requires a proper target and a valid transition construction. Arbitrary asymmetric proposals do not justify dropping the reverse-to-forward proposal ratio. Lowering T changes the target; stationarity for a fixed stage does not imply equilibrium throughout a finite cooling run. Positive-temperature uphill acceptance only permits escape through moves supported by the proposal. It does not ensure reaching every state, escaping a local basin in a chosen budget or tracking equilibrium. Rapid cooling can freeze search prematurely; schedule length, cost scale, move connectivity and constraints matter. The primary article’s heuristics and empirical scaling claims are not a finite-run global-convergence theorem or a universal complexity bound. The later mathematical conditions for asymptotic annealing convergence were not audited here. No electronic-design or traveling-salesman benchmark is reproduced.

### Identity, definition, mechanism, primary conventions and AIO assessment

evidence: supported. Targets: AIMech:CrossEntropyOptimization.

This is the optimization branch of the cross-entropy method, represented by Algorithm2.3 in the inspected 2005 tutorial. It is distinct from the rare-event probability estimator, the cross-entropy loss used to train a classifier, NES natural-gradient steps, and CMA-ES evolution-path covariance adaptation. The sampling family and its fit define concrete instances; the generic algorithm is not limited to independent Bernoulli variables or a Gaussian implementation. No normalized identity match was found across all 442 pinned AIO labels/scoped synonyms and 285 preceding native IDs/names/aliases. Full-checkout fixed-string searches included ignored and hidden files in worktree and main, returning 15 and 15 lines respectively. Every text hit was a prior candidate lead. Nine exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and seven native neighboring mechanisms were inspected. Absence is bounded to this snapshot and semantic neighborhood.

Specify a sampling family f(x;v), initial parameter, sample size N, elite parameter rho and stopping rule. For maximization, draw candidates from the current distribution, evaluate their scores and choose the empirical (1−rho) quantile as threshold gamma. Fit new parameters by maximizing the sum of log f(x;v) over sampled candidates with score at least gamma. The optimization formulation uses unit weights: it redefines the associated stochastic problem at each iteration, so the rare-event algorithm’s nominal-to-current likelihood ratio is absent. Optionally smooth the fitted parameter toward the old one via v_new=alpha*v_fit+(1−alpha)*v_old. For independent Bernoulli coordinates, the unsmoothed fit is the coordinatewise fraction of ones among selected samples. Iterate until the chosen stopping condition; the displayed Algorithm2.3 uses an unchanged threshold over several iterations. The source’s cross-entropy derivation minimizes KL from the ideal selected-event distribution to the parameterized sampling distribution, not the reverse direction. Limits: A score&gt;=threshold rule need not select exactly rho*N candidates: order-statistic indexing and tied scores can increase the elite count. Implementations must state their quantile, tie and optimization-direction conventions; minimization requires the corresponding lower-score criterion or an equivalent score transformation. Unsmoothed finite-sample fitting can produce Bernoulli probabilities 0 or 1 and remove future exploration. Interior initialization and 0&lt;alpha&lt;1 prevent exact endpoints after a single convex smoothing step in exact arithmetic; smoothing alone does not guarantee exploration forever or a global optimum, and finite precision can still collapse support. The choice of sampling family, initial support, sample size, elite fraction, fit constraints and stopping rule matters. A stabilized threshold is not an optimality certificate; the source explicitly permits getting trapped at a local minimum and limits its asymptotic discussion. Maximum-likelihood fitting of selected candidates is a sampling-distribution update, not an unbiased gradient of raw expected fitness. It does not require derivatives of the black-box objective; solving the distribution fit may still require numerical optimization. No universal performance or convergence-rate claim is curated.

### Best-memory velocity dynamics, inertia and stagnation

consistency: supported. Targets: AIMech:ParticleSwarmOptimization.

Retain the global-best PSO account with a qualified later inertia variant.

The original two stochastic pulls update the retained velocity rather than replacing it. The later source explicitly gives the position update and multiplies the retained velocity by an inertia parameter. The record does not assign every random-stream, update-order or boundary convention from memory. Current costs need not improve, and a collapsed zero-velocity swarm can be fixed away from an optimum. Source performance language is not a universal guarantee.

### Cooling versus fixed-target sampling and proposal correction

consistency: supported. Targets: AIMech:SimulatedAnnealing.

Retain temperature-scheduled optimization, with the Hastings qualification explicitly attributed as curator reasoning.

The effective temperature absorbs the physical energy-unit conversion. The simple downhill/uphill rule uses symmetric proposals at positive temperature. The general ratio requires reverse/forward proposal correction for a Boltzmann stationary interpretation. Changing temperatures changes the target, so fixed-stage invariance does not establish equilibrium throughout cooling or a finite-run global optimum. Proposal connectivity and schedule choices remain limitations.

### Elite likelihood fitting, quantiles, weights and support loss

consistency: supported. Targets: AIMech:CrossEntropyOptimization.

Retain the optimization branch of the CE framework.

Algorithm2.3 sets W=1 because its associated problem changes each iteration; rare-event nominal-to-current ratios are not imported. The KL direction is ideal selected-event density to sampling family. The selected score&gt;=quantile set need not have exactly rho*N elements. Bernoulli fitting can remove support; smoothing with an interior old parameter only supplies a bounded algebraic protection, not a global-convergence certificate. This is distinct from a classifier loss and a natural-gradient update.

### Optimization procedures, learning tasks and stochastic models

grounding: supported. Targets: AIMech:ParticleSwarmOptimization, AIMech:SimulatedAnnealing, AIMech:CrossEntropyOptimization.

Retain distinct native algorithms with one qualified related match and two no-match assessments.

Inspected nine exact pinned AIO CLASS nodes, all their scoped synonyms/comments and outgoing edges, plus seven native records. Simulated annealing has a qualified algorithm-to-Markov-process related match through its Metropolis transitions; cooling does not preserve one fixed target over the full run. Particle swarm and cross-entropy optimization receive explicit bounded no-match assessments: neither is an evolutionary LLM, training task, predictive forest or bias; a possible augmented-state Markov representation alone is too generic to establish their semantic identity. The native DE, CMA-ES and NES records differ in difference-vector selection, cumulative Gaussian adaptation and natural-gradient updates; MH/RWMH target sampling, TSA supervises a loss schedule, and NT-Xent is a contrastive loss.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries

- retain: AIMech:ParticleSwarmOptimization, AIMech:SimulatedAnnealing, AIMech:CrossEntropyOptimization. Best-memory particle dynamics, cooling of Metropolis acceptance and elite-sample likelihood refitting have distinct states and update mechanisms. Shared random search, optimization applications or temperature/entropy vocabulary do not establish equivalence.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| identity | research/discovery/20261011T130537Z-swarm-annealing-and-crossentropy-search.json | supports | Compared all 442 pinned AIO labels/scoped synonyms and 285 preceding native IDs/names/aliases, including candidate-internal normalized uniqueness. No identity match was found. Full-checkout fixed-string searches included ignored/hidden files and returned 15 worktree and 15 main lines; every hit was a prior candidate lead. Nine exact AIO CLASS nodes with scoped synonyms/comments/outgoing edges and seven native neighboring records were inspected. Absence is bounded to this snapshot and semantic neighborhood. |
| mapping | sources/aio/aio.json; Nine exact CLASS nodes and their scoped synonyms/comments/outgoing edges in source_analysis.aio_mapping_inspection | supports | Inspected nine exact pinned AIO CLASS nodes, all their scoped synonyms/comments and outgoing edges, plus seven native records. Simulated annealing has a qualified algorithm-to-Markov-process related match through its Metropolis transitions; cooling does not preserve one fixed target over the full run. Particle swarm and cross-entropy optimization receive explicit bounded no-match assessments: neither is an evolutionary LLM, training task, predictive forest or bias; a possible augmented-state Markov representation alone is too generic to establish their semantic identity. The native DE, CMA-ES and NES records differ in difference-vector selection, cumulative Gaussian adaptation and natural-gradient updates; MH/RWMH target sampling, TSA supervises a loss schedule, and NT-Xent is a contrastive loss. |
| neighbors | research/discovery/20261011T130537Z-swarm-annealing-and-crossentropy-search.json; source_analysis.aio_mapping_inspection.native_neighbors | supports | Read Differential Evolution, CMA-ES, NES, Metropolis–Hastings, random-walk Metropolis–Hastings, Training signal annealing and NT-Xent. Distinguish particle motion, sampling-distribution fitting, fixed-target sampling, supervised loss schedules and contrastive loss definitions. |
| finite-conventions | research/discovery/stochastic-optimization-boundaries.py; calculate(): particle overshoot/fixed states, thermal acceptance and proposal correction, elite quantiles and Bernoulli support | supports | Original finite arithmetic checks PSO stochastic pulls, overshoot and a nonoptimal fixed state; temperature dependence and asymmetric-proposal balance; and CE quantile counts, Bernoulli fitting, smoothing and loss of support. These are illustrative calculations, not author algorithms or benchmark runs. |
| particleswarmoptimization-source-0 | https://staff.washington.edu/paymana/swarm/kennedy95-ijcnn.pdf; Sections3.2–3.7, PDF pp.3–5 / printed1944–1946; Sections5–6, PDF pp.6–7 / printed1947–1948 | supports | Particle Swarm Optimization. Proceedings of ICNN 1995, volume4, pp.1942–1948; seven-page scanned conference article. Actual text/OCR/image reading scopes are declared in the ledger. Source rendering alone does not attest inspection. |
| particleswarmoptimization-source-1 | https://staff.washington.edu/paymana/swarm/shi99-cec.pdf; Introduction, Equations1a–1b and2a–2b, PDF pp.1–2 / printed1945–1946; experimental settings and discussion/conclusion, PDF pp.3–4 / printed1947–1948 | supports | Empirical Study of Particle Swarm Optimization. Proceedings of the 1999 Congress on Evolutionary Computation, pp.1945–1950; six-page scanned conference article. Actual text/OCR/image reading scopes are declared in the ledger. Source rendering alone does not attest inspection. |
| simulatedannealing-source-0 | https://hedibert.org/wp-content/uploads/2013/12/1983KirkpatrickGelattVecchi.pdf; Statistical Mechanics, PDF pp.3–4 / printed672–673; Statistical Mechanics, PDF pp.3–4 / printed672–673, Metropolis acceptance and cooling schedule; Summary and Conclusions, PDFp.10 / printed679 | supports | Optimization by Simulated Annealing. Science 220(4598):671–680, May 13, 1983; public hosted scan with cover at PDF1, article beginning at PDF2 and next unrelated article sharing PDF11. Actual text/OCR/image reading scopes are declared in the ledger. Source rendering alone does not attest inspection. |
| simulatedannealing-source-1 | https://probability.ca/hastings/hastings.pdf; Section2.2, PDF pp.3–5 / printed99–101 | supports | Monte Carlo sampling methods using Markov chains and their applications. Biometrika 57(1), 1970, printed pp. 97–109; 13-page published scan hosted by probability.ca. Actual text/OCR/image reading scopes are declared in the ledger. Source rendering alone does not attest inspection. |
| crossentropyoptimization-source-0 | https://people.smp.uq.edu.au/DirkKroese/ps/aortut.pdf; Section2.2, Algorithm2.3 and Remarks2.3–2.6, PDF pp.15–19 / printed33–37; Equation20, PDFp.12 / printed30; KL direction in Section2.1, PDF pp.10–11; discussion PDFp.46 / printed64 | supports | A Tutorial on the Cross-Entropy Method. Annals of Operations Research 134:19–67, 2005; 49-page published article hosted by Dirk Kroese; distinct from the September 2003 manuscript. Actual text/OCR/image reading scopes are declared in the ledger. Source rendering alone does not attest inspection. |

## Limits And Additional Notes

- Adversarial author self-review only; every record remains DRAFT.
- Only declared text/OCR/image pages were inspected. No training, benchmark, author-code execution or asymptotic-convergence proof audit was performed.
- PSO1995 was read through OCR with critical equation verification; PSO1999 was read directly through page images. Some companion-source opens failed, and unresolved variants remain discovery leads.
- Three additions and a nonempty inherited/new frontier leave discovery active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T130831Z-swarm-annealing-and-crossentropy-search
kind: batch
repository: CultureBotAI/AIMech
title: Scientific self-review of swarm, annealing and cross-entropy search
started_at: '2026-10-11T13:07:35Z'
finished_at: '2026-10-11T13:08:31Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-6
  independence: self_review
  independence_basis: The authoring agent adversarially reviewed all three records
    against declared primary methods, OCR and verified page images, the Hastings proposal
    construction, nine exact AIO nodes, seven native neighbors and original finite
    arithmetic. This is not independent approval.
skill: .claude/skills/review-category/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Retain PSO, simulated annealing and cross-entropy optimization with explicit
  source conventions, optimization/sampling distinctions and bounded AIO assessments.
  No actionable record defect was found in this scope.
source:
  git_revision: 886d146bca59db1de4a786c056fba5fd34fb818f
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
  - path: data/aio/MarkovChain.yaml
    sha256: 6a75421c39c34870654b6fff197be8f670b7d03e173f1cdcb85109c208efe67b
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
  - path: data/curated/CovarianceMatrixAdaptationEvolutionStrategy.yaml
    sha256: 7018c9916e78f34ba32a3a9d46e694d2a78c17a6e7222d9050d305eedf96ed06
    role: context
  - path: data/curated/CrossEntropyOptimization.yaml
    sha256: b2d993224f56b48738bbecc23df28fe0bc1e16e54c658979fdd28fc1924ba269
    role: target
  - path: data/curated/DifferentialEvolution.yaml
    sha256: 8c937f585818445a809f6aa26c51c4195e1fe2e3a634d349762322f89e97ff68
    role: context
  - path: data/curated/MetropolisHastings.yaml
    sha256: 01cb22a25242e8564e2a7bb839ecb46da1bc49eb09b3c85200f9a596e05b99b4
    role: context
  - path: data/curated/NTXentLoss.yaml
    sha256: 523d119e71f1c16672b42300e2a180495f3a09c53a55385f546f02850fed3255
    role: context
  - path: data/curated/NaturalEvolutionStrategies.yaml
    sha256: b11c8d02da55175afcf5d5c11cf91a864418d7396b726f423f865d95cfe76a4c
    role: context
  - path: data/curated/ParticleSwarmOptimization.yaml
    sha256: bd0c2298ecb01d94702f09f6ef1766c3b51216b4a4dbca9ae1c99142f5807d08
    role: target
  - path: data/curated/RandomWalkMetropolisHastings.yaml
    sha256: aeff822517db546b4e3dee3421a54d5887ed178f3b9e6e3df46283eceb39677d
    role: context
  - path: data/curated/SimulatedAnnealing.yaml
    sha256: 7e77f553c8b2afc4563dc7ef6cba2b53719f22b1fd02ed37d22de9821079d42c
    role: target
  - path: data/curated/TrainingSignalAnnealing.yaml
    sha256: d4450649d1cbe8afa01e72e9dddee4fe14893497a820d7a3e8089d594a9d095a
    role: context
  - path: research/discovery/20261011T130537Z-swarm-annealing-and-crossentropy-search.json
    sha256: c7310aebeaf968283439a775de11c6f1aa7326b42d10bf328d2d4f2427baa8d8
    role: context
  - path: research/discovery/stochastic-optimization-boundaries.py
    sha256: ef75dc56db8c969b8920f8ac2ffe171fbaebffcf581bf8d6d6d31b873d8a9601
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
- target_id: AIMech:ParticleSwarmOptimization
  path: data/curated/ParticleSwarmOptimization.yaml
  label: Particle swarm optimization
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/ParticleSwarmOptimization.yaml
    role: maintained
- target_id: AIMech:SimulatedAnnealing
  path: data/curated/SimulatedAnnealing.yaml
  label: Simulated annealing
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/SimulatedAnnealing.yaml
    role: maintained
- target_id: AIMech:CrossEntropyOptimization
  path: data/curated/CrossEntropyOptimization.yaml
  label: Cross-entropy optimization
  kind: maintained
  record_class: CuratedAIConcept
  owner_paths:
  - repository: CultureBotAI/AIMech
    path: data/curated/CrossEntropyOptimization.yaml
    role: maintained
scope:
  description: All fields of the three newly maintained stochastic optimization records.
  selection: Exact three IDs in the discovery ledger; no sampling.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - AIMech:ParticleSwarmOptimization
  - AIMech:SimulatedAnnealing
  - AIMech:CrossEntropyOptimization
  exclusions:
  - target: Older records and unselected candidates
    reason: Neighbors were inspected for boundaries, not a complete new review of
      the earlier corpus.
  - target: Unread pages, proofs, outcomes and implementations
    reason: Only declared primary-source pages and finite curator calculations were
      inspected. No author code or model was executed.
checks:
- check_id: required-0
  name: just check
  command: just check
  status: passed
  required: true
  target_ids:
  - AIMech:ParticleSwarmOptimization
  - AIMech:SimulatedAnnealing
  - AIMech:CrossEntropyOptimization
  exit_code: 0
  expected_exit_code: 0
  summary: "All checks passed!\n........................................................................\
    \ [ 29%]\n........................................................................\
    \ [ 59%]\n........................................................................\
    \ [ 89%]\n.......................sss                                         \
    \      [100%]\n239 passed, 3 skipped in 83.12s (0:01:23)\nChecked 442 record(s);\
    \ 0 failed.\nChecked 288 curated concept record(s); 0 error(s).\nAIO: 442 records;\
    \ 0 missing, 0 changed, 0 unexpected.\nChecked 71 history record(s); 0 error(s).\n\
    {\n  \"repository\": \"CultureBotAI/AIMech\",\n  \"valid_reviews\": 69,\n  \"\
    coverage\": \"declared_scopes_only\"\n}\nuv run --locked --extra dev python scripts/check.py\n\
    topClass is deprecated - use top_class\n"
- check_id: required-1
  name: just vendored-check
  command: just vendored-check
  status: passed
  required: true
  target_ids:
  - AIMech:ParticleSwarmOptimization
  - AIMech:SimulatedAnnealing
  - AIMech:CrossEntropyOptimization
  exit_code: 0
  expected_exit_code: 0
  summary: 'OK: 22 governed artifacts match the pinned claw revision

    bash scripts/check_vendored_sync.sh

    '
- check_id: finite-arithmetic
  name: Finite stochastic-optimization boundary calculations
  command: python3 research/discovery/stochastic-optimization-boundaries.py
  status: passed
  required: true
  target_ids:
  - AIMech:ParticleSwarmOptimization
  - AIMech:SimulatedAnnealing
  - AIMech:CrossEntropyOptimization
  exit_code: 0
  expected_exit_code: 0
  summary: '{"pso_two_pull_velocity": 1.0, "pso_midpoint_displacement": 0.0, "pso_fixed_nonoptimal_position":
    2.0, "pso_overshoot_position": 2.5, "annealing_uphill_probability_T2": 0.36787944117144233,
    "annealing_uphill_probability_T1": 0.1353352832366127, "equal_energy_uncorrected_stationary":
    [0.1, 0.9], "corrected_offdiagonal_probabilities": [0.1, 0.1], "ce_threshold":
    2, "ce_elite_indices": [2, 3], "ce_bernoulli_fit": [1.0, 0.5], "ce_smoothed_fit":
    [0.75, 0.5], "ce_collapsed_probability_one": 0.0}'
evidence:
- evidence_id: identity
  kind: search
  reference: research/discovery/20261011T130537Z-swarm-annealing-and-crossentropy-search.json
  accessed_at: '2026-10-11T13:07:35Z'
  support: supports
  summary: Compared all 442 pinned AIO labels/scoped synonyms and 285 preceding native
    IDs/names/aliases, including candidate-internal normalized uniqueness. No identity
    match was found. Full-checkout fixed-string searches included ignored/hidden files
    and returned 15 worktree and 15 main lines; every hit was a prior candidate lead.
    Nine exact AIO CLASS nodes with scoped synonyms/comments/outgoing edges and seven
    native neighboring records were inspected. Absence is bounded to this snapshot
    and semantic neighborhood.
  search_scope: All 442 pinned AIO labels/scoped synonyms and 285 preceding maintained
    IDs/names/aliases; full checkouts including ignored/hidden files; candidate-internal
    normalized uniqueness.
- evidence_id: mapping
  kind: record_content
  reference: sources/aio/aio.json
  locator: Nine exact CLASS nodes and their scoped synonyms/comments/outgoing edges
    in source_analysis.aio_mapping_inspection
  accessed_at: '2026-10-11T13:07:35Z'
  support: supports
  summary: 'Inspected nine exact pinned AIO CLASS nodes, all their scoped synonyms/comments
    and outgoing edges, plus seven native records. Simulated annealing has a qualified
    algorithm-to-Markov-process related match through its Metropolis transitions;
    cooling does not preserve one fixed target over the full run. Particle swarm and
    cross-entropy optimization receive explicit bounded no-match assessments: neither
    is an evolutionary LLM, training task, predictive forest or bias; a possible augmented-state
    Markov representation alone is too generic to establish their semantic identity.
    The native DE, CMA-ES and NES records differ in difference-vector selection, cumulative
    Gaussian adaptation and natural-gradient updates; MH/RWMH target sampling, TSA
    supervises a loss schedule, and NT-Xent is a contrastive loss.'
- evidence_id: neighbors
  kind: record_content
  reference: research/discovery/20261011T130537Z-swarm-annealing-and-crossentropy-search.json
  locator: source_analysis.aio_mapping_inspection.native_neighbors
  accessed_at: '2026-10-11T13:07:35Z'
  support: supports
  summary: Read Differential Evolution, CMA-ES, NES, Metropolis–Hastings, random-walk
    Metropolis–Hastings, Training signal annealing and NT-Xent. Distinguish particle
    motion, sampling-distribution fitting, fixed-target sampling, supervised loss
    schedules and contrastive loss definitions.
- evidence_id: finite-conventions
  kind: record_content
  reference: research/discovery/stochastic-optimization-boundaries.py
  locator: 'calculate(): particle overshoot/fixed states, thermal acceptance and proposal
    correction, elite quantiles and Bernoulli support'
  accessed_at: '2026-10-11T13:07:35Z'
  snapshot_sha256: ef75dc56db8c969b8920f8ac2ffe171fbaebffcf581bf8d6d6d31b873d8a9601
  support: supports
  summary: Original finite arithmetic checks PSO stochastic pulls, overshoot and a
    nonoptimal fixed state; temperature dependence and asymmetric-proposal balance;
    and CE quantile counts, Bernoulli fitting, smoothing and loss of support. These
    are illustrative calculations, not author algorithms or benchmark runs.
- evidence_id: particleswarmoptimization-source-0
  kind: primary_source
  reference: https://staff.washington.edu/paymana/swarm/kennedy95-ijcnn.pdf
  locator: Sections3.2–3.7, PDF pp.3–5 / printed1944–1946; Sections5–6, PDF pp.6–7
    / printed1947–1948
  accessed_at: '2026-10-11T12:53:34Z'
  snapshot_sha256: af61c5180e5d63fa57e8f601852f9173d3f88c779008d4a2b5f33bb53dd81e64
  support: supports
  summary: Particle Swarm Optimization. Proceedings of ICNN 1995, volume4, pp.1942–1948;
    seven-page scanned conference article. Actual text/OCR/image reading scopes are
    declared in the ledger. Source rendering alone does not attest inspection.
- evidence_id: particleswarmoptimization-source-1
  kind: primary_source
  reference: https://staff.washington.edu/paymana/swarm/shi99-cec.pdf
  locator: Introduction, Equations1a–1b and2a–2b, PDF pp.1–2 / printed1945–1946; experimental
    settings and discussion/conclusion, PDF pp.3–4 / printed1947–1948
  accessed_at: '2026-10-11T13:00:32Z'
  snapshot_sha256: ee6ea14234d00a0d2c38ede44159ebc42bf30f40a8a49a2e2cfc150ac1675c64
  support: supports
  summary: Empirical Study of Particle Swarm Optimization. Proceedings of the 1999
    Congress on Evolutionary Computation, pp.1945–1950; six-page scanned conference
    article. Actual text/OCR/image reading scopes are declared in the ledger. Source
    rendering alone does not attest inspection.
- evidence_id: simulatedannealing-source-0
  kind: primary_source
  reference: https://hedibert.org/wp-content/uploads/2013/12/1983KirkpatrickGelattVecchi.pdf
  locator: Statistical Mechanics, PDF pp.3–4 / printed672–673; Statistical Mechanics,
    PDF pp.3–4 / printed672–673, Metropolis acceptance and cooling schedule; Summary
    and Conclusions, PDFp.10 / printed679
  accessed_at: '2026-10-11T12:53:34Z'
  snapshot_sha256: 06f76ea70632b7e2a87e86d0484a936da3bcbd4050355010c2b2934cba999e6c
  support: supports
  summary: Optimization by Simulated Annealing. Science 220(4598):671–680, May 13,
    1983; public hosted scan with cover at PDF1, article beginning at PDF2 and next
    unrelated article sharing PDF11. Actual text/OCR/image reading scopes are declared
    in the ledger. Source rendering alone does not attest inspection.
- evidence_id: simulatedannealing-source-1
  kind: primary_source
  reference: https://probability.ca/hastings/hastings.pdf
  locator: Section2.2, PDF pp.3–5 / printed99–101
  accessed_at: '2026-10-11T06:40:06Z'
  snapshot_sha256: dc620d3651d30029729646649e9a26780f1a415d7fd251433b6a270a143de47c
  support: supports
  summary: Monte Carlo sampling methods using Markov chains and their applications.
    Biometrika 57(1), 1970, printed pp. 97–109; 13-page published scan hosted by probability.ca.
    Actual text/OCR/image reading scopes are declared in the ledger. Source rendering
    alone does not attest inspection.
- evidence_id: crossentropyoptimization-source-0
  kind: primary_source
  reference: https://people.smp.uq.edu.au/DirkKroese/ps/aortut.pdf
  locator: Section2.2, Algorithm2.3 and Remarks2.3–2.6, PDF pp.15–19 / printed33–37;
    Equation20, PDFp.12 / printed30; KL direction in Section2.1, PDF pp.10–11; discussion
    PDFp.46 / printed64
  accessed_at: '2026-10-11T12:53:34Z'
  snapshot_sha256: f68c734c278951aef659e8e4a984af80390c83daf06f76b500c6a37f10b3ff78
  support: supports
  summary: A Tutorial on the Cross-Entropy Method. Annals of Operations Research 134:19–67,
    2005; 49-page published article hosted by Dirk Kroese; distinct from the September
    2003 manuscript. Actual text/OCR/image reading scopes are declared in the ledger.
    Source rendering alone does not attest inspection.
assessments:
- assessment_id: particleswarmoptimization
  area: evidence
  topic: Identity, definition, mechanism, primary conventions and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:ParticleSwarmOptimization
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - particleswarmoptimization-source-0
  - particleswarmoptimization-source-1
  summary: The record describes continuous particle swarm optimization through the
    inspected global-best formulation. The 1995 simplified update retains the old
    velocity with coefficient 1 and uses two attraction coefficients equal to 2; the
    later inertia-weighted formulation is an explicit variant. It is not differential
    evolution, an objective-gradient method, a biological flock simulation, a trained
    neural network or an exact description of every discrete, neighborhood or constricted
    PSO variant. No normalized identity match was found across all 442 pinned AIO
    labels/scoped synonyms and 285 preceding native IDs/names/aliases. Full-checkout
    fixed-string searches included ignored and hidden files in worktree and main,
    returning 15 and 15 lines respectively. Every text hit was a prior candidate lead.
    Nine exact AIO CLASS nodes with scoped synonyms/comments and outgoing edges and
    seven native neighboring mechanisms were inspected. Absence is bounded to this
    snapshot and semantic neighborhood.
  details: 'Initialize a population of real-valued positions and velocities and evaluate
    the objective. Retain each particle’s best evaluated position and the best position
    shared across the population. For each coordinate in the inspected global-best
    rule, add two randomly scaled displacements to the retained velocity: one from
    the current position toward the personal best and one toward the global best.
    The baseline is v_new=v+c1*r1*(p−x)+c2*r2*(g−x), followed by x_new=x+v_new; the
    source gives random factors in [0,1]. Evaluate the resulting positions and refresh
    the remembered bests when improved. Particles remain population members rather
    than undergoing target-trial survival selection. In the 1995 simplified version
    c1=c2=2. The 1999 inertia variant replaces the retained term v by w*v and studies
    a decreasing w schedule. Initialization, population size, coefficients, velocity
    limits, boundary treatment, update ordering and stopping rules must be specified
    for an executable configuration. Limits: Current positions can overshoot remembered
    bests and have worse objective values. Attraction to a best-so-far position is
    not attraction to a known global optimum. If every particle has zero velocity
    and its current position equals both remembered attractors, this displayed rule
    has no motion; the fixed state need not be optimal. The original coefficient 1
    on old velocity and the later inertia weight must not be conflated. The 1999 experiment’s
    decreasing weight and Vmax/Xmax settings are particular choices, not universal
    optimal settings or a complete bound-repair specification. Clipping a velocity
    alone does not ensure a feasible position. The full random-stream coupling, synchronous
    versus asynchronous best updates, ties, constraints and noisy evaluations require
    declared implementation choices. The social analogy is not a convergence proof.
    The 1999 discussion explicitly allows failure to find the required optimum; no
    universal speed, accuracy or finite-budget global-optimum guarantee is asserted.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: An optimization procedure with explicit state, proposal/update mechanism
      and source-specific scope, not a trained model instance.
    evidence_ids:
    - particleswarmoptimization-source-0
    - particleswarmoptimization-source-1
  - name: aio-relations
    value: aio_no_match
    definition: No suitable mapping was found for this general optimization method
      in the inspected pin. Learning tasks, evolutionary language models, predictive
      forests, bias concepts and a generic stochastic-process representation do not
      establish the defining identity. This is a bounded local assessment, not a claim
      of absence from other ontologies. This exact CLASS is a large language model
      using evolutionary computation. Its related synonym evolutionary algorithms
      does not denote every stochastic optimizer or establish model equivalence. The
      definition concerns preprocessing/training machine-learning models. Optional
      neural-network or policy optimization applications do not define the full general
      optimization method. General objective optimization is not necessarily a task
      of learning from data as in this target. Updating optimizer state or a search
      distribution is not necessarily learning from metadata about machine-learning
      experiments. Objective evaluation does not require querying labels for data
      points. These general optimizers do not inherently specify a policy/environment
      learning task; a possible use in policy search is insufficient. Neither particle
      memory nor an adaptive sampling distribution is a predictive decision-tree ensemble.
      This class describes evaluation population/metric bias rather than an optimization
      algorithm. A possible augmented-state Markov representation is too generic to
      identify this optimizer. The inspected defining operation is particle motion
      or elite-distribution refitting, not construction of a target-invariant Markov
      sampler; the pinned network/model is not an equivalent or necessary semantic
      parent.
    evidence_ids:
    - mapping
- assessment_id: simulatedannealing
  area: evidence
  topic: Identity, definition, mechanism, primary conventions and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:SimulatedAnnealing
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - simulatedannealing-source-0
  - simulatedannealing-source-1
  summary: This record denotes the temperature-scheduled optimization procedure exemplified
    by Kirkpatrick, Gelatt and Vecchi. Its basic symmetric-proposal Metropolis step
    is distinguished from fixed-temperature target sampling, generic annealing metaphors,
    training signal annealing and a proof that a particular finite schedule reaches
    a global minimum. The 1983 article is a primary formulation, not a claim of exclusive
    invention. No normalized identity match was found across all 442 pinned AIO labels/scoped
    synonyms and 285 preceding native IDs/names/aliases. Full-checkout fixed-string
    searches included ignored and hidden files in worktree and main, returning 15
    and 15 lines respectively. Every text hit was a prior candidate lead. Nine exact
    AIO CLASS nodes with scoped synonyms/comments and outgoing edges and seven native
    neighboring mechanisms were inspected. Absence is bounded to this snapshot and
    semantic neighborhood.
  details: 'Choose a representation of feasible configurations, an objective E to
    minimize, a random rearrangement proposal and an annealing schedule specifying
    temperatures and work at each temperature. At current configuration x, propose
    y and compute delta=E(y)−E(x). For the basic symmetric-proposal Metropolis rule
    at effective temperature T>0 measured in cost units, accept delta<=0 moves and
    accept delta>0 with probability exp(−delta/T); otherwise retain x. Repeat transitions
    at the current temperature, then lower temperature according to the schedule.
    High temperatures permit larger cost-increasing moves more frequently; cooling
    reduces that probability. The source motivates sufficient equilibration at each
    stage. Candidate representation, move set and schedule depend on the optimization
    problem; the returned low-cost configuration is a search result rather than a
    certified global minimizer. Curator qualification by substituting pi_T(x) proportional
    to exp(−E(x)/T) into Hastings’s Metropolis choice: when the target is proper and
    the ratio is defined, an asymmetric proposal requires acceptance min(1,exp(−delta/T)*q(x|y)/q(y|x)).
    The uncorrected exponential rule follows when the proposal ratio cancels. This
    fixed-temperature construction does not establish finite-schedule equilibration
    or annealing convergence. Limits: The exp(−delta/T) expression is for positive
    effective temperature with the physical Boltzmann constant absorbed into its cost
    units. Zero temperature is a limiting or separately defined greedy rule, not evaluation
    of that quotient at T=0. Equal-cost moves are accepted in the displayed symmetric-proposal
    rule. At fixed T the Boltzmann interpretation requires a proper target and a valid
    transition construction. Arbitrary asymmetric proposals do not justify dropping
    the reverse-to-forward proposal ratio. Lowering T changes the target; stationarity
    for a fixed stage does not imply equilibrium throughout a finite cooling run.
    Positive-temperature uphill acceptance only permits escape through moves supported
    by the proposal. It does not ensure reaching every state, escaping a local basin
    in a chosen budget or tracking equilibrium. Rapid cooling can freeze search prematurely;
    schedule length, cost scale, move connectivity and constraints matter. The primary
    article’s heuristics and empirical scaling claims are not a finite-run global-convergence
    theorem or a universal complexity bound. The later mathematical conditions for
    asymptotic annealing convergence were not audited here. No electronic-design or
    traveling-salesman benchmark is reproduced.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: An optimization procedure with explicit state, proposal/update mechanism
      and source-specific scope, not a trained model instance.
    evidence_ids:
    - simulatedannealing-source-0
    - simulatedannealing-source-1
  - name: aio-relations
    value: 'related_match: AIO:MarkovChain'
    definition: Simulated annealing uses Metropolis transitions at a sequence of temperatures.
      The pinned AIO target denotes a stochastic process/model and is exported beneath
      Network; this algorithm-to-process relation is not equivalence or an is-a assertion.
      A fixed cooling schedule gives time-dependent transitions, and changing temperature
      does not preserve a single stationary Boltzmann target throughout the run.
    evidence_ids:
    - mapping
- assessment_id: crossentropyoptimization
  area: evidence
  topic: Identity, definition, mechanism, primary conventions and AIO assessment
  outcome: supported
  target_ids:
  - AIMech:CrossEntropyOptimization
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - crossentropyoptimization-source-0
  summary: This is the optimization branch of the cross-entropy method, represented
    by Algorithm2.3 in the inspected 2005 tutorial. It is distinct from the rare-event
    probability estimator, the cross-entropy loss used to train a classifier, NES
    natural-gradient steps, and CMA-ES evolution-path covariance adaptation. The sampling
    family and its fit define concrete instances; the generic algorithm is not limited
    to independent Bernoulli variables or a Gaussian implementation. No normalized
    identity match was found across all 442 pinned AIO labels/scoped synonyms and
    285 preceding native IDs/names/aliases. Full-checkout fixed-string searches included
    ignored and hidden files in worktree and main, returning 15 and 15 lines respectively.
    Every text hit was a prior candidate lead. Nine exact AIO CLASS nodes with scoped
    synonyms/comments and outgoing edges and seven native neighboring mechanisms were
    inspected. Absence is bounded to this snapshot and semantic neighborhood.
  details: 'Specify a sampling family f(x;v), initial parameter, sample size N, elite
    parameter rho and stopping rule. For maximization, draw candidates from the current
    distribution, evaluate their scores and choose the empirical (1−rho) quantile
    as threshold gamma. Fit new parameters by maximizing the sum of log f(x;v) over
    sampled candidates with score at least gamma. The optimization formulation uses
    unit weights: it redefines the associated stochastic problem at each iteration,
    so the rare-event algorithm’s nominal-to-current likelihood ratio is absent. Optionally
    smooth the fitted parameter toward the old one via v_new=alpha*v_fit+(1−alpha)*v_old.
    For independent Bernoulli coordinates, the unsmoothed fit is the coordinatewise
    fraction of ones among selected samples. Iterate until the chosen stopping condition;
    the displayed Algorithm2.3 uses an unchanged threshold over several iterations.
    The source’s cross-entropy derivation minimizes KL from the ideal selected-event
    distribution to the parameterized sampling distribution, not the reverse direction.
    Limits: A score>=threshold rule need not select exactly rho*N candidates: order-statistic
    indexing and tied scores can increase the elite count. Implementations must state
    their quantile, tie and optimization-direction conventions; minimization requires
    the corresponding lower-score criterion or an equivalent score transformation.
    Unsmoothed finite-sample fitting can produce Bernoulli probabilities 0 or 1 and
    remove future exploration. Interior initialization and 0<alpha<1 prevent exact
    endpoints after a single convex smoothing step in exact arithmetic; smoothing
    alone does not guarantee exploration forever or a global optimum, and finite precision
    can still collapse support. The choice of sampling family, initial support, sample
    size, elite fraction, fit constraints and stopping rule matters. A stabilized
    threshold is not an optimality certificate; the source explicitly permits getting
    trapped at a local minimum and limits its asymptotic discussion. Maximum-likelihood
    fitting of selected candidates is a sampling-distribution update, not an unbiased
    gradient of raw expected fitness. It does not require derivatives of the black-box
    objective; solving the distribution fit may still require numerical optimization.
    No universal performance or convergence-rate claim is curated.'
  dimensions:
  - name: concept-kind
    value: algorithm
    definition: An optimization procedure with explicit state, proposal/update mechanism
      and source-specific scope, not a trained model instance.
    evidence_ids:
    - crossentropyoptimization-source-0
  - name: aio-relations
    value: aio_no_match
    definition: No suitable mapping was found for this general optimization method
      in the inspected pin. Learning tasks, evolutionary language models, predictive
      forests, bias concepts and a generic stochastic-process representation do not
      establish the defining identity. This is a bounded local assessment, not a claim
      of absence from other ontologies. This exact CLASS is a large language model
      using evolutionary computation. Its related synonym evolutionary algorithms
      does not denote every stochastic optimizer or establish model equivalence. The
      definition concerns preprocessing/training machine-learning models. Optional
      neural-network or policy optimization applications do not define the full general
      optimization method. General objective optimization is not necessarily a task
      of learning from data as in this target. Updating optimizer state or a search
      distribution is not necessarily learning from metadata about machine-learning
      experiments. Objective evaluation does not require querying labels for data
      points. These general optimizers do not inherently specify a policy/environment
      learning task; a possible use in policy search is insufficient. Neither particle
      memory nor an adaptive sampling distribution is a predictive decision-tree ensemble.
      This class describes evaluation population/metric bias rather than an optimization
      algorithm. A possible augmented-state Markov representation is too generic to
      identify this optimizer. The inspected defining operation is particle motion
      or elite-distribution refitting, not construction of a target-invariant Markov
      sampler; the pinned network/model is not an equivalent or necessary semantic
      parent.
    evidence_ids:
    - mapping
- assessment_id: pso-boundaries
  area: consistency
  topic: Best-memory velocity dynamics, inertia and stagnation
  outcome: supported
  target_ids:
  - AIMech:ParticleSwarmOptimization
  evidence_ids:
  - particleswarmoptimization-source-0
  - particleswarmoptimization-source-1
  - finite-conventions
  - neighbors
  summary: Retain the global-best PSO account with a qualified later inertia variant.
  details: The original two stochastic pulls update the retained velocity rather than
    replacing it. The later source explicitly gives the position update and multiplies
    the retained velocity by an inertia parameter. The record does not assign every
    random-stream, update-order or boundary convention from memory. Current costs
    need not improve, and a collapsed zero-velocity swarm can be fixed away from an
    optimum. Source performance language is not a universal guarantee.
- assessment_id: annealing-boundaries
  area: consistency
  topic: Cooling versus fixed-target sampling and proposal correction
  outcome: supported
  target_ids:
  - AIMech:SimulatedAnnealing
  evidence_ids:
  - simulatedannealing-source-0
  - simulatedannealing-source-1
  - finite-conventions
  - neighbors
  summary: Retain temperature-scheduled optimization, with the Hastings qualification
    explicitly attributed as curator reasoning.
  details: The effective temperature absorbs the physical energy-unit conversion.
    The simple downhill/uphill rule uses symmetric proposals at positive temperature.
    The general ratio requires reverse/forward proposal correction for a Boltzmann
    stationary interpretation. Changing temperatures changes the target, so fixed-stage
    invariance does not establish equilibrium throughout cooling or a finite-run global
    optimum. Proposal connectivity and schedule choices remain limitations.
- assessment_id: ce-boundaries
  area: consistency
  topic: Elite likelihood fitting, quantiles, weights and support loss
  outcome: supported
  target_ids:
  - AIMech:CrossEntropyOptimization
  evidence_ids:
  - crossentropyoptimization-source-0
  - finite-conventions
  - neighbors
  summary: Retain the optimization branch of the CE framework.
  details: Algorithm2.3 sets W=1 because its associated problem changes each iteration;
    rare-event nominal-to-current ratios are not imported. The KL direction is ideal
    selected-event density to sampling family. The selected score>=quantile set need
    not have exactly rho*N elements. Bernoulli fitting can remove support; smoothing
    with an interior old parameter only supplies a bounded algebraic protection, not
    a global-convergence certificate. This is distinct from a classifier loss and
    a natural-gradient update.
- assessment_id: mapping-boundaries
  area: grounding
  topic: Optimization procedures, learning tasks and stochastic models
  outcome: supported
  target_ids:
  - AIMech:ParticleSwarmOptimization
  - AIMech:SimulatedAnnealing
  - AIMech:CrossEntropyOptimization
  evidence_ids:
  - identity
  - mapping
  - neighbors
  summary: Retain distinct native algorithms with one qualified related match and
    two no-match assessments.
  details: 'Inspected nine exact pinned AIO CLASS nodes, all their scoped synonyms/comments
    and outgoing edges, plus seven native records. Simulated annealing has a qualified
    algorithm-to-Markov-process related match through its Metropolis transitions;
    cooling does not preserve one fixed target over the full run. Particle swarm and
    cross-entropy optimization receive explicit bounded no-match assessments: neither
    is an evolutionary LLM, training task, predictive forest or bias; a possible augmented-state
    Markov representation alone is too generic to establish their semantic identity.
    The native DE, CMA-ES and NES records differ in difference-vector selection, cumulative
    Gaussian adaptation and natural-gradient updates; MH/RWMH target sampling, TSA
    supervises a loss schedule, and NT-Xent is a contrastive loss.'
findings: []
actions: []
boundary_decisions:
- action: retain
  target_ids:
  - AIMech:ParticleSwarmOptimization
  - AIMech:SimulatedAnnealing
  - AIMech:CrossEntropyOptimization
  evidence_ids:
  - identity
  - mapping
  - neighbors
  - finite-conventions
  - particleswarmoptimization-source-0
  - particleswarmoptimization-source-1
  - simulatedannealing-source-0
  - simulatedannealing-source-1
  - crossentropyoptimization-source-0
  rationale: Best-memory particle dynamics, cooling of Metropolis acceptance and elite-sample
    likelihood refitting have distinct states and update mechanisms. Shared random
    search, optimization applications or temperature/entropy vocabulary do not establish
    equivalence.
limitations:
- Adversarial author self-review only; every record remains DRAFT.
- Only declared text/OCR/image pages were inspected. No training, benchmark, author-code
  execution or asymptotic-convergence proof audit was performed.
- PSO1995 was read through OCR with critical equation verification; PSO1999 was read
  directly through page images. Some companion-source opens failed, and unresolved
  variants remain discovery leads.
- Three additions and a nonempty inherited/new frontier leave discovery active.
tags:
- native-concepts
- stochastic-optimization
- particle-swarm
- simulated-annealing
- cross-entropy-method
- source-conventions
- self-review
- discovery-ongoing
```
